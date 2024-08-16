import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiDistribution(typing_extensions.TypedDict, total=False):
    bucketCounts: _list[str]
    bucketOptions: GoogleApiDistributionBucketOptions
    count: str
    exemplars: _list[GoogleApiDistributionExemplar]
    mean: float
    range: GoogleApiDistributionRange
    sumOfSquaredDeviation: float

@typing.type_check_only
class GoogleApiDistributionBucketOptions(typing_extensions.TypedDict, total=False):
    explicitBuckets: GoogleApiDistributionBucketOptionsExplicit
    exponentialBuckets: GoogleApiDistributionBucketOptionsExponential
    linearBuckets: GoogleApiDistributionBucketOptionsLinear

@typing.type_check_only
class GoogleApiDistributionBucketOptionsExplicit(
    typing_extensions.TypedDict, total=False
):
    bounds: _list[float]

@typing.type_check_only
class GoogleApiDistributionBucketOptionsExponential(
    typing_extensions.TypedDict, total=False
):
    growthFactor: float
    numFiniteBuckets: int
    scale: float

@typing.type_check_only
class GoogleApiDistributionBucketOptionsLinear(
    typing_extensions.TypedDict, total=False
):
    numFiniteBuckets: int
    offset: float
    width: float

@typing.type_check_only
class GoogleApiDistributionExemplar(typing_extensions.TypedDict, total=False):
    attachments: _list[dict[str, typing.Any]]
    timestamp: str
    value: float

@typing.type_check_only
class GoogleApiDistributionRange(typing_extensions.TypedDict, total=False):
    max: float
    min: float

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleApiMonitoredResource(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingErrorContext(
    typing_extensions.TypedDict, total=False
):
    httpRequest: GoogleCloudDiscoveryengineLoggingHttpRequestContext
    reportLocation: GoogleCloudDiscoveryengineLoggingSourceLocation

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingErrorLog(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudDiscoveryengineLoggingErrorContext
    importPayload: GoogleCloudDiscoveryengineLoggingImportErrorContext
    message: str
    requestPayload: dict[str, typing.Any]
    responsePayload: dict[str, typing.Any]
    serviceContext: GoogleCloudDiscoveryengineLoggingServiceContext
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingHttpRequestContext(
    typing_extensions.TypedDict, total=False
):
    responseStatusCode: int

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingImportErrorContext(
    typing_extensions.TypedDict, total=False
):
    document: str
    gcsPath: str
    lineNumber: str
    operation: str
    userEvent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingServiceContext(
    typing_extensions.TypedDict, total=False
):
    service: str

@typing.type_check_only
class GoogleCloudDiscoveryengineLoggingSourceLocation(
    typing_extensions.TypedDict, total=False
):
    functionName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1BatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1TargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Condition(typing_extensions.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1ConditionTimeRange]
    queryTerms: _list[GoogleCloudDiscoveryengineV1ConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Control(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1ControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1Condition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1ControlFilterAction
    name: str
    redirectAction: GoogleCloudDiscoveryengineV1ControlRedirectAction
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1ControlSynonymsAction
    useCases: _list[
        typing_extensions.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlBoostAction(
    typing_extensions.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlFilterAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ControlSynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1CreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DataStore(typing_extensions.TypedDict, total=False):
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED", "NO_CONTENT", "CONTENT_REQUIRED", "PUBLIC_WEBSITE"
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfig
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    name: str
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1Schema

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DeleteTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfig
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EnableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Engine(typing_extensions.TypedDict, total=False):
    chatEngineConfig: GoogleCloudDiscoveryengineV1EngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1EngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1EngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    name: str
    searchEngineConfig: GoogleCloudDiscoveryengineV1EngineSearchEngineConfig
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineConfig(
    typing_extensions.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig
    )
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineConfigAgentCreationConfig(
    typing_extensions.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineChatEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineCommonConfig(
    typing_extensions.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1EngineSearchEngineConfig(
    typing_extensions.TypedDict, total=False
):
    searchAddOns: _list[
        typing_extensions.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing_extensions.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1ImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Project(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProjectServiceTerms(
    typing_extensions.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1ProvisionProjectMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeSucceeded: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1PurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1Schema(typing_extensions.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1SiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSite(typing_extensions.TypedDict, total=False):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1TargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing_extensions.Literal[
        "INDEXING_STATUS_UNSPECIFIED", "PENDING", "FAILED", "SUCCEEDED", "DELETING"
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1SiteVerificationInfo
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteFailureReason(
    typing_extensions.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1TargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1TargetSiteFailureReasonQuotaFailure(
    typing_extensions.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1UpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAclConfig(
    typing_extensions.TypedDict, total=False
):
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAlloyDbSource(
    typing_extensions.TypedDict, total=False
):
    clusterId: str
    databaseId: str
    gcsStagingDir: str
    locationId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswer(typing_extensions.TypedDict, total=False):
    answerSkippedReasons: _list[
        typing_extensions.Literal[
            "ANSWER_SKIPPED_REASON_UNSPECIFIED",
            "ADVERSARIAL_QUERY_IGNORED",
            "NON_ANSWER_SEEKING_QUERY_IGNORED",
            "OUT_OF_DOMAIN_QUERY_IGNORED",
            "POTENTIAL_POLICY_VIOLATION",
            "NO_RELEVANT_CONTENT",
            "JAIL_BREAKING_QUERY_IGNORED",
        ]
    ]
    answerText: str
    citations: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitation]
    completeTime: str
    createTime: str
    name: str
    queryUnderstandingInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfo
    )
    references: _list[GoogleCloudDiscoveryengineV1alphaAnswerReference]
    relatedQuestions: _list[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED"
    ]
    steps: _list[GoogleCloudDiscoveryengineV1alphaAnswerStep]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1alphaAnswerCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerCitationSource(
    typing_extensions.TypedDict, total=False
):
    referenceId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequest(
    typing_extensions.TypedDict, total=False
):
    answerGenerationSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpec
    )
    asynchronousMode: bool
    query: GoogleCloudDiscoveryengineV1alphaQuery
    queryUnderstandingSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpec
    )
    relatedQuestionsSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestRelatedQuestionsSpec
    )
    safetySpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSafetySpec
    searchSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpec
    session: str
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpec(
    typing_extensions.TypedDict, total=False
):
    answerLanguageCode: str
    ignoreAdversarialQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonAnswerSeekingQuery: bool
    includeCitations: bool
    modelSpec: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecModelSpec
    )
    promptSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecPromptSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    modelVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestAnswerGenerationSpecPromptSpec(
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpec(
    typing_extensions.TypedDict, total=False
):
    queryClassificationSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec
    queryRephraserSpec: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryClassificationSpec(
    typing_extensions.TypedDict, total=False
):
    types: _list[
        typing_extensions.Literal[
            "TYPE_UNSPECIFIED",
            "ADVERSARIAL_QUERY",
            "NON_ANSWER_SEEKING_QUERY",
            "JAIL_BREAKING_QUERY",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestQueryUnderstandingSpecQueryRephraserSpec(
    typing_extensions.TypedDict, total=False
):
    disable: bool
    maxRephraseSteps: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestRelatedQuestionsSpec(
    typing_extensions.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSafetySpec(
    typing_extensions.TypedDict, total=False
):
    enable: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpec(
    typing_extensions.TypedDict, total=False
):
    searchParams: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchParams
    )
    searchResultList: (
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultList
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchParams(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec]
    filter: str
    maxReturnResults: int
    orderBy: str
    searchResultMode: typing_extensions.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultList(
    typing_extensions.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResult(
    typing_extensions.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo
    unstructuredDocumentInfo: GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultChunkInfo(
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    document: str
    documentContexts: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoDocumentContext
    ]
    extractiveAnswers: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer
    ]
    extractiveSegments: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment
    ]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoDocumentContext(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveAnswer(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryRequestSearchSpecSearchResultListSearchResultUnstructuredDocumentInfoExtractiveSegment(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryResponse(
    typing_extensions.TypedDict, total=False
):
    answer: GoogleCloudDiscoveryengineV1alphaAnswer
    answerQueryToken: str
    session: GoogleCloudDiscoveryengineV1alphaSession

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfo(
    typing_extensions.TypedDict, total=False
):
    queryClassificationInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfoQueryClassificationInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerQueryUnderstandingInfoQueryClassificationInfo(
    typing_extensions.TypedDict, total=False
):
    positive: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "ADVERSARIAL_QUERY",
        "NON_ANSWER_SEEKING_QUERY",
        "JAIL_BREAKING_QUERY",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReference(
    typing_extensions.TypedDict, total=False
):
    chunkInfo: GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfo
    structuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceStructuredDocumentInfo
    )
    unstructuredDocumentInfo: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfo
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfo(
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    documentMetadata: (
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfoDocumentMetadata
    )
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceChunkInfoDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    document: str
    pageIdentifier: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceStructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    document: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfoChunkContent
    ]
    document: str
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerReferenceUnstructuredDocumentInfoChunkContent(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStep(
    typing_extensions.TypedDict, total=False
):
    actions: _list[GoogleCloudDiscoveryengineV1alphaAnswerStepAction]
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "FAILED", "SUCCEEDED"
    ]
    thought: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepAction(
    typing_extensions.TypedDict, total=False
):
    observation: GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservation
    searchAction: GoogleCloudDiscoveryengineV1alphaAnswerStepActionSearchAction

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservation(
    typing_extensions.TypedDict, total=False
):
    searchResults: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResult
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResult(
    typing_extensions.TypedDict, total=False
):
    chunkInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultChunkInfo
    ]
    document: str
    snippetInfo: _list[
        GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultSnippetInfo
    ]
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultChunkInfo(
    typing_extensions.TypedDict, total=False
):
    chunk: str
    content: str
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionObservationSearchResultSnippetInfo(
    typing_extensions.TypedDict, total=False
):
    snippet: str
    snippetStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaAnswerStepActionSearchAction(
    typing_extensions.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleCloudDiscoveryengineV1alphaCreateTargetSiteRequest]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBatchVerifyTargetSitesRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigtableOptions(
    typing_extensions.TypedDict, total=False
):
    families: dict[str, typing.Any]
    keyFieldName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigtableOptionsBigtableColumn(
    typing_extensions.TypedDict, total=False
):
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "TEXT", "BINARY"]
    fieldName: str
    qualifier: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "STRING",
        "NUMBER",
        "INTEGER",
        "VAR_INTEGER",
        "BIG_NUMERIC",
        "BOOLEAN",
        "JSON",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigtableOptionsBigtableColumnFamily(
    typing_extensions.TypedDict, total=False
):
    columns: _list[GoogleCloudDiscoveryengineV1alphaBigtableOptionsBigtableColumn]
    encoding: typing_extensions.Literal["ENCODING_UNSPECIFIED", "TEXT", "BINARY"]
    fieldName: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "STRING",
        "NUMBER",
        "INTEGER",
        "VAR_INTEGER",
        "BIG_NUMERIC",
        "BOOLEAN",
        "JSON",
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaBigtableSource(
    typing_extensions.TypedDict, total=False
):
    bigtableOptions: GoogleCloudDiscoveryengineV1alphaBigtableOptions
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingRequest(
    typing_extensions.TypedDict, total=False
):
    answerCandidate: str
    facts: _list[GoogleCloudDiscoveryengineV1alphaGroundingFact]
    groundingSpec: GoogleCloudDiscoveryengineV1alphaCheckGroundingSpec
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingResponse(
    typing_extensions.TypedDict, total=False
):
    citedChunks: _list[GoogleCloudDiscoveryengineV1alphaFactChunk]
    claims: _list[GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseClaim]
    supportScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingResponseClaim(
    typing_extensions.TypedDict, total=False
):
    citationIndices: _list[int]
    claimText: str
    endPos: int
    groundingCheckRequired: bool
    startPos: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckGroundingSpec(
    typing_extensions.TypedDict, total=False
):
    citationThreshold: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementRequest(
    typing_extensions.TypedDict, total=False
):
    requirementType: str
    resources: _list[GoogleApiMonitoredResource]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementResponse(
    typing_extensions.TypedDict, total=False
):
    metricResults: _list[
        GoogleCloudDiscoveryengineV1alphaCheckRequirementResponseMetricQueryResult
    ]
    oldestMetricTimestamp: str
    requirement: GoogleCloudDiscoveryengineV1alphaRequirement
    requirementCondition: GoogleTypeExpr
    requirementResult: typing_extensions.Literal[
        "UNKNOWN", "SUCCESS", "FAILURE", "WARNING"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCheckRequirementResponseMetricQueryResult(
    typing_extensions.TypedDict, total=False
):
    metricType: str
    name: str
    timestamp: str
    unit: str
    value: GoogleMonitoringV3TypedValue

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunk(typing_extensions.TypedDict, total=False):
    chunkMetadata: GoogleCloudDiscoveryengineV1alphaChunkChunkMetadata
    content: str
    derivedStructData: dict[str, typing.Any]
    documentMetadata: GoogleCloudDiscoveryengineV1alphaChunkDocumentMetadata
    id: str
    name: str
    pageSpan: GoogleCloudDiscoveryengineV1alphaChunkPageSpan
    relevanceScore: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkChunkMetadata(
    typing_extensions.TypedDict, total=False
):
    nextChunks: _list[GoogleCloudDiscoveryengineV1alphaChunk]
    previousChunks: _list[GoogleCloudDiscoveryengineV1alphaChunk]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkDocumentMetadata(
    typing_extensions.TypedDict, total=False
):
    structData: dict[str, typing.Any]
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaChunkPageSpan(
    typing_extensions.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCloudSqlSource(
    typing_extensions.TypedDict, total=False
):
    databaseId: str
    gcsStagingDir: str
    instanceId: str
    offload: bool
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    querySuggestions: _list[
        GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseQuerySuggestion
    ]
    tailMatchTriggered: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompleteQueryResponseQuerySuggestion(
    typing_extensions.TypedDict, total=False
):
    completableFieldPaths: _list[str]
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompletionInfo(
    typing_extensions.TypedDict, total=False
):
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCompletionSuggestion(
    typing_extensions.TypedDict, total=False
):
    alternativePhrases: _list[str]
    frequency: str
    globalScore: float
    groupId: str
    groupScore: float
    languageCode: str
    suggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCondition(
    typing_extensions.TypedDict, total=False
):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1alphaConditionTimeRange]
    queryTerms: _list[GoogleCloudDiscoveryengineV1alphaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControl(
    typing_extensions.TypedDict, total=False
):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1alphaControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1alphaCondition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1alphaControlFilterAction
    name: str
    redirectAction: GoogleCloudDiscoveryengineV1alphaControlRedirectAction
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1alphaControlSynonymsAction
    useCases: _list[
        typing_extensions.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlBoostAction(
    typing_extensions.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlFilterAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaControlSynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConversation(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    messages: _list[GoogleCloudDiscoveryengineV1alphaConversationMessage]
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETED"]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConversationContext(
    typing_extensions.TypedDict, total=False
):
    activeDocument: str
    contextDocuments: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConversationMessage(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    reply: GoogleCloudDiscoveryengineV1alphaReply
    userInput: GoogleCloudDiscoveryengineV1alphaTextInput

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConverseConversationRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    conversation: GoogleCloudDiscoveryengineV1alphaConversation
    filter: str
    query: GoogleCloudDiscoveryengineV1alphaTextInput
    safeSearch: bool
    servingConfig: str
    summarySpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec
    )
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaConverseConversationResponse(
    typing_extensions.TypedDict, total=False
):
    conversation: GoogleCloudDiscoveryengineV1alphaConversation
    relatedQuestions: _list[str]
    reply: GoogleCloudDiscoveryengineV1alphaReply
    searchResults: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateEvaluationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCreateTargetSiteRequest(
    typing_extensions.TypedDict, total=False
):
    parent: str
    targetSite: GoogleCloudDiscoveryengineV1alphaTargetSite

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomAttribute(
    typing_extensions.TypedDict, total=False
):
    numbers: _list[float]
    text: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec(
    typing_extensions.TypedDict, total=False
):
    enableSearchAdaptor: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaCustomTuningModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    metrics: dict[str, typing.Any]
    modelState: typing_extensions.Literal[
        "MODEL_STATE_UNSPECIFIED",
        "TRAINING_PAUSED",
        "TRAINING",
        "TRAINING_COMPLETE",
        "READY_FOR_SERVING",
        "TRAINING_FAILED",
        "NO_IMPROVEMENT",
    ]
    modelVersion: str
    name: str
    trainingStartTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDataStore(
    typing_extensions.TypedDict, total=False
):
    aclEnabled: bool
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED", "NO_CONTENT", "CONTENT_REQUIRED", "PUBLIC_WEBSITE"
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig
    idpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfig
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    languageInfo: GoogleCloudDiscoveryengineV1alphaLanguageInfo
    name: str
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1alphaSchema

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDeleteTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocument(
    typing_extensions.TypedDict, total=False
):
    aclInfo: GoogleCloudDiscoveryengineV1alphaDocumentAclInfo
    content: GoogleCloudDiscoveryengineV1alphaDocumentContent
    derivedStructData: dict[str, typing.Any]
    id: str
    indexTime: str
    jsonData: str
    name: str
    parentDocumentId: str
    schemaId: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentAclInfo(
    typing_extensions.TypedDict, total=False
):
    readers: _list[GoogleCloudDiscoveryengineV1alphaDocumentAclInfoAccessRestriction]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentAclInfoAccessRestriction(
    typing_extensions.TypedDict, total=False
):
    idpWide: bool
    principals: _list[GoogleCloudDiscoveryengineV1alphaPrincipal]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentContent(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    rawBytes: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    id: str
    joined: bool
    name: str
    promotionIds: _list[str]
    quantity: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkingConfig: (
        GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfig
    )
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaDoubleList(
    typing_extensions.TypedDict, total=False
):
    values: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEmbeddingConfig(
    typing_extensions.TypedDict, total=False
):
    fieldPath: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEnableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngine(typing_extensions.TypedDict, total=False):
    chatEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1alphaEngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    mediaRecommendationEngineConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig
    )
    name: str
    recommendationMetadata: (
        GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata
    )
    searchEngineConfig: GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig
    similarDocumentsConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfig
    )
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig(
    typing_extensions.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig
    )
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig(
    typing_extensions.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineChatEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineCommonConfig(
    typing_extensions.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfig(
    typing_extensions.TypedDict, total=False
):
    optimizationObjective: str
    optimizationObjectiveConfig: GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    type: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig(
    typing_extensions.TypedDict, total=False
):
    targetField: str
    targetFieldValueFloat: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineRecommendationMetadata(
    typing_extensions.TypedDict, total=False
):
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    lastTuneTime: str
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    tuningOperation: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineSearchEngineConfig(
    typing_extensions.TypedDict, total=False
):
    searchAddOns: _list[
        typing_extensions.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing_extensions.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEngineSimilarDocumentsEngineConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequest(
    typing_extensions.TypedDict, total=False
):
    fileDataSource: (
        GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestFileDataSource
    )
    websiteDataSource: (
        GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestFileDataSource(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSource(
    typing_extensions.TypedDict, total=False
):
    estimatorUriPatterns: _list[
        GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSourceEstimatorUriPattern
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeRequestWebsiteDataSourceEstimatorUriPattern(
    typing_extensions.TypedDict, total=False
):
    exactMatch: bool
    exclusive: bool
    providedUriPattern: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEstimateDataSizeResponse(
    typing_extensions.TypedDict, total=False
):
    dataSizeBytes: str
    documentCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluation(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    errorSamples: _list[GoogleRpcStatus]
    evaluationSpec: GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpec
    name: str
    qualityMetrics: GoogleCloudDiscoveryengineV1alphaQualityMetrics
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpec(
    typing_extensions.TypedDict, total=False
):
    querySetSpec: GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpecQuerySetSpec
    searchRequest: GoogleCloudDiscoveryengineV1alphaSearchRequest

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaEvaluationEvaluationSpecQuerySetSpec(
    typing_extensions.TypedDict, total=False
):
    sampleQuerySet: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFactChunk(
    typing_extensions.TypedDict, total=False
):
    chunkText: str
    index: int
    source: str
    sourceMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFetchDomainVerificationStatusResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFhirStoreSource(
    typing_extensions.TypedDict, total=False
):
    fhirStore: str
    gcsStagingDir: str
    resourceTypes: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFieldConfig(
    typing_extensions.TypedDict, total=False
):
    advancedSiteSearchDataSources: _list[
        typing_extensions.Literal[
            "ADVANCED_SITE_SEARCH_DATA_SOURCE_UNSPECIFIED",
            "METATAGS",
            "PAGEMAP",
            "URI_PATTERN_MAPPING",
            "SCHEMA_ORG",
        ]
    ]
    completableOption: typing_extensions.Literal[
        "COMPLETABLE_OPTION_UNSPECIFIED", "COMPLETABLE_ENABLED", "COMPLETABLE_DISABLED"
    ]
    dynamicFacetableOption: typing_extensions.Literal[
        "DYNAMIC_FACETABLE_OPTION_UNSPECIFIED",
        "DYNAMIC_FACETABLE_ENABLED",
        "DYNAMIC_FACETABLE_DISABLED",
    ]
    fieldPath: str
    fieldType: typing_extensions.Literal[
        "FIELD_TYPE_UNSPECIFIED",
        "OBJECT",
        "STRING",
        "NUMBER",
        "INTEGER",
        "BOOLEAN",
        "GEOLOCATION",
        "DATETIME",
    ]
    indexableOption: typing_extensions.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    keyPropertyType: str
    recsFilterableOption: typing_extensions.Literal[
        "FILTERABLE_OPTION_UNSPECIFIED", "FILTERABLE_ENABLED", "FILTERABLE_DISABLED"
    ]
    retrievableOption: typing_extensions.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    schemaOrgPaths: _list[str]
    searchableOption: typing_extensions.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaFirestoreSource(
    typing_extensions.TypedDict, total=False
):
    collectionId: str
    databaseId: str
    gcsStagingDir: str
    projectId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGcsSource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGetUriPatternDocumentDataResponse(
    typing_extensions.TypedDict, total=False
):
    documentDataMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGroundingFact(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    factText: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaGuidedSearchSpec(
    typing_extensions.TypedDict, total=False
):
    enableRefinementAttributes: bool
    enableRelatedQuestions: bool
    maxRelatedQuestions: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdpConfig(
    typing_extensions.TypedDict, total=False
):
    externalIdpConfig: GoogleCloudDiscoveryengineV1alphaIdpConfigExternalIdpConfig
    idpType: typing_extensions.Literal["IDP_TYPE_UNSPECIFIED", "GSUITE", "THIRD_PARTY"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaIdpConfigExternalIdpConfig(
    typing_extensions.TypedDict, total=False
):
    workforcePoolName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    suggestions: _list[GoogleCloudDiscoveryengineV1alphaCompletionSuggestion]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    alloyDbSource: GoogleCloudDiscoveryengineV1alphaAlloyDbSource
    autoGenerateIds: bool
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    bigtableSource: GoogleCloudDiscoveryengineV1alphaBigtableSource
    cloudSqlSource: GoogleCloudDiscoveryengineV1alphaCloudSqlSource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    fhirStoreSource: GoogleCloudDiscoveryengineV1alphaFhirStoreSource
    firestoreSource: GoogleCloudDiscoveryengineV1alphaFirestoreSource
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    idField: str
    inlineSource: GoogleCloudDiscoveryengineV1alphaImportDocumentsRequestInlineSource
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    spannerSource: GoogleCloudDiscoveryengineV1alphaSpannerSource
    updateMask: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocument]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: (
        GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequestInlineSource
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    sampleQueries: _list[GoogleCloudDiscoveryengineV1alphaSampleQuery]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSampleQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequest(
    typing_extensions.TypedDict, total=False
):
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudDiscoveryengineV1alphaSuggestionDenyListEntry]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1alphaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1alphaImportUserEventsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudDiscoveryengineV1alphaUserEvent]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaInterval(
    typing_extensions.TypedDict, total=False
):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaLanguageInfo(
    typing_extensions.TypedDict, total=False
):
    language: str
    languageCode: str
    normalizedLanguageCode: str
    region: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListChunksResponse(
    typing_extensions.TypedDict, total=False
):
    chunks: _list[GoogleCloudDiscoveryengineV1alphaChunk]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListControlsResponse(
    typing_extensions.TypedDict, total=False
):
    controls: _list[GoogleCloudDiscoveryengineV1alphaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListConversationsResponse(
    typing_extensions.TypedDict, total=False
):
    conversations: _list[GoogleCloudDiscoveryengineV1alphaConversation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListCustomModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudDiscoveryengineV1alphaCustomTuningModel]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListDataStoresResponse(
    typing_extensions.TypedDict, total=False
):
    dataStores: _list[GoogleCloudDiscoveryengineV1alphaDataStore]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocument]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEnginesResponse(
    typing_extensions.TypedDict, total=False
):
    engines: _list[GoogleCloudDiscoveryengineV1alphaEngine]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponse(
    typing_extensions.TypedDict, total=False
):
    evaluationResults: _list[
        GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseEvaluationResult
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationResultsResponseEvaluationResult(
    typing_extensions.TypedDict, total=False
):
    qualityMetrics: GoogleCloudDiscoveryengineV1alphaQualityMetrics
    sampleQuery: GoogleCloudDiscoveryengineV1alphaSampleQuery

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListEvaluationsResponse(
    typing_extensions.TypedDict, total=False
):
    evaluations: _list[GoogleCloudDiscoveryengineV1alphaEvaluation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSampleQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sampleQueries: _list[GoogleCloudDiscoveryengineV1alphaSampleQuery]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSampleQuerySetsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sampleQuerySets: _list[GoogleCloudDiscoveryengineV1alphaSampleQuerySet]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSchemasResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    schemas: _list[GoogleCloudDiscoveryengineV1alphaSchema]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListServingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudDiscoveryengineV1alphaServingConfig]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessions: _list[GoogleCloudDiscoveryengineV1alphaSession]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaListTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    targetSites: _list[GoogleCloudDiscoveryengineV1alphaTargetSite]
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaMediaInfo(
    typing_extensions.TypedDict, total=False
):
    mediaProgressDuration: str
    mediaProgressPercentage: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPageInfo(
    typing_extensions.TypedDict, total=False
):
    pageCategory: str
    pageviewId: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPanelInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    panelId: str
    panelPosition: int
    totalPanels: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPauseEngineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPrincipal(
    typing_extensions.TypedDict, total=False
):
    groupId: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProcessedDocument(
    typing_extensions.TypedDict, total=False
):
    document: str
    jsonData: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProject(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProjectServiceTerms(
    typing_extensions.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProvisionProjectMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaProvisionProjectRequest(
    typing_extensions.TypedDict, total=False
):
    acceptDataUseTerms: bool
    dataUseTermsVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeSucceeded: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig
    filter: str
    force: bool
    gcsSource: GoogleCloudDiscoveryengineV1alphaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQualityMetrics(
    typing_extensions.TypedDict, total=False
):
    docNdcg: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    docPrecision: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    docRecall: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    pageNdcg: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics
    pageRecall: GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQualityMetricsTopkMetrics(
    typing_extensions.TypedDict, total=False
):
    top1: float
    top10: float
    top3: float
    top5: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaQuery(typing_extensions.TypedDict, total=False):
    queryId: str
    text: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRankRequest(
    typing_extensions.TypedDict, total=False
):
    ignoreRecordDetailsInResponse: bool
    model: str
    query: str
    records: _list[GoogleCloudDiscoveryengineV1alphaRankingRecord]
    topN: int
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRankResponse(
    typing_extensions.TypedDict, total=False
):
    records: _list[GoogleCloudDiscoveryengineV1alphaRankingRecord]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRankingRecord(
    typing_extensions.TypedDict, total=False
):
    content: str
    id: str
    score: float
    title: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    params: dict[str, typing.Any]
    userEvent: GoogleCloudDiscoveryengineV1alphaUserEvent
    userLabels: dict[str, typing.Any]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    missingIds: _list[str]
    results: _list[
        GoogleCloudDiscoveryengineV1alphaRecommendResponseRecommendationResult
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecommendResponseRecommendationResult(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1alphaDocument
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    invalidUris: _list[str]
    pendingCount: int
    quotaExceededCount: int
    successCount: int
    updateTime: str
    validUrisCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisRequest(
    typing_extensions.TypedDict, total=False
):
    uris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponse(
    typing_extensions.TypedDict, total=False
):
    failedUris: _list[str]
    failureSamples: _list[
        GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfo(
    typing_extensions.TypedDict, total=False
):
    failureReasons: _list[
        GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason
    ]
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRecrawlUrisResponseFailureInfoFailureReason(
    typing_extensions.TypedDict, total=False
):
    corpusType: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "DESKTOP", "MOBILE"
    ]
    errorMessage: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReply(typing_extensions.TypedDict, total=False):
    references: _list[GoogleCloudDiscoveryengineV1alphaReplyReference]
    reply: str
    summary: GoogleCloudDiscoveryengineV1alphaSearchResponseSummary

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReplyReference(
    typing_extensions.TypedDict, total=False
):
    anchorText: str
    end: int
    start: int
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaReportConsentChangeRequest(
    typing_extensions.TypedDict, total=False
):
    consentChangeAction: typing_extensions.Literal[
        "CONSENT_CHANGE_ACTION_UNSPECIFIED", "ACCEPT"
    ]
    serviceTermId: str
    serviceTermVersion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirement(
    typing_extensions.TypedDict, total=False
):
    condition: GoogleTypeExpr
    description: str
    displayName: str
    metricBindings: _list[GoogleCloudDiscoveryengineV1alphaRequirementMetricBinding]
    thresholdBindings: _list[
        GoogleCloudDiscoveryengineV1alphaRequirementThresholdBinding
    ]
    type: str
    violationSamplesBindings: _list[
        GoogleCloudDiscoveryengineV1alphaRequirementViolationSamplesBinding
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementMetricBinding(
    typing_extensions.TypedDict, total=False
):
    category: str
    description: str
    metricFilter: str
    resourceType: str
    variableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementThresholdBinding(
    typing_extensions.TypedDict, total=False
):
    blockingThreshold: float
    description: str
    variableId: str
    warningThreshold: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaRequirementViolationSamplesBinding(
    typing_extensions.TypedDict, total=False
):
    description: str
    sampleFilter: str
    variableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaResumeEngineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQuery(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    name: str
    queryEntry: GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntry

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntry(
    typing_extensions.TypedDict, total=False
):
    query: str
    targets: _list[GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntryTarget]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQueryQueryEntryTarget(
    typing_extensions.TypedDict, total=False
):
    pageNumbers: _list[int]
    score: float
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSampleQuerySet(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSchema(typing_extensions.TypedDict, total=False):
    fieldConfigs: _list[GoogleCloudDiscoveryengineV1alphaFieldConfig]
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchInfo(
    typing_extensions.TypedDict, total=False
):
    offset: int
    orderBy: str
    searchQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec]
    embeddingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpec
    facetSpecs: _list[GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1alphaSearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec
    offset: int
    orderBy: str
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestQueryExpansionSpec
    rankingExpression: str
    regionCode: str
    relevanceThreshold: typing_extensions.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "LOWEST", "LOW", "MEDIUM", "HIGH"
    ]
    safeSearch: bool
    searchAsYouTypeSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAsYouTypeSpec
    )
    servingConfig: str
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestSessionSpec
    spellCorrectionSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestSpellCorrectionSpec
    )
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec(
    typing_extensions.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecExtractiveContentSpec
    searchResultMode: typing_extensions.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    snippetSpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSnippetSpec
    )
    summarySpec: (
        GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecChunkSpec(
    typing_extensions.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing_extensions.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSnippetSpec(
    typing_extensions.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpec(
    typing_extensions.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelSpec
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpecSummarySpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestDataStoreSpec(
    typing_extensions.TypedDict, total=False
):
    dataStore: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpec(
    typing_extensions.TypedDict, total=False
):
    embeddingVectors: _list[
        GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpecEmbeddingVector
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestEmbeddingSpecEmbeddingVector(
    typing_extensions.TypedDict, total=False
):
    fieldPath: str
    vector: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudDiscoveryengineV1alphaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    restrictedValues: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestImageQuery(
    typing_extensions.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing_extensions.TypedDict, total=False
):
    filterExtractionCondition: typing_extensions.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSearchAsYouTypeSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSessionSpec(
    typing_extensions.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponse(
    typing_extensions.TypedDict, total=False
):
    appliedControls: _list[str]
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseFacet]
    geoSearchDebugInfo: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseGeoSearchDebugInfo
    ]
    guidedSearchResult: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResult
    )
    naturalLanguageQueryUnderstandingInfo: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfo
    nextPageToken: str
    oneBoxResults: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseOneBoxResult]
    queryExpansionInfo: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseQueryExpansionInfo
    )
    redirectUri: str
    results: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult]
    sessionInfo: GoogleCloudDiscoveryengineV1alphaSearchResponseSessionInfo
    summary: GoogleCloudDiscoveryengineV1alphaSearchResponseSummary
    totalSize: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudDiscoveryengineV1alphaInterval
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseGeoSearchDebugInfo(
    typing_extensions.TypedDict, total=False
):
    errorMessage: str
    originalAddressQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResult(
    typing_extensions.TypedDict, total=False
):
    followUpQuestions: _list[str]
    refinementAttributes: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResultRefinementAttribute
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResultRefinementAttribute(
    typing_extensions.TypedDict, total=False
):
    attributeKey: str
    attributeValue: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfo(
    typing_extensions.TypedDict, total=False
):
    extractedFilters: str
    rewrittenQuery: str
    structuredExtractedFilter: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilter

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilter(
    typing_extensions.TypedDict, total=False
):
    expression: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterAndExpression(
    typing_extensions.TypedDict, total=False
):
    expressions: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression(
    typing_extensions.TypedDict, total=False
):
    andExpr: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterAndExpression
    geolocationConstraint: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterGeolocationConstraint
    numberConstraint: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterNumberConstraint
    orExpr: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterOrExpression
    stringConstraint: GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterStringConstraint

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterGeolocationConstraint(
    typing_extensions.TypedDict, total=False
):
    address: str
    fieldName: str
    latitude: float
    longitude: float
    radiusInMeters: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterNumberConstraint(
    typing_extensions.TypedDict, total=False
):
    comparison: typing_extensions.Literal[
        "COMPARISON_UNSPECIFIED",
        "EQUALS",
        "LESS_THAN_EQUALS",
        "LESS_THAN",
        "GREATER_THAN_EQUALS",
        "GREATER_THAN",
    ]
    fieldName: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterOrExpression(
    typing_extensions.TypedDict, total=False
):
    expressions: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterExpression
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseNaturalLanguageQueryUnderstandingInfoStructuredExtractedFilterStringConstraint(
    typing_extensions.TypedDict, total=False
):
    fieldName: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseOneBoxResult(
    typing_extensions.TypedDict, total=False
):
    oneBoxType: typing_extensions.Literal[
        "ONE_BOX_TYPE_UNSPECIFIED", "PEOPLE", "ORGANIZATION", "SLACK"
    ]
    searchResults: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult(
    typing_extensions.TypedDict, total=False
):
    chunk: GoogleCloudDiscoveryengineV1alphaChunk
    document: GoogleCloudDiscoveryengineV1alphaDocument
    id: str
    modelScores: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSessionInfo(
    typing_extensions.TypedDict, total=False
):
    name: str
    queryId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummary(
    typing_extensions.TypedDict, total=False
):
    safetyAttributes: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySafetyAttributes
    )
    summarySkippedReasons: _list[
        typing_extensions.Literal[
            "SUMMARY_SKIPPED_REASON_UNSPECIFIED",
            "ADVERSARIAL_QUERY_IGNORED",
            "NON_SUMMARY_SEEKING_QUERY_IGNORED",
            "OUT_OF_DOMAIN_QUERY_IGNORED",
            "POTENTIAL_POLICY_VIOLATION",
            "LLM_ADDON_NOT_ENABLED",
            "NO_RELEVANT_CONTENT",
            "JAIL_BREAKING_QUERY_IGNORED",
        ]
    ]
    summaryText: str
    summaryWithMetadata: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummaryWithMetadata
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitation(
    typing_extensions.TypedDict, total=False
):
    endIndex: str
    sources: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationSource]
    startIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationMetadata(
    typing_extensions.TypedDict, total=False
):
    citations: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitation]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationSource(
    typing_extensions.TypedDict, total=False
):
    referenceIndex: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReference(
    typing_extensions.TypedDict, total=False
):
    chunkContents: _list[
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReferenceChunkContent
    ]
    document: str
    title: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReferenceChunkContent(
    typing_extensions.TypedDict, total=False
):
    content: str
    pageIdentifier: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySafetyAttributes(
    typing_extensions.TypedDict, total=False
):
    categories: _list[str]
    scores: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSearchResponseSummarySummaryWithMetadata(
    typing_extensions.TypedDict, total=False
):
    citationMetadata: (
        GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryCitationMetadata
    )
    references: _list[GoogleCloudDiscoveryengineV1alphaSearchResponseSummaryReference]
    summary: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaServingConfig(
    typing_extensions.TypedDict, total=False
):
    boostControlIds: _list[str]
    createTime: str
    customFineTuningSpec: GoogleCloudDiscoveryengineV1alphaCustomFineTuningSpec
    displayName: str
    dissociateControlIds: _list[str]
    diversityLevel: str
    embeddingConfig: GoogleCloudDiscoveryengineV1alphaEmbeddingConfig
    filterControlIds: _list[str]
    genericConfig: GoogleCloudDiscoveryengineV1alphaServingConfigGenericConfig
    guidedSearchSpec: GoogleCloudDiscoveryengineV1alphaGuidedSearchSpec
    ignoreControlIds: _list[str]
    mediaConfig: GoogleCloudDiscoveryengineV1alphaServingConfigMediaConfig
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    rankingExpression: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsControlIds: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaServingConfigGenericConfig(
    typing_extensions.TypedDict, total=False
):
    contentSearchSpec: GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaServingConfigMediaConfig(
    typing_extensions.TypedDict, total=False
):
    contentFreshnessCutoffDays: int
    contentWatchedPercentageThreshold: float
    contentWatchedSecondsThreshold: float
    demotionEventType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSession(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    name: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "IN_PROGRESS"]
    turns: _list[GoogleCloudDiscoveryengineV1alphaSessionTurn]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSessionTurn(
    typing_extensions.TypedDict, total=False
):
    answer: str
    query: GoogleCloudDiscoveryengineV1alphaQuery

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataRequest(
    typing_extensions.TypedDict, total=False
):
    documentDataMap: dict[str, typing.Any]
    emptyDocumentDataMap: bool
    schema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSetUriPatternDocumentDataResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteSearchEngine(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSpannerSource(
    typing_extensions.TypedDict, total=False
):
    databaseId: str
    enableDataBoost: bool
    instanceId: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaSuggestionDenyListEntry(
    typing_extensions.TypedDict, total=False
):
    blockPhrase: str
    matchOperator: typing_extensions.Literal[
        "MATCH_OPERATOR_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSite(
    typing_extensions.TypedDict, total=False
):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing_extensions.Literal[
        "INDEXING_STATUS_UNSPECIFIED", "PENDING", "FAILED", "SUCCEEDED", "DELETING"
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1alphaSiteVerificationInfo
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReason(
    typing_extensions.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTargetSiteFailureReasonQuotaFailure(
    typing_extensions.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTextInput(
    typing_extensions.TypedDict, total=False
):
    context: GoogleCloudDiscoveryengineV1alphaConversationContext
    input: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequest(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    gcsTrainingInput: (
        GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequestGcsTrainingInput
    )
    modelId: str
    modelType: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelRequestGcsTrainingInput(
    typing_extensions.TypedDict, total=False
):
    corpusDataPath: str
    queryDataPath: str
    testDataPath: str
    trainDataPath: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTrainCustomModelResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTransactionInfo(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currency: str
    discountValue: float
    tax: float
    transactionId: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaTuneEngineResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserEvent(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    attributionToken: str
    completionInfo: GoogleCloudDiscoveryengineV1alphaCompletionInfo
    dataStore: str
    directUserRequest: bool
    documents: _list[GoogleCloudDiscoveryengineV1alphaDocumentInfo]
    engine: str
    eventTime: str
    eventType: str
    filter: str
    mediaInfo: GoogleCloudDiscoveryengineV1alphaMediaInfo
    pageInfo: GoogleCloudDiscoveryengineV1alphaPageInfo
    panel: GoogleCloudDiscoveryengineV1alphaPanelInfo
    promotionIds: _list[str]
    searchInfo: GoogleCloudDiscoveryengineV1alphaSearchInfo
    sessionId: str
    tagIds: _list[str]
    transactionInfo: GoogleCloudDiscoveryengineV1alphaTransactionInfo
    userInfo: GoogleCloudDiscoveryengineV1alphaUserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaUserInfo(
    typing_extensions.TypedDict, total=False
):
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBatchCreateTargetSitesResponse(
    typing_extensions.TypedDict, total=False
):
    targetSites: _list[GoogleCloudDiscoveryengineV1betaTargetSite]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCondition(
    typing_extensions.TypedDict, total=False
):
    activeTimeRange: _list[GoogleCloudDiscoveryengineV1betaConditionTimeRange]
    queryTerms: _list[GoogleCloudDiscoveryengineV1betaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControl(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    boostAction: GoogleCloudDiscoveryengineV1betaControlBoostAction
    conditions: _list[GoogleCloudDiscoveryengineV1betaCondition]
    displayName: str
    filterAction: GoogleCloudDiscoveryengineV1betaControlFilterAction
    name: str
    redirectAction: GoogleCloudDiscoveryengineV1betaControlRedirectAction
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    synonymsAction: GoogleCloudDiscoveryengineV1betaControlSynonymsAction
    useCases: _list[
        typing_extensions.Literal[
            "SEARCH_USE_CASE_UNSPECIFIED",
            "SEARCH_USE_CASE_SEARCH",
            "SEARCH_USE_CASE_BROWSE",
        ]
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlBoostAction(
    typing_extensions.TypedDict, total=False
):
    boost: float
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlFilterAction(
    typing_extensions.TypedDict, total=False
):
    dataStore: str
    filter: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaControlSynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateEvaluationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCreateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCustomTuningModel(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    metrics: dict[str, typing.Any]
    modelState: typing_extensions.Literal[
        "MODEL_STATE_UNSPECIFIED",
        "TRAINING_PAUSED",
        "TRAINING",
        "TRAINING_COMPLETE",
        "READY_FOR_SERVING",
        "TRAINING_FAILED",
        "NO_IMPROVEMENT",
    ]
    modelVersion: str
    name: str
    trainingStartTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDataStore(
    typing_extensions.TypedDict, total=False
):
    contentConfig: typing_extensions.Literal[
        "CONTENT_CONFIG_UNSPECIFIED", "NO_CONTENT", "CONTENT_REQUIRED", "PUBLIC_WEBSITE"
    ]
    createTime: str
    defaultSchemaId: str
    displayName: str
    documentProcessingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    languageInfo: GoogleCloudDiscoveryengineV1betaLanguageInfo
    name: str
    solutionTypes: _list[
        typing_extensions.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
            "SOLUTION_TYPE_CHAT",
            "SOLUTION_TYPE_GENERATIVE_CHAT",
        ]
    ]
    startingSchema: GoogleCloudDiscoveryengineV1betaSchema

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteDataStoreMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDeleteTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDisableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkingConfig: (
        GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfig
    )
    defaultParsingConfig: (
        GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig
    )
    name: str
    parsingConfigOverrides: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    layoutBasedChunkingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(
    typing_extensions.TypedDict, total=False
):
    chunkSize: int
    includeAncestorHeadings: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfig(
    typing_extensions.TypedDict, total=False
):
    digitalParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigDigitalParsingConfig
    layoutParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigLayoutParsingConfig
    ocrParsingConfig: GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigOcrParsingConfig

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigDigitalParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigLayoutParsingConfig(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentProcessingConfigParsingConfigOcrParsingConfig(
    typing_extensions.TypedDict, total=False
):
    enhancedDocumentElements: _list[str]
    useNativeText: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEnableAdvancedSiteSearchResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngine(typing_extensions.TypedDict, total=False):
    chatEngineConfig: GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig
    chatEngineMetadata: GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata
    commonConfig: GoogleCloudDiscoveryengineV1betaEngineCommonConfig
    createTime: str
    dataStoreIds: _list[str]
    displayName: str
    industryVertical: typing_extensions.Literal[
        "INDUSTRY_VERTICAL_UNSPECIFIED", "GENERIC", "MEDIA", "HEALTHCARE_FHIR"
    ]
    name: str
    searchEngineConfig: GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig
    solutionType: typing_extensions.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
        "SOLUTION_TYPE_CHAT",
        "SOLUTION_TYPE_GENERATIVE_CHAT",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineConfig(
    typing_extensions.TypedDict, total=False
):
    agentCreationConfig: (
        GoogleCloudDiscoveryengineV1betaEngineChatEngineConfigAgentCreationConfig
    )
    dialogflowAgentToLink: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineConfigAgentCreationConfig(
    typing_extensions.TypedDict, total=False
):
    business: str
    defaultLanguageCode: str
    location: str
    timeZone: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineChatEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    dialogflowAgent: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineCommonConfig(
    typing_extensions.TypedDict, total=False
):
    companyName: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEngineSearchEngineConfig(
    typing_extensions.TypedDict, total=False
):
    searchAddOns: _list[
        typing_extensions.Literal["SEARCH_ADD_ON_UNSPECIFIED", "SEARCH_ADD_ON_LLM"]
    ]
    searchTier: typing_extensions.Literal[
        "SEARCH_TIER_UNSPECIFIED", "SEARCH_TIER_STANDARD", "SEARCH_TIER_ENTERPRISE"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluation(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    error: GoogleRpcStatus
    errorSamples: _list[GoogleRpcStatus]
    evaluationSpec: GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpec
    name: str
    qualityMetrics: GoogleCloudDiscoveryengineV1betaQualityMetrics
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpec(
    typing_extensions.TypedDict, total=False
):
    querySetSpec: GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpecQuerySetSpec
    searchRequest: GoogleCloudDiscoveryengineV1betaSearchRequest

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaEvaluationEvaluationSpecQuerySetSpec(
    typing_extensions.TypedDict, total=False
):
    sampleQuerySet: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportCompletionSuggestionsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportCompletionSuggestionsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSampleQueriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    totalCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSampleQueriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    failedEntriesCount: str
    importedEntriesCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaInterval(
    typing_extensions.TypedDict, total=False
):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaLanguageInfo(
    typing_extensions.TypedDict, total=False
):
    language: str
    languageCode: str
    normalizedLanguageCode: str
    region: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListCustomModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudDiscoveryengineV1betaCustomTuningModel]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProject(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    provisionCompletionTime: str
    serviceTermsMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProjectServiceTerms(
    typing_extensions.TypedDict, total=False
):
    acceptTime: str
    declineTime: str
    id: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "TERMS_ACCEPTED", "TERMS_PENDING", "TERMS_DECLINED"
    ]
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaProvisionProjectMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    ignoredCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPurgeSuggestionDenyListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    purgeCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaQualityMetrics(
    typing_extensions.TypedDict, total=False
):
    docNdcg: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    docPrecision: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    docRecall: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    pageNdcg: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics
    pageRecall: GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaQualityMetricsTopkMetrics(
    typing_extensions.TypedDict, total=False
):
    top1: float
    top10: float
    top3: float
    top5: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSchema(typing_extensions.TypedDict, total=False):
    jsonSchema: str
    name: str
    structSchema: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequest(
    typing_extensions.TypedDict, total=False
):
    boostSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    contentSearchSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec
    dataStoreSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestDataStoreSpec]
    embeddingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec
    facetSpecs: _list[GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec]
    filter: str
    imageQuery: GoogleCloudDiscoveryengineV1betaSearchRequestImageQuery
    languageCode: str
    naturalLanguageQueryUnderstandingSpec: GoogleCloudDiscoveryengineV1betaSearchRequestNaturalLanguageQueryUnderstandingSpec
    offset: int
    orderBy: str
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    query: str
    queryExpansionSpec: GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec
    rankingExpression: str
    regionCode: str
    safeSearch: bool
    searchAsYouTypeSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestSearchAsYouTypeSpec
    )
    servingConfig: str
    session: str
    sessionSpec: GoogleCloudDiscoveryengineV1betaSearchRequestSessionSpec
    spellCorrectionSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestSpellCorrectionSpec
    )
    userInfo: GoogleCloudDiscoveryengineV1betaUserInfo
    userLabels: dict[str, typing.Any]
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpec
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    boostControlSpec: GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec
    condition: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpec(
    typing_extensions.TypedDict, total=False
):
    attributeType: typing_extensions.Literal[
        "ATTRIBUTE_TYPE_UNSPECIFIED", "NUMERICAL", "FRESHNESS"
    ]
    controlPoints: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint
    ]
    fieldName: str
    interpolationType: typing_extensions.Literal[
        "INTERPOLATION_TYPE_UNSPECIFIED", "LINEAR"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestBoostSpecConditionBoostSpecBoostControlSpecControlPoint(
    typing_extensions.TypedDict, total=False
):
    attributeValue: str
    boostAmount: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpec(
    typing_extensions.TypedDict, total=False
):
    chunkSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecChunkSpec
    extractiveContentSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec
    searchResultMode: typing_extensions.Literal[
        "SEARCH_RESULT_MODE_UNSPECIFIED", "DOCUMENTS", "CHUNKS"
    ]
    snippetSpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec
    )
    summarySpec: (
        GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec
    )

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecChunkSpec(
    typing_extensions.TypedDict, total=False
):
    numNextChunks: int
    numPreviousChunks: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecExtractiveContentSpec(
    typing_extensions.TypedDict, total=False
):
    maxExtractiveAnswerCount: int
    maxExtractiveSegmentCount: int
    numNextSegments: int
    numPreviousSegments: int
    returnExtractiveSegmentScore: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec(
    typing_extensions.TypedDict, total=False
):
    maxSnippetCount: int
    referenceOnly: bool
    returnSnippet: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpec(
    typing_extensions.TypedDict, total=False
):
    ignoreAdversarialQuery: bool
    ignoreLowRelevantContent: bool
    ignoreNonSummarySeekingQuery: bool
    includeCitations: bool
    languageCode: str
    modelPromptSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec
    modelSpec: GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec
    summaryResultCount: int
    useSemanticChunks: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelPromptSpec(
    typing_extensions.TypedDict, total=False
):
    preamble: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSummarySpecModelSpec(
    typing_extensions.TypedDict, total=False
):
    version: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestDataStoreSpec(
    typing_extensions.TypedDict, total=False
):
    dataStore: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpec(
    typing_extensions.TypedDict, total=False
):
    embeddingVectors: _list[
        GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpecEmbeddingVector
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestEmbeddingSpecEmbeddingVector(
    typing_extensions.TypedDict, total=False
):
    fieldPath: str
    vector: _list[float]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudDiscoveryengineV1betaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    restrictedValues: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestImageQuery(
    typing_extensions.TypedDict, total=False
):
    imageBytes: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestNaturalLanguageQueryUnderstandingSpec(
    typing_extensions.TypedDict, total=False
):
    filterExtractionCondition: typing_extensions.Literal[
        "CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    geoSearchQueryDetectionFieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSearchAsYouTypeSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSessionSpec(
    typing_extensions.TypedDict, total=False
):
    queryId: str
    searchResultPersistenceCount: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSiteVerificationInfo(
    typing_extensions.TypedDict, total=False
):
    siteVerificationState: typing_extensions.Literal[
        "SITE_VERIFICATION_STATE_UNSPECIFIED", "VERIFIED", "UNVERIFIED", "EXEMPTED"
    ]
    verifyTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSite(
    typing_extensions.TypedDict, total=False
):
    exactMatch: bool
    failureReason: GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason
    generatedUriPattern: str
    indexingStatus: typing_extensions.Literal[
        "INDEXING_STATUS_UNSPECIFIED", "PENDING", "FAILED", "SUCCEEDED", "DELETING"
    ]
    name: str
    providedUriPattern: str
    rootDomainUri: str
    siteVerificationInfo: GoogleCloudDiscoveryengineV1betaSiteVerificationInfo
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason(
    typing_extensions.TypedDict, total=False
):
    quotaFailure: GoogleCloudDiscoveryengineV1betaTargetSiteFailureReasonQuotaFailure

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTargetSiteFailureReasonQuotaFailure(
    typing_extensions.TypedDict, total=False
):
    totalRequiredQuota: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTrainCustomModelMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTrainCustomModelResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    metrics: dict[str, typing.Any]
    modelName: str
    modelStatus: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTuneEngineMetadata(
    typing_extensions.TypedDict, total=False
):
    engine: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTuneEngineResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUpdateSchemaMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUpdateTargetSiteMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserInfo(
    typing_extensions.TypedDict, total=False
):
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleMonitoringV3TypedValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    distributionValue: GoogleApiDistribution
    doubleValue: float
    int64Value: str
    stringValue: str

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
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
