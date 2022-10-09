import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcquisitionTargetingRule(typing_extensions.TypedDict, total=False):
    scope: TargetingRuleScope

@typing.type_check_only
class ActivateBasePlanRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ActivateSubscriptionOfferRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Apk(typing_extensions.TypedDict, total=False):
    binary: ApkBinary
    versionCode: int

@typing.type_check_only
class ApkBinary(typing_extensions.TypedDict, total=False):
    sha1: str
    sha256: str

@typing.type_check_only
class ApksAddExternallyHostedRequest(typing_extensions.TypedDict, total=False):
    externallyHostedApk: ExternallyHostedApk

@typing.type_check_only
class ApksAddExternallyHostedResponse(typing_extensions.TypedDict, total=False):
    externallyHostedApk: ExternallyHostedApk

@typing.type_check_only
class ApksListResponse(typing_extensions.TypedDict, total=False):
    apks: _list[Apk]
    kind: str

@typing.type_check_only
class AppDetails(typing_extensions.TypedDict, total=False):
    contactEmail: str
    contactPhone: str
    contactWebsite: str
    defaultLanguage: str

@typing.type_check_only
class AppEdit(typing_extensions.TypedDict, total=False):
    expiryTimeSeconds: str
    id: str

@typing.type_check_only
class ArchiveSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AutoRenewingBasePlanType(typing_extensions.TypedDict, total=False):
    billingPeriodDuration: str
    gracePeriodDuration: str
    legacyCompatible: bool
    legacyCompatibleSubscriptionOfferId: str
    prorationMode: typing_extensions.Literal[
        "SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY",
    ]
    resubscribeState: typing_extensions.Literal[
        "RESUBSCRIBE_STATE_UNSPECIFIED",
        "RESUBSCRIBE_STATE_ACTIVE",
        "RESUBSCRIBE_STATE_INACTIVE",
    ]

@typing.type_check_only
class AutoRenewingPlan(typing_extensions.TypedDict, total=False):
    autoRenewEnabled: bool

@typing.type_check_only
class BasePlan(typing_extensions.TypedDict, total=False):
    autoRenewingBasePlanType: AutoRenewingBasePlanType
    basePlanId: str
    offerTags: _list[OfferTag]
    otherRegionsConfig: OtherRegionsBasePlanConfig
    prepaidBasePlanType: PrepaidBasePlanType
    regionalConfigs: _list[RegionalBasePlanConfig]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class Bundle(typing_extensions.TypedDict, total=False):
    sha1: str
    sha256: str
    versionCode: int

@typing.type_check_only
class BundlesListResponse(typing_extensions.TypedDict, total=False):
    bundles: _list[Bundle]
    kind: str

@typing.type_check_only
class CancelSurveyResult(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "CANCEL_SURVEY_REASON_UNSPECIFIED",
        "CANCEL_SURVEY_REASON_NOT_ENOUGH_USAGE",
        "CANCEL_SURVEY_REASON_TECHNICAL_ISSUES",
        "CANCEL_SURVEY_REASON_COST_RELATED",
        "CANCEL_SURVEY_REASON_FOUND_BETTER_APP",
        "CANCEL_SURVEY_REASON_OTHERS",
    ]
    reasonUserInput: str

@typing.type_check_only
class CanceledStateContext(typing_extensions.TypedDict, total=False):
    developerInitiatedCancellation: DeveloperInitiatedCancellation
    replacementCancellation: ReplacementCancellation
    systemInitiatedCancellation: SystemInitiatedCancellation
    userInitiatedCancellation: UserInitiatedCancellation

@typing.type_check_only
class Comment(typing_extensions.TypedDict, total=False):
    developerComment: DeveloperComment
    userComment: UserComment

@typing.type_check_only
class ConvertRegionPricesRequest(typing_extensions.TypedDict, total=False):
    price: Money

@typing.type_check_only
class ConvertRegionPricesResponse(typing_extensions.TypedDict, total=False):
    convertedOtherRegionsPrice: ConvertedOtherRegionsPrice
    convertedRegionPrices: dict[str, typing.Any]

@typing.type_check_only
class ConvertedOtherRegionsPrice(typing_extensions.TypedDict, total=False):
    eurPrice: Money
    usdPrice: Money

@typing.type_check_only
class ConvertedRegionPrice(typing_extensions.TypedDict, total=False):
    price: Money
    regionCode: str
    taxAmount: Money

@typing.type_check_only
class CountryTargeting(typing_extensions.TypedDict, total=False):
    countries: _list[str]
    includeRestOfWorld: bool

@typing.type_check_only
class DeactivateBasePlanRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateSubscriptionOfferRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeobfuscationFile(typing_extensions.TypedDict, total=False):
    symbolType: typing_extensions.Literal[
        "deobfuscationFileTypeUnspecified", "proguard", "nativeCode"
    ]

@typing.type_check_only
class DeobfuscationFilesUploadResponse(typing_extensions.TypedDict, total=False):
    deobfuscationFile: DeobfuscationFile

@typing.type_check_only
class DeveloperComment(typing_extensions.TypedDict, total=False):
    lastModified: Timestamp
    text: str

@typing.type_check_only
class DeveloperInitiatedCancellation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeviceGroup(typing_extensions.TypedDict, total=False):
    deviceSelectors: _list[DeviceSelector]
    name: str

@typing.type_check_only
class DeviceId(typing_extensions.TypedDict, total=False):
    buildBrand: str
    buildDevice: str

@typing.type_check_only
class DeviceMetadata(typing_extensions.TypedDict, total=False):
    cpuMake: str
    cpuModel: str
    deviceClass: str
    glEsVersion: int
    manufacturer: str
    nativePlatform: str
    productName: str
    ramMb: int
    screenDensityDpi: int
    screenHeightPx: int
    screenWidthPx: int

@typing.type_check_only
class DeviceRam(typing_extensions.TypedDict, total=False):
    maxBytes: str
    minBytes: str

@typing.type_check_only
class DeviceSelector(typing_extensions.TypedDict, total=False):
    deviceRam: DeviceRam
    excludedDeviceIds: _list[DeviceId]
    forbiddenSystemFeatures: _list[SystemFeature]
    includedDeviceIds: _list[DeviceId]
    requiredSystemFeatures: _list[SystemFeature]

@typing.type_check_only
class DeviceSpec(typing_extensions.TypedDict, total=False):
    screenDensity: int
    supportedAbis: _list[str]
    supportedLocales: _list[str]

@typing.type_check_only
class DeviceTier(typing_extensions.TypedDict, total=False):
    deviceGroupNames: _list[str]
    level: int

@typing.type_check_only
class DeviceTierConfig(typing_extensions.TypedDict, total=False):
    deviceGroups: _list[DeviceGroup]
    deviceTierConfigId: str
    deviceTierSet: DeviceTierSet

@typing.type_check_only
class DeviceTierSet(typing_extensions.TypedDict, total=False):
    deviceTiers: _list[DeviceTier]

@typing.type_check_only
class ExpansionFile(typing_extensions.TypedDict, total=False):
    fileSize: str
    referencesVersion: int

@typing.type_check_only
class ExpansionFilesUploadResponse(typing_extensions.TypedDict, total=False):
    expansionFile: ExpansionFile

@typing.type_check_only
class ExternalAccountIdentifiers(typing_extensions.TypedDict, total=False):
    externalAccountId: str
    obfuscatedExternalAccountId: str
    obfuscatedExternalProfileId: str

@typing.type_check_only
class ExternallyHostedApk(typing_extensions.TypedDict, total=False):
    applicationLabel: str
    certificateBase64s: _list[str]
    externallyHostedUrl: str
    fileSha1Base64: str
    fileSha256Base64: str
    fileSize: str
    iconBase64: str
    maximumSdk: int
    minimumSdk: int
    nativeCodes: _list[str]
    packageName: str
    usesFeatures: _list[str]
    usesPermissions: _list[UsesPermission]
    versionCode: int
    versionName: str

@typing.type_check_only
class GeneratedApksListResponse(typing_extensions.TypedDict, total=False):
    generatedApks: _list[GeneratedApksPerSigningKey]

@typing.type_check_only
class GeneratedApksPerSigningKey(typing_extensions.TypedDict, total=False):
    certificateSha256Hash: str
    generatedAssetPackSlices: _list[GeneratedAssetPackSlice]
    generatedSplitApks: _list[GeneratedSplitApk]
    generatedStandaloneApks: _list[GeneratedStandaloneApk]
    generatedUniversalApk: GeneratedUniversalApk

@typing.type_check_only
class GeneratedAssetPackSlice(typing_extensions.TypedDict, total=False):
    downloadId: str
    moduleName: str
    sliceId: str
    version: str

@typing.type_check_only
class GeneratedSplitApk(typing_extensions.TypedDict, total=False):
    downloadId: str
    moduleName: str
    splitId: str
    variantId: int

@typing.type_check_only
class GeneratedStandaloneApk(typing_extensions.TypedDict, total=False):
    downloadId: str
    variantId: int

@typing.type_check_only
class GeneratedUniversalApk(typing_extensions.TypedDict, total=False):
    downloadId: str

@typing.type_check_only
class Grant(typing_extensions.TypedDict, total=False):
    appLevelPermissions: _list[str]
    name: str
    packageName: str

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    id: str
    sha1: str
    sha256: str
    url: str

@typing.type_check_only
class ImagesDeleteAllResponse(typing_extensions.TypedDict, total=False):
    deleted: _list[Image]

@typing.type_check_only
class ImagesListResponse(typing_extensions.TypedDict, total=False):
    images: _list[Image]

@typing.type_check_only
class ImagesUploadResponse(typing_extensions.TypedDict, total=False):
    image: Image

@typing.type_check_only
class InAppProduct(typing_extensions.TypedDict, total=False):
    defaultLanguage: str
    defaultPrice: Price
    gracePeriod: str
    listings: dict[str, typing.Any]
    managedProductTaxesAndComplianceSettings: ManagedProductTaxAndComplianceSettings
    packageName: str
    prices: dict[str, typing.Any]
    purchaseType: typing_extensions.Literal[
        "purchaseTypeUnspecified", "managedUser", "subscription"
    ]
    sku: str
    status: typing_extensions.Literal["statusUnspecified", "active", "inactive"]
    subscriptionPeriod: str
    subscriptionTaxesAndComplianceSettings: SubscriptionTaxAndComplianceSettings
    trialPeriod: str

@typing.type_check_only
class InAppProductListing(typing_extensions.TypedDict, total=False):
    benefits: _list[str]
    description: str
    title: str

@typing.type_check_only
class InappproductsListResponse(typing_extensions.TypedDict, total=False):
    inappproduct: _list[InAppProduct]
    kind: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination

@typing.type_check_only
class InternalAppSharingArtifact(typing_extensions.TypedDict, total=False):
    certificateFingerprint: str
    downloadUrl: str
    sha256: str

@typing.type_check_only
class IntroductoryPriceInfo(typing_extensions.TypedDict, total=False):
    introductoryPriceAmountMicros: str
    introductoryPriceCurrencyCode: str
    introductoryPriceCycles: int
    introductoryPricePeriod: str

@typing.type_check_only
class ListDeviceTierConfigsResponse(typing_extensions.TypedDict, total=False):
    deviceTierConfigs: _list[DeviceTierConfig]
    nextPageToken: str

@typing.type_check_only
class ListSubscriptionOffersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class Listing(typing_extensions.TypedDict, total=False):
    fullDescription: str
    language: str
    shortDescription: str
    title: str
    video: str

@typing.type_check_only
class ListingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    listings: _list[Listing]

@typing.type_check_only
class LocalizedText(typing_extensions.TypedDict, total=False):
    language: str
    text: str

@typing.type_check_only
class ManagedProductTaxAndComplianceSettings(typing_extensions.TypedDict, total=False):
    eeaWithdrawalRightType: typing_extensions.Literal[
        "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED",
        "WITHDRAWAL_RIGHT_DIGITAL_CONTENT",
        "WITHDRAWAL_RIGHT_SERVICE",
    ]
    taxRateInfoByRegionCode: dict[str, typing.Any]

@typing.type_check_only
class MigrateBasePlanPricesRequest(typing_extensions.TypedDict, total=False):
    regionalPriceMigrations: _list[RegionalPriceMigrationConfig]
    regionsVersion: RegionsVersion

@typing.type_check_only
class MigrateBasePlanPricesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class OfferTag(typing_extensions.TypedDict, total=False):
    tag: str

@typing.type_check_only
class OtherRegionsBasePlanConfig(typing_extensions.TypedDict, total=False):
    eurPrice: Money
    newSubscriberAvailability: bool
    usdPrice: Money

@typing.type_check_only
class OtherRegionsSubscriptionOfferConfig(typing_extensions.TypedDict, total=False):
    otherRegionsNewSubscriberAvailability: bool

@typing.type_check_only
class OtherRegionsSubscriptionOfferPhaseConfig(
    typing_extensions.TypedDict, total=False
):
    absoluteDiscounts: OtherRegionsSubscriptionOfferPhasePrices
    otherRegionsPrices: OtherRegionsSubscriptionOfferPhasePrices
    relativeDiscount: float

@typing.type_check_only
class OtherRegionsSubscriptionOfferPhasePrices(
    typing_extensions.TypedDict, total=False
):
    eurPrice: Money
    usdPrice: Money

@typing.type_check_only
class PageInfo(typing_extensions.TypedDict, total=False):
    resultPerPage: int
    startIndex: int
    totalResults: int

@typing.type_check_only
class PausedStateContext(typing_extensions.TypedDict, total=False):
    autoResumeTime: str

@typing.type_check_only
class PrepaidBasePlanType(typing_extensions.TypedDict, total=False):
    billingPeriodDuration: str
    timeExtension: typing_extensions.Literal[
        "TIME_EXTENSION_UNSPECIFIED", "TIME_EXTENSION_ACTIVE", "TIME_EXTENSION_INACTIVE"
    ]

@typing.type_check_only
class PrepaidPlan(typing_extensions.TypedDict, total=False):
    allowExtendAfterTime: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    currency: str
    priceMicros: str

@typing.type_check_only
class ProductPurchase(typing_extensions.TypedDict, total=False):
    acknowledgementState: int
    consumptionState: int
    developerPayload: str
    kind: str
    obfuscatedExternalAccountId: str
    obfuscatedExternalProfileId: str
    orderId: str
    productId: str
    purchaseState: int
    purchaseTimeMillis: str
    purchaseToken: str
    purchaseType: int
    quantity: int
    regionCode: str

@typing.type_check_only
class ProductPurchasesAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    developerPayload: str

@typing.type_check_only
class RegionalBasePlanConfig(typing_extensions.TypedDict, total=False):
    newSubscriberAvailability: bool
    price: Money
    regionCode: str

@typing.type_check_only
class RegionalPriceMigrationConfig(typing_extensions.TypedDict, total=False):
    oldestAllowedPriceVersionTime: str
    regionCode: str

@typing.type_check_only
class RegionalSubscriptionOfferConfig(typing_extensions.TypedDict, total=False):
    newSubscriberAvailability: bool
    regionCode: str

@typing.type_check_only
class RegionalSubscriptionOfferPhaseConfig(typing_extensions.TypedDict, total=False):
    absoluteDiscount: Money
    price: Money
    regionCode: str
    relativeDiscount: float

@typing.type_check_only
class RegionalTaxRateInfo(typing_extensions.TypedDict, total=False):
    eligibleForStreamingServiceTaxRate: bool
    taxTier: typing_extensions.Literal[
        "TAX_TIER_UNSPECIFIED",
        "TAX_TIER_BOOKS_1",
        "TAX_TIER_NEWS_1",
        "TAX_TIER_NEWS_2",
        "TAX_TIER_MUSIC_OR_AUDIO_1",
        "TAX_TIER_LIVE_OR_BROADCAST_1",
    ]

@typing.type_check_only
class RegionsVersion(typing_extensions.TypedDict, total=False):
    version: str

@typing.type_check_only
class ReplacementCancellation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Review(typing_extensions.TypedDict, total=False):
    authorName: str
    comments: _list[Comment]
    reviewId: str

@typing.type_check_only
class ReviewReplyResult(typing_extensions.TypedDict, total=False):
    lastEdited: Timestamp
    replyText: str

@typing.type_check_only
class ReviewsListResponse(typing_extensions.TypedDict, total=False):
    pageInfo: PageInfo
    reviews: _list[Review]
    tokenPagination: TokenPagination

@typing.type_check_only
class ReviewsReplyRequest(typing_extensions.TypedDict, total=False):
    replyText: str

@typing.type_check_only
class ReviewsReplyResponse(typing_extensions.TypedDict, total=False):
    result: ReviewReplyResult

@typing.type_check_only
class SubscribeWithGoogleInfo(typing_extensions.TypedDict, total=False):
    emailAddress: str
    familyName: str
    givenName: str
    profileId: str
    profileName: str

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    archived: bool
    basePlans: _list[BasePlan]
    listings: _list[SubscriptionListing]
    packageName: str
    productId: str
    taxAndComplianceSettings: SubscriptionTaxAndComplianceSettings

@typing.type_check_only
class SubscriptionCancelSurveyResult(typing_extensions.TypedDict, total=False):
    cancelSurveyReason: int
    userInputCancelReason: str

@typing.type_check_only
class SubscriptionDeferralInfo(typing_extensions.TypedDict, total=False):
    desiredExpiryTimeMillis: str
    expectedExpiryTimeMillis: str

@typing.type_check_only
class SubscriptionListing(typing_extensions.TypedDict, total=False):
    benefits: _list[str]
    description: str
    languageCode: str
    title: str

@typing.type_check_only
class SubscriptionOffer(typing_extensions.TypedDict, total=False):
    basePlanId: str
    offerId: str
    offerTags: _list[OfferTag]
    otherRegionsConfig: OtherRegionsSubscriptionOfferConfig
    packageName: str
    phases: _list[SubscriptionOfferPhase]
    productId: str
    regionalConfigs: _list[RegionalSubscriptionOfferConfig]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "INACTIVE"]
    targeting: SubscriptionOfferTargeting

@typing.type_check_only
class SubscriptionOfferPhase(typing_extensions.TypedDict, total=False):
    duration: str
    otherRegionsConfig: OtherRegionsSubscriptionOfferPhaseConfig
    recurrenceCount: int
    regionalConfigs: _list[RegionalSubscriptionOfferPhaseConfig]

@typing.type_check_only
class SubscriptionOfferTargeting(typing_extensions.TypedDict, total=False):
    acquisitionRule: AcquisitionTargetingRule
    upgradeRule: UpgradeTargetingRule

@typing.type_check_only
class SubscriptionPriceChange(typing_extensions.TypedDict, total=False):
    newPrice: Price
    state: int

@typing.type_check_only
class SubscriptionPurchase(typing_extensions.TypedDict, total=False):
    acknowledgementState: int
    autoRenewing: bool
    autoResumeTimeMillis: str
    cancelReason: int
    cancelSurveyResult: SubscriptionCancelSurveyResult
    countryCode: str
    developerPayload: str
    emailAddress: str
    expiryTimeMillis: str
    externalAccountId: str
    familyName: str
    givenName: str
    introductoryPriceInfo: IntroductoryPriceInfo
    kind: str
    linkedPurchaseToken: str
    obfuscatedExternalAccountId: str
    obfuscatedExternalProfileId: str
    orderId: str
    paymentState: int
    priceAmountMicros: str
    priceChange: SubscriptionPriceChange
    priceCurrencyCode: str
    profileId: str
    profileName: str
    promotionCode: str
    promotionType: int
    purchaseType: int
    startTimeMillis: str
    userCancellationTimeMillis: str

@typing.type_check_only
class SubscriptionPurchaseLineItem(typing_extensions.TypedDict, total=False):
    autoRenewingPlan: AutoRenewingPlan
    expiryTime: str
    prepaidPlan: PrepaidPlan
    productId: str

@typing.type_check_only
class SubscriptionPurchaseV2(typing_extensions.TypedDict, total=False):
    acknowledgementState: typing_extensions.Literal[
        "ACKNOWLEDGEMENT_STATE_UNSPECIFIED",
        "ACKNOWLEDGEMENT_STATE_PENDING",
        "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED",
    ]
    canceledStateContext: CanceledStateContext
    externalAccountIdentifiers: ExternalAccountIdentifiers
    kind: str
    latestOrderId: str
    lineItems: _list[SubscriptionPurchaseLineItem]
    linkedPurchaseToken: str
    pausedStateContext: PausedStateContext
    regionCode: str
    startTime: str
    subscribeWithGoogleInfo: SubscribeWithGoogleInfo
    subscriptionState: typing_extensions.Literal[
        "SUBSCRIPTION_STATE_UNSPECIFIED",
        "SUBSCRIPTION_STATE_PENDING",
        "SUBSCRIPTION_STATE_ACTIVE",
        "SUBSCRIPTION_STATE_PAUSED",
        "SUBSCRIPTION_STATE_IN_GRACE_PERIOD",
        "SUBSCRIPTION_STATE_ON_HOLD",
        "SUBSCRIPTION_STATE_CANCELED",
        "SUBSCRIPTION_STATE_EXPIRED",
    ]
    testPurchase: TestPurchase

@typing.type_check_only
class SubscriptionPurchasesAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    developerPayload: str

@typing.type_check_only
class SubscriptionPurchasesDeferRequest(typing_extensions.TypedDict, total=False):
    deferralInfo: SubscriptionDeferralInfo

@typing.type_check_only
class SubscriptionPurchasesDeferResponse(typing_extensions.TypedDict, total=False):
    newExpiryTimeMillis: str

@typing.type_check_only
class SubscriptionTaxAndComplianceSettings(typing_extensions.TypedDict, total=False):
    eeaWithdrawalRightType: typing_extensions.Literal[
        "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED",
        "WITHDRAWAL_RIGHT_DIGITAL_CONTENT",
        "WITHDRAWAL_RIGHT_SERVICE",
    ]
    taxRateInfoByRegionCode: dict[str, typing.Any]

@typing.type_check_only
class SystemApksListResponse(typing_extensions.TypedDict, total=False):
    variants: _list[Variant]

@typing.type_check_only
class SystemFeature(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class SystemInitiatedCancellation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TargetingRuleScope(typing_extensions.TypedDict, total=False):
    specificSubscriptionInApp: str

@typing.type_check_only
class TestPurchase(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Testers(typing_extensions.TypedDict, total=False):
    googleGroups: _list[str]

@typing.type_check_only
class Timestamp(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class TokenPagination(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    previousPageToken: str

@typing.type_check_only
class Track(typing_extensions.TypedDict, total=False):
    releases: _list[TrackRelease]
    track: str

@typing.type_check_only
class TrackCountryAvailability(typing_extensions.TypedDict, total=False):
    countries: _list[TrackTargetedCountry]
    restOfWorld: bool
    syncWithProduction: bool

@typing.type_check_only
class TrackRelease(typing_extensions.TypedDict, total=False):
    countryTargeting: CountryTargeting
    inAppUpdatePriority: int
    name: str
    releaseNotes: _list[LocalizedText]
    status: typing_extensions.Literal[
        "statusUnspecified", "draft", "inProgress", "halted", "completed"
    ]
    userFraction: float
    versionCodes: _list[str]

@typing.type_check_only
class TrackTargetedCountry(typing_extensions.TypedDict, total=False):
    countryCode: str

@typing.type_check_only
class TracksListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    tracks: _list[Track]

@typing.type_check_only
class UpgradeTargetingRule(typing_extensions.TypedDict, total=False):
    billingPeriodDuration: str
    oncePerUser: bool
    scope: TargetingRuleScope

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    accessState: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "INVITED",
        "INVITATION_EXPIRED",
        "ACCESS_GRANTED",
        "ACCESS_EXPIRED",
    ]
    developerAccountPermissions: _list[str]
    email: str
    expirationTime: str
    grants: _list[Grant]
    name: str
    partial: bool

@typing.type_check_only
class UserComment(typing_extensions.TypedDict, total=False):
    androidOsVersion: int
    appVersionCode: int
    appVersionName: str
    device: str
    deviceMetadata: DeviceMetadata
    lastModified: Timestamp
    originalText: str
    reviewerLanguage: str
    starRating: int
    text: str
    thumbsDownCount: int
    thumbsUpCount: int

@typing.type_check_only
class UserInitiatedCancellation(typing_extensions.TypedDict, total=False):
    cancelSurveyResult: CancelSurveyResult
    cancelTime: str

@typing.type_check_only
class UsesPermission(typing_extensions.TypedDict, total=False):
    maxSdkVersion: int
    name: str

@typing.type_check_only
class Variant(typing_extensions.TypedDict, total=False):
    deviceSpec: DeviceSpec
    variantId: int

@typing.type_check_only
class VoidedPurchase(typing_extensions.TypedDict, total=False):
    kind: str
    orderId: str
    purchaseTimeMillis: str
    purchaseToken: str
    voidedReason: int
    voidedSource: int
    voidedTimeMillis: str

@typing.type_check_only
class VoidedPurchasesListResponse(typing_extensions.TypedDict, total=False):
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    voidedPurchases: _list[VoidedPurchase]
