import typing

import typing_extensions

_list = list

@typing.type_check_only
class GooglePrivacyDlpV2Action(typing_extensions.TypedDict, total=False):
    deidentify: GooglePrivacyDlpV2Deidentify
    jobNotificationEmails: GooglePrivacyDlpV2JobNotificationEmails
    pubSub: GooglePrivacyDlpV2PublishToPubSub
    publishFindingsToCloudDataCatalog: GooglePrivacyDlpV2PublishFindingsToCloudDataCatalog
    publishSummaryToCscc: GooglePrivacyDlpV2PublishSummaryToCscc
    publishToStackdriver: GooglePrivacyDlpV2PublishToStackdriver
    saveFindings: GooglePrivacyDlpV2SaveFindings

@typing.type_check_only
class GooglePrivacyDlpV2ActivateJobTriggerRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2AllInfoTypes(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GooglePrivacyDlpV2AllText(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails(
    typing_extensions.TypedDict, total=False
):
    categoricalStatsResult: GooglePrivacyDlpV2CategoricalStatsResult
    deltaPresenceEstimationResult: GooglePrivacyDlpV2DeltaPresenceEstimationResult
    kAnonymityResult: GooglePrivacyDlpV2KAnonymityResult
    kMapEstimationResult: GooglePrivacyDlpV2KMapEstimationResult
    lDiversityResult: GooglePrivacyDlpV2LDiversityResult
    numericalStatsResult: GooglePrivacyDlpV2NumericalStatsResult
    requestedOptions: GooglePrivacyDlpV2RequestedRiskAnalysisOptions
    requestedPrivacyMetric: GooglePrivacyDlpV2PrivacyMetric
    requestedSourceTable: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2AuxiliaryTable(typing_extensions.TypedDict, total=False):
    quasiIds: _list[GooglePrivacyDlpV2QuasiIdField]
    relativeFrequency: GooglePrivacyDlpV2FieldId
    table: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2BigQueryField(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId
    table: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2BigQueryKey(typing_extensions.TypedDict, total=False):
    rowNumber: str
    tableReference: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2BigQueryOptions(typing_extensions.TypedDict, total=False):
    excludedFields: _list[GooglePrivacyDlpV2FieldId]
    identifyingFields: _list[GooglePrivacyDlpV2FieldId]
    includedFields: _list[GooglePrivacyDlpV2FieldId]
    rowsLimit: str
    rowsLimitPercent: int
    sampleMethod: typing_extensions.Literal[
        "SAMPLE_METHOD_UNSPECIFIED", "TOP", "RANDOM_START"
    ]
    tableReference: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2BigQueryTable(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GooglePrivacyDlpV2BoundingBox(typing_extensions.TypedDict, total=False):
    height: int
    left: int
    top: int
    width: int

@typing.type_check_only
class GooglePrivacyDlpV2Bucket(typing_extensions.TypedDict, total=False):
    max: GooglePrivacyDlpV2Value
    min: GooglePrivacyDlpV2Value
    replacementValue: GooglePrivacyDlpV2Value

@typing.type_check_only
class GooglePrivacyDlpV2BucketingConfig(typing_extensions.TypedDict, total=False):
    buckets: _list[GooglePrivacyDlpV2Bucket]

@typing.type_check_only
class GooglePrivacyDlpV2ByteContentItem(typing_extensions.TypedDict, total=False):
    data: str
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
        "POWERPOINT_DOCUMENT",
        "EXCEL_DOCUMENT",
        "AVRO",
        "CSV",
        "TSV",
    ]

@typing.type_check_only
class GooglePrivacyDlpV2CancelDlpJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2CategoricalStatsConfig(
    typing_extensions.TypedDict, total=False
):
    field: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2CategoricalStatsHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketSize: str
    bucketValueCount: str
    bucketValues: _list[GooglePrivacyDlpV2ValueFrequency]
    valueFrequencyLowerBound: str
    valueFrequencyUpperBound: str

@typing.type_check_only
class GooglePrivacyDlpV2CategoricalStatsResult(
    typing_extensions.TypedDict, total=False
):
    valueFrequencyHistogramBuckets: _list[
        GooglePrivacyDlpV2CategoricalStatsHistogramBucket
    ]

@typing.type_check_only
class GooglePrivacyDlpV2CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    charactersToIgnore: _list[GooglePrivacyDlpV2CharsToIgnore]
    maskingCharacter: str
    numberToMask: int
    reverseOrder: bool

@typing.type_check_only
class GooglePrivacyDlpV2CharsToIgnore(typing_extensions.TypedDict, total=False):
    charactersToSkip: str
    commonCharactersToIgnore: typing_extensions.Literal[
        "COMMON_CHARS_TO_IGNORE_UNSPECIFIED",
        "NUMERIC",
        "ALPHA_UPPER_CASE",
        "ALPHA_LOWER_CASE",
        "PUNCTUATION",
        "WHITESPACE",
    ]

@typing.type_check_only
class GooglePrivacyDlpV2CloudStorageFileSet(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class GooglePrivacyDlpV2CloudStorageOptions(typing_extensions.TypedDict, total=False):
    bytesLimitPerFile: str
    bytesLimitPerFilePercent: int
    fileSet: GooglePrivacyDlpV2FileSet
    fileTypes: _list[str]
    filesLimitPercent: int
    sampleMethod: typing_extensions.Literal[
        "SAMPLE_METHOD_UNSPECIFIED", "TOP", "RANDOM_START"
    ]

@typing.type_check_only
class GooglePrivacyDlpV2CloudStoragePath(typing_extensions.TypedDict, total=False):
    path: str

@typing.type_check_only
class GooglePrivacyDlpV2CloudStorageRegexFileSet(
    typing_extensions.TypedDict, total=False
):
    bucketName: str
    excludeRegex: _list[str]
    includeRegex: _list[str]

@typing.type_check_only
class GooglePrivacyDlpV2Color(typing_extensions.TypedDict, total=False):
    blue: float
    green: float
    red: float

@typing.type_check_only
class GooglePrivacyDlpV2Condition(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId
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

@typing.type_check_only
class GooglePrivacyDlpV2Conditions(typing_extensions.TypedDict, total=False):
    conditions: _list[GooglePrivacyDlpV2Condition]

@typing.type_check_only
class GooglePrivacyDlpV2Container(typing_extensions.TypedDict, total=False):
    fullPath: str
    projectId: str
    relativePath: str
    rootPath: str
    type: str
    updateTime: str
    version: str

@typing.type_check_only
class GooglePrivacyDlpV2ContentItem(typing_extensions.TypedDict, total=False):
    byteItem: GooglePrivacyDlpV2ByteContentItem
    table: GooglePrivacyDlpV2Table
    value: str

@typing.type_check_only
class GooglePrivacyDlpV2ContentLocation(typing_extensions.TypedDict, total=False):
    containerName: str
    containerTimestamp: str
    containerVersion: str
    documentLocation: GooglePrivacyDlpV2DocumentLocation
    imageLocation: GooglePrivacyDlpV2ImageLocation
    metadataLocation: GooglePrivacyDlpV2MetadataLocation
    recordLocation: GooglePrivacyDlpV2RecordLocation

@typing.type_check_only
class GooglePrivacyDlpV2CreateDeidentifyTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplate: GooglePrivacyDlpV2DeidentifyTemplate
    locationId: str
    templateId: str

@typing.type_check_only
class GooglePrivacyDlpV2CreateDlpJobRequest(typing_extensions.TypedDict, total=False):
    inspectJob: GooglePrivacyDlpV2InspectJobConfig
    jobId: str
    locationId: str
    riskJob: GooglePrivacyDlpV2RiskAnalysisJobConfig

@typing.type_check_only
class GooglePrivacyDlpV2CreateInspectTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    inspectTemplate: GooglePrivacyDlpV2InspectTemplate
    locationId: str
    templateId: str

@typing.type_check_only
class GooglePrivacyDlpV2CreateJobTriggerRequest(
    typing_extensions.TypedDict, total=False
):
    jobTrigger: GooglePrivacyDlpV2JobTrigger
    locationId: str
    triggerId: str

@typing.type_check_only
class GooglePrivacyDlpV2CreateStoredInfoTypeRequest(
    typing_extensions.TypedDict, total=False
):
    config: GooglePrivacyDlpV2StoredInfoTypeConfig
    locationId: str
    storedInfoTypeId: str

@typing.type_check_only
class GooglePrivacyDlpV2CryptoDeterministicConfig(
    typing_extensions.TypedDict, total=False
):
    context: GooglePrivacyDlpV2FieldId
    cryptoKey: GooglePrivacyDlpV2CryptoKey
    surrogateInfoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2CryptoHashConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: GooglePrivacyDlpV2CryptoKey

@typing.type_check_only
class GooglePrivacyDlpV2CryptoKey(typing_extensions.TypedDict, total=False):
    kmsWrapped: GooglePrivacyDlpV2KmsWrappedCryptoKey
    transient: GooglePrivacyDlpV2TransientCryptoKey
    unwrapped: GooglePrivacyDlpV2UnwrappedCryptoKey

@typing.type_check_only
class GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig(
    typing_extensions.TypedDict, total=False
):
    commonAlphabet: typing_extensions.Literal[
        "FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED",
        "NUMERIC",
        "HEXADECIMAL",
        "UPPER_CASE_ALPHA_NUMERIC",
        "ALPHA_NUMERIC",
    ]
    context: GooglePrivacyDlpV2FieldId
    cryptoKey: GooglePrivacyDlpV2CryptoKey
    customAlphabet: str
    radix: int
    surrogateInfoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2CustomInfoType(typing_extensions.TypedDict, total=False):
    detectionRules: _list[GooglePrivacyDlpV2DetectionRule]
    dictionary: GooglePrivacyDlpV2Dictionary
    exclusionType: typing_extensions.Literal[
        "EXCLUSION_TYPE_UNSPECIFIED", "EXCLUSION_TYPE_EXCLUDE"
    ]
    infoType: GooglePrivacyDlpV2InfoType
    likelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    regex: GooglePrivacyDlpV2Regex
    storedType: GooglePrivacyDlpV2StoredType
    surrogateType: GooglePrivacyDlpV2SurrogateType

@typing.type_check_only
class GooglePrivacyDlpV2DataProfileAction(typing_extensions.TypedDict, total=False):
    exportData: GooglePrivacyDlpV2Export
    pubSubNotification: GooglePrivacyDlpV2PubSubNotification

@typing.type_check_only
class GooglePrivacyDlpV2DataProfileConfigSnapshot(
    typing_extensions.TypedDict, total=False
):
    dataProfileJob: GooglePrivacyDlpV2DataProfileJobConfig
    inspectConfig: GooglePrivacyDlpV2InspectConfig

@typing.type_check_only
class GooglePrivacyDlpV2DataProfileJobConfig(typing_extensions.TypedDict, total=False):
    dataProfileActions: _list[GooglePrivacyDlpV2DataProfileAction]
    inspectTemplates: _list[str]
    location: GooglePrivacyDlpV2DataProfileLocation
    projectId: str

@typing.type_check_only
class GooglePrivacyDlpV2DataProfileLocation(typing_extensions.TypedDict, total=False):
    folderId: str
    organizationId: str

@typing.type_check_only
class GooglePrivacyDlpV2DataProfilePubSubCondition(
    typing_extensions.TypedDict, total=False
):
    expressions: GooglePrivacyDlpV2PubSubExpressions

@typing.type_check_only
class GooglePrivacyDlpV2DataProfilePubSubMessage(
    typing_extensions.TypedDict, total=False
):
    event: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "NEW_PROFILE",
        "CHANGED_PROFILE",
        "SCORE_INCREASED",
        "ERROR_CHANGED",
    ]
    profile: GooglePrivacyDlpV2TableDataProfile

@typing.type_check_only
class GooglePrivacyDlpV2DataRiskLevel(typing_extensions.TypedDict, total=False):
    score: typing_extensions.Literal[
        "RISK_SCORE_UNSPECIFIED", "RISK_LOW", "RISK_MODERATE", "RISK_HIGH"
    ]

@typing.type_check_only
class GooglePrivacyDlpV2DatastoreKey(typing_extensions.TypedDict, total=False):
    entityKey: GooglePrivacyDlpV2Key

@typing.type_check_only
class GooglePrivacyDlpV2DatastoreOptions(typing_extensions.TypedDict, total=False):
    kind: GooglePrivacyDlpV2KindExpression
    partitionId: GooglePrivacyDlpV2PartitionId

@typing.type_check_only
class GooglePrivacyDlpV2DateShiftConfig(typing_extensions.TypedDict, total=False):
    context: GooglePrivacyDlpV2FieldId
    cryptoKey: GooglePrivacyDlpV2CryptoKey
    lowerBoundDays: int
    upperBoundDays: int

@typing.type_check_only
class GooglePrivacyDlpV2DateTime(typing_extensions.TypedDict, total=False):
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
    time: GoogleTypeTimeOfDay
    timeZone: GooglePrivacyDlpV2TimeZone

@typing.type_check_only
class GooglePrivacyDlpV2Deidentify(typing_extensions.TypedDict, total=False):
    cloudStorageOutput: str
    fileTypesToTransform: _list[str]
    transformationConfig: GooglePrivacyDlpV2TransformationConfig
    transformationDetailsStorageConfig: GooglePrivacyDlpV2TransformationDetailsStorageConfig

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyConfig(typing_extensions.TypedDict, total=False):
    imageTransformations: GooglePrivacyDlpV2ImageTransformations
    infoTypeTransformations: GooglePrivacyDlpV2InfoTypeTransformations
    recordTransformations: GooglePrivacyDlpV2RecordTransformations
    transformationErrorHandling: GooglePrivacyDlpV2TransformationErrorHandling

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyContentRequest(
    typing_extensions.TypedDict, total=False
):
    deidentifyConfig: GooglePrivacyDlpV2DeidentifyConfig
    deidentifyTemplateName: str
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    inspectTemplateName: str
    item: GooglePrivacyDlpV2ContentItem
    locationId: str

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyContentResponse(
    typing_extensions.TypedDict, total=False
):
    item: GooglePrivacyDlpV2ContentItem
    overview: GooglePrivacyDlpV2TransformationOverview

@typing.type_check_only
class GooglePrivacyDlpV2DeidentifyTemplate(typing_extensions.TypedDict, total=False):
    createTime: str
    deidentifyConfig: GooglePrivacyDlpV2DeidentifyConfig
    description: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class GooglePrivacyDlpV2DeltaPresenceEstimationConfig(
    typing_extensions.TypedDict, total=False
):
    auxiliaryTables: _list[GooglePrivacyDlpV2StatisticalTable]
    quasiIds: _list[GooglePrivacyDlpV2QuasiId]
    regionCode: str

@typing.type_check_only
class GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketSize: str
    bucketValueCount: str
    bucketValues: _list[GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues]
    maxProbability: float
    minProbability: float

@typing.type_check_only
class GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues(
    typing_extensions.TypedDict, total=False
):
    estimatedProbability: float
    quasiIdsValues: _list[GooglePrivacyDlpV2Value]

@typing.type_check_only
class GooglePrivacyDlpV2DeltaPresenceEstimationResult(
    typing_extensions.TypedDict, total=False
):
    deltaPresenceEstimationHistogram: _list[
        GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucket
    ]

@typing.type_check_only
class GooglePrivacyDlpV2DetectionRule(typing_extensions.TypedDict, total=False):
    hotwordRule: GooglePrivacyDlpV2HotwordRule

@typing.type_check_only
class GooglePrivacyDlpV2Dictionary(typing_extensions.TypedDict, total=False):
    cloudStoragePath: GooglePrivacyDlpV2CloudStoragePath
    wordList: GooglePrivacyDlpV2WordList

@typing.type_check_only
class GooglePrivacyDlpV2DlpJob(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    errors: _list[GooglePrivacyDlpV2Error]
    inspectDetails: GooglePrivacyDlpV2InspectDataSourceDetails
    jobTriggerName: str
    name: str
    riskDetails: GooglePrivacyDlpV2AnalyzeDataSourceRiskDetails
    startTime: str
    state: typing_extensions.Literal[
        "JOB_STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "DONE",
        "CANCELED",
        "FAILED",
        "ACTIVE",
    ]
    type: typing_extensions.Literal[
        "DLP_JOB_TYPE_UNSPECIFIED", "INSPECT_JOB", "RISK_ANALYSIS_JOB"
    ]

@typing.type_check_only
class GooglePrivacyDlpV2DocumentLocation(typing_extensions.TypedDict, total=False):
    fileOffset: str

@typing.type_check_only
class GooglePrivacyDlpV2EntityId(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2Error(typing_extensions.TypedDict, total=False):
    details: GoogleRpcStatus
    timestamps: _list[str]

@typing.type_check_only
class GooglePrivacyDlpV2ExcludeInfoTypes(typing_extensions.TypedDict, total=False):
    infoTypes: _list[GooglePrivacyDlpV2InfoType]

@typing.type_check_only
class GooglePrivacyDlpV2ExclusionRule(typing_extensions.TypedDict, total=False):
    dictionary: GooglePrivacyDlpV2Dictionary
    excludeInfoTypes: GooglePrivacyDlpV2ExcludeInfoTypes
    matchingType: typing_extensions.Literal[
        "MATCHING_TYPE_UNSPECIFIED",
        "MATCHING_TYPE_FULL_MATCH",
        "MATCHING_TYPE_PARTIAL_MATCH",
        "MATCHING_TYPE_INVERSE_MATCH",
    ]
    regex: GooglePrivacyDlpV2Regex

@typing.type_check_only
class GooglePrivacyDlpV2Export(typing_extensions.TypedDict, total=False):
    profileTable: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2Expressions(typing_extensions.TypedDict, total=False):
    conditions: GooglePrivacyDlpV2Conditions
    logicalOperator: typing_extensions.Literal["LOGICAL_OPERATOR_UNSPECIFIED", "AND"]

@typing.type_check_only
class GooglePrivacyDlpV2FieldId(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GooglePrivacyDlpV2FieldTransformation(typing_extensions.TypedDict, total=False):
    condition: GooglePrivacyDlpV2RecordCondition
    fields: _list[GooglePrivacyDlpV2FieldId]
    infoTypeTransformations: GooglePrivacyDlpV2InfoTypeTransformations
    primitiveTransformation: GooglePrivacyDlpV2PrimitiveTransformation

@typing.type_check_only
class GooglePrivacyDlpV2FileSet(typing_extensions.TypedDict, total=False):
    regexFileSet: GooglePrivacyDlpV2CloudStorageRegexFileSet
    url: str

@typing.type_check_only
class GooglePrivacyDlpV2Finding(typing_extensions.TypedDict, total=False):
    createTime: str
    findingId: str
    infoType: GooglePrivacyDlpV2InfoType
    jobCreateTime: str
    jobName: str
    labels: dict[str, typing.Any]
    likelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    location: GooglePrivacyDlpV2Location
    name: str
    quote: str
    quoteInfo: GooglePrivacyDlpV2QuoteInfo
    resourceName: str
    triggerName: str

@typing.type_check_only
class GooglePrivacyDlpV2FindingLimits(typing_extensions.TypedDict, total=False):
    maxFindingsPerInfoType: _list[GooglePrivacyDlpV2InfoTypeLimit]
    maxFindingsPerItem: int
    maxFindingsPerRequest: int

@typing.type_check_only
class GooglePrivacyDlpV2FinishDlpJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2FixedSizeBucketingConfig(
    typing_extensions.TypedDict, total=False
):
    bucketSize: float
    lowerBound: GooglePrivacyDlpV2Value
    upperBound: GooglePrivacyDlpV2Value

@typing.type_check_only
class GooglePrivacyDlpV2HotwordRule(typing_extensions.TypedDict, total=False):
    hotwordRegex: GooglePrivacyDlpV2Regex
    likelihoodAdjustment: GooglePrivacyDlpV2LikelihoodAdjustment
    proximity: GooglePrivacyDlpV2Proximity

@typing.type_check_only
class GooglePrivacyDlpV2HybridContentItem(typing_extensions.TypedDict, total=False):
    findingDetails: GooglePrivacyDlpV2HybridFindingDetails
    item: GooglePrivacyDlpV2ContentItem

@typing.type_check_only
class GooglePrivacyDlpV2HybridFindingDetails(typing_extensions.TypedDict, total=False):
    containerDetails: GooglePrivacyDlpV2Container
    fileOffset: str
    labels: dict[str, typing.Any]
    rowOffset: str
    tableOptions: GooglePrivacyDlpV2TableOptions

@typing.type_check_only
class GooglePrivacyDlpV2HybridInspectDlpJobRequest(
    typing_extensions.TypedDict, total=False
):
    hybridItem: GooglePrivacyDlpV2HybridContentItem

@typing.type_check_only
class GooglePrivacyDlpV2HybridInspectJobTriggerRequest(
    typing_extensions.TypedDict, total=False
):
    hybridItem: GooglePrivacyDlpV2HybridContentItem

@typing.type_check_only
class GooglePrivacyDlpV2HybridInspectResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2HybridInspectStatistics(
    typing_extensions.TypedDict, total=False
):
    abortedCount: str
    pendingCount: str
    processedCount: str

@typing.type_check_only
class GooglePrivacyDlpV2HybridOptions(typing_extensions.TypedDict, total=False):
    description: str
    labels: dict[str, typing.Any]
    requiredFindingLabelKeys: _list[str]
    tableOptions: GooglePrivacyDlpV2TableOptions

@typing.type_check_only
class GooglePrivacyDlpV2ImageLocation(typing_extensions.TypedDict, total=False):
    boundingBoxes: _list[GooglePrivacyDlpV2BoundingBox]

@typing.type_check_only
class GooglePrivacyDlpV2ImageRedactionConfig(typing_extensions.TypedDict, total=False):
    infoType: GooglePrivacyDlpV2InfoType
    redactAllText: bool
    redactionColor: GooglePrivacyDlpV2Color

@typing.type_check_only
class GooglePrivacyDlpV2ImageTransformation(typing_extensions.TypedDict, total=False):
    allInfoTypes: GooglePrivacyDlpV2AllInfoTypes
    allText: GooglePrivacyDlpV2AllText
    redactionColor: GooglePrivacyDlpV2Color
    selectedInfoTypes: GooglePrivacyDlpV2SelectedInfoTypes

@typing.type_check_only
class GooglePrivacyDlpV2ImageTransformations(typing_extensions.TypedDict, total=False):
    transforms: _list[GooglePrivacyDlpV2ImageTransformation]

@typing.type_check_only
class GooglePrivacyDlpV2InfoType(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeCategory(typing_extensions.TypedDict, total=False):
    industryCategory: typing_extensions.Literal[
        "INDUSTRY_UNSPECIFIED", "FINANCE", "HEALTH", "TELECOMMUNICATIONS"
    ]
    locationCategory: typing_extensions.Literal[
        "LOCATION_UNSPECIFIED",
        "GLOBAL",
        "ARGENTINA",
        "AUSTRALIA",
        "BELGIUM",
        "BRAZIL",
        "CANADA",
        "CHILE",
        "CHINA",
        "COLOMBIA",
        "DENMARK",
        "FRANCE",
        "FINLAND",
        "GERMANY",
        "HONG_KONG",
        "INDIA",
        "INDONESIA",
        "IRELAND",
        "ISRAEL",
        "ITALY",
        "JAPAN",
        "KOREA",
        "MEXICO",
        "THE_NETHERLANDS",
        "NORWAY",
        "PARAGUAY",
        "PERU",
        "POLAND",
        "PORTUGAL",
        "SINGAPORE",
        "SOUTH_AFRICA",
        "SPAIN",
        "SWEDEN",
        "TAIWAN",
        "THAILAND",
        "TURKEY",
        "UNITED_KINGDOM",
        "UNITED_STATES",
        "URUGUAY",
        "VENEZUELA",
        "INTERNAL",
    ]
    typeCategory: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "PII",
        "SPII",
        "DEMOGRAPHIC",
        "CREDENTIAL",
        "GOVERNMENT_ID",
        "DOCUMENT",
        "CONTEXTUAL_INFORMATION",
    ]

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeDescription(typing_extensions.TypedDict, total=False):
    categories: _list[GooglePrivacyDlpV2InfoTypeCategory]
    description: str
    displayName: str
    name: str
    supportedBy: _list[str]
    versions: _list[GooglePrivacyDlpV2VersionDescription]

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeLimit(typing_extensions.TypedDict, total=False):
    infoType: GooglePrivacyDlpV2InfoType
    maxFindings: int

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeStats(typing_extensions.TypedDict, total=False):
    count: str
    infoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeSummary(typing_extensions.TypedDict, total=False):
    infoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeTransformation(
    typing_extensions.TypedDict, total=False
):
    infoTypes: _list[GooglePrivacyDlpV2InfoType]
    primitiveTransformation: GooglePrivacyDlpV2PrimitiveTransformation

@typing.type_check_only
class GooglePrivacyDlpV2InfoTypeTransformations(
    typing_extensions.TypedDict, total=False
):
    transformations: _list[GooglePrivacyDlpV2InfoTypeTransformation]

@typing.type_check_only
class GooglePrivacyDlpV2InspectConfig(typing_extensions.TypedDict, total=False):
    contentOptions: _list[str]
    customInfoTypes: _list[GooglePrivacyDlpV2CustomInfoType]
    excludeInfoTypes: bool
    includeQuote: bool
    infoTypes: _list[GooglePrivacyDlpV2InfoType]
    limits: GooglePrivacyDlpV2FindingLimits
    minLikelihood: typing_extensions.Literal[
        "LIKELIHOOD_UNSPECIFIED",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    ]
    ruleSet: _list[GooglePrivacyDlpV2InspectionRuleSet]

@typing.type_check_only
class GooglePrivacyDlpV2InspectContentRequest(typing_extensions.TypedDict, total=False):
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    inspectTemplateName: str
    item: GooglePrivacyDlpV2ContentItem
    locationId: str

@typing.type_check_only
class GooglePrivacyDlpV2InspectContentResponse(
    typing_extensions.TypedDict, total=False
):
    result: GooglePrivacyDlpV2InspectResult

@typing.type_check_only
class GooglePrivacyDlpV2InspectDataSourceDetails(
    typing_extensions.TypedDict, total=False
):
    requestedOptions: GooglePrivacyDlpV2RequestedOptions
    result: GooglePrivacyDlpV2Result

@typing.type_check_only
class GooglePrivacyDlpV2InspectJobConfig(typing_extensions.TypedDict, total=False):
    actions: _list[GooglePrivacyDlpV2Action]
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    inspectTemplateName: str
    storageConfig: GooglePrivacyDlpV2StorageConfig

@typing.type_check_only
class GooglePrivacyDlpV2InspectResult(typing_extensions.TypedDict, total=False):
    findings: _list[GooglePrivacyDlpV2Finding]
    findingsTruncated: bool

@typing.type_check_only
class GooglePrivacyDlpV2InspectTemplate(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    name: str
    updateTime: str

@typing.type_check_only
class GooglePrivacyDlpV2InspectionRule(typing_extensions.TypedDict, total=False):
    exclusionRule: GooglePrivacyDlpV2ExclusionRule
    hotwordRule: GooglePrivacyDlpV2HotwordRule

@typing.type_check_only
class GooglePrivacyDlpV2InspectionRuleSet(typing_extensions.TypedDict, total=False):
    infoTypes: _list[GooglePrivacyDlpV2InfoType]
    rules: _list[GooglePrivacyDlpV2InspectionRule]

@typing.type_check_only
class GooglePrivacyDlpV2JobNotificationEmails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2JobTrigger(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    errors: _list[GooglePrivacyDlpV2Error]
    inspectJob: GooglePrivacyDlpV2InspectJobConfig
    lastRunTime: str
    name: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "HEALTHY", "PAUSED", "CANCELLED"
    ]
    triggers: _list[GooglePrivacyDlpV2Trigger]
    updateTime: str

@typing.type_check_only
class GooglePrivacyDlpV2KAnonymityConfig(typing_extensions.TypedDict, total=False):
    entityId: GooglePrivacyDlpV2EntityId
    quasiIds: _list[GooglePrivacyDlpV2FieldId]

@typing.type_check_only
class GooglePrivacyDlpV2KAnonymityEquivalenceClass(
    typing_extensions.TypedDict, total=False
):
    equivalenceClassSize: str
    quasiIdsValues: _list[GooglePrivacyDlpV2Value]

@typing.type_check_only
class GooglePrivacyDlpV2KAnonymityHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketSize: str
    bucketValueCount: str
    bucketValues: _list[GooglePrivacyDlpV2KAnonymityEquivalenceClass]
    equivalenceClassSizeLowerBound: str
    equivalenceClassSizeUpperBound: str

@typing.type_check_only
class GooglePrivacyDlpV2KAnonymityResult(typing_extensions.TypedDict, total=False):
    equivalenceClassHistogramBuckets: _list[GooglePrivacyDlpV2KAnonymityHistogramBucket]

@typing.type_check_only
class GooglePrivacyDlpV2KMapEstimationConfig(typing_extensions.TypedDict, total=False):
    auxiliaryTables: _list[GooglePrivacyDlpV2AuxiliaryTable]
    quasiIds: _list[GooglePrivacyDlpV2TaggedField]
    regionCode: str

@typing.type_check_only
class GooglePrivacyDlpV2KMapEstimationHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketSize: str
    bucketValueCount: str
    bucketValues: _list[GooglePrivacyDlpV2KMapEstimationQuasiIdValues]
    maxAnonymity: str
    minAnonymity: str

@typing.type_check_only
class GooglePrivacyDlpV2KMapEstimationQuasiIdValues(
    typing_extensions.TypedDict, total=False
):
    estimatedAnonymity: str
    quasiIdsValues: _list[GooglePrivacyDlpV2Value]

@typing.type_check_only
class GooglePrivacyDlpV2KMapEstimationResult(typing_extensions.TypedDict, total=False):
    kMapEstimationHistogram: _list[GooglePrivacyDlpV2KMapEstimationHistogramBucket]

@typing.type_check_only
class GooglePrivacyDlpV2Key(typing_extensions.TypedDict, total=False):
    partitionId: GooglePrivacyDlpV2PartitionId
    path: _list[GooglePrivacyDlpV2PathElement]

@typing.type_check_only
class GooglePrivacyDlpV2KindExpression(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GooglePrivacyDlpV2KmsWrappedCryptoKey(typing_extensions.TypedDict, total=False):
    cryptoKeyName: str
    wrappedKey: str

@typing.type_check_only
class GooglePrivacyDlpV2LDiversityConfig(typing_extensions.TypedDict, total=False):
    quasiIds: _list[GooglePrivacyDlpV2FieldId]
    sensitiveAttribute: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2LDiversityEquivalenceClass(
    typing_extensions.TypedDict, total=False
):
    equivalenceClassSize: str
    numDistinctSensitiveValues: str
    quasiIdsValues: _list[GooglePrivacyDlpV2Value]
    topSensitiveValues: _list[GooglePrivacyDlpV2ValueFrequency]

@typing.type_check_only
class GooglePrivacyDlpV2LDiversityHistogramBucket(
    typing_extensions.TypedDict, total=False
):
    bucketSize: str
    bucketValueCount: str
    bucketValues: _list[GooglePrivacyDlpV2LDiversityEquivalenceClass]
    sensitiveValueFrequencyLowerBound: str
    sensitiveValueFrequencyUpperBound: str

@typing.type_check_only
class GooglePrivacyDlpV2LDiversityResult(typing_extensions.TypedDict, total=False):
    sensitiveValueFrequencyHistogramBuckets: _list[
        GooglePrivacyDlpV2LDiversityHistogramBucket
    ]

@typing.type_check_only
class GooglePrivacyDlpV2LargeCustomDictionaryConfig(
    typing_extensions.TypedDict, total=False
):
    bigQueryField: GooglePrivacyDlpV2BigQueryField
    cloudStorageFileSet: GooglePrivacyDlpV2CloudStorageFileSet
    outputPath: GooglePrivacyDlpV2CloudStoragePath

@typing.type_check_only
class GooglePrivacyDlpV2LargeCustomDictionaryStats(
    typing_extensions.TypedDict, total=False
):
    approxNumPhrases: str

@typing.type_check_only
class GooglePrivacyDlpV2LeaveUntransformed(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
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

@typing.type_check_only
class GooglePrivacyDlpV2ListDeidentifyTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplates: _list[GooglePrivacyDlpV2DeidentifyTemplate]
    nextPageToken: str

@typing.type_check_only
class GooglePrivacyDlpV2ListDlpJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[GooglePrivacyDlpV2DlpJob]
    nextPageToken: str

@typing.type_check_only
class GooglePrivacyDlpV2ListInfoTypesResponse(typing_extensions.TypedDict, total=False):
    infoTypes: _list[GooglePrivacyDlpV2InfoTypeDescription]

@typing.type_check_only
class GooglePrivacyDlpV2ListInspectTemplatesResponse(
    typing_extensions.TypedDict, total=False
):
    inspectTemplates: _list[GooglePrivacyDlpV2InspectTemplate]
    nextPageToken: str

@typing.type_check_only
class GooglePrivacyDlpV2ListJobTriggersResponse(
    typing_extensions.TypedDict, total=False
):
    jobTriggers: _list[GooglePrivacyDlpV2JobTrigger]
    nextPageToken: str

@typing.type_check_only
class GooglePrivacyDlpV2ListStoredInfoTypesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    storedInfoTypes: _list[GooglePrivacyDlpV2StoredInfoType]

@typing.type_check_only
class GooglePrivacyDlpV2Location(typing_extensions.TypedDict, total=False):
    byteRange: GooglePrivacyDlpV2Range
    codepointRange: GooglePrivacyDlpV2Range
    container: GooglePrivacyDlpV2Container
    contentLocations: _list[GooglePrivacyDlpV2ContentLocation]

@typing.type_check_only
class GooglePrivacyDlpV2Manual(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GooglePrivacyDlpV2MetadataLocation(typing_extensions.TypedDict, total=False):
    storageLabel: GooglePrivacyDlpV2StorageMetadataLabel
    type: typing_extensions.Literal["METADATATYPE_UNSPECIFIED", "STORAGE_METADATA"]

@typing.type_check_only
class GooglePrivacyDlpV2NumericalStatsConfig(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2NumericalStatsResult(typing_extensions.TypedDict, total=False):
    maxValue: GooglePrivacyDlpV2Value
    minValue: GooglePrivacyDlpV2Value
    quantileValues: _list[GooglePrivacyDlpV2Value]

@typing.type_check_only
class GooglePrivacyDlpV2OtherInfoTypeSummary(typing_extensions.TypedDict, total=False):
    estimatedPrevalence: int
    infoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2OutputStorageConfig(typing_extensions.TypedDict, total=False):
    outputSchema: typing_extensions.Literal[
        "OUTPUT_SCHEMA_UNSPECIFIED",
        "BASIC_COLUMNS",
        "GCS_COLUMNS",
        "DATASTORE_COLUMNS",
        "BIG_QUERY_COLUMNS",
        "ALL_COLUMNS",
    ]
    table: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2PartitionId(typing_extensions.TypedDict, total=False):
    namespaceId: str
    projectId: str

@typing.type_check_only
class GooglePrivacyDlpV2PathElement(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class GooglePrivacyDlpV2PrimitiveTransformation(
    typing_extensions.TypedDict, total=False
):
    bucketingConfig: GooglePrivacyDlpV2BucketingConfig
    characterMaskConfig: GooglePrivacyDlpV2CharacterMaskConfig
    cryptoDeterministicConfig: GooglePrivacyDlpV2CryptoDeterministicConfig
    cryptoHashConfig: GooglePrivacyDlpV2CryptoHashConfig
    cryptoReplaceFfxFpeConfig: GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig
    dateShiftConfig: GooglePrivacyDlpV2DateShiftConfig
    fixedSizeBucketingConfig: GooglePrivacyDlpV2FixedSizeBucketingConfig
    redactConfig: GooglePrivacyDlpV2RedactConfig
    replaceConfig: GooglePrivacyDlpV2ReplaceValueConfig
    replaceDictionaryConfig: GooglePrivacyDlpV2ReplaceDictionaryConfig
    replaceWithInfoTypeConfig: GooglePrivacyDlpV2ReplaceWithInfoTypeConfig
    timePartConfig: GooglePrivacyDlpV2TimePartConfig

@typing.type_check_only
class GooglePrivacyDlpV2PrivacyMetric(typing_extensions.TypedDict, total=False):
    categoricalStatsConfig: GooglePrivacyDlpV2CategoricalStatsConfig
    deltaPresenceEstimationConfig: GooglePrivacyDlpV2DeltaPresenceEstimationConfig
    kAnonymityConfig: GooglePrivacyDlpV2KAnonymityConfig
    kMapEstimationConfig: GooglePrivacyDlpV2KMapEstimationConfig
    lDiversityConfig: GooglePrivacyDlpV2LDiversityConfig
    numericalStatsConfig: GooglePrivacyDlpV2NumericalStatsConfig

@typing.type_check_only
class GooglePrivacyDlpV2ProfileStatus(typing_extensions.TypedDict, total=False):
    status: GoogleRpcStatus
    timestamp: str

@typing.type_check_only
class GooglePrivacyDlpV2Proximity(typing_extensions.TypedDict, total=False):
    windowAfter: int
    windowBefore: int

@typing.type_check_only
class GooglePrivacyDlpV2PubSubCondition(typing_extensions.TypedDict, total=False):
    minimumRiskScore: typing_extensions.Literal[
        "PROFILE_SCORE_BUCKET_UNSPECIFIED", "HIGH", "MEDIUM_OR_HIGH"
    ]
    minimumSensitivityScore: typing_extensions.Literal[
        "PROFILE_SCORE_BUCKET_UNSPECIFIED", "HIGH", "MEDIUM_OR_HIGH"
    ]

@typing.type_check_only
class GooglePrivacyDlpV2PubSubExpressions(typing_extensions.TypedDict, total=False):
    conditions: _list[GooglePrivacyDlpV2PubSubCondition]
    logicalOperator: typing_extensions.Literal[
        "LOGICAL_OPERATOR_UNSPECIFIED", "OR", "AND"
    ]

@typing.type_check_only
class GooglePrivacyDlpV2PubSubNotification(typing_extensions.TypedDict, total=False):
    detailOfMessage: typing_extensions.Literal[
        "DETAIL_LEVEL_UNSPECIFIED", "TABLE_PROFILE", "RESOURCE_NAME"
    ]
    event: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "NEW_PROFILE",
        "CHANGED_PROFILE",
        "SCORE_INCREASED",
        "ERROR_CHANGED",
    ]
    pubsubCondition: GooglePrivacyDlpV2DataProfilePubSubCondition
    topic: str

@typing.type_check_only
class GooglePrivacyDlpV2PublishFindingsToCloudDataCatalog(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2PublishSummaryToCscc(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2PublishToPubSub(typing_extensions.TypedDict, total=False):
    topic: str

@typing.type_check_only
class GooglePrivacyDlpV2PublishToStackdriver(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2QuasiId(typing_extensions.TypedDict, total=False):
    customTag: str
    field: GooglePrivacyDlpV2FieldId
    inferred: GoogleProtobufEmpty
    infoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2QuasiIdField(typing_extensions.TypedDict, total=False):
    customTag: str
    field: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2QuasiIdentifierField(typing_extensions.TypedDict, total=False):
    customTag: str
    field: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2QuoteInfo(typing_extensions.TypedDict, total=False):
    dateTime: GooglePrivacyDlpV2DateTime

@typing.type_check_only
class GooglePrivacyDlpV2Range(typing_extensions.TypedDict, total=False):
    end: str
    start: str

@typing.type_check_only
class GooglePrivacyDlpV2RecordCondition(typing_extensions.TypedDict, total=False):
    expressions: GooglePrivacyDlpV2Expressions

@typing.type_check_only
class GooglePrivacyDlpV2RecordKey(typing_extensions.TypedDict, total=False):
    bigQueryKey: GooglePrivacyDlpV2BigQueryKey
    datastoreKey: GooglePrivacyDlpV2DatastoreKey
    idValues: _list[str]

@typing.type_check_only
class GooglePrivacyDlpV2RecordLocation(typing_extensions.TypedDict, total=False):
    fieldId: GooglePrivacyDlpV2FieldId
    recordKey: GooglePrivacyDlpV2RecordKey
    tableLocation: GooglePrivacyDlpV2TableLocation

@typing.type_check_only
class GooglePrivacyDlpV2RecordSuppression(typing_extensions.TypedDict, total=False):
    condition: GooglePrivacyDlpV2RecordCondition

@typing.type_check_only
class GooglePrivacyDlpV2RecordTransformation(typing_extensions.TypedDict, total=False):
    containerTimestamp: str
    containerVersion: str
    fieldId: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2RecordTransformations(typing_extensions.TypedDict, total=False):
    fieldTransformations: _list[GooglePrivacyDlpV2FieldTransformation]
    recordSuppressions: _list[GooglePrivacyDlpV2RecordSuppression]

@typing.type_check_only
class GooglePrivacyDlpV2RedactConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GooglePrivacyDlpV2RedactImageRequest(typing_extensions.TypedDict, total=False):
    byteItem: GooglePrivacyDlpV2ByteContentItem
    imageRedactionConfigs: _list[GooglePrivacyDlpV2ImageRedactionConfig]
    includeFindings: bool
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    locationId: str

@typing.type_check_only
class GooglePrivacyDlpV2RedactImageResponse(typing_extensions.TypedDict, total=False):
    extractedText: str
    inspectResult: GooglePrivacyDlpV2InspectResult
    redactedImage: str

@typing.type_check_only
class GooglePrivacyDlpV2Regex(typing_extensions.TypedDict, total=False):
    groupIndexes: _list[int]
    pattern: str

@typing.type_check_only
class GooglePrivacyDlpV2ReidentifyContentRequest(
    typing_extensions.TypedDict, total=False
):
    inspectConfig: GooglePrivacyDlpV2InspectConfig
    inspectTemplateName: str
    item: GooglePrivacyDlpV2ContentItem
    locationId: str
    reidentifyConfig: GooglePrivacyDlpV2DeidentifyConfig
    reidentifyTemplateName: str

@typing.type_check_only
class GooglePrivacyDlpV2ReidentifyContentResponse(
    typing_extensions.TypedDict, total=False
):
    item: GooglePrivacyDlpV2ContentItem
    overview: GooglePrivacyDlpV2TransformationOverview

@typing.type_check_only
class GooglePrivacyDlpV2ReplaceDictionaryConfig(
    typing_extensions.TypedDict, total=False
):
    wordList: GooglePrivacyDlpV2WordList

@typing.type_check_only
class GooglePrivacyDlpV2ReplaceValueConfig(typing_extensions.TypedDict, total=False):
    newValue: GooglePrivacyDlpV2Value

@typing.type_check_only
class GooglePrivacyDlpV2ReplaceWithInfoTypeConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GooglePrivacyDlpV2RequestedOptions(typing_extensions.TypedDict, total=False):
    jobConfig: GooglePrivacyDlpV2InspectJobConfig
    snapshotInspectTemplate: GooglePrivacyDlpV2InspectTemplate

@typing.type_check_only
class GooglePrivacyDlpV2RequestedRiskAnalysisOptions(
    typing_extensions.TypedDict, total=False
):
    jobConfig: GooglePrivacyDlpV2RiskAnalysisJobConfig

@typing.type_check_only
class GooglePrivacyDlpV2Result(typing_extensions.TypedDict, total=False):
    hybridStats: GooglePrivacyDlpV2HybridInspectStatistics
    infoTypeStats: _list[GooglePrivacyDlpV2InfoTypeStats]
    processedBytes: str
    totalEstimatedBytes: str

@typing.type_check_only
class GooglePrivacyDlpV2RiskAnalysisJobConfig(typing_extensions.TypedDict, total=False):
    actions: _list[GooglePrivacyDlpV2Action]
    privacyMetric: GooglePrivacyDlpV2PrivacyMetric
    sourceTable: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2Row(typing_extensions.TypedDict, total=False):
    values: _list[GooglePrivacyDlpV2Value]

@typing.type_check_only
class GooglePrivacyDlpV2SaveFindings(typing_extensions.TypedDict, total=False):
    outputConfig: GooglePrivacyDlpV2OutputStorageConfig

@typing.type_check_only
class GooglePrivacyDlpV2Schedule(typing_extensions.TypedDict, total=False):
    recurrencePeriodDuration: str

@typing.type_check_only
class GooglePrivacyDlpV2SelectedInfoTypes(typing_extensions.TypedDict, total=False):
    infoTypes: _list[GooglePrivacyDlpV2InfoType]

@typing.type_check_only
class GooglePrivacyDlpV2SensitivityScore(typing_extensions.TypedDict, total=False):
    score: typing_extensions.Literal[
        "SENSITIVITY_SCORE_UNSPECIFIED",
        "SENSITIVITY_LOW",
        "SENSITIVITY_MODERATE",
        "SENSITIVITY_HIGH",
    ]

@typing.type_check_only
class GooglePrivacyDlpV2StatisticalTable(typing_extensions.TypedDict, total=False):
    quasiIds: _list[GooglePrivacyDlpV2QuasiIdentifierField]
    relativeFrequency: GooglePrivacyDlpV2FieldId
    table: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2StorageConfig(typing_extensions.TypedDict, total=False):
    bigQueryOptions: GooglePrivacyDlpV2BigQueryOptions
    cloudStorageOptions: GooglePrivacyDlpV2CloudStorageOptions
    datastoreOptions: GooglePrivacyDlpV2DatastoreOptions
    hybridOptions: GooglePrivacyDlpV2HybridOptions
    timespanConfig: GooglePrivacyDlpV2TimespanConfig

@typing.type_check_only
class GooglePrivacyDlpV2StorageMetadataLabel(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class GooglePrivacyDlpV2StoredInfoType(typing_extensions.TypedDict, total=False):
    currentVersion: GooglePrivacyDlpV2StoredInfoTypeVersion
    name: str
    pendingVersions: _list[GooglePrivacyDlpV2StoredInfoTypeVersion]

@typing.type_check_only
class GooglePrivacyDlpV2StoredInfoTypeConfig(typing_extensions.TypedDict, total=False):
    description: str
    dictionary: GooglePrivacyDlpV2Dictionary
    displayName: str
    largeCustomDictionary: GooglePrivacyDlpV2LargeCustomDictionaryConfig
    regex: GooglePrivacyDlpV2Regex

@typing.type_check_only
class GooglePrivacyDlpV2StoredInfoTypeStats(typing_extensions.TypedDict, total=False):
    largeCustomDictionary: GooglePrivacyDlpV2LargeCustomDictionaryStats

@typing.type_check_only
class GooglePrivacyDlpV2StoredInfoTypeVersion(typing_extensions.TypedDict, total=False):
    config: GooglePrivacyDlpV2StoredInfoTypeConfig
    createTime: str
    errors: _list[GooglePrivacyDlpV2Error]
    state: typing_extensions.Literal[
        "STORED_INFO_TYPE_STATE_UNSPECIFIED", "PENDING", "READY", "FAILED", "INVALID"
    ]
    stats: GooglePrivacyDlpV2StoredInfoTypeStats

@typing.type_check_only
class GooglePrivacyDlpV2StoredType(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str

@typing.type_check_only
class GooglePrivacyDlpV2SummaryResult(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "TRANSFORMATION_RESULT_CODE_UNSPECIFIED", "SUCCESS", "ERROR"
    ]
    count: str
    details: str

@typing.type_check_only
class GooglePrivacyDlpV2SurrogateType(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GooglePrivacyDlpV2Table(typing_extensions.TypedDict, total=False):
    headers: _list[GooglePrivacyDlpV2FieldId]
    rows: _list[GooglePrivacyDlpV2Row]

@typing.type_check_only
class GooglePrivacyDlpV2TableDataProfile(typing_extensions.TypedDict, total=False):
    configSnapshot: GooglePrivacyDlpV2DataProfileConfigSnapshot
    createTime: str
    dataRiskLevel: GooglePrivacyDlpV2DataRiskLevel
    datasetId: str
    datasetLocation: str
    datasetProjectId: str
    encryptionStatus: typing_extensions.Literal[
        "ENCRYPTION_STATUS_UNSPECIFIED",
        "ENCRYPTION_GOOGLE_MANAGED",
        "ENCRYPTION_CUSTOMER_MANAGED",
    ]
    expirationTime: str
    failedColumnCount: str
    fullResource: str
    lastModifiedTime: str
    name: str
    otherInfoTypes: _list[GooglePrivacyDlpV2OtherInfoTypeSummary]
    predictedInfoTypes: _list[GooglePrivacyDlpV2InfoTypeSummary]
    profileLastGenerated: str
    profileStatus: GooglePrivacyDlpV2ProfileStatus
    projectDataProfile: str
    resourceLabels: dict[str, typing.Any]
    resourceVisibility: typing_extensions.Literal[
        "RESOURCE_VISIBILITY_UNSPECIFIED",
        "RESOURCE_VISIBILITY_PUBLIC",
        "RESOURCE_VISIBILITY_RESTRICTED",
    ]
    rowCount: str
    scannedColumnCount: str
    sensitivityScore: GooglePrivacyDlpV2SensitivityScore
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "RUNNING", "DONE"]
    tableId: str
    tableSizeBytes: str

@typing.type_check_only
class GooglePrivacyDlpV2TableLocation(typing_extensions.TypedDict, total=False):
    rowIndex: str

@typing.type_check_only
class GooglePrivacyDlpV2TableOptions(typing_extensions.TypedDict, total=False):
    identifyingFields: _list[GooglePrivacyDlpV2FieldId]

@typing.type_check_only
class GooglePrivacyDlpV2TaggedField(typing_extensions.TypedDict, total=False):
    customTag: str
    field: GooglePrivacyDlpV2FieldId
    inferred: GoogleProtobufEmpty
    infoType: GooglePrivacyDlpV2InfoType

@typing.type_check_only
class GooglePrivacyDlpV2ThrowError(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
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

@typing.type_check_only
class GooglePrivacyDlpV2TimeZone(typing_extensions.TypedDict, total=False):
    offsetMinutes: int

@typing.type_check_only
class GooglePrivacyDlpV2TimespanConfig(typing_extensions.TypedDict, total=False):
    enableAutoPopulationOfTimespanConfig: bool
    endTime: str
    startTime: str
    timestampField: GooglePrivacyDlpV2FieldId

@typing.type_check_only
class GooglePrivacyDlpV2TransformationConfig(typing_extensions.TypedDict, total=False):
    deidentifyTemplate: str
    imageRedactTemplate: str
    structuredDeidentifyTemplate: str

@typing.type_check_only
class GooglePrivacyDlpV2TransformationDescription(
    typing_extensions.TypedDict, total=False
):
    condition: str
    description: str
    infoType: GooglePrivacyDlpV2InfoType
    type: typing_extensions.Literal[
        "TRANSFORMATION_TYPE_UNSPECIFIED",
        "RECORD_SUPPRESSION",
        "REPLACE_VALUE",
        "REPLACE_DICTIONARY",
        "REDACT",
        "CHARACTER_MASK",
        "CRYPTO_REPLACE_FFX_FPE",
        "FIXED_SIZE_BUCKETING",
        "BUCKETING",
        "REPLACE_WITH_INFO_TYPE",
        "TIME_PART",
        "CRYPTO_HASH",
        "DATE_SHIFT",
        "CRYPTO_DETERMINISTIC_CONFIG",
        "REDACT_IMAGE",
    ]

@typing.type_check_only
class GooglePrivacyDlpV2TransformationDetails(typing_extensions.TypedDict, total=False):
    containerName: str
    resourceName: str
    statusDetails: GooglePrivacyDlpV2TransformationResultStatus
    transformation: _list[GooglePrivacyDlpV2TransformationDescription]
    transformationLocation: GooglePrivacyDlpV2TransformationLocation
    transformedBytes: str

@typing.type_check_only
class GooglePrivacyDlpV2TransformationDetailsStorageConfig(
    typing_extensions.TypedDict, total=False
):
    table: GooglePrivacyDlpV2BigQueryTable

@typing.type_check_only
class GooglePrivacyDlpV2TransformationErrorHandling(
    typing_extensions.TypedDict, total=False
):
    leaveUntransformed: GooglePrivacyDlpV2LeaveUntransformed
    throwError: GooglePrivacyDlpV2ThrowError

@typing.type_check_only
class GooglePrivacyDlpV2TransformationLocation(
    typing_extensions.TypedDict, total=False
):
    containerType: typing_extensions.Literal[
        "TRANSFORM_UNKNOWN_CONTAINER",
        "TRANSFORM_BODY",
        "TRANSFORM_METADATA",
        "TRANSFORM_TABLE",
    ]
    findingId: str
    recordTransformation: GooglePrivacyDlpV2RecordTransformation

@typing.type_check_only
class GooglePrivacyDlpV2TransformationOverview(
    typing_extensions.TypedDict, total=False
):
    transformationSummaries: _list[GooglePrivacyDlpV2TransformationSummary]
    transformedBytes: str

@typing.type_check_only
class GooglePrivacyDlpV2TransformationResultStatus(
    typing_extensions.TypedDict, total=False
):
    details: GoogleRpcStatus
    resultStatusType: typing_extensions.Literal[
        "STATE_TYPE_UNSPECIFIED",
        "INVALID_TRANSFORM",
        "BIGQUERY_MAX_ROW_SIZE_EXCEEDED",
        "METADATA_UNRETRIEVABLE",
        "SUCCESS",
    ]

@typing.type_check_only
class GooglePrivacyDlpV2TransformationSummary(typing_extensions.TypedDict, total=False):
    field: GooglePrivacyDlpV2FieldId
    fieldTransformations: _list[GooglePrivacyDlpV2FieldTransformation]
    infoType: GooglePrivacyDlpV2InfoType
    recordSuppress: GooglePrivacyDlpV2RecordSuppression
    results: _list[GooglePrivacyDlpV2SummaryResult]
    transformation: GooglePrivacyDlpV2PrimitiveTransformation
    transformedBytes: str

@typing.type_check_only
class GooglePrivacyDlpV2TransientCryptoKey(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class GooglePrivacyDlpV2Trigger(typing_extensions.TypedDict, total=False):
    manual: GooglePrivacyDlpV2Manual
    schedule: GooglePrivacyDlpV2Schedule

@typing.type_check_only
class GooglePrivacyDlpV2UnwrappedCryptoKey(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class GooglePrivacyDlpV2UpdateDeidentifyTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    deidentifyTemplate: GooglePrivacyDlpV2DeidentifyTemplate
    updateMask: str

@typing.type_check_only
class GooglePrivacyDlpV2UpdateInspectTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    inspectTemplate: GooglePrivacyDlpV2InspectTemplate
    updateMask: str

@typing.type_check_only
class GooglePrivacyDlpV2UpdateJobTriggerRequest(
    typing_extensions.TypedDict, total=False
):
    jobTrigger: GooglePrivacyDlpV2JobTrigger
    updateMask: str

@typing.type_check_only
class GooglePrivacyDlpV2UpdateStoredInfoTypeRequest(
    typing_extensions.TypedDict, total=False
):
    config: GooglePrivacyDlpV2StoredInfoTypeConfig
    updateMask: str

@typing.type_check_only
class GooglePrivacyDlpV2Value(typing_extensions.TypedDict, total=False):
    booleanValue: bool
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
    floatValue: float
    integerValue: str
    stringValue: str
    timeValue: GoogleTypeTimeOfDay
    timestampValue: str

@typing.type_check_only
class GooglePrivacyDlpV2ValueFrequency(typing_extensions.TypedDict, total=False):
    count: str
    value: GooglePrivacyDlpV2Value

@typing.type_check_only
class GooglePrivacyDlpV2VersionDescription(typing_extensions.TypedDict, total=False):
    description: str
    version: str

@typing.type_check_only
class GooglePrivacyDlpV2WordList(typing_extensions.TypedDict, total=False):
    words: _list[str]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeTimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int
