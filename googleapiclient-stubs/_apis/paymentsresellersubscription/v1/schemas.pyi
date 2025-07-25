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
        "CANCELLATION_REASON_SYSTEM_ERROR",
        "CANCELLATION_REASON_SYSTEM_CANCEL",
        "CANCELLATION_REASON_OTHER",
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1CreateSubscriptionIntent(
    typing_extensions.TypedDict, total=False
):
    parent: str
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription
    subscriptionId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1Duration(
    typing_extensions.TypedDict, total=False
):
    count: int
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "MONTH", "DAY", "HOUR"]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionIntent(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest(
    typing_extensions.TypedDict, total=False
):
    lineItemEntitlementDetails: _list[
        GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestLineItemEntitlementDetails
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestLineItemEntitlementDetails(
    typing_extensions.TypedDict, total=False
):
    lineItemIndex: int
    products: _list[str]

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
class GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails(
    typing_extensions.TypedDict, total=False
):
    billingCycleCountLimit: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1GenerateUserSessionRequest(
    typing_extensions.TypedDict, total=False
):
    intentPayload: GoogleCloudPaymentsResellerSubscriptionV1IntentPayload

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1GenerateUserSessionResponse(
    typing_extensions.TypedDict, total=False
):
    userSession: GoogleCloudPaymentsResellerSubscriptionV1UserSession

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1GoogleHomePayload(
    typing_extensions.TypedDict, total=False
):
    attachedToGoogleStructure: bool
    partnerStructureId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayload(
    typing_extensions.TypedDict, total=False
):
    campaigns: _list[str]
    offering: typing_extensions.Literal[
        "OFFERING_UNSPECIFIED",
        "OFFERING_VAS_BUNDLE",
        "OFFERING_VAS_STANDALONE",
        "OFFERING_HARD_BUNDLE",
        "OFFERING_SOFT_BUNDLE",
    ]
    salesChannel: typing_extensions.Literal[
        "CHANNEL_UNSPECIFIED",
        "CHANNEL_RETAIL",
        "CHANNEL_ONLINE_WEB",
        "CHANNEL_ONLINE_ANDROID_APP",
        "CHANNEL_ONLINE_IOS_APP",
    ]
    storeId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1IntentPayload(
    typing_extensions.TypedDict, total=False
):
    createIntent: GoogleCloudPaymentsResellerSubscriptionV1CreateSubscriptionIntent
    entitleIntent: GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionIntent

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
    bundleDetails: ProductBundleDetails
    finiteBillingCycleDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails
    )
    name: str
    priceConfigs: _list[GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig]
    productType: typing_extensions.Literal[
        "PRODUCT_TYPE_UNSPECIFIED",
        "PRODUCT_TYPE_SUBSCRIPTION",
        "PRODUCT_TYPE_BUNDLE_SUBSCRIPTION",
    ]
    regionCodes: _list[str]
    subscriptionBillingCycleDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    titles: _list[GoogleTypeLocalizedText]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ProductBundleDetailsBundleElement(
    typing_extensions.TypedDict, total=False
):
    product: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ProductPayload(
    typing_extensions.TypedDict, total=False
):
    googleHomePayload: GoogleCloudPaymentsResellerSubscriptionV1GoogleHomePayload
    googleOnePayload: GoogleCloudPaymentsResellerSubscriptionV1GoogleOnePayload
    youtubePayload: GoogleCloudPaymentsResellerSubscriptionV1YoutubePayload

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
    introductoryPricingDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails
    )
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
class GoogleCloudPaymentsResellerSubscriptionV1ResumeSubscriptionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1ResumeSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription

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
    cancellationDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails
    )
    createTime: str
    cycleEndTime: str
    endUserEntitled: bool
    freeTrialEndTime: str
    lineItems: _list[GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem]
    migrationDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionMigrationDetails
    )
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
    purchaseTime: str
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
        "STATE_SUSPENDED",
    ]
    updateTime: str
    upgradeDowngradeDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails
    )

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
        "CANCELLATION_REASON_SYSTEM_ERROR",
        "CANCELLATION_REASON_SYSTEM_CANCEL",
        "CANCELLATION_REASON_OTHER",
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem(
    typing_extensions.TypedDict, total=False
):
    amount: GoogleCloudPaymentsResellerSubscriptionV1Amount
    bundleDetails: SubscriptionLineItemBundleDetails
    description: str
    finiteBillingCycleDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails
    )
    lineItemFreeTrialEndTime: str
    lineItemIndex: int
    lineItemPromotionSpecs: _list[
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec
    ]
    oneTimeRecurrenceDetails: GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails
    product: str
    productPayload: GoogleCloudPaymentsResellerSubscriptionV1ProductPayload
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
        "LINE_ITEM_STATE_WAITING_TO_DEACTIVATE",
        "LINE_ITEM_STATE_OFF_CYCLE_CHARGING",
    ]

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemBundleDetailsBundleElementDetails(
    typing_extensions.TypedDict, total=False
):
    product: str
    userAccountLinkedTime: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails(
    typing_extensions.TypedDict, total=False
):
    servicePeriod: GoogleCloudPaymentsResellerSubscriptionV1ServicePeriod

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionMigrationDetails(
    typing_extensions.TypedDict, total=False
):
    migratedSubscriptionId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec(
    typing_extensions.TypedDict, total=False
):
    freeTrialDuration: GoogleCloudPaymentsResellerSubscriptionV1Duration
    introductoryPricingDetails: (
        GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails
    )
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
        "BILLING_CYCLE_SPEC_DEFERRED_TO_NEXT_RECURRENCE",
    ]
    previousSubscriptionId: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SuspendSubscriptionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1SuspendSubscriptionResponse(
    typing_extensions.TypedDict, total=False
):
    subscription: GoogleCloudPaymentsResellerSubscriptionV1Subscription

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
class GoogleCloudPaymentsResellerSubscriptionV1UserSession(
    typing_extensions.TypedDict, total=False
):
    expireTime: str
    token: str

@typing.type_check_only
class GoogleCloudPaymentsResellerSubscriptionV1YoutubePayload(
    typing_extensions.TypedDict, total=False
):
    accessEndTime: str
    partnerEligibilityIds: _list[str]
    partnerPlanType: typing_extensions.Literal[
        "PARTNER_PLAN_TYPE_UNSPECIFIED",
        "PARTNER_PLAN_TYPE_STANDALONE",
        "PARTNER_PLAN_TYPE_HARD_BUNDLE",
        "PARTNER_PLAN_TYPE_SOFT_BUNDLE",
    ]

@typing.type_check_only
class GoogleTypeLocalizedText(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class ProductBundleDetails(typing_extensions.TypedDict, total=False):
    bundleElements: _list[
        GoogleCloudPaymentsResellerSubscriptionV1ProductBundleDetailsBundleElement
    ]
    entitlementMode: typing_extensions.Literal[
        "ENTITLEMENT_MODE_UNSPECIFIED",
        "ENTITLEMENT_MODE_FULL",
        "ENTITLEMENT_MODE_INCREMENTAL",
    ]

@typing.type_check_only
class SubscriptionLineItemBundleDetails(typing_extensions.TypedDict, total=False):
    bundleElementDetails: _list[
        GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemBundleDetailsBundleElementDetails
    ]
