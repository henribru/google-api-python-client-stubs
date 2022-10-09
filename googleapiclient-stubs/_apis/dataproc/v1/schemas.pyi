import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorTypeUri: str

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
    ]
    stateStartTime: str
    substate: typing_extensions.Literal["UNSPECIFIED", "UNHEALTHY", "STALE_STATUS"]

@typing.type_check_only
class ConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
    enableConfidentialCompute: bool

@typing.type_check_only
class DataprocMetricConfig(typing_extensions.TypedDict, total=False):
    metrics: _list[Metric]

@typing.type_check_only
class DiagnoseClusterRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DiagnoseClusterResults(typing_extensions.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class DiskConfig(typing_extensions.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str
    localSsdInterface: str
    numLocalSsds: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    gcePdKmsKeyName: str

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
    subnetworkUri: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
class GceNodePoolOperationMetadata(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    description: str
    gceNodePoolId: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "GCE_NODE_POOL_OPERATION_TYPE_UNSPECIFIED",
        "CREATE",
        "UPDATE",
        "DELETE",
        "RESIZE",
    ]
    status: ClusterOperationStatus
    statusHistory: _list[ClusterOperationStatus]
    warnings: _list[str]

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
    roles: _list[str]

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
class InstanceGroupAutoscalingPolicyConfig(typing_extensions.TypedDict, total=False):
    maxInstances: int
    minInstances: int
    weight: int

@typing.type_check_only
class InstanceGroupConfig(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    diskConfig: DiskConfig
    imageUri: str
    instanceNames: _list[str]
    instanceReferences: _list[InstanceReference]
    isPreemptible: bool
    machineTypeUri: str
    managedGroupConfig: ManagedGroupConfig
    minCpuPlatform: str
    numInstances: int
    preemptibility: typing_extensions.Literal[
        "PREEMPTIBILITY_UNSPECIFIED", "NON_PREEMPTIBLE", "PREEMPTIBLE", "SPOT"
    ]

@typing.type_check_only
class InstanceReference(typing_extensions.TypedDict, total=False):
    instanceId: str
    instanceName: str
    publicEciesKey: str
    publicKey: str

@typing.type_check_only
class InstantiateWorkflowTemplateRequest(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    requestId: str
    version: int

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    done: bool
    driverControlFilesUri: str
    driverOutputResourceUri: str
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

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListWorkflowTemplatesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    templates: _list[WorkflowTemplate]

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
    instanceTemplateName: str

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
    ]

@typing.type_check_only
class NamespacedGkeDeploymentTarget(typing_extensions.TypedDict, total=False):
    clusterNamespace: str
    targetGkeCluster: str

@typing.type_check_only
class NodeGroupAffinity(typing_extensions.TypedDict, total=False):
    nodeGroupUri: str

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
class PrestoJob(typing_extensions.TypedDict, total=False):
    clientTags: _list[str]
    continueOnFailure: bool
    loggingConfig: LoggingConfig
    outputFormat: str
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList

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
class QueryList(typing_extensions.TypedDict, total=False):
    queries: _list[str]

@typing.type_check_only
class RegexValidation(typing_extensions.TypedDict, total=False):
    regexes: _list[str]

@typing.type_check_only
class RepairClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    gracefulDecommissionTimeout: str
    nodePools: _list[NodePool]
    parentOperationId: str
    requestId: str

@typing.type_check_only
class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    containerImage: str
    properties: dict[str, typing.Any]
    version: str

@typing.type_check_only
class RuntimeInfo(typing_extensions.TypedDict, total=False):
    diagnosticOutputUri: str
    endpoints: dict[str, typing.Any]
    outputUri: str

@typing.type_check_only
class SecurityConfig(typing_extensions.TypedDict, total=False):
    identityConfig: IdentityConfig
    kerberosConfig: KerberosConfig

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
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class SoftwareConfig(typing_extensions.TypedDict, total=False):
    imageVersion: str
    optionalComponents: _list[str]
    properties: dict[str, typing.Any]

@typing.type_check_only
class SparkBatch(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    mainClass: str
    mainJarFileUri: str

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
    scaleDownFactor: float
    scaleDownMinWorkerFraction: float
    scaleUpFactor: float
    scaleUpMinWorkerFraction: float

@typing.type_check_only
class StartClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    requestId: str

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    requestId: str

@typing.type_check_only
class SubmitJobRequest(typing_extensions.TypedDict, total=False):
    job: Job
    requestId: str

@typing.type_check_only
class TemplateParameter(typing_extensions.TypedDict, total=False):
    description: str
    fields: _list[str]
    name: str
    validation: ParameterValidation

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
