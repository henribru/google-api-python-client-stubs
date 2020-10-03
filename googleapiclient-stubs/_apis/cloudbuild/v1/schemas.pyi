import typing

import typing_extensions

class ListBuildsResponse(typing_extensions.TypedDict, total=False):
    builds: typing.List[Build]
    nextPageToken: str

class NotifierConfig(typing_extensions.TypedDict, total=False):
    spec: NotifierSpec
    apiVersion: str
    metadata: NotifierMetadata
    kind: str

class TimeSpan(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class BuildOptions(typing_extensions.TypedDict, total=False):
    secretEnv: typing.List[str]
    machineType: typing_extensions.Literal[
        "UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32"
    ]
    diskSizeGb: str
    requestedVerifyOption: typing_extensions.Literal["NOT_VERIFIED", "VERIFIED"]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    env: typing.List[str]
    volumes: typing.List[Volume]
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
    workerPool: str
    dynamicSubstitutions: bool
    sourceProvenanceHash: typing.List[str]

class Artifacts(typing_extensions.TypedDict, total=False):
    objects: ArtifactObjects
    images: typing.List[str]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class NotifierSpec(typing_extensions.TypedDict, total=False):
    notification: Notification
    secrets: typing.List[NotifierSecret]

class SlackDelivery(typing_extensions.TypedDict, total=False):
    webhookUri: NotifierSecretRef

class Build(typing_extensions.TypedDict, total=False):
    secrets: typing.List[Secret]
    images: typing.List[str]
    statusDetail: str
    timeout: str
    projectId: str
    startTime: str
    results: Results
    queueTtl: str
    logsBucket: str
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
    substitutions: typing.Dict[str, typing.Any]
    options: BuildOptions
    createTime: str
    steps: typing.List[BuildStep]
    source: Source
    serviceAccount: str
    id: str
    finishTime: str
    logUrl: str
    sourceProvenance: SourceProvenance
    timing: typing.Dict[str, typing.Any]
    artifacts: Artifacts
    tags: typing.List[str]
    buildTriggerId: str

class Results(typing_extensions.TypedDict, total=False):
    images: typing.List[BuiltImage]
    artifactManifest: str
    numArtifacts: str
    buildStepImages: typing.List[str]
    buildStepOutputs: typing.List[str]
    artifactTiming: TimeSpan

class NotifierSecret(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class BuildStep(typing_extensions.TypedDict, total=False):
    env: typing.List[str]
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
    timeout: str
    timing: TimeSpan
    pullTiming: TimeSpan
    secretEnv: typing.List[str]
    entrypoint: str
    args: typing.List[str]
    dir: str
    volumes: typing.List[Volume]
    name: str
    waitFor: typing.List[str]
    id: str

class PushFilter(typing_extensions.TypedDict, total=False):
    branch: str
    invertRegex: bool
    tag: str

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]
    error: Status

class NotifierMetadata(typing_extensions.TypedDict, total=False):
    notifier: str
    name: str

class Source(typing_extensions.TypedDict, total=False):
    repoSource: RepoSource
    storageSource: StorageSource

class GitHubEventsConfig(typing_extensions.TypedDict, total=False):
    name: str
    pullRequest: PullRequestFilter
    push: PushFilter
    installationId: str
    owner: str

class CancelBuildRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    name: str
    id: str

class StorageSource(typing_extensions.TypedDict, total=False):
    object: str
    generation: str
    bucket: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

class ArtifactResult(typing_extensions.TypedDict, total=False):
    location: str
    fileHash: typing.List[FileHashes]

class Notification(typing_extensions.TypedDict, total=False):
    structDelivery: typing.Dict[str, typing.Any]
    httpDelivery: HTTPDelivery
    filter: str
    slackDelivery: SlackDelivery
    smtpDelivery: SMTPDelivery

class PullRequestFilter(typing_extensions.TypedDict, total=False):
    branch: str
    commentControl: typing_extensions.Literal[
        "COMMENTS_DISABLED",
        "COMMENTS_ENABLED",
        "COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY",
    ]
    invertRegex: bool

class Volume(typing_extensions.TypedDict, total=False):
    path: str
    name: str

class BuildTrigger(typing_extensions.TypedDict, total=False):
    triggerTemplate: RepoSource
    build: Build
    disabled: bool
    name: str
    description: str
    ignoredFiles: typing.List[str]
    github: GitHubEventsConfig
    includedFiles: typing.List[str]
    id: str
    tags: typing.List[str]
    filename: str
    substitutions: typing.Dict[str, typing.Any]
    createTime: str

class Secret(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: typing.Dict[str, typing.Any]

class SMTPDelivery(typing_extensions.TypedDict, total=False):
    server: str
    fromAddress: str
    password: NotifierSecretRef
    recipientAddresses: typing.List[str]
    senderAddress: str
    port: str

class BuildOperationMetadata(typing_extensions.TypedDict, total=False):
    build: Build

class ListBuildTriggersResponse(typing_extensions.TypedDict, total=False):
    triggers: typing.List[BuildTrigger]
    nextPageToken: str

class RetryBuildRequest(typing_extensions.TypedDict, total=False):
    name: str
    projectId: str
    id: str

class BuiltImage(typing_extensions.TypedDict, total=False):
    name: str
    pushTiming: TimeSpan
    digest: str

class ArtifactObjects(typing_extensions.TypedDict, total=False):
    location: str
    paths: typing.List[str]
    timing: TimeSpan

class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["NONE", "SHA256", "MD5"]
    value: str

class HTTPDelivery(typing_extensions.TypedDict, total=False):
    uri: str

class Empty(typing_extensions.TypedDict, total=False): ...

class RepoSource(typing_extensions.TypedDict, total=False):
    dir: str
    substitutions: typing.Dict[str, typing.Any]
    commitSha: str
    invertRegex: bool
    branchName: str
    projectId: str
    tagName: str
    repoName: str

class SourceProvenance(typing_extensions.TypedDict, total=False):
    resolvedRepoSource: RepoSource
    fileHashes: typing.Dict[str, typing.Any]
    resolvedStorageSource: StorageSource

class NotifierSecretRef(typing_extensions.TypedDict, total=False):
    secretRef: str
