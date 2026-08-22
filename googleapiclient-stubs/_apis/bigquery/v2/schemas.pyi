import typing

_list = list

@typing.type_check_only
class AggregateClassificationMetrics(typing.TypedDict, total=False):
    accuracy: float
    f1Score: float
    logLoss: float
    precision: float
    recall: float
    rocAuc: float
    threshold: float

@typing.type_check_only
class AggregationThresholdPolicy(typing.TypedDict, total=False):
    privacyUnitColumns: _list[str]
    threshold: str

@typing.type_check_only
class Argument(typing.TypedDict, total=False):
    argumentKind: typing.Literal[
        "ARGUMENT_KIND_UNSPECIFIED",
        "FIXED_TYPE",
        "ANY_TYPE",
        "FIXED_TABLE",
        "ANY_TABLE",
    ]
    dataType: StandardSqlDataType
    isAggregate: bool
    mode: typing.Literal["MODE_UNSPECIFIED", "IN", "OUT", "INOUT"]
    name: str
    tableType: StandardSqlTableType

@typing.type_check_only
class ArimaCoefficients(typing.TypedDict, total=False):
    autoRegressiveCoefficients: _list[float]
    interceptCoefficient: float
    movingAverageCoefficients: _list[float]

@typing.type_check_only
class ArimaFittingMetrics(typing.TypedDict, total=False):
    aic: float
    logLikelihood: float
    variance: float

@typing.type_check_only
class ArimaForecastingMetrics(typing.TypedDict, total=False):
    arimaFittingMetrics: _list[ArimaFittingMetrics]
    arimaSingleModelForecastingMetrics: _list[ArimaSingleModelForecastingMetrics]
    hasDrift: _list[bool]
    nonSeasonalOrder: _list[ArimaOrder]
    seasonalPeriods: _list[
        typing.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
            "HOURLY",
        ]
    ]
    timeSeriesId: _list[str]

@typing.type_check_only
class ArimaModelInfo(typing.TypedDict, total=False):
    arimaCoefficients: ArimaCoefficients
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    hasHolidayEffect: bool
    hasSpikesAndDips: bool
    hasStepChanges: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: _list[
        typing.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
            "HOURLY",
        ]
    ]
    timeSeriesId: str
    timeSeriesIds: _list[str]

@typing.type_check_only
class ArimaOrder(typing.TypedDict, total=False):
    d: str
    p: str
    q: str

@typing.type_check_only
class ArimaResult(typing.TypedDict, total=False):
    arimaModelInfo: _list[ArimaModelInfo]
    seasonalPeriods: _list[
        typing.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
            "HOURLY",
        ]
    ]

@typing.type_check_only
class ArimaSingleModelForecastingMetrics(typing.TypedDict, total=False):
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    hasHolidayEffect: bool
    hasSpikesAndDips: bool
    hasStepChanges: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: _list[
        typing.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
            "HOURLY",
        ]
    ]
    timeSeriesId: str
    timeSeriesIds: _list[str]

@typing.type_check_only
class ArrowRecordBatch(typing.TypedDict, total=False):
    serializedRecordBatch: str

@typing.type_check_only
class ArrowSchema(typing.TypedDict, total=False):
    serializedSchema: str

@typing.type_check_only
class ArrowSerializationOptions(typing.TypedDict, total=False):
    bufferCompression: typing.Literal["COMPRESSION_UNSPECIFIED", "LZ4_FRAME", "ZSTD"]
    picosTimestampPrecision: typing.Literal[
        "PICOS_TIMESTAMP_PRECISION_UNSPECIFIED",
        "TIMESTAMP_PRECISION_MICROS",
        "TIMESTAMP_PRECISION_NANOS",
        "TIMESTAMP_PRECISION_PICOS",
    ]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AvroOptions(typing.TypedDict, total=False):
    useAvroLogicalTypes: bool

@typing.type_check_only
class BatchDeleteRowAccessPoliciesRequest(typing.TypedDict, total=False):
    force: bool
    policyIds: _list[str]

@typing.type_check_only
class BiEngineReason(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED",
        "NO_RESERVATION",
        "INSUFFICIENT_RESERVATION",
        "UNSUPPORTED_SQL_TEXT",
        "INPUT_TOO_LARGE",
        "OTHER_REASON",
        "TABLE_EXCLUDED",
    ]
    message: str

@typing.type_check_only
class BiEngineStatistics(typing.TypedDict, total=False):
    accelerationMode: typing.Literal[
        "BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED",
        "BI_ENGINE_DISABLED",
        "PARTIAL_INPUT",
        "FULL_INPUT",
        "FULL_QUERY",
    ]
    biEngineMode: typing.Literal[
        "ACCELERATION_MODE_UNSPECIFIED", "DISABLED", "PARTIAL", "FULL"
    ]
    biEngineReasons: _list[BiEngineReason]

@typing.type_check_only
class BigLakeConfiguration(typing.TypedDict, total=False):
    connectionId: str
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "PARQUET"]
    storageUri: str
    tableFormat: typing.Literal["TABLE_FORMAT_UNSPECIFIED", "ICEBERG"]

@typing.type_check_only
class BigQueryModelTraining(typing.TypedDict, total=False):
    currentIteration: int
    expectedTotalIterations: str

@typing.type_check_only
class BigtableColumn(typing.TypedDict, total=False):
    encoding: str
    fieldName: str
    onlyReadLatest: bool
    protoConfig: BigtableProtoConfig
    qualifierEncoded: str
    qualifierString: str
    type: str

@typing.type_check_only
class BigtableColumnFamily(typing.TypedDict, total=False):
    columns: _list[BigtableColumn]
    encoding: str
    familyId: str
    onlyReadLatest: bool
    protoConfig: BigtableProtoConfig
    type: str

@typing.type_check_only
class BigtableOptions(typing.TypedDict, total=False):
    columnFamilies: _list[BigtableColumnFamily]
    ignoreUnspecifiedColumnFamilies: bool
    outputColumnFamiliesAsJson: bool
    readRowkeyAsString: bool

@typing.type_check_only
class BigtableProtoConfig(typing.TypedDict, total=False):
    protoMessageName: str
    schemaBundleId: str

@typing.type_check_only
class BinaryClassificationMetrics(typing.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    binaryConfusionMatrixList: _list[BinaryConfusionMatrix]
    negativeLabel: str
    positiveLabel: str

@typing.type_check_only
class BinaryConfusionMatrix(typing.TypedDict, total=False):
    accuracy: float
    f1Score: float
    falseNegatives: str
    falsePositives: str
    positiveClassThreshold: float
    precision: float
    recall: float
    trueNegatives: str
    truePositives: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BqmlIterationResult(typing.TypedDict, total=False):
    durationMs: str
    evalLoss: float
    index: int
    learnRate: float
    trainingLoss: float

@typing.type_check_only
class BqmlTrainingRun(typing.TypedDict, total=False):
    iterationResults: _list[BqmlIterationResult]
    startTime: str
    state: str
    trainingOptions: dict[str, typing.Any]

@typing.type_check_only
class CategoricalValue(typing.TypedDict, total=False):
    categoryCounts: _list[CategoryCount]

@typing.type_check_only
class CategoryCount(typing.TypedDict, total=False):
    category: str
    count: str

@typing.type_check_only
class CloneDefinition(typing.TypedDict, total=False):
    baseTableReference: TableReference
    cloneTime: str

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    centroidId: str
    count: str
    featureValues: _list[FeatureValue]

@typing.type_check_only
class ClusterInfo(typing.TypedDict, total=False):
    centroidId: str
    clusterRadius: float
    clusterSize: str

@typing.type_check_only
class Clustering(typing.TypedDict, total=False):
    fields: _list[str]

@typing.type_check_only
class ClusteringMetrics(typing.TypedDict, total=False):
    clusters: _list[Cluster]
    daviesBouldinIndex: float
    meanSquaredDistance: float

@typing.type_check_only
class ConfusionMatrix(typing.TypedDict, total=False):
    confidenceThreshold: float
    rows: _list[Row]

@typing.type_check_only
class ConnectionProperty(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class CsvOptions(typing.TypedDict, total=False):
    allowJaggedRows: bool
    allowQuotedNewlines: bool
    encoding: str
    fieldDelimiter: str
    nullMarker: str
    nullMarkers: _list[str]
    preserveAsciiControlCharacters: bool
    quote: str
    skipLeadingRows: str
    sourceColumnMatch: str

@typing.type_check_only
class DataFormatOptions(typing.TypedDict, total=False):
    timestampOutputFormat: typing.Literal[
        "TIMESTAMP_OUTPUT_FORMAT_UNSPECIFIED", "FLOAT64", "INT64", "ISO8601_STRING"
    ]
    useInt64Timestamp: bool

@typing.type_check_only
class DataMaskingStatistics(typing.TypedDict, total=False):
    dataMaskingApplied: bool

@typing.type_check_only
class DataPolicyList(typing.TypedDict, total=False):
    dataPolicies: _list[DataPolicyOption]

@typing.type_check_only
class DataPolicyOption(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DataSplitResult(typing.TypedDict, total=False):
    evaluationTable: TableReference
    testTable: TableReference
    trainingTable: TableReference

@typing.type_check_only
class Dataset(typing.TypedDict, total=False):
    access: _list[dict[str, typing.Any]]
    catalogSource: str
    creationTime: str
    datasetReference: DatasetReference
    defaultCollation: str
    defaultEncryptionConfiguration: EncryptionConfiguration
    defaultPartitionExpirationMs: str
    defaultRoundingMode: typing.Literal[
        "ROUNDING_MODE_UNSPECIFIED", "ROUND_HALF_AWAY_FROM_ZERO", "ROUND_HALF_EVEN"
    ]
    defaultTableExpirationMs: str
    description: str
    etag: str
    externalCatalogDatasetOptions: ExternalCatalogDatasetOptions
    externalDatasetReference: ExternalDatasetReference
    friendlyName: str
    id: str
    isCaseInsensitive: bool
    kind: str
    labels: dict[str, typing.Any]
    lastModifiedTime: str
    linkedDatasetMetadata: LinkedDatasetMetadata
    linkedDatasetSource: LinkedDatasetSource
    location: str
    maxTimeTravelHours: str
    resourceTags: dict[str, typing.Any]
    restrictions: RestrictionConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    storageBillingModel: typing.Literal[
        "STORAGE_BILLING_MODEL_UNSPECIFIED", "LOGICAL", "PHYSICAL"
    ]
    tags: _list[dict[str, typing.Any]]
    type: str

@typing.type_check_only
class DatasetAccessEntry(typing.TypedDict, total=False):
    dataset: DatasetReference
    targetTypes: _list[typing.Literal["TARGET_TYPE_UNSPECIFIED", "VIEWS", "ROUTINES"]]

@typing.type_check_only
class DatasetList(typing.TypedDict, total=False):
    datasets: _list[dict[str, typing.Any]]
    etag: str
    kind: str
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class DatasetReference(typing.TypedDict, total=False):
    datasetId: str
    projectId: str

@typing.type_check_only
class DestinationTableProperties(typing.TypedDict, total=False):
    description: str
    expirationTime: str
    friendlyName: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class DifferentialPrivacyPolicy(typing.TypedDict, total=False):
    deltaBudget: float
    deltaBudgetRemaining: float
    deltaPerQuery: float
    epsilonBudget: float
    epsilonBudgetRemaining: float
    maxEpsilonPerQuery: float
    maxGroupsContributed: str
    privacyUnitColumn: str

@typing.type_check_only
class DimensionalityReductionMetrics(typing.TypedDict, total=False):
    totalExplainedVarianceRatio: float

@typing.type_check_only
class DmlStatistics(typing.TypedDict, total=False):
    deletedRowCount: str
    dmlMode: typing.Literal[
        "DML_MODE_UNSPECIFIED", "COARSE_GRAINED_DML", "FINE_GRAINED_DML"
    ]
    fineGrainedDmlUnusedReason: typing.Literal[
        "FINE_GRAINED_DML_UNUSED_REASON_UNSPECIFIED",
        "MAX_PARTITION_SIZE_EXCEEDED",
        "TABLE_NOT_ENROLLED",
        "DML_IN_MULTI_STATEMENT_TRANSACTION",
    ]
    insertedRowCount: str
    updatedRowCount: str

@typing.type_check_only
class DoubleCandidates(typing.TypedDict, total=False):
    candidates: _list[float]

@typing.type_check_only
class DoubleHparamSearchSpace(typing.TypedDict, total=False):
    candidates: DoubleCandidates
    range: DoubleRange

@typing.type_check_only
class DoubleRange(typing.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class EncryptionConfiguration(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class Entry(typing.TypedDict, total=False):
    itemCount: str
    predictedLabel: str

@typing.type_check_only
class ErrorProto(typing.TypedDict, total=False):
    debugInfo: str
    location: str
    message: str
    reason: str

@typing.type_check_only
class EvaluationMetrics(typing.TypedDict, total=False):
    arimaForecastingMetrics: ArimaForecastingMetrics
    binaryClassificationMetrics: BinaryClassificationMetrics
    clusteringMetrics: ClusteringMetrics
    dimensionalityReductionMetrics: DimensionalityReductionMetrics
    multiClassClassificationMetrics: MultiClassClassificationMetrics
    rankingMetrics: RankingMetrics
    regressionMetrics: RegressionMetrics

@typing.type_check_only
class ExplainQueryStage(typing.TypedDict, total=False):
    completedParallelInputs: str
    computeMode: typing.Literal["COMPUTE_MODE_UNSPECIFIED", "BIGQUERY", "BI_ENGINE"]
    computeMsAvg: str
    computeMsMax: str
    computeRatioAvg: float
    computeRatioMax: float
    endMs: str
    id: str
    inputStages: _list[str]
    name: str
    parallelInputs: str
    readMsAvg: str
    readMsMax: str
    readRatioAvg: float
    readRatioMax: float
    recordsRead: str
    recordsWritten: str
    shuffleOutputBytes: str
    shuffleOutputBytesSpilled: str
    slotMs: str
    startMs: str
    status: str
    steps: _list[ExplainQueryStep]
    waitMsAvg: str
    waitMsMax: str
    waitRatioAvg: float
    waitRatioMax: float
    writeMsAvg: str
    writeMsMax: str
    writeRatioAvg: float
    writeRatioMax: float

@typing.type_check_only
class ExplainQueryStep(typing.TypedDict, total=False):
    kind: str
    substeps: _list[str]

@typing.type_check_only
class Explanation(typing.TypedDict, total=False):
    attribution: float
    featureName: str

@typing.type_check_only
class ExportDataStatistics(typing.TypedDict, total=False):
    fileCount: str
    rowCount: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalCatalogDatasetOptions(typing.TypedDict, total=False):
    defaultStorageLocationUri: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class ExternalCatalogTableOptions(typing.TypedDict, total=False):
    connectionId: str
    parameters: dict[str, typing.Any]
    storageDescriptor: StorageDescriptor

@typing.type_check_only
class ExternalDataConfiguration(typing.TypedDict, total=False):
    autodetect: bool
    avroOptions: AvroOptions
    bigtableOptions: BigtableOptions
    compression: str
    connectionId: str
    csvOptions: CsvOptions
    dateFormat: str
    datetimeFormat: str
    decimalTargetTypes: _list[
        typing.Literal[
            "DECIMAL_TARGET_TYPE_UNSPECIFIED", "NUMERIC", "BIGNUMERIC", "STRING"
        ]
    ]
    fileSetSpecType: typing.Literal[
        "FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH",
        "FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST",
    ]
    googleSheetsOptions: GoogleSheetsOptions
    hivePartitioningOptions: HivePartitioningOptions
    ignoreUnknownValues: bool
    jsonExtension: typing.Literal["JSON_EXTENSION_UNSPECIFIED", "GEOJSON"]
    jsonOptions: JsonOptions
    maxBadRecords: int
    metadataCacheMode: typing.Literal[
        "METADATA_CACHE_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    objectMetadata: typing.Literal["OBJECT_METADATA_UNSPECIFIED", "DIRECTORY", "SIMPLE"]
    parquetOptions: ParquetOptions
    referenceFileSchemaUri: str
    schema: TableSchema
    sourceFormat: str
    sourceUris: _list[str]
    timeFormat: str
    timeZone: str
    timestampFormat: str
    timestampTargetPrecision: _list[int]

@typing.type_check_only
class ExternalDatasetReference(typing.TypedDict, total=False):
    connection: str
    externalSource: str

@typing.type_check_only
class ExternalRuntimeOptions(typing.TypedDict, total=False):
    containerCpu: float
    containerMemory: str
    containerRequestConcurrency: str
    maxBatchingRows: str
    runtimeConnection: str
    runtimeVersion: str

@typing.type_check_only
class ExternalServiceCost(typing.TypedDict, total=False):
    billingMethod: str
    bytesBilled: str
    bytesProcessed: str
    externalService: str
    reservedSlotCount: str
    slotMs: str

@typing.type_check_only
class FeatureValue(typing.TypedDict, total=False):
    categoricalValue: CategoricalValue
    featureColumn: str
    numericalValue: float

@typing.type_check_only
class ForeignTypeInfo(typing.TypedDict, total=False):
    typeSystem: typing.Literal["TYPE_SYSTEM_UNSPECIFIED", "HIVE"]

@typing.type_check_only
class ForeignViewDefinition(typing.TypedDict, total=False):
    dialect: str
    query: str

@typing.type_check_only
class GenAiErrorStats(typing.TypedDict, total=False):
    errors: _list[str]

@typing.type_check_only
class GenAiFunctionCacheStats(typing.TypedDict, total=False):
    numCacheHitRows: str

@typing.type_check_only
class GenAiFunctionCostOptimizationStats(typing.TypedDict, total=False):
    message: str
    numCostOptimizedRows: str

@typing.type_check_only
class GenAiFunctionErrorStats(typing.TypedDict, total=False):
    errors: _list[str]
    numFailedRows: str

@typing.type_check_only
class GenAiFunctionStats(typing.TypedDict, total=False):
    cacheStats: GenAiFunctionCacheStats
    costOptimizationStats: GenAiFunctionCostOptimizationStats
    errorStats: GenAiFunctionErrorStats
    functionName: str
    numProcessedRows: str
    prompt: str

@typing.type_check_only
class GenAiStats(typing.TypedDict, total=False):
    errorStats: GenAiErrorStats
    functionStats: _list[GenAiFunctionStats]

@typing.type_check_only
class GeneratedColumn(typing.TypedDict, total=False):
    generatedExpressionInfo: GeneratedExpressionInfo
    generatedMode: typing.Literal[
        "GENERATED_MODE_UNSPECIFIED", "GENERATED_ALWAYS", "GENERATED_BY_DEFAULT"
    ]

@typing.type_check_only
class GeneratedExpressionInfo(typing.TypedDict, total=False):
    asynchronous: bool
    generationExpression: str
    stored: bool

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GetQueryResultsResponse(typing.TypedDict, total=False):
    cacheHit: bool
    errors: _list[ErrorProto]
    etag: str
    jobComplete: bool
    jobReference: JobReference
    kind: str
    numDmlAffectedRows: str
    pageToken: str
    rows: _list[TableRow]
    schema: TableSchema
    totalBytesProcessed: str
    totalRows: str

@typing.type_check_only
class GetServiceAccountResponse(typing.TypedDict, total=False):
    email: str
    kind: str

@typing.type_check_only
class GlobalExplanation(typing.TypedDict, total=False):
    classLabel: str
    explanations: _list[Explanation]

@typing.type_check_only
class GoogleSheetsOptions(typing.TypedDict, total=False):
    range: str
    skipLeadingRows: str

@typing.type_check_only
class HighCardinalityJoin(typing.TypedDict, total=False):
    leftRows: str
    outputRows: str
    rightRows: str
    stepIndex: int

@typing.type_check_only
class HivePartitioningOptions(typing.TypedDict, total=False):
    fields: _list[str]
    mode: str
    requirePartitionFilter: bool
    sourceUriPrefix: str

@typing.type_check_only
class HparamSearchSpaces(typing.TypedDict, total=False):
    activationFn: StringHparamSearchSpace
    batchSize: IntHparamSearchSpace
    boosterType: StringHparamSearchSpace
    colsampleBylevel: DoubleHparamSearchSpace
    colsampleBynode: DoubleHparamSearchSpace
    colsampleBytree: DoubleHparamSearchSpace
    dartNormalizeType: StringHparamSearchSpace
    dropout: DoubleHparamSearchSpace
    hiddenUnits: IntArrayHparamSearchSpace
    l1Reg: DoubleHparamSearchSpace
    l2Reg: DoubleHparamSearchSpace
    learnRate: DoubleHparamSearchSpace
    maxTreeDepth: IntHparamSearchSpace
    minSplitLoss: DoubleHparamSearchSpace
    minTreeChildWeight: IntHparamSearchSpace
    numClusters: IntHparamSearchSpace
    numFactors: IntHparamSearchSpace
    numParallelTree: IntHparamSearchSpace
    optimizer: StringHparamSearchSpace
    subsample: DoubleHparamSearchSpace
    treeMethod: StringHparamSearchSpace
    walsAlpha: DoubleHparamSearchSpace

@typing.type_check_only
class HparamTuningTrial(typing.TypedDict, total=False):
    endTimeMs: str
    errorMessage: str
    evalLoss: float
    evaluationMetrics: EvaluationMetrics
    hparamTuningEvaluationMetrics: EvaluationMetrics
    hparams: TrainingOptions
    startTimeMs: str
    status: typing.Literal[
        "TRIAL_STATUS_UNSPECIFIED",
        "NOT_STARTED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "INFEASIBLE",
        "STOPPED_EARLY",
    ]
    trainingLoss: float
    trialId: str

@typing.type_check_only
class IncrementalResultStats(typing.TypedDict, total=False):
    disabledReason: typing.Literal[
        "DISABLED_REASON_UNSPECIFIED", "OTHER", "UNSUPPORTED_OPERATOR"
    ]
    disabledReasonDetails: str
    firstIncrementalRowTime: str
    incrementalRowCount: str
    lastIncrementalRowTime: str
    resultSetLastModifyTime: str
    resultSetLastReplaceTime: str

@typing.type_check_only
class IndexPruningStats(typing.TypedDict, total=False):
    baseTable: TableReference
    indexId: str
    postIndexPruningParallelInputCount: str
    preIndexPruningParallelInputCount: str

@typing.type_check_only
class IndexUnusedReason(typing.TypedDict, total=False):
    baseTable: TableReference
    code: typing.Literal[
        "CODE_UNSPECIFIED",
        "INDEX_CONFIG_NOT_AVAILABLE",
        "PENDING_INDEX_CREATION",
        "BASE_TABLE_TRUNCATED",
        "INDEX_CONFIG_MODIFIED",
        "TIME_TRAVEL_QUERY",
        "NO_PRUNING_POWER",
        "UNINDEXED_SEARCH_FIELDS",
        "UNSUPPORTED_SEARCH_PATTERN",
        "OPTIMIZED_WITH_MATERIALIZED_VIEW",
        "SECURED_BY_DATA_MASKING",
        "MISMATCHED_TEXT_ANALYZER",
        "BASE_TABLE_TOO_SMALL",
        "BASE_TABLE_TOO_LARGE",
        "ESTIMATED_PERFORMANCE_GAIN_TOO_LOW",
        "COLUMN_METADATA_INDEX_NOT_USED",
        "NOT_SUPPORTED_IN_STANDARD_EDITION",
        "INDEX_SUPPRESSED_BY_FUNCTION_OPTION",
        "QUERY_CACHE_HIT",
        "STALE_INDEX",
        "INTERNAL_ERROR",
        "OTHER_REASON",
    ]
    indexName: str
    message: str

@typing.type_check_only
class InputDataChange(typing.TypedDict, total=False):
    recordsReadDiffPercentage: float

@typing.type_check_only
class IntArray(typing.TypedDict, total=False):
    elements: _list[str]

@typing.type_check_only
class IntArrayHparamSearchSpace(typing.TypedDict, total=False):
    candidates: _list[IntArray]

@typing.type_check_only
class IntCandidates(typing.TypedDict, total=False):
    candidates: _list[str]

@typing.type_check_only
class IntHparamSearchSpace(typing.TypedDict, total=False):
    candidates: IntCandidates
    range: IntRange

@typing.type_check_only
class IntRange(typing.TypedDict, total=False):
    max: str
    min: str

@typing.type_check_only
class IterationResult(typing.TypedDict, total=False):
    arimaResult: ArimaResult
    clusterInfos: _list[ClusterInfo]
    durationMs: str
    evalLoss: float
    index: int
    learnRate: float
    principalComponentInfos: _list[PrincipalComponentInfo]
    trainingLoss: float

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    configuration: JobConfiguration
    etag: str
    id: str
    jobCreationReason: JobCreationReason
    jobReference: JobReference
    kind: str
    principal_subject: str
    selfLink: str
    statistics: JobStatistics
    status: JobStatus
    user_email: str

@typing.type_check_only
class JobCancelResponse(typing.TypedDict, total=False):
    job: Job
    kind: str

@typing.type_check_only
class JobConfiguration(typing.TypedDict, total=False):
    copy: JobConfigurationTableCopy
    dryRun: bool
    extract: JobConfigurationExtract
    jobTimeoutMs: str
    jobType: str
    labels: dict[str, typing.Any]
    load: JobConfigurationLoad
    maxSlots: int
    query: JobConfigurationQuery
    reservation: str

@typing.type_check_only
class JobConfigurationExtract(typing.TypedDict, total=False):
    compression: str
    destinationFormat: str
    destinationUri: str
    destinationUris: _list[str]
    fieldDelimiter: str
    modelExtractOptions: ModelExtractOptions
    printHeader: bool
    sourceModel: ModelReference
    sourceTable: TableReference
    useAvroLogicalTypes: bool

@typing.type_check_only
class JobConfigurationLoad(typing.TypedDict, total=False):
    allowJaggedRows: bool
    allowQuotedNewlines: bool
    autodetect: bool
    clustering: Clustering
    columnNameCharacterMap: typing.Literal[
        "COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED", "STRICT", "V1", "V2"
    ]
    connectionProperties: _list[ConnectionProperty]
    copyFilesOnly: bool
    createDisposition: str
    createSession: bool
    dateFormat: str
    datetimeFormat: str
    decimalTargetTypes: _list[
        typing.Literal[
            "DECIMAL_TARGET_TYPE_UNSPECIFIED", "NUMERIC", "BIGNUMERIC", "STRING"
        ]
    ]
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationTable: TableReference
    destinationTableProperties: DestinationTableProperties
    encoding: str
    fieldDelimiter: str
    fileSetSpecType: typing.Literal[
        "FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH",
        "FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST",
    ]
    hivePartitioningOptions: HivePartitioningOptions
    ignoreUnknownValues: bool
    jsonExtension: typing.Literal["JSON_EXTENSION_UNSPECIFIED", "GEOJSON"]
    maxBadRecords: int
    nullMarker: str
    nullMarkers: _list[str]
    parquetOptions: ParquetOptions
    preserveAsciiControlCharacters: bool
    projectionFields: _list[str]
    quote: str
    rangePartitioning: RangePartitioning
    referenceFileSchemaUri: str
    schema: TableSchema
    schemaInline: str
    schemaInlineFormat: str
    schemaUpdateOptions: _list[str]
    skipLeadingRows: int
    sourceColumnMatch: typing.Literal[
        "SOURCE_COLUMN_MATCH_UNSPECIFIED", "POSITION", "NAME"
    ]
    sourceFormat: str
    sourceUris: _list[str]
    timeFormat: str
    timePartitioning: TimePartitioning
    timeZone: str
    timestampFormat: str
    timestampTargetPrecision: _list[int]
    useAvroLogicalTypes: bool
    writeDisposition: str

@typing.type_check_only
class JobConfigurationQuery(typing.TypedDict, total=False):
    allowLargeResults: bool
    clustering: Clustering
    connectionProperties: _list[ConnectionProperty]
    continuous: bool
    createDisposition: str
    createSession: bool
    defaultDataset: DatasetReference
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationTable: TableReference
    flattenResults: bool
    maximumBillingTier: int
    maximumBytesBilled: str
    parameterMode: str
    preserveNulls: bool
    priority: str
    query: str
    queryParameters: _list[QueryParameter]
    rangePartitioning: RangePartitioning
    schemaUpdateOptions: _list[str]
    scriptOptions: ScriptOptions
    systemVariables: SystemVariables
    tableDefinitions: dict[str, typing.Any]
    timePartitioning: TimePartitioning
    useLegacySql: bool
    useQueryCache: bool
    userDefinedFunctionResources: _list[UserDefinedFunctionResource]
    writeDisposition: str
    writeIncrementalResults: bool

@typing.type_check_only
class JobConfigurationTableCopy(typing.TypedDict, total=False):
    createDisposition: str
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationExpirationTime: str
    destinationTable: TableReference
    operationType: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "COPY", "SNAPSHOT", "RESTORE", "CLONE"
    ]
    sourceTable: TableReference
    sourceTables: _list[TableReference]
    writeDisposition: str

@typing.type_check_only
class JobCreationReason(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "REQUESTED", "LONG_RUNNING", "LARGE_RESULTS", "OTHER"
    ]

@typing.type_check_only
class JobList(typing.TypedDict, total=False):
    etag: str
    jobs: _list[dict[str, typing.Any]]
    kind: str
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class JobReference(typing.TypedDict, total=False):
    jobId: str
    location: str
    projectId: str

@typing.type_check_only
class JobStatistics(typing.TypedDict, total=False):
    completionRatio: float
    copy: JobStatistics5
    creationTime: str
    dataMaskingStatistics: DataMaskingStatistics
    edition: typing.Literal[
        "RESERVATION_EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    endTime: str
    extract: JobStatistics4
    finalExecutionDurationMs: str
    globalQueryRemoteRegions: _list[str]
    load: JobStatistics3
    numChildJobs: str
    parentGlobalQueryJob: JobReference
    parentJobId: str
    query: JobStatistics2
    quotaDeferments: _list[str]
    reservationGroupPath: _list[str]
    reservationUsage: _list[dict[str, typing.Any]]
    reservation_id: str
    rowLevelSecurityStatistics: RowLevelSecurityStatistics
    scriptStatistics: ScriptStatistics
    sessionInfo: SessionInfo
    startTime: str
    totalBytesProcessed: str
    totalSlotMs: str
    transactionInfo: TransactionInfo

@typing.type_check_only
class JobStatistics2(typing.TypedDict, total=False):
    biEngineStatistics: BiEngineStatistics
    billingTier: int
    cacheHit: bool
    dclTargetDataset: DatasetReference
    dclTargetTable: TableReference
    dclTargetView: TableReference
    ddlAffectedRowAccessPolicyCount: str
    ddlDestinationTable: TableReference
    ddlOperationPerformed: str
    ddlTargetDataset: DatasetReference
    ddlTargetRoutine: RoutineReference
    ddlTargetRowAccessPolicy: RowAccessPolicyReference
    ddlTargetTable: TableReference
    dmlStats: DmlStatistics
    estimatedBytesProcessed: str
    exportDataStatistics: ExportDataStatistics
    externalServiceCosts: _list[ExternalServiceCost]
    genAiStats: GenAiStats
    incrementalResultStats: IncrementalResultStats
    loadQueryStatistics: LoadQueryStatistics
    materializedViewStatistics: MaterializedViewStatistics
    metadataCacheStatistics: MetadataCacheStatistics
    mlStatistics: MlStatistics
    modelTraining: BigQueryModelTraining
    modelTrainingCurrentIteration: int
    modelTrainingExpectedTotalIteration: str
    numDmlAffectedRows: str
    objectStorageStats: _list[ObjectStorageStats]
    performanceInsights: PerformanceInsights
    queryInfo: QueryInfo
    queryPlan: _list[ExplainQueryStage]
    referencedPropertyGraphs: _list[PropertyGraphReference]
    referencedRoutines: _list[RoutineReference]
    referencedTables: _list[TableReference]
    reservationUsage: _list[dict[str, typing.Any]]
    schema: TableSchema
    searchStatistics: SearchStatistics
    sparkStatistics: SparkStatistics
    statementType: str
    timeline: _list[QueryTimelineSample]
    totalBytesBilled: str
    totalBytesProcessed: str
    totalBytesProcessedAccuracy: str
    totalPartitionsProcessed: str
    totalServicesSkuSlotMs: str
    totalSlotMs: str
    transferredBytes: str
    undeclaredQueryParameters: _list[QueryParameter]
    vectorSearchStatistics: VectorSearchStatistics

@typing.type_check_only
class JobStatistics3(typing.TypedDict, total=False):
    badRecords: str
    inputFileBytes: str
    inputFiles: str
    outputBytes: str
    outputRows: str
    timeline: _list[QueryTimelineSample]

@typing.type_check_only
class JobStatistics4(typing.TypedDict, total=False):
    destinationUriFileCounts: _list[str]
    inputBytes: str
    timeline: _list[QueryTimelineSample]

@typing.type_check_only
class JobStatistics5(typing.TypedDict, total=False):
    copiedLogicalBytes: str
    copiedRows: str
    remoteDestinationRegion: str

@typing.type_check_only
class JobStatus(typing.TypedDict, total=False):
    errorResult: ErrorProto
    errors: _list[ErrorProto]
    state: str

@typing.type_check_only
class JoinRestrictionPolicy(typing.TypedDict, total=False):
    joinAllowedColumns: _list[str]
    joinCondition: typing.Literal[
        "JOIN_CONDITION_UNSPECIFIED",
        "JOIN_ANY",
        "JOIN_ALL",
        "JOIN_NOT_REQUIRED",
        "JOIN_BLOCKED",
    ]

@typing.type_check_only
class JsonObject(dict[str, typing.Any]): ...

@typing.type_check_only
class JsonOptions(typing.TypedDict, total=False):
    encoding: str

@typing.type_check_only
class JsonValue(dict[str, typing.Any]): ...

@typing.type_check_only
class LinkedDatasetMetadata(typing.TypedDict, total=False):
    linkState: typing.Literal["LINK_STATE_UNSPECIFIED", "LINKED", "UNLINKED"]

@typing.type_check_only
class LinkedDatasetSource(typing.TypedDict, total=False):
    sourceDataset: DatasetReference

@typing.type_check_only
class ListModelsResponse(typing.TypedDict, total=False):
    models: _list[Model]
    nextPageToken: str

@typing.type_check_only
class ListRoutinesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    routines: _list[Routine]

@typing.type_check_only
class ListRowAccessPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rowAccessPolicies: _list[RowAccessPolicy]

@typing.type_check_only
class LoadQueryStatistics(typing.TypedDict, total=False):
    badRecords: str
    bytesTransferred: str
    inputFileBytes: str
    inputFiles: str
    outputBytes: str
    outputRows: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    legacyLocationId: str

@typing.type_check_only
class MaterializedView(typing.TypedDict, total=False):
    chosen: bool
    estimatedBytesSaved: str
    rejectedReason: typing.Literal[
        "REJECTED_REASON_UNSPECIFIED",
        "NO_DATA",
        "COST",
        "BASE_TABLE_TRUNCATED",
        "BASE_TABLE_DATA_CHANGE",
        "BASE_TABLE_PARTITION_EXPIRATION_CHANGE",
        "BASE_TABLE_EXPIRED_PARTITION",
        "BASE_TABLE_INCOMPATIBLE_METADATA_CHANGE",
        "TIME_ZONE",
        "OUT_OF_TIME_TRAVEL_WINDOW",
        "BASE_TABLE_FINE_GRAINED_SECURITY_POLICY",
        "BASE_TABLE_TOO_STALE",
    ]
    tableReference: TableReference

@typing.type_check_only
class MaterializedViewDefinition(typing.TypedDict, total=False):
    allowNonIncrementalDefinition: bool
    enableRefresh: bool
    lastRefreshTime: str
    maxStaleness: str
    query: str
    refreshIntervalMs: str

@typing.type_check_only
class MaterializedViewStatistics(typing.TypedDict, total=False):
    materializedView: _list[MaterializedView]

@typing.type_check_only
class MaterializedViewStatus(typing.TypedDict, total=False):
    lastRefreshStatus: ErrorProto
    refreshWatermark: str

@typing.type_check_only
class MetadataCacheStalenessInsight(typing.TypedDict, total=False):
    avgPreviousStalenessMs: str
    stalenessPercentageIncrease: float

@typing.type_check_only
class MetadataCacheStatistics(typing.TypedDict, total=False):
    tableMetadataCacheUsage: _list[TableMetadataCacheUsage]

@typing.type_check_only
class MlStatistics(typing.TypedDict, total=False):
    hparamTrials: _list[HparamTuningTrial]
    iterationResults: _list[IterationResult]
    maxIterations: str
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "LINEAR_REGRESSION",
        "LOGISTIC_REGRESSION",
        "KMEANS",
        "MATRIX_FACTORIZATION",
        "DNN_CLASSIFIER",
        "TENSORFLOW",
        "DNN_REGRESSOR",
        "XGBOOST",
        "BOOSTED_TREE_REGRESSOR",
        "BOOSTED_TREE_CLASSIFIER",
        "ARIMA",
        "AUTOML_REGRESSOR",
        "AUTOML_CLASSIFIER",
        "PCA",
        "DNN_LINEAR_COMBINED_CLASSIFIER",
        "DNN_LINEAR_COMBINED_REGRESSOR",
        "AUTOENCODER",
        "ARIMA_PLUS",
        "ARIMA_PLUS_XREG",
        "RANDOM_FOREST_REGRESSOR",
        "RANDOM_FOREST_CLASSIFIER",
        "TENSORFLOW_LITE",
        "ONNX",
        "TRANSFORM_ONLY",
        "CONTRIBUTION_ANALYSIS",
    ]
    trainingType: typing.Literal[
        "TRAINING_TYPE_UNSPECIFIED", "SINGLE_TRAINING", "HPARAM_TUNING"
    ]

@typing.type_check_only
class Model(typing.TypedDict, total=False):
    bestTrialId: str
    creationTime: str
    defaultTrialId: str
    description: str
    encryptionConfiguration: EncryptionConfiguration
    etag: str
    expirationTime: str
    featureColumns: _list[StandardSqlField]
    friendlyName: str
    hparamSearchSpaces: HparamSearchSpaces
    hparamTrials: _list[HparamTuningTrial]
    labelColumns: _list[StandardSqlField]
    labels: dict[str, typing.Any]
    lastModifiedTime: str
    location: str
    modelReference: ModelReference
    modelType: typing.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "LINEAR_REGRESSION",
        "LOGISTIC_REGRESSION",
        "KMEANS",
        "MATRIX_FACTORIZATION",
        "DNN_CLASSIFIER",
        "TENSORFLOW",
        "DNN_REGRESSOR",
        "XGBOOST",
        "BOOSTED_TREE_REGRESSOR",
        "BOOSTED_TREE_CLASSIFIER",
        "ARIMA",
        "AUTOML_REGRESSOR",
        "AUTOML_CLASSIFIER",
        "PCA",
        "DNN_LINEAR_COMBINED_CLASSIFIER",
        "DNN_LINEAR_COMBINED_REGRESSOR",
        "AUTOENCODER",
        "ARIMA_PLUS",
        "ARIMA_PLUS_XREG",
        "RANDOM_FOREST_REGRESSOR",
        "RANDOM_FOREST_CLASSIFIER",
        "TENSORFLOW_LITE",
        "ONNX",
        "TRANSFORM_ONLY",
        "CONTRIBUTION_ANALYSIS",
    ]
    optimalTrialIds: _list[str]
    remoteModelInfo: RemoteModelInfo
    trainingRuns: _list[TrainingRun]
    transformColumns: _list[TransformColumn]

@typing.type_check_only
class ModelDefinition(typing.TypedDict, total=False):
    modelOptions: dict[str, typing.Any]
    trainingRuns: _list[BqmlTrainingRun]

@typing.type_check_only
class ModelExtractOptions(typing.TypedDict, total=False):
    trialId: str

@typing.type_check_only
class ModelReference(typing.TypedDict, total=False):
    datasetId: str
    modelId: str
    projectId: str

@typing.type_check_only
class MultiClassClassificationMetrics(typing.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    confusionMatrixList: _list[ConfusionMatrix]

@typing.type_check_only
class ObjectStorageStats(typing.TypedDict, total=False):
    cacheBytesRead: str
    cloudProvider: typing.Literal["CLOUD_PROVIDER_UNSPECIFIED", "GCP", "AWS", "AZURE"]
    objectStorageBytesRead: str

@typing.type_check_only
class ParquetOptions(typing.TypedDict, total=False):
    enableListInference: bool
    enumAsString: bool
    mapTargetType: typing.Literal["MAP_TARGET_TYPE_UNSPECIFIED", "ARRAY_OF_STRUCT"]

@typing.type_check_only
class PartitionSkew(typing.TypedDict, total=False):
    skewSources: _list[SkewSource]

@typing.type_check_only
class PartitionedColumn(typing.TypedDict, total=False):
    field: str

@typing.type_check_only
class PartitioningDefinition(typing.TypedDict, total=False):
    partitionedColumn: _list[PartitionedColumn]

@typing.type_check_only
class PerformanceInsights(typing.TypedDict, total=False):
    avgPreviousExecutionMs: str
    stagePerformanceChangeInsights: _list[StagePerformanceChangeInsight]
    stagePerformanceStandaloneInsights: _list[StagePerformanceStandaloneInsight]
    tableChangeInsights: _list[TableChangeInsight]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrincipalComponentInfo(typing.TypedDict, total=False):
    cumulativeExplainedVarianceRatio: float
    explainedVariance: float
    explainedVarianceRatio: float
    principalComponentId: str

@typing.type_check_only
class PrivacyPolicy(typing.TypedDict, total=False):
    aggregationThresholdPolicy: AggregationThresholdPolicy
    differentialPrivacyPolicy: DifferentialPrivacyPolicy
    joinRestrictionPolicy: JoinRestrictionPolicy

@typing.type_check_only
class ProjectList(typing.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    projects: _list[dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class ProjectReference(typing.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class PropertyGraphReference(typing.TypedDict, total=False):
    datasetId: str
    projectId: str
    propertyGraphId: str

@typing.type_check_only
class PruningStats(typing.TypedDict, total=False):
    postCmetaPruningParallelInputCount: str
    postCmetaPruningPartitionCount: str
    preCmetaPruningParallelInputCount: str

@typing.type_check_only
class PythonOptions(typing.TypedDict, total=False):
    entryPoint: str
    packages: _list[str]

@typing.type_check_only
class QueryInfo(typing.TypedDict, total=False):
    optimizationDetails: dict[str, typing.Any]

@typing.type_check_only
class QueryParameter(typing.TypedDict, total=False):
    name: str
    parameterType: QueryParameterType
    parameterValue: QueryParameterValue

@typing.type_check_only
class QueryParameterType(typing.TypedDict, total=False):
    arrayType: QueryParameterType
    rangeElementType: QueryParameterType
    structTypes: _list[dict[str, typing.Any]]
    timestampPrecision: str
    type: str

@typing.type_check_only
class QueryParameterValue(typing.TypedDict, total=False):
    arrayValues: _list[QueryParameterValue]
    rangeValue: RangeValue
    structValues: dict[str, typing.Any]
    value: str

@typing.type_check_only
class QueryRequest(typing.TypedDict, total=False):
    arrowSerializationOptions: ArrowSerializationOptions
    connectionProperties: _list[ConnectionProperty]
    continuous: bool
    createSession: bool
    defaultDataset: DatasetReference
    destinationEncryptionConfiguration: EncryptionConfiguration
    dryRun: bool
    formatOptions: DataFormatOptions
    jobCreationMode: typing.Literal[
        "JOB_CREATION_MODE_UNSPECIFIED",
        "JOB_CREATION_REQUIRED",
        "JOB_CREATION_OPTIONAL",
    ]
    jobTimeoutMs: str
    kind: str
    labels: dict[str, typing.Any]
    location: str
    maxResults: int
    maxSlots: int
    maximumBytesBilled: str
    parameterMode: str
    preserveNulls: bool
    query: str
    queryParameters: _list[QueryParameter]
    queryResultsFormat: typing.Literal[
        "QUERY_RESULTS_FORMAT_UNSPECIFIED", "STRUCT_ENCODING", "ARROW"
    ]
    requestId: str
    reservation: str
    timeoutMs: int
    useLegacySql: bool
    useQueryCache: bool
    writeIncrementalResults: bool

@typing.type_check_only
class QueryResponse(typing.TypedDict, total=False):
    arrowRecordBatch: ArrowRecordBatch
    arrowSchema: ArrowSchema
    cacheHit: bool
    creationTime: str
    dmlStats: DmlStatistics
    endTime: str
    errors: _list[ErrorProto]
    jobComplete: bool
    jobCreationReason: JobCreationReason
    jobReference: JobReference
    kind: str
    location: str
    numDmlAffectedRows: str
    pageRowCount: str
    pageToken: str
    queryId: str
    rows: _list[TableRow]
    schema: TableSchema
    sessionInfo: SessionInfo
    startTime: str
    statementType: str
    totalBytesBilled: str
    totalBytesProcessed: str
    totalRows: str
    totalSlotMs: str

@typing.type_check_only
class QueryTimelineSample(typing.TypedDict, total=False):
    activeUnits: str
    completedUnits: str
    elapsedMs: str
    estimatedRunnableUnits: str
    pendingUnits: str
    shuffleRamUsageRatio: float
    totalSlotMs: str

@typing.type_check_only
class RangePartitioning(typing.TypedDict, total=False):
    field: str
    range: dict[str, typing.Any]

@typing.type_check_only
class RangeValue(typing.TypedDict, total=False):
    end: QueryParameterValue
    start: QueryParameterValue

@typing.type_check_only
class RankingMetrics(typing.TypedDict, total=False):
    averageRank: float
    meanAveragePrecision: float
    meanSquaredError: float
    normalizedDiscountedCumulativeGain: float

@typing.type_check_only
class RegressionMetrics(typing.TypedDict, total=False):
    meanAbsoluteError: float
    meanSquaredError: float
    meanSquaredLogError: float
    medianAbsoluteError: float
    rSquared: float

@typing.type_check_only
class RemoteFunctionOptions(typing.TypedDict, total=False):
    connection: str
    endpoint: str
    maxBatchingRows: str
    userDefinedContext: dict[str, typing.Any]

@typing.type_check_only
class RemoteModelInfo(typing.TypedDict, total=False):
    connection: str
    endpoint: str
    maxBatchingRows: str
    remoteModelVersion: str
    remoteServiceType: typing.Literal[
        "REMOTE_SERVICE_TYPE_UNSPECIFIED",
        "CLOUD_AI_TRANSLATE_V3",
        "CLOUD_AI_VISION_V1",
        "CLOUD_AI_NATURAL_LANGUAGE_V1",
        "CLOUD_AI_SPEECH_TO_TEXT_V2",
    ]
    speechRecognizer: str

@typing.type_check_only
class RestrictionConfig(typing.TypedDict, total=False):
    type: typing.Literal["RESTRICTION_TYPE_UNSPECIFIED", "RESTRICTED_DATA_EGRESS"]

@typing.type_check_only
class Routine(typing.TypedDict, total=False):
    arguments: _list[Argument]
    buildStatus: RoutineBuildStatus
    creationTime: str
    dataGovernanceType: typing.Literal[
        "DATA_GOVERNANCE_TYPE_UNSPECIFIED", "DATA_MASKING"
    ]
    definitionBody: str
    description: str
    determinismLevel: typing.Literal[
        "DETERMINISM_LEVEL_UNSPECIFIED", "DETERMINISTIC", "NOT_DETERMINISTIC"
    ]
    etag: str
    externalRuntimeOptions: ExternalRuntimeOptions
    importedLibraries: _list[str]
    language: typing.Literal[
        "LANGUAGE_UNSPECIFIED", "SQL", "JAVASCRIPT", "PYTHON", "JAVA", "SCALA"
    ]
    lastModifiedTime: str
    pythonOptions: PythonOptions
    remoteFunctionOptions: RemoteFunctionOptions
    returnTableType: StandardSqlTableType
    returnType: StandardSqlDataType
    routineReference: RoutineReference
    routineType: typing.Literal[
        "ROUTINE_TYPE_UNSPECIFIED",
        "SCALAR_FUNCTION",
        "PROCEDURE",
        "TABLE_VALUED_FUNCTION",
        "AGGREGATE_FUNCTION",
    ]
    securityMode: typing.Literal["SECURITY_MODE_UNSPECIFIED", "DEFINER", "INVOKER"]
    sparkOptions: SparkOptions
    strictMode: bool

@typing.type_check_only
class RoutineBuildStatus(typing.TypedDict, total=False):
    buildDuration: str
    buildState: typing.Literal[
        "BUILD_STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"
    ]
    buildStateUpdateTime: str
    errorResult: ErrorProto
    imageSizeBytes: str

@typing.type_check_only
class RoutineReference(typing.TypedDict, total=False):
    datasetId: str
    projectId: str
    routineId: str

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    actualLabel: str
    entries: _list[Entry]

@typing.type_check_only
class RowAccessPolicy(typing.TypedDict, total=False):
    creationTime: str
    etag: str
    filterPredicate: str
    grantees: _list[str]
    lastModifiedTime: str
    rowAccessPolicyReference: RowAccessPolicyReference

@typing.type_check_only
class RowAccessPolicyReference(typing.TypedDict, total=False):
    datasetId: str
    policyId: str
    projectId: str
    tableId: str

@typing.type_check_only
class RowLevelSecurityStatistics(typing.TypedDict, total=False):
    rowLevelSecurityApplied: bool

@typing.type_check_only
class ScriptOptions(typing.TypedDict, total=False):
    keyResultStatement: typing.Literal[
        "KEY_RESULT_STATEMENT_KIND_UNSPECIFIED", "LAST", "FIRST_SELECT"
    ]
    statementByteBudget: str
    statementTimeoutMs: str

@typing.type_check_only
class ScriptStackFrame(typing.TypedDict, total=False):
    endColumn: int
    endLine: int
    procedureId: str
    startColumn: int
    startLine: int
    text: str

@typing.type_check_only
class ScriptStatistics(typing.TypedDict, total=False):
    evaluationKind: typing.Literal[
        "EVALUATION_KIND_UNSPECIFIED", "STATEMENT", "EXPRESSION"
    ]
    stackFrames: _list[ScriptStackFrame]

@typing.type_check_only
class SearchStatistics(typing.TypedDict, total=False):
    indexPruningStats: _list[IndexPruningStats]
    indexUnusedReasons: _list[IndexUnusedReason]
    indexUsageMode: typing.Literal[
        "INDEX_USAGE_MODE_UNSPECIFIED", "UNUSED", "PARTIALLY_USED", "FULLY_USED"
    ]

@typing.type_check_only
class SerDeInfo(typing.TypedDict, total=False):
    name: str
    parameters: dict[str, typing.Any]
    serializationLibrary: str

@typing.type_check_only
class SessionInfo(typing.TypedDict, total=False):
    sessionId: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SkewSource(typing.TypedDict, total=False):
    outputBytesMax: str
    outputBytesMedian: str
    outputBytesP95: str
    stageId: str

@typing.type_check_only
class SnapshotDefinition(typing.TypedDict, total=False):
    baseTableReference: TableReference
    snapshotTime: str

@typing.type_check_only
class SparkLoggingInfo(typing.TypedDict, total=False):
    projectId: str
    resourceType: str

@typing.type_check_only
class SparkOptions(typing.TypedDict, total=False):
    archiveUris: _list[str]
    connection: str
    containerImage: str
    fileUris: _list[str]
    jarUris: _list[str]
    mainClass: str
    mainFileUri: str
    properties: dict[str, typing.Any]
    pyFileUris: _list[str]
    runtimeVersion: str

@typing.type_check_only
class SparkStatistics(typing.TypedDict, total=False):
    endpoints: dict[str, typing.Any]
    gcsStagingBucket: str
    kmsKeyName: str
    loggingInfo: SparkLoggingInfo
    sparkJobId: str
    sparkJobLocation: str

@typing.type_check_only
class StagePerformanceChangeInsight(typing.TypedDict, total=False):
    inputDataChange: InputDataChange
    stageId: str

@typing.type_check_only
class StagePerformanceStandaloneInsight(typing.TypedDict, total=False):
    biEngineReasons: _list[BiEngineReason]
    highCardinalityJoins: _list[HighCardinalityJoin]
    insufficientShuffleQuota: bool
    partitionSkew: PartitionSkew
    slotContention: bool
    stageId: str

@typing.type_check_only
class StandardSqlDataType(typing.TypedDict, total=False):
    arrayElementType: StandardSqlDataType
    rangeElementType: StandardSqlDataType
    structType: StandardSqlStructType
    typeKind: typing.Literal[
        "TYPE_KIND_UNSPECIFIED",
        "INT64",
        "BOOL",
        "FLOAT64",
        "STRING",
        "BYTES",
        "TIMESTAMP",
        "DATE",
        "TIME",
        "DATETIME",
        "INTERVAL",
        "GEOGRAPHY",
        "NUMERIC",
        "BIGNUMERIC",
        "JSON",
        "ARRAY",
        "STRUCT",
        "RANGE",
    ]

@typing.type_check_only
class StandardSqlField(typing.TypedDict, total=False):
    name: str
    type: StandardSqlDataType

@typing.type_check_only
class StandardSqlStructType(typing.TypedDict, total=False):
    fields: _list[StandardSqlField]

@typing.type_check_only
class StandardSqlTableType(typing.TypedDict, total=False):
    columns: _list[StandardSqlField]

@typing.type_check_only
class StorageDescriptor(typing.TypedDict, total=False):
    inputFormat: str
    locationUri: str
    outputFormat: str
    serdeInfo: SerDeInfo

@typing.type_check_only
class StoredColumnsUnusedReason(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED",
        "STORED_COLUMNS_COVER_INSUFFICIENT",
        "BASE_TABLE_HAS_RLS",
        "BASE_TABLE_HAS_CLS",
        "UNSUPPORTED_PREFILTER",
        "INTERNAL_ERROR",
        "OTHER_REASON",
    ]
    message: str
    uncoveredColumns: _list[str]

@typing.type_check_only
class StoredColumnsUsage(typing.TypedDict, total=False):
    baseTable: TableReference
    isQueryAccelerated: bool
    storedColumnsUnusedReasons: _list[StoredColumnsUnusedReason]

@typing.type_check_only
class Streamingbuffer(typing.TypedDict, total=False):
    estimatedBytes: str
    estimatedRows: str
    oldestEntryTime: str

@typing.type_check_only
class StringHparamSearchSpace(typing.TypedDict, total=False):
    candidates: _list[str]

@typing.type_check_only
class SystemVariables(typing.TypedDict, total=False):
    types: dict[str, typing.Any]
    values: dict[str, typing.Any]

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    biglakeConfiguration: BigLakeConfiguration
    cloneDefinition: CloneDefinition
    clustering: Clustering
    creationTime: str
    defaultCollation: str
    defaultRoundingMode: typing.Literal[
        "ROUNDING_MODE_UNSPECIFIED", "ROUND_HALF_AWAY_FROM_ZERO", "ROUND_HALF_EVEN"
    ]
    description: str
    encryptionConfiguration: EncryptionConfiguration
    etag: str
    expirationTime: str
    externalCatalogTableOptions: ExternalCatalogTableOptions
    externalDataConfiguration: ExternalDataConfiguration
    friendlyName: str
    id: str
    kind: str
    labels: dict[str, typing.Any]
    lastModifiedTime: str
    location: str
    managedTableType: typing.Literal[
        "MANAGED_TABLE_TYPE_UNSPECIFIED", "NATIVE", "BIGLAKE"
    ]
    materializedView: MaterializedViewDefinition
    materializedViewStatus: MaterializedViewStatus
    maxStaleness: str
    model: ModelDefinition
    numActiveLogicalBytes: str
    numActivePhysicalBytes: str
    numBytes: str
    numCurrentPhysicalBytes: str
    numLongTermBytes: str
    numLongTermLogicalBytes: str
    numLongTermPhysicalBytes: str
    numPartitions: str
    numPhysicalBytes: str
    numRows: str
    numTimeTravelPhysicalBytes: str
    numTotalLogicalBytes: str
    numTotalPhysicalBytes: str
    partitionDefinition: PartitioningDefinition
    rangePartitioning: RangePartitioning
    replicas: _list[TableReference]
    requirePartitionFilter: bool
    resourceTags: dict[str, typing.Any]
    restrictions: RestrictionConfig
    schema: TableSchema
    selfLink: str
    snapshotDefinition: SnapshotDefinition
    streamingBuffer: Streamingbuffer
    tableConstraints: TableConstraints
    tableReference: TableReference
    tableReplicationInfo: TableReplicationInfo
    timePartitioning: TimePartitioning
    type: str
    view: ViewDefinition

@typing.type_check_only
class TableCell(typing.TypedDict, total=False):
    v: typing.Any

@typing.type_check_only
class TableChangeInsight(typing.TypedDict, total=False):
    metadataCacheNotUsedButUsedPreviously: bool
    metadataCacheStalenessInsight: MetadataCacheStalenessInsight
    tableReference: TableReference

@typing.type_check_only
class TableConstraints(typing.TypedDict, total=False):
    foreignKeys: _list[dict[str, typing.Any]]
    primaryKey: dict[str, typing.Any]

@typing.type_check_only
class TableDataInsertAllRequest(typing.TypedDict, total=False):
    ignoreUnknownValues: bool
    kind: str
    rows: _list[dict[str, typing.Any]]
    skipInvalidRows: bool
    templateSuffix: str
    traceId: str

@typing.type_check_only
class TableDataInsertAllResponse(typing.TypedDict, total=False):
    insertErrors: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class TableDataList(typing.TypedDict, total=False):
    etag: str
    kind: str
    pageToken: str
    rows: _list[TableRow]
    totalRows: str

@typing.type_check_only
class TableFieldSchema(typing.TypedDict, total=False):
    categories: dict[str, typing.Any]
    collation: str
    dataGovernanceTagsInfo: dict[str, typing.Any]
    dataPolicies: _list[DataPolicyOption]
    dataPolicyList: DataPolicyList
    defaultValueExpression: str
    description: str
    fields: _list[TableFieldSchema]
    foreignTypeDefinition: str
    generatedColumn: GeneratedColumn
    maxLength: str
    mode: str
    name: str
    policyTags: dict[str, typing.Any]
    precision: str
    rangeElementType: dict[str, typing.Any]
    roundingMode: typing.Literal[
        "ROUNDING_MODE_UNSPECIFIED", "ROUND_HALF_AWAY_FROM_ZERO", "ROUND_HALF_EVEN"
    ]
    scale: str
    timestampPrecision: str
    type: str

@typing.type_check_only
class TableList(typing.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    tables: _list[dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class TableMetadataCacheUsage(typing.TypedDict, total=False):
    explanation: str
    pruningStats: PruningStats
    staleness: str
    tableReference: TableReference
    tableType: str
    unusedReason: typing.Literal[
        "UNUSED_REASON_UNSPECIFIED",
        "EXCEEDED_MAX_STALENESS",
        "METADATA_CACHING_NOT_ENABLED",
        "OTHER_REASON",
    ]

@typing.type_check_only
class TableReference(typing.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class TableReplicationInfo(typing.TypedDict, total=False):
    replicatedSourceLastRefreshTime: str
    replicationError: ErrorProto
    replicationIntervalMs: str
    replicationStatus: typing.Literal[
        "REPLICATION_STATUS_UNSPECIFIED",
        "ACTIVE",
        "SOURCE_DELETED",
        "PERMISSION_DENIED",
        "UNSUPPORTED_CONFIGURATION",
    ]
    sourceTable: TableReference

@typing.type_check_only
class TableRow(typing.TypedDict, total=False):
    f: _list[TableCell]

@typing.type_check_only
class TableSchema(typing.TypedDict, total=False):
    fields: _list[TableFieldSchema]
    foreignTypeInfo: ForeignTypeInfo

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimePartitioning(typing.TypedDict, total=False):
    expirationMs: str
    field: str
    requirePartitionFilter: bool
    type: str

@typing.type_check_only
class TrainingOptions(typing.TypedDict, total=False):
    activationFn: str
    adjustStepChanges: bool
    approxGlobalFeatureContrib: bool
    autoArima: bool
    autoArimaMaxOrder: str
    autoArimaMinOrder: str
    autoClassWeights: bool
    batchSize: str
    boosterType: typing.Literal["BOOSTER_TYPE_UNSPECIFIED", "GBTREE", "DART"]
    budgetHours: float
    calculatePValues: bool
    categoryEncodingMethod: typing.Literal[
        "ENCODING_METHOD_UNSPECIFIED",
        "ONE_HOT_ENCODING",
        "LABEL_ENCODING",
        "DUMMY_ENCODING",
    ]
    cleanSpikesAndDips: bool
    colorSpace: typing.Literal[
        "COLOR_SPACE_UNSPECIFIED", "RGB", "HSV", "YIQ", "YUV", "GRAYSCALE"
    ]
    colsampleBylevel: float
    colsampleBynode: float
    colsampleBytree: float
    contributionMetric: str
    dartNormalizeType: typing.Literal[
        "DART_NORMALIZE_TYPE_UNSPECIFIED", "TREE", "FOREST"
    ]
    dataFrequency: typing.Literal[
        "DATA_FREQUENCY_UNSPECIFIED",
        "AUTO_FREQUENCY",
        "YEARLY",
        "QUARTERLY",
        "MONTHLY",
        "WEEKLY",
        "DAILY",
        "HOURLY",
        "PER_MINUTE",
    ]
    dataSplitColumn: str
    dataSplitEvalFraction: float
    dataSplitMethod: typing.Literal[
        "DATA_SPLIT_METHOD_UNSPECIFIED",
        "RANDOM",
        "CUSTOM",
        "SEQUENTIAL",
        "NO_SPLIT",
        "AUTO_SPLIT",
    ]
    decomposeTimeSeries: bool
    dimensionIdColumns: _list[str]
    distanceType: typing.Literal["DISTANCE_TYPE_UNSPECIFIED", "EUCLIDEAN", "COSINE"]
    dropout: float
    earlyStop: bool
    enableGlobalExplain: bool
    endpointIdleTtl: str
    feedbackType: typing.Literal["FEEDBACK_TYPE_UNSPECIFIED", "IMPLICIT", "EXPLICIT"]
    fitIntercept: bool
    forecastLimitLowerBound: float
    forecastLimitUpperBound: float
    hiddenUnits: _list[str]
    holidayRegion: typing.Literal[
        "HOLIDAY_REGION_UNSPECIFIED",
        "GLOBAL",
        "NA",
        "JAPAC",
        "EMEA",
        "LAC",
        "AE",
        "AR",
        "AT",
        "AU",
        "BE",
        "BR",
        "CA",
        "CH",
        "CL",
        "CN",
        "CO",
        "CS",
        "CZ",
        "DE",
        "DK",
        "DZ",
        "EC",
        "EE",
        "EG",
        "ES",
        "FI",
        "FR",
        "GB",
        "GR",
        "HK",
        "HU",
        "ID",
        "IE",
        "IL",
        "IN",
        "IR",
        "IT",
        "JP",
        "KR",
        "LV",
        "MA",
        "MX",
        "MY",
        "NG",
        "NL",
        "NO",
        "NZ",
        "PE",
        "PH",
        "PK",
        "PL",
        "PT",
        "RO",
        "RS",
        "RU",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "TH",
        "TR",
        "TW",
        "UA",
        "US",
        "VE",
        "VN",
        "ZA",
    ]
    holidayRegions: _list[
        typing.Literal[
            "HOLIDAY_REGION_UNSPECIFIED",
            "GLOBAL",
            "NA",
            "JAPAC",
            "EMEA",
            "LAC",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BR",
            "CA",
            "CH",
            "CL",
            "CN",
            "CO",
            "CS",
            "CZ",
            "DE",
            "DK",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "HK",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IR",
            "IT",
            "JP",
            "KR",
            "LV",
            "MA",
            "MX",
            "MY",
            "NG",
            "NL",
            "NO",
            "NZ",
            "PE",
            "PH",
            "PK",
            "PL",
            "PT",
            "RO",
            "RS",
            "RU",
            "SA",
            "SE",
            "SG",
            "SI",
            "SK",
            "TH",
            "TR",
            "TW",
            "UA",
            "US",
            "VE",
            "VN",
            "ZA",
        ]
    ]
    horizon: str
    hparamTuningObjectives: _list[
        typing.Literal[
            "HPARAM_TUNING_OBJECTIVE_UNSPECIFIED",
            "MEAN_ABSOLUTE_ERROR",
            "MEAN_SQUARED_ERROR",
            "MEAN_SQUARED_LOG_ERROR",
            "MEDIAN_ABSOLUTE_ERROR",
            "R_SQUARED",
            "EXPLAINED_VARIANCE",
            "PRECISION",
            "RECALL",
            "ACCURACY",
            "F1_SCORE",
            "LOG_LOSS",
            "ROC_AUC",
            "DAVIES_BOULDIN_INDEX",
            "MEAN_AVERAGE_PRECISION",
            "NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN",
            "AVERAGE_RANK",
        ]
    ]
    huggingFaceModelId: str
    includeDrift: bool
    initialLearnRate: float
    inputLabelColumns: _list[str]
    instanceWeightColumn: str
    integratedGradientsNumSteps: str
    isTestColumn: str
    itemColumn: str
    kmeansInitializationColumn: str
    kmeansInitializationMethod: typing.Literal[
        "KMEANS_INITIALIZATION_METHOD_UNSPECIFIED",
        "RANDOM",
        "CUSTOM",
        "KMEANS_PLUS_PLUS",
    ]
    l1RegActivation: float
    l1Regularization: float
    l2Regularization: float
    labelClassWeights: dict[str, typing.Any]
    learnRate: float
    learnRateStrategy: typing.Literal[
        "LEARN_RATE_STRATEGY_UNSPECIFIED", "LINE_SEARCH", "CONSTANT"
    ]
    lossType: typing.Literal[
        "LOSS_TYPE_UNSPECIFIED", "MEAN_SQUARED_LOSS", "MEAN_LOG_LOSS"
    ]
    machineType: str
    maxIterations: str
    maxParallelTrials: str
    maxReplicaCount: str
    maxTimeSeriesLength: str
    maxTreeDepth: str
    minAprioriSupport: float
    minRelativeProgress: float
    minReplicaCount: str
    minSplitLoss: float
    minTimeSeriesLength: str
    minTreeChildWeight: str
    modelGardenModelName: str
    modelRegistry: typing.Literal["MODEL_REGISTRY_UNSPECIFIED", "VERTEX_AI"]
    modelUri: str
    nonSeasonalOrder: ArimaOrder
    numClusters: str
    numFactors: str
    numParallelTree: str
    numPrincipalComponents: str
    numTrials: str
    optimizationStrategy: typing.Literal[
        "OPTIMIZATION_STRATEGY_UNSPECIFIED", "BATCH_GRADIENT_DESCENT", "NORMAL_EQUATION"
    ]
    optimizer: str
    pcaExplainedVarianceRatio: float
    pcaSolver: typing.Literal["UNSPECIFIED", "FULL", "RANDOMIZED", "AUTO"]
    reservationAffinityKey: str
    reservationAffinityType: typing.Literal[
        "RESERVATION_AFFINITY_TYPE_UNSPECIFIED",
        "NO_RESERVATION",
        "ANY_RESERVATION",
        "SPECIFIC_RESERVATION",
    ]
    reservationAffinityValues: _list[str]
    sampledShapleyNumPaths: str
    scaleFeatures: bool
    standardizeFeatures: bool
    subsample: float
    tfVersion: str
    timeSeriesDataColumn: str
    timeSeriesIdColumn: str
    timeSeriesIdColumns: _list[str]
    timeSeriesLengthFraction: float
    timeSeriesTimestampColumn: str
    treeMethod: typing.Literal[
        "TREE_METHOD_UNSPECIFIED", "AUTO", "EXACT", "APPROX", "HIST"
    ]
    trendSmoothingWindowSize: str
    userColumn: str
    vertexAiModelVersionAliases: _list[str]
    walsAlpha: float
    warmStart: bool
    xgboostVersion: str

@typing.type_check_only
class TrainingRun(typing.TypedDict, total=False):
    classLevelGlobalExplanations: _list[GlobalExplanation]
    dataSplitResult: DataSplitResult
    evaluationMetrics: EvaluationMetrics
    modelLevelGlobalExplanation: GlobalExplanation
    results: _list[IterationResult]
    startTime: str
    trainingOptions: TrainingOptions
    trainingStartTime: str
    vertexAiModelId: str
    vertexAiModelVersion: str

@typing.type_check_only
class TransactionInfo(typing.TypedDict, total=False):
    transactionId: str

@typing.type_check_only
class TransformColumn(typing.TypedDict, total=False):
    name: str
    transformSql: str
    type: StandardSqlDataType

@typing.type_check_only
class UndeleteDatasetRequest(typing.TypedDict, total=False):
    deletionTime: str

@typing.type_check_only
class UserDefinedFunctionResource(typing.TypedDict, total=False):
    inlineCode: str
    resourceUri: str

@typing.type_check_only
class VectorSearchStatistics(typing.TypedDict, total=False):
    indexUnusedReasons: _list[IndexUnusedReason]
    indexUsageMode: typing.Literal[
        "INDEX_USAGE_MODE_UNSPECIFIED", "UNUSED", "PARTIALLY_USED", "FULLY_USED"
    ]
    storedColumnsUsages: _list[StoredColumnsUsage]

@typing.type_check_only
class ViewDefinition(typing.TypedDict, total=False):
    foreignDefinitions: _list[ForeignViewDefinition]
    privacyPolicy: PrivacyPolicy
    query: str
    useExplicitColumnNames: bool
    useLegacySql: bool
    userDefinedFunctionResources: _list[UserDefinedFunctionResource]
