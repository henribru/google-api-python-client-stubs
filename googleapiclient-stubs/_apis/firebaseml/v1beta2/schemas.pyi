import typing

import typing_extensions

class TfLiteModel(typing_extensions.TypedDict, total=False):
    automlModel: str
    gcsTfliteUri: str
    sizeBytes: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    name: str

class ListModelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    models: typing.List[Model]

class Empty(typing_extensions.TypedDict, total=False): ...

class Model(typing_extensions.TypedDict, total=False):
    state: ModelState
    activeOperations: typing.List[Operation]
    etag: str
    name: str
    modelHash: str
    tags: typing.List[str]
    tfliteModel: TfLiteModel
    displayName: str
    createTime: str
    updateTime: str

class ModelState(typing_extensions.TypedDict, total=False):
    published: bool
    validationError: Status

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class ModelOperationMetadata(typing_extensions.TypedDict, total=False):
    basicOperationStatus: typing_extensions.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str
