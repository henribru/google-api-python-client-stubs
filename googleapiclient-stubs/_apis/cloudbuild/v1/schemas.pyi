import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApprovalConfig(typing_extensions.TypedDict, total=False):
    approvalRequired: bool

@typing.type_check_only
class ApprovalResult(typing_extensions.TypedDict, total=False):
    approvalTime: str
    approverAccount: str
    comment: str
    decision: typing_extensions.Literal["DECISION_UNSPECIFIED", "APPROVED", "REJECTED"]
    url: str

@typing.type_check_only
class ApproveBuildRequest(typing_extensions.TypedDict, total=False):
    approvalResult: ApprovalResult

@typing.type_check_only
class ArtifactObjects(typing_extensions.TypedDict, total=False):
    location: str
    paths: _list[str]
    timing: TimeSpan

@typing.type_check_only
class ArtifactResult(typing_extensions.TypedDict, total=False):
    fileHash: _list[FileHashes]
    location: str

@typing.type_check_only
class Artifacts(typing_extensions.TypedDict, total=False):
    images: _list[str]
    objects: ArtifactObjects

@typing.type_check_only
class Build(typing_extensions.TypedDict, total=False):
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
    status: typing_extensions.Literal[
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
class BuildApproval(typing_extensions.TypedDict, total=False):
    config: ApprovalConfig
    result: ApprovalResult
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED", "CANCELLED"
    ]

@typing.type_check_only
class BuildOperationMetadata(typing_extensions.TypedDict, total=False):
    build: Build

@typing.type_check_only
class BuildOptions(typing_extensions.TypedDict, total=False):
    diskSizeGb: str
    dynamicSubstitutions: bool
    env: _list[str]
    logStreamingOption: typing_extensions.Literal[
        "STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"
    ]
    logging: typing_extensions.Literal[
        "LOGGING_UNSPECIFIED",
        "LEGACY",
        "GCS_ONLY",
        "STACKDRIVER_ONLY",
        "CLOUD_LOGGING_ONLY",
        "NONE",
    ]
    machineType: typing_extensions.Literal[
        "UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32", "E2_HIGHCPU_8", "E2_HIGHCPU_32"
    ]
    pool: PoolOption
    requestedVerifyOption: typing_extensions.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[str]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[Volume]
    workerPool: str

@typing.type_check_only
class BuildStep(typing_extensions.TypedDict, total=False):
    args: _list[str]
    dir: str
    entrypoint: str
    env: _list[str]
    id: str
    name: str
    pullTiming: TimeSpan
    script: str
    secretEnv: _list[str]
    status: typing_extensions.Literal[
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
class BuildTrigger(typing_extensions.TypedDict, total=False):
    approvalConfig: ApprovalConfig
    autodetect: bool
    build: Build
    createTime: str
    description: str
    disabled: bool
    filename: str
    filter: str
    gitFileSource: GitFileSource
    github: GitHubEventsConfig
    id: str
    ignoredFiles: _list[str]
    includedFiles: _list[str]
    name: str
    pubsubConfig: PubsubConfig
    resourceName: str
    serviceAccount: str
    sourceToBuild: GitRepoSource
    substitutions: dict[str, typing.Any]
    tags: _list[str]
    triggerTemplate: RepoSource
    webhookConfig: WebhookConfig

@typing.type_check_only
class BuiltImage(typing_extensions.TypedDict, total=False):
    digest: str
    name: str
    pushTiming: TimeSpan

@typing.type_check_only
class CancelBuildRequest(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    projectId: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateGitHubEnterpriseConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class CreateWorkerPoolOperationMetadata(typing_extensions.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

@typing.type_check_only
class DeleteGitHubEnterpriseConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class DeleteWorkerPoolOperationMetadata(typing_extensions.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FailureInfo(typing_extensions.TypedDict, total=False):
    detail: str
    type: typing_extensions.Literal[
        "FAILURE_TYPE_UNSPECIFIED",
        "PUSH_FAILED",
        "PUSH_IMAGE_NOT_FOUND",
        "PUSH_NOT_AUTHORIZED",
        "LOGGING_FAILURE",
        "USER_BUILD_STEP",
        "FETCH_SOURCE_FAILED",
    ]

@typing.type_check_only
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: _list[Hash]

@typing.type_check_only
class GitFileSource(typing_extensions.TypedDict, total=False):
    path: str
    repoType: typing_extensions.Literal[
        "UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB"
    ]
    revision: str
    uri: str

@typing.type_check_only
class GitHubEnterpriseConfig(typing_extensions.TypedDict, total=False):
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
class GitHubEnterpriseSecrets(typing_extensions.TypedDict, total=False):
    oauthClientIdName: str
    oauthClientIdVersionName: str
    oauthSecretName: str
    oauthSecretVersionName: str
    privateKeyName: str
    privateKeyVersionName: str
    webhookSecretName: str
    webhookSecretVersionName: str

@typing.type_check_only
class GitHubEventsConfig(typing_extensions.TypedDict, total=False):
    enterpriseConfigResourceName: str
    installationId: str
    name: str
    owner: str
    pullRequest: PullRequestFilter
    push: PushFilter

@typing.type_check_only
class GitRepoSource(typing_extensions.TypedDict, total=False):
    ref: str
    repoType: typing_extensions.Literal[
        "UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB"
    ]
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV2OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class HTTPDelivery(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["NONE", "SHA256", "MD5"]
    value: str

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class InlineSecret(typing_extensions.TypedDict, total=False):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ListBuildTriggersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    triggers: _list[BuildTrigger]

@typing.type_check_only
class ListBuildsResponse(typing_extensions.TypedDict, total=False):
    builds: _list[Build]
    nextPageToken: str

@typing.type_check_only
class ListGithubEnterpriseConfigsResponse(typing_extensions.TypedDict, total=False):
    configs: _list[GitHubEnterpriseConfig]

@typing.type_check_only
class ListWorkerPoolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workerPools: _list[WorkerPool]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    egressOption: typing_extensions.Literal[
        "EGRESS_OPTION_UNSPECIFIED", "NO_PUBLIC_EGRESS", "PUBLIC_EGRESS"
    ]
    peeredNetwork: str

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    filter: str
    httpDelivery: HTTPDelivery
    slackDelivery: SlackDelivery
    smtpDelivery: SMTPDelivery
    structDelivery: dict[str, typing.Any]

@typing.type_check_only
class NotifierConfig(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: NotifierMetadata
    spec: NotifierSpec

@typing.type_check_only
class NotifierMetadata(typing_extensions.TypedDict, total=False):
    name: str
    notifier: str

@typing.type_check_only
class NotifierSecret(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class NotifierSecretRef(typing_extensions.TypedDict, total=False):
    secretRef: str

@typing.type_check_only
class NotifierSpec(typing_extensions.TypedDict, total=False):
    notification: Notification
    secrets: _list[NotifierSecret]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class PoolOption(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class PrivatePoolV1Config(typing_extensions.TypedDict, total=False):
    networkConfig: NetworkConfig
    workerConfig: WorkerConfig

@typing.type_check_only
class ProcessAppManifestCallbackOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class PubsubConfig(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "OK",
        "SUBSCRIPTION_DELETED",
        "TOPIC_DELETED",
        "SUBSCRIPTION_MISCONFIGURED",
    ]
    subscription: str
    topic: str

@typing.type_check_only
class PullRequestFilter(typing_extensions.TypedDict, total=False):
    branch: str
    commentControl: typing_extensions.Literal[
        "COMMENTS_DISABLED",
        "COMMENTS_ENABLED",
        "COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY",
    ]
    invertRegex: bool

@typing.type_check_only
class PushFilter(typing_extensions.TypedDict, total=False):
    branch: str
    invertRegex: bool
    tag: str

@typing.type_check_only
class ReceiveTriggerWebhookResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RepoSource(typing_extensions.TypedDict, total=False):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    substitutions: dict[str, typing.Any]
    tagName: str

@typing.type_check_only
class Results(typing_extensions.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    images: _list[BuiltImage]
    numArtifacts: str

@typing.type_check_only
class RetryBuildRequest(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    projectId: str

@typing.type_check_only
class RunBuildTriggerRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    source: RepoSource
    triggerId: str

@typing.type_check_only
class SMTPDelivery(typing_extensions.TypedDict, total=False):
    fromAddress: str
    password: NotifierSecretRef
    port: str
    recipientAddresses: _list[str]
    senderAddress: str
    server: str

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: dict[str, typing.Any]

@typing.type_check_only
class SecretManagerSecret(typing_extensions.TypedDict, total=False):
    env: str
    versionName: str

@typing.type_check_only
class Secrets(typing_extensions.TypedDict, total=False):
    inline: _list[InlineSecret]
    secretManager: _list[SecretManagerSecret]

@typing.type_check_only
class SlackDelivery(typing_extensions.TypedDict, total=False):
    webhookUri: NotifierSecretRef

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    repoSource: RepoSource
    storageSource: StorageSource
    storageSourceManifest: StorageSourceManifest

@typing.type_check_only
class SourceProvenance(typing_extensions.TypedDict, total=False):
    fileHashes: dict[str, typing.Any]
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource
    resolvedStorageSourceManifest: StorageSourceManifest

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class StorageSourceManifest(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class TimeSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateGitHubEnterpriseConfigOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class UpdateWorkerPoolOperationMetadata(typing_extensions.TypedDict, total=False):
    completeTime: str
    createTime: str
    workerPool: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class Warning(typing_extensions.TypedDict, total=False):
    priority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "INFO", "WARNING", "ALERT"
    ]
    text: str

@typing.type_check_only
class WebhookConfig(typing_extensions.TypedDict, total=False):
    secret: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "OK", "SECRET_DELETED"]

@typing.type_check_only
class WorkerConfig(typing_extensions.TypedDict, total=False):
    diskSizeGb: str
    machineType: str

@typing.type_check_only
class WorkerPool(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    name: str
    privatePoolV1Config: PrivatePoolV1Config
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "DELETING", "DELETED"
    ]
    uid: str
    updateTime: str
