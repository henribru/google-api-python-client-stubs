import typing

_list = list

@typing.type_check_only
class ActivatePretargetingConfigRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class AdTechnologyProviders(typing.TypedDict, total=False):
    detectedGvlIds: _list[str]
    detectedProviderIds: _list[str]
    unidentifiedProviderDomains: _list[str]

@typing.type_check_only
class AddTargetedAppsRequest(typing.TypedDict, total=False):
    appIds: _list[str]
    targetingMode: typing.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]

@typing.type_check_only
class AddTargetedPublishersRequest(typing.TypedDict, total=False):
    publisherIds: _list[str]
    targetingMode: typing.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]

@typing.type_check_only
class AddTargetedSitesRequest(typing.TypedDict, total=False):
    sites: _list[str]
    targetingMode: typing.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]

@typing.type_check_only
class AdvertiserAndBrand(typing.TypedDict, total=False):
    advertiserId: str
    advertiserName: str
    brandId: str
    brandName: str

@typing.type_check_only
class AppTargeting(typing.TypedDict, total=False):
    mobileAppCategoryTargeting: NumericTargetingDimension
    mobileAppTargeting: StringTargetingDimension

@typing.type_check_only
class BatchApprovePublisherConnectionsRequest(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BatchApprovePublisherConnectionsResponse(typing.TypedDict, total=False):
    publisherConnections: _list[PublisherConnection]

@typing.type_check_only
class BatchRejectPublisherConnectionsRequest(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BatchRejectPublisherConnectionsResponse(typing.TypedDict, total=False):
    publisherConnections: _list[PublisherConnection]

@typing.type_check_only
class Bidder(typing.TypedDict, total=False):
    bypassNonguaranteedDealsPretargeting: bool
    cookieMatchingNetworkId: str
    cookieMatchingUrl: str
    dealsBillingId: str
    name: str

@typing.type_check_only
class Buyer(typing.TypedDict, total=False):
    activeCreativeCount: str
    bidder: str
    billingIds: _list[str]
    displayName: str
    maximumActiveCreativeCount: str
    name: str

@typing.type_check_only
class CloseUserListRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Creative(typing.TypedDict, total=False):
    accountId: str
    adChoicesDestinationUrl: str
    advertiserName: str
    agencyId: str
    apiUpdateTime: str
    creativeFormat: typing.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "HTML", "VIDEO", "NATIVE"
    ]
    creativeId: str
    creativeServingDecision: CreativeServingDecision
    dealIds: _list[str]
    declaredAttributes: _list[
        typing.Literal[
            "ATTRIBUTE_UNSPECIFIED",
            "IMAGE_RICH_MEDIA",
            "ADOBE_FLASH_FLV",
            "IS_TAGGED",
            "IS_COOKIE_TARGETED",
            "IS_USER_INTEREST_TARGETED",
            "EXPANDING_DIRECTION_NONE",
            "EXPANDING_DIRECTION_UP",
            "EXPANDING_DIRECTION_DOWN",
            "EXPANDING_DIRECTION_LEFT",
            "EXPANDING_DIRECTION_RIGHT",
            "EXPANDING_DIRECTION_UP_LEFT",
            "EXPANDING_DIRECTION_UP_RIGHT",
            "EXPANDING_DIRECTION_DOWN_LEFT",
            "EXPANDING_DIRECTION_DOWN_RIGHT",
            "CREATIVE_TYPE_HTML",
            "CREATIVE_TYPE_VAST_VIDEO",
            "EXPANDING_DIRECTION_UP_OR_DOWN",
            "EXPANDING_DIRECTION_LEFT_OR_RIGHT",
            "EXPANDING_DIRECTION_ANY_DIAGONAL",
            "EXPANDING_ACTION_ROLLOVER_TO_EXPAND",
            "INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH",
            "RICH_MEDIA_CAPABILITY_TYPE_MRAID",
            "RICH_MEDIA_CAPABILITY_TYPE_FLASH",
            "RICH_MEDIA_CAPABILITY_TYPE_HTML5",
            "SKIPPABLE_INSTREAM_VIDEO",
            "RICH_MEDIA_CAPABILITY_TYPE_SSL",
            "RICH_MEDIA_CAPABILITY_TYPE_NON_SSL",
            "RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL",
            "NON_SKIPPABLE_INSTREAM_VIDEO",
            "NATIVE_ELIGIBILITY_ELIGIBLE",
            "NON_VPAID",
            "NATIVE_ELIGIBILITY_NOT_ELIGIBLE",
            "ANY_INTERSTITIAL",
            "NON_INTERSTITIAL",
            "IN_BANNER_VIDEO",
            "RENDERING_SIZELESS_ADX",
            "OMSDK_1_0",
            "RENDERING_PLAYABLE",
        ]
    ]
    declaredClickThroughUrls: _list[str]
    declaredRestrictedCategories: _list[
        typing.Literal["RESTRICTED_CATEGORY_UNSPECIFIED", "ALCOHOL"]
    ]
    declaredVendorIds: _list[int]
    html: HtmlContent
    impressionTrackingUrls: _list[str]
    name: str
    native: NativeContent
    renderUrl: str
    restrictedCategories: _list[
        typing.Literal["RESTRICTED_CATEGORY_UNSPECIFIED", "ALCOHOL"]
    ]
    version: int
    video: VideoContent

@typing.type_check_only
class CreativeDimensions(typing.TypedDict, total=False):
    height: str
    width: str

@typing.type_check_only
class CreativeServingDecision(typing.TypedDict, total=False):
    adTechnologyProviders: AdTechnologyProviders
    chinaPolicyCompliance: PolicyCompliance
    dealsPolicyCompliance: PolicyCompliance
    detectedAdvertisers: _list[AdvertiserAndBrand]
    detectedAttributes: _list[
        typing.Literal[
            "ATTRIBUTE_UNSPECIFIED",
            "IMAGE_RICH_MEDIA",
            "ADOBE_FLASH_FLV",
            "IS_TAGGED",
            "IS_COOKIE_TARGETED",
            "IS_USER_INTEREST_TARGETED",
            "EXPANDING_DIRECTION_NONE",
            "EXPANDING_DIRECTION_UP",
            "EXPANDING_DIRECTION_DOWN",
            "EXPANDING_DIRECTION_LEFT",
            "EXPANDING_DIRECTION_RIGHT",
            "EXPANDING_DIRECTION_UP_LEFT",
            "EXPANDING_DIRECTION_UP_RIGHT",
            "EXPANDING_DIRECTION_DOWN_LEFT",
            "EXPANDING_DIRECTION_DOWN_RIGHT",
            "CREATIVE_TYPE_HTML",
            "CREATIVE_TYPE_VAST_VIDEO",
            "EXPANDING_DIRECTION_UP_OR_DOWN",
            "EXPANDING_DIRECTION_LEFT_OR_RIGHT",
            "EXPANDING_DIRECTION_ANY_DIAGONAL",
            "EXPANDING_ACTION_ROLLOVER_TO_EXPAND",
            "INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH",
            "RICH_MEDIA_CAPABILITY_TYPE_MRAID",
            "RICH_MEDIA_CAPABILITY_TYPE_FLASH",
            "RICH_MEDIA_CAPABILITY_TYPE_HTML5",
            "SKIPPABLE_INSTREAM_VIDEO",
            "RICH_MEDIA_CAPABILITY_TYPE_SSL",
            "RICH_MEDIA_CAPABILITY_TYPE_NON_SSL",
            "RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL",
            "NON_SKIPPABLE_INSTREAM_VIDEO",
            "NATIVE_ELIGIBILITY_ELIGIBLE",
            "NON_VPAID",
            "NATIVE_ELIGIBILITY_NOT_ELIGIBLE",
            "ANY_INTERSTITIAL",
            "NON_INTERSTITIAL",
            "IN_BANNER_VIDEO",
            "RENDERING_SIZELESS_ADX",
            "OMSDK_1_0",
            "RENDERING_PLAYABLE",
        ]
    ]
    detectedCategories: _list[str]
    detectedCategoriesTaxonomy: typing.Literal[
        "AD_CATEGORY_TAXONOMY_UNSPECIFIED",
        "GOOGLE_AD_CATEGORY_TAXONOMY",
        "IAB_CONTENT_1_0",
    ]
    detectedClickThroughUrls: _list[str]
    detectedDomains: _list[str]
    detectedLanguages: _list[str]
    detectedProductCategories: _list[int]
    detectedSensitiveCategories: _list[int]
    detectedVendorIds: _list[int]
    lastStatusUpdate: str
    networkPolicyCompliance: PolicyCompliance
    platformPolicyCompliance: PolicyCompliance
    russiaPolicyCompliance: PolicyCompliance

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DestinationNotCrawlableEvidence(typing.TypedDict, total=False):
    crawlTime: str
    crawledUrl: str
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "UNREACHABLE_ROBOTS",
        "TIMEOUT_ROBOTS",
        "ROBOTED_DENIED",
        "UNKNOWN",
    ]

@typing.type_check_only
class DestinationNotWorkingEvidence(typing.TypedDict, total=False):
    dnsError: typing.Literal[
        "DNS_ERROR_UNSPECIFIED", "ERROR_DNS", "GOOGLE_CRAWLER_DNS_ISSUE"
    ]
    expandedUrl: str
    httpError: int
    invalidPage: typing.Literal["INVALID_PAGE_UNSPECIFIED", "EMPTY_OR_ERROR_PAGE"]
    lastCheckTime: str
    platform: typing.Literal[
        "PLATFORM_UNSPECIFIED", "PERSONAL_COMPUTER", "ANDROID", "IOS"
    ]
    redirectionError: typing.Literal[
        "REDIRECTION_ERROR_UNSPECIFIED",
        "TOO_MANY_REDIRECTS",
        "INVALID_REDIRECT",
        "EMPTY_REDIRECT",
        "REDIRECT_ERROR_UNKNOWN",
    ]
    urlRejected: typing.Literal[
        "URL_REJECTED_UNSPECIFIED",
        "BAD_REQUEST",
        "MALFORMED_URL",
        "URL_REJECTED_UNKNOWN",
    ]

@typing.type_check_only
class DestinationUrlEvidence(typing.TypedDict, total=False):
    destinationUrl: str

@typing.type_check_only
class DomainCallEvidence(typing.TypedDict, total=False):
    topHttpCallDomains: _list[DomainCalls]
    totalHttpCallCount: int

@typing.type_check_only
class DomainCalls(typing.TypedDict, total=False):
    domain: str
    httpCallCount: int

@typing.type_check_only
class DownloadSizeEvidence(typing.TypedDict, total=False):
    topUrlDownloadSizeBreakdowns: _list[UrlDownloadSize]
    totalDownloadSizeKb: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing.TypedDict, total=False):
    bidProtocol: typing.Literal[
        "BID_PROTOCOL_UNSPECIFIED", "GOOGLE_RTB", "OPENRTB_JSON", "OPENRTB_PROTOBUF"
    ]
    maximumQps: str
    name: str
    tradingLocation: typing.Literal[
        "TRADING_LOCATION_UNSPECIFIED", "US_WEST", "US_EAST", "EUROPE", "ASIA"
    ]
    url: str

@typing.type_check_only
class GetRemarketingTagResponse(typing.TypedDict, total=False):
    snippet: str

@typing.type_check_only
class HtmlContent(typing.TypedDict, total=False):
    height: int
    snippet: str
    width: int

@typing.type_check_only
class HttpCallEvidence(typing.TypedDict, total=False):
    urls: _list[str]

@typing.type_check_only
class HttpCookieEvidence(typing.TypedDict, total=False):
    cookieNames: _list[str]
    maxCookieCount: int

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    height: int
    url: str
    width: int

@typing.type_check_only
class ListBiddersResponse(typing.TypedDict, total=False):
    bidders: _list[Bidder]
    nextPageToken: str

@typing.type_check_only
class ListBuyersResponse(typing.TypedDict, total=False):
    buyers: _list[Buyer]
    nextPageToken: str

@typing.type_check_only
class ListCreativesResponse(typing.TypedDict, total=False):
    creatives: _list[Creative]
    nextPageToken: str

@typing.type_check_only
class ListEndpointsResponse(typing.TypedDict, total=False):
    endpoints: _list[Endpoint]
    nextPageToken: str

@typing.type_check_only
class ListPretargetingConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pretargetingConfigs: _list[PretargetingConfig]

@typing.type_check_only
class ListPublisherConnectionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    publisherConnections: _list[PublisherConnection]

@typing.type_check_only
class ListUserListsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userLists: _list[UserList]

@typing.type_check_only
class MediaFile(typing.TypedDict, total=False):
    bitrate: str
    mimeType: typing.Literal[
        "VIDEO_MIME_TYPE_UNSPECIFIED",
        "MIME_VIDEO_XFLV",
        "MIME_VIDEO_WEBM",
        "MIME_VIDEO_MP4",
        "MIME_VIDEO_OGG",
        "MIME_VIDEO_YT_HOSTED",
        "MIME_VIDEO_X_MS_WMV",
        "MIME_VIDEO_3GPP",
        "MIME_VIDEO_MOV",
        "MIME_APPLICATION_SWF",
        "MIME_APPLICATION_SURVEY",
        "MIME_APPLICATION_JAVASCRIPT",
        "MIME_APPLICATION_SILVERLIGHT",
        "MIME_APPLICATION_MPEGURL",
        "MIME_APPLICATION_MPEGDASH",
        "MIME_AUDIO_MP4A",
        "MIME_AUDIO_MP3",
        "MIME_AUDIO_OGG",
    ]

@typing.type_check_only
class NativeContent(typing.TypedDict, total=False):
    advertiserName: str
    appIcon: Image
    body: str
    callToAction: str
    clickLinkUrl: str
    clickTrackingUrl: str
    headline: str
    image: Image
    logo: Image
    priceDisplayText: str
    starRating: float
    videoUrl: str
    videoVastXml: str

@typing.type_check_only
class NumericTargetingDimension(typing.TypedDict, total=False):
    excludedIds: _list[str]
    includedIds: _list[str]

@typing.type_check_only
class OpenUserListRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class PolicyCompliance(typing.TypedDict, total=False):
    status: typing.Literal[
        "STATUS_UNSPECIFIED",
        "PENDING_REVIEW",
        "DISAPPROVED",
        "APPROVED",
        "CERTIFICATE_REQUIRED",
    ]
    topics: _list[PolicyTopicEntry]

@typing.type_check_only
class PolicyTopicEntry(typing.TypedDict, total=False):
    evidences: _list[PolicyTopicEvidence]
    helpCenterUrl: str
    missingCertificate: bool
    policyTopic: str

@typing.type_check_only
class PolicyTopicEvidence(typing.TypedDict, total=False):
    destinationNotCrawlable: DestinationNotCrawlableEvidence
    destinationNotWorking: DestinationNotWorkingEvidence
    destinationUrl: DestinationUrlEvidence
    domainCall: DomainCallEvidence
    downloadSize: DownloadSizeEvidence
    httpCall: HttpCallEvidence
    httpCookie: HttpCookieEvidence

@typing.type_check_only
class PretargetingConfig(typing.TypedDict, total=False):
    allowedUserTargetingModes: _list[
        typing.Literal[
            "USER_TARGETING_MODE_UNSPECIFIED",
            "REMARKETING_ADS",
            "INTEREST_BASED_TARGETING",
        ]
    ]
    appTargeting: AppTargeting
    billingId: str
    displayName: str
    excludedContentLabelIds: _list[str]
    geoTargeting: NumericTargetingDimension
    includedCreativeDimensions: _list[CreativeDimensions]
    includedEnvironments: _list[typing.Literal["ENVIRONMENT_UNSPECIFIED", "APP", "WEB"]]
    includedFormats: _list[
        typing.Literal["CREATIVE_FORMAT_UNSPECIFIED", "HTML", "VAST", "NATIVE"]
    ]
    includedLanguages: _list[str]
    includedMobileOperatingSystemIds: _list[str]
    includedPlatforms: _list[
        typing.Literal[
            "PLATFORM_UNSPECIFIED",
            "PERSONAL_COMPUTER",
            "PHONE",
            "TABLET",
            "CONNECTED_TV",
        ]
    ]
    includedUserIdTypes: _list[
        typing.Literal[
            "USER_ID_TYPE_UNSPECIFIED",
            "HOSTED_MATCH_DATA",
            "GOOGLE_COOKIE",
            "DEVICE_ID",
            "PUBLISHER_PROVIDED_ID",
            "PUBLISHER_FIRST_PARTY_ID",
        ]
    ]
    interstitialTargeting: typing.Literal[
        "INTERSTITIAL_TARGETING_UNSPECIFIED",
        "ONLY_INTERSTITIAL_REQUESTS",
        "ONLY_NON_INTERSTITIAL_REQUESTS",
    ]
    invalidGeoIds: _list[str]
    maximumQps: str
    minimumViewabilityDecile: int
    name: str
    publisherTargeting: StringTargetingDimension
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED"]
    userListTargeting: NumericTargetingDimension
    verticalTargeting: NumericTargetingDimension
    webTargeting: StringTargetingDimension

@typing.type_check_only
class PublisherConnection(typing.TypedDict, total=False):
    biddingState: typing.Literal["STATE_UNSPECIFIED", "PENDING", "REJECTED", "APPROVED"]
    createTime: str
    displayName: str
    name: str
    publisherPlatform: typing.Literal[
        "PUBLISHER_PLATFORM_UNSPECIFIED", "GOOGLE_AD_MANAGER", "ADMOB"
    ]

@typing.type_check_only
class RemoveTargetedAppsRequest(typing.TypedDict, total=False):
    appIds: _list[str]

@typing.type_check_only
class RemoveTargetedPublishersRequest(typing.TypedDict, total=False):
    publisherIds: _list[str]

@typing.type_check_only
class RemoveTargetedSitesRequest(typing.TypedDict, total=False):
    sites: _list[str]

@typing.type_check_only
class StringTargetingDimension(typing.TypedDict, total=False):
    targetingMode: typing.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]
    values: _list[str]

@typing.type_check_only
class SuspendPretargetingConfigRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UrlDownloadSize(typing.TypedDict, total=False):
    downloadSizeKb: int
    normalizedUrl: str

@typing.type_check_only
class UrlRestriction(typing.TypedDict, total=False):
    endDate: Date
    restrictionType: typing.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED",
        "CONTAINS",
        "EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "DOES_NOT_EQUAL",
        "DOES_NOT_CONTAIN",
        "DOES_NOT_START_WITH",
        "DOES_NOT_END_WITH",
    ]
    startDate: Date
    url: str

@typing.type_check_only
class UserList(typing.TypedDict, total=False):
    description: str
    displayName: str
    membershipDurationDays: str
    name: str
    status: typing.Literal["STATUS_UNSPECIFIED", "OPEN", "CLOSED"]
    urlRestriction: UrlRestriction

@typing.type_check_only
class VideoContent(typing.TypedDict, total=False):
    videoMetadata: VideoMetadata
    videoUrl: str
    videoVastXml: str

@typing.type_check_only
class VideoMetadata(typing.TypedDict, total=False):
    duration: str
    isValidVast: bool
    isVpaid: bool
    mediaFiles: _list[MediaFile]
    skipOffset: str
    vastVersion: typing.Literal[
        "VAST_VERSION_UNSPECIFIED",
        "VAST_VERSION_1_0",
        "VAST_VERSION_2_0",
        "VAST_VERSION_3_0",
        "VAST_VERSION_4_0",
    ]

@typing.type_check_only
class WatchCreativesRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class WatchCreativesResponse(typing.TypedDict, total=False):
    subscription: str
    topic: str
