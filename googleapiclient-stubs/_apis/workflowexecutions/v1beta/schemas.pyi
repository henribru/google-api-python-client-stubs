import typing

import typing_extensions

class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: typing.List[Execution]
    nextPageToken: str

class CancelExecutionRequest(typing_extensions.TypedDict, total=False): ...

class Execution(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    result: str
    error: Error
    endTime: str
    argument: str
    startTime: str
    workflowRevisionId: str

class Error(typing_extensions.TypedDict, total=False):
    payload: str
    context: str
