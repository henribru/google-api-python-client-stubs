import typing

import typing_extensions
@typing.type_check_only
class ArrayValue(typing_extensions.TypedDict, total=False):
    values: typing.List[Value]

@typing.type_check_only
class BatchGetDocumentsRequest(typing_extensions.TypedDict, total=False):
    documents: typing.List[str]
    mask: DocumentMask
    newTransaction: TransactionOptions
    readTime: str
    transaction: str

@typing.type_check_only
class BatchGetDocumentsResponse(typing_extensions.TypedDict, total=False):
    found: Document
    missing: str
    readTime: str
    transaction: str

@typing.type_check_only
class BatchWriteRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    writes: typing.List[Write]

@typing.type_check_only
class BatchWriteResponse(typing_extensions.TypedDict, total=False):
    status: typing.List[Status]
    writeResults: typing.List[WriteResult]

@typing.type_check_only
class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    options: TransactionOptions

@typing.type_check_only
class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class CollectionSelector(typing_extensions.TypedDict, total=False):
    allDescendants: bool
    collectionId: str

@typing.type_check_only
class CommitRequest(typing_extensions.TypedDict, total=False):
    transaction: str
    writes: typing.List[Write]

@typing.type_check_only
class CommitResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    writeResults: typing.List[WriteResult]

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: typing.List[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

@typing.type_check_only
class Cursor(typing_extensions.TypedDict, total=False):
    before: bool
    values: typing.List[Value]

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    createTime: str
    fields: typing.Dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class DocumentChange(typing_extensions.TypedDict, total=False):
    document: Document
    removedTargetIds: typing.List[int]
    targetIds: typing.List[int]

@typing.type_check_only
class DocumentDelete(typing_extensions.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: typing.List[int]

@typing.type_check_only
class DocumentMask(typing_extensions.TypedDict, total=False):
    fieldPaths: typing.List[str]

@typing.type_check_only
class DocumentRemove(typing_extensions.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: typing.List[int]

@typing.type_check_only
class DocumentTransform(typing_extensions.TypedDict, total=False):
    document: str
    fieldTransforms: typing.List[FieldTransform]

@typing.type_check_only
class DocumentsTarget(typing_extensions.TypedDict, total=False):
    documents: typing.List[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExistenceFilter(typing_extensions.TypedDict, total=False):
    count: int
    targetId: int

@typing.type_check_only
class FieldFilter(typing_extensions.TypedDict, total=False):
    field: FieldReference
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
    value: Value

@typing.type_check_only
class FieldReference(typing_extensions.TypedDict, total=False):
    fieldPath: str

@typing.type_check_only
class FieldTransform(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Filter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
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
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1Field(typing_extensions.TypedDict, total=False):
    indexConfig: GoogleFirestoreAdminV1IndexConfig
    name: str

@typing.type_check_only
class GoogleFirestoreAdminV1FieldOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    field: str
    indexConfigDeltas: typing.List[GoogleFirestoreAdminV1IndexConfigDelta]
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
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
class GoogleFirestoreAdminV1ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
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
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: typing.List[str]
    inputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1Index(typing_extensions.TypedDict, total=False):
    fields: typing.List[GoogleFirestoreAdminV1IndexField]
    name: str
    queryScope: typing_extensions.Literal[
        "QUERY_SCOPE_UNSPECIFIED", "COLLECTION", "COLLECTION_GROUP"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "NEEDS_REPAIR"
    ]

@typing.type_check_only
class GoogleFirestoreAdminV1IndexConfig(typing_extensions.TypedDict, total=False):
    ancestorField: str
    indexes: typing.List[GoogleFirestoreAdminV1Index]
    reverting: bool
    usesAncestorConfig: bool

@typing.type_check_only
class GoogleFirestoreAdminV1IndexConfigDelta(typing_extensions.TypedDict, total=False):
    changeType: typing_extensions.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
    index: GoogleFirestoreAdminV1Index

@typing.type_check_only
class GoogleFirestoreAdminV1IndexField(typing_extensions.TypedDict, total=False):
    arrayConfig: typing_extensions.Literal["ARRAY_CONFIG_UNSPECIFIED", "CONTAINS"]
    fieldPath: str
    order: typing_extensions.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class GoogleFirestoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    index: str
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
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
class GoogleFirestoreAdminV1ListFieldsResponse(
    typing_extensions.TypedDict, total=False
):
    fields: typing.List[GoogleFirestoreAdminV1Field]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: typing.List[GoogleFirestoreAdminV1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1LocationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirestoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    completedWork: str
    estimatedWork: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListCollectionIdsRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str

@typing.type_check_only
class ListCollectionIdsResponse(typing_extensions.TypedDict, total=False):
    collectionIds: typing.List[str]
    nextPageToken: str

@typing.type_check_only
class ListDocumentsResponse(typing_extensions.TypedDict, total=False):
    documents: typing.List[Document]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListenRequest(typing_extensions.TypedDict, total=False):
    addTarget: Target
    labels: typing.Dict[str, typing.Any]
    removeTarget: int

@typing.type_check_only
class ListenResponse(typing_extensions.TypedDict, total=False):
    documentChange: DocumentChange
    documentDelete: DocumentDelete
    documentRemove: DocumentRemove
    filter: ExistenceFilter
    targetChange: TargetChange

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class MapValue(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]

@typing.type_check_only
class Order(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    field: FieldReference

@typing.type_check_only
class PartitionQueryRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    partitionCount: str
    structuredQuery: StructuredQuery

@typing.type_check_only
class PartitionQueryResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partitions: typing.List[Cursor]

@typing.type_check_only
class Precondition(typing_extensions.TypedDict, total=False):
    exists: bool
    updateTime: str

@typing.type_check_only
class Projection(typing_extensions.TypedDict, total=False):
    fields: typing.List[FieldReference]

@typing.type_check_only
class QueryTarget(typing_extensions.TypedDict, total=False):
    parent: str
    structuredQuery: StructuredQuery

@typing.type_check_only
class ReadOnly(typing_extensions.TypedDict, total=False):
    readTime: str

@typing.type_check_only
class ReadWrite(typing_extensions.TypedDict, total=False):
    retryTransaction: str

@typing.type_check_only
class RollbackRequest(typing_extensions.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class RunQueryRequest(typing_extensions.TypedDict, total=False):
    newTransaction: TransactionOptions
    readTime: str
    structuredQuery: StructuredQuery
    transaction: str

@typing.type_check_only
class RunQueryResponse(typing_extensions.TypedDict, total=False):
    document: Document
    readTime: str
    skippedResults: int
    transaction: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructuredQuery(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Target(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TargetChange(typing_extensions.TypedDict, total=False):
    cause: Status
    readTime: str
    resumeToken: str
    targetChangeType: typing_extensions.Literal[
        "NO_CHANGE", "ADD", "REMOVE", "CURRENT", "RESET"
    ]
    targetIds: typing.List[int]

@typing.type_check_only
class TransactionOptions(typing_extensions.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class UnaryFilter(typing_extensions.TypedDict, total=False):
    field: FieldReference
    op: typing_extensions.Literal[
        "OPERATOR_UNSPECIFIED", "IS_NAN", "IS_NULL", "IS_NOT_NAN", "IS_NOT_NULL"
    ]

@typing.type_check_only
class Value(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Write(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class WriteRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    streamId: str
    streamToken: str
    writes: typing.List[Write]

@typing.type_check_only
class WriteResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    streamId: str
    streamToken: str
    writeResults: typing.List[WriteResult]

@typing.type_check_only
class WriteResult(typing.Dict[str, typing.Any]): ...
