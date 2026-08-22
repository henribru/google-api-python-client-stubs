import typing

_list = list

@typing.type_check_only
class DownloadModelResponse(typing.TypedDict, total=False):
    downloadUri: str
    expireTime: str
    modelFormat: typing.Literal["MODEL_FORMAT_UNSPECIFIED", "TFLITE"]
    sizeBytes: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListModelsResponse(typing.TypedDict, total=False):
    models: _list[Model]
    nextPageToken: str

@typing.type_check_only
class Model(typing.TypedDict, total=False):
    activeOperations: _list[Operation]
    createTime: str
    displayName: str
    etag: str
    modelHash: str
    name: str
    state: ModelState
    tags: _list[str]
    tfliteModel: TfLiteModel
    updateTime: str

@typing.type_check_only
class ModelOperationMetadata(typing.TypedDict, total=False):
    basicOperationStatus: typing.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str

@typing.type_check_only
class ModelState(typing.TypedDict, total=False):
    published: bool
    validationError: Status

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TfLiteModel(typing.TypedDict, total=False):
    automlModel: str
    gcsTfliteUri: str
    sizeBytes: str
