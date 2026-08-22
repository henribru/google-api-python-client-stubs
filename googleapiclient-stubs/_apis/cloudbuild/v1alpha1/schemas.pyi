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
    images: _list[str]
    mavenArtifacts: _list[MavenArtifact]
    objects: ArtifactObjects
    pythonPackages: _list[PythonPackage]

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
class BatchCreateRepositoriesResponse(typing.TypedDict, total=False):
    repositories: _list[Repository]

@typing.type_check_only
class BitbucketServerConnectedRepository(typing.TypedDict, total=False):
    parent: str
    repo: BitbucketServerRepositoryId
    status: Status

@typing.type_check_only
class BitbucketServerRepositoryId(typing.TypedDict, total=False):
    projectKey: str
    repoSlug: str
    webhookId: int

@typing.type_check_only
class Build(typing.TypedDict, total=False):
    approval: BuildApproval
    artifacts: Artifacts
    availableSecrets: Secrets
    buildTriggerId: str
    createTime: str
    failureInfo: FailureInfo
    finishTime: str
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
    diskSizeGb: str
    dynamicSubstitutions: bool
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
        "UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32", "E2_HIGHCPU_8", "E2_HIGHCPU_32"
    ]
    pool: PoolOption
    requestedVerifyOption: typing.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[typing.Literal["NONE", "SHA256", "MD5"]]
    substitutionOption: typing.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[Volume]
    workerPool: str

@typing.type_check_only
class BuildStep(typing.TypedDict, total=False):
    allowExitCodes: _list[int]
    allowFailure: bool
    args: _list[str]
    dir: str
    entrypoint: str
    env: _list[str]
    exitCode: int
    id: str
    name: str
    pullTiming: TimeSpan
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
class BuiltImage(typing.TypedDict, total=False):
    digest: str
    name: str
    pushTiming: TimeSpan

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateBitbucketServerConfigOperationMetadata(typing.TypedDict, total=False):
    bitbucketServerConfig: str
    completeTime: str
    createTime: str

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
class CreateWorkerPoolOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

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
class GitLabConnectedRepository(typing.TypedDict, total=False):
    parent: str
    repo: GitLabRepositoryId
    status: Status

@typing.type_check_only
class GitLabRepositoryId(typing.TypedDict, total=False):
    id: str
    webhookId: int

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class HTTPDelivery(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Hash(typing.TypedDict, total=False):
    type: typing.Literal["NONE", "SHA256", "MD5"]
    value: str

@typing.type_check_only
class InlineSecret(typing.TypedDict, total=False):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ListWorkerPoolsResponse(typing.TypedDict, total=False):
    workerPools: _list[WorkerPool]

@typing.type_check_only
class MavenArtifact(typing.TypedDict, total=False):
    artifactId: str
    groupId: str
    path: str
    repository: str
    version: str

@typing.type_check_only
class Network(typing.TypedDict, total=False):
    network: str
    projectId: str
    subnetwork: str

@typing.type_check_only
class Notification(typing.TypedDict, total=False):
    filter: str
    httpDelivery: HTTPDelivery
    slackDelivery: SlackDelivery
    smtpDelivery: SMTPDelivery
    structDelivery: dict[str, typing.Any]

@typing.type_check_only
class NotifierConfig(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: NotifierMetadata
    spec: NotifierSpec

@typing.type_check_only
class NotifierMetadata(typing.TypedDict, total=False):
    name: str
    notifier: str

@typing.type_check_only
class NotifierSecret(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class NotifierSecretRef(typing.TypedDict, total=False):
    secretRef: str

@typing.type_check_only
class NotifierSpec(typing.TypedDict, total=False):
    notification: Notification
    secrets: _list[NotifierSecret]

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
class ProcessAppManifestCallbackOperationMetadata(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class PythonPackage(typing.TypedDict, total=False):
    paths: _list[str]
    repository: str

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
class Repository(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    etag: str
    name: str
    remoteUri: str
    updateTime: str

@typing.type_check_only
class Results(typing.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    images: _list[BuiltImage]
    mavenArtifacts: _list[UploadedMavenArtifact]
    numArtifacts: str
    pythonPackages: _list[UploadedPythonPackage]

@typing.type_check_only
class RunWorkflowCustomOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    pipelineRunId: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class SMTPDelivery(typing.TypedDict, total=False):
    fromAddress: str
    password: NotifierSecretRef
    port: str
    recipientAddresses: _list[str]
    senderAddress: str
    server: str

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
class SlackDelivery(typing.TypedDict, total=False):
    webhookUri: NotifierSecretRef

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    repoSource: RepoSource
    storageSource: StorageSource
    storageSourceManifest: StorageSourceManifest

@typing.type_check_only
class SourceProvenance(typing.TypedDict, total=False):
    fileHashes: dict[str, typing.Any]
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource
    resolvedStorageSourceManifest: StorageSourceManifest

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageSource(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

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
class UploadedMavenArtifact(typing.TypedDict, total=False):
    fileHashes: FileHashes
    pushTiming: TimeSpan
    uri: str

@typing.type_check_only
class UploadedPythonPackage(typing.TypedDict, total=False):
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
class WorkerConfig(typing.TypedDict, total=False):
    diskSizeGb: str
    machineType: str
    network: Network
    tag: str

@typing.type_check_only
class WorkerPool(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    name: str
    projectId: str
    regions: _list[
        typing.Literal[
            "REGION_UNSPECIFIED", "us-central1", "us-west1", "us-east1", "us-east4"
        ]
    ]
    serviceAccountEmail: str
    status: typing.Literal[
        "STATUS_UNSPECIFIED", "CREATING", "RUNNING", "DELETING", "DELETED"
    ]
    updateTime: str
    workerConfig: WorkerConfig
    workerCount: str
