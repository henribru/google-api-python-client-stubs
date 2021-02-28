import typing

import typing_extensions
@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListWorkflowsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: typing.List[str]
    workflows: typing.List[Workflow]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    target: str
    verb: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Workflow(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: typing.Dict[str, typing.Any]
    name: str
    revisionCreateTime: str
    revisionId: str
    serviceAccount: str
    sourceContents: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE"]
    updateTime: str
