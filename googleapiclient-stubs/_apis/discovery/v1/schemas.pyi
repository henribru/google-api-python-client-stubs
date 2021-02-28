import typing

import typing_extensions
@typing.type_check_only
class DirectoryList(typing_extensions.TypedDict, total=False):
    discoveryVersion: str
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

AlternativeJsonSchema = typing_extensions.TypedDict(
    "AlternativeJsonSchema",
    {
        "$ref": str,
        "additionalProperties": JsonSchema,
        "annotations": typing.Dict[str, typing.Any],
        "default": str,
        "description": str,
        "enum": typing.List[str],
        "enumDescriptions": typing.List[str],
        "format": str,
        "id": str,
        "items": JsonSchema,
        "location": str,
        "maximum": str,
        "minimum": str,
        "pattern": str,
        "properties": typing.Dict[str, typing.Any],
        "readOnly": bool,
        "repeated": bool,
        "required": bool,
        "type": str,
        "variant": typing.Dict[str, typing.Any],
    },
    total=False,
)
@typing.type_check_only
class JsonSchema(AlternativeJsonSchema): ...

@typing.type_check_only
class RestDescription(typing_extensions.TypedDict, total=False):
    auth: typing.Dict[str, typing.Any]
    basePath: str
    baseUrl: str
    batchPath: str
    canonicalName: str
    description: str
    discoveryVersion: str
    documentationLink: str
    etag: str
    exponentialBackoffDefault: bool
    features: typing.List[str]
    icons: typing.Dict[str, typing.Any]
    id: str
    kind: str
    labels: typing.List[str]
    methods: typing.Dict[str, typing.Any]
    name: str
    ownerDomain: str
    ownerName: str
    packagePath: str
    parameters: typing.Dict[str, typing.Any]
    protocol: str
    resources: typing.Dict[str, typing.Any]
    revision: str
    rootUrl: str
    schemas: typing.Dict[str, typing.Any]
    servicePath: str
    title: str
    version: str
    version_module: bool

@typing.type_check_only
class RestMethod(typing_extensions.TypedDict, total=False):
    description: str
    etagRequired: bool
    httpMethod: str
    id: str
    mediaUpload: typing.Dict[str, typing.Any]
    parameterOrder: typing.List[str]
    parameters: typing.Dict[str, typing.Any]
    path: str
    request: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    scopes: typing.List[str]
    supportsMediaDownload: bool
    supportsMediaUpload: bool
    supportsSubscription: bool
    useMediaDownloadService: bool

@typing.type_check_only
class RestResource(typing_extensions.TypedDict, total=False):
    methods: typing.Dict[str, typing.Any]
    resources: typing.Dict[str, typing.Any]
