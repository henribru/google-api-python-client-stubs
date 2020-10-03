import typing

import typing_extensions

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status

class Empty(typing_extensions.TypedDict, total=False): ...

class ModelOperationMetadata(typing_extensions.TypedDict, total=False):
    basicOperationStatus: typing_extensions.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
