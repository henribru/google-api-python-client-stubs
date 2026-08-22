import typing

_list = list

@typing.type_check_only
class CancelExecutionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing.TypedDict, total=False):
    context: str
    payload: str
    stackTrace: StackTrace

@typing.type_check_only
class Execution(typing.TypedDict, total=False):
    argument: str
    callLogLevel: typing.Literal[
        "CALL_LOG_LEVEL_UNSPECIFIED", "LOG_ALL_CALLS", "LOG_ERRORS_ONLY"
    ]
    endTime: str
    error: Error
    name: str
    result: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "UNAVAILABLE",
        "QUEUED",
    ]
    status: Status
    workflowRevisionId: str

@typing.type_check_only
class ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str

@typing.type_check_only
class Position(typing.TypedDict, total=False):
    column: str
    length: str
    line: str

@typing.type_check_only
class StackTrace(typing.TypedDict, total=False):
    elements: _list[StackTraceElement]

@typing.type_check_only
class StackTraceElement(typing.TypedDict, total=False):
    position: Position
    routine: str
    step: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    currentSteps: _list[Step]

@typing.type_check_only
class Step(typing.TypedDict, total=False):
    routine: str
    step: str
