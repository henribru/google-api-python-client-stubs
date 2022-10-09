import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudRetailLoggingErrorContext(typing_extensions.TypedDict, total=False):
    httpRequest: GoogleCloudRetailLoggingHttpRequestContext
    reportLocation: GoogleCloudRetailLoggingSourceLocation

@typing.type_check_only
class GoogleCloudRetailLoggingErrorLog(typing_extensions.TypedDict, total=False):
    context: GoogleCloudRetailLoggingErrorContext
    importPayload: GoogleCloudRetailLoggingImportErrorContext
    message: str
    requestPayload: dict[str, typing.Any]
    responsePayload: dict[str, typing.Any]
    serviceContext: GoogleCloudRetailLoggingServiceContext
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudRetailLoggingHttpRequestContext(
    typing_extensions.TypedDict, total=False
):
    responseStatusCode: int

@typing.type_check_only
class GoogleCloudRetailLoggingImportErrorContext(
    typing_extensions.TypedDict, total=False
):
    catalogItem: str
    gcsPath: str
    inventoryActivity: str
    lineNumber: str
    operationName: str
    order: str
    place: str
    placeAsset: str
    placeProductPrice: str
    placeProductSettings: str
    product: str
    userEvent: str

@typing.type_check_only
class GoogleCloudRetailLoggingServiceContext(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudRetailLoggingSourceLocation(typing_extensions.TypedDict, total=False):
    functionName: str

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2AddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2ImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2ImportErrorsConfig(typing_extensions.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2ImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2ImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig
    importSummary: GoogleCloudRetailV2UserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2PurgeMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudRetailV2PurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2RemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2SetInventoryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2UserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQueryOutputResult(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCreateModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaExportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig
    outputResult: GoogleCloudRetailV2alphaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2alphaImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2alphaImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    transformedUserEventsMetadata: GoogleCloudRetailV2alphaTransformedUserEventsMetadata
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    importSummary: GoogleCloudRetailV2alphaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2alphaModel(typing_extensions.TypedDict, total=False):
    createTime: str
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    displayName: str
    filteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    name: str
    optimizationObjective: str
    pageOptimizationConfig: GoogleCloudRetailV2alphaModelPageOptimizationConfig
    periodicTuningState: typing_extensions.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2alphaModelServingConfigList]
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfig(
    typing_extensions.TypedDict, total=False
):
    pageOptimizationEventType: str
    panels: _list[GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel]
    restriction: typing_extensions.Literal[
        "RESTRICTION_UNSPECIFIED",
        "NO_RESTRICTION",
        "UNIQUE_SERVING_CONFIG_RESTRICTION",
        "UNIQUE_MODEL_RESTRICTION",
        "UNIQUE_MODEL_TYPE_RESTRICTION",
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate(
    typing_extensions.TypedDict, total=False
):
    servingConfigId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelPageOptimizationConfigPanel(
    typing_extensions.TypedDict, total=False
):
    candidates: _list[GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate]
    defaultCandidate: GoogleCloudRetailV2alphaModelPageOptimizationConfigCandidate
    displayName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaModelServingConfigList(
    typing_extensions.TypedDict, total=False
):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaOutputResult(typing_extensions.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2alphaBigQueryOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaTransformedUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    sourceEventsCount: str
    transformedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2betaCatalogAttribute

@typing.type_check_only
class GoogleCloudRetailV2betaAddControlRequest(
    typing_extensions.TypedDict, total=False
):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    addTime: str
    allowMissing: bool
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesRequest(
    typing_extensions.TypedDict, total=False
):
    addMask: str
    addTime: str
    allowMissing: bool
    localInventories: _list[GoogleCloudRetailV2betaLocalInventory]

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAttributesConfig(typing_extensions.TypedDict, total=False):
    attributeConfigLevel: typing_extensions.Literal[
        "ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED",
        "PRODUCT_LEVEL_ATTRIBUTE_CONFIG",
        "CATALOG_LEVEL_ATTRIBUTE_CONFIG",
    ]
    catalogAttributes: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2betaAudience(typing_extensions.TypedDict, total=False):
    ageGroups: _list[str]
    genders: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesRequest(
    typing_extensions.TypedDict, total=False
):
    attributeKeys: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBatchRemoveCatalogAttributesResponse(
    typing_extensions.TypedDict, total=False
):
    deletedCatalogAttributes: _list[str]
    resetCatalogAttributes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaBigQueryOutputResult(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaBigQuerySource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaCatalog(typing_extensions.TypedDict, total=False):
    displayName: str
    merchantCenterLinkingConfig: GoogleCloudRetailV2betaMerchantCenterLinkingConfig
    name: str
    productLevelConfig: GoogleCloudRetailV2betaProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2betaCatalogAttribute(typing_extensions.TypedDict, total=False):
    dynamicFacetableOption: typing_extensions.Literal[
        "DYNAMIC_FACETABLE_OPTION_UNSPECIFIED",
        "DYNAMIC_FACETABLE_ENABLED",
        "DYNAMIC_FACETABLE_DISABLED",
    ]
    exactSearchableOption: typing_extensions.Literal[
        "EXACT_SEARCHABLE_OPTION_UNSPECIFIED",
        "EXACT_SEARCHABLE_ENABLED",
        "EXACT_SEARCHABLE_DISABLED",
    ]
    inUse: bool
    indexableOption: typing_extensions.Literal[
        "INDEXABLE_OPTION_UNSPECIFIED", "INDEXABLE_ENABLED", "INDEXABLE_DISABLED"
    ]
    key: str
    recommendationsFilteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    searchableOption: typing_extensions.Literal[
        "SEARCHABLE_OPTION_UNSPECIFIED", "SEARCHABLE_ENABLED", "SEARCHABLE_DISABLED"
    ]
    type: typing_extensions.Literal["UNKNOWN", "TEXTUAL", "NUMERICAL"]

@typing.type_check_only
class GoogleCloudRetailV2betaColorInfo(typing_extensions.TypedDict, total=False):
    colorFamilies: _list[str]
    colors: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    completionResults: _list[
        GoogleCloudRetailV2betaCompleteQueryResponseCompletionResult
    ]
    recentSearchResults: _list[
        GoogleCloudRetailV2betaCompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseCompletionResult(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    suggestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaCompleteQueryResponseRecentSearchResult(
    typing_extensions.TypedDict, total=False
):
    recentSearch: str

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionConfig(typing_extensions.TypedDict, total=False):
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
class GoogleCloudRetailV2betaCompletionDataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2betaBigQuerySource

@typing.type_check_only
class GoogleCloudRetailV2betaCompletionDetail(typing_extensions.TypedDict, total=False):
    completionAttributionToken: str
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudRetailV2betaCondition(typing_extensions.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudRetailV2betaConditionTimeRange]
    queryTerms: _list[GoogleCloudRetailV2betaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudRetailV2betaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaControl(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    displayName: str
    facetSpec: GoogleCloudRetailV2betaSearchRequestFacetSpec
    name: str
    rule: GoogleCloudRetailV2betaRule
    searchSolutionUseCase: _list[str]
    solutionTypes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaCreateModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaCustomAttribute(typing_extensions.TypedDict, total=False):
    indexable: bool
    numbers: _list[float]
    searchable: bool
    text: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaExportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaExportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig
    outputResult: GoogleCloudRetailV2betaOutputResult

@typing.type_check_only
class GoogleCloudRetailV2betaFulfillmentInfo(typing_extensions.TypedDict, total=False):
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaGcsSource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaGetDefaultBranchResponse(
    typing_extensions.TypedDict, total=False
):
    branch: str
    note: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaImage(typing_extensions.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataRequest(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudRetailV2betaCompletionDataInputConfig
    notificationPubsubTopic: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudRetailV2betaImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    notificationPubsubTopic: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportProductsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2betaProductInputConfig
    notificationPubsubTopic: str
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    requestId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2betaUserEventInputConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    importSummary: GoogleCloudRetailV2betaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2betaInterval(typing_extensions.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudRetailV2betaListCatalogsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogs: _list[GoogleCloudRetailV2betaCatalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListControlsResponse(
    typing_extensions.TypedDict, total=False
):
    controls: _list[GoogleCloudRetailV2betaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudRetailV2betaModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2betaListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaListServingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudRetailV2betaServingConfig]

@typing.type_check_only
class GoogleCloudRetailV2betaLocalInventory(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    fulfillmentTypes: _list[str]
    placeId: str
    priceInfo: GoogleCloudRetailV2betaPriceInfo

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterFeedFilter(
    typing_extensions.TypedDict, total=False
):
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterLink(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    destinations: _list[str]
    feeds: _list[GoogleCloudRetailV2betaMerchantCenterFeedFilter]
    languageCode: str
    merchantCenterAccountId: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRetailV2betaMerchantCenterLinkingConfig(
    typing_extensions.TypedDict, total=False
):
    links: _list[GoogleCloudRetailV2betaMerchantCenterLink]

@typing.type_check_only
class GoogleCloudRetailV2betaModel(typing_extensions.TypedDict, total=False):
    createTime: str
    dataState: typing_extensions.Literal[
        "DATA_STATE_UNSPECIFIED", "DATA_OK", "DATA_ERROR"
    ]
    displayName: str
    filteringOption: typing_extensions.Literal[
        "RECOMMENDATIONS_FILTERING_OPTION_UNSPECIFIED",
        "RECOMMENDATIONS_FILTERING_DISABLED",
        "RECOMMENDATIONS_FILTERING_ENABLED",
    ]
    lastTuneTime: str
    name: str
    optimizationObjective: str
    periodicTuningState: typing_extensions.Literal[
        "PERIODIC_TUNING_STATE_UNSPECIFIED",
        "PERIODIC_TUNING_DISABLED",
        "ALL_TUNING_DISABLED",
        "PERIODIC_TUNING_ENABLED",
    ]
    servingConfigLists: _list[GoogleCloudRetailV2betaModelServingConfigList]
    servingState: typing_extensions.Literal[
        "SERVING_STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "TUNED"
    ]
    trainingState: typing_extensions.Literal[
        "TRAINING_STATE_UNSPECIFIED", "PAUSED", "TRAINING"
    ]
    tuningOperation: str
    type: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaModelServingConfigList(
    typing_extensions.TypedDict, total=False
):
    servingConfigIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaOutputResult(typing_extensions.TypedDict, total=False):
    bigqueryResult: _list[GoogleCloudRetailV2betaBigQueryOutputResult]

@typing.type_check_only
class GoogleCloudRetailV2betaPauseModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPredictRequest(typing_extensions.TypedDict, total=False):
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2betaUserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponse(typing_extensions.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudRetailV2betaPredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPredictResponsePredictionResult(
    typing_extensions.TypedDict, total=False
):
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2betaPriceInfo(typing_extensions.TypedDict, total=False):
    cost: float
    currencyCode: str
    originalPrice: float
    price: float
    priceEffectiveTime: str
    priceExpireTime: str
    priceRange: GoogleCloudRetailV2betaPriceInfoPriceRange

@typing.type_check_only
class GoogleCloudRetailV2betaPriceInfoPriceRange(
    typing_extensions.TypedDict, total=False
):
    originalPrice: GoogleCloudRetailV2betaInterval
    price: GoogleCloudRetailV2betaInterval

@typing.type_check_only
class GoogleCloudRetailV2betaProduct(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2betaProductDetail(typing_extensions.TypedDict, total=False):
    product: GoogleCloudRetailV2betaProduct
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2betaProductInlineSource(
    typing_extensions.TypedDict, total=False
):
    products: _list[GoogleCloudRetailV2betaProduct]

@typing.type_check_only
class GoogleCloudRetailV2betaProductInputConfig(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2betaProductLevelConfig(
    typing_extensions.TypedDict, total=False
):
    ingestionProductType: str
    merchantCenterProductIdField: str

@typing.type_check_only
class GoogleCloudRetailV2betaPromotion(typing_extensions.TypedDict, total=False):
    promotionId: str

@typing.type_check_only
class GoogleCloudRetailV2betaPurchaseTransaction(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currencyCode: str
    id: str
    revenue: float
    tax: float

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRating(typing_extensions.TypedDict, total=False):
    averageRating: float
    ratingCount: int
    ratingHistogram: _list[int]

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    userEventRejoinScope: typing_extensions.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveControlRequest(
    typing_extensions.TypedDict, total=False
):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaReplaceCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2betaCatalogAttribute
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2betaResumeModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRule(typing_extensions.TypedDict, total=False):
    boostAction: GoogleCloudRetailV2betaRuleBoostAction
    condition: GoogleCloudRetailV2betaCondition
    doNotAssociateAction: GoogleCloudRetailV2betaRuleDoNotAssociateAction
    filterAction: GoogleCloudRetailV2betaRuleFilterAction
    ignoreAction: GoogleCloudRetailV2betaRuleIgnoreAction
    onewaySynonymsAction: GoogleCloudRetailV2betaRuleOnewaySynonymsAction
    redirectAction: GoogleCloudRetailV2betaRuleRedirectAction
    replacementAction: GoogleCloudRetailV2betaRuleReplacementAction
    twowaySynonymsAction: GoogleCloudRetailV2betaRuleTwowaySynonymsAction

@typing.type_check_only
class GoogleCloudRetailV2betaRuleBoostAction(typing_extensions.TypedDict, total=False):
    boost: float
    productsFilter: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleDoNotAssociateAction(
    typing_extensions.TypedDict, total=False
):
    doNotAssociateTerms: _list[str]
    queryTerms: _list[str]
    terms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleFilterAction(typing_extensions.TypedDict, total=False):
    filter: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleIgnoreAction(typing_extensions.TypedDict, total=False):
    ignoreTerms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleOnewaySynonymsAction(
    typing_extensions.TypedDict, total=False
):
    onewayTerms: _list[str]
    queryTerms: _list[str]
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaRuleRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleReplacementAction(
    typing_extensions.TypedDict, total=False
):
    queryTerms: _list[str]
    replacementTerm: str
    term: str

@typing.type_check_only
class GoogleCloudRetailV2betaRuleTwowaySynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequest(typing_extensions.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2betaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    dynamicFacetSpec: GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec
    facetSpecs: _list[GoogleCloudRetailV2betaSearchRequestFacetSpec]
    filter: str
    labels: dict[str, typing.Any]
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    personalizationSpec: GoogleCloudRetailV2betaSearchRequestPersonalizationSpec
    query: str
    queryExpansionSpec: GoogleCloudRetailV2betaSearchRequestQueryExpansionSpec
    searchMode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED", "PRODUCT_SEARCH_ONLY", "FACETED_SEARCH_ONLY"
    ]
    spellCorrectionSpec: GoogleCloudRetailV2betaSearchRequestSpellCorrectionSpec
    userInfo: GoogleCloudRetailV2betaUserInfo
    variantRollupKeys: _list[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec
    ]
    skipBoostSpecValidation: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudRetailV2betaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2betaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponse(typing_extensions.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudRetailV2betaSearchResponseFacet]
    invalidConditionBoostSpecs: _list[
        GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec
    ]
    nextPageToken: str
    queryExpansionInfo: GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudRetailV2betaSearchResponseSearchResult]
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudRetailV2betaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudRetailV2betaInterval
    maxValue: float
    minValue: float
    value: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaSearchResponseSearchResult(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2betaServingConfig(typing_extensions.TypedDict, total=False):
    boostControlIds: _list[str]
    displayName: str
    diversityLevel: str
    diversityType: typing_extensions.Literal[
        "DIVERSITY_TYPE_UNSPECIFIED", "RULE_BASED_DIVERSITY", "DATA_DRIVEN_DIVERSITY"
    ]
    doNotAssociateControlIds: _list[str]
    dynamicFacetSpec: GoogleCloudRetailV2betaSearchRequestDynamicFacetSpec
    enableCategoryFilterLevel: str
    facetControlIds: _list[str]
    filterControlIds: _list[str]
    ignoreControlIds: _list[str]
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: GoogleCloudRetailV2betaSearchRequestPersonalizationSpec
    priceRerankingLevel: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionTypes: _list[str]
    twowaySynonymsControlIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2betaSetDefaultBranchRequest(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    force: bool
    note: str

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    inventory: GoogleCloudRetailV2betaProduct
    setMask: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaTuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserEvent(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudRetailV2betaUserEvent]

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventInputConfig(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserInfo(typing_extensions.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

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
