import typing

import typing_extensions
@typing.type_check_only
class Accelerator(typing_extensions.TypedDict, total=False):
    count: str
    type: str

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    commands: typing.List[str]
    credentials: Secret
    entrypoint: str
    environment: typing.Dict[str, typing.Any]
    flags: typing.List[str]
    imageUri: str
    labels: typing.Dict[str, typing.Any]
    mounts: typing.List[Mount]
    name: str
    pidNamespace: str
    portMappings: typing.Dict[str, typing.Any]
    timeout: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckInRequest(typing_extensions.TypedDict, total=False):
    deadlineExpired: Empty
    event: typing.Dict[str, typing.Any]
    events: typing.List[TimestampedEvent]
    result: Status
    sosReport: str
    workerStatus: WorkerStatus

@typing.type_check_only
class CheckInResponse(typing_extensions.TypedDict, total=False):
    deadline: str
    features: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class ComputeEngine(typing_extensions.TypedDict, total=False):
    diskNames: typing.List[str]
    instanceName: str
    machineType: str
    zone: str

@typing.type_check_only
class ContainerKilledEvent(typing_extensions.TypedDict, total=False):
    actionId: int

@typing.type_check_only
class ContainerStartedEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    ipAddress: str
    portMappings: typing.Dict[str, typing.Any]

@typing.type_check_only
class ContainerStoppedEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int
    stderr: str

@typing.type_check_only
class DelayedEvent(typing_extensions.TypedDict, total=False):
    cause: str
    metrics: typing.List[str]

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    name: str
    sizeGb: int
    sourceImage: str
    type: str

@typing.type_check_only
class DiskStatus(typing_extensions.TypedDict, total=False):
    freeSpaceBytes: str
    totalSpaceBytes: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    description: str
    details: typing.Dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class ExistingDisk(typing_extensions.TypedDict, total=False):
    disk: str

@typing.type_check_only
class FailedEvent(typing_extensions.TypedDict, total=False):
    cause: str
    code: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    events: typing.List[Event]
    labels: typing.Dict[str, typing.Any]
    pipeline: Pipeline
    startTime: str

@typing.type_check_only
class Mount(typing_extensions.TypedDict, total=False):
    disk: str
    path: str
    readOnly: bool

@typing.type_check_only
class NFSMount(typing_extensions.TypedDict, total=False):
    target: str

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    name: str
    subnetwork: str
    usePrivateAddress: bool

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationEvent(typing_extensions.TypedDict, total=False):
    description: str
    endTime: str
    startTime: str

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    clientId: str
    createTime: str
    endTime: str
    events: typing.List[OperationEvent]
    labels: typing.Dict[str, typing.Any]
    projectId: str
    request: typing.Dict[str, typing.Any]
    runtimeMetadata: typing.Dict[str, typing.Any]
    startTime: str

@typing.type_check_only
class PersistentDisk(typing_extensions.TypedDict, total=False):
    sizeGb: int
    sourceImage: str
    type: str

@typing.type_check_only
class Pipeline(typing_extensions.TypedDict, total=False):
    actions: typing.List[Action]
    environment: typing.Dict[str, typing.Any]
    resources: Resources
    timeout: str

@typing.type_check_only
class PullStartedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

@typing.type_check_only
class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    projectId: str
    regions: typing.List[str]
    virtualMachine: VirtualMachine
    zones: typing.List[str]

@typing.type_check_only
class RunPipelineRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    pipeline: Pipeline
    pubSubTopic: str

@typing.type_check_only
class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    computeEngine: ComputeEngine

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    cipherText: str
    keyName: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimestampedEvent(typing_extensions.TypedDict, total=False):
    data: typing.Dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int

@typing.type_check_only
class VirtualMachine(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[Accelerator]
    bootDiskSizeGb: int
    bootImage: str
    cpuPlatform: str
    disks: typing.List[Disk]
    dockerCacheImages: typing.List[str]
    enableStackdriverMonitoring: bool
    labels: typing.Dict[str, typing.Any]
    machineType: str
    network: Network
    nvidiaDriverVersion: str
    preemptible: bool
    serviceAccount: ServiceAccount
    volumes: typing.List[Volume]

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    existingDisk: ExistingDisk
    nfsMount: NFSMount
    persistentDisk: PersistentDisk
    volume: str

@typing.type_check_only
class WorkerAssignedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    machineType: str
    zone: str

@typing.type_check_only
class WorkerReleasedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    zone: str

@typing.type_check_only
class WorkerStatus(typing_extensions.TypedDict, total=False):
    attachedDisks: typing.Dict[str, typing.Any]
    bootDisk: DiskStatus
    freeRamBytes: str
    totalRamBytes: str
    uptimeSeconds: str
