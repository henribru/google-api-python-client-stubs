import typing

import typing_extensions

_list = list

@typing.type_check_only
class Callback(typing_extensions.TypedDict, total=False):
    availablePayloads: _list[str]
    method: str
    name: str
    waiters: str

@typing.type_check_only
class CancelExecutionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteExecutionHistoryRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    context: str
    payload: str
    stackTrace: StackTrace

@typing.type_check_only
class Exception(typing_extensions.TypedDict, total=False):
    payload: str

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    argument: str
    callLogLevel: typing_extensions.Literal[
        "CALL_LOG_LEVEL_UNSPECIFIED", "LOG_ALL_CALLS", "LOG_ERRORS_ONLY", "LOG_NONE"
    ]
    createTime: str
    disableConcurrencyQuotaOverflowBuffering: bool
    duration: str
    endTime: str
    error: Error
    executionHistoryLevel: typing_extensions.Literal[
        "EXECUTION_HISTORY_LEVEL_UNSPECIFIED",
        "EXECUTION_HISTORY_BASIC",
        "EXECUTION_HISTORY_DETAILED",
    ]
    labels: dict[str, typing.Any]
    name: str
    result: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "UNAVAILABLE",
        "QUEUED",
    ]
    stateError: StateError
    status: Status
    workflowRevisionId: str

@typing.type_check_only
class ExportDataResponse(typing_extensions.TypedDict, total=False):
    data: str

@typing.type_check_only
class ListCallbacksResponse(typing_extensions.TypedDict, total=False):
    callbacks: _list[Callback]
    nextPageToken: str

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str

@typing.type_check_only
class ListStepEntriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    stepEntries: _list[StepEntry]
    totalSize: int

@typing.type_check_only
class NavigationInfo(typing_extensions.TypedDict, total=False):
    children: _list[str]
    next: str
    parent: str
    previous: str

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
class StateError(typing_extensions.TypedDict, total=False):
    details: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "KMS_ERROR"]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    currentSteps: _list[Step]

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    routine: str
    step: str

@typing.type_check_only
class StepEntry(typing_extensions.TypedDict, total=False):
    createTime: str
    entryId: str
    exception: Exception
    name: str
    navigationInfo: NavigationInfo
    routine: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_IN_PROGRESS",
        "STATE_SUCCEEDED",
        "STATE_FAILED",
        "STATE_CANCELLED",
    ]
    step: str
    stepEntryMetadata: StepEntryMetadata
    stepType: typing_extensions.Literal[
        "STEP_TYPE_UNSPECIFIED",
        "STEP_ASSIGN",
        "STEP_STD_LIB_CALL",
        "STEP_CONNECTOR_CALL",
        "STEP_SUBWORKFLOW_CALL",
        "STEP_CALL",
        "STEP_SWITCH",
        "STEP_CONDITION",
        "STEP_FOR",
        "STEP_FOR_ITERATION",
        "STEP_PARALLEL_FOR",
        "STEP_PARALLEL_BRANCH",
        "STEP_PARALLEL_BRANCH_ENTRY",
        "STEP_TRY_RETRY_EXCEPT",
        "STEP_TRY",
        "STEP_RETRY",
        "STEP_EXCEPT",
        "STEP_RETURN",
        "STEP_RAISE",
        "STEP_GOTO",
    ]
    updateTime: str
    variableData: VariableData

@typing.type_check_only
class StepEntryMetadata(typing_extensions.TypedDict, total=False):
    expectedIteration: str
    progressNumber: str
    progressType: typing_extensions.Literal[
        "PROGRESS_TYPE_UNSPECIFIED",
        "PROGRESS_TYPE_FOR",
        "PROGRESS_TYPE_SWITCH",
        "PROGRESS_TYPE_RETRY",
        "PROGRESS_TYPE_PARALLEL_FOR",
        "PROGRESS_TYPE_PARALLEL_BRANCH",
    ]
    threadId: str

@typing.type_check_only
class TriggerPubsubExecutionRequest(typing_extensions.TypedDict, total=False):
    GCPCloudEventsMode: str
    deliveryAttempt: int
    message: PubsubMessage
    subscription: str

@typing.type_check_only
class VariableData(typing_extensions.TypedDict, total=False):
    variables: dict[str, typing.Any]
