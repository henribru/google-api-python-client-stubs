import typing

_list = list

@typing.type_check_only
class Aggregation(typing.TypedDict, total=False):
    alias: str
    avg: Avg
    count: Count
    sum: Sum

@typing.type_check_only
class AggregationResult(typing.TypedDict, total=False):
    aggregateFields: dict[str, typing.Any]

@typing.type_check_only
class ArrayValue(typing.TypedDict, total=False):
    values: _list[Value]

@typing.type_check_only
class Avg(typing.TypedDict, total=False):
    field: FieldReference

@typing.type_check_only
class BatchGetDocumentsRequest(typing.TypedDict, total=False):
    documents: _list[str]
    mask: DocumentMask
    newTransaction: TransactionOptions
    readTime: str
    transaction: str

@typing.type_check_only
class BatchGetDocumentsResponse(typing.TypedDict, total=False):
    found: Document
    missing: str
    readTime: str
    transaction: str

@typing.type_check_only
class BatchWriteRequest(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    writes: _list[Write]

@typing.type_check_only
class BatchWriteResponse(typing.TypedDict, total=False):
    status: _list[Status]
    writeResults: _list[WriteResult]

@typing.type_check_only
class BeginTransactionRequest(typing.TypedDict, total=False):
    options: TransactionOptions

@typing.type_check_only
class BeginTransactionResponse(typing.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class BitSequence(typing.TypedDict, total=False):
    bitmap: str
    padding: int

@typing.type_check_only
class BloomFilter(typing.TypedDict, total=False):
    bits: BitSequence
    hashCount: int

@typing.type_check_only
class CollectionSelector(typing.TypedDict, total=False):
    allDescendants: bool
    collectionId: str

@typing.type_check_only
class CommitRequest(typing.TypedDict, total=False):
    transaction: str
    writes: _list[Write]

@typing.type_check_only
class CommitResponse(typing.TypedDict, total=False):
    commitTime: str
    writeResults: _list[WriteResult]

@typing.type_check_only
class CompositeFilter(typing.TypedDict, total=False):
    filters: _list[Filter]
    op: typing.Literal["OPERATOR_UNSPECIFIED", "AND", "OR"]

@typing.type_check_only
class Count(typing.TypedDict, total=False):
    upTo: str

@typing.type_check_only
class Cursor(typing.TypedDict, total=False):
    before: bool
    values: _list[Value]

@typing.type_check_only
class Document(typing.TypedDict, total=False):
    createTime: str
    fields: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class DocumentChange(typing.TypedDict, total=False):
    document: Document
    removedTargetIds: _list[int]
    targetIds: _list[int]

@typing.type_check_only
class DocumentDelete(typing.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: _list[int]

@typing.type_check_only
class DocumentMask(typing.TypedDict, total=False):
    fieldPaths: _list[str]

@typing.type_check_only
class DocumentRemove(typing.TypedDict, total=False):
    document: str
    readTime: str
    removedTargetIds: _list[int]

@typing.type_check_only
class DocumentTransform(typing.TypedDict, total=False):
    document: str
    fieldTransforms: _list[FieldTransform]

@typing.type_check_only
class DocumentsTarget(typing.TypedDict, total=False):
    documents: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExecutePipelineRequest(typing.TypedDict, total=False):
    autoCommitTransaction: bool
    newTransaction: TransactionOptions
    readTime: str
    structuredPipeline: StructuredPipeline
    transaction: str

@typing.type_check_only
class ExecutePipelineResponse(typing.TypedDict, total=False):
    executionTime: str
    explainStats: ExplainStats
    results: _list[Document]
    transaction: str

@typing.type_check_only
class ExecutionStats(typing.TypedDict, total=False):
    debugStats: dict[str, typing.Any]
    executionDuration: str
    readOperations: str
    resultsReturned: str

@typing.type_check_only
class ExistenceFilter(typing.TypedDict, total=False):
    count: int
    targetId: int
    unchangedNames: BloomFilter

@typing.type_check_only
class ExplainMetrics(typing.TypedDict, total=False):
    executionStats: ExecutionStats
    planSummary: PlanSummary

@typing.type_check_only
class ExplainOptions(typing.TypedDict, total=False):
    analyze: bool

@typing.type_check_only
class ExplainStats(typing.TypedDict, total=False):
    data: dict[str, typing.Any]

@typing.type_check_only
class FieldFilter(typing.TypedDict, total=False):
    field: FieldReference
    op: typing.Literal[
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
class FieldReference(typing.TypedDict, total=False):
    fieldPath: str

@typing.type_check_only
class FieldTransform(typing.TypedDict, total=False):
    appendMissingElements: ArrayValue
    fieldPath: str
    increment: Value
    maximum: Value
    minimum: Value
    removeAllFromArray: ArrayValue
    setToServerValue: typing.Literal["SERVER_VALUE_UNSPECIFIED", "REQUEST_TIME"]

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    compositeFilter: CompositeFilter
    fieldFilter: FieldFilter
    unaryFilter: UnaryFilter

@typing.type_check_only
class FindNearest(typing.TypedDict, total=False):
    distanceMeasure: typing.Literal[
        "DISTANCE_MEASURE_UNSPECIFIED", "EUCLIDEAN", "COSINE", "DOT_PRODUCT"
    ]
    distanceResultField: str
    distanceThreshold: float
    limit: int
    queryVector: Value
    vectorField: FieldReference

@typing.type_check_only
class Function(typing.TypedDict, total=False):
    args: _list[Value]
    name: str
    options: dict[str, typing.Any]

@typing.type_check_only
class GoogleFirestoreAdminV1Backup(typing.TypedDict, total=False):
    database: str
    databaseUid: str
    expireTime: str
    name: str
    snapshotTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY", "NOT_AVAILABLE"]
    stats: GoogleFirestoreAdminV1Stats

@typing.type_check_only
class GoogleFirestoreAdminV1BackupSchedule(typing.TypedDict, total=False):
    createTime: str
    dailyRecurrence: GoogleFirestoreAdminV1DailyRecurrence
    name: str
    retention: str
    updateTime: str
    weeklyRecurrence: GoogleFirestoreAdminV1WeeklyRecurrence

@typing.type_check_only
class GoogleFirestoreAdminV1BackupSource(typing.TypedDict, total=False):
    backup: str

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
class GoogleFirestoreAdminV1BulkDeleteDocumentsRequest(typing.TypedDict, total=False):
    collectionIds: _list[str]
    namespaceIds: _list[str]

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
class GoogleFirestoreAdminV1CloneDatabaseRequest(typing.TypedDict, total=False):
    databaseId: str
    encryptionConfig: GoogleFirestoreAdminV1EncryptionConfig
    pitrSnapshot: GoogleFirestoreAdminV1PitrSnapshot
    tags: dict[str, typing.Any]

@typing.type_check_only
class GoogleFirestoreAdminV1CmekConfig(typing.TypedDict, total=False):
    activeKeyVersion: _list[str]
    kmsKeyName: str

@typing.type_check_only
class GoogleFirestoreAdminV1CreateDatabaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1CustomerManagedEncryptionOptions(
    typing.TypedDict, total=False
):
    kmsKeyName: str

@typing.type_check_only
class GoogleFirestoreAdminV1DailyRecurrence(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1Database(typing.TypedDict, total=False):
    appEngineIntegrationMode: typing.Literal[
        "APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    cmekConfig: GoogleFirestoreAdminV1CmekConfig
    concurrencyMode: typing.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED",
        "OPTIMISTIC",
        "PESSIMISTIC",
        "OPTIMISTIC_WITH_ENTITY_GROUPS",
    ]
    createTime: str
    databaseEdition: typing.Literal[
        "DATABASE_EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE"
    ]
    deleteProtectionState: typing.Literal[
        "DELETE_PROTECTION_STATE_UNSPECIFIED",
        "DELETE_PROTECTION_DISABLED",
        "DELETE_PROTECTION_ENABLED",
    ]
    deleteTime: str
    earliestVersionTime: str
    etag: str
    firestoreDataAccessMode: typing.Literal[
        "DATA_ACCESS_MODE_UNSPECIFIED",
        "DATA_ACCESS_MODE_ENABLED",
        "DATA_ACCESS_MODE_DISABLED",
    ]
    freeTier: bool
    keyPrefix: str
    locationId: str
    mongodbCompatibleDataAccessMode: typing.Literal[
        "DATA_ACCESS_MODE_UNSPECIFIED",
        "DATA_ACCESS_MODE_ENABLED",
        "DATA_ACCESS_MODE_DISABLED",
    ]
    name: str
    pointInTimeRecoveryEnablement: typing.Literal[
        "POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED",
        "POINT_IN_TIME_RECOVERY_ENABLED",
        "POINT_IN_TIME_RECOVERY_DISABLED",
    ]
    previousId: str
    realtimeUpdatesMode: typing.Literal[
        "REALTIME_UPDATES_MODE_UNSPECIFIED",
        "REALTIME_UPDATES_MODE_ENABLED",
        "REALTIME_UPDATES_MODE_DISABLED",
    ]
    sourceInfo: GoogleFirestoreAdminV1SourceInfo
    tags: dict[str, typing.Any]
    type: typing.Literal[
        "DATABASE_TYPE_UNSPECIFIED", "FIRESTORE_NATIVE", "DATASTORE_MODE"
    ]
    uid: str
    updateTime: str
    versionRetentionPeriod: str

@typing.type_check_only
class GoogleFirestoreAdminV1DeleteDatabaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1DisableUserCredsRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1EnableUserCredsRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1EncryptionConfig(typing.TypedDict, total=False):
    customerManagedEncryption: GoogleFirestoreAdminV1CustomerManagedEncryptionOptions
    googleDefaultEncryption: GoogleFirestoreAdminV1GoogleDefaultEncryptionOptions
    useSourceEncryption: GoogleFirestoreAdminV1SourceEncryptionOptions

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsMetadata(typing.TypedDict, total=False):
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
    outputUriPrefix: str
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
    snapshotTime: str
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsRequest(typing.TypedDict, total=False):
    collectionIds: _list[str]
    namespaceIds: _list[str]
    outputUriPrefix: str
    snapshotTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ExportDocumentsResponse(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleFirestoreAdminV1Field(typing.TypedDict, total=False):
    indexConfig: GoogleFirestoreAdminV1IndexConfig
    name: str
    ttlConfig: GoogleFirestoreAdminV1TtlConfig

@typing.type_check_only
class GoogleFirestoreAdminV1FieldOperationMetadata(typing.TypedDict, total=False):
    endTime: str
    field: str
    indexConfigDeltas: _list[GoogleFirestoreAdminV1IndexConfigDelta]
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
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
    ttlConfigDelta: GoogleFirestoreAdminV1TtlConfigDelta

@typing.type_check_only
class GoogleFirestoreAdminV1FlatIndex(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1GoogleDefaultEncryptionOptions(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirestoreAdminV1ImportDocumentsMetadata(typing.TypedDict, total=False):
    collectionIds: _list[str]
    endTime: str
    inputUriPrefix: str
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
    startTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1ImportDocumentsRequest(typing.TypedDict, total=False):
    collectionIds: _list[str]
    inputUriPrefix: str
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleFirestoreAdminV1Index(typing.TypedDict, total=False):
    apiScope: typing.Literal["ANY_API", "DATASTORE_MODE_API", "MONGODB_COMPATIBLE_API"]
    density: typing.Literal["DENSITY_UNSPECIFIED", "SPARSE_ALL", "SPARSE_ANY", "DENSE"]
    fields: _list[GoogleFirestoreAdminV1IndexField]
    multikey: bool
    name: str
    queryScope: typing.Literal[
        "QUERY_SCOPE_UNSPECIFIED",
        "COLLECTION",
        "COLLECTION_GROUP",
        "COLLECTION_RECURSIVE",
    ]
    searchIndexOptions: GoogleFirestoreAdminV1SearchIndexOptions
    shardCount: int
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY", "NEEDS_REPAIR"]
    unique: bool

@typing.type_check_only
class GoogleFirestoreAdminV1IndexConfig(typing.TypedDict, total=False):
    ancestorField: str
    indexes: _list[GoogleFirestoreAdminV1Index]
    reverting: bool
    usesAncestorConfig: bool

@typing.type_check_only
class GoogleFirestoreAdminV1IndexConfigDelta(typing.TypedDict, total=False):
    changeType: typing.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
    index: GoogleFirestoreAdminV1Index

@typing.type_check_only
class GoogleFirestoreAdminV1IndexField(typing.TypedDict, total=False):
    arrayConfig: typing.Literal["ARRAY_CONFIG_UNSPECIFIED", "CONTAINS"]
    fieldPath: str
    order: typing.Literal["ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    searchConfig: GoogleFirestoreAdminV1SearchConfig
    vectorConfig: GoogleFirestoreAdminV1VectorConfig

@typing.type_check_only
class GoogleFirestoreAdminV1IndexOperationMetadata(typing.TypedDict, total=False):
    endTime: str
    index: str
    progressBytes: GoogleFirestoreAdminV1Progress
    progressDocuments: GoogleFirestoreAdminV1Progress
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
class GoogleFirestoreAdminV1ListBackupSchedulesResponse(typing.TypedDict, total=False):
    backupSchedules: _list[GoogleFirestoreAdminV1BackupSchedule]

@typing.type_check_only
class GoogleFirestoreAdminV1ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[GoogleFirestoreAdminV1Backup]
    unreachable: _list[str]

@typing.type_check_only
class GoogleFirestoreAdminV1ListDatabasesResponse(typing.TypedDict, total=False):
    databases: _list[GoogleFirestoreAdminV1Database]
    unreachable: _list[str]

@typing.type_check_only
class GoogleFirestoreAdminV1ListFieldsResponse(typing.TypedDict, total=False):
    fields: _list[GoogleFirestoreAdminV1Field]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1ListIndexesResponse(typing.TypedDict, total=False):
    indexes: _list[GoogleFirestoreAdminV1Index]
    nextPageToken: str

@typing.type_check_only
class GoogleFirestoreAdminV1ListUserCredsResponse(typing.TypedDict, total=False):
    userCreds: _list[GoogleFirestoreAdminV1UserCreds]

@typing.type_check_only
class GoogleFirestoreAdminV1LocationMetadata(typing.TypedDict, total=False): ...

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
class GoogleFirestoreAdminV1ResetUserPasswordRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1ResourceIdentity(typing.TypedDict, total=False):
    principal: str

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
class GoogleFirestoreAdminV1RestoreDatabaseRequest(typing.TypedDict, total=False):
    backup: str
    databaseId: str
    encryptionConfig: GoogleFirestoreAdminV1EncryptionConfig
    tags: dict[str, typing.Any]

@typing.type_check_only
class GoogleFirestoreAdminV1SearchConfig(typing.TypedDict, total=False):
    geoSpec: GoogleFirestoreAdminV1SearchGeoSpec
    textSpec: GoogleFirestoreAdminV1SearchTextSpec

@typing.type_check_only
class GoogleFirestoreAdminV1SearchGeoSpec(typing.TypedDict, total=False):
    geoJsonIndexingDisabled: bool

@typing.type_check_only
class GoogleFirestoreAdminV1SearchIndexOptions(typing.TypedDict, total=False):
    textLanguage: str
    textLanguageOverrideFieldPath: str

@typing.type_check_only
class GoogleFirestoreAdminV1SearchTextIndexSpec(typing.TypedDict, total=False):
    indexType: typing.Literal["TEXT_INDEX_TYPE_UNSPECIFIED", "TOKENIZED"]
    matchType: typing.Literal["TEXT_MATCH_TYPE_UNSPECIFIED", "MATCH_GLOBALLY"]

@typing.type_check_only
class GoogleFirestoreAdminV1SearchTextSpec(typing.TypedDict, total=False):
    indexSpecs: _list[GoogleFirestoreAdminV1SearchTextIndexSpec]

@typing.type_check_only
class GoogleFirestoreAdminV1SourceEncryptionOptions(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1SourceInfo(typing.TypedDict, total=False):
    backup: GoogleFirestoreAdminV1BackupSource
    operation: str

@typing.type_check_only
class GoogleFirestoreAdminV1Stats(typing.TypedDict, total=False):
    documentCount: str
    indexCount: str
    sizeBytes: str

@typing.type_check_only
class GoogleFirestoreAdminV1TtlConfig(typing.TypedDict, total=False):
    expirationOffset: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE", "NEEDS_REPAIR"]

@typing.type_check_only
class GoogleFirestoreAdminV1TtlConfigDelta(typing.TypedDict, total=False):
    changeType: typing.Literal["CHANGE_TYPE_UNSPECIFIED", "ADD", "REMOVE"]
    expirationOffset: str

@typing.type_check_only
class GoogleFirestoreAdminV1UpdateDatabaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirestoreAdminV1UserCreds(typing.TypedDict, total=False):
    createTime: str
    name: str
    resourceIdentity: GoogleFirestoreAdminV1ResourceIdentity
    securePassword: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    updateTime: str

@typing.type_check_only
class GoogleFirestoreAdminV1VectorConfig(typing.TypedDict, total=False):
    dimension: int
    flat: GoogleFirestoreAdminV1FlatIndex

@typing.type_check_only
class GoogleFirestoreAdminV1WeeklyRecurrence(typing.TypedDict, total=False):
    day: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class ListCollectionIdsRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    readTime: str

@typing.type_check_only
class ListCollectionIdsResponse(typing.TypedDict, total=False):
    collectionIds: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListDocumentsResponse(typing.TypedDict, total=False):
    documents: _list[Document]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListenRequest(typing.TypedDict, total=False):
    addTarget: Target
    labels: dict[str, typing.Any]
    removeTarget: int

@typing.type_check_only
class ListenResponse(typing.TypedDict, total=False):
    documentChange: DocumentChange
    documentDelete: DocumentDelete
    documentRemove: DocumentRemove
    filter: ExistenceFilter
    targetChange: TargetChange

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MapValue(typing.TypedDict, total=False):
    fields: dict[str, typing.Any]

@typing.type_check_only
class Order(typing.TypedDict, total=False):
    direction: typing.Literal["DIRECTION_UNSPECIFIED", "ASCENDING", "DESCENDING"]
    field: FieldReference

@typing.type_check_only
class PartitionQueryRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    partitionCount: str
    readTime: str
    structuredQuery: StructuredQuery

@typing.type_check_only
class PartitionQueryResponse(typing.TypedDict, total=False):
    nextPageToken: str
    partitions: _list[Cursor]

@typing.type_check_only
class Pipeline(typing.TypedDict, total=False):
    stages: _list[Stage]

@typing.type_check_only
class PlanSummary(typing.TypedDict, total=False):
    indexesUsed: _list[dict[str, typing.Any]]

@typing.type_check_only
class Precondition(typing.TypedDict, total=False):
    exists: bool
    updateTime: str

@typing.type_check_only
class Projection(typing.TypedDict, total=False):
    fields: _list[FieldReference]

@typing.type_check_only
class QueryTarget(typing.TypedDict, total=False):
    parent: str
    structuredQuery: StructuredQuery

@typing.type_check_only
class ReadOnly(typing.TypedDict, total=False):
    readTime: str

@typing.type_check_only
class ReadWrite(typing.TypedDict, total=False):
    concurrencyMode: typing.Literal[
        "CONCURRENCY_MODE_UNSPECIFIED", "OPTIMISTIC", "PESSIMISTIC"
    ]
    retryTransaction: str

@typing.type_check_only
class RollbackRequest(typing.TypedDict, total=False):
    transaction: str

@typing.type_check_only
class RunAggregationQueryRequest(typing.TypedDict, total=False):
    explainOptions: ExplainOptions
    newTransaction: TransactionOptions
    readTime: str
    structuredAggregationQuery: StructuredAggregationQuery
    transaction: str

@typing.type_check_only
class RunAggregationQueryResponse(typing.TypedDict, total=False):
    explainMetrics: ExplainMetrics
    readTime: str
    result: AggregationResult
    transaction: str

@typing.type_check_only
class RunQueryRequest(typing.TypedDict, total=False):
    explainOptions: ExplainOptions
    newTransaction: TransactionOptions
    readTime: str
    structuredQuery: StructuredQuery
    transaction: str

@typing.type_check_only
class RunQueryResponse(typing.TypedDict, total=False):
    document: Document
    done: bool
    explainMetrics: ExplainMetrics
    readTime: str
    skippedResults: int
    transaction: str

@typing.type_check_only
class Stage(typing.TypedDict, total=False):
    args: _list[Value]
    name: str
    options: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructuredAggregationQuery(typing.TypedDict, total=False):
    aggregations: _list[Aggregation]
    structuredQuery: StructuredQuery

@typing.type_check_only
class StructuredPipeline(typing.TypedDict, total=False):
    options: dict[str, typing.Any]
    pipeline: Pipeline

AlternativeStructuredQuery = typing.TypedDict(
    "AlternativeStructuredQuery",
    {
        "endAt": Cursor,
        "findNearest": FindNearest,
        "from": _list[CollectionSelector],
        "limit": int,
        "offset": int,
        "orderBy": _list[Order],
        "select": Projection,
        "startAt": Cursor,
        "where": Filter,
    },
    total=False,
)

@typing.type_check_only
class StructuredQuery(AlternativeStructuredQuery): ...

@typing.type_check_only
class Sum(typing.TypedDict, total=False):
    field: FieldReference

@typing.type_check_only
class Target(typing.TypedDict, total=False):
    documents: DocumentsTarget
    expectedCount: int
    once: bool
    query: QueryTarget
    readTime: str
    resumeToken: str
    targetId: int

@typing.type_check_only
class TargetChange(typing.TypedDict, total=False):
    cause: Status
    readTime: str
    resumeToken: str
    targetChangeType: typing.Literal["NO_CHANGE", "ADD", "REMOVE", "CURRENT", "RESET"]
    targetIds: _list[int]

@typing.type_check_only
class TransactionOptions(typing.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class UnaryFilter(typing.TypedDict, total=False):
    field: FieldReference
    op: typing.Literal[
        "OPERATOR_UNSPECIFIED", "IS_NAN", "IS_NULL", "IS_NOT_NAN", "IS_NOT_NULL"
    ]

@typing.type_check_only
class Value(typing.TypedDict, total=False):
    arrayValue: ArrayValue
    booleanValue: bool
    bytesValue: str
    doubleValue: float
    fieldReferenceValue: str
    functionValue: Function
    geoPointValue: LatLng
    integerValue: str
    mapValue: MapValue
    nullValue: typing.Literal["NULL_VALUE"]
    pipelineValue: Pipeline
    referenceValue: str
    stringValue: str
    timestampValue: str
    variableReferenceValue: str

@typing.type_check_only
class Write(typing.TypedDict, total=False):
    currentDocument: Precondition
    delete: str
    transform: DocumentTransform
    update: Document
    updateMask: DocumentMask
    updateTransforms: _list[FieldTransform]

@typing.type_check_only
class WriteRequest(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    streamId: str
    streamToken: str
    writes: _list[Write]

@typing.type_check_only
class WriteResponse(typing.TypedDict, total=False):
    commitTime: str
    streamId: str
    streamToken: str
    writeResults: _list[WriteResult]

@typing.type_check_only
class WriteResult(typing.TypedDict, total=False):
    transformResults: _list[Value]
    updateTime: str
