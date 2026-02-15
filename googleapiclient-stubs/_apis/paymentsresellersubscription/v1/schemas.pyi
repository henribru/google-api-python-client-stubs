import typing

import typing_extensions

_list = list

@typing.type_check_only
class Amount(typing_extensions.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class CancelSubscriptionRequest(typing_extensions.TypedDict, total=False):
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
        "CANCELLATION_REASON_BILLING_SYSTEM_SWITCH",
        "CANCELLATION_REASON_OTHER",
    ]

@typing.type_check_only
class CancelSubscriptionResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class CreateSubscriptionIntent(typing_extensions.TypedDict, total=False):
    cycleOptions: CycleOptions
    parent: str
    subscription: Subscription
    subscriptionId: str

@typing.type_check_only
class CycleOptions(typing_extensions.TypedDict, total=False):
    initialCycleDuration: Duration

@typing.type_check_only
class Duration(typing_extensions.TypedDict, total=False):
    count: int
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "MONTH", "DAY", "HOUR"]

@typing.type_check_only
class EntitleSubscriptionIntent(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class EntitleSubscriptionRequest(typing_extensions.TypedDict, total=False):
    lineItemEntitlementDetails: _list[
        EntitleSubscriptionRequestLineItemEntitlementDetails
    ]

@typing.type_check_only
class EntitleSubscriptionRequestLineItemEntitlementDetails(
    typing_extensions.TypedDict, total=False
):
    lineItemIndex: int
    products: _list[str]

@typing.type_check_only
class EntitleSubscriptionResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class ExtendSubscriptionRequest(typing_extensions.TypedDict, total=False):
    extension: Extension
    requestId: str

@typing.type_check_only
class ExtendSubscriptionResponse(typing_extensions.TypedDict, total=False):
    cycleEndTime: str
    freeTrialEndTime: str
    renewalTime: str

@typing.type_check_only
class Extension(typing_extensions.TypedDict, total=False):
    duration: Duration
    partnerUserToken: str

@typing.type_check_only
class FindEligiblePromotionsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class FindEligiblePromotionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    promotions: _list[Promotion]

@typing.type_check_only
class FiniteBillingCycleDetails(typing_extensions.TypedDict, total=False):
    billingCycleCountLimit: str

@typing.type_check_only
class GenerateUserSessionRequest(typing_extensions.TypedDict, total=False):
    intentPayload: IntentPayload

@typing.type_check_only
class GenerateUserSessionResponse(typing_extensions.TypedDict, total=False):
    userSession: UserSession

@typing.type_check_only
class GoogleHomePayload(typing_extensions.TypedDict, total=False):
    attachedToGoogleStructure: bool
    googleStructureId: str
    partnerStructureId: str

@typing.type_check_only
class GoogleOnePayload(typing_extensions.TypedDict, total=False):
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
class GoogleTypeLocalizedText(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class IntentPayload(typing_extensions.TypedDict, total=False):
    createIntent: CreateSubscriptionIntent
    entitleIntent: EntitleSubscriptionIntent
    intentOptions: IntentPayloadIntentOptions

@typing.type_check_only
class IntentPayloadIntentOptions(typing_extensions.TypedDict, total=False):
    enableOfferOverride: bool

@typing.type_check_only
class ListProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]

@typing.type_check_only
class ListPromotionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    promotions: _list[Promotion]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    postalCode: str
    regionCode: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    bundleDetails: ProductBundleDetails
    finiteBillingCycleDetails: FiniteBillingCycleDetails
    name: str
    priceConfigs: _list[ProductPriceConfig]
    productType: typing_extensions.Literal[
        "PRODUCT_TYPE_UNSPECIFIED",
        "PRODUCT_TYPE_SUBSCRIPTION",
        "PRODUCT_TYPE_BUNDLE_SUBSCRIPTION",
    ]
    regionCodes: _list[str]
    subscriptionBillingCycleDuration: Duration
    titles: _list[GoogleTypeLocalizedText]

@typing.type_check_only
class ProductBundleDetails(typing_extensions.TypedDict, total=False):
    bundleElements: _list[ProductBundleDetailsBundleElement]
    entitlementMode: typing_extensions.Literal[
        "ENTITLEMENT_MODE_UNSPECIFIED",
        "ENTITLEMENT_MODE_FULL",
        "ENTITLEMENT_MODE_INCREMENTAL",
    ]

@typing.type_check_only
class ProductBundleDetailsBundleElement(typing_extensions.TypedDict, total=False):
    product: str

@typing.type_check_only
class ProductPayload(typing_extensions.TypedDict, total=False):
    googleHomePayload: GoogleHomePayload
    googleOnePayload: GoogleOnePayload
    youtubePayload: YoutubePayload

@typing.type_check_only
class ProductPriceConfig(typing_extensions.TypedDict, total=False):
    amount: Amount
    regionCode: str

@typing.type_check_only
class Promotion(typing_extensions.TypedDict, total=False):
    applicableProducts: _list[str]
    endTime: str
    freeTrialDuration: Duration
    introductoryPricingDetails: PromotionIntroductoryPricingDetails
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
class PromotionIntroductoryPricingDetails(typing_extensions.TypedDict, total=False):
    introductoryPricingSpecs: _list[
        PromotionIntroductoryPricingDetailsIntroductoryPricingSpec
    ]

@typing.type_check_only
class PromotionIntroductoryPricingDetailsIntroductoryPricingSpec(
    typing_extensions.TypedDict, total=False
):
    discountAmount: Amount
    discountRatioMicros: str
    recurrenceCount: int
    regionCode: str

@typing.type_check_only
class ResumeSubscriptionRequest(typing_extensions.TypedDict, total=False):
    cycleOptions: CycleOptions
    resumeMode: typing_extensions.Literal[
        "RESUME_MODE_UNSPECIFIED",
        "RESUME_MODE_CYCLE_OPTIONS",
        "RESUME_MODE_RESTORE_EXISTING_BILLING_SCHEDULE",
    ]

@typing.type_check_only
class ResumeSubscriptionResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class ServicePeriod(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    cancellationDetails: SubscriptionCancellationDetails
    createTime: str
    cycleEndTime: str
    endUserEntitled: bool
    freeTrialEndTime: str
    lineItems: _list[SubscriptionLineItem]
    migrationDetails: SubscriptionMigrationDetails
    name: str
    partnerUserToken: str
    processingState: typing_extensions.Literal[
        "PROCESSING_STATE_UNSPECIFIED",
        "PROCESSING_STATE_CANCELLING",
        "PROCESSING_STATE_RECURRING",
        "PROCESSING_STATE_RESUMING",
    ]
    products: _list[str]
    promotionSpecs: _list[SubscriptionPromotionSpec]
    promotions: _list[str]
    purchaseTime: str
    redirectUri: str
    renewalTime: str
    serviceLocation: Location
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
    upgradeDowngradeDetails: SubscriptionUpgradeDowngradeDetails

@typing.type_check_only
class SubscriptionCancellationDetails(typing_extensions.TypedDict, total=False):
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
        "CANCELLATION_REASON_BILLING_SYSTEM_SWITCH",
        "CANCELLATION_REASON_OTHER",
    ]

@typing.type_check_only
class SubscriptionLineItem(typing_extensions.TypedDict, total=False):
    amount: Amount
    bundleDetails: SubscriptionLineItemBundleDetails
    description: str
    finiteBillingCycleDetails: FiniteBillingCycleDetails
    lineItemFreeTrialEndTime: str
    lineItemIndex: int
    lineItemPromotionSpecs: _list[SubscriptionPromotionSpec]
    name: str
    oneTimeRecurrenceDetails: SubscriptionLineItemOneTimeRecurrenceDetails
    product: str
    productPayload: ProductPayload
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
class SubscriptionLineItemBundleDetails(typing_extensions.TypedDict, total=False):
    bundleElementDetails: _list[SubscriptionLineItemBundleDetailsBundleElementDetails]

@typing.type_check_only
class SubscriptionLineItemBundleDetailsBundleElementDetails(
    typing_extensions.TypedDict, total=False
):
    product: str
    userAccountLinkedTime: str

@typing.type_check_only
class SubscriptionLineItemOneTimeRecurrenceDetails(
    typing_extensions.TypedDict, total=False
):
    servicePeriod: ServicePeriod

@typing.type_check_only
class SubscriptionMigrationDetails(typing_extensions.TypedDict, total=False):
    migratedSubscriptionId: str

@typing.type_check_only
class SubscriptionPromotionSpec(typing_extensions.TypedDict, total=False):
    freeTrialDuration: Duration
    introductoryPricingDetails: PromotionIntroductoryPricingDetails
    promotion: str
    type: typing_extensions.Literal[
        "PROMOTION_TYPE_UNSPECIFIED",
        "PROMOTION_TYPE_FREE_TRIAL",
        "PROMOTION_TYPE_INTRODUCTORY_PRICING",
    ]

@typing.type_check_only
class SubscriptionUpgradeDowngradeDetails(typing_extensions.TypedDict, total=False):
    billingCycleSpec: typing_extensions.Literal[
        "BILLING_CYCLE_SPEC_UNSPECIFIED",
        "BILLING_CYCLE_SPEC_ALIGN_WITH_PREVIOUS_SUBSCRIPTION",
        "BILLING_CYCLE_SPEC_START_IMMEDIATELY",
        "BILLING_CYCLE_SPEC_DEFERRED_TO_NEXT_RECURRENCE",
    ]
    previousSubscriptionId: str

@typing.type_check_only
class SuspendSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SuspendSubscriptionResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class UndoCancelSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndoCancelSubscriptionResponse(typing_extensions.TypedDict, total=False):
    subscription: Subscription

@typing.type_check_only
class UserSession(typing_extensions.TypedDict, total=False):
    expireTime: str
    token: str

@typing.type_check_only
class YoutubePayload(typing_extensions.TypedDict, total=False):
    accessEndTime: str
    partnerEligibilityIds: _list[str]
    partnerPlanType: typing_extensions.Literal[
        "PARTNER_PLAN_TYPE_UNSPECIFIED",
        "PARTNER_PLAN_TYPE_STANDALONE",
        "PARTNER_PLAN_TYPE_HARD_BUNDLE",
        "PARTNER_PLAN_TYPE_SOFT_BUNDLE",
    ]
