import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    pendingTasks: _list[str]
    premium: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "READY", "NEEDS_ATTENTION", "CLOSED"
    ]
    timeZone: TimeZone

@typing.type_check_only
class AdBlockingRecoveryTag(typing_extensions.TypedDict, total=False):
    errorProtectionCode: str
    tag: str

@typing.type_check_only
class AdClient(typing_extensions.TypedDict, total=False):
    name: str
    productCode: str
    reportingDimensionId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "READY", "GETTING_READY", "REQUIRES_REVIEW"
    ]

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
    active: bool
    displayName: str
    name: str
    reportingDimensionId: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

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
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListAdClientsResponse(typing_extensions.TypedDict, total=False):
    adClients: _list[AdClient]
    nextPageToken: str

@typing.type_check_only
class ListAdUnitsResponse(typing_extensions.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListAlertsResponse(typing_extensions.TypedDict, total=False):
    alerts: _list[Alert]

@typing.type_check_only
class ListChildAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListCustomChannelsResponse(typing_extensions.TypedDict, total=False):
    customChannels: _list[CustomChannel]
    nextPageToken: str

@typing.type_check_only
class ListLinkedAdUnitsResponse(typing_extensions.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListLinkedCustomChannelsResponse(typing_extensions.TypedDict, total=False):
    customChannels: _list[CustomChannel]
    nextPageToken: str

@typing.type_check_only
class ListPaymentsResponse(typing_extensions.TypedDict, total=False):
    payments: _list[Payment]

@typing.type_check_only
class ListSavedReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    savedReports: _list[SavedReport]

@typing.type_check_only
class ListSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class ListUrlChannelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    urlChannels: _list[UrlChannel]

@typing.type_check_only
class Payment(typing_extensions.TypedDict, total=False):
    amount: str
    date: Date
    name: str

@typing.type_check_only
class ReportResult(typing_extensions.TypedDict, total=False):
    averages: Row
    endDate: Date
    headers: _list[Header]
    rows: _list[Row]
    startDate: Date
    totalMatchedRows: str
    totals: Row
    warnings: _list[str]

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    cells: _list[Cell]

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
