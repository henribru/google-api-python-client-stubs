import typing

import typing_extensions

class Account(typing_extensions.TypedDict, total=False):
    applyPretargetingToNonGuaranteedDeals: bool
    bidderLocation: typing.List[typing.Dict[str, typing.Any]]
    cookieMatchingNid: str
    cookieMatchingUrl: str
    id: int
    kind: str
    maximumActiveCreatives: int
    maximumTotalQps: int
    numberActiveCreatives: int

class AccountsList(typing_extensions.TypedDict, total=False):
    items: typing.List[Account]
    kind: str

class AddOrderDealsRequest(typing_extensions.TypedDict, total=False):
    deals: typing.List[MarketplaceDeal]
    proposalRevisionNumber: str
    updateAction: str

class AddOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: typing.List[MarketplaceDeal]
    proposalRevisionNumber: str

class AddOrderNotesRequest(typing_extensions.TypedDict, total=False):
    notes: typing.List[MarketplaceNote]

class AddOrderNotesResponse(typing_extensions.TypedDict, total=False):
    notes: typing.List[MarketplaceNote]

class BillingInfo(typing_extensions.TypedDict, total=False):
    accountId: int
    accountName: str
    billingId: typing.List[str]
    kind: str

class BillingInfoList(typing_extensions.TypedDict, total=False):
    items: typing.List[BillingInfo]
    kind: str

class Budget(typing_extensions.TypedDict, total=False):
    accountId: str
    billingId: str
    budgetAmount: str
    currencyCode: str
    id: str
    kind: str

class Buyer(typing_extensions.TypedDict, total=False):
    accountId: str

class ContactInformation(typing_extensions.TypedDict, total=False):
    email: str
    name: str

class CreateOrdersRequest(typing_extensions.TypedDict, total=False):
    proposals: typing.List[Proposal]
    webPropertyCode: str

class CreateOrdersResponse(typing_extensions.TypedDict, total=False):
    proposals: typing.List[Proposal]

class Creative(typing_extensions.TypedDict, total=False):
    HTMLSnippet: str
    accountId: int
    adChoicesDestinationUrl: str
    adTechnologyProviders: typing.Dict[str, typing.Any]
    advertiserId: typing.List[str]
    advertiserName: str
    agencyId: str
    apiUploadTimestamp: str
    attribute: typing.List[int]
    buyerCreativeId: str
    clickThroughUrl: typing.List[str]
    corrections: typing.List[typing.Dict[str, typing.Any]]
    creativeStatusIdentityType: str
    dealsStatus: str
    detectedDomains: typing.List[str]
    filteringReasons: typing.Dict[str, typing.Any]
    height: int
    impressionTrackingUrl: typing.List[str]
    kind: str
    languages: typing.List[str]
    nativeAd: typing.Dict[str, typing.Any]
    openAuctionStatus: str
    productCategories: typing.List[int]
    restrictedCategories: typing.List[int]
    sensitiveCategories: typing.List[int]
    servingRestrictions: typing.List[typing.Dict[str, typing.Any]]
    vendorType: typing.List[int]
    version: int
    videoURL: str
    videoVastXML: str
    width: int

class CreativeDealIds(typing_extensions.TypedDict, total=False):
    dealStatuses: typing.List[typing.Dict[str, typing.Any]]
    kind: str

class CreativesList(typing_extensions.TypedDict, total=False):
    items: typing.List[Creative]
    kind: str
    nextPageToken: str

class DealServingMetadata(typing_extensions.TypedDict, total=False):
    alcoholAdsAllowed: bool
    dealPauseStatus: DealServingMetadataDealPauseStatus

class DealServingMetadataDealPauseStatus(typing_extensions.TypedDict, total=False):
    buyerPauseReason: str
    firstPausedBy: str
    hasBuyerPaused: bool
    hasSellerPaused: bool
    sellerPauseReason: str

class DealTerms(typing_extensions.TypedDict, total=False):
    brandingType: str
    crossListedExternalDealIdType: str
    description: str
    estimatedGrossSpend: Price
    estimatedImpressionsPerDay: str
    guaranteedFixedPriceTerms: DealTermsGuaranteedFixedPriceTerms
    nonGuaranteedAuctionTerms: DealTermsNonGuaranteedAuctionTerms
    nonGuaranteedFixedPriceTerms: DealTermsNonGuaranteedFixedPriceTerms
    rubiconNonGuaranteedTerms: DealTermsRubiconNonGuaranteedTerms
    sellerTimeZone: str

class DealTermsGuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    billingInfo: DealTermsGuaranteedFixedPriceTermsBillingInfo
    fixedPrices: typing.List[PricePerBuyer]
    guaranteedImpressions: str
    guaranteedLooks: str
    minimumDailyLooks: str

class DealTermsGuaranteedFixedPriceTermsBillingInfo(
    typing_extensions.TypedDict, total=False
):
    currencyConversionTimeMs: str
    dfpLineItemId: str
    originalContractedQuantity: str
    price: Price

class DealTermsNonGuaranteedAuctionTerms(typing_extensions.TypedDict, total=False):
    autoOptimizePrivateAuction: bool
    reservePricePerBuyers: typing.List[PricePerBuyer]

class DealTermsNonGuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    fixedPrices: typing.List[PricePerBuyer]

class DealTermsRubiconNonGuaranteedTerms(typing_extensions.TypedDict, total=False):
    priorityPrice: Price
    standardPrice: Price

class DeleteOrderDealsRequest(typing_extensions.TypedDict, total=False):
    dealIds: typing.List[str]
    proposalRevisionNumber: str
    updateAction: str

class DeleteOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: typing.List[MarketplaceDeal]
    proposalRevisionNumber: str

class DeliveryControl(typing_extensions.TypedDict, total=False):
    creativeBlockingLevel: str
    deliveryRateType: str
    frequencyCaps: typing.List[DeliveryControlFrequencyCap]

class DeliveryControlFrequencyCap(typing_extensions.TypedDict, total=False):
    maxImpressions: int
    numTimeUnits: int
    timeUnitType: str

class Dimension(typing_extensions.TypedDict, total=False):
    dimensionType: str
    dimensionValues: typing.List[DimensionDimensionValue]

class DimensionDimensionValue(typing_extensions.TypedDict, total=False):
    id: int
    name: str
    percentage: int

class EditAllOrderDealsRequest(typing_extensions.TypedDict, total=False):
    deals: typing.List[MarketplaceDeal]
    proposal: Proposal
    proposalRevisionNumber: str
    updateAction: str

class EditAllOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: typing.List[MarketplaceDeal]
    orderRevisionNumber: str

class GetOffersResponse(typing_extensions.TypedDict, total=False):
    products: typing.List[Product]

class GetOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: typing.List[MarketplaceDeal]

class GetOrderNotesResponse(typing_extensions.TypedDict, total=False):
    notes: typing.List[MarketplaceNote]

class GetOrdersResponse(typing_extensions.TypedDict, total=False):
    proposals: typing.List[Proposal]

class GetPublisherProfilesByAccountIdResponse(typing_extensions.TypedDict, total=False):
    profiles: typing.List[PublisherProfileApiProto]

class MarketplaceDeal(typing_extensions.TypedDict, total=False):
    buyerPrivateData: PrivateData
    creationTimeMs: str
    creativePreApprovalPolicy: str
    creativeSafeFrameCompatibility: str
    dealId: str
    dealServingMetadata: DealServingMetadata
    deliveryControl: DeliveryControl
    externalDealId: str
    flightEndTimeMs: str
    flightStartTimeMs: str
    inventoryDescription: str
    isRfpTemplate: bool
    isSetupComplete: bool
    kind: str
    lastUpdateTimeMs: str
    makegoodRequestedReason: str
    name: str
    productId: str
    productRevisionNumber: str
    programmaticCreativeSource: str
    proposalId: str
    sellerContacts: typing.List[ContactInformation]
    sharedTargetings: typing.List[SharedTargeting]
    syndicationProduct: str
    terms: DealTerms
    webPropertyCode: str

class MarketplaceDealParty(typing_extensions.TypedDict, total=False):
    buyer: Buyer
    seller: Seller

class MarketplaceLabel(typing_extensions.TypedDict, total=False):
    accountId: str
    createTimeMs: str
    deprecatedMarketplaceDealParty: MarketplaceDealParty
    label: str

class MarketplaceNote(typing_extensions.TypedDict, total=False):
    creatorRole: str
    dealId: str
    kind: str
    note: str
    noteId: str
    proposalId: str
    proposalRevisionNumber: str
    timestampMs: str

class MobileApplication(typing_extensions.TypedDict, total=False):
    appStore: str
    externalAppId: str

class PerformanceReport(typing_extensions.TypedDict, total=False):
    bidRate: float
    bidRequestRate: float
    calloutStatusRate: typing.List[typing.Any]
    cookieMatcherStatusRate: typing.List[typing.Any]
    creativeStatusRate: typing.List[typing.Any]
    filteredBidRate: float
    hostedMatchStatusRate: typing.List[typing.Any]
    inventoryMatchRate: float
    kind: str
    latency50thPercentile: float
    latency85thPercentile: float
    latency95thPercentile: float
    noQuotaInRegion: float
    outOfQuota: float
    pixelMatchRequests: float
    pixelMatchResponses: float
    quotaConfiguredLimit: float
    quotaThrottledLimit: float
    region: str
    successfulRequestRate: float
    timestamp: str
    unsuccessfulRequestRate: float

class PerformanceReportList(typing_extensions.TypedDict, total=False):
    kind: str
    performanceReport: typing.List[PerformanceReport]

class PretargetingConfig(typing_extensions.TypedDict, total=False):
    billingId: str
    configId: str
    configName: str
    creativeType: typing.List[str]
    dimensions: typing.List[typing.Dict[str, typing.Any]]
    excludedContentLabels: typing.List[str]
    excludedGeoCriteriaIds: typing.List[str]
    excludedPlacements: typing.List[typing.Dict[str, typing.Any]]
    excludedUserLists: typing.List[str]
    excludedVerticals: typing.List[str]
    geoCriteriaIds: typing.List[str]
    isActive: bool
    kind: str
    languages: typing.List[str]
    maximumQps: str
    minimumViewabilityDecile: int
    mobileCarriers: typing.List[str]
    mobileDevices: typing.List[str]
    mobileOperatingSystemVersions: typing.List[str]
    placements: typing.List[typing.Dict[str, typing.Any]]
    platforms: typing.List[str]
    supportedCreativeAttributes: typing.List[str]
    userIdentifierDataRequired: typing.List[str]
    userLists: typing.List[str]
    vendorTypes: typing.List[str]
    verticals: typing.List[str]
    videoPlayerSizes: typing.List[typing.Dict[str, typing.Any]]

class PretargetingConfigList(typing_extensions.TypedDict, total=False):
    items: typing.List[PretargetingConfig]
    kind: str

class Price(typing_extensions.TypedDict, total=False):
    amountMicros: float
    currencyCode: str
    expectedCpmMicros: float
    pricingType: str

class PricePerBuyer(typing_extensions.TypedDict, total=False):
    auctionTier: str
    billedBuyer: Buyer
    buyer: Buyer
    price: Price

class PrivateData(typing_extensions.TypedDict, total=False):
    referenceId: str
    referencePayload: str

class Product(typing_extensions.TypedDict, total=False):
    billedBuyer: Buyer
    buyer: Buyer
    creationTimeMs: str
    creatorContacts: typing.List[ContactInformation]
    creatorRole: str
    deliveryControl: DeliveryControl
    flightEndTimeMs: str
    flightStartTimeMs: str
    hasCreatorSignedOff: bool
    inventorySource: str
    kind: str
    labels: typing.List[MarketplaceLabel]
    lastUpdateTimeMs: str
    legacyOfferId: str
    marketplacePublisherProfileId: str
    name: str
    privateAuctionId: str
    productId: str
    publisherProfileId: str
    publisherProvidedForecast: PublisherProvidedForecast
    revisionNumber: str
    seller: Seller
    sharedTargetings: typing.List[SharedTargeting]
    state: str
    syndicationProduct: str
    terms: DealTerms
    webPropertyCode: str

class Proposal(typing_extensions.TypedDict, total=False):
    billedBuyer: Buyer
    buyer: Buyer
    buyerContacts: typing.List[ContactInformation]
    buyerPrivateData: PrivateData
    dbmAdvertiserIds: typing.List[str]
    hasBuyerSignedOff: bool
    hasSellerSignedOff: bool
    inventorySource: str
    isRenegotiating: bool
    isSetupComplete: bool
    kind: str
    labels: typing.List[MarketplaceLabel]
    lastUpdaterOrCommentorRole: str
    name: str
    negotiationId: str
    originatorRole: str
    privateAuctionId: str
    proposalId: str
    proposalState: str
    revisionNumber: str
    revisionTimeMs: str
    seller: Seller
    sellerContacts: typing.List[ContactInformation]

class PublisherProfileApiProto(typing_extensions.TypedDict, total=False):
    audience: str
    buyerPitchStatement: str
    directContact: str
    exchange: str
    googlePlusLink: str
    isParent: bool
    isPublished: bool
    kind: str
    logoUrl: str
    mediaKitLink: str
    name: str
    overview: str
    profileId: int
    programmaticContact: str
    publisherAppIds: typing.List[str]
    publisherApps: typing.List[MobileApplication]
    publisherDomains: typing.List[str]
    publisherProfileId: str
    publisherProvidedForecast: PublisherProvidedForecast
    rateCardInfoLink: str
    samplePageLink: str
    seller: Seller
    state: str
    topHeadlines: typing.List[str]

class PublisherProvidedForecast(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[Dimension]
    weeklyImpressions: str
    weeklyUniques: str

class Seller(typing_extensions.TypedDict, total=False):
    accountId: str
    subAccountId: str

class SharedTargeting(typing_extensions.TypedDict, total=False):
    exclusions: typing.List[TargetingValue]
    inclusions: typing.List[TargetingValue]
    key: str

class TargetingValue(typing_extensions.TypedDict, total=False):
    creativeSizeValue: TargetingValueCreativeSize
    dayPartTargetingValue: TargetingValueDayPartTargeting
    demogAgeCriteriaValue: TargetingValueDemogAgeCriteria
    demogGenderCriteriaValue: TargetingValueDemogGenderCriteria
    longValue: str
    stringValue: str

class TargetingValueCreativeSize(typing_extensions.TypedDict, total=False):
    allowedFormats: typing.List[str]
    companionSizes: typing.List[TargetingValueSize]
    creativeSizeType: str
    nativeTemplate: str
    size: TargetingValueSize
    skippableAdType: str

class TargetingValueDayPartTargeting(typing_extensions.TypedDict, total=False):
    dayParts: typing.List[TargetingValueDayPartTargetingDayPart]
    timeZoneType: str

class TargetingValueDayPartTargetingDayPart(typing_extensions.TypedDict, total=False):
    dayOfWeek: str
    endHour: int
    endMinute: int
    startHour: int
    startMinute: int

class TargetingValueDemogAgeCriteria(typing_extensions.TypedDict, total=False):
    demogAgeCriteriaIds: typing.List[str]

class TargetingValueDemogGenderCriteria(typing_extensions.TypedDict, total=False):
    demogGenderCriteriaIds: typing.List[str]

class TargetingValueSize(typing_extensions.TypedDict, total=False):
    height: int
    width: int

class UpdatePrivateAuctionProposalRequest(typing_extensions.TypedDict, total=False):
    externalDealId: str
    note: MarketplaceNote
    proposalRevisionNumber: str
    updateAction: str
