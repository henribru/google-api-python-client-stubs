import typing

import typing_extensions

class HTTPDelivery(typing_extensions.TypedDict, total=False):
    uri: str

class ArtifactResult(typing_extensions.TypedDict, total=False):
    location: str
    fileHash: typing.List[FileHashes]

class NotifierMetadata(typing_extensions.TypedDict, total=False):
    notifier: str
    name: str

class ListWorkerPoolsResponse(typing_extensions.TypedDict, total=False):
    workerPools: typing.List[WorkerPool]

class NotifierConfig(typing_extensions.TypedDict, total=False):
    kind: str
    metadata: NotifierMetadata
    apiVersion: str
    spec: NotifierSpec

class NetworkConfig(typing_extensions.TypedDict, total=False):
    peeredNetwork: str

class BuildOptions(typing_extensions.TypedDict, total=False):
    volumes: typing.List[Volume]
    sourceProvenanceHash: typing.List[str]
    secretEnv: typing.List[str]
    dynamicSubstitutions: bool
    env: typing.List[str]
    logging: typing_extensions.Literal[
        "LOGGING_UNSPECIFIED",
        "LEGACY",
        "GCS_ONLY",
        "STACKDRIVER_ONLY",
        "CLOUD_LOGGING_ONLY",
        "NONE",
    ]
    requestedVerifyOption: typing_extensions.Literal["NOT_VERIFIED", "VERIFIED"]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    logStreamingOption: typing_extensions.Literal[
        "STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"
    ]
    workerPool: str
    diskSizeGb: str
    machineType: typing_extensions.Literal[
        "UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32"
    ]

class ArtifactObjects(typing_extensions.TypedDict, total=False):
    paths: typing.List[str]
    location: str
    timing: TimeSpan

class BuiltImage(typing_extensions.TypedDict, total=False):
    name: str
    pushTiming: TimeSpan
    digest: str

class StorageSource(typing_extensions.TypedDict, total=False):
    object: str
    generation: str
    bucket: str

class SMTPDelivery(typing_extensions.TypedDict, total=False):
    password: NotifierSecretRef
    recipientAddresses: typing.List[str]
    senderAddress: str
    fromAddress: str
    server: str
    port: str

class Hash(typing_extensions.TypedDict, total=False):
    value: str
    type: typing_extensions.Literal["NONE", "SHA256", "MD5"]

class SlackDelivery(typing_extensions.TypedDict, total=False):
    webhookUri: NotifierSecretRef

class TimeSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class WorkerConfig(typing_extensions.TypedDict, total=False):
    machineType: str
    diskSizeGb: str

class Notification(typing_extensions.TypedDict, total=False):
    slackDelivery: SlackDelivery
    structDelivery: typing.Dict[str, typing.Any]
    filter: str
    httpDelivery: HTTPDelivery
    smtpDelivery: SMTPDelivery

class Empty(typing_extensions.TypedDict, total=False): ...

class NotifierSpec(typing_extensions.TypedDict, total=False):
    secrets: typing.List[NotifierSecret]
    notification: Notification

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class RepoSource(typing_extensions.TypedDict, total=False):
    tagName: str
    projectId: str
    repoName: str
    substitutions: typing.Dict[str, typing.Any]
    commitSha: str
    branchName: str
    invertRegex: bool
    dir: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class BuildStep(typing_extensions.TypedDict, total=False):
    pullTiming: TimeSpan
    name: str
    timing: TimeSpan
    timeout: str
    id: str
    env: typing.List[str]
    secretEnv: typing.List[str]
    args: typing.List[str]
    dir: str
    waitFor: typing.List[str]
    volumes: typing.List[Volume]
    entrypoint: str
    status: typing_extensions.Literal[
        "STATUS_UNKNOWN",
        "QUEUED",
        "WORKING",
        "SUCCESS",
        "FAILURE",
        "INTERNAL_ERROR",
        "TIMEOUT",
        "CANCELLED",
        "EXPIRED",
    ]

class Artifacts(typing_extensions.TypedDict, total=False):
    objects: ArtifactObjects
    images: typing.List[str]

class NotifierSecretRef(typing_extensions.TypedDict, total=False):
    secretRef: str

class Volume(typing_extensions.TypedDict, total=False):
    name: str
    path: str

class BuildOperationMetadata(typing_extensions.TypedDict, total=False):
    build: Build

class WorkerPool(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RUNNING", "DELETING", "DELETED"
    ]
    networkConfig: NetworkConfig
    name: str
    deleteTime: str
    region: str
    updateTime: str
    createTime: str
    workerConfig: WorkerConfig

class Source(typing_extensions.TypedDict, total=False):
    storageSource: StorageSource
    repoSource: RepoSource

class Secret(typing_extensions.TypedDict, total=False):
    secretEnv: typing.Dict[str, typing.Any]
    kmsKeyName: str

class Results(typing_extensions.TypedDict, total=False):
    numArtifacts: str
    artifactTiming: TimeSpan
    buildStepOutputs: typing.List[str]
    images: typing.List[BuiltImage]
    artifactManifest: str
    buildStepImages: typing.List[str]

class SourceProvenance(typing_extensions.TypedDict, total=False):
    resolvedRepoSource: RepoSource
    fileHashes: typing.Dict[str, typing.Any]
    resolvedStorageSource: StorageSource

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class Build(typing_extensions.TypedDict, total=False):
    timing: typing.Dict[str, typing.Any]
    logsBucket: str
    secrets: typing.List[Secret]
    startTime: str
    tags: typing.List[str]
    status: typing_extensions.Literal[
        "STATUS_UNKNOWN",
        "QUEUED",
        "WORKING",
        "SUCCESS",
        "FAILURE",
        "INTERNAL_ERROR",
        "TIMEOUT",
        "CANCELLED",
        "EXPIRED",
    ]
    name: str
    projectId: str
    options: BuildOptions
    createTime: str
    steps: typing.List[BuildStep]
    queueTtl: str
    finishTime: str
    timeout: str
    sourceProvenance: SourceProvenance
    source: Source
    results: Results
    artifacts: Artifacts
    images: typing.List[str]
    substitutions: typing.Dict[str, typing.Any]
    id: str
    buildTriggerId: str
    logUrl: str
    serviceAccount: str
    statusDetail: str

class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

class NotifierSecret(typing_extensions.TypedDict, total=False):
    value: str
    name: str
