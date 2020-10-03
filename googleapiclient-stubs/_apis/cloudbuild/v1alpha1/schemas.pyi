import typing

import typing_extensions

class RepoSource(typing_extensions.TypedDict, total=False):
    dir: str
    tagName: str
    branchName: str
    substitutions: typing.Dict[str, typing.Any]
    commitSha: str
    invertRegex: bool
    repoName: str
    projectId: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    name: str

class BuiltImage(typing_extensions.TypedDict, total=False):
    pushTiming: TimeSpan
    name: str
    digest: str

class Secret(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: typing.Dict[str, typing.Any]

class WorkerConfig(typing_extensions.TypedDict, total=False):
    machineType: str
    diskSizeGb: str
    tag: str
    network: Network

class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

class Notification(typing_extensions.TypedDict, total=False):
    smtpDelivery: SMTPDelivery
    structDelivery: typing.Dict[str, typing.Any]
    slackDelivery: SlackDelivery
    httpDelivery: HTTPDelivery
    filter: str

class ListWorkerPoolsResponse(typing_extensions.TypedDict, total=False):
    workerPools: typing.List[WorkerPool]

class SlackDelivery(typing_extensions.TypedDict, total=False):
    webhookUri: NotifierSecretRef

class NotifierConfig(typing_extensions.TypedDict, total=False):
    kind: str
    spec: NotifierSpec
    metadata: NotifierMetadata
    apiVersion: str

class NotifierSecret(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class BuildOptions(typing_extensions.TypedDict, total=False):
    machineType: typing_extensions.Literal[
        "UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32"
    ]
    sourceProvenanceHash: typing.List[str]
    logStreamingOption: typing_extensions.Literal[
        "STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"
    ]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    requestedVerifyOption: typing_extensions.Literal["NOT_VERIFIED", "VERIFIED"]
    env: typing.List[str]
    dynamicSubstitutions: bool
    diskSizeGb: str
    volumes: typing.List[Volume]
    workerPool: str
    secretEnv: typing.List[str]
    logging: typing_extensions.Literal[
        "LOGGING_UNSPECIFIED",
        "LEGACY",
        "GCS_ONLY",
        "STACKDRIVER_ONLY",
        "CLOUD_LOGGING_ONLY",
        "NONE",
    ]

class BuildStep(typing_extensions.TypedDict, total=False):
    secretEnv: typing.List[str]
    volumes: typing.List[Volume]
    timeout: str
    pullTiming: TimeSpan
    args: typing.List[str]
    env: typing.List[str]
    timing: TimeSpan
    name: str
    entrypoint: str
    dir: str
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
    waitFor: typing.List[str]
    id: str

class Build(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    timeout: str
    buildTriggerId: str
    logsBucket: str
    logUrl: str
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
    sourceProvenance: SourceProvenance
    images: typing.List[str]
    timing: typing.Dict[str, typing.Any]
    finishTime: str
    steps: typing.List[BuildStep]
    queueTtl: str
    artifacts: Artifacts
    id: str
    secrets: typing.List[Secret]
    statusDetail: str
    startTime: str
    substitutions: typing.Dict[str, typing.Any]
    name: str
    tags: typing.List[str]
    options: BuildOptions
    createTime: str
    results: Results
    projectId: str
    source: Source

class StorageSource(typing_extensions.TypedDict, total=False):
    generation: str
    object: str
    bucket: str

class Network(typing_extensions.TypedDict, total=False):
    projectId: str
    network: str
    subnetwork: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class WorkerPool(typing_extensions.TypedDict, total=False):
    workerCount: str
    workerConfig: WorkerConfig
    updateTime: str
    projectId: str
    name: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "CREATING", "RUNNING", "DELETING", "DELETED"
    ]
    serviceAccountEmail: str
    regions: typing.List[str]
    createTime: str
    deleteTime: str

class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["NONE", "SHA256", "MD5"]
    value: str

class Results(typing_extensions.TypedDict, total=False):
    buildStepOutputs: typing.List[str]
    numArtifacts: str
    images: typing.List[BuiltImage]
    artifactTiming: TimeSpan
    buildStepImages: typing.List[str]
    artifactManifest: str

class Empty(typing_extensions.TypedDict, total=False): ...

class TimeSpan(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class Artifacts(typing_extensions.TypedDict, total=False):
    images: typing.List[str]
    objects: ArtifactObjects

class HTTPDelivery(typing_extensions.TypedDict, total=False):
    uri: str

class Source(typing_extensions.TypedDict, total=False):
    storageSource: StorageSource
    repoSource: RepoSource

class NotifierMetadata(typing_extensions.TypedDict, total=False):
    name: str
    notifier: str

class Volume(typing_extensions.TypedDict, total=False):
    path: str
    name: str

class NotifierSpec(typing_extensions.TypedDict, total=False):
    secrets: typing.List[NotifierSecret]
    notification: Notification

class NotifierSecretRef(typing_extensions.TypedDict, total=False):
    secretRef: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class SourceProvenance(typing_extensions.TypedDict, total=False):
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource
    fileHashes: typing.Dict[str, typing.Any]

class SMTPDelivery(typing_extensions.TypedDict, total=False):
    recipientAddresses: typing.List[str]
    server: str
    senderAddress: str
    fromAddress: str
    password: NotifierSecretRef
    port: str

class ArtifactObjects(typing_extensions.TypedDict, total=False):
    location: str
    paths: typing.List[str]
    timing: TimeSpan

class BuildOperationMetadata(typing_extensions.TypedDict, total=False):
    build: Build

class ArtifactResult(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[FileHashes]
    location: str
