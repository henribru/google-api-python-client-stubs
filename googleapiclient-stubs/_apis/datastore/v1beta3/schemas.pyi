import typing

import typing_extensions

class GoogleDatastoreAdminV1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: typing.List[str]
    namespaceIds: typing.List[str]

class CompositeFilter(typing_extensions.TypedDict, total=False):
    filters: typing.List[Filter]
    op: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "AND"]

class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    progressEntities: GoogleDatastoreAdminV1beta1Progress
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    inputUrl: str

class ReadOptions(typing_extensions.TypedDict, total=False):
    readConsistency: typing_extensions.Literal[
        "READ_CONSISTENCY_UNSPECIFIED", "STRONG", "EVENTUAL"
    ]
    transaction: str

class ReserveIdsResponse(typing_extensions.TypedDict, total=False): ...

class EntityResult(typing_extensions.TypedDict, total=False):
    cursor: str
    version: str
    entity: Entity

class CommitRequest(typing_extensions.TypedDict, total=False):
    transaction: str
    mutations: typing.List[Mutation]
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "TRANSACTIONAL", "NON_TRANSACTIONAL"
    ]

class KindExpression(typing_extensions.TypedDict, total=False):
    name: str

class PartitionId(typing_extensions.TypedDict, total=False):
    namespaceId: str
    projectId: str

class TransactionOptions(typing_extensions.TypedDict, total=False):
    readWrite: ReadWrite
    readOnly: ReadOnly

class RunQueryRequest(typing_extensions.TypedDict, total=False):
    partitionId: PartitionId
    query: Query
    gqlQuery: GqlQuery
    readOptions: ReadOptions

class Value(typing_extensions.TypedDict, total=False):
    nullValue: typing_extensions.Literal["NULL_VALUE"]
    arrayValue: ArrayValue
    geoPointValue: LatLng
    timestampValue: str
    excludeFromIndexes: bool
    blobValue: str
    integerValue: str
    entityValue: Entity
    booleanValue: bool
    stringValue: str
    doubleValue: float
    meaning: int
    keyValue: Key

class GoogleDatastoreAdminV1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    progressEntities: GoogleDatastoreAdminV1Progress
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1Progress
    common: GoogleDatastoreAdminV1CommonMetadata

class Mutation(typing_extensions.TypedDict, total=False):
    upsert: Entity
    update: Entity
    baseVersion: str
    delete: Key
    insert: Entity

class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    transactionOptions: TransactionOptions

class LookupRequest(typing_extensions.TypedDict, total=False):
    readOptions: ReadOptions
    keys: typing.List[Key]

class Filter(typing.Dict[str, typing.Any]): ...
class ReadOnly(typing_extensions.TypedDict, total=False): ...

class ReadWrite(typing_extensions.TypedDict, total=False):
    previousTransaction: str

class ArrayValue(typing.Dict[str, typing.Any]): ...

class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    outputUrlPrefix: str
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

class PathElement(typing_extensions.TypedDict, total=False):
    kind: str
    id: str
    name: str

class GoogleDatastoreAdminV1beta1EntityFilter(typing_extensions.TypedDict, total=False):
    namespaceIds: typing.List[str]
    kinds: typing.List[str]

class GoogleDatastoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    indexId: str
    progressEntities: GoogleDatastoreAdminV1Progress

class ReserveIdsRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]
    databaseId: str

class Entity(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]
    key: Key

class GoogleDatastoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

class RollbackResponse(typing_extensions.TypedDict, total=False): ...

class GoogleDatastoreAdminV1CommonMetadata(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]
    labels: typing.Dict[str, typing.Any]
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

class QueryResultBatch(typing_extensions.TypedDict, total=False):
    entityResults: typing.List[EntityResult]
    skippedResults: int
    moreResults: typing_extensions.Literal[
        "MORE_RESULTS_TYPE_UNSPECIFIED",
        "NOT_FINISHED",
        "MORE_RESULTS_AFTER_LIMIT",
        "MORE_RESULTS_AFTER_CURSOR",
        "NO_MORE_RESULTS",
    ]
    skippedCursor: str
    snapshotVersion: str
    endCursor: str
    entityResultType: typing_extensions.Literal[
        "RESULT_TYPE_UNSPECIFIED", "FULL", "PROJECTION", "KEY_ONLY"
    ]

class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

class AllocateIdsRequest(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]

class AllocateIdsResponse(typing_extensions.TypedDict, total=False):
    keys: typing.List[Key]

class RunQueryResponse(typing_extensions.TypedDict, total=False):
    batch: QueryResultBatch
    query: Query

class GoogleDatastoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

class PropertyReference(typing_extensions.TypedDict, total=False):
    name: str

class GoogleDatastoreAdminV1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

class RollbackRequest(typing_extensions.TypedDict, total=False):
    transaction: str

class LookupResponse(typing_extensions.TypedDict, total=False):
    found: typing.List[EntityResult]
    missing: typing.List[EntityResult]
    deferred: typing.List[Key]

class Projection(typing_extensions.TypedDict, total=False):
    property: PropertyReference

class MutationResult(typing_extensions.TypedDict, total=False):
    key: Key
    conflictDetected: bool
    version: str

class GqlQueryParameter(typing_extensions.TypedDict, total=False):
    value: Value
    cursor: str

class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

class Key(typing_extensions.TypedDict, total=False):
    partitionId: PartitionId
    path: typing.List[PathElement]

class PropertyOrder(typing_extensions.TypedDict, total=False):
    property: PropertyReference
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"
    ]

class GoogleDatastoreAdminV1beta1CommonMetadata(
    typing_extensions.TypedDict, total=False
):
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
    endTime: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
    startTime: str
    labels: typing.Dict[str, typing.Any]

class Query(typing.Dict[str, typing.Any]): ...
class GqlQuery(typing.Dict[str, typing.Any]): ...
class PropertyFilter(typing.Dict[str, typing.Any]): ...

class BeginTransactionResponse(typing_extensions.TypedDict, total=False):
    transaction: str

class CommitResponse(typing_extensions.TypedDict, total=False):
    mutationResults: typing.List[MutationResult]
    indexUpdates: int

class GoogleDatastoreAdminV1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    progressBytes: GoogleDatastoreAdminV1Progress
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    common: GoogleDatastoreAdminV1CommonMetadata
    outputUrlPrefix: str
    progressEntities: GoogleDatastoreAdminV1Progress
