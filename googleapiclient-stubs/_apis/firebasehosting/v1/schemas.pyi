import typing

import typing_extensions

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    name: str
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    done: bool

class Empty(typing_extensions.TypedDict, total=False): ...
