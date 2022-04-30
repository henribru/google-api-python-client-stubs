import typing

import typing_extensions

_list = list

@typing.type_check_only
class AmpInspectionResult(typing_extensions.TypedDict, total=False):
    ampIndexStatusVerdict: typing_extensions.Literal[
        "VERDICT_UNSPECIFIED", "PASS", "PARTIAL", "FAIL", "NEUTRAL"
    ]
    ampUrl: str
    indexingState: typing_extensions.Literal[
        "AMP_INDEXING_STATE_UNSPECIFIED",
        "AMP_INDEXING_ALLOWED",
        "BLOCKED_DUE_TO_NOINDEX",
        "BLOCKED_DUE_TO_EXPIRED_UNAVAILABLE_AFTER",
    ]
    issues: _list[AmpIssue]
    lastCrawlTime: str
    pageFetchState: typing_extensions.Literal[
        "PAGE_FETCH_STATE_UNSPECIFIED",
        "SUCCESSFUL",
        "SOFT_404",
        "BLOCKED_ROBOTS_TXT",
        "NOT_FOUND",
        "ACCESS_DENIED",
        "SERVER_ERROR",
        "REDIRECT_ERROR",
        "ACCESS_FORBIDDEN",
        "BLOCKED_4XX",
        "INTERNAL_CRAWL_ERROR",
        "INVALID_URL",
    ]
    robotsTxtState: typing_extensions.Literal[
        "ROBOTS_TXT_STATE_UNSPECIFIED", "ALLOWED", "DISALLOWED"
    ]
    verdict: typing_extensions.Literal[
        "VERDICT_UNSPECIFIED", "PASS", "PARTIAL", "FAIL", "NEUTRAL"
    ]

@typing.type_check_only
class AmpIssue(typing_extensions.TypedDict, total=False):
    issueMessage: str
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "WARNING", "ERROR"]

@typing.type_check_only
class ApiDataRow(typing_extensions.TypedDict, total=False):
    clicks: float
    ctr: float
    impressions: float
    keys: _list[str]
    position: float

@typing.type_check_only
class ApiDimensionFilter(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal[
        "QUERY", "PAGE", "COUNTRY", "DEVICE", "SEARCH_APPEARANCE"
    ]
    expression: str
    operator: typing_extensions.Literal[
        "EQUALS",
        "NOT_EQUALS",
        "CONTAINS",
        "NOT_CONTAINS",
        "INCLUDING_REGEX",
        "EXCLUDING_REGEX",
    ]

@typing.type_check_only
class ApiDimensionFilterGroup(typing_extensions.TypedDict, total=False):
    filters: _list[ApiDimensionFilter]
    groupType: typing_extensions.Literal["AND"]

@typing.type_check_only
class BlockedResource(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class DetectedItems(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    richResultType: str

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

@typing.type_check_only
class IndexStatusInspectionResult(typing_extensions.TypedDict, total=False):
    coverageState: str
    crawledAs: typing_extensions.Literal[
        "CRAWLING_USER_AGENT_UNSPECIFIED", "DESKTOP", "MOBILE"
    ]
    googleCanonical: str
    indexingState: typing_extensions.Literal[
        "INDEXING_STATE_UNSPECIFIED",
        "INDEXING_ALLOWED",
        "BLOCKED_BY_META_TAG",
        "BLOCKED_BY_HTTP_HEADER",
        "BLOCKED_BY_ROBOTS_TXT",
    ]
    lastCrawlTime: str
    pageFetchState: typing_extensions.Literal[
        "PAGE_FETCH_STATE_UNSPECIFIED",
        "SUCCESSFUL",
        "SOFT_404",
        "BLOCKED_ROBOTS_TXT",
        "NOT_FOUND",
        "ACCESS_DENIED",
        "SERVER_ERROR",
        "REDIRECT_ERROR",
        "ACCESS_FORBIDDEN",
        "BLOCKED_4XX",
        "INTERNAL_CRAWL_ERROR",
        "INVALID_URL",
    ]
    referringUrls: _list[str]
    robotsTxtState: typing_extensions.Literal[
        "ROBOTS_TXT_STATE_UNSPECIFIED", "ALLOWED", "DISALLOWED"
    ]
    sitemap: _list[str]
    userCanonical: str
    verdict: typing_extensions.Literal[
        "VERDICT_UNSPECIFIED", "PASS", "PARTIAL", "FAIL", "NEUTRAL"
    ]

@typing.type_check_only
class InspectUrlIndexRequest(typing_extensions.TypedDict, total=False):
    inspectionUrl: str
    languageCode: str
    siteUrl: str

@typing.type_check_only
class InspectUrlIndexResponse(typing_extensions.TypedDict, total=False):
    inspectionResult: UrlInspectionResult

@typing.type_check_only
class Item(typing_extensions.TypedDict, total=False):
    issues: _list[RichResultsIssue]
    name: str

@typing.type_check_only
class MobileFriendlyIssue(typing_extensions.TypedDict, total=False):
    rule: typing_extensions.Literal[
        "MOBILE_FRIENDLY_RULE_UNSPECIFIED",
        "USES_INCOMPATIBLE_PLUGINS",
        "CONFIGURE_VIEWPORT",
        "FIXED_WIDTH_VIEWPORT",
        "SIZE_CONTENT_TO_VIEWPORT",
        "USE_LEGIBLE_FONT_SIZES",
        "TAP_TARGETS_TOO_CLOSE",
    ]

@typing.type_check_only
class MobileUsabilityInspectionResult(typing_extensions.TypedDict, total=False):
    issues: _list[MobileUsabilityIssue]
    verdict: typing_extensions.Literal[
        "VERDICT_UNSPECIFIED", "PASS", "PARTIAL", "FAIL", "NEUTRAL"
    ]

@typing.type_check_only
class MobileUsabilityIssue(typing_extensions.TypedDict, total=False):
    issueType: typing_extensions.Literal[
        "MOBILE_USABILITY_ISSUE_TYPE_UNSPECIFIED",
        "USES_INCOMPATIBLE_PLUGINS",
        "CONFIGURE_VIEWPORT",
        "FIXED_WIDTH_VIEWPORT",
        "SIZE_CONTENT_TO_VIEWPORT",
        "USE_LEGIBLE_FONT_SIZES",
        "TAP_TARGETS_TOO_CLOSE",
    ]
    message: str
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "WARNING", "ERROR"]

@typing.type_check_only
class ResourceIssue(typing_extensions.TypedDict, total=False):
    blockedResource: BlockedResource

@typing.type_check_only
class RichResultsInspectionResult(typing_extensions.TypedDict, total=False):
    detectedItems: _list[DetectedItems]
    verdict: typing_extensions.Literal[
        "VERDICT_UNSPECIFIED", "PASS", "PARTIAL", "FAIL", "NEUTRAL"
    ]

@typing.type_check_only
class RichResultsIssue(typing_extensions.TypedDict, total=False):
    issueMessage: str
    severity: typing_extensions.Literal["SEVERITY_UNSPECIFIED", "WARNING", "ERROR"]

@typing.type_check_only
class RunMobileFriendlyTestRequest(typing_extensions.TypedDict, total=False):
    requestScreenshot: bool
    url: str

@typing.type_check_only
class RunMobileFriendlyTestResponse(typing_extensions.TypedDict, total=False):
    mobileFriendliness: typing_extensions.Literal[
        "MOBILE_FRIENDLY_TEST_RESULT_UNSPECIFIED",
        "MOBILE_FRIENDLY",
        "NOT_MOBILE_FRIENDLY",
    ]
    mobileFriendlyIssues: _list[MobileFriendlyIssue]
    resourceIssues: _list[ResourceIssue]
    screenshot: Image
    testStatus: TestStatus

@typing.type_check_only
class SearchAnalyticsQueryRequest(typing_extensions.TypedDict, total=False):
    aggregationType: typing_extensions.Literal["AUTO", "BY_PROPERTY", "BY_PAGE"]
    dataState: typing_extensions.Literal["DATA_STATE_UNSPECIFIED", "FINAL", "ALL"]
    dimensionFilterGroups: _list[ApiDimensionFilterGroup]
    dimensions: _list[str]
    endDate: str
    rowLimit: int
    searchType: typing_extensions.Literal[
        "WEB", "IMAGE", "VIDEO", "NEWS", "DISCOVER", "GOOGLE_NEWS"
    ]
    startDate: str
    startRow: int
    type: typing_extensions.Literal[
        "WEB", "IMAGE", "VIDEO", "NEWS", "DISCOVER", "GOOGLE_NEWS"
    ]

@typing.type_check_only
class SearchAnalyticsQueryResponse(typing_extensions.TypedDict, total=False):
    responseAggregationType: typing_extensions.Literal["AUTO", "BY_PROPERTY", "BY_PAGE"]
    rows: _list[ApiDataRow]

@typing.type_check_only
class SitemapsListResponse(typing_extensions.TypedDict, total=False):
    sitemap: _list[WmxSitemap]

@typing.type_check_only
class SitesListResponse(typing_extensions.TypedDict, total=False):
    siteEntry: _list[WmxSite]

@typing.type_check_only
class TestStatus(typing_extensions.TypedDict, total=False):
    details: str
    status: typing_extensions.Literal[
        "TEST_STATUS_UNSPECIFIED", "COMPLETE", "INTERNAL_ERROR", "PAGE_UNREACHABLE"
    ]

@typing.type_check_only
class UrlInspectionResult(typing_extensions.TypedDict, total=False):
    ampResult: AmpInspectionResult
    indexStatusResult: IndexStatusInspectionResult
    inspectionResultLink: str
    mobileUsabilityResult: MobileUsabilityInspectionResult
    richResultsResult: RichResultsInspectionResult

@typing.type_check_only
class WmxSite(typing_extensions.TypedDict, total=False):
    permissionLevel: typing_extensions.Literal[
        "SITE_PERMISSION_LEVEL_UNSPECIFIED",
        "SITE_OWNER",
        "SITE_FULL_USER",
        "SITE_RESTRICTED_USER",
        "SITE_UNVERIFIED_USER",
    ]
    siteUrl: str

@typing.type_check_only
class WmxSitemap(typing_extensions.TypedDict, total=False):
    contents: _list[WmxSitemapContent]
    errors: str
    isPending: bool
    isSitemapsIndex: bool
    lastDownloaded: str
    lastSubmitted: str
    path: str
    type: typing_extensions.Literal[
        "NOT_SITEMAP",
        "URL_LIST",
        "SITEMAP",
        "RSS_FEED",
        "ATOM_FEED",
        "PATTERN_SITEMAP",
        "OCEANFRONT",
    ]
    warnings: str

@typing.type_check_only
class WmxSitemapContent(typing_extensions.TypedDict, total=False):
    indexed: str
    submitted: str
    type: typing_extensions.Literal[
        "WEB",
        "IMAGE",
        "VIDEO",
        "NEWS",
        "MOBILE",
        "ANDROID_APP",
        "PATTERN",
        "IOS_APP",
        "DATA_FEED_ELEMENT",
    ]
