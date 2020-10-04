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
class DelayedEvent(typing_extensions.TypedDict, total=False):
    cause: str
    metrics: typing.List[str]

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
class PullStartedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

@typing.type_check_only
class PullStoppedEvent(typing_extensions.TypedDict, total=False):
    imageUri: str

@typing.type_check_only
class RunPipelineResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeMetadata(typing_extensions.TypedDict, total=False):
    computeEngine: ComputeEngine

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

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
