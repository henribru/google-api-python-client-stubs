import typing

import typing_extensions

_list = list

@typing.type_check_only
class Aggregation(typing_extensions.TypedDict, total=False):
    alias: str
    count: Count

@typing.type_check_only
class AggregationResult(typing_extensions.TypedDict, total=False):
    aggregateFields: dict[str, typing.Any]

@typing.type_check_only
class ArrayValue(typing_extensions.TypedDict, total=False):
    values: _list[Value]

@typing.type_check_only
class BatchGetDocumentsRequest(typing_extensions.TypedDict, total=False):
    documents: _list[str]
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
    labels: dict[str, typing.Any]
    writes: _list[Write]

@typing.type_check_only
class BatchWriteResponse(typing_extensions.TypedDict, total=False):
    status: _list[Status]
    writeResults: _list[WriteResult]

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
    writes: _list[Write]

@typing.type_check_only
class CommitResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    writeResults: _list[WriteResult]

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: _list[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

@typing.type_check_only
class Count(typing_extensions.TypedDict, total=False):
    upTo: str

@typing.type_check_only
class Cursor(typing_extensions.TypedDict, total=False):
    before: bool
    values: _list[Value]

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    createTime: str
    fields: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class DocumentChange(typing_extensions.TypedDict, total=False):
    document: Document
    removedTargetIds: _list[int]
    targetIds: _list[int]

@typing.type_check_only
class DocumentDelete(typing_extensions.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: _list[int]

@typing.type_check_only
class DocumentMask(typing_extensions.TypedDict, total=False):
    fieldPaths: _list[str]

@typing.type_check_only
class DocumentRemove(typing_extensions.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: _list[int]

@typing.type_check_only
class DocumentTransform(typing_extensions.TypedDict, total=False):
    document: str
    fieldTransforms: _list[FieldTransform]

@typing.type_check_only
class DocumentsTarget(typing_extensions.TypedDict, total=False):
    documents: _list[str]

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
class FieldTransform(dict[str, typing.Any]): ...

@typing.type_check_only
class Filter(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleFirestoreAdminV1Database(typing_extensions.TypedDict, total=False):
    appEngineIntegrationMode: typing_extensions.Literal[
        "APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    concurrencyMode: typing_extensions.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED",
        "OPTIMISTIC",
        "PESSIMISTIC",
        "OPTIMISTIC_WITH_ENTITY_GROUPS",
    ]
    etag: str
    keyPrefix: str
    locationId: str
    name: str
    type: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED", "FIRESTORE_NATIVE", "DATASTORE_MODE"
    ]

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsMetadata(
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
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: _list[str]
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
    ttlConfig: GoogleFirestoreAdminV1TtlConfig

@typing.type_check_only
class GoogleFirestoreAdminV1FieldOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    field: str
    indexConfigDeltas: _list[GoogleFirestoreAdminV1IndexConfigDelta]
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
    ttlConfigDelta: GoogleFirestoreAdminV1TtlConfigDelta

@typing.type_check_only
class GoogleFirestoreAdminV1ImportDocumentsMetadata(
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
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    collectionIds: _list[str]
    inputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1Index(typing_extensions.TypedDict, total=False):
    fields: _list[GoogleFirestoreAdminV1IndexField]
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
    indexes: _list[GoogleFirestoreAdminV1Index]
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
class GoogleFirestoreAdminV1ListDatabasesResponse(
    typing_extensions.TypedDict, total=False
):
    databases: _list[GoogleFirestoreAdminV1Database]

@typing.type_check_only
class GoogleFirestoreAdminV1ListFieldsResponse(
    typing_extensions.TypedDict, total=False
):
    fields: _list[GoogleFirestoreAdminV1Field]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    indexes: _list[GoogleFirestoreAdminV1Index]
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
class GoogleFirestoreAdminV1TtlConfig(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "NEEDS_REPAIR"
    ]

@typing.type_check_only
class GoogleFirestoreAdminV1TtlConfigDelta(typing_extensions.TypedDict, total=False):
    changeType: typing_extensions.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]

@typing.type_check_only
class GoogleFirestoreAdminV1UpdateDatabaseMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListCollectionIdsRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    readTime: str

@typing.type_check_only
class ListCollectionIdsResponse(typing_extensions.TypedDict, total=False):
    collectionIds: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListDocumentsResponse(typing_extensions.TypedDict, total=False):
    documents: _list[Document]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListenRequest(typing_extensions.TypedDict, total=False):
    addTarget: Target
    labels: dict[str, typing.Any]
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
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MapValue(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]

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
    readTime: str
    structuredQuery: StructuredQuery

@typing.type_check_only
class PartitionQueryResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partitions: _list[Cursor]

@typing.type_check_only
class Precondition(typing_extensions.TypedDict, total=False):
    exists: bool
    updateTime: str

@typing.type_check_only
class Projection(typing_extensions.TypedDict, total=False):
    fields: _list[FieldReference]

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
class RunAggregationQueryRequest(typing_extensions.TypedDict, total=False):
    newTransaction: TransactionOptions
    readTime: str
    structuredAggregationQuery: StructuredAggregationQuery
    transaction: str

@typing.type_check_only
class RunAggregationQueryResponse(typing_extensions.TypedDict, total=False):
    readTime: str
    result: AggregationResult
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
    done: bool
    readTime: str
    skippedResults: int
    transaction: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructuredAggregationQuery(dict[str, typing.Any]): ...

@typing.type_check_only
class StructuredQuery(dict[str, typing.Any]): ...

@typing.type_check_only
class Target(dict[str, typing.Any]): ...

@typing.type_check_only
class TargetChange(typing_extensions.TypedDict, total=False):
    cause: Status
    readTime: str
    resumeToken: str
    targetChangeType: typing_extensions.Literal[
        "NO_CHANGE", "ADD", "REMOVE", "CURRENT", "RESET"
    ]
    targetIds: _list[int]

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
class Value(dict[str, typing.Any]): ...

@typing.type_check_only
class Write(dict[str, typing.Any]): ...

@typing.type_check_only
class WriteRequest(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    streamId: str
    streamToken: str
    writes: _list[Write]

@typing.type_check_only
class WriteResponse(typing_extensions.TypedDict, total=False):
    commitTime: str
    streamId: str
    streamToken: str
    writeResults: _list[WriteResult]

@typing.type_check_only
class WriteResult(dict[str, typing.Any]): ...
