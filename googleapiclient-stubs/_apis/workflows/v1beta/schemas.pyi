import typing

import typing_extensions

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]

class OperationMetadata(typing_extensions.TypedDict, total=False):
    target: str
    apiVersion: str
    endTime: str
    verb: str
    createTime: str

class Location(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]

class Workflow(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    description: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE"]
    createTime: str
    revisionId: str
    revisionCreateTime: str
    sourceContents: str
    name: str
    labels: typing.Dict[str, typing.Any]
    updateTime: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class ListWorkflowsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workflows: typing.List[Workflow]
    unreachable: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str
