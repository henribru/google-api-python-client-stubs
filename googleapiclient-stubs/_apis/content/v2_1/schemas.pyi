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
    businessInformation: AccountBusinessInformation
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
class AccountBusinessInformation(typing_extensions.TypedDict, total=False):
    address: AccountAddress
    customerService: AccountCustomerService
    koreanBusinessRegistrationNumber: str
    phoneNumber: str
    phoneVerificationStatus: str

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
class AccountImageImprovements(typing_extensions.TypedDict, total=False):
    accountImageImprovementsSettings: AccountImageImprovementsSettings
    effectiveAllowAutomaticImageImprovements: bool

@typing.type_check_only
class AccountImageImprovementsSettings(typing_extensions.TypedDict, total=False):
    allowAutomaticImageImprovements: bool

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
class ActivateBuyOnGoogleProgramRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    administrativeArea: str
    city: str
    country: str
    postalCode: str
    streetAddress: str

@typing.type_check_only
class Amount(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    taxAmount: Price

@typing.type_check_only
class BusinessDayConfig(typing_extensions.TypedDict, total=False):
    businessDays: _list[str]

@typing.type_check_only
class BuyOnGoogleProgramStatus(typing_extensions.TypedDict, total=False):
    businessModel: _list[str]
    customerServicePendingEmail: str
    customerServicePendingPhoneNumber: str
    customerServicePendingPhoneRegionCode: str
    customerServiceVerifiedEmail: str
    customerServiceVerifiedPhoneNumber: str
    customerServiceVerifiedPhoneRegionCode: str
    onlineSalesChannel: typing_extensions.Literal[
        "ONLINE_SALES_CHANNEL_UNSPECIFIED",
        "GOOGLE_EXCLUSIVE",
        "GOOGLE_AND_OTHER_WEBSITES",
    ]
    participationStage: typing_extensions.Literal[
        "PROGRAM_PARTICIPATION_STAGE_UNSPECIFIED",
        "NOT_ELIGIBLE",
        "ELIGIBLE",
        "ONBOARDING",
        "ELIGIBLE_FOR_REVIEW",
        "PENDING_REVIEW",
        "REVIEW_DISAPPROVED",
        "ACTIVE",
        "PAUSED",
    ]

@typing.type_check_only
class CaptureOrderRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CaptureOrderResponse(typing_extensions.TypedDict, total=False):
    executionStatus: typing_extensions.Literal[
        "EXECUTION_STATUS_UNSPECIFIED", "EXECUTED", "DUPLICATE"
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
class Css(typing_extensions.TypedDict, total=False):
    cssDomainId: str
    cssGroupId: str
    displayName: str
    fullName: str
    homepageUri: str
    labelIds: _list[str]

@typing.type_check_only
class CustomAttribute(dict[str, typing.Any]): ...

@typing.type_check_only
class CustomerReturnReason(typing_extensions.TypedDict, total=False):
    description: str
    reasonCode: str

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
    includedDestinations: _list[str]
    language: str

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
    reviewIneligibilityReasonDetails: FreeListingsProgramStatusReviewIneligibilityReasonDetails
    reviewIssues: _list[str]

@typing.type_check_only
class FreeListingsProgramStatusReviewIneligibilityReasonDetails(
    typing_extensions.TypedDict, total=False
):
    cooldownTime: str

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
class InapplicabilityDetails(typing_extensions.TypedDict, total=False):
    inapplicableCount: str
    inapplicableReason: typing_extensions.Literal[
        "INAPPLICABLE_REASON_UNSPECIFIED",
        "CANNOT_BEAT_BUYBOX_WINNER",
        "ALREADY_WINNING_BUYBOX",
        "TRIUMPHED_OVER_BY_SAME_TYPE_RULE",
        "TRIUMPHED_OVER_BY_OTHER_RULE_ON_OFFER",
        "RESTRICTIONS_NOT_MET",
        "UNCATEGORIZED",
        "INVALID_AUTO_PRICE_MIN",
        "INVALID_FLOOR_CONFIG",
    ]

@typing.type_check_only
class Installment(typing_extensions.TypedDict, total=False):
    amount: Price
    months: str

@typing.type_check_only
class InvoiceSummary(typing_extensions.TypedDict, total=False):
    additionalChargeSummaries: _list[InvoiceSummaryAdditionalChargeSummary]
    productTotal: Amount

@typing.type_check_only
class InvoiceSummaryAdditionalChargeSummary(typing_extensions.TypedDict, total=False):
    totalAmount: Amount
    type: str

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
class ListCssesResponse(typing_extensions.TypedDict, total=False):
    csses: _list[Css]
    nextPageToken: str

@typing.type_check_only
class ListRegionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    regions: _list[Region]

@typing.type_check_only
class ListRepricingProductReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repricingProductReports: _list[RepricingProductReport]

@typing.type_check_only
class ListRepricingRuleReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repricingRuleReports: _list[RepricingRuleReport]

@typing.type_check_only
class ListRepricingRulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repricingRules: _list[RepricingRule]

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
class LocalinventoryCustomBatchRequestEntry(dict[str, typing.Any]): ...

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
class LoyaltyPoints(typing_extensions.TypedDict, total=False):
    name: str
    pointsValue: str
    ratio: float

@typing.type_check_only
class MerchantOrderReturn(typing_extensions.TypedDict, total=False):
    creationDate: str
    merchantOrderId: str
    orderId: str
    orderReturnId: str
    returnItems: _list[MerchantOrderReturnItem]
    returnPricingInfo: ReturnPricingInfo
    returnShipments: _list[ReturnShipment]

@typing.type_check_only
class MerchantOrderReturnItem(typing_extensions.TypedDict, total=False):
    customerReturnReason: CustomerReturnReason
    itemId: str
    merchantRejectionReason: MerchantRejectionReason
    merchantReturnReason: RefundReason
    product: OrderLineItemProduct
    refundableAmount: MonetaryAmount
    returnItemId: str
    returnShipmentIds: _list[str]
    shipmentGroupId: str
    shipmentUnitId: str
    state: str

@typing.type_check_only
class MerchantRejectionReason(typing_extensions.TypedDict, total=False):
    description: str
    reasonCode: str

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
class MonetaryAmount(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    taxAmount: Price

@typing.type_check_only
class OnboardBuyOnGoogleProgramRequest(typing_extensions.TypedDict, total=False):
    customerServiceEmail: str

@typing.type_check_only
class Order(typing_extensions.TypedDict, total=False):
    acknowledged: bool
    annotations: _list[OrderOrderAnnotation]
    billingAddress: OrderAddress
    customer: OrderCustomer
    deliveryDetails: OrderDeliveryDetails
    id: str
    kind: str
    lineItems: _list[OrderLineItem]
    merchantId: str
    merchantOrderId: str
    netPriceAmount: Price
    netTaxAmount: Price
    paymentStatus: str
    pickupDetails: OrderPickupDetails
    placedDate: str
    promotions: _list[OrderPromotion]
    refunds: _list[OrderRefund]
    shipments: _list[OrderShipment]
    shippingCost: Price
    shippingCostTax: Price
    status: str
    taxCollector: str

@typing.type_check_only
class OrderAddress(typing_extensions.TypedDict, total=False):
    country: str
    fullAddress: _list[str]
    isPostOfficeBox: bool
    locality: str
    postalCode: str
    recipientName: str
    region: str
    streetAddress: _list[str]

@typing.type_check_only
class OrderCancellation(typing_extensions.TypedDict, total=False):
    actor: str
    creationDate: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrderCustomer(typing_extensions.TypedDict, total=False):
    fullName: str
    invoiceReceivingEmail: str
    loyaltyInfo: OrderCustomerLoyaltyInfo
    marketingRightsInfo: OrderCustomerMarketingRightsInfo

@typing.type_check_only
class OrderCustomerLoyaltyInfo(typing_extensions.TypedDict, total=False):
    loyaltyNumber: str
    name: str

@typing.type_check_only
class OrderCustomerMarketingRightsInfo(typing_extensions.TypedDict, total=False):
    explicitMarketingPreference: str
    lastUpdatedTimestamp: str
    marketingEmailAddress: str

@typing.type_check_only
class OrderDeliveryDetails(typing_extensions.TypedDict, total=False):
    address: OrderAddress
    phoneNumber: str

@typing.type_check_only
class OrderLineItem(typing_extensions.TypedDict, total=False):
    adjustments: _list[OrderLineItemAdjustment]
    annotations: _list[OrderMerchantProvidedAnnotation]
    cancellations: _list[OrderCancellation]
    id: str
    price: Price
    product: OrderLineItemProduct
    quantityCanceled: int
    quantityDelivered: int
    quantityOrdered: int
    quantityPending: int
    quantityReadyForPickup: int
    quantityReturned: int
    quantityShipped: int
    quantityUndeliverable: int
    returnInfo: OrderLineItemReturnInfo
    returns: _list[OrderReturn]
    shippingDetails: OrderLineItemShippingDetails
    tax: Price

@typing.type_check_only
class OrderLineItemAdjustment(typing_extensions.TypedDict, total=False):
    priceAdjustment: Price
    taxAdjustment: Price
    type: str

@typing.type_check_only
class OrderLineItemProduct(typing_extensions.TypedDict, total=False):
    brand: str
    condition: str
    contentLanguage: str
    fees: _list[OrderLineItemProductFee]
    gtin: str
    id: str
    imageLink: str
    itemGroupId: str
    mpn: str
    offerId: str
    price: Price
    shownImage: str
    targetCountry: str
    title: str
    variantAttributes: _list[OrderLineItemProductVariantAttribute]

@typing.type_check_only
class OrderLineItemProductFee(typing_extensions.TypedDict, total=False):
    amount: Price
    name: str

@typing.type_check_only
class OrderLineItemProductVariantAttribute(typing_extensions.TypedDict, total=False):
    dimension: str
    value: str

@typing.type_check_only
class OrderLineItemReturnInfo(typing_extensions.TypedDict, total=False):
    daysToReturn: int
    isReturnable: bool
    policyUrl: str

@typing.type_check_only
class OrderLineItemShippingDetails(typing_extensions.TypedDict, total=False):
    deliverByDate: str
    method: OrderLineItemShippingDetailsMethod
    pickupPromiseInMinutes: int
    shipByDate: str
    type: str

@typing.type_check_only
class OrderLineItemShippingDetailsMethod(typing_extensions.TypedDict, total=False):
    carrier: str
    maxDaysInTransit: int
    methodName: str
    minDaysInTransit: int

@typing.type_check_only
class OrderMerchantProvidedAnnotation(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class OrderOrderAnnotation(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class OrderPickupDetails(typing_extensions.TypedDict, total=False):
    address: OrderAddress
    collectors: _list[OrderPickupDetailsCollector]
    locationId: str
    pickupType: str

@typing.type_check_only
class OrderPickupDetailsCollector(typing_extensions.TypedDict, total=False):
    name: str
    phoneNumber: str

@typing.type_check_only
class OrderPromotion(typing_extensions.TypedDict, total=False):
    applicableItems: _list[OrderPromotionItem]
    appliedItems: _list[OrderPromotionItem]
    endTime: str
    funder: str
    merchantPromotionId: str
    priceValue: Price
    shortTitle: str
    startTime: str
    subtype: str
    taxValue: Price
    title: str
    type: str

@typing.type_check_only
class OrderPromotionItem(typing_extensions.TypedDict, total=False):
    lineItemId: str
    offerId: str
    productId: str
    quantity: int

@typing.type_check_only
class OrderRefund(typing_extensions.TypedDict, total=False):
    actor: str
    amount: Price
    creationDate: str
    reason: str
    reasonText: str

@typing.type_check_only
class OrderReportDisbursement(typing_extensions.TypedDict, total=False):
    disbursementAmount: Price
    disbursementCreationDate: str
    disbursementDate: str
    disbursementId: str
    merchantId: str

@typing.type_check_only
class OrderReportTransaction(typing_extensions.TypedDict, total=False):
    disbursementAmount: Price
    disbursementCreationDate: str
    disbursementDate: str
    disbursementId: str
    merchantId: str
    merchantOrderId: str
    orderId: str
    productAmount: ProductAmount
    transactionDate: str

@typing.type_check_only
class OrderReturn(typing_extensions.TypedDict, total=False):
    actor: str
    creationDate: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrderShipment(typing_extensions.TypedDict, total=False):
    carrier: str
    creationDate: str
    deliveryDate: str
    id: str
    lineItems: _list[OrderShipmentLineItemShipment]
    scheduledDeliveryDetails: OrderShipmentScheduledDeliveryDetails
    shipmentGroupId: str
    status: str
    trackingId: str

@typing.type_check_only
class OrderShipmentLineItemShipment(typing_extensions.TypedDict, total=False):
    lineItemId: str
    productId: str
    quantity: int

@typing.type_check_only
class OrderShipmentScheduledDeliveryDetails(typing_extensions.TypedDict, total=False):
    carrierPhoneNumber: str
    scheduledDate: str

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
class OrderinvoicesCreateChargeInvoiceRequest(typing_extensions.TypedDict, total=False):
    invoiceId: str
    invoiceSummary: InvoiceSummary
    lineItemInvoices: _list[ShipmentInvoiceLineItemInvoice]
    operationId: str
    shipmentGroupId: str

@typing.type_check_only
class OrderinvoicesCreateChargeInvoiceResponse(
    typing_extensions.TypedDict, total=False
):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrderinvoicesCreateRefundInvoiceRequest(typing_extensions.TypedDict, total=False):
    invoiceId: str
    operationId: str
    refundOnlyOption: OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOption
    returnOption: OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOption
    shipmentInvoices: _list[ShipmentInvoice]

@typing.type_check_only
class OrderinvoicesCreateRefundInvoiceResponse(
    typing_extensions.TypedDict, total=False
):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOption(
    typing_extensions.TypedDict, total=False
):
    description: str
    reason: str

@typing.type_check_only
class OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOption(
    typing_extensions.TypedDict, total=False
):
    description: str
    reason: str

@typing.type_check_only
class OrderreportsListDisbursementsResponse(typing_extensions.TypedDict, total=False):
    disbursements: _list[OrderReportDisbursement]
    kind: str
    nextPageToken: str

@typing.type_check_only
class OrderreportsListTransactionsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    transactions: _list[OrderReportTransaction]

@typing.type_check_only
class OrderreturnsAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class OrderreturnsAcknowledgeResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrderreturnsCreateOrderReturnRequest(typing_extensions.TypedDict, total=False):
    lineItems: _list[OrderreturnsLineItem]
    operationId: str
    orderId: str
    returnMethodType: str

@typing.type_check_only
class OrderreturnsCreateOrderReturnResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str
    orderReturn: MerchantOrderReturn

@typing.type_check_only
class OrderreturnsLineItem(typing_extensions.TypedDict, total=False):
    lineItemId: str
    productId: str
    quantity: int

@typing.type_check_only
class OrderreturnsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[MerchantOrderReturn]

@typing.type_check_only
class OrderreturnsPartialRefund(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    taxAmount: Price

@typing.type_check_only
class OrderreturnsProcessRequest(typing_extensions.TypedDict, total=False):
    fullChargeReturnShippingCost: bool
    operationId: str
    refundShippingFee: OrderreturnsRefundOperation
    returnItems: _list[OrderreturnsReturnItem]

@typing.type_check_only
class OrderreturnsProcessResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrderreturnsRefundOperation(typing_extensions.TypedDict, total=False):
    fullRefund: bool
    partialRefund: OrderreturnsPartialRefund
    paymentType: str
    reasonText: str
    returnRefundReason: str

@typing.type_check_only
class OrderreturnsRejectOperation(typing_extensions.TypedDict, total=False):
    reason: str
    reasonText: str

@typing.type_check_only
class OrderreturnsReturnItem(typing_extensions.TypedDict, total=False):
    refund: OrderreturnsRefundOperation
    reject: OrderreturnsRejectOperation
    returnItemId: str

@typing.type_check_only
class OrdersAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class OrdersAcknowledgeResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersAdvanceTestOrderResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class OrdersCancelLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCancelLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersCancelRequest(typing_extensions.TypedDict, total=False):
    operationId: str
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCancelResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersCancelTestOrderByCustomerRequest(typing_extensions.TypedDict, total=False):
    reason: str

@typing.type_check_only
class OrdersCancelTestOrderByCustomerResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class OrdersCreateTestOrderRequest(typing_extensions.TypedDict, total=False):
    country: str
    templateName: str
    testOrder: TestOrder

@typing.type_check_only
class OrdersCreateTestOrderResponse(typing_extensions.TypedDict, total=False):
    kind: str
    orderId: str

@typing.type_check_only
class OrdersCreateTestReturnRequest(typing_extensions.TypedDict, total=False):
    items: _list[OrdersCustomBatchRequestEntryCreateTestReturnReturnItem]

@typing.type_check_only
class OrdersCreateTestReturnResponse(typing_extensions.TypedDict, total=False):
    kind: str
    returnId: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryCreateTestReturnReturnItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    quantity: int

@typing.type_check_only
class OrdersCustomBatchRequestEntryRefundItemItem(
    typing_extensions.TypedDict, total=False
):
    amount: MonetaryAmount
    fullRefund: bool
    lineItemId: str
    productId: str
    quantity: int

@typing.type_check_only
class OrdersCustomBatchRequestEntryRefundItemShipping(
    typing_extensions.TypedDict, total=False
):
    amount: Price
    fullRefund: bool

@typing.type_check_only
class OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    shipmentId: str
    trackingId: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetails(
    typing_extensions.TypedDict, total=False
):
    carrierPhoneNumber: str
    scheduledDate: str

@typing.type_check_only
class OrdersGetByMerchantOrderIdResponse(typing_extensions.TypedDict, total=False):
    kind: str
    order: Order

@typing.type_check_only
class OrdersGetTestOrderTemplateResponse(typing_extensions.TypedDict, total=False):
    kind: str
    template: TestOrder

@typing.type_check_only
class OrdersInStoreRefundLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    priceAmount: Price
    productId: str
    quantity: int
    reason: str
    reasonText: str
    taxAmount: Price

@typing.type_check_only
class OrdersInStoreRefundLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[Order]

@typing.type_check_only
class OrdersRefundItemRequest(typing_extensions.TypedDict, total=False):
    items: _list[OrdersCustomBatchRequestEntryRefundItemItem]
    operationId: str
    reason: str
    reasonText: str
    shipping: OrdersCustomBatchRequestEntryRefundItemShipping

@typing.type_check_only
class OrdersRefundItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersRefundOrderRequest(typing_extensions.TypedDict, total=False):
    amount: MonetaryAmount
    fullRefund: bool
    operationId: str
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersRefundOrderResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersRejectReturnLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersRejectReturnLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersReturnRefundLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    priceAmount: Price
    productId: str
    quantity: int
    reason: str
    reasonText: str
    taxAmount: Price

@typing.type_check_only
class OrdersReturnRefundLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersSetLineItemMetadataRequest(typing_extensions.TypedDict, total=False):
    annotations: _list[OrderMerchantProvidedAnnotation]
    lineItemId: str
    operationId: str
    productId: str

@typing.type_check_only
class OrdersSetLineItemMetadataResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersShipLineItemsRequest(typing_extensions.TypedDict, total=False):
    lineItems: _list[OrderShipmentLineItemShipment]
    operationId: str
    shipmentGroupId: str
    shipmentInfos: _list[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]

@typing.type_check_only
class OrdersShipLineItemsResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersUpdateLineItemShippingDetailsRequest(
    typing_extensions.TypedDict, total=False
):
    deliverByDate: str
    lineItemId: str
    operationId: str
    productId: str
    shipByDate: str

@typing.type_check_only
class OrdersUpdateLineItemShippingDetailsResponse(
    typing_extensions.TypedDict, total=False
):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersUpdateMerchantOrderIdRequest(typing_extensions.TypedDict, total=False):
    merchantOrderId: str
    operationId: str

@typing.type_check_only
class OrdersUpdateMerchantOrderIdResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersUpdateShipmentRequest(typing_extensions.TypedDict, total=False):
    carrier: str
    deliveryDate: str
    lastPickupDate: str
    operationId: str
    readyPickupDate: str
    scheduledDeliveryDetails: OrdersCustomBatchRequestEntryUpdateShipmentScheduledDeliveryDetails
    shipmentId: str
    status: str
    trackingId: str
    undeliveredDate: str

@typing.type_check_only
class OrdersUpdateShipmentResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class PauseBuyOnGoogleProgramRequest(typing_extensions.TypedDict, total=False): ...

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
class Product(typing_extensions.TypedDict, total=False):
    additionalImageLinks: _list[str]
    additionalSizeType: str
    adsGrouping: str
    adsLabels: _list[str]
    adsRedirect: str
    adult: bool
    ageGroup: str
    availability: str
    availabilityDate: str
    brand: str
    canonicalLink: str
    channel: str
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
    link: str
    linkTemplate: str
    loyaltyPoints: LoyaltyPoints
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
    subscriptionCost: ProductSubscriptionCost
    targetCountry: str
    taxCategory: str
    taxes: _list[ProductTax]
    title: str
    transitTimeLabel: str
    unitPricingBaseMeasure: ProductUnitPricingBaseMeasure
    unitPricingMeasure: ProductUnitPricingMeasure

@typing.type_check_only
class ProductAmount(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    remittedTaxAmount: Price
    taxAmount: Price

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
class ProductSubscriptionCost(typing_extensions.TypedDict, total=False):
    amount: Price
    period: str
    periodLength: str

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
    channel: typing_extensions.Literal["CHANNEL_UNSPECIFIED", "LOCAL", "ONLINE"]
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

@typing.type_check_only
class ProductWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[ProductsCustomBatchRequestEntry]

@typing.type_check_only
class ProductsCustomBatchRequestEntry(dict[str, typing.Any]): ...

@typing.type_check_only
class ProductsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[ProductsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ProductsCustomBatchResponseEntry(dict[str, typing.Any]): ...

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
    redemptionChannel: _list[str]
    shippingServiceNames: _list[str]
    targetCountry: str

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
class RefundReason(typing_extensions.TypedDict, total=False):
    description: str
    reasonCode: str

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
class RegionalinventoryCustomBatchRequestEntry(dict[str, typing.Any]): ...

@typing.type_check_only
class RegionalinventoryCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[RegionalinventoryCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class RegionalinventoryCustomBatchResponseEntry(dict[str, typing.Any]): ...

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
    metrics: Metrics
    productView: ProductView
    segments: Segments

@typing.type_check_only
class RepricingProductReport(typing_extensions.TypedDict, total=False):
    applicationCount: str
    buyboxWinningProductStats: RepricingProductReportBuyboxWinningProductStats
    date: Date
    highWatermark: PriceAmount
    inapplicabilityDetails: _list[InapplicabilityDetails]
    lowWatermark: PriceAmount
    orderItemCount: int
    ruleIds: _list[str]
    totalGmv: PriceAmount
    type: typing_extensions.Literal[
        "REPRICING_RULE_TYPE_UNSPECIFIED",
        "TYPE_STATS_BASED",
        "TYPE_COGS_BASED",
        "TYPE_SALES_VOLUME_BASED",
        "TYPE_COMPETITIVE_PRICE",
    ]

@typing.type_check_only
class RepricingProductReportBuyboxWinningProductStats(
    typing_extensions.TypedDict, total=False
):
    buyboxWinsCount: int

@typing.type_check_only
class RepricingRule(typing_extensions.TypedDict, total=False):
    cogsBasedRule: RepricingRuleCostOfGoodsSaleRule
    countryCode: str
    effectiveTimePeriod: RepricingRuleEffectiveTime
    eligibleOfferMatcher: RepricingRuleEligibleOfferMatcher
    languageCode: str
    merchantId: str
    paused: bool
    restriction: RepricingRuleRestriction
    ruleId: str
    statsBasedRule: RepricingRuleStatsBasedRule
    title: str
    type: typing_extensions.Literal[
        "REPRICING_RULE_TYPE_UNSPECIFIED",
        "TYPE_STATS_BASED",
        "TYPE_COGS_BASED",
        "TYPE_SALES_VOLUME_BASED",
        "TYPE_COMPETITIVE_PRICE",
    ]

@typing.type_check_only
class RepricingRuleCostOfGoodsSaleRule(typing_extensions.TypedDict, total=False):
    percentageDelta: int
    priceDelta: str

@typing.type_check_only
class RepricingRuleEffectiveTime(typing_extensions.TypedDict, total=False):
    fixedTimePeriods: _list[RepricingRuleEffectiveTimeFixedTimePeriod]

@typing.type_check_only
class RepricingRuleEffectiveTimeFixedTimePeriod(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class RepricingRuleEligibleOfferMatcher(typing_extensions.TypedDict, total=False):
    brandMatcher: RepricingRuleEligibleOfferMatcherStringMatcher
    itemGroupIdMatcher: RepricingRuleEligibleOfferMatcherStringMatcher
    matcherOption: typing_extensions.Literal[
        "MATCHER_OPTION_UNSPECIFIED",
        "MATCHER_OPTION_CUSTOM_FILTER",
        "MATCHER_OPTION_USE_FEED_ATTRIBUTE",
        "MATCHER_OPTION_ALL_PRODUCTS",
    ]
    offerIdMatcher: RepricingRuleEligibleOfferMatcherStringMatcher
    skipWhenOnPromotion: bool

@typing.type_check_only
class RepricingRuleEligibleOfferMatcherStringMatcher(
    typing_extensions.TypedDict, total=False
):
    strAttributes: _list[str]

@typing.type_check_only
class RepricingRuleReport(typing_extensions.TypedDict, total=False):
    buyboxWinningRuleStats: RepricingRuleReportBuyboxWinningRuleStats
    date: Date
    impactedProducts: _list[str]
    inapplicabilityDetails: _list[InapplicabilityDetails]
    inapplicableProducts: _list[str]
    orderItemCount: int
    ruleId: str
    totalGmv: PriceAmount
    type: typing_extensions.Literal[
        "REPRICING_RULE_TYPE_UNSPECIFIED",
        "TYPE_STATS_BASED",
        "TYPE_COGS_BASED",
        "TYPE_SALES_VOLUME_BASED",
        "TYPE_COMPETITIVE_PRICE",
    ]

@typing.type_check_only
class RepricingRuleReportBuyboxWinningRuleStats(
    typing_extensions.TypedDict, total=False
):
    buyboxWonProductCount: int

@typing.type_check_only
class RepricingRuleRestriction(typing_extensions.TypedDict, total=False):
    floor: RepricingRuleRestrictionBoundary
    useAutoPricingMinPrice: bool

@typing.type_check_only
class RepricingRuleRestrictionBoundary(typing_extensions.TypedDict, total=False):
    percentageDelta: int
    priceDelta: str

@typing.type_check_only
class RepricingRuleStatsBasedRule(typing_extensions.TypedDict, total=False):
    percentageDelta: int
    priceDelta: str

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
class RequestReviewBuyOnGoogleProgramRequest(
    typing_extensions.TypedDict, total=False
): ...

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
    itemConditions: _list[str]
    label: str
    name: str
    policy: ReturnPolicyOnlinePolicy
    restockingFee: ReturnPolicyOnlineRestockingFee
    returnMethods: _list[str]
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
class ReturnPricingInfo(typing_extensions.TypedDict, total=False):
    chargeReturnShippingFee: bool
    maxReturnShippingFee: MonetaryAmount
    refundableItemsTotalAmount: MonetaryAmount
    refundableShippingAmount: MonetaryAmount
    totalRefundedAmount: MonetaryAmount

@typing.type_check_only
class ReturnShipment(typing_extensions.TypedDict, total=False):
    creationDate: str
    deliveryDate: str
    returnMethodType: str
    shipmentId: str
    shipmentTrackingInfos: _list[ShipmentTrackingInfo]
    shippingDate: str
    state: str

@typing.type_check_only
class ReturnShippingLabel(typing_extensions.TypedDict, total=False):
    carrier: str
    labelUri: str
    trackingId: str

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

@typing.type_check_only
class SettlementReport(typing_extensions.TypedDict, total=False):
    endDate: str
    kind: str
    previousBalance: Price
    settlementId: str
    startDate: str
    transferAmount: Price
    transferDate: str
    transferIds: _list[str]

@typing.type_check_only
class SettlementTransaction(typing_extensions.TypedDict, total=False):
    amount: SettlementTransactionAmount
    identifiers: SettlementTransactionIdentifiers
    kind: str
    transaction: SettlementTransactionTransaction

@typing.type_check_only
class SettlementTransactionAmount(typing_extensions.TypedDict, total=False):
    commission: SettlementTransactionAmountCommission
    description: str
    transactionAmount: Price
    type: str

@typing.type_check_only
class SettlementTransactionAmountCommission(typing_extensions.TypedDict, total=False):
    category: str
    rate: str

@typing.type_check_only
class SettlementTransactionIdentifiers(typing_extensions.TypedDict, total=False):
    adjustmentId: str
    merchantOrderId: str
    orderItemId: str
    settlementEntryId: str
    shipmentIds: _list[str]
    transactionId: str

@typing.type_check_only
class SettlementTransactionTransaction(typing_extensions.TypedDict, total=False):
    postDate: str
    type: str

@typing.type_check_only
class SettlementreportsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[SettlementReport]

@typing.type_check_only
class SettlementtransactionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[SettlementTransaction]

@typing.type_check_only
class ShipmentInvoice(typing_extensions.TypedDict, total=False):
    invoiceSummary: InvoiceSummary
    lineItemInvoices: _list[ShipmentInvoiceLineItemInvoice]
    shipmentGroupId: str

@typing.type_check_only
class ShipmentInvoiceLineItemInvoice(typing_extensions.TypedDict, total=False):
    lineItemId: str
    productId: str
    shipmentUnitIds: _list[str]
    unitInvoice: UnitInvoice

@typing.type_check_only
class ShipmentTrackingInfo(typing_extensions.TypedDict, total=False):
    carrier: str
    trackingNumber: str

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
    reviewIneligibilityReasonDetails: ShoppingAdsProgramStatusReviewIneligibilityReasonDetails
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
class TestOrder(typing_extensions.TypedDict, total=False):
    deliveryDetails: TestOrderDeliveryDetails
    enableOrderinvoices: bool
    kind: str
    lineItems: _list[TestOrderLineItem]
    notificationMode: str
    pickupDetails: TestOrderPickupDetails
    predefinedBillingAddress: str
    predefinedDeliveryAddress: str
    predefinedEmail: str
    predefinedPickupDetails: str
    promotions: _list[OrderPromotion]
    shippingCost: Price
    shippingOption: str

@typing.type_check_only
class TestOrderAddress(typing_extensions.TypedDict, total=False):
    country: str
    fullAddress: _list[str]
    isPostOfficeBox: bool
    locality: str
    postalCode: str
    recipientName: str
    region: str
    streetAddress: _list[str]

@typing.type_check_only
class TestOrderDeliveryDetails(typing_extensions.TypedDict, total=False):
    address: TestOrderAddress
    isScheduledDelivery: bool
    phoneNumber: str

@typing.type_check_only
class TestOrderLineItem(typing_extensions.TypedDict, total=False):
    product: TestOrderLineItemProduct
    quantityOrdered: int
    returnInfo: OrderLineItemReturnInfo
    shippingDetails: OrderLineItemShippingDetails

@typing.type_check_only
class TestOrderLineItemProduct(typing_extensions.TypedDict, total=False):
    brand: str
    condition: str
    contentLanguage: str
    fees: _list[OrderLineItemProductFee]
    gtin: str
    imageLink: str
    itemGroupId: str
    mpn: str
    offerId: str
    price: Price
    targetCountry: str
    title: str
    variantAttributes: _list[OrderLineItemProductVariantAttribute]

@typing.type_check_only
class TestOrderPickupDetails(typing_extensions.TypedDict, total=False):
    locationCode: str
    pickupLocationAddress: TestOrderAddress
    pickupLocationType: str
    pickupPersons: _list[TestOrderPickupDetailsPickupPerson]

@typing.type_check_only
class TestOrderPickupDetailsPickupPerson(typing_extensions.TypedDict, total=False):
    name: str
    phoneNumber: str

@typing.type_check_only
class TimePeriod(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

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
class UnitInvoice(typing_extensions.TypedDict, total=False):
    additionalCharges: _list[UnitInvoiceAdditionalCharge]
    unitPrice: Price
    unitPriceTaxes: _list[UnitInvoiceTaxLine]

@typing.type_check_only
class UnitInvoiceAdditionalCharge(typing_extensions.TypedDict, total=False):
    additionalChargeAmount: Amount
    type: str

@typing.type_check_only
class UnitInvoiceTaxLine(typing_extensions.TypedDict, total=False):
    taxAmount: Price
    taxName: str
    taxType: str

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
