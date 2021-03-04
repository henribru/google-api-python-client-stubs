import typing

import typing_extensions
@typing.type_check_only
class AllocateIdsRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]

@typing.type_check_only
class AllocateIdsResponse(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]

@typing.type_check_only
class ArrayValue(typing_extensions.TypedDict, total=False):
    values: typing.List[Value]

@typing.type_check_only
class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    transactionOptions: TransactionOptions

@typing.type_check_only
class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class CommitRequest(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "TRANSACTIONAL", "NON_TRANSACTIONAL"
    ]
    mutations: typing.List[Mutation]
    transaction: str

@typing.type_check_only
class CommitResponse(typing_extensions.TypedDict, total=False):
    indexUpdates: int
    mutationResults: typing.List[MutationResult]

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: typing.List[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    key: Key
    properties: typing.Dict[str, typing.Any]

@typing.type_check_only
class EntityResult(typing_extensions.TypedDict, total=False):
    cursor: str
    entity: Entity
    version: str

@typing.type_check_only
class Filter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleDatastoreAdminV1CommonMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    labels: typing.Dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]
    startTime: str
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

@typing.type_check_only
class GoogleDatastoreAdminV1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: typing.List[str]
    namespaceIds: typing.List[str]

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    indexId: str
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1CommonMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    labels: typing.Dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
    startTime: str
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

@typing.type_check_only
class GoogleDatastoreAdminV1beta1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: typing.List[str]
    namespaceIds: typing.List[str]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GqlQuery(typing_extensions.TypedDict, total=False):
    allowLiterals: bool
    namedBindings: typing.Dict[str, typing.Any]
    positionalBindings: typing.List[GqlQueryParameter]
    queryString: str

@typing.type_check_only
class GqlQueryParameter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Key(typing_extensions.TypedDict, total=False):
    partitionId: PartitionId
    path: typing.List[PathElement]

@typing.type_check_only
class KindExpression(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LookupRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]
    readOptions: ReadOptions

@typing.type_check_only
class LookupResponse(typing_extensions.TypedDict, total=False):
    deferred: typing.List[Key]
    found: typing.List[EntityResult]
    missing: typing.List[EntityResult]

@typing.type_check_only
class Mutation(typing_extensions.TypedDict, total=False):
    baseVersion: str
    delete: Key
    insert: Entity
    update: Entity
    upsert: Entity

@typing.type_check_only
class MutationResult(typing_extensions.TypedDict, total=False):
    conflictDetected: bool
    key: Key
    version: str

@typing.type_check_only
class PartitionId(typing_extensions.TypedDict, total=False):
    namespaceId: str
    projectId: str

@typing.type_check_only
class PathElement(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class Projection(typing_extensions.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class PropertyFilter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class PropertyOrder(typing_extensions.TypedDict, total=False):
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]
    property: PropertyReference

@typing.type_check_only
class PropertyReference(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    distinctOn: typing.List[PropertyReference]
    endCursor: str
    filter: Filter
    kind: typing.List[KindExpression]
    limit: int
    offset: int
    order: typing.List[PropertyOrder]
    projection: typing.List[Projection]
    startCursor: str

@typing.type_check_only
class QueryResultBatch(typing_extensions.TypedDict, total=False):
    endCursor: str
    entityResultType: typing_extensions.Literal[
        "RESULT_TYPE_UNSPECIFIED", "FULL", "PROJECTION", "KEY_ONLY"
    ]
    entityResults: typing.List[EntityResult]
    moreResults: typing_extensions.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    skippedCursor: str
    skippedResults: int
    snapshotVersion: str

@typing.type_check_only
class ReadOnly(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReadOptions(typing_extensions.TypedDict, total=False):
    readConsistency: typing_extensions.Literal[
        "READ_CONSISTENCY_UNSPECIFIED", "STRONG", "EVENTUAL"
    ]
    transaction: str

@typing.type_check_only
class ReadWrite(typing_extensions.TypedDict, total=False):
    previousTransaction: str

@typing.type_check_only
class ReserveIdsRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    keys: typing.List[Key]

@typing.type_check_only
class ReserveIdsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RollbackRequest(typing_extensions.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class RollbackResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RunQueryRequest(typing_extensions.TypedDict, total=False):
    gqlQuery: GqlQuery
    partitionId: PartitionId
    query: Query
    readOptions: ReadOptions

@typing.type_check_only
class RunQueryResponse(typing_extensions.TypedDict, total=False):
    batch: QueryResultBatch
    query: Query

@typing.type_check_only
class TransactionOptions(typing_extensions.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class Value(typing.Dict[str, typing.Any]): ...
