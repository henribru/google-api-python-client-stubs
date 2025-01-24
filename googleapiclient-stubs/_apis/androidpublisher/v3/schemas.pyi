import typing

import typing_extensions

_list = list

@typing.type_check_only
class Abi(typing_extensions.TypedDict, total=False):
    alias: typing_extensions.Literal[
        "UNSPECIFIED_CPU_ARCHITECTURE",
        "ARMEABI",
        "ARMEABI_V7A",
        "ARM64_V8A",
        "X86",
        "X86_64",
        "RISCV64",
    ]

@typing.type_check_only
class AbiTargeting(typing_extensions.TypedDict, total=False):
    alternatives: _list[Abi]
    value: _list[Abi]

@typing.type_check_only
class AcquisitionTargetingRule(typing_extensions.TypedDict, total=False):
    scope: TargetingRuleScope

@typing.type_check_only
class ActivateBasePlanRequest(typing_extensions.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str

@typing.type_check_only
class ActivateSubscriptionOfferRequest(typing_extensions.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str

@typing.type_check_only
class AddTargetingRequest(typing_extensions.TypedDict, total=False):
    targetingUpdate: TargetingUpdate

@typing.type_check_only
class AddTargetingResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AllUsers(typing_extensions.TypedDict, total=False):
    isAllUsersRequested: bool

@typing.type_check_only
class AndroidSdks(typing_extensions.TypedDict, total=False):
    sdkLevels: _list[str]

@typing.type_check_only
class Apk(typing_extensions.TypedDict, total=False):
    binary: ApkBinary
    versionCode: int

@typing.type_check_only
class ApkBinary(typing_extensions.TypedDict, total=False):
    sha1: str
    sha256: str

@typing.type_check_only
class ApkDescription(typing_extensions.TypedDict, total=False):
    assetSliceMetadata: SplitApkMetadata
    instantApkMetadata: SplitApkMetadata
    path: str
    splitApkMetadata: SplitApkMetadata
    standaloneApkMetadata: StandaloneApkMetadata
    targeting: ApkTargeting

@typing.type_check_only
class ApkSet(typing_extensions.TypedDict, total=False):
    apkDescription: _list[ApkDescription]
    moduleMetadata: ModuleMetadata

@typing.type_check_only
class ApkTargeting(typing_extensions.TypedDict, total=False):
    abiTargeting: AbiTargeting
    languageTargeting: LanguageTargeting
    multiAbiTargeting: MultiAbiTargeting
    screenDensityTargeting: ScreenDensityTargeting
    sdkVersionTargeting: SdkVersionTargeting
    textureCompressionFormatTargeting: TextureCompressionFormatTargeting

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
class AppRecoveryAction(typing_extensions.TypedDict, total=False):
    appRecoveryId: str
    cancelTime: str
    createTime: str
    deployTime: str
    lastUpdateTime: str
    remoteInAppUpdateData: RemoteInAppUpdateData
    status: typing_extensions.Literal[
        "RECOVERY_STATUS_UNSPECIFIED",
        "RECOVERY_STATUS_ACTIVE",
        "RECOVERY_STATUS_CANCELED",
        "RECOVERY_STATUS_DRAFT",
        "RECOVERY_STATUS_GENERATION_IN_PROGRESS",
        "RECOVERY_STATUS_GENERATION_FAILED",
    ]
    targeting: Targeting

@typing.type_check_only
class AppVersionList(typing_extensions.TypedDict, total=False):
    versionCodes: _list[str]

@typing.type_check_only
class AppVersionRange(typing_extensions.TypedDict, total=False):
    versionCodeEnd: str
    versionCodeStart: str

@typing.type_check_only
class ArchiveSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AssetModuleMetadata(typing_extensions.TypedDict, total=False):
    deliveryType: typing_extensions.Literal[
        "UNKNOWN_DELIVERY_TYPE", "INSTALL_TIME", "ON_DEMAND", "FAST_FOLLOW"
    ]
    name: str

@typing.type_check_only
class AssetSliceSet(typing_extensions.TypedDict, total=False):
    apkDescription: _list[ApkDescription]
    assetModuleMetadata: AssetModuleMetadata

@typing.type_check_only
class AutoRenewingBasePlanType(typing_extensions.TypedDict, total=False):
    accountHoldDuration: str
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
    installmentDetails: InstallmentPlan
    priceChangeDetails: SubscriptionItemPriceChangeDetails
    recurringPrice: Money

@typing.type_check_only
class BasePlan(typing_extensions.TypedDict, total=False):
    autoRenewingBasePlanType: AutoRenewingBasePlanType
    basePlanId: str
    installmentsBasePlanType: InstallmentsBasePlanType
    offerTags: _list[OfferTag]
    otherRegionsConfig: OtherRegionsBasePlanConfig
    prepaidBasePlanType: PrepaidBasePlanType
    regionalConfigs: _list[RegionalBasePlanConfig]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class BatchGetSubscriptionOffersRequest(typing_extensions.TypedDict, total=False):
    requests: _list[GetSubscriptionOfferRequest]

@typing.type_check_only
class BatchGetSubscriptionOffersResponse(typing_extensions.TypedDict, total=False):
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class BatchGetSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    subscriptions: _list[Subscription]

@typing.type_check_only
class BatchMigrateBasePlanPricesRequest(typing_extensions.TypedDict, total=False):
    requests: _list[MigrateBasePlanPricesRequest]

@typing.type_check_only
class BatchMigrateBasePlanPricesResponse(typing_extensions.TypedDict, total=False):
    responses: _list[MigrateBasePlanPricesResponse]

@typing.type_check_only
class BatchUpdateBasePlanStatesRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateBasePlanStateRequest]

@typing.type_check_only
class BatchUpdateBasePlanStatesResponse(typing_extensions.TypedDict, total=False):
    subscriptions: _list[Subscription]

@typing.type_check_only
class BatchUpdateSubscriptionOfferStatesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[UpdateSubscriptionOfferStateRequest]

@typing.type_check_only
class BatchUpdateSubscriptionOfferStatesResponse(
    typing_extensions.TypedDict, total=False
):
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class BatchUpdateSubscriptionOffersRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateSubscriptionOfferRequest]

@typing.type_check_only
class BatchUpdateSubscriptionOffersResponse(typing_extensions.TypedDict, total=False):
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class BatchUpdateSubscriptionsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateSubscriptionRequest]

@typing.type_check_only
class BatchUpdateSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    subscriptions: _list[Subscription]

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
class CancelAppRecoveryRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelAppRecoveryResponse(typing_extensions.TypedDict, total=False): ...

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
class CreateDraftAppRecoveryRequest(typing_extensions.TypedDict, total=False):
    remoteInAppUpdate: RemoteInAppUpdate
    targeting: Targeting

@typing.type_check_only
class DeactivateBasePlanRequest(typing_extensions.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str

@typing.type_check_only
class DeactivateSubscriptionOfferRequest(typing_extensions.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str

@typing.type_check_only
class DeferredItemReplacement(typing_extensions.TypedDict, total=False):
    productId: str

@typing.type_check_only
class DeobfuscationFile(typing_extensions.TypedDict, total=False):
    symbolType: typing_extensions.Literal[
        "deobfuscationFileTypeUnspecified", "proguard", "nativeCode"
    ]

@typing.type_check_only
class DeobfuscationFilesUploadResponse(typing_extensions.TypedDict, total=False):
    deobfuscationFile: DeobfuscationFile

@typing.type_check_only
class DeployAppRecoveryRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeployAppRecoveryResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeveloperComment(typing_extensions.TypedDict, total=False):
    lastModified: Timestamp
    text: str

@typing.type_check_only
class DeveloperInitiatedCancellation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeviceFeature(typing_extensions.TypedDict, total=False):
    featureName: str
    featureVersion: int

@typing.type_check_only
class DeviceFeatureTargeting(typing_extensions.TypedDict, total=False):
    requiredFeature: DeviceFeature

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
    systemOnChips: _list[SystemOnChip]

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
    userCountrySets: _list[UserCountrySet]

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
class ExternalSubscription(typing_extensions.TypedDict, total=False):
    subscriptionType: typing_extensions.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "RECURRING", "PREPAID"
    ]

@typing.type_check_only
class ExternalTransaction(typing_extensions.TypedDict, total=False):
    createTime: str
    currentPreTaxAmount: Price
    currentTaxAmount: Price
    externalTransactionId: str
    oneTimeTransaction: OneTimeExternalTransaction
    originalPreTaxAmount: Price
    originalTaxAmount: Price
    packageName: str
    recurringTransaction: RecurringExternalTransaction
    testPurchase: ExternalTransactionTestPurchase
    transactionProgramCode: int
    transactionState: typing_extensions.Literal[
        "TRANSACTION_STATE_UNSPECIFIED", "TRANSACTION_REPORTED", "TRANSACTION_CANCELED"
    ]
    transactionTime: str
    userTaxAddress: ExternalTransactionAddress

@typing.type_check_only
class ExternalTransactionAddress(typing_extensions.TypedDict, total=False):
    administrativeArea: str
    regionCode: str

@typing.type_check_only
class ExternalTransactionTestPurchase(typing_extensions.TypedDict, total=False): ...

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
class FullRefund(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GeneratedApksListResponse(typing_extensions.TypedDict, total=False):
    generatedApks: _list[GeneratedApksPerSigningKey]

@typing.type_check_only
class GeneratedApksPerSigningKey(typing_extensions.TypedDict, total=False):
    certificateSha256Hash: str
    generatedAssetPackSlices: _list[GeneratedAssetPackSlice]
    generatedRecoveryModules: _list[GeneratedRecoveryApk]
    generatedSplitApks: _list[GeneratedSplitApk]
    generatedStandaloneApks: _list[GeneratedStandaloneApk]
    generatedUniversalApk: GeneratedUniversalApk
    targetingInfo: TargetingInfo

@typing.type_check_only
class GeneratedAssetPackSlice(typing_extensions.TypedDict, total=False):
    downloadId: str
    moduleName: str
    sliceId: str
    version: str

@typing.type_check_only
class GeneratedRecoveryApk(typing_extensions.TypedDict, total=False):
    downloadId: str
    moduleName: str
    recoveryId: str
    recoveryStatus: typing_extensions.Literal[
        "RECOVERY_STATUS_UNSPECIFIED",
        "RECOVERY_STATUS_ACTIVE",
        "RECOVERY_STATUS_CANCELED",
        "RECOVERY_STATUS_DRAFT",
        "RECOVERY_STATUS_GENERATION_IN_PROGRESS",
        "RECOVERY_STATUS_GENERATION_FAILED",
    ]

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
class GetSubscriptionOfferRequest(typing_extensions.TypedDict, total=False):
    basePlanId: str
    offerId: str
    packageName: str
    productId: str

@typing.type_check_only
class Grant(typing_extensions.TypedDict, total=False):
    appLevelPermissions: _list[
        typing_extensions.Literal[
            "APP_LEVEL_PERMISSION_UNSPECIFIED",
            "CAN_ACCESS_APP",
            "CAN_VIEW_FINANCIAL_DATA",
            "CAN_MANAGE_PERMISSIONS",
            "CAN_REPLY_TO_REVIEWS",
            "CAN_MANAGE_PUBLIC_APKS",
            "CAN_MANAGE_TRACK_APKS",
            "CAN_MANAGE_TRACK_USERS",
            "CAN_MANAGE_PUBLIC_LISTING",
            "CAN_MANAGE_DRAFT_APPS",
            "CAN_MANAGE_ORDERS",
            "CAN_MANAGE_APP_CONTENT",
            "CAN_VIEW_NON_FINANCIAL_DATA",
            "CAN_VIEW_APP_QUALITY",
            "CAN_MANAGE_DEEPLINKS",
        ]
    ]
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
class InappproductsBatchDeleteRequest(typing_extensions.TypedDict, total=False):
    requests: _list[InappproductsDeleteRequest]

@typing.type_check_only
class InappproductsBatchGetResponse(typing_extensions.TypedDict, total=False):
    inappproduct: _list[InAppProduct]

@typing.type_check_only
class InappproductsBatchUpdateRequest(typing_extensions.TypedDict, total=False):
    requests: _list[InappproductsUpdateRequest]

@typing.type_check_only
class InappproductsBatchUpdateResponse(typing_extensions.TypedDict, total=False):
    inappproducts: _list[InAppProduct]

@typing.type_check_only
class InappproductsDeleteRequest(typing_extensions.TypedDict, total=False):
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    sku: str

@typing.type_check_only
class InappproductsListResponse(typing_extensions.TypedDict, total=False):
    inappproduct: _list[InAppProduct]
    kind: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination

@typing.type_check_only
class InappproductsUpdateRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    autoConvertMissingPrices: bool
    inappproduct: InAppProduct
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    sku: str

@typing.type_check_only
class InstallmentPlan(typing_extensions.TypedDict, total=False):
    initialCommittedPaymentsCount: int
    pendingCancellation: PendingCancellation
    remainingCommittedPaymentsCount: int
    subsequentCommittedPaymentsCount: int

@typing.type_check_only
class InstallmentsBasePlanType(typing_extensions.TypedDict, total=False):
    accountHoldDuration: str
    billingPeriodDuration: str
    committedPaymentsCount: int
    gracePeriodDuration: str
    prorationMode: typing_extensions.Literal[
        "SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY",
    ]
    renewalType: typing_extensions.Literal[
        "RENEWAL_TYPE_UNSPECIFIED",
        "RENEWAL_TYPE_RENEWS_WITHOUT_COMMITMENT",
        "RENEWAL_TYPE_RENEWS_WITH_COMMITMENT",
    ]
    resubscribeState: typing_extensions.Literal[
        "RESUBSCRIBE_STATE_UNSPECIFIED",
        "RESUBSCRIBE_STATE_ACTIVE",
        "RESUBSCRIBE_STATE_INACTIVE",
    ]

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
class LanguageTargeting(typing_extensions.TypedDict, total=False):
    alternatives: _list[str]
    value: _list[str]

@typing.type_check_only
class ListAppRecoveriesResponse(typing_extensions.TypedDict, total=False):
    recoveryActions: _list[AppRecoveryAction]

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
    isTokenizedDigitalAsset: bool
    taxRateInfoByRegionCode: dict[str, typing.Any]

@typing.type_check_only
class MigrateBasePlanPricesRequest(typing_extensions.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str
    regionalPriceMigrations: _list[RegionalPriceMigrationConfig]
    regionsVersion: RegionsVersion

@typing.type_check_only
class MigrateBasePlanPricesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ModuleMetadata(typing_extensions.TypedDict, total=False):
    deliveryType: typing_extensions.Literal[
        "UNKNOWN_DELIVERY_TYPE", "INSTALL_TIME", "ON_DEMAND", "FAST_FOLLOW"
    ]
    dependencies: _list[str]
    moduleType: typing_extensions.Literal["UNKNOWN_MODULE_TYPE", "FEATURE_MODULE"]
    name: str
    targeting: ModuleTargeting

@typing.type_check_only
class ModuleTargeting(typing_extensions.TypedDict, total=False):
    deviceFeatureTargeting: _list[DeviceFeatureTargeting]
    sdkVersionTargeting: SdkVersionTargeting
    userCountriesTargeting: UserCountriesTargeting

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MultiAbi(typing_extensions.TypedDict, total=False):
    abi: _list[Abi]

@typing.type_check_only
class MultiAbiTargeting(typing_extensions.TypedDict, total=False):
    alternatives: _list[MultiAbi]
    value: _list[MultiAbi]

@typing.type_check_only
class OfferDetails(typing_extensions.TypedDict, total=False):
    basePlanId: str
    offerId: str
    offerTags: _list[str]

@typing.type_check_only
class OfferTag(typing_extensions.TypedDict, total=False):
    tag: str

@typing.type_check_only
class OneTimeCode(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class OneTimeExternalTransaction(typing_extensions.TypedDict, total=False):
    externalTransactionToken: str

@typing.type_check_only
class OtherRecurringProduct(typing_extensions.TypedDict, total=False): ...

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
    free: OtherRegionsSubscriptionOfferPhaseFreePriceOverride
    otherRegionsPrices: OtherRegionsSubscriptionOfferPhasePrices
    relativeDiscount: float

@typing.type_check_only
class OtherRegionsSubscriptionOfferPhaseFreePriceOverride(
    typing_extensions.TypedDict, total=False
): ...

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
class PartialRefund(typing_extensions.TypedDict, total=False):
    refundId: str
    refundPreTaxAmount: Price

@typing.type_check_only
class PausedStateContext(typing_extensions.TypedDict, total=False):
    autoResumeTime: str

@typing.type_check_only
class PendingCancellation(typing_extensions.TypedDict, total=False): ...

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
    refundableQuantity: int
    regionCode: str

@typing.type_check_only
class ProductPurchasesAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    developerPayload: str

@typing.type_check_only
class RecurringExternalTransaction(typing_extensions.TypedDict, total=False):
    externalSubscription: ExternalSubscription
    externalTransactionToken: str
    initialExternalTransactionId: str
    migratedTransactionProgram: typing_extensions.Literal[
        "EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED",
        "USER_CHOICE_BILLING",
        "ALTERNATIVE_BILLING_ONLY",
    ]
    otherRecurringProduct: OtherRecurringProduct

@typing.type_check_only
class RefundExternalTransactionRequest(typing_extensions.TypedDict, total=False):
    fullRefund: FullRefund
    partialRefund: PartialRefund
    refundTime: str

@typing.type_check_only
class RegionalBasePlanConfig(typing_extensions.TypedDict, total=False):
    newSubscriberAvailability: bool
    price: Money
    regionCode: str

@typing.type_check_only
class RegionalPriceMigrationConfig(typing_extensions.TypedDict, total=False):
    oldestAllowedPriceVersionTime: str
    priceIncreaseType: typing_extensions.Literal[
        "PRICE_INCREASE_TYPE_UNSPECIFIED",
        "PRICE_INCREASE_TYPE_OPT_IN",
        "PRICE_INCREASE_TYPE_OPT_OUT",
    ]
    regionCode: str

@typing.type_check_only
class RegionalSubscriptionOfferConfig(typing_extensions.TypedDict, total=False):
    newSubscriberAvailability: bool
    regionCode: str

@typing.type_check_only
class RegionalSubscriptionOfferPhaseConfig(typing_extensions.TypedDict, total=False):
    absoluteDiscount: Money
    free: RegionalSubscriptionOfferPhaseFreePriceOverride
    price: Money
    regionCode: str
    relativeDiscount: float

@typing.type_check_only
class RegionalSubscriptionOfferPhaseFreePriceOverride(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class RegionalTaxRateInfo(typing_extensions.TypedDict, total=False):
    eligibleForStreamingServiceTaxRate: bool
    streamingTaxType: typing_extensions.Literal[
        "STREAMING_TAX_TYPE_UNSPECIFIED",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_SALES",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_SALES",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL",
    ]
    taxTier: typing_extensions.Literal[
        "TAX_TIER_UNSPECIFIED",
        "TAX_TIER_BOOKS_1",
        "TAX_TIER_NEWS_1",
        "TAX_TIER_NEWS_2",
        "TAX_TIER_MUSIC_OR_AUDIO_1",
        "TAX_TIER_LIVE_OR_BROADCAST_1",
    ]

@typing.type_check_only
class Regions(typing_extensions.TypedDict, total=False):
    regionCode: _list[str]

@typing.type_check_only
class RegionsVersion(typing_extensions.TypedDict, total=False):
    version: str

@typing.type_check_only
class RemoteInAppUpdate(typing_extensions.TypedDict, total=False):
    isRemoteInAppUpdateRequested: bool

@typing.type_check_only
class RemoteInAppUpdateData(typing_extensions.TypedDict, total=False):
    remoteAppUpdateDataPerBundle: _list[RemoteInAppUpdateDataPerBundle]

@typing.type_check_only
class RemoteInAppUpdateDataPerBundle(typing_extensions.TypedDict, total=False):
    recoveredDeviceCount: str
    totalDeviceCount: str
    versionCode: str

@typing.type_check_only
class ReplacementCancellation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestrictedPaymentCountries(typing_extensions.TypedDict, total=False):
    regionCodes: _list[str]

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
class RevocationContext(typing_extensions.TypedDict, total=False):
    fullRefund: RevocationContextFullRefund
    proratedRefund: RevocationContextProratedRefund

@typing.type_check_only
class RevocationContextFullRefund(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RevocationContextProratedRefund(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RevokeSubscriptionPurchaseRequest(typing_extensions.TypedDict, total=False):
    revocationContext: RevocationContext

@typing.type_check_only
class RevokeSubscriptionPurchaseResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SafetyLabelsUpdateRequest(typing_extensions.TypedDict, total=False):
    safetyLabels: str

@typing.type_check_only
class SafetyLabelsUpdateResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ScreenDensity(typing_extensions.TypedDict, total=False):
    densityAlias: typing_extensions.Literal[
        "DENSITY_UNSPECIFIED",
        "NODPI",
        "LDPI",
        "MDPI",
        "TVDPI",
        "HDPI",
        "XHDPI",
        "XXHDPI",
        "XXXHDPI",
    ]
    densityDpi: int

@typing.type_check_only
class ScreenDensityTargeting(typing_extensions.TypedDict, total=False):
    alternatives: _list[ScreenDensity]
    value: _list[ScreenDensity]

@typing.type_check_only
class SdkVersion(typing_extensions.TypedDict, total=False):
    min: int

@typing.type_check_only
class SdkVersionTargeting(typing_extensions.TypedDict, total=False):
    alternatives: _list[SdkVersion]
    value: _list[SdkVersion]

@typing.type_check_only
class SignupPromotion(typing_extensions.TypedDict, total=False):
    oneTimeCode: OneTimeCode
    vanityCode: VanityCode

@typing.type_check_only
class SplitApkMetadata(typing_extensions.TypedDict, total=False):
    isMasterSplit: bool
    splitId: str

@typing.type_check_only
class SplitApkVariant(typing_extensions.TypedDict, total=False):
    apkSet: _list[ApkSet]
    targeting: VariantTargeting
    variantNumber: int

@typing.type_check_only
class StandaloneApkMetadata(typing_extensions.TypedDict, total=False):
    fusedModuleName: _list[str]

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
    restrictedPaymentCountries: RestrictedPaymentCountries
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
class SubscriptionItemPriceChangeDetails(typing_extensions.TypedDict, total=False):
    expectedNewPriceChargeTime: str
    newPrice: Money
    priceChangeMode: typing_extensions.Literal[
        "PRICE_CHANGE_MODE_UNSPECIFIED",
        "PRICE_DECREASE",
        "PRICE_INCREASE",
        "OPT_OUT_PRICE_INCREASE",
    ]
    priceChangeState: typing_extensions.Literal[
        "PRICE_CHANGE_STATE_UNSPECIFIED", "OUTSTANDING", "CONFIRMED", "APPLIED"
    ]

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
    deferredItemReplacement: DeferredItemReplacement
    expiryTime: str
    offerDetails: OfferDetails
    prepaidPlan: PrepaidPlan
    productId: str
    signupPromotion: SignupPromotion

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
        "SUBSCRIPTION_STATE_PENDING_PURCHASE_CANCELED",
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
    isTokenizedDigitalAsset: bool
    taxRateInfoByRegionCode: dict[str, typing.Any]

@typing.type_check_only
class SystemApkOptions(typing_extensions.TypedDict, total=False):
    rotated: bool
    uncompressedDexFiles: bool
    uncompressedNativeLibraries: bool

@typing.type_check_only
class SystemApksListResponse(typing_extensions.TypedDict, total=False):
    variants: _list[Variant]

@typing.type_check_only
class SystemFeature(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class SystemInitiatedCancellation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SystemOnChip(typing_extensions.TypedDict, total=False):
    manufacturer: str
    model: str

@typing.type_check_only
class Targeting(typing_extensions.TypedDict, total=False):
    allUsers: AllUsers
    androidSdks: AndroidSdks
    regions: Regions
    versionList: AppVersionList
    versionRange: AppVersionRange

@typing.type_check_only
class TargetingInfo(typing_extensions.TypedDict, total=False):
    assetSliceSet: _list[AssetSliceSet]
    packageName: str
    variant: _list[SplitApkVariant]

@typing.type_check_only
class TargetingRuleScope(typing_extensions.TypedDict, total=False):
    anySubscriptionInApp: TargetingRuleScopeAnySubscriptionInApp
    specificSubscriptionInApp: str
    thisSubscription: TargetingRuleScopeThisSubscription

@typing.type_check_only
class TargetingRuleScopeAnySubscriptionInApp(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class TargetingRuleScopeThisSubscription(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TargetingUpdate(typing_extensions.TypedDict, total=False):
    allUsers: AllUsers
    androidSdks: AndroidSdks
    regions: Regions

@typing.type_check_only
class TestPurchase(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Testers(typing_extensions.TypedDict, total=False):
    googleGroups: _list[str]

@typing.type_check_only
class TextureCompressionFormat(typing_extensions.TypedDict, total=False):
    alias: typing_extensions.Literal[
        "UNSPECIFIED_TEXTURE_COMPRESSION_FORMAT",
        "ETC1_RGB8",
        "PALETTED",
        "THREE_DC",
        "ATC",
        "LATC",
        "DXT1",
        "S3TC",
        "PVRTC",
        "ASTC",
        "ETC2",
    ]

@typing.type_check_only
class TextureCompressionFormatTargeting(typing_extensions.TypedDict, total=False):
    alternatives: _list[TextureCompressionFormat]
    value: _list[TextureCompressionFormat]

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
class TrackConfig(typing_extensions.TypedDict, total=False):
    formFactor: typing_extensions.Literal[
        "FORM_FACTOR_UNSPECIFIED", "DEFAULT", "WEAR", "AUTOMOTIVE"
    ]
    track: str
    type: typing_extensions.Literal["TRACK_TYPE_UNSPECIFIED", "CLOSED_TESTING"]

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
class UpdateBasePlanStateRequest(typing_extensions.TypedDict, total=False):
    activateBasePlanRequest: ActivateBasePlanRequest
    deactivateBasePlanRequest: DeactivateBasePlanRequest

@typing.type_check_only
class UpdateSubscriptionOfferRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    regionsVersion: RegionsVersion
    subscriptionOffer: SubscriptionOffer
    updateMask: str

@typing.type_check_only
class UpdateSubscriptionOfferStateRequest(typing_extensions.TypedDict, total=False):
    activateSubscriptionOfferRequest: ActivateSubscriptionOfferRequest
    deactivateSubscriptionOfferRequest: DeactivateSubscriptionOfferRequest

@typing.type_check_only
class UpdateSubscriptionRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    latencyTolerance: typing_extensions.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    regionsVersion: RegionsVersion
    subscription: Subscription
    updateMask: str

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
    developerAccountPermissions: _list[
        typing_extensions.Literal[
            "DEVELOPER_LEVEL_PERMISSION_UNSPECIFIED",
            "CAN_SEE_ALL_APPS",
            "CAN_VIEW_FINANCIAL_DATA_GLOBAL",
            "CAN_MANAGE_PERMISSIONS_GLOBAL",
            "CAN_EDIT_GAMES_GLOBAL",
            "CAN_PUBLISH_GAMES_GLOBAL",
            "CAN_REPLY_TO_REVIEWS_GLOBAL",
            "CAN_MANAGE_PUBLIC_APKS_GLOBAL",
            "CAN_MANAGE_TRACK_APKS_GLOBAL",
            "CAN_MANAGE_TRACK_USERS_GLOBAL",
            "CAN_MANAGE_PUBLIC_LISTING_GLOBAL",
            "CAN_MANAGE_DRAFT_APPS_GLOBAL",
            "CAN_CREATE_MANAGED_PLAY_APPS_GLOBAL",
            "CAN_CHANGE_MANAGED_PLAY_SETTING_GLOBAL",
            "CAN_MANAGE_ORDERS_GLOBAL",
            "CAN_MANAGE_APP_CONTENT_GLOBAL",
            "CAN_VIEW_NON_FINANCIAL_DATA_GLOBAL",
            "CAN_VIEW_APP_QUALITY_GLOBAL",
            "CAN_MANAGE_DEEPLINKS_GLOBAL",
        ]
    ]
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
class UserCountriesTargeting(typing_extensions.TypedDict, total=False):
    countryCodes: _list[str]
    exclude: bool

@typing.type_check_only
class UserCountrySet(typing_extensions.TypedDict, total=False):
    countryCodes: _list[str]
    name: str

@typing.type_check_only
class UserInitiatedCancellation(typing_extensions.TypedDict, total=False):
    cancelSurveyResult: CancelSurveyResult
    cancelTime: str

@typing.type_check_only
class UsesPermission(typing_extensions.TypedDict, total=False):
    maxSdkVersion: int
    name: str

@typing.type_check_only
class VanityCode(typing_extensions.TypedDict, total=False):
    promotionCode: str

@typing.type_check_only
class Variant(typing_extensions.TypedDict, total=False):
    deviceSpec: DeviceSpec
    options: SystemApkOptions
    variantId: int

@typing.type_check_only
class VariantTargeting(typing_extensions.TypedDict, total=False):
    abiTargeting: AbiTargeting
    multiAbiTargeting: MultiAbiTargeting
    screenDensityTargeting: ScreenDensityTargeting
    sdkVersionTargeting: SdkVersionTargeting
    textureCompressionFormatTargeting: TextureCompressionFormatTargeting

@typing.type_check_only
class VoidedPurchase(typing_extensions.TypedDict, total=False):
    kind: str
    orderId: str
    purchaseTimeMillis: str
    purchaseToken: str
    voidedQuantity: int
    voidedReason: int
    voidedSource: int
    voidedTimeMillis: str

@typing.type_check_only
class VoidedPurchasesListResponse(typing_extensions.TypedDict, total=False):
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    voidedPurchases: _list[VoidedPurchase]
