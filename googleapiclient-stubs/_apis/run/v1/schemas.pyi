import typing

import typing_extensions

_list = list

@typing.type_check_only
class Addressable(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CSIVolumeSource(typing_extensions.TypedDict, total=False):
    driver: str
    readOnly: bool
    volumeAttributes: dict[str, typing.Any]

@typing.type_check_only
class CancelExecutionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConfigMapEnvSource(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapKeySelector(typing_extensions.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapVolumeSource(typing_extensions.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    name: str
    optional: bool

@typing.type_check_only
class Configuration(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ConfigurationSpec
    status: ConfigurationStatus

@typing.type_check_only
class ConfigurationSpec(typing_extensions.TypedDict, total=False):
    template: RevisionTemplate

@typing.type_check_only
class ConfigurationStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[EnvVar]
    envFrom: _list[EnvFromSource]
    image: str
    imagePullPolicy: str
    livenessProbe: Probe
    name: str
    ports: _list[ContainerPort]
    readinessProbe: Probe
    resources: ResourceRequirements
    securityContext: SecurityContext
    startupProbe: Probe
    terminationMessagePath: str
    terminationMessagePolicy: str
    volumeMounts: _list[VolumeMount]
    workingDir: str

@typing.type_check_only
class ContainerOverride(typing_extensions.TypedDict, total=False):
    args: _list[str]
    clearArgs: bool
    env: _list[EnvVar]
    name: str

@typing.type_check_only
class ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    name: str
    protocol: str

@typing.type_check_only
class DomainMapping(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: DomainMappingSpec
    status: DomainMappingStatus

@typing.type_check_only
class DomainMappingSpec(typing_extensions.TypedDict, total=False):
    certificateMode: typing_extensions.Literal[
        "CERTIFICATE_MODE_UNSPECIFIED", "NONE", "AUTOMATIC"
    ]
    forceOverride: bool
    routeName: str

@typing.type_check_only
class DomainMappingStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    mappedRouteName: str
    observedGeneration: int
    resourceRecords: _list[ResourceRecord]
    url: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EmptyDirVolumeSource(typing_extensions.TypedDict, total=False):
    medium: str
    sizeLimit: str

@typing.type_check_only
class EnvFromSource(typing_extensions.TypedDict, total=False):
    configMapRef: ConfigMapEnvSource
    prefix: str
    secretRef: SecretEnvSource

@typing.type_check_only
class EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    valueFrom: EnvVarSource

@typing.type_check_only
class EnvVarSource(typing_extensions.TypedDict, total=False):
    configMapKeyRef: ConfigMapKeySelector
    secretKeyRef: SecretKeySelector

@typing.type_check_only
class ExecAction(typing_extensions.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ExecutionSpec
    status: ExecutionStatus

@typing.type_check_only
class ExecutionReference(typing_extensions.TypedDict, total=False):
    completionStatus: typing_extensions.Literal[
        "COMPLETION_STATUS_UNSPECIFIED",
        "EXECUTION_SUCCEEDED",
        "EXECUTION_FAILED",
        "EXECUTION_RUNNING",
        "EXECUTION_PENDING",
        "EXECUTION_CANCELLED",
    ]
    completionTimestamp: str
    creationTimestamp: str
    deletionTimestamp: str
    name: str

@typing.type_check_only
class ExecutionSpec(typing_extensions.TypedDict, total=False):
    parallelism: int
    taskCount: int
    template: TaskTemplateSpec

@typing.type_check_only
class ExecutionStatus(typing_extensions.TypedDict, total=False):
    cancelledCount: int
    completionTime: str
    conditions: _list[GoogleCloudRunV1Condition]
    failedCount: int
    logUri: str
    observedGeneration: int
    retriedCount: int
    runningCount: int
    startTime: str
    succeededCount: int

@typing.type_check_only
class ExecutionTemplateSpec(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: ExecutionSpec

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GRPCAction(typing_extensions.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudRunV1Condition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ApprovalConfig(
    typing_extensions.TypedDict, total=False
):
    approvalRequired: bool

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ApprovalResult(
    typing_extensions.TypedDict, total=False
):
    approvalTime: str
    approverAccount: str
    comment: str
    decision: typing_extensions.Literal["DECISION_UNSPECIFIED", "APPROVED", "REJECTED"]
    url: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ArtifactObjects(
    typing_extensions.TypedDict, total=False
):
    location: str
    paths: _list[str]
    timing: GoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Artifacts(typing_extensions.TypedDict, total=False):
    images: _list[str]
    mavenArtifacts: _list[GoogleDevtoolsCloudbuildV1MavenArtifact]
    npmPackages: _list[GoogleDevtoolsCloudbuildV1NpmPackage]
    objects: GoogleDevtoolsCloudbuildV1ArtifactObjects
    pythonPackages: _list[GoogleDevtoolsCloudbuildV1PythonPackage]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Build(typing_extensions.TypedDict, total=False):
    approval: GoogleDevtoolsCloudbuildV1BuildApproval
    artifacts: GoogleDevtoolsCloudbuildV1Artifacts
    availableSecrets: GoogleDevtoolsCloudbuildV1Secrets
    buildTriggerId: str
    createTime: str
    failureInfo: GoogleDevtoolsCloudbuildV1FailureInfo
    finishTime: str
    gitConfig: GoogleDevtoolsCloudbuildV1GitConfig
    id: str
    images: _list[str]
    logUrl: str
    logsBucket: str
    name: str
    options: GoogleDevtoolsCloudbuildV1BuildOptions
    projectId: str
    queueTtl: str
    results: GoogleDevtoolsCloudbuildV1Results
    secrets: _list[GoogleDevtoolsCloudbuildV1Secret]
    serviceAccount: str
    source: GoogleDevtoolsCloudbuildV1Source
    sourceProvenance: GoogleDevtoolsCloudbuildV1SourceProvenance
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
    steps: _list[GoogleDevtoolsCloudbuildV1BuildStep]
    substitutions: dict[str, typing.Any]
    tags: _list[str]
    timeout: str
    timing: dict[str, typing.Any]
    warnings: _list[GoogleDevtoolsCloudbuildV1Warning]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildApproval(typing_extensions.TypedDict, total=False):
    config: GoogleDevtoolsCloudbuildV1ApprovalConfig
    result: GoogleDevtoolsCloudbuildV1ApprovalResult
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED", "CANCELLED"
    ]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    build: GoogleDevtoolsCloudbuildV1Build

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildOptions(typing_extensions.TypedDict, total=False):
    automapSubstitutions: bool
    defaultLogsBucketBehavior: typing_extensions.Literal[
        "DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED",
        "REGIONAL_USER_OWNED_BUCKET",
        "LEGACY_BUCKET",
    ]
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
        "UNSPECIFIED",
        "N1_HIGHCPU_8",
        "N1_HIGHCPU_32",
        "E2_HIGHCPU_8",
        "E2_HIGHCPU_32",
        "E2_MEDIUM",
    ]
    pool: GoogleDevtoolsCloudbuildV1PoolOption
    requestedVerifyOption: typing_extensions.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[
        typing_extensions.Literal["NONE", "SHA256", "MD5", "SHA512"]
    ]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[GoogleDevtoolsCloudbuildV1Volume]
    workerPool: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildStep(typing_extensions.TypedDict, total=False):
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
    pullTiming: GoogleDevtoolsCloudbuildV1TimeSpan
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
    timing: GoogleDevtoolsCloudbuildV1TimeSpan
    volumes: _list[GoogleDevtoolsCloudbuildV1Volume]
    waitFor: _list[str]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuiltImage(typing_extensions.TypedDict, total=False):
    digest: str
    name: str
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ConnectedRepository(
    typing_extensions.TypedDict, total=False
):
    dir: str
    repository: str
    revision: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1DeveloperConnectConfig(
    typing_extensions.TypedDict, total=False
):
    dir: str
    gitRepositoryLink: str
    revision: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1FailureInfo(typing_extensions.TypedDict, total=False):
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
class GoogleDevtoolsCloudbuildV1FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: _list[GoogleDevtoolsCloudbuildV1Hash]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GitConfig(typing_extensions.TypedDict, total=False):
    http: GoogleDevtoolsCloudbuildV1HttpConfig

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GitSource(typing_extensions.TypedDict, total=False):
    dir: str
    revision: str
    url: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["NONE", "SHA256", "MD5", "SHA512"]
    value: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1HttpConfig(typing_extensions.TypedDict, total=False):
    proxySecretVersionName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1InlineSecret(typing_extensions.TypedDict, total=False):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1MavenArtifact(typing_extensions.TypedDict, total=False):
    artifactId: str
    groupId: str
    path: str
    repository: str
    version: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1NpmPackage(typing_extensions.TypedDict, total=False):
    packagePath: str
    repository: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1PoolOption(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1PythonPackage(typing_extensions.TypedDict, total=False):
    paths: _list[str]
    repository: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1RepoSource(typing_extensions.TypedDict, total=False):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    substitutions: dict[str, typing.Any]
    tagName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Results(typing_extensions.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    images: _list[GoogleDevtoolsCloudbuildV1BuiltImage]
    mavenArtifacts: _list[GoogleDevtoolsCloudbuildV1UploadedMavenArtifact]
    npmPackages: _list[GoogleDevtoolsCloudbuildV1UploadedNpmPackage]
    numArtifacts: str
    pythonPackages: _list[GoogleDevtoolsCloudbuildV1UploadedPythonPackage]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Secret(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: dict[str, typing.Any]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1SecretManagerSecret(
    typing_extensions.TypedDict, total=False
):
    env: str
    versionName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Secrets(typing_extensions.TypedDict, total=False):
    inline: _list[GoogleDevtoolsCloudbuildV1InlineSecret]
    secretManager: _list[GoogleDevtoolsCloudbuildV1SecretManagerSecret]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Source(typing_extensions.TypedDict, total=False):
    connectedRepository: GoogleDevtoolsCloudbuildV1ConnectedRepository
    developerConnectConfig: GoogleDevtoolsCloudbuildV1DeveloperConnectConfig
    gitSource: GoogleDevtoolsCloudbuildV1GitSource
    repoSource: GoogleDevtoolsCloudbuildV1RepoSource
    storageSource: GoogleDevtoolsCloudbuildV1StorageSource
    storageSourceManifest: GoogleDevtoolsCloudbuildV1StorageSourceManifest

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1SourceProvenance(
    typing_extensions.TypedDict, total=False
):
    fileHashes: dict[str, typing.Any]
    resolvedConnectedRepository: GoogleDevtoolsCloudbuildV1ConnectedRepository
    resolvedGitSource: GoogleDevtoolsCloudbuildV1GitSource
    resolvedRepoSource: GoogleDevtoolsCloudbuildV1RepoSource
    resolvedStorageSource: GoogleDevtoolsCloudbuildV1StorageSource
    resolvedStorageSourceManifest: GoogleDevtoolsCloudbuildV1StorageSourceManifest

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str
    sourceFetcher: typing_extensions.Literal[
        "SOURCE_FETCHER_UNSPECIFIED", "GSUTIL", "GCS_FETCHER"
    ]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1StorageSourceManifest(
    typing_extensions.TypedDict, total=False
):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1TimeSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedMavenArtifact(
    typing_extensions.TypedDict, total=False
):
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedNpmPackage(
    typing_extensions.TypedDict, total=False
):
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedPythonPackage(
    typing_extensions.TypedDict, total=False
):
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Volume(typing_extensions.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Warning(typing_extensions.TypedDict, total=False):
    priority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "INFO", "WARNING", "ALERT"
    ]
    text: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleLongrunningWaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HTTPGetAction(typing_extensions.TypedDict, total=False):
    host: str
    httpHeaders: _list[HTTPHeader]
    path: str
    port: int
    scheme: str

@typing.type_check_only
class HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: JobSpec
    status: JobStatus

@typing.type_check_only
class JobSpec(typing_extensions.TypedDict, total=False):
    runExecutionToken: str
    startExecutionToken: str
    template: ExecutionTemplateSpec

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    executionCount: int
    latestCreatedExecution: ExecutionReference
    observedGeneration: int

@typing.type_check_only
class KeyToPath(typing_extensions.TypedDict, total=False):
    key: str
    mode: int
    path: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Configuration]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[DomainMapping]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Execution]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Job]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

AlternativeListMeta = typing_extensions.TypedDict(
    "AlternativeListMeta",
    {
        "continue": str,
        "resourceVersion": str,
        "selfLink": str,
    },
    total=False,
)

@typing.type_check_only
class ListMeta(AlternativeListMeta): ...

@typing.type_check_only
class ListRevisionsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Revision]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Route]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Service]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListTasksResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Task]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class LocalObjectReference(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NFSVolumeSource(typing_extensions.TypedDict, total=False):
    path: str
    readOnly: bool
    server: str

@typing.type_check_only
class ObjectMeta(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clusterName: str
    creationTimestamp: str
    deletionGracePeriodSeconds: int
    deletionTimestamp: str
    finalizers: _list[str]
    generateName: str
    generation: int
    labels: dict[str, typing.Any]
    name: str
    namespace: str
    ownerReferences: _list[OwnerReference]
    resourceVersion: str
    selfLink: str
    uid: str

@typing.type_check_only
class Overrides(typing_extensions.TypedDict, total=False):
    containerOverrides: _list[ContainerOverride]
    taskCount: int
    timeoutSeconds: int

@typing.type_check_only
class OwnerReference(typing_extensions.TypedDict, total=False):
    apiVersion: str
    blockOwnerDeletion: bool
    controller: bool
    kind: str
    name: str
    uid: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Probe(typing_extensions.TypedDict, total=False):
    exec: ExecAction
    failureThreshold: int
    grpc: GRPCAction
    httpGet: HTTPGetAction
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: TCPSocketAction
    timeoutSeconds: int

@typing.type_check_only
class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]

@typing.type_check_only
class ResourceRequirements(typing_extensions.TypedDict, total=False):
    limits: dict[str, typing.Any]
    requests: dict[str, typing.Any]

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RevisionSpec
    status: RevisionStatus

@typing.type_check_only
class RevisionSpec(typing_extensions.TypedDict, total=False):
    containerConcurrency: int
    containers: _list[Container]
    enableServiceLinks: bool
    imagePullSecrets: _list[LocalObjectReference]
    nodeSelector: dict[str, typing.Any]
    runtimeClassName: str
    serviceAccountName: str
    timeoutSeconds: int
    volumes: _list[Volume]

@typing.type_check_only
class RevisionStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    desiredReplicas: int
    imageDigest: str
    logUrl: str
    observedGeneration: int
    serviceName: str

@typing.type_check_only
class RevisionTemplate(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: RevisionSpec

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RouteSpec
    status: RouteStatus

@typing.type_check_only
class RouteSpec(typing_extensions.TypedDict, total=False):
    traffic: _list[TrafficTarget]

@typing.type_check_only
class RouteStatus(typing_extensions.TypedDict, total=False):
    address: Addressable
    conditions: _list[GoogleCloudRunV1Condition]
    observedGeneration: int
    traffic: _list[TrafficTarget]
    url: str

@typing.type_check_only
class RunJobRequest(typing_extensions.TypedDict, total=False):
    overrides: Overrides

@typing.type_check_only
class SecretEnvSource(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretKeySelector(typing_extensions.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretVolumeSource(typing_extensions.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    optional: bool
    secretName: str

@typing.type_check_only
class SecurityContext(typing_extensions.TypedDict, total=False):
    runAsUser: int

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ServiceSpec
    status: ServiceStatus

@typing.type_check_only
class ServiceSpec(typing_extensions.TypedDict, total=False):
    template: RevisionTemplate
    traffic: _list[TrafficTarget]

@typing.type_check_only
class ServiceStatus(typing_extensions.TypedDict, total=False):
    address: Addressable
    conditions: _list[GoogleCloudRunV1Condition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int
    traffic: _list[TrafficTarget]
    url: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: StatusDetails
    message: str
    metadata: ListMeta
    reason: str
    status: str

@typing.type_check_only
class StatusCause(typing_extensions.TypedDict, total=False):
    field: str
    message: str
    reason: str

@typing.type_check_only
class StatusDetails(typing_extensions.TypedDict, total=False):
    causes: _list[StatusCause]
    group: str
    kind: str
    name: str
    retryAfterSeconds: int
    uid: str

@typing.type_check_only
class TCPSocketAction(typing_extensions.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: TaskSpec
    status: TaskStatus

@typing.type_check_only
class TaskAttemptResult(typing_extensions.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus

@typing.type_check_only
class TaskSpec(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    maxRetries: int
    serviceAccountName: str
    timeoutSeconds: str
    volumes: _list[Volume]

@typing.type_check_only
class TaskStatus(typing_extensions.TypedDict, total=False):
    completionTime: str
    conditions: _list[GoogleCloudRunV1Condition]
    index: int
    lastAttemptResult: TaskAttemptResult
    logUri: str
    observedGeneration: int
    retried: int
    startTime: str

@typing.type_check_only
class TaskTemplateSpec(typing_extensions.TypedDict, total=False):
    spec: TaskSpec

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrafficTarget(typing_extensions.TypedDict, total=False):
    configurationName: str
    latestRevision: bool
    percent: int
    revisionName: str
    tag: str
    url: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    configMap: ConfigMapVolumeSource
    csi: CSIVolumeSource
    emptyDir: EmptyDirVolumeSource
    name: str
    nfs: NFSVolumeSource
    secret: SecretVolumeSource

@typing.type_check_only
class VolumeMount(typing_extensions.TypedDict, total=False):
    mountPath: str
    name: str
    readOnly: bool
    subPath: str
