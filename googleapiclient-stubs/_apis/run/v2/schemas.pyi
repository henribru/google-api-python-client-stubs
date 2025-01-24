import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudRunV2BinaryAuthorization(typing_extensions.TypedDict, total=False):
    breakglassJustification: str
    policy: str
    useDefault: bool

@typing.type_check_only
class GoogleCloudRunV2BuildpacksBuild(typing_extensions.TypedDict, total=False):
    baseImage: str
    cacheImageUri: str
    enableAutomaticUpdates: bool
    environmentVariables: dict[str, typing.Any]
    functionTarget: str
    projectDescriptor: str
    runtime: str

@typing.type_check_only
class GoogleCloudRunV2CancelExecutionRequest(typing_extensions.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRunV2CloudSqlInstance(typing_extensions.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class GoogleCloudRunV2Condition(typing_extensions.TypedDict, total=False):
    executionReason: typing_extensions.Literal[
        "EXECUTION_REASON_UNDEFINED",
        "JOB_STATUS_SERVICE_POLLING_ERROR",
        "NON_ZERO_EXIT_CODE",
        "CANCELLED",
        "CANCELLING",
        "DELETED",
    ]
    lastTransitionTime: str
    message: str
    reason: typing_extensions.Literal[
        "COMMON_REASON_UNDEFINED",
        "UNKNOWN",
        "REVISION_FAILED",
        "PROGRESS_DEADLINE_EXCEEDED",
        "CONTAINER_MISSING",
        "CONTAINER_PERMISSION_DENIED",
        "CONTAINER_IMAGE_UNAUTHORIZED",
        "CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED",
        "ENCRYPTION_KEY_PERMISSION_DENIED",
        "ENCRYPTION_KEY_CHECK_FAILED",
        "SECRETS_ACCESS_CHECK_FAILED",
        "WAITING_FOR_OPERATION",
        "IMMEDIATE_RETRY",
        "POSTPONED_RETRY",
        "INTERNAL",
    ]
    revisionReason: typing_extensions.Literal[
        "REVISION_REASON_UNDEFINED",
        "PENDING",
        "RESERVE",
        "RETIRED",
        "RETIRING",
        "RECREATING",
        "HEALTH_CHECK_CONTAINER_ERROR",
        "CUSTOMIZED_PATH_RESPONSE_PENDING",
        "MIN_INSTANCES_NOT_PROVISIONED",
        "ACTIVE_REVISION_LIMIT_REACHED",
        "NO_DEPLOYMENT",
        "HEALTH_CHECK_SKIPPED",
        "MIN_INSTANCES_WARMING",
    ]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CONDITION_PENDING",
        "CONDITION_RECONCILING",
        "CONDITION_FAILED",
        "CONDITION_SUCCEEDED",
    ]
    type: str

@typing.type_check_only
class GoogleCloudRunV2Container(typing_extensions.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    dependsOn: _list[str]
    env: _list[GoogleCloudRunV2EnvVar]
    image: str
    livenessProbe: GoogleCloudRunV2Probe
    name: str
    ports: _list[GoogleCloudRunV2ContainerPort]
    resources: GoogleCloudRunV2ResourceRequirements
    startupProbe: GoogleCloudRunV2Probe
    volumeMounts: _list[GoogleCloudRunV2VolumeMount]
    workingDir: str

@typing.type_check_only
class GoogleCloudRunV2ContainerOverride(typing_extensions.TypedDict, total=False):
    args: _list[str]
    clearArgs: bool
    env: _list[GoogleCloudRunV2EnvVar]
    name: str

@typing.type_check_only
class GoogleCloudRunV2ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    name: str

@typing.type_check_only
class GoogleCloudRunV2DockerBuild(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRunV2EmptyDirVolumeSource(typing_extensions.TypedDict, total=False):
    medium: typing_extensions.Literal["MEDIUM_UNSPECIFIED", "MEMORY"]
    sizeLimit: str

@typing.type_check_only
class GoogleCloudRunV2EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    valueSource: GoogleCloudRunV2EnvVarSource

@typing.type_check_only
class GoogleCloudRunV2EnvVarSource(typing_extensions.TypedDict, total=False):
    secretKeyRef: GoogleCloudRunV2SecretKeySelector

@typing.type_check_only
class GoogleCloudRunV2Execution(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    cancelledCount: int
    completionTime: str
    conditions: _list[GoogleCloudRunV2Condition]
    createTime: str
    deleteTime: str
    etag: str
    expireTime: str
    failedCount: int
    generation: str
    job: str
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    logUri: str
    name: str
    observedGeneration: str
    parallelism: int
    reconciling: bool
    retriedCount: int
    runningCount: int
    satisfiesPzs: bool
    startTime: str
    succeededCount: int
    taskCount: int
    template: GoogleCloudRunV2TaskTemplate
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRunV2ExecutionReference(typing_extensions.TypedDict, total=False):
    completionStatus: typing_extensions.Literal[
        "COMPLETION_STATUS_UNSPECIFIED",
        "EXECUTION_SUCCEEDED",
        "EXECUTION_FAILED",
        "EXECUTION_RUNNING",
        "EXECUTION_PENDING",
        "EXECUTION_CANCELLED",
    ]
    completionTime: str
    createTime: str
    deleteTime: str
    name: str

@typing.type_check_only
class GoogleCloudRunV2ExecutionTemplate(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    parallelism: int
    taskCount: int
    template: GoogleCloudRunV2TaskTemplate

@typing.type_check_only
class GoogleCloudRunV2ExportImageRequest(typing_extensions.TypedDict, total=False):
    destinationRepo: str

@typing.type_check_only
class GoogleCloudRunV2ExportImageResponse(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class GoogleCloudRunV2ExportStatusResponse(typing_extensions.TypedDict, total=False):
    imageExportStatuses: _list[GoogleCloudRunV2ImageExportStatus]
    operationId: str
    operationState: typing_extensions.Literal[
        "OPERATION_STATE_UNSPECIFIED", "IN_PROGRESS", "FINISHED"
    ]

@typing.type_check_only
class GoogleCloudRunV2GCSVolumeSource(typing_extensions.TypedDict, total=False):
    bucket: str
    mountOptions: _list[str]
    readOnly: bool

@typing.type_check_only
class GoogleCloudRunV2GRPCAction(typing_extensions.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudRunV2HTTPGetAction(typing_extensions.TypedDict, total=False):
    httpHeaders: _list[GoogleCloudRunV2HTTPHeader]
    path: str
    port: int

@typing.type_check_only
class GoogleCloudRunV2HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudRunV2ImageExportStatus(typing_extensions.TypedDict, total=False):
    exportJobState: typing_extensions.Literal[
        "EXPORT_JOB_STATE_UNSPECIFIED", "IN_PROGRESS", "FINISHED"
    ]
    exportedImageDigest: str
    status: UtilStatusProto
    tag: str

@typing.type_check_only
class GoogleCloudRunV2Job(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    binaryAuthorization: GoogleCloudRunV2BinaryAuthorization
    client: str
    clientVersion: str
    conditions: _list[GoogleCloudRunV2Condition]
    createTime: str
    creator: str
    deleteTime: str
    etag: str
    executionCount: int
    expireTime: str
    generation: str
    labels: dict[str, typing.Any]
    lastModifier: str
    latestCreatedExecution: GoogleCloudRunV2ExecutionReference
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    name: str
    observedGeneration: str
    reconciling: bool
    runExecutionToken: str
    satisfiesPzs: bool
    startExecutionToken: str
    template: GoogleCloudRunV2ExecutionTemplate
    terminalCondition: GoogleCloudRunV2Condition
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRunV2ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: _list[GoogleCloudRunV2Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRunV2ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[GoogleCloudRunV2Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRunV2ListRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[GoogleCloudRunV2Revision]

@typing.type_check_only
class GoogleCloudRunV2ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: _list[GoogleCloudRunV2Service]

@typing.type_check_only
class GoogleCloudRunV2ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[GoogleCloudRunV2Task]

@typing.type_check_only
class GoogleCloudRunV2Metadata(typing_extensions.TypedDict, total=False):
    metadata: str

@typing.type_check_only
class GoogleCloudRunV2NFSVolumeSource(typing_extensions.TypedDict, total=False):
    path: str
    readOnly: bool
    server: str

@typing.type_check_only
class GoogleCloudRunV2NetworkInterface(typing_extensions.TypedDict, total=False):
    network: str
    subnetwork: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudRunV2NodeSelector(typing_extensions.TypedDict, total=False):
    accelerator: str

@typing.type_check_only
class GoogleCloudRunV2Overrides(typing_extensions.TypedDict, total=False):
    containerOverrides: _list[GoogleCloudRunV2ContainerOverride]
    taskCount: int
    timeout: str

@typing.type_check_only
class GoogleCloudRunV2Probe(typing_extensions.TypedDict, total=False):
    failureThreshold: int
    grpc: GoogleCloudRunV2GRPCAction
    httpGet: GoogleCloudRunV2HTTPGetAction
    initialDelaySeconds: int
    periodSeconds: int
    tcpSocket: GoogleCloudRunV2TCPSocketAction
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudRunV2ResourceRequirements(typing_extensions.TypedDict, total=False):
    cpuIdle: bool
    limits: dict[str, typing.Any]
    startupCpuBoost: bool

@typing.type_check_only
class GoogleCloudRunV2Revision(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    conditions: _list[GoogleCloudRunV2Condition]
    containers: _list[GoogleCloudRunV2Container]
    createTime: str
    deleteTime: str
    encryptionKey: str
    encryptionKeyRevocationAction: typing_extensions.Literal[
        "ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED", "PREVENT_NEW", "SHUTDOWN"
    ]
    encryptionKeyShutdownDuration: str
    etag: str
    executionEnvironment: typing_extensions.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    expireTime: str
    generation: str
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    logUri: str
    maxInstanceRequestConcurrency: int
    name: str
    nodeSelector: GoogleCloudRunV2NodeSelector
    observedGeneration: str
    reconciling: bool
    satisfiesPzs: bool
    scaling: GoogleCloudRunV2RevisionScaling
    scalingStatus: GoogleCloudRunV2RevisionScalingStatus
    service: str
    serviceAccount: str
    serviceMesh: GoogleCloudRunV2ServiceMesh
    sessionAffinity: bool
    timeout: str
    uid: str
    updateTime: str
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2RevisionScaling(typing_extensions.TypedDict, total=False):
    maxInstanceCount: int
    minInstanceCount: int

@typing.type_check_only
class GoogleCloudRunV2RevisionScalingStatus(typing_extensions.TypedDict, total=False):
    desiredMinInstanceCount: int

@typing.type_check_only
class GoogleCloudRunV2RevisionTemplate(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    containers: _list[GoogleCloudRunV2Container]
    encryptionKey: str
    encryptionKeyRevocationAction: typing_extensions.Literal[
        "ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED", "PREVENT_NEW", "SHUTDOWN"
    ]
    encryptionKeyShutdownDuration: str
    executionEnvironment: typing_extensions.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    healthCheckDisabled: bool
    labels: dict[str, typing.Any]
    maxInstanceRequestConcurrency: int
    nodeSelector: GoogleCloudRunV2NodeSelector
    revision: str
    scaling: GoogleCloudRunV2RevisionScaling
    serviceAccount: str
    serviceMesh: GoogleCloudRunV2ServiceMesh
    sessionAffinity: bool
    timeout: str
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2RunJobRequest(typing_extensions.TypedDict, total=False):
    etag: str
    overrides: GoogleCloudRunV2Overrides
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRunV2SecretKeySelector(typing_extensions.TypedDict, total=False):
    secret: str
    version: str

@typing.type_check_only
class GoogleCloudRunV2SecretVolumeSource(typing_extensions.TypedDict, total=False):
    defaultMode: int
    items: _list[GoogleCloudRunV2VersionToPath]
    secret: str

@typing.type_check_only
class GoogleCloudRunV2Service(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    binaryAuthorization: GoogleCloudRunV2BinaryAuthorization
    client: str
    clientVersion: str
    conditions: _list[GoogleCloudRunV2Condition]
    createTime: str
    creator: str
    customAudiences: _list[str]
    defaultUriDisabled: bool
    deleteTime: str
    description: str
    etag: str
    expireTime: str
    generation: str
    ingress: typing_extensions.Literal[
        "INGRESS_TRAFFIC_UNSPECIFIED",
        "INGRESS_TRAFFIC_ALL",
        "INGRESS_TRAFFIC_INTERNAL_ONLY",
        "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER",
        "INGRESS_TRAFFIC_NONE",
    ]
    invokerIamDisabled: bool
    labels: dict[str, typing.Any]
    lastModifier: str
    latestCreatedRevision: str
    latestReadyRevision: str
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    name: str
    observedGeneration: str
    reconciling: bool
    satisfiesPzs: bool
    scaling: GoogleCloudRunV2ServiceScaling
    template: GoogleCloudRunV2RevisionTemplate
    terminalCondition: GoogleCloudRunV2Condition
    traffic: _list[GoogleCloudRunV2TrafficTarget]
    trafficStatuses: _list[GoogleCloudRunV2TrafficTargetStatus]
    uid: str
    updateTime: str
    uri: str
    urls: _list[str]

@typing.type_check_only
class GoogleCloudRunV2ServiceMesh(typing_extensions.TypedDict, total=False):
    mesh: str

@typing.type_check_only
class GoogleCloudRunV2ServiceScaling(typing_extensions.TypedDict, total=False):
    manualInstanceCount: int
    maxInstanceCount: int
    minInstanceCount: int
    scalingMode: typing_extensions.Literal[
        "SCALING_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]

@typing.type_check_only
class GoogleCloudRunV2StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class GoogleCloudRunV2SubmitBuildRequest(typing_extensions.TypedDict, total=False):
    buildpackBuild: GoogleCloudRunV2BuildpacksBuild
    dockerBuild: GoogleCloudRunV2DockerBuild
    imageUri: str
    serviceAccount: str
    storageSource: GoogleCloudRunV2StorageSource
    tags: _list[str]
    workerPool: str

@typing.type_check_only
class GoogleCloudRunV2SubmitBuildResponse(typing_extensions.TypedDict, total=False):
    baseImageUri: str
    baseImageWarning: str
    buildOperation: GoogleLongrunningOperation

@typing.type_check_only
class GoogleCloudRunV2TCPSocketAction(typing_extensions.TypedDict, total=False):
    port: int

@typing.type_check_only
class GoogleCloudRunV2Task(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    completionTime: str
    conditions: _list[GoogleCloudRunV2Condition]
    containers: _list[GoogleCloudRunV2Container]
    createTime: str
    deleteTime: str
    encryptionKey: str
    etag: str
    execution: str
    executionEnvironment: typing_extensions.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    expireTime: str
    generation: str
    index: int
    job: str
    labels: dict[str, typing.Any]
    lastAttemptResult: GoogleCloudRunV2TaskAttemptResult
    logUri: str
    maxRetries: int
    name: str
    observedGeneration: str
    reconciling: bool
    retried: int
    satisfiesPzs: bool
    scheduledTime: str
    serviceAccount: str
    startTime: str
    timeout: str
    uid: str
    updateTime: str
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2TaskAttemptResult(typing_extensions.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudRunV2TaskTemplate(typing_extensions.TypedDict, total=False):
    containers: _list[GoogleCloudRunV2Container]
    encryptionKey: str
    executionEnvironment: typing_extensions.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    maxRetries: int
    serviceAccount: str
    timeout: str
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2TrafficTarget(typing_extensions.TypedDict, total=False):
    percent: int
    revision: str
    tag: str
    type: typing_extensions.Literal[
        "TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION",
    ]

@typing.type_check_only
class GoogleCloudRunV2TrafficTargetStatus(typing_extensions.TypedDict, total=False):
    percent: int
    revision: str
    tag: str
    type: typing_extensions.Literal[
        "TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION",
    ]
    uri: str

@typing.type_check_only
class GoogleCloudRunV2VersionToPath(typing_extensions.TypedDict, total=False):
    mode: int
    path: str
    version: str

@typing.type_check_only
class GoogleCloudRunV2Volume(typing_extensions.TypedDict, total=False):
    cloudSqlInstance: GoogleCloudRunV2CloudSqlInstance
    emptyDir: GoogleCloudRunV2EmptyDirVolumeSource
    gcs: GoogleCloudRunV2GCSVolumeSource
    name: str
    nfs: GoogleCloudRunV2NFSVolumeSource
    secret: GoogleCloudRunV2SecretVolumeSource

@typing.type_check_only
class GoogleCloudRunV2VolumeMount(typing_extensions.TypedDict, total=False):
    mountPath: str
    name: str

@typing.type_check_only
class GoogleCloudRunV2VpcAccess(typing_extensions.TypedDict, total=False):
    connector: str
    egress: typing_extensions.Literal[
        "VPC_EGRESS_UNSPECIFIED", "ALL_TRAFFIC", "PRIVATE_RANGES_ONLY"
    ]
    networkInterfaces: _list[GoogleCloudRunV2NetworkInterface]

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
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

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
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Proto2BridgeMessageSet(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UtilStatusProto(typing_extensions.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: Proto2BridgeMessageSet
    space: str
