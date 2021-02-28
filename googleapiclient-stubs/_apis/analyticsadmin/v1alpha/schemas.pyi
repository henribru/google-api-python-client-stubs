import typing

import typing_extensions
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
    propertySummaries: typing.List[GoogleAnalyticsAdminV1alphaPropertySummary]

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
class GoogleAnalyticsAdminV1alphaAuditUserLink(
    typing_extensions.TypedDict, total=False
):
    directRoles: typing.List[str]
    effectiveRoles: typing.List[str]
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
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaAuditUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUsers: bool
    requests: typing.List[GoogleAnalyticsAdminV1alphaCreateUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: typing.List[GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUser: bool
    parent: str
    userLink: GoogleAnalyticsAdminV1alphaUserLink

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
    maximumUserAccess: typing_extensions.Literal[
        "MAXIMUM_USER_ACCESS_UNSPECIFIED",
        "NO_ACCESS",
        "READ_AND_ANALYZE",
        "EDITOR_WITHOUT_LINK_MANAGEMENT",
        "EDITOR_INCLUDING_LINK_MANAGEMENT",
    ]
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
    customerId: str
    emailAddress: str
    name: str
    updateTime: str

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
class GoogleAnalyticsAdminV1alphaListAccountSummariesResponse(
    typing_extensions.TypedDict, total=False
):
    accountSummaries: typing.List[GoogleAnalyticsAdminV1alphaAccountSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accounts: typing.List[GoogleAnalyticsAdminV1alphaAccount]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    androidAppDataStreams: typing.List[GoogleAnalyticsAdminV1alphaAndroidAppDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse(
    typing_extensions.TypedDict, total=False
):
    firebaseLinks: typing.List[GoogleAnalyticsAdminV1alphaFirebaseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse(
    typing_extensions.TypedDict, total=False
):
    googleAdsLinks: typing.List[GoogleAnalyticsAdminV1alphaGoogleAdsLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    iosAppDataStreams: typing.List[GoogleAnalyticsAdminV1alphaIosAppDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListPropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    properties: typing.List[GoogleAnalyticsAdminV1alphaProperty]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userLinks: typing.List[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListWebDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    webDataStreams: typing.List[GoogleAnalyticsAdminV1alphaWebDataStream]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProperty(typing_extensions.TypedDict, total=False):
    createTime: str
    currencyCode: str
    deleted: bool
    displayName: str
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
class GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    userLink: GoogleAnalyticsAdminV1alphaUserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUserLink(typing_extensions.TypedDict, total=False):
    directRoles: typing.List[str]
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
