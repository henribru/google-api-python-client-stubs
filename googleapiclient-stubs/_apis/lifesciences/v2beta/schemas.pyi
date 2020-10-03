import typing

import typing_extensions

class DelayedEvent(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    cause: str

class Action(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    commands: typing.List[str]
    ignoreExitStatus: bool
    mounts: typing.List[Mount]
    publishExposedPorts: bool
    pidNamespace: str
    credentials: Secret
    imageUri: str
    timeout: str
    portMappings: typing.Dict[str, typing.Any]
    runInBackground: bool
    entrypoint: str
    disableStandardErrorCapture: bool
    disableImagePrefetch: bool
    enableFuse: bool
    environment: typing.Dict[str, typing.Any]
    alwaysRun: bool
    containerName: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    exitStatus: int
    actionId: int

class PullStartedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

class Disk(typing_extensions.TypedDict, total=False):
    sizeGb: int
    name: str
    type: str
    sourceImage: str

class WorkerAssignedEvent(typing_extensions.TypedDict, total=False):
    machineType: str
    zone: str
    instance: str

class RunPipelineRequest(typing_extensions.TypedDict, total=False):
    pipeline: Pipeline
    labels: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class WorkerReleasedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    zone: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class ContainerKilledEvent(typing_extensions.TypedDict, total=False):
    actionId: int

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    name: str
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    metadata: typing.Dict[str, typing.Any]
    locationId: str
    labels: typing.Dict[str, typing.Any]
    name: str

class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

class VirtualMachine(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[Accelerator]
    labels: typing.Dict[str, typing.Any]
    bootImage: str
    disks: typing.List[Disk]
    bootDiskSizeGb: int
    machineType: str
    dockerCacheImages: typing.List[str]
    network: Network
    enableStackdriverMonitoring: bool
    cpuPlatform: str
    preemptible: bool
    nvidiaDriverVersion: str
    serviceAccount: ServiceAccount

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class Resources(typing_extensions.TypedDict, total=False):
    regions: typing.List[str]
    virtualMachine: VirtualMachine
    zones: typing.List[str]

class Event(typing_extensions.TypedDict, total=False):
    description: str
    failed: FailedEvent
    containerKilled: ContainerKilledEvent
    containerStarted: ContainerStartedEvent
    pullStarted: PullStartedEvent
    unexpectedExitStatus: UnexpectedExitStatusEvent
    delayed: DelayedEvent
    timestamp: str
    pullStopped: PullStoppedEvent
    workerAssigned: WorkerAssignedEvent
    workerReleased: WorkerReleasedEvent
    containerStopped: ContainerStoppedEvent

class ContainerStartedEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    ipAddress: str
    portMappings: typing.Dict[str, typing.Any]

class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

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

class Network(typing_extensions.TypedDict, total=False):
    network: str
    usePrivateAddress: bool
    subnetwork: str

class ServiceAccount(typing_extensions.TypedDict, total=False):
    scopes: typing.List[str]
    email: str

class Metadata(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    pipeline: Pipeline
    events: typing.List[Event]

class Secret(typing_extensions.TypedDict, total=False):
    keyName: str
    cipherText: str

class Mount(typing_extensions.TypedDict, total=False):
    readOnly: bool
    path: str
    disk: str

class Pipeline(typing_extensions.TypedDict, total=False):
    resources: Resources
    timeout: str
    environment: typing.Dict[str, typing.Any]
    actions: typing.List[Action]

class ContainerStoppedEvent(typing_extensions.TypedDict, total=False):
    exitStatus: int
    stderr: str
    actionId: int

class Accelerator(typing_extensions.TypedDict, total=False):
    count: str
    type: str
