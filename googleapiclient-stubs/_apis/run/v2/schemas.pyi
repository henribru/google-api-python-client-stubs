import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudRunV2BinaryAuthorization(typing_extensions.TypedDict, total=False):
    breakglassJustification: str
    useDefault: bool

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
class GoogleCloudRunV2ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    name: str

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
    name: str
    observedGeneration: str
    parallelism: int
    reconciling: bool
    runningCount: int
    startTime: str
    succeededCount: int
    taskCount: int
    template: GoogleCloudRunV2TaskTemplate
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRunV2ExecutionReference(typing_extensions.TypedDict, total=False):
    completionTime: str
    createTime: str
    name: str

@typing.type_check_only
class GoogleCloudRunV2ExecutionTemplate(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    parallelism: int
    taskCount: int
    template: GoogleCloudRunV2TaskTemplate

@typing.type_check_only
class GoogleCloudRunV2GRPCAction(typing_extensions.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudRunV2HTTPGetAction(typing_extensions.TypedDict, total=False):
    host: str
    httpHeaders: _list[GoogleCloudRunV2HTTPHeader]
    path: str
    scheme: str

@typing.type_check_only
class GoogleCloudRunV2HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

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

@typing.type_check_only
class GoogleCloudRunV2Revision(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    conditions: _list[GoogleCloudRunV2Condition]
    containers: _list[GoogleCloudRunV2Container]
    createTime: str
    deleteTime: str
    encryptionKey: str
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
    observedGeneration: str
    reconciling: bool
    scaling: GoogleCloudRunV2RevisionScaling
    service: str
    serviceAccount: str
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
class GoogleCloudRunV2RevisionTemplate(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    containers: _list[GoogleCloudRunV2Container]
    encryptionKey: str
    executionEnvironment: typing_extensions.Literal[
        "EXECUTION_ENVIRONMENT_UNSPECIFIED",
        "EXECUTION_ENVIRONMENT_GEN1",
        "EXECUTION_ENVIRONMENT_GEN2",
    ]
    labels: dict[str, typing.Any]
    maxInstanceRequestConcurrency: int
    revision: str
    scaling: GoogleCloudRunV2RevisionScaling
    serviceAccount: str
    timeout: str
    volumes: _list[GoogleCloudRunV2Volume]
    vpcAccess: GoogleCloudRunV2VpcAccess

@typing.type_check_only
class GoogleCloudRunV2RunJobRequest(typing_extensions.TypedDict, total=False):
    etag: str
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
    ]
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
    template: GoogleCloudRunV2RevisionTemplate
    terminalCondition: GoogleCloudRunV2Condition
    traffic: _list[GoogleCloudRunV2TrafficTarget]
    trafficStatuses: _list[GoogleCloudRunV2TrafficTargetStatus]
    uid: str
    updateTime: str
    uri: str

@typing.type_check_only
class GoogleCloudRunV2TCPSocketAction(typing_extensions.TypedDict, total=False):
    host: str
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
    maxRetries: int
    name: str
    observedGeneration: str
    reconciling: bool
    retried: int
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
    name: str
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
