import typing

import typing_extensions

class QueryTarget(typing_extensions.TypedDict, total=False):
    parent: str
    structuredQuery: StructuredQuery

class FieldFilter(typing_extensions.TypedDict, total=False):
    field: FieldReference
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

class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: typing.List[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

class Filter(typing.Dict[str, typing.Any]): ...

class ReadOnly(typing_extensions.TypedDict, total=False):
    readTime: str

class CommitResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    writeResults: typing.List[WriteResult]

class ExistenceFilter(typing_extensions.TypedDict, total=False):
    count: int
    targetId: int

class GoogleFirestoreAdminV1Index(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "NEEDS_REPAIR"
    ]
    name: str
    fields: typing.List[GoogleFirestoreAdminV1IndexField]
    queryScope: typing_extensions.Literal[
        "QUERY_SCOPE_UNSPECIFIED", "COLLECTION", "COLLECTION_GROUP"
    ]

class Empty(typing_extensions.TypedDict, total=False): ...

class DocumentChange(typing_extensions.TypedDict, total=False):
    document: Document
    targetIds: typing.List[int]
    removedTargetIds: typing.List[int]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class RunQueryResponse(typing_extensions.TypedDict, total=False):
    document: Document
    readTime: str
    transaction: str
    skippedResults: int

class GoogleFirestoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    estimatedWork: str
    completedWork: str

class PartitionQueryRequest(typing_extensions.TypedDict, total=False):
    structuredQuery: StructuredQuery
    pageSize: int
    partitionCount: str
    pageToken: str

class WriteRequest(typing_extensions.TypedDict, total=False):
    streamId: str
    writes: typing.List[Write]
    streamToken: str
    labels: typing.Dict[str, typing.Any]

class GoogleFirestoreAdminV1ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    progressDocuments: GoogleFirestoreAdminV1Progress
    collectionIds: typing.List[str]
    inputUriPrefix: str
    startTime: str
    endTime: str
    progressBytes: GoogleFirestoreAdminV1Progress
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

class DocumentsTarget(typing_extensions.TypedDict, total=False):
    documents: typing.List[str]

class GoogleFirestoreAdminV1Field(typing_extensions.TypedDict, total=False):
    indexConfig: GoogleFirestoreAdminV1IndexConfig
    name: str

class BatchGetDocumentsRequest(typing_extensions.TypedDict, total=False):
    newTransaction: TransactionOptions
    transaction: str
    documents: typing.List[str]
    readTime: str
    mask: DocumentMask

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class UnaryFilter(typing_extensions.TypedDict, total=False):
    op: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED", "IS_NAN", "IS_NULL", "IS_NOT_NAN", "IS_NOT_NULL"
    ]
    field: FieldReference

class FieldTransform(typing_extensions.TypedDict, total=False):
    increment: Value
    maximum: Value
    appendMissingElements: ArrayValue
    minimum: Value
    setToServerValue: typing_extensions.Literal[
        "SERVER_VALUE_UNSPECIFIED", "REQUEST_TIME"
    ]
    removeAllFromArray: ArrayValue
    fieldPath: str

class MapValue(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]

class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

class GoogleFirestoreAdminV1FieldOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    endTime: str
    indexConfigDeltas: typing.List[GoogleFirestoreAdminV1IndexConfigDelta]
    field: str
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
    startTime: str

class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    options: TransactionOptions

class FieldReference(typing_extensions.TypedDict, total=False):
    fieldPath: str

class Value(typing.Dict[str, typing.Any]): ...

class GoogleFirestoreAdminV1IndexField(typing_extensions.TypedDict, total=False):
    order: typing_extensions.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    fieldPath: str
    arrayConfig: typing_extensions.Literal["ARRAY_CONFIG_UNSPECIFIED", "CONTAINS"]

class GoogleFirestoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    progressDocuments: GoogleFirestoreAdminV1Progress
    progressBytes: GoogleFirestoreAdminV1Progress
    startTime: str
    endTime: str
    index: str
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

class DocumentDelete(typing_extensions.TypedDict, total=False):
    removedTargetIds: typing.List[int]
    document: str
    readTime: str

class CommitRequest(typing_extensions.TypedDict, total=False):
    transaction: str
    writes: typing.List[Write]

class PartitionQueryResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partitions: typing.List[Cursor]

class RollbackRequest(typing_extensions.TypedDict, total=False):
    transaction: str

class Projection(typing_extensions.TypedDict, total=False):
    fields: typing.List[FieldReference]

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    name: str
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]

class GoogleFirestoreAdminV1ListFieldsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    fields: typing.List[GoogleFirestoreAdminV1Field]

class WriteResponse(typing_extensions.TypedDict, total=False):
    streamToken: str
    streamId: str
    writeResults: typing.List[WriteResult]
    commitTime: str

class BatchWriteResponse(typing_extensions.TypedDict, total=False):
    writeResults: typing.List[WriteResult]
    status: typing.List[Status]

class GoogleFirestoreAdminV1ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    inputUriPrefix: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

class TransactionOptions(typing_extensions.TypedDict, total=False):
    readWrite: ReadWrite
    readOnly: ReadOnly

class ListDocumentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    documents: typing.List[Document]

class Precondition(typing_extensions.TypedDict, total=False):
    updateTime: str
    exists: bool

class ArrayValue(typing.Dict[str, typing.Any]): ...

class GoogleFirestoreAdminV1ExportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    progressDocuments: GoogleFirestoreAdminV1Progress
    startTime: str
    outputUriPrefix: str
    collectionIds: typing.List[str]
    progressBytes: GoogleFirestoreAdminV1Progress
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
    endTime: str

class DocumentRemove(typing_extensions.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: typing.List[int]

class DocumentMask(typing_extensions.TypedDict, total=False):
    fieldPaths: typing.List[str]

class Write(typing.Dict[str, typing.Any]): ...

class Location(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    name: str
    locationId: str
    displayName: str

class GoogleFirestoreAdminV1ExportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    outputUriPrefix: str

class GoogleFirestoreAdminV1IndexConfig(typing_extensions.TypedDict, total=False):
    indexes: typing.List[GoogleFirestoreAdminV1Index]
    ancestorField: str
    reverting: bool
    usesAncestorConfig: bool

class DocumentTransform(typing.Dict[str, typing.Any]): ...

class TargetChange(typing_extensions.TypedDict, total=False):
    targetChangeType: typing_extensions.Literal[
        "NO_CHANGE", "ADD", "REMOVE", "CURRENT", "RESET"
    ]
    targetIds: typing.List[int]
    resumeToken: str
    cause: Status
    readTime: str

class GoogleFirestoreAdminV1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: typing.List[GoogleFirestoreAdminV1Index]
    nextPageToken: str

class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class ListCollectionIdsResponse(typing_extensions.TypedDict, total=False):
    collectionIds: typing.List[str]
    nextPageToken: str

class ListenRequest(typing_extensions.TypedDict, total=False):
    addTarget: Target
    removeTarget: int
    labels: typing.Dict[str, typing.Any]

class BatchWriteRequest(typing_extensions.TypedDict, total=False):
    writes: typing.List[Write]
    labels: typing.Dict[str, typing.Any]

class CollectionSelector(typing_extensions.TypedDict, total=False):
    collectionId: str
    allDescendants: bool

class Target(typing.Dict[str, typing.Any]): ...
class StructuredQuery(typing.Dict[str, typing.Any]): ...

class GoogleFirestoreAdminV1IndexConfigDelta(typing_extensions.TypedDict, total=False):
    changeType: typing_extensions.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
    index: GoogleFirestoreAdminV1Index

class GoogleFirestoreAdminV1LocationMetadata(
    typing_extensions.TypedDict, total=False
): ...
class Cursor(typing.Dict[str, typing.Any]): ...
class WriteResult(typing.Dict[str, typing.Any]): ...

class RunQueryRequest(typing_extensions.TypedDict, total=False):
    readTime: str
    newTransaction: TransactionOptions
    transaction: str
    structuredQuery: StructuredQuery

class GoogleFirestoreAdminV1ExportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

class Document(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    fields: typing.Dict[str, typing.Any]

class BatchGetDocumentsResponse(typing_extensions.TypedDict, total=False):
    readTime: str
    missing: str
    transaction: str
    found: Document

class ListenResponse(typing_extensions.TypedDict, total=False):
    documentRemove: DocumentRemove
    targetChange: TargetChange
    filter: ExistenceFilter
    documentDelete: DocumentDelete
    documentChange: DocumentChange

class ReadWrite(typing_extensions.TypedDict, total=False):
    retryTransaction: str

class Order(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    field: FieldReference

class ListCollectionIdsRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
