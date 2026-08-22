import typing

_list = list

@typing.type_check_only
class Abi(typing.TypedDict, total=False):
    alias: typing.Literal[
        "UNSPECIFIED_CPU_ARCHITECTURE",
        "ARMEABI",
        "ARMEABI_V7A",
        "ARM64_V8A",
        "X86",
        "X86_64",
        "RISCV64",
    ]

@typing.type_check_only
class AbiTargeting(typing.TypedDict, total=False):
    alternatives: _list[Abi]
    value: _list[Abi]

@typing.type_check_only
class AcquisitionTargetingRule(typing.TypedDict, total=False):
    scope: TargetingRuleScope

@typing.type_check_only
class ActivateBasePlanRequest(typing.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str

@typing.type_check_only
class ActivateOneTimeProductOfferRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class ActivatePurchaseOptionRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class ActivateSubscriptionOfferRequest(typing.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str

@typing.type_check_only
class AddTargetingRequest(typing.TypedDict, total=False):
    targetingUpdate: TargetingUpdate

@typing.type_check_only
class AddTargetingResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class AllUsers(typing.TypedDict, total=False):
    isAllUsersRequested: bool

@typing.type_check_only
class AndroidSdks(typing.TypedDict, total=False):
    sdkLevels: _list[str]

@typing.type_check_only
class Apk(typing.TypedDict, total=False):
    binary: ApkBinary
    versionCode: int

@typing.type_check_only
class ApkBinary(typing.TypedDict, total=False):
    sha1: str
    sha256: str

@typing.type_check_only
class ApkDescription(typing.TypedDict, total=False):
    assetSliceMetadata: SplitApkMetadata
    instantApkMetadata: SplitApkMetadata
    path: str
    splitApkMetadata: SplitApkMetadata
    standaloneApkMetadata: StandaloneApkMetadata
    targeting: ApkTargeting

@typing.type_check_only
class ApkSet(typing.TypedDict, total=False):
    apkDescription: _list[ApkDescription]
    moduleMetadata: ModuleMetadata

@typing.type_check_only
class ApkTargeting(typing.TypedDict, total=False):
    abiTargeting: AbiTargeting
    languageTargeting: LanguageTargeting
    multiAbiTargeting: MultiAbiTargeting
    screenDensityTargeting: ScreenDensityTargeting
    sdkVersionTargeting: SdkVersionTargeting
    textureCompressionFormatTargeting: TextureCompressionFormatTargeting

@typing.type_check_only
class ApksAddExternallyHostedRequest(typing.TypedDict, total=False):
    externallyHostedApk: ExternallyHostedApk

@typing.type_check_only
class ApksAddExternallyHostedResponse(typing.TypedDict, total=False):
    externallyHostedApk: ExternallyHostedApk

@typing.type_check_only
class ApksListResponse(typing.TypedDict, total=False):
    apks: _list[Apk]
    kind: str

@typing.type_check_only
class AppContactInformation(typing.TypedDict, total=False):
    contactEmail: str
    phoneNumber: str
    websiteUrl: str

@typing.type_check_only
class AppDetails(typing.TypedDict, total=False):
    contactEmail: str
    contactPhone: str
    contactWebsite: str
    defaultLanguage: str

@typing.type_check_only
class AppEdit(typing.TypedDict, total=False):
    expiryTimeSeconds: str
    id: str

@typing.type_check_only
class AppRecoveryAction(typing.TypedDict, total=False):
    appRecoveryId: str
    cancelTime: str
    createTime: str
    deployTime: str
    lastUpdateTime: str
    remoteInAppUpdateData: RemoteInAppUpdateData
    status: typing.Literal[
        "RECOVERY_STATUS_UNSPECIFIED",
        "RECOVERY_STATUS_ACTIVE",
        "RECOVERY_STATUS_CANCELED",
        "RECOVERY_STATUS_DRAFT",
        "RECOVERY_STATUS_GENERATION_IN_PROGRESS",
        "RECOVERY_STATUS_GENERATION_FAILED",
    ]
    targeting: Targeting

@typing.type_check_only
class AppStoreAppActiveApkSet(typing.TypedDict, total=False):
    baseApkId: str
    splitApkId: _list[str]

@typing.type_check_only
class AppStoreAppActiveApks(typing.TypedDict, total=False):
    activeApkSets: _list[AppStoreAppActiveApkSet]

@typing.type_check_only
class AppStoreAppDetails(typing.TypedDict, total=False):
    contactEmail: str
    developerName: str
    developerWebsite: str

@typing.type_check_only
class AppStoreAppPolicyDeclaration(typing.TypedDict, total=False):
    declarationId: str
    responses: _list[PolicyResponse]

@typing.type_check_only
class AppStoreAppStoreListing(typing.TypedDict, total=False):
    appIconId: str
    appName: str
    fullDescription: str
    languageCode: str
    screenshotId: _list[str]
    shortDescription: str
    videoLink: str

@typing.type_check_only
class AppVersionList(typing.TypedDict, total=False):
    versionCodes: _list[str]

@typing.type_check_only
class AppVersionRange(typing.TypedDict, total=False):
    versionCodeEnd: str
    versionCodeStart: str

@typing.type_check_only
class ArchiveSubscriptionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ArtifactSummary(typing.TypedDict, total=False):
    versionCode: int

@typing.type_check_only
class AssetModuleMetadata(typing.TypedDict, total=False):
    deliveryType: typing.Literal[
        "UNKNOWN_DELIVERY_TYPE", "INSTALL_TIME", "ON_DEMAND", "FAST_FOLLOW"
    ]
    name: str

@typing.type_check_only
class AssetSliceSet(typing.TypedDict, total=False):
    apkDescription: _list[ApkDescription]
    assetModuleMetadata: AssetModuleMetadata

@typing.type_check_only
class AutoRenewingBasePlanType(typing.TypedDict, total=False):
    accountHoldDuration: str
    billingPeriodDuration: str
    gracePeriodDuration: str
    legacyCompatible: bool
    legacyCompatibleSubscriptionOfferId: str
    prorationMode: typing.Literal[
        "SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY",
    ]
    resubscribeState: typing.Literal[
        "RESUBSCRIBE_STATE_UNSPECIFIED",
        "RESUBSCRIBE_STATE_ACTIVE",
        "RESUBSCRIBE_STATE_INACTIVE",
    ]

@typing.type_check_only
class AutoRenewingPlan(typing.TypedDict, total=False):
    autoRenewEnabled: bool
    installmentDetails: InstallmentPlan
    priceChangeDetails: SubscriptionItemPriceChangeDetails
    priceStepUpConsentDetails: PriceStepUpConsentDetails
    recurringPrice: Money

@typing.type_check_only
class BaseDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class BasePlan(typing.TypedDict, total=False):
    autoRenewingBasePlanType: AutoRenewingBasePlanType
    basePlanId: str
    installmentsBasePlanType: InstallmentsBasePlanType
    offerTags: _list[OfferTag]
    otherRegionsConfig: OtherRegionsBasePlanConfig
    prepaidBasePlanType: PrepaidBasePlanType
    regionalConfigs: _list[RegionalBasePlanConfig]
    state: typing.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class BasePriceOfferPhase(typing.TypedDict, total=False): ...

@typing.type_check_only
class BatchDeleteOneTimeProductOffersRequest(typing.TypedDict, total=False):
    requests: _list[DeleteOneTimeProductOfferRequest]

@typing.type_check_only
class BatchDeleteOneTimeProductsRequest(typing.TypedDict, total=False):
    requests: _list[DeleteOneTimeProductRequest]

@typing.type_check_only
class BatchDeletePurchaseOptionsRequest(typing.TypedDict, total=False):
    requests: _list[DeletePurchaseOptionRequest]

@typing.type_check_only
class BatchGetOneTimeProductOffersRequest(typing.TypedDict, total=False):
    requests: _list[GetOneTimeProductOfferRequest]

@typing.type_check_only
class BatchGetOneTimeProductOffersResponse(typing.TypedDict, total=False):
    oneTimeProductOffers: _list[OneTimeProductOffer]

@typing.type_check_only
class BatchGetOneTimeProductsResponse(typing.TypedDict, total=False):
    oneTimeProducts: _list[OneTimeProduct]

@typing.type_check_only
class BatchGetOrdersResponse(typing.TypedDict, total=False):
    orders: _list[Order]

@typing.type_check_only
class BatchGetSubscriptionOffersRequest(typing.TypedDict, total=False):
    requests: _list[GetSubscriptionOfferRequest]

@typing.type_check_only
class BatchGetSubscriptionOffersResponse(typing.TypedDict, total=False):
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class BatchGetSubscriptionsResponse(typing.TypedDict, total=False):
    subscriptions: _list[Subscription]

@typing.type_check_only
class BatchMigrateBasePlanPricesRequest(typing.TypedDict, total=False):
    requests: _list[MigrateBasePlanPricesRequest]

@typing.type_check_only
class BatchMigrateBasePlanPricesResponse(typing.TypedDict, total=False):
    responses: _list[MigrateBasePlanPricesResponse]

@typing.type_check_only
class BatchUpdateBasePlanStatesRequest(typing.TypedDict, total=False):
    requests: _list[UpdateBasePlanStateRequest]

@typing.type_check_only
class BatchUpdateBasePlanStatesResponse(typing.TypedDict, total=False):
    subscriptions: _list[Subscription]

@typing.type_check_only
class BatchUpdateOneTimeProductOfferStatesRequest(typing.TypedDict, total=False):
    requests: _list[UpdateOneTimeProductOfferStateRequest]

@typing.type_check_only
class BatchUpdateOneTimeProductOfferStatesResponse(typing.TypedDict, total=False):
    oneTimeProductOffers: _list[OneTimeProductOffer]

@typing.type_check_only
class BatchUpdateOneTimeProductOffersRequest(typing.TypedDict, total=False):
    requests: _list[UpdateOneTimeProductOfferRequest]

@typing.type_check_only
class BatchUpdateOneTimeProductOffersResponse(typing.TypedDict, total=False):
    oneTimeProductOffers: _list[OneTimeProductOffer]

@typing.type_check_only
class BatchUpdateOneTimeProductsRequest(typing.TypedDict, total=False):
    requests: _list[UpdateOneTimeProductRequest]

@typing.type_check_only
class BatchUpdateOneTimeProductsResponse(typing.TypedDict, total=False):
    oneTimeProducts: _list[OneTimeProduct]

@typing.type_check_only
class BatchUpdatePurchaseOptionStatesRequest(typing.TypedDict, total=False):
    requests: _list[UpdatePurchaseOptionStateRequest]

@typing.type_check_only
class BatchUpdatePurchaseOptionStatesResponse(typing.TypedDict, total=False):
    oneTimeProducts: _list[OneTimeProduct]

@typing.type_check_only
class BatchUpdateSubscriptionOfferStatesRequest(typing.TypedDict, total=False):
    requests: _list[UpdateSubscriptionOfferStateRequest]

@typing.type_check_only
class BatchUpdateSubscriptionOfferStatesResponse(typing.TypedDict, total=False):
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class BatchUpdateSubscriptionOffersRequest(typing.TypedDict, total=False):
    requests: _list[UpdateSubscriptionOfferRequest]

@typing.type_check_only
class BatchUpdateSubscriptionOffersResponse(typing.TypedDict, total=False):
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class BatchUpdateSubscriptionsRequest(typing.TypedDict, total=False):
    requests: _list[UpdateSubscriptionRequest]

@typing.type_check_only
class BatchUpdateSubscriptionsResponse(typing.TypedDict, total=False):
    subscriptions: _list[Subscription]

@typing.type_check_only
class Bundle(typing.TypedDict, total=False):
    sha1: str
    sha256: str
    versionCode: int

@typing.type_check_only
class BundlesListResponse(typing.TypedDict, total=False):
    bundles: _list[Bundle]
    kind: str

@typing.type_check_only
class BuyerAddress(typing.TypedDict, total=False):
    buyerCountry: str
    buyerPostcode: str
    buyerState: str

@typing.type_check_only
class CancelAppRecoveryRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelAppRecoveryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelOneTimeProductOfferRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class CancelSubscriptionPurchaseRequest(typing.TypedDict, total=False):
    cancellationContext: CancellationContext

@typing.type_check_only
class CancelSubscriptionPurchaseResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelSurveyResult(typing.TypedDict, total=False):
    reason: typing.Literal[
        "CANCEL_SURVEY_REASON_UNSPECIFIED",
        "CANCEL_SURVEY_REASON_NOT_ENOUGH_USAGE",
        "CANCEL_SURVEY_REASON_TECHNICAL_ISSUES",
        "CANCEL_SURVEY_REASON_COST_RELATED",
        "CANCEL_SURVEY_REASON_FOUND_BETTER_APP",
        "CANCEL_SURVEY_REASON_OTHERS",
    ]
    reasonUserInput: str

@typing.type_check_only
class CanceledStateContext(typing.TypedDict, total=False):
    developerInitiatedCancellation: DeveloperInitiatedCancellation
    replacementCancellation: ReplacementCancellation
    systemInitiatedCancellation: SystemInitiatedCancellation
    userInitiatedCancellation: UserInitiatedCancellation

@typing.type_check_only
class CancellationContext(typing.TypedDict, total=False):
    cancellationType: typing.Literal[
        "CANCELLATION_TYPE_UNSPECIFIED",
        "USER_REQUESTED_STOP_RENEWALS",
        "DEVELOPER_REQUESTED_STOP_PAYMENTS",
    ]

@typing.type_check_only
class CancellationEvent(typing.TypedDict, total=False):
    eventTime: str

@typing.type_check_only
class CatalogAppView(typing.TypedDict, total=False):
    activeVersionNames: _list[str]
    appCategory: typing.Literal["APP_CATEGORY_UNSPECIFIED", "GAME", "APP"]
    appContactInformation: AppContactInformation
    appSubcategory: str
    deliveryToken: str
    developerDetails: DeveloperDetails
    deviceCompatibilityRequirements: _list[DeviceCompatibilityRequirements]
    excludedDevicesByIdentifier: _list[DeviceIdentifier]
    excludedDevicesBySelector: _list[CatalogDeviceSelector]
    firstReleaseDate: Date
    hasInAppAds: bool
    hasInAppPurchases: bool
    iarcCertificateId: str
    isAdultOnlyAudience: bool
    lastPublishTime: str
    localizedStoreListings: LocalizedStoreListings
    packageName: str
    permissions: _list[CatalogPermission]
    permissionsSdk23: _list[CatalogPermission]
    priceInTheUnitedStates: Money
    privacyPolicyUrl: str
    salePriceInTheUnitedStates: Money

@typing.type_check_only
class CatalogDeviceSelector(typing.TypedDict, total=False):
    deviceTypeSelector: typing.Literal["DEVICE_TYPE_SELECTOR_UNSPECIFIED", "ANDROID_GO"]
    ramSelector: RamSelector
    socSelectors: _list[SocSelector]

@typing.type_check_only
class CatalogPermission(typing.TypedDict, total=False):
    maxSdkVersion: int
    name: str

@typing.type_check_only
class CatalogSdkVersion(typing.TypedDict, total=False):
    maxSdkVersion: str
    minSdkVersion: str
    targetSdkVersion: str

@typing.type_check_only
class CoarseLocation(typing.TypedDict, total=False):
    administrativeArea: str
    locality: str
    regionCode: str
    sublocality: str

@typing.type_check_only
class Comment(typing.TypedDict, total=False):
    developerComment: DeveloperComment
    userComment: UserComment

@typing.type_check_only
class CompatibleScreen(typing.TypedDict, total=False):
    density: typing.Literal[
        "DENSITY_UNSPECIFIED",
        "DENSITY_NODPI",
        "DENSITY_LDPI",
        "DENSITY_MDPI",
        "DENSITY_TVDPI",
        "DENSITY_HDPI",
        "DENSITY_280",
        "DENSITY_XHDPI",
        "DENSITY_360",
        "DENSITY_400",
        "DENSITY_420",
        "DENSITY_XXHDPI",
        "DENSITY_560",
        "DENSITY_XXXHDPI",
    ]
    screenSize: typing.Literal[
        "SCREEN_SIZE_UNSPECIFIED",
        "SCREEN_SIZE_SMALL",
        "SCREEN_SIZE_NORMAL",
        "SCREEN_SIZE_LARGE",
        "SCREEN_SIZE_EXTRA_LARGE",
    ]

@typing.type_check_only
class ConsumptionUsageEvent(typing.TypedDict, total=False):
    consumptionItemDescription: str
    consumptionTime: str
    ipAddress: str
    location: CoarseLocation
    obfuscatedAccountId: str
    obfuscatedProfileId: str

@typing.type_check_only
class ConvertRegionPricesRequest(typing.TypedDict, total=False):
    price: Money
    productTaxCategoryCode: str

@typing.type_check_only
class ConvertRegionPricesResponse(typing.TypedDict, total=False):
    convertedOtherRegionsPrice: ConvertedOtherRegionsPrice
    convertedRegionPrices: dict[str, typing.Any]
    regionVersion: RegionsVersion

@typing.type_check_only
class ConvertedOtherRegionsPrice(typing.TypedDict, total=False):
    eurPrice: Money
    usdPrice: Money

@typing.type_check_only
class ConvertedRegionPrice(typing.TypedDict, total=False):
    price: Money
    regionCode: str
    taxAmount: Money

@typing.type_check_only
class CountryTargeting(typing.TypedDict, total=False):
    countries: _list[str]
    includeRestOfWorld: bool

@typing.type_check_only
class CreateAppStoreHostedAppRequest(typing.TypedDict, total=False):
    packageName: str

@typing.type_check_only
class CreateAppStoreHostedAppResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateDraftAppRecoveryRequest(typing.TypedDict, total=False):
    remoteInAppUpdate: RemoteInAppUpdate
    targeting: Targeting

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeactivateBasePlanRequest(typing.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str

@typing.type_check_only
class DeactivateOneTimeProductOfferRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class DeactivatePurchaseOptionRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class DeactivateSubscriptionOfferRequest(typing.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str

@typing.type_check_only
class DeferSubscriptionPurchaseRequest(typing.TypedDict, total=False):
    deferralContext: DeferralContext

@typing.type_check_only
class DeferSubscriptionPurchaseResponse(typing.TypedDict, total=False):
    itemExpiryTimeDetails: _list[ItemExpiryTimeDetails]

@typing.type_check_only
class DeferralContext(typing.TypedDict, total=False):
    deferDuration: str
    etag: str
    validateOnly: bool

@typing.type_check_only
class DeferredItemRemoval(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeferredItemReplacement(typing.TypedDict, total=False):
    productId: str

@typing.type_check_only
class DeleteOneTimeProductOfferRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    offerId: str
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class DeleteOneTimeProductRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str

@typing.type_check_only
class DeletePurchaseOptionRequest(typing.TypedDict, total=False):
    force: bool
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class DeobfuscationFile(typing.TypedDict, total=False):
    symbolType: typing.Literal[
        "deobfuscationFileTypeUnspecified", "proguard", "nativeCode"
    ]

@typing.type_check_only
class DeobfuscationFilesUploadResponse(typing.TypedDict, total=False):
    deobfuscationFile: DeobfuscationFile

@typing.type_check_only
class DeployAppRecoveryRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeployAppRecoveryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeveloperComment(typing.TypedDict, total=False):
    lastModified: Timestamp
    text: str

@typing.type_check_only
class DeveloperDetails(typing.TypedDict, total=False):
    address: str
    contactEmail: str
    developerName: str
    phoneNumber: str
    website: str

@typing.type_check_only
class DeveloperInitiatedCancellation(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeviceCompatibilityRequirements(typing.TypedDict, total=False):
    compatibleScreens: _list[CompatibleScreen]
    glEsVersion: int
    isScreenRequired: bool
    nativePlatforms: _list[str]
    requiredSoftwareLibraries: _list[str]
    requiredSystemFeatures: _list[str]
    requiresSmallestWidthDp: str
    sdkVersion: CatalogSdkVersion
    supportedGlTextures: _list[str]
    supportedScreens: _list[
        typing.Literal[
            "SCREEN_SIZE_UNSPECIFIED",
            "SCREEN_SIZE_SMALL",
            "SCREEN_SIZE_NORMAL",
            "SCREEN_SIZE_LARGE",
            "SCREEN_SIZE_EXTRA_LARGE",
        ]
    ]
    use32BitAbi: typing.Literal[
        "USE_32_BIT_ABI_UNSPECIFIED", "USE_32_BIT_ABI_TRUE", "USE_32_BIT_ABI_OTHER"
    ]
    usesConfigurations: _list[UsesConfiguration]

@typing.type_check_only
class DeviceFeature(typing.TypedDict, total=False):
    featureName: str
    featureVersion: int

@typing.type_check_only
class DeviceFeatureTargeting(typing.TypedDict, total=False):
    requiredFeature: DeviceFeature

@typing.type_check_only
class DeviceGroup(typing.TypedDict, total=False):
    deviceSelectors: _list[DeviceSelector]
    name: str

@typing.type_check_only
class DeviceId(typing.TypedDict, total=False):
    buildBrand: str
    buildDevice: str

@typing.type_check_only
class DeviceIdentifier(typing.TypedDict, total=False):
    deviceBrand: str
    deviceModel: str

@typing.type_check_only
class DeviceMetadata(typing.TypedDict, total=False):
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
class DeviceRam(typing.TypedDict, total=False):
    maxBytes: str
    minBytes: str

@typing.type_check_only
class DeviceSelector(typing.TypedDict, total=False):
    deviceRam: DeviceRam
    excludedDeviceIds: _list[DeviceId]
    forbiddenSystemFeatures: _list[SystemFeature]
    includedDeviceIds: _list[DeviceId]
    requiredSystemFeatures: _list[SystemFeature]
    systemOnChips: _list[SystemOnChip]

@typing.type_check_only
class DeviceSpec(typing.TypedDict, total=False):
    screenDensity: int
    supportedAbis: _list[str]
    supportedLocales: _list[str]

@typing.type_check_only
class DeviceTier(typing.TypedDict, total=False):
    deviceGroupNames: _list[str]
    level: int

@typing.type_check_only
class DeviceTierConfig(typing.TypedDict, total=False):
    deviceGroups: _list[DeviceGroup]
    deviceTierConfigId: str
    deviceTierSet: DeviceTierSet
    userCountrySets: _list[UserCountrySet]

@typing.type_check_only
class DeviceTierSet(typing.TypedDict, total=False):
    deviceTiers: _list[DeviceTier]

@typing.type_check_only
class ExpansionFile(typing.TypedDict, total=False):
    fileSize: str
    referencesVersion: int

@typing.type_check_only
class ExpansionFilesUploadResponse(typing.TypedDict, total=False):
    expansionFile: ExpansionFile

@typing.type_check_only
class ExternalAccountIdentifiers(typing.TypedDict, total=False):
    externalAccountId: str
    obfuscatedExternalAccountId: str
    obfuscatedExternalProfileId: str

@typing.type_check_only
class ExternalAccountIds(typing.TypedDict, total=False):
    obfuscatedAccountId: str
    obfuscatedProfileId: str

@typing.type_check_only
class ExternalOfferDetails(typing.TypedDict, total=False):
    appDownloadEventExternalTransactionId: str
    installedAppCategory: typing.Literal[
        "EXTERNAL_OFFER_APP_CATEGORY_UNSPECIFIED", "APP", "GAME"
    ]
    installedAppPackage: str
    linkType: typing.Literal[
        "EXTERNAL_OFFER_LINK_TYPE_UNSPECIFIED",
        "LINK_TO_DIGITAL_CONTENT_OFFER",
        "LINK_TO_APP_DOWNLOAD",
    ]

@typing.type_check_only
class ExternalSubscription(typing.TypedDict, total=False):
    subscriptionType: typing.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "RECURRING", "PREPAID"
    ]

@typing.type_check_only
class ExternalTransaction(typing.TypedDict, total=False):
    createTime: str
    currentPreTaxAmount: Price
    currentTaxAmount: Price
    externalOfferDetails: ExternalOfferDetails
    externalTransactionId: str
    oneTimeTransaction: OneTimeExternalTransaction
    originalPreTaxAmount: Price
    originalTaxAmount: Price
    packageName: str
    recurringTransaction: RecurringExternalTransaction
    testPurchase: ExternalTransactionTestPurchase
    transactionProgramCode: int
    transactionState: typing.Literal[
        "TRANSACTION_STATE_UNSPECIFIED", "TRANSACTION_REPORTED", "TRANSACTION_CANCELED"
    ]
    transactionTime: str
    userTaxAddress: ExternalTransactionAddress

@typing.type_check_only
class ExternalTransactionAddress(typing.TypedDict, total=False):
    administrativeArea: str
    regionCode: str

@typing.type_check_only
class ExternalTransactionTestPurchase(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExternallyHostedApk(typing.TypedDict, total=False):
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
class FreeTrialDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class FreeTrialOfferPhase(typing.TypedDict, total=False): ...

@typing.type_check_only
class FullRefund(typing.TypedDict, total=False): ...

@typing.type_check_only
class GeneratedApksListResponse(typing.TypedDict, total=False):
    generatedApks: _list[GeneratedApksPerSigningKey]

@typing.type_check_only
class GeneratedApksPerSigningKey(typing.TypedDict, total=False):
    certificateSha256Hash: str
    generatedAssetPackSlices: _list[GeneratedAssetPackSlice]
    generatedRecoveryModules: _list[GeneratedRecoveryApk]
    generatedSplitApks: _list[GeneratedSplitApk]
    generatedStandaloneApks: _list[GeneratedStandaloneApk]
    generatedUniversalApk: GeneratedUniversalApk
    targetingInfo: TargetingInfo
    unprotectedGeneratedSplitApks: _list[GeneratedSplitApk]
    unprotectedGeneratedStandaloneApks: _list[GeneratedStandaloneApk]

@typing.type_check_only
class GeneratedAssetPackSlice(typing.TypedDict, total=False):
    downloadId: str
    moduleName: str
    sliceId: str
    version: str

@typing.type_check_only
class GeneratedRecoveryApk(typing.TypedDict, total=False):
    downloadId: str
    moduleName: str
    recoveryId: str
    recoveryStatus: typing.Literal[
        "RECOVERY_STATUS_UNSPECIFIED",
        "RECOVERY_STATUS_ACTIVE",
        "RECOVERY_STATUS_CANCELED",
        "RECOVERY_STATUS_DRAFT",
        "RECOVERY_STATUS_GENERATION_IN_PROGRESS",
        "RECOVERY_STATUS_GENERATION_FAILED",
    ]

@typing.type_check_only
class GeneratedSplitApk(typing.TypedDict, total=False):
    downloadId: str
    moduleName: str
    splitId: str
    variantId: int

@typing.type_check_only
class GeneratedStandaloneApk(typing.TypedDict, total=False):
    downloadId: str
    variantId: int

@typing.type_check_only
class GeneratedUniversalApk(typing.TypedDict, total=False):
    downloadId: str

@typing.type_check_only
class GetOneTimeProductOfferRequest(typing.TypedDict, total=False):
    offerId: str
    packageName: str
    productId: str
    purchaseOptionId: str

@typing.type_check_only
class GetSubscriptionOfferRequest(typing.TypedDict, total=False):
    basePlanId: str
    offerId: str
    packageName: str
    productId: str

@typing.type_check_only
class Grant(typing.TypedDict, total=False):
    appLevelPermissions: _list[
        typing.Literal[
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
class Group(typing.TypedDict, total=False):
    responses: _list[NestedPolicyResponse]

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    aiGeneratedState: typing.Literal[
        "aiGeneratedStateUnspecified",
        "aiGeneratedStateNotAiGenerated",
        "aiGeneratedStateAiGeneratedDeveloperAttested",
    ]
    id: str
    sha1: str
    sha256: str
    url: str

@typing.type_check_only
class ImageAsset(typing.TypedDict, total=False):
    imageUrl: str

@typing.type_check_only
class ImagesDeleteAllResponse(typing.TypedDict, total=False):
    deleted: _list[Image]

@typing.type_check_only
class ImagesListResponse(typing.TypedDict, total=False):
    images: _list[Image]

@typing.type_check_only
class ImagesUploadResponse(typing.TypedDict, total=False):
    image: Image

@typing.type_check_only
class InAppProduct(typing.TypedDict, total=False):
    defaultLanguage: str
    defaultPrice: Price
    gracePeriod: str
    listings: dict[str, typing.Any]
    managedProductTaxesAndComplianceSettings: ManagedProductTaxAndComplianceSettings
    packageName: str
    prices: dict[str, typing.Any]
    purchaseType: typing.Literal[
        "purchaseTypeUnspecified", "managedUser", "subscription"
    ]
    sku: str
    status: typing.Literal["statusUnspecified", "active", "inactive"]
    subscriptionPeriod: str
    subscriptionTaxesAndComplianceSettings: SubscriptionTaxAndComplianceSettings
    trialPeriod: str

@typing.type_check_only
class InAppProductListing(typing.TypedDict, total=False):
    benefits: _list[str]
    description: str
    title: str

@typing.type_check_only
class InGracePeriodStateContext(typing.TypedDict, total=False):
    renewalDeclined: RenewalDeclinedContext

@typing.type_check_only
class InappproductsBatchDeleteRequest(typing.TypedDict, total=False):
    requests: _list[InappproductsDeleteRequest]

@typing.type_check_only
class InappproductsBatchGetResponse(typing.TypedDict, total=False):
    inappproduct: _list[InAppProduct]

@typing.type_check_only
class InappproductsBatchUpdateRequest(typing.TypedDict, total=False):
    requests: _list[InappproductsUpdateRequest]

@typing.type_check_only
class InappproductsBatchUpdateResponse(typing.TypedDict, total=False):
    inappproducts: _list[InAppProduct]

@typing.type_check_only
class InappproductsDeleteRequest(typing.TypedDict, total=False):
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    sku: str

@typing.type_check_only
class InappproductsListResponse(typing.TypedDict, total=False):
    inappproduct: _list[InAppProduct]
    kind: str
    pageInfo: PageInfo
    tokenPagination: TokenPagination

@typing.type_check_only
class InappproductsUpdateRequest(typing.TypedDict, total=False):
    allowMissing: bool
    autoConvertMissingPrices: bool
    inappproduct: InAppProduct
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    sku: str

@typing.type_check_only
class InstallmentPlan(typing.TypedDict, total=False):
    initialCommittedPaymentsCount: int
    pendingCancellation: PendingCancellation
    remainingCommittedPaymentsCount: int
    subsequentCommittedPaymentsCount: int

@typing.type_check_only
class InstallmentsBasePlanType(typing.TypedDict, total=False):
    accountHoldDuration: str
    billingPeriodDuration: str
    committedPaymentsCount: int
    gracePeriodDuration: str
    prorationMode: typing.Literal[
        "SUBSCRIPTION_PRORATION_MODE_UNSPECIFIED",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_ON_NEXT_BILLING_DATE",
        "SUBSCRIPTION_PRORATION_MODE_CHARGE_FULL_PRICE_IMMEDIATELY",
    ]
    renewalType: typing.Literal[
        "RENEWAL_TYPE_UNSPECIFIED",
        "RENEWAL_TYPE_RENEWS_WITHOUT_COMMITMENT",
        "RENEWAL_TYPE_RENEWS_WITH_COMMITMENT",
    ]
    resubscribeState: typing.Literal[
        "RESUBSCRIBE_STATE_UNSPECIFIED",
        "RESUBSCRIBE_STATE_ACTIVE",
        "RESUBSCRIBE_STATE_INACTIVE",
    ]

@typing.type_check_only
class InternalAppSharingArtifact(typing.TypedDict, total=False):
    certificateFingerprint: str
    downloadUrl: str
    sha256: str

@typing.type_check_only
class IntroductoryPriceDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class IntroductoryPriceOfferPhase(typing.TypedDict, total=False): ...

@typing.type_check_only
class ItemExpiryTimeDetails(typing.TypedDict, total=False):
    expiryTime: str
    productId: str

@typing.type_check_only
class ItemReplacement(typing.TypedDict, total=False):
    basePlanId: str
    offerId: str
    productId: str
    replacementMode: typing.Literal[
        "REPLACEMENT_MODE_UNSPECIFIED",
        "WITH_TIME_PRORATION",
        "CHARGE_PRORATED_PRICE",
        "WITHOUT_PRORATION",
        "CHARGE_FULL_PRICE",
        "DEFERRED",
        "KEEP_EXISTING",
    ]

@typing.type_check_only
class KeyedGroup(typing.TypedDict, total=False):
    key: str
    responses: _list[NestedPolicyResponse]

@typing.type_check_only
class LanguageTargeting(typing.TypedDict, total=False):
    alternatives: _list[str]
    value: _list[str]

@typing.type_check_only
class LineItem(typing.TypedDict, total=False):
    listingPrice: Money
    oneTimePurchaseDetails: OneTimePurchaseDetails
    paidAppDetails: PaidAppDetails
    productId: str
    productTitle: str
    subscriptionDetails: SubscriptionDetails
    tax: Money
    total: Money

@typing.type_check_only
class ListAppRecoveriesResponse(typing.TypedDict, total=False):
    recoveryActions: _list[AppRecoveryAction]

@typing.type_check_only
class ListDeviceTierConfigsResponse(typing.TypedDict, total=False):
    deviceTierConfigs: _list[DeviceTierConfig]
    nextPageToken: str

@typing.type_check_only
class ListOneTimeProductOffersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    oneTimeProductOffers: _list[OneTimeProductOffer]

@typing.type_check_only
class ListOneTimeProductsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    oneTimeProducts: _list[OneTimeProduct]

@typing.type_check_only
class ListRecentUpdateEventsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    recentUpdateEvents: _list[RecentUpdateEvent]

@typing.type_check_only
class ListReleaseSummariesResponse(typing.TypedDict, total=False):
    releases: _list[ReleaseSummary]

@typing.type_check_only
class ListSubscriptionOffersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptionOffers: _list[SubscriptionOffer]

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class Listing(typing.TypedDict, total=False):
    fullDescription: str
    language: str
    shortDescription: str
    title: str
    video: str

@typing.type_check_only
class ListingsListResponse(typing.TypedDict, total=False):
    kind: str
    listings: _list[Listing]

@typing.type_check_only
class LocalizedStoreListing(typing.TypedDict, total=False):
    appName: str
    featureGraphic: ImageAsset
    fullDescription: str
    icon: ImageAsset
    languageCode: str
    phoneScreenshots: ScreenshotSet
    shortDescription: str
    tabletRegularScreenshots: ScreenshotSet
    tabletSmallScreenshots: ScreenshotSet
    video: VideoAsset

@typing.type_check_only
class LocalizedStoreListings(typing.TypedDict, total=False):
    defaultLanguageCode: str
    localizedStoreListings: _list[LocalizedStoreListing]

@typing.type_check_only
class LocalizedText(typing.TypedDict, total=False):
    language: str
    text: str

@typing.type_check_only
class ManagedProductTaxAndComplianceSettings(typing.TypedDict, total=False):
    eeaWithdrawalRightType: typing.Literal[
        "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED",
        "WITHDRAWAL_RIGHT_DIGITAL_CONTENT",
        "WITHDRAWAL_RIGHT_SERVICE",
    ]
    isTokenizedDigitalAsset: bool
    productTaxCategoryCode: str
    regionalProductAgeRatingInfos: _list[RegionalProductAgeRatingInfo]
    taxRateInfoByRegionCode: dict[str, typing.Any]

@typing.type_check_only
class MigrateBasePlanPricesRequest(typing.TypedDict, total=False):
    basePlanId: str
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    packageName: str
    productId: str
    regionalPriceMigrations: _list[RegionalPriceMigrationConfig]
    regionsVersion: RegionsVersion

@typing.type_check_only
class MigrateBasePlanPricesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ModuleMetadata(typing.TypedDict, total=False):
    deliveryType: typing.Literal[
        "UNKNOWN_DELIVERY_TYPE", "INSTALL_TIME", "ON_DEMAND", "FAST_FOLLOW"
    ]
    dependencies: _list[str]
    moduleType: typing.Literal["UNKNOWN_MODULE_TYPE", "FEATURE_MODULE"]
    name: str
    targeting: ModuleTargeting

@typing.type_check_only
class ModuleTargeting(typing.TypedDict, total=False):
    deviceFeatureTargeting: _list[DeviceFeatureTargeting]
    sdkVersionTargeting: SdkVersionTargeting
    userCountriesTargeting: UserCountriesTargeting

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MultiAbi(typing.TypedDict, total=False):
    abi: _list[Abi]

@typing.type_check_only
class MultiAbiTargeting(typing.TypedDict, total=False):
    alternatives: _list[MultiAbi]
    value: _list[MultiAbi]

@typing.type_check_only
class NestedPolicyResponse(typing.TypedDict, total=False):
    booleanResponse: PolicyBooleanResponse
    documentResponse: PolicyDocumentResponse
    multipleChoiceResponse: PolicyMultipleChoiceResponse
    questionId: str
    singleChoiceResponse: PolicySingleChoiceResponse
    stringResponse: PolicyStringResponse

@typing.type_check_only
class OfferDetails(typing.TypedDict, total=False):
    basePlanId: str
    offerId: str
    offerTags: _list[str]

@typing.type_check_only
class OfferPhase(typing.TypedDict, total=False):
    basePrice: BasePriceOfferPhase
    freeTrial: FreeTrialOfferPhase
    introductoryPrice: IntroductoryPriceOfferPhase
    prorationPeriod: ProrationPeriodOfferPhase

@typing.type_check_only
class OfferPhaseDetails(typing.TypedDict, total=False):
    baseDetails: BaseDetails
    freeTrialDetails: FreeTrialDetails
    introductoryPriceDetails: IntroductoryPriceDetails
    prorationPeriodDetails: ProrationPeriodDetails

@typing.type_check_only
class OfferTag(typing.TypedDict, total=False):
    tag: str

@typing.type_check_only
class OnHoldStateContext(typing.TypedDict, total=False):
    renewalDeclined: RenewalDeclinedContext

@typing.type_check_only
class OneTimeCode(typing.TypedDict, total=False): ...

@typing.type_check_only
class OneTimeExternalTransaction(typing.TypedDict, total=False):
    externalTransactionToken: str

@typing.type_check_only
class OneTimeProduct(typing.TypedDict, total=False):
    listings: _list[OneTimeProductListing]
    offerTags: _list[OfferTag]
    packageName: str
    productId: str
    purchaseOptions: _list[OneTimeProductPurchaseOption]
    regionsVersion: RegionsVersion
    restrictedPaymentCountries: RestrictedPaymentCountries
    taxAndComplianceSettings: OneTimeProductTaxAndComplianceSettings

@typing.type_check_only
class OneTimeProductBuyPurchaseOption(typing.TypedDict, total=False):
    legacyCompatible: bool
    multiQuantityEnabled: bool

@typing.type_check_only
class OneTimeProductDiscountedOffer(typing.TypedDict, total=False):
    endTime: str
    redemptionLimit: str
    startTime: str

@typing.type_check_only
class OneTimeProductListing(typing.TypedDict, total=False):
    description: str
    languageCode: str
    title: str

@typing.type_check_only
class OneTimeProductOffer(typing.TypedDict, total=False):
    discountedOffer: OneTimeProductDiscountedOffer
    offerId: str
    offerTags: _list[OfferTag]
    packageName: str
    preOrderOffer: OneTimeProductPreOrderOffer
    productId: str
    purchaseOptionId: str
    regionalPricingAndAvailabilityConfigs: _list[
        OneTimeProductOfferRegionalPricingAndAvailabilityConfig
    ]
    regionsVersion: RegionsVersion
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "CANCELLED", "INACTIVE"
    ]

@typing.type_check_only
class OneTimeProductOfferNoPriceOverrideOptions(typing.TypedDict, total=False): ...

@typing.type_check_only
class OneTimeProductOfferRegionalPricingAndAvailabilityConfig(
    typing.TypedDict, total=False
):
    absoluteDiscount: Money
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "AVAILABLE", "NO_LONGER_AVAILABLE"
    ]
    noOverride: OneTimeProductOfferNoPriceOverrideOptions
    regionCode: str
    relativeDiscount: float

@typing.type_check_only
class OneTimeProductPreOrderOffer(typing.TypedDict, total=False):
    endTime: str
    priceChangeBehavior: typing.Literal[
        "PRE_ORDER_PRICE_CHANGE_BEHAVIOR_UNSPECIFIED",
        "PRE_ORDER_PRICE_CHANGE_BEHAVIOR_TWO_POINT_LOWEST",
        "PRE_ORDER_PRICE_CHANGE_BEHAVIOR_NEW_ORDERS_ONLY",
    ]
    releaseTime: str
    startTime: str

@typing.type_check_only
class OneTimeProductPurchaseOption(typing.TypedDict, total=False):
    buyOption: OneTimeProductBuyPurchaseOption
    newRegionsConfig: OneTimeProductPurchaseOptionNewRegionsConfig
    offerTags: _list[OfferTag]
    purchaseOptionId: str
    regionalPricingAndAvailabilityConfigs: _list[
        OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig
    ]
    rentOption: OneTimeProductRentPurchaseOption
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "INACTIVE", "INACTIVE_PUBLISHED"
    ]
    taxAndComplianceSettings: PurchaseOptionTaxAndComplianceSettings

@typing.type_check_only
class OneTimeProductPurchaseOptionNewRegionsConfig(typing.TypedDict, total=False):
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "AVAILABLE", "NO_LONGER_AVAILABLE"
    ]
    eurPrice: Money
    usdPrice: Money

@typing.type_check_only
class OneTimeProductPurchaseOptionRegionalPricingAndAvailabilityConfig(
    typing.TypedDict, total=False
):
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED",
        "AVAILABLE",
        "NO_LONGER_AVAILABLE",
        "AVAILABLE_IF_RELEASED",
        "AVAILABLE_FOR_OFFERS_ONLY",
    ]
    price: Money
    regionCode: str

@typing.type_check_only
class OneTimeProductRentPurchaseOption(typing.TypedDict, total=False):
    expirationPeriod: str
    rentalPeriod: str

@typing.type_check_only
class OneTimeProductTaxAndComplianceSettings(typing.TypedDict, total=False):
    isTokenizedDigitalAsset: bool
    productTaxCategoryCode: str
    regionalProductAgeRatingInfos: _list[RegionalProductAgeRatingInfo]
    regionalTaxConfigs: _list[RegionalTaxConfig]

@typing.type_check_only
class OneTimePurchaseDetails(typing.TypedDict, total=False):
    offerId: str
    preorderDetails: PreorderDetails
    purchaseOptionId: str
    quantity: int
    rentalDetails: RentalDetails

@typing.type_check_only
class Order(typing.TypedDict, total=False):
    buyerAddress: BuyerAddress
    createTime: str
    developerRevenueInBuyerCurrency: Money
    lastEventTime: str
    lineItems: _list[LineItem]
    orderDetails: OrderDetails
    orderHistory: OrderHistory
    orderId: str
    pointsDetails: PointsDetails
    purchaseToken: str
    salesChannel: typing.Literal[
        "SALES_CHANNEL_UNSPECIFIED",
        "IN_APP",
        "PC_EMULATOR",
        "NATIVE_PC",
        "PLAY_STORE",
        "OUTSIDE_PLAY_STORE",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "PROCESSED",
        "CANCELED",
        "PENDING_REFUND",
        "PARTIALLY_REFUNDED",
        "REFUNDED",
    ]
    tax: Money
    total: Money

@typing.type_check_only
class OrderDetails(typing.TypedDict, total=False):
    taxInclusive: bool

@typing.type_check_only
class OrderHistory(typing.TypedDict, total=False):
    cancellationEvent: CancellationEvent
    partialRefundEvents: _list[PartialRefundEvent]
    processedEvent: ProcessedEvent
    refundEvent: RefundEvent

@typing.type_check_only
class OrdersReviewRefundRequest(typing.TypedDict, total=False):
    consumptionPercentageMilliunits: int
    consumptionUsageEvents: _list[ConsumptionUsageEvent]
    pendingRefundToken: str
    refundPreference: typing.Literal[
        "REFUND_PREFERENCE_UNSPECIFIED", "DECLINE", "APPROVE", "NEUTRAL"
    ]
    sampleContentProvided: bool

@typing.type_check_only
class OtherRecurringProduct(typing.TypedDict, total=False): ...

@typing.type_check_only
class OtherRegionsBasePlanConfig(typing.TypedDict, total=False):
    eurPrice: Money
    newSubscriberAvailability: bool
    usdPrice: Money

@typing.type_check_only
class OtherRegionsSubscriptionOfferConfig(typing.TypedDict, total=False):
    otherRegionsNewSubscriberAvailability: bool

@typing.type_check_only
class OtherRegionsSubscriptionOfferPhaseConfig(typing.TypedDict, total=False):
    absoluteDiscounts: OtherRegionsSubscriptionOfferPhasePrices
    free: OtherRegionsSubscriptionOfferPhaseFreePriceOverride
    otherRegionsPrices: OtherRegionsSubscriptionOfferPhasePrices
    relativeDiscount: float

@typing.type_check_only
class OtherRegionsSubscriptionOfferPhaseFreePriceOverride(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class OtherRegionsSubscriptionOfferPhasePrices(typing.TypedDict, total=False):
    eurPrice: Money
    usdPrice: Money

@typing.type_check_only
class OutOfAppPurchaseContext(typing.TypedDict, total=False):
    expiredExternalAccountIdentifiers: ExternalAccountIdentifiers
    expiredPurchaseToken: str

@typing.type_check_only
class PageInfo(typing.TypedDict, total=False):
    resultPerPage: int
    startIndex: int
    totalResults: int

@typing.type_check_only
class PaidAppDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class PartialRefund(typing.TypedDict, total=False):
    refundId: str
    refundPreTaxAmount: Price

@typing.type_check_only
class PartialRefundEvent(typing.TypedDict, total=False):
    createTime: str
    processTime: str
    refundDetails: RefundDetails
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "PROCESSED_SUCCESSFULLY"]

@typing.type_check_only
class PausedStateContext(typing.TypedDict, total=False):
    autoResumeTime: str

@typing.type_check_only
class PendingCancellation(typing.TypedDict, total=False): ...

@typing.type_check_only
class PointsDetails(typing.TypedDict, total=False):
    pointsCouponValue: Money
    pointsDiscountRateMicros: str
    pointsOfferId: str
    pointsSpent: str

@typing.type_check_only
class PolicyBooleanResponse(typing.TypedDict, total=False):
    value: bool

@typing.type_check_only
class PolicyDocumentResponse(typing.TypedDict, total=False):
    documentId: str
    expiryDate: Date
    nonExpiring: bool

@typing.type_check_only
class PolicyGroupResponse(typing.TypedDict, total=False):
    groups: _list[Group]

@typing.type_check_only
class PolicyKeyedGroupResponse(typing.TypedDict, total=False):
    groups: _list[KeyedGroup]

@typing.type_check_only
class PolicyMultipleChoiceResponse(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class PolicyResponse(typing.TypedDict, total=False):
    booleanResponse: PolicyBooleanResponse
    documentResponse: PolicyDocumentResponse
    groupResponse: PolicyGroupResponse
    keyedGroupResponse: PolicyKeyedGroupResponse
    multipleChoiceResponse: PolicyMultipleChoiceResponse
    questionId: str
    singleChoiceResponse: PolicySingleChoiceResponse
    stringResponse: PolicyStringResponse

@typing.type_check_only
class PolicySingleChoiceResponse(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class PolicyStringResponse(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class PreorderDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class PreorderOfferDetails(typing.TypedDict, total=False):
    preorderReleaseTime: str

@typing.type_check_only
class PrepaidBasePlanType(typing.TypedDict, total=False):
    billingPeriodDuration: str
    timeExtension: typing.Literal[
        "TIME_EXTENSION_UNSPECIFIED", "TIME_EXTENSION_ACTIVE", "TIME_EXTENSION_INACTIVE"
    ]

@typing.type_check_only
class PrepaidPlan(typing.TypedDict, total=False):
    allowExtendAfterTime: str

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    currency: str
    priceMicros: str

@typing.type_check_only
class PriceStepUpConsentDetails(typing.TypedDict, total=False):
    consentDeadlineTime: str
    newPrice: Money
    state: typing.Literal[
        "CONSENT_STATE_UNSPECIFIED", "PENDING", "CONFIRMED", "COMPLETED"
    ]

@typing.type_check_only
class ProcessedEvent(typing.TypedDict, total=False):
    eventTime: str

@typing.type_check_only
class ProductLineItem(typing.TypedDict, total=False):
    productId: str
    productOfferDetails: ProductOfferDetails

@typing.type_check_only
class ProductOfferDetails(typing.TypedDict, total=False):
    consumptionState: typing.Literal[
        "CONSUMPTION_STATE_UNSPECIFIED",
        "CONSUMPTION_STATE_YET_TO_BE_CONSUMED",
        "CONSUMPTION_STATE_CONSUMED",
    ]
    offerId: str
    offerTags: _list[str]
    offerToken: str
    preorderOfferDetails: PreorderOfferDetails
    purchaseOptionId: str
    quantity: int
    refundableQuantity: int
    rentOfferDetails: RentOfferDetails

@typing.type_check_only
class ProductPurchase(typing.TypedDict, total=False):
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
class ProductPurchaseV2(typing.TypedDict, total=False):
    acknowledgementState: typing.Literal[
        "ACKNOWLEDGEMENT_STATE_UNSPECIFIED",
        "ACKNOWLEDGEMENT_STATE_PENDING",
        "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED",
    ]
    kind: str
    obfuscatedExternalAccountId: str
    obfuscatedExternalProfileId: str
    orderId: str
    productLineItem: _list[ProductLineItem]
    purchaseCompletionTime: str
    purchaseStateContext: PurchaseStateContext
    regionCode: str
    testPurchaseContext: TestPurchaseContext

@typing.type_check_only
class ProductPurchasesAcknowledgeRequest(typing.TypedDict, total=False):
    developerPayload: str

@typing.type_check_only
class ProrationPeriodDetails(typing.TypedDict, total=False):
    originalOfferPhase: typing.Literal[
        "OFFER_PHASE_UNSPECIFIED", "BASE", "INTRODUCTORY", "FREE_TRIAL"
    ]

@typing.type_check_only
class ProrationPeriodOfferPhase(typing.TypedDict, total=False):
    originalOfferPhaseType: typing.Literal[
        "ORIGINAL_OFFER_PHASE_TYPE_UNSPECIFIED", "BASE", "INTRODUCTORY", "FREE_TRIAL"
    ]

@typing.type_check_only
class PurchaseOptionTaxAndComplianceSettings(typing.TypedDict, total=False):
    withdrawalRightType: typing.Literal[
        "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED",
        "WITHDRAWAL_RIGHT_DIGITAL_CONTENT",
        "WITHDRAWAL_RIGHT_SERVICE",
    ]

@typing.type_check_only
class PurchaseStateContext(typing.TypedDict, total=False):
    purchaseState: typing.Literal[
        "PURCHASE_STATE_UNSPECIFIED", "PURCHASED", "CANCELLED", "PENDING"
    ]

@typing.type_check_only
class RamSelector(typing.TypedDict, total=False):
    ramMbLessThanOrEqual: str

@typing.type_check_only
class RecentAppView(typing.TypedDict, total=False):
    appView: CatalogAppView

@typing.type_check_only
class RecentUpdateEvent(typing.TypedDict, total=False):
    eventTime: str
    playAppPackageName: str
    updateType: typing.Literal["UPDATE_TYPE_UNSPECIFIED", "MODIFICATION", "DELETION"]

@typing.type_check_only
class RecurringExternalTransaction(typing.TypedDict, total=False):
    externalSubscription: ExternalSubscription
    externalTransactionToken: str
    initialExternalTransactionId: str
    migratedTransactionProgram: typing.Literal[
        "EXTERNAL_TRANSACTION_PROGRAM_UNSPECIFIED",
        "USER_CHOICE_BILLING",
        "ALTERNATIVE_BILLING_ONLY",
    ]
    otherRecurringProduct: OtherRecurringProduct

@typing.type_check_only
class RefundDetails(typing.TypedDict, total=False):
    tax: Money
    total: Money

@typing.type_check_only
class RefundEvent(typing.TypedDict, total=False):
    eventTime: str
    refundDetails: RefundDetails
    refundReason: typing.Literal["REFUND_REASON_UNSPECIFIED", "OTHER", "CHARGEBACK"]

@typing.type_check_only
class RefundExternalTransactionRequest(typing.TypedDict, total=False):
    fullRefund: FullRefund
    partialRefund: PartialRefund
    refundTime: str

@typing.type_check_only
class RegionalBasePlanConfig(typing.TypedDict, total=False):
    newSubscriberAvailability: bool
    price: Money
    regionCode: str

@typing.type_check_only
class RegionalPriceMigrationConfig(typing.TypedDict, total=False):
    oldestAllowedPriceVersionTime: str
    priceIncreaseType: typing.Literal[
        "PRICE_INCREASE_TYPE_UNSPECIFIED",
        "PRICE_INCREASE_TYPE_OPT_IN",
        "PRICE_INCREASE_TYPE_OPT_OUT",
    ]
    regionCode: str

@typing.type_check_only
class RegionalProductAgeRatingInfo(typing.TypedDict, total=False):
    productAgeRatingTier: typing.Literal[
        "PRODUCT_AGE_RATING_TIER_UNKNOWN",
        "PRODUCT_AGE_RATING_TIER_EVERYONE",
        "PRODUCT_AGE_RATING_TIER_THIRTEEN_AND_ABOVE",
        "PRODUCT_AGE_RATING_TIER_SIXTEEN_AND_ABOVE",
        "PRODUCT_AGE_RATING_TIER_EIGHTEEN_AND_ABOVE",
    ]
    regionCode: str

@typing.type_check_only
class RegionalSubscriptionOfferConfig(typing.TypedDict, total=False):
    newSubscriberAvailability: bool
    regionCode: str

@typing.type_check_only
class RegionalSubscriptionOfferPhaseConfig(typing.TypedDict, total=False):
    absoluteDiscount: Money
    free: RegionalSubscriptionOfferPhaseFreePriceOverride
    price: Money
    regionCode: str
    relativeDiscount: float

@typing.type_check_only
class RegionalSubscriptionOfferPhaseFreePriceOverride(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class RegionalTaxConfig(typing.TypedDict, total=False):
    eligibleForStreamingServiceTaxRate: bool
    regionCode: str
    streamingTaxType: typing.Literal[
        "STREAMING_TAX_TYPE_UNSPECIFIED",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_SALES",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_SALES",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL",
    ]
    taxTier: typing.Literal[
        "TAX_TIER_UNSPECIFIED",
        "TAX_TIER_BOOKS_1",
        "TAX_TIER_NEWS_1",
        "TAX_TIER_NEWS_2",
        "TAX_TIER_MUSIC_OR_AUDIO_1",
        "TAX_TIER_LIVE_OR_BROADCAST_1",
    ]

@typing.type_check_only
class RegionalTaxRateInfo(typing.TypedDict, total=False):
    eligibleForStreamingServiceTaxRate: bool
    streamingTaxType: typing.Literal[
        "STREAMING_TAX_TYPE_UNSPECIFIED",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_SALES",
        "STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_SALES",
        "STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL",
    ]
    taxTier: typing.Literal[
        "TAX_TIER_UNSPECIFIED",
        "TAX_TIER_BOOKS_1",
        "TAX_TIER_NEWS_1",
        "TAX_TIER_NEWS_2",
        "TAX_TIER_MUSIC_OR_AUDIO_1",
        "TAX_TIER_LIVE_OR_BROADCAST_1",
    ]

@typing.type_check_only
class Regions(typing.TypedDict, total=False):
    regionCode: _list[str]

@typing.type_check_only
class RegionsVersion(typing.TypedDict, total=False):
    version: str

@typing.type_check_only
class ReleaseSummary(typing.TypedDict, total=False):
    activeArtifacts: _list[ArtifactSummary]
    releaseLifecycleState: typing.Literal[
        "RELEASE_LIFECYCLE_STATE_UNSPECIFIED",
        "RELEASE_LIFECYCLE_STATE_DRAFT",
        "RELEASE_LIFECYCLE_STATE_NOT_SENT_FOR_REVIEW",
        "RELEASE_LIFECYCLE_STATE_IN_REVIEW",
        "RELEASE_LIFECYCLE_STATE_APPROVED_NOT_PUBLISHED",
        "RELEASE_LIFECYCLE_STATE_NOT_APPROVED",
        "RELEASE_LIFECYCLE_STATE_PUBLISHED",
    ]
    releaseName: str
    track: str

@typing.type_check_only
class RemoteInAppUpdate(typing.TypedDict, total=False):
    isRemoteInAppUpdateRequested: bool

@typing.type_check_only
class RemoteInAppUpdateData(typing.TypedDict, total=False):
    remoteAppUpdateDataPerBundle: _list[RemoteInAppUpdateDataPerBundle]

@typing.type_check_only
class RemoteInAppUpdateDataPerBundle(typing.TypedDict, total=False):
    recoveredDeviceCount: str
    totalDeviceCount: str
    versionCode: str

@typing.type_check_only
class RenewalDeclinedContext(typing.TypedDict, total=False):
    pendingOrderId: str

@typing.type_check_only
class RentOfferDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class RentalDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class ReplacementCancellation(typing.TypedDict, total=False): ...

@typing.type_check_only
class RestrictedPaymentCountries(typing.TypedDict, total=False):
    regionCodes: _list[str]

@typing.type_check_only
class Review(typing.TypedDict, total=False):
    authorName: str
    comments: _list[Comment]
    reviewId: str

@typing.type_check_only
class ReviewReplyResult(typing.TypedDict, total=False):
    lastEdited: Timestamp
    replyText: str

@typing.type_check_only
class ReviewsListResponse(typing.TypedDict, total=False):
    pageInfo: PageInfo
    reviews: _list[Review]
    tokenPagination: TokenPagination

@typing.type_check_only
class ReviewsReplyRequest(typing.TypedDict, total=False):
    replyText: str

@typing.type_check_only
class ReviewsReplyResponse(typing.TypedDict, total=False):
    result: ReviewReplyResult

@typing.type_check_only
class RevocationContext(typing.TypedDict, total=False):
    fullRefund: RevocationContextFullRefund
    itemBasedRefund: RevocationContextItemBasedRefund
    proratedRefund: RevocationContextProratedRefund

@typing.type_check_only
class RevocationContextFullRefund(typing.TypedDict, total=False): ...

@typing.type_check_only
class RevocationContextItemBasedRefund(typing.TypedDict, total=False):
    productId: str

@typing.type_check_only
class RevocationContextProratedRefund(typing.TypedDict, total=False): ...

@typing.type_check_only
class RevokeSubscriptionPurchaseRequest(typing.TypedDict, total=False):
    revocationContext: RevocationContext

@typing.type_check_only
class RevokeSubscriptionPurchaseResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SafetyLabelsUpdateRequest(typing.TypedDict, total=False):
    safetyLabels: str

@typing.type_check_only
class SafetyLabelsUpdateResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ScreenDensity(typing.TypedDict, total=False):
    densityAlias: typing.Literal[
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
class ScreenDensityTargeting(typing.TypedDict, total=False):
    alternatives: _list[ScreenDensity]
    value: _list[ScreenDensity]

@typing.type_check_only
class ScreenshotSet(typing.TypedDict, total=False):
    screenshots: _list[ImageAsset]

@typing.type_check_only
class SdkVersion(typing.TypedDict, total=False):
    min: int

@typing.type_check_only
class SdkVersionTargeting(typing.TypedDict, total=False):
    alternatives: _list[SdkVersion]
    value: _list[SdkVersion]

@typing.type_check_only
class SignupPromotion(typing.TypedDict, total=False):
    oneTimeCode: OneTimeCode
    vanityCode: VanityCode

@typing.type_check_only
class SocSelector(typing.TypedDict, total=False):
    socMake: str
    socModel: str

@typing.type_check_only
class SplitApkMetadata(typing.TypedDict, total=False):
    isMasterSplit: bool
    splitId: str

@typing.type_check_only
class SplitApkVariant(typing.TypedDict, total=False):
    apkSet: _list[ApkSet]
    targeting: VariantTargeting
    variantNumber: int

@typing.type_check_only
class StandaloneApkMetadata(typing.TypedDict, total=False):
    fusedModuleName: _list[str]

@typing.type_check_only
class SubscribeWithGoogleInfo(typing.TypedDict, total=False):
    emailAddress: str
    familyName: str
    givenName: str
    profileId: str
    profileName: str

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    archived: bool
    basePlans: _list[BasePlan]
    listings: _list[SubscriptionListing]
    packageName: str
    productId: str
    restrictedPaymentCountries: RestrictedPaymentCountries
    taxAndComplianceSettings: SubscriptionTaxAndComplianceSettings

@typing.type_check_only
class SubscriptionDeferralInfo(typing.TypedDict, total=False):
    desiredExpiryTimeMillis: str
    expectedExpiryTimeMillis: str

@typing.type_check_only
class SubscriptionDetails(typing.TypedDict, total=False):
    basePlanId: str
    offerId: str
    offerPhase: typing.Literal[
        "OFFER_PHASE_UNSPECIFIED", "BASE", "INTRODUCTORY", "FREE_TRIAL"
    ]
    offerPhaseDetails: OfferPhaseDetails
    servicePeriodEndTime: str
    servicePeriodStartTime: str

@typing.type_check_only
class SubscriptionItemPriceChangeDetails(typing.TypedDict, total=False):
    expectedNewPriceChargeTime: str
    newPrice: Money
    priceChangeMode: typing.Literal[
        "PRICE_CHANGE_MODE_UNSPECIFIED",
        "PRICE_DECREASE",
        "PRICE_INCREASE",
        "OPT_OUT_PRICE_INCREASE",
    ]
    priceChangeState: typing.Literal[
        "PRICE_CHANGE_STATE_UNSPECIFIED",
        "OUTSTANDING",
        "CONFIRMED",
        "APPLIED",
        "CANCELED",
    ]

@typing.type_check_only
class SubscriptionListing(typing.TypedDict, total=False):
    benefits: _list[str]
    description: str
    languageCode: str
    title: str

@typing.type_check_only
class SubscriptionOffer(typing.TypedDict, total=False):
    basePlanId: str
    offerId: str
    offerTags: _list[OfferTag]
    otherRegionsConfig: OtherRegionsSubscriptionOfferConfig
    packageName: str
    phases: _list[SubscriptionOfferPhase]
    productId: str
    regionalConfigs: _list[RegionalSubscriptionOfferConfig]
    state: typing.Literal["STATE_UNSPECIFIED", "DRAFT", "ACTIVE", "INACTIVE"]
    targeting: SubscriptionOfferTargeting

@typing.type_check_only
class SubscriptionOfferPhase(typing.TypedDict, total=False):
    duration: str
    otherRegionsConfig: OtherRegionsSubscriptionOfferPhaseConfig
    recurrenceCount: int
    regionalConfigs: _list[RegionalSubscriptionOfferPhaseConfig]

@typing.type_check_only
class SubscriptionOfferTargeting(typing.TypedDict, total=False):
    acquisitionRule: AcquisitionTargetingRule
    upgradeRule: UpgradeTargetingRule

@typing.type_check_only
class SubscriptionPurchaseLineItem(typing.TypedDict, total=False):
    autoRenewingPlan: AutoRenewingPlan
    deferredItemRemoval: DeferredItemRemoval
    deferredItemReplacement: DeferredItemReplacement
    expiryTime: str
    itemReplacement: ItemReplacement
    latestSuccessfulOrderId: str
    offerDetails: OfferDetails
    offerPhase: OfferPhase
    prepaidPlan: PrepaidPlan
    productId: str
    signupPromotion: SignupPromotion

@typing.type_check_only
class SubscriptionPurchaseV2(typing.TypedDict, total=False):
    acknowledgementState: typing.Literal[
        "ACKNOWLEDGEMENT_STATE_UNSPECIFIED",
        "ACKNOWLEDGEMENT_STATE_PENDING",
        "ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED",
    ]
    canceledStateContext: CanceledStateContext
    etag: str
    externalAccountIdentifiers: ExternalAccountIdentifiers
    inGracePeriodStateContext: InGracePeriodStateContext
    kind: str
    lineItems: _list[SubscriptionPurchaseLineItem]
    linkedPurchaseToken: str
    onHoldStateContext: OnHoldStateContext
    outOfAppPurchaseContext: OutOfAppPurchaseContext
    pausedStateContext: PausedStateContext
    regionCode: str
    startTime: str
    subscribeWithGoogleInfo: SubscribeWithGoogleInfo
    subscriptionState: typing.Literal[
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
class SubscriptionPurchasesAcknowledgeRequest(typing.TypedDict, total=False):
    developerPayload: str
    externalAccountIds: ExternalAccountIds

@typing.type_check_only
class SubscriptionPurchasesDeferRequest(typing.TypedDict, total=False):
    deferralInfo: SubscriptionDeferralInfo

@typing.type_check_only
class SubscriptionPurchasesDeferResponse(typing.TypedDict, total=False):
    newExpiryTimeMillis: str

@typing.type_check_only
class SubscriptionTaxAndComplianceSettings(typing.TypedDict, total=False):
    eeaWithdrawalRightType: typing.Literal[
        "WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED",
        "WITHDRAWAL_RIGHT_DIGITAL_CONTENT",
        "WITHDRAWAL_RIGHT_SERVICE",
    ]
    isTokenizedDigitalAsset: bool
    productTaxCategoryCode: str
    regionalProductAgeRatingInfos: _list[RegionalProductAgeRatingInfo]
    taxRateInfoByRegionCode: dict[str, typing.Any]

@typing.type_check_only
class SystemApkOptions(typing.TypedDict, total=False):
    rotated: bool
    uncompressedDexFiles: bool
    uncompressedNativeLibraries: bool

@typing.type_check_only
class SystemApksListResponse(typing.TypedDict, total=False):
    variants: _list[Variant]

@typing.type_check_only
class SystemFeature(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class SystemInitiatedCancellation(typing.TypedDict, total=False): ...

@typing.type_check_only
class SystemOnChip(typing.TypedDict, total=False):
    manufacturer: str
    model: str

@typing.type_check_only
class Targeting(typing.TypedDict, total=False):
    allUsers: AllUsers
    androidSdks: AndroidSdks
    regions: Regions
    versionList: AppVersionList
    versionRange: AppVersionRange

@typing.type_check_only
class TargetingInfo(typing.TypedDict, total=False):
    assetSliceSet: _list[AssetSliceSet]
    packageName: str
    variant: _list[SplitApkVariant]

@typing.type_check_only
class TargetingRuleScope(typing.TypedDict, total=False):
    anySubscriptionInApp: TargetingRuleScopeAnySubscriptionInApp
    specificSubscriptionInApp: str
    thisSubscription: TargetingRuleScopeThisSubscription

@typing.type_check_only
class TargetingRuleScopeAnySubscriptionInApp(typing.TypedDict, total=False): ...

@typing.type_check_only
class TargetingRuleScopeThisSubscription(typing.TypedDict, total=False): ...

@typing.type_check_only
class TargetingUpdate(typing.TypedDict, total=False):
    allUsers: AllUsers
    androidSdks: AndroidSdks
    regions: Regions

@typing.type_check_only
class TestPurchase(typing.TypedDict, total=False): ...

@typing.type_check_only
class TestPurchaseContext(typing.TypedDict, total=False):
    fopType: typing.Literal["FOP_TYPE_UNSPECIFIED", "TEST"]

@typing.type_check_only
class Testers(typing.TypedDict, total=False):
    googleGroups: _list[str]

@typing.type_check_only
class TextureCompressionFormat(typing.TypedDict, total=False):
    alias: typing.Literal[
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
class TextureCompressionFormatTargeting(typing.TypedDict, total=False):
    alternatives: _list[TextureCompressionFormat]
    value: _list[TextureCompressionFormat]

@typing.type_check_only
class Timestamp(typing.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class TokenPagination(typing.TypedDict, total=False):
    nextPageToken: str
    previousPageToken: str

@typing.type_check_only
class Track(typing.TypedDict, total=False):
    releases: _list[TrackRelease]
    track: str

@typing.type_check_only
class TrackConfig(typing.TypedDict, total=False):
    formFactor: typing.Literal[
        "FORM_FACTOR_UNSPECIFIED", "DEFAULT", "WEAR", "AUTOMOTIVE"
    ]
    track: str
    type: typing.Literal["TRACK_TYPE_UNSPECIFIED", "CLOSED_TESTING"]

@typing.type_check_only
class TrackCountryAvailability(typing.TypedDict, total=False):
    countries: _list[TrackTargetedCountry]
    restOfWorld: bool
    syncWithProduction: bool

@typing.type_check_only
class TrackRelease(typing.TypedDict, total=False):
    countryTargeting: CountryTargeting
    inAppUpdatePriority: int
    name: str
    releaseNotes: _list[LocalizedText]
    status: typing.Literal[
        "statusUnspecified", "draft", "inProgress", "halted", "completed"
    ]
    userFraction: float
    versionCodes: _list[str]

@typing.type_check_only
class TrackTargetedCountry(typing.TypedDict, total=False):
    countryCode: str

@typing.type_check_only
class TracksListResponse(typing.TypedDict, total=False):
    kind: str
    tracks: _list[Track]

@typing.type_check_only
class UpdateAppStoreHostedAppPublishStatusRequest(typing.TypedDict, total=False):
    publishState: typing.Literal[
        "APP_STORE_APP_PUBLISH_STATE_UNSPECIFIED",
        "APP_STORE_APP_PUBLISH_STATE_PUBLISHED",
        "APP_STORE_APP_PUBLISH_STATE_UNPUBLISHED",
    ]

@typing.type_check_only
class UpdateAppStoreHostedAppPublishStatusResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateAppStoreHostedAppRequest(typing.TypedDict, total=False):
    activeApks: AppStoreAppActiveApks
    activeLocalizedStoreListings: _list[AppStoreAppStoreListing]
    appDetails: AppStoreAppDetails
    packageName: str
    policyDeclarations: _list[AppStoreAppPolicyDeclaration]

@typing.type_check_only
class UpdateAppStoreHostedAppResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateBasePlanStateRequest(typing.TypedDict, total=False):
    activateBasePlanRequest: ActivateBasePlanRequest
    deactivateBasePlanRequest: DeactivateBasePlanRequest

@typing.type_check_only
class UpdateOneTimeProductOfferRequest(typing.TypedDict, total=False):
    allowMissing: bool
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    oneTimeProductOffer: OneTimeProductOffer
    regionsVersion: RegionsVersion
    updateMask: str

@typing.type_check_only
class UpdateOneTimeProductOfferStateRequest(typing.TypedDict, total=False):
    activateOneTimeProductOfferRequest: ActivateOneTimeProductOfferRequest
    cancelOneTimeProductOfferRequest: CancelOneTimeProductOfferRequest
    deactivateOneTimeProductOfferRequest: DeactivateOneTimeProductOfferRequest

@typing.type_check_only
class UpdateOneTimeProductRequest(typing.TypedDict, total=False):
    allowMissing: bool
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    oneTimeProduct: OneTimeProduct
    regionsVersion: RegionsVersion
    updateMask: str

@typing.type_check_only
class UpdatePurchaseOptionStateRequest(typing.TypedDict, total=False):
    activatePurchaseOptionRequest: ActivatePurchaseOptionRequest
    deactivatePurchaseOptionRequest: DeactivatePurchaseOptionRequest

@typing.type_check_only
class UpdateSubscriptionOfferRequest(typing.TypedDict, total=False):
    allowMissing: bool
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    regionsVersion: RegionsVersion
    subscriptionOffer: SubscriptionOffer
    updateMask: str

@typing.type_check_only
class UpdateSubscriptionOfferStateRequest(typing.TypedDict, total=False):
    activateSubscriptionOfferRequest: ActivateSubscriptionOfferRequest
    deactivateSubscriptionOfferRequest: DeactivateSubscriptionOfferRequest

@typing.type_check_only
class UpdateSubscriptionRequest(typing.TypedDict, total=False):
    allowMissing: bool
    latencyTolerance: typing.Literal[
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
        "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
    ]
    regionsVersion: RegionsVersion
    subscription: Subscription
    updateMask: str

@typing.type_check_only
class UpgradeTargetingRule(typing.TypedDict, total=False):
    billingPeriodDuration: str
    oncePerUser: bool
    scope: TargetingRuleScope

@typing.type_check_only
class UploadApkRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadApkResponse(typing.TypedDict, total=False):
    apkId: str

@typing.type_check_only
class UploadAppStoreAppPolicyDeclarationFileRequest(typing.TypedDict, total=False):
    fileType: typing.Literal[
        "DECLARATION_FILE_TYPE_UNSPECIFIED", "DECLARATION_FILE_TYPE_DOCUMENT"
    ]

@typing.type_check_only
class UploadAppStoreAppPolicyDeclarationFileResponse(typing.TypedDict, total=False):
    fileId: str

@typing.type_check_only
class UploadImageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadImageResponse(typing.TypedDict, total=False):
    imageId: str

@typing.type_check_only
class User(typing.TypedDict, total=False):
    accessState: typing.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "INVITED",
        "INVITATION_EXPIRED",
        "ACCESS_GRANTED",
        "ACCESS_EXPIRED",
    ]
    developerAccountPermissions: _list[
        typing.Literal[
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
            "CAN_VIEW_CONNECTED_APPS_GLOBAL",
            "CAN_EDIT_CONNECTED_APPS_GLOBAL",
        ]
    ]
    email: str
    expirationTime: str
    grants: _list[Grant]
    name: str
    partial: bool

@typing.type_check_only
class UserComment(typing.TypedDict, total=False):
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
class UserCountriesTargeting(typing.TypedDict, total=False):
    countryCodes: _list[str]
    exclude: bool

@typing.type_check_only
class UserCountrySet(typing.TypedDict, total=False):
    countryCodes: _list[str]
    name: str

@typing.type_check_only
class UserInitiatedCancellation(typing.TypedDict, total=False):
    cancelSurveyResult: CancelSurveyResult
    cancelTime: str

@typing.type_check_only
class UsesConfiguration(typing.TypedDict, total=False):
    requiredKeyboardType: typing.Literal[
        "KEYBOARD_TYPE_UNSPECIFIED",
        "KEYBOARD_TYPE_UNDEFINED",
        "KEYBOARD_TYPE_NO_KEYS",
        "KEYBOARD_TYPE_QWERTY",
        "KEYBOARD_TYPE_TWELVE_KEY",
    ]
    requiredNavigationType: typing.Literal[
        "NAVIGATION_TYPE_UNSPECIFIED",
        "NAVIGATION_TYPE_UNDEFINED",
        "NAVIGATION_TYPE_NO_NAVIGATION",
        "NAVIGATION_TYPE_DPAD",
        "NAVIGATION_TYPE_TRACKBALL",
        "NAVIGATION_TYPE_WHEEL",
    ]
    requiredTouchscreenType: typing.Literal[
        "TOUCHSCREEN_TYPE_UNSPECIFIED",
        "TOUCHSCREEN_TYPE_UNDEFINED",
        "TOUCHSCREEN_TYPE_NO_TOUCHSCREEN",
        "TOUCHSCREEN_TYPE_STYLUS",
        "TOUCHSCREEN_TYPE_FINGER",
    ]
    requiresFiveWayNavigation: bool
    requiresHardwareKeyboard: bool

@typing.type_check_only
class UsesPermission(typing.TypedDict, total=False):
    maxSdkVersion: int
    name: str

@typing.type_check_only
class VanityCode(typing.TypedDict, total=False):
    promotionCode: str

@typing.type_check_only
class Variant(typing.TypedDict, total=False):
    deviceSpec: DeviceSpec
    options: SystemApkOptions
    variantId: int

@typing.type_check_only
class VariantTargeting(typing.TypedDict, total=False):
    abiTargeting: AbiTargeting
    multiAbiTargeting: MultiAbiTargeting
    screenDensityTargeting: ScreenDensityTargeting
    sdkVersionTargeting: SdkVersionTargeting
    textureCompressionFormatTargeting: TextureCompressionFormatTargeting

@typing.type_check_only
class VideoAsset(typing.TypedDict, total=False):
    videoUrl: str

@typing.type_check_only
class VoidedPurchase(typing.TypedDict, total=False):
    kind: str
    orderId: str
    purchaseTimeMillis: str
    purchaseToken: str
    voidedQuantity: int
    voidedReason: int
    voidedSource: int
    voidedTimeMillis: str

@typing.type_check_only
class VoidedPurchasesListResponse(typing.TypedDict, total=False):
    pageInfo: PageInfo
    tokenPagination: TokenPagination
    voidedPurchases: _list[VoidedPurchase]
