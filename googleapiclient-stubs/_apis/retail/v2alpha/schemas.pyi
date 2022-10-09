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
class GoogleCloudRetailV2alphaAddCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2alphaCatalogAttribute

@typing.type_check_only
class GoogleCloudRetailV2alphaAddControlRequest(
    typing_extensions.TypedDict, total=False
):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    addTime: str
    allowMissing: bool
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesRequest(
    typing_extensions.TypedDict, total=False
):
    addMask: str
    addTime: str
    allowMissing: bool
    localInventories: _list[GoogleCloudRetailV2alphaLocalInventory]

@typing.type_check_only
class GoogleCloudRetailV2alphaAddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAttributesConfig(
    typing_extensions.TypedDict, total=False
):
    attributeConfigLevel: typing_extensions.Literal[
        "ATTRIBUTE_CONFIG_LEVEL_UNSPECIFIED",
        "PRODUCT_LEVEL_ATTRIBUTE_CONFIG",
        "CATALOG_LEVEL_ATTRIBUTE_CONFIG",
    ]
    catalogAttributes: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAudience(typing_extensions.TypedDict, total=False):
    ageGroups: _list[str]
    genders: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesRequest(
    typing_extensions.TypedDict, total=False
):
    attributeKeys: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesResponse(
    typing_extensions.TypedDict, total=False
):
    deletedCatalogAttributes: _list[str]
    resetCatalogAttributes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQueryOutputResult(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQuerySource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalog(typing_extensions.TypedDict, total=False):
    displayName: str
    merchantCenterLinkingConfig: GoogleCloudRetailV2alphaMerchantCenterLinkingConfig
    name: str
    productLevelConfig: GoogleCloudRetailV2alphaProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalogAttribute(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudRetailV2alphaColorInfo(typing_extensions.TypedDict, total=False):
    colorFamilies: _list[str]
    colors: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    completionResults: _list[
        GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult
    ]
    recentSearchResults: _list[
        GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    suggestion: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult(
    typing_extensions.TypedDict, total=False
):
    recentSearch: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCompletionConfig(
    typing_extensions.TypedDict, total=False
):
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
class GoogleCloudRetailV2alphaCompletionDataInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2alphaBigQuerySource

@typing.type_check_only
class GoogleCloudRetailV2alphaCompletionDetail(
    typing_extensions.TypedDict, total=False
):
    completionAttributionToken: str
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCondition(typing_extensions.TypedDict, total=False):
    activeTimeRange: _list[GoogleCloudRetailV2alphaConditionTimeRange]
    queryTerms: _list[GoogleCloudRetailV2alphaConditionQueryTerm]

@typing.type_check_only
class GoogleCloudRetailV2alphaConditionQueryTerm(
    typing_extensions.TypedDict, total=False
):
    fullMatch: bool
    value: str

@typing.type_check_only
class GoogleCloudRetailV2alphaConditionTimeRange(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaControl(typing_extensions.TypedDict, total=False):
    associatedServingConfigIds: _list[str]
    displayName: str
    facetSpec: GoogleCloudRetailV2alphaSearchRequestFacetSpec
    name: str
    rule: GoogleCloudRetailV2alphaRule
    searchSolutionUseCase: _list[str]
    solutionTypes: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCreateModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCustomAttribute(typing_extensions.TypedDict, total=False):
    indexable: bool
    numbers: _list[float]
    searchable: bool
    text: _list[str]

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
class GoogleCloudRetailV2alphaFulfillmentInfo(typing_extensions.TypedDict, total=False):
    placeIds: _list[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaGcsSource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaGetDefaultBranchResponse(
    typing_extensions.TypedDict, total=False
):
    branch: str
    note: str
    setTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImage(typing_extensions.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2alphaImportCompletionDataRequest(
    typing_extensions.TypedDict, total=False
):
    inputConfig: GoogleCloudRetailV2alphaCompletionDataInputConfig
    notificationPubsubTopic: str

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
class GoogleCloudRetailV2alphaImportProductsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2alphaProductInputConfig
    notificationPubsubTopic: str
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]
    requestId: str
    skipDefaultBranchProtection: bool
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2alphaUserEventInputConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    importSummary: GoogleCloudRetailV2alphaUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2alphaInterval(typing_extensions.TypedDict, total=False):
    exclusiveMaximum: float
    exclusiveMinimum: float
    maximum: float
    minimum: float

@typing.type_check_only
class GoogleCloudRetailV2alphaListCatalogsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogs: _list[GoogleCloudRetailV2alphaCatalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListControlsResponse(
    typing_extensions.TypedDict, total=False
):
    controls: _list[GoogleCloudRetailV2alphaControl]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListModelsResponse(
    typing_extensions.TypedDict, total=False
):
    models: _list[GoogleCloudRetailV2alphaModel]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: _list[GoogleCloudRetailV2alphaProduct]
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2alphaListServingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    servingConfigs: _list[GoogleCloudRetailV2alphaServingConfig]

@typing.type_check_only
class GoogleCloudRetailV2alphaLocalInventory(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    fulfillmentTypes: _list[str]
    placeId: str
    priceInfo: GoogleCloudRetailV2alphaPriceInfo

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterFeedFilter(
    typing_extensions.TypedDict, total=False
):
    primaryFeedId: str
    primaryFeedName: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterLink(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    destinations: _list[str]
    feeds: _list[GoogleCloudRetailV2alphaMerchantCenterFeedFilter]
    languageCode: str
    merchantCenterAccountId: str
    regionCode: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterLinkingConfig(
    typing_extensions.TypedDict, total=False
):
    links: _list[GoogleCloudRetailV2alphaMerchantCenterLink]

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
class GoogleCloudRetailV2alphaPauseModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictRequest(typing_extensions.TypedDict, total=False):
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2alphaUserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponse(typing_extensions.TypedDict, total=False):
    attributionToken: str
    missingIds: _list[str]
    results: _list[GoogleCloudRetailV2alphaPredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponsePredictionResult(
    typing_extensions.TypedDict, total=False
):
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRetailV2alphaPriceInfo(typing_extensions.TypedDict, total=False):
    cost: float
    currencyCode: str
    originalPrice: float
    price: float
    priceEffectiveTime: str
    priceExpireTime: str
    priceRange: GoogleCloudRetailV2alphaPriceInfoPriceRange

@typing.type_check_only
class GoogleCloudRetailV2alphaPriceInfoPriceRange(
    typing_extensions.TypedDict, total=False
):
    originalPrice: GoogleCloudRetailV2alphaInterval
    price: GoogleCloudRetailV2alphaInterval

@typing.type_check_only
class GoogleCloudRetailV2alphaProduct(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaProductDetail(typing_extensions.TypedDict, total=False):
    product: GoogleCloudRetailV2alphaProduct
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2alphaProductInlineSource(
    typing_extensions.TypedDict, total=False
):
    products: _list[GoogleCloudRetailV2alphaProduct]

@typing.type_check_only
class GoogleCloudRetailV2alphaProductInputConfig(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaProductLevelConfig(
    typing_extensions.TypedDict, total=False
):
    ingestionProductType: str
    merchantCenterProductIdField: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPromotion(typing_extensions.TypedDict, total=False):
    promotionId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaPurchaseTransaction(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currencyCode: str
    id: str
    revenue: float
    tax: float

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
class GoogleCloudRetailV2alphaPurgeProductsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeProductsResponse(
    typing_extensions.TypedDict, total=False
):
    purgeCount: str
    purgeSample: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRating(typing_extensions.TypedDict, total=False):
    averageRating: float
    ratingCount: int
    ratingHistogram: _list[int]

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    userEventRejoinScope: typing_extensions.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    key: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveControlRequest(
    typing_extensions.TypedDict, total=False
):
    controlId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: _list[str]
    removeTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaReplaceCatalogAttributeRequest(
    typing_extensions.TypedDict, total=False
):
    catalogAttribute: GoogleCloudRetailV2alphaCatalogAttribute
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2alphaResumeModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRule(typing_extensions.TypedDict, total=False):
    boostAction: GoogleCloudRetailV2alphaRuleBoostAction
    condition: GoogleCloudRetailV2alphaCondition
    doNotAssociateAction: GoogleCloudRetailV2alphaRuleDoNotAssociateAction
    filterAction: GoogleCloudRetailV2alphaRuleFilterAction
    ignoreAction: GoogleCloudRetailV2alphaRuleIgnoreAction
    onewaySynonymsAction: GoogleCloudRetailV2alphaRuleOnewaySynonymsAction
    redirectAction: GoogleCloudRetailV2alphaRuleRedirectAction
    replacementAction: GoogleCloudRetailV2alphaRuleReplacementAction
    twowaySynonymsAction: GoogleCloudRetailV2alphaRuleTwowaySynonymsAction

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleBoostAction(typing_extensions.TypedDict, total=False):
    boost: float
    productsFilter: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleDoNotAssociateAction(
    typing_extensions.TypedDict, total=False
):
    doNotAssociateTerms: _list[str]
    queryTerms: _list[str]
    terms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleFilterAction(
    typing_extensions.TypedDict, total=False
):
    filter: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleIgnoreAction(
    typing_extensions.TypedDict, total=False
):
    ignoreTerms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleOnewaySynonymsAction(
    typing_extensions.TypedDict, total=False
):
    onewayTerms: _list[str]
    queryTerms: _list[str]
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleRedirectAction(
    typing_extensions.TypedDict, total=False
):
    redirectUri: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleReplacementAction(
    typing_extensions.TypedDict, total=False
):
    queryTerms: _list[str]
    replacementTerm: str
    term: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRuleTwowaySynonymsAction(
    typing_extensions.TypedDict, total=False
):
    synonyms: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequest(typing_extensions.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2alphaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    dynamicFacetSpec: GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec
    facetSpecs: _list[GoogleCloudRetailV2alphaSearchRequestFacetSpec]
    filter: str
    labels: dict[str, typing.Any]
    offset: int
    orderBy: str
    pageCategories: _list[str]
    pageSize: int
    pageToken: str
    personalizationSpec: GoogleCloudRetailV2alphaSearchRequestPersonalizationSpec
    query: str
    queryExpansionSpec: GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec
    relevanceThreshold: typing_extensions.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "LOWEST"
    ]
    searchMode: typing_extensions.Literal[
        "SEARCH_MODE_UNSPECIFIED", "PRODUCT_SEARCH_ONLY", "FACETED_SEARCH_ONLY"
    ]
    spellCorrectionSpec: GoogleCloudRetailV2alphaSearchRequestSpellCorrectionSpec
    userInfo: GoogleCloudRetailV2alphaUserInfo
    variantRollupKeys: _list[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: _list[
        GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec
    ]
    skipBoostSpecValidation: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec(
    typing_extensions.TypedDict, total=False
):
    boost: float
    condition: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestFacetSpec(
    typing_extensions.TypedDict, total=False
):
    enableDynamicPosition: bool
    excludedFilterKeys: _list[str]
    facetKey: GoogleCloudRetailV2alphaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "AUTO", "DISABLED"]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestSpellCorrectionSpec(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "SUGGESTION_ONLY", "AUTO"]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponse(typing_extensions.TypedDict, total=False):
    appliedControls: _list[str]
    attributionToken: str
    correctedQuery: str
    facets: _list[GoogleCloudRetailV2alphaSearchResponseFacet]
    invalidConditionBoostSpecs: _list[
        GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec
    ]
    nextPageToken: str
    queryExpansionInfo: GoogleCloudRetailV2alphaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: _list[GoogleCloudRetailV2alphaSearchResponseSearchResult]
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: _list[GoogleCloudRetailV2alphaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudRetailV2alphaInterval
    maxValue: float
    minValue: float
    value: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseSearchResult(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaServingConfig(typing_extensions.TypedDict, total=False):
    boostControlIds: _list[str]
    displayName: str
    diversityLevel: str
    diversityType: typing_extensions.Literal[
        "DIVERSITY_TYPE_UNSPECIFIED", "RULE_BASED_DIVERSITY", "DATA_DRIVEN_DIVERSITY"
    ]
    doNotAssociateControlIds: _list[str]
    dynamicFacetSpec: GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec
    enableCategoryFilterLevel: str
    facetControlIds: _list[str]
    filterControlIds: _list[str]
    ignoreControlIds: _list[str]
    modelId: str
    name: str
    onewaySynonymsControlIds: _list[str]
    personalizationSpec: GoogleCloudRetailV2alphaSearchRequestPersonalizationSpec
    priceRerankingLevel: str
    redirectControlIds: _list[str]
    replacementControlIds: _list[str]
    solutionTypes: _list[str]
    twowaySynonymsControlIds: _list[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaSetDefaultBranchRequest(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    force: bool
    note: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetInventoryRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    inventory: GoogleCloudRetailV2alphaProduct
    setMask: str
    setTime: str

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
class GoogleCloudRetailV2alphaTuneModelRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaTuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEvent(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudRetailV2alphaUserEvent]

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventInputConfig(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaUserInfo(typing_extensions.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaAddLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaBigQueryOutputResult(
    typing_extensions.TypedDict, total=False
):
    datasetId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2betaCreateModelMetadata(
    typing_extensions.TypedDict, total=False
):
    model: str

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
class GoogleCloudRetailV2betaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    importSummary: GoogleCloudRetailV2betaUserEventImportSummary

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
class GoogleCloudRetailV2betaPurgeMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaRemoveLocalInventoriesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

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
class GoogleCloudRetailV2betaTuneModelResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

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
