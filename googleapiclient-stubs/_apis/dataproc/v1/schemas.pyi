import typing

import typing_extensions

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    etag: str

class DiskConfig(typing_extensions.TypedDict, total=False):
    bootDiskSizeGb: int
    bootDiskType: str
    numLocalSsds: int

class EndpointConfig(typing_extensions.TypedDict, total=False):
    enableHttpPortAccess: bool
    httpPorts: typing.Dict[str, typing.Any]

class InstanceGroupAutoscalingPolicyConfig(typing_extensions.TypedDict, total=False):
    minInstances: int
    maxInstances: int
    weight: int

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class Job(typing_extensions.TypedDict, total=False):
    statusHistory: typing.List[JobStatus]
    hiveJob: HiveJob
    sparkJob: SparkJob
    pigJob: PigJob
    scheduling: JobScheduling
    hadoopJob: HadoopJob
    driverControlFilesUri: str
    pysparkJob: PySparkJob
    reference: JobReference
    driverOutputResourceUri: str
    yarnApplications: typing.List[YarnApplication]
    prestoJob: PrestoJob
    sparkSqlJob: SparkSqlJob
    placement: JobPlacement
    sparkRJob: SparkRJob
    done: bool
    labels: typing.Dict[str, typing.Any]
    jobUuid: str
    status: JobStatus

class ClusterSelector(typing_extensions.TypedDict, total=False):
    clusterLabels: typing.Dict[str, typing.Any]
    zone: str

class InstanceGroupConfig(typing_extensions.TypedDict, total=False):
    machineTypeUri: str
    instanceNames: typing.List[str]
    minCpuPlatform: str
    imageUri: str
    managedGroupConfig: ManagedGroupConfig
    instanceReferences: typing.List[InstanceReference]
    preemptibility: typing_extensions.Literal[
        "PREEMPTIBILITY_UNSPECIFIED", "NON_PREEMPTIBLE", "PREEMPTIBLE"
    ]
    diskConfig: DiskConfig
    numInstances: int
    accelerators: typing.List[AcceleratorConfig]
    isPreemptible: bool

class CancelJobRequest(typing_extensions.TypedDict, total=False): ...

class ListWorkflowTemplatesResponse(typing_extensions.TypedDict, total=False):
    templates: typing.List[WorkflowTemplate]
    nextPageToken: str

class LoggingConfig(typing_extensions.TypedDict, total=False):
    driverLogLevels: typing.Dict[str, typing.Any]

class ValueValidation(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class SecurityConfig(typing_extensions.TypedDict, total=False):
    kerberosConfig: KerberosConfig

class JobReference(typing_extensions.TypedDict, total=False):
    jobId: str
    projectId: str

class NodeGroupAffinity(typing_extensions.TypedDict, total=False):
    nodeGroupUri: str

class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorTypeUri: str

class EncryptionConfig(typing_extensions.TypedDict, total=False):
    gcePdKmsKeyName: str

class WorkflowGraph(typing_extensions.TypedDict, total=False):
    nodes: typing.List[WorkflowNode]

class OrderedJob(typing_extensions.TypedDict, total=False):
    sparkRJob: SparkRJob
    sparkSqlJob: SparkSqlJob
    stepId: str
    prerequisiteStepIds: typing.List[str]
    pysparkJob: PySparkJob
    prestoJob: PrestoJob
    hadoopJob: HadoopJob
    sparkJob: SparkJob
    hiveJob: HiveJob
    scheduling: JobScheduling
    labels: typing.Dict[str, typing.Any]
    pigJob: PigJob

class PigJob(typing_extensions.TypedDict, total=False):
    queryList: QueryList
    continueOnFailure: bool
    queryFileUri: str
    jarFileUris: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    loggingConfig: LoggingConfig
    scriptVariables: typing.Dict[str, typing.Any]

class PrestoJob(typing_extensions.TypedDict, total=False):
    clientTags: typing.List[str]
    continueOnFailure: bool
    queryFileUri: str
    outputFormat: str
    properties: typing.Dict[str, typing.Any]
    queryList: QueryList
    loggingConfig: LoggingConfig

class TemplateParameter(typing_extensions.TypedDict, total=False):
    validation: ParameterValidation
    fields: typing.List[str]
    name: str
    description: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class BasicYarnAutoscalingConfig(typing_extensions.TypedDict, total=False):
    scaleDownMinWorkerFraction: float
    scaleUpFactor: float
    scaleDownFactor: float
    scaleUpMinWorkerFraction: float
    gracefulDecommissionTimeout: str

class ListClustersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    clusters: typing.List[Cluster]

class ClusterOperationMetadata(typing_extensions.TypedDict, total=False):
    operationType: str
    statusHistory: typing.List[ClusterOperationStatus]
    clusterUuid: str
    warnings: typing.List[str]
    description: str
    clusterName: str
    status: ClusterOperationStatus
    labels: typing.Dict[str, typing.Any]

class ClusterConfig(typing_extensions.TypedDict, total=False):
    configBucket: str
    lifecycleConfig: LifecycleConfig
    autoscalingConfig: AutoscalingConfig
    endpointConfig: EndpointConfig
    masterConfig: InstanceGroupConfig
    encryptionConfig: EncryptionConfig
    gceClusterConfig: GceClusterConfig
    secondaryWorkerConfig: InstanceGroupConfig
    workerConfig: InstanceGroupConfig
    softwareConfig: SoftwareConfig
    securityConfig: SecurityConfig
    initializationActions: typing.List[NodeInitializationAction]
    tempBucket: str

class QueryList(typing_extensions.TypedDict, total=False):
    queries: typing.List[str]

class ClusterOperationStatus(typing_extensions.TypedDict, total=False):
    details: str
    state: typing_extensions.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    innerState: str
    stateStartTime: str

class JobScheduling(typing_extensions.TypedDict, total=False):
    maxFailuresPerHour: int

class ClusterOperation(typing_extensions.TypedDict, total=False):
    done: bool
    operationId: str
    error: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class ManagedGroupConfig(typing_extensions.TypedDict, total=False):
    instanceGroupManagerName: str
    instanceTemplateName: str

class SoftwareConfig(typing_extensions.TypedDict, total=False):
    imageVersion: str
    properties: typing.Dict[str, typing.Any]
    optionalComponents: typing.List[str]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class SubmitJobRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    job: Job

class SparkRJob(typing_extensions.TypedDict, total=False):
    archiveUris: typing.List[str]
    loggingConfig: LoggingConfig
    fileUris: typing.List[str]
    args: typing.List[str]
    mainRFileUri: str
    properties: typing.Dict[str, typing.Any]

class ClusterMetrics(typing_extensions.TypedDict, total=False):
    hdfsMetrics: typing.Dict[str, typing.Any]
    yarnMetrics: typing.Dict[str, typing.Any]

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    description: str
    expression: str
    location: str

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    nextPageToken: str

class LifecycleConfig(typing_extensions.TypedDict, total=False):
    idleDeleteTtl: str
    autoDeleteTime: str
    idleStartTime: str
    autoDeleteTtl: str

class WorkflowNode(typing_extensions.TypedDict, total=False):
    prerequisiteStepIds: typing.List[str]
    stepId: str
    jobId: str
    state: typing_extensions.Literal[
        "NODE_STATE_UNSPECIFIED",
        "BLOCKED",
        "RUNNABLE",
        "RUNNING",
        "COMPLETED",
        "FAILED",
    ]
    error: str

class AutoscalingConfig(typing_extensions.TypedDict, total=False):
    policyUri: str

class HiveJob(typing_extensions.TypedDict, total=False):
    continueOnFailure: bool
    queryFileUri: str
    queryList: QueryList
    jarFileUris: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    scriptVariables: typing.Dict[str, typing.Any]

class DiagnoseClusterResults(typing_extensions.TypedDict, total=False):
    outputUri: str

class Cluster(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    status: ClusterStatus
    projectId: str
    config: ClusterConfig
    metrics: ClusterMetrics
    labels: typing.Dict[str, typing.Any]
    clusterName: str
    statusHistory: typing.List[ClusterStatus]

class GceClusterConfig(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    nodeGroupAffinity: NodeGroupAffinity
    serviceAccount: str
    subnetworkUri: str
    reservationAffinity: ReservationAffinity
    tags: typing.List[str]
    zoneUri: str
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "INHERIT_FROM_SUBNETWORK",
        "OUTBOUND",
        "BIDIRECTIONAL",
    ]
    internalIpOnly: bool
    networkUri: str
    serviceAccountScopes: typing.List[str]

class JobPlacement(typing_extensions.TypedDict, total=False):
    clusterUuid: str
    clusterName: str

class ManagedCluster(typing_extensions.TypedDict, total=False):
    config: ClusterConfig
    labels: typing.Dict[str, typing.Any]
    clusterName: str

class SparkJob(typing_extensions.TypedDict, total=False):
    args: typing.List[str]
    jarFileUris: typing.List[str]
    mainClass: str
    loggingConfig: LoggingConfig
    fileUris: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    mainJarFileUri: str
    archiveUris: typing.List[str]

class YarnApplication(typing_extensions.TypedDict, total=False):
    name: str
    trackingUrl: str
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

class InstanceReference(typing_extensions.TypedDict, total=False):
    instanceName: str
    instanceId: str

class RegexValidation(typing_extensions.TypedDict, total=False):
    regexes: typing.List[str]

class NodeInitializationAction(typing_extensions.TypedDict, total=False):
    executionTimeout: str
    executableFile: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class WorkflowMetadata(typing_extensions.TypedDict, total=False):
    graph: WorkflowGraph
    deleteCluster: ClusterOperation
    version: int
    clusterUuid: str
    template: str
    parameters: typing.Dict[str, typing.Any]
    endTime: str
    startTime: str
    state: typing_extensions.Literal["UNKNOWN", "PENDING", "RUNNING", "DONE"]
    createCluster: ClusterOperation
    clusterName: str

class JobStatus(typing_extensions.TypedDict, total=False):
    stateStartTime: str
    details: str
    substate: typing_extensions.Literal[
        "UNSPECIFIED", "SUBMITTED", "QUEUED", "STALE_STATUS"
    ]
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

class PySparkJob(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]
    jarFileUris: typing.List[str]
    mainPythonFileUri: str
    pythonFileUris: typing.List[str]
    args: typing.List[str]
    archiveUris: typing.List[str]
    fileUris: typing.List[str]
    loggingConfig: LoggingConfig

class WorkflowTemplate(typing_extensions.TypedDict, total=False):
    updateTime: str
    labels: typing.Dict[str, typing.Any]
    placement: WorkflowTemplatePlacement
    jobs: typing.List[OrderedJob]
    createTime: str
    parameters: typing.List[TemplateParameter]
    id: str
    name: str
    version: int

class InstantiateWorkflowTemplateRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    parameters: typing.Dict[str, typing.Any]
    version: int

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DiagnoseClusterRequest(typing_extensions.TypedDict, total=False): ...

class ParameterValidation(typing_extensions.TypedDict, total=False):
    regex: RegexValidation
    values: ValueValidation

class ListAutoscalingPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: typing.List[AutoscalingPolicy]

class KerberosConfig(typing_extensions.TypedDict, total=False):
    enableKerberos: bool
    kdcDbKeyUri: str
    crossRealmTrustAdminServer: str
    crossRealmTrustKdc: str
    rootPrincipalPasswordUri: str
    keystorePasswordUri: str
    truststoreUri: str
    keystoreUri: str
    tgtLifetimeHours: int
    crossRealmTrustSharedPasswordUri: str
    realm: str
    keyPasswordUri: str
    kmsKeyUri: str
    truststorePasswordUri: str
    crossRealmTrustRealm: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    values: typing.List[str]
    key: str

class SparkSqlJob(typing_extensions.TypedDict, total=False):
    queryFileUri: str
    loggingConfig: LoggingConfig
    jarFileUris: typing.List[str]
    scriptVariables: typing.Dict[str, typing.Any]
    properties: typing.Dict[str, typing.Any]
    queryList: QueryList

class JobMetadata(typing_extensions.TypedDict, total=False):
    status: JobStatus
    operationType: str
    startTime: str
    jobId: str

class BasicAutoscalingAlgorithm(typing_extensions.TypedDict, total=False):
    cooldownPeriod: str
    yarnConfig: BasicYarnAutoscalingConfig

class AutoscalingPolicy(typing_extensions.TypedDict, total=False):
    basicAlgorithm: BasicAutoscalingAlgorithm
    secondaryWorkerConfig: InstanceGroupAutoscalingPolicyConfig
    name: str
    workerConfig: InstanceGroupAutoscalingPolicyConfig
    id: str

class HadoopJob(typing_extensions.TypedDict, total=False):
    mainClass: str
    args: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    mainJarFileUri: str
    jarFileUris: typing.List[str]
    archiveUris: typing.List[str]
    loggingConfig: LoggingConfig
    fileUris: typing.List[str]

class ClusterStatus(typing_extensions.TypedDict, total=False):
    substate: typing_extensions.Literal["UNSPECIFIED", "UNHEALTHY", "STALE_STATUS"]
    stateStartTime: str
    detail: str
    state: typing_extensions.Literal[
        "UNKNOWN", "CREATING", "RUNNING", "ERROR", "DELETING", "UPDATING"
    ]

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    bindingId: str
    condition: Expr

class WorkflowTemplatePlacement(typing_extensions.TypedDict, total=False):
    managedCluster: ManagedCluster
    clusterSelector: ClusterSelector
