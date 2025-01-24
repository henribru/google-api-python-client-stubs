import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListWorkflowRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workflows: _list[Workflow]

@typing.type_check_only
class ListWorkflowsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workflows: _list[Workflow]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    target: str
    verb: str

@typing.type_check_only
class StateError(typing_extensions.TypedDict, total=False):
    details: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "KMS_ERROR"]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Workflow(typing_extensions.TypedDict, total=False):
    allKmsKeys: _list[str]
    allKmsKeysVersions: _list[str]
    callLogLevel: typing_extensions.Literal[
        "CALL_LOG_LEVEL_UNSPECIFIED", "LOG_ALL_CALLS", "LOG_ERRORS_ONLY", "LOG_NONE"
    ]
    createTime: str
    cryptoKeyName: str
    cryptoKeyVersion: str
    description: str
    executionHistoryLevel: typing_extensions.Literal[
        "EXECUTION_HISTORY_LEVEL_UNSPECIFIED",
        "EXECUTION_HISTORY_BASIC",
        "EXECUTION_HISTORY_DETAILED",
    ]
    labels: dict[str, typing.Any]
    name: str
    revisionCreateTime: str
    revisionId: str
    serviceAccount: str
    sourceContents: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "UNAVAILABLE"]
    stateError: StateError
    tags: dict[str, typing.Any]
    updateTime: str
    userEnvVars: dict[str, typing.Any]
