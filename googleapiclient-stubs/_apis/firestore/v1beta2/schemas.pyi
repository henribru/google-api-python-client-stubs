import typing

import typing_extensions

class GoogleFirestoreAdminV1beta2ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    operationState: typing_extensions.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    progressBytes: GoogleFirestoreAdminV1beta2Progress
    inputUriPrefix: str
    endTime: str
    startTime: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleFirestoreAdminV1beta2ListFieldsResponse(
    typing_extensions.TypedDict, total=False
):
    fields: typing.List[GoogleFirestoreAdminV1beta2Field]
    nextPageToken: str

class GoogleFirestoreAdminV1beta2FieldOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    documentProgress: GoogleFirestoreAdminV1beta2Progress
    field: str
    startTime: str
    bytesProgress: GoogleFirestoreAdminV1beta2Progress
    state: typing_extensions.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    indexConfigDeltas: typing.List[GoogleFirestoreAdminV1beta2IndexConfigDelta]
    endTime: str

class GoogleFirestoreAdminV1beta2ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    indexes: typing.List[GoogleFirestoreAdminV1beta2Index]

class GoogleFirestoreAdminV1beta2ExportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str
    collectionIds: typing.List[str]
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    endTime: str
    startTime: str
    operationState: typing_extensions.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    progressBytes: GoogleFirestoreAdminV1beta2Progress

class GoogleFirestoreAdminV1beta2ExportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

class GoogleFirestoreAdminV1beta2ExportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    outputUriPrefix: str

class GoogleFirestoreAdminV1beta2Progress(typing_extensions.TypedDict, total=False):
    completedWork: str
    estimatedWork: str

class GoogleFirestoreAdminV1beta2ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    inputUriPrefix: str
    collectionIds: typing.List[str]

class GoogleFirestoreAdminV1beta2Index(typing_extensions.TypedDict, total=False):
    queryScope: typing_extensions.Literal[
        "QUERY_SCOPE_UNSPECIFIED", "COLLECTION", "COLLECTION_GROUP"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "NEEDS_REPAIR"
    ]
    fields: typing.List[GoogleFirestoreAdminV1beta2IndexField]
    name: str

class GoogleFirestoreAdminV1beta2IndexConfig(typing_extensions.TypedDict, total=False):
    reverting: bool
    usesAncestorConfig: bool
    ancestorField: str
    indexes: typing.List[GoogleFirestoreAdminV1beta2Index]

class GoogleFirestoreAdminV1beta2IndexField(typing_extensions.TypedDict, total=False):
    order: typing_extensions.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    arrayConfig: typing_extensions.Literal["ARRAY_CONFIG_UNSPECIFIED", "CONTAINS"]
    fieldPath: str

class GoogleFirestoreAdminV1beta2Field(typing_extensions.TypedDict, total=False):
    name: str
    indexConfig: GoogleFirestoreAdminV1beta2IndexConfig

class GoogleFirestoreAdminV1beta2IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    progressBytes: GoogleFirestoreAdminV1beta2Progress
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    state: typing_extensions.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    endTime: str
    startTime: str
    index: str

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    name: str
    response: typing.Dict[str, typing.Any]

class GoogleFirestoreAdminV1beta2IndexConfigDelta(
    typing_extensions.TypedDict, total=False
):
    index: GoogleFirestoreAdminV1beta2Index
    changeType: typing_extensions.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
