import typing

import typing_extensions

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    pendingTasks: typing.List[str]
    premium: bool
    timeZone: TimeZone

@typing.type_check_only
class AdClient(typing_extensions.TypedDict, total=False):
    name: str
    productCode: str
    reportingDimensionId: str

@typing.type_check_only
class AdClientAdCode(typing_extensions.TypedDict, total=False):
    adCode: str
    ampBody: str
    ampHead: str

@typing.type_check_only
class AdUnit(typing_extensions.TypedDict, total=False):
    contentAdsSettings: ContentAdsSettings
    displayName: str
    name: str
    reportingDimensionId: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED"]

@typing.type_check_only
class AdUnitAdCode(typing_extensions.TypedDict, total=False):
    adCode: str

@typing.type_check_only
class Alert(typing_extensions.TypedDict, total=False):
    message: str
    name: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "SEVERE"
    ]
    type: str

@typing.type_check_only
class Cell(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class ContentAdsSettings(typing_extensions.TypedDict, total=False):
    size: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "DISPLAY", "FEED", "ARTICLE", "MATCHED_CONTENT", "LINK"
    ]

@typing.type_check_only
class CustomChannel(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    reportingDimensionId: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    currencyCode: str
    name: str
    type: typing_extensions.Literal[
        "HEADER_TYPE_UNSPECIFIED",
        "DIMENSION",
        "METRIC_TALLY",
        "METRIC_RATIO",
        "METRIC_CURRENCY",
        "METRIC_MILLISECONDS",
        "METRIC_DECIMAL",
    ]

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: typing.List[Account]
    nextPageToken: str

@typing.type_check_only
class ListAdClientsResponse(typing_extensions.TypedDict, total=False):
    adClients: typing.List[AdClient]
    nextPageToken: str

@typing.type_check_only
class ListAdUnitsResponse(typing_extensions.TypedDict, total=False):
    adUnits: typing.List[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListAlertsResponse(typing_extensions.TypedDict, total=False):
    alerts: typing.List[Alert]

@typing.type_check_only
class ListChildAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: typing.List[Account]
    nextPageToken: str

@typing.type_check_only
class ListCustomChannelsResponse(typing_extensions.TypedDict, total=False):
    customChannels: typing.List[CustomChannel]
    nextPageToken: str

@typing.type_check_only
class ListLinkedAdUnitsResponse(typing_extensions.TypedDict, total=False):
    adUnits: typing.List[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListLinkedCustomChannelsResponse(typing_extensions.TypedDict, total=False):
    customChannels: typing.List[CustomChannel]
    nextPageToken: str

@typing.type_check_only
class ListPaymentsResponse(typing_extensions.TypedDict, total=False):
    payments: typing.List[Payment]

@typing.type_check_only
class ListSavedReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    savedReports: typing.List[SavedReport]

@typing.type_check_only
class ListSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sites: typing.List[Site]

@typing.type_check_only
class ListUrlChannelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    urlChannels: typing.List[UrlChannel]

@typing.type_check_only
class Payment(typing_extensions.TypedDict, total=False):
    amount: str
    date: Date
    name: str

@typing.type_check_only
class ReportResult(typing_extensions.TypedDict, total=False):
    averages: Row
    endDate: Date
    headers: typing.List[Header]
    rows: typing.List[Row]
    startDate: Date
    totalMatchedRows: str
    totals: Row
    warnings: typing.List[str]

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    cells: typing.List[Cell]

@typing.type_check_only
class SavedReport(typing_extensions.TypedDict, total=False):
    name: str
    title: str

@typing.type_check_only
class Site(typing_extensions.TypedDict, total=False):
    autoAdsEnabled: bool
    domain: str
    name: str
    reportingDimensionId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REQUIRES_REVIEW",
        "GETTING_READY",
        "READY",
        "NEEDS_ATTENTION",
    ]

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class UrlChannel(typing_extensions.TypedDict, total=False):
    name: str
    reportingDimensionId: str
    uriPattern: str
