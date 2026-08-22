import typing

_list = list

@typing.type_check_only
class AptArtifact(typing.TypedDict, total=False):
    architecture: str
    component: str
    controlFile: str
    name: str
    packageName: str
    packageType: typing.Literal["PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"]

@typing.type_check_only
class AptRepository(typing.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryCustomRepository
    publicRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository

@typing.type_check_only
class Attachment(typing.TypedDict, total=False):
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
class BatchDeleteVersionsMetadata(typing.TypedDict, total=False):
    failedVersions: _list[str]

@typing.type_check_only
class BatchDeleteVersionsRequest(typing.TypedDict, total=False):
    names: _list[str]
    validateOnly: bool

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckPrewarmedArtifactRequest(typing.TypedDict, total=False):
    streamLocation: str
    tag: str
    version: str

@typing.type_check_only
class CheckPrewarmedArtifactResponse(typing.TypedDict, total=False):
    prewarmedArtifact: PrewarmedArtifact

@typing.type_check_only
class CleanupPolicy(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "DELETE", "KEEP"]
    condition: CleanupPolicyCondition
    id: str
    mostRecentVersions: CleanupPolicyMostRecentVersions

@typing.type_check_only
class CleanupPolicyCondition(typing.TypedDict, total=False):
    newerThan: str
    olderThan: str
    packageNamePrefixes: _list[str]
    tagPrefixes: _list[str]
    tagState: typing.Literal["TAG_STATE_UNSPECIFIED", "TAGGED", "UNTAGGED", "ANY"]
    versionNamePrefixes: _list[str]

@typing.type_check_only
class CleanupPolicyMostRecentVersions(typing.TypedDict, total=False):
    keepCount: int
    packageNamePrefixes: _list[str]

@typing.type_check_only
class CommonRemoteRepository(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class DockerImage(typing.TypedDict, total=False):
    artifactType: str
    buildTime: str
    imageManifests: _list[ImageManifest]
    imageSizeBytes: str
    mediaType: str
    name: str
    tags: _list[str]
    updateTime: str
    uploadTime: str
    uri: str

@typing.type_check_only
class DockerRepository(typing.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository
    publicRepository: typing.Literal["PUBLIC_REPOSITORY_UNSPECIFIED", "DOCKER_HUB"]

@typing.type_check_only
class DockerRepositoryConfig(typing.TypedDict, total=False):
    immutableTags: bool

@typing.type_check_only
class DownloadFileResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportArtifactMetadata(typing.TypedDict, total=False):
    exportedFiles: _list[ExportedFile]

@typing.type_check_only
class ExportArtifactRequest(typing.TypedDict, total=False):
    gcsPath: str
    sourceTag: str
    sourceVersion: str

@typing.type_check_only
class ExportArtifactResponse(typing.TypedDict, total=False):
    exportedVersion: Version

@typing.type_check_only
class ExportedFile(typing.TypedDict, total=False):
    gcsObjectPath: str
    hashes: _list[Hash]
    name: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GenericArtifact(typing.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    version: str

@typing.type_check_only
class GoModule(typing.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    version: str

@typing.type_check_only
class GoogetArtifact(typing.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1File(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository(
    typing.TypedDict, total=False
):
    repositoryBase: typing.Literal[
        "REPOSITORY_BASE_UNSPECIFIED", "DEBIAN", "UBUNTU", "DEBIAN_SNAPSHOT"
    ]
    repositoryPath: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigDockerRepositoryCustomRepository(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository(
    typing.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository(
    typing.TypedDict, total=False
):
    repositoryBase: typing.Literal[
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
class GoogleDevtoolsArtifactregistryV1Rule(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    condition: Expr
    name: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "DOWNLOAD"]
    packageId: str

@typing.type_check_only
class Hash(typing.TypedDict, total=False):
    type: typing.Literal["HASH_TYPE_UNSPECIFIED", "SHA256", "MD5", "DIRSUM_SHA256"]
    value: str

@typing.type_check_only
class ImageManifest(typing.TypedDict, total=False):
    architecture: str
    digest: str
    mediaType: str
    os: str
    osFeatures: _list[str]
    osVersion: str
    variant: str

@typing.type_check_only
class ImportAptArtifactsErrorInfo(typing.TypedDict, total=False):
    error: Status
    gcsSource: ImportAptArtifactsGcsSource

@typing.type_check_only
class ImportAptArtifactsGcsSource(typing.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportAptArtifactsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class ImportAptArtifactsRequest(typing.TypedDict, total=False):
    gcsSource: ImportAptArtifactsGcsSource

@typing.type_check_only
class ImportAptArtifactsResponse(typing.TypedDict, total=False):
    aptArtifacts: _list[AptArtifact]
    errors: _list[ImportAptArtifactsErrorInfo]

@typing.type_check_only
class ImportGoogetArtifactsErrorInfo(typing.TypedDict, total=False):
    error: Status
    gcsSource: ImportGoogetArtifactsGcsSource

@typing.type_check_only
class ImportGoogetArtifactsGcsSource(typing.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportGoogetArtifactsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class ImportGoogetArtifactsRequest(typing.TypedDict, total=False):
    gcsSource: ImportGoogetArtifactsGcsSource

@typing.type_check_only
class ImportGoogetArtifactsResponse(typing.TypedDict, total=False):
    errors: _list[ImportGoogetArtifactsErrorInfo]
    googetArtifacts: _list[GoogetArtifact]

@typing.type_check_only
class ImportYumArtifactsErrorInfo(typing.TypedDict, total=False):
    error: Status
    gcsSource: ImportYumArtifactsGcsSource

@typing.type_check_only
class ImportYumArtifactsGcsSource(typing.TypedDict, total=False):
    uris: _list[str]
    useWildcards: bool

@typing.type_check_only
class ImportYumArtifactsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class ImportYumArtifactsRequest(typing.TypedDict, total=False):
    gcsSource: ImportYumArtifactsGcsSource

@typing.type_check_only
class ImportYumArtifactsResponse(typing.TypedDict, total=False):
    errors: _list[ImportYumArtifactsErrorInfo]
    yumArtifacts: _list[YumArtifact]

@typing.type_check_only
class KfpArtifact(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ListAttachmentsResponse(typing.TypedDict, total=False):
    attachments: _list[Attachment]
    nextPageToken: str

@typing.type_check_only
class ListDockerImagesResponse(typing.TypedDict, total=False):
    dockerImages: _list[DockerImage]
    nextPageToken: str

@typing.type_check_only
class ListFilesResponse(typing.TypedDict, total=False):
    files: _list[GoogleDevtoolsArtifactregistryV1File]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMavenArtifactsResponse(typing.TypedDict, total=False):
    mavenArtifacts: _list[MavenArtifact]
    nextPageToken: str

@typing.type_check_only
class ListNpmPackagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    npmPackages: _list[NpmPackage]

@typing.type_check_only
class ListPackagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    packages: _list[Package]

@typing.type_check_only
class ListPrewarmedArtifactsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    prewarmedArtifacts: _list[PrewarmedArtifact]

@typing.type_check_only
class ListPythonPackagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pythonPackages: _list[PythonPackage]

@typing.type_check_only
class ListRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class ListRulesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rules: _list[GoogleDevtoolsArtifactregistryV1Rule]

@typing.type_check_only
class ListTagsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tags: _list[Tag]

@typing.type_check_only
class ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MavenArtifact(typing.TypedDict, total=False):
    artifactId: str
    createTime: str
    groupId: str
    name: str
    pomUri: str
    updateTime: str
    version: str

@typing.type_check_only
class MavenRepository(typing.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigMavenRepositoryCustomRepository
    publicRepository: typing.Literal["PUBLIC_REPOSITORY_UNSPECIFIED", "MAVEN_CENTRAL"]

@typing.type_check_only
class MavenRepositoryConfig(typing.TypedDict, total=False):
    allowSnapshotOverwrites: bool
    versionPolicy: typing.Literal["VERSION_POLICY_UNSPECIFIED", "RELEASE", "SNAPSHOT"]

@typing.type_check_only
class NoCacheFetching(typing.TypedDict, total=False): ...

@typing.type_check_only
class NpmPackage(typing.TypedDict, total=False):
    createTime: str
    name: str
    packageName: str
    tags: _list[str]
    updateTime: str
    version: str

@typing.type_check_only
class NpmRepository(typing.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigNpmRepositoryCustomRepository
    publicRepository: typing.Literal["PUBLIC_REPOSITORY_UNSPECIFIED", "NPMJS"]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class Package(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class PlatformLogsConfig(typing.TypedDict, total=False):
    loggingState: typing.Literal["LOGGING_STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    severityLevel: typing.Literal[
        "SEVERITY_LEVEL_UNSPECIFIED",
        "DEBUG",
        "INFO",
        "NOTICE",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "ALERT",
        "EMERGENCY",
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrewarmArtifactRequest(typing.TypedDict, total=False):
    force: bool
    platform: PrewarmPlatform
    retentionDays: str
    streamLocation: str
    tag: str
    version: str

@typing.type_check_only
class PrewarmArtifactResponse(typing.TypedDict, total=False):
    prewarmedArtifact: PrewarmedArtifact

@typing.type_check_only
class PrewarmPlatform(typing.TypedDict, total=False):
    architecture: str
    os: str

@typing.type_check_only
class PrewarmedArtifact(typing.TypedDict, total=False):
    expirationTime: str
    location: str
    uri: str

@typing.type_check_only
class ProjectConfig(typing.TypedDict, total=False):
    name: str
    platformLogsConfig: PlatformLogsConfig

@typing.type_check_only
class ProjectSettings(typing.TypedDict, total=False):
    legacyRedirectionState: typing.Literal[
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
class PythonPackage(typing.TypedDict, total=False):
    createTime: str
    name: str
    packageName: str
    updateTime: str
    uri: str
    version: str

@typing.type_check_only
class PythonRepository(typing.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigPythonRepositoryCustomRepository
    publicRepository: typing.Literal["PUBLIC_REPOSITORY_UNSPECIFIED", "PYPI"]

@typing.type_check_only
class RemoteRepositoryConfig(typing.TypedDict, total=False):
    aptRepository: AptRepository
    commonRepository: CommonRemoteRepository
    description: str
    disableUpstreamValidation: bool
    dockerRepository: DockerRepository
    mavenRepository: MavenRepository
    noCache: NoCacheFetching
    npmRepository: NpmRepository
    pythonRepository: PythonRepository
    upstreamCredentials: UpstreamCredentials
    yumRepository: YumRepository

@typing.type_check_only
class RemovePrewarmedArtifactRequest(typing.TypedDict, total=False):
    streamLocation: str
    tag: str
    version: str

@typing.type_check_only
class RemovePrewarmedArtifactResponse(typing.TypedDict, total=False):
    prewarmedArtifact: PrewarmedArtifact

@typing.type_check_only
class Repository(typing.TypedDict, total=False):
    cleanupPolicies: dict[str, typing.Any]
    cleanupPolicyDryRun: bool
    createTime: str
    description: str
    disallowUnspecifiedMode: bool
    dockerConfig: DockerRepositoryConfig
    format: typing.Literal[
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
        "RUBY",
    ]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    mavenConfig: MavenRepositoryConfig
    mode: typing.Literal[
        "MODE_UNSPECIFIED",
        "STANDARD_REPOSITORY",
        "VIRTUAL_REPOSITORY",
        "REMOTE_REPOSITORY",
        "AOSS_REPOSITORY",
        "ASSURED_OSS_REPOSITORY",
    ]
    name: str
    platformLogsConfig: PlatformLogsConfig
    registryUri: str
    remoteRepositoryConfig: RemoteRepositoryConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    sizeBytes: str
    updateTime: str
    virtualRepositoryConfig: VirtualRepositoryConfig
    vulnerabilityScanningConfig: VulnerabilityScanningConfig

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UploadAptArtifactMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadAptArtifactMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadAptArtifactRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadAptArtifactResponse(typing.TypedDict, total=False):
    aptArtifacts: _list[AptArtifact]

@typing.type_check_only
class UploadFileMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadFileRequest(typing.TypedDict, total=False):
    fileId: str

@typing.type_check_only
class UploadGenericArtifactMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadGenericArtifactMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadGenericArtifactRequest(typing.TypedDict, total=False):
    filename: str
    packageId: str
    versionId: str

@typing.type_check_only
class UploadGoModuleMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadGoModuleMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoModuleRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoogetArtifactMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadGoogetArtifactMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoogetArtifactRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadGoogetArtifactResponse(typing.TypedDict, total=False):
    googetArtifacts: _list[GoogetArtifact]

@typing.type_check_only
class UploadKfpArtifactMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadKfpArtifactMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadKfpArtifactRequest(typing.TypedDict, total=False):
    description: str
    tags: _list[str]

@typing.type_check_only
class UploadYumArtifactMediaResponse(typing.TypedDict, total=False):
    operation: Operation

@typing.type_check_only
class UploadYumArtifactMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadYumArtifactRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadYumArtifactResponse(typing.TypedDict, total=False):
    yumArtifacts: _list[YumArtifact]

@typing.type_check_only
class UpstreamCredentials(typing.TypedDict, total=False):
    usernamePasswordCredentials: UsernamePasswordCredentials

@typing.type_check_only
class UpstreamPolicy(typing.TypedDict, total=False):
    id: str
    priority: int
    repository: str

@typing.type_check_only
class UsernamePasswordCredentials(typing.TypedDict, total=False):
    passwordSecretVersion: str
    username: str

@typing.type_check_only
class VPCSCConfig(typing.TypedDict, total=False):
    name: str
    vpcscPolicy: typing.Literal["VPCSC_POLICY_UNSPECIFIED", "DENY", "ALLOW"]

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    description: str
    fingerprints: _list[Hash]
    metadata: dict[str, typing.Any]
    name: str
    relatedTags: _list[Tag]
    updateTime: str

@typing.type_check_only
class VirtualRepositoryConfig(typing.TypedDict, total=False):
    upstreamPolicies: _list[UpstreamPolicy]

@typing.type_check_only
class VulnerabilityScanningConfig(typing.TypedDict, total=False):
    enablementConfig: typing.Literal[
        "ENABLEMENT_CONFIG_UNSPECIFIED", "INHERITED", "DISABLED"
    ]
    enablementState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED",
        "SCANNING_UNSUPPORTED",
        "SCANNING_DISABLED",
        "SCANNING_ACTIVE",
    ]
    enablementStateReason: str
    lastEnableTime: str

@typing.type_check_only
class YumArtifact(typing.TypedDict, total=False):
    architecture: str
    name: str
    packageName: str
    packageType: typing.Literal["PACKAGE_TYPE_UNSPECIFIED", "BINARY", "SOURCE"]

@typing.type_check_only
class YumRepository(typing.TypedDict, total=False):
    customRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryCustomRepository
    publicRepository: GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository
