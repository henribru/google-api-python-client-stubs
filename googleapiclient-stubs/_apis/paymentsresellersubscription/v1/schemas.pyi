import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Amount(
    typing_extensions.TypedDict, total=False
):
    amountMicros: str
    currencyCode: str

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
    renewalTime: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Extension(
    typing_extensions.TypedDict, total=False
):
    duration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    partnerUserToken: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest(
    typing_extensions.TypedDict, total=False
):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    promotions: _list[GoogleCloudPaymentsResellerSubscriptionV1Promotion]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: _list[GoogleCloudPaymentsResellerSubscriptionV1Product]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    promotions: _list[GoogleCloudPaymentsResellerSubscriptionV1Promotion]

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
    priceConfigs: _list[GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig]
    regionCodes: _list[str]
    subscriptionBillingCycleDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    titles: _list[GoogleTypeLocalizedText]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig(
    typing_extensions.TypedDict, total=False
):
    amount: GoogleCloudPaymentsResellerSubscriptionV1Amount
    regionCode: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Promotion(
    typing_extensions.TypedDict, total=False
):
    applicableProducts: _list[str]
    endTime: str
    freeTrialDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    introductoryPricingDetails: GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails
    name: str
    promotionType: typing_extensions.Literal[
        "PROMOTION_TYPE_UNSPECIFIED",
        "PROMOTION_TYPE_FREE_TRIAL",
        "PROMOTION_TYPE_INTRODUCTORY_PRICING",
    ]
    regionCodes: _list[str]
    startTime: str
    titles: _list[GoogleTypeLocalizedText]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails(
    typing_extensions.TypedDict, total=False
):
    introductoryPricingSpecs: _list[
        GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpec
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetailsIntroductoryPricingSpec(
    typing_extensions.TypedDict, total=False
):
    discountAmount: GoogleCloudPaymentsResellerSubscriptionV1Amount
    discountRatioMicros: str
    recurrenceCount: int
    regionCode: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ServicePeriod(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Subscription(
    typing_extensions.TypedDict, total=False
):
    cancellationDetails: GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails
    createTime: str
    cycleEndTime: str
    endUserEntitled: bool
    freeTrialEndTime: str
    lineItems: _list[GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem]
    name: str
    partnerUserToken: str
    processingState: typing_extensions.Literal[
        "PROCESSING_STATE_UNSPECIFIED",
        "PROCESSING_STATE_CANCELLING",
        "PROCESSING_STATE_RECURRING",
    ]
    products: _list[str]
    promotionSpecs: _list[
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec
    ]
    promotions: _list[str]
    redirectUri: str
    renewalTime: str
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
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem(
    typing_extensions.TypedDict, total=False
):
    description: str
    lineItemFreeTrialEndTime: str
    lineItemPromotionSpecs: _list[
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec
    ]
    oneTimeRecurrenceDetails: GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails
    product: str
    recurrenceType: typing_extensions.Literal[
        "LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED",
        "LINE_ITEM_RECURRENCE_TYPE_PERIODIC",
        "LINE_ITEM_RECURRENCE_TYPE_ONE_TIME",
    ]
    state: typing_extensions.Literal[
        "LINE_ITEM_STATE_UNSPECIFIED",
        "LINE_ITEM_STATE_ACTIVE",
        "LINE_ITEM_STATE_INACTIVE",
        "LINE_ITEM_STATE_NEW",
        "LINE_ITEM_STATE_ACTIVATING",
        "LINE_ITEM_STATE_DEACTIVATING",
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails(
    typing_extensions.TypedDict, total=False
):
    servicePeriod: GoogleCloudPaymentsResellerSubscriptionV1ServicePeriod

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec(
    typing_extensions.TypedDict, total=False
):
    freeTrialDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    introductoryPricingDetails: GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails
    promotion: str
    type: typing_extensions.Literal[
        "PROMOTION_TYPE_UNSPECIFIED",
        "PROMOTION_TYPE_FREE_TRIAL",
        "PROMOTION_TYPE_INTRODUCTORY_PRICING",
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
