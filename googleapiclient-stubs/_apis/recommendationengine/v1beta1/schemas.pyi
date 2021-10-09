import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaRejoinCatalogMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaRejoinCatalogResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaTuningMetadata(
    typing_extensions.TypedDict, total=False
):
    recommendationModel: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1alphaTuningResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1BigQuerySource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1Catalog(
    typing_extensions.TypedDict, total=False
):
    catalogItemLevelConfig: GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig
    defaultEventStoreId: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogInlineSource(
    typing_extensions.TypedDict, total=False
):
    catalogItems: _list[GoogleCloudRecommendationengineV1beta1CatalogItem]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogItem(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    categories: _list[str]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CatalogItemLevelConfig(
    typing_extensions.TypedDict, total=False
):
    eventItemLevel: typing_extensions.Literal[
        "CATALOG_ITEM_LEVEL_UNSPECIFIED", "VARIANT", "MASTER"
    ]
    predictItemLevel: typing_extensions.Literal[
        "CATALOG_ITEM_LEVEL_UNSPECIFIED", "VARIANT", "MASTER"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1CreatePredictionApiKeyRegistrationRequest(
    typing_extensions.TypedDict, total=False
):
    predictionApiKeyRegistration: GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1EventDetail(
    typing_extensions.TypedDict, total=False
):
    eventAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    experimentIds: _list[str]
    pageViewId: str
    recommendationToken: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1FeatureMap(
    typing_extensions.TypedDict, total=False
):
    categoricalFeatures: dict[str, typing.Any]
    numericalFeatures: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1FeatureMapFloatList(
    typing_extensions.TypedDict, total=False
):
    value: _list[float]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1FeatureMapStringList(
    typing_extensions.TypedDict, total=False
):
    value: _list[str]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1GcsSource(
    typing_extensions.TypedDict, total=False
):
    inputUris: _list[str]
    jsonSchema: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1Image(
    typing_extensions.TypedDict, total=False
):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportCatalogItemsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    inputConfig: GoogleCloudRecommendationengineV1beta1InputConfig
    requestId: str
    updateMask: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportCatalogItemsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    operationName: str
    requestId: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    inputConfig: GoogleCloudRecommendationengineV1beta1InputConfig
    requestId: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: _list[GoogleRpcStatus]
    errorsConfig: GoogleCloudRecommendationengineV1beta1ImportErrorsConfig
    importSummary: GoogleCloudRecommendationengineV1beta1UserEventImportSummary

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1InputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRecommendationengineV1beta1BigQuerySource
    catalogInlineSource: GoogleCloudRecommendationengineV1beta1CatalogInlineSource
    gcsSource: GoogleCloudRecommendationengineV1beta1GcsSource
    userEventInlineSource: GoogleCloudRecommendationengineV1beta1UserEventInlineSource

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListCatalogItemsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogItems: _list[GoogleCloudRecommendationengineV1beta1CatalogItem]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListCatalogsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogs: _list[GoogleCloudRecommendationengineV1beta1Catalog]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListPredictionApiKeyRegistrationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    predictionApiKeyRegistrations: _list[
        GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ListUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userEvents: _list[GoogleCloudRecommendationengineV1beta1UserEvent]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictRequest(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    id: str
    itemMetadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PredictionApiKeyRegistration(
    typing_extensions.TypedDict, total=False
):
    apiKey: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductCatalogItem(
    typing_extensions.TypedDict, total=False
):
    availableQuantity: str
    canonicalProductUri: str
    costs: dict[str, typing.Any]
    currencyCode: str
    exactPrice: GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice
    images: _list[GoogleCloudRecommendationengineV1beta1Image]
    priceRange: GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange
    stockState: typing_extensions.Literal[
        "STOCK_STATE_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductCatalogItemExactPrice(
    typing_extensions.TypedDict, total=False
):
    displayPrice: float
    originalPrice: float

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductCatalogItemPriceRange(
    typing_extensions.TypedDict, total=False
):
    max: float
    min: float

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductDetail(
    typing_extensions.TypedDict, total=False
):
    availableQuantity: int
    currencyCode: str
    displayPrice: float
    id: str
    itemAttributes: GoogleCloudRecommendationengineV1beta1FeatureMap
    originalPrice: float
    quantity: int
    stockState: typing_extensions.Literal[
        "STOCK_STATE_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1ProductEventDetail(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    costs: dict[str, typing.Any]
    currencyCode: str
    id: str
    revenue: float
    taxes: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurgeUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    operationName: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurgeUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    force: bool

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str
    userEventsSample: _list[GoogleCloudRecommendationengineV1beta1UserEvent]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1RejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1RejoinUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    userEventRejoinScope: typing_extensions.Literal[
        "USER_EVENT_REJOIN_SCOPE_UNSPECIFIED", "JOINED_EVENTS", "UNJOINED_EVENTS"
    ]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1RejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEvent(
    typing_extensions.TypedDict, total=False
):
    eventDetail: GoogleCloudRecommendationengineV1beta1EventDetail
    eventSource: typing_extensions.Literal[
        "EVENT_SOURCE_UNSPECIFIED", "AUTOML", "ECOMMERCE", "BATCH_UPLOAD"
    ]
    eventTime: str
    eventType: str
    productEventDetail: GoogleCloudRecommendationengineV1beta1ProductEventDetail
    userInfo: GoogleCloudRecommendationengineV1beta1UserInfo

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserEventInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudRecommendationengineV1beta1UserEvent]

@typing.type_check_only
class GoogleCloudRecommendationengineV1beta1UserInfo(
    typing_extensions.TypedDict, total=False
):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str
    visitorId: str

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
