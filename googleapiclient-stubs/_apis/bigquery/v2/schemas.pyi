import typing

import typing_extensions

class BinaryClassificationMetrics(typing_extensions.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    binaryConfusionMatrixList: typing.List[BinaryConfusionMatrix]
    negativeLabel: str
    positiveLabel: str

class QueryRequest(typing_extensions.TypedDict, total=False):
    maxResults: int
    maximumBytesBilled: str
    kind: str
    parameterMode: str
    defaultDataset: DatasetReference
    location: str
    queryParameters: typing.List[QueryParameter]
    requestId: str
    preserveNulls: bool
    query: str
    dryRun: bool
    labels: typing.Dict[str, typing.Any]
    connectionProperties: typing.List[ConnectionProperty]
    timeoutMs: int
    useQueryCache: bool
    useLegacySql: bool

class RegressionMetrics(typing_extensions.TypedDict, total=False):
    meanSquaredError: float
    meanSquaredLogError: float
    medianAbsoluteError: float
    rSquared: float
    meanAbsoluteError: float

class ModelDefinition(typing_extensions.TypedDict, total=False):
    modelOptions: typing.Dict[str, typing.Any]
    trainingRuns: typing.List[BqmlTrainingRun]

class AggregateClassificationMetrics(typing_extensions.TypedDict, total=False):
    logLoss: float
    f1Score: float
    accuracy: float
    threshold: float
    precision: float
    rocAuc: float
    recall: float

class TableFieldSchema(typing.Dict[str, typing.Any]): ...

class TableSchema(typing_extensions.TypedDict, total=False):
    fields: typing.List[TableFieldSchema]

class Cluster(typing_extensions.TypedDict, total=False):
    count: str
    centroidId: str
    featureValues: typing.List[FeatureValue]

class ArimaModelInfo(typing_extensions.TypedDict, total=False):
    arimaCoefficients: ArimaCoefficients
    nonSeasonalOrder: ArimaOrder
    hasDrift: bool
    seasonalPeriods: typing.List[str]
    arimaFittingMetrics: ArimaFittingMetrics
    timeSeriesId: str

class LocationMetadata(typing_extensions.TypedDict, total=False):
    legacyLocationId: str

class JobStatistics4(typing_extensions.TypedDict, total=False):
    inputBytes: str
    destinationUriFileCounts: typing.List[str]

class Streamingbuffer(typing_extensions.TypedDict, total=False):
    estimatedRows: str
    oldestEntryTime: str
    estimatedBytes: str

class JobConfigurationLoad(typing_extensions.TypedDict, total=False):
    rangePartitioning: RangePartitioning
    schema: TableSchema
    allowQuotedNewlines: bool
    destinationEncryptionConfiguration: EncryptionConfiguration
    writeDisposition: str
    autodetect: bool
    schemaInlineFormat: str
    clustering: Clustering
    schemaUpdateOptions: typing.List[str]
    createDisposition: str
    destinationTableProperties: DestinationTableProperties
    maxBadRecords: int
    hivePartitioningOptions: HivePartitioningOptions
    encoding: str
    sourceUris: typing.List[str]
    ignoreUnknownValues: bool
    fieldDelimiter: str
    allowJaggedRows: bool
    nullMarker: str
    schemaInline: str
    decimalTargetTypes: typing.List[str]
    sourceFormat: str
    quote: str
    useAvroLogicalTypes: bool
    destinationTable: TableReference
    skipLeadingRows: int
    projectionFields: typing.List[str]
    timePartitioning: TimePartitioning

class StandardSqlStructType(typing_extensions.TypedDict, total=False):
    fields: typing.List[StandardSqlField]

class CategoryCount(typing_extensions.TypedDict, total=False):
    count: str
    category: str

class IterationResult(typing_extensions.TypedDict, total=False):
    learnRate: float
    arimaResult: ArimaResult
    trainingLoss: float
    index: int
    durationMs: str
    clusterInfos: typing.List[ClusterInfo]
    evalLoss: float

class BqmlTrainingRun(typing_extensions.TypedDict, total=False):
    startTime: str
    trainingOptions: typing.Dict[str, typing.Any]
    iterationResults: typing.List[BqmlIterationResult]
    state: str

class CategoricalValue(typing_extensions.TypedDict, total=False):
    categoryCounts: typing.List[CategoryCount]

class DatasetReference(typing_extensions.TypedDict, total=False):
    projectId: str
    datasetId: str

class BinaryConfusionMatrix(typing_extensions.TypedDict, total=False):
    f1Score: float
    falsePositives: str
    falseNegatives: str
    truePositives: str
    precision: float
    recall: float
    positiveClassThreshold: float
    trueNegatives: str
    accuracy: float

class ArimaForecastingMetrics(typing_extensions.TypedDict, total=False):
    arimaSingleModelForecastingMetrics: typing.List[ArimaSingleModelForecastingMetrics]
    timeSeriesId: typing.List[str]
    arimaFittingMetrics: typing.List[ArimaFittingMetrics]
    nonSeasonalOrder: typing.List[ArimaOrder]
    hasDrift: typing.List[bool]
    seasonalPeriods: typing.List[str]

class ConfusionMatrix(typing_extensions.TypedDict, total=False):
    rows: typing.List[Row]
    confidenceThreshold: float

class Entry(typing_extensions.TypedDict, total=False):
    predictedLabel: str
    itemCount: str

class TableReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

class JobStatistics(typing_extensions.TypedDict, total=False):
    creationTime: str
    endTime: str
    load: JobStatistics3
    transactionInfoTemplate: TransactionInfo
    startTime: str
    quotaDeferments: typing.List[str]
    extract: JobStatistics4
    query: JobStatistics2
    totalSlotMs: str
    scriptStatistics: ScriptStatistics
    totalBytesProcessed: str
    rowLevelSecurityStatistics: RowLevelSecurityStatistics
    completionRatio: float
    numChildJobs: str
    reservationUsage: typing.List[typing.Dict[str, typing.Any]]
    reservation_id: str
    parentJobId: str

class BqmlIterationResult(typing_extensions.TypedDict, total=False):
    learnRate: float
    trainingLoss: float
    durationMs: str
    index: int
    evalLoss: float

class TableDataList(typing_extensions.TypedDict, total=False):
    totalRows: str
    rows: typing.List[TableRow]
    kind: str
    etag: str
    pageToken: str

class ScriptStackFrame(typing_extensions.TypedDict, total=False):
    startLine: int
    endColumn: int
    endLine: int
    procedureId: str
    text: str
    startColumn: int

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ModelReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    modelId: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class JobStatus(typing_extensions.TypedDict, total=False):
    errorResult: ErrorProto
    errors: typing.List[ErrorProto]
    state: str

class BigtableColumn(typing_extensions.TypedDict, total=False):
    qualifierString: str
    fieldName: str
    onlyReadLatest: bool
    encoding: str
    type: str
    qualifierEncoded: str

class TableRow(typing_extensions.TypedDict, total=False):
    f: typing.List[TableCell]

class HivePartitioningOptions(typing_extensions.TypedDict, total=False):
    sourceUriPrefix: str
    mode: str
    requirePartitionFilter: bool

class QueryParameterValue(typing.Dict[str, typing.Any]): ...

class TableDataInsertAllRequest(typing_extensions.TypedDict, total=False):
    kind: str
    ignoreUnknownValues: bool
    templateSuffix: str
    rows: typing.List[typing.Dict[str, typing.Any]]
    skipInvalidRows: bool

class ExplainQueryStage(typing_extensions.TypedDict, total=False):
    startMs: str
    waitRatioMax: float
    waitMsAvg: str
    readMsMax: str
    waitMsMax: str
    inputStages: typing.List[str]
    computeRatioMax: float
    name: str
    shuffleOutputBytes: str
    status: str
    slotMs: str
    shuffleOutputBytesSpilled: str
    computeMsMax: str
    writeMsAvg: str
    writeMsMax: str
    parallelInputs: str
    recordsWritten: str
    writeRatioMax: float
    steps: typing.List[ExplainQueryStep]
    recordsRead: str
    readRatioAvg: float
    writeRatioAvg: float
    readRatioMax: float
    computeMsAvg: str
    id: str
    endMs: str
    computeRatioAvg: float
    completedParallelInputs: str
    readMsAvg: str
    waitRatioAvg: float

class ArimaCoefficients(typing_extensions.TypedDict, total=False):
    interceptCoefficient: float
    movingAverageCoefficients: typing.List[float]
    autoRegressiveCoefficients: typing.List[float]

class ArimaResult(typing_extensions.TypedDict, total=False):
    arimaModelInfo: typing.List[ArimaModelInfo]
    seasonalPeriods: typing.List[str]

class UserDefinedFunctionResource(typing_extensions.TypedDict, total=False):
    inlineCode: str
    resourceUri: str

class ArimaSingleModelForecastingMetrics(typing_extensions.TypedDict, total=False):
    timeSeriesId: str
    seasonalPeriods: typing.List[str]
    nonSeasonalOrder: ArimaOrder
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool

class Model(typing_extensions.TypedDict, total=False):
    expirationTime: str
    featureColumns: typing.List[StandardSqlField]
    creationTime: str
    modelReference: ModelReference
    labels: typing.Dict[str, typing.Any]
    trainingRuns: typing.List[TrainingRun]
    description: str
    labelColumns: typing.List[StandardSqlField]
    lastModifiedTime: str
    encryptionConfiguration: EncryptionConfiguration
    modelType: typing_extensions.Literal[
        "MODEL_TYPE_UNSPECIFIED",
        "LINEAR_REGRESSION",
        "LOGISTIC_REGRESSION",
        "KMEANS",
        "MATRIX_FACTORIZATION",
        "DNN_CLASSIFIER",
        "TENSORFLOW",
        "DNN_REGRESSOR",
        "BOOSTED_TREE_REGRESSOR",
        "BOOSTED_TREE_CLASSIFIER",
        "ARIMA",
        "AUTOML_REGRESSOR",
        "AUTOML_CLASSIFIER",
    ]
    friendlyName: str
    etag: str
    location: str

class JsonValue(typing.Dict[str, typing.Any]): ...

class RoutineReference(typing_extensions.TypedDict, total=False):
    routineId: str
    projectId: str
    datasetId: str

class BigtableOptions(typing_extensions.TypedDict, total=False):
    columnFamilies: typing.List[BigtableColumnFamily]
    readRowkeyAsString: bool
    ignoreUnspecifiedColumnFamilies: bool

class RangePartitioning(typing_extensions.TypedDict, total=False):
    field: str
    range: typing.Dict[str, typing.Any]

class FeatureValue(typing_extensions.TypedDict, total=False):
    categoricalValue: CategoricalValue
    featureColumn: str
    numericalValue: float

class RowLevelSecurityStatistics(typing_extensions.TypedDict, total=False):
    rowLevelSecurityApplied: bool

class JobList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    jobs: typing.List[typing.Dict[str, typing.Any]]
    etag: str
    kind: str

class DatasetList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    etag: str
    kind: str
    datasets: typing.List[typing.Dict[str, typing.Any]]

class JobReference(typing_extensions.TypedDict, total=False):
    location: str
    projectId: str
    jobId: str

class JobConfigurationQuery(typing_extensions.TypedDict, total=False):
    priority: str
    parameterMode: str
    schemaUpdateOptions: typing.List[str]
    flattenResults: bool
    timePartitioning: TimePartitioning
    query: str
    defaultDataset: DatasetReference
    userDefinedFunctionResources: typing.List[UserDefinedFunctionResource]
    maximumBytesBilled: str
    createDisposition: str
    writeDisposition: str
    connectionProperties: typing.List[ConnectionProperty]
    useLegacySql: bool
    destinationTable: TableReference
    preserveNulls: bool
    tableDefinitions: typing.Dict[str, typing.Any]
    maximumBillingTier: int
    destinationEncryptionConfiguration: EncryptionConfiguration
    allowLargeResults: bool
    useQueryCache: bool
    clustering: Clustering
    queryParameters: typing.List[QueryParameter]
    rangePartitioning: RangePartitioning

class ArimaFittingMetrics(typing_extensions.TypedDict, total=False):
    aic: float
    variance: float
    logLikelihood: float

class ListRoutinesResponse(typing_extensions.TypedDict, total=False):
    routines: typing.List[Routine]
    nextPageToken: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class StandardSqlField(typing.Dict[str, typing.Any]): ...
class JobStatistics2(typing.Dict[str, typing.Any]): ...

class BigQueryModelTraining(typing_extensions.TypedDict, total=False):
    currentIteration: int
    expectedTotalIterations: str

class ProjectList(typing_extensions.TypedDict, total=False):
    etag: str
    totalItems: int
    projects: typing.List[typing.Dict[str, typing.Any]]
    nextPageToken: str
    kind: str

class ClusterInfo(typing_extensions.TypedDict, total=False):
    clusterSize: str
    centroidId: str
    clusterRadius: float

class MultiClassClassificationMetrics(typing_extensions.TypedDict, total=False):
    confusionMatrixList: typing.List[ConfusionMatrix]
    aggregateClassificationMetrics: AggregateClassificationMetrics

class EncryptionConfiguration(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

class GetServiceAccountResponse(typing_extensions.TypedDict, total=False):
    email: str
    kind: str

class ExplainQueryStep(typing_extensions.TypedDict, total=False):
    kind: str
    substeps: typing.List[str]

class ProjectReference(typing_extensions.TypedDict, total=False):
    projectId: str

class Clustering(typing_extensions.TypedDict, total=False):
    fields: typing.List[str]

class StandardSqlDataType(typing.Dict[str, typing.Any]): ...

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class DestinationTableProperties(typing_extensions.TypedDict, total=False):
    description: str
    labels: typing.Dict[str, typing.Any]
    friendlyName: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class RankingMetrics(typing_extensions.TypedDict, total=False):
    normalizedDiscountedCumulativeGain: float
    averageRank: float
    meanAveragePrecision: float
    meanSquaredError: float

class Row(typing_extensions.TypedDict, total=False):
    entries: typing.List[Entry]
    actualLabel: str

class TimePartitioning(typing_extensions.TypedDict, total=False):
    type: str
    expirationMs: str
    requirePartitionFilter: bool
    field: str

class Argument(typing_extensions.TypedDict, total=False):
    name: str
    argumentKind: typing_extensions.Literal[
        "ARGUMENT_KIND_UNSPECIFIED", "FIXED_TYPE", "ANY_TYPE"
    ]
    dataType: StandardSqlDataType
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "IN", "OUT", "INOUT"]

class TrainingOptions(typing_extensions.TypedDict, total=False):
    horizon: str
    includeDrift: bool
    l1Regularization: float
    autoArimaMaxOrder: str
    dropout: float
    preserveInputStructs: bool
    userColumn: str
    modelUri: str
    maxTreeDepth: str
    subsample: float
    inputLabelColumns: typing.List[str]
    learnRate: float
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
    kmeansInitializationColumn: str
    lossType: typing_extensions.Literal[
        "LOSS_TYPE_UNSPECIFIED", "MEAN_SQUARED_LOSS", "MEAN_LOG_LOSS"
    ]
    hiddenUnits: typing.List[str]
    minSplitLoss: float
    earlyStop: bool
    l2Regularization: float
    feedbackType: typing_extensions.Literal[
        "FEEDBACK_TYPE_UNSPECIFIED", "IMPLICIT", "EXPLICIT"
    ]
    minRelativeProgress: float
    dataSplitMethod: typing_extensions.Literal[
        "DATA_SPLIT_METHOD_UNSPECIFIED",
        "RANDOM",
        "CUSTOM",
        "SEQUENTIAL",
        "NO_SPLIT",
        "AUTO_SPLIT",
    ]
    timeSeriesIdColumn: str
    numClusters: str
    warmStart: bool
    numFactors: str
    walsAlpha: float
    kmeansInitializationMethod: typing_extensions.Literal[
        "KMEANS_INITIALIZATION_METHOD_UNSPECIFIED",
        "RANDOM",
        "CUSTOM",
        "KMEANS_PLUS_PLUS",
    ]
    timeSeriesTimestampColumn: str
    itemColumn: str
    maxIterations: str
    initialLearnRate: float
    timeSeriesDataColumn: str
    batchSize: str
    nonSeasonalOrder: ArimaOrder
    autoArima: bool
    distanceType: typing_extensions.Literal[
        "DISTANCE_TYPE_UNSPECIFIED", "EUCLIDEAN", "COSINE"
    ]
    dataSplitColumn: str
    dataSplitEvalFraction: float
    dataFrequency: typing_extensions.Literal[
        "DATA_FREQUENCY_UNSPECIFIED",
        "AUTO_FREQUENCY",
        "YEARLY",
        "QUARTERLY",
        "MONTHLY",
        "WEEKLY",
        "DAILY",
        "HOURLY",
    ]
    labelClassWeights: typing.Dict[str, typing.Any]
    optimizationStrategy: typing_extensions.Literal[
        "OPTIMIZATION_STRATEGY_UNSPECIFIED", "BATCH_GRADIENT_DESCENT", "NORMAL_EQUATION"
    ]
    learnRateStrategy: typing_extensions.Literal[
        "LEARN_RATE_STRATEGY_UNSPECIFIED", "LINE_SEARCH", "CONSTANT"
    ]

class DataSplitResult(typing_extensions.TypedDict, total=False):
    evaluationTable: TableReference
    trainingTable: TableReference

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class ClusteringMetrics(typing_extensions.TypedDict, total=False):
    meanSquaredDistance: float
    daviesBouldinIndex: float
    clusters: typing.List[Cluster]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class SnapshotDefinition(typing_extensions.TypedDict, total=False):
    baseTableReference: TableReference
    snapshotTime: str

class JobConfigurationExtract(typing_extensions.TypedDict, total=False):
    destinationUri: str
    destinationFormat: str
    destinationUris: typing.List[str]
    compression: str
    sourceTable: TableReference
    sourceModel: ModelReference
    printHeader: bool
    useAvroLogicalTypes: bool
    fieldDelimiter: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class ExternalDataConfiguration(typing_extensions.TypedDict, total=False):
    connectionId: str
    schema: TableSchema
    compression: str
    autodetect: bool
    sourceFormat: str
    sourceUris: typing.List[str]
    csvOptions: CsvOptions
    ignoreUnknownValues: bool
    googleSheetsOptions: GoogleSheetsOptions
    maxBadRecords: int
    hivePartitioningOptions: HivePartitioningOptions
    bigtableOptions: BigtableOptions

class RowAccessPolicyReference(typing_extensions.TypedDict, total=False):
    policyId: str
    tableId: str
    datasetId: str
    projectId: str

class Table(typing_extensions.TypedDict, total=False):
    type: str
    selfLink: str
    timePartitioning: TimePartitioning
    numRows: str
    description: str
    streamingBuffer: Streamingbuffer
    rangePartitioning: RangePartitioning
    clustering: Clustering
    encryptionConfiguration: EncryptionConfiguration
    externalDataConfiguration: ExternalDataConfiguration
    labels: typing.Dict[str, typing.Any]
    schema: TableSchema
    expirationTime: str
    numPhysicalBytes: str
    kind: str
    materializedView: MaterializedViewDefinition
    lastModifiedTime: str
    tableReference: TableReference
    model: ModelDefinition
    numBytes: str
    etag: str
    creationTime: str
    id: str
    requirePartitionFilter: bool
    snapshotDefinition: SnapshotDefinition
    view: ViewDefinition
    location: str
    numLongTermBytes: str
    friendlyName: str

class TableCell(typing_extensions.TypedDict, total=False):
    v: typing.Any

class JobStatistics3(typing_extensions.TypedDict, total=False):
    inputFileBytes: str
    outputBytes: str
    inputFiles: str
    outputRows: str
    badRecords: str

class TransactionInfo(typing_extensions.TypedDict, total=False):
    transactionId: str

class CsvOptions(typing_extensions.TypedDict, total=False):
    allowJaggedRows: bool
    allowQuotedNewlines: bool
    skipLeadingRows: str
    fieldDelimiter: str
    encoding: str
    quote: str

class ListModelsResponse(typing_extensions.TypedDict, total=False):
    models: typing.List[Model]
    nextPageToken: str

class ScriptStatistics(typing_extensions.TypedDict, total=False):
    stackFrames: typing.List[ScriptStackFrame]
    evaluationKind: str

class Routine(typing.Dict[str, typing.Any]): ...

class ErrorProto(typing_extensions.TypedDict, total=False):
    message: str
    debugInfo: str
    reason: str
    location: str

class ConnectionProperty(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class Dataset(typing_extensions.TypedDict, total=False):
    id: str
    defaultTableExpirationMs: str
    access: typing.List[typing.Dict[str, typing.Any]]
    etag: str
    defaultEncryptionConfiguration: EncryptionConfiguration
    datasetReference: DatasetReference
    satisfiesPZS: bool
    description: str
    labels: typing.Dict[str, typing.Any]
    friendlyName: str
    kind: str
    creationTime: str
    selfLink: str
    defaultPartitionExpirationMs: str
    location: str
    lastModifiedTime: str

class EvaluationMetrics(typing_extensions.TypedDict, total=False):
    multiClassClassificationMetrics: MultiClassClassificationMetrics
    binaryClassificationMetrics: BinaryClassificationMetrics
    clusteringMetrics: ClusteringMetrics
    regressionMetrics: RegressionMetrics
    rankingMetrics: RankingMetrics
    arimaForecastingMetrics: ArimaForecastingMetrics

class QueryTimelineSample(typing_extensions.TypedDict, total=False):
    elapsedMs: str
    activeUnits: str
    pendingUnits: str
    totalSlotMs: str
    completedUnits: str

class TableDataInsertAllResponse(typing_extensions.TypedDict, total=False):
    insertErrors: typing.List[typing.Dict[str, typing.Any]]
    kind: str

class TrainingRun(typing_extensions.TypedDict, total=False):
    startTime: str
    dataSplitResult: DataSplitResult
    results: typing.List[IterationResult]
    evaluationMetrics: EvaluationMetrics
    trainingOptions: TrainingOptions

class GoogleSheetsOptions(typing_extensions.TypedDict, total=False):
    skipLeadingRows: str
    range: str

class JobConfigurationTableCopy(typing_extensions.TypedDict, total=False):
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationExpirationTime: typing.Any
    sourceTable: TableReference
    writeDisposition: str
    destinationTable: TableReference
    operationType: str
    sourceTables: typing.List[TableReference]
    createDisposition: str

class JsonObject(typing.Dict[str, typing.Any]): ...

class Job(typing_extensions.TypedDict, total=False):
    jobReference: JobReference
    etag: str
    user_email: str
    id: str
    configuration: JobConfiguration
    status: JobStatus
    selfLink: str
    kind: str
    statistics: JobStatistics

class BigtableColumnFamily(typing_extensions.TypedDict, total=False):
    encoding: str
    onlyReadLatest: bool
    familyId: str
    type: str
    columns: typing.List[BigtableColumn]

class QueryParameter(typing.Dict[str, typing.Any]): ...

class ViewDefinition(typing_extensions.TypedDict, total=False):
    useLegacySql: bool
    userDefinedFunctionResources: typing.List[UserDefinedFunctionResource]
    query: str

class TableList(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    tables: typing.List[typing.Dict[str, typing.Any]]
    totalItems: int
    nextPageToken: str

class GetQueryResultsResponse(typing_extensions.TypedDict, total=False):
    etag: str
    numDmlAffectedRows: str
    totalRows: str
    schema: TableSchema
    cacheHit: bool
    errors: typing.List[ErrorProto]
    jobComplete: bool
    totalBytesProcessed: str
    jobReference: JobReference
    pageToken: str
    kind: str
    rows: typing.List[TableRow]

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    version: int
    bindings: typing.List[Binding]
    etag: str

class MaterializedViewDefinition(typing_extensions.TypedDict, total=False):
    refreshIntervalMs: str
    query: str
    enableRefresh: bool
    lastRefreshTime: str

class ArimaOrder(typing_extensions.TypedDict, total=False):
    d: str
    p: str
    q: str

class QueryResponse(typing_extensions.TypedDict, total=False):
    totalBytesProcessed: str
    jobReference: JobReference
    errors: typing.List[ErrorProto]
    schema: TableSchema
    pageToken: str
    numDmlAffectedRows: str
    kind: str
    totalRows: str
    rows: typing.List[TableRow]
    jobComplete: bool
    cacheHit: bool

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    title: str
    location: str

class QueryParameterType(typing.Dict[str, typing.Any]): ...

class JobCancelResponse(typing_extensions.TypedDict, total=False):
    job: Job
    kind: str

class JobConfiguration(typing.Dict[str, typing.Any]): ...
