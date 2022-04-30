import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    adultContent: bool
    adwordsLinks: _list[AccountAdwordsLink]
    businessInformation: AccountBusinessInformation
    googleMyBusinessLink: AccountGoogleMyBusinessLink
    id: str
    kind: str
    name: str
    reviewsUrl: str
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
class AccountAdwordsLink(typing_extensions.TypedDict, total=False):
    adwordsId: str
    status: str

@typing.type_check_only
class AccountBusinessInformation(typing_extensions.TypedDict, total=False):
    address: AccountAddress
    customerService: AccountCustomerService
    koreanBusinessRegistrationNumber: str
    phoneNumber: str

@typing.type_check_only
class AccountCustomerService(typing_extensions.TypedDict, total=False):
    email: str
    phoneNumber: str
    url: str

@typing.type_check_only
class AccountGoogleMyBusinessLink(typing_extensions.TypedDict, total=False):
    gmbEmail: str
    status: str

@typing.type_check_only
class AccountIdentifier(typing_extensions.TypedDict, total=False):
    aggregatorId: str
    merchantId: str

@typing.type_check_only
class AccountStatus(typing_extensions.TypedDict, total=False):
    accountId: str
    accountLevelIssues: _list[AccountStatusAccountLevelIssue]
    dataQualityIssues: _list[AccountStatusDataQualityIssue]
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
class AccountStatusDataQualityIssue(typing_extensions.TypedDict, total=False):
    country: str
    destination: str
    detail: str
    displayedValue: str
    exampleItems: _list[AccountStatusExampleItem]
    id: str
    lastChecked: str
    location: str
    numItems: int
    severity: str
    submittedValue: str

@typing.type_check_only
class AccountStatusExampleItem(typing_extensions.TypedDict, total=False):
    itemId: str
    link: str
    submittedValue: str
    title: str
    valueOnLandingPage: str

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

@typing.type_check_only
class AccountsCustomBatchRequestEntryLinkRequest(
    typing_extensions.TypedDict, total=False
):
    action: str
    linkType: str
    linkedAccountId: str

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
    linkStatus: str

@typing.type_check_only
class AccountsLinkRequest(typing_extensions.TypedDict, total=False):
    action: str
    linkType: str
    linkedAccountId: str

@typing.type_check_only
class AccountsLinkResponse(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class AccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[Account]

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
class Address(typing_extensions.TypedDict, total=False):
    administrativeArea: str
    city: str
    country: str
    postalCode: str
    streetAddress: str

@typing.type_check_only
class Amount(typing_extensions.TypedDict, total=False):
    pretax: Price
    tax: Price

@typing.type_check_only
class BusinessDayConfig(typing_extensions.TypedDict, total=False):
    businessDays: _list[str]

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
class CustomAttribute(typing_extensions.TypedDict, total=False):
    name: str
    type: str
    unit: str
    value: str

@typing.type_check_only
class CustomGroup(typing_extensions.TypedDict, total=False):
    attributes: _list[CustomAttribute]
    name: str

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
    contentLanguage: str
    contentType: str
    fetchSchedule: DatafeedFetchSchedule
    fileName: str
    format: DatafeedFormat
    id: str
    intendedDestinations: _list[str]
    kind: str
    name: str
    targetCountry: str
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
class Installment(typing_extensions.TypedDict, total=False):
    amount: Price
    months: str

@typing.type_check_only
class InvoiceSummary(typing_extensions.TypedDict, total=False):
    additionalChargeSummaries: _list[InvoiceSummaryAdditionalChargeSummary]
    customerBalance: Amount
    googleBalance: Amount
    merchantBalance: Amount
    productTotal: Amount
    promotionSummaries: _list[Promotion]

@typing.type_check_only
class InvoiceSummaryAdditionalChargeSummary(typing_extensions.TypedDict, total=False):
    totalAmount: Amount
    type: str

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
    returnShipments: _list[ReturnShipment]

@typing.type_check_only
class MerchantOrderReturnItem(typing_extensions.TypedDict, total=False):
    customerReturnReason: CustomerReturnReason
    itemId: str
    merchantReturnReason: RefundReason
    product: OrderLineItemProduct
    returnShipmentIds: _list[str]
    state: str

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
class Order(typing_extensions.TypedDict, total=False):
    acknowledged: bool
    channelType: str
    customer: OrderCustomer
    deliveryDetails: OrderDeliveryDetails
    id: str
    kind: str
    lineItems: _list[OrderLineItem]
    merchantId: str
    merchantOrderId: str
    netAmount: Price
    paymentMethod: OrderPaymentMethod
    paymentStatus: str
    pickupDetails: OrderPickupDetails
    placedDate: str
    promotions: _list[OrderLegacyPromotion]
    refunds: _list[OrderRefund]
    shipments: _list[OrderShipment]
    shippingCost: Price
    shippingCostTax: Price
    shippingOption: str
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
    email: str
    explicitMarketingPreference: bool
    fullName: str
    invoiceReceivingEmail: str
    marketingRightsInfo: OrderCustomerMarketingRightsInfo

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
class OrderLegacyPromotion(typing_extensions.TypedDict, total=False):
    benefits: _list[OrderLegacyPromotionBenefit]
    effectiveDates: str
    genericRedemptionCode: str
    id: str
    longTitle: str
    productApplicability: str
    redemptionChannel: str

@typing.type_check_only
class OrderLegacyPromotionBenefit(typing_extensions.TypedDict, total=False):
    discount: Price
    offerIds: _list[str]
    subType: str
    taxImpact: Price
    type: str

@typing.type_check_only
class OrderLineItem(typing_extensions.TypedDict, total=False):
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
    returnInfo: OrderLineItemReturnInfo
    returns: _list[OrderReturn]
    shippingDetails: OrderLineItemShippingDetails
    tax: Price

@typing.type_check_only
class OrderLineItemProduct(typing_extensions.TypedDict, total=False):
    brand: str
    channel: str
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
class OrderPaymentMethod(typing_extensions.TypedDict, total=False):
    billingAddress: OrderAddress
    expirationMonth: int
    expirationYear: int
    lastFourDigits: str
    phoneNumber: str
    type: str

@typing.type_check_only
class OrderPickupDetails(typing_extensions.TypedDict, total=False):
    address: OrderAddress
    collectors: _list[OrderPickupDetailsCollector]
    locationId: str

@typing.type_check_only
class OrderPickupDetailsCollector(typing_extensions.TypedDict, total=False):
    name: str
    phoneNumber: str

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
    productAmount: Amount
    productAmountWithRemittedTax: ProductAmount
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
class OrderreturnsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[MerchantOrderReturn]

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
    amount: Price
    amountPretax: Price
    amountTax: Price
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
class OrdersCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: _list[OrdersCustomBatchRequestEntry]

@typing.type_check_only
class OrdersCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    cancel: OrdersCustomBatchRequestEntryCancel
    cancelLineItem: OrdersCustomBatchRequestEntryCancelLineItem
    inStoreRefundLineItem: OrdersCustomBatchRequestEntryInStoreRefundLineItem
    merchantId: str
    merchantOrderId: str
    method: str
    operationId: str
    orderId: str
    refund: OrdersCustomBatchRequestEntryRefund
    rejectReturnLineItem: OrdersCustomBatchRequestEntryRejectReturnLineItem
    returnLineItem: OrdersCustomBatchRequestEntryReturnLineItem
    returnRefundLineItem: OrdersCustomBatchRequestEntryReturnRefundLineItem
    setLineItemMetadata: OrdersCustomBatchRequestEntrySetLineItemMetadata
    shipLineItems: OrdersCustomBatchRequestEntryShipLineItems
    updateLineItemShippingDetails: OrdersCustomBatchRequestEntryUpdateLineItemShippingDetails
    updateShipment: OrdersCustomBatchRequestEntryUpdateShipment

@typing.type_check_only
class OrdersCustomBatchRequestEntryCancel(typing_extensions.TypedDict, total=False):
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryCancelLineItem(
    typing_extensions.TypedDict, total=False
):
    amount: Price
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryCreateTestReturnReturnItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    quantity: int

@typing.type_check_only
class OrdersCustomBatchRequestEntryInStoreRefundLineItem(
    typing_extensions.TypedDict, total=False
):
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryRefund(typing_extensions.TypedDict, total=False):
    amount: Price
    amountPretax: Price
    amountTax: Price
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryRejectReturnLineItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryReturnLineItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryReturnRefundLineItem(
    typing_extensions.TypedDict, total=False
):
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersCustomBatchRequestEntrySetLineItemMetadata(
    typing_extensions.TypedDict, total=False
):
    annotations: _list[OrderMerchantProvidedAnnotation]
    lineItemId: str
    productId: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryShipLineItems(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    lineItems: _list[OrderShipmentLineItemShipment]
    shipmentGroupId: str
    shipmentId: str
    shipmentInfos: _list[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]
    trackingId: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    shipmentId: str
    trackingId: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryUpdateLineItemShippingDetails(
    typing_extensions.TypedDict, total=False
):
    deliverByDate: str
    lineItemId: str
    productId: str
    shipByDate: str

@typing.type_check_only
class OrdersCustomBatchRequestEntryUpdateShipment(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    deliveryDate: str
    shipmentId: str
    status: str
    trackingId: str

@typing.type_check_only
class OrdersCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: _list[OrdersCustomBatchResponseEntry]
    kind: str

@typing.type_check_only
class OrdersCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    executionStatus: str
    kind: str
    order: Order

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
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

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
class OrdersRefundRequest(typing_extensions.TypedDict, total=False):
    amount: Price
    amountPretax: Price
    amountTax: Price
    operationId: str
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersRefundResponse(typing_extensions.TypedDict, total=False):
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
class OrdersReturnLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

@typing.type_check_only
class OrdersReturnLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

@typing.type_check_only
class OrdersReturnRefundLineItemRequest(typing_extensions.TypedDict, total=False):
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

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
    carrier: str
    lineItems: _list[OrderShipmentLineItemShipment]
    operationId: str
    shipmentGroupId: str
    shipmentId: str
    shipmentInfos: _list[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]
    trackingId: str

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
    operationId: str
    shipmentId: str
    status: str
    trackingId: str

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
class Product(typing_extensions.TypedDict, total=False):
    additionalImageLinks: _list[str]
    additionalProductTypes: _list[str]
    adult: bool
    adwordsGrouping: str
    adwordsLabels: _list[str]
    adwordsRedirect: str
    ageGroup: str
    aspects: _list[ProductAspect]
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
    customGroups: _list[CustomGroup]
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    description: str
    destinations: _list[ProductDestination]
    displayAdsId: str
    displayAdsLink: str
    displayAdsSimilarIds: _list[str]
    displayAdsTitle: str
    displayAdsValue: float
    energyEfficiencyClass: str
    expirationDate: str
    gender: str
    googleProductCategory: str
    gtin: str
    id: str
    identifierExists: bool
    imageLink: str
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
    onlineOnly: bool
    pattern: str
    price: Price
    productType: str
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
    sizeSystem: str
    sizeType: str
    sizes: _list[str]
    source: str
    targetCountry: str
    taxes: _list[ProductTax]
    title: str
    unitPricingBaseMeasure: ProductUnitPricingBaseMeasure
    unitPricingMeasure: ProductUnitPricingMeasure
    validatedDestinations: _list[str]
    warnings: _list[Error]

@typing.type_check_only
class ProductAmount(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    remittedTaxAmount: Price
    taxAmount: Price

@typing.type_check_only
class ProductAspect(typing_extensions.TypedDict, total=False):
    aspectName: str
    destinationName: str
    intention: str

@typing.type_check_only
class ProductDestination(typing_extensions.TypedDict, total=False):
    destinationName: str
    intention: str

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
    dataQualityIssues: _list[ProductStatusDataQualityIssue]
    destinationStatuses: _list[ProductStatusDestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: _list[ProductStatusItemLevelIssue]
    kind: str
    lastUpdateDate: str
    link: str
    product: Product
    productId: str
    title: str

@typing.type_check_only
class ProductStatusDataQualityIssue(typing_extensions.TypedDict, total=False):
    destination: str
    detail: str
    fetchStatus: str
    id: str
    location: str
    severity: str
    timestamp: str
    valueOnLandingPage: str
    valueProvided: str

@typing.type_check_only
class ProductStatusDestinationStatus(typing_extensions.TypedDict, total=False):
    approvalPending: bool
    approvalStatus: str
    destination: str
    intention: str

@typing.type_check_only
class ProductStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    attributeName: str
    code: str
    description: str
    destination: str
    detail: str
    documentation: str
    resolution: str
    servability: str

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
    entries: _list[ProductsCustomBatchRequestEntry]

@typing.type_check_only
class ProductsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    merchantId: str
    method: str
    product: Product
    productId: str

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
    promotionAmount: Amount
    promotionId: str

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
class ReturnShipment(typing_extensions.TypedDict, total=False):
    creationDate: str
    deliveryDate: str
    returnMethodType: str
    shipmentId: str
    shipmentTrackingInfos: _list[ShipmentTrackingInfo]
    shippingDate: str
    state: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    cells: _list[Value]

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
class Table(typing_extensions.TypedDict, total=False):
    columnHeaders: Headers
    name: str
    rowHeaders: Headers
    rows: _list[Row]

@typing.type_check_only
class TestOrder(typing_extensions.TypedDict, total=False):
    customer: TestOrderCustomer
    enableOrderinvoices: bool
    kind: str
    lineItems: _list[TestOrderLineItem]
    notificationMode: str
    paymentMethod: TestOrderPaymentMethod
    predefinedDeliveryAddress: str
    predefinedPickupDetails: str
    promotions: _list[OrderLegacyPromotion]
    shippingCost: Price
    shippingCostTax: Price
    shippingOption: str

@typing.type_check_only
class TestOrderCustomer(typing_extensions.TypedDict, total=False):
    email: str
    explicitMarketingPreference: bool
    fullName: str
    marketingRightsInfo: TestOrderCustomerMarketingRightsInfo

@typing.type_check_only
class TestOrderCustomerMarketingRightsInfo(typing_extensions.TypedDict, total=False):
    explicitMarketingPreference: str
    lastUpdatedTimestamp: str

@typing.type_check_only
class TestOrderLineItem(typing_extensions.TypedDict, total=False):
    product: TestOrderLineItemProduct
    quantityOrdered: int
    returnInfo: OrderLineItemReturnInfo
    shippingDetails: OrderLineItemShippingDetails
    unitTax: Price

@typing.type_check_only
class TestOrderLineItemProduct(typing_extensions.TypedDict, total=False):
    brand: str
    channel: str
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
class TestOrderPaymentMethod(typing_extensions.TypedDict, total=False):
    expirationMonth: int
    expirationYear: int
    lastFourDigits: str
    predefinedBillingAddress: str
    type: str

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
    promotions: _list[Promotion]
    unitPricePretax: Price
    unitPriceTaxes: _list[UnitInvoiceTaxLine]

@typing.type_check_only
class UnitInvoiceAdditionalCharge(typing_extensions.TypedDict, total=False):
    additionalChargeAmount: Amount
    additionalChargePromotions: _list[Promotion]
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
