import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1BulkDeleteDocumentsMetadata(typing.TypedDict, total=False):
    collectionIds: _list[str]
    endTime: str
    namespaceIds: _list[str]
    operationState: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1CloneDatabaseMetadata(typing.TypedDict, total=False):
    database: str
    endTime: str
    operationState: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    pitrSnapshot: GoogleFirestoreAdminV1PitrSnapshot
    progressPercentage: GoogleFirestoreAdminV1Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1CreateDatabaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1DeleteDatabaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1PitrSnapshot(typing.TypedDict, total=False):
    database: str
    databaseUid: str
    snapshotTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1Progress(typing.TypedDict, total=False):
    completedWork: str
    estimatedWork: str

@typing.type_check_only
class GoogleFirestoreAdminV1RestoreDatabaseMetadata(typing.TypedDict, total=False):
    backup: str
    database: str
    endTime: str
    operationState: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    progressPercentage: GoogleFirestoreAdminV1Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1UpdateDatabaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ExportDocumentsMetadata(typing.TypedDict, total=False):
    collectionIds: _list[str]
    endTime: str
    operationState: typing.Literal[
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
class GoogleFirestoreAdminV1beta2ExportDocumentsRequest(typing.TypedDict, total=False):
    collectionIds: _list[str]
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ExportDocumentsResponse(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2Field(typing.TypedDict, total=False):
    indexConfig: GoogleFirestoreAdminV1beta2IndexConfig
    name: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2FieldOperationMetadata(typing.TypedDict, total=False):
    bytesProgress: GoogleFirestoreAdminV1beta2Progress
    documentProgress: GoogleFirestoreAdminV1beta2Progress
    endTime: str
    field: str
    indexConfigDeltas: _list[GoogleFirestoreAdminV1beta2IndexConfigDelta]
    startTime: str
    state: typing.Literal[
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
class GoogleFirestoreAdminV1beta2ImportDocumentsMetadata(typing.TypedDict, total=False):
    collectionIds: _list[str]
    endTime: str
    inputUriPrefix: str
    operationState: typing.Literal[
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
class GoogleFirestoreAdminV1beta2ImportDocumentsRequest(typing.TypedDict, total=False):
    collectionIds: _list[str]
    inputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2Index(typing.TypedDict, total=False):
    fields: _list[GoogleFirestoreAdminV1beta2IndexField]
    name: str
    queryScope: typing.Literal[
        "QUERY_SCOPE_UNSPECIFIED", "COLLECTION", "COLLECTION_GROUP"
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY", "NEEDS_REPAIR"]

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexConfig(typing.TypedDict, total=False):
    ancestorField: str
    indexes: _list[GoogleFirestoreAdminV1beta2Index]
    reverting: bool
    usesAncestorConfig: bool

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexConfigDelta(typing.TypedDict, total=False):
    changeType: typing.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
    index: GoogleFirestoreAdminV1beta2Index

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexField(typing.TypedDict, total=False):
    arrayConfig: typing.Literal["ARRAY_CONFIG_UNSPECIFIED", "CONTAINS"]
    fieldPath: str
    order: typing.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexOperationMetadata(typing.TypedDict, total=False):
    endTime: str
    index: str
    progressBytes: GoogleFirestoreAdminV1beta2Progress
    progressDocuments: GoogleFirestoreAdminV1beta2Progress
    startTime: str
    state: typing.Literal[
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
class GoogleFirestoreAdminV1beta2ListFieldsResponse(typing.TypedDict, total=False):
    fields: _list[GoogleFirestoreAdminV1beta2Field]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ListIndexesResponse(typing.TypedDict, total=False):
    indexes: _list[GoogleFirestoreAdminV1beta2Index]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1beta2Progress(typing.TypedDict, total=False):
    completedWork: str
    estimatedWork: str

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
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
