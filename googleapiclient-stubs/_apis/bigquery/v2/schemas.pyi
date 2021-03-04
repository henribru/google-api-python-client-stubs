import typing

import typing_extensions
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
class Argument(typing_extensions.TypedDict, total=False):
    argumentKind: typing_extensions.Literal[
        "ARGUMENT_KIND_UNSPECIFIED", "FIXED_TYPE", "ANY_TYPE"
    ]
    dataType: StandardSqlDataType
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "IN", "OUT", "INOUT"]
    name: str

@typing.type_check_only
class ArimaCoefficients(typing_extensions.TypedDict, total=False):
    autoRegressiveCoefficients: typing.List[float]
    interceptCoefficient: float
    movingAverageCoefficients: typing.List[float]

@typing.type_check_only
class ArimaFittingMetrics(typing_extensions.TypedDict, total=False):
    aic: float
    logLikelihood: float
    variance: float

@typing.type_check_only
class ArimaForecastingMetrics(typing_extensions.TypedDict, total=False):
    arimaFittingMetrics: typing.List[ArimaFittingMetrics]
    arimaSingleModelForecastingMetrics: typing.List[ArimaSingleModelForecastingMetrics]
    hasDrift: typing.List[bool]
    nonSeasonalOrder: typing.List[ArimaOrder]
    seasonalPeriods: typing.List[str]
    timeSeriesId: typing.List[str]

@typing.type_check_only
class ArimaModelInfo(typing_extensions.TypedDict, total=False):
    arimaCoefficients: ArimaCoefficients
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: typing.List[str]
    timeSeriesId: str

@typing.type_check_only
class ArimaOrder(typing_extensions.TypedDict, total=False):
    d: str
    p: str
    q: str

@typing.type_check_only
class ArimaResult(typing_extensions.TypedDict, total=False):
    arimaModelInfo: typing.List[ArimaModelInfo]
    seasonalPeriods: typing.List[str]

@typing.type_check_only
class ArimaSingleModelForecastingMetrics(typing_extensions.TypedDict, total=False):
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: typing.List[str]
    timeSeriesId: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

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
    columns: typing.List[BigtableColumn]
    encoding: str
    familyId: str
    onlyReadLatest: bool
    type: str

@typing.type_check_only
class BigtableOptions(typing_extensions.TypedDict, total=False):
    columnFamilies: typing.List[BigtableColumnFamily]
    ignoreUnspecifiedColumnFamilies: bool
    readRowkeyAsString: bool

@typing.type_check_only
class BinaryClassificationMetrics(typing_extensions.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    binaryConfusionMatrixList: typing.List[BinaryConfusionMatrix]
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
    members: typing.List[str]
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
    iterationResults: typing.List[BqmlIterationResult]
    startTime: str
    state: str
    trainingOptions: typing.Dict[str, typing.Any]

@typing.type_check_only
class CategoricalValue(typing_extensions.TypedDict, total=False):
    categoryCounts: typing.List[CategoryCount]

@typing.type_check_only
class CategoryCount(typing_extensions.TypedDict, total=False):
    category: str
    count: str

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    centroidId: str
    count: str
    featureValues: typing.List[FeatureValue]

@typing.type_check_only
class ClusterInfo(typing_extensions.TypedDict, total=False):
    centroidId: str
    clusterRadius: float
    clusterSize: str

@typing.type_check_only
class Clustering(typing_extensions.TypedDict, total=False):
    fields: typing.List[str]

@typing.type_check_only
class ClusteringMetrics(typing_extensions.TypedDict, total=False):
    clusters: typing.List[Cluster]
    daviesBouldinIndex: float
    meanSquaredDistance: float

@typing.type_check_only
class ConfusionMatrix(typing_extensions.TypedDict, total=False):
    confidenceThreshold: float
    rows: typing.List[Row]

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
    quote: str
    skipLeadingRows: str

@typing.type_check_only
class DataSplitResult(typing_extensions.TypedDict, total=False):
    evaluationTable: TableReference
    trainingTable: TableReference

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    access: typing.List[typing.Dict[str, typing.Any]]
    creationTime: str
    datasetReference: DatasetReference
    defaultEncryptionConfiguration: EncryptionConfiguration
    defaultPartitionExpirationMs: str
    defaultTableExpirationMs: str
    description: str
    etag: str
    friendlyName: str
    id: str
    kind: str
    labels: typing.Dict[str, typing.Any]
    lastModifiedTime: str
    location: str
    satisfiesPZS: bool
    selfLink: str

@typing.type_check_only
class DatasetAccessEntry(typing_extensions.TypedDict, total=False):
    dataset: DatasetReference
    target_types: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class DatasetList(typing_extensions.TypedDict, total=False):
    datasets: typing.List[typing.Dict[str, typing.Any]]
    etag: str
    kind: str
    nextPageToken: str

@typing.type_check_only
class DatasetReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str

@typing.type_check_only
class DestinationTableProperties(typing_extensions.TypedDict, total=False):
    description: str
    friendlyName: str
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class DimensionalityReductionMetrics(typing_extensions.TypedDict, total=False):
    totalExplainedVarianceRatio: float

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
    computeMsAvg: str
    computeMsMax: str
    computeRatioAvg: float
    computeRatioMax: float
    endMs: str
    id: str
    inputStages: typing.List[str]
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
    steps: typing.List[ExplainQueryStep]
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
    substeps: typing.List[str]

@typing.type_check_only
class Explanation(typing_extensions.TypedDict, total=False):
    attribution: float
    featureName: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalDataConfiguration(typing_extensions.TypedDict, total=False):
    autodetect: bool
    bigtableOptions: BigtableOptions
    compression: str
    connectionId: str
    csvOptions: CsvOptions
    googleSheetsOptions: GoogleSheetsOptions
    hivePartitioningOptions: HivePartitioningOptions
    ignoreUnknownValues: bool
    maxBadRecords: int
    parquetOptions: ParquetOptions
    schema: TableSchema
    sourceFormat: str
    sourceUris: typing.List[str]

@typing.type_check_only
class FeatureValue(typing_extensions.TypedDict, total=False):
    categoricalValue: CategoricalValue
    featureColumn: str
    numericalValue: float

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GetQueryResultsResponse(typing_extensions.TypedDict, total=False):
    cacheHit: bool
    errors: typing.List[ErrorProto]
    etag: str
    jobComplete: bool
    jobReference: JobReference
    kind: str
    numDmlAffectedRows: str
    pageToken: str
    rows: typing.List[TableRow]
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
    explanations: typing.List[Explanation]

@typing.type_check_only
class GoogleSheetsOptions(typing_extensions.TypedDict, total=False):
    range: str
    skipLeadingRows: str

@typing.type_check_only
class HivePartitioningOptions(typing_extensions.TypedDict, total=False):
    mode: str
    requirePartitionFilter: bool
    sourceUriPrefix: str

@typing.type_check_only
class IterationResult(typing_extensions.TypedDict, total=False):
    arimaResult: ArimaResult
    clusterInfos: typing.List[ClusterInfo]
    durationMs: str
    evalLoss: float
    index: int
    learnRate: float
    principalComponentInfos: typing.List[PrincipalComponentInfo]
    trainingLoss: float

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    configuration: JobConfiguration
    etag: str
    id: str
    jobReference: JobReference
    kind: str
    selfLink: str
    statistics: JobStatistics
    status: JobStatus
    user_email: str

@typing.type_check_only
class JobCancelResponse(typing_extensions.TypedDict, total=False):
    job: Job
    kind: str

@typing.type_check_only
class JobConfiguration(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JobConfigurationExtract(typing_extensions.TypedDict, total=False):
    compression: str
    destinationFormat: str
    destinationUri: str
    destinationUris: typing.List[str]
    fieldDelimiter: str
    printHeader: bool
    sourceModel: ModelReference
    sourceTable: TableReference
    useAvroLogicalTypes: bool

@typing.type_check_only
class JobConfigurationLoad(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JobConfigurationQuery(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JobConfigurationTableCopy(typing_extensions.TypedDict, total=False):
    createDisposition: str
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationExpirationTime: typing.Any
    destinationTable: TableReference
    operationType: str
    sourceTable: TableReference
    sourceTables: typing.List[TableReference]
    writeDisposition: str

@typing.type_check_only
class JobList(typing_extensions.TypedDict, total=False):
    etag: str
    jobs: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    nextPageToken: str

@typing.type_check_only
class JobReference(typing_extensions.TypedDict, total=False):
    jobId: str
    location: str
    projectId: str

@typing.type_check_only
class JobStatistics(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JobStatistics2(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JobStatistics3(typing_extensions.TypedDict, total=False):
    badRecords: str
    inputFileBytes: str
    inputFiles: str
    outputBytes: str
    outputRows: str

@typing.type_check_only
class JobStatistics4(typing_extensions.TypedDict, total=False):
    destinationUriFileCounts: typing.List[str]
    inputBytes: str

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    errorResult: ErrorProto
    errors: typing.List[ErrorProto]
    state: str

@typing.type_check_only
class JsonObject(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class JsonValue(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ListModelsResponse(typing_extensions.TypedDict, total=False):
    models: typing.List[Model]
    nextPageToken: str

@typing.type_check_only
class ListRoutinesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    routines: typing.List[Routine]

@typing.type_check_only
class ListRowAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rowAccessPolicies: typing.List[RowAccessPolicy]

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    legacyLocationId: str

@typing.type_check_only
class MaterializedViewDefinition(typing_extensions.TypedDict, total=False):
    enableRefresh: bool
    lastRefreshTime: str
    query: str
    refreshIntervalMs: str

@typing.type_check_only
class Model(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ModelDefinition(typing_extensions.TypedDict, total=False):
    modelOptions: typing.Dict[str, typing.Any]
    trainingRuns: typing.List[BqmlTrainingRun]

@typing.type_check_only
class ModelReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    modelId: str
    projectId: str

@typing.type_check_only
class MultiClassClassificationMetrics(typing_extensions.TypedDict, total=False):
    aggregateClassificationMetrics: AggregateClassificationMetrics
    confusionMatrixList: typing.List[ConfusionMatrix]

@typing.type_check_only
class ParquetOptions(typing_extensions.TypedDict, total=False):
    enableListInference: bool
    enumAsString: bool

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrincipalComponentInfo(typing_extensions.TypedDict, total=False):
    cumulativeExplainedVarianceRatio: float
    explainedVariance: float
    explainedVarianceRatio: float
    principalComponentId: str

@typing.type_check_only
class ProjectList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    projects: typing.List[typing.Dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class ProjectReference(typing_extensions.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class QueryParameter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class QueryParameterType(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class QueryParameterValue(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class QueryRequest(typing_extensions.TypedDict, total=False):
    connectionProperties: typing.List[ConnectionProperty]
    defaultDataset: DatasetReference
    dryRun: bool
    kind: str
    labels: typing.Dict[str, typing.Any]
    location: str
    maxResults: int
    maximumBytesBilled: str
    parameterMode: str
    preserveNulls: bool
    query: str
    queryParameters: typing.List[QueryParameter]
    requestId: str
    timeoutMs: int
    useLegacySql: bool
    useQueryCache: bool

@typing.type_check_only
class QueryResponse(typing_extensions.TypedDict, total=False):
    cacheHit: bool
    errors: typing.List[ErrorProto]
    jobComplete: bool
    jobReference: JobReference
    kind: str
    numDmlAffectedRows: str
    pageToken: str
    rows: typing.List[TableRow]
    schema: TableSchema
    totalBytesProcessed: str
    totalRows: str

@typing.type_check_only
class QueryTimelineSample(typing_extensions.TypedDict, total=False):
    activeUnits: str
    completedUnits: str
    elapsedMs: str
    pendingUnits: str
    totalSlotMs: str

@typing.type_check_only
class RangePartitioning(typing_extensions.TypedDict, total=False):
    field: str
    range: typing.Dict[str, typing.Any]

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
class Routine(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class RoutineReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    routineId: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    actualLabel: str
    entries: typing.List[Entry]

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
class ScriptStackFrame(typing_extensions.TypedDict, total=False):
    endColumn: int
    endLine: int
    procedureId: str
    startColumn: int
    startLine: int
    text: str

@typing.type_check_only
class ScriptStatistics(typing_extensions.TypedDict, total=False):
    evaluationKind: str
    stackFrames: typing.List[ScriptStackFrame]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SnapshotDefinition(typing_extensions.TypedDict, total=False):
    baseTableReference: TableReference
    snapshotTime: str

@typing.type_check_only
class StandardSqlDataType(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class StandardSqlField(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class StandardSqlStructType(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Streamingbuffer(typing_extensions.TypedDict, total=False):
    estimatedBytes: str
    estimatedRows: str
    oldestEntryTime: str

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    clustering: Clustering
    creationTime: str
    description: str
    encryptionConfiguration: EncryptionConfiguration
    etag: str
    expirationTime: str
    externalDataConfiguration: ExternalDataConfiguration
    friendlyName: str
    id: str
    kind: str
    labels: typing.Dict[str, typing.Any]
    lastModifiedTime: str
    location: str
    materializedView: MaterializedViewDefinition
    model: ModelDefinition
    numBytes: str
    numLongTermBytes: str
    numPhysicalBytes: str
    numRows: str
    rangePartitioning: RangePartitioning
    requirePartitionFilter: bool
    schema: TableSchema
    selfLink: str
    snapshotDefinition: SnapshotDefinition
    streamingBuffer: Streamingbuffer
    tableReference: TableReference
    timePartitioning: TimePartitioning
    type: str
    view: ViewDefinition

@typing.type_check_only
class TableCell(typing_extensions.TypedDict, total=False):
    v: typing.Any

@typing.type_check_only
class TableDataInsertAllRequest(typing_extensions.TypedDict, total=False):
    ignoreUnknownValues: bool
    kind: str
    rows: typing.List[typing.Dict[str, typing.Any]]
    skipInvalidRows: bool
    templateSuffix: str

@typing.type_check_only
class TableDataInsertAllResponse(typing_extensions.TypedDict, total=False):
    insertErrors: typing.List[typing.Dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class TableDataList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    pageToken: str
    rows: typing.List[TableRow]
    totalRows: str

@typing.type_check_only
class TableFieldSchema(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TableList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    tables: typing.List[typing.Dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class TableReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class TableRow(typing_extensions.TypedDict, total=False):
    f: typing.List[TableCell]

@typing.type_check_only
class TableSchema(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TimePartitioning(typing_extensions.TypedDict, total=False):
    expirationMs: str
    field: str
    requirePartitionFilter: bool
    type: str

@typing.type_check_only
class TrainingOptions(typing_extensions.TypedDict, total=False):
    autoArima: bool
    autoArimaMaxOrder: str
    batchSize: str
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
    distanceType: typing_extensions.Literal[
        "DISTANCE_TYPE_UNSPECIFIED", "EUCLIDEAN", "COSINE"
    ]
    dropout: float
    earlyStop: bool
    feedbackType: typing_extensions.Literal[
        "FEEDBACK_TYPE_UNSPECIFIED", "IMPLICIT", "EXPLICIT"
    ]
    hiddenUnits: typing.List[str]
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
    horizon: str
    includeDrift: bool
    initialLearnRate: float
    inputLabelColumns: typing.List[str]
    itemColumn: str
    kmeansInitializationColumn: str
    kmeansInitializationMethod: typing_extensions.Literal[
        "KMEANS_INITIALIZATION_METHOD_UNSPECIFIED",
        "RANDOM",
        "CUSTOM",
        "KMEANS_PLUS_PLUS",
    ]
    l1Regularization: float
    l2Regularization: float
    labelClassWeights: typing.Dict[str, typing.Any]
    learnRate: float
    learnRateStrategy: typing_extensions.Literal[
        "LEARN_RATE_STRATEGY_UNSPECIFIED", "LINE_SEARCH", "CONSTANT"
    ]
    lossType: typing_extensions.Literal[
        "LOSS_TYPE_UNSPECIFIED", "MEAN_SQUARED_LOSS", "MEAN_LOG_LOSS"
    ]
    maxIterations: str
    maxTreeDepth: str
    minRelativeProgress: float
    minSplitLoss: float
    modelUri: str
    nonSeasonalOrder: ArimaOrder
    numClusters: str
    numFactors: str
    optimizationStrategy: typing_extensions.Literal[
        "OPTIMIZATION_STRATEGY_UNSPECIFIED", "BATCH_GRADIENT_DESCENT", "NORMAL_EQUATION"
    ]
    preserveInputStructs: bool
    subsample: float
    timeSeriesDataColumn: str
    timeSeriesIdColumn: str
    timeSeriesTimestampColumn: str
    userColumn: str
    walsAlpha: float
    warmStart: bool

@typing.type_check_only
class TrainingRun(typing_extensions.TypedDict, total=False):
    dataSplitResult: DataSplitResult
    evaluationMetrics: EvaluationMetrics
    globalExplanations: typing.List[GlobalExplanation]
    results: typing.List[IterationResult]
    startTime: str
    trainingOptions: TrainingOptions

@typing.type_check_only
class TransactionInfo(typing_extensions.TypedDict, total=False):
    transactionId: str

@typing.type_check_only
class UserDefinedFunctionResource(typing_extensions.TypedDict, total=False):
    inlineCode: str
    resourceUri: str

@typing.type_check_only
class ViewDefinition(typing_extensions.TypedDict, total=False):
    query: str
    useLegacySql: bool
    userDefinedFunctionResources: typing.List[UserDefinedFunctionResource]
