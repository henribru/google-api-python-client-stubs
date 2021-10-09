import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    applyPretargetingToNonGuaranteedDeals: bool
    bidderLocation: _list[dict[str, typing.Any]]
    cookieMatchingNid: str
    cookieMatchingUrl: str
    id: int
    kind: str
    maximumActiveCreatives: int
    maximumTotalQps: int
    numberActiveCreatives: int

@typing.type_check_only
class AccountsList(typing_extensions.TypedDict, total=False):
    items: _list[Account]
    kind: str

@typing.type_check_only
class AddOrderDealsRequest(typing_extensions.TypedDict, total=False):
    deals: _list[MarketplaceDeal]
    proposalRevisionNumber: str
    updateAction: str

@typing.type_check_only
class AddOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: _list[MarketplaceDeal]
    proposalRevisionNumber: str

@typing.type_check_only
class AddOrderNotesRequest(typing_extensions.TypedDict, total=False):
    notes: _list[MarketplaceNote]

@typing.type_check_only
class AddOrderNotesResponse(typing_extensions.TypedDict, total=False):
    notes: _list[MarketplaceNote]

@typing.type_check_only
class BillingInfo(typing_extensions.TypedDict, total=False):
    accountId: int
    accountName: str
    billingId: _list[str]
    kind: str

@typing.type_check_only
class BillingInfoList(typing_extensions.TypedDict, total=False):
    items: _list[BillingInfo]
    kind: str

@typing.type_check_only
class Budget(typing_extensions.TypedDict, total=False):
    accountId: str
    billingId: str
    budgetAmount: str
    currencyCode: str
    id: str
    kind: str

@typing.type_check_only
class Buyer(typing_extensions.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class ContactInformation(typing_extensions.TypedDict, total=False):
    email: str
    name: str

@typing.type_check_only
class CreateOrdersRequest(typing_extensions.TypedDict, total=False):
    proposals: _list[Proposal]
    webPropertyCode: str

@typing.type_check_only
class CreateOrdersResponse(typing_extensions.TypedDict, total=False):
    proposals: _list[Proposal]

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    HTMLSnippet: str
    accountId: int
    adChoicesDestinationUrl: str
    adTechnologyProviders: dict[str, typing.Any]
    advertiserId: _list[str]
    advertiserName: str
    agencyId: str
    apiUploadTimestamp: str
    attribute: _list[int]
    buyerCreativeId: str
    clickThroughUrl: _list[str]
    corrections: _list[dict[str, typing.Any]]
    creativeStatusIdentityType: str
    dealsStatus: str
    detectedDomains: _list[str]
    filteringReasons: dict[str, typing.Any]
    height: int
    impressionTrackingUrl: _list[str]
    kind: str
    languages: _list[str]
    nativeAd: dict[str, typing.Any]
    openAuctionStatus: str
    productCategories: _list[int]
    restrictedCategories: _list[int]
    sensitiveCategories: _list[int]
    servingRestrictions: _list[dict[str, typing.Any]]
    vendorType: _list[int]
    version: int
    videoURL: str
    videoVastXML: str
    width: int

@typing.type_check_only
class CreativeDealIds(typing_extensions.TypedDict, total=False):
    dealStatuses: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class CreativesList(typing_extensions.TypedDict, total=False):
    items: _list[Creative]
    kind: str
    nextPageToken: str

@typing.type_check_only
class DealServingMetadata(typing_extensions.TypedDict, total=False):
    alcoholAdsAllowed: bool
    dealPauseStatus: DealServingMetadataDealPauseStatus

@typing.type_check_only
class DealServingMetadataDealPauseStatus(typing_extensions.TypedDict, total=False):
    buyerPauseReason: str
    firstPausedBy: str
    hasBuyerPaused: bool
    hasSellerPaused: bool
    sellerPauseReason: str

@typing.type_check_only
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

@typing.type_check_only
class DealTermsGuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    billingInfo: DealTermsGuaranteedFixedPriceTermsBillingInfo
    fixedPrices: _list[PricePerBuyer]
    guaranteedImpressions: str
    guaranteedLooks: str
    minimumDailyLooks: str

@typing.type_check_only
class DealTermsGuaranteedFixedPriceTermsBillingInfo(
    typing_extensions.TypedDict, total=False
):
    currencyConversionTimeMs: str
    dfpLineItemId: str
    originalContractedQuantity: str
    price: Price

@typing.type_check_only
class DealTermsNonGuaranteedAuctionTerms(typing_extensions.TypedDict, total=False):
    autoOptimizePrivateAuction: bool
    reservePricePerBuyers: _list[PricePerBuyer]

@typing.type_check_only
class DealTermsNonGuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    fixedPrices: _list[PricePerBuyer]

@typing.type_check_only
class DealTermsRubiconNonGuaranteedTerms(typing_extensions.TypedDict, total=False):
    priorityPrice: Price
    standardPrice: Price

@typing.type_check_only
class DeleteOrderDealsRequest(typing_extensions.TypedDict, total=False):
    dealIds: _list[str]
    proposalRevisionNumber: str
    updateAction: str

@typing.type_check_only
class DeleteOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: _list[MarketplaceDeal]
    proposalRevisionNumber: str

@typing.type_check_only
class DeliveryControl(typing_extensions.TypedDict, total=False):
    creativeBlockingLevel: str
    deliveryRateType: str
    frequencyCaps: _list[DeliveryControlFrequencyCap]

@typing.type_check_only
class DeliveryControlFrequencyCap(typing_extensions.TypedDict, total=False):
    maxImpressions: int
    numTimeUnits: int
    timeUnitType: str

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    dimensionType: str
    dimensionValues: _list[DimensionDimensionValue]

@typing.type_check_only
class DimensionDimensionValue(typing_extensions.TypedDict, total=False):
    id: int
    name: str
    percentage: int

@typing.type_check_only
class EditAllOrderDealsRequest(typing_extensions.TypedDict, total=False):
    deals: _list[MarketplaceDeal]
    proposal: Proposal
    proposalRevisionNumber: str
    updateAction: str

@typing.type_check_only
class EditAllOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: _list[MarketplaceDeal]
    orderRevisionNumber: str

@typing.type_check_only
class GetOffersResponse(typing_extensions.TypedDict, total=False):
    products: _list[Product]

@typing.type_check_only
class GetOrderDealsResponse(typing_extensions.TypedDict, total=False):
    deals: _list[MarketplaceDeal]

@typing.type_check_only
class GetOrderNotesResponse(typing_extensions.TypedDict, total=False):
    notes: _list[MarketplaceNote]

@typing.type_check_only
class GetOrdersResponse(typing_extensions.TypedDict, total=False):
    proposals: _list[Proposal]

@typing.type_check_only
class GetPublisherProfilesByAccountIdResponse(typing_extensions.TypedDict, total=False):
    profiles: _list[PublisherProfileApiProto]

@typing.type_check_only
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
    sellerContacts: _list[ContactInformation]
    sharedTargetings: _list[SharedTargeting]
    syndicationProduct: str
    terms: DealTerms
    webPropertyCode: str

@typing.type_check_only
class MarketplaceDealParty(typing_extensions.TypedDict, total=False):
    buyer: Buyer
    seller: Seller

@typing.type_check_only
class MarketplaceLabel(typing_extensions.TypedDict, total=False):
    accountId: str
    createTimeMs: str
    deprecatedMarketplaceDealParty: MarketplaceDealParty
    label: str

@typing.type_check_only
class MarketplaceNote(typing_extensions.TypedDict, total=False):
    creatorRole: str
    dealId: str
    kind: str
    note: str
    noteId: str
    proposalId: str
    proposalRevisionNumber: str
    timestampMs: str

@typing.type_check_only
class MobileApplication(typing_extensions.TypedDict, total=False):
    appStore: str
    externalAppId: str

@typing.type_check_only
class PerformanceReport(typing_extensions.TypedDict, total=False):
    bidRate: float
    bidRequestRate: float
    calloutStatusRate: _list[typing.Any]
    cookieMatcherStatusRate: _list[typing.Any]
    creativeStatusRate: _list[typing.Any]
    filteredBidRate: float
    hostedMatchStatusRate: _list[typing.Any]
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

@typing.type_check_only
class PerformanceReportList(typing_extensions.TypedDict, total=False):
    kind: str
    performanceReport: _list[PerformanceReport]

@typing.type_check_only
class PretargetingConfig(typing_extensions.TypedDict, total=False):
    billingId: str
    configId: str
    configName: str
    creativeType: _list[str]
    dimensions: _list[dict[str, typing.Any]]
    excludedContentLabels: _list[str]
    excludedGeoCriteriaIds: _list[str]
    excludedPlacements: _list[dict[str, typing.Any]]
    excludedUserLists: _list[str]
    excludedVerticals: _list[str]
    geoCriteriaIds: _list[str]
    isActive: bool
    kind: str
    languages: _list[str]
    maximumQps: str
    minimumViewabilityDecile: int
    mobileCarriers: _list[str]
    mobileDevices: _list[str]
    mobileOperatingSystemVersions: _list[str]
    placements: _list[dict[str, typing.Any]]
    platforms: _list[str]
    supportedCreativeAttributes: _list[str]
    userIdentifierDataRequired: _list[str]
    userLists: _list[str]
    vendorTypes: _list[str]
    verticals: _list[str]
    videoPlayerSizes: _list[dict[str, typing.Any]]

@typing.type_check_only
class PretargetingConfigList(typing_extensions.TypedDict, total=False):
    items: _list[PretargetingConfig]
    kind: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amountMicros: float
    currencyCode: str
    expectedCpmMicros: float
    pricingType: str

@typing.type_check_only
class PricePerBuyer(typing_extensions.TypedDict, total=False):
    auctionTier: str
    billedBuyer: Buyer
    buyer: Buyer
    price: Price

@typing.type_check_only
class PrivateData(typing_extensions.TypedDict, total=False):
    referenceId: str
    referencePayload: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    billedBuyer: Buyer
    buyer: Buyer
    creationTimeMs: str
    creatorContacts: _list[ContactInformation]
    creatorRole: str
    deliveryControl: DeliveryControl
    flightEndTimeMs: str
    flightStartTimeMs: str
    hasCreatorSignedOff: bool
    inventorySource: str
    kind: str
    labels: _list[MarketplaceLabel]
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
    sharedTargetings: _list[SharedTargeting]
    state: str
    syndicationProduct: str
    terms: DealTerms
    webPropertyCode: str

@typing.type_check_only
class Proposal(typing_extensions.TypedDict, total=False):
    billedBuyer: Buyer
    buyer: Buyer
    buyerContacts: _list[ContactInformation]
    buyerPrivateData: PrivateData
    dbmAdvertiserIds: _list[str]
    hasBuyerSignedOff: bool
    hasSellerSignedOff: bool
    inventorySource: str
    isRenegotiating: bool
    isSetupComplete: bool
    kind: str
    labels: _list[MarketplaceLabel]
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
    sellerContacts: _list[ContactInformation]

@typing.type_check_only
class PublisherProfileApiProto(typing_extensions.TypedDict, total=False):
    audience: str
    buyerPitchStatement: str
    directContact: str
    exchange: str
    forecastInventory: str
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
    publisherAppIds: _list[str]
    publisherApps: _list[MobileApplication]
    publisherDomains: _list[str]
    publisherProfileId: str
    publisherProvidedForecast: PublisherProvidedForecast
    rateCardInfoLink: str
    samplePageLink: str
    seller: Seller
    state: str
    topHeadlines: _list[str]

@typing.type_check_only
class PublisherProvidedForecast(typing_extensions.TypedDict, total=False):
    dimensions: _list[Dimension]
    weeklyImpressions: str
    weeklyUniques: str

@typing.type_check_only
class Seller(typing_extensions.TypedDict, total=False):
    accountId: str
    subAccountId: str

@typing.type_check_only
class SharedTargeting(typing_extensions.TypedDict, total=False):
    exclusions: _list[TargetingValue]
    inclusions: _list[TargetingValue]
    key: str

@typing.type_check_only
class TargetingValue(typing_extensions.TypedDict, total=False):
    creativeSizeValue: TargetingValueCreativeSize
    dayPartTargetingValue: TargetingValueDayPartTargeting
    demogAgeCriteriaValue: TargetingValueDemogAgeCriteria
    demogGenderCriteriaValue: TargetingValueDemogGenderCriteria
    longValue: str
    requestPlatformTargetingValue: TargetingValueRequestPlatformTargeting
    stringValue: str

@typing.type_check_only
class TargetingValueCreativeSize(typing_extensions.TypedDict, total=False):
    allowedFormats: _list[str]
    companionSizes: _list[TargetingValueSize]
    creativeSizeType: str
    nativeTemplate: str
    size: TargetingValueSize
    skippableAdType: str

@typing.type_check_only
class TargetingValueDayPartTargeting(typing_extensions.TypedDict, total=False):
    dayParts: _list[TargetingValueDayPartTargetingDayPart]
    timeZoneType: str

@typing.type_check_only
class TargetingValueDayPartTargetingDayPart(typing_extensions.TypedDict, total=False):
    dayOfWeek: str
    endHour: int
    endMinute: int
    startHour: int
    startMinute: int

@typing.type_check_only
class TargetingValueDemogAgeCriteria(typing_extensions.TypedDict, total=False):
    demogAgeCriteriaIds: _list[str]

@typing.type_check_only
class TargetingValueDemogGenderCriteria(typing_extensions.TypedDict, total=False):
    demogGenderCriteriaIds: _list[str]

@typing.type_check_only
class TargetingValueRequestPlatformTargeting(typing_extensions.TypedDict, total=False):
    requestPlatforms: _list[str]

@typing.type_check_only
class TargetingValueSize(typing_extensions.TypedDict, total=False):
    height: int
    width: int

@typing.type_check_only
class UpdatePrivateAuctionProposalRequest(typing_extensions.TypedDict, total=False):
    externalDealId: str
    note: MarketplaceNote
    proposalRevisionNumber: str
    updateAction: str
