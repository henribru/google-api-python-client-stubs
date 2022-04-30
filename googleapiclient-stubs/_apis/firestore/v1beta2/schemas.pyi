import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1UpdateDatabaseMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ExportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    collectionIds: _list[str]
    endTime: str
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
    outputUriPrefix: str
    progressBytes: GoogleFirestoreAdminV1beta2Progress
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ExportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: _list[str]
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ExportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2Field(typing_extensions.TypedDict, total=False):
    indexConfig: GoogleFirestoreAdminV1beta2IndexConfig
    name: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2FieldOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    bytesProgress: GoogleFirestoreAdminV1beta2Progress
    documentProgress: GoogleFirestoreAdminV1beta2Progress
    endTime: str
    field: str
    indexConfigDeltas: _list[GoogleFirestoreAdminV1beta2IndexConfigDelta]
    startTime: str
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

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    collectionIds: _list[str]
    endTime: str
    inputUriPrefix: str
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
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: _list[str]
    inputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2Index(typing_extensions.TypedDict, total=False):
    fields: _list[GoogleFirestoreAdminV1beta2IndexField]
    name: str
    queryScope: typing_extensions.Literal[
        "QUERY_SCOPE_UNSPECIFIED", "COLLECTION", "COLLECTION_GROUP"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "NEEDS_REPAIR"
    ]

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexConfig(typing_extensions.TypedDict, total=False):
    ancestorField: str
    indexes: _list[GoogleFirestoreAdminV1beta2Index]
    reverting: bool
    usesAncestorConfig: bool

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexConfigDelta(
    typing_extensions.TypedDict, total=False
):
    changeType: typing_extensions.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
    index: GoogleFirestoreAdminV1beta2Index

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexField(typing_extensions.TypedDict, total=False):
    arrayConfig: typing_extensions.Literal["ARRAY_CONFIG_UNSPECIFIED", "CONTAINS"]
    fieldPath: str
    order: typing_extensions.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    index: str
    progressBytes: GoogleFirestoreAdminV1beta2Progress
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    startTime: str
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

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ListFieldsResponse(
    typing_extensions.TypedDict, total=False
):
    fields: _list[GoogleFirestoreAdminV1beta2Field]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: _list[GoogleFirestoreAdminV1beta2Index]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2Progress(typing_extensions.TypedDict, total=False):
    completedWork: str
    estimatedWork: str

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
