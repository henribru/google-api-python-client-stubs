import typing

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudRetailLoggingErrorContext(typing.TypedDict, total=False):
    httpRequest: GoogleCloudRetailLoggingHttpRequestContext
    reportLocation: GoogleCloudRetailLoggingSourceLocation

@typing.type_check_only
class GoogleCloudRetailLoggingErrorLog(typing.TypedDict, total=False):
    context: GoogleCloudRetailLoggingErrorContext
    importPayload: GoogleCloudRetailLoggingImportErrorContext
    message: str
    requestPayload: dict[str, typing.Any]
    responsePayload: dict[str, typing.Any]
    serviceContext: GoogleCloudRetailLoggingServiceContext
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudRetailLoggingHttpRequestContext(typing.TypedDict, total=False):
    responseStatusCode: int

@typing.type_check_only
class GoogleCloudRetailLoggingImportErrorContext(typing.TypedDict, total=False):
    catalogItem: str
    gcsPath: str
    lineNumber: str
    operationName: str
    product: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailLoggingServiceContext(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudRetailLoggingSourceLocation(typing.TypedDict, total=False):
    functionName: str

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2BigQueryOutputResult(typing.TypedDict, total=False):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2CreateModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2ExportAnalyticsMetricsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ExportErrorsConfig
    outputResult: GoogleCloudRetailV2OutputResult

@typing.type_check_only
class GoogleCloudRetailV2ExportErrorsConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2ExportMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2GcsOutputResult(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2ImportCompletionDataResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2ImportErrorsConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2ImportMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2ImportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2ImportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig
    importSummary: GoogleCloudRetailV2UserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2Model(typing.TypedDict, total=False):
    createTime: str
    dataState: typing.Literal["DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"]
    displayName: str
    filteringOption: typing.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    modelFeaturesConfig: GoogleCloudRetailV2ModelModelFeaturesConfig
    name: str
    optimizationObjective: str
    periodicTuningState: typing.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2ModelServingConfigList]
    servingState: typing.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing.Literal["TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfig(
    typing.TypedDict, total=False
):
    contextProductsType: typing.Literal[
        "CONTEXT_PRODUCTS_TYPE_UNSPECIFIED",
        "SINGLE_CONTEXT_PRODUCT",
        "MULTIPLE_CONTEXT_PRODUCTS",
    ]

@typing.type_check_only
class GoogleCloudRetailV2ModelModelFeaturesConfig(typing.TypedDict, total=False):
    frequentlyBoughtTogetherConfig: (
        GoogleCloudRetailV2ModelFrequentlyBoughtTogetherFeaturesConfig
    )

@typing.type_check_only
class GoogleCloudRetailV2ModelServingConfigList(typing.TypedDict, total=False):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2OutputResult(typing.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2BigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2GcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2PurgeMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2PurgeUserEventsResponse(typing.TypedDict, total=False):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsResponse(typing.TypedDict, total=False):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2TuneModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2TuneModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2UserEventImportSummary(typing.TypedDict, total=False):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAcceptTermsRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddCatalogAttributeRequest(typing.TypedDict, total=False):
    catalogAttribute: GoogleCloudRetailV2alphaCatalogAttribute

@typing.type_check_only
class GoogleCloudRetailV2alphaAddControlRequest(typing.TypedDict, total=False):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesRequest(
    typing.TypedDict, total=False
):
    addTime: str
    allowMissing: bool
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesRequest(typing.TypedDict, total=False):
    addMask: str
    addTime: str
    allowMissing: bool
    localInventories: _list[GoogleCloudRetailV2alphaLocalInventory]

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAlertConfig(typing.TypedDict, total=False):
    alertPolicies: _list[GoogleCloudRetailV2alphaAlertConfigAlertPolicy]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAlertConfigAlertPolicy(typing.TypedDict, total=False):
    alertGroup: str
    enrollStatus: typing.Literal["ENROLL_STATUS_UNSPECIFIED", "ENROLLED", "DECLINED"]
    recipients: _list[GoogleCloudRetailV2alphaAlertConfigAlertPolicyRecipient]

@typing.type_check_only
class GoogleCloudRetailV2alphaAlertConfigAlertPolicyRecipient(
    typing.TypedDict, total=False
):
    emailAddress: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAttributesConfig(typing.TypedDict, total=False):
    attributeConfigLevel: typing.Literal[
        "ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED",
        "PRODUCT_LEVEL_ATTRIBUTE_CONFIG",
        "CATALOG_LEVEL_ATTRIBUTE_CONFIG",
    ]
    catalogAttributes: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAudience(typing.TypedDict, total=False):
    ageGroups: _list[str]
    genders: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesRequest(
    typing.TypedDict, total=False
):
    attributeKeys: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesResponse(
    typing.TypedDict, total=False
):
    deletedCatalogAttributes: _list[str]
    resetCatalogAttributes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchUpdateGenerativeQuestionConfigsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudRetailV2alphaUpdateGenerativeQuestionConfigRequest]

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchUpdateGenerativeQuestionConfigsResponse(
    typing.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2alphaGenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQueryOutputResult(typing.TypedDict, total=False):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQuerySource(typing.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaBranch(typing.TypedDict, total=False):
    displayName: str
    isDefault: bool
    lastProductImportTime: str
    name: str
    productCountStats: _list[GoogleCloudRetailV2alphaBranchProductCountStatistic]
    qualityMetrics: _list[GoogleCloudRetailV2alphaBranchQualityMetric]

@typing.type_check_only
class GoogleCloudRetailV2alphaBranchProductCountStatistic(
    typing.TypedDict, total=False
):
    counts: dict[str, typing.Any]
    scope: typing.Literal[
        "PRODUCT_COUNT_SCOPE_UNSPECIFIED", "ALL_PRODUCTS", "LAST_24_HOUR_UPDATE"
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaBranchQualityMetric(typing.TypedDict, total=False):
    qualifiedProductCount: int
    requirementKey: str
    suggestedQualityPercentThreshold: float
    unqualifiedProductCount: int
    unqualifiedSampleProducts: _list[GoogleCloudRetailV2alphaProduct]

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalog(typing.TypedDict, total=False):
    displayName: str
    merchantCenterLinkingConfig: GoogleCloudRetailV2alphaMerchantCenterLinkingConfig
    name: str
    productLevelConfig: GoogleCloudRetailV2alphaProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttribute(typing.TypedDict, total=False):
    dynamicFacetableOption: typing.Literal[
        "DYNAMIC_FACETABLE_OPTION_UNSPECIFIED",
        "DYNAMIC_FACETABLE_ENABLED",
        "DYNAMIC_FACETABLE_DISABLED",
    ]
    exactSearchableOption: typing.Literal[
        "EXACT_SEARCHABLE_OPTION_UNSPECIFIED",
        "EXACT_SEARCHABLE_ENABLED",
        "EXACT_SEARCHABLE_DISABLED",
    ]
    facetConfig: GoogleCloudRetailV2alphaCatalogAttributeFacetConfig
    inUse: bool
    indexableOption: typing.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    key: str
    recommendationsFilteringOption: typing.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    retrievableOption: typing.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    searchableOption: typing.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]
    type: typing.Literal["UNKNOWN", "TEXTUAL", "NUMERICAL"]

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttributeFacetConfig(
    typing.TypedDict, total=False
):
    facetIntervals: _list[GoogleCloudRetailV2alphaInterval]
    ignoredFacetValues: _list[
        GoogleCloudRetailV2alphaCatalogAttributeFacetConfigIgnoredFacetValues
    ]
    mergedFacet: GoogleCloudRetailV2alphaCatalogAttributeFacetConfigMergedFacet
    mergedFacetValues: _list[
        GoogleCloudRetailV2alphaCatalogAttributeFacetConfigMergedFacetValue
    ]
    rerankConfig: GoogleCloudRetailV2alphaCatalogAttributeFacetConfigRerankConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttributeFacetConfigIgnoredFacetValues(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttributeFacetConfigMergedFacet(
    typing.TypedDict, total=False
):
    mergedFacetKey: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttributeFacetConfigMergedFacetValue(
    typing.TypedDict, total=False
):
    mergedValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttributeFacetConfigRerankConfig(
    typing.TypedDict, total=False
):
    facetValues: _list[str]
    rerankFacet: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaCollectUserEventRequest(typing.TypedDict, total=False):
    ets: str
    prebuiltRule: str
    rawJson: str
    uri: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailV2alphaColorInfo(typing.TypedDict, total=False):
    colorFamilies: _list[str]
    colors: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponse(typing.TypedDict, total=False):
    attributeResults: dict[str, typing.Any]
    attributionToken: str
    completionResults: _list[
        GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult
    ]
    recentSearchResults: _list[
        GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseAttributeResult(
    typing.TypedDict, total=False
):
    suggestions: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult(
    typing.TypedDict, total=False
):
    agentPrompts: _list[
        GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResultAgentPrompt
    ]
    attributes: dict[str, typing.Any]
    facets: _list[GoogleCloudRetailV2alphaSearchResponseFacet]
    suggestion: str
    totalProductCount: int

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResultAgentPrompt(
    typing.TypedDict, total=False
):
    prompt: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult(
    typing.TypedDict, total=False
):
    recentSearch: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCompletionConfig(typing.TypedDict, total=False):
    allowlistInputConfig: GoogleCloudRetailV2alphaCompletionDataInputConfig
    autoLearning: bool
    denylistInputConfig: GoogleCloudRetailV2alphaCompletionDataInputConfig
    lastAllowlistImportOperation: str
    lastDenylistImportOperation: str
    lastSuggestionsImportOperation: str
    matchingOrder: str
    maxSuggestions: int
    minPrefixLength: int
    name: str
    suggestionsInputConfig: GoogleCloudRetailV2alphaCompletionDataInputConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaCompletionDataInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2alphaBigQuerySource

@typing.type_check_only
class GoogleCloudRetailV2alphaCompletionDetail(typing.TypedDict, total=False):
    completionAttributionToken: str
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCondition(typing.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudRetailV2alphaConditionTimeRange]
    pageCategories: _list[str]
    queryTerms: _list[GoogleCloudRetailV2alphaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudRetailV2alphaConditionQueryTerm(typing.TypedDict, total=False):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudRetailV2alphaConditionTimeRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaControl(typing.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    displayName: str
    name: str
    rule: GoogleCloudRetailV2alphaRule
    searchSolutionUseCase: _list[
        typing.Literal[
            "SEARCH_SOLUTION_USE_CASE_UNSPECIFIED",
            "SEARCH_SOLUTION_USE_CASE_SEARCH",
            "SEARCH_SOLUTION_USE_CASE_BROWSE",
        ]
    ]
    solutionTypes: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
        ]
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchCustomizationConfig(
    typing.TypedDict, total=False
):
    catalog: str
    intentClassificationConfig: GoogleCloudRetailV2alphaIntentClassificationConfig
    retailerDisplayName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchRequest(
    typing.TypedDict, total=False
):
    branch: str
    conversationId: str
    conversationalFilteringSpec: (
        GoogleCloudRetailV2alphaConversationalSearchRequestConversationalFilteringSpec
    )
    pageCategories: _list[str]
    query: str
    safetySettings: _list[GoogleCloudRetailV2alphaSafetySetting]
    searchParams: GoogleCloudRetailV2alphaConversationalSearchRequestSearchParams
    userInfo: GoogleCloudRetailV2alphaUserInfo
    userLabels: dict[str, typing.Any]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchRequestConversationalFilteringSpec(
    typing.TypedDict, total=False
):
    conversationalFilteringMode: typing.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "ENABLED", "CONVERSATIONAL_FILTER_ONLY"
    ]
    enableConversationalFiltering: bool
    userAnswer: GoogleCloudRetailV2alphaConversationalSearchRequestUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchRequestSearchParams(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudRetailV2alphaSearchRequestBoostSpec
    canonicalFilter: str
    filter: str
    sortBy: str

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchRequestUserAnswer(
    typing.TypedDict, total=False
):
    selectedAnswer: (
        GoogleCloudRetailV2alphaConversationalSearchRequestUserAnswerSelectedAnswer
    )
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchRequestUserAnswerSelectedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchResponse(
    typing.TypedDict, total=False
):
    conversationId: str
    conversationalFilteringResult: GoogleCloudRetailV2alphaConversationalSearchResponseConversationalFilteringResult
    conversationalTextResponse: str
    followupQuestion: (
        GoogleCloudRetailV2alphaConversationalSearchResponseFollowupQuestion
    )
    refinedSearch: _list[
        GoogleCloudRetailV2alphaConversationalSearchResponseRefinedSearch
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "STREAMING", "SUCCEEDED"]
    userQueryTypes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchResponseConversationalFilteringResult(
    typing.TypedDict, total=False
):
    additionalFilter: GoogleCloudRetailV2alphaConversationalSearchResponseConversationalFilteringResultAdditionalFilter
    followupQuestion: (
        GoogleCloudRetailV2alphaConversationalSearchResponseFollowupQuestion
    )

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchResponseConversationalFilteringResultAdditionalFilter(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchResponseFollowupQuestion(
    typing.TypedDict, total=False
):
    followupQuestion: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2alphaConversationalSearchResponseFollowupQuestionSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchResponseFollowupQuestionSuggestedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2alphaConversationalSearchResponseRefinedSearch(
    typing.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCreateMerchantCenterAccountLinkMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCreateModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCustomAttribute(typing.TypedDict, total=False):
    indexable: bool
    numbers: _list[float]
    searchable: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaDoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionRequest(typing.TypedDict, total=False):
    solution: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionResponse(typing.TypedDict, total=False):
    enrolledSolution: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaExperimentInfo(typing.TypedDict, total=False):
    experiment: str
    servingConfigExperiment: (
        GoogleCloudRetailV2alphaExperimentInfoServingConfigExperiment
    )

@typing.type_check_only
class GoogleCloudRetailV2alphaExperimentInfoServingConfigExperiment(
    typing.TypedDict, total=False
):
    experimentServingConfig: str
    originalServingConfig: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportAnalyticsMetricsRequest(
    typing.TypedDict, total=False
):
    filter: str
    outputConfig: GoogleCloudRetailV2alphaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaExportAnalyticsMetricsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaExportErrorsConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportProductsRequest(typing.TypedDict, total=False):
    filter: str
    outputConfig: GoogleCloudRetailV2alphaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaExportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaExportUserEventsRequest(typing.TypedDict, total=False):
    filter: str
    outputConfig: GoogleCloudRetailV2alphaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaExportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaFulfillmentInfo(typing.TypedDict, total=False):
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaGcsOutputResult(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2alphaGcsSource(typing.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaGenerativeQuestionConfig(typing.TypedDict, total=False):
    allowedInConversation: bool
    catalog: str
    exampleValues: _list[str]
    facet: str
    finalQuestion: str
    frequency: float
    generatedQuestion: str

@typing.type_check_only
class GoogleCloudRetailV2alphaGenerativeQuestionsFeatureConfig(
    typing.TypedDict, total=False
):
    catalog: str
    featureEnabled: bool
    minimumProducts: int

@typing.type_check_only
class GoogleCloudRetailV2alphaGetDefaultBranchResponse(typing.TypedDict, total=False):
    branch: str
    note: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImage(typing.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2alphaImportCompletionDataRequest(
    typing.TypedDict, total=False
):
    inputConfig: GoogleCloudRetailV2alphaCompletionDataInputConfig
    notificationPubsubTopic: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportCompletionDataResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2alphaImportErrorsConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    transformedUserEventsMetadata: GoogleCloudRetailV2alphaTransformedUserEventsMetadata
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsRequest(typing.TypedDict, total=False):
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2alphaProductInputConfig
    notificationPubsubTopic: str
    reconciliationMode: typing.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    requestId: str
    skipDefaultBranchProtection: bool
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsRequest(typing.TypedDict, total=False):
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2alphaUserEventInputConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    importSummary: GoogleCloudRetailV2alphaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2alphaIntentClassificationConfig(typing.TypedDict, total=False):
    blocklistKeywords: _list[str]
    disabledIntentTypes: _list[str]
    example: _list[GoogleCloudRetailV2alphaIntentClassificationConfigExample]
    inlineSource: GoogleCloudRetailV2alphaIntentClassificationConfigInlineSource
    modelPreamble: str

@typing.type_check_only
class GoogleCloudRetailV2alphaIntentClassificationConfigExample(
    typing.TypedDict, total=False
):
    classifiedPositive: bool
    intentType: str
    query: str
    reason: str

@typing.type_check_only
class GoogleCloudRetailV2alphaIntentClassificationConfigInlineForceIntent(
    typing.TypedDict, total=False
):
    intentType: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"]
    query: str

@typing.type_check_only
class GoogleCloudRetailV2alphaIntentClassificationConfigInlineSource(
    typing.TypedDict, total=False
):
    inlineForceIntents: _list[
        GoogleCloudRetailV2alphaIntentClassificationConfigInlineForceIntent
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaInterval(typing.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudRetailV2alphaListBranchesResponse(typing.TypedDict, total=False):
    branches: _list[GoogleCloudRetailV2alphaBranch]

@typing.type_check_only
class GoogleCloudRetailV2alphaListCatalogsResponse(typing.TypedDict, total=False):
    catalogs: _list[GoogleCloudRetailV2alphaCatalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListControlsResponse(typing.TypedDict, total=False):
    controls: _list[GoogleCloudRetailV2alphaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListEnrolledSolutionsResponse(
    typing.TypedDict, total=False
):
    enrolledSolutions: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
        ]
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaListGenerativeQuestionConfigsResponse(
    typing.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2alphaGenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2alphaListMerchantCenterAccountLinksResponse(
    typing.TypedDict, total=False
):
    merchantCenterAccountLinks: _list[GoogleCloudRetailV2alphaMerchantCenterAccountLink]

@typing.type_check_only
class GoogleCloudRetailV2alphaListModelsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudRetailV2alphaModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListProductsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    products: _list[GoogleCloudRetailV2alphaProduct]
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2alphaListServingConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudRetailV2alphaServingConfig]

@typing.type_check_only
class GoogleCloudRetailV2alphaLocalInventory(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    fulfillmentTypes: _list[str]
    placeId: str
    priceInfo: GoogleCloudRetailV2alphaPriceInfo

@typing.type_check_only
class GoogleCloudRetailV2alphaLoggingConfig(typing.TypedDict, total=False):
    defaultLogGenerationRule: GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule
    name: str
    serviceLogGenerationRules: _list[
        GoogleCloudRetailV2alphaLoggingConfigServiceLogGenerationRule
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule(
    typing.TypedDict, total=False
):
    infoLogSampleRate: float
    loggingLevel: typing.Literal[
        "LOGGING_LEVEL_UNSPECIFIED",
        "LOGGING_DISABLED",
        "LOG_ERRORS_AND_ABOVE",
        "LOG_WARNINGS_AND_ABOVE",
        "LOG_ALL",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaLoggingConfigServiceLogGenerationRule(
    typing.TypedDict, total=False
):
    logGenerationRule: GoogleCloudRetailV2alphaLoggingConfigLogGenerationRule
    serviceName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterAccountLink(typing.TypedDict, total=False):
    branchId: str
    feedFilters: _list[
        GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilter
    ]
    feedLabel: str
    id: str
    languageCode: str
    merchantCenterAccountId: str
    name: str
    projectId: str
    source: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterAccountLinkMerchantCenterFeedFilter(
    typing.TypedDict, total=False
):
    dataSourceId: str
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterFeedFilter(typing.TypedDict, total=False):
    dataSourceId: str
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterLink(typing.TypedDict, total=False):
    branchId: str
    destinations: _list[str]
    feeds: _list[GoogleCloudRetailV2alphaMerchantCenterFeedFilter]
    languageCode: str
    merchantCenterAccountId: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterLinkingConfig(
    typing.TypedDict, total=False
):
    links: _list[GoogleCloudRetailV2alphaMerchantCenterLink]

@typing.type_check_only
class GoogleCloudRetailV2alphaModel(typing.TypedDict, total=False):
    createTime: str
    dataState: typing.Literal["DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"]
    displayName: str
    filteringOption: typing.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    modelFeaturesConfig: GoogleCloudRetailV2alphaModelModelFeaturesConfig
    name: str
    optimizationObjective: str
    pageOptimizationConfig: GoogleCloudRetailV2alphaModelPageOptimizationConfig
    periodicTuningState: typing.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2alphaModelServingConfigList]
    servingState: typing.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing.Literal["TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfig(
    typing.TypedDict, total=False
):
    contextProductsType: typing.Literal[
        "CONTEXT_PRODUCTS_TYPE_UNSPECIFIED",
        "SINGLE_CONTEXT_PRODUCT",
        "MULTIPLE_CONTEXT_PRODUCTS",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaModelModelFeaturesConfig(typing.TypedDict, total=False):
    frequentlyBoughtTogetherConfig: (
        GoogleCloudRetailV2alphaModelFrequentlyBoughtTogetherFeaturesConfig
    )

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfig(
    typing.TypedDict, total=False
):
    pageOptimizationEventType: str
    panels: _list[GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel]
    restriction: typing.Literal[
        "RESTRICTION_UNSPECIFIED",
        "NO_RESTRICTION",
        "UNIQUE_SERVING_CONFIG_RESTRICTION",
        "UNIQUE_MODEL_RESTRICTION",
        "UNIQUE_MODEL_TYPE_RESTRICTION",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate(
    typing.TypedDict, total=False
):
    servingConfigId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel(
    typing.TypedDict, total=False
):
    candidates: _list[GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate]
    defaultCandidate: GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate
    displayName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelServingConfigList(typing.TypedDict, total=False):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaOutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudRetailV2alphaOutputConfigBigQueryDestination
    gcsDestination: GoogleCloudRetailV2alphaOutputConfigGcsDestination

@typing.type_check_only
class GoogleCloudRetailV2alphaOutputConfigBigQueryDestination(
    typing.TypedDict, total=False
):
    datasetId: str
    tableIdPrefix: str
    tableType: str

@typing.type_check_only
class GoogleCloudRetailV2alphaOutputConfigGcsDestination(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaOutputResult(typing.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2alphaBigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2alphaGcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2alphaPanelInfo(typing.TypedDict, total=False):
    attributionToken: str
    displayName: str
    panelId: str
    panelPosition: int
    productDetails: _list[GoogleCloudRetailV2alphaProductDetail]
    totalPanels: int

@typing.type_check_only
class GoogleCloudRetailV2alphaPauseModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPinControlMetadata(typing.TypedDict, total=False):
    allMatchedPins: dict[str, typing.Any]
    droppedPins: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2alphaPinControlMetadataProductPins(
    typing.TypedDict, total=False
):
    productId: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictRequest(typing.TypedDict, total=False):
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2alphaUserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponse(typing.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudRetailV2alphaPredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponsePredictionResult(
    typing.TypedDict, total=False
):
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2alphaPriceInfo(typing.TypedDict, total=False):
    cost: float
    currencyCode: str
    originalPrice: float
    price: float
    priceEffectiveTime: str
    priceExpireTime: str
    priceRange: GoogleCloudRetailV2alphaPriceInfoPriceRange

@typing.type_check_only
class GoogleCloudRetailV2alphaPriceInfoPriceRange(typing.TypedDict, total=False):
    originalPrice: GoogleCloudRetailV2alphaInterval
    price: GoogleCloudRetailV2alphaInterval

@typing.type_check_only
class GoogleCloudRetailV2alphaProduct(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    audience: GoogleCloudRetailV2alphaAudience
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    availableQuantity: int
    availableTime: str
    brands: _list[str]
    categories: _list[str]
    collectionMemberIds: _list[str]
    colorInfo: GoogleCloudRetailV2alphaColorInfo
    conditions: _list[str]
    description: str
    expireTime: str
    fulfillmentInfo: _list[GoogleCloudRetailV2alphaFulfillmentInfo]
    gtin: str
    id: str
    images: _list[GoogleCloudRetailV2alphaImage]
    languageCode: str
    localInventories: _list[GoogleCloudRetailV2alphaLocalInventory]
    materials: _list[str]
    name: str
    patterns: _list[str]
    priceInfo: GoogleCloudRetailV2alphaPriceInfo
    primaryProductId: str
    promotions: _list[GoogleCloudRetailV2alphaPromotion]
    publishTime: str
    rating: GoogleCloudRetailV2alphaRating
    retrievableFields: str
    sizes: _list[str]
    tags: _list[str]
    title: str
    ttl: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PRIMARY", "VARIANT", "COLLECTION"]
    uri: str
    variants: _list[GoogleCloudRetailV2alphaProduct]

@typing.type_check_only
class GoogleCloudRetailV2alphaProductAttributeInterval(typing.TypedDict, total=False):
    interval: GoogleCloudRetailV2alphaInterval
    name: str

@typing.type_check_only
class GoogleCloudRetailV2alphaProductAttributeValue(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudRetailV2alphaProductDetail(typing.TypedDict, total=False):
    product: GoogleCloudRetailV2alphaProduct
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2alphaProductInlineSource(typing.TypedDict, total=False):
    products: _list[GoogleCloudRetailV2alphaProduct]

@typing.type_check_only
class GoogleCloudRetailV2alphaProductInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2alphaBigQuerySource
    gcsSource: GoogleCloudRetailV2alphaGcsSource
    productInlineSource: GoogleCloudRetailV2alphaProductInlineSource

@typing.type_check_only
class GoogleCloudRetailV2alphaProductLevelConfig(typing.TypedDict, total=False):
    ingestionProductType: str
    merchantCenterProductIdField: str

@typing.type_check_only
class GoogleCloudRetailV2alphaProject(typing.TypedDict, total=False):
    enrolledSolutions: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
        ]
    ]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPromotion(typing.TypedDict, total=False):
    promotionId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPurchaseTransaction(typing.TypedDict, total=False):
    cost: float
    currencyCode: str
    id: str
    revenue: float
    tax: float

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsResponse(typing.TypedDict, total=False):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRating(typing.TypedDict, total=False):
    averageRating: float
    ratingCount: int
    ratingHistogram: _list[int]

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsRequest(typing.TypedDict, total=False):
    userEventRejoinScope: typing.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsResponse(typing.TypedDict, total=False):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveCatalogAttributeRequest(
    typing.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveControlRequest(typing.TypedDict, total=False):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesRequest(
    typing.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesRequest(
    typing.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaReplaceCatalogAttributeRequest(
    typing.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2alphaCatalogAttribute
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2alphaResumeModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRule(typing.TypedDict, total=False):
    boostAction: GoogleCloudRetailV2alphaRuleBoostAction
    condition: GoogleCloudRetailV2alphaCondition
    doNotAssociateAction: GoogleCloudRetailV2alphaRuleDoNotAssociateAction
    filterAction: GoogleCloudRetailV2alphaRuleFilterAction
    forceReturnFacetAction: GoogleCloudRetailV2alphaRuleForceReturnFacetAction
    ignoreAction: GoogleCloudRetailV2alphaRuleIgnoreAction
    onewaySynonymsAction: GoogleCloudRetailV2alphaRuleOnewaySynonymsAction
    pinAction: GoogleCloudRetailV2alphaRulePinAction
    redirectAction: GoogleCloudRetailV2alphaRuleRedirectAction
    removeFacetAction: GoogleCloudRetailV2alphaRuleRemoveFacetAction
    replacementAction: GoogleCloudRetailV2alphaRuleReplacementAction
    twowaySynonymsAction: GoogleCloudRetailV2alphaRuleTwowaySynonymsAction

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleBoostAction(typing.TypedDict, total=False):
    boost: float
    productsFilter: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleDoNotAssociateAction(typing.TypedDict, total=False):
    doNotAssociateTerms: _list[str]
    queryTerms: _list[str]
    terms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleFilterAction(typing.TypedDict, total=False):
    filter: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleForceReturnFacetAction(typing.TypedDict, total=False):
    facetPositionAdjustments: _list[
        GoogleCloudRetailV2alphaRuleForceReturnFacetActionFacetPositionAdjustment
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleForceReturnFacetActionFacetPositionAdjustment(
    typing.TypedDict, total=False
):
    attributeName: str
    position: int

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleIgnoreAction(typing.TypedDict, total=False):
    ignoreTerms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleOnewaySynonymsAction(typing.TypedDict, total=False):
    onewayTerms: _list[str]
    queryTerms: _list[str]
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRulePinAction(typing.TypedDict, total=False):
    pinMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleRedirectAction(typing.TypedDict, total=False):
    redirectUri: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleRemoveFacetAction(typing.TypedDict, total=False):
    attributeNames: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleReplacementAction(typing.TypedDict, total=False):
    queryTerms: _list[str]
    replacementTerm: str
    term: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleTwowaySynonymsAction(typing.TypedDict, total=False):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaSafetySetting(typing.TypedDict, total=False):
    category: typing.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_CIVIC_INTEGRITY",
    ]
    method: typing.Literal["HARM_BLOCK_METHOD_UNSPECIFIED", "SEVERITY", "PROBABILITY"]
    threshold: typing.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequest(typing.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2alphaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    conversationalSearchSpec: (
        GoogleCloudRetailV2alphaSearchRequestConversationalSearchSpec
    )
    dynamicControls: _list[GoogleCloudRetailV2alphaControl]
    dynamicFacetSpec: GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec
    entity: str
    experimentId: str
    facetSpecs: _list[GoogleCloudRetailV2alphaSearchRequestFacetSpec]
    filter: str
    ignoredControlIds: _list[str]
    labels: dict[str, typing.Any]
    languageCode: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    personalizationSpec: GoogleCloudRetailV2alphaSearchRequestPersonalizationSpec
    placeId: str
    query: str
    queryExpansionSpec: GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec
    regionCode: str
    relevanceThreshold: typing.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "LOWEST"
    ]
    searchMode: typing.Literal[
        "SEARCH_MODE_UNSPECIFIED", "PRODUCT_SEARCH_ONLY", "FACETED_SEARCH_ONLY"
    ]
    spellCorrectionSpec: GoogleCloudRetailV2alphaSearchRequestSpellCorrectionSpec
    tileNavigationSpec: GoogleCloudRetailV2alphaSearchRequestTileNavigationSpec
    userAttributes: dict[str, typing.Any]
    userInfo: GoogleCloudRetailV2alphaUserInfo
    variantRollupKeys: _list[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestBoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[
        GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec
    ]
    skipBoostSpecValidation: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestConversationalSearchSpec(
    typing.TypedDict, total=False
):
    conversationId: str
    followupConversationRequested: bool
    userAnswer: GoogleCloudRetailV2alphaSearchRequestConversationalSearchSpecUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestConversationalSearchSpecUserAnswer(
    typing.TypedDict, total=False
):
    selectedAnswer: GoogleCloudRetailV2alphaSearchRequestConversationalSearchSpecUserAnswerSelectedAnswer
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestConversationalSearchSpecUserAnswerSelectedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue
    productAttributeValues: _list[GoogleCloudRetailV2alphaProductAttributeValue]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestFacetSpec(typing.TypedDict, total=False):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudRetailV2alphaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestFacetSpecFacetKey(
    typing.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudRetailV2alphaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    query: str
    restrictedValues: _list[str]
    returnMinMax: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestPersonalizationSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestSpellCorrectionSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestTileNavigationSpec(
    typing.TypedDict, total=False
):
    appliedTiles: _list[GoogleCloudRetailV2alphaTile]
    tileNavigationRequested: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponse(typing.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    conversationalSearchResult: (
        GoogleCloudRetailV2alphaSearchResponseConversationalSearchResult
    )
    correctedQuery: str
    experimentInfo: _list[GoogleCloudRetailV2alphaExperimentInfo]
    facets: _list[GoogleCloudRetailV2alphaSearchResponseFacet]
    invalidConditionBoostSpecs: _list[
        GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec
    ]
    nextPageToken: str
    pinControlMetadata: GoogleCloudRetailV2alphaPinControlMetadata
    queryExpansionInfo: GoogleCloudRetailV2alphaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudRetailV2alphaSearchResponseSearchResult]
    tileNavigationResult: GoogleCloudRetailV2alphaSearchResponseTileNavigationResult
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseConversationalSearchResult(
    typing.TypedDict, total=False
):
    additionalFilter: (
        GoogleCloudRetailV2alphaSearchResponseConversationalSearchResultAdditionalFilter
    )
    additionalFilters: _list[
        GoogleCloudRetailV2alphaSearchResponseConversationalSearchResultAdditionalFilter
    ]
    conversationId: str
    followupQuestion: str
    refinedQuery: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2alphaSearchResponseConversationalSearchResultSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseConversationalSearchResultAdditionalFilter(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseConversationalSearchResultSuggestedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseFacet(typing.TypedDict, total=False):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudRetailV2alphaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseFacetFacetValue(
    typing.TypedDict, total=False
):
    count: str
    interval: GoogleCloudRetailV2alphaInterval
    maxValue: float
    minValue: float
    value: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseQueryExpansionInfo(
    typing.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseSearchResult(typing.TypedDict, total=False):
    id: str
    matchingVariantCount: int
    matchingVariantFields: dict[str, typing.Any]
    modelScores: dict[str, typing.Any]
    personalLabels: _list[str]
    product: GoogleCloudRetailV2alphaProduct
    variantRollupValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseTileNavigationResult(
    typing.TypedDict, total=False
):
    tiles: _list[GoogleCloudRetailV2alphaTile]

@typing.type_check_only
class GoogleCloudRetailV2alphaServingConfig(typing.TypedDict, total=False):
    boostControlIds: _list[str]
    displayName: str
    diversityLevel: str
    diversityType: typing.Literal[
        "DIVERSITY_TYPE_UNSPECIFIED", "RULE_BASED_DIVERSITY", "DATA_DRIVEN_DIVERSITY"
    ]
    doNotAssociateControlIds: _list[str]
    dynamicFacetSpec: GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec
    enableCategoryFilterLevel: str
    facetControlIds: _list[str]
    filterControlIds: _list[str]
    ignoreControlIds: _list[str]
    ignoreRecsDenylist: bool
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: GoogleCloudRetailV2alphaSearchRequestPersonalizationSpec
    priceRerankingLevel: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionTypes: _list[
        typing.Literal[
            "SOLUTION_TYPE_UNSPECIFIED",
            "SOLUTION_TYPE_RECOMMENDATION",
            "SOLUTION_TYPE_SEARCH",
        ]
    ]
    twowaySynonymsControlIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaSetDefaultBranchRequest(typing.TypedDict, total=False):
    branchId: str
    force: bool
    note: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryRequest(typing.TypedDict, total=False):
    allowMissing: bool
    inventory: GoogleCloudRetailV2alphaProduct
    setMask: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaStringList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaTile(typing.TypedDict, total=False):
    productAttributeInterval: GoogleCloudRetailV2alphaProductAttributeInterval
    productAttributeValue: GoogleCloudRetailV2alphaProductAttributeValue
    representativeProductId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTransformedUserEventsMetadata(
    typing.TypedDict, total=False
):
    sourceEventsCount: str
    transformedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUpdateGenerativeQuestionConfigRequest(
    typing.TypedDict, total=False
):
    generativeQuestionConfig: GoogleCloudRetailV2alphaGenerativeQuestionConfig
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEvent(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    cartId: str
    completionDetail: GoogleCloudRetailV2alphaCompletionDetail
    entity: str
    eventTime: str
    eventType: str
    experimentIds: _list[str]
    filter: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageViewId: str
    panels: _list[GoogleCloudRetailV2alphaPanelInfo]
    productDetails: _list[GoogleCloudRetailV2alphaProductDetail]
    purchaseTransaction: GoogleCloudRetailV2alphaPurchaseTransaction
    referrerUri: str
    searchQuery: str
    sessionId: str
    uri: str
    userInfo: GoogleCloudRetailV2alphaUserInfo
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventImportSummary(typing.TypedDict, total=False):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventInlineSource(typing.TypedDict, total=False):
    userEvents: _list[GoogleCloudRetailV2alphaUserEvent]

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2alphaBigQuerySource
    gcsSource: GoogleCloudRetailV2alphaGcsSource
    userEventInlineSource: GoogleCloudRetailV2alphaUserEventInlineSource

@typing.type_check_only
class GoogleCloudRetailV2alphaUserInfo(typing.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaBigQueryOutputResult(typing.TypedDict, total=False):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaCreateModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportAnalyticsMetricsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaExportErrorsConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportMetadata(typing.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaGcsOutputResult(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2betaImportErrorsConfig(typing.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    importSummary: GoogleCloudRetailV2betaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2betaModel(typing.TypedDict, total=False):
    createTime: str
    dataState: typing.Literal["DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"]
    displayName: str
    filteringOption: typing.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    modelFeaturesConfig: GoogleCloudRetailV2betaModelModelFeaturesConfig
    name: str
    optimizationObjective: str
    periodicTuningState: typing.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2betaModelServingConfigList]
    servingState: typing.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing.Literal["TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfig(
    typing.TypedDict, total=False
):
    contextProductsType: typing.Literal[
        "CONTEXT_PRODUCTS_TYPE_UNSPECIFIED",
        "SINGLE_CONTEXT_PRODUCT",
        "MULTIPLE_CONTEXT_PRODUCTS",
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaModelModelFeaturesConfig(typing.TypedDict, total=False):
    frequentlyBoughtTogetherConfig: (
        GoogleCloudRetailV2betaModelFrequentlyBoughtTogetherFeaturesConfig
    )

@typing.type_check_only
class GoogleCloudRetailV2betaModelServingConfigList(typing.TypedDict, total=False):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaOutputResult(typing.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2betaBigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2betaGcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsResponse(typing.TypedDict, total=False):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsResponse(typing.TypedDict, total=False):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventImportSummary(typing.TypedDict, total=False):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int
