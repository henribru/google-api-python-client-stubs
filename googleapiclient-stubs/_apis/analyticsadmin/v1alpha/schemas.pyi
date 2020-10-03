import typing

import typing_extensions

class GoogleAnalyticsAdminV1alphaUserLink(typing_extensions.TypedDict, total=False):
    name: str
    directRoles: typing.List[str]
    emailAddress: str

class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse(
    typing_extensions.TypedDict, total=False
):
    firebaseLinks: typing.List[GoogleAnalyticsAdminV1alphaFirebaseLink]

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings(
    typing_extensions.TypedDict, total=False
):
    searchQueryParameter: str
    dataTaggedElementClicksEnabled: bool
    streamEnabled: bool
    fileDownloadsEnabled: bool
    excludedDomains: str
    pageViewsEnabled: bool
    formInteractionsEnabled: bool
    outboundClicksEnabled: bool
    scrollsEnabled: bool
    articlesAndBlogsEnabled: bool
    urlQueryParameter: str
    pageChangesEnabled: bool
    videoEngagementEnabled: bool
    siteSearchEnabled: bool
    pageLoadsEnabled: bool
    productsAndEcommerceEnabled: bool
    contentViewsEnabled: bool
    name: str

class GoogleAnalyticsAdminV1alphaListAccountSummariesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    accountSummaries: typing.List[GoogleAnalyticsAdminV1alphaAccountSummary]

class GoogleAnalyticsAdminV1alphaIosAppDataStream(
    typing_extensions.TypedDict, total=False
):
    name: str
    updateTime: str
    displayName: str
    bundleId: str
    firebaseAppId: str
    createTime: str

class GoogleAnalyticsAdminV1alphaPropertySummary(
    typing_extensions.TypedDict, total=False
):
    property: str
    displayName: str

class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUsers: bool
    requests: typing.List[GoogleAnalyticsAdminV1alphaCreateUserLinkRequest]

class GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest]

class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

class GoogleAnalyticsAdminV1alphaCreateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUser: bool
    parent: str
    userLink: GoogleAnalyticsAdminV1alphaUserLink

class GoogleAnalyticsAdminV1alphaAccount(typing_extensions.TypedDict, total=False):
    updateTime: str
    displayName: str
    countryCode: str
    deleted: bool
    createTime: str
    name: str

class GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    androidAppDataStreams: typing.List[GoogleAnalyticsAdminV1alphaAndroidAppDataStream]
    nextPageToken: str

class GoogleAnalyticsAdminV1alphaListUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]
    nextPageToken: str

class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

class GoogleAnalyticsAdminV1alphaProperty(typing_extensions.TypedDict, total=False):
    displayName: str
    parent: str
    updateTime: str
    createTime: str
    currencyCode: str
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
    deleted: bool
    timeZone: str
    name: str

class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    googleAdsLinks: typing.List[GoogleAnalyticsAdminV1alphaGoogleAdsLink]

class GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest(
    typing_extensions.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    redirectUri: str

class GoogleAnalyticsAdminV1alphaAccountSummary(
    typing_extensions.TypedDict, total=False
):
    propertySummaries: typing.List[GoogleAnalyticsAdminV1alphaPropertySummary]
    displayName: str
    name: str
    account: str

class GoogleAnalyticsAdminV1alphaListAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accounts: typing.List[GoogleAnalyticsAdminV1alphaAccount]
    nextPageToken: str

class GoogleAnalyticsAdminV1alphaGoogleAdsLink(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    emailAddress: str
    updateTime: str
    adsPersonalizationEnabled: bool
    customerId: str
    canManageClients: bool
    name: str
    parent: str

class GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

class GoogleAnalyticsAdminV1alphaListWebDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    webDataStreams: typing.List[GoogleAnalyticsAdminV1alphaWebDataStream]
    nextPageToken: str

class GoogleAnalyticsAdminV1alphaWebDataStream(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    updateTime: str
    firebaseAppId: str
    createTime: str
    measurementId: str
    name: str
    defaultUri: str

class GoogleAnalyticsAdminV1alphaListPropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    properties: typing.List[GoogleAnalyticsAdminV1alphaProperty]

class GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    iosAppDataStreams: typing.List[GoogleAnalyticsAdminV1alphaIosAppDataStream]
    nextPageToken: str

class GoogleAnalyticsAdminV1alphaGlobalSiteTag(
    typing_extensions.TypedDict, total=False
):
    snippet: str

class GoogleAnalyticsAdminV1alphaAuditUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaAuditUserLink]
    nextPageToken: str

class GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    userLink: GoogleAnalyticsAdminV1alphaUserLink

class GoogleAnalyticsAdminV1alphaDataSharingSettings(
    typing_extensions.TypedDict, total=False
):
    sharingWithGoogleAssignedSalesEnabled: bool
    sharingWithGoogleSupportEnabled: bool
    sharingWithGoogleProductsEnabled: bool
    sharingWithGoogleAnySalesEnabled: bool
    name: str
    sharingWithOthersEnabled: bool

class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse(
    typing_extensions.TypedDict, total=False
):
    accountTicketId: str

class GoogleAnalyticsAdminV1alphaFirebaseLink(typing_extensions.TypedDict, total=False):
    maximumUserAccess: typing_extensions.Literal[
        "MAXIMUM_USER_ACCESS_UNSPECIFIED",
        "NO_ACCESS",
        "READ_AND_ANALYZE",
        "EDITOR_WITHOUT_LINK_MANAGEMENT",
        "EDITOR_INCLUDING_LINK_MANAGEMENT",
    ]
    name: str
    createTime: str
    project: str

class GoogleAnalyticsAdminV1alphaAuditUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str

class GoogleAnalyticsAdminV1alphaAuditUserLink(
    typing_extensions.TypedDict, total=False
):
    effectiveRoles: typing.List[str]
    directRoles: typing.List[str]
    name: str
    emailAddress: str

class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest]

class GoogleAnalyticsAdminV1alphaAndroidAppDataStream(
    typing_extensions.TypedDict, total=False
):
    firebaseAppId: str
    updateTime: str
    packageName: str
    createTime: str
    displayName: str
    name: str
