import typing

import typing_extensions
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
    artifacts: Artifacts
    availableSecrets: Secrets
    buildTriggerId: str
    createTime: str
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
    secretEnv: typing.List[str]
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
    volumes: typing.List[Volume]
    waitFor: typing.List[str]

@typing.type_check_only
class BuildTrigger(typing_extensions.TypedDict, total=False):
    build: Build
    createTime: str
    description: str
    disabled: bool
    filename: str
    github: GitHubEventsConfig
    id: str
    ignoredFiles: typing.List[str]
    includedFiles: typing.List[str]
    name: str
    substitutions: typing.Dict[str, typing.Any]
    tags: typing.List[str]
    triggerTemplate: RepoSource

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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

@typing.type_check_only
class GitHubEventsConfig(typing_extensions.TypedDict, total=False):
    installationId: str
    name: str
    owner: str
    pullRequest: PullRequestFilter
    push: PushFilter

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
    extensions: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class InlineSecret(typing_extensions.TypedDict, total=False):
    envMap: typing.Dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ListBuildTriggersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    triggers: typing.List[BuildTrigger]

@typing.type_check_only
class ListBuildsResponse(typing_extensions.TypedDict, total=False):
    builds: typing.List[Build]
    nextPageToken: str

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
class RetryBuildRequest(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    projectId: str

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

@typing.type_check_only
class SourceProvenance(typing_extensions.TypedDict, total=False):
    fileHashes: typing.Dict[str, typing.Any]
    resolvedRepoSource: RepoSource
    resolvedStorageSource: StorageSource

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
class TimeSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    name: str
    path: str
