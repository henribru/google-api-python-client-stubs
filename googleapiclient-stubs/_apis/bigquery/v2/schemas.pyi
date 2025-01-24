import typing

import typing_extensions

_list = list

@typing.type_check_only
class AggregateClassificationMetrics(typing_extensions.TypedDict, total=False):
    accuracy: float
    f1Score: float
    logLoss: float
    precision: float
    recall: float
    rocAuc: float
    threshold: float

@typing.type_check_only
class AggregationThresholdPolicy(typing_extensions.TypedDict, total=False):
    privacyUnitColumns: _list[str]
    threshold: str

@typing.type_check_only
class Argument(typing_extensions.TypedDict, total=False):
    argumentKind: typing_extensions.Literal[
        "ARGUMENT_KIND_UNSPECIFIED", "FIXED_TYPE", "ANY_TYPE"
    ]
    dataType: StandardSqlDataType
    isAggregate: bool
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "IN", "OUT", "INOUT"]
    name: str

@typing.type_check_only
class ArimaCoefficients(typing_extensions.TypedDict, total=False):
    autoRegressiveCoefficients: _list[float]
    interceptCoefficient: float
    movingAverageCoefficients: _list[float]

@typing.type_check_only
class ArimaFittingMetrics(typing_extensions.TypedDict, total=False):
    aic: float
    logLikelihood: float
    variance: float

@typing.type_check_only
class ArimaForecastingMetrics(typing_extensions.TypedDict, total=False):
    arimaFittingMetrics: _list[ArimaFittingMetrics]
    arimaSingleModelForecastingMetrics: _list[ArimaSingleModelForecastingMetrics]
    hasDrift: _list[bool]
    nonSeasonalOrder: _list[ArimaOrder]
    seasonalPeriods: _list[
        typing_extensions.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
        ]
    ]
    timeSeriesId: _list[str]

@typing.type_check_only
class ArimaModelInfo(typing_extensions.TypedDict, total=False):
    arimaCoefficients: ArimaCoefficients
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    hasHolidayEffect: bool
    hasSpikesAndDips: bool
    hasStepChanges: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: _list[
        typing_extensions.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
        ]
    ]
    timeSeriesId: str
    timeSeriesIds: _list[str]

@typing.type_check_only
class ArimaOrder(typing_extensions.TypedDict, total=False):
    d: str
    p: str
    q: str

@typing.type_check_only
class ArimaResult(typing_extensions.TypedDict, total=False):
    arimaModelInfo: _list[ArimaModelInfo]
    seasonalPeriods: _list[
        typing_extensions.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
        ]
    ]

@typing.type_check_only
class ArimaSingleModelForecastingMetrics(typing_extensions.TypedDict, total=False):
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    hasHolidayEffect: bool
    hasSpikesAndDips: bool
    hasStepChanges: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: _list[
        typing_extensions.Literal[
            "SEASONAL_PERIOD_TYPE_UNSPECIFIED",
            "NO_SEASONALITY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "QUARTERLY",
            "YEARLY",
        ]
    ]
    timeSeriesId: str
    timeSeriesIds: _list[str]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AvroOptions(typing_extensions.TypedDict, total=False):
    useAvroLogicalTypes: bool

@typing.type_check_only
class BiEngineReason(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
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
class BiEngineStatistics(typing_extensions.TypedDict, total=False):
    accelerationMode: typing_extensions.Literal[
        "BI_ENGINE_ACCELERATION_MODE_UNSPECIFIED",
        "BI_ENGINE_DISABLED",
        "PARTIAL_INPUT",
        "FULL_INPUT",
        "FULL_QUERY",
    ]
    biEngineMode: typing_extensions.Literal[
        "ACCELERATION_MODE_UNSPECIFIED", "DISABLED", "PARTIAL", "FULL"
    ]
    biEngineReasons: _list[BiEngineReason]

@typing.type_check_only
class BigLakeConfiguration(typing_extensions.TypedDict, total=False):
    connectionId: str
    fileFormat: typing_extensions.Literal["FILE_FORMAT_UNSPECIFIED", "PARQUET"]
    storageUri: str
    tableFormat: typing_extensions.Literal["TABLE_FORMAT_UNSPECIFIED", "ICEBERG"]

@typing.type_check_only
class BigQueryModelTraining(typing_extensions.TypedDict, total=False):
    currentIteration: int
    expectedTotalIterations: str

@typing.type_check_only
class BigtableColumn(typing_extensions.TypedDict, total=False):
    encoding: str
    fieldName: str
    onlyReadLatest: bool
    qualifierEncoded: str
    qualifierString: str
    type: str

@typing.type_check_only
class BigtableColumnFamily(typing_extensions.TypedDict, total=False):
    columns: _list[BigtableColumn]
    encoding: str
    familyId: str
    onlyReadLatest: bool
    type: str

@typing.type_check_only
class BigtableOptions(typing_extensions.TypedDict, total=False):
    columnFamilies: _list[BigtableColumnFamily]
    ignoreUnspecifiedColumnFamilies: bool
    outputColumnFamiliesAsJson: bool
    readRowkeyAsString: bool

@typing.type_check_only
class BinaryClassificationMetrics(typing_extensions.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    binaryConfusionMatrixList: _list[BinaryConfusionMatrix]
    negativeLabel: str
    positiveLabel: str

@typing.type_check_only
class BinaryConfusionMatrix(typing_extensions.TypedDict, total=False):
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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BqmlIterationResult(typing_extensions.TypedDict, total=False):
    durationMs: str
    evalLoss: float
    index: int
    learnRate: float
    trainingLoss: float

@typing.type_check_only
class BqmlTrainingRun(typing_extensions.TypedDict, total=False):
    iterationResults: _list[BqmlIterationResult]
    startTime: str
    state: str
    trainingOptions: dict[str, typing.Any]

@typing.type_check_only
class CategoricalValue(typing_extensions.TypedDict, total=False):
    categoryCounts: _list[CategoryCount]

@typing.type_check_only
class CategoryCount(typing_extensions.TypedDict, total=False):
    category: str
    count: str

@typing.type_check_only
class CloneDefinition(typing_extensions.TypedDict, total=False):
    baseTableReference: TableReference
    cloneTime: str

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    centroidId: str
    count: str
    featureValues: _list[FeatureValue]

@typing.type_check_only
class ClusterInfo(typing_extensions.TypedDict, total=False):
    centroidId: str
    clusterRadius: float
    clusterSize: str

@typing.type_check_only
class Clustering(typing_extensions.TypedDict, total=False):
    fields: _list[str]

@typing.type_check_only
class ClusteringMetrics(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    daviesBouldinIndex: float
    meanSquaredDistance: float

@typing.type_check_only
class ConfusionMatrix(typing_extensions.TypedDict, total=False):
    confidenceThreshold: float
    rows: _list[Row]

@typing.type_check_only
class ConnectionProperty(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class CsvOptions(typing_extensions.TypedDict, total=False):
    allowJaggedRows: bool
    allowQuotedNewlines: bool
    encoding: str
    fieldDelimiter: str
    nullMarker: str
    preserveAsciiControlCharacters: bool
    quote: str
    skipLeadingRows: str

@typing.type_check_only
class DataFormatOptions(typing_extensions.TypedDict, total=False):
    useInt64Timestamp: bool

@typing.type_check_only
class DataMaskingStatistics(typing_extensions.TypedDict, total=False):
    dataMaskingApplied: bool

@typing.type_check_only
class DataPolicyOption(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class DataSplitResult(typing_extensions.TypedDict, total=False):
    evaluationTable: TableReference
    testTable: TableReference
    trainingTable: TableReference

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    access: _list[dict[str, typing.Any]]
    creationTime: str
    datasetReference: DatasetReference
    defaultCollation: str
    defaultEncryptionConfiguration: EncryptionConfiguration
    defaultPartitionExpirationMs: str
    defaultRoundingMode: typing_extensions.Literal[
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
    storageBillingModel: typing_extensions.Literal[
        "STORAGE_BILLING_MODEL_UNSPECIFIED", "LOGICAL", "PHYSICAL"
    ]
    tags: _list[dict[str, typing.Any]]
    type: str

@typing.type_check_only
class DatasetAccessEntry(typing_extensions.TypedDict, total=False):
    dataset: DatasetReference
    targetTypes: _list[
        typing_extensions.Literal["TARGET_TYPE_UNSPECIFIED", "VIEWS", "ROUTINES"]
    ]

@typing.type_check_only
class DatasetList(typing_extensions.TypedDict, total=False):
    datasets: _list[dict[str, typing.Any]]
    etag: str
    kind: str
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class DatasetReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str

@typing.type_check_only
class DestinationTableProperties(typing_extensions.TypedDict, total=False):
    description: str
    expirationTime: str
    friendlyName: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class DifferentialPrivacyPolicy(typing_extensions.TypedDict, total=False):
    deltaBudget: float
    deltaBudgetRemaining: float
    deltaPerQuery: float
    epsilonBudget: float
    epsilonBudgetRemaining: float
    maxEpsilonPerQuery: float
    maxGroupsContributed: str
    privacyUnitColumn: str

@typing.type_check_only
class DimensionalityReductionMetrics(typing_extensions.TypedDict, total=False):
    totalExplainedVarianceRatio: float

@typing.type_check_only
class DmlStatistics(typing_extensions.TypedDict, total=False):
    deletedRowCount: str
    insertedRowCount: str
    updatedRowCount: str

@typing.type_check_only
class DoubleCandidates(typing_extensions.TypedDict, total=False):
    candidates: _list[float]

@typing.type_check_only
class DoubleHparamSearchSpace(typing_extensions.TypedDict, total=False):
    candidates: DoubleCandidates
    range: DoubleRange

@typing.type_check_only
class DoubleRange(typing_extensions.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class EncryptionConfiguration(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class Entry(typing_extensions.TypedDict, total=False):
    itemCount: str
    predictedLabel: str

@typing.type_check_only
class ErrorProto(typing_extensions.TypedDict, total=False):
    debugInfo: str
    location: str
    message: str
    reason: str

@typing.type_check_only
class EvaluationMetrics(typing_extensions.TypedDict, total=False):
    arimaForecastingMetrics: ArimaForecastingMetrics
    binaryClassificationMetrics: BinaryClassificationMetrics
    clusteringMetrics: ClusteringMetrics
    dimensionalityReductionMetrics: DimensionalityReductionMetrics
    multiClassClassificationMetrics: MultiClassClassificationMetrics
    rankingMetrics: RankingMetrics
    regressionMetrics: RegressionMetrics

@typing.type_check_only
class ExplainQueryStage(typing_extensions.TypedDict, total=False):
    completedParallelInputs: str
    computeMode: typing_extensions.Literal[
        "COMPUTE_MODE_UNSPECIFIED", "BIGQUERY", "BI_ENGINE"
    ]
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
class ExplainQueryStep(typing_extensions.TypedDict, total=False):
    kind: str
    substeps: _list[str]

@typing.type_check_only
class Explanation(typing_extensions.TypedDict, total=False):
    attribution: float
    featureName: str

@typing.type_check_only
class ExportDataStatistics(typing_extensions.TypedDict, total=False):
    fileCount: str
    rowCount: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalCatalogDatasetOptions(typing_extensions.TypedDict, total=False):
    defaultStorageLocationUri: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class ExternalCatalogTableOptions(typing_extensions.TypedDict, total=False):
    connectionId: str
    parameters: dict[str, typing.Any]
    storageDescriptor: StorageDescriptor

@typing.type_check_only
class ExternalDataConfiguration(typing_extensions.TypedDict, total=False):
    autodetect: bool
    avroOptions: AvroOptions
    bigtableOptions: BigtableOptions
    compression: str
    connectionId: str
    csvOptions: CsvOptions
    decimalTargetTypes: _list[
        typing_extensions.Literal[
            "DECIMAL_TARGET_TYPE_UNSPECIFIED", "NUMERIC", "BIGNUMERIC", "STRING"
        ]
    ]
    fileSetSpecType: typing_extensions.Literal[
        "FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH",
        "FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST",
    ]
    googleSheetsOptions: GoogleSheetsOptions
    hivePartitioningOptions: HivePartitioningOptions
    ignoreUnknownValues: bool
    jsonExtension: typing_extensions.Literal["JSON_EXTENSION_UNSPECIFIED", "GEOJSON"]
    jsonOptions: JsonOptions
    maxBadRecords: int
    metadataCacheMode: typing_extensions.Literal[
        "METADATA_CACHE_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    objectMetadata: typing_extensions.Literal[
        "OBJECT_METADATA_UNSPECIFIED", "DIRECTORY", "SIMPLE"
    ]
    parquetOptions: ParquetOptions
    referenceFileSchemaUri: str
    schema: TableSchema
    sourceFormat: str
    sourceUris: _list[str]

@typing.type_check_only
class ExternalDatasetReference(typing_extensions.TypedDict, total=False):
    connection: str
    externalSource: str

@typing.type_check_only
class ExternalServiceCost(typing_extensions.TypedDict, total=False):
    bytesBilled: str
    bytesProcessed: str
    externalService: str
    reservedSlotCount: str
    slotMs: str

@typing.type_check_only
class FeatureValue(typing_extensions.TypedDict, total=False):
    categoricalValue: CategoricalValue
    featureColumn: str
    numericalValue: float

@typing.type_check_only
class ForeignTypeInfo(typing_extensions.TypedDict, total=False):
    typeSystem: typing_extensions.Literal["TYPE_SYSTEM_UNSPECIFIED", "HIVE"]

@typing.type_check_only
class ForeignViewDefinition(typing_extensions.TypedDict, total=False):
    dialect: str
    query: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GetQueryResultsResponse(typing_extensions.TypedDict, total=False):
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
class GetServiceAccountResponse(typing_extensions.TypedDict, total=False):
    email: str
    kind: str

@typing.type_check_only
class GlobalExplanation(typing_extensions.TypedDict, total=False):
    classLabel: str
    explanations: _list[Explanation]

@typing.type_check_only
class GoogleSheetsOptions(typing_extensions.TypedDict, total=False):
    range: str
    skipLeadingRows: str

@typing.type_check_only
class HighCardinalityJoin(typing_extensions.TypedDict, total=False):
    leftRows: str
    outputRows: str
    rightRows: str
    stepIndex: int

@typing.type_check_only
class HivePartitioningOptions(typing_extensions.TypedDict, total=False):
    fields: _list[str]
    mode: str
    requirePartitionFilter: bool
    sourceUriPrefix: str

@typing.type_check_only
class HparamSearchSpaces(typing_extensions.TypedDict, total=False):
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
class HparamTuningTrial(typing_extensions.TypedDict, total=False):
    endTimeMs: str
    errorMessage: str
    evalLoss: float
    evaluationMetrics: EvaluationMetrics
    hparamTuningEvaluationMetrics: EvaluationMetrics
    hparams: TrainingOptions
    startTimeMs: str
    status: typing_extensions.Literal[
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
class IndexUnusedReason(typing_extensions.TypedDict, total=False):
    baseTable: TableReference
    code: typing_extensions.Literal[
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
class InputDataChange(typing_extensions.TypedDict, total=False):
    recordsReadDiffPercentage: float

@typing.type_check_only
class IntArray(typing_extensions.TypedDict, total=False):
    elements: _list[str]

@typing.type_check_only
class IntArrayHparamSearchSpace(typing_extensions.TypedDict, total=False):
    candidates: _list[IntArray]

@typing.type_check_only
class IntCandidates(typing_extensions.TypedDict, total=False):
    candidates: _list[str]

@typing.type_check_only
class IntHparamSearchSpace(typing_extensions.TypedDict, total=False):
    candidates: IntCandidates
    range: IntRange

@typing.type_check_only
class IntRange(typing_extensions.TypedDict, total=False):
    max: str
    min: str

@typing.type_check_only
class IterationResult(typing_extensions.TypedDict, total=False):
    arimaResult: ArimaResult
    clusterInfos: _list[ClusterInfo]
    durationMs: str
    evalLoss: float
    index: int
    learnRate: float
    principalComponentInfos: _list[PrincipalComponentInfo]
    trainingLoss: float

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
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
class JobCancelResponse(typing_extensions.TypedDict, total=False):
    job: Job
    kind: str

@typing.type_check_only
class JobConfiguration(typing_extensions.TypedDict, total=False):
    copy: JobConfigurationTableCopy
    dryRun: bool
    extract: JobConfigurationExtract
    jobTimeoutMs: str
    jobType: str
    labels: dict[str, typing.Any]
    load: JobConfigurationLoad
    query: JobConfigurationQuery

@typing.type_check_only
class JobConfigurationExtract(typing_extensions.TypedDict, total=False):
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
class JobConfigurationLoad(typing_extensions.TypedDict, total=False):
    allowJaggedRows: bool
    allowQuotedNewlines: bool
    autodetect: bool
    clustering: Clustering
    columnNameCharacterMap: typing_extensions.Literal[
        "COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED", "STRICT", "V1", "V2"
    ]
    connectionProperties: _list[ConnectionProperty]
    copyFilesOnly: bool
    createDisposition: str
    createSession: bool
    decimalTargetTypes: _list[
        typing_extensions.Literal[
            "DECIMAL_TARGET_TYPE_UNSPECIFIED", "NUMERIC", "BIGNUMERIC", "STRING"
        ]
    ]
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationTable: TableReference
    destinationTableProperties: DestinationTableProperties
    encoding: str
    fieldDelimiter: str
    fileSetSpecType: typing_extensions.Literal[
        "FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH",
        "FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST",
    ]
    hivePartitioningOptions: HivePartitioningOptions
    ignoreUnknownValues: bool
    jsonExtension: typing_extensions.Literal["JSON_EXTENSION_UNSPECIFIED", "GEOJSON"]
    maxBadRecords: int
    nullMarker: str
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
    sourceFormat: str
    sourceUris: _list[str]
    timePartitioning: TimePartitioning
    useAvroLogicalTypes: bool
    writeDisposition: str

@typing.type_check_only
class JobConfigurationQuery(typing_extensions.TypedDict, total=False):
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

@typing.type_check_only
class JobConfigurationTableCopy(typing_extensions.TypedDict, total=False):
    createDisposition: str
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationExpirationTime: str
    destinationTable: TableReference
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "COPY", "SNAPSHOT", "RESTORE", "CLONE"
    ]
    sourceTable: TableReference
    sourceTables: _list[TableReference]
    writeDisposition: str

@typing.type_check_only
class JobCreationReason(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "REQUESTED", "LONG_RUNNING", "LARGE_RESULTS", "OTHER"
    ]

@typing.type_check_only
class JobList(typing_extensions.TypedDict, total=False):
    etag: str
    jobs: _list[dict[str, typing.Any]]
    kind: str
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class JobReference(typing_extensions.TypedDict, total=False):
    jobId: str
    location: str
    projectId: str

@typing.type_check_only
class JobStatistics(typing_extensions.TypedDict, total=False):
    completionRatio: float
    copy: JobStatistics5
    creationTime: str
    dataMaskingStatistics: DataMaskingStatistics
    edition: typing_extensions.Literal[
        "RESERVATION_EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    endTime: str
    extract: JobStatistics4
    finalExecutionDurationMs: str
    load: JobStatistics3
    numChildJobs: str
    parentJobId: str
    query: JobStatistics2
    quotaDeferments: _list[str]
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
class JobStatistics2(typing_extensions.TypedDict, total=False):
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
    loadQueryStatistics: LoadQueryStatistics
    materializedViewStatistics: MaterializedViewStatistics
    metadataCacheStatistics: MetadataCacheStatistics
    mlStatistics: MlStatistics
    modelTraining: BigQueryModelTraining
    modelTrainingCurrentIteration: int
    modelTrainingExpectedTotalIteration: str
    numDmlAffectedRows: str
    performanceInsights: PerformanceInsights
    queryInfo: QueryInfo
    queryPlan: _list[ExplainQueryStage]
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
    totalSlotMs: str
    transferredBytes: str
    undeclaredQueryParameters: _list[QueryParameter]
    vectorSearchStatistics: VectorSearchStatistics

@typing.type_check_only
class JobStatistics3(typing_extensions.TypedDict, total=False):
    badRecords: str
    inputFileBytes: str
    inputFiles: str
    outputBytes: str
    outputRows: str
    timeline: _list[QueryTimelineSample]

@typing.type_check_only
class JobStatistics4(typing_extensions.TypedDict, total=False):
    destinationUriFileCounts: _list[str]
    inputBytes: str
    timeline: _list[QueryTimelineSample]

@typing.type_check_only
class JobStatistics5(typing_extensions.TypedDict, total=False):
    copiedLogicalBytes: str
    copiedRows: str

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    errorResult: ErrorProto
    errors: _list[ErrorProto]
    state: str

@typing.type_check_only
class JoinRestrictionPolicy(typing_extensions.TypedDict, total=False):
    joinAllowedColumns: _list[str]
    joinCondition: typing_extensions.Literal[
        "JOIN_CONDITION_UNSPECIFIED",
        "JOIN_ANY",
        "JOIN_ALL",
        "JOIN_NOT_REQUIRED",
        "JOIN_BLOCKED",
    ]

@typing.type_check_only
class JsonObject(dict[str, typing.Any]): ...

@typing.type_check_only
class JsonOptions(typing_extensions.TypedDict, total=False):
    encoding: str

@typing.type_check_only
class JsonValue(dict[str, typing.Any]): ...

@typing.type_check_only
class LinkedDatasetMetadata(typing_extensions.TypedDict, total=False):
    linkState: typing_extensions.Literal["LINK_STATE_UNSPECIFIED", "LINKED", "UNLINKED"]

@typing.type_check_only
class LinkedDatasetSource(typing_extensions.TypedDict, total=False):
    sourceDataset: DatasetReference

@typing.type_check_only
class ListModelsResponse(typing_extensions.TypedDict, total=False):
    models: _list[Model]
    nextPageToken: str

@typing.type_check_only
class ListRoutinesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    routines: _list[Routine]

@typing.type_check_only
class ListRowAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rowAccessPolicies: _list[RowAccessPolicy]

@typing.type_check_only
class LoadQueryStatistics(typing_extensions.TypedDict, total=False):
    badRecords: str
    bytesTransferred: str
    inputFileBytes: str
    inputFiles: str
    outputBytes: str
    outputRows: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    legacyLocationId: str

@typing.type_check_only
class MaterializedView(typing_extensions.TypedDict, total=False):
    chosen: bool
    estimatedBytesSaved: str
    rejectedReason: typing_extensions.Literal[
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
class MaterializedViewDefinition(typing_extensions.TypedDict, total=False):
    allowNonIncrementalDefinition: bool
    enableRefresh: bool
    lastRefreshTime: str
    maxStaleness: str
    query: str
    refreshIntervalMs: str

@typing.type_check_only
class MaterializedViewStatistics(typing_extensions.TypedDict, total=False):
    materializedView: _list[MaterializedView]

@typing.type_check_only
class MaterializedViewStatus(typing_extensions.TypedDict, total=False):
    lastRefreshStatus: ErrorProto
    refreshWatermark: str

@typing.type_check_only
class MetadataCacheStatistics(typing_extensions.TypedDict, total=False):
    tableMetadataCacheUsage: _list[TableMetadataCacheUsage]

@typing.type_check_only
class MlStatistics(typing_extensions.TypedDict, total=False):
    hparamTrials: _list[HparamTuningTrial]
    iterationResults: _list[IterationResult]
    maxIterations: str
    modelType: typing_extensions.Literal[
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
    trainingType: typing_extensions.Literal[
        "TRAINING_TYPE_UNSPECIFIED", "SINGLE_TRAINING", "HPARAM_TUNING"
    ]

@typing.type_check_only
class Model(typing_extensions.TypedDict, total=False):
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
    modelType: typing_extensions.Literal[
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
class ModelDefinition(typing_extensions.TypedDict, total=False):
    modelOptions: dict[str, typing.Any]
    trainingRuns: _list[BqmlTrainingRun]

@typing.type_check_only
class ModelExtractOptions(typing_extensions.TypedDict, total=False):
    trialId: str

@typing.type_check_only
class ModelReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    modelId: str
    projectId: str

@typing.type_check_only
class MultiClassClassificationMetrics(typing_extensions.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    confusionMatrixList: _list[ConfusionMatrix]

@typing.type_check_only
class ParquetOptions(typing_extensions.TypedDict, total=False):
    enableListInference: bool
    enumAsString: bool
    mapTargetType: typing_extensions.Literal[
        "MAP_TARGET_TYPE_UNSPECIFIED", "ARRAY_OF_STRUCT"
    ]

@typing.type_check_only
class PartitionSkew(typing_extensions.TypedDict, total=False):
    skewSources: _list[SkewSource]

@typing.type_check_only
class PartitionedColumn(typing_extensions.TypedDict, total=False):
    field: str

@typing.type_check_only
class PartitioningDefinition(typing_extensions.TypedDict, total=False):
    partitionedColumn: _list[PartitionedColumn]

@typing.type_check_only
class PerformanceInsights(typing_extensions.TypedDict, total=False):
    avgPreviousExecutionMs: str
    stagePerformanceChangeInsights: _list[StagePerformanceChangeInsight]
    stagePerformanceStandaloneInsights: _list[StagePerformanceStandaloneInsight]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrincipalComponentInfo(typing_extensions.TypedDict, total=False):
    cumulativeExplainedVarianceRatio: float
    explainedVariance: float
    explainedVarianceRatio: float
    principalComponentId: str

@typing.type_check_only
class PrivacyPolicy(typing_extensions.TypedDict, total=False):
    aggregationThresholdPolicy: AggregationThresholdPolicy
    differentialPrivacyPolicy: DifferentialPrivacyPolicy
    joinRestrictionPolicy: JoinRestrictionPolicy

@typing.type_check_only
class ProjectList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    projects: _list[dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class ProjectReference(typing_extensions.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class QueryInfo(typing_extensions.TypedDict, total=False):
    optimizationDetails: dict[str, typing.Any]

@typing.type_check_only
class QueryParameter(typing_extensions.TypedDict, total=False):
    name: str
    parameterType: QueryParameterType
    parameterValue: QueryParameterValue

@typing.type_check_only
class QueryParameterType(typing_extensions.TypedDict, total=False):
    arrayType: QueryParameterType
    rangeElementType: QueryParameterType
    structTypes: _list[dict[str, typing.Any]]
    type: str

@typing.type_check_only
class QueryParameterValue(typing_extensions.TypedDict, total=False):
    arrayValues: _list[QueryParameterValue]
    rangeValue: RangeValue
    structValues: dict[str, typing.Any]
    value: str

@typing.type_check_only
class QueryRequest(typing_extensions.TypedDict, total=False):
    connectionProperties: _list[ConnectionProperty]
    continuous: bool
    createSession: bool
    defaultDataset: DatasetReference
    dryRun: bool
    formatOptions: DataFormatOptions
    jobCreationMode: typing_extensions.Literal[
        "JOB_CREATION_MODE_UNSPECIFIED",
        "JOB_CREATION_REQUIRED",
        "JOB_CREATION_OPTIONAL",
    ]
    kind: str
    labels: dict[str, typing.Any]
    location: str
    maxResults: int
    maximumBytesBilled: str
    parameterMode: str
    preserveNulls: bool
    query: str
    queryParameters: _list[QueryParameter]
    requestId: str
    timeoutMs: int
    useLegacySql: bool
    useQueryCache: bool

@typing.type_check_only
class QueryResponse(typing_extensions.TypedDict, total=False):
    cacheHit: bool
    dmlStats: DmlStatistics
    errors: _list[ErrorProto]
    jobComplete: bool
    jobCreationReason: JobCreationReason
    jobReference: JobReference
    kind: str
    numDmlAffectedRows: str
    pageToken: str
    queryId: str
    rows: _list[TableRow]
    schema: TableSchema
    sessionInfo: SessionInfo
    totalBytesProcessed: str
    totalRows: str

@typing.type_check_only
class QueryTimelineSample(typing_extensions.TypedDict, total=False):
    activeUnits: str
    completedUnits: str
    elapsedMs: str
    estimatedRunnableUnits: str
    pendingUnits: str
    totalSlotMs: str

@typing.type_check_only
class RangePartitioning(typing_extensions.TypedDict, total=False):
    field: str
    range: dict[str, typing.Any]

@typing.type_check_only
class RangeValue(typing_extensions.TypedDict, total=False):
    end: QueryParameterValue
    start: QueryParameterValue

@typing.type_check_only
class RankingMetrics(typing_extensions.TypedDict, total=False):
    averageRank: float
    meanAveragePrecision: float
    meanSquaredError: float
    normalizedDiscountedCumulativeGain: float

@typing.type_check_only
class RegressionMetrics(typing_extensions.TypedDict, total=False):
    meanAbsoluteError: float
    meanSquaredError: float
    meanSquaredLogError: float
    medianAbsoluteError: float
    rSquared: float

@typing.type_check_only
class RemoteFunctionOptions(typing_extensions.TypedDict, total=False):
    connection: str
    endpoint: str
    maxBatchingRows: str
    userDefinedContext: dict[str, typing.Any]

@typing.type_check_only
class RemoteModelInfo(typing_extensions.TypedDict, total=False):
    connection: str
    endpoint: str
    maxBatchingRows: str
    remoteModelVersion: str
    remoteServiceType: typing_extensions.Literal[
        "REMOTE_SERVICE_TYPE_UNSPECIFIED",
        "CLOUD_AI_TRANSLATE_V3",
        "CLOUD_AI_VISION_V1",
        "CLOUD_AI_NATURAL_LANGUAGE_V1",
        "CLOUD_AI_SPEECH_TO_TEXT_V2",
    ]
    speechRecognizer: str

@typing.type_check_only
class RestrictionConfig(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED", "RESTRICTED_DATA_EGRESS"
    ]

@typing.type_check_only
class Routine(typing_extensions.TypedDict, total=False):
    arguments: _list[Argument]
    creationTime: str
    dataGovernanceType: typing_extensions.Literal[
        "DATA_GOVERNANCE_TYPE_UNSPECIFIED", "DATA_MASKING"
    ]
    definitionBody: str
    description: str
    determinismLevel: typing_extensions.Literal[
        "DETERMINISM_LEVEL_UNSPECIFIED", "DETERMINISTIC", "NOT_DETERMINISTIC"
    ]
    etag: str
    importedLibraries: _list[str]
    language: typing_extensions.Literal[
        "LANGUAGE_UNSPECIFIED", "SQL", "JAVASCRIPT", "PYTHON", "JAVA", "SCALA"
    ]
    lastModifiedTime: str
    remoteFunctionOptions: RemoteFunctionOptions
    returnTableType: StandardSqlTableType
    returnType: StandardSqlDataType
    routineReference: RoutineReference
    routineType: typing_extensions.Literal[
        "ROUTINE_TYPE_UNSPECIFIED",
        "SCALAR_FUNCTION",
        "PROCEDURE",
        "TABLE_VALUED_FUNCTION",
        "AGGREGATE_FUNCTION",
    ]
    securityMode: typing_extensions.Literal[
        "SECURITY_MODE_UNSPECIFIED", "DEFINER", "INVOKER"
    ]
    sparkOptions: SparkOptions
    strictMode: bool

@typing.type_check_only
class RoutineReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    routineId: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    actualLabel: str
    entries: _list[Entry]

@typing.type_check_only
class RowAccessPolicy(typing_extensions.TypedDict, total=False):
    creationTime: str
    etag: str
    filterPredicate: str
    lastModifiedTime: str
    rowAccessPolicyReference: RowAccessPolicyReference

@typing.type_check_only
class RowAccessPolicyReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    policyId: str
    projectId: str
    tableId: str

@typing.type_check_only
class RowLevelSecurityStatistics(typing_extensions.TypedDict, total=False):
    rowLevelSecurityApplied: bool

@typing.type_check_only
class ScriptOptions(typing_extensions.TypedDict, total=False):
    keyResultStatement: typing_extensions.Literal[
        "KEY_RESULT_STATEMENT_KIND_UNSPECIFIED", "LAST", "FIRST_SELECT"
    ]
    statementByteBudget: str
    statementTimeoutMs: str

@typing.type_check_only
class ScriptStackFrame(typing_extensions.TypedDict, total=False):
    endColumn: int
    endLine: int
    procedureId: str
    startColumn: int
    startLine: int
    text: str

@typing.type_check_only
class ScriptStatistics(typing_extensions.TypedDict, total=False):
    evaluationKind: typing_extensions.Literal[
        "EVALUATION_KIND_UNSPECIFIED", "STATEMENT", "EXPRESSION"
    ]
    stackFrames: _list[ScriptStackFrame]

@typing.type_check_only
class SearchStatistics(typing_extensions.TypedDict, total=False):
    indexUnusedReasons: _list[IndexUnusedReason]
    indexUsageMode: typing_extensions.Literal[
        "INDEX_USAGE_MODE_UNSPECIFIED", "UNUSED", "PARTIALLY_USED", "FULLY_USED"
    ]

@typing.type_check_only
class SerDeInfo(typing_extensions.TypedDict, total=False):
    name: str
    parameters: dict[str, typing.Any]
    serializationLibrary: str

@typing.type_check_only
class SessionInfo(typing_extensions.TypedDict, total=False):
    sessionId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SkewSource(typing_extensions.TypedDict, total=False):
    stageId: str

@typing.type_check_only
class SnapshotDefinition(typing_extensions.TypedDict, total=False):
    baseTableReference: TableReference
    snapshotTime: str

@typing.type_check_only
class SparkLoggingInfo(typing_extensions.TypedDict, total=False):
    projectId: str
    resourceType: str

@typing.type_check_only
class SparkOptions(typing_extensions.TypedDict, total=False):
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
class SparkStatistics(typing_extensions.TypedDict, total=False):
    endpoints: dict[str, typing.Any]
    gcsStagingBucket: str
    kmsKeyName: str
    loggingInfo: SparkLoggingInfo
    sparkJobId: str
    sparkJobLocation: str

@typing.type_check_only
class StagePerformanceChangeInsight(typing_extensions.TypedDict, total=False):
    inputDataChange: InputDataChange
    stageId: str

@typing.type_check_only
class StagePerformanceStandaloneInsight(typing_extensions.TypedDict, total=False):
    biEngineReasons: _list[BiEngineReason]
    highCardinalityJoins: _list[HighCardinalityJoin]
    insufficientShuffleQuota: bool
    partitionSkew: PartitionSkew
    slotContention: bool
    stageId: str

@typing.type_check_only
class StandardSqlDataType(typing_extensions.TypedDict, total=False):
    arrayElementType: StandardSqlDataType
    rangeElementType: StandardSqlDataType
    structType: StandardSqlStructType
    typeKind: typing_extensions.Literal[
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
class StandardSqlField(typing_extensions.TypedDict, total=False):
    name: str
    type: StandardSqlDataType

@typing.type_check_only
class StandardSqlStructType(typing_extensions.TypedDict, total=False):
    fields: _list[StandardSqlField]

@typing.type_check_only
class StandardSqlTableType(typing_extensions.TypedDict, total=False):
    columns: _list[StandardSqlField]

@typing.type_check_only
class StorageDescriptor(typing_extensions.TypedDict, total=False):
    inputFormat: str
    locationUri: str
    outputFormat: str
    serdeInfo: SerDeInfo

@typing.type_check_only
class Streamingbuffer(typing_extensions.TypedDict, total=False):
    estimatedBytes: str
    estimatedRows: str
    oldestEntryTime: str

@typing.type_check_only
class StringHparamSearchSpace(typing_extensions.TypedDict, total=False):
    candidates: _list[str]

@typing.type_check_only
class SystemVariables(typing_extensions.TypedDict, total=False):
    types: dict[str, typing.Any]
    values: dict[str, typing.Any]

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    biglakeConfiguration: BigLakeConfiguration
    cloneDefinition: CloneDefinition
    clustering: Clustering
    creationTime: str
    defaultCollation: str
    defaultRoundingMode: typing_extensions.Literal[
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
    managedTableType: typing_extensions.Literal[
        "MANAGED_TABLE_TYPE_UNSPECIFIED", "NATIVE", "ICEBERG"
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
class TableCell(typing_extensions.TypedDict, total=False):
    v: typing.Any

@typing.type_check_only
class TableConstraints(typing_extensions.TypedDict, total=False):
    foreignKeys: _list[dict[str, typing.Any]]
    primaryKey: dict[str, typing.Any]

@typing.type_check_only
class TableDataInsertAllRequest(typing_extensions.TypedDict, total=False):
    ignoreUnknownValues: bool
    kind: str
    rows: _list[dict[str, typing.Any]]
    skipInvalidRows: bool
    templateSuffix: str
    traceId: str

@typing.type_check_only
class TableDataInsertAllResponse(typing_extensions.TypedDict, total=False):
    insertErrors: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class TableDataList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    pageToken: str
    rows: _list[TableRow]
    totalRows: str

@typing.type_check_only
class TableFieldSchema(typing_extensions.TypedDict, total=False):
    categories: dict[str, typing.Any]
    collation: str
    dataPolicies: _list[DataPolicyOption]
    defaultValueExpression: str
    description: str
    fields: _list[TableFieldSchema]
    foreignTypeDefinition: str
    maxLength: str
    mode: str
    name: str
    policyTags: dict[str, typing.Any]
    precision: str
    rangeElementType: dict[str, typing.Any]
    roundingMode: typing_extensions.Literal[
        "ROUNDING_MODE_UNSPECIFIED", "ROUND_HALF_AWAY_FROM_ZERO", "ROUND_HALF_EVEN"
    ]
    scale: str
    type: str

@typing.type_check_only
class TableList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    tables: _list[dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class TableMetadataCacheUsage(typing_extensions.TypedDict, total=False):
    explanation: str
    staleness: str
    tableReference: TableReference
    tableType: str
    unusedReason: typing_extensions.Literal[
        "UNUSED_REASON_UNSPECIFIED",
        "EXCEEDED_MAX_STALENESS",
        "METADATA_CACHING_NOT_ENABLED",
        "OTHER_REASON",
    ]

@typing.type_check_only
class TableReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class TableReplicationInfo(typing_extensions.TypedDict, total=False):
    replicatedSourceLastRefreshTime: str
    replicationError: ErrorProto
    replicationIntervalMs: str
    replicationStatus: typing_extensions.Literal[
        "REPLICATION_STATUS_UNSPECIFIED",
        "ACTIVE",
        "SOURCE_DELETED",
        "PERMISSION_DENIED",
        "UNSUPPORTED_CONFIGURATION",
    ]
    sourceTable: TableReference

@typing.type_check_only
class TableRow(typing_extensions.TypedDict, total=False):
    f: _list[TableCell]

@typing.type_check_only
class TableSchema(typing_extensions.TypedDict, total=False):
    fields: _list[TableFieldSchema]
    foreignTypeInfo: ForeignTypeInfo

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimePartitioning(typing_extensions.TypedDict, total=False):
    expirationMs: str
    field: str
    requirePartitionFilter: bool
    type: str

@typing.type_check_only
class TrainingOptions(typing_extensions.TypedDict, total=False):
    activationFn: str
    adjustStepChanges: bool
    approxGlobalFeatureContrib: bool
    autoArima: bool
    autoArimaMaxOrder: str
    autoArimaMinOrder: str
    autoClassWeights: bool
    batchSize: str
    boosterType: typing_extensions.Literal["BOOSTER_TYPE_UNSPECIFIED", "GBTREE", "DART"]
    budgetHours: float
    calculatePValues: bool
    categoryEncodingMethod: typing_extensions.Literal[
        "ENCODING_METHOD_UNSPECIFIED",
        "ONE_HOT_ENCODING",
        "LABEL_ENCODING",
        "DUMMY_ENCODING",
    ]
    cleanSpikesAndDips: bool
    colorSpace: typing_extensions.Literal[
        "COLOR_SPACE_UNSPECIFIED", "RGB", "HSV", "YIQ", "YUV", "GRAYSCALE"
    ]
    colsampleBylevel: float
    colsampleBynode: float
    colsampleBytree: float
    contributionMetric: str
    dartNormalizeType: typing_extensions.Literal[
        "DART_NORMALIZE_TYPE_UNSPECIFIED", "TREE", "FOREST"
    ]
    dataFrequency: typing_extensions.Literal[
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
    dataSplitMethod: typing_extensions.Literal[
        "DATA_SPLIT_METHOD_UNSPECIFIED",
        "RANDOM",
        "CUSTOM",
        "SEQUENTIAL",
        "NO_SPLIT",
        "AUTO_SPLIT",
    ]
    decomposeTimeSeries: bool
    dimensionIdColumns: _list[str]
    distanceType: typing_extensions.Literal[
        "DISTANCE_TYPE_UNSPECIFIED", "EUCLIDEAN", "COSINE"
    ]
    dropout: float
    earlyStop: bool
    enableGlobalExplain: bool
    feedbackType: typing_extensions.Literal[
        "FEEDBACK_TYPE_UNSPECIFIED", "IMPLICIT", "EXPLICIT"
    ]
    fitIntercept: bool
    hiddenUnits: _list[str]
    holidayRegion: typing_extensions.Literal[
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
        typing_extensions.Literal[
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
        typing_extensions.Literal[
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
    includeDrift: bool
    initialLearnRate: float
    inputLabelColumns: _list[str]
    instanceWeightColumn: str
    integratedGradientsNumSteps: str
    isTestColumn: str
    itemColumn: str
    kmeansInitializationColumn: str
    kmeansInitializationMethod: typing_extensions.Literal[
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
    learnRateStrategy: typing_extensions.Literal[
        "LEARN_RATE_STRATEGY_UNSPECIFIED", "LINE_SEARCH", "CONSTANT"
    ]
    lossType: typing_extensions.Literal[
        "LOSS_TYPE_UNSPECIFIED", "MEAN_SQUARED_LOSS", "MEAN_LOG_LOSS"
    ]
    maxIterations: str
    maxParallelTrials: str
    maxTimeSeriesLength: str
    maxTreeDepth: str
    minAprioriSupport: float
    minRelativeProgress: float
    minSplitLoss: float
    minTimeSeriesLength: str
    minTreeChildWeight: str
    modelRegistry: typing_extensions.Literal["MODEL_REGISTRY_UNSPECIFIED", "VERTEX_AI"]
    modelUri: str
    nonSeasonalOrder: ArimaOrder
    numClusters: str
    numFactors: str
    numParallelTree: str
    numPrincipalComponents: str
    numTrials: str
    optimizationStrategy: typing_extensions.Literal[
        "OPTIMIZATION_STRATEGY_UNSPECIFIED", "BATCH_GRADIENT_DESCENT", "NORMAL_EQUATION"
    ]
    optimizer: str
    pcaExplainedVarianceRatio: float
    pcaSolver: typing_extensions.Literal["UNSPECIFIED", "FULL", "RANDOMIZED", "AUTO"]
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
    treeMethod: typing_extensions.Literal[
        "TREE_METHOD_UNSPECIFIED", "AUTO", "EXACT", "APPROX", "HIST"
    ]
    trendSmoothingWindowSize: str
    userColumn: str
    vertexAiModelVersionAliases: _list[str]
    walsAlpha: float
    warmStart: bool
    xgboostVersion: str

@typing.type_check_only
class TrainingRun(typing_extensions.TypedDict, total=False):
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
class TransactionInfo(typing_extensions.TypedDict, total=False):
    transactionId: str

@typing.type_check_only
class TransformColumn(typing_extensions.TypedDict, total=False):
    name: str
    transformSql: str
    type: StandardSqlDataType

@typing.type_check_only
class UndeleteDatasetRequest(typing_extensions.TypedDict, total=False):
    deletionTime: str

@typing.type_check_only
class UserDefinedFunctionResource(typing_extensions.TypedDict, total=False):
    inlineCode: str
    resourceUri: str

@typing.type_check_only
class VectorSearchStatistics(typing_extensions.TypedDict, total=False):
    indexUnusedReasons: _list[IndexUnusedReason]
    indexUsageMode: typing_extensions.Literal[
        "INDEX_USAGE_MODE_UNSPECIFIED", "UNUSED", "PARTIALLY_USED", "FULLY_USED"
    ]

@typing.type_check_only
class ViewDefinition(typing_extensions.TypedDict, total=False):
    foreignDefinitions: _list[ForeignViewDefinition]
    privacyPolicy: PrivacyPolicy
    query: str
    useExplicitColumnNames: bool
    useLegacySql: bool
    userDefinedFunctionResources: _list[UserDefinedFunctionResource]
