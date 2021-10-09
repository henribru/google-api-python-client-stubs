import typing

import typing_extensions

_list = list

@typing.type_check_only
class AptArtifact(typing_extensions.TypedDict, total=False):
    architecture: str
    component: str
    controlFile: str
    name: str
    packageName: str
    packageType: typing_extensions.Literal[
        "PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"
    ]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DockerImage(typing_extensions.TypedDict, total=False):
    buildTime: str
    imageSizeBytes: str
    mediaType: str
    name: str
    tags: _list[str]
    uploadTime: str
    uri: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportAptArtifactsErrorInfo(typing_extensions.TypedDict, total=False):
    error: Status
    gcsSource: ImportAptArtifactsGcsSource

@typing.type_check_only
class ImportAptArtifactsGcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportAptArtifactsResponse(typing_extensions.TypedDict, total=False):
    aptArtifacts: _list[AptArtifact]
    errors: _list[ImportAptArtifactsErrorInfo]

@typing.type_check_only
class ImportYumArtifactsErrorInfo(typing_extensions.TypedDict, total=False):
    error: Status
    gcsSource: ImportYumArtifactsGcsSource

@typing.type_check_only
class ImportYumArtifactsGcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportYumArtifactsResponse(typing_extensions.TypedDict, total=False):
    errors: _list[ImportYumArtifactsErrorInfo]
    yumArtifacts: _list[YumArtifact]

@typing.type_check_only
class ListDockerImagesResponse(typing_extensions.TypedDict, total=False):
    dockerImages: _list[DockerImage]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListRepositoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Repository(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED", "DOCKER", "MAVEN", "NPM", "APT", "YUM", "PYTHON"
    ]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UploadAptArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadAptArtifactResponse(typing_extensions.TypedDict, total=False):
    aptArtifacts: _list[AptArtifact]

@typing.type_check_only
class UploadYumArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadYumArtifactResponse(typing_extensions.TypedDict, total=False):
    yumArtifacts: _list[YumArtifact]

@typing.type_check_only
class YumArtifact(typing_extensions.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str
    packageType: typing_extensions.Literal[
        "PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"
    ]
