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
class GoogleCloudRetailV2ImportErrorsConfig(typing_extensions.TypedDict, total=False):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2ImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
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
class GoogleCloudRetailV2UserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2alphaBigQuerySource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudRetailV2alphaCatalog(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    productLevelConfig: GoogleCloudRetailV2alphaProductLevelConfig

@typing.type_check_only
class GoogleCloudRetailV2alphaCustomAttribute(typing_extensions.TypedDict, total=False):
    numbers: typing.List[float]
    text: typing.List[str]

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
class GoogleCloudRetailV2alphaGcsSource(typing_extensions.TypedDict, total=False):
    dataSchema: str
    inputUris: typing.List[str]

@typing.type_check_only
class GoogleCloudRetailV2alphaImage(typing_extensions.TypedDict, total=False):
    height: int
    uri: str
    width: int

@typing.type_check_only
class GoogleCloudRetailV2alphaImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2alphaImportProductsRequest(
    typing_extensions.TypedDict, total=False
):
    errorsConfig: GoogleCloudRetailV2alphaImportErrorsConfig
    inputConfig: GoogleCloudRetailV2alphaProductInputConfig
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
class GoogleCloudRetailV2alphaListCatalogsResponse(
    typing_extensions.TypedDict, total=False
):
    catalogs: typing.List[GoogleCloudRetailV2alphaCatalog]
    nextPageToken: str

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

@typing.type_check_only
class GoogleCloudRetailV2alphaProduct(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    availability: typing_extensions.Literal[
        "AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "PREORDER", "BACKORDER"
    ]
    availableQuantity: int
    availableTime: str
    categories: typing.List[str]
    description: str
    id: str
    images: typing.List[GoogleCloudRetailV2alphaImage]
    name: str
    priceInfo: GoogleCloudRetailV2alphaPriceInfo
    primaryProductId: str
    tags: typing.List[str]
    title: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PRIMARY", "VARIANT", "COLLECTION"
    ]
    uri: str

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
class GoogleCloudRetailV2alphaProductInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2alphaBigQuerySource
    gcsSource: GoogleCloudRetailV2alphaGcsSource
    productInlineSource: GoogleCloudRetailV2alphaProductInlineSource

@typing.type_check_only
class GoogleCloudRetailV2alphaProductLevelConfig(
    typing_extensions.TypedDict, total=False
):
    ingestionProductType: str
    merchantCenterProductIdField: str

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
class GoogleCloudRetailV2alphaUserEvent(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    attributionToken: str
    cartId: str
    eventTime: str
    eventType: str
    experimentIds: typing.List[str]
    pageCategories: typing.List[str]
    pageViewId: str
    productDetails: typing.List[GoogleCloudRetailV2alphaProductDetail]
    purchaseTransaction: GoogleCloudRetailV2alphaPurchaseTransaction
    referrerUri: str
    searchQuery: str
    uri: str
    userInfo: GoogleCloudRetailV2alphaUserInfo
    visitorId: str

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
class GoogleCloudRetailV2alphaUserEventInputConfig(
    typing_extensions.TypedDict, total=False
):
    bigQuerySource: GoogleCloudRetailV2alphaBigQuerySource
    gcsSource: GoogleCloudRetailV2alphaGcsSource
    userEventInlineSource: GoogleCloudRetailV2alphaUserEventInlineSource

@typing.type_check_only
class GoogleCloudRetailV2alphaUserInfo(typing_extensions.TypedDict, total=False):
    directUserRequest: bool
    ipAddress: str
    userAgent: str
    userId: str

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
class GoogleCloudRetailV2betaImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2betaImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
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
class GoogleCloudRetailV2betaUserEventImportSummary(
    typing_extensions.TypedDict, total=False
):
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2mainExportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2mainExportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2mainExportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2mainExportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2mainExportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2mainExportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2mainImportErrorsConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudRetailV2mainImportMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudRetailV2mainImportProductsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2mainImportErrorsConfig

@typing.type_check_only
class GoogleCloudRetailV2mainImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorSamples: typing.List[GoogleRpcStatus]
    errorsConfig: GoogleCloudRetailV2mainImportErrorsConfig
    importSummary: GoogleCloudRetailV2mainUserEventImportSummary

@typing.type_check_only
class GoogleCloudRetailV2mainPurgeMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2mainPurgeUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    purgedEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2mainRejoinUserEventsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudRetailV2mainRejoinUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    rejoinedUserEventsCount: str

@typing.type_check_only
class GoogleCloudRetailV2mainUserEventImportSummary(
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
