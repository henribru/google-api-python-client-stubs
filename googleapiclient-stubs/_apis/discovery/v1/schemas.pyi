import typing

import typing_extensions

_list = list

@typing.type_check_only
class DirectoryList(typing_extensions.TypedDict, total=False):
    discoveryVersion: str
    items: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class JsonSchema(dict[str, typing.Any]): ...

@typing.type_check_only
class RestDescription(typing_extensions.TypedDict, total=False):
    auth: dict[str, typing.Any]
    basePath: str
    baseUrl: str
    batchPath: str
    canonicalName: str
    description: str
    discoveryVersion: str
    documentationLink: str
    etag: str
    exponentialBackoffDefault: bool
    features: _list[str]
    icons: dict[str, typing.Any]
    id: str
    kind: str
    labels: _list[str]
    methods: dict[str, typing.Any]
    name: str
    ownerDomain: str
    ownerName: str
    packagePath: str
    parameters: dict[str, typing.Any]
    protocol: str
    resources: dict[str, typing.Any]
    revision: str
    rootUrl: str
    schemas: dict[str, typing.Any]
    servicePath: str
    title: str
    version: str
    version_module: bool

@typing.type_check_only
class RestMethod(typing_extensions.TypedDict, total=False):
    description: str
    etagRequired: bool
    flatPath: str
    httpMethod: str
    id: str
    mediaUpload: dict[str, typing.Any]
    parameterOrder: _list[str]
    parameters: dict[str, typing.Any]
    path: str
    request: dict[str, typing.Any]
    response: dict[str, typing.Any]
    scopes: _list[str]
    supportsMediaDownload: bool
    supportsMediaUpload: bool
    supportsSubscription: bool
    useMediaDownloadService: bool

@typing.type_check_only
class RestResource(typing_extensions.TypedDict, total=False):
    methods: dict[str, typing.Any]
    resources: dict[str, typing.Any]
