import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccount(typing_extensions.TypedDict, total=False):
    createTime: str
    deleted: bool
    displayName: str
    name: str
    regionCode: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccountSummary(
    typing_extensions.TypedDict, total=False
):
    account: str
    displayName: str
    name: str
    propertySummaries: _list[GoogleAnalyticsAdminV1alphaPropertySummary]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAndroidAppDataStream(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    firebaseAppId: str
    name: str
    packageName: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse(
    typing_extensions.TypedDict, total=False
):
    displayVideo360AdvertiserLink: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLink(
    typing_extensions.TypedDict, total=False
):
    directRoles: _list[str]
    effectiveRoles: _list[str]
    emailAddress: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userLinks: _list[GoogleAnalyticsAdminV1alphaAuditUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUsers: bool
    requests: _list[GoogleAnalyticsAdminV1alphaCreateUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryChange(
    typing_extensions.TypedDict, total=False
):
    action: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"
    ]
    resource: str
    resourceAfterChange: GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource
    resourceBeforeChange: GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource(
    typing_extensions.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    androidAppDataStream: GoogleAnalyticsAdminV1alphaAndroidAppDataStream
    conversionEvent: GoogleAnalyticsAdminV1alphaConversionEvent
    customDimension: GoogleAnalyticsAdminV1alphaCustomDimension
    customMetric: GoogleAnalyticsAdminV1alphaCustomMetric
    dataRetentionSettings: GoogleAnalyticsAdminV1alphaDataRetentionSettings
    displayVideo360AdvertiserLink: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    displayVideo360AdvertiserLinkProposal: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
    firebaseLink: GoogleAnalyticsAdminV1alphaFirebaseLink
    googleAdsLink: GoogleAnalyticsAdminV1alphaGoogleAdsLink
    googleSignalsSettings: GoogleAnalyticsAdminV1alphaGoogleSignalsSettings
    iosAppDataStream: GoogleAnalyticsAdminV1alphaIosAppDataStream
    measurementProtocolSecret: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
    property: GoogleAnalyticsAdminV1alphaProperty
    webDataStream: GoogleAnalyticsAdminV1alphaWebDataStream

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryEvent(
    typing_extensions.TypedDict, total=False
):
    actorType: typing_extensions.Literal[
        "ACTOR_TYPE_UNSPECIFIED", "USER", "SYSTEM", "SUPPORT"
    ]
    changeTime: str
    changes: _list[GoogleAnalyticsAdminV1alphaChangeHistoryChange]
    changesFiltered: bool
    id: str
    userActorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaConversionEvent(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    custom: bool
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUser: bool
    parent: str
    userLink: GoogleAnalyticsAdminV1alphaUserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomDimension(
    typing_extensions.TypedDict, total=False
):
    description: str
    disallowAdsPersonalization: bool
    displayName: str
    name: str
    parameterName: str
    scope: typing_extensions.Literal["DIMENSION_SCOPE_UNSPECIFIED", "EVENT", "USER"]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomMetric(typing_extensions.TypedDict, total=False):
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
    scope: typing_extensions.Literal["METRIC_SCOPE_UNSPECIFIED", "EVENT"]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataRetentionSettings(
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
class GoogleAnalyticsAdminV1alphaDataSharingSettings(
    typing_extensions.TypedDict, total=False
):
    name: str
    sharingWithGoogleAnySalesEnabled: bool
    sharingWithGoogleAssignedSalesEnabled: bool
    sharingWithGoogleProductsEnabled: bool
    sharingWithGoogleSupportEnabled: bool
    sharingWithOthersEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    linkProposalStatusDetails: GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails
    name: str
    validationEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings(
    typing_extensions.TypedDict, total=False
):
    fileDownloadsEnabled: bool
    name: str
    outboundClicksEnabled: bool
    pageChangesEnabled: bool
    pageLoadsEnabled: bool
    pageViewsEnabled: bool
    scrollsEnabled: bool
    searchQueryParameter: str
    siteSearchEnabled: bool
    streamEnabled: bool
    uriQueryParameter: str
    videoEngagementEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFirebaseLink(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    project: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGlobalSiteTag(
    typing_extensions.TypedDict, total=False
):
    name: str
    snippet: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleAdsLink(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    canManageClients: bool
    createTime: str
    creatorEmailAddress: str
    customerId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleSignalsSettings(
    typing_extensions.TypedDict, total=False
):
    consent: typing_extensions.Literal[
        "GOOGLE_SIGNALS_CONSENT_UNSPECIFIED",
        "GOOGLE_SIGNALS_CONSENT_CONSENTED",
        "GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED",
    ]
    name: str
    state: typing_extensions.Literal[
        "GOOGLE_SIGNALS_STATE_UNSPECIFIED",
        "GOOGLE_SIGNALS_ENABLED",
        "GOOGLE_SIGNALS_DISABLED",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaIosAppDataStream(
    typing_extensions.TypedDict, total=False
):
    bundleId: str
    createTime: str
    displayName: str
    firebaseAppId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails(
    typing_extensions.TypedDict, total=False
):
    linkProposalInitiatingProduct: typing_extensions.Literal[
        "LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED",
        "GOOGLE_ANALYTICS",
        "LINKED_PRODUCT",
    ]
    linkProposalState: typing_extensions.Literal[
        "LINK_PROPOSAL_STATE_UNSPECIFIED",
        "AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS",
        "AWAITING_REVIEW_FROM_LINKED_PRODUCT",
        "WITHDRAWN",
        "DECLINED",
        "EXPIRED",
        "OBSOLETE",
    ]
    requestorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountSummariesResponse(
    typing_extensions.TypedDict, total=False
):
    accountSummaries: _list[GoogleAnalyticsAdminV1alphaAccountSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accounts: _list[GoogleAnalyticsAdminV1alphaAccount]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    androidAppDataStreams: _list[GoogleAnalyticsAdminV1alphaAndroidAppDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListConversionEventsResponse(
    typing_extensions.TypedDict, total=False
):
    conversionEvents: _list[GoogleAnalyticsAdminV1alphaConversionEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse(
    typing_extensions.TypedDict, total=False
):
    customDimensions: _list[GoogleAnalyticsAdminV1alphaCustomDimension]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    customMetrics: _list[GoogleAnalyticsAdminV1alphaCustomMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse(
    typing_extensions.TypedDict, total=False
):
    displayVideo360AdvertiserLinkProposals: _list[
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    displayVideo360AdvertiserLinks: _list[
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse(
    typing_extensions.TypedDict, total=False
):
    firebaseLinks: _list[GoogleAnalyticsAdminV1alphaFirebaseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse(
    typing_extensions.TypedDict, total=False
):
    googleAdsLinks: _list[GoogleAnalyticsAdminV1alphaGoogleAdsLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    iosAppDataStreams: _list[GoogleAnalyticsAdminV1alphaIosAppDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse(
    typing_extensions.TypedDict, total=False
):
    measurementProtocolSecrets: _list[
        GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListPropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    properties: _list[GoogleAnalyticsAdminV1alphaProperty]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListWebDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    webDataStreams: _list[GoogleAnalyticsAdminV1alphaWebDataStream]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    secretValue: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProperty(typing_extensions.TypedDict, total=False):
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
    serviceLevel: typing_extensions.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "GOOGLE_ANALYTICS_STANDARD", "GOOGLE_ANALYTICS_360"
    ]
    timeZone: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaPropertySummary(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    property: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest(
    typing_extensions.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    redirectUri: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse(
    typing_extensions.TypedDict, total=False
):
    accountTicketId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest(
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
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse(
    typing_extensions.TypedDict, total=False
):
    changeHistoryEvents: _list[GoogleAnalyticsAdminV1alphaChangeHistoryEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    userLink: GoogleAnalyticsAdminV1alphaUserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUserLink(typing_extensions.TypedDict, total=False):
    directRoles: _list[str]
    emailAddress: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaWebDataStream(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    defaultUri: str
    displayName: str
    firebaseAppId: str
    measurementId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
