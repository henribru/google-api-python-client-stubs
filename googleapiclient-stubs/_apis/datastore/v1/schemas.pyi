import typing

import typing_extensions

class GoogleDatastoreAdminV1beta1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: typing.List[str]
    namespaceIds: typing.List[str]

class ArrayValue(typing_extensions.TypedDict, total=False):
    values: typing.List[Value]

class GqlQueryParameter(typing_extensions.TypedDict, total=False):
    value: Value
    cursor: str

class GoogleDatastoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    progressEntities: GoogleDatastoreAdminV1Progress
    indexId: str

class PropertyReference(typing_extensions.TypedDict, total=False):
    name: str

class EntityResult(typing_extensions.TypedDict, total=False):
    version: str
    entity: Entity
    cursor: str

class Empty(typing_extensions.TypedDict, total=False): ...

class PathElement(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    id: str

class Value(typing.Dict[str, typing.Any]): ...

class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

class GoogleDatastoreAdminV1CommonMetadata(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]
    startTime: str
    endTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    labels: typing.Dict[str, typing.Any]

class LookupResponse(typing_extensions.TypedDict, total=False):
    found: typing.List[EntityResult]
    missing: typing.List[EntityResult]
    deferred: typing.List[Key]

class RunQueryResponse(typing_extensions.TypedDict, total=False):
    query: Query
    batch: QueryResultBatch

class AllocateIdsRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]

class GoogleDatastoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workEstimated: str
    workCompleted: str

class Entity(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]
    key: Key

class GoogleDatastoreAdminV1ImportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    inputUrl: str
    labels: typing.Dict[str, typing.Any]
    entityFilter: GoogleDatastoreAdminV1EntityFilter

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    error: Status
    done: bool
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: typing.List[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

class Mutation(typing_extensions.TypedDict, total=False):
    upsert: Entity
    update: Entity
    insert: Entity
    delete: Key
    baseVersion: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress
    common: GoogleDatastoreAdminV1beta1CommonMetadata

class PropertyOrder(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    property: PropertyReference

class AllocateIdsResponse(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]

class RollbackResponse(typing_extensions.TypedDict, total=False): ...

class QueryResultBatch(typing_extensions.TypedDict, total=False):
    snapshotVersion: str
    endCursor: str
    skippedCursor: str
    skippedResults: int
    moreResults: typing_extensions.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    entityResults: typing.List[EntityResult]
    entityResultType: typing_extensions.Literal[
        "RESULT_TYPE_UNSPECIFIED", "FULL", "PROJECTION", "KEY_ONLY"
    ]

class CommitResponse(typing_extensions.TypedDict, total=False):
    indexUpdates: int
    mutationResults: typing.List[MutationResult]

class GoogleDatastoreAdminV1ExportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    outputUrlPrefix: str
    labels: typing.Dict[str, typing.Any]
    entityFilter: GoogleDatastoreAdminV1EntityFilter

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class GoogleDatastoreAdminV1beta1CommonMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]
    labels: typing.Dict[str, typing.Any]
    endTime: str

class PartitionId(typing_extensions.TypedDict, total=False):
    projectId: str
    namespaceId: str

class GoogleDatastoreAdminV1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    progressBytes: GoogleDatastoreAdminV1Progress
    inputUrl: str
    progressEntities: GoogleDatastoreAdminV1Progress
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter

class Key(typing_extensions.TypedDict, total=False):
    path: typing.List[PathElement]
    partitionId: PartitionId

class LookupRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]
    readOptions: ReadOptions

class ReserveIdsRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]
    databaseId: str

class TransactionOptions(typing_extensions.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite

class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

class RunQueryRequest(typing_extensions.TypedDict, total=False):
    partitionId: PartitionId
    readOptions: ReadOptions
    gqlQuery: GqlQuery
    query: Query

class GoogleDatastoreAdminV1ListIndexesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    indexes: typing.List[GoogleDatastoreAdminV1Index]

class GoogleDatastoreAdminV1IndexedProperty(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    name: str

class ReadOptions(typing_extensions.TypedDict, total=False):
    readConsistency: typing_extensions.Literal[
        "READ_CONSISTENCY_UNSPECIFIED", "STRONG", "EVENTUAL"
    ]
    transaction: str

class Filter(typing.Dict[str, typing.Any]): ...

class GoogleDatastoreAdminV1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    progressBytes: GoogleDatastoreAdminV1Progress
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    common: GoogleDatastoreAdminV1CommonMetadata
    progressEntities: GoogleDatastoreAdminV1Progress
    outputUrlPrefix: str

class CommitRequest(typing_extensions.TypedDict, total=False):
    transaction: str
    mutations: typing.List[Mutation]
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "TRANSACTIONAL", "NON_TRANSACTIONAL"
    ]

class GoogleDatastoreAdminV1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: typing.List[str]
    namespaceIds: typing.List[str]

class Projection(typing_extensions.TypedDict, total=False):
    property: PropertyReference

class GoogleDatastoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    workEstimated: str
    workCompleted: str

class MutationResult(typing_extensions.TypedDict, total=False):
    key: Key
    conflictDetected: bool
    version: str

class GqlQuery(typing.Dict[str, typing.Any]): ...
class ReadOnly(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class Query(typing.Dict[str, typing.Any]): ...

class GoogleDatastoreAdminV1Index(typing_extensions.TypedDict, total=False):
    kind: str
    properties: typing.List[GoogleDatastoreAdminV1IndexedProperty]
    ancestor: typing_extensions.Literal[
        "ANCESTOR_MODE_UNSPECIFIED", "NONE", "ALL_ANCESTORS"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "ERROR"
    ]
    indexId: str
    projectId: str

class GoogleDatastoreAdminV1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

class KindExpression(typing_extensions.TypedDict, total=False):
    name: str

class ReserveIdsResponse(typing_extensions.TypedDict, total=False): ...

class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    transactionOptions: TransactionOptions

class ReadWrite(typing_extensions.TypedDict, total=False):
    previousTransaction: str

class PropertyFilter(typing.Dict[str, typing.Any]): ...

class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    progressEntities: GoogleDatastoreAdminV1beta1Progress
    inputUrl: str

class RollbackRequest(typing_extensions.TypedDict, total=False):
    transaction: str
