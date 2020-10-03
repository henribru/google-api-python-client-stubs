import typing

import typing_extensions

class OperationMetadata(typing_extensions.TypedDict, total=False):
    runtimeMetadata: typing.Dict[str, typing.Any]
    endTime: str
    startTime: str
    projectId: str
    clientId: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    events: typing.List[OperationEvent]
    request: typing.Dict[str, typing.Any]

class DelayedEvent(typing_extensions.TypedDict, total=False):
    cause: str
    metrics: typing.List[str]

class WorkerAssignedEvent(typing_extensions.TypedDict, total=False):
    zone: str
    machineType: str
    instance: str

class Event(typing_extensions.TypedDict, total=False):
    timestamp: str
    details: typing.Dict[str, typing.Any]
    description: str

class ComputeEngine(typing_extensions.TypedDict, total=False):
    machineType: str
    instanceName: str
    diskNames: typing.List[str]
    zone: str

class ContainerStoppedEvent(typing_extensions.TypedDict, total=False):
    stderr: str
    actionId: int
    exitStatus: int

class Empty(typing_extensions.TypedDict, total=False): ...

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: Status
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]

class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

class ContainerStartedEvent(typing_extensions.TypedDict, total=False):
    ipAddress: str
    actionId: int
    portMappings: typing.Dict[str, typing.Any]

class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    computeEngine: ComputeEngine

class WorkerReleasedEvent(typing_extensions.TypedDict, total=False):
    instance: str
    zone: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class UnexpectedExitStatusEvent(typing_extensions.TypedDict, total=False):
    actionId: int
    exitStatus: int

class OperationEvent(typing_extensions.TypedDict, total=False):
    endTime: str
    description: str
    startTime: str

class ContainerKilledEvent(typing_extensions.TypedDict, total=False):
    actionId: int

class PullStartedEvent(typing_extensions.TypedDict, total=False):
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
