import typing

_list = list

@typing.type_check_only
class GoogleCloudBillingBudgetsV1Budget(typing.TypedDict, total=False):
    amount: GoogleCloudBillingBudgetsV1BudgetAmount
    budgetFilter: GoogleCloudBillingBudgetsV1Filter
    displayName: str
    etag: str
    name: str
    notificationsRule: GoogleCloudBillingBudgetsV1NotificationsRule
    ownershipScope: typing.Literal[
        "OWNERSHIP_SCOPE_UNSPECIFIED", "ALL_USERS", "BILLING_ACCOUNT"
    ]
    thresholdRules: _list[GoogleCloudBillingBudgetsV1ThresholdRule]

@typing.type_check_only
class GoogleCloudBillingBudgetsV1BudgetAmount(typing.TypedDict, total=False):
    lastPeriodAmount: GoogleCloudBillingBudgetsV1LastPeriodAmount
    specifiedAmount: GoogleTypeMoney

@typing.type_check_only
class GoogleCloudBillingBudgetsV1CustomPeriod(typing.TypedDict, total=False):
    endDate: GoogleTypeDate
    startDate: GoogleTypeDate

@typing.type_check_only
class GoogleCloudBillingBudgetsV1Filter(typing.TypedDict, total=False):
    calendarPeriod: typing.Literal[
        "CALENDAR_PERIOD_UNSPECIFIED", "MONTH", "QUARTER", "YEAR"
    ]
    creditTypes: _list[str]
    creditTypesTreatment: typing.Literal[
        "CREDIT_TYPES_TREATMENT_UNSPECIFIED",
        "INCLUDE_ALL_CREDITS",
        "EXCLUDE_ALL_CREDITS",
        "INCLUDE_SPECIFIED_CREDITS",
    ]
    customPeriod: GoogleCloudBillingBudgetsV1CustomPeriod
    labels: dict[str, typing.Any]
    projects: _list[str]
    resourceAncestors: _list[str]
    services: _list[str]
    subaccounts: _list[str]

@typing.type_check_only
class GoogleCloudBillingBudgetsV1LastPeriodAmount(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudBillingBudgetsV1ListBudgetsResponse(typing.TypedDict, total=False):
    budgets: _list[GoogleCloudBillingBudgetsV1Budget]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBudgetsV1NotificationsRule(typing.TypedDict, total=False):
    disableDefaultIamRecipients: bool
    enableProjectLevelRecipients: bool
    monitoringNotificationChannels: _list[str]
    pubsubTopic: str
    schemaVersion: str

@typing.type_check_only
class GoogleCloudBillingBudgetsV1ThresholdRule(typing.TypedDict, total=False):
    spendBasis: typing.Literal["BASIS_UNSPECIFIED", "CURRENT_SPEND", "FORECASTED_SPEND"]
    thresholdPercent: float

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
