import typing

import typing_extensions

class SetOperationStatusRequest(typing_extensions.TypedDict, total=False):
    validationToken: str
    operationId: str
    errorMessage: str
    timestampEvents: typing.List[TimestampEvent]
    errorCode: typing_extensions.Literal[
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

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class DelayedEvent(typing_extensions.TypedDict, total=False):
    metrics: typing.List[str]
    cause: str

class DockerExecutor(typing_extensions.TypedDict, total=False):
    imageName: str
    cmd: str

class PipelineResources(typing_extensions.TypedDict, total=False):
    preemptible: bool
    zones: typing.List[str]
    acceleratorCount: str
    disks: typing.List[Disk]
    bootDiskSizeGb: int
    minimumRamGb: float
    acceleratorType: str
    minimumCpuCores: int
    noAddress: bool

class Event(typing_extensions.TypedDict, total=False):
    timestamp: str
    description: str
    details: typing.Dict[str, typing.Any]

class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class OperationEvent(typing_extensions.TypedDict, total=False):
    description: str
    endTime: str
    startTime: str

class TimestampEvent(typing_extensions.TypedDict, total=False):
    description: str
    timestamp: str

class WorkerAssignedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    machineType: str
    zone: str

class ContainerStoppedEvent(typing_extensions.TypedDict, total=False):
    stderr: str
    actionId: int
    exitStatus: int

class RunPipelineRequest(typing_extensions.TypedDict, total=False):
    pipelineArgs: RunPipelineArgs
    ephemeralPipeline: Pipeline
    pipelineId: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

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

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    done: bool
    name: str
    error: Status
    response: typing.Dict[str, typing.Any]

class OperationMetadata(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    request: typing.Dict[str, typing.Any]
    endTime: str
    events: typing.List[OperationEvent]
    createTime: str
    projectId: str
    clientId: str
    startTime: str
    runtimeMetadata: typing.Dict[str, typing.Any]

class PullStartedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class LocalCopy(typing_extensions.TypedDict, total=False):
    path: str
    disk: str

class RunPipelineArgs(typing_extensions.TypedDict, total=False):
    resources: PipelineResources
    logging: LoggingOptions
    serviceAccount: ServiceAccount
    outputs: typing.Dict[str, typing.Any]
    clientId: str
    inputs: typing.Dict[str, typing.Any]
    projectId: str
    labels: typing.Dict[str, typing.Any]
    keepVmAliveOnFailureDuration: str

class ListPipelinesResponse(typing_extensions.TypedDict, total=False):
    pipelines: typing.List[Pipeline]
    nextPageToken: str

class ContainerKilledEvent(typing_extensions.TypedDict, total=False):
    actionId: int

class PipelineParameter(typing_extensions.TypedDict, total=False):
    defaultValue: str
    description: str
    name: str
    localCopy: LocalCopy

class ControllerConfig(typing_extensions.TypedDict, total=False):
    gcsSources: typing.Dict[str, typing.Any]
    disks: typing.Dict[str, typing.Any]
    vars: typing.Dict[str, typing.Any]
    gcsSinks: typing.Dict[str, typing.Any]
    image: str
    gcsLogPath: str
    machineType: str
    cmd: str

class LoggingOptions(typing_extensions.TypedDict, total=False):
    gcsPath: str

class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    computeEngine: ComputeEngine

class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int

class ContainerStartedEvent(typing_extensions.TypedDict, total=False):
    portMappings: typing.Dict[str, typing.Any]
    ipAddress: str
    actionId: int

class WorkerReleasedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    zone: str

class Pipeline(typing_extensions.TypedDict, total=False):
    inputParameters: typing.List[PipelineParameter]
    docker: DockerExecutor
    resources: PipelineResources
    description: str
    name: str
    outputParameters: typing.List[PipelineParameter]
    pipelineId: str
    projectId: str

class Disk(typing_extensions.TypedDict, total=False):
    name: str
    sizeGb: int
    autoDelete: bool
    readOnly: bool
    source: str
    mountPoint: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PERSISTENT_HDD", "PERSISTENT_SSD", "LOCAL_SSD"
    ]

class ComputeEngine(typing_extensions.TypedDict, total=False):
    instanceName: str
    diskNames: typing.List[str]
    zone: str
    machineType: str

class RepeatedString(typing_extensions.TypedDict, total=False):
    values: typing.List[str]
