import typing

import typing_extensions

class Volume(typing_extensions.TypedDict, total=False):
    existingDisk: ExistingDisk
    persistentDisk: PersistentDisk
    volume: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ContainerStoppedEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    stderr: str
    exitStatus: int

class CheckInResponse(typing_extensions.TypedDict, total=False):
    deadline: str
    metadata: typing.Dict[str, typing.Any]

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]
    error: Status
    done: bool

class Pipeline(typing_extensions.TypedDict, total=False):
    timeout: str
    resources: Resources
    environment: typing.Dict[str, typing.Any]
    actions: typing.List[Action]

class WorkerStatus(typing_extensions.TypedDict, total=False):
    freeRamBytes: str
    attachedDisks: typing.Dict[str, typing.Any]
    bootDisk: DiskStatus
    uptimeSeconds: str
    totalRamBytes: str

class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

class Accelerator(typing_extensions.TypedDict, total=False):
    count: str
    type: str

class ContainerStartedEvent(typing_extensions.TypedDict, total=False):
    portMappings: typing.Dict[str, typing.Any]
    ipAddress: str
    actionId: int

class PullStartedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    projectId: str
    createTime: str
    clientId: str
    startTime: str
    events: typing.List[OperationEvent]
    labels: typing.Dict[str, typing.Any]
    runtimeMetadata: typing.Dict[str, typing.Any]
    endTime: str
    request: typing.Dict[str, typing.Any]

class PersistentDisk(typing_extensions.TypedDict, total=False):
    sourceImage: str
    sizeGb: int
    type: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ContainerKilledEvent(typing_extensions.TypedDict, total=False):
    actionId: int

class Resources(typing_extensions.TypedDict, total=False):
    virtualMachine: VirtualMachine
    projectId: str
    regions: typing.List[str]
    zones: typing.List[str]

class ComputeEngine(typing_extensions.TypedDict, total=False):
    diskNames: typing.List[str]
    zone: str
    machineType: str
    instanceName: str

class Action(typing_extensions.TypedDict, total=False):
    entrypoint: str
    portMappings: typing.Dict[str, typing.Any]
    mounts: typing.List[Mount]
    name: str
    flags: typing.List[str]
    pidNamespace: str
    credentials: Secret
    commands: typing.List[str]
    imageUri: str
    timeout: str
    labels: typing.Dict[str, typing.Any]
    environment: typing.Dict[str, typing.Any]

class TimestampedEvent(typing_extensions.TypedDict, total=False):
    timestamp: str
    data: typing.Dict[str, typing.Any]

class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    computeEngine: ComputeEngine

class CheckInRequest(typing_extensions.TypedDict, total=False):
    deadlineExpired: Empty
    sosReport: str
    event: typing.Dict[str, typing.Any]
    workerStatus: WorkerStatus
    events: typing.List[TimestampedEvent]
    result: Status

class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

class Disk(typing_extensions.TypedDict, total=False):
    type: str
    sourceImage: str
    sizeGb: int
    name: str

class DelayedEvent(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    cause: str

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

class ServiceAccount(typing_extensions.TypedDict, total=False):
    scopes: typing.List[str]
    email: str

class Metadata(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str
    labels: typing.Dict[str, typing.Any]
    createTime: str
    events: typing.List[Event]
    pipeline: Pipeline

class WorkerAssignedEvent(typing_extensions.TypedDict, total=False):
    machineType: str
    instance: str
    zone: str

class Network(typing_extensions.TypedDict, total=False):
    subnetwork: str
    name: str
    usePrivateAddress: bool

class Secret(typing_extensions.TypedDict, total=False):
    keyName: str
    cipherText: str

class OperationEvent(typing_extensions.TypedDict, total=False):
    endTime: str
    description: str
    startTime: str

class DiskStatus(typing_extensions.TypedDict, total=False):
    freeSpaceBytes: str
    totalSpaceBytes: str

class WorkerReleasedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    zone: str

class Event(typing_extensions.TypedDict, total=False):
    details: typing.Dict[str, typing.Any]
    description: str
    timestamp: str

class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    exitStatus: int
    actionId: int

class ExistingDisk(typing_extensions.TypedDict, total=False):
    disk: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class VirtualMachine(typing_extensions.TypedDict, total=False):
    enableStackdriverMonitoring: bool
    nvidiaDriverVersion: str
    labels: typing.Dict[str, typing.Any]
    cpuPlatform: str
    network: Network
    disks: typing.List[Disk]
    volumes: typing.List[Volume]
    machineType: str
    accelerators: typing.List[Accelerator]
    bootDiskSizeGb: int
    serviceAccount: ServiceAccount
    preemptible: bool
    dockerCacheImages: typing.List[str]
    bootImage: str

class RunPipelineRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    pipeline: Pipeline

class Mount(typing_extensions.TypedDict, total=False):
    readOnly: bool
    path: str
    disk: str
