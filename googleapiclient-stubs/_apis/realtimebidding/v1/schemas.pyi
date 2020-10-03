import typing

import typing_extensions

class ListUserListsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userLists: typing.List[UserList]

class DomainCalls(typing_extensions.TypedDict, total=False):
    httpCallCount: int
    domain: str

class OpenUserListRequest(typing_extensions.TypedDict, total=False): ...

class AdvertiserAndBrand(typing_extensions.TypedDict, total=False):
    advertiserId: str
    advertiserName: str
    brandName: str
    brandId: str

class UserList(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    description: str
    urlRestriction: UrlRestriction
    membershipDurationDays: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "OPEN", "CLOSED"]

class CreativeServingDecision(typing_extensions.TypedDict, total=False):
    dealsServingStatus: ServingStatus
    openAuctionServingStatus: ServingStatus
    detectedDomains: typing.List[str]
    detectedAdvertisers: typing.List[AdvertiserAndBrand]
    detectedClickThroughUrls: typing.List[str]
    detectedProductCategories: typing.List[int]
    detectedLanguages: typing.List[str]
    adTechnologyProviders: AdTechnologyProviders
    russiaServingStatus: ServingStatus
    chinaServingStatus: ServingStatus
    detectedVendorIds: typing.List[int]
    detectedAttributes: typing.List[str]
    lastStatusUpdate: str
    detectedSensitiveCategories: typing.List[int]

class Date(typing_extensions.TypedDict, total=False):
    day: int
    year: int
    month: int

class MediaFile(typing_extensions.TypedDict, total=False):
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
    bitrate: str

class ListCreativesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    creatives: typing.List[Creative]

class DestinationUrlEvidence(typing_extensions.TypedDict, total=False):
    destinationUrl: str

class DestinationNotWorkingEvidence(typing_extensions.TypedDict, total=False):
    dnsError: typing_extensions.Literal[
        "DNS_ERROR_UNSPECIFIED", "ERROR_DNS", "GOOGLE_CRAWLER_DNS_ISSUE"
    ]
    lastCheckTime: str
    urlRejected: typing_extensions.Literal[
        "URL_REJECTED_UNSPECIFIED",
        "BAD_REQUEST",
        "MALFORMED_URL",
        "URL_REJECTED_UNKNOWN",
    ]
    redirectionError: typing_extensions.Literal[
        "REDIRECTION_ERROR_UNSPECIFIED",
        "TOO_MANY_REDIRECTS",
        "INVALID_REDIRECT",
        "EMPTY_REDIRECT",
        "REDIRECT_ERROR_UNKNOWN",
    ]
    platform: typing_extensions.Literal[
        "PLATFORM_UNSPECIFIED", "PERSONAL_COMPUTER", "ANDROID", "IOS"
    ]
    invalidPage: typing_extensions.Literal[
        "INVALID_PAGE_UNSPECIFIED", "EMPTY_OR_ERROR_PAGE"
    ]
    httpError: int
    expandedUrl: str

class HttpCallEvidence(typing_extensions.TypedDict, total=False):
    urls: typing.List[str]

class HtmlContent(typing_extensions.TypedDict, total=False):
    snippet: str
    height: int
    width: int

class AdTechnologyProviders(typing_extensions.TypedDict, total=False):
    detectedProviderIds: typing.List[str]
    hasUnidentifiedProvider: bool

class PolicyTopicEvidence(typing_extensions.TypedDict, total=False):
    downloadSize: DownloadSizeEvidence
    httpCall: HttpCallEvidence
    domainCall: DomainCallEvidence
    httpCookie: HttpCookieEvidence
    destinationNotCrawlable: DestinationNotCrawlableEvidence
    destinationNotWorking: DestinationNotWorkingEvidence
    destinationUrl: DestinationUrlEvidence

class DownloadSizeEvidence(typing_extensions.TypedDict, total=False):
    totalDownloadSizeKb: int
    topUrlDownloadSizeBreakdowns: typing.List[UrlDownloadSize]

class Creative(typing_extensions.TypedDict, total=False):
    creativeId: str
    accountId: str
    apiUpdateTime: str
    adChoicesDestinationUrl: str
    restrictedCategories: typing.List[str]
    creativeServingDecision: CreativeServingDecision
    html: HtmlContent
    creativeFormat: typing_extensions.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "HTML", "VIDEO", "NATIVE"
    ]
    agencyId: str
    declaredVendorIds: typing.List[int]
    video: VideoContent
    native: NativeContent
    declaredRestrictedCategories: typing.List[str]
    version: int
    advertiserName: str
    declaredAttributes: typing.List[str]
    impressionTrackingUrls: typing.List[str]
    declaredClickThroughUrls: typing.List[str]
    name: str
    dealIds: typing.List[str]

class UrlDownloadSize(typing_extensions.TypedDict, total=False):
    downloadSizeKb: int
    normalizedUrl: str

class GetRemarketingTagResponse(typing_extensions.TypedDict, total=False):
    snippet: str

class UrlRestriction(typing_extensions.TypedDict, total=False):
    startDate: Date
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
    url: str

class DestinationNotCrawlableEvidence(typing_extensions.TypedDict, total=False):
    crawlTime: str
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED",
        "UNREACHABLE_ROBOTS",
        "TIMEOUT_ROBOTS",
        "ROBOTED_DENIED",
        "UNKNOWN",
    ]
    crawledUrl: str

class PolicyTopicEntry(typing_extensions.TypedDict, total=False):
    helpCenterUrl: str
    policyTopic: str
    evidences: typing.List[PolicyTopicEvidence]

class VideoContent(typing_extensions.TypedDict, total=False):
    videoVastXml: str
    videoUrl: str
    videoMetadata: VideoMetadata

class VideoMetadata(typing_extensions.TypedDict, total=False):
    duration: str
    vastVersion: typing_extensions.Literal[
        "VAST_VERSION_UNSPECIFIED",
        "VAST_VERSION_1_0",
        "VAST_VERSION_2_0",
        "VAST_VERSION_3_0",
        "VAST_VERSION_4_0",
    ]
    skipOffset: str
    isValidVast: bool
    mediaFiles: typing.List[MediaFile]
    isVpaid: bool

class ServingStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "PENDING_REVIEW", "DISAPPROVED", "APPROVED"
    ]
    topics: typing.List[PolicyTopicEntry]

class WatchCreativesRequest(typing_extensions.TypedDict, total=False): ...
class CloseUserListRequest(typing_extensions.TypedDict, total=False): ...

class Image(typing_extensions.TypedDict, total=False):
    height: int
    width: int
    url: str

class HttpCookieEvidence(typing_extensions.TypedDict, total=False):
    cookieNames: typing.List[str]
    maxCookieCount: int

class NativeContent(typing_extensions.TypedDict, total=False):
    priceDisplayText: str
    advertiserName: str
    clickLinkUrl: str
    appIcon: Image
    image: Image
    headline: str
    logo: Image
    starRating: float
    clickTrackingUrl: str
    videoUrl: str
    callToAction: str
    body: str

class WatchCreativesResponse(typing_extensions.TypedDict, total=False):
    topic: str
    subscription: str

class DomainCallEvidence(typing_extensions.TypedDict, total=False):
    totalHttpCallCount: int
    topHttpCallDomains: typing.List[DomainCalls]
