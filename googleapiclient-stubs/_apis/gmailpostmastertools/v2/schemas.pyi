import typing

import typing_extensions

_list = list

@typing.type_check_only
class BaseMetric(typing_extensions.TypedDict, total=False):
    standardMetric: typing_extensions.Literal[
        "STANDARD_METRIC_UNSPECIFIED",
        "FEEDBACK_LOOP_ID",
        "FEEDBACK_LOOP_SPAM_RATE",
        "SPAM_RATE",
        "AUTH_SUCCESS_RATE",
        "TLS_ENCRYPTION_MESSAGE_COUNT",
        "TLS_ENCRYPTION_RATE",
        "DELIVERY_ERROR_COUNT",
        "DELIVERY_ERROR_RATE",
    ]

@typing.type_check_only
class BatchQueryDomainStatsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[QueryDomainStatsRequest]

@typing.type_check_only
class BatchQueryDomainStatsResponse(typing_extensions.TypedDict, total=False):
    results: _list[BatchQueryDomainStatsResult]

@typing.type_check_only
class BatchQueryDomainStatsResult(typing_extensions.TypedDict, total=False):
    error: Status
    response: QueryDomainStatsResponse

@typing.type_check_only
class ComplianceRowData(typing_extensions.TypedDict, total=False):
    requirement: typing_extensions.Literal[
        "COMPLIANCE_REQUIREMENT_UNSPECIFIED",
        "SPF",
        "DKIM",
        "SPF_AND_DKIM",
        "DMARC_POLICY",
        "DMARC_ALIGNMENT",
        "MESSAGE_FORMATTING",
        "DNS_RECORDS",
        "ENCRYPTION",
        "USER_REPORTED_SPAM_RATE",
        "ONE_CLICK_UNSUBSCRIBE",
        "HONOR_UNSUBSCRIBE",
    ]
    status: ComplianceStatus

@typing.type_check_only
class ComplianceStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal["STATE_UNSPECIFIED", "COMPLIANT", "NEEDS_WORK"]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateList(typing_extensions.TypedDict, total=False):
    dates: _list[Date]

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    end: Date
    start: Date

@typing.type_check_only
class DateRanges(typing_extensions.TypedDict, total=False):
    dateRanges: _list[DateRange]

@typing.type_check_only
class Domain(typing_extensions.TypedDict, total=False):
    createTime: str
    lastVerifyTime: str
    name: str
    permission: typing_extensions.Literal[
        "PERMISSION_UNSPECIFIED", "READER", "OWNER", "NONE"
    ]
    verificationState: typing_extensions.Literal[
        "VERIFICATION_STATE_UNSPECIFIED", "UNVERIFIED", "VERIFIED"
    ]

@typing.type_check_only
class DomainComplianceData(typing_extensions.TypedDict, total=False):
    domainId: str
    honorUnsubscribeVerdict: HonorUnsubscribeVerdict
    oneClickUnsubscribeVerdict: OneClickUnsubscribeVerdict
    rowData: _list[ComplianceRowData]

@typing.type_check_only
class DomainComplianceStatus(typing_extensions.TypedDict, total=False):
    complianceData: DomainComplianceData
    name: str
    subdomainComplianceData: DomainComplianceData

@typing.type_check_only
class DomainStat(typing_extensions.TypedDict, total=False):
    date: Date
    metric: str
    name: str
    value: StatisticValue

@typing.type_check_only
class HonorUnsubscribeVerdict(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED",
        "NOT_HONORING",
        "NOT_HONORING_TOO_FEW_CAMPAIGNS",
        "NOT_HONORING_TOO_MANY_CAMPAIGNS",
    ]
    status: ComplianceStatus

@typing.type_check_only
class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str

@typing.type_check_only
class MetricDefinition(typing_extensions.TypedDict, total=False):
    baseMetric: BaseMetric
    filter: str
    name: str

@typing.type_check_only
class OneClickUnsubscribeVerdict(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED",
        "NO_UNSUB_GENERAL",
        "NO_UNSUB_SPAM_REPORTS",
        "NO_UNSUB_PROMO_SPAM_REPORTS",
    ]
    status: ComplianceStatus

@typing.type_check_only
class QueryDomainStatsRequest(typing_extensions.TypedDict, total=False):
    aggregationGranularity: typing_extensions.Literal[
        "AGGREGATION_GRANULARITY_UNSPECIFIED", "DAILY", "OVERALL"
    ]
    metricDefinitions: _list[MetricDefinition]
    pageSize: int
    pageToken: str
    parent: str
    timeQuery: TimeQuery

@typing.type_check_only
class QueryDomainStatsResponse(typing_extensions.TypedDict, total=False):
    domainStats: _list[DomainStat]
    nextPageToken: str

@typing.type_check_only
class StatisticValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    floatValue: float
    intValue: str
    stringList: StringList
    stringValue: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringList(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class TimeQuery(typing_extensions.TypedDict, total=False):
    dateList: DateList
    dateRanges: DateRanges
