import typing

import typing_extensions

class GooglePrivacyDlpV2StoredInfoTypeConfig(typing_extensions.TypedDict, total=False):
    regex: GooglePrivacyDlpV2Regex
    dictionary: GooglePrivacyDlpV2Dictionary
    description: str
    displayName: str
    largeCustomDictionary: GooglePrivacyDlpV2LargeCustomDictionaryConfig

class GooglePrivacyDlpV2StorageConfig(typing_extensions.TypedDict, total=False):
    bigQueryOptions: GooglePrivacyDlpV2BigQueryOptions
    cloudStorageOptions: GooglePrivacyDlpV2CloudStorageOptions
    hybridOptions: GooglePrivacyDlpV2HybridOptions
    timespanConfig: GooglePrivacyDlpV2TimespanConfig
    datastoreOptions: GooglePrivacyDlpV2DatastoreOptions

class GooglePrivacyDlpV2DeltaPresenceEstimationConfig(
    typing_extensions.TypedDict, total=False
):
    auxiliaryTables: typing.List[GooglePrivacyDlpV2StatisticalTable]
    regionCode: str
    quasiIds: typing.List[GooglePrivacyDlpV2QuasiId]

class GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplate: GooglePrivacyDlpV2DeidentifyTemplate
    updateMask: str

class GooglePrivacyDlpV2RedactImageRequest(typing_extensions.TypedDict, total=False):
    imageRedactionConfigs: typing.List[GooglePrivacyDlpV2ImageRedactionConfig]
    byteItem: GooglePrivacyDlpV2ByteContentItem
    includeFindings: bool
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    locationId: str

class GooglePrivacyDlpV2DatastoreKey(typing_extensions.TypedDict, total=False):
    entityKey: GooglePrivacyDlpV2Key

class GooglePrivacyDlpV2RecordLocation(typing_extensions.TypedDict, total=False):
    fieldId: GooglePrivacyDlpV2FieldId
    tableLocation: GooglePrivacyDlpV2TableLocation
    recordKey: GooglePrivacyDlpV2RecordKey

class GooglePrivacyDlpV2CreateDeidentifyTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplate: GooglePrivacyDlpV2DeidentifyTemplate
    templateId: str
    locationId: str

class GooglePrivacyDlpV2UpdateJobTriggerRequest(
    typing_extensions.TypedDict, total=False
):
    jobTrigger: GooglePrivacyDlpV2JobTrigger
    updateMask: str

class GooglePrivacyDlpV2LDiversityConfig(typing_extensions.TypedDict, total=False):
    quasiIds: typing.List[GooglePrivacyDlpV2FieldId]
    sensitiveAttribute: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2CreateDlpJobRequest(typing_extensions.TypedDict, total=False):
    riskJob: GooglePrivacyDlpV2RiskAnalysisJobConfig
    inspectJob: GooglePrivacyDlpV2InspectJobConfig
    locationId: str
    jobId: str

class GooglePrivacyDlpV2PublishToStackdriver(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2InspectTemplate(typing_extensions.TypedDict, total=False):
    displayName: str
    createTime: str
    name: str
    description: str
    updateTime: str
    inspectConfig: GooglePrivacyDlpV2InspectConfig

class GooglePrivacyDlpV2ImageLocation(typing_extensions.TypedDict, total=False):
    boundingBoxes: typing.List[GooglePrivacyDlpV2BoundingBox]

class GooglePrivacyDlpV2Trigger(typing_extensions.TypedDict, total=False):
    manual: GooglePrivacyDlpV2Manual
    schedule: GooglePrivacyDlpV2Schedule

class GooglePrivacyDlpV2StoredType(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str

class GooglePrivacyDlpV2KAnonymityResult(typing_extensions.TypedDict, total=False):
    equivalenceClassHistogramBuckets: typing.List[
        GooglePrivacyDlpV2KAnonymityHistogramBucket
    ]

class GooglePrivacyDlpV2HybridContentItem(typing_extensions.TypedDict, total=False):
    item: GooglePrivacyDlpV2ContentItem
    findingDetails: GooglePrivacyDlpV2HybridFindingDetails

class GooglePrivacyDlpV2KAnonymityConfig(typing_extensions.TypedDict, total=False):
    entityId: GooglePrivacyDlpV2EntityId
    quasiIds: typing.List[GooglePrivacyDlpV2FieldId]

class GooglePrivacyDlpV2KindExpression(typing_extensions.TypedDict, total=False):
    name: str

class GooglePrivacyDlpV2CreateJobTriggerRequest(
    typing_extensions.TypedDict, total=False
):
    triggerId: str
    locationId: str
    jobTrigger: GooglePrivacyDlpV2JobTrigger

class GooglePrivacyDlpV2DateTime(typing_extensions.TypedDict, total=False):
    timeZone: GooglePrivacyDlpV2TimeZone
    time: GoogleTypeTimeOfDay
    date: GoogleTypeDate
    dayOfWeek: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]

class GooglePrivacyDlpV2RiskAnalysisJobConfig(typing_extensions.TypedDict, total=False):
    sourceTable: GooglePrivacyDlpV2BigQueryTable
    actions: typing.List[GooglePrivacyDlpV2Action]
    privacyMetric: GooglePrivacyDlpV2PrivacyMetric

class GooglePrivacyDlpV2CategoricalStatsResult(
    typing_extensions.TypedDict, total=False
):
    valueFrequencyHistogramBuckets: typing.List[
        GooglePrivacyDlpV2CategoricalStatsHistogramBucket
    ]

class GooglePrivacyDlpV2InfoTypeDescription(typing_extensions.TypedDict, total=False):
    name: str
    description: str
    displayName: str
    supportedBy: typing.List[str]

class GooglePrivacyDlpV2LargeCustomDictionaryConfig(
    typing_extensions.TypedDict, total=False
):
    cloudStorageFileSet: GooglePrivacyDlpV2CloudStorageFileSet
    bigQueryField: GooglePrivacyDlpV2BigQueryField
    outputPath: GooglePrivacyDlpV2CloudStoragePath

class GooglePrivacyDlpV2NumericalStatsResult(typing_extensions.TypedDict, total=False):
    minValue: GooglePrivacyDlpV2Value
    quantileValues: typing.List[GooglePrivacyDlpV2Value]
    maxValue: GooglePrivacyDlpV2Value

class GooglePrivacyDlpV2InspectContentRequest(typing_extensions.TypedDict, total=False):
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    locationId: str
    inspectTemplateName: str
    item: GooglePrivacyDlpV2ContentItem

class GooglePrivacyDlpV2Manual(typing_extensions.TypedDict, total=False): ...

class GooglePrivacyDlpV2Dictionary(typing_extensions.TypedDict, total=False):
    wordList: GooglePrivacyDlpV2WordList
    cloudStoragePath: GooglePrivacyDlpV2CloudStoragePath

class GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails(
    typing_extensions.TypedDict, total=False
):
    requestedSourceTable: GooglePrivacyDlpV2BigQueryTable
    categoricalStatsResult: GooglePrivacyDlpV2CategoricalStatsResult
    requestedPrivacyMetric: GooglePrivacyDlpV2PrivacyMetric
    kAnonymityResult: GooglePrivacyDlpV2KAnonymityResult
    kMapEstimationResult: GooglePrivacyDlpV2KMapEstimationResult
    deltaPresenceEstimationResult: GooglePrivacyDlpV2DeltaPresenceEstimationResult
    requestedOptions: GooglePrivacyDlpV2RequestedRiskAnalysisOptions
    lDiversityResult: GooglePrivacyDlpV2LDiversityResult
    numericalStatsResult: GooglePrivacyDlpV2NumericalStatsResult

class GooglePrivacyDlpV2KmsWrappedCryptoKey(typing_extensions.TypedDict, total=False):
    wrappedKey: str
    cryptoKeyName: str

class GooglePrivacyDlpV2InfoTypeLimit(typing_extensions.TypedDict, total=False):
    maxFindings: int
    infoType: GooglePrivacyDlpV2InfoType

class GooglePrivacyDlpV2InfoTypeTransformation(
    typing_extensions.TypedDict, total=False
):
    primitiveTransformation: GooglePrivacyDlpV2PrimitiveTransformation
    infoTypes: typing.List[GooglePrivacyDlpV2InfoType]

class GooglePrivacyDlpV2StoredInfoType(typing_extensions.TypedDict, total=False):
    pendingVersions: typing.List[GooglePrivacyDlpV2StoredInfoTypeVersion]
    name: str
    currentVersion: GooglePrivacyDlpV2StoredInfoTypeVersion

class GooglePrivacyDlpV2QuasiId(typing_extensions.TypedDict, total=False):
    infoType: GooglePrivacyDlpV2InfoType
    field: GooglePrivacyDlpV2FieldId
    inferred: GoogleProtobufEmpty
    customTag: str

class GooglePrivacyDlpV2CustomInfoType(typing_extensions.TypedDict, total=False):
    detectionRules: typing.List[GooglePrivacyDlpV2DetectionRule]
    regex: GooglePrivacyDlpV2Regex
    infoType: GooglePrivacyDlpV2InfoType
    surrogateType: GooglePrivacyDlpV2SurrogateType
    storedType: GooglePrivacyDlpV2StoredType
    likelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    dictionary: GooglePrivacyDlpV2Dictionary
    exclusionType: typing_extensions.Literal[
        "EXCLUSION_TYPE_UNSPECIFIED", "EXCLUSION_TYPE_EXCLUDE"
    ]

class GooglePrivacyDlpV2ExclusionRule(typing_extensions.TypedDict, total=False):
    regex: GooglePrivacyDlpV2Regex
    excludeInfoTypes: GooglePrivacyDlpV2ExcludeInfoTypes
    matchingType: typing_extensions.Literal[
        "MATCHING_TYPE_UNSPECIFIED",
        "MATCHING_TYPE_FULL_MATCH",
        "MATCHING_TYPE_PARTIAL_MATCH",
        "MATCHING_TYPE_INVERSE_MATCH",
    ]
    dictionary: GooglePrivacyDlpV2Dictionary

class GooglePrivacyDlpV2FileSet(typing_extensions.TypedDict, total=False):
    regexFileSet: GooglePrivacyDlpV2CloudStorageRegexFileSet
    url: str

class GooglePrivacyDlpV2QuasiIdentifierField(typing_extensions.TypedDict, total=False):
    customTag: str
    field: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2InspectJobConfig(typing_extensions.TypedDict, total=False):
    actions: typing.List[GooglePrivacyDlpV2Action]
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    storageConfig: GooglePrivacyDlpV2StorageConfig
    inspectTemplateName: str

class GooglePrivacyDlpV2PrivacyMetric(typing_extensions.TypedDict, total=False):
    kAnonymityConfig: GooglePrivacyDlpV2KAnonymityConfig
    deltaPresenceEstimationConfig: GooglePrivacyDlpV2DeltaPresenceEstimationConfig
    numericalStatsConfig: GooglePrivacyDlpV2NumericalStatsConfig
    kMapEstimationConfig: GooglePrivacyDlpV2KMapEstimationConfig
    lDiversityConfig: GooglePrivacyDlpV2LDiversityConfig
    categoricalStatsConfig: GooglePrivacyDlpV2CategoricalStatsConfig

class GooglePrivacyDlpV2Container(typing_extensions.TypedDict, total=False):
    relativePath: str
    projectId: str
    updateTime: str
    type: str
    version: str
    fullPath: str
    rootPath: str

class GooglePrivacyDlpV2UnwrappedCryptoKey(typing_extensions.TypedDict, total=False):
    key: str

class GooglePrivacyDlpV2KAnonymityHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    equivalenceClassSizeUpperBound: str
    equivalenceClassSizeLowerBound: str
    bucketSize: str
    bucketValues: typing.List[GooglePrivacyDlpV2KAnonymityEquivalenceClass]
    bucketValueCount: str

class GooglePrivacyDlpV2Result(typing_extensions.TypedDict, total=False):
    hybridStats: GooglePrivacyDlpV2HybridInspectStatistics
    infoTypeStats: typing.List[GooglePrivacyDlpV2InfoTypeStats]
    processedBytes: str
    totalEstimatedBytes: str

class GooglePrivacyDlpV2Range(typing_extensions.TypedDict, total=False):
    end: str
    start: str

class GooglePrivacyDlpV2InfoType(typing_extensions.TypedDict, total=False):
    name: str

class GooglePrivacyDlpV2LeaveUntransformed(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2DateShiftConfig(typing_extensions.TypedDict, total=False):
    context: GooglePrivacyDlpV2FieldId
    upperBoundDays: int
    cryptoKey: GooglePrivacyDlpV2CryptoKey
    lowerBoundDays: int

class GooglePrivacyDlpV2CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    charactersToIgnore: typing.List[GooglePrivacyDlpV2CharsToIgnore]
    reverseOrder: bool
    maskingCharacter: str
    numberToMask: int

class GooglePrivacyDlpV2Conditions(typing_extensions.TypedDict, total=False):
    conditions: typing.List[GooglePrivacyDlpV2Condition]

class GooglePrivacyDlpV2FixedSizeBucketingConfig(
    typing_extensions.TypedDict, total=False
):
    lowerBound: GooglePrivacyDlpV2Value
    upperBound: GooglePrivacyDlpV2Value
    bucketSize: float

class GooglePrivacyDlpV2ReidentifyContentRequest(
    typing_extensions.TypedDict, total=False
):
    reidentifyConfig: GooglePrivacyDlpV2DeidentifyConfig
    locationId: str
    inspectTemplateName: str
    reidentifyTemplateName: str
    item: GooglePrivacyDlpV2ContentItem
    inspectConfig: GooglePrivacyDlpV2InspectConfig

class GooglePrivacyDlpV2KMapEstimationQuasiIdValues(
    typing_extensions.TypedDict, total=False
):
    quasiIdsValues: typing.List[GooglePrivacyDlpV2Value]
    estimatedAnonymity: str

class GooglePrivacyDlpV2UpdateInspectTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    inspectTemplate: GooglePrivacyDlpV2InspectTemplate
    updateMask: str

class GooglePrivacyDlpV2MetadataLocation(typing_extensions.TypedDict, total=False):
    storageLabel: GooglePrivacyDlpV2StorageMetadataLabel
    type: typing_extensions.Literal["METADATATYPE_UNSPECIFIED", "STORAGE_METADATA"]

class GooglePrivacyDlpV2RedactConfig(typing_extensions.TypedDict, total=False): ...

class GooglePrivacyDlpV2PrimitiveTransformation(
    typing_extensions.TypedDict, total=False
):
    fixedSizeBucketingConfig: GooglePrivacyDlpV2FixedSizeBucketingConfig
    cryptoReplaceFfxFpeConfig: GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig
    replaceWithInfoTypeConfig: GooglePrivacyDlpV2ReplaceWithInfoTypeConfig
    replaceConfig: GooglePrivacyDlpV2ReplaceValueConfig
    dateShiftConfig: GooglePrivacyDlpV2DateShiftConfig
    redactConfig: GooglePrivacyDlpV2RedactConfig
    cryptoHashConfig: GooglePrivacyDlpV2CryptoHashConfig
    bucketingConfig: GooglePrivacyDlpV2BucketingConfig
    cryptoDeterministicConfig: GooglePrivacyDlpV2CryptoDeterministicConfig
    timePartConfig: GooglePrivacyDlpV2TimePartConfig
    characterMaskConfig: GooglePrivacyDlpV2CharacterMaskConfig

class GooglePrivacyDlpV2LDiversityEquivalenceClass(
    typing_extensions.TypedDict, total=False
):
    quasiIdsValues: typing.List[GooglePrivacyDlpV2Value]
    numDistinctSensitiveValues: str
    topSensitiveValues: typing.List[GooglePrivacyDlpV2ValueFrequency]
    equivalenceClassSize: str

class GooglePrivacyDlpV2Value(typing_extensions.TypedDict, total=False):
    dateValue: GoogleTypeDate
    dayOfWeekValue: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    stringValue: str
    floatValue: float
    timestampValue: str
    booleanValue: bool
    timeValue: GoogleTypeTimeOfDay
    integerValue: str

class GooglePrivacyDlpV2Finding(typing_extensions.TypedDict, total=False):
    location: GooglePrivacyDlpV2Location
    createTime: str
    name: str
    resourceName: str
    quote: str
    jobCreateTime: str
    quoteInfo: GooglePrivacyDlpV2QuoteInfo
    jobName: str
    labels: typing.Dict[str, typing.Any]
    triggerName: str
    likelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    infoType: GooglePrivacyDlpV2InfoType

class GooglePrivacyDlpV2StoredInfoTypeStats(typing_extensions.TypedDict, total=False):
    largeCustomDictionary: GooglePrivacyDlpV2LargeCustomDictionaryStats

class GooglePrivacyDlpV2DeltaPresenceEstimationResult(
    typing_extensions.TypedDict, total=False
):
    deltaPresenceEstimationHistogram: typing.List[
        GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucket
    ]

class GooglePrivacyDlpV2ListDeidentifyTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    deidentifyTemplates: typing.List[GooglePrivacyDlpV2DeidentifyTemplate]

class GooglePrivacyDlpV2HybridInspectDlpJobRequest(
    typing_extensions.TypedDict, total=False
):
    hybridItem: GooglePrivacyDlpV2HybridContentItem

class GooglePrivacyDlpV2DeidentifyContentResponse(
    typing_extensions.TypedDict, total=False
):
    overview: GooglePrivacyDlpV2TransformationOverview
    item: GooglePrivacyDlpV2ContentItem

class GooglePrivacyDlpV2HybridInspectJobTriggerRequest(
    typing_extensions.TypedDict, total=False
):
    hybridItem: GooglePrivacyDlpV2HybridContentItem

class GooglePrivacyDlpV2Error(typing_extensions.TypedDict, total=False):
    details: GoogleRpcStatus
    timestamps: typing.List[str]

class GooglePrivacyDlpV2LDiversityResult(typing_extensions.TypedDict, total=False):
    sensitiveValueFrequencyHistogramBuckets: typing.List[
        GooglePrivacyDlpV2LDiversityHistogramBucket
    ]

class GooglePrivacyDlpV2AuxiliaryTable(typing_extensions.TypedDict, total=False):
    table: GooglePrivacyDlpV2BigQueryTable
    quasiIds: typing.List[GooglePrivacyDlpV2QuasiIdField]
    relativeFrequency: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2CharsToIgnore(typing_extensions.TypedDict, total=False):
    commonCharactersToIgnore: typing_extensions.Literal[
        "COMMON_CHARS_TO_IGNORE_UNSPECIFIED",
        "NUMERIC",
        "ALPHA_UPPER_CASE",
        "ALPHA_LOWER_CASE",
        "PUNCTUATION",
        "WHITESPACE",
    ]
    charactersToSkip: str

class GooglePrivacyDlpV2KMapEstimationHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketValueCount: str
    maxAnonymity: str
    bucketValues: typing.List[GooglePrivacyDlpV2KMapEstimationQuasiIdValues]
    minAnonymity: str
    bucketSize: str

class GooglePrivacyDlpV2ListJobTriggersResponse(
    typing_extensions.TypedDict, total=False
):
    jobTriggers: typing.List[GooglePrivacyDlpV2JobTrigger]
    nextPageToken: str

class GooglePrivacyDlpV2HybridOptions(typing_extensions.TypedDict, total=False):
    requiredFindingLabelKeys: typing.List[str]
    labels: typing.Dict[str, typing.Any]
    tableOptions: GooglePrivacyDlpV2TableOptions
    description: str

class GooglePrivacyDlpV2ThrowError(typing_extensions.TypedDict, total=False): ...

class GooglePrivacyDlpV2Expressions(typing_extensions.TypedDict, total=False):
    logicalOperator: typing_extensions.Literal["LOGICAL_OPERATOR_UNSPECIFIED", "AND"]
    conditions: GooglePrivacyDlpV2Conditions

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GooglePrivacyDlpV2BucketingConfig(typing_extensions.TypedDict, total=False):
    buckets: typing.List[GooglePrivacyDlpV2Bucket]

class GooglePrivacyDlpV2StoredInfoTypeVersion(typing_extensions.TypedDict, total=False):
    errors: typing.List[GooglePrivacyDlpV2Error]
    config: GooglePrivacyDlpV2StoredInfoTypeConfig
    createTime: str
    stats: GooglePrivacyDlpV2StoredInfoTypeStats
    state: typing_extensions.Literal[
        "STORED_INFO_TYPE_STATE_UNSPECIFIED", "PENDING", "READY", "FAILED", "INVALID"
    ]

class GooglePrivacyDlpV2InspectResult(typing_extensions.TypedDict, total=False):
    findingsTruncated: bool
    findings: typing.List[GooglePrivacyDlpV2Finding]

class GooglePrivacyDlpV2KMapEstimationResult(typing_extensions.TypedDict, total=False):
    kMapEstimationHistogram: typing.List[
        GooglePrivacyDlpV2KMapEstimationHistogramBucket
    ]

class GooglePrivacyDlpV2BoundingBox(typing_extensions.TypedDict, total=False):
    top: int
    height: int
    left: int
    width: int

class GooglePrivacyDlpV2ReidentifyContentResponse(
    typing_extensions.TypedDict, total=False
):
    overview: GooglePrivacyDlpV2TransformationOverview
    item: GooglePrivacyDlpV2ContentItem

class GooglePrivacyDlpV2TransformationOverview(
    typing_extensions.TypedDict, total=False
):
    transformedBytes: str
    transformationSummaries: typing.List[GooglePrivacyDlpV2TransformationSummary]

class GooglePrivacyDlpV2KMapEstimationConfig(typing_extensions.TypedDict, total=False):
    quasiIds: typing.List[GooglePrivacyDlpV2TaggedField]
    regionCode: str
    auxiliaryTables: typing.List[GooglePrivacyDlpV2AuxiliaryTable]

class GooglePrivacyDlpV2NumericalStatsConfig(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2CategoricalStatsConfig(
    typing_extensions.TypedDict, total=False
):
    field: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2Schedule(typing_extensions.TypedDict, total=False):
    recurrencePeriodDuration: str

class GooglePrivacyDlpV2HybridFindingDetails(typing_extensions.TypedDict, total=False):
    rowOffset: str
    fileOffset: str
    tableOptions: GooglePrivacyDlpV2TableOptions
    containerDetails: GooglePrivacyDlpV2Container
    labels: typing.Dict[str, typing.Any]

class GooglePrivacyDlpV2PublishSummaryToCscc(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2CloudStorageFileSet(typing_extensions.TypedDict, total=False):
    url: str

class GooglePrivacyDlpV2WordList(typing_extensions.TypedDict, total=False):
    words: typing.List[str]

class GooglePrivacyDlpV2Color(typing_extensions.TypedDict, total=False):
    green: float
    red: float
    blue: float

class GooglePrivacyDlpV2HybridInspectStatistics(
    typing_extensions.TypedDict, total=False
):
    processedCount: str
    abortedCount: str
    pendingCount: str

class GooglePrivacyDlpV2FinishDlpJobRequest(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2OutputStorageConfig(typing_extensions.TypedDict, total=False):
    table: GooglePrivacyDlpV2BigQueryTable
    outputSchema: typing_extensions.Literal[
        "OUTPUT_SCHEMA_UNSPECIFIED",
        "BASIC_COLUMNS",
        "GCS_COLUMNS",
        "DATASTORE_COLUMNS",
        "BIG_QUERY_COLUMNS",
        "ALL_COLUMNS",
    ]

class GooglePrivacyDlpV2EntityId(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId

class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    year: int
    day: int
    month: int

class GooglePrivacyDlpV2BigQueryKey(typing_extensions.TypedDict, total=False):
    rowNumber: str
    tableReference: GooglePrivacyDlpV2BigQueryTable

class GooglePrivacyDlpV2InspectConfig(typing_extensions.TypedDict, total=False):
    minLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    includeQuote: bool
    contentOptions: typing.List[str]
    limits: GooglePrivacyDlpV2FindingLimits
    infoTypes: typing.List[GooglePrivacyDlpV2InfoType]
    customInfoTypes: typing.List[GooglePrivacyDlpV2CustomInfoType]
    ruleSet: typing.List[GooglePrivacyDlpV2InspectionRuleSet]
    excludeInfoTypes: bool

class GooglePrivacyDlpV2Location(typing_extensions.TypedDict, total=False):
    codepointRange: GooglePrivacyDlpV2Range
    byteRange: GooglePrivacyDlpV2Range
    container: GooglePrivacyDlpV2Container
    contentLocations: typing.List[GooglePrivacyDlpV2ContentLocation]

class GooglePrivacyDlpV2DeidentifyTemplate(typing_extensions.TypedDict, total=False):
    displayName: str
    deidentifyConfig: GooglePrivacyDlpV2DeidentifyConfig
    createTime: str
    description: str
    name: str
    updateTime: str

class GooglePrivacyDlpV2Table(typing_extensions.TypedDict, total=False):
    rows: typing.List[GooglePrivacyDlpV2Row]
    headers: typing.List[GooglePrivacyDlpV2FieldId]

class GooglePrivacyDlpV2Key(typing_extensions.TypedDict, total=False):
    path: typing.List[GooglePrivacyDlpV2PathElement]
    partitionId: GooglePrivacyDlpV2PartitionId

class GooglePrivacyDlpV2Condition(typing_extensions.TypedDict, total=False):
    operator: typing_extensions.Literal[
        "RELATIONAL_OPERATOR_UNSPECIFIED",
        "EQUAL_TO",
        "NOT_EQUAL_TO",
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_OR_EQUALS",
        "LESS_THAN_OR_EQUALS",
        "EXISTS",
    ]
    value: GooglePrivacyDlpV2Value
    field: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2InspectContentResponse(
    typing_extensions.TypedDict, total=False
):
    result: GooglePrivacyDlpV2InspectResult

class GooglePrivacyDlpV2InspectDataSourceDetails(
    typing_extensions.TypedDict, total=False
):
    result: GooglePrivacyDlpV2Result
    requestedOptions: GooglePrivacyDlpV2RequestedOptions

class GooglePrivacyDlpV2ImageRedactionConfig(typing_extensions.TypedDict, total=False):
    infoType: GooglePrivacyDlpV2InfoType
    redactionColor: GooglePrivacyDlpV2Color
    redactAllText: bool

class GooglePrivacyDlpV2InspectionRuleSet(typing_extensions.TypedDict, total=False):
    infoTypes: typing.List[GooglePrivacyDlpV2InfoType]
    rules: typing.List[GooglePrivacyDlpV2InspectionRule]

class GooglePrivacyDlpV2FindingLimits(typing_extensions.TypedDict, total=False):
    maxFindingsPerItem: int
    maxFindingsPerInfoType: typing.List[GooglePrivacyDlpV2InfoTypeLimit]
    maxFindingsPerRequest: int

class GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    maxProbability: float
    minProbability: float
    bucketValues: typing.List[GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues]
    bucketSize: str
    bucketValueCount: str

class GooglePrivacyDlpV2TransformationSummary(typing_extensions.TypedDict, total=False):
    transformedBytes: str
    recordSuppress: GooglePrivacyDlpV2RecordSuppression
    infoType: GooglePrivacyDlpV2InfoType
    fieldTransformations: typing.List[GooglePrivacyDlpV2FieldTransformation]
    results: typing.List[GooglePrivacyDlpV2SummaryResult]
    field: GooglePrivacyDlpV2FieldId
    transformation: GooglePrivacyDlpV2PrimitiveTransformation

class GooglePrivacyDlpV2LDiversityHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketValueCount: str
    bucketSize: str
    bucketValues: typing.List[GooglePrivacyDlpV2LDiversityEquivalenceClass]
    sensitiveValueFrequencyLowerBound: str
    sensitiveValueFrequencyUpperBound: str

class GooglePrivacyDlpV2CreateStoredInfoTypeRequest(
    typing_extensions.TypedDict, total=False
):
    config: GooglePrivacyDlpV2StoredInfoTypeConfig
    storedInfoTypeId: str
    locationId: str

class GooglePrivacyDlpV2LikelihoodAdjustment(typing_extensions.TypedDict, total=False):
    fixedLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    relativeLikelihood: int

class GooglePrivacyDlpV2InfoTypeStats(typing_extensions.TypedDict, total=False):
    count: str
    infoType: GooglePrivacyDlpV2InfoType

class GooglePrivacyDlpV2RequestedOptions(typing_extensions.TypedDict, total=False):
    jobConfig: GooglePrivacyDlpV2InspectJobConfig
    snapshotInspectTemplate: GooglePrivacyDlpV2InspectTemplate

class GooglePrivacyDlpV2ContentItem(typing_extensions.TypedDict, total=False):
    byteItem: GooglePrivacyDlpV2ByteContentItem
    value: str
    table: GooglePrivacyDlpV2Table

class GooglePrivacyDlpV2RedactImageResponse(typing_extensions.TypedDict, total=False):
    extractedText: str
    redactedImage: str
    inspectResult: GooglePrivacyDlpV2InspectResult

class GooglePrivacyDlpV2BigQueryOptions(typing_extensions.TypedDict, total=False):
    tableReference: GooglePrivacyDlpV2BigQueryTable
    rowsLimit: str
    rowsLimitPercent: int
    identifyingFields: typing.List[GooglePrivacyDlpV2FieldId]
    sampleMethod: typing_extensions.Literal[
        "SAMPLE_METHOD_UNSPECIFIED", "TOP", "RANDOM_START"
    ]
    excludedFields: typing.List[GooglePrivacyDlpV2FieldId]

class GooglePrivacyDlpV2CryptoDeterministicConfig(
    typing_extensions.TypedDict, total=False
):
    surrogateInfoType: GooglePrivacyDlpV2InfoType
    context: GooglePrivacyDlpV2FieldId
    cryptoKey: GooglePrivacyDlpV2CryptoKey

class GooglePrivacyDlpV2RecordSuppression(typing_extensions.TypedDict, total=False):
    condition: GooglePrivacyDlpV2RecordCondition

class GooglePrivacyDlpV2DatastoreOptions(typing_extensions.TypedDict, total=False):
    kind: GooglePrivacyDlpV2KindExpression
    partitionId: GooglePrivacyDlpV2PartitionId

class GooglePrivacyDlpV2SurrogateType(typing_extensions.TypedDict, total=False): ...

class GooglePrivacyDlpV2FieldTransformation(typing_extensions.TypedDict, total=False):
    condition: GooglePrivacyDlpV2RecordCondition
    primitiveTransformation: GooglePrivacyDlpV2PrimitiveTransformation
    infoTypeTransformations: GooglePrivacyDlpV2InfoTypeTransformations
    fields: typing.List[GooglePrivacyDlpV2FieldId]

class GooglePrivacyDlpV2ContentLocation(typing_extensions.TypedDict, total=False):
    containerTimestamp: str
    containerVersion: str
    recordLocation: GooglePrivacyDlpV2RecordLocation
    containerName: str
    documentLocation: GooglePrivacyDlpV2DocumentLocation
    metadataLocation: GooglePrivacyDlpV2MetadataLocation
    imageLocation: GooglePrivacyDlpV2ImageLocation

class GooglePrivacyDlpV2ListInspectTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    inspectTemplates: typing.List[GooglePrivacyDlpV2InspectTemplate]
    nextPageToken: str

class GooglePrivacyDlpV2PublishFindingsToCloudDataCatalog(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2ValueFrequency(typing_extensions.TypedDict, total=False):
    count: str
    value: GooglePrivacyDlpV2Value

class GooglePrivacyDlpV2DocumentLocation(typing_extensions.TypedDict, total=False):
    fileOffset: str

class GooglePrivacyDlpV2RecordKey(typing_extensions.TypedDict, total=False):
    bigQueryKey: GooglePrivacyDlpV2BigQueryKey
    idValues: typing.List[str]
    datastoreKey: GooglePrivacyDlpV2DatastoreKey

class GooglePrivacyDlpV2RecordTransformations(typing_extensions.TypedDict, total=False):
    fieldTransformations: typing.List[GooglePrivacyDlpV2FieldTransformation]
    recordSuppressions: typing.List[GooglePrivacyDlpV2RecordSuppression]

class GooglePrivacyDlpV2JobNotificationEmails(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2TransformationErrorHandling(
    typing_extensions.TypedDict, total=False
):
    leaveUntransformed: GooglePrivacyDlpV2LeaveUntransformed
    throwError: GooglePrivacyDlpV2ThrowError

class GooglePrivacyDlpV2BigQueryField(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId
    table: GooglePrivacyDlpV2BigQueryTable

class GooglePrivacyDlpV2StatisticalTable(typing_extensions.TypedDict, total=False):
    quasiIds: typing.List[GooglePrivacyDlpV2QuasiIdentifierField]
    table: GooglePrivacyDlpV2BigQueryTable
    relativeFrequency: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2ReplaceWithInfoTypeConfig(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2DeidentifyConfig(typing_extensions.TypedDict, total=False):
    infoTypeTransformations: GooglePrivacyDlpV2InfoTypeTransformations
    recordTransformations: GooglePrivacyDlpV2RecordTransformations
    transformationErrorHandling: GooglePrivacyDlpV2TransformationErrorHandling

class GooglePrivacyDlpV2JobTrigger(typing_extensions.TypedDict, total=False):
    displayName: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "HEALTHY", "PAUSED", "CANCELLED"
    ]
    description: str
    name: str
    triggers: typing.List[GooglePrivacyDlpV2Trigger]
    lastRunTime: str
    errors: typing.List[GooglePrivacyDlpV2Error]
    updateTime: str
    inspectJob: GooglePrivacyDlpV2InspectJobConfig
    createTime: str

class GooglePrivacyDlpV2TransientCryptoKey(typing_extensions.TypedDict, total=False):
    name: str

class GooglePrivacyDlpV2KAnonymityEquivalenceClass(
    typing_extensions.TypedDict, total=False
):
    quasiIdsValues: typing.List[GooglePrivacyDlpV2Value]
    equivalenceClassSize: str

class GooglePrivacyDlpV2SummaryResult(typing_extensions.TypedDict, total=False):
    details: str
    count: str
    code: typing_extensions.Literal[
        "TRANSFORMATION_RESULT_CODE_UNSPECIFIED", "SUCCESS", "ERROR"
    ]

class GooglePrivacyDlpV2BigQueryTable(typing_extensions.TypedDict, total=False):
    tableId: str
    datasetId: str
    projectId: str

class GooglePrivacyDlpV2Action(typing_extensions.TypedDict, total=False):
    publishSummaryToCscc: GooglePrivacyDlpV2PublishSummaryToCscc
    pubSub: GooglePrivacyDlpV2PublishToPubSub
    jobNotificationEmails: GooglePrivacyDlpV2JobNotificationEmails
    publishToStackdriver: GooglePrivacyDlpV2PublishToStackdriver
    publishFindingsToCloudDataCatalog: GooglePrivacyDlpV2PublishFindingsToCloudDataCatalog
    saveFindings: GooglePrivacyDlpV2SaveFindings

class GooglePrivacyDlpV2TableLocation(typing_extensions.TypedDict, total=False):
    rowIndex: str

class GooglePrivacyDlpV2RequestedRiskAnalysisOptions(
    typing_extensions.TypedDict, total=False
):
    jobConfig: GooglePrivacyDlpV2RiskAnalysisJobConfig

class GooglePrivacyDlpV2TimePartConfig(typing_extensions.TypedDict, total=False):
    partToExtract: typing_extensions.Literal[
        "TIME_PART_UNSPECIFIED",
        "YEAR",
        "MONTH",
        "DAY_OF_MONTH",
        "DAY_OF_WEEK",
        "WEEK_OF_YEAR",
        "HOUR_OF_DAY",
    ]

class GooglePrivacyDlpV2Bucket(typing_extensions.TypedDict, total=False):
    max: GooglePrivacyDlpV2Value
    replacementValue: GooglePrivacyDlpV2Value
    min: GooglePrivacyDlpV2Value

class GooglePrivacyDlpV2TimespanConfig(typing_extensions.TypedDict, total=False):
    enableAutoPopulationOfTimespanConfig: bool
    timestampField: GooglePrivacyDlpV2FieldId
    startTime: str
    endTime: str

class GooglePrivacyDlpV2ListDlpJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[GooglePrivacyDlpV2DlpJob]
    nextPageToken: str

class GooglePrivacyDlpV2HybridInspectResponse(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2LargeCustomDictionaryStats(
    typing_extensions.TypedDict, total=False
):
    approxNumPhrases: str

class GooglePrivacyDlpV2UpdateStoredInfoTypeRequest(
    typing_extensions.TypedDict, total=False
):
    config: GooglePrivacyDlpV2StoredInfoTypeConfig
    updateMask: str

class GooglePrivacyDlpV2Regex(typing_extensions.TypedDict, total=False):
    groupIndexes: typing.List[int]
    pattern: str

class GooglePrivacyDlpV2ExcludeInfoTypes(typing_extensions.TypedDict, total=False):
    infoTypes: typing.List[GooglePrivacyDlpV2InfoType]

class GooglePrivacyDlpV2StorageMetadataLabel(typing_extensions.TypedDict, total=False):
    key: str

class GooglePrivacyDlpV2QuasiIdField(typing_extensions.TypedDict, total=False):
    customTag: str
    field: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2PartitionId(typing_extensions.TypedDict, total=False):
    projectId: str
    namespaceId: str

class GooglePrivacyDlpV2CategoricalStatsHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketSize: str
    valueFrequencyLowerBound: str
    valueFrequencyUpperBound: str
    bucketValues: typing.List[GooglePrivacyDlpV2ValueFrequency]
    bucketValueCount: str

class GooglePrivacyDlpV2CryptoKey(typing_extensions.TypedDict, total=False):
    unwrapped: GooglePrivacyDlpV2UnwrappedCryptoKey
    kmsWrapped: GooglePrivacyDlpV2KmsWrappedCryptoKey
    transient: GooglePrivacyDlpV2TransientCryptoKey

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class GooglePrivacyDlpV2InfoTypeTransformations(
    typing_extensions.TypedDict, total=False
):
    transformations: typing.List[GooglePrivacyDlpV2InfoTypeTransformation]

class GooglePrivacyDlpV2TimeZone(typing_extensions.TypedDict, total=False):
    offsetMinutes: int

class GooglePrivacyDlpV2TableOptions(typing_extensions.TypedDict, total=False):
    identifyingFields: typing.List[GooglePrivacyDlpV2FieldId]

class GooglePrivacyDlpV2CreateInspectTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    inspectTemplate: GooglePrivacyDlpV2InspectTemplate
    templateId: str
    locationId: str

class GooglePrivacyDlpV2QuoteInfo(typing_extensions.TypedDict, total=False):
    dateTime: GooglePrivacyDlpV2DateTime

class GooglePrivacyDlpV2PublishToPubSub(typing_extensions.TypedDict, total=False):
    topic: str

class GoogleTypeTimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    nanos: int
    seconds: int
    minutes: int

class GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig(
    typing_extensions.TypedDict, total=False
):
    surrogateInfoType: GooglePrivacyDlpV2InfoType
    customAlphabet: str
    context: GooglePrivacyDlpV2FieldId
    cryptoKey: GooglePrivacyDlpV2CryptoKey
    radix: int
    commonAlphabet: typing_extensions.Literal[
        "FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED",
        "NUMERIC",
        "HEXADECIMAL",
        "UPPER_CASE_ALPHA_NUMERIC",
        "ALPHA_NUMERIC",
    ]

class GooglePrivacyDlpV2DeidentifyContentRequest(
    typing_extensions.TypedDict, total=False
):
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    deidentifyConfig: GooglePrivacyDlpV2DeidentifyConfig
    inspectTemplateName: str
    item: GooglePrivacyDlpV2ContentItem
    deidentifyTemplateName: str
    locationId: str

class GooglePrivacyDlpV2RecordCondition(typing_extensions.TypedDict, total=False):
    expressions: GooglePrivacyDlpV2Expressions

class GooglePrivacyDlpV2CryptoHashConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: GooglePrivacyDlpV2CryptoKey

class GooglePrivacyDlpV2ByteContentItem(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "BYTES_TYPE_UNSPECIFIED",
        "IMAGE",
        "IMAGE_JPEG",
        "IMAGE_BMP",
        "IMAGE_PNG",
        "IMAGE_SVG",
        "TEXT_UTF8",
        "WORD_DOCUMENT",
        "PDF",
        "AVRO",
        "CSV",
        "TSV",
    ]
    data: str

class GooglePrivacyDlpV2CloudStorageOptions(typing_extensions.TypedDict, total=False):
    filesLimitPercent: int
    fileSet: GooglePrivacyDlpV2FileSet
    bytesLimitPerFile: str
    bytesLimitPerFilePercent: int
    fileTypes: typing.List[str]
    sampleMethod: typing_extensions.Literal[
        "SAMPLE_METHOD_UNSPECIFIED", "TOP", "RANDOM_START"
    ]

class GooglePrivacyDlpV2ListInfoTypesResponse(typing_extensions.TypedDict, total=False):
    infoTypes: typing.List[GooglePrivacyDlpV2InfoTypeDescription]

class GooglePrivacyDlpV2CloudStoragePath(typing_extensions.TypedDict, total=False):
    path: str

class GooglePrivacyDlpV2SaveFindings(typing_extensions.TypedDict, total=False):
    outputConfig: GooglePrivacyDlpV2OutputStorageConfig

class GooglePrivacyDlpV2Proximity(typing_extensions.TypedDict, total=False):
    windowBefore: int
    windowAfter: int

class GooglePrivacyDlpV2FieldId(typing_extensions.TypedDict, total=False):
    name: str

class GooglePrivacyDlpV2InspectionRule(typing_extensions.TypedDict, total=False):
    exclusionRule: GooglePrivacyDlpV2ExclusionRule
    hotwordRule: GooglePrivacyDlpV2HotwordRule

class GooglePrivacyDlpV2CancelDlpJobRequest(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2ListStoredInfoTypesResponse(
    typing_extensions.TypedDict, total=False
):
    storedInfoTypes: typing.List[GooglePrivacyDlpV2StoredInfoType]
    nextPageToken: str

class GooglePrivacyDlpV2ReplaceValueConfig(typing_extensions.TypedDict, total=False):
    newValue: GooglePrivacyDlpV2Value

class GooglePrivacyDlpV2Row(typing_extensions.TypedDict, total=False):
    values: typing.List[GooglePrivacyDlpV2Value]

class GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues(
    typing_extensions.TypedDict, total=False
):
    estimatedProbability: float
    quasiIdsValues: typing.List[GooglePrivacyDlpV2Value]

class GooglePrivacyDlpV2ActivateJobTriggerRequest(
    typing_extensions.TypedDict, total=False
): ...

class GooglePrivacyDlpV2PathElement(typing_extensions.TypedDict, total=False):
    kind: str
    id: str
    name: str

class GooglePrivacyDlpV2TaggedField(typing_extensions.TypedDict, total=False):
    infoType: GooglePrivacyDlpV2InfoType
    inferred: GoogleProtobufEmpty
    customTag: str
    field: GooglePrivacyDlpV2FieldId

class GooglePrivacyDlpV2DlpJob(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
    ]
    riskDetails: GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails
    createTime: str
    startTime: str
    errors: typing.List[GooglePrivacyDlpV2Error]
    name: str
    inspectDetails: GooglePrivacyDlpV2InspectDataSourceDetails
    jobTriggerName: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "DONE",
        "CANCELED",
        "FAILED",
        "ACTIVE",
    ]
    endTime: str

class GooglePrivacyDlpV2CloudStorageRegexFileSet(
    typing_extensions.TypedDict, total=False
):
    includeRegex: typing.List[str]
    excludeRegex: typing.List[str]
    bucketName: str

class GooglePrivacyDlpV2HotwordRule(typing_extensions.TypedDict, total=False):
    hotwordRegex: GooglePrivacyDlpV2Regex
    proximity: GooglePrivacyDlpV2Proximity
    likelihoodAdjustment: GooglePrivacyDlpV2LikelihoodAdjustment

class GooglePrivacyDlpV2DetectionRule(typing_extensions.TypedDict, total=False):
    hotwordRule: GooglePrivacyDlpV2HotwordRule
