import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountManagement: str
    adsLinks: _list[AccountAdsLink]
    adultContent: bool
    automaticImprovements: AccountAutomaticImprovements
    automaticLabelIds: _list[str]
    businessIdentity: AccountBusinessIdentity
    businessInformation: AccountBusinessInformation
    conversionSettings: AccountConversionSettings
    cssId: str
    googleMyBusinessLink: AccountGoogleMyBusinessLink
    id: str
    kind: str
    labelIds: _list[str]
    name: str
    sellerId: str
    users: _list[AccountUser]
    websiteUrl: str
    youtubeChannelLinks: _list[AccountYouTubeChannelLink]

@typing.type_check_only
class AccountAddress(typing_extensions.TypedDict, total=False):
    country: str
    locality: str
    postalCode: str
    region: str
    streetAddress: str

@typing.type_check_only
class AccountAdsLink(typing_extensions.TypedDict, total=False):
    adsId: str
    status: str

@typing.type_check_only
class AccountAutomaticImprovements(typing_extensions.TypedDict, total=False):
    imageImprovements: AccountImageImprovements
    itemUpdates: AccountItemUpdates
    shippingImprovements: AccountShippingImprovements

@typing.type_check_only
class AccountBusinessIdentity(typing_extensions.TypedDict, total=False):
    blackOwned: AccountIdentityType
    includeForPromotions: bool
    latinoOwned: AccountIdentityType
    smallBusiness: AccountIdentityType
    veteranOwned: AccountIdentityType
    womenOwned: AccountIdentityType

@typing.type_check_only
class AccountBusinessInformation(typing_extensions.TypedDict, total=False):
    address: AccountAddress
    customerService: AccountCustomerService
    koreanBusinessRegistrationNumber: str
    phoneNumber: str
    phoneVerificationStatus: str

@typing.type_check_only
class AccountConversionSettings(typing_extensions.TypedDict, total=False):
    freeListingsAutoTaggingEnabled: bool

@typing.type_check_only
class AccountCredentials(typing_extensions.TypedDict, total=False):
    accessToken: str
    expiresIn: str
    purpose: typing_extensions.Literal[
        "ACCOUNT_CREDENTIALS_PURPOSE_UNSPECIFIED",
        "SHOPIFY_ORDER_MANAGEMENT",
        "SHOPIFY_INTEGRATION",
    ]

@typing.type_check_only
class AccountCustomerService(typing_extensions.TypedDict, total=False):
    email: str
    phoneNumber: str
    url: str

@typing.type_check_only
class AccountGoogleMyBusinessLink(typing_extensions.TypedDict, total=False):
    gmbAccountId: str
    gmbEmail: str
    status: str

@typing.type_check_only
class AccountIdentifier(typing_extensions.TypedDict, total=False):
    aggregatorId: str
    merchantId: str

@typing.type_check_only
class AccountIdentityType(typing_extensions.TypedDict, total=False):
    selfIdentified: bool

@typing.type_check_only
class AccountImageImprovements(typing_extensions.TypedDict, total=False):
    accountImageImprovementsSettings: AccountImageImprovementsSettings
    effectiveAllowAutomaticImageImprovements: bool

@typing.type_check_only
class AccountImageImprovementsSettings(typing_extensions.TypedDict, total=False):
    allowAutomaticImageImprovements: bool

@typing.type_check_only
class AccountIssue(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    impact: AccountIssueImpact
    prerenderedContent: str
    title: str

@typing.type_check_only
class AccountIssueImpact(typing_extensions.TypedDict, total=False):
    breakdowns: _list[Breakdown]
    message: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class AccountItemUpdates(typing_extensions.TypedDict, total=False):
    accountItemUpdatesSettings: AccountItemUpdatesSettings
    effectiveAllowAvailabilityUpdates: bool
    effectiveAllowConditionUpdates: bool
    effectiveAllowPriceUpdates: bool
    effectiveAllowStrictAvailabilityUpdates: bool

@typing.type_check_only
class AccountItemUpdatesSettings(typing_extensions.TypedDict, total=False):
    allowAvailabilityUpdates: bool
    allowConditionUpdates: bool
    allowPriceUpdates: bool
    allowStrictAvailabilityUpdates: bool

@typing.type_check_only
class AccountLabel(typing_extensions.TypedDict, total=False):
    accountId: str
    description: str
    labelId: str
    labelType: typing_extensions.Literal[
        "LABEL_TYPE_UNSPECIFIED", "MANUAL", "AUTOMATIC"
    ]
    name: str

@typing.type_check_only
class AccountReturnCarrier(typing_extensions.TypedDict, total=False):
    carrierAccountId: str
    carrierAccountName: str
    carrierAccountNumber: str
    carrierCode: typing_extensions.Literal["CARRIER_CODE_UNSPECIFIED", "FEDEX", "UPS"]

@typing.type_check_only
class AccountShippingImprovements(typing_extensions.TypedDict, total=False):
    allowShippingImprovements: bool

@typing.type_check_only
class AccountStatus(typing_extensions.TypedDict, total=False):
    accountId: str
    accountLevelIssues: _list[AccountStatusAccountLevelIssue]
    accountManagement: str
    kind: str
    products: _list[AccountStatusProducts]
    websiteClaimed: bool

@typing.type_check_only
class AccountStatusAccountLevelIssue(typing_extensions.TypedDict, total=False):
    country: str
    destination: str
    detail: str
    documentation: str
    id: str
    severity: str
    title: str

@typing.type_check_only
class AccountStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    attributeName: str
    code: str
    description: str
    detail: str
    documentation: str
    numItems: str
    resolution: str
    servability: str

@typing.type_check_only
class AccountStatusProducts(typing_extensions.TypedDict, total=False):
    channel: str
    country: str
    destination: str
    itemLevelIssues: _list[AccountStatusItemLevelIssue]
    statistics: AccountStatusStatistics

@typing.type_check_only
class AccountStatusStatistics(typing_extensions.TypedDict, total=False):
    active: str
    disapproved: str
    expiring: str
    pending: str

@typing.type_check_only
class AccountTax(typing_extensions.TypedDict, total=False):
    accountId: str
    kind: str
    rules: _list[AccountTaxTaxRule]

@typing.type_check_only
class AccountTaxTaxRule(typing_extensions.TypedDict, total=False):
    country: str
    locationId: str
    ratePercent: str
    shippingTaxed: bool
    useGlobalRate: bool

@typing.type_check_only
class AccountUser(typing_extensions.TypedDict, total=False):
    admin: bool
    emailAddress: str
    orderManager: bool
    paymentsAnalyst: bool
    paymentsManager: bool
    reportingManager: bool

@typing.type_check_only
class AccountYouTubeChannelLink(typing_extensions.TypedDict, total=False):
    channelId: str
    status: str

@typing.type_check_only
class AccountsAuthInfoResponse(typing_extensions.TypedDict, total=False):
    accountIdentifiers: _list[AccountIdentifier]
    kind: str

@typing.type_check_only
class AccountsClaimWebsiteResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[AccountsCustomBatchRequestEntry]

@typing.type_check_only
class AccountsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    account: Account
    accountId: str
    batchId: int
    force: bool
    labelIds: _list[str]
    linkRequest: AccountsCustomBatchRequestEntryLinkRequest
    merchantId: str
    method: str
    overwrite: bool
    view: str

@typing.type_check_only
class AccountsCustomBatchRequestEntryLinkRequest(
    typing_extensions.TypedDict, total=False
):
    action: str
    linkType: str
    linkedAccountId: str
    services: _list[str]

@typing.type_check_only
class AccountsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[AccountsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class AccountsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    account: Account
    batchId: int
    errors: Errors
    kind: str

@typing.type_check_only
class AccountsLinkRequest(typing_extensions.TypedDict, total=False):
    action: str
    eCommercePlatformLinkInfo: ECommercePlatformLinkInfo
    linkType: str
    linkedAccountId: str
    paymentServiceProviderLinkInfo: PaymentServiceProviderLinkInfo
    services: _list[str]

@typing.type_check_only
class AccountsLinkResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountsListLinksResponse(typing_extensions.TypedDict, total=False):
    kind: str
    links: _list[LinkedAccount]
    nextPageToken: str

@typing.type_check_only
class AccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[Account]

@typing.type_check_only
class AccountsUpdateLabelsRequest(typing_extensions.TypedDict, total=False):
    labelIds: _list[str]

@typing.type_check_only
class AccountsUpdateLabelsResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[AccountstatusesCustomBatchRequestEntry]

@typing.type_check_only
class AccountstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    destinations: _list[str]
    merchantId: str
    method: str

@typing.type_check_only
class AccountstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[AccountstatusesCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class AccountstatusesCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    accountStatus: AccountStatus
    batchId: int
    errors: Errors

@typing.type_check_only
class AccountstatusesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[AccountStatus]

@typing.type_check_only
class AccounttaxCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[AccounttaxCustomBatchRequestEntry]

@typing.type_check_only
class AccounttaxCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    accountTax: AccountTax
    batchId: int
    merchantId: str
    method: str

@typing.type_check_only
class AccounttaxCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[AccounttaxCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class AccounttaxCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    accountTax: AccountTax
    batchId: int
    errors: Errors
    kind: str

@typing.type_check_only
class AccounttaxListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[AccountTax]

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    builtinSimpleAction: BuiltInSimpleAction
    builtinUserInputAction: BuiltInUserInputAction
    buttonLabel: str
    externalAction: ExternalAction
    isAvailable: bool
    reasons: _list[ActionReason]

@typing.type_check_only
class ActionFlow(typing_extensions.TypedDict, total=False):
    dialogButtonLabel: str
    dialogCallout: Callout
    dialogMessage: TextWithTooltip
    dialogTitle: str
    id: str
    inputs: _list[InputField]
    label: str

@typing.type_check_only
class ActionInput(typing_extensions.TypedDict, total=False):
    actionFlowId: str
    inputValues: _list[InputValue]

@typing.type_check_only
class ActionReason(typing_extensions.TypedDict, total=False):
    action: Action
    detail: str
    message: str

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    administrativeArea: str
    city: str
    country: str
    postalCode: str
    streetAddress: str

@typing.type_check_only
class AlternateDisputeResolution(typing_extensions.TypedDict, total=False):
    label: str
    uri: str

@typing.type_check_only
class AttributionSettings(typing_extensions.TypedDict, total=False):
    attributionLookbackWindowInDays: int
    attributionModel: typing_extensions.Literal[
        "ATTRIBUTION_MODEL_UNSPECIFIED",
        "CROSS_CHANNEL_LAST_CLICK",
        "ADS_PREFERRED_LAST_CLICK",
        "CROSS_CHANNEL_DATA_DRIVEN",
        "CROSS_CHANNEL_FIRST_CLICK",
        "CROSS_CHANNEL_LINEAR",
        "CROSS_CHANNEL_POSITION_BASED",
        "CROSS_CHANNEL_TIME_DECAY",
    ]
    conversionType: _list[AttributionSettingsConversionType]

@typing.type_check_only
class AttributionSettingsConversionType(typing_extensions.TypedDict, total=False):
    includeInReporting: bool
    name: str

@typing.type_check_only
class BestSellers(typing_extensions.TypedDict, total=False):
    categoryId: str
    countryCode: str
    previousRank: str
    previousRelativeDemand: typing_extensions.Literal[
        "RELATIVE_DEMAND_UNSPECIFIED", "VERY_LOW", "LOW", "MEDIUM", "HIGH", "VERY_HIGH"
    ]
    rank: str
    relativeDemand: typing_extensions.Literal[
        "RELATIVE_DEMAND_UNSPECIFIED", "VERY_LOW", "LOW", "MEDIUM", "HIGH", "VERY_HIGH"
    ]
    relativeDemandChange: typing_extensions.Literal[
        "RELATIVE_DEMAND_CHANGE_TYPE_UNSPECIFIED", "SINKER", "FLAT", "RISER"
    ]
    reportDate: Date
    reportGranularity: typing_extensions.Literal[
        "REPORT_GRANULARITY_UNSPECIFIED", "WEEKLY", "MONTHLY"
    ]

@typing.type_check_only
class Brand(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Breakdown(typing_extensions.TypedDict, total=False):
    details: _list[str]
    regions: _list[BreakdownRegion]

@typing.type_check_only
class BreakdownRegion(typing_extensions.TypedDict, total=False):
    code: str
    name: str

@typing.type_check_only
class BuiltInSimpleAction(typing_extensions.TypedDict, total=False):
    additionalContent: BuiltInSimpleActionAdditionalContent
    attributeCode: str
    type: typing_extensions.Literal[
        "BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED",
        "VERIFY_PHONE",
        "CLAIM_WEBSITE",
        "ADD_PRODUCTS",
        "ADD_CONTACT_INFO",
        "LINK_ADS_ACCOUNT",
        "ADD_BUSINESS_REGISTRATION_NUMBER",
        "EDIT_ITEM_ATTRIBUTE",
        "FIX_ACCOUNT_ISSUE",
        "SHOW_ADDITIONAL_CONTENT",
    ]

@typing.type_check_only
class BuiltInSimpleActionAdditionalContent(typing_extensions.TypedDict, total=False):
    paragraphs: _list[str]
    title: str

@typing.type_check_only
class BuiltInUserInputAction(typing_extensions.TypedDict, total=False):
    actionContext: str
    flows: _list[ActionFlow]

@typing.type_check_only
class BusinessDayConfig(typing_extensions.TypedDict, total=False):
    businessDays: _list[str]

@typing.type_check_only
class Callout(typing_extensions.TypedDict, total=False):
    fullMessage: TextWithTooltip
    styleHint: typing_extensions.Literal[
        "CALLOUT_STYLE_HINT_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class CarrierRate(typing_extensions.TypedDict, total=False):
    carrierName: str
    carrierService: str
    flatAdjustment: Price
    name: str
    originPostalCode: str
    percentageAdjustment: str

@typing.type_check_only
class CarriersCarrier(typing_extensions.TypedDict, total=False):
    country: str
    eddServices: _list[str]
    name: str
    services: _list[str]

@typing.type_check_only
class CheckoutSettings(typing_extensions.TypedDict, total=False):
    effectiveEnrollmentState: typing_extensions.Literal[
        "CHECKOUT_ON_MERCHANT_ENROLLMENT_STATE_UNSPECIFIED",
        "INACTIVE",
        "ENROLLED",
        "OPT_OUT",
    ]
    effectiveReviewState: typing_extensions.Literal[
        "CHECKOUT_ON_MERCHANT_REVIEW_STATE_UNSPECIFIED",
        "IN_REVIEW",
        "APPROVED",
        "DISAPPROVED",
    ]
    effectiveUriSettings: UrlSettings
    enrollmentState: typing_extensions.Literal[
        "CHECKOUT_ON_MERCHANT_ENROLLMENT_STATE_UNSPECIFIED",
        "INACTIVE",
        "ENROLLED",
        "OPT_OUT",
    ]
    merchantId: str
    reviewState: typing_extensions.Literal[
        "CHECKOUT_ON_MERCHANT_REVIEW_STATE_UNSPECIFIED",
        "IN_REVIEW",
        "APPROVED",
        "DISAPPROVED",
    ]
    uriSettings: UrlSettings

@typing.type_check_only
class CloudExportAdditionalProperties(typing_extensions.TypedDict, total=False):
    boolValue: bool
    floatValue: _list[float]
    intValue: _list[str]
    maxValue: float
    minValue: float
    propertyName: str
    textValue: _list[str]
    unitCode: str

@typing.type_check_only
class Collection(typing_extensions.TypedDict, total=False):
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    featuredProduct: _list[CollectionFeaturedProduct]
    headline: _list[str]
    id: str
    imageLink: _list[str]
    language: str
    link: str
    mobileLink: str
    productCountry: str

@typing.type_check_only
class CollectionFeaturedProduct(typing_extensions.TypedDict, total=False):
    offerId: str
    x: float
    y: float

@typing.type_check_only
class CollectionStatus(typing_extensions.TypedDict, total=False):
    collectionLevelIssuses: _list[CollectionStatusItemLevelIssue]
    creationDate: str
    destinationStatuses: _list[CollectionStatusDestinationStatus]
    id: str
    lastUpdateDate: str

@typing.type_check_only
class CollectionStatusDestinationStatus(typing_extensions.TypedDict, total=False):
    approvedCountries: _list[str]
    destination: str
    disapprovedCountries: _list[str]
    pendingCountries: _list[str]
    status: str

@typing.type_check_only
class CollectionStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    applicableCountries: _list[str]
    attributeName: str
    code: str
    description: str
    destination: str
    detail: str
    documentation: str
    resolution: str
    servability: str

@typing.type_check_only
class CompetitiveVisibility(typing_extensions.TypedDict, total=False):
    adsOrganicRatio: float
    categoryBenchmarkVisibilityTrend: float
    categoryId: str
    countryCode: str
    date: Date
    domain: str
    higherPositionRate: float
    isYourDomain: bool
    pageOverlapRate: float
    rank: str
    relativeVisibility: float
    trafficSource: typing_extensions.Literal["UNKNOWN", "ORGANIC", "ADS", "ALL"]
    yourDomainVisibilityTrend: float

@typing.type_check_only
class ConversionSource(typing_extensions.TypedDict, total=False):
    conversionSourceId: str
    expireTime: str
    googleAnalyticsLink: GoogleAnalyticsLink
    merchantCenterDestination: MerchantCenterDestination
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED", "PENDING"
    ]

@typing.type_check_only
class Css(typing_extensions.TypedDict, total=False):
    cssDomainId: str
    cssGroupId: str
    displayName: str
    fullName: str
    homepageUri: str
    labelIds: _list[str]

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class CutoffTime(typing_extensions.TypedDict, total=False):
    hour: int
    minute: int
    timezone: str

@typing.type_check_only
class Datafeed(typing_extensions.TypedDict, total=False):
    attributeLanguage: str
    contentType: str
    fetchSchedule: DatafeedFetchSchedule
    fileName: str
    format: DatafeedFormat
    id: str
    kind: str
    name: str
    targets: _list[DatafeedTarget]

@typing.type_check_only
class DatafeedFetchSchedule(typing_extensions.TypedDict, total=False):
    dayOfMonth: int
    fetchUrl: str
    hour: int
    minuteOfHour: int
    password: str
    paused: bool
    timeZone: str
    username: str
    weekday: str

@typing.type_check_only
class DatafeedFormat(typing_extensions.TypedDict, total=False):
    columnDelimiter: str
    fileEncoding: str
    quotingMode: str

@typing.type_check_only
class DatafeedStatus(typing_extensions.TypedDict, total=False):
    country: str
    datafeedId: str
    errors: _list[DatafeedStatusError]
    feedLabel: str
    itemsTotal: str
    itemsValid: str
    kind: str
    language: str
    lastUploadDate: str
    processingStatus: str
    warnings: _list[DatafeedStatusError]

@typing.type_check_only
class DatafeedStatusError(typing_extensions.TypedDict, total=False):
    code: str
    count: str
    examples: _list[DatafeedStatusExample]
    message: str

@typing.type_check_only
class DatafeedStatusExample(typing_extensions.TypedDict, total=False):
    itemId: str
    lineNumber: str
    value: str

@typing.type_check_only
class DatafeedTarget(typing_extensions.TypedDict, total=False):
    country: str
    excludedDestinations: _list[str]
    feedLabel: str
    includedDestinations: _list[str]
    language: str
    targetCountries: _list[str]

@typing.type_check_only
class DatafeedsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[DatafeedsCustomBatchRequestEntry]

@typing.type_check_only
class DatafeedsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    datafeed: Datafeed
    datafeedId: str
    merchantId: str
    method: str

@typing.type_check_only
class DatafeedsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[DatafeedsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class DatafeedsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    datafeed: Datafeed
    errors: Errors

@typing.type_check_only
class DatafeedsFetchNowResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class DatafeedsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[Datafeed]

@typing.type_check_only
class DatafeedstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[DatafeedstatusesCustomBatchRequestEntry]

@typing.type_check_only
class DatafeedstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    country: str
    datafeedId: str
    feedLabel: str
    language: str
    merchantId: str
    method: str

@typing.type_check_only
class DatafeedstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[DatafeedstatusesCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class DatafeedstatusesCustomBatchResponseEntry(
    typing_extensions.TypedDict, total=False
):
    batchId: int
    datafeedStatus: DatafeedStatus
    errors: Errors

@typing.type_check_only
class DatafeedstatusesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[DatafeedStatus]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateTime(typing_extensions.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: TimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class DeliveryArea(typing_extensions.TypedDict, total=False):
    countryCode: str
    postalCodeRange: DeliveryAreaPostalCodeRange
    regionCode: str

@typing.type_check_only
class DeliveryAreaPostalCodeRange(typing_extensions.TypedDict, total=False):
    firstPostalCode: str
    lastPostalCode: str

@typing.type_check_only
class DeliveryTime(typing_extensions.TypedDict, total=False):
    cutoffTime: CutoffTime
    handlingBusinessDayConfig: BusinessDayConfig
    holidayCutoffs: _list[HolidayCutoff]
    maxHandlingTimeInDays: int
    maxTransitTimeInDays: int
    minHandlingTimeInDays: int
    minTransitTimeInDays: int
    transitBusinessDayConfig: BusinessDayConfig
    transitTimeTable: TransitTable
    warehouseBasedDeliveryTimes: _list[WarehouseBasedDeliveryTime]

@typing.type_check_only
class Distance(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class ECommercePlatformLinkInfo(typing_extensions.TypedDict, total=False):
    externalAccountId: str

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    domain: str
    message: str
    reason: str

@typing.type_check_only
class Errors(typing_extensions.TypedDict, total=False):
    code: int
    errors: _list[Error]
    message: str

@typing.type_check_only
class ExternalAction(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "EXTERNAL_ACTION_TYPE_UNSPECIFIED",
        "REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER",
        "REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER",
        "LEGAL_APPEAL_IN_HELP_CENTER",
        "VERIFY_IDENTITY_IN_MERCHANT_CENTER",
    ]
    uri: str

@typing.type_check_only
class FreeListingsProgramStatus(typing_extensions.TypedDict, total=False):
    globalState: typing_extensions.Literal[
        "PROGRAM_STATE_UNSPECIFIED", "NOT_ENABLED", "NO_OFFERS_UPLOADED", "ENABLED"
    ]
    regionStatuses: _list[FreeListingsProgramStatusRegionStatus]

@typing.type_check_only
class FreeListingsProgramStatusRegionStatus(typing_extensions.TypedDict, total=False):
    disapprovalDate: str
    eligibilityStatus: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "APPROVED",
        "DISAPPROVED",
        "WARNING",
        "UNDER_REVIEW",
        "PENDING_REVIEW",
        "ONBOARDING",
    ]
    onboardingIssues: _list[str]
    regionCodes: _list[str]
    reviewEligibilityStatus: typing_extensions.Literal[
        "REVIEW_ELIGIBILITY_UNSPECIFIED", "ELIGIBLE", "INELIGIBLE"
    ]
    reviewIneligibilityReason: typing_extensions.Literal[
        "REVIEW_INELIGIBILITY_REASON_UNSPECIFIED",
        "ONBOARDING_ISSUES",
        "NOT_ENOUGH_OFFERS",
        "IN_COOLDOWN_PERIOD",
        "ALREADY_UNDER_REVIEW",
        "NO_REVIEW_REQUIRED",
        "WILL_BE_REVIEWED_AUTOMATICALLY",
        "IS_RETIRED",
        "ALREADY_REVIEWED",
    ]
    reviewIneligibilityReasonDescription: str
    reviewIneligibilityReasonDetails: (
        FreeListingsProgramStatusReviewIneligibilityReasonDetails
    )
    reviewIssues: _list[str]

@typing.type_check_only
class FreeListingsProgramStatusReviewIneligibilityReasonDetails(
    typing_extensions.TypedDict, total=False
):
    cooldownTime: str

@typing.type_check_only
class FreeShippingThreshold(typing_extensions.TypedDict, total=False):
    country: str
    priceThreshold: Price

@typing.type_check_only
class GenerateRecommendationsResponse(typing_extensions.TypedDict, total=False):
    recommendations: _list[Recommendation]
    responseToken: str

@typing.type_check_only
class GmbAccounts(typing_extensions.TypedDict, total=False):
    accountId: str
    gmbAccounts: _list[GmbAccountsGmbAccount]

@typing.type_check_only
class GmbAccountsGmbAccount(typing_extensions.TypedDict, total=False):
    email: str
    listingCount: str
    name: str
    type: str

@typing.type_check_only
class GoogleAnalyticsLink(typing_extensions.TypedDict, total=False):
    attributionSettings: AttributionSettings
    propertyId: str
    propertyName: str

@typing.type_check_only
class Headers(typing_extensions.TypedDict, total=False):
    locations: _list[LocationIdSet]
    numberOfItems: _list[str]
    postalCodeGroupNames: _list[str]
    prices: _list[Price]
    weights: _list[Weight]

@typing.type_check_only
class HolidayCutoff(typing_extensions.TypedDict, total=False):
    deadlineDate: str
    deadlineHour: int
    deadlineTimezone: str
    holidayId: str
    visibleFromDate: str

@typing.type_check_only
class HolidaysHoliday(typing_extensions.TypedDict, total=False):
    countryCode: str
    date: str
    deliveryGuaranteeDate: str
    deliveryGuaranteeHour: str
    id: str
    type: str

@typing.type_check_only
class InputField(typing_extensions.TypedDict, total=False):
    checkboxInput: InputFieldCheckboxInput
    choiceInput: InputFieldChoiceInput
    id: str
    label: TextWithTooltip
    required: bool
    textInput: InputFieldTextInput

@typing.type_check_only
class InputFieldCheckboxInput(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InputFieldChoiceInput(typing_extensions.TypedDict, total=False):
    options: _list[InputFieldChoiceInputChoiceInputOption]

@typing.type_check_only
class InputFieldChoiceInputChoiceInputOption(typing_extensions.TypedDict, total=False):
    additionalInput: InputField
    id: str
    label: TextWithTooltip

@typing.type_check_only
class InputFieldTextInput(typing_extensions.TypedDict, total=False):
    additionalInfo: TextWithTooltip
    ariaLabel: str
    formatInfo: str
    type: typing_extensions.Literal[
        "TEXT_INPUT_TYPE_UNSPECIFIED", "GENERIC_SHORT_TEXT", "GENERIC_LONG_TEXT"
    ]

@typing.type_check_only
class InputValue(typing_extensions.TypedDict, total=False):
    checkboxInputValue: InputValueCheckboxInputValue
    choiceInputValue: InputValueChoiceInputValue
    inputFieldId: str
    textInputValue: InputValueTextInputValue

@typing.type_check_only
class InputValueCheckboxInputValue(typing_extensions.TypedDict, total=False):
    value: bool

@typing.type_check_only
class InputValueChoiceInputValue(typing_extensions.TypedDict, total=False):
    choiceInputOptionId: str

@typing.type_check_only
class InputValueTextInputValue(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class InsertCheckoutSettingsRequest(typing_extensions.TypedDict, total=False):
    uriSettings: UrlSettings

@typing.type_check_only
class Installment(typing_extensions.TypedDict, total=False):
    amount: Price
    creditType: str
    downpayment: Price
    months: str

@typing.type_check_only
class LabelIds(typing_extensions.TypedDict, total=False):
    labelIds: _list[str]

@typing.type_check_only
class LiaAboutPageSettings(typing_extensions.TypedDict, total=False):
    status: str
    url: str

@typing.type_check_only
class LiaCountrySettings(typing_extensions.TypedDict, total=False):
    about: LiaAboutPageSettings
    country: str
    hostedLocalStorefrontActive: bool
    inventory: LiaInventorySettings
    omnichannelExperience: LiaOmnichannelExperience
    onDisplayToOrder: LiaOnDisplayToOrderSettings
    posDataProvider: LiaPosDataProvider
    storePickupActive: bool

@typing.type_check_only
class LiaInventorySettings(typing_extensions.TypedDict, total=False):
    inventoryVerificationContactEmail: str
    inventoryVerificationContactName: str
    inventoryVerificationContactStatus: str
    status: str

@typing.type_check_only
class LiaOmnichannelExperience(typing_extensions.TypedDict, total=False):
    country: str
    lsfType: str
    pickupTypes: _list[str]

@typing.type_check_only
class LiaOnDisplayToOrderSettings(typing_extensions.TypedDict, total=False):
    shippingCostPolicyUrl: str
    status: str

@typing.type_check_only
class LiaPosDataProvider(typing_extensions.TypedDict, total=False):
    posDataProviderId: str
    posExternalAccountId: str

@typing.type_check_only
class LiaSettings(typing_extensions.TypedDict, total=False):
    accountId: str
    countrySettings: _list[LiaCountrySettings]
    kind: str

@typing.type_check_only
class LiasettingsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[LiasettingsCustomBatchRequestEntry]

@typing.type_check_only
class LiasettingsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    contactEmail: str
    contactName: str
    country: str
    gmbEmail: str
    liaSettings: LiaSettings
    merchantId: str
    method: str
    omnichannelExperience: LiaOmnichannelExperience
    posDataProviderId: str
    posExternalAccountId: str

@typing.type_check_only
class LiasettingsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[LiasettingsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class LiasettingsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    gmbAccounts: GmbAccounts
    kind: str
    liaSettings: LiaSettings
    omnichannelExperience: LiaOmnichannelExperience
    posDataProviders: _list[PosDataProviders]

@typing.type_check_only
class LiasettingsGetAccessibleGmbAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    gmbAccounts: _list[GmbAccountsGmbAccount]
    kind: str

@typing.type_check_only
class LiasettingsListPosDataProvidersResponse(typing_extensions.TypedDict, total=False):
    kind: str
    posDataProviders: _list[PosDataProviders]

@typing.type_check_only
class LiasettingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[LiaSettings]

@typing.type_check_only
class LiasettingsRequestGmbAccessResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class LiasettingsRequestInventoryVerificationResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str

@typing.type_check_only
class LiasettingsSetInventoryVerificationContactResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str

@typing.type_check_only
class LiasettingsSetPosDataProviderResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class LinkService(typing_extensions.TypedDict, total=False):
    service: str
    status: str

@typing.type_check_only
class LinkedAccount(typing_extensions.TypedDict, total=False):
    linkedAccountId: str
    services: _list[LinkService]

@typing.type_check_only
class ListAccountLabelsResponse(typing_extensions.TypedDict, total=False):
    accountLabels: _list[AccountLabel]
    nextPageToken: str

@typing.type_check_only
class ListAccountReturnCarrierResponse(typing_extensions.TypedDict, total=False):
    accountReturnCarriers: _list[AccountReturnCarrier]

@typing.type_check_only
class ListCollectionStatusesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[CollectionStatus]

@typing.type_check_only
class ListCollectionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Collection]

@typing.type_check_only
class ListConversionSourcesResponse(typing_extensions.TypedDict, total=False):
    conversionSources: _list[ConversionSource]
    nextPageToken: str

@typing.type_check_only
class ListCssesResponse(typing_extensions.TypedDict, total=False):
    csses: _list[Css]
    nextPageToken: str

@typing.type_check_only
class ListMethodQuotasResponse(typing_extensions.TypedDict, total=False):
    methodQuotas: _list[MethodQuota]
    nextPageToken: str

@typing.type_check_only
class ListPromotionResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    promotions: _list[Promotion]

@typing.type_check_only
class ListRegionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    regions: _list[Region]

@typing.type_check_only
class ListReturnPolicyOnlineResponse(typing_extensions.TypedDict, total=False):
    returnPolicies: _list[ReturnPolicyOnline]

@typing.type_check_only
class LocalInventory(typing_extensions.TypedDict, total=False):
    availability: str
    customAttributes: _list[CustomAttribute]
    instoreProductLocation: str
    kind: str
    pickupMethod: str
    pickupSla: str
    price: Price
    quantity: int
    salePrice: Price
    salePriceEffectiveDate: str
    storeCode: str

@typing.type_check_only
class LocalinventoryCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[LocalinventoryCustomBatchRequestEntry]

@typing.type_check_only
class LocalinventoryCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    localInventory: LocalInventory
    merchantId: str
    method: str
    productId: str

@typing.type_check_only
class LocalinventoryCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[LocalinventoryCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class LocalinventoryCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str

@typing.type_check_only
class LocationIdSet(typing_extensions.TypedDict, total=False):
    locationIds: _list[str]

@typing.type_check_only
class LoyaltyProgram(typing_extensions.TypedDict, total=False):
    cashbackForFutureUse: Price
    loyaltyPoints: str
    memberPriceEffectiveDate: str
    price: Price
    programLabel: str
    shippingLabel: str
    tierLabel: str

@typing.type_check_only
class MerchantCenterDestination(typing_extensions.TypedDict, total=False):
    attributionSettings: AttributionSettings
    currencyCode: str
    destinationId: str
    displayName: str

@typing.type_check_only
class MethodQuota(typing_extensions.TypedDict, total=False):
    method: str
    quotaLimit: str
    quotaMinuteLimit: str
    quotaUsage: str

@typing.type_check_only
class Metrics(typing_extensions.TypedDict, total=False):
    aos: float
    aovMicros: float
    clicks: str
    conversionRate: float
    conversionValueMicros: str
    conversions: float
    ctr: float
    daysToShip: float
    impressions: str
    itemDaysToShip: float
    itemFillRate: float
    orderedItemSalesMicros: str
    orderedItems: str
    orders: str
    rejectedItems: str
    returnRate: float
    returnedItems: str
    returnsMicros: str
    shippedItemSalesMicros: str
    shippedItems: str
    shippedOrders: str
    unshippedItems: float
    unshippedOrders: float

@typing.type_check_only
class MinimumOrderValueTable(typing_extensions.TypedDict, total=False):
    storeCodeSetWithMovs: _list[MinimumOrderValueTableStoreCodeSetWithMov]

@typing.type_check_only
class MinimumOrderValueTableStoreCodeSetWithMov(
    typing_extensions.TypedDict, total=False
):
    storeCodes: _list[str]
    value: Price

@typing.type_check_only
class OrderTrackingSignal(typing_extensions.TypedDict, total=False):
    customerShippingFee: PriceAmount
    deliveryPostalCode: str
    deliveryRegionCode: str
    lineItems: _list[OrderTrackingSignalLineItemDetails]
    merchantId: str
    orderCreatedTime: DateTime
    orderId: str
    orderTrackingSignalId: str
    shipmentLineItemMapping: _list[OrderTrackingSignalShipmentLineItemMapping]
    shippingInfo: _list[OrderTrackingSignalShippingInfo]

@typing.type_check_only
class OrderTrackingSignalLineItemDetails(typing_extensions.TypedDict, total=False):
    brand: str
    gtin: str
    lineItemId: str
    mpn: str
    productDescription: str
    productId: str
    productTitle: str
    quantity: str
    sku: str
    upc: str

@typing.type_check_only
class OrderTrackingSignalShipmentLineItemMapping(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    quantity: str
    shipmentId: str

@typing.type_check_only
class OrderTrackingSignalShippingInfo(typing_extensions.TypedDict, total=False):
    actualDeliveryTime: DateTime
    carrierName: str
    carrierServiceName: str
    earliestDeliveryPromiseTime: DateTime
    latestDeliveryPromiseTime: DateTime
    originPostalCode: str
    originRegionCode: str
    shipmentId: str
    shippedTime: DateTime
    shippingStatus: typing_extensions.Literal[
        "SHIPPING_STATE_UNSPECIFIED", "SHIPPED", "DELIVERED"
    ]
    trackingId: str

@typing.type_check_only
class PaymentServiceProviderLinkInfo(typing_extensions.TypedDict, total=False):
    externalAccountBusinessCountry: str
    externalAccountId: str

@typing.type_check_only
class PickupCarrierService(typing_extensions.TypedDict, total=False):
    carrierName: str
    serviceName: str

@typing.type_check_only
class PickupServicesPickupService(typing_extensions.TypedDict, total=False):
    carrierName: str
    country: str
    serviceName: str

@typing.type_check_only
class PosCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[PosCustomBatchRequestEntry]

@typing.type_check_only
class PosCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    inventory: PosInventory
    merchantId: str
    method: str
    sale: PosSale
    store: PosStore
    storeCode: str
    targetMerchantId: str

@typing.type_check_only
class PosCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[PosCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class PosCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    inventory: PosInventory
    kind: str
    sale: PosSale
    store: PosStore

@typing.type_check_only
class PosDataProviders(typing_extensions.TypedDict, total=False):
    country: str
    posDataProviders: _list[PosDataProvidersPosDataProvider]

@typing.type_check_only
class PosDataProvidersPosDataProvider(typing_extensions.TypedDict, total=False):
    displayName: str
    fullName: str
    providerId: str

@typing.type_check_only
class PosInventory(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    kind: str
    pickupMethod: str
    pickupSla: str
    price: Price
    quantity: str
    storeCode: str
    targetCountry: str
    timestamp: str

@typing.type_check_only
class PosInventoryRequest(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    pickupMethod: str
    pickupSla: str
    price: Price
    quantity: str
    storeCode: str
    targetCountry: str
    timestamp: str

@typing.type_check_only
class PosInventoryResponse(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    kind: str
    pickupMethod: str
    pickupSla: str
    price: Price
    quantity: str
    storeCode: str
    targetCountry: str
    timestamp: str

@typing.type_check_only
class PosListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    resources: _list[PosStore]

@typing.type_check_only
class PosSale(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    kind: str
    price: Price
    quantity: str
    saleId: str
    storeCode: str
    targetCountry: str
    timestamp: str

@typing.type_check_only
class PosSaleRequest(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    price: Price
    quantity: str
    saleId: str
    storeCode: str
    targetCountry: str
    timestamp: str

@typing.type_check_only
class PosSaleResponse(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    kind: str
    price: Price
    quantity: str
    saleId: str
    storeCode: str
    targetCountry: str
    timestamp: str

@typing.type_check_only
class PosStore(typing_extensions.TypedDict, total=False):
    gcidCategory: _list[str]
    kind: str
    matchingStatus: str
    matchingStatusHint: str
    phoneNumber: str
    placeId: str
    storeAddress: str
    storeCode: str
    storeName: str
    websiteUrl: str

@typing.type_check_only
class PostalCodeGroup(typing_extensions.TypedDict, total=False):
    country: str
    name: str
    postalCodeRanges: _list[PostalCodeRange]

@typing.type_check_only
class PostalCodeRange(typing_extensions.TypedDict, total=False):
    postalCodeRangeBegin: str
    postalCodeRangeEnd: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    currency: str
    value: str

@typing.type_check_only
class PriceAmount(typing_extensions.TypedDict, total=False):
    currency: str
    value: str

@typing.type_check_only
class PriceCompetitiveness(typing_extensions.TypedDict, total=False):
    benchmarkPriceCurrencyCode: str
    benchmarkPriceMicros: str
    countryCode: str

@typing.type_check_only
class PriceInsights(typing_extensions.TypedDict, total=False):
    effectiveness: typing_extensions.Literal[
        "EFFECTIVENESS_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    predictedClicksChangeFraction: float
    predictedConversionsChangeFraction: float
    predictedGrossProfitChangeFraction: float
    predictedImpressionsChangeFraction: float
    predictedMonthlyGrossProfitChangeCurrencyCode: str
    predictedMonthlyGrossProfitChangeMicros: str
    suggestedPriceCurrencyCode: str
    suggestedPriceMicros: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    additionalImageLinks: _list[str]
    additionalSizeType: str
    adsGrouping: str
    adsLabels: _list[str]
    adsRedirect: str
    adult: bool
    ageGroup: str
    autoPricingMinPrice: Price
    availability: str
    availabilityDate: str
    brand: str
    canonicalLink: str
    certifications: _list[ProductCertification]
    channel: str
    cloudExportAdditionalProperties: _list[CloudExportAdditionalProperties]
    color: str
    condition: str
    contentLanguage: str
    costOfGoodsSold: Price
    customAttributes: _list[CustomAttribute]
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    description: str
    disclosureDate: str
    displayAdsId: str
    displayAdsLink: str
    displayAdsSimilarIds: _list[str]
    displayAdsTitle: str
    displayAdsValue: float
    energyEfficiencyClass: str
    excludedDestinations: _list[str]
    expirationDate: str
    externalSellerId: str
    feedLabel: str
    freeShippingThreshold: _list[FreeShippingThreshold]
    gender: str
    googleProductCategory: str
    gtin: str
    id: str
    identifierExists: bool
    imageLink: str
    includedDestinations: _list[str]
    installment: Installment
    isBundle: bool
    itemGroupId: str
    kind: str
    lifestyleImageLinks: _list[str]
    link: str
    linkTemplate: str
    loyaltyProgram: LoyaltyProgram
    loyaltyPrograms: _list[LoyaltyProgram]
    material: str
    maxEnergyEfficiencyClass: str
    maxHandlingTime: str
    minEnergyEfficiencyClass: str
    minHandlingTime: str
    mobileLink: str
    mobileLinkTemplate: str
    mpn: str
    multipack: str
    offerId: str
    pattern: str
    pause: str
    pickupMethod: str
    pickupSla: str
    price: Price
    productDetails: _list[ProductProductDetail]
    productHeight: ProductDimension
    productHighlights: _list[str]
    productLength: ProductDimension
    productTypes: _list[str]
    productWeight: ProductWeight
    productWidth: ProductDimension
    promotionIds: _list[str]
    salePrice: Price
    salePriceEffectiveDate: str
    sellOnGoogleQuantity: str
    shipping: _list[ProductShipping]
    shippingHeight: ProductShippingDimension
    shippingLabel: str
    shippingLength: ProductShippingDimension
    shippingWeight: ProductShippingWeight
    shippingWidth: ProductShippingDimension
    shoppingAdsExcludedCountries: _list[str]
    sizeSystem: str
    sizeType: str
    sizes: _list[str]
    source: str
    structuredDescription: ProductStructuredDescription
    structuredTitle: ProductStructuredTitle
    subscriptionCost: ProductSubscriptionCost
    sustainabilityIncentives: _list[ProductSustainabilityIncentive]
    targetCountry: str
    taxCategory: str
    taxes: _list[ProductTax]
    title: str
    transitTimeLabel: str
    unitPricingBaseMeasure: ProductUnitPricingBaseMeasure
    unitPricingMeasure: ProductUnitPricingMeasure
    virtualModelLink: str

@typing.type_check_only
class ProductCertification(typing_extensions.TypedDict, total=False):
    certificationAuthority: str
    certificationCode: str
    certificationName: str
    certificationValue: str

@typing.type_check_only
class ProductCluster(typing_extensions.TypedDict, total=False):
    brand: str
    brandInventoryStatus: typing_extensions.Literal[
        "INVENTORY_STATUS_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "NOT_IN_INVENTORY"
    ]
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    inventoryStatus: typing_extensions.Literal[
        "INVENTORY_STATUS_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK", "NOT_IN_INVENTORY"
    ]
    title: str
    variantGtins: _list[str]

@typing.type_check_only
class ProductDeliveryTime(typing_extensions.TypedDict, total=False):
    areaDeliveryTimes: _list[ProductDeliveryTimeAreaDeliveryTime]
    productId: ProductId

@typing.type_check_only
class ProductDeliveryTimeAreaDeliveryTime(typing_extensions.TypedDict, total=False):
    deliveryArea: DeliveryArea
    deliveryTime: ProductDeliveryTimeAreaDeliveryTimeDeliveryTime

@typing.type_check_only
class ProductDeliveryTimeAreaDeliveryTimeDeliveryTime(
    typing_extensions.TypedDict, total=False
):
    maxHandlingTimeDays: int
    maxTransitTimeDays: int
    minHandlingTimeDays: int
    minTransitTimeDays: int

@typing.type_check_only
class ProductDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductId(typing_extensions.TypedDict, total=False):
    productId: str

@typing.type_check_only
class ProductIssue(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    impact: ProductIssueImpact
    prerenderedContent: str
    title: str

@typing.type_check_only
class ProductIssueImpact(typing_extensions.TypedDict, total=False):
    breakdowns: _list[Breakdown]
    message: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class ProductProductDetail(typing_extensions.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

@typing.type_check_only
class ProductShipping(typing_extensions.TypedDict, total=False):
    country: str
    locationGroupName: str
    locationId: str
    maxHandlingTime: str
    maxTransitTime: str
    minHandlingTime: str
    minTransitTime: str
    postalCode: str
    price: Price
    region: str
    service: str

@typing.type_check_only
class ProductShippingDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductShippingWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductStatus(typing_extensions.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[ProductStatusDestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: _list[ProductStatusItemLevelIssue]
    kind: str
    lastUpdateDate: str
    link: str
    productId: str
    title: str

@typing.type_check_only
class ProductStatusDestinationStatus(typing_extensions.TypedDict, total=False):
    approvedCountries: _list[str]
    destination: str
    disapprovedCountries: _list[str]
    pendingCountries: _list[str]
    status: str

@typing.type_check_only
class ProductStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    applicableCountries: _list[str]
    attributeName: str
    code: str
    description: str
    destination: str
    detail: str
    documentation: str
    resolution: str
    servability: str

@typing.type_check_only
class ProductStructuredDescription(typing_extensions.TypedDict, total=False):
    content: str
    digitalSourceType: str

@typing.type_check_only
class ProductStructuredTitle(typing_extensions.TypedDict, total=False):
    content: str
    digitalSourceType: str

@typing.type_check_only
class ProductSubscriptionCost(typing_extensions.TypedDict, total=False):
    amount: Price
    period: str
    periodLength: str

@typing.type_check_only
class ProductSustainabilityIncentive(typing_extensions.TypedDict, total=False):
    amount: Price
    percentage: float
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "EV_TAX_CREDIT", "EV_PRICE_DISCOUNT"
    ]

@typing.type_check_only
class ProductTax(typing_extensions.TypedDict, total=False):
    country: str
    locationId: str
    postalCode: str
    rate: float
    region: str
    taxShip: bool

@typing.type_check_only
class ProductUnitPricingBaseMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class ProductUnitPricingMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductView(typing_extensions.TypedDict, total=False):
    aggregatedDestinationStatus: typing_extensions.Literal[
        "AGGREGATED_STATUS_UNSPECIFIED",
        "NOT_ELIGIBLE_OR_DISAPPROVED",
        "PENDING",
        "ELIGIBLE_LIMITED",
        "ELIGIBLE",
    ]
    availability: str
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    channel: typing_extensions.Literal["CHANNEL_UNSPECIFIED", "LOCAL", "ONLINE"]
    clickPotential: typing_extensions.Literal[
        "CLICK_POTENTIAL_UNSPECIFIED", "LOW", "MEDIUM", "HIGH"
    ]
    clickPotentialRank: str
    condition: str
    creationTime: str
    currencyCode: str
    expirationDate: Date
    gtin: _list[str]
    id: str
    itemGroupId: str
    itemIssues: _list[ProductViewItemIssue]
    languageCode: str
    offerId: str
    priceMicros: str
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    shippingLabel: str
    title: str

@typing.type_check_only
class ProductViewItemIssue(typing_extensions.TypedDict, total=False):
    issueType: ProductViewItemIssueItemIssueType
    resolution: typing_extensions.Literal[
        "UNKNOWN", "MERCHANT_ACTION", "PENDING_PROCESSING"
    ]
    severity: ProductViewItemIssueItemIssueSeverity

@typing.type_check_only
class ProductViewItemIssueIssueSeverityPerDestination(
    typing_extensions.TypedDict, total=False
):
    demotedCountries: _list[str]
    destination: str
    disapprovedCountries: _list[str]

@typing.type_check_only
class ProductViewItemIssueItemIssueSeverity(typing_extensions.TypedDict, total=False):
    aggregatedSeverity: typing_extensions.Literal[
        "AGGREGATED_ISSUE_SEVERITY_UNSPECIFIED", "DISAPPROVED", "DEMOTED", "PENDING"
    ]
    severityPerDestination: _list[ProductViewItemIssueIssueSeverityPerDestination]

@typing.type_check_only
class ProductViewItemIssueItemIssueType(typing_extensions.TypedDict, total=False):
    canonicalAttribute: str
    code: str

@typing.type_check_only
class ProductWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[ProductsCustomBatchRequestEntry]

@typing.type_check_only
class ProductsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    feedId: str
    merchantId: str
    method: str
    product: Product
    productId: str
    updateMask: str

@typing.type_check_only
class ProductsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[ProductsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ProductsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str
    product: Product

@typing.type_check_only
class ProductsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[Product]

@typing.type_check_only
class ProductstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[ProductstatusesCustomBatchRequestEntry]

@typing.type_check_only
class ProductstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    destinations: _list[str]
    includeAttributes: bool
    merchantId: str
    method: str
    productId: str

@typing.type_check_only
class ProductstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[ProductstatusesCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ProductstatusesCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str
    productStatus: ProductStatus

@typing.type_check_only
class ProductstatusesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[ProductStatus]

@typing.type_check_only
class Promotion(typing_extensions.TypedDict, total=False):
    brand: _list[str]
    brandExclusion: _list[str]
    contentLanguage: str
    couponValueType: typing_extensions.Literal[
        "COUPON_VALUE_TYPE_UNSPECIFIED",
        "MONEY_OFF",
        "PERCENT_OFF",
        "BUY_M_GET_N_MONEY_OFF",
        "BUY_M_GET_N_PERCENT_OFF",
        "BUY_M_GET_MONEY_OFF",
        "BUY_M_GET_PERCENT_OFF",
        "FREE_GIFT",
        "FREE_GIFT_WITH_VALUE",
        "FREE_GIFT_WITH_ITEM_ID",
        "FREE_SHIPPING_STANDARD",
        "FREE_SHIPPING_OVERNIGHT",
        "FREE_SHIPPING_TWO_DAY",
    ]
    freeGiftDescription: str
    freeGiftItemId: str
    freeGiftValue: PriceAmount
    genericRedemptionCode: str
    getThisQuantityDiscounted: int
    id: str
    itemGroupId: _list[str]
    itemGroupIdExclusion: _list[str]
    itemId: _list[str]
    itemIdExclusion: _list[str]
    limitQuantity: int
    limitValue: PriceAmount
    longTitle: str
    minimumPurchaseAmount: PriceAmount
    minimumPurchaseQuantity: int
    moneyBudget: PriceAmount
    moneyOffAmount: PriceAmount
    offerType: typing_extensions.Literal[
        "OFFER_TYPE_UNSPECIFIED", "NO_CODE", "GENERIC_CODE"
    ]
    orderLimit: int
    percentOff: int
    productApplicability: typing_extensions.Literal[
        "PRODUCT_APPLICABILITY_UNSPECIFIED", "ALL_PRODUCTS", "SPECIFIC_PRODUCTS"
    ]
    productType: _list[str]
    productTypeExclusion: _list[str]
    promotionDestinationIds: _list[str]
    promotionDisplayDates: str
    promotionDisplayTimePeriod: TimePeriod
    promotionEffectiveDates: str
    promotionEffectiveTimePeriod: TimePeriod
    promotionId: str
    promotionStatus: PromotionPromotionStatus
    promotionUrl: str
    redemptionChannel: _list[
        typing_extensions.Literal[
            "REDEMPTION_CHANNEL_UNSPECIFIED", "IN_STORE", "ONLINE"
        ]
    ]
    shippingServiceNames: _list[str]
    storeApplicability: typing_extensions.Literal[
        "STORE_APPLICABILITY_UNSPECIFIED", "ALL_STORES", "SPECIFIC_STORES"
    ]
    storeCode: _list[str]
    storeCodeExclusion: _list[str]
    targetCountry: str

@typing.type_check_only
class PromotionPromotionStatus(typing_extensions.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[PromotionPromotionStatusDestinationStatus]
    lastUpdateDate: str
    promotionIssue: _list[PromotionPromotionStatusPromotionIssue]

@typing.type_check_only
class PromotionPromotionStatusDestinationStatus(
    typing_extensions.TypedDict, total=False
):
    destination: str
    status: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "IN_REVIEW",
        "REJECTED",
        "LIVE",
        "STOPPED",
        "EXPIRED",
        "PENDING",
    ]

@typing.type_check_only
class PromotionPromotionStatusPromotionIssue(typing_extensions.TypedDict, total=False):
    code: str
    detail: str

@typing.type_check_only
class PubsubNotificationSettings(typing_extensions.TypedDict, total=False):
    cloudTopicName: str
    kind: str
    registeredEvents: _list[str]

@typing.type_check_only
class RateGroup(typing_extensions.TypedDict, total=False):
    applicableShippingLabels: _list[str]
    carrierRates: _list[CarrierRate]
    mainTable: Table
    name: str
    singleValue: Value
    subtables: _list[Table]

@typing.type_check_only
class Recommendation(typing_extensions.TypedDict, total=False):
    additionalCallToAction: _list[RecommendationCallToAction]
    additionalDescriptions: _list[RecommendationDescription]
    creative: _list[RecommendationCreative]
    defaultCallToAction: RecommendationCallToAction
    defaultDescription: str
    numericalImpact: int
    paid: bool
    recommendationName: str
    subType: str
    title: str
    type: str

@typing.type_check_only
class RecommendationCallToAction(typing_extensions.TypedDict, total=False):
    intent: str
    localizedText: str
    uri: str

@typing.type_check_only
class RecommendationCreative(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["CREATIVE_TYPE_UNSPECIFIED", "VIDEO", "PHOTO"]
    uri: str

@typing.type_check_only
class RecommendationDescription(typing_extensions.TypedDict, total=False):
    text: str
    type: typing_extensions.Literal["DESCRIPTION_TYPE_UNSPECIFIED", "SHORT", "LONG"]

@typing.type_check_only
class Region(typing_extensions.TypedDict, total=False):
    displayName: str
    geotargetArea: RegionGeoTargetArea
    merchantId: str
    postalCodeArea: RegionPostalCodeArea
    regionId: str
    regionalInventoryEligible: bool
    shippingEligible: bool

@typing.type_check_only
class RegionGeoTargetArea(typing_extensions.TypedDict, total=False):
    geotargetCriteriaIds: _list[str]

@typing.type_check_only
class RegionPostalCodeArea(typing_extensions.TypedDict, total=False):
    postalCodes: _list[RegionPostalCodeAreaPostalCodeRange]
    regionCode: str

@typing.type_check_only
class RegionPostalCodeAreaPostalCodeRange(typing_extensions.TypedDict, total=False):
    begin: str
    end: str

@typing.type_check_only
class RegionalInventory(typing_extensions.TypedDict, total=False):
    availability: str
    customAttributes: _list[CustomAttribute]
    kind: str
    price: Price
    regionId: str
    salePrice: Price
    salePriceEffectiveDate: str

@typing.type_check_only
class RegionalinventoryCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[RegionalinventoryCustomBatchRequestEntry]

@typing.type_check_only
class RegionalinventoryCustomBatchRequestEntry(
    typing_extensions.TypedDict, total=False
):
    batchId: int
    merchantId: str
    method: str
    productId: str
    regionalInventory: RegionalInventory

@typing.type_check_only
class RegionalinventoryCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[RegionalinventoryCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class RegionalinventoryCustomBatchResponseEntry(
    typing_extensions.TypedDict, total=False
):
    batchId: int
    errors: Errors
    kind: str
    regionalInventory: RegionalInventory

@typing.type_check_only
class RenderAccountIssuesRequestPayload(typing_extensions.TypedDict, total=False):
    contentOption: typing_extensions.Literal[
        "CONTENT_OPTION_UNSPECIFIED", "PRE_RENDERED_HTML"
    ]
    userInputActionOption: typing_extensions.Literal[
        "USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED",
        "REDIRECT_TO_MERCHANT_CENTER",
        "BUILT_IN_USER_INPUT_ACTIONS",
    ]

@typing.type_check_only
class RenderAccountIssuesResponse(typing_extensions.TypedDict, total=False):
    alternateDisputeResolution: AlternateDisputeResolution
    issues: _list[AccountIssue]

@typing.type_check_only
class RenderProductIssuesRequestPayload(typing_extensions.TypedDict, total=False):
    contentOption: typing_extensions.Literal[
        "CONTENT_OPTION_UNSPECIFIED", "PRE_RENDERED_HTML"
    ]
    userInputActionOption: typing_extensions.Literal[
        "USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED",
        "REDIRECT_TO_MERCHANT_CENTER",
        "BUILT_IN_USER_INPUT_ACTIONS",
    ]

@typing.type_check_only
class RenderProductIssuesResponse(typing_extensions.TypedDict, total=False):
    alternateDisputeResolution: AlternateDisputeResolution
    issues: _list[ProductIssue]

@typing.type_check_only
class ReportInteractionRequest(typing_extensions.TypedDict, total=False):
    interactionType: typing_extensions.Literal[
        "INTERACTION_TYPE_UNSPECIFIED", "INTERACTION_DISMISS", "INTERACTION_CLICK"
    ]
    responseToken: str
    subtype: str
    type: str

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
    bestSellers: BestSellers
    brand: Brand
    competitiveVisibility: CompetitiveVisibility
    metrics: Metrics
    priceCompetitiveness: PriceCompetitiveness
    priceInsights: PriceInsights
    productCluster: ProductCluster
    productView: ProductView
    segments: Segments
    topicTrends: TopicTrends

@typing.type_check_only
class RequestPhoneVerificationRequest(typing_extensions.TypedDict, total=False):
    languageCode: str
    phoneNumber: str
    phoneRegionCode: str
    phoneVerificationMethod: typing_extensions.Literal[
        "PHONE_VERIFICATION_METHOD_UNSPECIFIED", "SMS", "PHONE_CALL"
    ]

@typing.type_check_only
class RequestPhoneVerificationResponse(typing_extensions.TypedDict, total=False):
    verificationId: str

@typing.type_check_only
class RequestReviewFreeListingsRequest(typing_extensions.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class RequestReviewShoppingAdsRequest(typing_extensions.TypedDict, total=False):
    regionCode: str

@typing.type_check_only
class ReturnAddress(typing_extensions.TypedDict, total=False):
    address: ReturnAddressAddress
    country: str
    kind: str
    label: str
    phoneNumber: str
    returnAddressId: str

@typing.type_check_only
class ReturnAddressAddress(typing_extensions.TypedDict, total=False):
    country: str
    locality: str
    postalCode: str
    recipientName: str
    region: str
    streetAddress: _list[str]

@typing.type_check_only
class ReturnPolicy(typing_extensions.TypedDict, total=False):
    country: str
    kind: str
    label: str
    name: str
    nonFreeReturnReasons: _list[str]
    policy: ReturnPolicyPolicy
    returnPolicyId: str
    returnShippingFee: Price
    seasonalOverrides: _list[ReturnPolicySeasonalOverride]

@typing.type_check_only
class ReturnPolicyOnline(typing_extensions.TypedDict, total=False):
    countries: _list[str]
    itemConditions: _list[
        typing_extensions.Literal["ITEM_CONDITION_UNSPECIFIED", "NEW", "USED"]
    ]
    label: str
    name: str
    policy: ReturnPolicyOnlinePolicy
    restockingFee: ReturnPolicyOnlineRestockingFee
    returnMethods: _list[
        typing_extensions.Literal[
            "RETURN_METHOD_UNSPECIFIED", "BY_MAIL", "IN_STORE", "AT_A_KIOSK"
        ]
    ]
    returnPolicyId: str
    returnPolicyUri: str
    returnReasonCategoryInfo: _list[ReturnPolicyOnlineReturnReasonCategoryInfo]

@typing.type_check_only
class ReturnPolicyOnlinePolicy(typing_extensions.TypedDict, total=False):
    days: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "NUMBER_OF_DAYS_AFTER_DELIVERY",
        "NO_RETURNS",
        "LIFETIME_RETURNS",
    ]

@typing.type_check_only
class ReturnPolicyOnlineRestockingFee(typing_extensions.TypedDict, total=False):
    fixedFee: PriceAmount
    microPercent: int

@typing.type_check_only
class ReturnPolicyOnlineReturnReasonCategoryInfo(
    typing_extensions.TypedDict, total=False
):
    returnLabelSource: typing_extensions.Literal[
        "RETURN_LABEL_SOURCE_UNSPECIFIED",
        "DOWNLOAD_AND_PRINT",
        "IN_THE_BOX",
        "CUSTOMER_RESPONSIBILITY",
    ]
    returnReasonCategory: typing_extensions.Literal[
        "RETURN_REASON_CATEGORY_UNSPECIFIED", "BUYER_REMORSE", "ITEM_DEFECT"
    ]
    returnShippingFee: ReturnPolicyOnlineReturnShippingFee

@typing.type_check_only
class ReturnPolicyOnlineReturnShippingFee(typing_extensions.TypedDict, total=False):
    fixedFee: PriceAmount
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "FIXED", "CUSTOMER_PAYING_ACTUAL_FEE"
    ]

@typing.type_check_only
class ReturnPolicyPolicy(typing_extensions.TypedDict, total=False):
    lastReturnDate: str
    numberOfDays: str
    type: str

@typing.type_check_only
class ReturnPolicySeasonalOverride(typing_extensions.TypedDict, total=False):
    endDate: str
    name: str
    policy: ReturnPolicyPolicy
    startDate: str

@typing.type_check_only
class ReturnaddressCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[ReturnaddressCustomBatchRequestEntry]

@typing.type_check_only
class ReturnaddressCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    merchantId: str
    method: str
    returnAddress: ReturnAddress
    returnAddressId: str

@typing.type_check_only
class ReturnaddressCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[ReturnaddressCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ReturnaddressCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str
    returnAddress: ReturnAddress

@typing.type_check_only
class ReturnaddressListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[ReturnAddress]

@typing.type_check_only
class ReturnpolicyCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[ReturnpolicyCustomBatchRequestEntry]

@typing.type_check_only
class ReturnpolicyCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    merchantId: str
    method: str
    returnPolicy: ReturnPolicy
    returnPolicyId: str

@typing.type_check_only
class ReturnpolicyCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[ReturnpolicyCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ReturnpolicyCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str
    returnPolicy: ReturnPolicy

@typing.type_check_only
class ReturnpolicyListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    resources: _list[ReturnPolicy]

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    cells: _list[Value]

@typing.type_check_only
class SearchRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: _list[ReportRow]

@typing.type_check_only
class Segments(typing_extensions.TypedDict, total=False):
    brand: str
    categoryL1: str
    categoryL2: str
    categoryL3: str
    categoryL4: str
    categoryL5: str
    currencyCode: str
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    customerCountryCode: str
    date: Date
    offerId: str
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    program: typing_extensions.Literal[
        "PROGRAM_UNSPECIFIED",
        "SHOPPING_ADS",
        "FREE_PRODUCT_LISTING",
        "FREE_LOCAL_PRODUCT_LISTING",
        "BUY_ON_GOOGLE_LISTING",
    ]
    title: str
    week: Date

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    active: bool
    currency: str
    deliveryCountry: str
    deliveryTime: DeliveryTime
    eligibility: str
    minimumOrderValue: Price
    minimumOrderValueTable: MinimumOrderValueTable
    name: str
    pickupService: PickupCarrierService
    rateGroups: _list[RateGroup]
    shipmentType: str
    storeConfig: ServiceStoreConfig

@typing.type_check_only
class ServiceStoreConfig(typing_extensions.TypedDict, total=False):
    cutoffConfig: ServiceStoreConfigCutoffConfig
    serviceRadius: Distance
    storeCodes: _list[str]
    storeServiceType: str

@typing.type_check_only
class ServiceStoreConfigCutoffConfig(typing_extensions.TypedDict, total=False):
    localCutoffTime: ServiceStoreConfigCutoffConfigLocalCutoffTime
    noDeliveryPostCutoff: bool
    storeCloseOffsetHours: str

@typing.type_check_only
class ServiceStoreConfigCutoffConfigLocalCutoffTime(
    typing_extensions.TypedDict, total=False
):
    hour: str
    minute: str

@typing.type_check_only
class ShippingSettings(typing_extensions.TypedDict, total=False):
    accountId: str
    postalCodeGroups: _list[PostalCodeGroup]
    services: _list[Service]
    warehouses: _list[Warehouse]

@typing.type_check_only
class ShippingsettingsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[ShippingsettingsCustomBatchRequestEntry]

@typing.type_check_only
class ShippingsettingsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    merchantId: str
    method: str
    shippingSettings: ShippingSettings

@typing.type_check_only
class ShippingsettingsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[ShippingsettingsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ShippingsettingsCustomBatchResponseEntry(
    typing_extensions.TypedDict, total=False
):
    batchId: int
    errors: Errors
    kind: str
    shippingSettings: ShippingSettings

@typing.type_check_only
class ShippingsettingsGetSupportedCarriersResponse(
    typing_extensions.TypedDict, total=False
):
    carriers: _list[CarriersCarrier]
    kind: str

@typing.type_check_only
class ShippingsettingsGetSupportedHolidaysResponse(
    typing_extensions.TypedDict, total=False
):
    holidays: _list[HolidaysHoliday]
    kind: str

@typing.type_check_only
class ShippingsettingsGetSupportedPickupServicesResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    pickupServices: _list[PickupServicesPickupService]

@typing.type_check_only
class ShippingsettingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[ShippingSettings]

@typing.type_check_only
class ShoppingAdsProgramStatus(typing_extensions.TypedDict, total=False):
    globalState: typing_extensions.Literal[
        "PROGRAM_STATE_UNSPECIFIED", "NOT_ENABLED", "NO_OFFERS_UPLOADED", "ENABLED"
    ]
    regionStatuses: _list[ShoppingAdsProgramStatusRegionStatus]

@typing.type_check_only
class ShoppingAdsProgramStatusRegionStatus(typing_extensions.TypedDict, total=False):
    disapprovalDate: str
    eligibilityStatus: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "APPROVED",
        "DISAPPROVED",
        "WARNING",
        "UNDER_REVIEW",
        "PENDING_REVIEW",
        "ONBOARDING",
    ]
    onboardingIssues: _list[str]
    regionCodes: _list[str]
    reviewEligibilityStatus: typing_extensions.Literal[
        "REVIEW_ELIGIBILITY_UNSPECIFIED", "ELIGIBLE", "INELIGIBLE"
    ]
    reviewIneligibilityReason: typing_extensions.Literal[
        "REVIEW_INELIGIBILITY_REASON_UNSPECIFIED",
        "ONBOARDING_ISSUES",
        "NOT_ENOUGH_OFFERS",
        "IN_COOLDOWN_PERIOD",
        "ALREADY_UNDER_REVIEW",
        "NO_REVIEW_REQUIRED",
        "WILL_BE_REVIEWED_AUTOMATICALLY",
        "IS_RETIRED",
        "ALREADY_REVIEWED",
    ]
    reviewIneligibilityReasonDescription: str
    reviewIneligibilityReasonDetails: (
        ShoppingAdsProgramStatusReviewIneligibilityReasonDetails
    )
    reviewIssues: _list[str]

@typing.type_check_only
class ShoppingAdsProgramStatusReviewIneligibilityReasonDetails(
    typing_extensions.TypedDict, total=False
):
    cooldownTime: str

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    columnHeaders: Headers
    name: str
    rowHeaders: Headers
    rows: _list[Row]

@typing.type_check_only
class TextWithTooltip(typing_extensions.TypedDict, total=False):
    simpleTooltipValue: str
    simpleValue: str
    tooltipIconStyle: typing_extensions.Literal[
        "TOOLTIP_ICON_STYLE_UNSPECIFIED", "INFO", "QUESTION"
    ]

@typing.type_check_only
class TimePeriod(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class TopicTrends(typing_extensions.TypedDict, total=False):
    customerCountryCode: str
    date: Date
    last120DaysSearchInterest: float
    last30DaysSearchInterest: float
    last7DaysSearchInterest: float
    last90DaysSearchInterest: float
    next7DaysSearchInterest: float
    searchInterest: float
    topic: str

@typing.type_check_only
class TransitTable(typing_extensions.TypedDict, total=False):
    postalCodeGroupNames: _list[str]
    rows: _list[TransitTableTransitTimeRow]
    transitTimeLabels: _list[str]

@typing.type_check_only
class TransitTableTransitTimeRow(typing_extensions.TypedDict, total=False):
    values: _list[TransitTableTransitTimeRowTransitTimeValue]

@typing.type_check_only
class TransitTableTransitTimeRowTransitTimeValue(
    typing_extensions.TypedDict, total=False
):
    maxTransitTimeInDays: int
    minTransitTimeInDays: int

@typing.type_check_only
class TriggerActionPayload(typing_extensions.TypedDict, total=False):
    actionContext: str
    actionInput: ActionInput

@typing.type_check_only
class TriggerActionResponse(typing_extensions.TypedDict, total=False):
    message: str

@typing.type_check_only
class UndeleteConversionSourceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UrlSettings(typing_extensions.TypedDict, total=False):
    cartUriTemplate: str
    checkoutUriTemplate: str

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    carrierRateName: str
    flatRate: Price
    noShipping: bool
    pricePercentage: str
    subtableName: str

@typing.type_check_only
class VerifyPhoneNumberRequest(typing_extensions.TypedDict, total=False):
    phoneVerificationMethod: typing_extensions.Literal[
        "PHONE_VERIFICATION_METHOD_UNSPECIFIED", "SMS", "PHONE_CALL"
    ]
    verificationCode: str
    verificationId: str

@typing.type_check_only
class VerifyPhoneNumberResponse(typing_extensions.TypedDict, total=False):
    verifiedPhoneNumber: str

@typing.type_check_only
class Warehouse(typing_extensions.TypedDict, total=False):
    businessDayConfig: BusinessDayConfig
    cutoffTime: WarehouseCutoffTime
    handlingDays: str
    name: str
    shippingAddress: Address

@typing.type_check_only
class WarehouseBasedDeliveryTime(typing_extensions.TypedDict, total=False):
    carrier: str
    carrierService: str
    originAdministrativeArea: str
    originCity: str
    originCountry: str
    originPostalCode: str
    originStreetAddress: str
    warehouseName: str

@typing.type_check_only
class WarehouseCutoffTime(typing_extensions.TypedDict, total=False):
    hour: int
    minute: int

@typing.type_check_only
class Weight(typing_extensions.TypedDict, total=False):
    unit: str
    value: str
