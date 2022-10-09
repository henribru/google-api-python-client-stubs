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
class Argument(typing_extensions.TypedDict, total=False):
    argumentKind: typing_extensions.Literal[
        "ARGUMENT_KIND_UNSPECIFIED", "FIXED_TYPE", "ANY_TYPE"
    ]
    dataType: StandardSqlDataType
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
    seasonalPeriods: _list[str]
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
    seasonalPeriods: _list[str]
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
    seasonalPeriods: _list[str]

@typing.type_check_only
class ArimaSingleModelForecastingMetrics(typing_extensions.TypedDict, total=False):
    arimaFittingMetrics: ArimaFittingMetrics
    hasDrift: bool
    hasHolidayEffect: bool
    hasSpikesAndDips: bool
    hasStepChanges: bool
    nonSeasonalOrder: ArimaOrder
    seasonalPeriods: _list[str]
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
    code: str
    message: str

@typing.type_check_only
class BiEngineStatistics(typing_extensions.TypedDict, total=False):
    biEngineMode: str
    biEngineReasons: _list[BiEngineReason]

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
    null_marker: str
    preserveAsciiControlCharacters: bool
    quote: str
    skipLeadingRows: str

@typing.type_check_only
class DataMaskingStatistics(typing_extensions.TypedDict, total=False):
    dataMaskingApplied: bool

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
    defaultTableExpirationMs: str
    description: str
    etag: str
    friendlyName: str
    id: str
    isCaseInsensitive: bool
    kind: str
    labels: dict[str, typing.Any]
    lastModifiedTime: str
    location: str
    maxTimeTravelHours: str
    satisfiesPzs: bool
    selfLink: str
    tags: _list[dict[str, typing.Any]]

@typing.type_check_only
class DatasetAccessEntry(typing_extensions.TypedDict, total=False):
    dataset: DatasetReference
    targetTypes: _list[str]

@typing.type_check_only
class DatasetList(typing_extensions.TypedDict, total=False):
    datasets: _list[dict[str, typing.Any]]
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
    expirationTime: str
    friendlyName: str
    labels: dict[str, typing.Any]

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
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalDataConfiguration(typing_extensions.TypedDict, total=False):
    autodetect: bool
    avroOptions: AvroOptions
    bigtableOptions: BigtableOptions
    compression: str
    connectionId: str
    csvOptions: CsvOptions
    decimalTargetTypes: _list[str]
    googleSheetsOptions: GoogleSheetsOptions
    hivePartitioningOptions: HivePartitioningOptions
    ignoreUnknownValues: bool
    maxBadRecords: int
    parquetOptions: ParquetOptions
    referenceFileSchemaUri: str
    schema: TableSchema
    sourceFormat: str
    sourceUris: _list[str]

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
class HivePartitioningOptions(typing_extensions.TypedDict, total=False):
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
    base_table: TableReference
    code: str
    index_name: str
    message: str

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
    durationMs: str
    evalLoss: float
    index: int
    learnRate: float
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
class JobConfiguration(dict[str, typing.Any]): ...

@typing.type_check_only
class JobConfigurationExtract(typing_extensions.TypedDict, total=False):
    compression: str
    destinationFormat: str
    destinationUri: str
    destinationUris: _list[str]
    fieldDelimiter: str
    printHeader: bool
    sourceModel: ModelReference
    sourceTable: TableReference
    useAvroLogicalTypes: bool

@typing.type_check_only
class JobConfigurationLoad(dict[str, typing.Any]): ...

@typing.type_check_only
class JobConfigurationQuery(dict[str, typing.Any]): ...

@typing.type_check_only
class JobConfigurationTableCopy(typing_extensions.TypedDict, total=False):
    createDisposition: str
    destinationEncryptionConfiguration: EncryptionConfiguration
    destinationExpirationTime: typing.Any
    destinationTable: TableReference
    operationType: str
    sourceTable: TableReference
    sourceTables: _list[TableReference]
    writeDisposition: str

@typing.type_check_only
class JobList(typing_extensions.TypedDict, total=False):
    etag: str
    jobs: _list[dict[str, typing.Any]]
    kind: str
    nextPageToken: str

@typing.type_check_only
class JobReference(typing_extensions.TypedDict, total=False):
    jobId: str
    location: str
    projectId: str

@typing.type_check_only
class JobStatistics(dict[str, typing.Any]): ...

@typing.type_check_only
class JobStatistics2(dict[str, typing.Any]): ...

@typing.type_check_only
class JobStatistics3(typing_extensions.TypedDict, total=False):
    badRecords: str
    inputFileBytes: str
    inputFiles: str
    outputBytes: str
    outputRows: str

@typing.type_check_only
class JobStatistics4(typing_extensions.TypedDict, total=False):
    destinationUriFileCounts: _list[str]
    inputBytes: str

@typing.type_check_only
class JobStatistics5(typing_extensions.TypedDict, total=False):
    copied_logical_bytes: str
    copied_rows: str

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    errorResult: ErrorProto
    errors: _list[ErrorProto]
    state: str

@typing.type_check_only
class JsonObject(dict[str, typing.Any]): ...

@typing.type_check_only
class JsonValue(dict[str, typing.Any]): ...

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
class LocationMetadata(typing_extensions.TypedDict, total=False):
    legacyLocationId: str

@typing.type_check_only
class MaterializedViewDefinition(typing_extensions.TypedDict, total=False):
    enableRefresh: bool
    lastRefreshTime: str
    maxStaleness: str
    query: str
    refreshIntervalMs: str

@typing.type_check_only
class MlStatistics(typing_extensions.TypedDict, total=False):
    iterationResults: _list[IterationResult]
    maxIterations: str

@typing.type_check_only
class Model(dict[str, typing.Any]): ...

@typing.type_check_only
class ModelDefinition(typing_extensions.TypedDict, total=False):
    modelOptions: dict[str, typing.Any]
    trainingRuns: _list[BqmlTrainingRun]

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
class QueryParameter(dict[str, typing.Any]): ...

@typing.type_check_only
class QueryParameterType(dict[str, typing.Any]): ...

@typing.type_check_only
class QueryParameterValue(dict[str, typing.Any]): ...

@typing.type_check_only
class QueryRequest(typing_extensions.TypedDict, total=False):
    connectionProperties: _list[ConnectionProperty]
    createSession: bool
    defaultDataset: DatasetReference
    dryRun: bool
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
    jobReference: JobReference
    kind: str
    numDmlAffectedRows: str
    pageToken: str
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
class Routine(dict[str, typing.Any]): ...

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
    stackFrames: _list[ScriptStackFrame]

@typing.type_check_only
class SearchStatistics(typing_extensions.TypedDict, total=False):
    indexUnusedReason: _list[IndexUnusedReason]
    indexUsageMode: str

@typing.type_check_only
class SessionInfo(typing_extensions.TypedDict, total=False):
    sessionId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SnapshotDefinition(typing_extensions.TypedDict, total=False):
    baseTableReference: TableReference
    snapshotTime: str

@typing.type_check_only
class SparkLoggingInfo(typing_extensions.TypedDict, total=False):
    project_id: str
    resource_type: str

@typing.type_check_only
class SparkOptions(typing_extensions.TypedDict, total=False):
    archiveUris: _list[str]
    connection: str
    containerImage: str
    fileUris: _list[str]
    jarUris: _list[str]
    mainFileUri: str
    properties: dict[str, typing.Any]
    pyFileUris: _list[str]
    runtimeVersion: str

@typing.type_check_only
class SparkStatistics(typing_extensions.TypedDict, total=False):
    endpoints: dict[str, typing.Any]
    logging_info: SparkLoggingInfo
    spark_job_id: str
    spark_job_location: str

@typing.type_check_only
class StandardSqlDataType(dict[str, typing.Any]): ...

@typing.type_check_only
class StandardSqlField(dict[str, typing.Any]): ...

@typing.type_check_only
class StandardSqlStructType(dict[str, typing.Any]): ...

@typing.type_check_only
class StandardSqlTableType(dict[str, typing.Any]): ...

@typing.type_check_only
class Streamingbuffer(typing_extensions.TypedDict, total=False):
    estimatedBytes: str
    estimatedRows: str
    oldestEntryTime: str

@typing.type_check_only
class StringHparamSearchSpace(typing_extensions.TypedDict, total=False):
    candidates: _list[str]

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    cloneDefinition: CloneDefinition
    clustering: Clustering
    creationTime: str
    defaultCollation: str
    description: str
    encryptionConfiguration: EncryptionConfiguration
    etag: str
    expirationTime: str
    externalDataConfiguration: ExternalDataConfiguration
    friendlyName: str
    id: str
    kind: str
    labels: dict[str, typing.Any]
    lastModifiedTime: str
    location: str
    materializedView: MaterializedViewDefinition
    maxStaleness: str
    model: ModelDefinition
    numBytes: str
    numLongTermBytes: str
    numPhysicalBytes: str
    numRows: str
    num_active_logical_bytes: str
    num_active_physical_bytes: str
    num_long_term_logical_bytes: str
    num_long_term_physical_bytes: str
    num_partitions: str
    num_time_travel_physical_bytes: str
    num_total_logical_bytes: str
    num_total_physical_bytes: str
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
    rows: _list[dict[str, typing.Any]]
    skipInvalidRows: bool
    templateSuffix: str

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
class TableFieldSchema(dict[str, typing.Any]): ...

@typing.type_check_only
class TableList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    tables: _list[dict[str, typing.Any]]
    totalItems: int

@typing.type_check_only
class TableReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class TableRow(typing_extensions.TypedDict, total=False):
    f: _list[TableCell]

@typing.type_check_only
class TableSchema(dict[str, typing.Any]): ...

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
    adjustStepChanges: bool
    autoArima: bool
    autoArimaMaxOrder: str
    batchSize: str
    boosterType: typing_extensions.Literal["BOOSTER_TYPE_UNSPECIFIED", "GBTREE", "DART"]
    calculatePValues: bool
    cleanSpikesAndDips: bool
    colorSpace: typing_extensions.Literal[
        "COLOR_SPACE_UNSPECIFIED", "RGB", "HSV", "YIQ", "YUV", "GRAYSCALE"
    ]
    colsampleBylevel: float
    colsampleBynode: float
    colsampleBytree: float
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
    distanceType: typing_extensions.Literal[
        "DISTANCE_TYPE_UNSPECIFIED", "EUCLIDEAN", "COSINE"
    ]
    dropout: float
    earlyStop: bool
    enableGlobalExplain: bool
    feedbackType: typing_extensions.Literal[
        "FEEDBACK_TYPE_UNSPECIFIED", "IMPLICIT", "EXPLICIT"
    ]
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
    horizon: str
    hparamTuningObjectives: _list[str]
    includeDrift: bool
    initialLearnRate: float
    inputLabelColumns: _list[str]
    integratedGradientsNumSteps: str
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
    minRelativeProgress: float
    minSplitLoss: float
    minTimeSeriesLength: str
    minTreeChildWeight: str
    modelUri: str
    nonSeasonalOrder: ArimaOrder
    numClusters: str
    numFactors: str
    numParallelTree: str
    numTrials: str
    optimizationStrategy: typing_extensions.Literal[
        "OPTIMIZATION_STRATEGY_UNSPECIFIED", "BATCH_GRADIENT_DESCENT", "NORMAL_EQUATION"
    ]
    preserveInputStructs: bool
    sampledShapleyNumPaths: str
    subsample: float
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
    walsAlpha: float
    warmStart: bool

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
class UserDefinedFunctionResource(typing_extensions.TypedDict, total=False):
    inlineCode: str
    resourceUri: str

@typing.type_check_only
class ViewDefinition(typing_extensions.TypedDict, total=False):
    query: str
    useExplicitColumnNames: bool
    useLegacySql: bool
    userDefinedFunctionResources: _list[UserDefinedFunctionResource]
