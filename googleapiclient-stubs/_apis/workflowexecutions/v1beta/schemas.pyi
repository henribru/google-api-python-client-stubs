import typing

import typing_extensions
@typing.type_check_only
class CancelExecutionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    context: str
    payload: str

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
