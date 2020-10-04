import typing

import typing_extensions
@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

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
class ControllerConfig(typing_extensions.TypedDict, total=False):
    cmd: str
    disks: typing.Dict[str, typing.Any]
    gcsLogPath: str
    gcsSinks: typing.Dict[str, typing.Any]
    gcsSources: typing.Dict[str, typing.Any]
    image: str
    machineType: str
    vars: typing.Dict[str, typing.Any]

@typing.type_check_only
class DelayedEvent(typing_extensions.TypedDict, total=False):
    cause: str
    metrics: typing.List[str]

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    mountPoint: str
    name: str
    readOnly: bool
    sizeGb: int
    source: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PERSISTENT_HDD", "PERSISTENT_SSD", "LOCAL_SSD"
    ]

@typing.type_check_only
class DockerExecutor(typing_extensions.TypedDict, total=False):
    cmd: str
    imageName: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    description: str
    details: typing.Dict[str, typing.Any]
    timestamp: str

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
class ListPipelinesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    pipelines: typing.List[Pipeline]

@typing.type_check_only
class LocalCopy(typing_extensions.TypedDict, total=False):
    disk: str
    path: str

@typing.type_check_only
class LoggingOptions(typing_extensions.TypedDict, total=False):
    gcsPath: str

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
class Pipeline(typing_extensions.TypedDict, total=False):
    description: str
    docker: DockerExecutor
    inputParameters: typing.List[PipelineParameter]
    name: str
    outputParameters: typing.List[PipelineParameter]
    pipelineId: str
    projectId: str
    resources: PipelineResources

@typing.type_check_only
class PipelineParameter(typing_extensions.TypedDict, total=False):
    defaultValue: str
    description: str
    localCopy: LocalCopy
    name: str

@typing.type_check_only
class PipelineResources(typing_extensions.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str
    bootDiskSizeGb: int
    disks: typing.List[Disk]
    minimumCpuCores: int
    minimumRamGb: float
    noAddress: bool
    preemptible: bool
    zones: typing.List[str]

@typing.type_check_only
class PullStartedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

@typing.type_check_only
class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

@typing.type_check_only
class RepeatedString(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

@typing.type_check_only
class RunPipelineArgs(typing_extensions.TypedDict, total=False):
    clientId: str
    inputs: typing.Dict[str, typing.Any]
    keepVmAliveOnFailureDuration: str
    labels: typing.Dict[str, typing.Any]
    logging: LoggingOptions
    outputs: typing.Dict[str, typing.Any]
    projectId: str
    resources: PipelineResources
    serviceAccount: ServiceAccount

@typing.type_check_only
class RunPipelineRequest(typing_extensions.TypedDict, total=False):
    ephemeralPipeline: Pipeline
    pipelineArgs: RunPipelineArgs
    pipelineId: str

@typing.type_check_only
class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    computeEngine: ComputeEngine

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

@typing.type_check_only
class SetOperationStatusRequest(typing_extensions.TypedDict, total=False):
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
    errorMessage: str
    operationId: str
    timestampEvents: typing.List[TimestampEvent]
    validationToken: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimestampEvent(typing_extensions.TypedDict, total=False):
    description: str
    timestamp: str

@typing.type_check_only
class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int

@typing.type_check_only
class WorkerAssignedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    machineType: str
    zone: str

@typing.type_check_only
class WorkerReleasedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    zone: str
