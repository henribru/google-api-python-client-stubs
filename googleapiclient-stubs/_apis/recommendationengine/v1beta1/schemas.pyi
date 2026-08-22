import typing

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaRejoinCatalogResponse(
    typing.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaTuningMetadata(
    typing.TypedDict, total=False
):
    recommendationModel: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaTuningResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1BigQuerySource(
    typing.TypedDict, total=False
):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1Catalog(typing.TypedDict, total=False):
    catalogItemLevelConfig: GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig
    defaultEventStoreId: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogInlineSource(
    typing.TypedDict, total=False
):
    catalogItems: _list[GoogleCloudRecommendationengineV1beta1CatalogItem]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogItem(typing.TypedDict, total=False):
    categoryHierarchies: _list[
        GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy
    ]
    description: str
    id: str
    itemAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    itemGroupId: str
    languageCode: str
    productMetadata: GoogleCloudRecommendationengineV1beta1ProductCatalogItem
    tags: _list[str]
    title: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy(
    typing.TypedDict, total=False
):
    categories: _list[str]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig(
    typing.TypedDict, total=False
):
    eventItemLevel: typing.Literal[
        "CATALOG_ITEM_LEVEL_UNSPECIFIED", "VARIANT", "MASTER"
    ]
    predictItemLevel: typing.Literal[
        "CATALOG_ITEM_LEVEL_UNSPECIFIED", "VARIANT", "MASTER"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequest(
    typing.TypedDict, total=False
):
    predictionApiKeyRegistration: (
        GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration
    )

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1EventDetail(typing.TypedDict, total=False):
    eventAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    experimentIds: _list[str]
    pageViewId: str
    recommendationToken: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1FeatureMap(typing.TypedDict, total=False):
    categoricalFeatures: dict[str, typing.Any]
    numericalFeatures: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1FeatureMapFloatList(
    typing.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1FeatureMapStringList(
    typing.TypedDict, total=False
):
    value: _list[str]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1GcsSource(typing.TypedDict, total=False):
    inputUris: _list[str]
    jsonSchema: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1Image(typing.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest(
    typing.TypedDict, total=False
):
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    inputConfig: GoogleCloudRecommendationengineV1beta1InputConfig
    requestId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportErrorsConfig(
    typing.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    failureCount: str
    operationName: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportUserEventsRequest(
    typing.TypedDict, total=False
):
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    inputConfig: GoogleCloudRecommendationengineV1beta1InputConfig
    requestId: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportUserEventsResponse(
    typing.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    importSummary: GoogleCloudRecommendationengineV1beta1UserEventImportSummary

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1InputConfig(typing.TypedDict, total=False):
    bigQuerySource: GoogleCloudRecommendationengineV1beta1BigQuerySource
    catalogInlineSource: GoogleCloudRecommendationengineV1beta1CatalogInlineSource
    gcsSource: GoogleCloudRecommendationengineV1beta1GcsSource
    userEventInlineSource: GoogleCloudRecommendationengineV1beta1UserEventInlineSource

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse(
    typing.TypedDict, total=False
):
    catalogItems: _list[GoogleCloudRecommendationengineV1beta1CatalogItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListCatalogsResponse(
    typing.TypedDict, total=False
):
    catalogs: _list[GoogleCloudRecommendationengineV1beta1Catalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    predictionApiKeyRegistrations: _list[
        GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListUserEventsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    userEvents: _list[GoogleCloudRecommendationengineV1beta1UserEvent]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictRequest(
    typing.TypedDict, total=False
):
    dryRun: bool
    filter: str
    labels: dict[str, typing.Any]
    pageSize: int
    pageToken: str
    params: dict[str, typing.Any]
    userEvent: GoogleCloudRecommendationengineV1beta1UserEvent

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictResponse(
    typing.TypedDict, total=False
):
    dryRun: bool
    itemsMissingInCatalog: _list[str]
    metadata: dict[str, typing.Any]
    nextPageToken: str
    recommendationToken: str
    results: _list[
        GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult(
    typing.TypedDict, total=False
):
    id: str
    itemMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration(
    typing.TypedDict, total=False
):
    apiKey: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductCatalogItem(
    typing.TypedDict, total=False
):
    availableQuantity: str
    canonicalProductUri: str
    costs: dict[str, typing.Any]
    currencyCode: str
    exactPrice: GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice
    images: _list[GoogleCloudRecommendationengineV1beta1Image]
    priceRange: GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange
    stockState: typing.Literal[
        "STOCK_STATE_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice(
    typing.TypedDict, total=False
):
    displayPrice: float
    originalPrice: float

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange(
    typing.TypedDict, total=False
):
    max: float
    min: float

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductDetail(
    typing.TypedDict, total=False
):
    availableQuantity: int
    currencyCode: str
    displayPrice: float
    id: str
    itemAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    originalPrice: float
    quantity: int
    stockState: typing.Literal[
        "STOCK_STATE_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductEventDetail(
    typing.TypedDict, total=False
):
    cartId: str
    listId: str
    pageCategories: _list[
        GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy
    ]
    productDetails: _list[GoogleCloudRecommendationengineV1beta1ProductDetail]
    purchaseTransaction: GoogleCloudRecommendationengineV1beta1PurchaseTransaction
    searchQuery: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurchaseTransaction(
    typing.TypedDict, total=False
):
    costs: dict[str, typing.Any]
    currencyCode: str
    id: str
    revenue: float
    taxes: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    operationName: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest(
    typing.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponse(
    typing.TypedDict, total=False
):
    purgedEventsCount: str
    userEventsSample: _list[GoogleCloudRecommendationengineV1beta1UserEvent]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequest(
    typing.TypedDict, total=False
):
    userEventRejoinScope: typing.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponse(
    typing.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEvent(typing.TypedDict, total=False):
    eventDetail: GoogleCloudRecommendationengineV1beta1EventDetail
    eventSource: typing.Literal[
        "EVENT_SOURCE_UNSPECIFIED", "AUTOML", "ECOMMERCE", "BATCH_UPLOAD"
    ]
    eventTime: str
    eventType: str
    productEventDetail: GoogleCloudRecommendationengineV1beta1ProductEventDetail
    userInfo: GoogleCloudRecommendationengineV1beta1UserInfo

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEventImportSummary(
    typing.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEventInlineSource(
    typing.TypedDict, total=False
):
    userEvents: _list[GoogleCloudRecommendationengineV1beta1UserEvent]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserInfo(typing.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str
    visitorId: str

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
