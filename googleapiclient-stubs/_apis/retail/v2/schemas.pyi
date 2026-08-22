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
class GoogleCloudRetailV2AddCatalogAttributeRequest(typing.TypedDict, total=False):
    catalogAttribute: GoogleCloudRetailV2CatalogAttribute

@typing.type_check_only
class GoogleCloudRetailV2AddControlRequest(typing.TypedDict, total=False):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesRequest(typing.TypedDict, total=False):
    addTime: str
    allowMissing: bool
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesRequest(typing.TypedDict, total=False):
    addMask: str
    addTime: str
    allowMissing: bool
    localInventories: _list[GoogleCloudRetailV2LocalInventory]

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2AttributesConfig(typing.TypedDict, total=False):
    attributeConfigLevel: typing.Literal[
        "ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED",
        "PRODUCT_LEVEL_ATTRIBUTE_CONFIG",
        "CATALOG_LEVEL_ATTRIBUTE_CONFIG",
    ]
    catalogAttributes: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2Audience(typing.TypedDict, total=False):
    ageGroups: _list[str]
    genders: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2BatchUpdateGenerativeQuestionConfigsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudRetailV2UpdateGenerativeQuestionConfigRequest]

@typing.type_check_only
class GoogleCloudRetailV2BatchUpdateGenerativeQuestionConfigsResponse(
    typing.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2GenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2BigQueryOutputResult(typing.TypedDict, total=False):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2BigQuerySource(typing.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2Catalog(typing.TypedDict, total=False):
    displayName: str
    name: str
    productLevelConfig: GoogleCloudRetailV2ProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2CatalogAttribute(typing.TypedDict, total=False):
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
    facetConfig: GoogleCloudRetailV2CatalogAttributeFacetConfig
    inUse: bool
    indexableOption: typing.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    key: str
    retrievableOption: typing.Literal[
        "RETRIEVABLE_OPTION_UNSPECIFIED", "RETRIEVABLE_ENABLED", "RETRIEVABLE_DISABLED"
    ]
    searchableOption: typing.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]
    type: typing.Literal["UNKNOWN", "TEXTUAL", "NUMERICAL"]

@typing.type_check_only
class GoogleCloudRetailV2CatalogAttributeFacetConfig(typing.TypedDict, total=False):
    facetIntervals: _list[GoogleCloudRetailV2Interval]
    ignoredFacetValues: _list[
        GoogleCloudRetailV2CatalogAttributeFacetConfigIgnoredFacetValues
    ]
    mergedFacet: GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacet
    mergedFacetValues: _list[
        GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue
    ]
    rerankConfig: GoogleCloudRetailV2CatalogAttributeFacetConfigRerankConfig

@typing.type_check_only
class GoogleCloudRetailV2CatalogAttributeFacetConfigIgnoredFacetValues(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacet(
    typing.TypedDict, total=False
):
    mergedFacetKey: str

@typing.type_check_only
class GoogleCloudRetailV2CatalogAttributeFacetConfigMergedFacetValue(
    typing.TypedDict, total=False
):
    mergedValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2CatalogAttributeFacetConfigRerankConfig(
    typing.TypedDict, total=False
):
    facetValues: _list[str]
    rerankFacet: bool

@typing.type_check_only
class GoogleCloudRetailV2CollectUserEventRequest(typing.TypedDict, total=False):
    ets: str
    prebuiltRule: str
    rawJson: str
    uri: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailV2ColorInfo(typing.TypedDict, total=False):
    colorFamilies: _list[str]
    colors: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2CompleteQueryResponse(typing.TypedDict, total=False):
    attributeResults: dict[str, typing.Any]
    attributionToken: str
    completionResults: _list[GoogleCloudRetailV2CompleteQueryResponseCompletionResult]
    recentSearchResults: _list[
        GoogleCloudRetailV2CompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2CompleteQueryResponseAttributeResult(
    typing.TypedDict, total=False
):
    suggestions: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2CompleteQueryResponseCompletionResult(
    typing.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    suggestion: str

@typing.type_check_only
class GoogleCloudRetailV2CompleteQueryResponseRecentSearchResult(
    typing.TypedDict, total=False
):
    recentSearch: str

@typing.type_check_only
class GoogleCloudRetailV2CompletionConfig(typing.TypedDict, total=False):
    allowlistInputConfig: GoogleCloudRetailV2CompletionDataInputConfig
    autoLearning: bool
    denylistInputConfig: GoogleCloudRetailV2CompletionDataInputConfig
    lastAllowlistImportOperation: str
    lastDenylistImportOperation: str
    lastSuggestionsImportOperation: str
    matchingOrder: str
    maxSuggestions: int
    minPrefixLength: int
    name: str
    suggestionsInputConfig: GoogleCloudRetailV2CompletionDataInputConfig

@typing.type_check_only
class GoogleCloudRetailV2CompletionDataInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2BigQuerySource

@typing.type_check_only
class GoogleCloudRetailV2CompletionDetail(typing.TypedDict, total=False):
    completionAttributionToken: str
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudRetailV2Condition(typing.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudRetailV2ConditionTimeRange]
    pageCategories: _list[str]
    queryTerms: _list[GoogleCloudRetailV2ConditionQueryTerm]

@typing.type_check_only
class GoogleCloudRetailV2ConditionQueryTerm(typing.TypedDict, total=False):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudRetailV2ConditionTimeRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudRetailV2Control(typing.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    displayName: str
    name: str
    rule: GoogleCloudRetailV2Rule
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
class GoogleCloudRetailV2ConversationalSearchCustomizationConfig(
    typing.TypedDict, total=False
):
    catalog: str
    intentClassificationConfig: GoogleCloudRetailV2IntentClassificationConfig
    retailerDisplayName: str

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchRequest(typing.TypedDict, total=False):
    branch: str
    conversationId: str
    conversationalFilteringSpec: (
        GoogleCloudRetailV2ConversationalSearchRequestConversationalFilteringSpec
    )
    pageCategories: _list[str]
    query: str
    safetySettings: _list[GoogleCloudRetailV2SafetySetting]
    searchParams: GoogleCloudRetailV2ConversationalSearchRequestSearchParams
    userInfo: GoogleCloudRetailV2UserInfo
    userLabels: dict[str, typing.Any]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchRequestConversationalFilteringSpec(
    typing.TypedDict, total=False
):
    conversationalFilteringMode: typing.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "ENABLED", "CONVERSATIONAL_FILTER_ONLY"
    ]
    enableConversationalFiltering: bool
    userAnswer: GoogleCloudRetailV2ConversationalSearchRequestUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchRequestSearchParams(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudRetailV2SearchRequestBoostSpec
    canonicalFilter: str
    filter: str
    sortBy: str

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchRequestUserAnswer(
    typing.TypedDict, total=False
):
    selectedAnswer: (
        GoogleCloudRetailV2ConversationalSearchRequestUserAnswerSelectedAnswer
    )
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchRequestUserAnswerSelectedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchResponse(typing.TypedDict, total=False):
    conversationId: str
    conversationalFilteringResult: (
        GoogleCloudRetailV2ConversationalSearchResponseConversationalFilteringResult
    )
    conversationalTextResponse: str
    followupQuestion: GoogleCloudRetailV2ConversationalSearchResponseFollowupQuestion
    refinedSearch: _list[GoogleCloudRetailV2ConversationalSearchResponseRefinedSearch]
    state: typing.Literal["STATE_UNSPECIFIED", "STREAMING", "SUCCEEDED"]
    userQueryTypes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchResponseConversationalFilteringResult(
    typing.TypedDict, total=False
):
    additionalFilter: GoogleCloudRetailV2ConversationalSearchResponseConversationalFilteringResultAdditionalFilter
    followupQuestion: GoogleCloudRetailV2ConversationalSearchResponseFollowupQuestion

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchResponseConversationalFilteringResultAdditionalFilter(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchResponseFollowupQuestion(
    typing.TypedDict, total=False
):
    followupQuestion: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2ConversationalSearchResponseFollowupQuestionSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchResponseFollowupQuestionSuggestedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2ConversationalSearchResponseRefinedSearch(
    typing.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudRetailV2CreateModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2CustomAttribute(typing.TypedDict, total=False):
    indexable: bool
    numbers: _list[float]
    searchable: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2DoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudRetailV2ExperimentInfo(typing.TypedDict, total=False):
    experiment: str
    servingConfigExperiment: GoogleCloudRetailV2ExperimentInfoServingConfigExperiment

@typing.type_check_only
class GoogleCloudRetailV2ExperimentInfoServingConfigExperiment(
    typing.TypedDict, total=False
):
    experimentServingConfig: str
    originalServingConfig: str

@typing.type_check_only
class GoogleCloudRetailV2ExportAnalyticsMetricsRequest(typing.TypedDict, total=False):
    filter: str
    outputConfig: GoogleCloudRetailV2OutputConfig

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
class GoogleCloudRetailV2FulfillmentInfo(typing.TypedDict, total=False):
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2GcsOutputResult(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2GcsSource(typing.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2GenerativeQuestionConfig(typing.TypedDict, total=False):
    allowedInConversation: bool
    catalog: str
    exampleValues: _list[str]
    facet: str
    finalQuestion: str
    frequency: float
    generatedQuestion: str

@typing.type_check_only
class GoogleCloudRetailV2GenerativeQuestionsFeatureConfig(
    typing.TypedDict, total=False
):
    catalog: str
    featureEnabled: bool
    minimumProducts: int

@typing.type_check_only
class GoogleCloudRetailV2GetDefaultBranchResponse(typing.TypedDict, total=False):
    branch: str
    note: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2Image(typing.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2ImportCompletionDataRequest(typing.TypedDict, total=False):
    inputConfig: GoogleCloudRetailV2CompletionDataInputConfig
    notificationPubsubTopic: str

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
class GoogleCloudRetailV2ImportProductsRequest(typing.TypedDict, total=False):
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig
    inputConfig: GoogleCloudRetailV2ProductInputConfig
    notificationPubsubTopic: str
    reconciliationMode: typing.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    requestId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2ImportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2ImportUserEventsRequest(typing.TypedDict, total=False):
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig
    inputConfig: GoogleCloudRetailV2UserEventInputConfig

@typing.type_check_only
class GoogleCloudRetailV2ImportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig
    importSummary: GoogleCloudRetailV2UserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2IntentClassificationConfig(typing.TypedDict, total=False):
    blocklistKeywords: _list[str]
    disabledIntentTypes: _list[str]
    example: _list[GoogleCloudRetailV2IntentClassificationConfigExample]
    inlineSource: GoogleCloudRetailV2IntentClassificationConfigInlineSource
    modelPreamble: str

@typing.type_check_only
class GoogleCloudRetailV2IntentClassificationConfigExample(
    typing.TypedDict, total=False
):
    classifiedPositive: bool
    intentType: str
    query: str
    reason: str

@typing.type_check_only
class GoogleCloudRetailV2IntentClassificationConfigInlineForceIntent(
    typing.TypedDict, total=False
):
    intentType: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"]
    query: str

@typing.type_check_only
class GoogleCloudRetailV2IntentClassificationConfigInlineSource(
    typing.TypedDict, total=False
):
    inlineForceIntents: _list[
        GoogleCloudRetailV2IntentClassificationConfigInlineForceIntent
    ]

@typing.type_check_only
class GoogleCloudRetailV2Interval(typing.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudRetailV2ListCatalogsResponse(typing.TypedDict, total=False):
    catalogs: _list[GoogleCloudRetailV2Catalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2ListControlsResponse(typing.TypedDict, total=False):
    controls: _list[GoogleCloudRetailV2Control]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2ListGenerativeQuestionConfigsResponse(
    typing.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2GenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2ListModelsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudRetailV2Model]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2ListProductsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    products: _list[GoogleCloudRetailV2Product]

@typing.type_check_only
class GoogleCloudRetailV2ListServingConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudRetailV2ServingConfig]

@typing.type_check_only
class GoogleCloudRetailV2LocalInventory(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    fulfillmentTypes: _list[str]
    placeId: str
    priceInfo: GoogleCloudRetailV2PriceInfo

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
class GoogleCloudRetailV2OutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudRetailV2OutputConfigBigQueryDestination
    gcsDestination: GoogleCloudRetailV2OutputConfigGcsDestination

@typing.type_check_only
class GoogleCloudRetailV2OutputConfigBigQueryDestination(typing.TypedDict, total=False):
    datasetId: str
    tableIdPrefix: str
    tableType: str

@typing.type_check_only
class GoogleCloudRetailV2OutputConfigGcsDestination(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2OutputResult(typing.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2BigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2GcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2PanelInfo(typing.TypedDict, total=False):
    attributionToken: str
    displayName: str
    panelId: str
    panelPosition: int
    productDetails: _list[GoogleCloudRetailV2ProductDetail]
    totalPanels: int

@typing.type_check_only
class GoogleCloudRetailV2PauseModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2PinControlMetadata(typing.TypedDict, total=False):
    allMatchedPins: dict[str, typing.Any]
    droppedPins: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2PinControlMetadataProductPins(typing.TypedDict, total=False):
    productId: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2PredictRequest(typing.TypedDict, total=False):
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2UserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2PredictResponse(typing.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudRetailV2PredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2PredictResponsePredictionResult(typing.TypedDict, total=False):
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2PriceInfo(typing.TypedDict, total=False):
    cost: float
    currencyCode: str
    originalPrice: float
    price: float
    priceEffectiveTime: str
    priceExpireTime: str
    priceRange: GoogleCloudRetailV2PriceInfoPriceRange

@typing.type_check_only
class GoogleCloudRetailV2PriceInfoPriceRange(typing.TypedDict, total=False):
    originalPrice: GoogleCloudRetailV2Interval
    price: GoogleCloudRetailV2Interval

@typing.type_check_only
class GoogleCloudRetailV2Product(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    audience: GoogleCloudRetailV2Audience
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    availableQuantity: int
    availableTime: str
    brands: _list[str]
    categories: _list[str]
    collectionMemberIds: _list[str]
    colorInfo: GoogleCloudRetailV2ColorInfo
    conditions: _list[str]
    description: str
    expireTime: str
    fulfillmentInfo: _list[GoogleCloudRetailV2FulfillmentInfo]
    gtin: str
    id: str
    images: _list[GoogleCloudRetailV2Image]
    languageCode: str
    localInventories: _list[GoogleCloudRetailV2LocalInventory]
    materials: _list[str]
    name: str
    patterns: _list[str]
    priceInfo: GoogleCloudRetailV2PriceInfo
    primaryProductId: str
    promotions: _list[GoogleCloudRetailV2Promotion]
    publishTime: str
    rating: GoogleCloudRetailV2Rating
    retrievableFields: str
    sizes: _list[str]
    tags: _list[str]
    title: str
    ttl: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PRIMARY", "VARIANT", "COLLECTION"]
    uri: str
    variants: _list[GoogleCloudRetailV2Product]

@typing.type_check_only
class GoogleCloudRetailV2ProductAttributeInterval(typing.TypedDict, total=False):
    interval: GoogleCloudRetailV2Interval
    name: str

@typing.type_check_only
class GoogleCloudRetailV2ProductAttributeValue(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudRetailV2ProductDetail(typing.TypedDict, total=False):
    product: GoogleCloudRetailV2Product
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2ProductInlineSource(typing.TypedDict, total=False):
    products: _list[GoogleCloudRetailV2Product]

@typing.type_check_only
class GoogleCloudRetailV2ProductInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2BigQuerySource
    gcsSource: GoogleCloudRetailV2GcsSource
    productInlineSource: GoogleCloudRetailV2ProductInlineSource

@typing.type_check_only
class GoogleCloudRetailV2ProductLevelConfig(typing.TypedDict, total=False):
    ingestionProductType: str
    merchantCenterProductIdField: str

@typing.type_check_only
class GoogleCloudRetailV2Promotion(typing.TypedDict, total=False):
    promotionId: str

@typing.type_check_only
class GoogleCloudRetailV2PurchaseTransaction(typing.TypedDict, total=False):
    cost: float
    currencyCode: str
    id: str
    revenue: float
    tax: float

@typing.type_check_only
class GoogleCloudRetailV2PurgeMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2PurgeProductsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2PurgeUserEventsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2PurgeUserEventsResponse(typing.TypedDict, total=False):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2Rating(typing.TypedDict, total=False):
    averageRating: float
    ratingCount: int
    ratingHistogram: _list[int]

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsRequest(typing.TypedDict, total=False):
    userEventRejoinScope: typing.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsResponse(typing.TypedDict, total=False):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveCatalogAttributeRequest(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveControlRequest(typing.TypedDict, total=False):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesRequest(typing.TypedDict, total=False):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesRequest(typing.TypedDict, total=False):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2ReplaceCatalogAttributeRequest(typing.TypedDict, total=False):
    catalogAttribute: GoogleCloudRetailV2CatalogAttribute
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2ResumeModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2Rule(typing.TypedDict, total=False):
    boostAction: GoogleCloudRetailV2RuleBoostAction
    condition: GoogleCloudRetailV2Condition
    doNotAssociateAction: GoogleCloudRetailV2RuleDoNotAssociateAction
    filterAction: GoogleCloudRetailV2RuleFilterAction
    forceReturnFacetAction: GoogleCloudRetailV2RuleForceReturnFacetAction
    ignoreAction: GoogleCloudRetailV2RuleIgnoreAction
    onewaySynonymsAction: GoogleCloudRetailV2RuleOnewaySynonymsAction
    pinAction: GoogleCloudRetailV2RulePinAction
    redirectAction: GoogleCloudRetailV2RuleRedirectAction
    removeFacetAction: GoogleCloudRetailV2RuleRemoveFacetAction
    replacementAction: GoogleCloudRetailV2RuleReplacementAction
    twowaySynonymsAction: GoogleCloudRetailV2RuleTwowaySynonymsAction

@typing.type_check_only
class GoogleCloudRetailV2RuleBoostAction(typing.TypedDict, total=False):
    boost: float
    productsFilter: str

@typing.type_check_only
class GoogleCloudRetailV2RuleDoNotAssociateAction(typing.TypedDict, total=False):
    doNotAssociateTerms: _list[str]
    queryTerms: _list[str]
    terms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2RuleFilterAction(typing.TypedDict, total=False):
    filter: str

@typing.type_check_only
class GoogleCloudRetailV2RuleForceReturnFacetAction(typing.TypedDict, total=False):
    facetPositionAdjustments: _list[
        GoogleCloudRetailV2RuleForceReturnFacetActionFacetPositionAdjustment
    ]

@typing.type_check_only
class GoogleCloudRetailV2RuleForceReturnFacetActionFacetPositionAdjustment(
    typing.TypedDict, total=False
):
    attributeName: str
    position: int

@typing.type_check_only
class GoogleCloudRetailV2RuleIgnoreAction(typing.TypedDict, total=False):
    ignoreTerms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2RuleOnewaySynonymsAction(typing.TypedDict, total=False):
    onewayTerms: _list[str]
    queryTerms: _list[str]
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2RulePinAction(typing.TypedDict, total=False):
    pinMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2RuleRedirectAction(typing.TypedDict, total=False):
    redirectUri: str

@typing.type_check_only
class GoogleCloudRetailV2RuleRemoveFacetAction(typing.TypedDict, total=False):
    attributeNames: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2RuleReplacementAction(typing.TypedDict, total=False):
    queryTerms: _list[str]
    replacementTerm: str
    term: str

@typing.type_check_only
class GoogleCloudRetailV2RuleTwowaySynonymsAction(typing.TypedDict, total=False):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2SafetySetting(typing.TypedDict, total=False):
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
class GoogleCloudRetailV2SearchRequest(typing.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2SearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    conversationalSearchSpec: GoogleCloudRetailV2SearchRequestConversationalSearchSpec
    dynamicFacetSpec: GoogleCloudRetailV2SearchRequestDynamicFacetSpec
    entity: str
    facetSpecs: _list[GoogleCloudRetailV2SearchRequestFacetSpec]
    filter: str
    labels: dict[str, typing.Any]
    languageCode: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    personalizationSpec: GoogleCloudRetailV2SearchRequestPersonalizationSpec
    placeId: str
    query: str
    queryExpansionSpec: GoogleCloudRetailV2SearchRequestQueryExpansionSpec
    regionCode: str
    searchMode: typing.Literal[
        "SEARCH_MODE_UNSPECIFIED", "PRODUCT_SEARCH_ONLY", "FACETED_SEARCH_ONLY"
    ]
    spellCorrectionSpec: GoogleCloudRetailV2SearchRequestSpellCorrectionSpec
    tileNavigationSpec: GoogleCloudRetailV2SearchRequestTileNavigationSpec
    userAttributes: dict[str, typing.Any]
    userInfo: GoogleCloudRetailV2UserInfo
    variantRollupKeys: _list[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestBoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[
        GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpec
    ]
    skipBoostSpecValidation: bool

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestConversationalSearchSpec(
    typing.TypedDict, total=False
):
    conversationId: str
    followupConversationRequested: bool
    userAnswer: GoogleCloudRetailV2SearchRequestConversationalSearchSpecUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestConversationalSearchSpecUserAnswer(
    typing.TypedDict, total=False
):
    selectedAnswer: (
        GoogleCloudRetailV2SearchRequestConversationalSearchSpecUserAnswerSelectedAnswer
    )
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestConversationalSearchSpecUserAnswerSelectedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue
    productAttributeValues: _list[GoogleCloudRetailV2ProductAttributeValue]

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestDynamicFacetSpec(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestFacetSpec(typing.TypedDict, total=False):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudRetailV2SearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestFacetSpecFacetKey(typing.TypedDict, total=False):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudRetailV2Interval]
    key: str
    orderBy: str
    prefixes: _list[str]
    query: str
    restrictedValues: _list[str]
    returnMinMax: bool

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestPersonalizationSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestQueryExpansionSpec(typing.TypedDict, total=False):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestSpellCorrectionSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudRetailV2SearchRequestTileNavigationSpec(typing.TypedDict, total=False):
    appliedTiles: _list[GoogleCloudRetailV2Tile]
    tileNavigationRequested: bool

@typing.type_check_only
class GoogleCloudRetailV2SearchResponse(typing.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    conversationalSearchResult: (
        GoogleCloudRetailV2SearchResponseConversationalSearchResult
    )
    correctedQuery: str
    experimentInfo: _list[GoogleCloudRetailV2ExperimentInfo]
    facets: _list[GoogleCloudRetailV2SearchResponseFacet]
    invalidConditionBoostSpecs: _list[
        GoogleCloudRetailV2SearchRequestBoostSpecConditionBoostSpec
    ]
    nextPageToken: str
    pinControlMetadata: GoogleCloudRetailV2PinControlMetadata
    queryExpansionInfo: GoogleCloudRetailV2SearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudRetailV2SearchResponseSearchResult]
    tileNavigationResult: GoogleCloudRetailV2SearchResponseTileNavigationResult
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseConversationalSearchResult(
    typing.TypedDict, total=False
):
    additionalFilter: (
        GoogleCloudRetailV2SearchResponseConversationalSearchResultAdditionalFilter
    )
    additionalFilters: _list[
        GoogleCloudRetailV2SearchResponseConversationalSearchResultAdditionalFilter
    ]
    conversationId: str
    followupQuestion: str
    refinedQuery: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2SearchResponseConversationalSearchResultSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseConversationalSearchResultAdditionalFilter(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseConversationalSearchResultSuggestedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseFacet(typing.TypedDict, total=False):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudRetailV2SearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseFacetFacetValue(typing.TypedDict, total=False):
    count: str
    interval: GoogleCloudRetailV2Interval
    maxValue: float
    minValue: float
    value: str

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseQueryExpansionInfo(
    typing.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseSearchResult(typing.TypedDict, total=False):
    id: str
    matchingVariantCount: int
    matchingVariantFields: dict[str, typing.Any]
    modelScores: dict[str, typing.Any]
    personalLabels: _list[str]
    product: GoogleCloudRetailV2Product
    variantRollupValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2SearchResponseTileNavigationResult(
    typing.TypedDict, total=False
):
    tiles: _list[GoogleCloudRetailV2Tile]

@typing.type_check_only
class GoogleCloudRetailV2ServingConfig(typing.TypedDict, total=False):
    boostControlIds: _list[str]
    displayName: str
    diversityLevel: str
    diversityType: typing.Literal[
        "DIVERSITY_TYPE_UNSPECIFIED", "RULE_BASED_DIVERSITY", "DATA_DRIVEN_DIVERSITY"
    ]
    doNotAssociateControlIds: _list[str]
    dynamicFacetSpec: GoogleCloudRetailV2SearchRequestDynamicFacetSpec
    enableCategoryFilterLevel: str
    facetControlIds: _list[str]
    filterControlIds: _list[str]
    ignoreControlIds: _list[str]
    ignoreRecsDenylist: bool
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: GoogleCloudRetailV2SearchRequestPersonalizationSpec
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
class GoogleCloudRetailV2SetDefaultBranchRequest(typing.TypedDict, total=False):
    branchId: str
    force: bool
    note: str

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryRequest(typing.TypedDict, total=False):
    allowMissing: bool
    inventory: GoogleCloudRetailV2Product
    setMask: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2StringList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2Tile(typing.TypedDict, total=False):
    productAttributeInterval: GoogleCloudRetailV2ProductAttributeInterval
    productAttributeValue: GoogleCloudRetailV2ProductAttributeValue
    representativeProductId: str

@typing.type_check_only
class GoogleCloudRetailV2TuneModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2TuneModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2TuneModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2UpdateGenerativeQuestionConfigRequest(
    typing.TypedDict, total=False
):
    generativeQuestionConfig: GoogleCloudRetailV2GenerativeQuestionConfig
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2UserEvent(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    cartId: str
    completionDetail: GoogleCloudRetailV2CompletionDetail
    entity: str
    eventTime: str
    eventType: str
    experimentIds: _list[str]
    filter: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageViewId: str
    panels: _list[GoogleCloudRetailV2PanelInfo]
    productDetails: _list[GoogleCloudRetailV2ProductDetail]
    purchaseTransaction: GoogleCloudRetailV2PurchaseTransaction
    referrerUri: str
    searchQuery: str
    sessionId: str
    uri: str
    userInfo: GoogleCloudRetailV2UserInfo
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2UserEventImportSummary(typing.TypedDict, total=False):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2UserEventInlineSource(typing.TypedDict, total=False):
    userEvents: _list[GoogleCloudRetailV2UserEvent]

@typing.type_check_only
class GoogleCloudRetailV2UserEventInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2BigQuerySource
    gcsSource: GoogleCloudRetailV2GcsSource
    userEventInlineSource: GoogleCloudRetailV2UserEventInlineSource

@typing.type_check_only
class GoogleCloudRetailV2UserInfo(typing.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQueryOutputResult(typing.TypedDict, total=False):
    datasetId: str
    tableId: str

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
class GoogleCloudRetailV2alphaEnrollSolutionMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionResponse(typing.TypedDict, total=False):
    enrolledSolution: typing.Literal[
        "SOLUTION_TYPE_UNSPECIFIED",
        "SOLUTION_TYPE_RECOMMENDATION",
        "SOLUTION_TYPE_SEARCH",
    ]

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
class GoogleCloudRetailV2alphaExportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaExportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaGcsOutputResult(typing.TypedDict, total=False):
    outputUri: str

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
class GoogleCloudRetailV2alphaImportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    importSummary: GoogleCloudRetailV2alphaUserEventImportSummary

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
class GoogleCloudRetailV2alphaOutputResult(typing.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2alphaBigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2alphaGcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsResponse(typing.TypedDict, total=False):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsResponse(typing.TypedDict, total=False):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryResponse(typing.TypedDict, total=False): ...

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
class GoogleCloudRetailV2alphaTuneModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventImportSummary(typing.TypedDict, total=False):
    joinedEventsCount: str
    unjoinedEventsCount: str

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
