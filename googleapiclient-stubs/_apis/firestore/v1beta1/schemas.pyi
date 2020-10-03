import typing

import typing_extensions

class CommitResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    writeResults: typing.List[WriteResult]

class ListCollectionIdsRequest(typing_extensions.TypedDict, total=False):
    pageToken: str
    pageSize: int

class TransactionOptions(typing_extensions.TypedDict, total=False):
    readWrite: ReadWrite
    readOnly: ReadOnly

class LatLng(typing_extensions.TypedDict, total=False):
    longitude: float
    latitude: float

StructuredQuery = typing_extensions.TypedDict(
    "StructuredQuery",
    {
        "orderBy": typing.List[Order],
        "endAt": Cursor,
        "startAt": Cursor,
        "from": typing.List[CollectionSelector],
        "where": Filter,
        "limit": int,
        "offset": int,
        "select": Projection,
    },
    total=False,
)

class GoogleFirestoreAdminV1beta1Index(typing_extensions.TypedDict, total=False):
    fields: typing.List[GoogleFirestoreAdminV1beta1IndexField]
    collectionId: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY", "ERROR"]

class RunQueryResponse(typing_extensions.TypedDict, total=False):
    skippedResults: int
    readTime: str
    document: Document
    transaction: str

class ListenResponse(typing_extensions.TypedDict, total=False):
    documentDelete: DocumentDelete
    filter: ExistenceFilter
    documentRemove: DocumentRemove
    targetChange: TargetChange
    documentChange: DocumentChange

class QueryTarget(typing_extensions.TypedDict, total=False):
    structuredQuery: StructuredQuery
    parent: str

class Value(typing_extensions.TypedDict, total=False):
    timestampValue: str
    nullValue: typing_extensions.Literal["NULL_VALUE"]
    mapValue: MapValue
    doubleValue: float
    geoPointValue: LatLng
    referenceValue: str
    arrayValue: ArrayValue
    booleanValue: bool
    stringValue: str
    bytesValue: str
    integerValue: str

class GoogleFirestoreAdminV1beta1ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    inputUriPrefix: str

class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    options: TransactionOptions

class CommitRequest(typing_extensions.TypedDict, total=False):
    writes: typing.List[Write]
    transaction: str

class GoogleFirestoreAdminV1beta1LocationMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleFirestoreAdminV1beta1ExportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    outputUriPrefix: str

class Document(typing_extensions.TypedDict, total=False):
    updateTime: str
    fields: typing.Dict[str, typing.Any]
    createTime: str
    name: str

class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: typing.List[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

class ListenRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    addTarget: Target
    removeTarget: int

class DocumentRemove(typing_extensions.TypedDict, total=False):
    removedTargetIds: typing.List[int]
    readTime: str
    document: str

class Target(typing.Dict[str, typing.Any]): ...

class Precondition(typing_extensions.TypedDict, total=False):
    updateTime: str
    exists: bool

class GoogleFirestoreAdminV1beta1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: typing.List[GoogleFirestoreAdminV1beta1Index]
    nextPageToken: str

class ReadWrite(typing_extensions.TypedDict, total=False):
    retryTransaction: str

class DocumentMask(typing_extensions.TypedDict, total=False):
    fieldPaths: typing.List[str]

class ReadOnly(typing_extensions.TypedDict, total=False):
    readTime: str

class ArrayValue(typing.Dict[str, typing.Any]): ...

class BatchGetDocumentsRequest(typing_extensions.TypedDict, total=False):
    documents: typing.List[str]
    transaction: str
    mask: DocumentMask
    readTime: str
    newTransaction: TransactionOptions

class PartitionQueryRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    structuredQuery: StructuredQuery
    pageToken: str
    partitionCount: str

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class RollbackRequest(typing_extensions.TypedDict, total=False):
    transaction: str

class GoogleFirestoreAdminV1beta1ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    operationState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    progressDocuments: GoogleFirestoreAdminV1beta1Progress
    progressBytes: GoogleFirestoreAdminV1beta1Progress
    inputUriPrefix: str
    startTime: str
    endTime: str
    collectionIds: typing.List[str]

class FieldReference(typing_extensions.TypedDict, total=False):
    fieldPath: str

class BatchWriteRequest(typing_extensions.TypedDict, total=False):
    writes: typing.List[Write]
    labels: typing.Dict[str, typing.Any]

class FieldFilter(typing_extensions.TypedDict, total=False):
    value: Value
    op: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "EQUAL",
        "NOT_EQUAL",
        "ARRAY_CONTAINS",
        "IN",
        "ARRAY_CONTAINS_ANY",
        "NOT_IN",
    ]
    field: FieldReference

class PartitionQueryResponse(typing_extensions.TypedDict, total=False):
    partitions: typing.List[Cursor]
    nextPageToken: str

class Empty(typing_extensions.TypedDict, total=False): ...

class MapValue(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]

class DocumentChange(typing_extensions.TypedDict, total=False):
    targetIds: typing.List[int]
    document: Document
    removedTargetIds: typing.List[int]

class GoogleFirestoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workEstimated: str
    workCompleted: str

class WriteResponse(typing_extensions.TypedDict, total=False):
    streamToken: str
    writeResults: typing.List[WriteResult]
    commitTime: str
    streamId: str

class GoogleFirestoreAdminV1beta1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    documentProgress: GoogleFirestoreAdminV1beta1Progress
    startTime: str
    cancelled: bool
    endTime: str
    index: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "CREATING_INDEX"
    ]

class ListDocumentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    documents: typing.List[Document]

class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

class RunQueryRequest(typing_extensions.TypedDict, total=False):
    transaction: str
    readTime: str
    newTransaction: TransactionOptions
    structuredQuery: StructuredQuery

class Projection(typing_extensions.TypedDict, total=False):
    fields: typing.List[FieldReference]

class DocumentDelete(typing_extensions.TypedDict, total=False):
    readTime: str
    removedTargetIds: typing.List[int]
    document: str

class WriteRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    streamId: str
    writes: typing.List[Write]
    streamToken: str

class GoogleFirestoreAdminV1beta1IndexField(typing_extensions.TypedDict, total=False):
    fieldPath: str
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "ASCENDING", "DESCENDING", "ARRAY_CONTAINS"
    ]

class GoogleFirestoreAdminV1beta1ExportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    progressBytes: GoogleFirestoreAdminV1beta1Progress
    operationState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    outputUriPrefix: str
    startTime: str
    collectionIds: typing.List[str]
    endTime: str
    progressDocuments: GoogleFirestoreAdminV1beta1Progress

class UnaryFilter(typing_extensions.TypedDict, total=False):
    op: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED", "IS_NAN", "IS_NULL", "IS_NOT_NAN", "IS_NOT_NULL"
    ]
    field: FieldReference

class FieldTransform(typing_extensions.TypedDict, total=False):
    removeAllFromArray: ArrayValue
    appendMissingElements: ArrayValue
    fieldPath: str
    increment: Value
    setToServerValue: typing_extensions.Literal[
        "SERVER_VALUE_UNSPECIFIED", "REQUEST_TIME"
    ]
    minimum: Value
    maximum: Value

class DocumentsTarget(typing_extensions.TypedDict, total=False):
    documents: typing.List[str]

class Write(typing.Dict[str, typing.Any]): ...
class Cursor(typing.Dict[str, typing.Any]): ...

class GoogleFirestoreAdminV1beta1ExportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

class BatchGetDocumentsResponse(typing_extensions.TypedDict, total=False):
    readTime: str
    missing: str
    transaction: str
    found: Document

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class CollectionSelector(typing_extensions.TypedDict, total=False):
    allDescendants: bool
    collectionId: str

class ExistenceFilter(typing_extensions.TypedDict, total=False):
    count: int
    targetId: int

class Filter(typing.Dict[str, typing.Any]): ...
class DocumentTransform(typing.Dict[str, typing.Any]): ...

class BatchWriteResponse(typing_extensions.TypedDict, total=False):
    status: typing.List[Status]
    writeResults: typing.List[WriteResult]

class WriteResult(typing.Dict[str, typing.Any]): ...

class TargetChange(typing_extensions.TypedDict, total=False):
    cause: Status
    targetChangeType: typing_extensions.Literal[
        "NO_CHANGE", "ADD", "REMOVE", "CURRENT", "RESET"
    ]
    resumeToken: str
    targetIds: typing.List[int]
    readTime: str

class Order(typing_extensions.TypedDict, total=False):
    field: FieldReference
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]

class ListCollectionIdsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    collectionIds: typing.List[str]
