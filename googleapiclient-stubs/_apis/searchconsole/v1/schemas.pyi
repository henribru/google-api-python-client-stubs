import typing

import typing_extensions

class WmxSite(typing_extensions.TypedDict, total=False):
    permissionLevel: typing_extensions.Literal[
        "SITE_PERMISSION_LEVEL_UNSPECIFIED",
        "SITE_OWNER",
        "SITE_FULL_USER",
        "SITE_RESTRICTED_USER",
        "SITE_UNVERIFIED_USER",
    ]
    siteUrl: str

class WmxSitemapContent(typing_extensions.TypedDict, total=False):
    indexed: str
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
    submitted: str

class WmxSitemap(typing_extensions.TypedDict, total=False):
    warnings: str
    contents: typing.List[WmxSitemapContent]
    isPending: bool
    lastSubmitted: str
    path: str
    isSitemapsIndex: bool
    type: typing_extensions.Literal[
        "NOT_SITEMAP",
        "URL_LIST",
        "SITEMAP",
        "RSS_FEED",
        "ATOM_FEED",
        "PATTERN_SITEMAP",
        "OCEANFRONT",
    ]
    lastDownloaded: str
    errors: str

class SearchAnalyticsQueryRequest(typing_extensions.TypedDict, total=False):
    dimensionFilterGroups: typing.List[ApiDimensionFilterGroup]
    aggregationType: typing_extensions.Literal["AUTO", "BY_PROPERTY", "BY_PAGE"]
    rowLimit: int
    dimensions: typing.List[str]
    startDate: str
    startRow: int
    endDate: str
    searchType: typing_extensions.Literal["WEB", "IMAGE", "VIDEO"]

class SitemapsListResponse(typing_extensions.TypedDict, total=False):
    sitemap: typing.List[WmxSitemap]

class ResourceIssue(typing_extensions.TypedDict, total=False):
    blockedResource: BlockedResource

class Image(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

class TestStatus(typing_extensions.TypedDict, total=False):
    details: str
    status: typing_extensions.Literal[
        "TEST_STATUS_UNSPECIFIED", "COMPLETE", "INTERNAL_ERROR", "PAGE_UNREACHABLE"
    ]

class ApiDimensionFilterGroup(typing_extensions.TypedDict, total=False):
    groupType: typing_extensions.Literal["AND"]
    filters: typing.List[ApiDimensionFilter]

class SitesListResponse(typing_extensions.TypedDict, total=False):
    siteEntry: typing.List[WmxSite]

class BlockedResource(typing_extensions.TypedDict, total=False):
    url: str

class RunMobileFriendlyTestRequest(typing_extensions.TypedDict, total=False):
    url: str
    requestScreenshot: bool

class ApiDimensionFilter(typing_extensions.TypedDict, total=False):
    operator: typing_extensions.Literal[
        "EQUALS", "NOT_EQUALS", "CONTAINS", "NOT_CONTAINS"
    ]
    dimension: typing_extensions.Literal[
        "QUERY", "PAGE", "COUNTRY", "DEVICE", "SEARCH_APPEARANCE"
    ]
    expression: str

class SearchAnalyticsQueryResponse(typing_extensions.TypedDict, total=False):
    responseAggregationType: typing_extensions.Literal["AUTO", "BY_PROPERTY", "BY_PAGE"]
    rows: typing.List[ApiDataRow]

class ApiDataRow(typing_extensions.TypedDict, total=False):
    impressions: float
    keys: typing.List[str]
    position: float
    clicks: float
    ctr: float

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

class RunMobileFriendlyTestResponse(typing_extensions.TypedDict, total=False):
    mobileFriendlyIssues: typing.List[MobileFriendlyIssue]
    screenshot: Image
    resourceIssues: typing.List[ResourceIssue]
    mobileFriendliness: typing_extensions.Literal[
        "MOBILE_FRIENDLY_TEST_RESULT_UNSPECIFIED",
        "MOBILE_FRIENDLY",
        "NOT_MOBILE_FRIENDLY",
    ]
    testStatus: TestStatus
