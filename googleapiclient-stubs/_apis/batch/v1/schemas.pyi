import typing

import typing_extensions

_list = list

@typing.type_check_only
class Accelerator(typing_extensions.TypedDict, total=False):
    count: str
    installGpuDrivers: bool
    type: str

@typing.type_check_only
class ActionCondition(typing_extensions.TypedDict, total=False):
    exitCodes: _list[int]

@typing.type_check_only
class AgentInfo(typing_extensions.TypedDict, total=False):
    jobId: str
    reportTime: str
    state: typing_extensions.Literal[
        "AGENT_STATE_UNSPECIFIED", "AGENT_STARTING", "AGENT_RUNNING", "AGENT_STOPPED"
    ]
    taskGroupId: str
    tasks: _list[AgentTaskInfo]

@typing.type_check_only
class AgentMetadata(typing_extensions.TypedDict, total=False):
    creationTime: str
    creator: str
    imageVersion: str
    instance: str
    instanceId: str
    osRelease: dict[str, typing.Any]
    version: str
    zone: str

@typing.type_check_only
class AgentTask(typing_extensions.TypedDict, total=False):
    intendedState: typing_extensions.Literal[
        "INTENDED_STATE_UNSPECIFIED", "ASSIGNED", "CANCELLED", "DELETED"
    ]
    reachedBarrier: str
    spec: TaskSpec
    status: TaskStatus
    task: str

@typing.type_check_only
class AgentTaskInfo(typing_extensions.TypedDict, total=False):
    runnable: str
    taskId: str
    taskStatus: TaskStatus

@typing.type_check_only
class AgentTimingInfo(typing_extensions.TypedDict, total=False):
    agentStartupTime: str
    bootTime: str
    scriptStartupTime: str

@typing.type_check_only
class AllocationPolicy(typing_extensions.TypedDict, total=False):
    instances: _list[InstancePolicyOrTemplate]
    labels: dict[str, typing.Any]
    location: LocationPolicy
    network: NetworkPolicy
    serviceAccount: ServiceAccount

@typing.type_check_only
class AttachedDisk(typing_extensions.TypedDict, total=False):
    deviceName: str
    existingDisk: str
    newDisk: Disk

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Barrier(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ComputeResource(typing_extensions.TypedDict, total=False):
    bootDiskMib: str
    cpuMilli: str
    memoryMib: str

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    blockExternalNetwork: bool
    commands: _list[str]
    entrypoint: str
    imageUri: str
    options: str
    password: str
    username: str
    volumes: _list[str]

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    diskInterface: str
    image: str
    sizeGb: str
    snapshot: str
    type: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    variables: dict[str, typing.Any]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GCS(typing_extensions.TypedDict, total=False):
    remotePath: str

@typing.type_check_only
class InstancePolicy(typing_extensions.TypedDict, total=False):
    accelerators: _list[Accelerator]
    disks: _list[AttachedDisk]
    machineType: str
    minCpuPlatform: str
    provisioningModel: typing_extensions.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED", "STANDARD", "SPOT", "PREEMPTIBLE"
    ]

@typing.type_check_only
class InstancePolicyOrTemplate(typing_extensions.TypedDict, total=False):
    installGpuDrivers: bool
    instanceTemplate: str
    policy: InstancePolicy

@typing.type_check_only
class InstanceStatus(typing_extensions.TypedDict, total=False):
    machineType: str
    provisioningModel: typing_extensions.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED", "STANDARD", "SPOT", "PREEMPTIBLE"
    ]
    taskPack: str

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
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
class JobNotification(typing_extensions.TypedDict, total=False):
    message: Message
    pubsubTopic: str

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    runDuration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "SCHEDULED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "DELETION_IN_PROGRESS",
    ]
    statusEvents: _list[StatusEvent]
    taskGroups: dict[str, typing.Any]

@typing.type_check_only
class LifecyclePolicy(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "RETRY_TASK", "FAIL_TASK"]
    actionCondition: ActionCondition

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[Task]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationPolicy(typing_extensions.TypedDict, total=False):
    allowedLocations: _list[str]

@typing.type_check_only
class LogsPolicy(typing_extensions.TypedDict, total=False):
    destination: typing_extensions.Literal[
        "DESTINATION_UNSPECIFIED", "CLOUD_LOGGING", "PATH"
    ]
    logsPath: str

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    newJobState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "SCHEDULED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "DELETION_IN_PROGRESS",
    ]
    newTaskState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "ASSIGNED", "RUNNING", "FAILED", "SUCCEEDED"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "JOB_STATE_CHANGED", "TASK_STATE_CHANGED"
    ]

@typing.type_check_only
class NFS(typing_extensions.TypedDict, total=False):
    remotePath: str
    server: str

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    network: str
    noExternalIpAddress: bool
    subnetwork: str

@typing.type_check_only
class NetworkPolicy(typing_extensions.TypedDict, total=False):
    networkInterfaces: _list[NetworkInterface]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ReportAgentStateRequest(typing_extensions.TypedDict, total=False):
    agentInfo: AgentInfo
    agentTimingInfo: AgentTimingInfo
    metadata: AgentMetadata

@typing.type_check_only
class ReportAgentStateResponse(typing_extensions.TypedDict, total=False):
    minReportInterval: str
    tasks: _list[AgentTask]

@typing.type_check_only
class Runnable(typing_extensions.TypedDict, total=False):
    alwaysRun: bool
    background: bool
    barrier: Barrier
    container: Container
    environment: Environment
    ignoreExitStatus: bool
    script: Script
    timeout: str

@typing.type_check_only
class Script(typing_extensions.TypedDict, total=False):
    path: str
    text: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusEvent(typing_extensions.TypedDict, total=False):
    description: str
    eventTime: str
    taskExecution: TaskExecution
    type: str

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
    name: str
    status: TaskStatus

@typing.type_check_only
class TaskExecution(typing_extensions.TypedDict, total=False):
    exitCode: int

@typing.type_check_only
class TaskGroup(typing_extensions.TypedDict, total=False):
    name: str
    parallelism: str
    permissiveSsh: bool
    requireHostsFile: bool
    taskCount: str
    taskCountPerNode: str
    taskEnvironments: _list[Environment]
    taskSpec: TaskSpec

@typing.type_check_only
class TaskGroupStatus(typing_extensions.TypedDict, total=False):
    counts: dict[str, typing.Any]
    instances: _list[InstanceStatus]

@typing.type_check_only
class TaskSpec(typing_extensions.TypedDict, total=False):
    computeResource: ComputeResource
    environment: Environment
    environments: dict[str, typing.Any]
    lifecyclePolicies: _list[LifecyclePolicy]
    maxRetryCount: int
    maxRunDuration: str
    runnables: _list[Runnable]
    volumes: _list[Volume]

@typing.type_check_only
class TaskStatus(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "ASSIGNED", "RUNNING", "FAILED", "SUCCEEDED"
    ]
    statusEvents: _list[StatusEvent]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    deviceName: str
    gcs: GCS
    mountOptions: _list[str]
    mountPath: str
    nfs: NFS
