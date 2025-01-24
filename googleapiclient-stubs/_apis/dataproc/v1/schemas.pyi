import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorTypeUri: str

@typing.type_check_only
class AccessSessionSparkApplicationEnvironmentInfoResponse(
    typing_extensions.TypedDict, total=False
):
    applicationEnvironmentInfo: ApplicationEnvironmentInfo

@typing.type_check_only
class AccessSessionSparkApplicationJobResponse(
    typing_extensions.TypedDict, total=False
):
    jobData: JobData

@typing.type_check_only
class AccessSessionSparkApplicationResponse(typing_extensions.TypedDict, total=False):
    application: ApplicationInfo

@typing.type_check_only
class AccessSessionSparkApplicationSqlQueryResponse(
    typing_extensions.TypedDict, total=False
):
    executionData: SqlExecutionUiData

@typing.type_check_only
class AccessSessionSparkApplicationSqlSparkPlanGraphResponse(
    typing_extensions.TypedDict, total=False
):
    sparkPlanGraph: SparkPlanGraph

@typing.type_check_only
class AccessSessionSparkApplicationStageAttemptResponse(
    typing_extensions.TypedDict, total=False
):
    stageData: StageData

@typing.type_check_only
class AccessSessionSparkApplicationStageRddOperationGraphResponse(
    typing_extensions.TypedDict, total=False
):
    rddOperationGraph: RddOperationGraph

@typing.type_check_only
class AccessSparkApplicationEnvironmentInfoResponse(
    typing_extensions.TypedDict, total=False
):
    applicationEnvironmentInfo: ApplicationEnvironmentInfo

@typing.type_check_only
class AccessSparkApplicationJobResponse(typing_extensions.TypedDict, total=False):
    jobData: JobData

@typing.type_check_only
class AccessSparkApplicationResponse(typing_extensions.TypedDict, total=False):
    application: ApplicationInfo

@typing.type_check_only
class AccessSparkApplicationSqlQueryResponse(typing_extensions.TypedDict, total=False):
    executionData: SqlExecutionUiData

@typing.type_check_only
class AccessSparkApplicationSqlSparkPlanGraphResponse(
    typing_extensions.TypedDict, total=False
):
    sparkPlanGraph: SparkPlanGraph

@typing.type_check_only
class AccessSparkApplicationStageAttemptResponse(
    typing_extensions.TypedDict, total=False
):
    stageData: StageData

@typing.type_check_only
class AccessSparkApplicationStageRddOperationGraphResponse(
    typing_extensions.TypedDict, total=False
):
    rddOperationGraph: RddOperationGraph

@typing.type_check_only
class AccumulableInfo(typing_extensions.TypedDict, total=False):
    accumullableInfoId: str
    name: str
    update: str
    value: str

@typing.type_check_only
class AnalyzeBatchRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class AnalyzeOperationMetadata(typing_extensions.TypedDict, total=False):
    analyzedWorkloadName: str
    analyzedWorkloadType: typing_extensions.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "BATCH"
    ]
    analyzedWorkloadUuid: str
    createTime: str
    description: str
    doneTime: str
    labels: dict[str, typing.Any]
    warnings: _list[str]

@typing.type_check_only
class AppSummary(typing_extensions.TypedDict, total=False):
    numCompletedJobs: int
    numCompletedStages: int

@typing.type_check_only
class ApplicationAttemptInfo(typing_extensions.TypedDict, total=False):
    appSparkVersion: str
    attemptId: str
    completed: bool
    durationMillis: str
    endTime: str
    lastUpdated: str
    sparkUser: str
    startTime: str

@typing.type_check_only
class ApplicationEnvironmentInfo(typing_extensions.TypedDict, total=False):
    classpathEntries: dict[str, typing.Any]
    hadoopProperties: dict[str, typing.Any]
    metricsProperties: dict[str, typing.Any]
    resourceProfiles: _list[ResourceProfileInfo]
    runtime: SparkRuntimeInfo
    sparkProperties: dict[str, typing.Any]
    systemProperties: dict[str, typing.Any]

@typing.type_check_only
class ApplicationInfo(typing_extensions.TypedDict, total=False):
    applicationContextIngestionStatus: typing_extensions.Literal[
        "APPLICATION_CONTEXT_INGESTION_STATUS_UNSPECIFIED",
        "APPLICATION_CONTEXT_INGESTION_STATUS_COMPLETED",
    ]
    applicationId: str
    attempts: _list[ApplicationAttemptInfo]
    coresGranted: int
    coresPerExecutor: int
    maxCores: int
    memoryPerExecutorMb: int
    name: str
    quantileDataStatus: typing_extensions.Literal[
        "QUANTILE_DATA_STATUS_UNSPECIFIED",
        "QUANTILE_DATA_STATUS_COMPLETED",
        "QUANTILE_DATA_STATUS_FAILED",
    ]

@typing.type_check_only
class AutoscalingConfig(typing_extensions.TypedDict, total=False):
    policyUri: str

@typing.type_check_only
class AutoscalingPolicy(typing_extensions.TypedDict, total=False):
    basicAlgorithm: BasicAutoscalingAlgorithm
    id: str
    labels: dict[str, typing.Any]
    name: str
    secondaryWorkerConfig: InstanceGroupAutoscalingPolicyConfig
    workerConfig: InstanceGroupAutoscalingPolicyConfig

@typing.type_check_only
class AutotuningConfig(typing_extensions.TypedDict, total=False):
    scenarios: _list[
        typing_extensions.Literal[
            "SCENARIO_UNSPECIFIED", "SCALING", "BROADCAST_HASH_JOIN", "MEMORY"
        ]
    ]

@typing.type_check_only
class AuxiliaryNodeGroup(typing_extensions.TypedDict, total=False):
    nodeGroup: NodeGroup
    nodeGroupId: str

@typing.type_check_only
class AuxiliaryServicesConfig(typing_extensions.TypedDict, total=False):
    metastoreConfig: MetastoreConfig
    sparkHistoryServerConfig: SparkHistoryServerConfig

@typing.type_check_only
class BasicAutoscalingAlgorithm(typing_extensions.TypedDict, total=False):
    cooldownPeriod: str
    sparkStandaloneConfig: SparkStandaloneAutoscalingConfig
    yarnConfig: BasicYarnAutoscalingConfig

@typing.type_check_only
class BasicYarnAutoscalingConfig(typing_extensions.TypedDict, total=False):
    gracefulDecommissionTimeout: str
    scaleDownFactor: float
    scaleDownMinWorkerFraction: float
    scaleUpFactor: float
    scaleUpMinWorkerFraction: float

@typing.type_check_only
class Batch(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    environmentConfig: EnvironmentConfig
    labels: dict[str, typing.Any]
    name: str
    operation: str
    pysparkBatch: PySparkBatch
    runtimeConfig: RuntimeConfig
    runtimeInfo: RuntimeInfo
    sparkBatch: SparkBatch
    sparkRBatch: SparkRBatch
    sparkSqlBatch: SparkSqlBatch
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
    ]
    stateHistory: _list[StateHistory]
    stateMessage: str
    stateTime: str
    uuid: str

@typing.type_check_only
class BatchOperationMetadata(typing_extensions.TypedDict, total=False):
    batch: str
    batchUuid: str
    createTime: str
    description: str
    doneTime: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "BATCH_OPERATION_TYPE_UNSPECIFIED", "BATCH"
    ]
    warnings: _list[str]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    clusterName: str
    clusterUuid: str
    config: ClusterConfig
    labels: dict[str, typing.Any]
    metrics: ClusterMetrics
    projectId: str
    status: ClusterStatus
    statusHistory: _list[ClusterStatus]
    virtualClusterConfig: VirtualClusterConfig

@typing.type_check_only
class ClusterConfig(typing_extensions.TypedDict, total=False):
    autoscalingConfig: AutoscalingConfig
    auxiliaryNodeGroups: _list[AuxiliaryNodeGroup]
    configBucket: str
    dataprocMetricConfig: DataprocMetricConfig
    encryptionConfig: EncryptionConfig
    endpointConfig: EndpointConfig
    gceClusterConfig: GceClusterConfig
    gkeClusterConfig: GkeClusterConfig
    initializationActions: _list[NodeInitializationAction]
    lifecycleConfig: LifecycleConfig
    masterConfig: InstanceGroupConfig
    metastoreConfig: MetastoreConfig
    secondaryWorkerConfig: InstanceGroupConfig
    securityConfig: SecurityConfig
    softwareConfig: SoftwareConfig
    tempBucket: str
    workerConfig: InstanceGroupConfig

@typing.type_check_only
class ClusterMetrics(typing_extensions.TypedDict, total=False):
    hdfsMetrics: dict[str, typing.Any]
    yarnMetrics: dict[str, typing.Any]

@typing.type_check_only
class ClusterOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: str
    operationId: str

@typing.type_check_only
class ClusterOperationMetadata(typing_extensions.TypedDict, total=False):
    childOperationIds: _list[str]
    clusterName: str
    clusterUuid: str
    description: str
    labels: dict[str, typing.Any]
    operationType: str
    status: ClusterOperationStatus
    statusHistory: _list[ClusterOperationStatus]
    warnings: _list[str]

@typing.type_check_only
class ClusterOperationStatus(typing_extensions.TypedDict, total=False):
    details: str
    innerState: str
    state: typing_extensions.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    stateStartTime: str

@typing.type_check_only
class ClusterSelector(typing_extensions.TypedDict, total=False):
    clusterLabels: dict[str, typing.Any]
    zone: str

@typing.type_check_only
class ClusterStatus(typing_extensions.TypedDict, total=False):
    detail: str
    state: typing_extensions.Literal[
        "UNKNOWN",
        "CREATING",
        "RUNNING",
        "ERROR",
        "ERROR_DUE_TO_UPDATE",
        "DELETING",
        "UPDATING",
        "STOPPING",
        "STOPPED",
        "STARTING",
        "REPAIRING",
        "SCHEDULED",
    ]
    stateStartTime: str
    substate: typing_extensions.Literal["UNSPECIFIED", "UNHEALTHY", "STALE_STATUS"]

@typing.type_check_only
class ClusterToRepair(typing_extensions.TypedDict, total=False):
    clusterRepairAction: typing_extensions.Literal[
        "CLUSTER_REPAIR_ACTION_UNSPECIFIED", "REPAIR_ERROR_DUE_TO_UPDATE_CLUSTER"
    ]

@typing.type_check_only
class ConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
    enableConfidentialCompute: bool

@typing.type_check_only
class ConsolidatedExecutorSummary(typing_extensions.TypedDict, total=False):
    activeTasks: int
    completedTasks: int
    count: int
    diskUsed: str
    failedTasks: int
    isExcluded: int
    maxMemory: str
    memoryMetrics: MemoryMetrics
    memoryUsed: str
    rddBlocks: int
    totalCores: int
    totalDurationMillis: str
    totalGcTimeMillis: str
    totalInputBytes: str
    totalShuffleRead: str
    totalShuffleWrite: str
    totalTasks: int

@typing.type_check_only
class DataprocMetricConfig(typing_extensions.TypedDict, total=False):
    metrics: _list[Metric]

@typing.type_check_only
class DiagnoseClusterRequest(typing_extensions.TypedDict, total=False):
    diagnosisInterval: Interval
    job: str
    jobs: _list[str]
    tarballAccess: typing_extensions.Literal[
        "TARBALL_ACCESS_UNSPECIFIED", "GOOGLE_CLOUD_SUPPORT", "GOOGLE_DATAPROC_DIAGNOSE"
    ]
    tarballGcsDir: str
    yarnApplicationId: str
    yarnApplicationIds: _list[str]

@typing.type_check_only
class DiagnoseClusterResults(typing_extensions.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class DiskConfig(typing_extensions.TypedDict, total=False):
    bootDiskProvisionedIops: str
    bootDiskProvisionedThroughput: str
    bootDiskSizeGb: int
    bootDiskType: str
    localSsdInterface: str
    numLocalSsds: int

@typing.type_check_only
class DriverSchedulingConfig(typing_extensions.TypedDict, total=False):
    memoryMb: int
    vcores: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    gcePdKmsKeyName: str
    kmsKey: str

@typing.type_check_only
class EndpointConfig(typing_extensions.TypedDict, total=False):
    enableHttpPortAccess: bool
    httpPorts: dict[str, typing.Any]

@typing.type_check_only
class EnvironmentConfig(typing_extensions.TypedDict, total=False):
    executionConfig: ExecutionConfig
    peripheralsConfig: PeripheralsConfig

@typing.type_check_only
class ExecutionConfig(typing_extensions.TypedDict, total=False):
    idleTtl: str
    kmsKey: str
    networkTags: _list[str]
    networkUri: str
    serviceAccount: str
    stagingBucket: str
    subnetworkUri: str
    ttl: str

@typing.type_check_only
class ExecutorMetrics(typing_extensions.TypedDict, total=False):
    metrics: dict[str, typing.Any]

@typing.type_check_only
class ExecutorMetricsDistributions(typing_extensions.TypedDict, total=False):
    diskBytesSpilled: _list[float]
    failedTasks: _list[float]
    inputBytes: _list[float]
    inputRecords: _list[float]
    killedTasks: _list[float]
    memoryBytesSpilled: _list[float]
    outputBytes: _list[float]
    outputRecords: _list[float]
    peakMemoryMetrics: ExecutorPeakMetricsDistributions
    quantiles: _list[float]
    shuffleRead: _list[float]
    shuffleReadRecords: _list[float]
    shuffleWrite: _list[float]
    shuffleWriteRecords: _list[float]
    succeededTasks: _list[float]
    taskTimeMillis: _list[float]

@typing.type_check_only
class ExecutorPeakMetricsDistributions(typing_extensions.TypedDict, total=False):
    executorMetrics: _list[ExecutorMetrics]
    quantiles: _list[float]

@typing.type_check_only
class ExecutorResourceRequest(typing_extensions.TypedDict, total=False):
    amount: str
    discoveryScript: str
    resourceName: str
    vendor: str

@typing.type_check_only
class ExecutorStageSummary(typing_extensions.TypedDict, total=False):
    diskBytesSpilled: str
    executorId: str
    failedTasks: int
    inputBytes: str
    inputRecords: str
    isExcludedForStage: bool
    killedTasks: int
    memoryBytesSpilled: str
    outputBytes: str
    outputRecords: str
    peakMemoryMetrics: ExecutorMetrics
    shuffleRead: str
    shuffleReadRecords: str
    shuffleWrite: str
    shuffleWriteRecords: str
    stageAttemptId: int
    stageId: str
    succeededTasks: int
    taskTimeMillis: str

@typing.type_check_only
class ExecutorSummary(typing_extensions.TypedDict, total=False):
    activeTasks: int
    addTime: str
    attributes: dict[str, typing.Any]
    completedTasks: int
    diskUsed: str
    excludedInStages: _list[str]
    executorId: str
    executorLogs: dict[str, typing.Any]
    failedTasks: int
    hostPort: str
    isActive: bool
    isExcluded: bool
    maxMemory: str
    maxTasks: int
    memoryMetrics: MemoryMetrics
    memoryUsed: str
    peakMemoryMetrics: ExecutorMetrics
    rddBlocks: int
    removeReason: str
    removeTime: str
    resourceProfileId: int
    resources: dict[str, typing.Any]
    totalCores: int
    totalDurationMillis: str
    totalGcTimeMillis: str
    totalInputBytes: str
    totalShuffleRead: str
    totalShuffleWrite: str
    totalTasks: int

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FlinkJob(typing_extensions.TypedDict, total=False):
    args: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainClass: str
    mainJarFileUri: str
    properties: dict[str, typing.Any]
    savepointUri: str

@typing.type_check_only
class GceClusterConfig(typing_extensions.TypedDict, total=False):
    confidentialInstanceConfig: ConfidentialInstanceConfig
    internalIpOnly: bool
    metadata: dict[str, typing.Any]
    networkUri: str
    nodeGroupAffinity: NodeGroupAffinity
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "INHERIT_FROM_SUBNETWORK",
        "OUTBOUND",
        "BIDIRECTIONAL",
    ]
    reservationAffinity: ReservationAffinity
    serviceAccount: str
    serviceAccountScopes: _list[str]
    shieldedInstanceConfig: ShieldedInstanceConfig
    subnetworkUri: str
    tags: _list[str]
    zoneUri: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GkeClusterConfig(typing_extensions.TypedDict, total=False):
    gkeClusterTarget: str
    namespacedGkeDeploymentTarget: NamespacedGkeDeploymentTarget
    nodePoolTarget: _list[GkeNodePoolTarget]

@typing.type_check_only
class GkeNodeConfig(typing_extensions.TypedDict, total=False):
    accelerators: _list[GkeNodePoolAcceleratorConfig]
    bootDiskKmsKey: str
    localSsdCount: int
    machineType: str
    minCpuPlatform: str
    preemptible: bool
    spot: bool

@typing.type_check_only
class GkeNodePoolAcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str
    gpuPartitionSize: str

@typing.type_check_only
class GkeNodePoolAutoscalingConfig(typing_extensions.TypedDict, total=False):
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class GkeNodePoolConfig(typing_extensions.TypedDict, total=False):
    autoscaling: GkeNodePoolAutoscalingConfig
    config: GkeNodeConfig
    locations: _list[str]

@typing.type_check_only
class GkeNodePoolTarget(typing_extensions.TypedDict, total=False):
    nodePool: str
    nodePoolConfig: GkeNodePoolConfig
    roles: _list[
        typing_extensions.Literal[
            "ROLE_UNSPECIFIED",
            "DEFAULT",
            "CONTROLLER",
            "SPARK_DRIVER",
            "SPARK_EXECUTOR",
        ]
    ]

@typing.type_check_only
class GoogleCloudDataprocV1WorkflowTemplateEncryptionConfig(
    typing_extensions.TypedDict, total=False
):
    kmsKey: str

@typing.type_check_only
class HadoopJob(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainClass: str
    mainJarFileUri: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class HiveJob(typing_extensions.TypedDict, total=False):
    continueOnFailure: bool
    jarFileUris: _list[str]
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList
    scriptVariables: dict[str, typing.Any]

@typing.type_check_only
class IdentityConfig(typing_extensions.TypedDict, total=False):
    userServiceAccountMapping: dict[str, typing.Any]

@typing.type_check_only
class InjectCredentialsRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    credentialsCiphertext: str

@typing.type_check_only
class InputMetrics(typing_extensions.TypedDict, total=False):
    bytesRead: str
    recordsRead: str

@typing.type_check_only
class InputQuantileMetrics(typing_extensions.TypedDict, total=False):
    bytesRead: Quantiles
    recordsRead: Quantiles

@typing.type_check_only
class InstanceFlexibilityPolicy(typing_extensions.TypedDict, total=False):
    instanceSelectionList: _list[InstanceSelection]
    instanceSelectionResults: _list[InstanceSelectionResult]
    provisioningModelMix: ProvisioningModelMix

@typing.type_check_only
class InstanceGroupAutoscalingPolicyConfig(typing_extensions.TypedDict, total=False):
    maxInstances: int
    minInstances: int
    weight: int

@typing.type_check_only
class InstanceGroupConfig(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    diskConfig: DiskConfig
    imageUri: str
    instanceFlexibilityPolicy: InstanceFlexibilityPolicy
    instanceNames: _list[str]
    instanceReferences: _list[InstanceReference]
    isPreemptible: bool
    machineTypeUri: str
    managedGroupConfig: ManagedGroupConfig
    minCpuPlatform: str
    minNumInstances: int
    numInstances: int
    preemptibility: typing_extensions.Literal[
        "PREEMPTIBILITY_UNSPECIFIED", "NON_PREEMPTIBLE", "PREEMPTIBLE", "SPOT"
    ]
    startupConfig: StartupConfig

@typing.type_check_only
class InstanceReference(typing_extensions.TypedDict, total=False):
    instanceId: str
    instanceName: str
    publicEciesKey: str
    publicKey: str

@typing.type_check_only
class InstanceSelection(typing_extensions.TypedDict, total=False):
    machineTypes: _list[str]
    rank: int

@typing.type_check_only
class InstanceSelectionResult(typing_extensions.TypedDict, total=False):
    machineType: str
    vmCount: int

@typing.type_check_only
class InstantiateWorkflowTemplateRequest(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    requestId: str
    version: int

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    done: bool
    driverControlFilesUri: str
    driverOutputResourceUri: str
    driverSchedulingConfig: DriverSchedulingConfig
    flinkJob: FlinkJob
    hadoopJob: HadoopJob
    hiveJob: HiveJob
    jobUuid: str
    labels: dict[str, typing.Any]
    pigJob: PigJob
    placement: JobPlacement
    prestoJob: PrestoJob
    pysparkJob: PySparkJob
    reference: JobReference
    scheduling: JobScheduling
    sparkJob: SparkJob
    sparkRJob: SparkRJob
    sparkSqlJob: SparkSqlJob
    status: JobStatus
    statusHistory: _list[JobStatus]
    trinoJob: TrinoJob
    yarnApplications: _list[YarnApplication]

@typing.type_check_only
class JobData(typing_extensions.TypedDict, total=False):
    completionTime: str
    description: str
    jobGroup: str
    jobId: str
    killTasksSummary: dict[str, typing.Any]
    name: str
    numActiveStages: int
    numActiveTasks: int
    numCompletedIndices: int
    numCompletedStages: int
    numCompletedTasks: int
    numFailedStages: int
    numFailedTasks: int
    numKilledTasks: int
    numSkippedStages: int
    numSkippedTasks: int
    numTasks: int
    skippedStages: _list[int]
    sqlExecutionId: str
    stageIds: _list[str]
    status: typing_extensions.Literal[
        "JOB_EXECUTION_STATUS_UNSPECIFIED",
        "JOB_EXECUTION_STATUS_RUNNING",
        "JOB_EXECUTION_STATUS_SUCCEEDED",
        "JOB_EXECUTION_STATUS_FAILED",
        "JOB_EXECUTION_STATUS_UNKNOWN",
    ]
    submissionTime: str

@typing.type_check_only
class JobMetadata(typing_extensions.TypedDict, total=False):
    jobId: str
    operationType: str
    startTime: str
    status: JobStatus

@typing.type_check_only
class JobPlacement(typing_extensions.TypedDict, total=False):
    clusterLabels: dict[str, typing.Any]
    clusterName: str
    clusterUuid: str

@typing.type_check_only
class JobReference(typing_extensions.TypedDict, total=False):
    jobId: str
    projectId: str

@typing.type_check_only
class JobScheduling(typing_extensions.TypedDict, total=False):
    maxFailuresPerHour: int
    maxFailuresTotal: int

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    details: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "SETUP_DONE",
        "RUNNING",
        "CANCEL_PENDING",
        "CANCEL_STARTED",
        "CANCELLED",
        "DONE",
        "ERROR",
        "ATTEMPT_FAILURE",
    ]
    stateStartTime: str
    substate: typing_extensions.Literal[
        "UNSPECIFIED", "SUBMITTED", "QUEUED", "STALE_STATUS"
    ]

@typing.type_check_only
class JobsSummary(typing_extensions.TypedDict, total=False):
    activeJobs: int
    applicationId: str
    attempts: _list[ApplicationAttemptInfo]
    completedJobs: int
    failedJobs: int
    schedulingMode: str

@typing.type_check_only
class JupyterConfig(typing_extensions.TypedDict, total=False):
    displayName: str
    kernel: typing_extensions.Literal["KERNEL_UNSPECIFIED", "PYTHON", "SCALA"]

@typing.type_check_only
class KerberosConfig(typing_extensions.TypedDict, total=False):
    crossRealmTrustAdminServer: str
    crossRealmTrustKdc: str
    crossRealmTrustRealm: str
    crossRealmTrustSharedPasswordUri: str
    enableKerberos: bool
    kdcDbKeyUri: str
    keyPasswordUri: str
    keystorePasswordUri: str
    keystoreUri: str
    kmsKeyUri: str
    realm: str
    rootPrincipalPasswordUri: str
    tgtLifetimeHours: int
    truststorePasswordUri: str
    truststoreUri: str

@typing.type_check_only
class KubernetesClusterConfig(typing_extensions.TypedDict, total=False):
    gkeClusterConfig: GkeClusterConfig
    kubernetesNamespace: str
    kubernetesSoftwareConfig: KubernetesSoftwareConfig

@typing.type_check_only
class KubernetesSoftwareConfig(typing_extensions.TypedDict, total=False):
    componentVersion: dict[str, typing.Any]
    properties: dict[str, typing.Any]

@typing.type_check_only
class LifecycleConfig(typing_extensions.TypedDict, total=False):
    autoDeleteTime: str
    autoDeleteTtl: str
    idleDeleteTtl: str
    idleStartTime: str

@typing.type_check_only
class ListAutoscalingPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: _list[AutoscalingPolicy]

@typing.type_check_only
class ListBatchesResponse(typing_extensions.TypedDict, total=False):
    batches: _list[Batch]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSessionTemplatesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sessionTemplates: _list[SessionTemplate]

@typing.type_check_only
class ListSessionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[Session]

@typing.type_check_only
class ListWorkflowTemplatesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    templates: _list[WorkflowTemplate]
    unreachable: _list[str]

@typing.type_check_only
class LoggingConfig(typing_extensions.TypedDict, total=False):
    driverLogLevels: dict[str, typing.Any]

@typing.type_check_only
class ManagedCluster(typing_extensions.TypedDict, total=False):
    clusterName: str
    config: ClusterConfig
    labels: dict[str, typing.Any]

@typing.type_check_only
class ManagedGroupConfig(typing_extensions.TypedDict, total=False):
    instanceGroupManagerName: str
    instanceGroupManagerUri: str
    instanceTemplateName: str

@typing.type_check_only
class MemoryMetrics(typing_extensions.TypedDict, total=False):
    totalOffHeapStorageMemory: str
    totalOnHeapStorageMemory: str
    usedOffHeapStorageMemory: str
    usedOnHeapStorageMemory: str

@typing.type_check_only
class MetastoreConfig(typing_extensions.TypedDict, total=False):
    dataprocMetastoreService: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    metricOverrides: _list[str]
    metricSource: typing_extensions.Literal[
        "METRIC_SOURCE_UNSPECIFIED",
        "MONITORING_AGENT_DEFAULTS",
        "HDFS",
        "SPARK",
        "YARN",
        "SPARK_HISTORY_SERVER",
        "HIVESERVER2",
        "HIVEMETASTORE",
        "FLINK",
    ]

@typing.type_check_only
class NamespacedGkeDeploymentTarget(typing_extensions.TypedDict, total=False):
    clusterNamespace: str
    targetGkeCluster: str

@typing.type_check_only
class NodeGroup(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    name: str
    nodeGroupConfig: InstanceGroupConfig
    roles: _list[typing_extensions.Literal["ROLE_UNSPECIFIED", "DRIVER"]]

@typing.type_check_only
class NodeGroupAffinity(typing_extensions.TypedDict, total=False):
    nodeGroupUri: str

@typing.type_check_only
class NodeGroupOperationMetadata(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    description: str
    labels: dict[str, typing.Any]
    nodeGroupId: str
    operationType: typing_extensions.Literal[
        "NODE_GROUP_OPERATION_TYPE_UNSPECIFIED",
        "CREATE",
        "UPDATE",
        "DELETE",
        "RESIZE",
        "REPAIR",
        "UPDATE_LABELS",
        "START",
        "STOP",
    ]
    status: ClusterOperationStatus
    statusHistory: _list[ClusterOperationStatus]
    warnings: _list[str]

@typing.type_check_only
class NodeInitializationAction(typing_extensions.TypedDict, total=False):
    executableFile: str
    executionTimeout: str

@typing.type_check_only
class NodePool(typing_extensions.TypedDict, total=False):
    id: str
    instanceNames: _list[str]
    repairAction: typing_extensions.Literal["REPAIR_ACTION_UNSPECIFIED", "DELETE"]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrderedJob(typing_extensions.TypedDict, total=False):
    flinkJob: FlinkJob
    hadoopJob: HadoopJob
    hiveJob: HiveJob
    labels: dict[str, typing.Any]
    pigJob: PigJob
    prerequisiteStepIds: _list[str]
    prestoJob: PrestoJob
    pysparkJob: PySparkJob
    scheduling: JobScheduling
    sparkJob: SparkJob
    sparkRJob: SparkRJob
    sparkSqlJob: SparkSqlJob
    stepId: str
    trinoJob: TrinoJob

@typing.type_check_only
class OutputMetrics(typing_extensions.TypedDict, total=False):
    bytesWritten: str
    recordsWritten: str

@typing.type_check_only
class OutputQuantileMetrics(typing_extensions.TypedDict, total=False):
    bytesWritten: Quantiles
    recordsWritten: Quantiles

@typing.type_check_only
class ParameterValidation(typing_extensions.TypedDict, total=False):
    regex: RegexValidation
    values: ValueValidation

@typing.type_check_only
class PeripheralsConfig(typing_extensions.TypedDict, total=False):
    metastoreService: str
    sparkHistoryServerConfig: SparkHistoryServerConfig

@typing.type_check_only
class PigJob(typing_extensions.TypedDict, total=False):
    continueOnFailure: bool
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList
    scriptVariables: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PoolData(typing_extensions.TypedDict, total=False):
    name: str
    stageIds: _list[str]

@typing.type_check_only
class PrestoJob(typing_extensions.TypedDict, total=False):
    clientTags: _list[str]
    continueOnFailure: bool
    loggingConfig: LoggingConfig
    outputFormat: str
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList

@typing.type_check_only
class ProcessSummary(typing_extensions.TypedDict, total=False):
    addTime: str
    hostPort: str
    isActive: bool
    processId: str
    processLogs: dict[str, typing.Any]
    removeTime: str
    totalCores: int

@typing.type_check_only
class ProvisioningModelMix(typing_extensions.TypedDict, total=False):
    standardCapacityBase: int
    standardCapacityPercentAboveBase: int

@typing.type_check_only
class PyPiRepositoryConfig(typing_extensions.TypedDict, total=False):
    pypiRepository: str

@typing.type_check_only
class PySparkBatch(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    mainPythonFileUri: str
    pythonFileUris: _list[str]

@typing.type_check_only
class PySparkJob(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainPythonFileUri: str
    properties: dict[str, typing.Any]
    pythonFileUris: _list[str]

@typing.type_check_only
class Quantiles(typing_extensions.TypedDict, total=False):
    count: str
    maximum: str
    minimum: str
    percentile25: str
    percentile50: str
    percentile75: str
    sum: str

@typing.type_check_only
class QueryList(typing_extensions.TypedDict, total=False):
    queries: _list[str]

@typing.type_check_only
class RddDataDistribution(typing_extensions.TypedDict, total=False):
    address: str
    diskUsed: str
    memoryRemaining: str
    memoryUsed: str
    offHeapMemoryRemaining: str
    offHeapMemoryUsed: str
    onHeapMemoryRemaining: str
    onHeapMemoryUsed: str

@typing.type_check_only
class RddOperationCluster(typing_extensions.TypedDict, total=False):
    childClusters: _list[RddOperationCluster]
    childNodes: _list[RddOperationNode]
    name: str
    rddClusterId: str

@typing.type_check_only
class RddOperationEdge(typing_extensions.TypedDict, total=False):
    fromId: int
    toId: int

@typing.type_check_only
class RddOperationGraph(typing_extensions.TypedDict, total=False):
    edges: _list[RddOperationEdge]
    incomingEdges: _list[RddOperationEdge]
    outgoingEdges: _list[RddOperationEdge]
    rootCluster: RddOperationCluster
    stageId: str

@typing.type_check_only
class RddOperationNode(typing_extensions.TypedDict, total=False):
    barrier: bool
    cached: bool
    callsite: str
    name: str
    nodeId: int
    outputDeterministicLevel: typing_extensions.Literal[
        "DETERMINISTIC_LEVEL_UNSPECIFIED",
        "DETERMINISTIC_LEVEL_DETERMINATE",
        "DETERMINISTIC_LEVEL_UNORDERED",
        "DETERMINISTIC_LEVEL_INDETERMINATE",
    ]

@typing.type_check_only
class RddPartitionInfo(typing_extensions.TypedDict, total=False):
    blockName: str
    diskUsed: str
    executors: _list[str]
    memoryUsed: str
    storageLevel: str

@typing.type_check_only
class RddStorageInfo(typing_extensions.TypedDict, total=False):
    dataDistribution: _list[RddDataDistribution]
    diskUsed: str
    memoryUsed: str
    name: str
    numCachedPartitions: int
    numPartitions: int
    partitions: _list[RddPartitionInfo]
    rddStorageId: int
    storageLevel: str

@typing.type_check_only
class RegexValidation(typing_extensions.TypedDict, total=False):
    regexes: _list[str]

@typing.type_check_only
class RepairClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: ClusterToRepair
    clusterUuid: str
    gracefulDecommissionTimeout: str
    nodePools: _list[NodePool]
    parentOperationId: str
    requestId: str

@typing.type_check_only
class RepairNodeGroupRequest(typing_extensions.TypedDict, total=False):
    instanceNames: _list[str]
    repairAction: typing_extensions.Literal["REPAIR_ACTION_UNSPECIFIED", "REPLACE"]
    requestId: str

@typing.type_check_only
class RepositoryConfig(typing_extensions.TypedDict, total=False):
    pypiRepositoryConfig: PyPiRepositoryConfig

@typing.type_check_only
class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResizeNodeGroupRequest(typing_extensions.TypedDict, total=False):
    gracefulDecommissionTimeout: str
    parentOperationId: str
    requestId: str
    size: int

@typing.type_check_only
class ResourceInformation(typing_extensions.TypedDict, total=False):
    addresses: _list[str]
    name: str

@typing.type_check_only
class ResourceProfileInfo(typing_extensions.TypedDict, total=False):
    executorResources: dict[str, typing.Any]
    resourceProfileId: int
    taskResources: dict[str, typing.Any]

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    autotuningConfig: AutotuningConfig
    cohort: str
    containerImage: str
    properties: dict[str, typing.Any]
    repositoryConfig: RepositoryConfig
    version: str

@typing.type_check_only
class RuntimeInfo(typing_extensions.TypedDict, total=False):
    approximateUsage: UsageMetrics
    currentUsage: UsageSnapshot
    diagnosticOutputUri: str
    endpoints: dict[str, typing.Any]
    outputUri: str

@typing.type_check_only
class SearchSessionSparkApplicationExecutorStageSummaryResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStageExecutors: _list[ExecutorStageSummary]

@typing.type_check_only
class SearchSessionSparkApplicationExecutorsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationExecutors: _list[ExecutorSummary]

@typing.type_check_only
class SearchSessionSparkApplicationJobsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationJobs: _list[JobData]

@typing.type_check_only
class SearchSessionSparkApplicationSqlQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationSqlQueries: _list[SqlExecutionUiData]

@typing.type_check_only
class SearchSessionSparkApplicationStageAttemptTasksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStageAttemptTasks: _list[TaskData]

@typing.type_check_only
class SearchSessionSparkApplicationStageAttemptsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStageAttempts: _list[StageData]

@typing.type_check_only
class SearchSessionSparkApplicationStagesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStages: _list[StageData]

@typing.type_check_only
class SearchSessionSparkApplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sparkApplications: _list[SparkApplication]

@typing.type_check_only
class SearchSparkApplicationExecutorStageSummaryResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStageExecutors: _list[ExecutorStageSummary]

@typing.type_check_only
class SearchSparkApplicationExecutorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sparkApplicationExecutors: _list[ExecutorSummary]

@typing.type_check_only
class SearchSparkApplicationJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sparkApplicationJobs: _list[JobData]

@typing.type_check_only
class SearchSparkApplicationSqlQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationSqlQueries: _list[SqlExecutionUiData]

@typing.type_check_only
class SearchSparkApplicationStageAttemptTasksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStageAttemptTasks: _list[TaskData]

@typing.type_check_only
class SearchSparkApplicationStageAttemptsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sparkApplicationStageAttempts: _list[StageData]

@typing.type_check_only
class SearchSparkApplicationStagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sparkApplicationStages: _list[StageData]

@typing.type_check_only
class SearchSparkApplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sparkApplications: _list[SparkApplication]

@typing.type_check_only
class SecurityConfig(typing_extensions.TypedDict, total=False):
    identityConfig: IdentityConfig
    kerberosConfig: KerberosConfig

@typing.type_check_only
class Session(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    environmentConfig: EnvironmentConfig
    jupyterSession: JupyterConfig
    labels: dict[str, typing.Any]
    name: str
    runtimeConfig: RuntimeConfig
    runtimeInfo: RuntimeInfo
    sessionTemplate: str
    sparkConnectSession: SparkConnectConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "TERMINATING", "TERMINATED", "FAILED"
    ]
    stateHistory: _list[SessionStateHistory]
    stateMessage: str
    stateTime: str
    user: str
    uuid: str

@typing.type_check_only
class SessionOperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    doneTime: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "SESSION_OPERATION_TYPE_UNSPECIFIED", "CREATE", "TERMINATE", "DELETE"
    ]
    session: str
    sessionUuid: str
    warnings: _list[str]

@typing.type_check_only
class SessionStateHistory(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "TERMINATING", "TERMINATED", "FAILED"
    ]
    stateMessage: str
    stateStartTime: str

@typing.type_check_only
class SessionTemplate(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    description: str
    environmentConfig: EnvironmentConfig
    jupyterSession: JupyterConfig
    labels: dict[str, typing.Any]
    name: str
    runtimeConfig: RuntimeConfig
    sparkConnectSession: SparkConnectConfig
    updateTime: str
    uuid: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class ShufflePushReadMetrics(typing_extensions.TypedDict, total=False):
    corruptMergedBlockChunks: str
    localMergedBlocksFetched: str
    localMergedBytesRead: str
    localMergedChunksFetched: str
    mergedFetchFallbackCount: str
    remoteMergedBlocksFetched: str
    remoteMergedBytesRead: str
    remoteMergedChunksFetched: str
    remoteMergedReqsDuration: str

@typing.type_check_only
class ShufflePushReadQuantileMetrics(typing_extensions.TypedDict, total=False):
    corruptMergedBlockChunks: Quantiles
    localMergedBlocksFetched: Quantiles
    localMergedBytesRead: Quantiles
    localMergedChunksFetched: Quantiles
    mergedFetchFallbackCount: Quantiles
    remoteMergedBlocksFetched: Quantiles
    remoteMergedBytesRead: Quantiles
    remoteMergedChunksFetched: Quantiles
    remoteMergedReqsDuration: Quantiles

@typing.type_check_only
class ShuffleReadMetrics(typing_extensions.TypedDict, total=False):
    fetchWaitTimeMillis: str
    localBlocksFetched: str
    localBytesRead: str
    recordsRead: str
    remoteBlocksFetched: str
    remoteBytesRead: str
    remoteBytesReadToDisk: str
    remoteReqsDuration: str
    shufflePushReadMetrics: ShufflePushReadMetrics

@typing.type_check_only
class ShuffleReadQuantileMetrics(typing_extensions.TypedDict, total=False):
    fetchWaitTimeMillis: Quantiles
    localBlocksFetched: Quantiles
    readBytes: Quantiles
    readRecords: Quantiles
    remoteBlocksFetched: Quantiles
    remoteBytesRead: Quantiles
    remoteBytesReadToDisk: Quantiles
    remoteReqsDuration: Quantiles
    shufflePushReadMetrics: ShufflePushReadQuantileMetrics
    totalBlocksFetched: Quantiles

@typing.type_check_only
class ShuffleWriteMetrics(typing_extensions.TypedDict, total=False):
    bytesWritten: str
    recordsWritten: str
    writeTimeNanos: str

@typing.type_check_only
class ShuffleWriteQuantileMetrics(typing_extensions.TypedDict, total=False):
    writeBytes: Quantiles
    writeRecords: Quantiles
    writeTimeNanos: Quantiles

@typing.type_check_only
class SinkProgress(typing_extensions.TypedDict, total=False):
    description: str
    metrics: dict[str, typing.Any]
    numOutputRows: str

@typing.type_check_only
class SoftwareConfig(typing_extensions.TypedDict, total=False):
    imageVersion: str
    optionalComponents: _list[
        typing_extensions.Literal[
            "COMPONENT_UNSPECIFIED",
            "ANACONDA",
            "DOCKER",
            "DRUID",
            "FLINK",
            "HBASE",
            "HIVE_WEBHCAT",
            "HUDI",
            "JUPYTER",
            "PRESTO",
            "TRINO",
            "RANGER",
            "SOLR",
            "ZEPPELIN",
            "ZOOKEEPER",
        ]
    ]
    properties: dict[str, typing.Any]

@typing.type_check_only
class SourceProgress(typing_extensions.TypedDict, total=False):
    description: str
    endOffset: str
    inputRowsPerSecond: float
    latestOffset: str
    metrics: dict[str, typing.Any]
    numInputRows: str
    processedRowsPerSecond: float
    startOffset: str

@typing.type_check_only
class SparkApplication(typing_extensions.TypedDict, total=False):
    application: ApplicationInfo
    name: str

@typing.type_check_only
class SparkBatch(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    mainClass: str
    mainJarFileUri: str

@typing.type_check_only
class SparkConnectConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SparkHistoryServerConfig(typing_extensions.TypedDict, total=False):
    dataprocCluster: str

@typing.type_check_only
class SparkJob(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainClass: str
    mainJarFileUri: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class SparkPlanGraph(typing_extensions.TypedDict, total=False):
    edges: _list[SparkPlanGraphEdge]
    executionId: str
    nodes: _list[SparkPlanGraphNodeWrapper]

@typing.type_check_only
class SparkPlanGraphCluster(typing_extensions.TypedDict, total=False):
    desc: str
    metrics: _list[SqlPlanMetric]
    name: str
    nodes: _list[SparkPlanGraphNodeWrapper]
    sparkPlanGraphClusterId: str

@typing.type_check_only
class SparkPlanGraphEdge(typing_extensions.TypedDict, total=False):
    fromId: str
    toId: str

@typing.type_check_only
class SparkPlanGraphNode(typing_extensions.TypedDict, total=False):
    desc: str
    metrics: _list[SqlPlanMetric]
    name: str
    sparkPlanGraphNodeId: str

@typing.type_check_only
class SparkPlanGraphNodeWrapper(typing_extensions.TypedDict, total=False):
    cluster: SparkPlanGraphCluster
    node: SparkPlanGraphNode

@typing.type_check_only
class SparkRBatch(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    mainRFileUri: str

@typing.type_check_only
class SparkRJob(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    loggingConfig: LoggingConfig
    mainRFileUri: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class SparkRuntimeInfo(typing_extensions.TypedDict, total=False):
    javaHome: str
    javaVersion: str
    scalaVersion: str

@typing.type_check_only
class SparkSqlBatch(typing_extensions.TypedDict, total=False):
    jarFileUris: _list[str]
    queryFileUri: str
    queryVariables: dict[str, typing.Any]

@typing.type_check_only
class SparkSqlJob(typing_extensions.TypedDict, total=False):
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList
    scriptVariables: dict[str, typing.Any]

@typing.type_check_only
class SparkStandaloneAutoscalingConfig(typing_extensions.TypedDict, total=False):
    gracefulDecommissionTimeout: str
    removeOnlyIdleWorkers: bool
    scaleDownFactor: float
    scaleDownMinWorkerFraction: float
    scaleUpFactor: float
    scaleUpMinWorkerFraction: float

@typing.type_check_only
class SparkWrapperObject(typing_extensions.TypedDict, total=False):
    appSummary: AppSummary
    applicationEnvironmentInfo: ApplicationEnvironmentInfo
    applicationId: str
    applicationInfo: ApplicationInfo
    eventTimestamp: str
    executorStageSummary: ExecutorStageSummary
    executorSummary: ExecutorSummary
    jobData: JobData
    poolData: PoolData
    processSummary: ProcessSummary
    rddOperationGraph: RddOperationGraph
    rddStorageInfo: RddStorageInfo
    resourceProfileInfo: ResourceProfileInfo
    sparkPlanGraph: SparkPlanGraph
    speculationStageSummary: SpeculationStageSummary
    sqlExecutionUiData: SqlExecutionUiData
    stageData: StageData
    streamBlockData: StreamBlockData
    streamingQueryData: StreamingQueryData
    streamingQueryProgress: StreamingQueryProgress
    taskData: TaskData

@typing.type_check_only
class SpeculationStageSummary(typing_extensions.TypedDict, total=False):
    numActiveTasks: int
    numCompletedTasks: int
    numFailedTasks: int
    numKilledTasks: int
    numTasks: int
    stageAttemptId: int
    stageId: str

@typing.type_check_only
class SqlExecutionUiData(typing_extensions.TypedDict, total=False):
    completionTime: str
    description: str
    details: str
    errorMessage: str
    executionId: str
    jobs: dict[str, typing.Any]
    metricValues: dict[str, typing.Any]
    metricValuesIsNull: bool
    metrics: _list[SqlPlanMetric]
    modifiedConfigs: dict[str, typing.Any]
    physicalPlanDescription: str
    rootExecutionId: str
    stages: _list[str]
    submissionTime: str

@typing.type_check_only
class SqlPlanMetric(typing_extensions.TypedDict, total=False):
    accumulatorId: str
    metricType: str
    name: str

@typing.type_check_only
class StageAttemptTasksSummary(typing_extensions.TypedDict, total=False):
    applicationId: str
    numFailedTasks: int
    numKilledTasks: int
    numPendingTasks: int
    numRunningTasks: int
    numSuccessTasks: int
    numTasks: int
    stageAttemptId: int
    stageId: str

@typing.type_check_only
class StageData(typing_extensions.TypedDict, total=False):
    accumulatorUpdates: _list[AccumulableInfo]
    completionTime: str
    description: str
    details: str
    executorMetricsDistributions: ExecutorMetricsDistributions
    executorSummary: dict[str, typing.Any]
    failureReason: str
    firstTaskLaunchedTime: str
    isShufflePushEnabled: bool
    jobIds: _list[str]
    killedTasksSummary: dict[str, typing.Any]
    locality: dict[str, typing.Any]
    name: str
    numActiveTasks: int
    numCompleteTasks: int
    numCompletedIndices: int
    numFailedTasks: int
    numKilledTasks: int
    numTasks: int
    parentStageIds: _list[str]
    peakExecutorMetrics: ExecutorMetrics
    rddIds: _list[str]
    resourceProfileId: int
    schedulingPool: str
    shuffleMergersCount: int
    speculationSummary: SpeculationStageSummary
    stageAttemptId: int
    stageId: str
    stageMetrics: StageMetrics
    status: typing_extensions.Literal[
        "STAGE_STATUS_UNSPECIFIED",
        "STAGE_STATUS_ACTIVE",
        "STAGE_STATUS_COMPLETE",
        "STAGE_STATUS_FAILED",
        "STAGE_STATUS_PENDING",
        "STAGE_STATUS_SKIPPED",
    ]
    submissionTime: str
    taskQuantileMetrics: TaskQuantileMetrics
    tasks: dict[str, typing.Any]

@typing.type_check_only
class StageInputMetrics(typing_extensions.TypedDict, total=False):
    bytesRead: str
    recordsRead: str

@typing.type_check_only
class StageMetrics(typing_extensions.TypedDict, total=False):
    diskBytesSpilled: str
    executorCpuTimeNanos: str
    executorDeserializeCpuTimeNanos: str
    executorDeserializeTimeMillis: str
    executorRunTimeMillis: str
    jvmGcTimeMillis: str
    memoryBytesSpilled: str
    peakExecutionMemoryBytes: str
    resultSerializationTimeMillis: str
    resultSize: str
    stageInputMetrics: StageInputMetrics
    stageOutputMetrics: StageOutputMetrics
    stageShuffleReadMetrics: StageShuffleReadMetrics
    stageShuffleWriteMetrics: StageShuffleWriteMetrics

@typing.type_check_only
class StageOutputMetrics(typing_extensions.TypedDict, total=False):
    bytesWritten: str
    recordsWritten: str

@typing.type_check_only
class StageShufflePushReadMetrics(typing_extensions.TypedDict, total=False):
    corruptMergedBlockChunks: str
    localMergedBlocksFetched: str
    localMergedBytesRead: str
    localMergedChunksFetched: str
    mergedFetchFallbackCount: str
    remoteMergedBlocksFetched: str
    remoteMergedBytesRead: str
    remoteMergedChunksFetched: str
    remoteMergedReqsDuration: str

@typing.type_check_only
class StageShuffleReadMetrics(typing_extensions.TypedDict, total=False):
    bytesRead: str
    fetchWaitTimeMillis: str
    localBlocksFetched: str
    localBytesRead: str
    recordsRead: str
    remoteBlocksFetched: str
    remoteBytesRead: str
    remoteBytesReadToDisk: str
    remoteReqsDuration: str
    stageShufflePushReadMetrics: StageShufflePushReadMetrics

@typing.type_check_only
class StageShuffleWriteMetrics(typing_extensions.TypedDict, total=False):
    bytesWritten: str
    recordsWritten: str
    writeTimeNanos: str

@typing.type_check_only
class StagesSummary(typing_extensions.TypedDict, total=False):
    applicationId: str
    numActiveStages: int
    numCompletedStages: int
    numFailedStages: int
    numPendingStages: int
    numSkippedStages: int

@typing.type_check_only
class StartClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    requestId: str

@typing.type_check_only
class StartupConfig(typing_extensions.TypedDict, total=False):
    requiredRegistrationFraction: float

@typing.type_check_only
class StateHistory(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
    ]
    stateMessage: str
    stateStartTime: str

@typing.type_check_only
class StateOperatorProgress(typing_extensions.TypedDict, total=False):
    allRemovalsTimeMs: str
    allUpdatesTimeMs: str
    commitTimeMs: str
    customMetrics: dict[str, typing.Any]
    memoryUsedBytes: str
    numRowsDroppedByWatermark: str
    numRowsRemoved: str
    numRowsTotal: str
    numRowsUpdated: str
    numShufflePartitions: str
    numStateStoreInstances: str
    operatorName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    requestId: str

@typing.type_check_only
class StreamBlockData(typing_extensions.TypedDict, total=False):
    deserialized: bool
    diskSize: str
    executorId: str
    hostPort: str
    memSize: str
    name: str
    storageLevel: str
    useDisk: bool
    useMemory: bool

@typing.type_check_only
class StreamingQueryData(typing_extensions.TypedDict, total=False):
    endTimestamp: str
    exception: str
    isActive: bool
    name: str
    runId: str
    startTimestamp: str
    streamingQueryId: str

@typing.type_check_only
class StreamingQueryProgress(typing_extensions.TypedDict, total=False):
    batchDuration: str
    batchId: str
    durationMillis: dict[str, typing.Any]
    eventTime: dict[str, typing.Any]
    name: str
    observedMetrics: dict[str, typing.Any]
    runId: str
    sink: SinkProgress
    sources: _list[SourceProgress]
    stateOperators: _list[StateOperatorProgress]
    streamingQueryProgressId: str
    timestamp: str

@typing.type_check_only
class SubmitJobRequest(typing_extensions.TypedDict, total=False):
    job: Job
    requestId: str

@typing.type_check_only
class SummarizeSessionSparkApplicationExecutorsResponse(
    typing_extensions.TypedDict, total=False
):
    activeExecutorSummary: ConsolidatedExecutorSummary
    applicationId: str
    deadExecutorSummary: ConsolidatedExecutorSummary
    totalExecutorSummary: ConsolidatedExecutorSummary

@typing.type_check_only
class SummarizeSessionSparkApplicationJobsResponse(
    typing_extensions.TypedDict, total=False
):
    jobsSummary: JobsSummary

@typing.type_check_only
class SummarizeSessionSparkApplicationStageAttemptTasksResponse(
    typing_extensions.TypedDict, total=False
):
    stageAttemptTasksSummary: StageAttemptTasksSummary

@typing.type_check_only
class SummarizeSessionSparkApplicationStagesResponse(
    typing_extensions.TypedDict, total=False
):
    stagesSummary: StagesSummary

@typing.type_check_only
class SummarizeSparkApplicationExecutorsResponse(
    typing_extensions.TypedDict, total=False
):
    activeExecutorSummary: ConsolidatedExecutorSummary
    applicationId: str
    deadExecutorSummary: ConsolidatedExecutorSummary
    totalExecutorSummary: ConsolidatedExecutorSummary

@typing.type_check_only
class SummarizeSparkApplicationJobsResponse(typing_extensions.TypedDict, total=False):
    jobsSummary: JobsSummary

@typing.type_check_only
class SummarizeSparkApplicationStageAttemptTasksResponse(
    typing_extensions.TypedDict, total=False
):
    stageAttemptTasksSummary: StageAttemptTasksSummary

@typing.type_check_only
class SummarizeSparkApplicationStagesResponse(typing_extensions.TypedDict, total=False):
    stagesSummary: StagesSummary

@typing.type_check_only
class TaskData(typing_extensions.TypedDict, total=False):
    accumulatorUpdates: _list[AccumulableInfo]
    attempt: int
    durationMillis: str
    errorMessage: str
    executorId: str
    executorLogs: dict[str, typing.Any]
    gettingResultTimeMillis: str
    hasMetrics: bool
    host: str
    index: int
    launchTime: str
    partitionId: int
    resultFetchStart: str
    schedulerDelayMillis: str
    speculative: bool
    stageAttemptId: int
    stageId: str
    status: str
    taskId: str
    taskLocality: str
    taskMetrics: TaskMetrics

@typing.type_check_only
class TaskMetrics(typing_extensions.TypedDict, total=False):
    diskBytesSpilled: str
    executorCpuTimeNanos: str
    executorDeserializeCpuTimeNanos: str
    executorDeserializeTimeMillis: str
    executorRunTimeMillis: str
    inputMetrics: InputMetrics
    jvmGcTimeMillis: str
    memoryBytesSpilled: str
    outputMetrics: OutputMetrics
    peakExecutionMemoryBytes: str
    resultSerializationTimeMillis: str
    resultSize: str
    shuffleReadMetrics: ShuffleReadMetrics
    shuffleWriteMetrics: ShuffleWriteMetrics

@typing.type_check_only
class TaskQuantileMetrics(typing_extensions.TypedDict, total=False):
    diskBytesSpilled: Quantiles
    durationMillis: Quantiles
    executorCpuTimeNanos: Quantiles
    executorDeserializeCpuTimeNanos: Quantiles
    executorDeserializeTimeMillis: Quantiles
    executorRunTimeMillis: Quantiles
    gettingResultTimeMillis: Quantiles
    inputMetrics: InputQuantileMetrics
    jvmGcTimeMillis: Quantiles
    memoryBytesSpilled: Quantiles
    outputMetrics: OutputQuantileMetrics
    peakExecutionMemoryBytes: Quantiles
    resultSerializationTimeMillis: Quantiles
    resultSize: Quantiles
    schedulerDelayMillis: Quantiles
    shuffleReadMetrics: ShuffleReadQuantileMetrics
    shuffleWriteMetrics: ShuffleWriteQuantileMetrics

@typing.type_check_only
class TaskResourceRequest(typing_extensions.TypedDict, total=False):
    amount: float
    resourceName: str

@typing.type_check_only
class TemplateParameter(typing_extensions.TypedDict, total=False):
    description: str
    fields: _list[str]
    name: str
    validation: ParameterValidation

@typing.type_check_only
class TerminateSessionRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrinoJob(typing_extensions.TypedDict, total=False):
    clientTags: _list[str]
    continueOnFailure: bool
    loggingConfig: LoggingConfig
    outputFormat: str
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList

@typing.type_check_only
class UsageMetrics(typing_extensions.TypedDict, total=False):
    acceleratorType: str
    milliAcceleratorSeconds: str
    milliDcuSeconds: str
    shuffleStorageGbSeconds: str

@typing.type_check_only
class UsageSnapshot(typing_extensions.TypedDict, total=False):
    acceleratorType: str
    milliAccelerator: str
    milliDcu: str
    milliDcuPremium: str
    shuffleStorageGb: str
    shuffleStorageGbPremium: str
    snapshotTime: str

@typing.type_check_only
class ValueValidation(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class VirtualClusterConfig(typing_extensions.TypedDict, total=False):
    auxiliaryServicesConfig: AuxiliaryServicesConfig
    kubernetesClusterConfig: KubernetesClusterConfig
    stagingBucket: str

@typing.type_check_only
class WorkflowGraph(typing_extensions.TypedDict, total=False):
    nodes: _list[WorkflowNode]

@typing.type_check_only
class WorkflowMetadata(typing_extensions.TypedDict, total=False):
    clusterName: str
    clusterUuid: str
    createCluster: ClusterOperation
    dagEndTime: str
    dagStartTime: str
    dagTimeout: str
    deleteCluster: ClusterOperation
    endTime: str
    graph: WorkflowGraph
    parameters: dict[str, typing.Any]
    startTime: str
    state: typing_extensions.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    template: str
    version: int

@typing.type_check_only
class WorkflowNode(typing_extensions.TypedDict, total=False):
    error: str
    jobId: str
    prerequisiteStepIds: _list[str]
    state: typing_extensions.Literal[
        "NODE_STATE_UNSPECIFIED",
        "BLOCKED",
        "RUNNABLE",
        "RUNNING",
        "COMPLETED",
        "FAILED",
    ]
    stepId: str

@typing.type_check_only
class WorkflowTemplate(typing_extensions.TypedDict, total=False):
    createTime: str
    dagTimeout: str
    encryptionConfig: GoogleCloudDataprocV1WorkflowTemplateEncryptionConfig
    id: str
    jobs: _list[OrderedJob]
    labels: dict[str, typing.Any]
    name: str
    parameters: _list[TemplateParameter]
    placement: WorkflowTemplatePlacement
    updateTime: str
    version: int

@typing.type_check_only
class WorkflowTemplatePlacement(typing_extensions.TypedDict, total=False):
    clusterSelector: ClusterSelector
    managedCluster: ManagedCluster

@typing.type_check_only
class WriteSessionSparkApplicationContextRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    sparkWrapperObjects: _list[SparkWrapperObject]

@typing.type_check_only
class WriteSessionSparkApplicationContextResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class WriteSparkApplicationContextRequest(typing_extensions.TypedDict, total=False):
    parent: str
    sparkWrapperObjects: _list[SparkWrapperObject]

@typing.type_check_only
class WriteSparkApplicationContextResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class YarnApplication(typing_extensions.TypedDict, total=False):
    name: str
    progress: float
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NEW",
        "NEW_SAVING",
        "SUBMITTED",
        "ACCEPTED",
        "RUNNING",
        "FINISHED",
        "FAILED",
        "KILLED",
    ]
    trackingUrl: str
