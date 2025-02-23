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
class AptRepository(typing_extensions.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository
    publicRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    attachmentNamespace: str
    createTime: str
    files: _list[str]
    name: str
    ociVersionName: str
    target: str
    type: str
    updateTime: str

@typing.type_check_only
class BatchDeleteVersionsMetadata(typing_extensions.TypedDict, total=False):
    failedVersions: _list[str]

@typing.type_check_only
class BatchDeleteVersionsRequest(typing_extensions.TypedDict, total=False):
    names: _list[str]
    validateOnly: bool

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CleanupPolicy(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "DELETE", "KEEP"]
    condition: CleanupPolicyCondition
    id: str
    mostRecentVersions: CleanupPolicyMostRecentVersions

@typing.type_check_only
class CleanupPolicyCondition(typing_extensions.TypedDict, total=False):
    newerThan: str
    olderThan: str
    packageNamePrefixes: _list[str]
    tagPrefixes: _list[str]
    tagState: typing_extensions.Literal[
        "TAG_STATE_UNSPECIFIED", "TAGGED", "UNTAGGED", "ANY"
    ]
    versionNamePrefixes: _list[str]

@typing.type_check_only
class CleanupPolicyMostRecentVersions(typing_extensions.TypedDict, total=False):
    keepCount: int
    packageNamePrefixes: _list[str]

@typing.type_check_only
class CommonRemoteRepository(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class DockerImage(typing_extensions.TypedDict, total=False):
    buildTime: str
    imageSizeBytes: str
    mediaType: str
    name: str
    tags: _list[str]
    updateTime: str
    uploadTime: str
    uri: str

@typing.type_check_only
class DockerRepository(typing_extensions.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository
    publicRepository: typing_extensions.Literal[
        "PUBLIC_REPOSITORY_UNSPECIFIED", "DOCKER_HUB"
    ]

@typing.type_check_only
class DockerRepositoryConfig(typing_extensions.TypedDict, total=False):
    immutableTags: bool

@typing.type_check_only
class DownloadFileResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GenericArtifact(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    version: str

@typing.type_check_only
class GoModule(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    version: str

@typing.type_check_only
class GoogetArtifact(typing_extensions.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1File(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    fetchTime: str
    hashes: _list[Hash]
    name: str
    owner: str
    sizeBytes: str
    updateTime: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository(
    typing_extensions.TypedDict, total=False
):
    repositoryBase: typing_extensions.Literal[
        "REPOSITORY_BASE_UNSPECIFIED", "DEBIAN", "UBUNTU", "DEBIAN_SNAPSHOT"
    ]
    repositoryPath: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository(
    typing_extensions.TypedDict, total=False
):
    repositoryBase: typing_extensions.Literal[
        "REPOSITORY_BASE_UNSPECIFIED",
        "CENTOS",
        "CENTOS_DEBUG",
        "CENTOS_VAULT",
        "CENTOS_STREAM",
        "ROCKY",
        "EPEL",
    ]
    repositoryPath: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1Rule(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    condition: Expr
    name: str
    operation: typing_extensions.Literal["OPERATION_UNSPECIFIED", "DOWNLOAD"]
    packageId: str

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
class ImportGoogetArtifactsErrorInfo(typing_extensions.TypedDict, total=False):
    error: Status
    gcsSource: ImportGoogetArtifactsGcsSource

@typing.type_check_only
class ImportGoogetArtifactsGcsSource(typing_extensions.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportGoogetArtifactsMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportGoogetArtifactsRequest(typing_extensions.TypedDict, total=False):
    gcsSource: ImportGoogetArtifactsGcsSource

@typing.type_check_only
class ImportGoogetArtifactsResponse(typing_extensions.TypedDict, total=False):
    errors: _list[ImportGoogetArtifactsErrorInfo]
    googetArtifacts: _list[GoogetArtifact]

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
class KfpArtifact(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ListAttachmentsResponse(typing_extensions.TypedDict, total=False):
    attachments: _list[Attachment]
    nextPageToken: str

@typing.type_check_only
class ListDockerImagesResponse(typing_extensions.TypedDict, total=False):
    dockerImages: _list[DockerImage]
    nextPageToken: str

@typing.type_check_only
class ListFilesResponse(typing_extensions.TypedDict, total=False):
    files: _list[GoogleDevtoolsArtifactregistryV1File]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMavenArtifactsResponse(typing_extensions.TypedDict, total=False):
    mavenArtifacts: _list[MavenArtifact]
    nextPageToken: str

@typing.type_check_only
class ListNpmPackagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    npmPackages: _list[NpmPackage]

@typing.type_check_only
class ListPackagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    packages: _list[Package]

@typing.type_check_only
class ListPythonPackagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    pythonPackages: _list[PythonPackage]

@typing.type_check_only
class ListRepositoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class ListRulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rules: _list[GoogleDevtoolsArtifactregistryV1Rule]

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
class MavenArtifact(typing_extensions.TypedDict, total=False):
    artifactId: str
    createTime: str
    groupId: str
    name: str
    pomUri: str
    updateTime: str
    version: str

@typing.type_check_only
class MavenRepository(typing_extensions.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository
    publicRepository: typing_extensions.Literal[
        "PUBLIC_REPOSITORY_UNSPECIFIED", "MAVEN_CENTRAL"
    ]

@typing.type_check_only
class MavenRepositoryConfig(typing_extensions.TypedDict, total=False):
    allowSnapshotOverwrites: bool
    versionPolicy: typing_extensions.Literal[
        "VERSION_POLICY_UNSPECIFIED", "RELEASE", "SNAPSHOT"
    ]

@typing.type_check_only
class NpmPackage(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    packageName: str
    tags: _list[str]
    updateTime: str
    version: str

@typing.type_check_only
class NpmRepository(typing_extensions.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository
    publicRepository: typing_extensions.Literal[
        "PUBLIC_REPOSITORY_UNSPECIFIED", "NPMJS"
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
    annotations: dict[str, typing.Any]
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
        "REDIRECTION_FROM_GCR_IO_ENABLED_AND_COPYING",
        "REDIRECTION_FROM_GCR_IO_PARTIAL_AND_COPYING",
    ]
    name: str
    pullPercent: int

@typing.type_check_only
class PythonPackage(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    packageName: str
    updateTime: str
    uri: str
    version: str

@typing.type_check_only
class PythonRepository(typing_extensions.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository
    publicRepository: typing_extensions.Literal["PUBLIC_REPOSITORY_UNSPECIFIED", "PYPI"]

@typing.type_check_only
class RemoteRepositoryConfig(typing_extensions.TypedDict, total=False):
    aptRepository: AptRepository
    commonRepository: CommonRemoteRepository
    description: str
    disableUpstreamValidation: bool
    dockerRepository: DockerRepository
    mavenRepository: MavenRepository
    npmRepository: NpmRepository
    pythonRepository: PythonRepository
    upstreamCredentials: UpstreamCredentials
    yumRepository: YumRepository

@typing.type_check_only
class Repository(typing_extensions.TypedDict, total=False):
    cleanupPolicies: dict[str, typing.Any]
    cleanupPolicyDryRun: bool
    createTime: str
    description: str
    disallowUnspecifiedMode: bool
    dockerConfig: DockerRepositoryConfig
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED",
        "DOCKER",
        "MAVEN",
        "NPM",
        "APT",
        "YUM",
        "GOOGET",
        "PYTHON",
        "KFP",
        "GO",
        "GENERIC",
    ]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    mavenConfig: MavenRepositoryConfig
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED",
        "STANDARD_REPOSITORY",
        "VIRTUAL_REPOSITORY",
        "REMOTE_REPOSITORY",
        "AOSS_REPOSITORY",
        "ASSURED_OSS_REPOSITORY",
    ]
    name: str
    registryUri: str
    remoteRepositoryConfig: RemoteRepositoryConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    sizeBytes: str
    updateTime: str
    virtualRepositoryConfig: VirtualRepositoryConfig
    vulnerabilityScanningConfig: VulnerabilityScanningConfig

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
class UploadFileMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadFileRequest(typing_extensions.TypedDict, total=False):
    fileId: str

@typing.type_check_only
class UploadGenericArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadGenericArtifactMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadGenericArtifactRequest(typing_extensions.TypedDict, total=False):
    filename: str
    packageId: str
    versionId: str

@typing.type_check_only
class UploadGoModuleMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadGoModuleMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoModuleRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoogetArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadGoogetArtifactMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoogetArtifactRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoogetArtifactResponse(typing_extensions.TypedDict, total=False):
    googetArtifacts: _list[GoogetArtifact]

@typing.type_check_only
class UploadKfpArtifactMediaResponse(typing_extensions.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadKfpArtifactMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadKfpArtifactRequest(typing_extensions.TypedDict, total=False):
    description: str
    tags: _list[str]

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
class UpstreamCredentials(typing_extensions.TypedDict, total=False):
    usernamePasswordCredentials: UsernamePasswordCredentials

@typing.type_check_only
class UpstreamPolicy(typing_extensions.TypedDict, total=False):
    id: str
    priority: int
    repository: str

@typing.type_check_only
class UsernamePasswordCredentials(typing_extensions.TypedDict, total=False):
    passwordSecretVersion: str
    username: str

@typing.type_check_only
class VPCSCConfig(typing_extensions.TypedDict, total=False):
    name: str
    vpcscPolicy: typing_extensions.Literal["VPCSC_POLICY_UNSPECIFIED", "DENY", "ALLOW"]

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    description: str
    metadata: dict[str, typing.Any]
    name: str
    relatedTags: _list[Tag]
    updateTime: str

@typing.type_check_only
class VirtualRepositoryConfig(typing_extensions.TypedDict, total=False):
    upstreamPolicies: _list[UpstreamPolicy]

@typing.type_check_only
class VulnerabilityScanningConfig(typing_extensions.TypedDict, total=False):
    enablementConfig: typing_extensions.Literal[
        "ENABLEMENT_CONFIG_UNSPECIFIED", "INHERITED", "DISABLED"
    ]
    enablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED",
        "SCANNING_UNSUPPORTED",
        "SCANNING_DISABLED",
        "SCANNING_ACTIVE",
    ]
    enablementStateReason: str
    lastEnableTime: str

@typing.type_check_only
class YumArtifact(typing_extensions.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str
    packageType: typing_extensions.Literal[
        "PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"
    ]

@typing.type_check_only
class YumRepository(typing_extensions.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository
    publicRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository
