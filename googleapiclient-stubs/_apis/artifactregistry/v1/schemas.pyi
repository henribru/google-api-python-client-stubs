import typing

import typing_extensions

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
    tags: typing.List[str]
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
    uris: typing.List[str]
    useWildcards: bool

@typing.type_check_only
class ImportAptArtifactsResponse(typing_extensions.TypedDict, total=False):
    aptArtifacts: typing.List[AptArtifact]
    errors: typing.List[ImportAptArtifactsErrorInfo]

@typing.type_check_only
class ImportYumArtifactsErrorInfo(typing_extensions.TypedDict, total=False):
    error: Status
    gcsSource: ImportYumArtifactsGcsSource

@typing.type_check_only
class ImportYumArtifactsGcsSource(typing_extensions.TypedDict, total=False):
    uris: typing.List[str]
    useWildcards: bool

@typing.type_check_only
class ImportYumArtifactsResponse(typing_extensions.TypedDict, total=False):
    errors: typing.List[ImportYumArtifactsErrorInfo]
    yumArtifacts: typing.List[YumArtifact]

@typing.type_check_only
class ListDockerImagesResponse(typing_extensions.TypedDict, total=False):
    dockerImages: typing.List[DockerImage]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListRepositoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repositories: typing.List[Repository]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Repository(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED", "DOCKER", "MAVEN", "NPM", "APT", "YUM", "PYTHON"
    ]
    kmsKeyName: str
    labels: typing.Dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UploadAptArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadAptArtifactResponse(typing_extensions.TypedDict, total=False):
    aptArtifacts: typing.List[AptArtifact]

@typing.type_check_only
class UploadYumArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadYumArtifactResponse(typing_extensions.TypedDict, total=False):
    yumArtifacts: typing.List[YumArtifact]

@typing.type_check_only
class YumArtifact(typing_extensions.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str
    packageType: typing_extensions.Literal[
        "PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"
    ]
