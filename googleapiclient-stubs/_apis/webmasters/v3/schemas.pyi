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
    dimension: str
    expression: str
    operator: str

@typing.type_check_only
class ApiDimensionFilterGroup(typing_extensions.TypedDict, total=False):
    filters: typing.List[ApiDimensionFilter]
    groupType: str

@typing.type_check_only
class SearchAnalyticsQueryRequest(typing_extensions.TypedDict, total=False):
    aggregationType: str
    dataState: str
    dimensionFilterGroups: typing.List[ApiDimensionFilterGroup]
    dimensions: typing.List[str]
    endDate: str
    rowLimit: int
    searchType: str
    startDate: str
    startRow: int

@typing.type_check_only
class SearchAnalyticsQueryResponse(typing_extensions.TypedDict, total=False):
    responseAggregationType: str
    rows: typing.List[ApiDataRow]

@typing.type_check_only
class SitemapsListResponse(typing_extensions.TypedDict, total=False):
    sitemap: typing.List[WmxSitemap]

@typing.type_check_only
class SitesListResponse(typing_extensions.TypedDict, total=False):
    siteEntry: typing.List[WmxSite]

@typing.type_check_only
class WmxSite(typing_extensions.TypedDict, total=False):
    permissionLevel: str
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
    type: str
    warnings: str

@typing.type_check_only
class WmxSitemapContent(typing_extensions.TypedDict, total=False):
    indexed: str
    submitted: str
    type: str
