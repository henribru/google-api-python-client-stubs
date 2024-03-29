import typing

import typing_extensions

_list = list

@typing.type_check_only
class Accelerator(typing_extensions.TypedDict, total=False):
    count: str
    type: str

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    commands: _list[str]
    credentials: Secret
    encryptedEnvironment: Secret
    entrypoint: str
    environment: dict[str, typing.Any]
    flags: _list[
        typing_extensions.Literal[
            "FLAG_UNSPECIFIED",
            "IGNORE_EXIT_STATUS",
            "RUN_IN_BACKGROUND",
            "ALWAYS_RUN",
            "ENABLE_FUSE",
            "PUBLISH_EXPOSED_PORTS",
            "DISABLE_IMAGE_PREFETCH",
            "DISABLE_STANDARD_ERROR_CAPTURE",
            "BLOCK_EXTERNAL_NETWORK",
        ]
    ]
    imageUri: str
    labels: dict[str, typing.Any]
    mounts: _list[Mount]
    name: str
    pidNamespace: str
    portMappings: dict[str, typing.Any]
    timeout: str

@typing.type_check_only
class ContainerKilledEvent(typing_extensions.TypedDict, total=False):
    actionId: int

@typing.type_check_only
class ContainerStartedEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    ipAddress: str
    portMappings: dict[str, typing.Any]

@typing.type_check_only
class ContainerStoppedEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int
    stderr: str

@typing.type_check_only
class DelayedEvent(typing_extensions.TypedDict, total=False):
    cause: str
    metrics: _list[str]

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    name: str
    sizeGb: int
    sourceImage: str
    type: str

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    description: str
    details: dict[str, typing.Any]
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
class Metadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    events: _list[Event]
    labels: dict[str, typing.Any]
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
class PersistentDisk(typing_extensions.TypedDict, total=False):
    sizeGb: int
    sourceImage: str
    type: str

@typing.type_check_only
class Pipeline(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    encryptedEnvironment: Secret
    environment: dict[str, typing.Any]
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
    regions: _list[str]
    virtualMachine: VirtualMachine
    zones: _list[str]

@typing.type_check_only
class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    cipherText: str
    keyName: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int

@typing.type_check_only
class VirtualMachine(typing_extensions.TypedDict, total=False):
    accelerators: _list[Accelerator]
    bootDiskSizeGb: int
    bootImage: str
    cpuPlatform: str
    disks: _list[Disk]
    dockerCacheImages: _list[str]
    enableStackdriverMonitoring: bool
    labels: dict[str, typing.Any]
    machineType: str
    network: Network
    nvidiaDriverVersion: str
    preemptible: bool
    serviceAccount: ServiceAccount
    volumes: _list[Volume]

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
