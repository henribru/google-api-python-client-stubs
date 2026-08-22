import typing

_list = list

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessBetweenFilter(typing.TypedDict, total=False):
    fromValue: GoogleAnalyticsAdminV1betaNumericValue
    toValue: GoogleAnalyticsAdminV1betaNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessDateRange(typing.TypedDict, total=False):
    endDate: str
    startDate: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessDimension(typing.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessDimensionHeader(typing.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessDimensionValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessFilter(typing.TypedDict, total=False):
    betweenFilter: GoogleAnalyticsAdminV1betaAccessBetweenFilter
    fieldName: str
    inListFilter: GoogleAnalyticsAdminV1betaAccessInListFilter
    numericFilter: GoogleAnalyticsAdminV1betaAccessNumericFilter
    stringFilter: GoogleAnalyticsAdminV1betaAccessStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessFilterExpression(typing.TypedDict, total=False):
    accessFilter: GoogleAnalyticsAdminV1betaAccessFilter
    andGroup: GoogleAnalyticsAdminV1betaAccessFilterExpressionList
    notExpression: GoogleAnalyticsAdminV1betaAccessFilterExpression
    orGroup: GoogleAnalyticsAdminV1betaAccessFilterExpressionList

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessFilterExpressionList(
    typing.TypedDict, total=False
):
    expressions: _list[GoogleAnalyticsAdminV1betaAccessFilterExpression]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessInListFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessMetric(typing.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessMetricHeader(typing.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessMetricValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessNumericFilter(typing.TypedDict, total=False):
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED",
        "EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
    ]
    value: GoogleAnalyticsAdminV1betaNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessOrderBy(typing.TypedDict, total=False):
    desc: bool
    dimension: GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy
    metric: GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy(
    typing.TypedDict, total=False
):
    dimensionName: str
    orderType: typing.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy(
    typing.TypedDict, total=False
):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessQuota(typing.TypedDict, total=False):
    concurrentRequests: GoogleAnalyticsAdminV1betaAccessQuotaStatus
    serverErrorsPerProjectPerHour: GoogleAnalyticsAdminV1betaAccessQuotaStatus
    tokensPerDay: GoogleAnalyticsAdminV1betaAccessQuotaStatus
    tokensPerHour: GoogleAnalyticsAdminV1betaAccessQuotaStatus
    tokensPerProjectPerHour: GoogleAnalyticsAdminV1betaAccessQuotaStatus

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessQuotaStatus(typing.TypedDict, total=False):
    consumed: int
    remaining: int

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessRow(typing.TypedDict, total=False):
    dimensionValues: _list[GoogleAnalyticsAdminV1betaAccessDimensionValue]
    metricValues: _list[GoogleAnalyticsAdminV1betaAccessMetricValue]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccessStringFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    matchType: typing.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
        "PARTIAL_REGEXP",
    ]
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccount(typing.TypedDict, total=False):
    createTime: str
    deleted: bool
    displayName: str
    gmpOrganization: str
    name: str
    regionCode: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccountSummary(typing.TypedDict, total=False):
    account: str
    displayName: str
    name: str
    propertySummaries: _list[GoogleAnalyticsAdminV1betaPropertySummary]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest(
    typing.TypedDict, total=False
):
    acknowledgement: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaChangeHistoryChange(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"]
    resource: str
    resourceAfterChange: (
        GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource
    )
    resourceBeforeChange: (
        GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource
    )

@typing.type_check_only
class GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource(
    typing.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1betaAccount
    conversionEvent: GoogleAnalyticsAdminV1betaConversionEvent
    dataRetentionSettings: GoogleAnalyticsAdminV1betaDataRetentionSettings
    dataStream: GoogleAnalyticsAdminV1betaDataStream
    firebaseLink: GoogleAnalyticsAdminV1betaFirebaseLink
    googleAdsLink: GoogleAnalyticsAdminV1betaGoogleAdsLink
    measurementProtocolSecret: GoogleAnalyticsAdminV1betaMeasurementProtocolSecret
    property: GoogleAnalyticsAdminV1betaProperty

@typing.type_check_only
class GoogleAnalyticsAdminV1betaChangeHistoryEvent(typing.TypedDict, total=False):
    actorType: typing.Literal["ACTOR_TYPE_UNSPECIFIED", "USER", "SYSTEM", "SUPPORT"]
    changeTime: str
    changes: _list[GoogleAnalyticsAdminV1betaChangeHistoryChange]
    changesFiltered: bool
    id: str
    userActorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaConversionEvent(typing.TypedDict, total=False):
    countingMethod: typing.Literal[
        "CONVERSION_COUNTING_METHOD_UNSPECIFIED", "ONCE_PER_EVENT", "ONCE_PER_SESSION"
    ]
    createTime: str
    custom: bool
    defaultConversionValue: (
        GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue
    )
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue(
    typing.TypedDict, total=False
):
    currencyCode: str
    value: float

@typing.type_check_only
class GoogleAnalyticsAdminV1betaCustomDimension(typing.TypedDict, total=False):
    description: str
    disallowAdsPersonalization: bool
    displayName: str
    name: str
    parameterName: str
    scope: typing.Literal["DIMENSION_SCOPE_UNSPECIFIED", "EVENT", "USER", "ITEM"]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaCustomMetric(typing.TypedDict, total=False):
    description: str
    displayName: str
    measurementUnit: typing.Literal[
        "MEASUREMENT_UNIT_UNSPECIFIED",
        "STANDARD",
        "CURRENCY",
        "FEET",
        "METERS",
        "KILOMETERS",
        "MILES",
        "MILLISECONDS",
        "SECONDS",
        "MINUTES",
        "HOURS",
    ]
    name: str
    parameterName: str
    restrictedMetricType: _list[
        typing.Literal[
            "RESTRICTED_METRIC_TYPE_UNSPECIFIED", "COST_DATA", "REVENUE_DATA"
        ]
    ]
    scope: typing.Literal["METRIC_SCOPE_UNSPECIFIED", "EVENT"]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataRetentionSettings(typing.TypedDict, total=False):
    eventDataRetention: typing.Literal[
        "RETENTION_DURATION_UNSPECIFIED",
        "TWO_MONTHS",
        "FOURTEEN_MONTHS",
        "TWENTY_SIX_MONTHS",
        "THIRTY_EIGHT_MONTHS",
        "FIFTY_MONTHS",
    ]
    name: str
    resetUserDataOnNewActivity: bool
    userDataRetention: typing.Literal[
        "RETENTION_DURATION_UNSPECIFIED",
        "TWO_MONTHS",
        "FOURTEEN_MONTHS",
        "TWENTY_SIX_MONTHS",
        "THIRTY_EIGHT_MONTHS",
        "FIFTY_MONTHS",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataSharingSettings(typing.TypedDict, total=False):
    name: str
    sharingWithGoogleAnySalesEnabled: bool
    sharingWithGoogleAssignedSalesEnabled: bool
    sharingWithGoogleProductsEnabled: bool
    sharingWithGoogleSupportEnabled: bool
    sharingWithOthersEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStream(typing.TypedDict, total=False):
    androidAppStreamData: GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData
    createTime: str
    displayName: str
    iosAppStreamData: GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData
    name: str
    type: typing.Literal[
        "DATA_STREAM_TYPE_UNSPECIFIED",
        "WEB_DATA_STREAM",
        "ANDROID_APP_DATA_STREAM",
        "IOS_APP_DATA_STREAM",
    ]
    updateTime: str
    webStreamData: GoogleAnalyticsAdminV1betaDataStreamWebStreamData

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData(
    typing.TypedDict, total=False
):
    firebaseAppId: str
    packageName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData(
    typing.TypedDict, total=False
):
    bundleId: str
    firebaseAppId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamWebStreamData(typing.TypedDict, total=False):
    defaultUri: str
    firebaseAppId: str
    measurementId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaFirebaseLink(typing.TypedDict, total=False):
    createTime: str
    name: str
    project: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaGoogleAdsLink(typing.TypedDict, total=False):
    adsPersonalizationEnabled: bool
    canManageClients: bool
    createTime: str
    creatorEmailAddress: str
    customerId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaKeyEvent(typing.TypedDict, total=False):
    countingMethod: typing.Literal[
        "COUNTING_METHOD_UNSPECIFIED", "ONCE_PER_EVENT", "ONCE_PER_SESSION"
    ]
    createTime: str
    custom: bool
    defaultValue: GoogleAnalyticsAdminV1betaKeyEventDefaultValue
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaKeyEventDefaultValue(typing.TypedDict, total=False):
    currencyCode: str
    numericValue: float

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListAccountSummariesResponse(
    typing.TypedDict, total=False
):
    accountSummaries: _list[GoogleAnalyticsAdminV1betaAccountSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[GoogleAnalyticsAdminV1betaAccount]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListConversionEventsResponse(
    typing.TypedDict, total=False
):
    conversionEvents: _list[GoogleAnalyticsAdminV1betaConversionEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListCustomDimensionsResponse(
    typing.TypedDict, total=False
):
    customDimensions: _list[GoogleAnalyticsAdminV1betaCustomDimension]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListCustomMetricsResponse(
    typing.TypedDict, total=False
):
    customMetrics: _list[GoogleAnalyticsAdminV1betaCustomMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListDataStreamsResponse(typing.TypedDict, total=False):
    dataStreams: _list[GoogleAnalyticsAdminV1betaDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListFirebaseLinksResponse(
    typing.TypedDict, total=False
):
    firebaseLinks: _list[GoogleAnalyticsAdminV1betaFirebaseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse(
    typing.TypedDict, total=False
):
    googleAdsLinks: _list[GoogleAnalyticsAdminV1betaGoogleAdsLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListKeyEventsResponse(typing.TypedDict, total=False):
    keyEvents: _list[GoogleAnalyticsAdminV1betaKeyEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse(
    typing.TypedDict, total=False
):
    measurementProtocolSecrets: _list[
        GoogleAnalyticsAdminV1betaMeasurementProtocolSecret
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListPropertiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    properties: _list[GoogleAnalyticsAdminV1betaProperty]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaMeasurementProtocolSecret(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    secretValue: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaNumericValue(typing.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProperty(typing.TypedDict, total=False):
    account: str
    createTime: str
    currencyCode: str
    deleteTime: str
    displayName: str
    expireTime: str
    industryCategory: typing.Literal[
        "INDUSTRY_CATEGORY_UNSPECIFIED",
        "AUTOMOTIVE",
        "BUSINESS_AND_INDUSTRIAL_MARKETS",
        "FINANCE",
        "HEALTHCARE",
        "TECHNOLOGY",
        "TRAVEL",
        "OTHER",
        "ARTS_AND_ENTERTAINMENT",
        "BEAUTY_AND_FITNESS",
        "BOOKS_AND_LITERATURE",
        "FOOD_AND_DRINK",
        "GAMES",
        "HOBBIES_AND_LEISURE",
        "HOME_AND_GARDEN",
        "INTERNET_AND_TELECOM",
        "LAW_AND_GOVERNMENT",
        "NEWS",
        "ONLINE_COMMUNITIES",
        "PEOPLE_AND_SOCIETY",
        "PETS_AND_ANIMALS",
        "REAL_ESTATE",
        "REFERENCE",
        "SCIENCE",
        "SPORTS",
        "JOBS_AND_EDUCATION",
        "SHOPPING",
    ]
    name: str
    parent: str
    propertyType: typing.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]
    serviceLevel: typing.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "GOOGLE_ANALYTICS_STANDARD", "GOOGLE_ANALYTICS_360"
    ]
    timeZone: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaPropertySummary(typing.TypedDict, total=False):
    canEdit: bool
    displayName: str
    parent: str
    property: str
    propertyType: typing.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest(
    typing.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1betaAccount
    redirectUri: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse(
    typing.TypedDict, total=False
):
    accountTicketId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaRunAccessReportRequest(typing.TypedDict, total=False):
    dateRanges: _list[GoogleAnalyticsAdminV1betaAccessDateRange]
    dimensionFilter: GoogleAnalyticsAdminV1betaAccessFilterExpression
    dimensions: _list[GoogleAnalyticsAdminV1betaAccessDimension]
    expandGroups: bool
    includeAllUsers: bool
    limit: str
    metricFilter: GoogleAnalyticsAdminV1betaAccessFilterExpression
    metrics: _list[GoogleAnalyticsAdminV1betaAccessMetric]
    offset: str
    orderBys: _list[GoogleAnalyticsAdminV1betaAccessOrderBy]
    returnEntityQuota: bool
    timeZone: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaRunAccessReportResponse(typing.TypedDict, total=False):
    dimensionHeaders: _list[GoogleAnalyticsAdminV1betaAccessDimensionHeader]
    metricHeaders: _list[GoogleAnalyticsAdminV1betaAccessMetricHeader]
    quota: GoogleAnalyticsAdminV1betaAccessQuota
    rowCount: int
    rows: _list[GoogleAnalyticsAdminV1betaAccessRow]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest(
    typing.TypedDict, total=False
):
    action: _list[
        typing.Literal["ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"]
    ]
    actorEmail: _list[str]
    earliestChangeTime: str
    latestChangeTime: str
    pageSize: int
    pageToken: str
    property: str
    resourceType: _list[
        typing.Literal[
            "CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED",
            "ACCOUNT",
            "PROPERTY",
            "FIREBASE_LINK",
            "GOOGLE_ADS_LINK",
            "GOOGLE_SIGNALS_SETTINGS",
            "CONVERSION_EVENT",
            "MEASUREMENT_PROTOCOL_SECRET",
            "CUSTOM_DIMENSION",
            "CUSTOM_METRIC",
            "DATA_RETENTION_SETTINGS",
            "DISPLAY_VIDEO_360_ADVERTISER_LINK",
            "DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL",
            "DATA_STREAM",
            "ATTRIBUTION_SETTINGS",
        ]
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse(
    typing.TypedDict, total=False
):
    changeHistoryEvents: _list[GoogleAnalyticsAdminV1betaChangeHistoryEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...
