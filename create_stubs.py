#!/usr/bin/env python3
import json
import keyword
import os
import shutil
import subprocess
import textwrap
from contextlib import contextmanager
from pathlib import Path
from typing import Any, DefaultDict, Dict, List, Set

from googleapiclient.discovery import fix_method_name, key2param


def type_to_python_type(type: str):
    return {
        "integer": "int",
        "string": "str",
        "number": "float",
        "boolean": "bool",
        "array": "_list",
        "object": "dict[str, typing.Any]",
        "any": "typing.Any",
    }[type]


def get_type(property: Dict[str, Any]):
    type = property.get("type")
    if type is None:
        type = property["$ref"]
    else:
        # FIXME: Maps with some known keys? Not sure.
        # if type == "object":
        # assert not property.get("properties")
        if property.get("description") != "The request body.":
            assert not property.get("$ref")
        type = type_to_python_type(type)
        if "items" in property:
            assert type == "_list"
            type = f"_list[{get_type(property['items'])}]"
        if "enum" in property:
            assert type == "str"
            quoted_enum_members = [
                f'"{enum_member}"' for enum_member in property["enum"]
            ]
            type = f"typing_extensions.Literal[{', '.join(quoted_enum_members)}]"
    return type


def is_valid_identifier(identifier: str) -> bool:
    return identifier.isidentifier() and not keyword.iskeyword(identifier)


class Writer:
    def __init__(self, file):
        self.file = file
        self.lines = []
        self._indent_level = 0

    @contextmanager
    def indent(self):
        self._indent_level += 1
        yield
        self._indent_level -= 1

    def write(self, s: str = "", end="\n", indent=True, prepend=False):
        if not isinstance(s, str):
            s = str(s)
        if indent:
            s = textwrap.indent(s, " " * self._indent_level * 4)
        if prepend:
            self.lines.insert(0, s + end)
        else:
            self.lines.append(s + end)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        if exc_type is None:
            self.file.writelines(self.lines)


def write_typed_dict(writer, typed_dict_description):
    writer.write("@typing.type_check_only")
    writer.write(
        f"class {typed_dict_description['name']}(typing_extensions.TypedDict, total=False):"
    )
    properties = typed_dict_description["properties"]
    sorted_property_names = sorted(properties)
    with writer.indent():
        for property_name in sorted_property_names:
            type = properties[property_name]
            writer.write(f"{property_name}: {type}")
    if not typed_dict_description["properties"]:
        with writer.indent():
            writer.write("...")


def write_alternative_typed_dict(writer, typed_dict_description):
    name = typed_dict_description["name"]
    writer.write(
        f"Alternative{name} = typing_extensions.TypedDict('Alternative{name}', {{"
    )
    properties = typed_dict_description["properties"]
    sorted_property_names = sorted(properties)
    with writer.indent():
        for property_name in sorted_property_names:
            type = properties[property_name]
            writer.write(f'"{property_name}": {type},')
    writer.write("}, total=False)")
    writer.write("@typing.type_check_only")
    writer.write(f"class {name}(Alternative{name}): ...")


def capitalize(s: str) -> str:
    return s[0].upper() + s[1:]


def write_schemas(writer, schemas):
    writer.write("import typing")
    writer.write("import typing_extensions")
    writer.write("_list = list")
    sorted_schema_names = sorted(schemas)
    for schema_name in sorted_schema_names:
        schema = schemas[schema_name]
        typed_dict_description = {"name": schema_name, "properties": {}}
        properties = schema.get("properties", {})
        for property_name, property in properties.items():
            type = get_type(property)
            typed_dict_description["properties"][property_name] = type
        if "properties" not in schema:
            writer.write("@typing.type_check_only")
            writer.write(f"class {schema_name}(dict[str, typing.Any]): ...")
        elif all(
            is_valid_identifier(identifier) for identifier in schema["properties"]
        ):
            write_typed_dict(writer, typed_dict_description)
        else:
            write_alternative_typed_dict(writer, typed_dict_description)


def fix_resource_name(resource_name) -> str:
    resource_name = resource_name.replace("&", " and ")
    for sep in ["-", " "]:
        resource_name = "".join(capitalize(part) for part in resource_name.split(sep))
    return resource_name


def write_resource(writer, resource_name, resource, api, top_level=True) -> Set[str]:
    if top_level:
        writer.write("import googleapiclient.discovery")
        writer.write("import googleapiclient.http")
        writer.write("from .schemas import *")
        writer.write("import httplib2")
        writer.write("import typing")
        writer.write("import typing_extensions")
        writer.write("import collections.abc")
        writer.write("_list = list")
    response_types = set()
    writer.write("@typing.type_check_only")
    writer.write(
        f"class {capitalize(resource_name)}Resource(googleapiclient.discovery.Resource):"
    )
    sub_resources = resource.get("resources", {})
    sorted_sub_resource_names = sorted(sub_resources)
    with writer.indent():
        for sub_resource_name in sorted_sub_resource_names:
            sub_resource = sub_resources[sub_resource_name]
            response_types |= write_resource(
                writer,
                fix_resource_name(sub_resource_name),
                sub_resource,
                api,
                top_level=False,
            )

    sub_resource_method_names = {
        fix_method_name(sub_resource_name) for sub_resource_name in sub_resources
    }

    methods = resource.get("methods", {})
    sorted_method_names = sorted(methods)
    with writer.indent():
        for method_name in sorted_method_names:
            if fix_method_name(method_name) in sub_resource_method_names:
                continue
            method = methods[method_name]
            from googleapiclient.schema import Schemas

            schema = Schemas(api)
            from googleapiclient.discovery import ResourceMethodParameters, createMethod

            # createMethod(method_name, method, api, schema)
            request = method.get("request")
            response = method.get("response")
            if response and "$ref" in response:
                response_type = response["$ref"]
                response_types.add(response_type)
            else:
                response_type = None
            parameters = {}
            required_parameters = []
            for parameter_name, parameter in method.get("parameters", {}).items():
                parameter_name = key2param(parameter_name)
                if keyword.iskeyword(parameter_name):
                    continue
                if parameter.get("required"):
                    required_parameters.append(parameter_name)
                type = get_type(parameter)
                if parameter.get("repeated"):
                    assert "_list[" not in type and type != "_list"
                    type = f"{type} | _list[{type}]"
                parameters[parameter_name] = type
            ordered_parameters = [
                key2param(param) for param in method.get("parameterOrder", [])
            ]
            if request:
                ordered_parameters.append("body")
                parameters["body"] = (
                    request["$ref"]
                    if "$ref" in request
                    else type_to_python_type(request["type"])
                )
            sorted_parameter_names = sorted(parameters)
            for parameter_name in sorted_parameter_names:
                if parameter_name not in ordered_parameters:
                    ordered_parameters.append(parameter_name)
            ordered_parameters.append("**kwargs")
            required_parameters.append("**kwargs")
            parameters["**kwargs"] = "typing.Any"

            # parameters_ = ResourceMethodParameters(method)
            # for parameter in ordered_parameters:
            #     assert parameter in parameters_.argmap
            # FIXME: Some parameters are reserved words. Type with Unpack and TypedDict?
            # for parameter in parameters_.argmap:
            # if parameter not in ordered_parameters:
            #     print("--", parameter, ordered_parameters, parameters, required_parameters, method, parameters_, keyword.iskeyword(parameter), sep="\n")
            #     raise ValueError()

            def format_parameter(parameter_name):
                formatted_parameter = f"{parameter_name}: {parameters[parameter_name]}"
                if parameter_name not in required_parameters:
                    formatted_parameter += " = ..."
                return formatted_parameter

            formatted_parameters = [
                format_parameter(parameter_name)
                for parameter_name in ordered_parameters
            ]
            if response_type:
                return_type = f"{response_type}HttpRequest"
            else:
                # TODO: HttpRequest subclass for empty responses
                return_type = "googleapiclient.http.HttpRequest"
            writer.write(
                f"def {fix_method_name(method_name)}({'  # type: ignore[override]' if fix_method_name(method_name) == 'close' else ''}"
            )
            writer.write(
                f"self, {'*, ' if len(formatted_parameters) > 1 else ''}{', '.join(formatted_parameters)}) -> {return_type}: ..."
            )

            if method.get("supportsMediaDownload", False):
                response_types.add("bytes")
                writer.write(
                    f"def {fix_method_name(method_name)}_media({'  # type: ignore[override]' if fix_method_name(method_name) == 'close' else ''}"
                )
                writer.write(
                    f"self, {'*, ' if len(formatted_parameters) > 1 else ''}{', '.join(formatted_parameters)}) -> BytesHttpRequest: ..."
                )

            from googleapiclient.discovery import _findPageTokenName, _methodProperties

            nextPageTokenName = _findPageTokenName(
                _methodProperties(method, api["schemas"], "response")
            )
            if not nextPageTokenName:
                continue
            pageTokenName = _findPageTokenName(method.get("parameters", {}))
            if not pageTokenName:
                pageTokenName = _findPageTokenName(
                    _methodProperties(method, api["schemas"], "request")
                )
            if not pageTokenName:
                continue

            writer.write(
                f"def {fix_method_name(method_name)}_next(self, previous_request: {return_type}, previous_response: {response_type}) -> {return_type} | None: ..."
            )

    with writer.indent():
        if top_level:
            writer.write(
                f"def new_batch_http_request(self, callback: collections.abc.Callable[[str, googleapiclient.http.HttpRequest, googleapiclient.errors.HttpError | None], typing.Any] | None = None) -> googleapiclient.http.BatchHttpRequest: ..."
            )

        for sub_resource_name in sorted_sub_resource_names:
            writer.write(
                f"def {fix_method_name(sub_resource_name)}(self) -> {fix_resource_name(sub_resource_name)}Resource: ..."
            )

    if not (methods or sub_resources or top_level):
        with writer.indent():
            writer.write("...")

    return response_types


def write_build_overload(writer, service_name: str, version: str, resource_name: str):
    resource_path = (
        f"googleapiclient._apis.{service_name}.{'_'.join(version.split('.'))}"
    )
    writer.write(f"import {resource_path}", prepend=True)
    write_build(
        writer,
        f'Literal["{service_name}"]',
        f'Literal["{version}"]',
        f"{resource_path}.{resource_name}Resource",
    )


def write_build(
    writer,
    service_name_type: str = "str",
    version_type: str = "str",
    return_type: str = "Resource",
):
    writer.write("@overload")
    writer.write(
        f"""def build(
        serviceName: {service_name_type},
        version: {version_type},
        http: httplib2.Http | HttpMock | None = None,
        discoveryServiceUrl: str | None = None,
        developerKey: str | None = None,
        model: Model | None = None,
        requestBuilder: _RequestBuilder = HttpRequest,
        credentials: oauth2client.Credentials | google.auth.credentials.Credentials | None = None,
        cache_discovery: bool = True,
        cache: Cache | None = None,
        client_options: dict[str, Any] | ClientOptions | None = None,
        adc_cert_path: str | None = None,
        adc_key_path: str | None = None,
        num_retries: int = 1,
        static_discovery: bool | None = None,
    ) -> {return_type}: ..."""
    )


def type_schemas(api, directory):
    print(f"Writing schemas for {api['id']}")
    schemas = api["schemas"]
    with open(directory / "schemas.pyi", "w", encoding="utf-8") as f:
        with Writer(f) as writer:
            write_schemas(writer, schemas)


def type_resources(api, directory):
    print(f"Writing resources for {api['id']}")

    with open(directory / "resources.pyi", "w", encoding="utf-8") as f:
        with Writer(f) as writer:
            resource_name = fix_resource_name(api.get("canonicalName", api["name"]))
            sorted_response_types = sorted(
                write_resource(writer, resource_name, api, api)
            )
            for response_type in sorted_response_types:
                writer.write("@typing.type_check_only")
                writer.write(
                    f"class {'Bytes' if response_type == 'bytes' else response_type}HttpRequest(googleapiclient.http.HttpRequest):"
                )
                with writer.indent():
                    writer.write(
                        f"def execute(self, http: httplib2.Http | googleapiclient.http.HttpMock | None = None, num_retries: int = 0) -> {response_type}: ..."
                    )


def copytree(src, dst, symlinks=False, ignore=None, overwrite=True):
    """Rough reimplementation of shutil.copytree with support for
    existing directories and not overwriting existing files."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore, overwrite)
        else:
            if not os.path.exists(d) or (
                overwrite and os.stat(s).st_mtime - os.stat(d).st_mtime > 1
            ):
                shutil.copy2(s, d)


def main():
    subprocess.run(["uv", "remove", "google-api-python-client"])
    subprocess.run(["uv", "add", "google-api-python-client"])
    subprocess.run(["git", "clone", "https://github.com/googleapis/google-api-python-client.git"]);
    subprocess.run(["git", "restore", "."], cwd="google-api-python-client")
    subprocess.run(["git", "pull"], cwd="google-api-python-client")
    shutil.rmtree("apiclient-stubs", ignore_errors=True)
    apis = []
    ignored_apis = [
        "admin.datatransferv1.json",
        "admin.directoryv1.json",
        "admin.reportsv1.json",
        "content.v21.json",
    ]
    for path in sorted(
        Path("google-api-python-client/googleapiclient/discovery_cache/documents").glob(
            "*.json"
        )
    ):
        if (
            path.name != "index.json"
            and not path.is_symlink()
            and path.name not in ignored_apis
        ):
            with open(path, encoding="utf-8") as f:
                apis.append(json.load(f))
    api_by_directory = {}
    for api in apis:
        directory = Path(
            "googleapiclient-stubs",
            "_apis",
            api["name"],
            "_".join(api["version"].split(".")),
        )
        directory.mkdir(parents=True, exist_ok=True)
        api_by_directory[directory] = api
        type_schemas(api, directory)
        type_resources(api, directory)
        with open(directory / "__init__.pyi", "w", encoding="utf-8") as f:
            f.write("from .resources import *\n")
            f.write("from .schemas import *\n")

    print("Stubbing")
    subprocess.run(
        ["stubgen", "googleapiclient", "-o", ".."], cwd="google-api-python-client"
    )
    for package in ["googleapiclient"]:
        stubs_package = f"{package}-stubs"
        copytree(package, stubs_package, overwrite=False)
        shutil.rmtree(package)
        for dir, _, _ in os.walk(stubs_package):
            Path(dir, "__init__.pyi").touch()

    print("Writing build overloads")
    with open("discovery.pyi", encoding="utf-8") as in_file, open(
        Path("googleapiclient-stubs", "discovery.pyi"), "w", encoding="utf-8"
    ) as out_file:
        with Writer(out_file) as writer:
            for line in in_file:
                writer.write(line)
            for api in apis:
                resource_name = fix_resource_name(
                    capitalize(api.get("canonicalName", api["name"]))
                )
                write_build_overload(writer, api["name"], api["version"], resource_name)
            write_build(writer)

    Path("googleapiclient").mkdir()
    Path("googleapiclient-stubs/_apis").rename("_apis")
    Path("googleapiclient-stubs").rename("googleapiclient/googleapiclient")
    subprocess.run(["stubdefaulter", "-p", "googleapiclient"])
    Path("googleapiclient/googleapiclient").rename("googleapiclient-stubs")
    Path("_apis").rename("googleapiclient-stubs/_apis")
    Path("googleapiclient").rmdir()

    print("Formatting")
    Path(".gitignore").rename("gitignore")
    subprocess.run(
        ["ruff", "check", "--fix", "--unsafe-fixes", "googleapiclient-stubs"]
    )
    subprocess.run(["ruff", "format", "googleapiclient-stubs"])
    Path("gitignore").rename(".gitignore")

    shutil.copytree(
        "googleapiclient-stubs",
        "apiclient-stubs",
        ignore=shutil.ignore_patterns(
            "__init__.pyi", "_auth.pyi", "_helpers.pyi", "discovery_cache", "_apis"
        ),
    )
    for path in Path("apiclient-stubs").glob("*.pyi"):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"from googleapiclient.{path.stem} import *\n")
    Path("apiclient-stubs/__init__.pyi").touch()


if __name__ == "__main__":
    main()
