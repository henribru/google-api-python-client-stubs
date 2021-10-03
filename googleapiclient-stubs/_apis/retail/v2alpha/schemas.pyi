import typing

import typing_extensions

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudRetailLoggingErrorContext(typing_extensions.TypedDict, total=False):
    httpRequest: GoogleCloudRetailLoggingHttpRequestContext
    reportLocation: GoogleCloudRetailLoggingSourceLocation

@typing.type_check_only
class GoogleCloudRetailLoggingErrorLog(typing_extensions.TypedDict, total=False):
    context: GoogleCloudRetailLoggingErrorContext
    importPayload: GoogleCloudRetailLoggingImportErrorContext
    message: str
    requestPayload: typing.Dict[str, typing.Any]
    responsePayload: typing.Dict[str, typing.Any]
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
    lineNumber: str
    operationName: str
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
class GoogleCloudRetailV2ImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]

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
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
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
class GoogleCloudRetailV2alphaAddFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    addTime: str
    allowMissing: bool
    placeIds: typing.List[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaAddFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaAudience(typing_extensions.TypedDict, total=False):
    ageGroups: typing.List[str]
    genders: typing.List[str]

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
class GoogleCloudRetailV2alphaColorInfo(typing_extensions.TypedDict, total=False):
    colorFamilies: typing.List[str]
    colors: typing.List[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    completionResults: typing.List[
        GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult
    ]
    recentSearchResults: typing.List[
        GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult
    ]

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseCompletionResult(
    typing_extensions.TypedDict, total=False
):
    attributes: typing.Dict[str, typing.Any]
    suggestion: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCompleteQueryResponseRecentSearchResult(
    typing_extensions.TypedDict, total=False
):
    recentSearch: str

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
class GoogleCloudRetailV2alphaCustomAttribute(typing_extensions.TypedDict, total=False):
    indexable: bool
    numbers: typing.List[float]
    searchable: bool
    text: typing.List[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaEnrollSolutionMetadata(
    typing_extensions.TypedDict, total=False
): ...

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
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2alphaExportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaFulfillmentInfo(typing_extensions.TypedDict, total=False):
    placeIds: typing.List[str]
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaGcsSource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    inputUris: typing.List[str]

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
    errorSamples: typing.List[GoogleRpcStatus]

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
    updateMask: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
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
    errorSamples: typing.List[GoogleRpcStatus]
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
    catalogs: typing.List[GoogleCloudRetailV2alphaCatalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRetailV2alphaListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: typing.List[GoogleCloudRetailV2alphaProduct]
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterLink(
    typing_extensions.TypedDict, total=False
):
    branchId: str
    destinations: typing.List[str]
    merchantCenterAccountId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaMerchantCenterLinkingConfig(
    typing_extensions.TypedDict, total=False
):
    links: typing.List[GoogleCloudRetailV2alphaMerchantCenterLink]

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictRequest(typing_extensions.TypedDict, total=False):
    filter: str
    labels: typing.Dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: typing.Dict[str, typing.Any]
    userEvent: GoogleCloudRetailV2alphaUserEvent
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponse(typing_extensions.TypedDict, total=False):
    attributionToken: str
    missingIds: typing.List[str]
    results: typing.List[GoogleCloudRetailV2alphaPredictResponsePredictionResult]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaPredictResponsePredictionResult(
    typing_extensions.TypedDict, total=False
):
    id: str
    metadata: typing.Dict[str, typing.Any]

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
class GoogleCloudRetailV2alphaProduct(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaProductDetail(typing_extensions.TypedDict, total=False):
    product: GoogleCloudRetailV2alphaProduct
    quantity: int

@typing.type_check_only
class GoogleCloudRetailV2alphaProductInlineSource(
    typing_extensions.TypedDict, total=False
):
    products: typing.List[GoogleCloudRetailV2alphaProduct]

@typing.type_check_only
class GoogleCloudRetailV2alphaProductInputConfig(typing.Dict[str, typing.Any]): ...

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
    ratingHistogram: typing.List[int]

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
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesRequest(
    typing_extensions.TypedDict, total=False
):
    allowMissing: bool
    placeIds: typing.List[str]
    removeTime: str
    type: str

@typing.type_check_only
class GoogleCloudRetailV2alphaRemoveFulfillmentPlacesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequest(typing_extensions.TypedDict, total=False):
    boostSpec: GoogleCloudRetailV2alphaSearchRequestBoostSpec
    branch: str
    canonicalFilter: str
    dynamicFacetSpec: GoogleCloudRetailV2alphaSearchRequestDynamicFacetSpec
    facetSpecs: typing.List[GoogleCloudRetailV2alphaSearchRequestFacetSpec]
    filter: str
    offset: int
    orderBy: str
    pageCategories: typing.List[str]
    pageSize: int
    pageToken: str
    query: str
    queryExpansionSpec: GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec
    relevanceThreshold: typing_extensions.Literal[
        "RELEVANCE_THRESHOLD_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "LOWEST"
    ]
    userInfo: GoogleCloudRetailV2alphaUserInfo
    variantRollupKeys: typing.List[str]
    visitorId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestBoostSpec(
    typing_extensions.TypedDict, total=False
):
    conditionBoostSpecs: typing.List[
        GoogleCloudRetailV2alphaSearchRequestBoostSpecConditionBoostSpec
    ]

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
    excludedFilterKeys: typing.List[str]
    facetKey: GoogleCloudRetailV2alphaSearchRequestFacetSpecFacetKey
    limit: int

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestFacetSpecFacetKey(
    typing_extensions.TypedDict, total=False
):
    contains: typing.List[str]
    intervals: typing.List[GoogleCloudRetailV2alphaInterval]
    key: str
    orderBy: str
    prefixes: typing.List[str]
    query: str
    restrictedValues: typing.List[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchRequestQueryExpansionSpec(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal["CONDITION_UNSPECIFIED", "DISABLED", "AUTO"]
    pinUnexpandedResults: bool

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponse(typing_extensions.TypedDict, total=False):
    attributionToken: str
    correctedQuery: str
    facets: typing.List[GoogleCloudRetailV2alphaSearchResponseFacet]
    nextPageToken: str
    queryExpansionInfo: GoogleCloudRetailV2alphaSearchResponseQueryExpansionInfo
    redirectUri: str
    results: typing.List[GoogleCloudRetailV2alphaSearchResponseSearchResult]
    totalSize: int

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseFacet(
    typing_extensions.TypedDict, total=False
):
    dynamicFacet: bool
    key: str
    values: typing.List[GoogleCloudRetailV2alphaSearchResponseFacetFacetValue]

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseFacetFacetValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    interval: GoogleCloudRetailV2alphaInterval
    value: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseQueryExpansionInfo(
    typing_extensions.TypedDict, total=False
):
    expandedQuery: bool
    pinnedResultCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaSearchResponseSearchResult(
    typing.Dict[str, typing.Any]
): ...

@typing.type_check_only
class GoogleCloudRetailV2alphaSetDefaultBranchRequest(
    typing_extensions.TypedDict, total=False
):
    branchId: str
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
class GoogleCloudRetailV2alphaUserEvent(typing.Dict[str, typing.Any]): ...

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
    userEvents: typing.List[GoogleCloudRetailV2alphaUserEvent]

@typing.type_check_only
class GoogleCloudRetailV2alphaUserEventInputConfig(typing.Dict[str, typing.Any]): ...

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
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaExportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportCompletionDataResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]

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
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2betaImportErrorsConfig
    importSummary: GoogleCloudRetailV2betaUserEventImportSummary

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
class GoogleCloudRetailV2betaSetInventoryMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2betaSetInventoryResponse(
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
    operations: typing.List[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int
