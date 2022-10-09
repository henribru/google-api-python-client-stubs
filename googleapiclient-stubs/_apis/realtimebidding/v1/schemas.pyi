import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActivatePretargetingConfigRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdTechnologyProviders(typing_extensions.TypedDict, total=False):
    detectedGvlIds: _list[str]
    detectedProviderIds: _list[str]
    unidentifiedProviderDomains: _list[str]

@typing.type_check_only
class AddTargetedAppsRequest(typing_extensions.TypedDict, total=False):
    appIds: _list[str]
    targetingMode: typing_extensions.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]

@typing.type_check_only
class AddTargetedPublishersRequest(typing_extensions.TypedDict, total=False):
    publisherIds: _list[str]
    targetingMode: typing_extensions.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]

@typing.type_check_only
class AddTargetedSitesRequest(typing_extensions.TypedDict, total=False):
    sites: _list[str]
    targetingMode: typing_extensions.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]

@typing.type_check_only
class AdvertiserAndBrand(typing_extensions.TypedDict, total=False):
    advertiserId: str
    advertiserName: str
    brandId: str
    brandName: str

@typing.type_check_only
class AppTargeting(typing_extensions.TypedDict, total=False):
    mobileAppCategoryTargeting: NumericTargetingDimension
    mobileAppTargeting: StringTargetingDimension

@typing.type_check_only
class BatchApprovePublisherConnectionsRequest(typing_extensions.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BatchApprovePublisherConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    publisherConnections: _list[PublisherConnection]

@typing.type_check_only
class BatchRejectPublisherConnectionsRequest(typing_extensions.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BatchRejectPublisherConnectionsResponse(typing_extensions.TypedDict, total=False):
    publisherConnections: _list[PublisherConnection]

@typing.type_check_only
class Bidder(typing_extensions.TypedDict, total=False):
    bypassNonguaranteedDealsPretargeting: bool
    cookieMatchingNetworkId: str
    cookieMatchingUrl: str
    dealsBillingId: str
    name: str

@typing.type_check_only
class Buyer(typing_extensions.TypedDict, total=False):
    activeCreativeCount: str
    bidder: str
    billingIds: _list[str]
    displayName: str
    maximumActiveCreativeCount: str
    name: str

@typing.type_check_only
class CloseUserListRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    accountId: str
    adChoicesDestinationUrl: str
    advertiserName: str
    agencyId: str
    apiUpdateTime: str
    creativeFormat: typing_extensions.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "HTML", "VIDEO", "NATIVE"
    ]
    creativeId: str
    creativeServingDecision: CreativeServingDecision
    dealIds: _list[str]
    declaredAttributes: _list[str]
    declaredClickThroughUrls: _list[str]
    declaredRestrictedCategories: _list[str]
    declaredVendorIds: _list[int]
    html: HtmlContent
    impressionTrackingUrls: _list[str]
    name: str
    native: NativeContent
    renderUrl: str
    restrictedCategories: _list[str]
    version: int
    video: VideoContent

@typing.type_check_only
class CreativeDimensions(typing_extensions.TypedDict, total=False):
    height: str
    width: str

@typing.type_check_only
class CreativeServingDecision(typing_extensions.TypedDict, total=False):
    adTechnologyProviders: AdTechnologyProviders
    chinaPolicyCompliance: PolicyCompliance
    dealsPolicyCompliance: PolicyCompliance
    detectedAdvertisers: _list[AdvertiserAndBrand]
    detectedAttributes: _list[str]
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
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DestinationNotCrawlableEvidence(typing_extensions.TypedDict, total=False):
    crawlTime: str
    crawledUrl: str
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED",
        "UNREACHABLE_ROBOTS",
        "TIMEOUT_ROBOTS",
        "ROBOTED_DENIED",
        "UNKNOWN",
    ]

@typing.type_check_only
class DestinationNotWorkingEvidence(typing_extensions.TypedDict, total=False):
    dnsError: typing_extensions.Literal[
        "DNS_ERROR_UNSPECIFIED", "ERROR_DNS", "GOOGLE_CRAWLER_DNS_ISSUE"
    ]
    expandedUrl: str
    httpError: int
    invalidPage: typing_extensions.Literal[
        "INVALID_PAGE_UNSPECIFIED", "EMPTY_OR_ERROR_PAGE"
    ]
    lastCheckTime: str
    platform: typing_extensions.Literal[
        "PLATFORM_UNSPECIFIED", "PERSONAL_COMPUTER", "ANDROID", "IOS"
    ]
    redirectionError: typing_extensions.Literal[
        "REDIRECTION_ERROR_UNSPECIFIED",
        "TOO_MANY_REDIRECTS",
        "INVALID_REDIRECT",
        "EMPTY_REDIRECT",
        "REDIRECT_ERROR_UNKNOWN",
    ]
    urlRejected: typing_extensions.Literal[
        "URL_REJECTED_UNSPECIFIED",
        "BAD_REQUEST",
        "MALFORMED_URL",
        "URL_REJECTED_UNKNOWN",
    ]

@typing.type_check_only
class DestinationUrlEvidence(typing_extensions.TypedDict, total=False):
    destinationUrl: str

@typing.type_check_only
class DomainCallEvidence(typing_extensions.TypedDict, total=False):
    topHttpCallDomains: _list[DomainCalls]
    totalHttpCallCount: int

@typing.type_check_only
class DomainCalls(typing_extensions.TypedDict, total=False):
    domain: str
    httpCallCount: int

@typing.type_check_only
class DownloadSizeEvidence(typing_extensions.TypedDict, total=False):
    topUrlDownloadSizeBreakdowns: _list[UrlDownloadSize]
    totalDownloadSizeKb: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    bidProtocol: typing_extensions.Literal[
        "BID_PROTOCOL_UNSPECIFIED",
        "GOOGLE_RTB",
        "OPENRTB_2_2",
        "OPENRTB_2_3",
        "OPENRTB_PROTOBUF_2_3",
        "OPENRTB_2_4",
        "OPENRTB_PROTOBUF_2_4",
        "OPENRTB_2_5",
        "OPENRTB_PROTOBUF_2_5",
    ]
    maximumQps: str
    name: str
    tradingLocation: typing_extensions.Literal[
        "TRADING_LOCATION_UNSPECIFIED", "US_WEST", "US_EAST", "EUROPE", "ASIA"
    ]
    url: str

@typing.type_check_only
class GetRemarketingTagResponse(typing_extensions.TypedDict, total=False):
    snippet: str

@typing.type_check_only
class HtmlContent(typing_extensions.TypedDict, total=False):
    height: int
    snippet: str
    width: int

@typing.type_check_only
class HttpCallEvidence(typing_extensions.TypedDict, total=False):
    urls: _list[str]

@typing.type_check_only
class HttpCookieEvidence(typing_extensions.TypedDict, total=False):
    cookieNames: _list[str]
    maxCookieCount: int

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    height: int
    url: str
    width: int

@typing.type_check_only
class ListBiddersResponse(typing_extensions.TypedDict, total=False):
    bidders: _list[Bidder]
    nextPageToken: str

@typing.type_check_only
class ListBuyersResponse(typing_extensions.TypedDict, total=False):
    buyers: _list[Buyer]
    nextPageToken: str

@typing.type_check_only
class ListCreativesResponse(typing_extensions.TypedDict, total=False):
    creatives: _list[Creative]
    nextPageToken: str

@typing.type_check_only
class ListEndpointsResponse(typing_extensions.TypedDict, total=False):
    endpoints: _list[Endpoint]
    nextPageToken: str

@typing.type_check_only
class ListPretargetingConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    pretargetingConfigs: _list[PretargetingConfig]

@typing.type_check_only
class ListPublisherConnectionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    publisherConnections: _list[PublisherConnection]

@typing.type_check_only
class ListUserListsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userLists: _list[UserList]

@typing.type_check_only
class MediaFile(typing_extensions.TypedDict, total=False):
    bitrate: str
    mimeType: typing_extensions.Literal[
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
class NativeContent(typing_extensions.TypedDict, total=False):
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
class NumericTargetingDimension(typing_extensions.TypedDict, total=False):
    excludedIds: _list[str]
    includedIds: _list[str]

@typing.type_check_only
class OpenUserListRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PolicyCompliance(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PENDING_REVIEW",
        "DISAPPROVED",
        "APPROVED",
        "CERTIFICATE_REQUIRED",
    ]
    topics: _list[PolicyTopicEntry]

@typing.type_check_only
class PolicyTopicEntry(typing_extensions.TypedDict, total=False):
    evidences: _list[PolicyTopicEvidence]
    helpCenterUrl: str
    policyTopic: str

@typing.type_check_only
class PolicyTopicEvidence(typing_extensions.TypedDict, total=False):
    destinationNotCrawlable: DestinationNotCrawlableEvidence
    destinationNotWorking: DestinationNotWorkingEvidence
    destinationUrl: DestinationUrlEvidence
    domainCall: DomainCallEvidence
    downloadSize: DownloadSizeEvidence
    httpCall: HttpCallEvidence
    httpCookie: HttpCookieEvidence

@typing.type_check_only
class PretargetingConfig(typing_extensions.TypedDict, total=False):
    allowedUserTargetingModes: _list[str]
    appTargeting: AppTargeting
    billingId: str
    displayName: str
    excludedContentLabelIds: _list[str]
    geoTargeting: NumericTargetingDimension
    includedCreativeDimensions: _list[CreativeDimensions]
    includedEnvironments: _list[str]
    includedFormats: _list[str]
    includedLanguages: _list[str]
    includedMobileOperatingSystemIds: _list[str]
    includedPlatforms: _list[str]
    includedUserIdTypes: _list[str]
    interstitialTargeting: typing_extensions.Literal[
        "INTERSTITIAL_TARGETING_UNSPECIFIED",
        "ONLY_INTERSTITIAL_REQUESTS",
        "ONLY_NON_INTERSTITIAL_REQUESTS",
    ]
    invalidGeoIds: _list[str]
    maximumQps: str
    minimumViewabilityDecile: int
    name: str
    publisherTargeting: StringTargetingDimension
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED"]
    userListTargeting: NumericTargetingDimension
    verticalTargeting: NumericTargetingDimension
    webTargeting: StringTargetingDimension

@typing.type_check_only
class PublisherConnection(typing_extensions.TypedDict, total=False):
    biddingState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "REJECTED", "APPROVED"
    ]
    createTime: str
    displayName: str
    name: str
    publisherPlatform: typing_extensions.Literal[
        "PUBLISHER_PLATFORM_UNSPECIFIED", "GOOGLE_AD_MANAGER", "ADMOB"
    ]

@typing.type_check_only
class RemoveTargetedAppsRequest(typing_extensions.TypedDict, total=False):
    appIds: _list[str]

@typing.type_check_only
class RemoveTargetedPublishersRequest(typing_extensions.TypedDict, total=False):
    publisherIds: _list[str]

@typing.type_check_only
class RemoveTargetedSitesRequest(typing_extensions.TypedDict, total=False):
    sites: _list[str]

@typing.type_check_only
class StringTargetingDimension(typing_extensions.TypedDict, total=False):
    targetingMode: typing_extensions.Literal[
        "TARGETING_MODE_UNSPECIFIED", "INCLUSIVE", "EXCLUSIVE"
    ]
    values: _list[str]

@typing.type_check_only
class SuspendPretargetingConfigRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UrlDownloadSize(typing_extensions.TypedDict, total=False):
    downloadSizeKb: int
    normalizedUrl: str

@typing.type_check_only
class UrlRestriction(typing_extensions.TypedDict, total=False):
    endDate: Date
    restrictionType: typing_extensions.Literal[
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
class UserList(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    membershipDurationDays: str
    name: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "OPEN", "CLOSED"]
    urlRestriction: UrlRestriction

@typing.type_check_only
class VideoContent(typing_extensions.TypedDict, total=False):
    videoMetadata: VideoMetadata
    videoUrl: str
    videoVastXml: str

@typing.type_check_only
class VideoMetadata(typing_extensions.TypedDict, total=False):
    duration: str
    isValidVast: bool
    isVpaid: bool
    mediaFiles: _list[MediaFile]
    skipOffset: str
    vastVersion: typing_extensions.Literal[
        "VAST_VERSION_UNSPECIFIED",
        "VAST_VERSION_1_0",
        "VAST_VERSION_2_0",
        "VAST_VERSION_3_0",
        "VAST_VERSION_4_0",
    ]

@typing.type_check_only
class WatchCreativesRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WatchCreativesResponse(typing_extensions.TypedDict, total=False):
    subscription: str
    topic: str
