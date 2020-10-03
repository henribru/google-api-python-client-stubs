import typing

import typing_extensions

class Account(typing_extensions.TypedDict, total=False):
    adultContent: bool
    adwordsLinks: typing.List[AccountAdwordsLink]
    businessInformation: AccountBusinessInformation
    googleMyBusinessLink: AccountGoogleMyBusinessLink
    id: str
    kind: str
    name: str
    reviewsUrl: str
    sellerId: str
    users: typing.List[AccountUser]
    websiteUrl: str
    youtubeChannelLinks: typing.List[AccountYouTubeChannelLink]

class AccountAddress(typing_extensions.TypedDict, total=False):
    country: str
    locality: str
    postalCode: str
    region: str
    streetAddress: str

class AccountAdwordsLink(typing_extensions.TypedDict, total=False):
    adwordsId: str
    status: str

class AccountBusinessInformation(typing_extensions.TypedDict, total=False):
    address: AccountAddress
    customerService: AccountCustomerService
    phoneNumber: str

class AccountCustomerService(typing_extensions.TypedDict, total=False):
    email: str
    phoneNumber: str
    url: str

class AccountGoogleMyBusinessLink(typing_extensions.TypedDict, total=False):
    gmbEmail: str
    status: str

class AccountIdentifier(typing_extensions.TypedDict, total=False):
    aggregatorId: str
    merchantId: str

class AccountStatus(typing_extensions.TypedDict, total=False):
    accountId: str
    accountLevelIssues: typing.List[AccountStatusAccountLevelIssue]
    dataQualityIssues: typing.List[AccountStatusDataQualityIssue]
    kind: str
    products: typing.List[AccountStatusProducts]
    websiteClaimed: bool

class AccountStatusAccountLevelIssue(typing_extensions.TypedDict, total=False):
    country: str
    destination: str
    detail: str
    documentation: str
    id: str
    severity: str
    title: str

class AccountStatusDataQualityIssue(typing_extensions.TypedDict, total=False):
    country: str
    destination: str
    detail: str
    displayedValue: str
    exampleItems: typing.List[AccountStatusExampleItem]
    id: str
    lastChecked: str
    location: str
    numItems: int
    severity: str
    submittedValue: str

class AccountStatusExampleItem(typing_extensions.TypedDict, total=False):
    itemId: str
    link: str
    submittedValue: str
    title: str
    valueOnLandingPage: str

class AccountStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    attributeName: str
    code: str
    description: str
    detail: str
    documentation: str
    numItems: str
    resolution: str
    servability: str

class AccountStatusProducts(typing_extensions.TypedDict, total=False):
    channel: str
    country: str
    destination: str
    itemLevelIssues: typing.List[AccountStatusItemLevelIssue]
    statistics: AccountStatusStatistics

class AccountStatusStatistics(typing_extensions.TypedDict, total=False):
    active: str
    disapproved: str
    expiring: str
    pending: str

class AccountTax(typing_extensions.TypedDict, total=False):
    accountId: str
    kind: str
    rules: typing.List[AccountTaxTaxRule]

class AccountTaxTaxRule(typing_extensions.TypedDict, total=False):
    country: str
    locationId: str
    ratePercent: str
    shippingTaxed: bool
    useGlobalRate: bool

class AccountUser(typing_extensions.TypedDict, total=False):
    admin: bool
    emailAddress: str
    orderManager: bool
    paymentsAnalyst: bool
    paymentsManager: bool

class AccountYouTubeChannelLink(typing_extensions.TypedDict, total=False):
    channelId: str
    status: str

class AccountsAuthInfoResponse(typing_extensions.TypedDict, total=False):
    accountIdentifiers: typing.List[AccountIdentifier]
    kind: str

class AccountsClaimWebsiteResponse(typing_extensions.TypedDict, total=False):
    kind: str

class AccountsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountsCustomBatchRequestEntry]

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

class AccountsCustomBatchRequestEntryLinkRequest(
    typing_extensions.TypedDict, total=False
):
    action: str
    linkType: str
    linkedAccountId: str

class AccountsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountsCustomBatchResponseEntry]
    kind: str

class AccountsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    account: Account
    batchId: int
    errors: Errors
    kind: str
    linkStatus: str

class AccountsLinkRequest(typing_extensions.TypedDict, total=False):
    action: str
    linkType: str
    linkedAccountId: str

class AccountsLinkResponse(typing_extensions.TypedDict, total=False):
    kind: str

class AccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[Account]

class AccountstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountstatusesCustomBatchRequestEntry]

class AccountstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    destinations: typing.List[str]
    merchantId: str
    method: str

class AccountstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccountstatusesCustomBatchResponseEntry]
    kind: str

class AccountstatusesCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    accountStatus: AccountStatus
    batchId: int
    errors: Errors

class AccountstatusesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[AccountStatus]

class AccounttaxCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccounttaxCustomBatchRequestEntry]

class AccounttaxCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    accountTax: AccountTax
    batchId: int
    merchantId: str
    method: str

class AccounttaxCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[AccounttaxCustomBatchResponseEntry]
    kind: str

class AccounttaxCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    accountTax: AccountTax
    batchId: int
    errors: Errors
    kind: str

class AccounttaxListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[AccountTax]

class Amount(typing_extensions.TypedDict, total=False):
    pretax: Price
    tax: Price

class BusinessDayConfig(typing_extensions.TypedDict, total=False):
    businessDays: typing.List[str]

class CarrierRate(typing_extensions.TypedDict, total=False):
    carrierName: str
    carrierService: str
    flatAdjustment: Price
    name: str
    originPostalCode: str
    percentageAdjustment: str

class CarriersCarrier(typing_extensions.TypedDict, total=False):
    country: str
    name: str
    services: typing.List[str]

class CustomAttribute(typing_extensions.TypedDict, total=False):
    name: str
    type: str
    unit: str
    value: str

class CustomGroup(typing_extensions.TypedDict, total=False):
    attributes: typing.List[CustomAttribute]
    name: str

class CustomerReturnReason(typing_extensions.TypedDict, total=False):
    description: str
    reasonCode: str

class CutoffTime(typing_extensions.TypedDict, total=False):
    hour: int
    minute: int
    timezone: str

class Datafeed(typing_extensions.TypedDict, total=False):
    attributeLanguage: str
    contentLanguage: str
    contentType: str
    fetchSchedule: DatafeedFetchSchedule
    fileName: str
    format: DatafeedFormat
    id: str
    intendedDestinations: typing.List[str]
    kind: str
    name: str
    targetCountry: str
    targets: typing.List[DatafeedTarget]

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

class DatafeedFormat(typing_extensions.TypedDict, total=False):
    columnDelimiter: str
    fileEncoding: str
    quotingMode: str

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

class DatafeedStatusError(typing_extensions.TypedDict, total=False):
    code: str
    count: str
    examples: typing.List[DatafeedStatusExample]
    message: str

class DatafeedStatusExample(typing_extensions.TypedDict, total=False):
    itemId: str
    lineNumber: str
    value: str

class DatafeedTarget(typing_extensions.TypedDict, total=False):
    country: str
    excludedDestinations: typing.List[str]
    includedDestinations: typing.List[str]
    language: str

class DatafeedsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedsCustomBatchRequestEntry]

class DatafeedsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    datafeed: Datafeed
    datafeedId: str
    merchantId: str
    method: str

class DatafeedsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedsCustomBatchResponseEntry]
    kind: str

class DatafeedsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    datafeed: Datafeed
    errors: Errors

class DatafeedsFetchNowResponse(typing_extensions.TypedDict, total=False):
    kind: str

class DatafeedsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[Datafeed]

class DatafeedstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedstatusesCustomBatchRequestEntry]

class DatafeedstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    country: str
    datafeedId: str
    language: str
    merchantId: str
    method: str

class DatafeedstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[DatafeedstatusesCustomBatchResponseEntry]
    kind: str

class DatafeedstatusesCustomBatchResponseEntry(
    typing_extensions.TypedDict, total=False
):
    batchId: int
    datafeedStatus: DatafeedStatus
    errors: Errors

class DatafeedstatusesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[DatafeedStatus]

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

class Error(typing_extensions.TypedDict, total=False):
    domain: str
    message: str
    reason: str

class Errors(typing_extensions.TypedDict, total=False):
    code: int
    errors: typing.List[Error]
    message: str

class GmbAccounts(typing_extensions.TypedDict, total=False):
    accountId: str
    gmbAccounts: typing.List[GmbAccountsGmbAccount]

class GmbAccountsGmbAccount(typing_extensions.TypedDict, total=False):
    email: str
    listingCount: str
    name: str
    type: str

class Headers(typing_extensions.TypedDict, total=False):
    locations: typing.List[LocationIdSet]
    numberOfItems: typing.List[str]
    postalCodeGroupNames: typing.List[str]
    prices: typing.List[Price]
    weights: typing.List[Weight]

class HolidayCutoff(typing_extensions.TypedDict, total=False):
    deadlineDate: str
    deadlineHour: int
    deadlineTimezone: str
    holidayId: str
    visibleFromDate: str

class HolidaysHoliday(typing_extensions.TypedDict, total=False):
    countryCode: str
    date: str
    deliveryGuaranteeDate: str
    deliveryGuaranteeHour: str
    id: str
    type: str

class Installment(typing_extensions.TypedDict, total=False):
    amount: Price
    months: str

class Inventory(typing_extensions.TypedDict, total=False):
    availability: str
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    installment: Installment
    instoreProductLocation: str
    kind: str
    loyaltyPoints: LoyaltyPoints
    pickup: InventoryPickup
    price: Price
    quantity: int
    salePrice: Price
    salePriceEffectiveDate: str
    sellOnGoogleQuantity: int

class InventoryCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[InventoryCustomBatchRequestEntry]

class InventoryCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    inventory: Inventory
    merchantId: str
    productId: str
    storeCode: str

class InventoryCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[InventoryCustomBatchResponseEntry]
    kind: str

class InventoryCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str

class InventoryPickup(typing_extensions.TypedDict, total=False):
    pickupMethod: str
    pickupSla: str

class InventorySetRequest(typing_extensions.TypedDict, total=False):
    availability: str
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    installment: Installment
    instoreProductLocation: str
    loyaltyPoints: LoyaltyPoints
    pickup: InventoryPickup
    price: Price
    quantity: int
    salePrice: Price
    salePriceEffectiveDate: str
    sellOnGoogleQuantity: int

class InventorySetResponse(typing_extensions.TypedDict, total=False):
    kind: str

class InvoiceSummary(typing_extensions.TypedDict, total=False):
    additionalChargeSummaries: typing.List[InvoiceSummaryAdditionalChargeSummary]
    customerBalance: Amount
    googleBalance: Amount
    merchantBalance: Amount
    productTotal: Amount
    promotionSummaries: typing.List[Promotion]

class InvoiceSummaryAdditionalChargeSummary(typing_extensions.TypedDict, total=False):
    totalAmount: Amount
    type: str

class LiaAboutPageSettings(typing_extensions.TypedDict, total=False):
    status: str
    url: str

class LiaCountrySettings(typing_extensions.TypedDict, total=False):
    about: LiaAboutPageSettings
    country: str
    hostedLocalStorefrontActive: bool
    inventory: LiaInventorySettings
    onDisplayToOrder: LiaOnDisplayToOrderSettings
    posDataProvider: LiaPosDataProvider
    storePickupActive: bool

class LiaInventorySettings(typing_extensions.TypedDict, total=False):
    inventoryVerificationContactEmail: str
    inventoryVerificationContactName: str
    inventoryVerificationContactStatus: str
    status: str

class LiaOnDisplayToOrderSettings(typing_extensions.TypedDict, total=False):
    shippingCostPolicyUrl: str
    status: str

class LiaPosDataProvider(typing_extensions.TypedDict, total=False):
    posDataProviderId: str
    posExternalAccountId: str

class LiaSettings(typing_extensions.TypedDict, total=False):
    accountId: str
    countrySettings: typing.List[LiaCountrySettings]
    kind: str

class LiasettingsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[LiasettingsCustomBatchRequestEntry]

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

class LiasettingsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[LiasettingsCustomBatchResponseEntry]
    kind: str

class LiasettingsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    gmbAccounts: GmbAccounts
    kind: str
    liaSettings: LiaSettings
    posDataProviders: typing.List[PosDataProviders]

class LiasettingsGetAccessibleGmbAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accountId: str
    gmbAccounts: typing.List[GmbAccountsGmbAccount]
    kind: str

class LiasettingsListPosDataProvidersResponse(typing_extensions.TypedDict, total=False):
    kind: str
    posDataProviders: typing.List[PosDataProviders]

class LiasettingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[LiaSettings]

class LiasettingsRequestGmbAccessResponse(typing_extensions.TypedDict, total=False):
    kind: str

class LiasettingsRequestInventoryVerificationResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str

class LiasettingsSetInventoryVerificationContactResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str

class LiasettingsSetPosDataProviderResponse(typing_extensions.TypedDict, total=False):
    kind: str

class LocationIdSet(typing_extensions.TypedDict, total=False):
    locationIds: typing.List[str]

class LoyaltyPoints(typing_extensions.TypedDict, total=False):
    name: str
    pointsValue: str
    ratio: float

class MerchantOrderReturn(typing_extensions.TypedDict, total=False):
    creationDate: str
    merchantOrderId: str
    orderId: str
    orderReturnId: str
    returnItems: typing.List[MerchantOrderReturnItem]
    returnShipments: typing.List[ReturnShipment]

class MerchantOrderReturnItem(typing_extensions.TypedDict, total=False):
    customerReturnReason: CustomerReturnReason
    itemId: str
    merchantReturnReason: RefundReason
    product: OrderLineItemProduct
    returnShipmentIds: typing.List[str]
    state: str

class MinimumOrderValueTable(typing_extensions.TypedDict, total=False):
    storeCodeSetWithMovs: typing.List[MinimumOrderValueTableStoreCodeSetWithMov]

class MinimumOrderValueTableStoreCodeSetWithMov(
    typing_extensions.TypedDict, total=False
):
    storeCodes: typing.List[str]
    value: Price

class Order(typing_extensions.TypedDict, total=False):
    acknowledged: bool
    channelType: str
    customer: OrderCustomer
    deliveryDetails: OrderDeliveryDetails
    id: str
    kind: str
    lineItems: typing.List[OrderLineItem]
    merchantId: str
    merchantOrderId: str
    netAmount: Price
    paymentMethod: OrderPaymentMethod
    paymentStatus: str
    pickupDetails: OrderPickupDetails
    placedDate: str
    promotions: typing.List[OrderLegacyPromotion]
    refunds: typing.List[OrderRefund]
    shipments: typing.List[OrderShipment]
    shippingCost: Price
    shippingCostTax: Price
    shippingOption: str
    status: str
    taxCollector: str

class OrderAddress(typing_extensions.TypedDict, total=False):
    country: str
    fullAddress: typing.List[str]
    isPostOfficeBox: bool
    locality: str
    postalCode: str
    recipientName: str
    region: str
    streetAddress: typing.List[str]

class OrderCancellation(typing_extensions.TypedDict, total=False):
    actor: str
    creationDate: str
    quantity: int
    reason: str
    reasonText: str

class OrderCustomer(typing_extensions.TypedDict, total=False):
    email: str
    explicitMarketingPreference: bool
    fullName: str
    invoiceReceivingEmail: str
    marketingRightsInfo: OrderCustomerMarketingRightsInfo

class OrderCustomerMarketingRightsInfo(typing_extensions.TypedDict, total=False):
    explicitMarketingPreference: str
    lastUpdatedTimestamp: str
    marketingEmailAddress: str

class OrderDeliveryDetails(typing_extensions.TypedDict, total=False):
    address: OrderAddress
    phoneNumber: str

class OrderLegacyPromotion(typing_extensions.TypedDict, total=False):
    benefits: typing.List[OrderLegacyPromotionBenefit]
    effectiveDates: str
    genericRedemptionCode: str
    id: str
    longTitle: str
    productApplicability: str
    redemptionChannel: str

class OrderLegacyPromotionBenefit(typing_extensions.TypedDict, total=False):
    discount: Price
    offerIds: typing.List[str]
    subType: str
    taxImpact: Price
    type: str

class OrderLineItem(typing_extensions.TypedDict, total=False):
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
    returnInfo: OrderLineItemReturnInfo
    returns: typing.List[OrderReturn]
    shippingDetails: OrderLineItemShippingDetails
    tax: Price

class OrderLineItemProduct(typing_extensions.TypedDict, total=False):
    brand: str
    channel: str
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

class OrderLineItemProductFee(typing_extensions.TypedDict, total=False):
    amount: Price
    name: str

class OrderLineItemProductVariantAttribute(typing_extensions.TypedDict, total=False):
    dimension: str
    value: str

class OrderLineItemReturnInfo(typing_extensions.TypedDict, total=False):
    daysToReturn: int
    isReturnable: bool
    policyUrl: str

class OrderLineItemShippingDetails(typing_extensions.TypedDict, total=False):
    deliverByDate: str
    method: OrderLineItemShippingDetailsMethod
    shipByDate: str
    type: str

class OrderLineItemShippingDetailsMethod(typing_extensions.TypedDict, total=False):
    carrier: str
    maxDaysInTransit: int
    methodName: str
    minDaysInTransit: int

class OrderMerchantProvidedAnnotation(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class OrderPaymentMethod(typing_extensions.TypedDict, total=False):
    billingAddress: OrderAddress
    expirationMonth: int
    expirationYear: int
    lastFourDigits: str
    phoneNumber: str
    type: str

class OrderPickupDetails(typing_extensions.TypedDict, total=False):
    address: OrderAddress
    collectors: typing.List[OrderPickupDetailsCollector]
    locationId: str

class OrderPickupDetailsCollector(typing_extensions.TypedDict, total=False):
    name: str
    phoneNumber: str

class OrderRefund(typing_extensions.TypedDict, total=False):
    actor: str
    amount: Price
    creationDate: str
    reason: str
    reasonText: str

class OrderReportDisbursement(typing_extensions.TypedDict, total=False):
    disbursementAmount: Price
    disbursementCreationDate: str
    disbursementDate: str
    disbursementId: str
    merchantId: str

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

class OrderReturn(typing_extensions.TypedDict, total=False):
    actor: str
    creationDate: str
    quantity: int
    reason: str
    reasonText: str

class OrderShipment(typing_extensions.TypedDict, total=False):
    carrier: str
    creationDate: str
    deliveryDate: str
    id: str
    lineItems: typing.List[OrderShipmentLineItemShipment]
    scheduledDeliveryDetails: OrderShipmentScheduledDeliveryDetails
    status: str
    trackingId: str

class OrderShipmentLineItemShipment(typing_extensions.TypedDict, total=False):
    lineItemId: str
    productId: str
    quantity: int

class OrderShipmentScheduledDeliveryDetails(typing_extensions.TypedDict, total=False):
    carrierPhoneNumber: str
    scheduledDate: str

class OrderinvoicesCreateChargeInvoiceRequest(typing_extensions.TypedDict, total=False):
    invoiceId: str
    invoiceSummary: InvoiceSummary
    lineItemInvoices: typing.List[ShipmentInvoiceLineItemInvoice]
    operationId: str
    shipmentGroupId: str

class OrderinvoicesCreateChargeInvoiceResponse(
    typing_extensions.TypedDict, total=False
):
    executionStatus: str
    kind: str

class OrderinvoicesCreateRefundInvoiceRequest(typing_extensions.TypedDict, total=False):
    invoiceId: str
    operationId: str
    refundOnlyOption: OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOption
    returnOption: OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOption
    shipmentInvoices: typing.List[ShipmentInvoice]

class OrderinvoicesCreateRefundInvoiceResponse(
    typing_extensions.TypedDict, total=False
):
    executionStatus: str
    kind: str

class OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOption(
    typing_extensions.TypedDict, total=False
):
    description: str
    reason: str

class OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOption(
    typing_extensions.TypedDict, total=False
):
    description: str
    reason: str

class OrderreportsListDisbursementsResponse(typing_extensions.TypedDict, total=False):
    disbursements: typing.List[OrderReportDisbursement]
    kind: str
    nextPageToken: str

class OrderreportsListTransactionsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    transactions: typing.List[OrderReportTransaction]

class OrderreturnsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[MerchantOrderReturn]

class OrdersAcknowledgeRequest(typing_extensions.TypedDict, total=False):
    operationId: str

class OrdersAcknowledgeResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersAdvanceTestOrderResponse(typing_extensions.TypedDict, total=False):
    kind: str

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

class OrdersCancelLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersCancelRequest(typing_extensions.TypedDict, total=False):
    operationId: str
    reason: str
    reasonText: str

class OrdersCancelResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersCancelTestOrderByCustomerRequest(typing_extensions.TypedDict, total=False):
    reason: str

class OrdersCancelTestOrderByCustomerResponse(typing_extensions.TypedDict, total=False):
    kind: str

class OrdersCreateTestOrderRequest(typing_extensions.TypedDict, total=False):
    country: str
    templateName: str
    testOrder: TestOrder

class OrdersCreateTestOrderResponse(typing_extensions.TypedDict, total=False):
    kind: str
    orderId: str

class OrdersCreateTestReturnRequest(typing_extensions.TypedDict, total=False):
    items: typing.List[OrdersCustomBatchRequestEntryCreateTestReturnReturnItem]

class OrdersCreateTestReturnResponse(typing_extensions.TypedDict, total=False):
    kind: str
    returnId: str

class OrdersCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[OrdersCustomBatchRequestEntry]

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

class OrdersCustomBatchRequestEntryCancel(typing_extensions.TypedDict, total=False):
    reason: str
    reasonText: str

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

class OrdersCustomBatchRequestEntryCreateTestReturnReturnItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    quantity: int

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

class OrdersCustomBatchRequestEntryRefund(typing_extensions.TypedDict, total=False):
    amount: Price
    amountPretax: Price
    amountTax: Price
    reason: str
    reasonText: str

class OrdersCustomBatchRequestEntryRejectReturnLineItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

class OrdersCustomBatchRequestEntryReturnLineItem(
    typing_extensions.TypedDict, total=False
):
    lineItemId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

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

class OrdersCustomBatchRequestEntrySetLineItemMetadata(
    typing_extensions.TypedDict, total=False
):
    annotations: typing.List[OrderMerchantProvidedAnnotation]
    lineItemId: str
    productId: str

class OrdersCustomBatchRequestEntryShipLineItems(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    lineItems: typing.List[OrderShipmentLineItemShipment]
    shipmentGroupId: str
    shipmentId: str
    shipmentInfos: typing.List[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]
    trackingId: str

class OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    shipmentId: str
    trackingId: str

class OrdersCustomBatchRequestEntryUpdateLineItemShippingDetails(
    typing_extensions.TypedDict, total=False
):
    deliverByDate: str
    lineItemId: str
    productId: str
    shipByDate: str

class OrdersCustomBatchRequestEntryUpdateShipment(
    typing_extensions.TypedDict, total=False
):
    carrier: str
    deliveryDate: str
    shipmentId: str
    status: str
    trackingId: str

class OrdersCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[OrdersCustomBatchResponseEntry]
    kind: str

class OrdersCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    executionStatus: str
    kind: str
    order: Order

class OrdersGetByMerchantOrderIdResponse(typing_extensions.TypedDict, total=False):
    kind: str
    order: Order

class OrdersGetTestOrderTemplateResponse(typing_extensions.TypedDict, total=False):
    kind: str
    template: TestOrder

class OrdersInStoreRefundLineItemRequest(typing_extensions.TypedDict, total=False):
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

class OrdersInStoreRefundLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[Order]

class OrdersRefundRequest(typing_extensions.TypedDict, total=False):
    amount: Price
    amountPretax: Price
    amountTax: Price
    operationId: str
    reason: str
    reasonText: str

class OrdersRefundResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersRejectReturnLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

class OrdersRejectReturnLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersReturnLineItemRequest(typing_extensions.TypedDict, total=False):
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

class OrdersReturnLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersReturnRefundLineItemRequest(typing_extensions.TypedDict, total=False):
    amountPretax: Price
    amountTax: Price
    lineItemId: str
    operationId: str
    productId: str
    quantity: int
    reason: str
    reasonText: str

class OrdersReturnRefundLineItemResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersSetLineItemMetadataRequest(typing_extensions.TypedDict, total=False):
    annotations: typing.List[OrderMerchantProvidedAnnotation]
    lineItemId: str
    operationId: str
    productId: str

class OrdersSetLineItemMetadataResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersShipLineItemsRequest(typing_extensions.TypedDict, total=False):
    carrier: str
    lineItems: typing.List[OrderShipmentLineItemShipment]
    operationId: str
    shipmentGroupId: str
    shipmentId: str
    shipmentInfos: typing.List[OrdersCustomBatchRequestEntryShipLineItemsShipmentInfo]
    trackingId: str

class OrdersShipLineItemsResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersUpdateLineItemShippingDetailsRequest(
    typing_extensions.TypedDict, total=False
):
    deliverByDate: str
    lineItemId: str
    operationId: str
    productId: str
    shipByDate: str

class OrdersUpdateLineItemShippingDetailsResponse(
    typing_extensions.TypedDict, total=False
):
    executionStatus: str
    kind: str

class OrdersUpdateMerchantOrderIdRequest(typing_extensions.TypedDict, total=False):
    merchantOrderId: str
    operationId: str

class OrdersUpdateMerchantOrderIdResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class OrdersUpdateShipmentRequest(typing_extensions.TypedDict, total=False):
    carrier: str
    deliveryDate: str
    operationId: str
    shipmentId: str
    status: str
    trackingId: str

class OrdersUpdateShipmentResponse(typing_extensions.TypedDict, total=False):
    executionStatus: str
    kind: str

class PickupCarrierService(typing_extensions.TypedDict, total=False):
    carrierName: str
    serviceName: str

class PickupServicesPickupService(typing_extensions.TypedDict, total=False):
    carrierName: str
    country: str
    serviceName: str

class PosCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[PosCustomBatchRequestEntry]

class PosCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    inventory: PosInventory
    merchantId: str
    method: str
    sale: PosSale
    store: PosStore
    storeCode: str
    targetMerchantId: str

class PosCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[PosCustomBatchResponseEntry]
    kind: str

class PosCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    inventory: PosInventory
    kind: str
    sale: PosSale
    store: PosStore

class PosDataProviders(typing_extensions.TypedDict, total=False):
    country: str
    posDataProviders: typing.List[PosDataProvidersPosDataProvider]

class PosDataProvidersPosDataProvider(typing_extensions.TypedDict, total=False):
    displayName: str
    fullName: str
    providerId: str

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

class PosInventoryRequest(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    gtin: str
    itemId: str
    price: Price
    quantity: str
    storeCode: str
    targetCountry: str
    timestamp: str

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

class PosListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    resources: typing.List[PosStore]

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

class PosStore(typing_extensions.TypedDict, total=False):
    kind: str
    storeAddress: str
    storeCode: str

class PostalCodeGroup(typing_extensions.TypedDict, total=False):
    country: str
    name: str
    postalCodeRanges: typing.List[PostalCodeRange]

class PostalCodeRange(typing_extensions.TypedDict, total=False):
    postalCodeRangeBegin: str
    postalCodeRangeEnd: str

class Price(typing_extensions.TypedDict, total=False):
    currency: str
    value: str

class Product(typing_extensions.TypedDict, total=False):
    additionalImageLinks: typing.List[str]
    additionalProductTypes: typing.List[str]
    adult: bool
    adwordsGrouping: str
    adwordsLabels: typing.List[str]
    adwordsRedirect: str
    ageGroup: str
    aspects: typing.List[ProductAspect]
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
    customGroups: typing.List[CustomGroup]
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    description: str
    destinations: typing.List[ProductDestination]
    displayAdsId: str
    displayAdsLink: str
    displayAdsSimilarIds: typing.List[str]
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
    sizeSystem: str
    sizeType: str
    sizes: typing.List[str]
    source: str
    targetCountry: str
    taxes: typing.List[ProductTax]
    title: str
    unitPricingBaseMeasure: ProductUnitPricingBaseMeasure
    unitPricingMeasure: ProductUnitPricingMeasure
    validatedDestinations: typing.List[str]
    warnings: typing.List[Error]

class ProductAmount(typing_extensions.TypedDict, total=False):
    priceAmount: Price
    remittedTaxAmount: Price
    taxAmount: Price

class ProductAspect(typing_extensions.TypedDict, total=False):
    aspectName: str
    destinationName: str
    intention: str

class ProductDestination(typing_extensions.TypedDict, total=False):
    destinationName: str
    intention: str

class ProductShipping(typing_extensions.TypedDict, total=False):
    country: str
    locationGroupName: str
    locationId: str
    postalCode: str
    price: Price
    region: str
    service: str

class ProductShippingDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

class ProductShippingWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

class ProductStatus(typing_extensions.TypedDict, total=False):
    creationDate: str
    dataQualityIssues: typing.List[ProductStatusDataQualityIssue]
    destinationStatuses: typing.List[ProductStatusDestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: typing.List[ProductStatusItemLevelIssue]
    kind: str
    lastUpdateDate: str
    link: str
    product: Product
    productId: str
    title: str

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

class ProductStatusDestinationStatus(typing_extensions.TypedDict, total=False):
    approvalPending: bool
    approvalStatus: str
    destination: str
    intention: str

class ProductStatusItemLevelIssue(typing_extensions.TypedDict, total=False):
    attributeName: str
    code: str
    description: str
    destination: str
    detail: str
    documentation: str
    resolution: str
    servability: str

class ProductTax(typing_extensions.TypedDict, total=False):
    country: str
    locationId: str
    postalCode: str
    rate: float
    region: str
    taxShip: bool

class ProductUnitPricingBaseMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

class ProductUnitPricingMeasure(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

class ProductsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductsCustomBatchRequestEntry]

class ProductsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    merchantId: str
    method: str
    product: Product
    productId: str

class ProductsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductsCustomBatchResponseEntry]
    kind: str

class ProductsCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str
    product: Product

class ProductsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[Product]

class ProductstatusesCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductstatusesCustomBatchRequestEntry]

class ProductstatusesCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    destinations: typing.List[str]
    includeAttributes: bool
    merchantId: str
    method: str
    productId: str

class ProductstatusesCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ProductstatusesCustomBatchResponseEntry]
    kind: str

class ProductstatusesCustomBatchResponseEntry(typing_extensions.TypedDict, total=False):
    batchId: int
    errors: Errors
    kind: str
    productStatus: ProductStatus

class ProductstatusesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[ProductStatus]

class Promotion(typing_extensions.TypedDict, total=False):
    promotionAmount: Amount
    promotionId: str

class RateGroup(typing_extensions.TypedDict, total=False):
    applicableShippingLabels: typing.List[str]
    carrierRates: typing.List[CarrierRate]
    mainTable: Table
    name: str
    singleValue: Value
    subtables: typing.List[Table]

class RefundReason(typing_extensions.TypedDict, total=False):
    description: str
    reasonCode: str

class ReturnShipment(typing_extensions.TypedDict, total=False):
    creationDate: str
    deliveryDate: str
    returnMethodType: str
    shipmentId: str
    shipmentTrackingInfos: typing.List[ShipmentTrackingInfo]
    shippingDate: str
    state: str

class Row(typing_extensions.TypedDict, total=False):
    cells: typing.List[Value]

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

class ShipmentInvoice(typing_extensions.TypedDict, total=False):
    invoiceSummary: InvoiceSummary
    lineItemInvoices: typing.List[ShipmentInvoiceLineItemInvoice]
    shipmentGroupId: str

class ShipmentInvoiceLineItemInvoice(typing_extensions.TypedDict, total=False):
    lineItemId: str
    productId: str
    shipmentUnitIds: typing.List[str]
    unitInvoice: UnitInvoice

class ShipmentTrackingInfo(typing_extensions.TypedDict, total=False):
    carrier: str
    trackingNumber: str

class ShippingSettings(typing_extensions.TypedDict, total=False):
    accountId: str
    postalCodeGroups: typing.List[PostalCodeGroup]
    services: typing.List[Service]

class ShippingsettingsCustomBatchRequest(typing_extensions.TypedDict, total=False):
    entries: typing.List[ShippingsettingsCustomBatchRequestEntry]

class ShippingsettingsCustomBatchRequestEntry(typing_extensions.TypedDict, total=False):
    accountId: str
    batchId: int
    merchantId: str
    method: str
    shippingSettings: ShippingSettings

class ShippingsettingsCustomBatchResponse(typing_extensions.TypedDict, total=False):
    entries: typing.List[ShippingsettingsCustomBatchResponseEntry]
    kind: str

class ShippingsettingsCustomBatchResponseEntry(
    typing_extensions.TypedDict, total=False
):
    batchId: int
    errors: Errors
    kind: str
    shippingSettings: ShippingSettings

class ShippingsettingsGetSupportedCarriersResponse(
    typing_extensions.TypedDict, total=False
):
    carriers: typing.List[CarriersCarrier]
    kind: str

class ShippingsettingsGetSupportedHolidaysResponse(
    typing_extensions.TypedDict, total=False
):
    holidays: typing.List[HolidaysHoliday]
    kind: str

class ShippingsettingsGetSupportedPickupServicesResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    pickupServices: typing.List[PickupServicesPickupService]

class ShippingsettingsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[ShippingSettings]

class Table(typing_extensions.TypedDict, total=False):
    columnHeaders: Headers
    name: str
    rowHeaders: Headers
    rows: typing.List[Row]

class TestOrder(typing_extensions.TypedDict, total=False):
    customer: TestOrderCustomer
    enableOrderinvoices: bool
    kind: str
    lineItems: typing.List[TestOrderLineItem]
    notificationMode: str
    paymentMethod: TestOrderPaymentMethod
    predefinedDeliveryAddress: str
    predefinedPickupDetails: str
    promotions: typing.List[OrderLegacyPromotion]
    shippingCost: Price
    shippingCostTax: Price
    shippingOption: str

class TestOrderCustomer(typing_extensions.TypedDict, total=False):
    email: str
    explicitMarketingPreference: bool
    fullName: str
    marketingRightsInfo: TestOrderCustomerMarketingRightsInfo

class TestOrderCustomerMarketingRightsInfo(typing_extensions.TypedDict, total=False):
    explicitMarketingPreference: str
    lastUpdatedTimestamp: str

class TestOrderLineItem(typing_extensions.TypedDict, total=False):
    product: TestOrderLineItemProduct
    quantityOrdered: int
    returnInfo: OrderLineItemReturnInfo
    shippingDetails: OrderLineItemShippingDetails
    unitTax: Price

class TestOrderLineItemProduct(typing_extensions.TypedDict, total=False):
    brand: str
    channel: str
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

class TestOrderPaymentMethod(typing_extensions.TypedDict, total=False):
    expirationMonth: int
    expirationYear: int
    lastFourDigits: str
    predefinedBillingAddress: str
    type: str

class TransitTable(typing_extensions.TypedDict, total=False):
    postalCodeGroupNames: typing.List[str]
    rows: typing.List[TransitTableTransitTimeRow]
    transitTimeLabels: typing.List[str]

class TransitTableTransitTimeRow(typing_extensions.TypedDict, total=False):
    values: typing.List[TransitTableTransitTimeRowTransitTimeValue]

class TransitTableTransitTimeRowTransitTimeValue(
    typing_extensions.TypedDict, total=False
):
    maxTransitTimeInDays: int
    minTransitTimeInDays: int

class UnitInvoice(typing_extensions.TypedDict, total=False):
    additionalCharges: typing.List[UnitInvoiceAdditionalCharge]
    promotions: typing.List[Promotion]
    unitPricePretax: Price
    unitPriceTaxes: typing.List[UnitInvoiceTaxLine]

class UnitInvoiceAdditionalCharge(typing_extensions.TypedDict, total=False):
    additionalChargeAmount: Amount
    additionalChargePromotions: typing.List[Promotion]
    type: str

class UnitInvoiceTaxLine(typing_extensions.TypedDict, total=False):
    taxAmount: Price
    taxName: str
    taxType: str

class Value(typing_extensions.TypedDict, total=False):
    carrierRateName: str
    flatRate: Price
    noShipping: bool
    pricePercentage: str
    subtableName: str

class Weight(typing_extensions.TypedDict, total=False):
    unit: str
    value: str
