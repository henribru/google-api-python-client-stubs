import typing

import typing_extensions

class Comment(typing_extensions.TypedDict, total=False):
    userComment: UserComment
    developerComment: DeveloperComment

class Image(typing_extensions.TypedDict, total=False):
    sha256: str
    sha1: str
    id: str
    url: str

class AppDetails(typing_extensions.TypedDict, total=False):
    defaultLanguage: str
    contactWebsite: str
    contactPhone: str
    contactEmail: str

class AppEdit(typing_extensions.TypedDict, total=False):
    expiryTimeSeconds: str
    id: str

class ProductPurchase(typing_extensions.TypedDict, total=False):
    quantity: int
    orderId: str
    kind: str
    obfuscatedExternalProfileId: str
    purchaseTimeMillis: str
    purchaseToken: str
    developerPayload: str
    productId: str
    purchaseType: int
    obfuscatedExternalAccountId: str
    purchaseState: int
    acknowledgementState: int
    consumptionState: int
    regionCode: str

class ImagesListResponse(typing_extensions.TypedDict, total=False):
    images: typing.List[Image]

class ReviewsReplyRequest(typing_extensions.TypedDict, total=False):
    replyText: str

class Apk(typing_extensions.TypedDict, total=False):
    versionCode: int
    binary: ApkBinary

class LocalizedText(typing_extensions.TypedDict, total=False):
    text: str
    language: str

class UsesPermission(typing_extensions.TypedDict, total=False):
    name: str
    maxSdkVersion: int

class TracksListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    tracks: typing.List[Track]

class ReviewsListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    pageInfo: PageInfo
    reviews: typing.List[Review]

class InAppProductListing(typing_extensions.TypedDict, total=False):
    title: str
    benefits: typing.List[str]
    description: str

class ImagesDeleteAllResponse(typing_extensions.TypedDict, total=False):
    deleted: typing.List[Image]

class SubscriptionPurchase(typing_extensions.TypedDict, total=False):
    obfuscatedExternalProfileId: str
    linkedPurchaseToken: str
    cancelSurveyResult: SubscriptionCancelSurveyResult
    countryCode: str
    acknowledgementState: int
    paymentState: int
    cancelReason: int
    emailAddress: str
    priceChange: SubscriptionPriceChange
    startTimeMillis: str
    priceCurrencyCode: str
    profileId: str
    autoResumeTimeMillis: str
    expiryTimeMillis: str
    familyName: str
    obfuscatedExternalAccountId: str
    kind: str
    introductoryPriceInfo: IntroductoryPriceInfo
    developerPayload: str
    orderId: str
    givenName: str
    priceAmountMicros: str
    externalAccountId: str
    promotionCode: str
    purchaseType: int
    profileName: str
    promotionType: int
    autoRenewing: bool
    userCancellationTimeMillis: str

class TokenPagination(typing_extensions.TypedDict, total=False):
    previousPageToken: str
    nextPageToken: str

class InternalAppSharingArtifact(typing_extensions.TypedDict, total=False):
    certificateFingerprint: str
    downloadUrl: str
    sha256: str

class DeviceSpec(typing_extensions.TypedDict, total=False):
    supportedLocales: typing.List[str]
    supportedAbis: typing.List[str]
    screenDensity: int

class DeveloperComment(typing_extensions.TypedDict, total=False):
    text: str
    lastModified: Timestamp

class ApksAddExternallyHostedResponse(typing_extensions.TypedDict, total=False):
    externallyHostedApk: ExternallyHostedApk

class CountryTargeting(typing_extensions.TypedDict, total=False):
    includeRestOfWorld: bool
    countries: typing.List[str]

class Timestamp(typing_extensions.TypedDict, total=False):
    seconds: str
    nanos: int

class PageInfo(typing_extensions.TypedDict, total=False):
    startIndex: int
    totalResults: int
    resultPerPage: int

class Review(typing_extensions.TypedDict, total=False):
    reviewId: str
    comments: typing.List[Comment]
    authorName: str

class BundlesListResponse(typing_extensions.TypedDict, total=False):
    bundles: typing.List[Bundle]
    kind: str

class TrackRelease(typing_extensions.TypedDict, total=False):
    versionCodes: typing.List[str]
    name: str
    releaseNotes: typing.List[LocalizedText]
    inAppUpdatePriority: int
    countryTargeting: CountryTargeting
    status: typing_extensions.Literal[
        "statusUnspecified", "draft", "inProgress", "halted", "completed"
    ]
    userFraction: float

class ProductPurchasesAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    developerPayload: str

class Variant(typing_extensions.TypedDict, total=False):
    variantId: int
    deviceSpec: DeviceSpec

class SubscriptionPriceChange(typing_extensions.TypedDict, total=False):
    state: int
    newPrice: Price

class ReviewReplyResult(typing_extensions.TypedDict, total=False):
    lastEdited: Timestamp
    replyText: str

class ExternallyHostedApk(typing_extensions.TypedDict, total=False):
    fileSize: str
    minimumSdk: int
    maximumSdk: int
    fileSha1Base64: str
    fileSha256Base64: str
    nativeCodes: typing.List[str]
    versionName: str
    applicationLabel: str
    externallyHostedUrl: str
    usesFeatures: typing.List[str]
    packageName: str
    certificateBase64s: typing.List[str]
    versionCode: int
    usesPermissions: typing.List[UsesPermission]
    iconBase64: str

class InappproductsListResponse(typing_extensions.TypedDict, total=False):
    tokenPagination: TokenPagination
    pageInfo: PageInfo
    inappproduct: typing.List[InAppProduct]
    kind: str

class DeviceMetadata(typing_extensions.TypedDict, total=False):
    screenWidthPx: int
    deviceClass: str
    productName: str
    screenDensityDpi: int
    screenHeightPx: int
    manufacturer: str
    nativePlatform: str
    glEsVersion: int
    ramMb: int
    cpuModel: str
    cpuMake: str

class SubscriptionDeferralInfo(typing_extensions.TypedDict, total=False):
    expectedExpiryTimeMillis: str
    desiredExpiryTimeMillis: str

class ListingsListResponse(typing_extensions.TypedDict, total=False):
    listings: typing.List[Listing]
    kind: str

class ReviewsReplyResponse(typing_extensions.TypedDict, total=False):
    result: ReviewReplyResult

class Bundle(typing_extensions.TypedDict, total=False):
    sha1: str
    sha256: str
    versionCode: int

class Testers(typing_extensions.TypedDict, total=False):
    googleGroups: typing.List[str]

class ExpansionFilesUploadResponse(typing_extensions.TypedDict, total=False):
    expansionFile: ExpansionFile

class Track(typing_extensions.TypedDict, total=False):
    track: str
    releases: typing.List[TrackRelease]

class SubscriptionPurchasesAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    developerPayload: str

class VoidedPurchasesListResponse(typing_extensions.TypedDict, total=False):
    voidedPurchases: typing.List[VoidedPurchase]
    tokenPagination: TokenPagination
    pageInfo: PageInfo

class ExpansionFile(typing_extensions.TypedDict, total=False):
    referencesVersion: int
    fileSize: str

class SubscriptionPurchasesDeferRequest(typing_extensions.TypedDict, total=False):
    deferralInfo: SubscriptionDeferralInfo

class ImagesUploadResponse(typing_extensions.TypedDict, total=False):
    image: Image

class ApkBinary(typing_extensions.TypedDict, total=False):
    sha256: str
    sha1: str

class ApksListResponse(typing_extensions.TypedDict, total=False):
    apks: typing.List[Apk]
    kind: str

class Listing(typing_extensions.TypedDict, total=False):
    video: str
    shortDescription: str
    language: str
    fullDescription: str
    title: str

class SubscriptionPurchasesDeferResponse(typing_extensions.TypedDict, total=False):
    newExpiryTimeMillis: str

class UserComment(typing_extensions.TypedDict, total=False):
    text: str
    androidOsVersion: int
    deviceMetadata: DeviceMetadata
    originalText: str
    starRating: int
    thumbsDownCount: int
    reviewerLanguage: str
    device: str
    appVersionName: str
    thumbsUpCount: int
    appVersionCode: int
    lastModified: Timestamp

class SubscriptionCancelSurveyResult(typing_extensions.TypedDict, total=False):
    cancelSurveyReason: int
    userInputCancelReason: str

class InAppProduct(typing_extensions.TypedDict, total=False):
    defaultPrice: Price
    purchaseType: typing_extensions.Literal[
        "purchaseTypeUnspecified", "managedUser", "subscription"
    ]
    status: typing_extensions.Literal["statusUnspecified", "active", "inactive"]
    prices: typing.Dict[str, typing.Any]
    packageName: str
    subscriptionPeriod: str
    defaultLanguage: str
    gracePeriod: str
    listings: typing.Dict[str, typing.Any]
    trialPeriod: str
    sku: str

class IntroductoryPriceInfo(typing_extensions.TypedDict, total=False):
    introductoryPricePeriod: str
    introductoryPriceCurrencyCode: str
    introductoryPriceAmountMicros: str
    introductoryPriceCycles: int

class ApksAddExternallyHostedRequest(typing_extensions.TypedDict, total=False):
    externallyHostedApk: ExternallyHostedApk

class SystemApksListResponse(typing_extensions.TypedDict, total=False):
    variants: typing.List[Variant]

class Price(typing_extensions.TypedDict, total=False):
    currency: str
    priceMicros: str

class DeobfuscationFilesUploadResponse(typing_extensions.TypedDict, total=False):
    deobfuscationFile: DeobfuscationFile

class DeobfuscationFile(typing_extensions.TypedDict, total=False):
    symbolType: typing_extensions.Literal[
        "deobfuscationFileTypeUnspecified", "proguard", "nativeCode"
    ]

class VoidedPurchase(typing_extensions.TypedDict, total=False):
    orderId: str
    purchaseTimeMillis: str
    voidedSource: int
    voidedReason: int
    voidedTimeMillis: str
    purchaseToken: str
    kind: str
