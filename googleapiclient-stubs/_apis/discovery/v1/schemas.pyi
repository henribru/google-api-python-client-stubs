import typing

import typing_extensions
@typing.type_check_only
class DirectoryList(typing_extensions.TypedDict, total=False):
    discoveryVersion: str
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class JsonSchema(typing.Dict[str, typing.Any]): ...

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
