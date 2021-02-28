import typing

import typing_extensions
@typing.type_check_only
class ApiDataRow(typing_extensions.TypedDict, total=False):
    clicks: float
    ctr: float
    impressions: float
    keys: typing.List[str]
    position: float

@typing.type_check_only
class ApiDimensionFilter(typing_extensions.TypedDict, total=False):
    dimension: typing_extensions.Literal[
        "QUERY", "PAGE", "COUNTRY", "DEVICE", "SEARCH_APPEARANCE"
    ]
    expression: str
    operator: typing_extensions.Literal[
        "EQUALS", "NOT_EQUALS", "CONTAINS", "NOT_CONTAINS"
    ]

@typing.type_check_only
class ApiDimensionFilterGroup(typing_extensions.TypedDict, total=False):
    filters: typing.List[ApiDimensionFilter]
    groupType: typing_extensions.Literal["AND"]

@typing.type_check_only
class BlockedResource(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    data: str
    mimeType: str

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
class ResourceIssue(typing_extensions.TypedDict, total=False):
    blockedResource: BlockedResource

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
    mobileFriendlyIssues: typing.List[MobileFriendlyIssue]
    resourceIssues: typing.List[ResourceIssue]
    screenshot: Image
    testStatus: TestStatus

@typing.type_check_only
class SearchAnalyticsQueryRequest(typing_extensions.TypedDict, total=False):
    aggregationType: typing_extensions.Literal["AUTO", "BY_PROPERTY", "BY_PAGE"]
    dataState: typing_extensions.Literal["DATA_STATE_UNSPECIFIED", "FINAL", "ALL"]
    dimensionFilterGroups: typing.List[ApiDimensionFilterGroup]
    dimensions: typing.List[str]
    endDate: str
    rowLimit: int
    searchType: typing_extensions.Literal["WEB", "IMAGE", "VIDEO", "NEWS"]
    startDate: str
    startRow: int

@typing.type_check_only
class SearchAnalyticsQueryResponse(typing_extensions.TypedDict, total=False):
    responseAggregationType: typing_extensions.Literal["AUTO", "BY_PROPERTY", "BY_PAGE"]
    rows: typing.List[ApiDataRow]

@typing.type_check_only
class SitemapsListResponse(typing_extensions.TypedDict, total=False):
    sitemap: typing.List[WmxSitemap]

@typing.type_check_only
class SitesListResponse(typing_extensions.TypedDict, total=False):
    siteEntry: typing.List[WmxSite]

@typing.type_check_only
class TestStatus(typing_extensions.TypedDict, total=False):
    details: str
    status: typing_extensions.Literal[
        "TEST_STATUS_UNSPECIFIED", "COMPLETE", "INTERNAL_ERROR", "PAGE_UNREACHABLE"
    ]

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
    contents: typing.List[WmxSitemapContent]
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
