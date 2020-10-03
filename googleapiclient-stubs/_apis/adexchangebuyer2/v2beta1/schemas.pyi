import typing

import typing_extensions

class AppContext(typing_extensions.TypedDict, total=False):
    appTypes: typing.List[str]

class AddDealAssociationRequest(typing_extensions.TypedDict, total=False):
    association: CreativeDealAssociation

class CreativeSize(typing_extensions.TypedDict, total=False):
    creativeSizeType: typing_extensions.Literal[
        "CREATIVE_SIZE_TYPE_UNSPECIFIED", "REGULAR", "INTERSTITIAL", "VIDEO", "NATIVE"
    ]
    companionSizes: typing.List[Size]
    size: Size
    nativeTemplate: typing_extensions.Literal[
        "UNKNOWN_NATIVE_TEMPLATE",
        "NATIVE_CONTENT_AD",
        "NATIVE_APP_INSTALL_AD",
        "NATIVE_VIDEO_CONTENT_AD",
        "NATIVE_VIDEO_APP_INSTALL_AD",
    ]
    allowedFormats: typing.List[str]
    skippableAdType: typing_extensions.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED", "GENERIC", "INSTREAM_SELECT", "NOT_SKIPPABLE"
    ]

class FirstPartyMobileApplicationTargeting(typing_extensions.TypedDict, total=False):
    excludedAppIds: typing.List[str]
    targetedAppIds: typing.List[str]

class Product(typing_extensions.TypedDict, total=False):
    updateTime: str
    creatorContacts: typing.List[ContactInformation]
    seller: Seller
    syndicationProduct: typing_extensions.Literal[
        "SYNDICATION_PRODUCT_UNSPECIFIED", "CONTENT", "MOBILE", "VIDEO", "GAMES"
    ]
    productId: str
    productRevision: str
    hasCreatorSignedOff: bool
    displayName: str
    availableStartTime: str
    availableEndTime: str
    targetingCriterion: typing.List[TargetingCriteria]
    webPropertyCode: str
    publisherProfileId: str
    terms: DealTerms
    createTime: str

class Disapproval(typing_extensions.TypedDict, total=False):
    reason: typing_extensions.Literal[
        "LENGTH_OF_IMAGE_ANIMATION",
        "BROKEN_URL",
        "MEDIA_NOT_FUNCTIONAL",
        "INVALID_FOURTH_PARTY_CALL",
        "INCORRECT_REMARKETING_DECLARATION",
        "LANDING_PAGE_ERROR",
        "AD_SIZE_DOES_NOT_MATCH_AD_SLOT",
        "NO_BORDER",
        "FOURTH_PARTY_BROWSER_COOKIES",
        "LSO_OBJECTS",
        "BLANK_CREATIVE",
        "DESTINATION_URLS_UNDECLARED",
        "PROBLEM_WITH_CLICK_MACRO",
        "INCORRECT_AD_TECHNOLOGY_DECLARATION",
        "INCORRECT_DESTINATION_URL_DECLARATION",
        "EXPANDABLE_INCORRECT_DIRECTION",
        "EXPANDABLE_DIRECTION_NOT_SUPPORTED",
        "EXPANDABLE_INVALID_VENDOR",
        "EXPANDABLE_FUNCTIONALITY",
        "VIDEO_INVALID_VENDOR",
        "VIDEO_UNSUPPORTED_LENGTH",
        "VIDEO_UNSUPPORTED_FORMAT",
        "VIDEO_FUNCTIONALITY",
        "LANDING_PAGE_DISABLED",
        "MALWARE_SUSPECTED",
        "ADULT_IMAGE_OR_VIDEO",
        "INACCURATE_AD_TEXT",
        "COUNTERFEIT_DESIGNER_GOODS",
        "POP_UP",
        "INVALID_RTB_PROTOCOL_USAGE",
        "RAW_IP_ADDRESS_IN_SNIPPET",
        "UNACCEPTABLE_CONTENT_SOFTWARE",
        "UNAUTHORIZED_COOKIE_ON_GOOGLE_DOMAIN",
        "UNDECLARED_FLASH_OBJECTS",
        "INVALID_SSL_DECLARATION",
        "DIRECT_DOWNLOAD_IN_AD",
        "MAXIMUM_DOWNLOAD_SIZE_EXCEEDED",
        "DESTINATION_URL_SITE_NOT_CRAWLABLE",
        "BAD_URL_LEGAL_DISAPPROVAL",
        "PHARMA_GAMBLING_ALCOHOL_NOT_ALLOWED",
        "DYNAMIC_DNS_AT_DESTINATION_URL",
        "POOR_IMAGE_OR_VIDEO_QUALITY",
        "UNACCEPTABLE_IMAGE_CONTENT",
        "INCORRECT_IMAGE_LAYOUT",
        "IRRELEVANT_IMAGE_OR_VIDEO",
        "DESTINATION_SITE_DOES_NOT_ALLOW_GOING_BACK",
        "MISLEADING_CLAIMS_IN_AD",
        "RESTRICTED_PRODUCTS",
        "UNACCEPTABLE_CONTENT",
        "AUTOMATED_AD_CLICKING",
        "INVALID_URL_PROTOCOL",
        "UNDECLARED_RESTRICTED_CONTENT",
        "INVALID_REMARKETING_LIST_USAGE",
        "DESTINATION_SITE_NOT_CRAWLABLE_ROBOTS_TXT",
        "CLICK_TO_DOWNLOAD_NOT_AN_APP",
        "INACCURATE_REVIEW_EXTENSION",
        "SEXUALLY_EXPLICIT_CONTENT",
        "GAINING_AN_UNFAIR_ADVANTAGE",
        "GAMING_THE_GOOGLE_NETWORK",
        "DANGEROUS_PRODUCTS_KNIVES",
        "DANGEROUS_PRODUCTS_EXPLOSIVES",
        "DANGEROUS_PRODUCTS_GUNS",
        "DANGEROUS_PRODUCTS_DRUGS",
        "DANGEROUS_PRODUCTS_TOBACCO",
        "DANGEROUS_PRODUCTS_WEAPONS",
        "UNCLEAR_OR_IRRELEVANT_AD",
        "PROFESSIONAL_STANDARDS",
        "DYSFUNCTIONAL_PROMOTION",
        "INVALID_INTEREST_BASED_AD",
        "MISUSE_OF_PERSONAL_INFORMATION",
        "OMISSION_OF_RELEVANT_INFORMATION",
        "UNAVAILABLE_PROMOTIONS",
        "MISLEADING_PROMOTIONS",
        "INAPPROPRIATE_CONTENT",
        "SENSITIVE_EVENTS",
        "SHOCKING_CONTENT",
        "ENABLING_DISHONEST_BEHAVIOR",
        "TECHNICAL_REQUIREMENTS",
        "RESTRICTED_POLITICAL_CONTENT",
        "UNSUPPORTED_CONTENT",
        "INVALID_BIDDING_METHOD",
        "VIDEO_TOO_LONG",
        "VIOLATES_JAPANESE_PHARMACY_LAW",
        "UNACCREDITED_PET_PHARMACY",
        "ABORTION",
        "CONTRACEPTIVES",
        "NEED_CERTIFICATES_TO_ADVERTISE_IN_CHINA",
        "KCDSP_REGISTRATION",
        "NOT_FAMILY_SAFE",
        "CLINICAL_TRIAL_RECRUITMENT",
        "MAXIMUM_NUMBER_OF_HTTP_CALLS_EXCEEDED",
        "MAXIMUM_NUMBER_OF_COOKIES_EXCEEDED",
        "PERSONAL_LOANS",
        "UNSUPPORTED_FLASH_CONTENT",
        "MISUSE_BY_OMID_SCRIPT",
        "NON_WHITELISTED_OMID_VENDOR",
        "DESTINATION_EXPERIENCE",
        "UNSUPPORTED_LANGUAGE",
        "NON_SSL_COMPLIANT",
        "TEMPORARY_PAUSE",
        "BAIL_BONDS",
        "EXPERIMENTAL_MEDICAL_TREATMENT",
    ]
    details: typing.List[str]

class Price(typing_extensions.TypedDict, total=False):
    pricingType: typing_extensions.Literal[
        "PRICING_TYPE_UNSPECIFIED", "COST_PER_MILLE", "COST_PER_DAY"
    ]
    amount: Money

class ListFilterSetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    filterSets: typing.List[FilterSet]

class ListClientsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    clients: typing.List[Client]

class CreativeDealAssociation(typing_extensions.TypedDict, total=False):
    accountId: str
    dealsId: str
    creativeId: str

class CalloutStatusRow(typing_extensions.TypedDict, total=False):
    calloutStatusId: int
    impressionCount: MetricValue
    rowDimensions: RowDimensions

class ListBidMetricsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    bidMetricsRows: typing.List[BidMetricsRow]

class ListPublisherProfilesResponse(typing_extensions.TypedDict, total=False):
    publisherProfiles: typing.List[PublisherProfile]
    nextPageToken: str

class TargetingValue(typing_extensions.TypedDict, total=False):
    stringValue: str
    longValue: str
    dayPartTargetingValue: DayPartTargeting
    creativeSizeValue: CreativeSize

class Note(typing_extensions.TypedDict, total=False):
    proposalRevision: str
    createTime: str
    note: str
    noteId: str
    creatorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]

class Size(typing_extensions.TypedDict, total=False):
    height: int
    width: int

class FilteredBidDetailRow(typing_extensions.TypedDict, total=False):
    detail: str
    rowDimensions: RowDimensions
    detailId: int
    bidCount: MetricValue

class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

class RemoveDealAssociationRequest(typing_extensions.TypedDict, total=False):
    association: CreativeDealAssociation

class SecurityContext(typing_extensions.TypedDict, total=False):
    securities: typing.List[str]

class TechnologyTargeting(typing_extensions.TypedDict, total=False):
    deviceCategoryTargeting: CriteriaTargeting
    operatingSystemTargeting: OperatingSystemTargeting
    deviceCapabilityTargeting: CriteriaTargeting

class AddNoteRequest(typing_extensions.TypedDict, total=False):
    note: Note

class TimeInterval(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

class Correction(typing_extensions.TypedDict, total=False):
    details: typing.List[str]
    contexts: typing.List[ServingContext]
    type: typing_extensions.Literal[
        "CORRECTION_TYPE_UNSPECIFIED",
        "VENDOR_IDS_ADDED",
        "SSL_ATTRIBUTE_REMOVED",
        "FLASH_FREE_ATTRIBUTE_REMOVED",
        "FLASH_FREE_ATTRIBUTE_ADDED",
        "REQUIRED_ATTRIBUTE_ADDED",
        "REQUIRED_VENDOR_ADDED",
        "SSL_ATTRIBUTE_ADDED",
        "IN_BANNER_VIDEO_ATTRIBUTE_ADDED",
        "MRAID_ATTRIBUTE_ADDED",
        "FLASH_ATTRIBUTE_REMOVED",
        "VIDEO_IN_SNIPPET_ATTRIBUTE_ADDED",
    ]

class MarketplaceTargeting(typing_extensions.TypedDict, total=False):
    placementTargeting: PlacementTargeting
    inventorySizeTargeting: InventorySizeTargeting
    geoTargeting: CriteriaTargeting
    technologyTargeting: TechnologyTargeting
    videoTargeting: VideoTargeting

class PrivateData(typing_extensions.TypedDict, total=False):
    referenceId: str

class AuctionContext(typing_extensions.TypedDict, total=False):
    auctionTypes: typing.List[str]

class MobileApplicationTargeting(typing_extensions.TypedDict, total=False):
    firstPartyTargeting: FirstPartyMobileApplicationTargeting

class VideoContent(typing_extensions.TypedDict, total=False):
    videoUrl: str
    videoVastXml: str

class ListProposalsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    proposals: typing.List[Proposal]

class CancelNegotiationRequest(typing_extensions.TypedDict, total=False): ...

class FilteredBidCreativeRow(typing_extensions.TypedDict, total=False):
    rowDimensions: RowDimensions
    creativeId: str
    bidCount: MetricValue

class ServingRestriction(typing_extensions.TypedDict, total=False):
    disapproval: Disapproval
    disapprovalReasons: typing.List[Disapproval]
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "DISAPPROVAL", "PENDING_REVIEW"
    ]
    contexts: typing.List[ServingContext]

class ListLosingBidsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    creativeStatusRows: typing.List[CreativeStatusRow]

class VideoTargeting(typing_extensions.TypedDict, total=False):
    targetedPositionTypes: typing.List[str]
    excludedPositionTypes: typing.List[str]

class Buyer(typing_extensions.TypedDict, total=False):
    accountId: str

class RelativeDateRange(typing_extensions.TypedDict, total=False):
    durationDays: int
    offsetDays: int

class DealServingMetadata(typing_extensions.TypedDict, total=False):
    dealPauseStatus: DealPauseStatus

class Creative(typing_extensions.TypedDict, total=False):
    accountId: str
    creativeId: str
    detectedSensitiveCategories: typing.List[int]
    restrictedCategories: typing.List[str]
    dealsStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_CHECKED",
        "CONDITIONALLY_APPROVED",
        "APPROVED",
        "DISAPPROVED",
        "PENDING_REVIEW",
        "STATUS_TYPE_UNSPECIFIED",
    ]
    openAuctionStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_CHECKED",
        "CONDITIONALLY_APPROVED",
        "APPROVED",
        "DISAPPROVED",
        "PENDING_REVIEW",
        "STATUS_TYPE_UNSPECIFIED",
    ]
    advertiserName: str
    detectedLanguages: typing.List[str]
    vendorIds: typing.List[int]
    impressionTrackingUrls: typing.List[str]
    detectedDomains: typing.List[str]
    clickThroughUrls: typing.List[str]
    detectedAdvertiserIds: typing.List[str]
    declaredClickThroughUrls: typing.List[str]
    html: HtmlContent
    adChoicesDestinationUrl: str
    native: NativeContent
    agencyId: str
    apiUpdateTime: str
    adTechnologyProviders: AdTechnologyProviders
    attributes: typing.List[str]
    version: int
    corrections: typing.List[Correction]
    detectedProductCategories: typing.List[int]
    servingRestrictions: typing.List[ServingRestriction]
    video: VideoContent

class ListClientUserInvitationsResponse(typing_extensions.TypedDict, total=False):
    invitations: typing.List[ClientUserInvitation]
    nextPageToken: str

class PauseProposalRequest(typing_extensions.TypedDict, total=False):
    reason: str

class DayPart(typing_extensions.TypedDict, total=False):
    endTime: TimeOfDay
    dayOfWeek: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    startTime: TimeOfDay

class ServingContext(typing_extensions.TypedDict, total=False):
    all: typing_extensions.Literal["SIMPLE_CONTEXT"]
    securityType: SecurityContext
    location: LocationContext
    platform: PlatformContext
    appType: AppContext
    auctionType: AuctionContext

class PlacementTargeting(typing_extensions.TypedDict, total=False):
    urlTargeting: UrlTargeting
    mobileApplicationTargeting: MobileApplicationTargeting

class InventorySizeTargeting(typing_extensions.TypedDict, total=False):
    targetedInventorySizes: typing.List[AdSize]
    excludedInventorySizes: typing.List[AdSize]

class RealtimeTimeRange(typing_extensions.TypedDict, total=False):
    startTimestamp: str

class AcceptProposalRequest(typing_extensions.TypedDict, total=False):
    proposalRevision: str

class DealPauseStatus(typing_extensions.TypedDict, total=False):
    firstPausedBy: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    buyerPauseReason: str
    hasBuyerPaused: bool
    hasSellerPaused: bool
    sellerPauseReason: str

class BidMetricsRow(typing_extensions.TypedDict, total=False):
    impressionsWon: MetricValue
    viewableImpressions: MetricValue
    bidsInAuction: MetricValue
    reachedQueries: MetricValue
    billedImpressions: MetricValue
    bids: MetricValue
    measurableImpressions: MetricValue
    rowDimensions: RowDimensions

class CreativeRestrictions(typing_extensions.TypedDict, total=False):
    creativeSpecifications: typing.List[CreativeSpecification]
    skippableAdType: typing_extensions.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED", "SKIPPABLE", "INSTREAM_SELECT", "NOT_SKIPPABLE"
    ]
    creativeFormat: typing_extensions.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "DISPLAY", "VIDEO"
    ]

class ListCreativeStatusBreakdownByDetailResponse(
    typing_extensions.TypedDict, total=False
):
    detailType: typing_extensions.Literal[
        "DETAIL_TYPE_UNSPECIFIED",
        "CREATIVE_ATTRIBUTE",
        "VENDOR",
        "SENSITIVE_CATEGORY",
        "PRODUCT_CATEGORY",
        "DISAPPROVAL_REASON",
        "POLICY_TOPIC",
    ]
    filteredBidDetailRows: typing.List[FilteredBidDetailRow]
    nextPageToken: str

class NativeContent(typing_extensions.TypedDict, total=False):
    body: str
    videoUrl: str
    appIcon: Image
    starRating: float
    clickLinkUrl: str
    logo: Image
    advertiserName: str
    storeUrl: str
    headline: str
    clickTrackingUrl: str
    image: Image
    callToAction: str
    priceDisplayText: str

class AdSize(typing_extensions.TypedDict, total=False):
    height: str
    width: str
    sizeType: typing_extensions.Literal[
        "SIZE_TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"
    ]

class ListBidResponsesWithoutBidsResponse(typing_extensions.TypedDict, total=False):
    bidResponseWithoutBidsStatusRows: typing.List[BidResponseWithoutBidsStatusRow]
    nextPageToken: str

class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    nanos: int
    minutes: int
    seconds: int

class PricePerBuyer(typing_extensions.TypedDict, total=False):
    price: Price
    buyer: Buyer
    advertiserIds: typing.List[str]

class OperatingSystemTargeting(typing_extensions.TypedDict, total=False):
    operatingSystemCriteria: CriteriaTargeting
    operatingSystemVersionCriteria: CriteriaTargeting

class UrlTargeting(typing_extensions.TypedDict, total=False):
    excludedUrls: typing.List[str]
    targetedUrls: typing.List[str]

class ClientUser(typing_extensions.TypedDict, total=False):
    userId: str
    email: str
    status: typing_extensions.Literal[
        "USER_STATUS_UNSPECIFIED", "PENDING", "ACTIVE", "DISABLED"
    ]
    clientAccountId: str

class ClientUserInvitation(typing_extensions.TypedDict, total=False):
    invitationId: str
    clientAccountId: str
    email: str

class Client(typing_extensions.TypedDict, total=False):
    entityType: typing_extensions.Literal[
        "ENTITY_TYPE_UNSPECIFIED",
        "ADVERTISER",
        "BRAND",
        "AGENCY",
        "ENTITY_TYPE_UNCLASSIFIED",
    ]
    partnerClientId: str
    visibleToSeller: bool
    entityId: str
    status: typing_extensions.Literal["CLIENT_STATUS_UNSPECIFIED", "DISABLED", "ACTIVE"]
    entityName: str
    role: typing_extensions.Literal[
        "CLIENT_ROLE_UNSPECIFIED",
        "CLIENT_DEAL_VIEWER",
        "CLIENT_DEAL_NEGOTIATOR",
        "CLIENT_DEAL_APPROVER",
    ]
    clientAccountId: str
    clientName: str

class NonBillableWinningBidStatusRow(typing_extensions.TypedDict, total=False):
    rowDimensions: RowDimensions
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "AD_NOT_RENDERED",
        "INVALID_IMPRESSION",
        "FATAL_VAST_ERROR",
        "LOST_IN_MEDIATION",
    ]
    bidCount: MetricValue

class AdTechnologyProviders(typing_extensions.TypedDict, total=False):
    hasUnidentifiedProvider: bool
    detectedProviderIds: typing.List[str]

class DayPartTargeting(typing_extensions.TypedDict, total=False):
    dayParts: typing.List[DayPart]
    timeZoneType: typing_extensions.Literal[
        "TIME_ZONE_SOURCE_UNSPECIFIED", "PUBLISHER", "USER"
    ]

class StopWatchingCreativeRequest(typing_extensions.TypedDict, total=False): ...

class WatchCreativeRequest(typing_extensions.TypedDict, total=False):
    topic: str

class ImpressionMetricsRow(typing_extensions.TypedDict, total=False):
    successfulResponses: MetricValue
    inventoryMatches: MetricValue
    responsesWithBids: MetricValue
    rowDimensions: RowDimensions
    bidRequests: MetricValue
    availableImpressions: MetricValue

class CreativeSpecification(typing_extensions.TypedDict, total=False):
    creativeSize: AdSize
    creativeCompanionSizes: typing.List[AdSize]

class GuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    guaranteedLooks: str
    guaranteedImpressions: str
    minimumDailyLooks: str
    fixedPrices: typing.List[PricePerBuyer]

class AbsoluteDateRange(typing_extensions.TypedDict, total=False):
    startDate: Date
    endDate: Date

class LocationContext(typing_extensions.TypedDict, total=False):
    geoCriteriaIds: typing.List[int]

class ListCreativesResponse(typing_extensions.TypedDict, total=False):
    creatives: typing.List[Creative]
    nextPageToken: str

class DeliveryControl(typing_extensions.TypedDict, total=False):
    creativeBlockingLevel: typing_extensions.Literal[
        "CREATIVE_BLOCKING_LEVEL_UNSPECIFIED",
        "PUBLISHER_BLOCKING_RULES",
        "ADX_POLICY_BLOCKING_ONLY",
    ]
    frequencyCaps: typing.List[FrequencyCap]
    deliveryRateType: typing_extensions.Literal[
        "DELIVERY_RATE_TYPE_UNSPECIFIED",
        "EVENLY",
        "FRONT_LOADED",
        "AS_FAST_AS_POSSIBLE",
    ]

class CompleteSetupRequest(typing_extensions.TypedDict, total=False): ...

class ListProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: typing.List[Product]

class ListBidResponseErrorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    calloutStatusRows: typing.List[CalloutStatusRow]

class TargetingCriteria(typing_extensions.TypedDict, total=False):
    inclusions: typing.List[TargetingValue]
    exclusions: typing.List[TargetingValue]
    key: str

class FilterSet(typing_extensions.TypedDict, total=False):
    sellerNetworkIds: typing.List[int]
    absoluteDateRange: AbsoluteDateRange
    name: str
    relativeDateRange: RelativeDateRange
    dealId: str
    formats: typing.List[str]
    environment: typing_extensions.Literal["ENVIRONMENT_UNSPECIFIED", "WEB", "APP"]
    realtimeTimeRange: RealtimeTimeRange
    timeSeriesGranularity: typing_extensions.Literal[
        "TIME_SERIES_GRANULARITY_UNSPECIFIED", "HOURLY", "DAILY"
    ]
    publisherIdentifiers: typing.List[str]
    platforms: typing.List[str]
    creativeId: str
    breakdownDimensions: typing.List[str]
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED",
        "NATIVE_DISPLAY",
        "NATIVE_VIDEO",
        "NON_NATIVE_DISPLAY",
        "NON_NATIVE_VIDEO",
    ]

class PublisherProfile(typing_extensions.TypedDict, total=False):
    topHeadlines: typing.List[str]
    programmaticDealsContact: str
    seller: Seller
    isParent: bool
    logoUrl: str
    rateCardInfoUrl: str
    domains: typing.List[str]
    googlePlusUrl: str
    buyerPitchStatement: str
    directDealsContact: str
    overview: str
    samplePageUrl: str
    mediaKitUrl: str
    publisherProfileId: str
    audienceDescription: str
    displayName: str

class Deal(typing_extensions.TypedDict, total=False):
    displayName: str
    description: str
    programmaticCreativeSource: typing_extensions.Literal[
        "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED", "ADVERTISER", "PUBLISHER"
    ]
    availableEndTime: str
    proposalId: str
    sellerContacts: typing.List[ContactInformation]
    externalDealId: str
    availableStartTime: str
    creativeRestrictions: CreativeRestrictions
    createTime: str
    buyerPrivateData: PrivateData
    creativeSafeFrameCompatibility: typing_extensions.Literal[
        "CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    createProductRevision: str
    dealServingMetadata: DealServingMetadata
    syndicationProduct: typing_extensions.Literal[
        "SYNDICATION_PRODUCT_UNSPECIFIED", "CONTENT", "MOBILE", "VIDEO", "GAMES"
    ]
    updateTime: str
    dealTerms: DealTerms
    creativePreApprovalPolicy: typing_extensions.Literal[
        "CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED",
        "SELLER_PRE_APPROVAL_REQUIRED",
        "SELLER_PRE_APPROVAL_NOT_REQUIRED",
    ]
    targetingCriterion: typing.List[TargetingCriteria]
    webPropertyCode: str
    createProductId: str
    isSetupComplete: bool
    dealId: str
    targeting: MarketplaceTargeting
    deliveryControl: DeliveryControl

class ListClientUsersResponse(typing_extensions.TypedDict, total=False):
    users: typing.List[ClientUser]
    nextPageToken: str

class BidResponseWithoutBidsStatusRow(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "RESPONSES_WITHOUT_BIDS",
        "RESPONSES_WITHOUT_BIDS_FOR_ACCOUNT",
        "RESPONSES_WITHOUT_BIDS_FOR_DEAL",
    ]
    impressionCount: MetricValue
    rowDimensions: RowDimensions

class Image(typing_extensions.TypedDict, total=False):
    url: str
    height: int
    width: int

class RowDimensions(typing_extensions.TypedDict, total=False):
    timeInterval: TimeInterval
    publisherIdentifier: str

class ResumeProposalRequest(typing_extensions.TypedDict, total=False): ...

class NonGuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    fixedPrices: typing.List[PricePerBuyer]

class DealTerms(typing_extensions.TypedDict, total=False):
    estimatedGrossSpend: Price
    sellerTimeZone: str
    brandingType: typing_extensions.Literal[
        "BRANDING_TYPE_UNSPECIFIED", "BRANDED", "SEMI_TRANSPARENT"
    ]
    nonGuaranteedAuctionTerms: NonGuaranteedAuctionTerms
    nonGuaranteedFixedPriceTerms: NonGuaranteedFixedPriceTerms
    estimatedImpressionsPerDay: str
    description: str
    guaranteedFixedPriceTerms: GuaranteedFixedPriceTerms

class ListDealAssociationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    associations: typing.List[CreativeDealAssociation]

class FrequencyCap(typing_extensions.TypedDict, total=False):
    maxImpressions: int
    timeUnitType: typing_extensions.Literal[
        "TIME_UNIT_TYPE_UNSPECIFIED",
        "MINUTE",
        "HOUR",
        "DAY",
        "WEEK",
        "MONTH",
        "LIFETIME",
    ]
    numTimeUnits: int

class PlatformContext(typing_extensions.TypedDict, total=False):
    platforms: typing.List[str]

class ListImpressionMetricsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    impressionMetricsRows: typing.List[ImpressionMetricsRow]

class MetricValue(typing_extensions.TypedDict, total=False):
    variance: str
    value: str

class Proposal(typing_extensions.TypedDict, total=False):
    buyerPrivateData: PrivateData
    proposalId: str
    isSetupComplete: bool
    originatorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    displayName: str
    buyer: Buyer
    isRenegotiating: bool
    deals: typing.List[Deal]
    billedBuyer: Buyer
    seller: Seller
    notes: typing.List[Note]
    buyerContacts: typing.List[ContactInformation]
    privateAuctionId: str
    updateTime: str
    sellerContacts: typing.List[ContactInformation]
    proposalRevision: str
    proposalState: typing_extensions.Literal[
        "PROPOSAL_STATE_UNSPECIFIED",
        "PROPOSED",
        "BUYER_ACCEPTED",
        "SELLER_ACCEPTED",
        "CANCELED",
        "FINALIZED",
    ]
    lastUpdaterOrCommentorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]

class Empty(typing_extensions.TypedDict, total=False): ...

class CriteriaTargeting(typing_extensions.TypedDict, total=False):
    excludedCriteriaIds: typing.List[str]
    targetedCriteriaIds: typing.List[str]

class ListNonBillableWinningBidsResponse(typing_extensions.TypedDict, total=False):
    nonBillableWinningBidStatusRows: typing.List[NonBillableWinningBidStatusRow]
    nextPageToken: str

class ListFilteredBidsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    creativeStatusRows: typing.List[CreativeStatusRow]

class HtmlContent(typing_extensions.TypedDict, total=False):
    width: int
    snippet: str
    height: int

class Seller(typing_extensions.TypedDict, total=False):
    accountId: str
    subAccountId: str

class ContactInformation(typing_extensions.TypedDict, total=False):
    email: str
    name: str

class NonGuaranteedAuctionTerms(typing_extensions.TypedDict, total=False):
    reservePricesPerBuyer: typing.List[PricePerBuyer]
    autoOptimizePrivateAuction: bool

class ListFilteredBidRequestsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    calloutStatusRows: typing.List[CalloutStatusRow]

class CreativeStatusRow(typing_extensions.TypedDict, total=False):
    rowDimensions: RowDimensions
    creativeStatusId: int
    bidCount: MetricValue

class ListCreativeStatusBreakdownByCreativeResponse(
    typing_extensions.TypedDict, total=False
):
    filteredBidCreativeRows: typing.List[FilteredBidCreativeRow]
    nextPageToken: str
