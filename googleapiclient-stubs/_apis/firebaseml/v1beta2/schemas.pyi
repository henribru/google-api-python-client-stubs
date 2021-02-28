import typing

import typing_extensions
@typing.type_check_only
class DownloadModelResponse(typing_extensions.TypedDict, total=False):
    downloadUri: str
    expireTime: str
    modelFormat: typing_extensions.Literal["MODEL_FORMAT_UNSPECIFIED", "TFLITE"]
    sizeBytes: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListModelsResponse(typing_extensions.TypedDict, total=False):
    models: typing.List[Model]
    nextPageToken: str

@typing.type_check_only
class Model(typing_extensions.TypedDict, total=False):
    activeOperations: typing.List[Operation]
    createTime: str
    displayName: str
    etag: str
    modelHash: str
    name: str
    state: ModelState
    tags: typing.List[str]
    tfliteModel: TfLiteModel
    updateTime: str

@typing.type_check_only
class ModelOperationMetadata(typing_extensions.TypedDict, total=False):
    basicOperationStatus: typing_extensions.Literal[
        "BASIC_OPERATION_STATUS_UNSPECIFIED",
        "BASIC_OPERATION_STATUS_UPLOADING",
        "BASIC_OPERATION_STATUS_VERIFYING",
    ]
    name: str

@typing.type_check_only
class ModelState(typing_extensions.TypedDict, total=False):
    published: bool
    validationError: Status

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TfLiteModel(typing_extensions.TypedDict, total=False):
    automlModel: str
    gcsTfliteUri: str
    sizeBytes: str
