import typing

_list = list

@typing.type_check_only
class Addressable(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthorizedDomain(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CSIVolumeSource(typing.TypedDict, total=False):
    driver: str
    readOnly: bool
    volumeAttributes: dict[str, typing.Any]

@typing.type_check_only
class CancelExecutionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConfigMapEnvSource(typing.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapKeySelector(typing.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapVolumeSource(typing.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    name: str
    optional: bool

@typing.type_check_only
class Configuration(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ConfigurationSpec
    status: ConfigurationStatus

@typing.type_check_only
class ConfigurationSpec(typing.TypedDict, total=False):
    template: RevisionTemplate

@typing.type_check_only
class ConfigurationStatus(typing.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int

@typing.type_check_only
class Container(typing.TypedDict, total=False):
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
    sandboxLauncher: bool
    securityContext: SecurityContext
    startupProbe: Probe
    terminationMessagePath: str
    terminationMessagePolicy: str
    volumeMounts: _list[VolumeMount]
    workingDir: str

@typing.type_check_only
class ContainerOverride(typing.TypedDict, total=False):
    args: _list[str]
    clearArgs: bool
    env: _list[EnvVar]
    name: str

@typing.type_check_only
class ContainerPort(typing.TypedDict, total=False):
    containerPort: int
    name: str
    protocol: str

@typing.type_check_only
class DomainMapping(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: DomainMappingSpec
    status: DomainMappingStatus

@typing.type_check_only
class DomainMappingSpec(typing.TypedDict, total=False):
    certificateMode: typing.Literal["CERTIFICATE_MODE_UNSPECIFIED", "NONE", "AUTOMATIC"]
    forceOverride: bool
    routeName: str

@typing.type_check_only
class DomainMappingStatus(typing.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    mappedRouteName: str
    observedGeneration: int
    resourceRecords: _list[ResourceRecord]
    url: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EmptyDirVolumeSource(typing.TypedDict, total=False):
    medium: str
    sizeLimit: str

@typing.type_check_only
class EnvFromSource(typing.TypedDict, total=False):
    configMapRef: ConfigMapEnvSource
    prefix: str
    secretRef: SecretEnvSource

@typing.type_check_only
class EnvVar(typing.TypedDict, total=False):
    name: str
    value: str
    valueFrom: EnvVarSource

@typing.type_check_only
class EnvVarSource(typing.TypedDict, total=False):
    configMapKeyRef: ConfigMapKeySelector
    secretKeyRef: SecretKeySelector

@typing.type_check_only
class ExecAction(typing.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class Execution(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ExecutionSpec
    status: ExecutionStatus

@typing.type_check_only
class ExecutionReference(typing.TypedDict, total=False):
    completionStatus: typing.Literal[
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
class ExecutionSpec(typing.TypedDict, total=False):
    parallelism: int
    taskCount: int
    template: TaskTemplateSpec

@typing.type_check_only
class ExecutionStatus(typing.TypedDict, total=False):
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
class ExecutionTemplateSpec(typing.TypedDict, total=False):
    metadata: ObjectMeta
    spec: ExecutionSpec

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GRPCAction(typing.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudRunV1Condition(typing.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ApprovalConfig(typing.TypedDict, total=False):
    approvalRequired: bool

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ApprovalResult(typing.TypedDict, total=False):
    approvalTime: str
    approverAccount: str
    comment: str
    decision: typing.Literal["DECISION_UNSPECIFIED", "APPROVED", "REJECTED"]
    url: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ArtifactObjects(typing.TypedDict, total=False):
    location: str
    paths: _list[str]
    timing: GoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Artifacts(typing.TypedDict, total=False):
    genericArtifacts: _list[GoogleDevtoolsCloudbuildV1GenericArtifact]
    goModules: _list[GoogleDevtoolsCloudbuildV1GoModule]
    images: _list[str]
    mavenArtifacts: _list[GoogleDevtoolsCloudbuildV1MavenArtifact]
    npmPackages: _list[GoogleDevtoolsCloudbuildV1NpmPackage]
    objects: GoogleDevtoolsCloudbuildV1ArtifactObjects
    oci: _list[GoogleDevtoolsCloudbuildV1Oci]
    pythonPackages: _list[GoogleDevtoolsCloudbuildV1PythonPackage]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Build(typing.TypedDict, total=False):
    approval: GoogleDevtoolsCloudbuildV1BuildApproval
    artifacts: GoogleDevtoolsCloudbuildV1Artifacts
    availableSecrets: GoogleDevtoolsCloudbuildV1Secrets
    buildTriggerId: str
    createTime: str
    dependencies: _list[GoogleDevtoolsCloudbuildV1Dependency]
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
    steps: _list[GoogleDevtoolsCloudbuildV1BuildStep]
    substitutions: dict[str, typing.Any]
    tags: _list[str]
    timeout: str
    timing: dict[str, typing.Any]
    warnings: _list[GoogleDevtoolsCloudbuildV1Warning]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildApproval(typing.TypedDict, total=False):
    config: GoogleDevtoolsCloudbuildV1ApprovalConfig
    result: GoogleDevtoolsCloudbuildV1ApprovalResult
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED", "CANCELLED"
    ]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildOperationMetadata(typing.TypedDict, total=False):
    build: GoogleDevtoolsCloudbuildV1Build

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildOptions(typing.TypedDict, total=False):
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
    pool: GoogleDevtoolsCloudbuildV1PoolOption
    pubsubTopic: str
    requestedVerifyOption: typing.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[
        typing.Literal[
            "NONE", "SHA256", "MD5", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
        ]
    ]
    substitutionOption: typing.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[GoogleDevtoolsCloudbuildV1Volume]
    workerPool: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildStep(typing.TypedDict, total=False):
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
    results: _list[GoogleDevtoolsCloudbuildV1StepResult]
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
    timing: GoogleDevtoolsCloudbuildV1TimeSpan
    volumes: _list[GoogleDevtoolsCloudbuildV1Volume]
    waitFor: _list[str]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuildStepResults(typing.TypedDict, total=False):
    results: dict[str, typing.Any]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1BuiltImage(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    digest: str
    name: str
    ociMediaType: typing.Literal[
        "OCI_MEDIA_TYPE_UNSPECIFIED", "IMAGE_MANIFEST", "IMAGE_INDEX"
    ]
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1ConnectedRepository(typing.TypedDict, total=False):
    dir: str
    repository: str
    revision: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Dependency(typing.TypedDict, total=False):
    empty: bool
    genericArtifact: GoogleDevtoolsCloudbuildV1GenericArtifactDependency
    gitSource: GoogleDevtoolsCloudbuildV1GitSourceDependency

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1DeveloperConnectConfig(typing.TypedDict, total=False):
    dir: str
    gitRepositoryLink: str
    revision: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1FailureInfo(typing.TypedDict, total=False):
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
class GoogleDevtoolsCloudbuildV1FileHashes(typing.TypedDict, total=False):
    fileHash: _list[GoogleDevtoolsCloudbuildV1Hash]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GenericArtifact(typing.TypedDict, total=False):
    folder: str
    registryPath: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GenericArtifactDependency(
    typing.TypedDict, total=False
):
    destPath: str
    resource: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GitConfig(typing.TypedDict, total=False):
    http: GoogleDevtoolsCloudbuildV1HttpConfig

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GitSource(typing.TypedDict, total=False):
    dir: str
    revision: str
    url: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GitSourceDependency(typing.TypedDict, total=False):
    depth: str
    destPath: str
    recurseSubmodules: bool
    repository: GoogleDevtoolsCloudbuildV1GitSourceRepository
    revision: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GitSourceRepository(typing.TypedDict, total=False):
    developerConnect: str
    url: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1GoModule(typing.TypedDict, total=False):
    modulePath: str
    moduleVersion: str
    repositoryLocation: str
    repositoryName: str
    repositoryProjectId: str
    sourcePath: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Hash(typing.TypedDict, total=False):
    type: typing.Literal[
        "NONE", "SHA256", "MD5", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
    ]
    value: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1HttpConfig(typing.TypedDict, total=False):
    proxySecretVersionName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1InlineSecret(typing.TypedDict, total=False):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1MavenArtifact(typing.TypedDict, total=False):
    artifactId: str
    deployFolder: str
    groupId: str
    path: str
    repository: str
    version: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1NpmPackage(typing.TypedDict, total=False):
    packagePath: str
    repository: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Oci(typing.TypedDict, total=False):
    file: str
    registryPath: str
    tags: _list[str]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1PoolOption(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1PythonPackage(typing.TypedDict, total=False):
    paths: _list[str]
    repository: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1RepoSource(typing.TypedDict, total=False):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    substitutions: dict[str, typing.Any]
    tagName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Results(typing.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    buildStepResults: dict[str, typing.Any]
    genericArtifacts: _list[GoogleDevtoolsCloudbuildV1UploadedGenericArtifact]
    goModules: _list[GoogleDevtoolsCloudbuildV1UploadedGoModule]
    images: _list[GoogleDevtoolsCloudbuildV1BuiltImage]
    mavenArtifacts: _list[GoogleDevtoolsCloudbuildV1UploadedMavenArtifact]
    npmPackages: _list[GoogleDevtoolsCloudbuildV1UploadedNpmPackage]
    numArtifacts: str
    pythonPackages: _list[GoogleDevtoolsCloudbuildV1UploadedPythonPackage]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Secret(typing.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: dict[str, typing.Any]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1SecretManagerSecret(typing.TypedDict, total=False):
    env: str
    versionName: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Secrets(typing.TypedDict, total=False):
    inline: _list[GoogleDevtoolsCloudbuildV1InlineSecret]
    secretManager: _list[GoogleDevtoolsCloudbuildV1SecretManagerSecret]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Source(typing.TypedDict, total=False):
    connectedRepository: GoogleDevtoolsCloudbuildV1ConnectedRepository
    developerConnectConfig: GoogleDevtoolsCloudbuildV1DeveloperConnectConfig
    gitSource: GoogleDevtoolsCloudbuildV1GitSource
    repoSource: GoogleDevtoolsCloudbuildV1RepoSource
    storageSource: GoogleDevtoolsCloudbuildV1StorageSource
    storageSourceManifest: GoogleDevtoolsCloudbuildV1StorageSourceManifest

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1SourceProvenance(typing.TypedDict, total=False):
    fileHashes: dict[str, typing.Any]
    resolvedConnectedRepository: GoogleDevtoolsCloudbuildV1ConnectedRepository
    resolvedGitSource: GoogleDevtoolsCloudbuildV1GitSource
    resolvedRepoSource: GoogleDevtoolsCloudbuildV1RepoSource
    resolvedStorageSource: GoogleDevtoolsCloudbuildV1StorageSource
    resolvedStorageSourceManifest: GoogleDevtoolsCloudbuildV1StorageSourceManifest

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1StepResult(typing.TypedDict, total=False):
    attestationContent: str
    attestationType: str
    name: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1StorageSource(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str
    sourceFetcher: typing.Literal["SOURCE_FETCHER_UNSPECIFIED", "GSUTIL", "GCS_FETCHER"]

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1StorageSourceManifest(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1TimeSpan(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedGenericArtifact(typing.TypedDict, total=False):
    artifactFingerprint: GoogleDevtoolsCloudbuildV1FileHashes
    artifactRegistryPackage: str
    fileHashes: dict[str, typing.Any]
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedGoModule(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedMavenArtifact(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedNpmPackage(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1UploadedPythonPackage(typing.TypedDict, total=False):
    artifactRegistryPackage: str
    fileHashes: GoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: GoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Volume(typing.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class GoogleDevtoolsCloudbuildV1Warning(typing.TypedDict, total=False):
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "INFO", "WARNING", "ALERT"]
    text: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleLongrunningWaitOperationRequest(typing.TypedDict, total=False):
    timeout: str

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HTTPGetAction(typing.TypedDict, total=False):
    host: str
    httpHeaders: _list[HTTPHeader]
    path: str
    port: int
    scheme: str

@typing.type_check_only
class HTTPHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: InstanceSpec
    status: InstanceStatus

@typing.type_check_only
class InstanceSpec(typing.TypedDict, total=False):
    containers: _list[Container]
    nodeSelector: dict[str, typing.Any]
    restartPolicy: str
    serviceAccountName: str
    volumes: _list[Volume]

@typing.type_check_only
class InstanceSplit(typing.TypedDict, total=False):
    latestRevision: bool
    percent: int
    revisionName: str

@typing.type_check_only
class InstanceStatus(typing.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    logUri: str
    observedGeneration: int
    urls: _list[str]

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: JobSpec
    status: JobStatus

@typing.type_check_only
class JobSpec(typing.TypedDict, total=False):
    runExecutionToken: str
    startExecutionToken: str
    template: ExecutionTemplateSpec

@typing.type_check_only
class JobStatus(typing.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    executionCount: int
    latestCreatedExecution: ExecutionReference
    observedGeneration: int

@typing.type_check_only
class KeyToPath(typing.TypedDict, total=False):
    key: str
    mode: int
    path: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListConfigurationsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Configuration]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListDomainMappingsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[DomainMapping]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListExecutionsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Execution]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Instance]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Job]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

AlternativeListMeta = typing.TypedDict(
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
class ListRevisionsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Revision]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListRoutesResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Route]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Service]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListTasksResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Task]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListWorkerPoolsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[WorkerPool]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class LocalObjectReference(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NFSVolumeSource(typing.TypedDict, total=False):
    path: str
    readOnly: bool
    server: str

@typing.type_check_only
class ObjectMeta(typing.TypedDict, total=False):
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
class Overrides(typing.TypedDict, total=False):
    containerOverrides: _list[ContainerOverride]
    taskCount: int
    timeoutSeconds: int

@typing.type_check_only
class OwnerReference(typing.TypedDict, total=False):
    apiVersion: str
    blockOwnerDeletion: bool
    controller: bool
    kind: str
    name: str
    uid: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Probe(typing.TypedDict, total=False):
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
class ResourceRecord(typing.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]

@typing.type_check_only
class ResourceRequirements(typing.TypedDict, total=False):
    limits: dict[str, typing.Any]
    requests: dict[str, typing.Any]

@typing.type_check_only
class Revision(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RevisionSpec
    status: RevisionStatus

@typing.type_check_only
class RevisionSpec(typing.TypedDict, total=False):
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
class RevisionStatus(typing.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    desiredReplicas: int
    imageDigest: str
    logUrl: str
    observedGeneration: int
    serviceName: str

@typing.type_check_only
class RevisionTemplate(typing.TypedDict, total=False):
    metadata: ObjectMeta
    spec: RevisionSpec

@typing.type_check_only
class Route(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RouteSpec
    status: RouteStatus

@typing.type_check_only
class RouteSpec(typing.TypedDict, total=False):
    traffic: _list[TrafficTarget]

@typing.type_check_only
class RouteStatus(typing.TypedDict, total=False):
    address: Addressable
    conditions: _list[GoogleCloudRunV1Condition]
    observedGeneration: int
    traffic: _list[TrafficTarget]
    url: str

@typing.type_check_only
class RunJobRequest(typing.TypedDict, total=False):
    overrides: Overrides

@typing.type_check_only
class SecretEnvSource(typing.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretKeySelector(typing.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretVolumeSource(typing.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    optional: bool
    secretName: str

@typing.type_check_only
class SecurityContext(typing.TypedDict, total=False):
    runAsUser: int

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ServiceSpec
    status: ServiceStatus

@typing.type_check_only
class ServiceSpec(typing.TypedDict, total=False):
    template: RevisionTemplate
    traffic: _list[TrafficTarget]

@typing.type_check_only
class ServiceStatus(typing.TypedDict, total=False):
    address: Addressable
    conditions: _list[GoogleCloudRunV1Condition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int
    traffic: _list[TrafficTarget]
    url: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class StartInstanceRequest(typing.TypedDict, total=False):
    dryRun: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: StatusDetails
    message: str
    metadata: ListMeta
    reason: str
    status: str

@typing.type_check_only
class StatusCause(typing.TypedDict, total=False):
    field: str
    message: str
    reason: str

@typing.type_check_only
class StatusDetails(typing.TypedDict, total=False):
    causes: _list[StatusCause]
    group: str
    kind: str
    name: str
    retryAfterSeconds: int
    uid: str

@typing.type_check_only
class StopInstanceRequest(typing.TypedDict, total=False):
    dryRun: str

@typing.type_check_only
class TCPSocketAction(typing.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class Task(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: TaskSpec
    status: TaskStatus

@typing.type_check_only
class TaskAttemptResult(typing.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus
    termSignal: int

@typing.type_check_only
class TaskSpec(typing.TypedDict, total=False):
    containers: _list[Container]
    maxRetries: int
    nodeSelector: dict[str, typing.Any]
    serviceAccountName: str
    timeoutSeconds: str
    volumes: _list[Volume]

@typing.type_check_only
class TaskStatus(typing.TypedDict, total=False):
    completionTime: str
    conditions: _list[GoogleCloudRunV1Condition]
    index: int
    lastAttemptResult: TaskAttemptResult
    logUri: str
    observedGeneration: int
    retried: int
    startTime: str

@typing.type_check_only
class TaskTemplateSpec(typing.TypedDict, total=False):
    spec: TaskSpec

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrafficTarget(typing.TypedDict, total=False):
    configurationName: str
    latestRevision: bool
    percent: int
    revisionName: str
    tag: str
    url: str

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    configMap: ConfigMapVolumeSource
    csi: CSIVolumeSource
    emptyDir: EmptyDirVolumeSource
    name: str
    nfs: NFSVolumeSource
    secret: SecretVolumeSource

@typing.type_check_only
class VolumeMount(typing.TypedDict, total=False):
    mountPath: str
    name: str
    readOnly: bool
    subPath: str

@typing.type_check_only
class WorkerPool(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: WorkerPoolSpec
    status: WorkerPoolStatus

@typing.type_check_only
class WorkerPoolSpec(typing.TypedDict, total=False):
    instanceSplits: _list[InstanceSplit]
    template: RevisionTemplate

@typing.type_check_only
class WorkerPoolStatus(typing.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    instanceSplits: _list[InstanceSplit]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int
