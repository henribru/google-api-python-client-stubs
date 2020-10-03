import typing

import typing_extensions

class ApiDataRow(typing_extensions.TypedDict, total=False):
    clicks: float
    ctr: float
    impressions: float
    keys: typing.List[str]
    position: float

class ApiDimensionFilter(typing_extensions.TypedDict, total=False):
    dimension: str
    expression: str
    operator: str

class ApiDimensionFilterGroup(typing_extensions.TypedDict, total=False):
    filters: typing.List[ApiDimensionFilter]
    groupType: str

class SearchAnalyticsQueryRequest(typing_extensions.TypedDict, total=False):
    aggregationType: str
    dimensionFilterGroups: typing.List[ApiDimensionFilterGroup]
    dimensions: typing.List[str]
    endDate: str
    rowLimit: int
    searchType: str
    startDate: str
    startRow: int

class SearchAnalyticsQueryResponse(typing_extensions.TypedDict, total=False):
    responseAggregationType: str
    rows: typing.List[ApiDataRow]

class SitemapsListResponse(typing_extensions.TypedDict, total=False):
    sitemap: typing.List[WmxSitemap]

class SitesListResponse(typing_extensions.TypedDict, total=False):
    siteEntry: typing.List[WmxSite]

class WmxSite(typing_extensions.TypedDict, total=False):
    permissionLevel: str
    siteUrl: str

class WmxSitemap(typing_extensions.TypedDict, total=False):
    contents: typing.List[WmxSitemapContent]
    errors: str
    isPending: bool
    isSitemapsIndex: bool
    lastDownloaded: str
    lastSubmitted: str
    path: str
    type: str
    warnings: str

class WmxSitemapContent(typing_extensions.TypedDict, total=False):
    indexed: str
    submitted: str
    type: str
