import typing

import typing_extensions

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest(
    typing_extensions.TypedDict, total=False
):
    cancelImmediately: bool
    cancellationReason: typing_extensions.Literal[
        "CANCELLATION_REASON_UNSPECIFIED",
        "CANCELLATION_REASON_FRAUD",
        "CANCELLATION_REASON_REMORSE",
        "CANCELLATION_REASON_ACCIDENTAL_PURCHASE",
        "CANCELLATION_REASON_PAST_DUE",
        "CANCELLATION_REASON_ACCOUNT_CLOSED",
        "CANCELLATION_REASON_UPGRADE_DOWNGRADE",
        "CANCELLATION_REASON_USER_DELINQUENCY",
        "CANCELLATION_REASON_OTHER",
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Duration(
    typing_extensions.TypedDict, total=False
):
    count: int
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "MONTH", "DAY"]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest(
    typing_extensions.TypedDict, total=False
):
    extension: GoogleCloudPaymentsResellerSubscriptionV1Extension
    requestId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    cycleEndTime: str
    freeTrialEndTime: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Extension(
    typing_extensions.TypedDict, total=False
):
    duration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    partnerUserToken: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: typing.List[GoogleCloudPaymentsResellerSubscriptionV1Product]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    promotions: typing.List[GoogleCloudPaymentsResellerSubscriptionV1Promotion]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Location(
    typing_extensions.TypedDict, total=False
):
    postalCode: str
    regionCode: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Product(
    typing_extensions.TypedDict, total=False
):
    name: str
    regionCodes: typing.List[str]
    subscriptionBillingCycleDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    titles: typing.List[GoogleTypeLocalizedText]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Promotion(
    typing_extensions.TypedDict, total=False
):
    applicableProducts: typing.List[str]
    endTime: str
    freeTrialDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    name: str
    regionCodes: typing.List[str]
    startTime: str
    titles: typing.List[GoogleTypeLocalizedText]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Subscription(
    typing_extensions.TypedDict, total=False
):
    cancellationDetails: GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails
    createTime: str
    cycleEndTime: str
    endUserEntitled: bool
    freeTrialEndTime: str
    name: str
    partnerUserToken: str
    processingState: typing_extensions.Literal[
        "PROCESSING_STATE_UNSPECIFIED",
        "PROCESSING_STATE_CANCELLING",
        "PROCESSING_STATE_RECURRING",
    ]
    products: typing.List[str]
    promotions: typing.List[str]
    redirectUri: str
    serviceLocation: GoogleCloudPaymentsResellerSubscriptionV1Location
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_CREATED",
        "STATE_ACTIVE",
        "STATE_CANCELLED",
        "STATE_IN_GRACE_PERIOD",
        "STATE_CANCEL_AT_END_OF_CYCLE",
    ]
    updateTime: str
    upgradeDowngradeDetails: GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails(
    typing_extensions.TypedDict, total=False
):
    reason: typing_extensions.Literal[
        "CANCELLATION_REASON_UNSPECIFIED",
        "CANCELLATION_REASON_FRAUD",
        "CANCELLATION_REASON_REMORSE",
        "CANCELLATION_REASON_ACCIDENTAL_PURCHASE",
        "CANCELLATION_REASON_PAST_DUE",
        "CANCELLATION_REASON_ACCOUNT_CLOSED",
        "CANCELLATION_REASON_UPGRADE_DOWNGRADE",
        "CANCELLATION_REASON_USER_DELINQUENCY",
        "CANCELLATION_REASON_OTHER",
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails(
    typing_extensions.TypedDict, total=False
):
    billingCycleSpec: typing_extensions.Literal[
        "BILLING_CYCLE_SPEC_UNSPECIFIED",
        "BILLING_CYCLE_SPEC_ALIGN_WITH_PREVIOUS_SUBSCRIPTION",
        "BILLING_CYCLE_SPEC_START_IMMEDIATELY",
    ]
    previousSubscriptionId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription

@typing.type_check_only
class GoogleTypeLocalizedText(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str
