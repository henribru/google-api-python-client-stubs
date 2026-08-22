import typing

_list = list

@typing.type_check_only
class Accelerator(typing.TypedDict, total=False):
    count: str
    driverVersion: str
    installGpuDrivers: bool
    type: str

@typing.type_check_only
class ActionCondition(typing.TypedDict, total=False):
    exitCodes: _list[int]

@typing.type_check_only
class AgentContainer(typing.TypedDict, total=False):
    commands: _list[str]
    entrypoint: str
    imageUri: str
    options: str
    volumes: _list[str]

@typing.type_check_only
class AgentEnvironment(typing.TypedDict, total=False):
    encryptedVariables: AgentKMSEnvMap
    secretVariables: dict[str, typing.Any]
    variables: dict[str, typing.Any]

@typing.type_check_only
class AgentInfo(typing.TypedDict, total=False):
    jobId: str
    reportTime: str
    state: typing.Literal[
        "AGENT_STATE_UNSPECIFIED", "AGENT_STARTING", "AGENT_RUNNING", "AGENT_STOPPED"
    ]
    taskGroupId: str
    tasks: _list[AgentTaskInfo]

@typing.type_check_only
class AgentKMSEnvMap(typing.TypedDict, total=False):
    cipherText: str
    keyName: str

@typing.type_check_only
class AgentMetadata(typing.TypedDict, total=False):
    creationTime: str
    creator: str
    imageVersion: str
    instance: str
    instanceId: str
    instancePreemptionNoticeReceived: bool
    machineType: str
    osRelease: dict[str, typing.Any]
    version: str
    zone: str

@typing.type_check_only
class AgentScript(typing.TypedDict, total=False):
    path: str
    text: str

@typing.type_check_only
class AgentTask(typing.TypedDict, total=False):
    agentTaskSpec: AgentTaskSpec
    intendedState: typing.Literal[
        "INTENDED_STATE_UNSPECIFIED", "ASSIGNED", "CANCELLED", "DELETED"
    ]
    reachedBarrier: str
    spec: TaskSpec
    status: TaskStatus
    task: str
    taskSource: typing.Literal["TASK_SOURCE_UNSPECIFIED", "BATCH_INTERNAL", "USER"]

@typing.type_check_only
class AgentTaskInfo(typing.TypedDict, total=False):
    runnable: str
    taskId: str
    taskStatus: TaskStatus

@typing.type_check_only
class AgentTaskLoggingOption(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class AgentTaskRunnable(typing.TypedDict, total=False):
    alwaysRun: bool
    background: bool
    container: AgentContainer
    environment: AgentEnvironment
    ignoreExitStatus: bool
    script: AgentScript
    timeout: str

@typing.type_check_only
class AgentTaskSpec(typing.TypedDict, total=False):
    environment: AgentEnvironment
    loggingOption: AgentTaskLoggingOption
    maxRunDuration: str
    runnables: _list[AgentTaskRunnable]
    userAccount: AgentTaskUserAccount

@typing.type_check_only
class AgentTaskUserAccount(typing.TypedDict, total=False):
    gid: str
    uid: str

@typing.type_check_only
class AgentTimingInfo(typing.TypedDict, total=False):
    agentStartupTime: str
    bootTime: str
    scriptStartupTime: str

@typing.type_check_only
class AllocationPolicy(typing.TypedDict, total=False):
    instances: _list[InstancePolicyOrTemplate]
    labels: dict[str, typing.Any]
    location: LocationPolicy
    network: NetworkPolicy
    placement: PlacementPolicy
    serviceAccount: ServiceAccount
    tags: _list[str]

@typing.type_check_only
class AttachedDisk(typing.TypedDict, total=False):
    deviceName: str
    existingDisk: str
    newDisk: Disk

@typing.type_check_only
class Barrier(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class CancelJobRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloudLoggingOption(typing.TypedDict, total=False):
    useGenericTaskMonitoredResource: bool

@typing.type_check_only
class ComputeResource(typing.TypedDict, total=False):
    bootDiskMib: str
    cpuMilli: str
    memoryMib: str

@typing.type_check_only
class Container(typing.TypedDict, total=False):
    blockExternalNetwork: bool
    commands: _list[str]
    enableImageStreaming: bool
    entrypoint: str
    imageUri: str
    options: str
    password: str
    username: str
    volumes: _list[str]

@typing.type_check_only
class Disk(typing.TypedDict, total=False):
    diskInterface: str
    image: str
    sizeGb: str
    snapshot: str
    type: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    encryptedVariables: KMSEnvMap
    secretVariables: dict[str, typing.Any]
    variables: dict[str, typing.Any]

@typing.type_check_only
class GCS(typing.TypedDict, total=False):
    remotePath: str

@typing.type_check_only
class InstancePolicy(typing.TypedDict, total=False):
    accelerators: _list[Accelerator]
    bootDisk: Disk
    disks: _list[AttachedDisk]
    machineType: str
    minCpuPlatform: str
    provisioningModel: typing.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED",
        "STANDARD",
        "SPOT",
        "PREEMPTIBLE",
        "RESERVATION_BOUND",
        "FLEX_START",
    ]
    reservation: str

@typing.type_check_only
class InstancePolicyOrTemplate(typing.TypedDict, total=False):
    blockProjectSshKeys: bool
    installGpuDrivers: bool
    installOpsAgent: bool
    instanceTemplate: str
    policy: InstancePolicy

@typing.type_check_only
class InstanceStatus(typing.TypedDict, total=False):
    bootDisk: Disk
    machineType: str
    provisioningModel: typing.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED",
        "STANDARD",
        "SPOT",
        "PREEMPTIBLE",
        "RESERVATION_BOUND",
        "FLEX_START",
    ]
    taskPack: str

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    allocationPolicy: AllocationPolicy
    createTime: str
    labels: dict[str, typing.Any]
    logsPolicy: LogsPolicy
    name: str
    notifications: _list[JobNotification]
    priority: str
    status: JobStatus
    taskGroups: _list[TaskGroup]
    uid: str
    updateTime: str

@typing.type_check_only
class JobNotification(typing.TypedDict, total=False):
    message: Message
    pubsubTopic: str

@typing.type_check_only
class JobStatus(typing.TypedDict, total=False):
    runDuration: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "SCHEDULED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "DELETION_IN_PROGRESS",
        "CANCELLATION_IN_PROGRESS",
        "CANCELLED",
    ]
    statusEvents: _list[StatusEvent]
    taskGroups: dict[str, typing.Any]

@typing.type_check_only
class KMSEnvMap(typing.TypedDict, total=False):
    cipherText: str
    keyName: str

@typing.type_check_only
class LifecyclePolicy(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "RETRY_TASK", "FAIL_TASK"]
    actionCondition: ActionCondition

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListTasksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[Task]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationPolicy(typing.TypedDict, total=False):
    allowedLocations: _list[str]

@typing.type_check_only
class LogsPolicy(typing.TypedDict, total=False):
    cloudLoggingOption: CloudLoggingOption
    destination: typing.Literal["DESTINATION_UNSPECIFIED", "CLOUD_LOGGING", "PATH"]
    logsPath: str

@typing.type_check_only
class Message(typing.TypedDict, total=False):
    newJobState: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "SCHEDULED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "DELETION_IN_PROGRESS",
        "CANCELLATION_IN_PROGRESS",
        "CANCELLED",
    ]
    newTaskState: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "ASSIGNED",
        "RUNNING",
        "FAILED",
        "SUCCEEDED",
        "UNEXECUTED",
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "JOB_STATE_CHANGED", "TASK_STATE_CHANGED"]

@typing.type_check_only
class NFS(typing.TypedDict, total=False):
    remotePath: str
    server: str

@typing.type_check_only
class NetworkInterface(typing.TypedDict, total=False):
    network: str
    nicType: typing.Literal["NIC_TYPE_UNSPECIFIED", "GVNIC", "IRDMA", "MRDMA"]
    noExternalIpAddress: bool
    subnetwork: str

@typing.type_check_only
class NetworkPolicy(typing.TypedDict, total=False):
    networkInterfaces: _list[NetworkInterface]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PlacementPolicy(typing.TypedDict, total=False):
    collocation: str
    maxDistance: str

@typing.type_check_only
class ReportAgentStateRequest(typing.TypedDict, total=False):
    agentInfo: AgentInfo
    agentTimingInfo: AgentTimingInfo
    metadata: AgentMetadata

@typing.type_check_only
class ReportAgentStateResponse(typing.TypedDict, total=False):
    defaultReportInterval: str
    minReportInterval: str
    tasks: _list[AgentTask]
    useBatchMonitoredResource: bool

@typing.type_check_only
class Runnable(typing.TypedDict, total=False):
    alwaysRun: bool
    background: bool
    barrier: Barrier
    container: Container
    displayName: str
    environment: Environment
    ignoreExitStatus: bool
    labels: dict[str, typing.Any]
    script: Script
    timeout: str

@typing.type_check_only
class Script(typing.TypedDict, total=False):
    path: str
    text: str

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusEvent(typing.TypedDict, total=False):
    description: str
    eventTime: str
    taskExecution: TaskExecution
    taskState: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "ASSIGNED",
        "RUNNING",
        "FAILED",
        "SUCCEEDED",
        "UNEXECUTED",
    ]
    type: str

@typing.type_check_only
class Task(typing.TypedDict, total=False):
    name: str
    status: TaskStatus

@typing.type_check_only
class TaskExecution(typing.TypedDict, total=False):
    exitCode: int

@typing.type_check_only
class TaskGroup(typing.TypedDict, total=False):
    name: str
    parallelism: str
    permissiveSsh: bool
    requireHostsFile: bool
    runAsNonRoot: bool
    schedulingPolicy: typing.Literal[
        "SCHEDULING_POLICY_UNSPECIFIED", "AS_SOON_AS_POSSIBLE", "IN_ORDER"
    ]
    taskCount: str
    taskCountPerNode: str
    taskEnvironments: _list[Environment]
    taskSpec: TaskSpec

@typing.type_check_only
class TaskGroupStatus(typing.TypedDict, total=False):
    counts: dict[str, typing.Any]
    instances: _list[InstanceStatus]

@typing.type_check_only
class TaskSpec(typing.TypedDict, total=False):
    computeResource: ComputeResource
    environment: Environment
    environments: dict[str, typing.Any]
    lifecyclePolicies: _list[LifecyclePolicy]
    maxRetryCount: int
    maxRunDuration: str
    runnables: _list[Runnable]
    volumes: _list[Volume]

@typing.type_check_only
class TaskStatus(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "ASSIGNED",
        "RUNNING",
        "FAILED",
        "SUCCEEDED",
        "UNEXECUTED",
    ]
    statusEvents: _list[StatusEvent]

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    deviceName: str
    gcs: GCS
    mountOptions: _list[str]
    mountPath: str
    nfs: NFS
