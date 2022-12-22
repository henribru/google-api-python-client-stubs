import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleApiHttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1alphaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1alphaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaBigQuerySource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    datasetId: str
    gcsStagingDir: str
    partitionDate: GoogleTypeDate
    projectId: str
    tableId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCompletionInfo(
    typing_extensions.TypedDict, total=False
):
    selectedPosition: int
    selectedSuggestion: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaCustomAttribute(
    typing_extensions.TypedDict, total=False
):
    numbers: _list[float]
    text: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocument(
    typing_extensions.TypedDict, total=False
):
    id: str
    jsonData: str
    name: str
    parentDocumentId: str
    schemaId: str
    structData: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaDocumentInfo(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str
    promotionIds: _list[str]
    quantity: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaGcsSource(
    typing_extensions.TypedDict, total=False
):
    dataSchema: str
    inputUris: _list[str]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1betaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1betaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSource
    reconciliationMode: typing_extensions.Literal[
        "RECONCILIATION_MODE_UNSPECIFIED", "INCREMENTAL", "FULL"
    ]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1betaDocument]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportErrorConfig(
    typing_extensions.TypedDict, total=False
):
    gcsPrefix: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    failureCount: str
    successCount: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsRequest(
    typing_extensions.TypedDict, total=False
):
    bigquerySource: GoogleCloudDiscoveryengineV1betaBigQuerySource
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    gcsSource: GoogleCloudDiscoveryengineV1betaGcsSource
    inlineSource: GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSource

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsRequestInlineSource(
    typing_extensions.TypedDict, total=False
):
    userEvents: _list[GoogleCloudDiscoveryengineV1betaUserEvent]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaImportUserEventsResponse(
    typing_extensions.TypedDict, total=False
):
    errorConfig: GoogleCloudDiscoveryengineV1betaImportErrorConfig
    errorSamples: _list[GoogleRpcStatus]
    joinedEventsCount: str
    unjoinedEventsCount: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaListDocumentsResponse(
    typing_extensions.TypedDict, total=False
):
    documents: _list[GoogleCloudDiscoveryengineV1betaDocument]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaMediaInfo(
    typing_extensions.TypedDict, total=False
):
    mediaProgressDuration: str
    mediaProgressPercentage: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPageInfo(
    typing_extensions.TypedDict, total=False
):
    pageCategory: str
    pageviewId: str
    referrerUri: str
    uri: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaPanelInfo(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    panelId: str
    panelPosition: int
    totalPanels: int

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    params: dict[str, typing.Any]
    userEvent: GoogleCloudDiscoveryengineV1betaUserEvent
    userLabels: dict[str, typing.Any]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendResponse(
    typing_extensions.TypedDict, total=False
):
    attributionToken: str
    missingIds: _list[str]
    results: _list[
        GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResult
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaRecommendResponseRecommendationResult(
    typing_extensions.TypedDict, total=False
):
    document: GoogleCloudDiscoveryengineV1betaDocument
    id: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaSearchInfo(
    typing_extensions.TypedDict, total=False
):
    offset: int
    orderBy: str
    searchQuery: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaTransactionInfo(
    typing_extensions.TypedDict, total=False
):
    cost: float
    currency: str
    discountValue: float
    tax: float
    transactionId: str
    value: float

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserEvent(
    typing_extensions.TypedDict, total=False
):
    attributes: dict[str, typing.Any]
    attributionToken: str
    completionInfo: GoogleCloudDiscoveryengineV1betaCompletionInfo
    directUserRequest: bool
    documents: _list[GoogleCloudDiscoveryengineV1betaDocumentInfo]
    eventTime: str
    eventType: str
    filter: str
    mediaInfo: GoogleCloudDiscoveryengineV1betaMediaInfo
    pageInfo: GoogleCloudDiscoveryengineV1betaPageInfo
    panel: GoogleCloudDiscoveryengineV1betaPanelInfo
    promotionIds: _list[str]
    searchInfo: GoogleCloudDiscoveryengineV1betaSearchInfo
    sessionId: str
    tagIds: _list[str]
    transactionInfo: GoogleCloudDiscoveryengineV1betaTransactionInfo
    userInfo: GoogleCloudDiscoveryengineV1betaUserInfo
    userPseudoId: str

@typing.type_check_only
class GoogleCloudDiscoveryengineV1betaUserInfo(
    typing_extensions.TypedDict, total=False
):
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
