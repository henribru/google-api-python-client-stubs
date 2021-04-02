import typing

import typing_extensions
@typing.type_check_only
class CancelExecutionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    context: str
    payload: str
    stackTrace: StackTrace

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    argument: str
    endTime: str
    error: Error
    name: str
    result: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    workflowRevisionId: str

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: typing.List[Execution]
    nextPageToken: str

@typing.type_check_only
class Position(typing_extensions.TypedDict, total=False):
    column: str
    length: str
    line: str

@typing.type_check_only
class StackTrace(typing_extensions.TypedDict, total=False):
    elements: typing.List[StackTraceElement]

@typing.type_check_only
class StackTraceElement(typing_extensions.TypedDict, total=False):
    position: Position
    routine: str
    step: str
