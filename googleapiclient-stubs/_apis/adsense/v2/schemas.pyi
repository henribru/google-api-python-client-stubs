import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    pendingTasks: _list[str]
    premium: bool
    state: typing.Literal["STATE_UNSPECIFIED", "READY", "NEEDS_ATTENTION", "CLOSED"]
    timeZone: TimeZone

@typing.type_check_only
class AdBlockingRecoveryTag(typing.TypedDict, total=False):
    errorProtectionCode: str
    tag: str

@typing.type_check_only
class AdClient(typing.TypedDict, total=False):
    name: str
    productCode: str
    reportingDimensionId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "READY", "GETTING_READY", "REQUIRES_REVIEW"
    ]

@typing.type_check_only
class AdClientAdCode(typing.TypedDict, total=False):
    adCode: str
    ampBody: str
    ampHead: str

@typing.type_check_only
class AdUnit(typing.TypedDict, total=False):
    contentAdsSettings: ContentAdsSettings
    displayName: str
    name: str
    reportingDimensionId: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED"]

@typing.type_check_only
class AdUnitAdCode(typing.TypedDict, total=False):
    adCode: str

@typing.type_check_only
class Alert(typing.TypedDict, total=False):
    message: str
    name: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "INFO", "WARNING", "SEVERE"]
    type: str

@typing.type_check_only
class Cell(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class ContentAdsSettings(typing.TypedDict, total=False):
    size: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "DISPLAY", "FEED", "ARTICLE", "MATCHED_CONTENT", "LINK"
    ]

@typing.type_check_only
class CustomChannel(typing.TypedDict, total=False):
    active: bool
    displayName: str
    name: str
    reportingDimensionId: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Header(typing.TypedDict, total=False):
    currencyCode: str
    name: str
    type: typing.Literal[
        "HEADER_TYPE_UNSPECIFIED",
        "DIMENSION",
        "METRIC_TALLY",
        "METRIC_RATIO",
        "METRIC_CURRENCY",
        "METRIC_MILLISECONDS",
        "METRIC_DECIMAL",
    ]

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListAdClientsResponse(typing.TypedDict, total=False):
    adClients: _list[AdClient]
    nextPageToken: str

@typing.type_check_only
class ListAdUnitsResponse(typing.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListAlertsResponse(typing.TypedDict, total=False):
    alerts: _list[Alert]

@typing.type_check_only
class ListChildAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListCustomChannelsResponse(typing.TypedDict, total=False):
    customChannels: _list[CustomChannel]
    nextPageToken: str

@typing.type_check_only
class ListLinkedAdUnitsResponse(typing.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListLinkedCustomChannelsResponse(typing.TypedDict, total=False):
    customChannels: _list[CustomChannel]
    nextPageToken: str

@typing.type_check_only
class ListPaymentsResponse(typing.TypedDict, total=False):
    payments: _list[Payment]

@typing.type_check_only
class ListPolicyIssuesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    policyIssues: _list[PolicyIssue]

@typing.type_check_only
class ListSavedReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    savedReports: _list[SavedReport]

@typing.type_check_only
class ListSitesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class ListUrlChannelsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    urlChannels: _list[UrlChannel]

@typing.type_check_only
class Payment(typing.TypedDict, total=False):
    amount: str
    date: Date
    name: str

@typing.type_check_only
class PolicyIssue(typing.TypedDict, total=False):
    action: typing.Literal[
        "ENFORCEMENT_ACTION_UNSPECIFIED",
        "WARNED",
        "AD_SERVING_RESTRICTED",
        "AD_SERVING_DISABLED",
        "AD_SERVED_WITH_CLICK_CONFIRMATION",
        "AD_PERSONALIZATION_RESTRICTED",
    ]
    adClients: _list[str]
    adRequestCount: str
    entityType: typing.Literal[
        "ENTITY_TYPE_UNSPECIFIED", "SITE", "SITE_SECTION", "PAGE"
    ]
    firstDetectedDate: Date
    lastDetectedDate: Date
    name: str
    policyTopics: _list[PolicyTopic]
    site: str
    siteSection: str
    uri: str
    warningEscalationDate: Date

@typing.type_check_only
class PolicyTopic(typing.TypedDict, total=False):
    mustFix: bool
    topic: str
    type: typing.Literal[
        "POLICY_TOPIC_TYPE_UNSPECIFIED", "POLICY", "ADVERTISER_PREFERENCE", "REGULATORY"
    ]

@typing.type_check_only
class ReportResult(typing.TypedDict, total=False):
    averages: Row
    endDate: Date
    headers: _list[Header]
    rows: _list[Row]
    startDate: Date
    totalMatchedRows: str
    totals: Row
    warnings: _list[str]

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    cells: _list[Cell]

@typing.type_check_only
class SavedReport(typing.TypedDict, total=False):
    name: str
    title: str

@typing.type_check_only
class Site(typing.TypedDict, total=False):
    autoAdsEnabled: bool
    domain: str
    name: str
    reportingDimensionId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "REQUIRES_REVIEW",
        "GETTING_READY",
        "READY",
        "NEEDS_ATTENTION",
    ]

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class UrlChannel(typing.TypedDict, total=False):
    name: str
    reportingDimensionId: str
    uriPattern: str
