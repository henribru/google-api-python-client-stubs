import typing

import typing_extensions

_list = list

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
    callLogLevel: typing_extensions.Literal[
        "CALL_LOG_LEVEL_UNSPECIFIED", "LOG_ALL_CALLS", "LOG_ERRORS_ONLY"
    ]
    endTime: str
    error: Error
    name: str
    result: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    status: Status
    workflowRevisionId: str

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str

@typing.type_check_only
class Position(typing_extensions.TypedDict, total=False):
    column: str
    length: str
    line: str

@typing.type_check_only
class PubsubMessage(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    data: str
    messageId: str
    orderingKey: str
    publishTime: str

@typing.type_check_only
class StackTrace(typing_extensions.TypedDict, total=False):
    elements: _list[StackTraceElement]

@typing.type_check_only
class StackTraceElement(typing_extensions.TypedDict, total=False):
    position: Position
    routine: str
    step: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    currentSteps: _list[Step]

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    routine: str
    step: str

@typing.type_check_only
class TriggerPubsubExecutionRequest(typing_extensions.TypedDict, total=False):
    GCPCloudEventsMode: str
    message: PubsubMessage
    subscription: str
