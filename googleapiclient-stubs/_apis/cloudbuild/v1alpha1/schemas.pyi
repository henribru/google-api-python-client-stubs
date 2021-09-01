import typing

import typing_extensions

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
class ArtifactObjects(typing_extensions.TypedDict, total=False):
    location: str
    paths: typing.List[str]
    timing: TimeSpan

@typing.type_check_only
class ArtifactResult(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[FileHashes]
    location: str

@typing.type_check_only
class Artifacts(typing_extensions.TypedDict, total=False):
    images: typing.List[str]
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
    images: typing.List[str]
    logUrl: str
    logsBucket: str
    name: str
    options: BuildOptions
    projectId: str
    queueTtl: str
    results: Results
    secrets: typing.List[Secret]
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
    steps: typing.List[BuildStep]
    substitutions: typing.Dict[str, typing.Any]
    tags: typing.List[str]
    timeout: str
    timing: typing.Dict[str, typing.Any]
    warnings: typing.List[Warning]

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
    env: typing.List[str]
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
    secretEnv: typing.List[str]
    sourceProvenanceHash: typing.List[str]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: typing.List[Volume]
    workerPool: str

@typing.type_check_only
class BuildStep(typing_extensions.TypedDict, total=False):
    args: typing.List[str]
    dir: str
    entrypoint: str
    env: typing.List[str]
    id: str
    name: str
    pullTiming: TimeSpan
    script: str
    secretEnv: typing.List[str]
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
    volumes: typing.List[Volume]
    waitFor: typing.List[str]

@typing.type_check_only
class BuiltImage(typing_extensions.TypedDict, total=False):
    digest: str
    name: str
    pushTiming: TimeSpan

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
    fileHash: typing.List[Hash]

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
class InlineSecret(typing_extensions.TypedDict, total=False):
    envMap: typing.Dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ListWorkerPoolsResponse(typing_extensions.TypedDict, total=False):
    workerPools: typing.List[WorkerPool]

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    network: str
    projectId: str
    subnetwork: str

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    filter: str
    httpDelivery: HTTPDelivery
    slackDelivery: SlackDelivery
    smtpDelivery: SMTPDelivery
    structDelivery: typing.Dict[str, typing.Any]

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
    secrets: typing.List[NotifierSecret]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
class ProcessAppManifestCallbackOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    completeTime: str
    createTime: str
    githubEnterpriseConfig: str

@typing.type_check_only
class RepoSource(typing_extensions.TypedDict, total=False):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    substitutions: typing.Dict[str, typing.Any]
    tagName: str

@typing.type_check_only
class Results(typing_extensions.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: TimeSpan
    buildStepImages: typing.List[str]
    buildStepOutputs: typing.List[str]
    images: typing.List[BuiltImage]
    numArtifacts: str

@typing.type_check_only
class SMTPDelivery(typing_extensions.TypedDict, total=False):
    fromAddress: str
    password: NotifierSecretRef
    port: str
    recipientAddresses: typing.List[str]
    senderAddress: str
    server: str

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: typing.Dict[str, typing.Any]

@typing.type_check_only
class SecretManagerSecret(typing_extensions.TypedDict, total=False):
    env: str
    versionName: str

@typing.type_check_only
class Secrets(typing_extensions.TypedDict, total=False):
    inline: typing.List[InlineSecret]
    secretManager: typing.List[SecretManagerSecret]

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
    fileHashes: typing.Dict[str, typing.Any]
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource
    resolvedStorageSourceManifest: StorageSourceManifest

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
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
class WorkerConfig(typing_extensions.TypedDict, total=False):
    diskSizeGb: str
    machineType: str
    network: Network
    tag: str

@typing.type_check_only
class WorkerPool(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    name: str
    projectId: str
    regions: typing.List[str]
    serviceAccountEmail: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "CREATING", "RUNNING", "DELETING", "DELETED"
    ]
    updateTime: str
    workerConfig: WorkerConfig
    workerCount: str
