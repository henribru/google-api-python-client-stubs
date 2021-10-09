import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1AllUpdatesRule(
    typing_extensions.TypedDict, total=False
):
    disableDefaultIamRecipients: bool
    monitoringNotificationChannels: _list[str]
    pubsubTopic: str
    schemaVersion: str

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1Budget(typing_extensions.TypedDict, total=False):
    allUpdatesRule: GoogleCloudBillingBudgetsV1beta1AllUpdatesRule
    amount: GoogleCloudBillingBudgetsV1beta1BudgetAmount
    budgetFilter: GoogleCloudBillingBudgetsV1beta1Filter
    displayName: str
    etag: str
    name: str
    thresholdRules: _list[GoogleCloudBillingBudgetsV1beta1ThresholdRule]

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1BudgetAmount(
    typing_extensions.TypedDict, total=False
):
    lastPeriodAmount: GoogleCloudBillingBudgetsV1beta1LastPeriodAmount
    specifiedAmount: GoogleTypeMoney

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1CreateBudgetRequest(
    typing_extensions.TypedDict, total=False
):
    budget: GoogleCloudBillingBudgetsV1beta1Budget

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1CustomPeriod(
    typing_extensions.TypedDict, total=False
):
    endDate: GoogleTypeDate
    startDate: GoogleTypeDate

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1Filter(typing_extensions.TypedDict, total=False):
    calendarPeriod: typing_extensions.Literal[
        "CALENDAR_PERIOD_UNSPECIFIED", "MONTH", "QUARTER", "YEAR"
    ]
    creditTypes: _list[str]
    creditTypesTreatment: typing_extensions.Literal[
        "CREDIT_TYPES_TREATMENT_UNSPECIFIED",
        "INCLUDE_ALL_CREDITS",
        "EXCLUDE_ALL_CREDITS",
        "INCLUDE_SPECIFIED_CREDITS",
    ]
    customPeriod: GoogleCloudBillingBudgetsV1beta1CustomPeriod
    labels: dict[str, typing.Any]
    projects: _list[str]
    services: _list[str]
    subaccounts: _list[str]

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1LastPeriodAmount(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1ListBudgetsResponse(
    typing_extensions.TypedDict, total=False
):
    budgets: _list[GoogleCloudBillingBudgetsV1beta1Budget]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1ThresholdRule(
    typing_extensions.TypedDict, total=False
):
    spendBasis: typing_extensions.Literal[
        "BASIS_UNSPECIFIED", "CURRENT_SPEND", "FORECASTED_SPEND"
    ]
    thresholdPercent: float

@typing.type_check_only
class GoogleCloudBillingBudgetsV1beta1UpdateBudgetRequest(
    typing_extensions.TypedDict, total=False
):
    budget: GoogleCloudBillingBudgetsV1beta1Budget
    updateMask: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
