import typing

import typing_extensions

class NodeGroupAffinity(typing_extensions.TypedDict, total=False):
    nodeGroupUri: str

class KerberosConfig(typing_extensions.TypedDict, total=False):
    keyPasswordUri: str
    realm: str
    kmsKeyUri: str
    kdcDbKeyUri: str
    truststorePasswordUri: str
    crossRealmTrustRealm: str
    crossRealmTrustSharedPasswordUri: str
    rootPrincipalPasswordUri: str
    truststoreUri: str
    tgtLifetimeHours: int
    keystoreUri: str
    enableKerberos: bool
    crossRealmTrustKdc: str
    crossRealmTrustAdminServer: str
    keystorePasswordUri: str

class GkeClusterConfig(typing_extensions.TypedDict, total=False):
    namespacedGkeDeploymentTarget: NamespacedGkeDeploymentTarget

class NamespacedGkeDeploymentTarget(typing_extensions.TypedDict, total=False):
    clusterNamespace: str
    targetGkeCluster: str

class YarnApplication(typing_extensions.TypedDict, total=False):
    trackingUrl: str
    progress: float
    name: str
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

class ClusterStatus(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "UNKNOWN",
        "CREATING",
        "RUNNING",
        "ERROR",
        "DELETING",
        "UPDATING",
        "STOPPING",
        "STOPPED",
        "STARTING",
    ]
    stateStartTime: str
    detail: str
    substate: typing_extensions.Literal["UNSPECIFIED", "UNHEALTHY", "STALE_STATUS"]

class InstanceReference(typing_extensions.TypedDict, total=False):
    instanceName: str
    instanceId: str

class SubmitJobRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    job: Job

class HiveJob(typing_extensions.TypedDict, total=False):
    queryList: QueryList
    continueOnFailure: bool
    jarFileUris: typing.List[str]
    queryFileUri: str
    scriptVariables: typing.Dict[str, typing.Any]
    properties: typing.Dict[str, typing.Any]

class SparkJob(typing_extensions.TypedDict, total=False):
    jarFileUris: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    archiveUris: typing.List[str]
    mainJarFileUri: str
    loggingConfig: LoggingConfig
    fileUris: typing.List[str]
    args: typing.List[str]
    mainClass: str

class JobScheduling(typing_extensions.TypedDict, total=False):
    maxFailuresPerHour: int

class ListWorkflowTemplatesResponse(typing_extensions.TypedDict, total=False):
    templates: typing.List[WorkflowTemplate]
    nextPageToken: str

class CancelJobRequest(typing_extensions.TypedDict, total=False): ...

class JobStatus(typing_extensions.TypedDict, total=False):
    stateStartTime: str
    substate: typing_extensions.Literal[
        "UNSPECIFIED", "SUBMITTED", "QUEUED", "STALE_STATUS"
    ]
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

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class SecurityConfig(typing_extensions.TypedDict, total=False):
    kerberosConfig: KerberosConfig

class ClusterConfig(typing_extensions.TypedDict, total=False):
    masterConfig: InstanceGroupConfig
    lifecycleConfig: LifecycleConfig
    workerConfig: InstanceGroupConfig
    initializationActions: typing.List[NodeInitializationAction]
    encryptionConfig: EncryptionConfig
    autoscalingConfig: AutoscalingConfig
    softwareConfig: SoftwareConfig
    secondaryWorkerConfig: InstanceGroupConfig
    metastoreConfig: MetastoreConfig
    gkeClusterConfig: GkeClusterConfig
    securityConfig: SecurityConfig
    tempBucket: str
    configBucket: str
    gceClusterConfig: GceClusterConfig
    endpointConfig: EndpointConfig

class DiagnoseClusterResults(typing_extensions.TypedDict, total=False):
    outputUri: str

class DiagnoseClusterRequest(typing_extensions.TypedDict, total=False): ...

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    bindingId: str
    role: str

class SparkSqlJob(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]
    queryList: QueryList
    scriptVariables: typing.Dict[str, typing.Any]
    loggingConfig: LoggingConfig
    jarFileUris: typing.List[str]
    queryFileUri: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    error: Status
    response: typing.Dict[str, typing.Any]
    name: str
    done: bool

class JobReference(typing_extensions.TypedDict, total=False):
    projectId: str
    jobId: str

class QueryList(typing_extensions.TypedDict, total=False):
    queries: typing.List[str]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SoftwareConfig(typing_extensions.TypedDict, total=False):
    optionalComponents: typing.List[str]
    imageVersion: str
    properties: typing.Dict[str, typing.Any]

class TemplateParameter(typing_extensions.TypedDict, total=False):
    fields: typing.List[str]
    name: str
    validation: ParameterValidation
    description: str

class AutoscalingConfig(typing_extensions.TypedDict, total=False):
    policyUri: str

class JobMetadata(typing_extensions.TypedDict, total=False):
    startTime: str
    jobId: str
    operationType: str
    status: JobStatus

class WorkflowMetadata(typing_extensions.TypedDict, total=False):
    dagTimeout: str
    deleteCluster: ClusterOperation
    dagStartTime: str
    endTime: str
    state: typing_extensions.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    startTime: str
    clusterUuid: str
    parameters: typing.Dict[str, typing.Any]
    createCluster: ClusterOperation
    dagEndTime: str
    version: int
    clusterName: str
    template: str
    graph: WorkflowGraph

class StopClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    requestId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    nextPageToken: str

class RegexValidation(typing_extensions.TypedDict, total=False):
    regexes: typing.List[str]

class OrderedJob(typing_extensions.TypedDict, total=False):
    sparkRJob: SparkRJob
    prerequisiteStepIds: typing.List[str]
    pigJob: PigJob
    scheduling: JobScheduling
    hadoopJob: HadoopJob
    labels: typing.Dict[str, typing.Any]
    pysparkJob: PySparkJob
    hiveJob: HiveJob
    sparkSqlJob: SparkSqlJob
    stepId: str
    prestoJob: PrestoJob
    sparkJob: SparkJob

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class ManagedCluster(typing_extensions.TypedDict, total=False):
    config: ClusterConfig
    clusterName: str
    labels: typing.Dict[str, typing.Any]

class WorkflowNode(typing_extensions.TypedDict, total=False):
    error: str
    stepId: str
    state: typing_extensions.Literal[
        "NODE_STATUS_UNSPECIFIED",
        "BLOCKED",
        "RUNNABLE",
        "RUNNING",
        "COMPLETED",
        "FAILED",
    ]
    prerequisiteStepIds: typing.List[str]
    jobId: str

class WorkflowTemplate(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    jobs: typing.List[OrderedJob]
    name: str
    placement: WorkflowTemplatePlacement
    dagTimeout: str
    createTime: str
    version: int
    parameters: typing.List[TemplateParameter]
    id: str
    updateTime: str

class PySparkJob(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]
    fileUris: typing.List[str]
    args: typing.List[str]
    archiveUris: typing.List[str]
    mainPythonFileUri: str
    jarFileUris: typing.List[str]
    pythonFileUris: typing.List[str]
    loggingConfig: LoggingConfig

class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: typing.List[Cluster]
    nextPageToken: str

class ClusterOperationStatus(typing_extensions.TypedDict, total=False):
    stateStartTime: str
    state: typing_extensions.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    details: str
    innerState: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class AutoscalingPolicy(typing_extensions.TypedDict, total=False):
    secondaryWorkerConfig: InstanceGroupAutoscalingPolicyConfig
    name: str
    id: str
    workerConfig: InstanceGroupAutoscalingPolicyConfig
    basicAlgorithm: BasicAutoscalingAlgorithm

class LifecycleConfig(typing_extensions.TypedDict, total=False):
    autoDeleteTtl: str
    idleDeleteTtl: str
    autoDeleteTime: str
    idleStartTime: str

class InstantiateWorkflowTemplateRequest(typing_extensions.TypedDict, total=False):
    version: int
    instanceId: str
    requestId: str
    parameters: typing.Dict[str, typing.Any]

class PrestoJob(typing_extensions.TypedDict, total=False):
    continueOnFailure: bool
    properties: typing.Dict[str, typing.Any]
    outputFormat: str
    loggingConfig: LoggingConfig
    queryList: QueryList
    clientTags: typing.List[str]
    queryFileUri: str

class ClusterOperation(typing_extensions.TypedDict, total=False):
    operationId: str
    done: bool
    error: str

class DiskConfig(typing_extensions.TypedDict, total=False):
    numLocalSsds: int
    bootDiskType: str
    bootDiskSizeGb: int

class Cluster(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    metrics: ClusterMetrics
    clusterName: str
    labels: typing.Dict[str, typing.Any]
    config: ClusterConfig
    statusHistory: typing.List[ClusterStatus]
    status: ClusterStatus
    projectId: str

class ClusterOperationMetadata(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    clusterUuid: str
    clusterName: str
    statusHistory: typing.List[ClusterOperationStatus]
    status: ClusterOperationStatus
    warnings: typing.List[str]
    operationType: str
    description: str

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    location: str
    description: str
    title: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ManagedGroupConfig(typing_extensions.TypedDict, total=False):
    instanceGroupManagerName: str
    instanceTemplateName: str

class SparkRJob(typing_extensions.TypedDict, total=False):
    mainRFileUri: str
    loggingConfig: LoggingConfig
    args: typing.List[str]
    fileUris: typing.List[str]
    archiveUris: typing.List[str]
    properties: typing.Dict[str, typing.Any]

class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorTypeUri: str

class WorkflowGraph(typing_extensions.TypedDict, total=False):
    nodes: typing.List[WorkflowNode]

class ClusterMetrics(typing_extensions.TypedDict, total=False):
    hdfsMetrics: typing.Dict[str, typing.Any]
    yarnMetrics: typing.Dict[str, typing.Any]

class MetastoreConfig(typing_extensions.TypedDict, total=False):
    dataprocMetastoreService: str

class BasicAutoscalingAlgorithm(typing_extensions.TypedDict, total=False):
    cooldownPeriod: str
    yarnConfig: BasicYarnAutoscalingConfig

class InstanceGroupAutoscalingPolicyConfig(typing_extensions.TypedDict, total=False):
    minInstances: int
    weight: int
    maxInstances: int

class HadoopJob(typing_extensions.TypedDict, total=False):
    jarFileUris: typing.List[str]
    fileUris: typing.List[str]
    loggingConfig: LoggingConfig
    mainJarFileUri: str
    mainClass: str
    args: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    archiveUris: typing.List[str]

class StartClusterRequest(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    requestId: str

class ReservationAffinity(typing_extensions.TypedDict, total=False):
    key: str
    values: typing.List[str]
    consumeReservationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]

class JobPlacement(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    clusterName: str

class EndpointConfig(typing_extensions.TypedDict, total=False):
    httpPorts: typing.Dict[str, typing.Any]
    enableHttpPortAccess: bool

class BasicYarnAutoscalingConfig(typing_extensions.TypedDict, total=False):
    scaleUpFactor: float
    gracefulDecommissionTimeout: str
    scaleUpMinWorkerFraction: float
    scaleDownFactor: float
    scaleDownMinWorkerFraction: float

class ClusterSelector(typing_extensions.TypedDict, total=False):
    clusterLabels: typing.Dict[str, typing.Any]
    zone: str

class EncryptionConfig(typing_extensions.TypedDict, total=False):
    gcePdKmsKeyName: str

class PigJob(typing_extensions.TypedDict, total=False):
    queryList: QueryList
    jarFileUris: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    continueOnFailure: bool
    loggingConfig: LoggingConfig
    scriptVariables: typing.Dict[str, typing.Any]
    queryFileUri: str

class WorkflowTemplatePlacement(typing_extensions.TypedDict, total=False):
    clusterSelector: ClusterSelector
    managedCluster: ManagedCluster

class NodeInitializationAction(typing_extensions.TypedDict, total=False):
    executionTimeout: str
    executableFile: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class ParameterValidation(typing_extensions.TypedDict, total=False):
    values: ValueValidation
    regex: RegexValidation

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class GceClusterConfig(typing_extensions.TypedDict, total=False):
    internalIpOnly: bool
    zoneUri: str
    networkUri: str
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "INHERIT_FROM_SUBNETWORK",
        "OUTBOUND",
        "BIDIRECTIONAL",
    ]
    nodeGroupAffinity: NodeGroupAffinity
    serviceAccountScopes: typing.List[str]
    metadata: typing.Dict[str, typing.Any]
    subnetworkUri: str
    tags: typing.List[str]
    serviceAccount: str
    reservationAffinity: ReservationAffinity

class ListAutoscalingPoliciesResponse(typing_extensions.TypedDict, total=False):
    policies: typing.List[AutoscalingPolicy]
    nextPageToken: str

class LoggingConfig(typing_extensions.TypedDict, total=False):
    driverLogLevels: typing.Dict[str, typing.Any]

class InstanceGroupConfig(typing_extensions.TypedDict, total=False):
    isPreemptible: bool
    preemptibility: typing_extensions.Literal[
        "PREEMPTIBILITY_UNSPECIFIED", "NON_PREEMPTIBLE", "PREEMPTIBLE"
    ]
    instanceNames: typing.List[str]
    managedGroupConfig: ManagedGroupConfig
    machineTypeUri: str
    instanceReferences: typing.List[InstanceReference]
    minCpuPlatform: str
    diskConfig: DiskConfig
    accelerators: typing.List[AcceleratorConfig]
    imageUri: str
    numInstances: int

class ValueValidation(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class Job(typing_extensions.TypedDict, total=False):
    driverControlFilesUri: str
    submittedBy: str
    sparkJob: SparkJob
    hiveJob: HiveJob
    pigJob: PigJob
    pysparkJob: PySparkJob
    sparkSqlJob: SparkSqlJob
    status: JobStatus
    driverOutputResourceUri: str
    hadoopJob: HadoopJob
    scheduling: JobScheduling
    labels: typing.Dict[str, typing.Any]
    statusHistory: typing.List[JobStatus]
    prestoJob: PrestoJob
    jobUuid: str
    placement: JobPlacement
    yarnApplications: typing.List[YarnApplication]
    sparkRJob: SparkRJob
    done: bool
    reference: JobReference
