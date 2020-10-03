import typing

import typing_extensions

class RestMethod(typing_extensions.TypedDict, total=False):
    id: str
    parameterOrder: typing.List[str]
    description: str
    etagRequired: bool
    httpMethod: str
    mediaUpload: typing.Dict[str, typing.Any]
    supportsMediaDownload: bool
    path: str
    request: typing.Dict[str, typing.Any]
    supportsMediaUpload: bool
    response: typing.Dict[str, typing.Any]
    supportsSubscription: bool
    useMediaDownloadService: bool
    parameters: typing.Dict[str, typing.Any]
    scopes: typing.List[str]

class RestResource(typing_extensions.TypedDict, total=False):
    resources: typing.Dict[str, typing.Any]
    methods: typing.Dict[str, typing.Any]

class RestDescription(typing_extensions.TypedDict, total=False):
    id: str
    version_module: bool
    features: typing.List[str]
    labels: typing.List[str]
    ownerName: str
    revision: str
    batchPath: str
    description: str
    auth: typing.Dict[str, typing.Any]
    version: str
    discoveryVersion: str
    name: str
    methods: typing.Dict[str, typing.Any]
    icons: typing.Dict[str, typing.Any]
    packagePath: str
    basePath: str
    resources: typing.Dict[str, typing.Any]
    exponentialBackoffDefault: bool
    kind: str
    parameters: typing.Dict[str, typing.Any]
    etag: str
    servicePath: str
    canonicalName: str
    schemas: typing.Dict[str, typing.Any]
    protocol: str
    documentationLink: str
    rootUrl: str
    baseUrl: str
    ownerDomain: str
    title: str

class JsonSchema(typing.Dict[str, typing.Any]): ...

class DirectoryList(typing_extensions.TypedDict, total=False):
    discoveryVersion: str
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str
