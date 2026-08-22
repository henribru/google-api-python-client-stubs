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
class GoogleCloudRetailV2betaAddCatalogAttributeRequest(typing.TypedDict, total=False):
    catalogAttribute: GoogleCloudRetailV2betaCatalogAttribute

@typing.type_check_only
class GoogleCloudRetailV2betaAddControlRequest(typing.TypedDict, total=False):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesRequest(typing.TypedDict, total=False):
    addTime: str
    allowMissing: bool
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesRequest(typing.TypedDict, total=False):
    addMask: str
    addTime: str
    allowMissing: bool
    localInventories: _list[GoogleCloudRetailV2betaLocalInventory]

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAlertConfig(typing.TypedDict, total=False):
    alertPolicies: _list[GoogleCloudRetailV2betaAlertConfigAlertPolicy]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaAlertConfigAlertPolicy(typing.TypedDict, total=False):
    alertGroup: str
    enrollStatus: typing.Literal["ENROLL_STATUS_UNSPECIFIED", "ENROLLED", "DECLINED"]
    recipients: _list[GoogleCloudRetailV2betaAlertConfigAlertPolicyRecipient]

@typing.type_check_only
class GoogleCloudRetailV2betaAlertConfigAlertPolicyRecipient(
    typing.TypedDict, total=False
):
    emailAddress: str

@typing.type_check_only
class GoogleCloudRetailV2betaAttributesConfig(typing.TypedDict, total=False):
    attributeConfigLevel: typing.Literal[
        "ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED",
        "PRODUCT_LEVEL_ATTRIBUTE_CONFIG",
        "CATALOG_LEVEL_ATTRIBUTE_CONFIG",
    ]
    catalogAttributes: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaAudience(typing.TypedDict, total=False):
    ageGroups: _list[str]
    genders: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesRequest(
    typing.TypedDict, total=False
):
    attributeKeys: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponse(
    typing.TypedDict, total=False
):
    deletedCatalogAttributes: _list[str]
    resetCatalogAttributes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleCloudRetailV2betaUpdateGenerativeQuestionConfigRequest]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchUpdateGenerativeQuestionConfigsResponse(
    typing.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2betaGenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaBigQueryOutputResult(typing.TypedDict, total=False):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaBigQuerySource(typing.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaCatalog(typing.TypedDict, total=False):
    displayName: str
    merchantCenterLinkingConfig: GoogleCloudRetailV2betaMerchantCenterLinkingConfig
    name: str
    productLevelConfig: GoogleCloudRetailV2betaProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttribute(typing.TypedDict, total=False):
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
    facetConfig: GoogleCloudRetailV2betaCatalogAttributeFacetConfig
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
class GoogleCloudRetailV2betaCatalogAttributeFacetConfig(typing.TypedDict, total=False):
    facetIntervals: _list[GoogleCloudRetailV2betaInterval]
    ignoredFacetValues: _list[
        GoogleCloudRetailV2betaCatalogAttributeFacetConfigIgnoredFacetValues
    ]
    mergedFacet: GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacet
    mergedFacetValues: _list[
        GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacetValue
    ]
    rerankConfig: GoogleCloudRetailV2betaCatalogAttributeFacetConfigRerankConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigIgnoredFacetValues(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacet(
    typing.TypedDict, total=False
):
    mergedFacetKey: str

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigMergedFacetValue(
    typing.TypedDict, total=False
):
    mergedValue: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttributeFacetConfigRerankConfig(
    typing.TypedDict, total=False
):
    facetValues: _list[str]
    rerankFacet: bool

@typing.type_check_only
class GoogleCloudRetailV2betaCollectUserEventRequest(typing.TypedDict, total=False):
    ets: str
    prebuiltRule: str
    rawJson: str
    uri: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailV2betaColorInfo(typing.TypedDict, total=False):
    colorFamilies: _list[str]
    colors: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponse(typing.TypedDict, total=False):
    attributeResults: dict[str, typing.Any]
    attributionToken: str
    completionResults: _list[
        GoogleCloudRetailV2betaCompleteQueryResponseCompletionResult
    ]
    recentSearchResults: _list[
        GoogleCloudRetailV2betaCompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseAttributeResult(
    typing.TypedDict, total=False
):
    suggestions: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseCompletionResult(
    typing.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    suggestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseRecentSearchResult(
    typing.TypedDict, total=False
):
    recentSearch: str

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionConfig(typing.TypedDict, total=False):
    allowlistInputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    autoLearning: bool
    denylistInputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    lastAllowlistImportOperation: str
    lastDenylistImportOperation: str
    lastSuggestionsImportOperation: str
    matchingOrder: str
    maxSuggestions: int
    minPrefixLength: int
    name: str
    suggestionsInputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionDataInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionDetail(typing.TypedDict, total=False):
    completionAttributionToken: str
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaCondition(typing.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudRetailV2betaConditionTimeRange]
    pageCategories: _list[str]
    queryTerms: _list[GoogleCloudRetailV2betaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudRetailV2betaConditionQueryTerm(typing.TypedDict, total=False):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaConditionTimeRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaControl(typing.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    displayName: str
    name: str
    rule: GoogleCloudRetailV2betaRule
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
class GoogleCloudRetailV2betaConversationalSearchCustomizationConfig(
    typing.TypedDict, total=False
):
    catalog: str
    intentClassificationConfig: GoogleCloudRetailV2betaIntentClassificationConfig
    retailerDisplayName: str

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchRequest(typing.TypedDict, total=False):
    branch: str
    conversationId: str
    conversationalFilteringSpec: (
        GoogleCloudRetailV2betaConversationalSearchRequestConversationalFilteringSpec
    )
    pageCategories: _list[str]
    query: str
    safetySettings: _list[GoogleCloudRetailV2betaSafetySetting]
    searchParams: GoogleCloudRetailV2betaConversationalSearchRequestSearchParams
    userInfo: GoogleCloudRetailV2betaUserInfo
    userLabels: dict[str, typing.Any]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchRequestConversationalFilteringSpec(
    typing.TypedDict, total=False
):
    conversationalFilteringMode: typing.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "ENABLED", "CONVERSATIONAL_FILTER_ONLY"
    ]
    enableConversationalFiltering: bool
    userAnswer: GoogleCloudRetailV2betaConversationalSearchRequestUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchRequestSearchParams(
    typing.TypedDict, total=False
):
    boostSpec: GoogleCloudRetailV2betaSearchRequestBoostSpec
    canonicalFilter: str
    filter: str
    sortBy: str

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchRequestUserAnswer(
    typing.TypedDict, total=False
):
    selectedAnswer: (
        GoogleCloudRetailV2betaConversationalSearchRequestUserAnswerSelectedAnswer
    )
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchRequestUserAnswerSelectedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchResponse(
    typing.TypedDict, total=False
):
    conversationId: str
    conversationalFilteringResult: (
        GoogleCloudRetailV2betaConversationalSearchResponseConversationalFilteringResult
    )
    conversationalTextResponse: str
    followupQuestion: (
        GoogleCloudRetailV2betaConversationalSearchResponseFollowupQuestion
    )
    refinedSearch: _list[
        GoogleCloudRetailV2betaConversationalSearchResponseRefinedSearch
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "STREAMING", "SUCCEEDED"]
    userQueryTypes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchResponseConversationalFilteringResult(
    typing.TypedDict, total=False
):
    additionalFilter: GoogleCloudRetailV2betaConversationalSearchResponseConversationalFilteringResultAdditionalFilter
    followupQuestion: (
        GoogleCloudRetailV2betaConversationalSearchResponseFollowupQuestion
    )

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchResponseConversationalFilteringResultAdditionalFilter(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchResponseFollowupQuestion(
    typing.TypedDict, total=False
):
    followupQuestion: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2betaConversationalSearchResponseFollowupQuestionSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchResponseFollowupQuestionSuggestedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaConversationalSearchResponseRefinedSearch(
    typing.TypedDict, total=False
):
    query: str

@typing.type_check_only
class GoogleCloudRetailV2betaCreateModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaCustomAttribute(typing.TypedDict, total=False):
    indexable: bool
    numbers: _list[float]
    searchable: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaDoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudRetailV2betaExperimentInfo(typing.TypedDict, total=False):
    experiment: str
    servingConfigExperiment: (
        GoogleCloudRetailV2betaExperimentInfoServingConfigExperiment
    )

@typing.type_check_only
class GoogleCloudRetailV2betaExperimentInfoServingConfigExperiment(
    typing.TypedDict, total=False
):
    experimentServingConfig: str
    originalServingConfig: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportAnalyticsMetricsRequest(
    typing.TypedDict, total=False
):
    filter: str
    outputConfig: GoogleCloudRetailV2betaOutputConfig

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
class GoogleCloudRetailV2betaExportProductsRequest(typing.TypedDict, total=False):
    filter: str
    outputConfig: GoogleCloudRetailV2betaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaExportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsRequest(typing.TypedDict, total=False):
    filter: str
    outputConfig: GoogleCloudRetailV2betaOutputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaFulfillmentInfo(typing.TypedDict, total=False):
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaGcsOutputResult(typing.TypedDict, total=False):
    outputUri: str

@typing.type_check_only
class GoogleCloudRetailV2betaGcsSource(typing.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaGenerativeQuestionConfig(typing.TypedDict, total=False):
    allowedInConversation: bool
    catalog: str
    exampleValues: _list[str]
    facet: str
    finalQuestion: str
    frequency: float
    generatedQuestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaGenerativeQuestionsFeatureConfig(
    typing.TypedDict, total=False
):
    catalog: str
    featureEnabled: bool
    minimumProducts: int

@typing.type_check_only
class GoogleCloudRetailV2betaGetDefaultBranchResponse(typing.TypedDict, total=False):
    branch: str
    note: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaImage(typing.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataRequest(typing.TypedDict, total=False):
    inputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    notificationPubsubTopic: str

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
class GoogleCloudRetailV2betaImportProductsRequest(typing.TypedDict, total=False):
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2betaProductInputConfig
    notificationPubsubTopic: str
    reconciliationMode: typing.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    requestId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportProductsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsRequest(typing.TypedDict, total=False):
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2betaUserEventInputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsResponse(typing.TypedDict, total=False):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    importSummary: GoogleCloudRetailV2betaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2betaIntentClassificationConfig(typing.TypedDict, total=False):
    blocklistKeywords: _list[str]
    disabledIntentTypes: _list[str]
    example: _list[GoogleCloudRetailV2betaIntentClassificationConfigExample]
    inlineSource: GoogleCloudRetailV2betaIntentClassificationConfigInlineSource
    modelPreamble: str

@typing.type_check_only
class GoogleCloudRetailV2betaIntentClassificationConfigExample(
    typing.TypedDict, total=False
):
    classifiedPositive: bool
    intentType: str
    query: str
    reason: str

@typing.type_check_only
class GoogleCloudRetailV2betaIntentClassificationConfigInlineForceIntent(
    typing.TypedDict, total=False
):
    intentType: str
    operation: typing.Literal["OPERATION_UNSPECIFIED", "EXACT_MATCH", "CONTAINS"]
    query: str

@typing.type_check_only
class GoogleCloudRetailV2betaIntentClassificationConfigInlineSource(
    typing.TypedDict, total=False
):
    inlineForceIntents: _list[
        GoogleCloudRetailV2betaIntentClassificationConfigInlineForceIntent
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaInterval(typing.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudRetailV2betaListCatalogsResponse(typing.TypedDict, total=False):
    catalogs: _list[GoogleCloudRetailV2betaCatalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListControlsResponse(typing.TypedDict, total=False):
    controls: _list[GoogleCloudRetailV2betaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListGenerativeQuestionConfigsResponse(
    typing.TypedDict, total=False
):
    generativeQuestionConfigs: _list[GoogleCloudRetailV2betaGenerativeQuestionConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaListModelsResponse(typing.TypedDict, total=False):
    models: _list[GoogleCloudRetailV2betaModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListProductsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    products: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaListServingConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudRetailV2betaServingConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaLocalInventory(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    fulfillmentTypes: _list[str]
    placeId: str
    priceInfo: GoogleCloudRetailV2betaPriceInfo

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterFeedFilter(typing.TypedDict, total=False):
    dataSourceId: str
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterLink(typing.TypedDict, total=False):
    branchId: str
    destinations: _list[str]
    feeds: _list[GoogleCloudRetailV2betaMerchantCenterFeedFilter]
    languageCode: str
    merchantCenterAccountId: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterLinkingConfig(typing.TypedDict, total=False):
    links: _list[GoogleCloudRetailV2betaMerchantCenterLink]

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
class GoogleCloudRetailV2betaOutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudRetailV2betaOutputConfigBigQueryDestination
    gcsDestination: GoogleCloudRetailV2betaOutputConfigGcsDestination

@typing.type_check_only
class GoogleCloudRetailV2betaOutputConfigBigQueryDestination(
    typing.TypedDict, total=False
):
    datasetId: str
    tableIdPrefix: str
    tableType: str

@typing.type_check_only
class GoogleCloudRetailV2betaOutputConfigGcsDestination(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaOutputResult(typing.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2betaBigQueryOutputResult]
    gcsResult: _list[GoogleCloudRetailV2betaGcsOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2betaPanelInfo(typing.TypedDict, total=False):
    attributionToken: str
    displayName: str
    panelId: str
    panelPosition: int
    productDetails: _list[GoogleCloudRetailV2betaProductDetail]
    totalPanels: int

@typing.type_check_only
class GoogleCloudRetailV2betaPauseModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPinControlMetadata(typing.TypedDict, total=False):
    allMatchedPins: dict[str, typing.Any]
    droppedPins: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaPinControlMetadataProductPins(
    typing.TypedDict, total=False
):
    productId: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaPredictRequest(typing.TypedDict, total=False):
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2betaUserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponse(typing.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudRetailV2betaPredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponsePredictionResult(
    typing.TypedDict, total=False
):
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaPriceInfo(typing.TypedDict, total=False):
    cost: float
    currencyCode: str
    originalPrice: float
    price: float
    priceEffectiveTime: str
    priceExpireTime: str
    priceRange: GoogleCloudRetailV2betaPriceInfoPriceRange

@typing.type_check_only
class GoogleCloudRetailV2betaPriceInfoPriceRange(typing.TypedDict, total=False):
    originalPrice: GoogleCloudRetailV2betaInterval
    price: GoogleCloudRetailV2betaInterval

@typing.type_check_only
class GoogleCloudRetailV2betaProduct(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    audience: GoogleCloudRetailV2betaAudience
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    availableQuantity: int
    availableTime: str
    brands: _list[str]
    categories: _list[str]
    collectionMemberIds: _list[str]
    colorInfo: GoogleCloudRetailV2betaColorInfo
    conditions: _list[str]
    description: str
    expireTime: str
    fulfillmentInfo: _list[GoogleCloudRetailV2betaFulfillmentInfo]
    gtin: str
    id: str
    images: _list[GoogleCloudRetailV2betaImage]
    languageCode: str
    localInventories: _list[GoogleCloudRetailV2betaLocalInventory]
    materials: _list[str]
    name: str
    patterns: _list[str]
    priceInfo: GoogleCloudRetailV2betaPriceInfo
    primaryProductId: str
    promotions: _list[GoogleCloudRetailV2betaPromotion]
    publishTime: str
    rating: GoogleCloudRetailV2betaRating
    retrievableFields: str
    sizes: _list[str]
    tags: _list[str]
    title: str
    ttl: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PRIMARY", "VARIANT", "COLLECTION"]
    uri: str
    variants: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaProductAttributeInterval(typing.TypedDict, total=False):
    interval: GoogleCloudRetailV2betaInterval
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaProductAttributeValue(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaProductDetail(typing.TypedDict, total=False):
    product: GoogleCloudRetailV2betaProduct
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2betaProductInlineSource(typing.TypedDict, total=False):
    products: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaProductInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource
    gcsSource: GoogleCloudRetailV2betaGcsSource
    productInlineSource: GoogleCloudRetailV2betaProductInlineSource

@typing.type_check_only
class GoogleCloudRetailV2betaProductLevelConfig(typing.TypedDict, total=False):
    ingestionProductType: str
    merchantCenterProductIdField: str

@typing.type_check_only
class GoogleCloudRetailV2betaPromotion(typing.TypedDict, total=False):
    promotionId: str

@typing.type_check_only
class GoogleCloudRetailV2betaPurchaseTransaction(typing.TypedDict, total=False):
    cost: float
    currencyCode: str
    id: str
    revenue: float
    tax: float

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsMetadata(typing.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeProductsResponse(typing.TypedDict, total=False):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsRequest(typing.TypedDict, total=False):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsResponse(typing.TypedDict, total=False):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRating(typing.TypedDict, total=False):
    averageRating: float
    ratingCount: int
    ratingHistogram: _list[int]

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsRequest(typing.TypedDict, total=False):
    userEventRejoinScope: typing.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsResponse(typing.TypedDict, total=False):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveCatalogAttributeRequest(
    typing.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveControlRequest(typing.TypedDict, total=False):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest(
    typing.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesRequest(
    typing.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaReplaceCatalogAttributeRequest(
    typing.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2betaCatalogAttribute
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaResumeModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRule(typing.TypedDict, total=False):
    boostAction: GoogleCloudRetailV2betaRuleBoostAction
    condition: GoogleCloudRetailV2betaCondition
    doNotAssociateAction: GoogleCloudRetailV2betaRuleDoNotAssociateAction
    filterAction: GoogleCloudRetailV2betaRuleFilterAction
    forceReturnFacetAction: GoogleCloudRetailV2betaRuleForceReturnFacetAction
    ignoreAction: GoogleCloudRetailV2betaRuleIgnoreAction
    onewaySynonymsAction: GoogleCloudRetailV2betaRuleOnewaySynonymsAction
    pinAction: GoogleCloudRetailV2betaRulePinAction
    redirectAction: GoogleCloudRetailV2betaRuleRedirectAction
    removeFacetAction: GoogleCloudRetailV2betaRuleRemoveFacetAction
    replacementAction: GoogleCloudRetailV2betaRuleReplacementAction
    twowaySynonymsAction: GoogleCloudRetailV2betaRuleTwowaySynonymsAction

@typing.type_check_only
class GoogleCloudRetailV2betaRuleBoostAction(typing.TypedDict, total=False):
    boost: float
    productsFilter: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleDoNotAssociateAction(typing.TypedDict, total=False):
    doNotAssociateTerms: _list[str]
    queryTerms: _list[str]
    terms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleFilterAction(typing.TypedDict, total=False):
    filter: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleForceReturnFacetAction(typing.TypedDict, total=False):
    facetPositionAdjustments: _list[
        GoogleCloudRetailV2betaRuleForceReturnFacetActionFacetPositionAdjustment
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleForceReturnFacetActionFacetPositionAdjustment(
    typing.TypedDict, total=False
):
    attributeName: str
    position: int

@typing.type_check_only
class GoogleCloudRetailV2betaRuleIgnoreAction(typing.TypedDict, total=False):
    ignoreTerms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleOnewaySynonymsAction(typing.TypedDict, total=False):
    onewayTerms: _list[str]
    queryTerms: _list[str]
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRulePinAction(typing.TypedDict, total=False):
    pinMap: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleRedirectAction(typing.TypedDict, total=False):
    redirectUri: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleRemoveFacetAction(typing.TypedDict, total=False):
    attributeNames: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleReplacementAction(typing.TypedDict, total=False):
    queryTerms: _list[str]
    replacementTerm: str
    term: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleTwowaySynonymsAction(typing.TypedDict, total=False):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaSafetySetting(typing.TypedDict, total=False):
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
class GoogleCloudRetailV2betaSearchRequest(typing.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    conversationalSearchSpec: (
        GoogleCloudRetailV2betaSearchRequestConversationalSearchSpec
    )
    dynamicFacetSpec: GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec
    entity: str
    facetSpecs: _list[GoogleCloudRetailV2betaSearchRequestFacetSpec]
    filter: str
    labels: dict[str, typing.Any]
    languageCode: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    personalizationSpec: GoogleCloudRetailV2betaSearchRequestPersonalizationSpec
    placeId: str
    query: str
    queryExpansionSpec: GoogleCloudRetailV2betaSearchRequestQueryExpansionSpec
    regionCode: str
    searchMode: typing.Literal[
        "SEARCH_MODE_UNSPECIFIED", "PRODUCT_SEARCH_ONLY", "FACETED_SEARCH_ONLY"
    ]
    spellCorrectionSpec: GoogleCloudRetailV2betaSearchRequestSpellCorrectionSpec
    tileNavigationSpec: GoogleCloudRetailV2betaSearchRequestTileNavigationSpec
    userAttributes: dict[str, typing.Any]
    userInfo: GoogleCloudRetailV2betaUserInfo
    variantRollupKeys: _list[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestBoostSpec(typing.TypedDict, total=False):
    conditionBoostSpecs: _list[
        GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec
    ]
    skipBoostSpecValidation: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec(
    typing.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestConversationalSearchSpec(
    typing.TypedDict, total=False
):
    conversationId: str
    followupConversationRequested: bool
    userAnswer: GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswer

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswer(
    typing.TypedDict, total=False
):
    selectedAnswer: GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswerSelectedAnswer
    textAnswer: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestConversationalSearchSpecUserAnswerSelectedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue
    productAttributeValues: _list[GoogleCloudRetailV2betaProductAttributeValue]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestFacetSpec(typing.TypedDict, total=False):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudRetailV2betaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestFacetSpecFacetKey(
    typing.TypedDict, total=False
):
    caseInsensitive: bool
    contains: _list[str]
    intervals: _list[GoogleCloudRetailV2betaInterval]
    key: str
    orderBy: str
    prefixes: _list[str]
    query: str
    restrictedValues: _list[str]
    returnMinMax: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestPersonalizationSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestQueryExpansionSpec(
    typing.TypedDict, total=False
):
    condition: typing.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestSpellCorrectionSpec(
    typing.TypedDict, total=False
):
    mode: typing.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestTileNavigationSpec(
    typing.TypedDict, total=False
):
    appliedTiles: _list[GoogleCloudRetailV2betaTile]
    tileNavigationRequested: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponse(typing.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    conversationalSearchResult: (
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResult
    )
    correctedQuery: str
    experimentInfo: _list[GoogleCloudRetailV2betaExperimentInfo]
    facets: _list[GoogleCloudRetailV2betaSearchResponseFacet]
    invalidConditionBoostSpecs: _list[
        GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec
    ]
    nextPageToken: str
    pinControlMetadata: GoogleCloudRetailV2betaPinControlMetadata
    queryExpansionInfo: GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudRetailV2betaSearchResponseSearchResult]
    tileNavigationResult: GoogleCloudRetailV2betaSearchResponseTileNavigationResult
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseConversationalSearchResult(
    typing.TypedDict, total=False
):
    additionalFilter: (
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResultAdditionalFilter
    )
    additionalFilters: _list[
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResultAdditionalFilter
    ]
    conversationId: str
    followupQuestion: str
    refinedQuery: str
    suggestedAnswers: _list[
        GoogleCloudRetailV2betaSearchResponseConversationalSearchResultSuggestedAnswer
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseConversationalSearchResultAdditionalFilter(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseConversationalSearchResultSuggestedAnswer(
    typing.TypedDict, total=False
):
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseFacet(typing.TypedDict, total=False):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudRetailV2betaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseFacetFacetValue(
    typing.TypedDict, total=False
):
    count: str
    interval: GoogleCloudRetailV2betaInterval
    maxValue: float
    minValue: float
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo(
    typing.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseSearchResult(typing.TypedDict, total=False):
    id: str
    matchingVariantCount: int
    matchingVariantFields: dict[str, typing.Any]
    modelScores: dict[str, typing.Any]
    personalLabels: _list[str]
    product: GoogleCloudRetailV2betaProduct
    variantRollupValues: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseTileNavigationResult(
    typing.TypedDict, total=False
):
    tiles: _list[GoogleCloudRetailV2betaTile]

@typing.type_check_only
class GoogleCloudRetailV2betaServingConfig(typing.TypedDict, total=False):
    boostControlIds: _list[str]
    displayName: str
    diversityLevel: str
    diversityType: typing.Literal[
        "DIVERSITY_TYPE_UNSPECIFIED", "RULE_BASED_DIVERSITY", "DATA_DRIVEN_DIVERSITY"
    ]
    doNotAssociateControlIds: _list[str]
    dynamicFacetSpec: GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec
    enableCategoryFilterLevel: str
    facetControlIds: _list[str]
    filterControlIds: _list[str]
    ignoreControlIds: _list[str]
    ignoreRecsDenylist: bool
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: GoogleCloudRetailV2betaSearchRequestPersonalizationSpec
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
class GoogleCloudRetailV2betaSetDefaultBranchRequest(typing.TypedDict, total=False):
    branchId: str
    force: bool
    note: str

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryRequest(typing.TypedDict, total=False):
    allowMissing: bool
    inventory: GoogleCloudRetailV2betaProduct
    setMask: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaStringList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaTile(typing.TypedDict, total=False):
    productAttributeInterval: GoogleCloudRetailV2betaProductAttributeInterval
    productAttributeValue: GoogleCloudRetailV2betaProductAttributeValue
    representativeProductId: str

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelMetadata(typing.TypedDict, total=False):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUpdateGenerativeQuestionConfigRequest(
    typing.TypedDict, total=False
):
    generativeQuestionConfig: GoogleCloudRetailV2betaGenerativeQuestionConfig
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEvent(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    attributionToken: str
    cartId: str
    completionDetail: GoogleCloudRetailV2betaCompletionDetail
    entity: str
    eventTime: str
    eventType: str
    experimentIds: _list[str]
    filter: str
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageViewId: str
    panels: _list[GoogleCloudRetailV2betaPanelInfo]
    productDetails: _list[GoogleCloudRetailV2betaProductDetail]
    purchaseTransaction: GoogleCloudRetailV2betaPurchaseTransaction
    referrerUri: str
    searchQuery: str
    sessionId: str
    uri: str
    userInfo: GoogleCloudRetailV2betaUserInfo
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventImportSummary(typing.TypedDict, total=False):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventInlineSource(typing.TypedDict, total=False):
    userEvents: _list[GoogleCloudRetailV2betaUserEvent]

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventInputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource
    gcsSource: GoogleCloudRetailV2betaGcsSource
    userEventInlineSource: GoogleCloudRetailV2betaUserEventInlineSource

@typing.type_check_only
class GoogleCloudRetailV2betaUserInfo(typing.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

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
