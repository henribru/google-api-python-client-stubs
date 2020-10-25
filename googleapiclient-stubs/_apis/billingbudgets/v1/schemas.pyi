import typing

import typing_extensions
@typing.type_check_only
class GoogleCloudBillingBudgetsV1Budget(typing_extensions.TypedDict, total=False):
    amount: GoogleCloudBillingBudgetsV1BudgetAmount
    budgetFilter: GoogleCloudBillingBudgetsV1Filter
    displayName: str
    etag: str
    name: str
    notificationsRule: GoogleCloudBillingBudgetsV1NotificationsRule
    thresholdRules: typing.List[GoogleCloudBillingBudgetsV1ThresholdRule]

@typing.type_check_only
class GoogleCloudBillingBudgetsV1BudgetAmount(typing_extensions.TypedDict, total=False):
    lastPeriodAmount: GoogleCloudBillingBudgetsV1LastPeriodAmount
    specifiedAmount: GoogleTypeMoney

@typing.type_check_only
class GoogleCloudBillingBudgetsV1Filter(typing_extensions.TypedDict, total=False):
    creditTypesTreatment: typing_extensions.Literal[
        "CREDIT_TYPES_TREATMENT_UNSPECIFIED",
        "INCLUDE_ALL_CREDITS",
        "EXCLUDE_ALL_CREDITS",
    ]
    labels: typing.Dict[str, typing.Any]
    projects: typing.List[str]
    services: typing.List[str]
    subaccounts: typing.List[str]

@typing.type_check_only
class GoogleCloudBillingBudgetsV1LastPeriodAmount(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBillingBudgetsV1ListBudgetsResponse(
    typing_extensions.TypedDict, total=False
):
    budgets: typing.List[GoogleCloudBillingBudgetsV1Budget]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBillingBudgetsV1NotificationsRule(
    typing_extensions.TypedDict, total=False
):
    disableDefaultIamRecipients: bool
    monitoringNotificationChannels: typing.List[str]
    pubsubTopic: str
    schemaVersion: str

@typing.type_check_only
class GoogleCloudBillingBudgetsV1ThresholdRule(
    typing_extensions.TypedDict, total=False
):
    spendBasis: typing_extensions.Literal[
        "BASIS_UNSPECIFIED", "CURRENT_SPEND", "FORECASTED_SPEND"
    ]
    thresholdPercent: float

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
