import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    error: Status
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    done: bool

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int
