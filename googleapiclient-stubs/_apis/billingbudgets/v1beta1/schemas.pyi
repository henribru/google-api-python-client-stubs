import typing

import typing_extensions

class GoogleCloudBillingBudgetsV1beta1LastPeriodAmount(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudBillingBudgetsV1beta1Budget(typing_extensions.TypedDict, total=False):
    budgetFilter: GoogleCloudBillingBudgetsV1beta1Filter
    thresholdRules: typing.List[GoogleCloudBillingBudgetsV1beta1ThresholdRule]
    etag: str
    allUpdatesRule: GoogleCloudBillingBudgetsV1beta1AllUpdatesRule
    amount: GoogleCloudBillingBudgetsV1beta1BudgetAmount
    displayName: str
    name: str

class GoogleCloudBillingBudgetsV1beta1BudgetAmount(
    typing_extensions.TypedDict, total=False
):
    lastPeriodAmount: GoogleCloudBillingBudgetsV1beta1LastPeriodAmount
    specifiedAmount: GoogleTypeMoney

class GoogleCloudBillingBudgetsV1beta1UpdateBudgetRequest(
    typing_extensions.TypedDict, total=False
):
    updateMask: str
    budget: GoogleCloudBillingBudgetsV1beta1Budget

class GoogleCloudBillingBudgetsV1beta1AllUpdatesRule(
    typing_extensions.TypedDict, total=False
):
    schemaVersion: str
    disableDefaultIamRecipients: bool
    pubsubTopic: str
    monitoringNotificationChannels: typing.List[str]

class GoogleCloudBillingBudgetsV1beta1ListBudgetsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    budgets: typing.List[GoogleCloudBillingBudgetsV1beta1Budget]

class GoogleCloudBillingBudgetsV1beta1ThresholdRule(
    typing_extensions.TypedDict, total=False
):
    thresholdPercent: float
    spendBasis: typing_extensions.Literal[
        "BASIS_UNSPECIFIED", "CURRENT_SPEND", "FORECASTED_SPEND"
    ]

class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    nanos: int
    currencyCode: str
    units: str

class GoogleCloudBillingBudgetsV1beta1Filter(typing_extensions.TypedDict, total=False):
    creditTypesTreatment: typing_extensions.Literal[
        "CREDIT_TYPES_TREATMENT_UNSPECIFIED",
        "INCLUDE_ALL_CREDITS",
        "EXCLUDE_ALL_CREDITS",
    ]
    subaccounts: typing.List[str]
    projects: typing.List[str]
    labels: typing.Dict[str, typing.Any]
    services: typing.List[str]

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudBillingBudgetsV1beta1CreateBudgetRequest(
    typing_extensions.TypedDict, total=False
):
    budget: GoogleCloudBillingBudgetsV1beta1Budget
