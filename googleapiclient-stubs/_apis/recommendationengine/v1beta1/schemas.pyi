import typing

import typing_extensions

class GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice(
    typing_extensions.TypedDict, total=False
):
    originalPrice: float
    displayPrice: float

class GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    catalogItems: typing.List[GoogleCloudRecommendationengineV1beta1CatalogItem]

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str
    error: GoogleRpcStatus
    done: bool

class GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    requestId: str
    inputConfig: GoogleCloudRecommendationengineV1beta1InputConfig
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig

class GoogleCloudRecommendationengineV1beta1CatalogInlineSource(
    typing_extensions.TypedDict, total=False
):
    catalogItems: typing.List[GoogleCloudRecommendationengineV1beta1CatalogItem]

class GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    predictionApiKeyRegistrations: typing.List[
        GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration
    ]

class GoogleCloudRecommendationengineV1beta1Image(
    typing_extensions.TypedDict, total=False
):
    uri: str
    width: int
    height: int

class GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult(
    typing_extensions.TypedDict, total=False
):
    id: str
    itemMetadata: typing.Dict[str, typing.Any]

class GoogleCloudRecommendationengineV1beta1FeatureMapFloatList(
    typing_extensions.TypedDict, total=False
):
    value: typing.List[float]

class GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

class GoogleCloudRecommendationengineV1alphaTuningMetadata(
    typing_extensions.TypedDict, total=False
):
    recommendationModel: str

class GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy(
    typing_extensions.TypedDict, total=False
):
    categories: typing.List[str]

class GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange(
    typing_extensions.TypedDict, total=False
):
    max: float
    min: float

class GoogleCloudRecommendationengineV1alphaRejoinCatalogResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

class GoogleCloudRecommendationengineV1beta1FeatureMapStringList(
    typing_extensions.TypedDict, total=False
):
    value: typing.List[str]

class GoogleCloudRecommendationengineV1alphaTuningResponse(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudRecommendationengineV1beta1ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    importSummary: GoogleCloudRecommendationengineV1beta1UserEventImportSummary
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig

class GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponse(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    errorSamples: typing.List[GoogleRpcStatus]

class GoogleCloudRecommendationengineV1beta1ImportMetadata(
    typing_extensions.TypedDict, total=False
):
    failureCount: str
    requestId: str
    createTime: str
    operationName: str
    successCount: str
    updateTime: str

class GoogleCloudRecommendationengineV1beta1FeatureMap(
    typing_extensions.TypedDict, total=False
):
    categoricalFeatures: typing.Dict[str, typing.Any]
    numericalFeatures: typing.Dict[str, typing.Any]

class GoogleCloudRecommendationengineV1beta1ProductCatalogItem(
    typing_extensions.TypedDict, total=False
):
    availableQuantity: str
    priceRange: GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange
    canonicalProductUri: str
    images: typing.List[GoogleCloudRecommendationengineV1beta1Image]
    stockState: typing_extensions.Literal[
        "STOCK_STATE_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    currencyCode: str
    exactPrice: GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice
    costs: typing.Dict[str, typing.Any]

class GoogleCloudRecommendationengineV1beta1ImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    inputConfig: GoogleCloudRecommendationengineV1beta1InputConfig
    requestId: str

class GoogleCloudRecommendationengineV1beta1UserEvent(
    typing_extensions.TypedDict, total=False
):
    eventType: str
    eventDetail: GoogleCloudRecommendationengineV1beta1EventDetail
    eventTime: str
    productEventDetail: GoogleCloudRecommendationengineV1beta1ProductEventDetail
    eventSource: typing_extensions.Literal[
        "EVENT_SOURCE_UNSPECIFIED", "AUTOML", "ECOMMERCE", "BATCH_UPLOAD"
    ]
    userInfo: GoogleCloudRecommendationengineV1beta1UserInfo

class GoogleCloudRecommendationengineV1beta1GcsSource(
    typing_extensions.TypedDict, total=False
):
    jsonSchema: str
    inputUris: typing.List[str]

class GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration(
    typing_extensions.TypedDict, total=False
):
    apiKey: str

class GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig(
    typing_extensions.TypedDict, total=False
):
    eventItemLevel: typing_extensions.Literal[
        "CATALOG_ITEM_LEVEL_UNSPECIFIED", "VARIANT", "MASTER"
    ]
    predictItemLevel: typing_extensions.Literal[
        "CATALOG_ITEM_LEVEL_UNSPECIFIED", "VARIANT", "MASTER"
    ]

class GoogleCloudRecommendationengineV1beta1UserEventInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: typing.List[GoogleCloudRecommendationengineV1beta1UserEvent]

class GoogleCloudRecommendationengineV1beta1ListCatalogsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogs: typing.List[GoogleCloudRecommendationengineV1beta1Catalog]
    nextPageToken: str

class GoogleCloudRecommendationengineV1beta1ProductEventDetail(
    typing_extensions.TypedDict, total=False
):
    purchaseTransaction: GoogleCloudRecommendationengineV1beta1PurchaseTransaction
    pageCategories: typing.List[
        GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy
    ]
    cartId: str
    productDetails: typing.List[GoogleCloudRecommendationengineV1beta1ProductDetail]
    searchQuery: str
    listId: str

class GoogleCloudRecommendationengineV1beta1PredictResponse(
    typing_extensions.TypedDict, total=False
):
    results: typing.List[
        GoogleCloudRecommendationengineV1beta1PredictResponsePredictionResult
    ]
    recommendationToken: str
    dryRun: bool
    itemsMissingInCatalog: typing.List[str]
    metadata: typing.Dict[str, typing.Any]
    nextPageToken: str

class GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    operationName: str

class GoogleCloudRecommendationengineV1beta1Catalog(
    typing_extensions.TypedDict, total=False
):
    name: str
    catalogItemLevelConfig: GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig
    displayName: str
    defaultEventStoreId: str

class GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    userEventRejoinScope: typing_extensions.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    userEventsSample: typing.List[GoogleCloudRecommendationengineV1beta1UserEvent]
    purgedEventsCount: str

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudRecommendationengineV1beta1InputConfig(
    typing_extensions.TypedDict, total=False
):
    gcsSource: GoogleCloudRecommendationengineV1beta1GcsSource
    catalogInlineSource: GoogleCloudRecommendationengineV1beta1CatalogInlineSource
    userEventInlineSource: GoogleCloudRecommendationengineV1beta1UserEventInlineSource
    bigQuerySource: GoogleCloudRecommendationengineV1beta1BigQuerySource

class GoogleCloudRecommendationengineV1beta1ListUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    userEvents: typing.List[GoogleCloudRecommendationengineV1beta1UserEvent]
    nextPageToken: str

class GoogleCloudRecommendationengineV1beta1ImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

class GoogleCloudRecommendationengineV1beta1PredictRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str
    labels: typing.Dict[str, typing.Any]
    params: typing.Dict[str, typing.Any]
    dryRun: bool
    userEvent: GoogleCloudRecommendationengineV1beta1UserEvent

class GoogleCloudRecommendationengineV1beta1UserInfo(
    typing_extensions.TypedDict, total=False
):
    directUserRequest: bool
    ipAddress: str
    userId: str
    visitorId: str
    userAgent: str

class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]
    contentType: str

class GoogleCloudRecommendationengineV1beta1EventDetail(
    typing_extensions.TypedDict, total=False
):
    uri: str
    pageViewId: str
    referrerUri: str
    experimentIds: typing.List[str]
    recommendationToken: str
    eventAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap

class GoogleCloudRecommendationengineV1beta1ProductDetail(
    typing_extensions.TypedDict, total=False
):
    id: str
    stockState: typing_extensions.Literal[
        "STOCK_STATE_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    displayPrice: float
    availableQuantity: int
    originalPrice: float
    itemAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    quantity: int
    currencyCode: str

class GoogleCloudRecommendationengineV1beta1CatalogItem(
    typing_extensions.TypedDict, total=False
):
    productMetadata: GoogleCloudRecommendationengineV1beta1ProductCatalogItem
    itemAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    languageCode: str
    title: str
    id: str
    description: str
    categoryHierarchies: typing.List[
        GoogleCloudRecommendationengineV1beta1CatalogItemCategoryHierarchy
    ]
    tags: typing.List[str]
    itemGroupId: str

class GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequest(
    typing_extensions.TypedDict, total=False
):
    predictionApiKeyRegistration: GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration

class GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadata(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudRecommendationengineV1beta1UserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    unjoinedEventsCount: str
    joinedEventsCount: str

class GoogleCloudRecommendationengineV1beta1PurchaseTransaction(
    typing_extensions.TypedDict, total=False
):
    costs: typing.Dict[str, typing.Any]
    currencyCode: str
    id: str
    revenue: float
    taxes: typing.Dict[str, typing.Any]

class GoogleCloudRecommendationengineV1beta1BigQuerySource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    tableId: str
    projectId: str
    datasetId: str
    gcsStagingDir: str

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[GoogleLongrunningOperation]
    nextPageToken: str
