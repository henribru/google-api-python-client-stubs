import typing

import typing_extensions
@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    adsLinks: typing.List[AccountAdsLink]
    adultContent: bool
    automaticLabelIds: typing.List[str]
    businessInformation: AccountBusinessInformation
    cssId: str
    googleMyBusinessLink: AccountGoogleMyBusinessLink
    id: str
    kind: str
    labelIds: typing.List[str]
    name: str
    sellerId: str
    users: typing.List[AccountUser]
    websiteUrl: str
    youtubeChannelLinks: typing.List[AccountYouTubeChannelLink]

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
class AccountBusinessInformation(typing_extensions.TypedDict, total=False):
    address: AccountAddress
    customerService: AccountCustomerService
    phoneNumber: str

@typing.type_check_only
class AccountCredentials(typing_extensions.TypedDict, total=False):
    accessToken: str
    expiresIn: str
    purpose: typing_extensions.Literal[
        "ACCOUNT_CREDENTIALS_PURPOSE_UNSPECIFIED", "SHOPIFY_ORDER_MANAGEMENT"
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
class AccountStatus(typing_extensions.TypedDict, total=False):
    accountId: str
    accountLevelIssues: typing.List[AccountStatusAccountLevelIssue]
    kind: str
    products: typing.List[AccountStatusProducts]
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
    itemLevelIssues: typing.List[AccountStatusItemLevelIssue]
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
    rules: typing.List[AccountTaxTaxRule]

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

@typing.type_check_only
class AccountYouTubeChannelLink(typing_extensions.TypedDict, total=False):
    channelId: str
    status: str

@typing.type_check_only
class AccountsAuthInfoResponse(typing_extensions.TypedDict, total=False):
    accountIdentifiers: typing.List[AccountIdentifier]
    kind: str

@typing.type_check_only
class AccountsClaimWebsiteResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountsCustomBatchRequestEntry]

@typing.type_check_only
class AccountsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    account: Account
    accountId: str
    batchId: int
    force: bool
    labelIds: typing.List[str]
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
    services: typing.List[str]

@typing.type_check_only
class AccountsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountsCustomBatchResponseEntry]
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
    linkType: str
    linkedAccountId: str
    services: typing.List[str]

@typing.type_check_only
class AccountsLinkResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountsListLinksResponse(typing_extensions.TypedDict, total=False):
    kind: str
    links: typing.List[LinkedAccount]
    nextPageToken: str

@typing.type_check_only
class AccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[Account]

@typing.type_check_only
class AccountsUpdateLabelsRequest(typing_extensions.TypedDict, total=False):
    labelIds: typing.List[str]

@typing.type_check_only
class AccountsUpdateLabelsResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountstatusesCustomBatchRequestEntry]

@typing.type_check_only
class AccountstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    destinations: typing.List[str]
    merchantId: str
    method: str

@typing.type_check_only
class AccountstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountstatusesCustomBatchResponseEntry]
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
    resources: typing.List[AccountStatus]

@typing.type_check_only
class AccounttaxCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccounttaxCustomBatchRequestEntry]

@typing.type_check_only
class AccounttaxCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    accountTax: AccountTax
    batchId: int
    merchantId: str
    method: str

@typing.type_check_only
class AccounttaxCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccounttaxCustomBatchResponseEntry]
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
    resources: typing.List[AccountTax]

@typing.type_check_only
class Amount(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    taxAmount: Price

@typing.type_check_only
class BusinessDayConfig(typing_extensions.TypedDict, total=False):
    businessDays: typing.List[str]

@typing.type_check_only
class BuyOnGoogleProgramStatus(typing_extensions.TypedDict, total=False):
    customerServicePendingEmail: str
    customerServiceVerifiedEmail: str
    participationStage: typing_extensions.Literal[
        "PROGRAM_PARTICIPATION_STAGE_UNSPECIFIED",
        "NOT_ELIGIBLE",
        "ELIGIBLE",
        "ONBOARDING",
        "ACTIVE",
        "PAUSED",
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
    name: str
    services: typing.List[str]

@typing.type_check_only
class Collection(typing_extensions.TypedDict, total=False):
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    featuredProduct: typing.List[CollectionFeaturedProduct]
    headline: typing.List[str]
    id: str
    imageLink: typing.List[str]
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
    collectionLevelIssuses: typing.List[CollectionStatusItemLevelIssue]
    creationDate: str
    destinationStatuses: typing.List[CollectionStatusDestinationStatus]
    id: str
    lastUpdateDate: str

@typing.type_check_only
class CollectionStatusDestinationStatus(typing_extensions.TypedDict, total=False):
    destination: str
    status: str

@typing.type_check_only
class CollectionStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
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
    labelIds: typing.List[str]

@typing.type_check_only
class CustomAttribute(typing.Dict[str, typing.Any]): ...

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
    targets: typing.List[DatafeedTarget]

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
    errors: typing.List[DatafeedStatusError]
    itemsTotal: str
    itemsValid: str
    kind: str
    language: str
    lastUploadDate: str
    processingStatus: str
    warnings: typing.List[DatafeedStatusError]

@typing.type_check_only
class DatafeedStatusError(typing_extensions.TypedDict, total=False):
    code: str
    count: str
    examples: typing.List[DatafeedStatusExample]
    message: str

@typing.type_check_only
class DatafeedStatusExample(typing_extensions.TypedDict, total=False):
    itemId: str
    lineNumber: str
    value: str

@typing.type_check_only
class DatafeedTarget(typing_extensions.TypedDict, total=False):
    country: str
    excludedDestinations: typing.List[str]
    includedDestinations: typing.List[str]
    language: str

@typing.type_check_only
class DatafeedsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedsCustomBatchRequestEntry]

@typing.type_check_only
class DatafeedsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    datafeed: Datafeed
    datafeedId: str
    merchantId: str
    method: str

@typing.type_check_only
class DatafeedsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedsCustomBatchResponseEntry]
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
    resources: typing.List[Datafeed]

@typing.type_check_only
class DatafeedstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedstatusesCustomBatchRequestEntry]

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
    entries: typing.List[DatafeedstatusesCustomBatchResponseEntry]
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
    resources: typing.List[DatafeedStatus]

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
class DeliveryTime(typing_extensions.TypedDict, total=False):
    cutoffTime: CutoffTime
    handlingBusinessDayConfig: BusinessDayConfig
    holidayCutoffs: typing.List[HolidayCutoff]
    maxHandlingTimeInDays: int
    maxTransitTimeInDays: int
    minHandlingTimeInDays: int
    minTransitTimeInDays: int
    transitBusinessDayConfig: BusinessDayConfig
    transitTimeTable: TransitTable

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    domain: str
    message: str
    reason: str

@typing.type_check_only
class Errors(typing_extensions.TypedDict, total=False):
    code: int
    errors: typing.List[Error]
    message: str

@typing.type_check_only
class GmbAccounts(typing_extensions.TypedDict, total=False):
    accountId: str
    gmbAccounts: typing.List[GmbAccountsGmbAccount]

@typing.type_check_only
class GmbAccountsGmbAccount(typing_extensions.TypedDict, total=False):
    email: str
    listingCount: str
    name: str
    type: str

@typing.type_check_only
class Headers(typing_extensions.TypedDict, total=False):
    locations: typing.List[LocationIdSet]
    numberOfItems: typing.List[str]
    postalCodeGroupNames: typing.List[str]
    prices: typing.List[Price]
    weights: typing.List[Weight]

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
    ]

@typing.type_check_only
class Installment(typing_extensions.TypedDict, total=False):
    amount: Price
    months: str

@typing.type_check_only
class InvoiceSummary(typing_extensions.TypedDict, total=False):
    additionalChargeSummaries: typing.List[InvoiceSummaryAdditionalChargeSummary]
    productTotal: Amount

@typing.type_check_only
class InvoiceSummaryAdditionalChargeSummary(typing_extensions.TypedDict, total=False):
    totalAmount: Amount
    type: str

@typing.type_check_only
class LabelIds(typing_extensions.TypedDict, total=False):
    labelIds: typing.List[str]

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
    countrySettings: typing.List[LiaCountrySettings]
    kind: str

@typing.type_check_only
class LiasettingsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[LiasettingsCustomBatchRequestEntry]

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
    entries: typing.List[LiasettingsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class LiasettingsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    gmbAccounts: GmbAccounts
    kind: str
    liaSettings: LiaSettings
    posDataProviders: typing.List[PosDataProviders]

@typing.type_check_only
class LiasettingsGetAccessibleGmbAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    gmbAccounts: typing.List[GmbAccountsGmbAccount]
    kind: str

@typing.type_check_only
class LiasettingsListPosDataProvidersResponse(typing_extensions.TypedDict, total=False):
    kind: str
    posDataProviders: typing.List[PosDataProviders]

@typing.type_check_only
class LiasettingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[LiaSettings]

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
    services: typing.List[LinkService]

@typing.type_check_only
class ListAccountLabelsResponse(typing_extensions.TypedDict, total=False):
    accountLabels: typing.List[AccountLabel]
    nextPageToken: str

@typing.type_check_only
class ListAccountReturnCarrierResponse(typing_extensions.TypedDict, total=False):
    accountReturnCarriers: typing.List[AccountReturnCarrier]

@typing.type_check_only
class ListCollectionStatusesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[CollectionStatus]

@typing.type_check_only
class ListCollectionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Collection]

@typing.type_check_only
class ListCssesResponse(typing_extensions.TypedDict, total=False):
    csses: typing.List[Css]
    nextPageToken: str

@typing.type_check_only
class ListRegionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    regions: typing.List[Region]

@typing.type_check_only
class ListRepricingProductReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repricingProductReports: typing.List[RepricingProductReport]

@typing.type_check_only
class ListRepricingRuleReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repricingRuleReports: typing.List[RepricingRuleReport]

@typing.type_check_only
class ListRepricingRulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repricingRules: typing.List[RepricingRule]

@typing.type_check_only
class ListReturnPolicyOnlineResponse(typing_extensions.TypedDict, total=False):
    returnPolicies: typing.List[ReturnPolicyOnline]

@typing.type_check_only
class LocalInventory(typing_extensions.TypedDict, total=False):
    availability: str
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
    entries: typing.List[LocalinventoryCustomBatchRequestEntry]

@typing.type_check_only
class LocalinventoryCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    localInventory: LocalInventory
    merchantId: str
    method: str
    productId: str

@typing.type_check_only
class LocalinventoryCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[LocalinventoryCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class LocalinventoryCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str

@typing.type_check_only
class LocationIdSet(typing_extensions.TypedDict, total=False):
    locationIds: typing.List[str]

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
    returnItems: typing.List[MerchantOrderReturnItem]
    returnPricingInfo: ReturnPricingInfo
    returnShipments: typing.List[ReturnShipment]

@typing.type_check_only
class MerchantOrderReturnItem(typing_extensions.TypedDict, total=False):
    customerReturnReason: CustomerReturnReason
    itemId: str
    merchantRejectionReason: MerchantRejectionReason
    merchantReturnReason: RefundReason
    product: OrderLineItemProduct
    refundableAmount: MonetaryAmount
    returnItemId: str
    returnShipmentIds: typing.List[str]
    shipmentGroupId: str
    shipmentUnitId: str
    state: str

@typing.type_check_only
class MerchantRejectionReason(typing_extensions.TypedDict, total=False):
    description: str
    reasonCode: str

@typing.type_check_only
class Metrics(typing_extensions.TypedDict, total=False):
    clicks: str
    ctr: float
    impressions: str

@typing.type_check_only
class MinimumOrderValueTable(typing_extensions.TypedDict, total=False):
    storeCodeSetWithMovs: typing.List[MinimumOrderValueTableStoreCodeSetWithMov]

@typing.type_check_only
class MinimumOrderValueTableStoreCodeSetWithMov(
    typing_extensions.TypedDict, total=False
):
    storeCodes: typing.List[str]
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
    annotations: typing.List[OrderOrderAnnotation]
    billingAddress: OrderAddress
    customer: OrderCustomer
    deliveryDetails: OrderDeliveryDetails
    id: str
    kind: str
    lineItems: typing.List[OrderLineItem]
    merchantId: str
    merchantOrderId: str
    netPriceAmount: Price
    netTaxAmount: Price
    paymentStatus: str
    pickupDetails: OrderPickupDetails
    placedDate: str
    promotions: typing.List[OrderPromotion]
    refunds: typing.List[OrderRefund]
    shipments: typing.List[OrderShipment]
    shippingCost: Price
    shippingCostTax: Price
    status: str
    taxCollector: str

@typing.type_check_only
class OrderAddress(typing_extensions.TypedDict, total=False):
    country: str
    fullAddress: typing.List[str]
    isPostOfficeBox: bool
    locality: str
    postalCode: str
    recipientName: str
    region: str
    streetAddress: typing.List[str]

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
    adjustments: typing.List[OrderLineItemAdjustment]
    annotations: typing.List[OrderMerchantProvidedAnnotation]
    cancellations: typing.List[OrderCancellation]
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
    returns: typing.List[OrderReturn]
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
    fees: typing.List[OrderLineItemProductFee]
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
    variantAttributes: typing.List[OrderLineItemProductVariantAttribute]

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
    collectors: typing.List[OrderPickupDetailsCollector]
    locationId: str
    pickupType: str

@typing.type_check_only
class OrderPickupDetailsCollector(typing_extensions.TypedDict, total=False):
    name: str
    phoneNumber: str

@typing.type_check_only
class OrderPromotion(typing_extensions.TypedDict, total=False):
    applicableItems: typing.List[OrderPromotionItem]
    appliedItems: typing.List[OrderPromotionItem]
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
    lineItems: typing.List[OrderShipmentLineItemShipment]
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
    lineItems: typing.List[OrderTrackingSignalLineItemDetails]
    merchantId: str
    orderCreatedTime: DateTime
    orderId: str
    orderTrackingSignalId: str
    shipmentLineItemMapping: typing.List[OrderTrackingSignalShipmentLineItemMapping]
    shippingInfo: typing.List[OrderTrackingSignalShippingInfo]

@typing.type_check_only
class OrderTrackingSignalLineItemDetails(typing_extensions.TypedDict, total=False):
    gtin: str
    lineItemId: str
    mpn: str
    productId: str
    quantity: str

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
    lineItemInvoices: typing.List[ShipmentInvoiceLineItemInvoice]
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
    shipmentInvoices: typing.List[ShipmentInvoice]

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
    disbursements: typing.List[OrderReportDisbursement]
    kind: str
    nextPageToken: str

@typing.type_check_only
class OrderreportsListTransactionsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    transactions: typing.List[OrderReportTransaction]

@typing.type_check_only
class OrderreturnsAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class OrderreturnsAcknowledgeResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrderreturnsCreateOrderReturnRequest(typing_extensions.TypedDict, total=False):
    lineItems: typing.List[OrderreturnsLineItem]
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
    quantity: int

@typing.type_check_only
class OrderreturnsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[MerchantOrderReturn]

@typing.type_check_only
class OrderreturnsPartialRefund(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    taxAmount: Price

@typing.type_check_only
class OrderreturnsProcessRequest(typing_extensions.TypedDict, total=False):
    fullChargeReturnShippingCost: bool
    operationId: str
    refundShippingFee: OrderreturnsRefundOperation
    returnItems: typing.List[OrderreturnsReturnItem]

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
    items: typing.List[OrdersCustomBatchRequestEntryCreateTestReturnReturnItem]

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
    resources: typing.List[Order]

@typing.type_check_only
class OrdersRefundItemRequest(typing_extensions.TypedDict, total=False):
    items: typing.List[OrdersCustomBatchRequestEntryRefundItemItem]
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
    annotations: typing.List[OrderMerchantProvidedAnnotation]
    lineItemId: str
    operationId: str
    productId: str

@typing.type_check_only
class OrdersSetLineItemMetadataResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersShipLineItemsRequest(typing_extensions.TypedDict, total=False):
    lineItems: typing.List[OrderShipmentLineItemShipment]
    operationId: str
    shipmentGroupId: str
    shipmentInfos: typing.List[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]

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
    entries: typing.List[PosCustomBatchRequestEntry]

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
    entries: typing.List[PosCustomBatchResponseEntry]
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
    posDataProviders: typing.List[PosDataProvidersPosDataProvider]

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
    resources: typing.List[PosStore]

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
    kind: str
    storeAddress: str
    storeCode: str

@typing.type_check_only
class PostalCodeGroup(typing_extensions.TypedDict, total=False):
    country: str
    name: str
    postalCodeRanges: typing.List[PostalCodeRange]

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
    additionalImageLinks: typing.List[str]
    adsGrouping: str
    adsLabels: typing.List[str]
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
    customAttributes: typing.List[CustomAttribute]
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    description: str
    displayAdsId: str
    displayAdsLink: str
    displayAdsSimilarIds: typing.List[str]
    displayAdsTitle: str
    displayAdsValue: float
    energyEfficiencyClass: str
    excludedDestinations: typing.List[str]
    expirationDate: str
    gender: str
    googleProductCategory: str
    gtin: str
    id: str
    identifierExists: bool
    imageLink: str
    includedDestinations: typing.List[str]
    installment: Installment
    isBundle: bool
    itemGroupId: str
    kind: str
    link: str
    loyaltyPoints: LoyaltyPoints
    material: str
    maxEnergyEfficiencyClass: str
    maxHandlingTime: str
    minEnergyEfficiencyClass: str
    minHandlingTime: str
    mobileLink: str
    mpn: str
    multipack: str
    offerId: str
    pattern: str
    price: Price
    productDetails: typing.List[ProductProductDetail]
    productHighlights: typing.List[str]
    productTypes: typing.List[str]
    promotionIds: typing.List[str]
    salePrice: Price
    salePriceEffectiveDate: str
    sellOnGoogleQuantity: str
    shipping: typing.List[ProductShipping]
    shippingHeight: ProductShippingDimension
    shippingLabel: str
    shippingLength: ProductShippingDimension
    shippingWeight: ProductShippingWeight
    shippingWidth: ProductShippingDimension
    shoppingAdsExcludedCountries: typing.List[str]
    sizeSystem: str
    sizeType: str
    sizes: typing.List[str]
    source: str
    subscriptionCost: ProductSubscriptionCost
    targetCountry: str
    taxCategory: str
    taxes: typing.List[ProductTax]
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
class ProductProductDetail(typing_extensions.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

@typing.type_check_only
class ProductShipping(typing_extensions.TypedDict, total=False):
    country: str
    locationGroupName: str
    locationId: str
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
    destinationStatuses: typing.List[ProductStatusDestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: typing.List[ProductStatusItemLevelIssue]
    kind: str
    lastUpdateDate: str
    link: str
    productId: str
    title: str

@typing.type_check_only
class ProductStatusDestinationStatus(typing_extensions.TypedDict, total=False):
    approvedCountries: typing.List[str]
    destination: str
    disapprovedCountries: typing.List[str]
    pendingCountries: typing.List[str]
    status: str

@typing.type_check_only
class ProductStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    applicableCountries: typing.List[str]
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
class ProductsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductsCustomBatchRequestEntry]

@typing.type_check_only
class ProductsCustomBatchRequestEntry(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ProductsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductsCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class ProductsCustomBatchResponseEntry(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ProductsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[Product]

@typing.type_check_only
class ProductstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductstatusesCustomBatchRequestEntry]

@typing.type_check_only
class ProductstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    destinations: typing.List[str]
    includeAttributes: bool
    merchantId: str
    method: str
    productId: str

@typing.type_check_only
class ProductstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductstatusesCustomBatchResponseEntry]
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
    resources: typing.List[ProductStatus]

@typing.type_check_only
class PubsubNotificationSettings(typing_extensions.TypedDict, total=False):
    cloudTopicName: str
    kind: str
    registeredEvents: typing.List[str]

@typing.type_check_only
class RateGroup(typing_extensions.TypedDict, total=False):
    applicableShippingLabels: typing.List[str]
    carrierRates: typing.List[CarrierRate]
    mainTable: Table
    name: str
    singleValue: Value
    subtables: typing.List[Table]

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
    geotargetCriteriaIds: typing.List[str]

@typing.type_check_only
class RegionPostalCodeArea(typing_extensions.TypedDict, total=False):
    postalCodes: typing.List[RegionPostalCodeAreaPostalCodeRange]
    regionCode: str

@typing.type_check_only
class RegionPostalCodeAreaPostalCodeRange(typing_extensions.TypedDict, total=False):
    begin: str
    end: str

@typing.type_check_only
class RegionalInventory(typing_extensions.TypedDict, total=False):
    availability: str
    customAttributes: typing.List[CustomAttribute]
    kind: str
    price: Price
    regionId: str
    salePrice: Price
    salePriceEffectiveDate: str

@typing.type_check_only
class RegionalinventoryCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[RegionalinventoryCustomBatchRequestEntry]

@typing.type_check_only
class RegionalinventoryCustomBatchRequestEntry(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class RegionalinventoryCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[RegionalinventoryCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class RegionalinventoryCustomBatchResponseEntry(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ReportRow(typing_extensions.TypedDict, total=False):
    metrics: Metrics
    segments: Segments

@typing.type_check_only
class RepricingProductReport(typing_extensions.TypedDict, total=False):
    applicationCount: str
    buyboxWinningProductStats: RepricingProductReportBuyboxWinningProductStats
    date: Date
    highWatermark: PriceAmount
    inapplicabilityDetails: typing.List[InapplicabilityDetails]
    lowWatermark: PriceAmount
    orderItemCount: int
    ruleIds: typing.List[str]
    totalGmv: PriceAmount
    type: typing_extensions.Literal[
        "REPRICING_RULE_TYPE_UNSPECIFIED", "TYPE_STATS_BASED", "TYPE_COGS_BASED"
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
        "REPRICING_RULE_TYPE_UNSPECIFIED", "TYPE_STATS_BASED", "TYPE_COGS_BASED"
    ]

@typing.type_check_only
class RepricingRuleCostOfGoodsSaleRule(typing_extensions.TypedDict, total=False):
    percentageDelta: int
    priceDelta: str

@typing.type_check_only
class RepricingRuleEffectiveTime(typing_extensions.TypedDict, total=False):
    fixedTimePeriods: typing.List[RepricingRuleEffectiveTimeFixedTimePeriod]

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
    strAttributes: typing.List[str]

@typing.type_check_only
class RepricingRuleReport(typing_extensions.TypedDict, total=False):
    buyboxWinningRuleStats: RepricingRuleReportBuyboxWinningRuleStats
    date: Date
    impactedProducts: typing.List[str]
    inapplicabilityDetails: typing.List[InapplicabilityDetails]
    inapplicableProducts: typing.List[str]
    orderItemCount: int
    ruleId: str
    totalGmv: PriceAmount
    type: typing_extensions.Literal[
        "REPRICING_RULE_TYPE_UNSPECIFIED", "TYPE_STATS_BASED", "TYPE_COGS_BASED"
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
    streetAddress: typing.List[str]

@typing.type_check_only
class ReturnPolicy(typing_extensions.TypedDict, total=False):
    country: str
    kind: str
    label: str
    name: str
    nonFreeReturnReasons: typing.List[str]
    policy: ReturnPolicyPolicy
    returnPolicyId: str
    returnShippingFee: Price
    seasonalOverrides: typing.List[ReturnPolicySeasonalOverride]

@typing.type_check_only
class ReturnPolicyOnline(typing_extensions.TypedDict, total=False):
    countries: typing.List[str]
    itemConditions: typing.List[str]
    label: str
    name: str
    policy: ReturnPolicyOnlinePolicy
    restockingFee: ReturnPolicyOnlineRestockingFee
    returnMethods: typing.List[str]
    returnPolicyId: str
    returnPolicyUri: str
    returnReasonCategoryInfo: typing.List[ReturnPolicyOnlineReturnReasonCategoryInfo]

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
    shipmentTrackingInfos: typing.List[ShipmentTrackingInfo]
    shippingDate: str
    state: str

@typing.type_check_only
class ReturnaddressCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ReturnaddressCustomBatchRequestEntry]

@typing.type_check_only
class ReturnaddressCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    merchantId: str
    method: str
    returnAddress: ReturnAddress
    returnAddressId: str

@typing.type_check_only
class ReturnaddressCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ReturnaddressCustomBatchResponseEntry]
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
    resources: typing.List[ReturnAddress]

@typing.type_check_only
class ReturnpolicyCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ReturnpolicyCustomBatchRequestEntry]

@typing.type_check_only
class ReturnpolicyCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    merchantId: str
    method: str
    returnPolicy: ReturnPolicy
    returnPolicyId: str

@typing.type_check_only
class ReturnpolicyCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ReturnpolicyCustomBatchResponseEntry]
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
    resources: typing.List[ReturnPolicy]

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    cells: typing.List[Value]

@typing.type_check_only
class SearchRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[ReportRow]

@typing.type_check_only
class Segments(typing_extensions.TypedDict, total=False):
    date: Date
    offerId: str
    program: typing_extensions.Literal[
        "PROGRAM_UNSPECIFIED",
        "SHOPPING_ADS",
        "FREE_PRODUCT_LISTING",
        "FREE_LOCAL_PRODUCT_LISTING",
        "BUY_ON_GOOGLE_LISTING",
    ]

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
    rateGroups: typing.List[RateGroup]
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
    transferIds: typing.List[str]

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
    shipmentIds: typing.List[str]
    transactionId: str

@typing.type_check_only
class SettlementTransactionTransaction(typing_extensions.TypedDict, total=False):
    postDate: str
    type: str

@typing.type_check_only
class SettlementreportsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[SettlementReport]

@typing.type_check_only
class SettlementtransactionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[SettlementTransaction]

@typing.type_check_only
class ShipmentInvoice(typing_extensions.TypedDict, total=False):
    invoiceSummary: InvoiceSummary
    lineItemInvoices: typing.List[ShipmentInvoiceLineItemInvoice]
    shipmentGroupId: str

@typing.type_check_only
class ShipmentInvoiceLineItemInvoice(typing_extensions.TypedDict, total=False):
    lineItemId: str
    productId: str
    shipmentUnitIds: typing.List[str]
    unitInvoice: UnitInvoice

@typing.type_check_only
class ShipmentTrackingInfo(typing_extensions.TypedDict, total=False):
    carrier: str
    trackingNumber: str

@typing.type_check_only
class ShippingSettings(typing_extensions.TypedDict, total=False):
    accountId: str
    postalCodeGroups: typing.List[PostalCodeGroup]
    services: typing.List[Service]

@typing.type_check_only
class ShippingsettingsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ShippingsettingsCustomBatchRequestEntry]

@typing.type_check_only
class ShippingsettingsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    merchantId: str
    method: str
    shippingSettings: ShippingSettings

@typing.type_check_only
class ShippingsettingsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ShippingsettingsCustomBatchResponseEntry]
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
    carriers: typing.List[CarriersCarrier]
    kind: str

@typing.type_check_only
class ShippingsettingsGetSupportedHolidaysResponse(
    typing_extensions.TypedDict, total=False
):
    holidays: typing.List[HolidaysHoliday]
    kind: str

@typing.type_check_only
class ShippingsettingsGetSupportedPickupServicesResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    pickupServices: typing.List[PickupServicesPickupService]

@typing.type_check_only
class ShippingsettingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[ShippingSettings]

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    columnHeaders: Headers
    name: str
    rowHeaders: Headers
    rows: typing.List[Row]

@typing.type_check_only
class TestOrder(typing_extensions.TypedDict, total=False):
    deliveryDetails: TestOrderDeliveryDetails
    enableOrderinvoices: bool
    kind: str
    lineItems: typing.List[TestOrderLineItem]
    notificationMode: str
    pickupDetails: TestOrderPickupDetails
    predefinedBillingAddress: str
    predefinedDeliveryAddress: str
    predefinedEmail: str
    predefinedPickupDetails: str
    promotions: typing.List[OrderPromotion]
    shippingCost: Price
    shippingOption: str

@typing.type_check_only
class TestOrderAddress(typing_extensions.TypedDict, total=False):
    country: str
    fullAddress: typing.List[str]
    isPostOfficeBox: bool
    locality: str
    postalCode: str
    recipientName: str
    region: str
    streetAddress: typing.List[str]

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
    fees: typing.List[OrderLineItemProductFee]
    gtin: str
    imageLink: str
    itemGroupId: str
    mpn: str
    offerId: str
    price: Price
    targetCountry: str
    title: str
    variantAttributes: typing.List[OrderLineItemProductVariantAttribute]

@typing.type_check_only
class TestOrderPickupDetails(typing_extensions.TypedDict, total=False):
    locationCode: str
    pickupLocationAddress: TestOrderAddress
    pickupLocationType: str
    pickupPersons: typing.List[TestOrderPickupDetailsPickupPerson]

@typing.type_check_only
class TestOrderPickupDetailsPickupPerson(typing_extensions.TypedDict, total=False):
    name: str
    phoneNumber: str

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class TransitTable(typing_extensions.TypedDict, total=False):
    postalCodeGroupNames: typing.List[str]
    rows: typing.List[TransitTableTransitTimeRow]
    transitTimeLabels: typing.List[str]

@typing.type_check_only
class TransitTableTransitTimeRow(typing_extensions.TypedDict, total=False):
    values: typing.List[TransitTableTransitTimeRowTransitTimeValue]

@typing.type_check_only
class TransitTableTransitTimeRowTransitTimeValue(
    typing_extensions.TypedDict, total=False
):
    maxTransitTimeInDays: int
    minTransitTimeInDays: int

@typing.type_check_only
class UnitInvoice(typing_extensions.TypedDict, total=False):
    additionalCharges: typing.List[UnitInvoiceAdditionalCharge]
    unitPrice: Price
    unitPriceTaxes: typing.List[UnitInvoiceTaxLine]

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
class Weight(typing_extensions.TypedDict, total=False):
    unit: str
    value: str
