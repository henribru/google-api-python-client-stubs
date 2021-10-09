import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbsoluteDateRange(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class AcceptProposalRequest(typing_extensions.TypedDict, total=False):
    proposalRevision: str

@typing.type_check_only
class AdSize(typing_extensions.TypedDict, total=False):
    height: str
    sizeType: typing_extensions.Literal[
        "SIZE_TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"
    ]
    width: str

@typing.type_check_only
class AdTechnologyProviders(typing_extensions.TypedDict, total=False):
    detectedProviderIds: _list[str]
    hasUnidentifiedProvider: bool

@typing.type_check_only
class AddDealAssociationRequest(typing_extensions.TypedDict, total=False):
    association: CreativeDealAssociation

@typing.type_check_only
class AddNoteRequest(typing_extensions.TypedDict, total=False):
    note: Note

@typing.type_check_only
class AppContext(typing_extensions.TypedDict, total=False):
    appTypes: _list[str]

@typing.type_check_only
class AuctionContext(typing_extensions.TypedDict, total=False):
    auctionTypes: _list[str]

@typing.type_check_only
class BidMetricsRow(typing_extensions.TypedDict, total=False):
    bids: MetricValue
    bidsInAuction: MetricValue
    billedImpressions: MetricValue
    impressionsWon: MetricValue
    measurableImpressions: MetricValue
    reachedQueries: MetricValue
    rowDimensions: RowDimensions
    viewableImpressions: MetricValue

@typing.type_check_only
class BidResponseWithoutBidsStatusRow(typing_extensions.TypedDict, total=False):
    impressionCount: MetricValue
    rowDimensions: RowDimensions
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "RESPONSES_WITHOUT_BIDS",
        "RESPONSES_WITHOUT_BIDS_FOR_ACCOUNT",
        "RESPONSES_WITHOUT_BIDS_FOR_DEAL",
    ]

@typing.type_check_only
class Buyer(typing_extensions.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class CalloutStatusRow(typing_extensions.TypedDict, total=False):
    calloutStatusId: int
    impressionCount: MetricValue
    rowDimensions: RowDimensions

@typing.type_check_only
class CancelNegotiationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Client(typing_extensions.TypedDict, total=False):
    clientAccountId: str
    clientName: str
    entityId: str
    entityName: str
    entityType: typing_extensions.Literal[
        "ENTITY_TYPE_UNSPECIFIED",
        "ADVERTISER",
        "BRAND",
        "AGENCY",
        "ENTITY_TYPE_UNCLASSIFIED",
    ]
    partnerClientId: str
    role: typing_extensions.Literal[
        "CLIENT_ROLE_UNSPECIFIED",
        "CLIENT_DEAL_VIEWER",
        "CLIENT_DEAL_NEGOTIATOR",
        "CLIENT_DEAL_APPROVER",
    ]
    status: typing_extensions.Literal["CLIENT_STATUS_UNSPECIFIED", "DISABLED", "ACTIVE"]
    visibleToSeller: bool

@typing.type_check_only
class ClientUser(typing_extensions.TypedDict, total=False):
    clientAccountId: str
    email: str
    status: typing_extensions.Literal[
        "USER_STATUS_UNSPECIFIED", "PENDING", "ACTIVE", "DISABLED"
    ]
    userId: str

@typing.type_check_only
class ClientUserInvitation(typing_extensions.TypedDict, total=False):
    clientAccountId: str
    email: str
    invitationId: str

@typing.type_check_only
class CompleteSetupRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ContactInformation(typing_extensions.TypedDict, total=False):
    email: str
    name: str

@typing.type_check_only
class Correction(typing_extensions.TypedDict, total=False):
    contexts: _list[ServingContext]
    details: _list[str]
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

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    accountId: str
    adChoicesDestinationUrl: str
    adTechnologyProviders: AdTechnologyProviders
    advertiserName: str
    agencyId: str
    apiUpdateTime: str
    attributes: _list[str]
    clickThroughUrls: _list[str]
    corrections: _list[Correction]
    creativeId: str
    dealsStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_CHECKED",
        "CONDITIONALLY_APPROVED",
        "APPROVED",
        "DISAPPROVED",
        "PENDING_REVIEW",
        "STATUS_TYPE_UNSPECIFIED",
    ]
    declaredClickThroughUrls: _list[str]
    detectedAdvertiserIds: _list[str]
    detectedDomains: _list[str]
    detectedLanguages: _list[str]
    detectedProductCategories: _list[int]
    detectedSensitiveCategories: _list[int]
    html: HtmlContent
    impressionTrackingUrls: _list[str]
    native: NativeContent
    openAuctionStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_CHECKED",
        "CONDITIONALLY_APPROVED",
        "APPROVED",
        "DISAPPROVED",
        "PENDING_REVIEW",
        "STATUS_TYPE_UNSPECIFIED",
    ]
    restrictedCategories: _list[str]
    servingRestrictions: _list[ServingRestriction]
    vendorIds: _list[int]
    version: int
    video: VideoContent

@typing.type_check_only
class CreativeDealAssociation(typing_extensions.TypedDict, total=False):
    accountId: str
    creativeId: str
    dealsId: str

@typing.type_check_only
class CreativeRestrictions(typing_extensions.TypedDict, total=False):
    creativeFormat: typing_extensions.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "DISPLAY", "VIDEO"
    ]
    creativeSpecifications: _list[CreativeSpecification]
    skippableAdType: typing_extensions.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED", "SKIPPABLE", "INSTREAM_SELECT", "NOT_SKIPPABLE"
    ]

@typing.type_check_only
class CreativeSize(typing_extensions.TypedDict, total=False):
    allowedFormats: _list[str]
    companionSizes: _list[Size]
    creativeSizeType: typing_extensions.Literal[
        "CREATIVE_SIZE_TYPE_UNSPECIFIED", "REGULAR", "INTERSTITIAL", "VIDEO", "NATIVE"
    ]
    nativeTemplate: typing_extensions.Literal[
        "UNKNOWN_NATIVE_TEMPLATE",
        "NATIVE_CONTENT_AD",
        "NATIVE_APP_INSTALL_AD",
        "NATIVE_VIDEO_CONTENT_AD",
        "NATIVE_VIDEO_APP_INSTALL_AD",
    ]
    size: Size
    skippableAdType: typing_extensions.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED", "GENERIC", "INSTREAM_SELECT", "NOT_SKIPPABLE"
    ]

@typing.type_check_only
class CreativeSpecification(typing_extensions.TypedDict, total=False):
    creativeCompanionSizes: _list[AdSize]
    creativeSize: AdSize

@typing.type_check_only
class CreativeStatusRow(typing_extensions.TypedDict, total=False):
    bidCount: MetricValue
    creativeStatusId: int
    rowDimensions: RowDimensions

@typing.type_check_only
class CriteriaTargeting(typing_extensions.TypedDict, total=False):
    excludedCriteriaIds: _list[str]
    targetedCriteriaIds: _list[str]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DayPart(typing_extensions.TypedDict, total=False):
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
    endTime: TimeOfDay
    startTime: TimeOfDay

@typing.type_check_only
class DayPartTargeting(typing_extensions.TypedDict, total=False):
    dayParts: _list[DayPart]
    timeZoneType: typing_extensions.Literal[
        "TIME_ZONE_SOURCE_UNSPECIFIED", "PUBLISHER", "USER"
    ]

@typing.type_check_only
class Deal(typing_extensions.TypedDict, total=False):
    availableEndTime: str
    availableStartTime: str
    buyerPrivateData: PrivateData
    createProductId: str
    createProductRevision: str
    createTime: str
    creativePreApprovalPolicy: typing_extensions.Literal[
        "CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED",
        "SELLER_PRE_APPROVAL_REQUIRED",
        "SELLER_PRE_APPROVAL_NOT_REQUIRED",
    ]
    creativeRestrictions: CreativeRestrictions
    creativeSafeFrameCompatibility: typing_extensions.Literal[
        "CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    dealId: str
    dealServingMetadata: DealServingMetadata
    dealTerms: DealTerms
    deliveryControl: DeliveryControl
    description: str
    displayName: str
    externalDealId: str
    isSetupComplete: bool
    programmaticCreativeSource: typing_extensions.Literal[
        "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED", "ADVERTISER", "PUBLISHER"
    ]
    proposalId: str
    sellerContacts: _list[ContactInformation]
    syndicationProduct: typing_extensions.Literal[
        "SYNDICATION_PRODUCT_UNSPECIFIED", "CONTENT", "MOBILE", "VIDEO", "GAMES"
    ]
    targeting: MarketplaceTargeting
    targetingCriterion: _list[TargetingCriteria]
    updateTime: str
    webPropertyCode: str

@typing.type_check_only
class DealPauseStatus(typing_extensions.TypedDict, total=False):
    buyerPauseReason: str
    firstPausedBy: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    hasBuyerPaused: bool
    hasSellerPaused: bool
    sellerPauseReason: str

@typing.type_check_only
class DealServingMetadata(typing_extensions.TypedDict, total=False):
    dealPauseStatus: DealPauseStatus

@typing.type_check_only
class DealTerms(typing_extensions.TypedDict, total=False):
    brandingType: typing_extensions.Literal[
        "BRANDING_TYPE_UNSPECIFIED", "BRANDED", "SEMI_TRANSPARENT"
    ]
    description: str
    estimatedGrossSpend: Price
    estimatedImpressionsPerDay: str
    guaranteedFixedPriceTerms: GuaranteedFixedPriceTerms
    nonGuaranteedAuctionTerms: NonGuaranteedAuctionTerms
    nonGuaranteedFixedPriceTerms: NonGuaranteedFixedPriceTerms
    sellerTimeZone: str

@typing.type_check_only
class DeliveryControl(typing_extensions.TypedDict, total=False):
    creativeBlockingLevel: typing_extensions.Literal[
        "CREATIVE_BLOCKING_LEVEL_UNSPECIFIED",
        "PUBLISHER_BLOCKING_RULES",
        "ADX_POLICY_BLOCKING_ONLY",
    ]
    deliveryRateType: typing_extensions.Literal[
        "DELIVERY_RATE_TYPE_UNSPECIFIED",
        "EVENLY",
        "FRONT_LOADED",
        "AS_FAST_AS_POSSIBLE",
    ]
    frequencyCaps: _list[FrequencyCap]

@typing.type_check_only
class Disapproval(typing_extensions.TypedDict, total=False):
    details: _list[str]
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

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FilterSet(typing_extensions.TypedDict, total=False):
    absoluteDateRange: AbsoluteDateRange
    breakdownDimensions: _list[str]
    creativeId: str
    dealId: str
    environment: typing_extensions.Literal["ENVIRONMENT_UNSPECIFIED", "WEB", "APP"]
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED",
        "NATIVE_DISPLAY",
        "NATIVE_VIDEO",
        "NON_NATIVE_DISPLAY",
        "NON_NATIVE_VIDEO",
    ]
    formats: _list[str]
    name: str
    platforms: _list[str]
    publisherIdentifiers: _list[str]
    realtimeTimeRange: RealtimeTimeRange
    relativeDateRange: RelativeDateRange
    sellerNetworkIds: _list[int]
    timeSeriesGranularity: typing_extensions.Literal[
        "TIME_SERIES_GRANULARITY_UNSPECIFIED", "HOURLY", "DAILY"
    ]

@typing.type_check_only
class FilteredBidCreativeRow(typing_extensions.TypedDict, total=False):
    bidCount: MetricValue
    creativeId: str
    rowDimensions: RowDimensions

@typing.type_check_only
class FilteredBidDetailRow(typing_extensions.TypedDict, total=False):
    bidCount: MetricValue
    detail: str
    detailId: int
    rowDimensions: RowDimensions

@typing.type_check_only
class FirstPartyMobileApplicationTargeting(typing_extensions.TypedDict, total=False):
    excludedAppIds: _list[str]
    targetedAppIds: _list[str]

@typing.type_check_only
class FrequencyCap(typing_extensions.TypedDict, total=False):
    maxImpressions: int
    numTimeUnits: int
    timeUnitType: typing_extensions.Literal[
        "TIME_UNIT_TYPE_UNSPECIFIED",
        "MINUTE",
        "HOUR",
        "DAY",
        "WEEK",
        "MONTH",
        "LIFETIME",
        "POD",
        "STREAM",
    ]

@typing.type_check_only
class GuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    fixedPrices: _list[PricePerBuyer]
    guaranteedImpressions: str
    guaranteedLooks: str
    impressionCap: str
    minimumDailyLooks: str
    percentShareOfVoice: str
    reservationType: typing_extensions.Literal[
        "RESERVATION_TYPE_UNSPECIFIED", "STANDARD", "SPONSORSHIP"
    ]

@typing.type_check_only
class HtmlContent(typing_extensions.TypedDict, total=False):
    height: int
    snippet: str
    width: int

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    height: int
    url: str
    width: int

@typing.type_check_only
class ImpressionMetricsRow(typing_extensions.TypedDict, total=False):
    availableImpressions: MetricValue
    bidRequests: MetricValue
    inventoryMatches: MetricValue
    responsesWithBids: MetricValue
    rowDimensions: RowDimensions
    successfulResponses: MetricValue

@typing.type_check_only
class InventorySizeTargeting(typing_extensions.TypedDict, total=False):
    excludedInventorySizes: _list[AdSize]
    targetedInventorySizes: _list[AdSize]

@typing.type_check_only
class ListBidMetricsResponse(typing_extensions.TypedDict, total=False):
    bidMetricsRows: _list[BidMetricsRow]
    nextPageToken: str

@typing.type_check_only
class ListBidResponseErrorsResponse(typing_extensions.TypedDict, total=False):
    calloutStatusRows: _list[CalloutStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListBidResponsesWithoutBidsResponse(typing_extensions.TypedDict, total=False):
    bidResponseWithoutBidsStatusRows: _list[BidResponseWithoutBidsStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListClientUserInvitationsResponse(typing_extensions.TypedDict, total=False):
    invitations: _list[ClientUserInvitation]
    nextPageToken: str

@typing.type_check_only
class ListClientUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    users: _list[ClientUser]

@typing.type_check_only
class ListClientsResponse(typing_extensions.TypedDict, total=False):
    clients: _list[Client]
    nextPageToken: str

@typing.type_check_only
class ListCreativeStatusBreakdownByCreativeResponse(
    typing_extensions.TypedDict, total=False
):
    filteredBidCreativeRows: _list[FilteredBidCreativeRow]
    nextPageToken: str

@typing.type_check_only
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
        "ATP_VENDOR",
        "VENDOR_DOMAIN",
        "GVL_ID",
    ]
    filteredBidDetailRows: _list[FilteredBidDetailRow]
    nextPageToken: str

@typing.type_check_only
class ListCreativesResponse(typing_extensions.TypedDict, total=False):
    creatives: _list[Creative]
    nextPageToken: str

@typing.type_check_only
class ListDealAssociationsResponse(typing_extensions.TypedDict, total=False):
    associations: _list[CreativeDealAssociation]
    nextPageToken: str

@typing.type_check_only
class ListFilterSetsResponse(typing_extensions.TypedDict, total=False):
    filterSets: _list[FilterSet]
    nextPageToken: str

@typing.type_check_only
class ListFilteredBidRequestsResponse(typing_extensions.TypedDict, total=False):
    calloutStatusRows: _list[CalloutStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListFilteredBidsResponse(typing_extensions.TypedDict, total=False):
    creativeStatusRows: _list[CreativeStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListImpressionMetricsResponse(typing_extensions.TypedDict, total=False):
    impressionMetricsRows: _list[ImpressionMetricsRow]
    nextPageToken: str

@typing.type_check_only
class ListLosingBidsResponse(typing_extensions.TypedDict, total=False):
    creativeStatusRows: _list[CreativeStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListNonBillableWinningBidsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nonBillableWinningBidStatusRows: _list[NonBillableWinningBidStatusRow]

@typing.type_check_only
class ListProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]

@typing.type_check_only
class ListProposalsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    proposals: _list[Proposal]

@typing.type_check_only
class ListPublisherProfilesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    publisherProfiles: _list[PublisherProfile]

@typing.type_check_only
class LocationContext(typing_extensions.TypedDict, total=False):
    geoCriteriaIds: _list[int]

@typing.type_check_only
class MarketplaceTargeting(typing_extensions.TypedDict, total=False):
    geoTargeting: CriteriaTargeting
    inventorySizeTargeting: InventorySizeTargeting
    placementTargeting: PlacementTargeting
    technologyTargeting: TechnologyTargeting
    videoTargeting: VideoTargeting

@typing.type_check_only
class MetricValue(typing_extensions.TypedDict, total=False):
    value: str
    variance: str

@typing.type_check_only
class MobileApplicationTargeting(typing_extensions.TypedDict, total=False):
    firstPartyTargeting: FirstPartyMobileApplicationTargeting

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class NativeContent(typing_extensions.TypedDict, total=False):
    advertiserName: str
    appIcon: Image
    body: str
    callToAction: str
    clickLinkUrl: str
    clickTrackingUrl: str
    headline: str
    image: Image
    logo: Image
    priceDisplayText: str
    starRating: float
    storeUrl: str
    videoUrl: str

@typing.type_check_only
class NonBillableWinningBidStatusRow(typing_extensions.TypedDict, total=False):
    bidCount: MetricValue
    rowDimensions: RowDimensions
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "AD_NOT_RENDERED",
        "INVALID_IMPRESSION",
        "FATAL_VAST_ERROR",
        "LOST_IN_MEDIATION",
    ]

@typing.type_check_only
class NonGuaranteedAuctionTerms(typing_extensions.TypedDict, total=False):
    autoOptimizePrivateAuction: bool
    reservePricesPerBuyer: _list[PricePerBuyer]

@typing.type_check_only
class NonGuaranteedFixedPriceTerms(typing_extensions.TypedDict, total=False):
    fixedPrices: _list[PricePerBuyer]

@typing.type_check_only
class Note(typing_extensions.TypedDict, total=False):
    createTime: str
    creatorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    note: str
    noteId: str
    proposalRevision: str

@typing.type_check_only
class OperatingSystemTargeting(typing_extensions.TypedDict, total=False):
    operatingSystemCriteria: CriteriaTargeting
    operatingSystemVersionCriteria: CriteriaTargeting

@typing.type_check_only
class PauseProposalDealsRequest(typing_extensions.TypedDict, total=False):
    externalDealIds: _list[str]
    reason: str

@typing.type_check_only
class PauseProposalRequest(typing_extensions.TypedDict, total=False):
    reason: str

@typing.type_check_only
class PlacementTargeting(typing_extensions.TypedDict, total=False):
    mobileApplicationTargeting: MobileApplicationTargeting
    urlTargeting: UrlTargeting

@typing.type_check_only
class PlatformContext(typing_extensions.TypedDict, total=False):
    platforms: _list[str]

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amount: Money
    pricingType: typing_extensions.Literal[
        "PRICING_TYPE_UNSPECIFIED", "COST_PER_MILLE", "COST_PER_DAY"
    ]

@typing.type_check_only
class PricePerBuyer(typing_extensions.TypedDict, total=False):
    advertiserIds: _list[str]
    buyer: Buyer
    price: Price

@typing.type_check_only
class PrivateData(typing_extensions.TypedDict, total=False):
    referenceId: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    availableEndTime: str
    availableStartTime: str
    createTime: str
    creatorContacts: _list[ContactInformation]
    displayName: str
    hasCreatorSignedOff: bool
    productId: str
    productRevision: str
    publisherProfileId: str
    seller: Seller
    syndicationProduct: typing_extensions.Literal[
        "SYNDICATION_PRODUCT_UNSPECIFIED", "CONTENT", "MOBILE", "VIDEO", "GAMES"
    ]
    targetingCriterion: _list[TargetingCriteria]
    terms: DealTerms
    updateTime: str
    webPropertyCode: str

@typing.type_check_only
class Proposal(typing_extensions.TypedDict, total=False):
    billedBuyer: Buyer
    buyer: Buyer
    buyerContacts: _list[ContactInformation]
    buyerPrivateData: PrivateData
    deals: _list[Deal]
    displayName: str
    isRenegotiating: bool
    isSetupComplete: bool
    lastUpdaterOrCommentorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    notes: _list[Note]
    originatorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    privateAuctionId: str
    proposalId: str
    proposalRevision: str
    proposalState: typing_extensions.Literal[
        "PROPOSAL_STATE_UNSPECIFIED",
        "PROPOSED",
        "BUYER_ACCEPTED",
        "SELLER_ACCEPTED",
        "CANCELED",
        "FINALIZED",
    ]
    seller: Seller
    sellerContacts: _list[ContactInformation]
    termsAndConditions: str
    updateTime: str

@typing.type_check_only
class PublisherProfile(typing_extensions.TypedDict, total=False):
    audienceDescription: str
    buyerPitchStatement: str
    directDealsContact: str
    displayName: str
    domains: _list[str]
    googlePlusUrl: str
    isParent: bool
    logoUrl: str
    mediaKitUrl: str
    mobileApps: _list[PublisherProfileMobileApplication]
    overview: str
    programmaticDealsContact: str
    publisherProfileId: str
    rateCardInfoUrl: str
    samplePageUrl: str
    seller: Seller
    topHeadlines: _list[str]

@typing.type_check_only
class PublisherProfileMobileApplication(typing_extensions.TypedDict, total=False):
    appStore: typing_extensions.Literal[
        "APP_STORE_TYPE_UNSPECIFIED",
        "APPLE_ITUNES",
        "GOOGLE_PLAY",
        "ROKU",
        "AMAZON_FIRETV",
        "PLAYSTATION",
        "XBOX",
        "SAMSUNG_TV",
        "AMAZON",
        "OPPO",
        "SAMSUNG",
        "VIVO",
        "XIAOMI",
    ]
    externalAppId: str
    name: str

@typing.type_check_only
class RealtimeTimeRange(typing_extensions.TypedDict, total=False):
    startTimestamp: str

@typing.type_check_only
class RelativeDateRange(typing_extensions.TypedDict, total=False):
    durationDays: int
    offsetDays: int

@typing.type_check_only
class RemoveDealAssociationRequest(typing_extensions.TypedDict, total=False):
    association: CreativeDealAssociation

@typing.type_check_only
class ResumeProposalDealsRequest(typing_extensions.TypedDict, total=False):
    externalDealIds: _list[str]

@typing.type_check_only
class ResumeProposalRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RowDimensions(typing_extensions.TypedDict, total=False):
    publisherIdentifier: str
    timeInterval: TimeInterval

@typing.type_check_only
class SecurityContext(typing_extensions.TypedDict, total=False):
    securities: _list[str]

@typing.type_check_only
class Seller(typing_extensions.TypedDict, total=False):
    accountId: str
    subAccountId: str

@typing.type_check_only
class ServingContext(typing_extensions.TypedDict, total=False):
    all: typing_extensions.Literal["SIMPLE_CONTEXT"]
    appType: AppContext
    auctionType: AuctionContext
    location: LocationContext
    platform: PlatformContext
    securityType: SecurityContext

@typing.type_check_only
class ServingRestriction(typing_extensions.TypedDict, total=False):
    contexts: _list[ServingContext]
    disapproval: Disapproval
    disapprovalReasons: _list[Disapproval]
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "DISAPPROVAL", "PENDING_REVIEW"
    ]

@typing.type_check_only
class Size(typing_extensions.TypedDict, total=False):
    height: int
    width: int

@typing.type_check_only
class StopWatchingCreativeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TargetingCriteria(typing_extensions.TypedDict, total=False):
    exclusions: _list[TargetingValue]
    inclusions: _list[TargetingValue]
    key: str

@typing.type_check_only
class TargetingValue(typing_extensions.TypedDict, total=False):
    creativeSizeValue: CreativeSize
    dayPartTargetingValue: DayPartTargeting
    longValue: str
    stringValue: str

@typing.type_check_only
class TechnologyTargeting(typing_extensions.TypedDict, total=False):
    deviceCapabilityTargeting: CriteriaTargeting
    deviceCategoryTargeting: CriteriaTargeting
    operatingSystemTargeting: OperatingSystemTargeting

@typing.type_check_only
class TimeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UrlTargeting(typing_extensions.TypedDict, total=False):
    excludedUrls: _list[str]
    targetedUrls: _list[str]

@typing.type_check_only
class VideoContent(typing_extensions.TypedDict, total=False):
    videoUrl: str
    videoVastXml: str

@typing.type_check_only
class VideoTargeting(typing_extensions.TypedDict, total=False):
    excludedPositionTypes: _list[str]
    targetedPositionTypes: _list[str]

@typing.type_check_only
class WatchCreativeRequest(typing_extensions.TypedDict, total=False):
    topic: str
