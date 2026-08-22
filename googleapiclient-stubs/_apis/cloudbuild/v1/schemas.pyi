import typing

_list = list

@typing.type_check_only
class ApprovalConfig(typing.TypedDict, total=False):
    approvalRequired: bool

@typing.type_check_only
class ApprovalResult(typing.TypedDict, total=False):
    approvalTime: str
    approverAccount: str
    comment: str
    decision: typing.Literal["DECISION_UNSPECIFIED", "APPROVED", "REJECTED"]
    url: str

@typing.type_check_only
class ApproveBuildRequest(typing.TypedDict, total=False):
    approvalResult: ApprovalResult

@typing.type_check_only
class ArtifactObjects(typing.TypedDict, total=False):
    location: str
    paths: _list[str]
    timing: TimeSpan

@typing.type_check_only
class ArtifactResult(typing.TypedDict, total=False):
    fileHash: _list[FileHashes]
    location: str

@typing.type_check_only
class Artifacts(typing.TypedDict, total=False):
    genericArtifacts: _list[GenericArtifact]
    goModules: _list[GoModule]
    images: _list[str]
    mavenArtifacts: _list[MavenArtifact]
    npmPackages: _list[NpmPackage]
    objects: ArtifactObjects
    oci: _list[Oci]
    pythonPackages: _list[PythonPackage]

@typing.type_check_only
class BatchCreateBitbucketServerConnectedRepositoriesRequest(
    typing.TypedDict, total=False
):
    requests: _list[CreateBitbucketServerConnectedRepositoryRequest]

@typing.type_check_only
class BatchCreateBitbucketServerConnectedRepositoriesResponse(
    typing.TypedDict, total=False
):
    bitbucketServerConnectedRepositories: _list[BitbucketServerConnectedRepository]

@typing.type_check_only
class BatchCreateBitbucketServerConnectedRepositoriesResponseMetadata(
    typing.TypedDict, total=False
):
    completeTime: str
    config: str
    createTime: str

@typing.type_check_only
class BatchCreateGitLabConnectedRepositoriesRequest(typing.TypedDict, total=False):
    requests: _list[CreateGitLabConnectedRepositoryRequest]

@typing.type_check_only
class BatchCreateGitLabConnectedRepositoriesResponse(typing.TypedDict, total=False):
    gitlabConnectedRepositories: _list[GitLabConnectedRepository]

@typing.type_check_only
class BatchCreateGitLabConnectedRepositoriesResponseMetadata(
    typing.TypedDict, total=False
):
    completeTime: str
    config: str
    createTime: str

@typing.type_check_only
class BitbucketServerConfig(typing.TypedDict, total=False):
    apiKey: str
    connectedRepositories: _list[BitbucketServerRepositoryId]
    createTime: str
    hostUri: str
    name: str
    peeredNetwork: str
    peeredNetworkIpRange: str
    secrets: BitbucketServerSecrets
    sslCa: str
    username: str
    webhookKey: str

@typing.type_check_only
class BitbucketServerConnectedRepository(typing.TypedDict, total=False):
    parent: str
    repo: BitbucketServerRepositoryId
    status: Status

@typing.type_check_only
class BitbucketServerRepository(typing.TypedDict, total=False):
    browseUri: str
    description: str
    displayName: str
    name: str
    repoId: BitbucketServerRepositoryId

@typing.type_check_only
class BitbucketServerRepositoryId(typing.TypedDict, total=False):
    projectKey: str
    repoSlug: str
    webhookId: int

@typing.type_check_only
class BitbucketServerSecrets(typing.TypedDict, total=False):
    adminAccessTokenVersionName: str
    readAccessTokenVersionName: str
    webhookSecretVersionName: str

@typing.type_check_only
class BitbucketServerTriggerConfig(typing.TypedDict, total=False):
    bitbucketServerConfig: BitbucketServerConfig
    bitbucketServerConfigResource: str
    projectKey: str
    pullRequest: PullRequestFilter
    push: PushFilter
    repoSlug: str

@typing.type_check_only
class Build(typing.TypedDict, total=False):
    approval: BuildApproval
    artifacts: Artifacts
    availableSecrets: Secrets
    buildTriggerId: str
    createTime: str
    dependencies: _list[Dependency]
    failureInfo: FailureInfo
    finishTime: str
    gitConfig: GitConfig
    id: str
    images: _list[str]
    logUrl: str
    logsBucket: str
    name: str
    options: BuildOptions
    projectId: str
    queueTtl: str
    results: Results
    secrets: _list[Secret]
    serviceAccount: str
    source: Source
    sourceProvenance: SourceProvenance
    startTime: str
    status: typing.Literal[
        "STATUS_UNKNOWN",
        "PENDING",
        "QUEUED",
        "WORKING",
        "SUCCESS",
        "FAILURE",
        "INTERNAL_ERROR",
        "TIMEOUT",
        "CANCELLED",
        "EXPIRED",
    ]
    statusDetail: str
    steps: _list[BuildStep]
    substitutions: dict[str, typing.Any]
    tags: _list[str]
    timeout: str
    timing: dict[str, typing.Any]
    warnings: _list[Warning]

@typing.type_check_only
class BuildApproval(typing.TypedDict, total=False):
    config: ApprovalConfig
    result: ApprovalResult
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED", "CANCELLED"
    ]

@typing.type_check_only
class BuildOperationMetadata(typing.TypedDict, total=False):
    build: Build

@typing.type_check_only
class BuildOptions(typing.TypedDict, total=False):
    automapSubstitutions: bool
    defaultLogsBucketBehavior: typing.Literal[
        "DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED",
        "REGIONAL_USER_OWNED_BUCKET",
        "LEGACY_BUCKET",
    ]
    diskSizeGb: str
    dynamicSubstitutions: bool
    enableStructuredLogging: bool
    env: _list[str]
    logStreamingOption: typing.Literal["STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"]
    logging: typing.Literal[
        "LOGGING_UNSPECIFIED",
        "LEGACY",
        "GCS_ONLY",
        "STACKDRIVER_ONLY",
        "CLOUD_LOGGING_ONLY",
        "NONE",
    ]
    machineType: typing.Literal[
        "UNSPECIFIED",
        "N1_HIGHCPU_8",
        "N1_HIGHCPU_32",
        "E2_HIGHCPU_8",
        "E2_HIGHCPU_32",
        "E2_MEDIUM",
        "E2_STANDARD_2",
    ]
    pool: PoolOption
    pubsubTopic: str
    requestedVerifyOption: typing.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[
        typing.Literal[
            "NONE", "SHA256", "MD5", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
        ]
    ]
    substitutionOption: typing.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[Volume]
    workerPool: str

@typing.type_check_only
class BuildStep(typing.TypedDict, total=False):
    allowExitCodes: _list[int]
    allowFailure: bool
    args: _list[str]
    automapSubstitutions: bool
    dir: str
    entrypoint: str
    env: _list[str]
    exitCode: int
    id: str
    name: str
    pullTiming: TimeSpan
    results: _list[StepResult]
    script: str
    secretEnv: _list[str]
    status: typing.Literal[
        "STATUS_UNKNOWN",
        "PENDING",
        "QUEUED",
        "WORKING",
        "SUCCESS",
        "FAILURE",
        "INTERNAL_ERROR",
        "TIMEOUT",
        "CANCELLED",
        "EXPIRED",
    ]
    timeout: str
    timing: TimeSpan
    volumes: _list[Volume]
    waitFor: _list[str]

@typing.type_check_only
class BuildStepResults(typing.TypedDict, total=False):
    results: dict[str, typing.Any]

@typing.type_check_only
class BuildTrigger(typing.TypedDict, total=False):
    approvalConfig: ApprovalConfig
    autodetect: bool
    bitbucketServerTriggerConfig: BitbucketServerTriggerConfig
    build: Build
    createTime: str
    description: str
    developerConnectEventConfig: DeveloperConnectEventConfig
    disabled: bool
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED", "REPO", "WEBHOOK", "PUBSUB", "MANUAL"
    ]
    filename: str
    filter: str
    gitFileSource: GitFileSource
    github: GitHubEventsConfig
    gitlabEnterpriseEventsConfig: GitLabEventsConfig
    id: str
    ignoredFiles: _list[str]
    includeBuildLogs: typing.Literal[
        "INCLUDE_BUILD_LOGS_UNSPECIFIED", "INCLUDE_BUILD_LOGS_WITH_STATUS"
    ]
    includedFiles: _list[str]
    name: str
    pubsubConfig: PubsubConfig
    repositoryEventConfig: RepositoryEventConfig
    resourceName: str
    serviceAccount: str
    sourceToBuild: GitRepoSource
    substitutions: dict[str, typing.Any]
    tags: _list[str]
    triggerTemplate: RepoSource
    webhookConfig: WebhookConfig

@typing.type_check_only
class BuiltImage(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    digest: str
    name: str
    ociMediaType: typing.Literal[
        "OCI_MEDIA_TYPE_UNSPECIFIED", "IMAGE_MANIFEST", "IMAGE_INDEX"
    ]
    pushTiming: TimeSpan

@typing.type_check_only
class CancelBuildRequest(typing.TypedDict, total=False):
    id: str
    name: str
    projectId: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConnectedRepository(typing.TypedDict, total=False):
    dir: str
    repository: str
    revision: str

@typing.type_check_only
class CreateBitbucketServerConfigOperationMetadata(typing.TypedDict, total=False):
    bitbucketServerConfig: str
    completeTime: str
    createTime: str

@typing.type_check_only
class CreateBitbucketServerConnectedRepositoryRequest(typing.TypedDict, total=False):
    bitbucketServerConnectedRepository: BitbucketServerConnectedRepository
    parent: str

@typing.type_check_only
class CreateGitHubEnterpriseConfigOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class CreateGitLabConfigOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    gitlabConfig: str

@typing.type_check_only
class CreateGitLabConnectedRepositoryRequest(typing.TypedDict, total=False):
    gitlabConnectedRepository: GitLabConnectedRepository
    parent: str

@typing.type_check_only
class CreateWorkerPoolOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

@typing.type_check_only
class DefaultServiceAccount(typing.TypedDict, total=False):
    name: str
    serviceAccountEmail: str

@typing.type_check_only
class DeleteBitbucketServerConfigOperationMetadata(typing.TypedDict, total=False):
    bitbucketServerConfig: str
    completeTime: str
    createTime: str

@typing.type_check_only
class DeleteGitHubEnterpriseConfigOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class DeleteGitLabConfigOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    gitlabConfig: str

@typing.type_check_only
class DeleteWorkerPoolOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

@typing.type_check_only
class Dependency(typing.TypedDict, total=False):
    empty: bool
    genericArtifact: GenericArtifactDependency
    gitSource: GitSourceDependency

@typing.type_check_only
class DeveloperConnectConfig(typing.TypedDict, total=False):
    dir: str
    gitRepositoryLink: str
    revision: str

@typing.type_check_only
class DeveloperConnectEventConfig(typing.TypedDict, total=False):
    gitRepositoryLink: str
    gitRepositoryLinkType: typing.Literal[
        "GIT_REPOSITORY_LINK_TYPE_UNSPECIFIED",
        "GITHUB",
        "GITHUB_ENTERPRISE",
        "GITLAB",
        "GITLAB_ENTERPRISE",
        "BITBUCKET_DATA_CENTER",
        "BITBUCKET_CLOUD",
    ]
    pullRequest: PullRequestFilter
    push: PushFilter

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FailureInfo(typing.TypedDict, total=False):
    detail: str
    type: typing.Literal[
        "FAILURE_TYPE_UNSPECIFIED",
        "PUSH_FAILED",
        "PUSH_IMAGE_NOT_FOUND",
        "PUSH_NOT_AUTHORIZED",
        "LOGGING_FAILURE",
        "USER_BUILD_STEP",
        "FETCH_SOURCE_FAILED",
    ]

@typing.type_check_only
class FileHashes(typing.TypedDict, total=False):
    fileHash: _list[Hash]

@typing.type_check_only
class GenericArtifact(typing.TypedDict, total=False):
    folder: str
    registryPath: str

@typing.type_check_only
class GenericArtifactDependency(typing.TypedDict, total=False):
    destPath: str
    resource: str

@typing.type_check_only
class GitConfig(typing.TypedDict, total=False):
    http: HttpConfig

@typing.type_check_only
class GitFileSource(typing.TypedDict, total=False):
    bitbucketServerConfig: str
    githubEnterpriseConfig: str
    path: str
    repoType: typing.Literal[
        "UNKNOWN",
        "CLOUD_SOURCE_REPOSITORIES",
        "GITHUB",
        "BITBUCKET_SERVER",
        "GITLAB",
        "BITBUCKET_CLOUD",
    ]
    repository: str
    revision: str
    uri: str

@typing.type_check_only
class GitHubEnterpriseConfig(typing.TypedDict, total=False):
    appId: str
    createTime: str
    displayName: str
    hostUrl: str
    name: str
    peeredNetwork: str
    secrets: GitHubEnterpriseSecrets
    sslCa: str
    webhookKey: str

@typing.type_check_only
class GitHubEnterpriseSecrets(typing.TypedDict, total=False):
    oauthClientIdName: str
    oauthClientIdVersionName: str
    oauthSecretName: str
    oauthSecretVersionName: str
    privateKeyName: str
    privateKeyVersionName: str
    webhookSecretName: str
    webhookSecretVersionName: str

@typing.type_check_only
class GitHubEventsConfig(typing.TypedDict, total=False):
    enterpriseConfigResourceName: str
    installationId: str
    name: str
    owner: str
    pullRequest: PullRequestFilter
    push: PushFilter

@typing.type_check_only
class GitLabConfig(typing.TypedDict, total=False):
    connectedRepositories: _list[GitLabRepositoryId]
    createTime: str
    enterpriseConfig: GitLabEnterpriseConfig
    name: str
    secrets: GitLabSecrets
    username: str
    webhookKey: str

@typing.type_check_only
class GitLabConnectedRepository(typing.TypedDict, total=False):
    parent: str
    repo: GitLabRepositoryId
    status: Status

@typing.type_check_only
class GitLabEnterpriseConfig(typing.TypedDict, total=False):
    hostUri: str
    serviceDirectoryConfig: ServiceDirectoryConfig
    sslCa: str

@typing.type_check_only
class GitLabEventsConfig(typing.TypedDict, total=False):
    gitlabConfig: GitLabConfig
    gitlabConfigResource: str
    projectNamespace: str
    pullRequest: PullRequestFilter
    push: PushFilter

@typing.type_check_only
class GitLabRepository(typing.TypedDict, total=False):
    browseUri: str
    description: str
    displayName: str
    name: str
    repositoryId: GitLabRepositoryId

@typing.type_check_only
class GitLabRepositoryId(typing.TypedDict, total=False):
    id: str
    webhookId: int

@typing.type_check_only
class GitLabSecrets(typing.TypedDict, total=False):
    apiAccessTokenVersion: str
    apiKeyVersion: str
    readAccessTokenVersion: str
    webhookSecretVersion: str

@typing.type_check_only
class GitRepoSource(typing.TypedDict, total=False):
    bitbucketServerConfig: str
    githubEnterpriseConfig: str
    ref: str
    repoType: typing.Literal[
        "UNKNOWN",
        "CLOUD_SOURCE_REPOSITORIES",
        "GITHUB",
        "BITBUCKET_SERVER",
        "GITLAB",
        "BITBUCKET_CLOUD",
    ]
    repository: str
    uri: str

@typing.type_check_only
class GitSource(typing.TypedDict, total=False):
    dir: str
    revision: str
    url: str

@typing.type_check_only
class GitSourceDependency(typing.TypedDict, total=False):
    depth: str
    destPath: str
    recurseSubmodules: bool
    repository: GitSourceRepository
    revision: str

@typing.type_check_only
class GitSourceRepository(typing.TypedDict, total=False):
    developerConnect: str
    url: str

@typing.type_check_only
class GoModule(typing.TypedDict, total=False):
    modulePath: str
    moduleVersion: str
    repositoryLocation: str
    repositoryName: str
    repositoryProjectId: str
    sourcePath: str

@typing.type_check_only
class Hash(typing.TypedDict, total=False):
    type: typing.Literal[
        "NONE", "SHA256", "MD5", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
    ]
    value: str

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class HttpConfig(typing.TypedDict, total=False):
    proxySecretVersionName: str

@typing.type_check_only
class InlineSecret(typing.TypedDict, total=False):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ListBitbucketServerConfigsResponse(typing.TypedDict, total=False):
    bitbucketServerConfigs: _list[BitbucketServerConfig]
    nextPageToken: str

@typing.type_check_only
class ListBitbucketServerRepositoriesResponse(typing.TypedDict, total=False):
    bitbucketServerRepositories: _list[BitbucketServerRepository]
    nextPageToken: str

@typing.type_check_only
class ListBuildTriggersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    triggers: _list[BuildTrigger]

@typing.type_check_only
class ListBuildsResponse(typing.TypedDict, total=False):
    builds: _list[Build]
    nextPageToken: str

@typing.type_check_only
class ListGitLabConfigsResponse(typing.TypedDict, total=False):
    gitlabConfigs: _list[GitLabConfig]
    nextPageToken: str

@typing.type_check_only
class ListGitLabRepositoriesResponse(typing.TypedDict, total=False):
    gitlabRepositories: _list[GitLabRepository]
    nextPageToken: str

@typing.type_check_only
class ListGithubEnterpriseConfigsResponse(typing.TypedDict, total=False):
    configs: _list[GitHubEnterpriseConfig]

@typing.type_check_only
class ListWorkerPoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workerPools: _list[WorkerPool]

@typing.type_check_only
class MavenArtifact(typing.TypedDict, total=False):
    artifactId: str
    deployFolder: str
    groupId: str
    path: str
    repository: str
    version: str

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    egressOption: typing.Literal[
        "EGRESS_OPTION_UNSPECIFIED", "NO_PUBLIC_EGRESS", "PUBLIC_EGRESS"
    ]
    peeredNetwork: str
    peeredNetworkIpRange: str

@typing.type_check_only
class NpmPackage(typing.TypedDict, total=False):
    packagePath: str
    repository: str

@typing.type_check_only
class Oci(typing.TypedDict, total=False):
    file: str
    registryPath: str
    tags: _list[str]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class PoolOption(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class PrivatePoolV1Config(typing.TypedDict, total=False):
    networkConfig: NetworkConfig
    privateServiceConnect: PrivateServiceConnect
    workerConfig: WorkerConfig

@typing.type_check_only
class PrivateServiceConnect(typing.TypedDict, total=False):
    networkAttachment: str
    publicIpAddressDisabled: bool
    routeAllTraffic: bool

@typing.type_check_only
class ProcessAppManifestCallbackOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class PubsubConfig(typing.TypedDict, total=False):
    serviceAccountEmail: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "OK",
        "SUBSCRIPTION_DELETED",
        "TOPIC_DELETED",
        "SUBSCRIPTION_MISCONFIGURED",
    ]
    subscription: str
    topic: str

@typing.type_check_only
class PullRequestFilter(typing.TypedDict, total=False):
    branch: str
    commentControl: typing.Literal[
        "COMMENTS_DISABLED",
        "COMMENTS_ENABLED",
        "COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY",
    ]
    invertRegex: bool

@typing.type_check_only
class PushFilter(typing.TypedDict, total=False):
    branch: str
    invertRegex: bool
    tag: str

@typing.type_check_only
class PythonPackage(typing.TypedDict, total=False):
    paths: _list[str]
    repository: str

@typing.type_check_only
class ReceiveTriggerWebhookResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveBitbucketServerConnectedRepositoryRequest(typing.TypedDict, total=False):
    connectedRepository: BitbucketServerRepositoryId

@typing.type_check_only
class RemoveGitLabConnectedRepositoryRequest(typing.TypedDict, total=False):
    connectedRepository: GitLabRepositoryId

@typing.type_check_only
class RepoSource(typing.TypedDict, total=False):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    substitutions: dict[str, typing.Any]
    tagName: str

@typing.type_check_only
class RepositoryEventConfig(typing.TypedDict, total=False):
    pullRequest: PullRequestFilter
    push: PushFilter
    repository: str
    repositoryType: typing.Literal[
        "REPOSITORY_TYPE_UNSPECIFIED",
        "GITHUB",
        "GITHUB_ENTERPRISE",
        "GITLAB_ENTERPRISE",
        "BITBUCKET_DATA_CENTER",
        "BITBUCKET_CLOUD",
    ]

@typing.type_check_only
class Results(typing.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    buildStepResults: dict[str, typing.Any]
    genericArtifacts: _list[UploadedGenericArtifact]
    goModules: _list[UploadedGoModule]
    images: _list[BuiltImage]
    mavenArtifacts: _list[UploadedMavenArtifact]
    npmPackages: _list[UploadedNpmPackage]
    numArtifacts: str
    pythonPackages: _list[UploadedPythonPackage]

@typing.type_check_only
class RetryBuildRequest(typing.TypedDict, total=False):
    id: str
    name: str
    projectId: str

@typing.type_check_only
class RunBuildTriggerRequest(typing.TypedDict, total=False):
    projectId: str
    source: RepoSource
    triggerId: str

@typing.type_check_only
class Secret(typing.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: dict[str, typing.Any]

@typing.type_check_only
class SecretManagerSecret(typing.TypedDict, total=False):
    env: str
    versionName: str

@typing.type_check_only
class Secrets(typing.TypedDict, total=False):
    inline: _list[InlineSecret]
    secretManager: _list[SecretManagerSecret]

@typing.type_check_only
class ServiceDirectoryConfig(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    connectedRepository: ConnectedRepository
    developerConnectConfig: DeveloperConnectConfig
    gitSource: GitSource
    repoSource: RepoSource
    storageSource: StorageSource
    storageSourceManifest: StorageSourceManifest

@typing.type_check_only
class SourceProvenance(typing.TypedDict, total=False):
    fileHashes: dict[str, typing.Any]
    resolvedConnectedRepository: ConnectedRepository
    resolvedGitSource: GitSource
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource
    resolvedStorageSourceManifest: StorageSourceManifest

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StepResult(typing.TypedDict, total=False):
    attestationContent: str
    attestationType: str
    name: str

@typing.type_check_only
class StorageSource(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str
    sourceFetcher: typing.Literal["SOURCE_FETCHER_UNSPECIFIED", "GSUTIL", "GCS_FETCHER"]

@typing.type_check_only
class StorageSourceManifest(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class TimeSpan(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateBitbucketServerConfigOperationMetadata(typing.TypedDict, total=False):
    bitbucketServerConfig: str
    completeTime: str
    createTime: str

@typing.type_check_only
class UpdateGitHubEnterpriseConfigOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class UpdateGitLabConfigOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    gitlabConfig: str

@typing.type_check_only
class UpdateWorkerPoolOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

@typing.type_check_only
class UploadedGenericArtifact(typing.TypedDict, total=False):
    artifactFingerprint: FileHashes
    artifactRegistryPackage: str
    fileHashes: dict[str, typing.Any]
    pushTiming: TimeSpan
    uri: str

@typing.type_check_only
class UploadedGoModule(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: FileHashes
    pushTiming: TimeSpan
    uri: str

@typing.type_check_only
class UploadedMavenArtifact(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: FileHashes
    pushTiming: TimeSpan
    uri: str

@typing.type_check_only
class UploadedNpmPackage(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: FileHashes
    pushTiming: TimeSpan
    uri: str

@typing.type_check_only
class UploadedPythonPackage(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: FileHashes
    pushTiming: TimeSpan
    uri: str

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class Warning(typing.TypedDict, total=False):
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "INFO", "WARNING", "ALERT"]
    text: str

@typing.type_check_only
class WebhookConfig(typing.TypedDict, total=False):
    secret: str
    state: typing.Literal["STATE_UNSPECIFIED", "OK", "SECRET_DELETED"]

@typing.type_check_only
class WorkerConfig(typing.TypedDict, total=False):
    diskSizeGb: str
    enableNestedVirtualization: bool
    machineType: str

@typing.type_check_only
class WorkerPool(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    name: str
    privatePoolV1Config: PrivatePoolV1Config
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "DELETING", "DELETED", "UPDATING"
    ]
    uid: str
    updateTime: str
