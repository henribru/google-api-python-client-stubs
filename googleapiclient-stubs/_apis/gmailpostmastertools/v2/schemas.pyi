import typing

_list = list

@typing.type_check_only
class BaseMetric(typing.TypedDict, total=False):
    standardMetric: typing.Literal[
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
class BatchQueryDomainStatsRequest(typing.TypedDict, total=False):
    requests: _list[QueryDomainStatsRequest]

@typing.type_check_only
class BatchQueryDomainStatsResponse(typing.TypedDict, total=False):
    results: _list[BatchQueryDomainStatsResult]

@typing.type_check_only
class BatchQueryDomainStatsResult(typing.TypedDict, total=False):
    error: Status
    response: QueryDomainStatsResponse

@typing.type_check_only
class ComplianceRowData(typing.TypedDict, total=False):
    requirement: typing.Literal[
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
class ComplianceStatus(typing.TypedDict, total=False):
    status: typing.Literal["STATE_UNSPECIFIED", "COMPLIANT", "NEEDS_WORK"]

@typing.type_check_only
class CreateDomainRequest(typing.TypedDict, total=False):
    domainId: str

@typing.type_check_only
class CreateUserRequest(typing.TypedDict, total=False):
    permission: typing.Literal[
        "PERMISSION_UNSPECIFIED", "READER", "ADMIN", "OWNER", "NONE"
    ]
    userId: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateList(typing.TypedDict, total=False):
    dates: _list[Date]

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    end: Date
    start: Date

@typing.type_check_only
class DateRanges(typing.TypedDict, total=False):
    dateRanges: _list[DateRange]

@typing.type_check_only
class DeliverabilityStatusVerdict(typing.TypedDict, total=False):
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "MESSAGE_VOLUME_LOW",
        "SMTP_ERRORS_HIGH",
        "SENDER_NOT_COMPLIANT",
        "SPAM_RATE_HIGH",
        "USER_FEEDBACK_NEGATIVE",
        "USER_FEEDBACK_LOW",
        "USER_FEEDBACK_POSITIVE",
    ]
    state: ComplianceStatus

@typing.type_check_only
class Domain(typing.TypedDict, total=False):
    createTime: str
    lastVerifyTime: str
    name: str
    permission: typing.Literal[
        "PERMISSION_UNSPECIFIED", "READER", "ADMIN", "OWNER", "NONE"
    ]
    verificationState: typing.Literal[
        "VERIFICATION_STATE_UNSPECIFIED", "UNVERIFIED", "VERIFIED"
    ]

@typing.type_check_only
class DomainComplianceData(typing.TypedDict, total=False):
    deliverabilityStatusVerdict: DeliverabilityStatusVerdict
    domainId: str
    honorUnsubscribeVerdict: HonorUnsubscribeVerdict
    oneClickUnsubscribeVerdict: OneClickUnsubscribeVerdict
    rowData: _list[ComplianceRowData]

@typing.type_check_only
class DomainComplianceStatus(typing.TypedDict, total=False):
    complianceData: DomainComplianceData
    name: str
    subdomainComplianceData: DomainComplianceData

@typing.type_check_only
class DomainStat(typing.TypedDict, total=False):
    date: Date
    metric: str
    name: str
    value: StatisticValue

@typing.type_check_only
class DomainVerificationToken(typing.TypedDict, total=False):
    name: str
    token: str
    verificationMethod: typing.Literal[
        "DOMAIN_VERIFICATION_METHOD_UNSPECIFIED", "TXT", "CNAME"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class HonorUnsubscribeVerdict(typing.TypedDict, total=False):
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "NOT_HONORING",
        "NOT_HONORING_TOO_FEW_CAMPAIGNS",
        "NOT_HONORING_TOO_MANY_CAMPAIGNS",
    ]
    status: ComplianceStatus

@typing.type_check_only
class ListDomainsResponse(typing.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str

@typing.type_check_only
class ListUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class MetricDefinition(typing.TypedDict, total=False):
    baseMetric: BaseMetric
    filter: str
    name: str

@typing.type_check_only
class OneClickUnsubscribeVerdict(typing.TypedDict, total=False):
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "NO_UNSUB_GENERAL",
        "NO_UNSUB_SPAM_REPORTS",
        "NO_UNSUB_PROMO_SPAM_REPORTS",
    ]
    status: ComplianceStatus

@typing.type_check_only
class QueryDomainStatsRequest(typing.TypedDict, total=False):
    aggregationGranularity: typing.Literal[
        "AGGREGATION_GRANULARITY_UNSPECIFIED", "DAILY", "OVERALL"
    ]
    metricDefinitions: _list[MetricDefinition]
    pageSize: int
    pageToken: str
    parent: str
    timeQuery: TimeQuery

@typing.type_check_only
class QueryDomainStatsResponse(typing.TypedDict, total=False):
    domainStats: _list[DomainStat]
    nextPageToken: str

@typing.type_check_only
class StatisticValue(typing.TypedDict, total=False):
    doubleValue: float
    floatValue: float
    intValue: str
    stringList: StringList
    stringValue: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class TimeQuery(typing.TypedDict, total=False):
    dateList: DateList
    dateRanges: DateRanges

@typing.type_check_only
class User(typing.TypedDict, total=False):
    accessGranter: str
    createTime: str
    name: str
    permission: typing.Literal[
        "PERMISSION_UNSPECIFIED", "READER", "ADMIN", "OWNER", "NONE"
    ]
    user: str

@typing.type_check_only
class VerifyDomainRequest(typing.TypedDict, total=False):
    verificationMethod: typing.Literal[
        "DOMAIN_VERIFICATION_METHOD_UNSPECIFIED", "TXT", "CNAME"
    ]

@typing.type_check_only
class VerifyDomainResponse(typing.TypedDict, total=False): ...
