import typing

_list = list

@typing.type_check_only
class ApiDataRow(typing.TypedDict, total=False):
    clicks: float
    ctr: float
    impressions: float
    keys: _list[str]
    position: float

@typing.type_check_only
class ApiDimensionFilter(typing.TypedDict, total=False):
    dimension: str
    expression: str
    operator: str

@typing.type_check_only
class ApiDimensionFilterGroup(typing.TypedDict, total=False):
    filters: _list[ApiDimensionFilter]
    groupType: str

@typing.type_check_only
class SearchAnalyticsQueryRequest(typing.TypedDict, total=False):
    aggregationType: str
    dataState: str
    dimensionFilterGroups: _list[ApiDimensionFilterGroup]
    dimensions: _list[str]
    endDate: str
    rowLimit: int
    searchType: str
    startDate: str
    startRow: int

@typing.type_check_only
class SearchAnalyticsQueryResponse(typing.TypedDict, total=False):
    responseAggregationType: str
    rows: _list[ApiDataRow]

@typing.type_check_only
class SitemapsListResponse(typing.TypedDict, total=False):
    sitemap: _list[WmxSitemap]

@typing.type_check_only
class SitesListResponse(typing.TypedDict, total=False):
    siteEntry: _list[WmxSite]

@typing.type_check_only
class WmxSite(typing.TypedDict, total=False):
    permissionLevel: str
    siteUrl: str

@typing.type_check_only
class WmxSitemap(typing.TypedDict, total=False):
    contents: _list[WmxSitemapContent]
    errors: str
    isPending: bool
    isSitemapsIndex: bool
    lastDownloaded: str
    lastSubmitted: str
    path: str
    type: str
    warnings: str

@typing.type_check_only
class WmxSitemapContent(typing.TypedDict, total=False):
    indexed: str
    submitted: str
    type: str
