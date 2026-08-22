import typing

_list = list

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    acceleratorCount: int
    acceleratorTypeUri: str

@typing.type_check_only
class AutoscalingConfig(typing.TypedDict, total=False):
    policyUri: str

@typing.type_check_only
class AutoscalingPolicy(typing.TypedDict, total=False):
    basicAlgorithm: BasicAutoscalingAlgorithm
    id: str
    name: str
    secondaryWorkerConfig: InstanceGroupAutoscalingPolicyConfig
    workerConfig: InstanceGroupAutoscalingPolicyConfig

@typing.type_check_only
class BasicAutoscalingAlgorithm(typing.TypedDict, total=False):
    cooldownPeriod: str
    yarnConfig: BasicYarnAutoscalingConfig

@typing.type_check_only
class BasicYarnAutoscalingConfig(typing.TypedDict, total=False):
    gracefulDecommissionTimeout: str
    scaleDownFactor: float
    scaleDownMinWorkerFraction: float
    scaleUpFactor: float
    scaleUpMinWorkerFraction: float

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    clusterName: str
    clusterUuid: str
    config: ClusterConfig
    labels: dict[str, typing.Any]
    metrics: ClusterMetrics
    projectId: str
    status: ClusterStatus
    statusHistory: _list[ClusterStatus]

@typing.type_check_only
class ClusterConfig(typing.TypedDict, total=False):
    autoscalingConfig: AutoscalingConfig
    configBucket: str
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
class ClusterMetrics(typing.TypedDict, total=False):
    hdfsMetrics: dict[str, typing.Any]
    yarnMetrics: dict[str, typing.Any]

@typing.type_check_only
class ClusterOperation(typing.TypedDict, total=False):
    done: bool
    error: str
    operationId: str

@typing.type_check_only
class ClusterOperationMetadata(typing.TypedDict, total=False):
    clusterName: str
    clusterUuid: str
    description: str
    labels: dict[str, typing.Any]
    operationType: str
    status: ClusterOperationStatus
    statusHistory: _list[ClusterOperationStatus]
    warnings: _list[str]

@typing.type_check_only
class ClusterOperationStatus(typing.TypedDict, total=False):
    details: str
    innerState: str
    state: typing.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    stateStartTime: str

@typing.type_check_only
class ClusterSelector(typing.TypedDict, total=False):
    clusterLabels: dict[str, typing.Any]
    zone: str

@typing.type_check_only
class ClusterStatus(typing.TypedDict, total=False):
    detail: str
    state: typing.Literal[
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
    ]
    stateStartTime: str
    substate: typing.Literal["UNSPECIFIED", "UNHEALTHY", "STALE_STATUS"]

@typing.type_check_only
class DiagnoseClusterRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DiagnoseClusterResults(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class DiskConfig(typing.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str
    numLocalSsds: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    gcePdKmsKeyName: str

@typing.type_check_only
class EndpointConfig(typing.TypedDict, total=False):
    enableHttpPortAccess: bool
    httpPorts: dict[str, typing.Any]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GceClusterConfig(typing.TypedDict, total=False):
    internalIpOnly: bool
    metadata: dict[str, typing.Any]
    networkUri: str
    nodeGroupAffinity: NodeGroupAffinity
    privateIpv6GoogleAccess: typing.Literal[
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
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GkeClusterConfig(typing.TypedDict, total=False):
    namespacedGkeDeploymentTarget: NamespacedGkeDeploymentTarget

@typing.type_check_only
class HadoopJob(typing.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainClass: str
    mainJarFileUri: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class HiveJob(typing.TypedDict, total=False):
    continueOnFailure: bool
    jarFileUris: _list[str]
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList
    scriptVariables: dict[str, typing.Any]

@typing.type_check_only
class InjectCredentialsRequest(typing.TypedDict, total=False):
    clusterUuid: str
    credentialsCiphertext: str

@typing.type_check_only
class InstanceGroupAutoscalingPolicyConfig(typing.TypedDict, total=False):
    maxInstances: int
    minInstances: int
    weight: int

@typing.type_check_only
class InstanceGroupConfig(typing.TypedDict, total=False):
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
    preemptibility: typing.Literal[
        "PREEMPTIBILITY_UNSPECIFIED", "NON_PREEMPTIBLE", "PREEMPTIBLE"
    ]

@typing.type_check_only
class InstanceReference(typing.TypedDict, total=False):
    instanceId: str
    instanceName: str
    publicKey: str

@typing.type_check_only
class InstantiateWorkflowTemplateRequest(typing.TypedDict, total=False):
    instanceId: str
    parameters: dict[str, typing.Any]
    requestId: str
    version: int

@typing.type_check_only
class Job(typing.TypedDict, total=False):
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
    submittedBy: str
    yarnApplications: _list[YarnApplication]

@typing.type_check_only
class JobMetadata(typing.TypedDict, total=False):
    jobId: str
    operationType: str
    startTime: str
    status: JobStatus

@typing.type_check_only
class JobPlacement(typing.TypedDict, total=False):
    clusterLabels: dict[str, typing.Any]
    clusterName: str
    clusterUuid: str

@typing.type_check_only
class JobReference(typing.TypedDict, total=False):
    jobId: str
    projectId: str

@typing.type_check_only
class JobScheduling(typing.TypedDict, total=False):
    maxFailuresPerHour: int
    maxFailuresTotal: int

@typing.type_check_only
class JobStatus(typing.TypedDict, total=False):
    details: str
    state: typing.Literal[
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
    substate: typing.Literal["UNSPECIFIED", "SUBMITTED", "QUEUED", "STALE_STATUS"]

@typing.type_check_only
class KerberosConfig(typing.TypedDict, total=False):
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
class LifecycleConfig(typing.TypedDict, total=False):
    autoDeleteTime: str
    autoDeleteTtl: str
    idleDeleteTtl: str
    idleStartTime: str

@typing.type_check_only
class ListAutoscalingPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    policies: _list[AutoscalingPolicy]

@typing.type_check_only
class ListClustersResponse(typing.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListWorkflowTemplatesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    templates: _list[WorkflowTemplate]

@typing.type_check_only
class LoggingConfig(typing.TypedDict, total=False):
    driverLogLevels: dict[str, typing.Any]

@typing.type_check_only
class ManagedCluster(typing.TypedDict, total=False):
    clusterName: str
    config: ClusterConfig
    labels: dict[str, typing.Any]

@typing.type_check_only
class ManagedGroupConfig(typing.TypedDict, total=False):
    instanceGroupManagerName: str
    instanceTemplateName: str

@typing.type_check_only
class MetastoreConfig(typing.TypedDict, total=False):
    dataprocMetastoreService: str

@typing.type_check_only
class NamespacedGkeDeploymentTarget(typing.TypedDict, total=False):
    clusterNamespace: str
    targetGkeCluster: str

@typing.type_check_only
class NodeGroupAffinity(typing.TypedDict, total=False):
    nodeGroupUri: str

@typing.type_check_only
class NodeInitializationAction(typing.TypedDict, total=False):
    executableFile: str
    executionTimeout: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrderedJob(typing.TypedDict, total=False):
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

@typing.type_check_only
class ParameterValidation(typing.TypedDict, total=False):
    regex: RegexValidation
    values: ValueValidation

@typing.type_check_only
class PigJob(typing.TypedDict, total=False):
    continueOnFailure: bool
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList
    scriptVariables: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrestoJob(typing.TypedDict, total=False):
    clientTags: _list[str]
    continueOnFailure: bool
    loggingConfig: LoggingConfig
    outputFormat: str
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList

@typing.type_check_only
class PySparkJob(typing.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainPythonFileUri: str
    properties: dict[str, typing.Any]
    pythonFileUris: _list[str]

@typing.type_check_only
class QueryList(typing.TypedDict, total=False):
    queries: _list[str]

@typing.type_check_only
class RegexValidation(typing.TypedDict, total=False):
    regexes: _list[str]

@typing.type_check_only
class ReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class SecurityConfig(typing.TypedDict, total=False):
    kerberosConfig: KerberosConfig

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class SoftwareConfig(typing.TypedDict, total=False):
    imageVersion: str
    optionalComponents: _list[
        typing.Literal[
            "COMPONENT_UNSPECIFIED",
            "ANACONDA",
            "DOCKER",
            "DRUID",
            "FLINK",
            "HBASE",
            "HIVE_WEBHCAT",
            "JUPYTER",
            "KERBEROS",
            "PRESTO",
            "RANGER",
            "SOLR",
            "ZEPPELIN",
            "ZOOKEEPER",
        ]
    ]
    properties: dict[str, typing.Any]

@typing.type_check_only
class SparkJob(typing.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    mainClass: str
    mainJarFileUri: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class SparkRJob(typing.TypedDict, total=False):
    archiveUris: _list[str]
    args: _list[str]
    fileUris: _list[str]
    loggingConfig: LoggingConfig
    mainRFileUri: str
    properties: dict[str, typing.Any]

@typing.type_check_only
class SparkSqlJob(typing.TypedDict, total=False):
    jarFileUris: _list[str]
    loggingConfig: LoggingConfig
    properties: dict[str, typing.Any]
    queryFileUri: str
    queryList: QueryList
    scriptVariables: dict[str, typing.Any]

@typing.type_check_only
class StartClusterRequest(typing.TypedDict, total=False):
    clusterUuid: str
    requestId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopClusterRequest(typing.TypedDict, total=False):
    clusterUuid: str
    requestId: str

@typing.type_check_only
class SubmitJobRequest(typing.TypedDict, total=False):
    job: Job
    requestId: str

@typing.type_check_only
class TemplateParameter(typing.TypedDict, total=False):
    description: str
    fields: _list[str]
    name: str
    validation: ParameterValidation

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class ValueValidation(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class WorkflowGraph(typing.TypedDict, total=False):
    nodes: _list[WorkflowNode]

@typing.type_check_only
class WorkflowMetadata(typing.TypedDict, total=False):
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
    state: typing.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    template: str
    version: int

@typing.type_check_only
class WorkflowNode(typing.TypedDict, total=False):
    error: str
    jobId: str
    prerequisiteStepIds: _list[str]
    state: typing.Literal[
        "NODE_STATUS_UNSPECIFIED",
        "BLOCKED",
        "RUNNABLE",
        "RUNNING",
        "COMPLETED",
        "FAILED",
    ]
    stepId: str

@typing.type_check_only
class WorkflowTemplate(typing.TypedDict, total=False):
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
class WorkflowTemplatePlacement(typing.TypedDict, total=False):
    clusterSelector: ClusterSelector
    managedCluster: ManagedCluster

@typing.type_check_only
class YarnApplication(typing.TypedDict, total=False):
    name: str
    progress: float
    state: typing.Literal[
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
