import typing

_list = list

@typing.type_check_only
class Aggregation(typing.TypedDict, total=False):
    alias: str
    avg: Avg
    count: Count
    sum: Sum

@typing.type_check_only
class AggregationQuery(typing.TypedDict, total=False):
    aggregations: _list[Aggregation]
    nestedQuery: Query

@typing.type_check_only
class AggregationResult(typing.TypedDict, total=False):
    aggregateProperties: dict[str, typing.Any]

@typing.type_check_only
class AggregationResultBatch(typing.TypedDict, total=False):
    aggregationResults: _list[AggregationResult]
    moreResults: typing.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    readTime: str

@typing.type_check_only
class AllocateIdsRequest(typing.TypedDict, total=False):
    keys: _list[Key]

@typing.type_check_only
class AllocateIdsResponse(typing.TypedDict, total=False):
    keys: _list[Key]

@typing.type_check_only
class ArrayValue(typing.TypedDict, total=False):
    values: _list[Value]

@typing.type_check_only
class Avg(typing.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class BeginTransactionRequest(typing.TypedDict, total=False):
    transactionOptions: TransactionOptions

@typing.type_check_only
class BeginTransactionResponse(typing.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class CommitRequest(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "TRANSACTIONAL", "NON_TRANSACTIONAL"]
    mutations: _list[Mutation]
    transaction: str

@typing.type_check_only
class CommitResponse(typing.TypedDict, total=False):
    commitTime: str
    indexUpdates: int
    mutationResults: _list[MutationResult]

@typing.type_check_only
class CompositeFilter(typing.TypedDict, total=False):
    filters: _list[Filter]
    op: typing.Literal["OPERATOR_UNSPECIFIED", "AND", "OR"]

@typing.type_check_only
class Count(typing.TypedDict, total=False):
    upTo: str

@typing.type_check_only
class Entity(typing.TypedDict, total=False):
    key: Key
    properties: dict[str, typing.Any]

@typing.type_check_only
class EntityResult(typing.TypedDict, total=False):
    createTime: str
    cursor: str
    entity: Entity
    updateTime: str
    version: str

@typing.type_check_only
class ExecutionStats(typing.TypedDict, total=False):
    debugStats: dict[str, typing.Any]
    executionDuration: str
    readOperations: str
    resultsReturned: str

@typing.type_check_only
class ExplainMetrics(typing.TypedDict, total=False):
    executionStats: ExecutionStats
    planSummary: PlanSummary

@typing.type_check_only
class ExplainOptions(typing.TypedDict, total=False):
    analyze: bool

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    compositeFilter: CompositeFilter
    propertyFilter: PropertyFilter

@typing.type_check_only
class FindNearest(typing.TypedDict, total=False):
    distanceMeasure: typing.Literal[
        "DISTANCE_MEASURE_UNSPECIFIED", "EUCLIDEAN", "COSINE", "DOT_PRODUCT"
    ]
    distanceResultProperty: str
    distanceThreshold: float
    limit: int
    queryVector: Value
    vectorProperty: PropertyReference

@typing.type_check_only
class GoogleDatastoreAdminV1CommonMetadata(typing.TypedDict, total=False):
    endTime: str
    labels: dict[str, typing.Any]
    operationType: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]
    startTime: str
    state: typing.Literal[
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
class GoogleDatastoreAdminV1DatastoreFirestoreMigrationMetadata(
    typing.TypedDict, total=False
):
    migrationState: typing.Literal[
        "MIGRATION_STATE_UNSPECIFIED", "RUNNING", "PAUSED", "COMPLETE"
    ]
    migrationStep: typing.Literal[
        "MIGRATION_STEP_UNSPECIFIED",
        "PREPARE",
        "START",
        "APPLY_WRITES_SYNCHRONOUSLY",
        "COPY_AND_VERIFY",
        "REDIRECT_EVENTUALLY_CONSISTENT_READS",
        "REDIRECT_STRONGLY_CONSISTENT_READS",
        "REDIRECT_WRITES",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1EntityFilter(typing.TypedDict, total=False):
    kinds: _list[str]
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesMetadata(typing.TypedDict, total=False):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesResponse(typing.TypedDict, total=False):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1ImportEntitiesMetadata(typing.TypedDict, total=False):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1IndexOperationMetadata(typing.TypedDict, total=False):
    common: GoogleDatastoreAdminV1CommonMetadata
    indexId: str
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1MigrationProgressEvent(typing.TypedDict, total=False):
    prepareStepDetails: GoogleDatastoreAdminV1PrepareStepDetails
    redirectWritesStepDetails: GoogleDatastoreAdminV1RedirectWritesStepDetails
    step: typing.Literal[
        "MIGRATION_STEP_UNSPECIFIED",
        "PREPARE",
        "START",
        "APPLY_WRITES_SYNCHRONOUSLY",
        "COPY_AND_VERIFY",
        "REDIRECT_EVENTUALLY_CONSISTENT_READS",
        "REDIRECT_STRONGLY_CONSISTENT_READS",
        "REDIRECT_WRITES",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1MigrationStateEvent(typing.TypedDict, total=False):
    state: typing.Literal[
        "MIGRATION_STATE_UNSPECIFIED", "RUNNING", "PAUSED", "COMPLETE"
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1PrepareStepDetails(typing.TypedDict, total=False):
    concurrencyMode: typing.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED",
        "PESSIMISTIC",
        "OPTIMISTIC",
        "OPTIMISTIC_WITH_ENTITY_GROUPS",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1Progress(typing.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GoogleDatastoreAdminV1RedirectWritesStepDetails(typing.TypedDict, total=False):
    concurrencyMode: typing.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED",
        "PESSIMISTIC",
        "OPTIMISTIC",
        "OPTIMISTIC_WITH_ENTITY_GROUPS",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1CommonMetadata(typing.TypedDict, total=False):
    endTime: str
    labels: dict[str, typing.Any]
    operationType: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
    startTime: str
    state: typing.Literal[
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
class GoogleDatastoreAdminV1beta1EntityFilter(typing.TypedDict, total=False):
    kinds: _list[str]
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(typing.TypedDict, total=False):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(typing.TypedDict, total=False):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(typing.TypedDict, total=False):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1Progress(typing.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GqlQuery(typing.TypedDict, total=False):
    allowLiterals: bool
    namedBindings: dict[str, typing.Any]
    positionalBindings: _list[GqlQueryParameter]
    queryString: str

@typing.type_check_only
class GqlQueryParameter(typing.TypedDict, total=False):
    cursor: str
    value: Value

@typing.type_check_only
class Key(typing.TypedDict, total=False):
    partitionId: PartitionId
    path: _list[PathElement]

@typing.type_check_only
class KindExpression(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LookupRequest(typing.TypedDict, total=False):
    keys: _list[Key]
    propertyMask: PropertyMask
    readOptions: ReadOptions

@typing.type_check_only
class LookupResponse(typing.TypedDict, total=False):
    deferred: _list[Key]
    found: _list[EntityResult]
    missing: _list[EntityResult]
    readTime: str

@typing.type_check_only
class Mutation(typing.TypedDict, total=False):
    baseVersion: str
    conflictResolutionStrategy: typing.Literal[
        "STRATEGY_UNSPECIFIED", "SERVER_VALUE", "FAIL"
    ]
    delete: Key
    insert: Entity
    propertyMask: PropertyMask
    propertyTransforms: _list[PropertyTransform]
    update: Entity
    updateTime: str
    upsert: Entity

@typing.type_check_only
class MutationResult(typing.TypedDict, total=False):
    conflictDetected: bool
    createTime: str
    key: Key
    transformResults: _list[Value]
    updateTime: str
    version: str

@typing.type_check_only
class PartitionId(typing.TypedDict, total=False):
    namespaceId: str
    projectId: str

@typing.type_check_only
class PathElement(typing.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class PlanSummary(typing.TypedDict, total=False):
    indexesUsed: _list[dict[str, typing.Any]]

@typing.type_check_only
class Projection(typing.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class PropertyFilter(typing.TypedDict, total=False):
    op: typing.Literal[
        "OPERATOR_UNSPECIFIED",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "EQUAL",
        "IN",
        "NOT_EQUAL",
        "HAS_ANCESTOR",
        "NOT_IN",
    ]
    property: PropertyReference
    value: Value

@typing.type_check_only
class PropertyMask(typing.TypedDict, total=False):
    paths: _list[str]

@typing.type_check_only
class PropertyOrder(typing.TypedDict, total=False):
    direction: typing.Literal["DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    property: PropertyReference

@typing.type_check_only
class PropertyReference(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class PropertyTransform(typing.TypedDict, total=False):
    appendMissingElements: ArrayValue
    increment: Value
    maximum: Value
    minimum: Value
    property: str
    removeAllFromArray: ArrayValue
    setToServerValue: typing.Literal["SERVER_VALUE_UNSPECIFIED", "REQUEST_TIME"]

@typing.type_check_only
class Query(typing.TypedDict, total=False):
    distinctOn: _list[PropertyReference]
    endCursor: str
    filter: Filter
    findNearest: FindNearest
    kind: _list[KindExpression]
    limit: int
    offset: int
    order: _list[PropertyOrder]
    projection: _list[Projection]
    startCursor: str

@typing.type_check_only
class QueryResultBatch(typing.TypedDict, total=False):
    endCursor: str
    entityResultType: typing.Literal[
        "RESULT_TYPE_UNSPECIFIED", "FULL", "PROJECTION", "KEY_ONLY"
    ]
    entityResults: _list[EntityResult]
    moreResults: typing.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    readTime: str
    skippedCursor: str
    skippedResults: int
    snapshotVersion: str

@typing.type_check_only
class ReadOnly(typing.TypedDict, total=False):
    readTime: str

@typing.type_check_only
class ReadOptions(typing.TypedDict, total=False):
    readConsistency: typing.Literal[
        "READ_CONSISTENCY_UNSPECIFIED", "STRONG", "EVENTUAL"
    ]
    readTime: str
    transaction: str

@typing.type_check_only
class ReadWrite(typing.TypedDict, total=False):
    previousTransaction: str

@typing.type_check_only
class ReserveIdsRequest(typing.TypedDict, total=False):
    databaseId: str
    keys: _list[Key]

@typing.type_check_only
class ReserveIdsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RollbackRequest(typing.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class RollbackResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RunAggregationQueryRequest(typing.TypedDict, total=False):
    aggregationQuery: AggregationQuery
    explainOptions: ExplainOptions
    gqlQuery: GqlQuery
    partitionId: PartitionId
    readOptions: ReadOptions

@typing.type_check_only
class RunAggregationQueryResponse(typing.TypedDict, total=False):
    batch: AggregationResultBatch
    explainMetrics: ExplainMetrics
    query: AggregationQuery

@typing.type_check_only
class RunQueryRequest(typing.TypedDict, total=False):
    explainOptions: ExplainOptions
    gqlQuery: GqlQuery
    partitionId: PartitionId
    propertyMask: PropertyMask
    query: Query
    readOptions: ReadOptions

@typing.type_check_only
class RunQueryResponse(typing.TypedDict, total=False):
    batch: QueryResultBatch
    explainMetrics: ExplainMetrics
    query: Query

@typing.type_check_only
class Sum(typing.TypedDict, total=False):
    property: PropertyReference

@typing.type_check_only
class TransactionOptions(typing.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class Value(typing.TypedDict, total=False):
    arrayValue: ArrayValue
    blobValue: str
    booleanValue: bool
    doubleValue: float
    entityValue: Entity
    excludeFromIndexes: bool
    geoPointValue: LatLng
    integerValue: str
    keyValue: Key
    meaning: int
    nullValue: typing.Literal["NULL_VALUE"]
    stringValue: str
    timestampValue: str
