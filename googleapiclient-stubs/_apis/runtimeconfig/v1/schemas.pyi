import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str
