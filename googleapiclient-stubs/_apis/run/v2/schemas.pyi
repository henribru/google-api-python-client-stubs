import typing

_list = list

@typing.type_check_only
class GoogleCloudRunV2BinaryAuthorization(typing.TypedDict, total=False):
    breakglassJustification: str
    policy: str
    useDefault: bool

@typing.type_check_only
class GoogleCloudRunV2BuildConfig(typing.TypedDict, total=False):
    baseImage: str
    enableAutomaticUpdates: bool
    environmentVariables: dict[str, typing.Any]
    functionTarget: str
    imageUri: str
    name: str
    serviceAccount: str
    sourceLocation: str
    workerPool: str

@typing.type_check_only
class GoogleCloudRunV2BuildInfo(typing.TypedDict, total=False):
    functionTarget: str
    sourceLocation: str

@typing.type_check_only
class GoogleCloudRunV2BuildpacksBuild(typing.TypedDict, total=False):
    baseImage: str
    cacheImageUri: str
    enableAutomaticUpdates: bool
    environmentVariables: dict[str, typing.Any]
    functionTarget: str
    projectDescriptor: str
    runtime: str

@typing.type_check_only
class GoogleCloudRunV2CancelExecutionRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRunV2CloudSqlInstance(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class GoogleCloudRunV2CloudStorageSource(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class GoogleCloudRunV2Condition(typing.TypedDict, total=False):
    executionReason: typing.Literal[
        "EXECUTION_REASON_UNDEFINED",
        "JOB_STATUS_SERVICE_POLLING_ERROR",
        "NON_ZERO_EXIT_CODE",
        "CANCELLED",
        "CANCELLING",
        "DELETED",
        "DELAYED_START_PENDING",
    ]
    instanceReason: typing.Literal[
        "INSTANCE_REASON_UNSPECIFIED",
        "INSTANCE_DELETED",
        "INSTANCE_STOPPED",
        "INSTANCE_STOPPING",
        "INSTANCE_NON_ZERO_EXIT_CODE",
    ]
    lastTransitionTime: str
    message: str
    reason: typing.Literal[
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
        "VPC_NETWORK_NOT_FOUND",
    ]
    revisionReason: typing.Literal[
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
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CONDITION_PENDING",
        "CONDITION_RECONCILING",
        "CONDITION_FAILED",
        "CONDITION_SUCCEEDED",
    ]
    type: str

@typing.type_check_only
class GoogleCloudRunV2Container(typing.TypedDict, total=False):
    args: _list[str]
    baseImageUri: str
    buildInfo: GoogleCloudRunV2BuildInfo
    command: _list[str]
    dependsOn: _list[str]
    env: _list[GoogleCloudRunV2EnvVar]
    image: str
    livenessProbe: GoogleCloudRunV2Probe
    name: str
    ports: _list[GoogleCloudRunV2ContainerPort]
    readinessProbe: GoogleCloudRunV2Probe
    resources: GoogleCloudRunV2ResourceRequirements
    sandboxLauncher: bool
    sourceCode: GoogleCloudRunV2SourceCode
    startupProbe: GoogleCloudRunV2Probe
    volumeMounts: _list[GoogleCloudRunV2VolumeMount]
    workingDir: str

@typing.type_check_only
class GoogleCloudRunV2ContainerOverride(typing.TypedDict, total=False):
    args: _list[str]
    clearArgs: bool
    env: _list[GoogleCloudRunV2EnvVar]
    name: str

@typing.type_check_only
class GoogleCloudRunV2ContainerPort(typing.TypedDict, total=False):
    containerPort: int
    name: str

@typing.type_check_only
class GoogleCloudRunV2ContainerStatus(typing.TypedDict, total=False):
    imageDigest: str
    name: str

@typing.type_check_only
class GoogleCloudRunV2DockerBuild(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRunV2EmptyDirVolumeSource(typing.TypedDict, total=False):
    medium: typing.Literal["MEDIUM_UNSPECIFIED", "MEMORY", "DISK"]
    sizeLimit: str

@typing.type_check_only
class GoogleCloudRunV2EnvVar(typing.TypedDict, total=False):
    name: str
    value: str
    valueSource: GoogleCloudRunV2EnvVarSource

@typing.type_check_only
class GoogleCloudRunV2EnvVarSource(typing.TypedDict, total=False):
    secretKeyRef: GoogleCloudRunV2SecretKeySelector

@typing.type_check_only
class GoogleCloudRunV2Execution(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    cancelledCount: int
    client: str
    clientVersion: str
    completionTime: str
    conditions: _list[GoogleCloudRunV2Condition]
    createTime: str
    creator: str
    deleteTime: str
    etag: str
    expireTime: str
    failedCount: int
    generation: str
    job: str
    labels: dict[str, typing.Any]
    launchStage: typing.Literal[
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
class GoogleCloudRunV2ExecutionReference(typing.TypedDict, total=False):
    completionStatus: typing.Literal[
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
class GoogleCloudRunV2ExecutionTemplate(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    client: str
    clientVersion: str
    labels: dict[str, typing.Any]
    parallelism: int
    taskCount: int
    template: GoogleCloudRunV2TaskTemplate

@typing.type_check_only
class GoogleCloudRunV2ExportImageRequest(typing.TypedDict, total=False):
    destinationRepo: str

@typing.type_check_only
class GoogleCloudRunV2ExportImageResponse(typing.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class GoogleCloudRunV2ExportStatusResponse(typing.TypedDict, total=False):
    imageExportStatuses: _list[GoogleCloudRunV2ImageExportStatus]
    operationId: str
    operationState: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED", "IN_PROGRESS", "FINISHED"
    ]

@typing.type_check_only
class GoogleCloudRunV2GCSVolumeSource(typing.TypedDict, total=False):
    bucket: str
    mountOptions: _list[str]
    readOnly: bool

@typing.type_check_only
class GoogleCloudRunV2GRPCAction(typing.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudRunV2HTTPGetAction(typing.TypedDict, total=False):
    httpHeaders: _list[GoogleCloudRunV2HTTPHeader]
    path: str
    port: int

@typing.type_check_only
class GoogleCloudRunV2HTTPHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudRunV2ImageExportStatus(typing.TypedDict, total=False):
    exportJobState: typing.Literal[
        "EXPORT_JOB_STATE_UNSPECIFIED", "IN_PROGRESS", "FINISHED"
    ]
    exportedImageDigest: str
    status: UtilStatusProto
    tag: str

@typing.type_check_only
class GoogleCloudRunV2InlinedSource(typing.TypedDict, total=False):
    sources: _list[GoogleCloudRunV2SourceFile]

@typing.type_check_only
class GoogleCloudRunV2Instance(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    binaryAuthorization: GoogleCloudRunV2BinaryAuthorization
    client: str
    clientVersion: str
    conditions: _list[GoogleCloudRunV2Condition]
    containerStatuses: _list[GoogleCloudRunV2ContainerStatus]
    containers: _list[GoogleCloudRunV2Container]
    createTime: str
    creator: str
    defaultUriDisabled: bool
    deleteTime: str
    description: str
    encryptionKey: str
    encryptionKeyRevocationAction: typing.Literal[
        "ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED", "PREVENT_NEW", "SHUTDOWN"
    ]
    encryptionKeyShutdownDuration: str
    etag: str
    expireTime: str
    generation: str
    gpuZonalRedundancyDisabled: bool
    iapEnabled: bool
    ingress: typing.Literal[
        "INGRESS_TRAFFIC_UNSPECIFIED",
        "INGRESS_TRAFFIC_ALL",
        "INGRESS_TRAFFIC_INTERNAL_ONLY",
        "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER",
        "INGRESS_TRAFFIC_NONE",
    ]
    invokerIamDisabled: bool
    labels: dict[str, typing.Any]
    lastModifier: str
    launchStage: typing.Literal[
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
    nodeSelector: GoogleCloudRunV2NodeSelector
    observedGeneration: str
    reconciling: bool
    restartPolicy: typing.Literal[
        "RESTART_POLICY_UNSPECIFIED", "ALWAYS", "ON_FAILURE", "NEVER"
    ]
    satisfiesPzs: bool
    serviceAccount: str
    terminalCondition: GoogleCloudRunV2Condition
    uid: str
    updateTime: str
    urls: _list[str]
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2InstanceSplit(typing.TypedDict, total=False):
    percent: int
    revision: str
    type: typing.Literal[
        "INSTANCE_SPLIT_ALLOCATION_TYPE_UNSPECIFIED",
        "INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST",
        "INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION",
    ]

@typing.type_check_only
class GoogleCloudRunV2InstanceSplitStatus(typing.TypedDict, total=False):
    percent: int
    revision: str
    type: typing.Literal[
        "INSTANCE_SPLIT_ALLOCATION_TYPE_UNSPECIFIED",
        "INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST",
        "INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION",
    ]

@typing.type_check_only
class GoogleCloudRunV2Job(typing.TypedDict, total=False):
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
    launchStage: typing.Literal[
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
class GoogleCloudRunV2ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[GoogleCloudRunV2Execution]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRunV2ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[GoogleCloudRunV2Instance]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRunV2ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[GoogleCloudRunV2Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRunV2ListRevisionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[GoogleCloudRunV2Revision]

@typing.type_check_only
class GoogleCloudRunV2ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[GoogleCloudRunV2Service]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudRunV2ListTasksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[GoogleCloudRunV2Task]

@typing.type_check_only
class GoogleCloudRunV2ListWorkerPoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workerPools: _list[GoogleCloudRunV2WorkerPool]

@typing.type_check_only
class GoogleCloudRunV2Metadata(typing.TypedDict, total=False):
    metadata: str

@typing.type_check_only
class GoogleCloudRunV2MultiRegionSettings(typing.TypedDict, total=False):
    multiRegionId: str
    regions: _list[str]

@typing.type_check_only
class GoogleCloudRunV2NFSVolumeSource(typing.TypedDict, total=False):
    path: str
    readOnly: bool
    server: str

@typing.type_check_only
class GoogleCloudRunV2NetworkInterface(typing.TypedDict, total=False):
    network: str
    subnetwork: str
    tags: _list[str]

@typing.type_check_only
class GoogleCloudRunV2NodeSelector(typing.TypedDict, total=False):
    accelerator: str

@typing.type_check_only
class GoogleCloudRunV2Overrides(typing.TypedDict, total=False):
    containerOverrides: _list[GoogleCloudRunV2ContainerOverride]
    taskCount: int
    timeout: str

@typing.type_check_only
class GoogleCloudRunV2Probe(typing.TypedDict, total=False):
    failureThreshold: int
    grpc: GoogleCloudRunV2GRPCAction
    httpGet: GoogleCloudRunV2HTTPGetAction
    initialDelaySeconds: int
    periodSeconds: int
    tcpSocket: GoogleCloudRunV2TCPSocketAction
    timeoutSeconds: int

@typing.type_check_only
class GoogleCloudRunV2ResourceRequirements(typing.TypedDict, total=False):
    cpuIdle: bool
    limits: dict[str, typing.Any]
    startupCpuBoost: bool

@typing.type_check_only
class GoogleCloudRunV2Revision(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    client: str
    clientVersion: str
    conditions: _list[GoogleCloudRunV2Condition]
    containers: _list[GoogleCloudRunV2Container]
    createTime: str
    creator: str
    deleteTime: str
    encryptionKey: str
    encryptionKeyRevocationAction: typing.Literal[
        "ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED", "PREVENT_NEW", "SHUTDOWN"
    ]
    encryptionKeyShutdownDuration: str
    etag: str
    executionEnvironment: typing.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    expireTime: str
    generation: str
    gpuZonalRedundancyDisabled: bool
    labels: dict[str, typing.Any]
    launchStage: typing.Literal[
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
class GoogleCloudRunV2RevisionScaling(typing.TypedDict, total=False):
    concurrencyUtilization: float
    cpuUtilization: float
    maxInstanceCount: int
    minInstanceCount: int

@typing.type_check_only
class GoogleCloudRunV2RevisionScalingStatus(typing.TypedDict, total=False):
    desiredMinInstanceCount: int

@typing.type_check_only
class GoogleCloudRunV2RevisionTemplate(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    client: str
    clientVersion: str
    containers: _list[GoogleCloudRunV2Container]
    encryptionKey: str
    encryptionKeyRevocationAction: typing.Literal[
        "ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED", "PREVENT_NEW", "SHUTDOWN"
    ]
    encryptionKeyShutdownDuration: str
    executionEnvironment: typing.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    gpuZonalRedundancyDisabled: bool
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
class GoogleCloudRunV2RunJobRequest(typing.TypedDict, total=False):
    etag: str
    overrides: GoogleCloudRunV2Overrides
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRunV2SecretKeySelector(typing.TypedDict, total=False):
    secret: str
    version: str

@typing.type_check_only
class GoogleCloudRunV2SecretVolumeSource(typing.TypedDict, total=False):
    defaultMode: int
    items: _list[GoogleCloudRunV2VersionToPath]
    secret: str

@typing.type_check_only
class GoogleCloudRunV2Service(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    binaryAuthorization: GoogleCloudRunV2BinaryAuthorization
    buildConfig: GoogleCloudRunV2BuildConfig
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
    iapEnabled: bool
    ingress: typing.Literal[
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
    launchStage: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    multiRegionSettings: GoogleCloudRunV2MultiRegionSettings
    name: str
    observedGeneration: str
    reconciling: bool
    satisfiesPzs: bool
    scaling: GoogleCloudRunV2ServiceScaling
    sshEnabled: bool
    template: GoogleCloudRunV2RevisionTemplate
    terminalCondition: GoogleCloudRunV2Condition
    threatDetectionEnabled: bool
    traffic: _list[GoogleCloudRunV2TrafficTarget]
    trafficStatuses: _list[GoogleCloudRunV2TrafficTargetStatus]
    uid: str
    updateTime: str
    uri: str
    urls: _list[str]

@typing.type_check_only
class GoogleCloudRunV2ServiceMesh(typing.TypedDict, total=False):
    mesh: str

@typing.type_check_only
class GoogleCloudRunV2ServiceScaling(typing.TypedDict, total=False):
    manualInstanceCount: int
    maxInstanceCount: int
    minInstanceCount: int
    scalingMode: typing.Literal["SCALING_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"]

@typing.type_check_only
class GoogleCloudRunV2SourceCode(typing.TypedDict, total=False):
    cloudStorageSource: GoogleCloudRunV2CloudStorageSource
    inlinedSource: GoogleCloudRunV2InlinedSource

@typing.type_check_only
class GoogleCloudRunV2SourceFile(typing.TypedDict, total=False):
    content: str
    filename: str

@typing.type_check_only
class GoogleCloudRunV2StartInstanceRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRunV2StopInstanceRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRunV2StorageSource(typing.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class GoogleCloudRunV2SubmitBuildRequest(typing.TypedDict, total=False):
    buildpackBuild: GoogleCloudRunV2BuildpacksBuild
    client: str
    dockerBuild: GoogleCloudRunV2DockerBuild
    imageUri: str
    machineType: str
    releaseTrack: typing.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    serviceAccount: str
    storageSource: GoogleCloudRunV2StorageSource
    tags: _list[str]
    workerPool: str

@typing.type_check_only
class GoogleCloudRunV2SubmitBuildResponse(typing.TypedDict, total=False):
    baseImageUri: str
    baseImageWarning: str
    buildOperation: GoogleLongrunningOperation

@typing.type_check_only
class GoogleCloudRunV2TCPSocketAction(typing.TypedDict, total=False):
    port: int

@typing.type_check_only
class GoogleCloudRunV2Task(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    completionTime: str
    conditions: _list[GoogleCloudRunV2Condition]
    containers: _list[GoogleCloudRunV2Container]
    createTime: str
    deleteTime: str
    encryptionKey: str
    etag: str
    execution: str
    executionEnvironment: typing.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    expireTime: str
    generation: str
    gpuZonalRedundancyDisabled: bool
    index: int
    job: str
    labels: dict[str, typing.Any]
    lastAttemptResult: GoogleCloudRunV2TaskAttemptResult
    logUri: str
    maxRetries: int
    name: str
    nodeSelector: GoogleCloudRunV2NodeSelector
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
class GoogleCloudRunV2TaskAttemptResult(typing.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus
    termSignal: int

@typing.type_check_only
class GoogleCloudRunV2TaskTemplate(typing.TypedDict, total=False):
    containers: _list[GoogleCloudRunV2Container]
    encryptionKey: str
    executionEnvironment: typing.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    gpuZonalRedundancyDisabled: bool
    maxRetries: int
    nodeSelector: GoogleCloudRunV2NodeSelector
    serviceAccount: str
    timeout: str
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2TrafficTarget(typing.TypedDict, total=False):
    percent: int
    revision: str
    tag: str
    type: typing.Literal[
        "TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION",
    ]

@typing.type_check_only
class GoogleCloudRunV2TrafficTargetStatus(typing.TypedDict, total=False):
    percent: int
    revision: str
    tag: str
    type: typing.Literal[
        "TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST",
        "TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION",
    ]
    uri: str

@typing.type_check_only
class GoogleCloudRunV2UploadSourceRequest(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudRunV2UploadSourceResponse(typing.TypedDict, total=False):
    cloudStorageSource: GoogleCloudRunV2CloudStorageSource

@typing.type_check_only
class GoogleCloudRunV2VersionToPath(typing.TypedDict, total=False):
    mode: int
    path: str
    version: str

@typing.type_check_only
class GoogleCloudRunV2Volume(typing.TypedDict, total=False):
    cloudSqlInstance: GoogleCloudRunV2CloudSqlInstance
    emptyDir: GoogleCloudRunV2EmptyDirVolumeSource
    gcs: GoogleCloudRunV2GCSVolumeSource
    name: str
    nfs: GoogleCloudRunV2NFSVolumeSource
    secret: GoogleCloudRunV2SecretVolumeSource

@typing.type_check_only
class GoogleCloudRunV2VolumeMount(typing.TypedDict, total=False):
    mountPath: str
    name: str
    subPath: str

@typing.type_check_only
class GoogleCloudRunV2VpcAccess(typing.TypedDict, total=False):
    connector: str
    egress: typing.Literal[
        "VPC_EGRESS_UNSPECIFIED", "ALL_TRAFFIC", "PRIVATE_RANGES_ONLY"
    ]
    networkInterfaces: _list[GoogleCloudRunV2NetworkInterface]

@typing.type_check_only
class GoogleCloudRunV2WorkerPool(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    binaryAuthorization: GoogleCloudRunV2BinaryAuthorization
    client: str
    clientVersion: str
    conditions: _list[GoogleCloudRunV2Condition]
    createTime: str
    creator: str
    customAudiences: _list[str]
    deleteTime: str
    description: str
    etag: str
    expireTime: str
    generation: str
    instanceSplitStatuses: _list[GoogleCloudRunV2InstanceSplitStatus]
    instanceSplits: _list[GoogleCloudRunV2InstanceSplit]
    labels: dict[str, typing.Any]
    lastModifier: str
    latestCreatedRevision: str
    latestReadyRevision: str
    launchStage: typing.Literal[
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
    scaling: GoogleCloudRunV2WorkerPoolScaling
    template: GoogleCloudRunV2WorkerPoolRevisionTemplate
    terminalCondition: GoogleCloudRunV2Condition
    threatDetectionEnabled: bool
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRunV2WorkerPoolRevisionTemplate(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    client: str
    clientVersion: str
    containers: _list[GoogleCloudRunV2Container]
    encryptionKey: str
    encryptionKeyRevocationAction: typing.Literal[
        "ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED", "PREVENT_NEW", "SHUTDOWN"
    ]
    encryptionKeyShutdownDuration: str
    gpuZonalRedundancyDisabled: bool
    labels: dict[str, typing.Any]
    nodeSelector: GoogleCloudRunV2NodeSelector
    revision: str
    serviceAccount: str
    serviceMesh: GoogleCloudRunV2ServiceMesh
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2WorkerPoolScaling(typing.TypedDict, total=False):
    manualInstanceCount: int

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
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

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
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Proto2BridgeMessageSet(typing.TypedDict, total=False): ...

@typing.type_check_only
class UtilStatusProto(typing.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: Proto2BridgeMessageSet
    space: str
