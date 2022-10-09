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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1beta2File(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    hashes: _list[Hash]
    name: str
    owner: str
    sizeBytes: str
    updateTime: str

@typing.type_check_only
class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["HASH_TYPE_UNSPECIFIED", "SHA256", "MD5"]
    value: str

@typing.type_check_only
class ImportAptArtifactsErrorInfo(typing_extensions.TypedDict, total=False):
    error: Status
    gcsSource: ImportAptArtifactsGcsSource

@typing.type_check_only
class ImportAptArtifactsGcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportAptArtifactsMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportAptArtifactsRequest(typing_extensions.TypedDict, total=False):
    gcsSource: ImportAptArtifactsGcsSource

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
class ImportYumArtifactsMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportYumArtifactsRequest(typing_extensions.TypedDict, total=False):
    gcsSource: ImportYumArtifactsGcsSource

@typing.type_check_only
class ImportYumArtifactsResponse(typing_extensions.TypedDict, total=False):
    errors: _list[ImportYumArtifactsErrorInfo]
    yumArtifacts: _list[YumArtifact]

@typing.type_check_only
class ListFilesResponse(typing_extensions.TypedDict, total=False):
    files: _list[GoogleDevtoolsArtifactregistryV1beta2File]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListPackagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    packages: _list[Package]

@typing.type_check_only
class ListRepositoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class ListTagsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tags: _list[Tag]

@typing.type_check_only
class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MavenRepositoryConfig(typing_extensions.TypedDict, total=False):
    allowSnapshotOverwrites: bool
    versionPolicy: typing_extensions.Literal[
        "VERSION_POLICY_UNSPECIFIED", "RELEASE", "SNAPSHOT"
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectSettings(typing_extensions.TypedDict, total=False):
    legacyRedirectionState: typing_extensions.Literal[
        "REDIRECTION_STATE_UNSPECIFIED",
        "REDIRECTION_FROM_GCR_IO_DISABLED",
        "REDIRECTION_FROM_GCR_IO_ENABLED",
        "REDIRECTION_FROM_GCR_IO_FINALIZED",
    ]
    name: str

@typing.type_check_only
class Repository(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED", "DOCKER", "MAVEN", "NPM", "APT", "YUM", "PYTHON"
    ]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    mavenConfig: MavenRepositoryConfig
    name: str
    sizeBytes: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tag(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UploadAptArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadAptArtifactMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadAptArtifactRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadAptArtifactResponse(typing_extensions.TypedDict, total=False):
    aptArtifacts: _list[AptArtifact]

@typing.type_check_only
class UploadYumArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadYumArtifactMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadYumArtifactRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadYumArtifactResponse(typing_extensions.TypedDict, total=False):
    yumArtifacts: _list[YumArtifact]

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    metadata: dict[str, typing.Any]
    name: str
    relatedTags: _list[Tag]
    updateTime: str

@typing.type_check_only
class YumArtifact(typing_extensions.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str
    packageType: typing_extensions.Literal[
        "PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"
    ]
