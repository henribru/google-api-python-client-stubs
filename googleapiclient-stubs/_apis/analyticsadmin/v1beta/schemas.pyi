import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccount(typing_extensions.TypedDict, total=False):
    createTime: str
    deleted: bool
    displayName: str
    name: str
    regionCode: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAccountSummary(
    typing_extensions.TypedDict, total=False
):
    account: str
    displayName: str
    name: str
    propertySummaries: _list[GoogleAnalyticsAdminV1betaPropertySummary]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest(
    typing_extensions.TypedDict, total=False
):
    acknowledgement: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaChangeHistoryChange(
    typing_extensions.TypedDict, total=False
):
    action: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"
    ]
    resource: str
    resourceAfterChange: GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource
    resourceBeforeChange: GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource

@typing.type_check_only
class GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource(
    typing_extensions.TypedDict, total=False
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
class GoogleAnalyticsAdminV1betaChangeHistoryEvent(
    typing_extensions.TypedDict, total=False
):
    actorType: typing_extensions.Literal[
        "ACTOR_TYPE_UNSPECIFIED", "USER", "SYSTEM", "SUPPORT"
    ]
    changeTime: str
    changes: _list[GoogleAnalyticsAdminV1betaChangeHistoryChange]
    changesFiltered: bool
    id: str
    userActorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaConversionEvent(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    custom: bool
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaCustomDimension(
    typing_extensions.TypedDict, total=False
):
    description: str
    disallowAdsPersonalization: bool
    displayName: str
    name: str
    parameterName: str
    scope: typing_extensions.Literal["DIMENSION_SCOPE_UNSPECIFIED", "EVENT", "USER"]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaCustomMetric(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    measurementUnit: typing_extensions.Literal[
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
    restrictedMetricType: _list[str]
    scope: typing_extensions.Literal["METRIC_SCOPE_UNSPECIFIED", "EVENT"]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataRetentionSettings(
    typing_extensions.TypedDict, total=False
):
    eventDataRetention: typing_extensions.Literal[
        "RETENTION_DURATION_UNSPECIFIED",
        "TWO_MONTHS",
        "FOURTEEN_MONTHS",
        "TWENTY_SIX_MONTHS",
        "THIRTY_EIGHT_MONTHS",
        "FIFTY_MONTHS",
    ]
    name: str
    resetUserDataOnNewActivity: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataSharingSettings(
    typing_extensions.TypedDict, total=False
):
    name: str
    sharingWithGoogleAnySalesEnabled: bool
    sharingWithGoogleAssignedSalesEnabled: bool
    sharingWithGoogleProductsEnabled: bool
    sharingWithGoogleSupportEnabled: bool
    sharingWithOthersEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStream(typing_extensions.TypedDict, total=False):
    androidAppStreamData: GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData
    createTime: str
    displayName: str
    iosAppStreamData: GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData
    name: str
    type: typing_extensions.Literal[
        "DATA_STREAM_TYPE_UNSPECIFIED",
        "WEB_DATA_STREAM",
        "ANDROID_APP_DATA_STREAM",
        "IOS_APP_DATA_STREAM",
    ]
    updateTime: str
    webStreamData: GoogleAnalyticsAdminV1betaDataStreamWebStreamData

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData(
    typing_extensions.TypedDict, total=False
):
    firebaseAppId: str
    packageName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData(
    typing_extensions.TypedDict, total=False
):
    bundleId: str
    firebaseAppId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamWebStreamData(
    typing_extensions.TypedDict, total=False
):
    defaultUri: str
    firebaseAppId: str
    measurementId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaFirebaseLink(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    project: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaGoogleAdsLink(typing_extensions.TypedDict, total=False):
    adsPersonalizationEnabled: bool
    canManageClients: bool
    createTime: str
    creatorEmailAddress: str
    customerId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListAccountSummariesResponse(
    typing_extensions.TypedDict, total=False
):
    accountSummaries: _list[GoogleAnalyticsAdminV1betaAccountSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accounts: _list[GoogleAnalyticsAdminV1betaAccount]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListConversionEventsResponse(
    typing_extensions.TypedDict, total=False
):
    conversionEvents: _list[GoogleAnalyticsAdminV1betaConversionEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListCustomDimensionsResponse(
    typing_extensions.TypedDict, total=False
):
    customDimensions: _list[GoogleAnalyticsAdminV1betaCustomDimension]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListCustomMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    customMetrics: _list[GoogleAnalyticsAdminV1betaCustomMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    dataStreams: _list[GoogleAnalyticsAdminV1betaDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListFirebaseLinksResponse(
    typing_extensions.TypedDict, total=False
):
    firebaseLinks: _list[GoogleAnalyticsAdminV1betaFirebaseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse(
    typing_extensions.TypedDict, total=False
):
    googleAdsLinks: _list[GoogleAnalyticsAdminV1betaGoogleAdsLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse(
    typing_extensions.TypedDict, total=False
):
    measurementProtocolSecrets: _list[
        GoogleAnalyticsAdminV1betaMeasurementProtocolSecret
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListPropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    properties: _list[GoogleAnalyticsAdminV1betaProperty]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaMeasurementProtocolSecret(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    secretValue: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProperty(typing_extensions.TypedDict, total=False):
    account: str
    createTime: str
    currencyCode: str
    deleteTime: str
    displayName: str
    expireTime: str
    industryCategory: typing_extensions.Literal[
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
    propertyType: typing_extensions.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]
    serviceLevel: typing_extensions.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "GOOGLE_ANALYTICS_STANDARD", "GOOGLE_ANALYTICS_360"
    ]
    timeZone: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaPropertySummary(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    parent: str
    property: str
    propertyType: typing_extensions.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest(
    typing_extensions.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1betaAccount
    redirectUri: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse(
    typing_extensions.TypedDict, total=False
):
    accountTicketId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest(
    typing_extensions.TypedDict, total=False
):
    action: _list[str]
    actorEmail: _list[str]
    earliestChangeTime: str
    latestChangeTime: str
    pageSize: int
    pageToken: str
    property: str
    resourceType: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse(
    typing_extensions.TypedDict, total=False
):
    changeHistoryEvents: _list[GoogleAnalyticsAdminV1betaChangeHistoryEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
