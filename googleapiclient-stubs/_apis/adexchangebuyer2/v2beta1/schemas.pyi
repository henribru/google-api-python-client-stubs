import typing

_list = list

@typing.type_check_only
class AbsoluteDateRange(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class AcceptProposalRequest(typing.TypedDict, total=False):
    proposalRevision: str

@typing.type_check_only
class AdSize(typing.TypedDict, total=False):
    height: str
    sizeType: typing.Literal[
        "SIZE_TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"
    ]
    width: str

@typing.type_check_only
class AdTechnologyProviders(typing.TypedDict, total=False):
    detectedProviderIds: _list[str]
    hasUnidentifiedProvider: bool

@typing.type_check_only
class AddDealAssociationRequest(typing.TypedDict, total=False):
    association: CreativeDealAssociation

@typing.type_check_only
class AddNoteRequest(typing.TypedDict, total=False):
    note: Note

@typing.type_check_only
class AppContext(typing.TypedDict, total=False):
    appTypes: _list[typing.Literal["NATIVE", "WEB"]]

@typing.type_check_only
class AuctionContext(typing.TypedDict, total=False):
    auctionTypes: _list[typing.Literal["OPEN_AUCTION", "DIRECT_DEALS"]]

@typing.type_check_only
class BidMetricsRow(typing.TypedDict, total=False):
    bids: MetricValue
    bidsInAuction: MetricValue
    billedImpressions: MetricValue
    impressionsWon: MetricValue
    measurableImpressions: MetricValue
    reachedQueries: MetricValue
    rowDimensions: RowDimensions
    viewableImpressions: MetricValue

@typing.type_check_only
class BidResponseWithoutBidsStatusRow(typing.TypedDict, total=False):
    impressionCount: MetricValue
    rowDimensions: RowDimensions
    status: typing.Literal[
        "STATUS_UNSPECIFIED",
        "RESPONSES_WITHOUT_BIDS",
        "RESPONSES_WITHOUT_BIDS_FOR_ACCOUNT",
        "RESPONSES_WITHOUT_BIDS_FOR_DEAL",
    ]

@typing.type_check_only
class Buyer(typing.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class CalloutStatusRow(typing.TypedDict, total=False):
    calloutStatusId: int
    impressionCount: MetricValue
    rowDimensions: RowDimensions

@typing.type_check_only
class CancelNegotiationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Client(typing.TypedDict, total=False):
    clientAccountId: str
    clientName: str
    entityId: str
    entityName: str
    entityType: typing.Literal[
        "ENTITY_TYPE_UNSPECIFIED",
        "ADVERTISER",
        "BRAND",
        "AGENCY",
        "ENTITY_TYPE_UNCLASSIFIED",
    ]
    partnerClientId: str
    role: typing.Literal[
        "CLIENT_ROLE_UNSPECIFIED",
        "CLIENT_DEAL_VIEWER",
        "CLIENT_DEAL_NEGOTIATOR",
        "CLIENT_DEAL_APPROVER",
    ]
    status: typing.Literal["CLIENT_STATUS_UNSPECIFIED", "DISABLED", "ACTIVE"]
    visibleToSeller: bool

@typing.type_check_only
class ClientUser(typing.TypedDict, total=False):
    clientAccountId: str
    email: str
    status: typing.Literal["USER_STATUS_UNSPECIFIED", "PENDING", "ACTIVE", "DISABLED"]
    userId: str

@typing.type_check_only
class ClientUserInvitation(typing.TypedDict, total=False):
    clientAccountId: str
    email: str
    invitationId: str

@typing.type_check_only
class CompleteSetupRequest(typing.TypedDict, total=False):
    externalDealIds: _list[str]

@typing.type_check_only
class ContactInformation(typing.TypedDict, total=False):
    email: str
    name: str

@typing.type_check_only
class Correction(typing.TypedDict, total=False):
    contexts: _list[ServingContext]
    details: _list[str]
    type: typing.Literal[
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
class Creative(typing.TypedDict, total=False):
    accountId: str
    adChoicesDestinationUrl: str
    adTechnologyProviders: AdTechnologyProviders
    advertiserName: str
    agencyId: str
    apiUpdateTime: str
    attributes: _list[
        typing.Literal[
            "ATTRIBUTE_UNSPECIFIED",
            "IMAGE_RICH_MEDIA",
            "ADOBE_FLASH_FLV",
            "IS_TAGGED",
            "IS_COOKIE_TARGETED",
            "IS_USER_INTEREST_TARGETED",
            "EXPANDING_DIRECTION_NONE",
            "EXPANDING_DIRECTION_UP",
            "EXPANDING_DIRECTION_DOWN",
            "EXPANDING_DIRECTION_LEFT",
            "EXPANDING_DIRECTION_RIGHT",
            "EXPANDING_DIRECTION_UP_LEFT",
            "EXPANDING_DIRECTION_UP_RIGHT",
            "EXPANDING_DIRECTION_DOWN_LEFT",
            "EXPANDING_DIRECTION_DOWN_RIGHT",
            "CREATIVE_TYPE_HTML",
            "CREATIVE_TYPE_VAST_VIDEO",
            "EXPANDING_DIRECTION_UP_OR_DOWN",
            "EXPANDING_DIRECTION_LEFT_OR_RIGHT",
            "EXPANDING_DIRECTION_ANY_DIAGONAL",
            "EXPANDING_ACTION_ROLLOVER_TO_EXPAND",
            "INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH",
            "RICH_MEDIA_CAPABILITY_TYPE_MRAID",
            "RICH_MEDIA_CAPABILITY_TYPE_FLASH",
            "RICH_MEDIA_CAPABILITY_TYPE_HTML5",
            "SKIPPABLE_INSTREAM_VIDEO",
            "RICH_MEDIA_CAPABILITY_TYPE_SSL",
            "RICH_MEDIA_CAPABILITY_TYPE_NON_SSL",
            "RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL",
            "NON_SKIPPABLE_INSTREAM_VIDEO",
            "NATIVE_ELIGIBILITY_ELIGIBLE",
            "NON_VPAID",
            "NATIVE_ELIGIBILITY_NOT_ELIGIBLE",
            "ANY_INTERSTITIAL",
            "NON_INTERSTITIAL",
            "IN_BANNER_VIDEO",
            "RENDERING_SIZELESS_ADX",
            "OMSDK_1_0",
            "RENDERING_PLAYABLE",
        ]
    ]
    clickThroughUrls: _list[str]
    corrections: _list[Correction]
    creativeId: str
    dealsStatus: typing.Literal[
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
    openAuctionStatus: typing.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_CHECKED",
        "CONDITIONALLY_APPROVED",
        "APPROVED",
        "DISAPPROVED",
        "PENDING_REVIEW",
        "STATUS_TYPE_UNSPECIFIED",
    ]
    restrictedCategories: _list[typing.Literal["NO_RESTRICTED_CATEGORIES", "ALCOHOL"]]
    servingRestrictions: _list[ServingRestriction]
    vendorIds: _list[int]
    version: int
    video: VideoContent

@typing.type_check_only
class CreativeDealAssociation(typing.TypedDict, total=False):
    accountId: str
    creativeId: str
    dealsId: str

@typing.type_check_only
class CreativeRestrictions(typing.TypedDict, total=False):
    creativeFormat: typing.Literal["CREATIVE_FORMAT_UNSPECIFIED", "DISPLAY", "VIDEO"]
    creativeSpecifications: _list[CreativeSpecification]
    skippableAdType: typing.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED", "SKIPPABLE", "INSTREAM_SELECT", "NOT_SKIPPABLE"
    ]

@typing.type_check_only
class CreativeSize(typing.TypedDict, total=False):
    allowedFormats: _list[typing.Literal["UNKNOWN", "AUDIO"]]
    companionSizes: _list[Size]
    creativeSizeType: typing.Literal[
        "CREATIVE_SIZE_TYPE_UNSPECIFIED", "REGULAR", "INTERSTITIAL", "VIDEO", "NATIVE"
    ]
    nativeTemplate: typing.Literal[
        "UNKNOWN_NATIVE_TEMPLATE",
        "NATIVE_CONTENT_AD",
        "NATIVE_APP_INSTALL_AD",
        "NATIVE_VIDEO_CONTENT_AD",
        "NATIVE_VIDEO_APP_INSTALL_AD",
    ]
    size: Size
    skippableAdType: typing.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED", "GENERIC", "INSTREAM_SELECT", "NOT_SKIPPABLE"
    ]

@typing.type_check_only
class CreativeSpecification(typing.TypedDict, total=False):
    creativeCompanionSizes: _list[AdSize]
    creativeSize: AdSize

@typing.type_check_only
class CreativeStatusRow(typing.TypedDict, total=False):
    bidCount: MetricValue
    creativeStatusId: int
    rowDimensions: RowDimensions

@typing.type_check_only
class CriteriaTargeting(typing.TypedDict, total=False):
    excludedCriteriaIds: _list[str]
    targetedCriteriaIds: _list[str]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DayPart(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
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
class DayPartTargeting(typing.TypedDict, total=False):
    dayParts: _list[DayPart]
    timeZoneType: typing.Literal["TIME_ZONE_SOURCE_UNSPECIFIED", "PUBLISHER", "USER"]

@typing.type_check_only
class Deal(typing.TypedDict, total=False):
    availableEndTime: str
    availableStartTime: str
    buyerPrivateData: PrivateData
    createProductId: str
    createProductRevision: str
    createTime: str
    creativePreApprovalPolicy: typing.Literal[
        "CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED",
        "SELLER_PRE_APPROVAL_REQUIRED",
        "SELLER_PRE_APPROVAL_NOT_REQUIRED",
    ]
    creativeRestrictions: CreativeRestrictions
    creativeSafeFrameCompatibility: typing.Literal[
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
    programmaticCreativeSource: typing.Literal[
        "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED", "ADVERTISER", "PUBLISHER"
    ]
    proposalId: str
    sellerContacts: _list[ContactInformation]
    syndicationProduct: typing.Literal[
        "SYNDICATION_PRODUCT_UNSPECIFIED", "CONTENT", "MOBILE", "VIDEO", "GAMES"
    ]
    targeting: MarketplaceTargeting
    targetingCriterion: _list[TargetingCriteria]
    updateTime: str
    webPropertyCode: str

@typing.type_check_only
class DealPauseStatus(typing.TypedDict, total=False):
    buyerPauseReason: str
    firstPausedBy: typing.Literal["BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"]
    hasBuyerPaused: bool
    hasSellerPaused: bool
    sellerPauseReason: str

@typing.type_check_only
class DealServingMetadata(typing.TypedDict, total=False):
    dealPauseStatus: DealPauseStatus

@typing.type_check_only
class DealTerms(typing.TypedDict, total=False):
    brandingType: typing.Literal[
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
class DeliveryControl(typing.TypedDict, total=False):
    creativeBlockingLevel: typing.Literal[
        "CREATIVE_BLOCKING_LEVEL_UNSPECIFIED",
        "PUBLISHER_BLOCKING_RULES",
        "ADX_POLICY_BLOCKING_ONLY",
    ]
    deliveryRateType: typing.Literal[
        "DELIVERY_RATE_TYPE_UNSPECIFIED",
        "EVENLY",
        "FRONT_LOADED",
        "AS_FAST_AS_POSSIBLE",
    ]
    frequencyCaps: _list[FrequencyCap]

@typing.type_check_only
class Disapproval(typing.TypedDict, total=False):
    details: _list[str]
    reason: typing.Literal[
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
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FilterSet(typing.TypedDict, total=False):
    absoluteDateRange: AbsoluteDateRange
    breakdownDimensions: _list[
        typing.Literal["BREAKDOWN_DIMENSION_UNSPECIFIED", "PUBLISHER_IDENTIFIER"]
    ]
    creativeId: str
    dealId: str
    environment: typing.Literal["ENVIRONMENT_UNSPECIFIED", "WEB", "APP"]
    format: typing.Literal[
        "FORMAT_UNSPECIFIED",
        "NATIVE_DISPLAY",
        "NATIVE_VIDEO",
        "NON_NATIVE_DISPLAY",
        "NON_NATIVE_VIDEO",
    ]
    formats: _list[
        typing.Literal[
            "FORMAT_UNSPECIFIED",
            "NATIVE_DISPLAY",
            "NATIVE_VIDEO",
            "NON_NATIVE_DISPLAY",
            "NON_NATIVE_VIDEO",
        ]
    ]
    name: str
    platforms: _list[
        typing.Literal["PLATFORM_UNSPECIFIED", "DESKTOP", "TABLET", "MOBILE"]
    ]
    publisherIdentifiers: _list[str]
    realtimeTimeRange: RealtimeTimeRange
    relativeDateRange: RelativeDateRange
    sellerNetworkIds: _list[int]
    timeSeriesGranularity: typing.Literal[
        "TIME_SERIES_GRANULARITY_UNSPECIFIED", "HOURLY", "DAILY"
    ]

@typing.type_check_only
class FilteredBidCreativeRow(typing.TypedDict, total=False):
    bidCount: MetricValue
    creativeId: str
    rowDimensions: RowDimensions

@typing.type_check_only
class FilteredBidDetailRow(typing.TypedDict, total=False):
    bidCount: MetricValue
    detail: str
    detailId: int
    rowDimensions: RowDimensions

@typing.type_check_only
class FirstPartyMobileApplicationTargeting(typing.TypedDict, total=False):
    excludedAppIds: _list[str]
    targetedAppIds: _list[str]

@typing.type_check_only
class FrequencyCap(typing.TypedDict, total=False):
    maxImpressions: int
    numTimeUnits: int
    timeUnitType: typing.Literal[
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
class GuaranteedFixedPriceTerms(typing.TypedDict, total=False):
    fixedPrices: _list[PricePerBuyer]
    guaranteedImpressions: str
    guaranteedLooks: str
    impressionCap: str
    minimumDailyLooks: str
    percentShareOfVoice: str
    reservationType: typing.Literal[
        "RESERVATION_TYPE_UNSPECIFIED", "STANDARD", "SPONSORSHIP"
    ]

@typing.type_check_only
class HtmlContent(typing.TypedDict, total=False):
    height: int
    snippet: str
    width: int

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    height: int
    url: str
    width: int

@typing.type_check_only
class ImpressionMetricsRow(typing.TypedDict, total=False):
    availableImpressions: MetricValue
    bidRequests: MetricValue
    inventoryMatches: MetricValue
    responsesWithBids: MetricValue
    rowDimensions: RowDimensions
    successfulResponses: MetricValue

@typing.type_check_only
class InventorySizeTargeting(typing.TypedDict, total=False):
    excludedInventorySizes: _list[AdSize]
    targetedInventorySizes: _list[AdSize]

@typing.type_check_only
class ListBidMetricsResponse(typing.TypedDict, total=False):
    bidMetricsRows: _list[BidMetricsRow]
    nextPageToken: str

@typing.type_check_only
class ListBidResponseErrorsResponse(typing.TypedDict, total=False):
    calloutStatusRows: _list[CalloutStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListBidResponsesWithoutBidsResponse(typing.TypedDict, total=False):
    bidResponseWithoutBidsStatusRows: _list[BidResponseWithoutBidsStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListClientUserInvitationsResponse(typing.TypedDict, total=False):
    invitations: _list[ClientUserInvitation]
    nextPageToken: str

@typing.type_check_only
class ListClientUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    users: _list[ClientUser]

@typing.type_check_only
class ListClientsResponse(typing.TypedDict, total=False):
    clients: _list[Client]
    nextPageToken: str

@typing.type_check_only
class ListCreativeStatusBreakdownByCreativeResponse(typing.TypedDict, total=False):
    filteredBidCreativeRows: _list[FilteredBidCreativeRow]
    nextPageToken: str

@typing.type_check_only
class ListCreativeStatusBreakdownByDetailResponse(typing.TypedDict, total=False):
    detailType: typing.Literal[
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
class ListCreativesResponse(typing.TypedDict, total=False):
    creatives: _list[Creative]
    nextPageToken: str

@typing.type_check_only
class ListDealAssociationsResponse(typing.TypedDict, total=False):
    associations: _list[CreativeDealAssociation]
    nextPageToken: str

@typing.type_check_only
class ListFilterSetsResponse(typing.TypedDict, total=False):
    filterSets: _list[FilterSet]
    nextPageToken: str

@typing.type_check_only
class ListFilteredBidRequestsResponse(typing.TypedDict, total=False):
    calloutStatusRows: _list[CalloutStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListFilteredBidsResponse(typing.TypedDict, total=False):
    creativeStatusRows: _list[CreativeStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListImpressionMetricsResponse(typing.TypedDict, total=False):
    impressionMetricsRows: _list[ImpressionMetricsRow]
    nextPageToken: str

@typing.type_check_only
class ListLosingBidsResponse(typing.TypedDict, total=False):
    creativeStatusRows: _list[CreativeStatusRow]
    nextPageToken: str

@typing.type_check_only
class ListNonBillableWinningBidsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nonBillableWinningBidStatusRows: _list[NonBillableWinningBidStatusRow]

@typing.type_check_only
class ListProductsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]

@typing.type_check_only
class ListProposalsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    proposals: _list[Proposal]

@typing.type_check_only
class ListPublisherProfilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    publisherProfiles: _list[PublisherProfile]

@typing.type_check_only
class LocationContext(typing.TypedDict, total=False):
    geoCriteriaIds: _list[int]

@typing.type_check_only
class MarketplaceTargeting(typing.TypedDict, total=False):
    geoTargeting: CriteriaTargeting
    inventorySizeTargeting: InventorySizeTargeting
    placementTargeting: PlacementTargeting
    technologyTargeting: TechnologyTargeting
    videoTargeting: VideoTargeting

@typing.type_check_only
class MetricValue(typing.TypedDict, total=False):
    value: str
    variance: str

@typing.type_check_only
class MobileApplicationTargeting(typing.TypedDict, total=False):
    firstPartyTargeting: FirstPartyMobileApplicationTargeting

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class NativeContent(typing.TypedDict, total=False):
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
class NonBillableWinningBidStatusRow(typing.TypedDict, total=False):
    bidCount: MetricValue
    rowDimensions: RowDimensions
    status: typing.Literal[
        "STATUS_UNSPECIFIED",
        "AD_NOT_RENDERED",
        "INVALID_IMPRESSION",
        "FATAL_VAST_ERROR",
        "LOST_IN_MEDIATION",
        "OVERDELIVERED_IMPRESSION",
    ]

@typing.type_check_only
class NonGuaranteedAuctionTerms(typing.TypedDict, total=False):
    autoOptimizePrivateAuction: bool
    reservePricesPerBuyer: _list[PricePerBuyer]

@typing.type_check_only
class NonGuaranteedFixedPriceTerms(typing.TypedDict, total=False):
    fixedPrices: _list[PricePerBuyer]

@typing.type_check_only
class Note(typing.TypedDict, total=False):
    createTime: str
    creatorRole: typing.Literal["BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"]
    note: str
    noteId: str
    proposalRevision: str

@typing.type_check_only
class OperatingSystemTargeting(typing.TypedDict, total=False):
    operatingSystemCriteria: CriteriaTargeting
    operatingSystemVersionCriteria: CriteriaTargeting

@typing.type_check_only
class PauseProposalDealsRequest(typing.TypedDict, total=False):
    externalDealIds: _list[str]
    reason: str

@typing.type_check_only
class PauseProposalRequest(typing.TypedDict, total=False):
    reason: str

@typing.type_check_only
class PlacementTargeting(typing.TypedDict, total=False):
    mobileApplicationTargeting: MobileApplicationTargeting
    urlTargeting: UrlTargeting

@typing.type_check_only
class PlatformContext(typing.TypedDict, total=False):
    platforms: _list[typing.Literal["DESKTOP", "ANDROID", "IOS"]]

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    amount: Money
    pricingType: typing.Literal[
        "PRICING_TYPE_UNSPECIFIED", "COST_PER_MILLE", "COST_PER_DAY"
    ]

@typing.type_check_only
class PricePerBuyer(typing.TypedDict, total=False):
    advertiserIds: _list[str]
    buyer: Buyer
    price: Price

@typing.type_check_only
class PrivateData(typing.TypedDict, total=False):
    referenceId: str

@typing.type_check_only
class Product(typing.TypedDict, total=False):
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
    syndicationProduct: typing.Literal[
        "SYNDICATION_PRODUCT_UNSPECIFIED", "CONTENT", "MOBILE", "VIDEO", "GAMES"
    ]
    targetingCriterion: _list[TargetingCriteria]
    terms: DealTerms
    updateTime: str
    webPropertyCode: str

@typing.type_check_only
class Proposal(typing.TypedDict, total=False):
    billedBuyer: Buyer
    buyer: Buyer
    buyerContacts: _list[ContactInformation]
    buyerPrivateData: PrivateData
    deals: _list[Deal]
    displayName: str
    isRenegotiating: bool
    isSetupComplete: bool
    lastUpdaterOrCommentorRole: typing.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    notes: _list[Note]
    originatorRole: typing.Literal["BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"]
    privateAuctionId: str
    proposalId: str
    proposalRevision: str
    proposalState: typing.Literal[
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
class PublisherProfile(typing.TypedDict, total=False):
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
class PublisherProfileMobileApplication(typing.TypedDict, total=False):
    appStore: typing.Literal[
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
        "LG_TV",
    ]
    externalAppId: str
    name: str

@typing.type_check_only
class RealtimeTimeRange(typing.TypedDict, total=False):
    startTimestamp: str

@typing.type_check_only
class RelativeDateRange(typing.TypedDict, total=False):
    durationDays: int
    offsetDays: int

@typing.type_check_only
class RemoveDealAssociationRequest(typing.TypedDict, total=False):
    association: CreativeDealAssociation

@typing.type_check_only
class ResumeProposalDealsRequest(typing.TypedDict, total=False):
    externalDealIds: _list[str]

@typing.type_check_only
class ResumeProposalRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RowDimensions(typing.TypedDict, total=False):
    publisherIdentifier: str
    timeInterval: TimeInterval

@typing.type_check_only
class SecurityContext(typing.TypedDict, total=False):
    securities: _list[typing.Literal["INSECURE", "SSL"]]

@typing.type_check_only
class Seller(typing.TypedDict, total=False):
    accountId: str
    subAccountId: str

@typing.type_check_only
class ServingContext(typing.TypedDict, total=False):
    all: typing.Literal["SIMPLE_CONTEXT"]
    appType: AppContext
    auctionType: AuctionContext
    location: LocationContext
    platform: PlatformContext
    securityType: SecurityContext

@typing.type_check_only
class ServingRestriction(typing.TypedDict, total=False):
    contexts: _list[ServingContext]
    disapproval: Disapproval
    disapprovalReasons: _list[Disapproval]
    status: typing.Literal["STATUS_UNSPECIFIED", "DISAPPROVAL", "PENDING_REVIEW"]

@typing.type_check_only
class Size(typing.TypedDict, total=False):
    height: int
    width: int

@typing.type_check_only
class StopWatchingCreativeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class TargetingCriteria(typing.TypedDict, total=False):
    exclusions: _list[TargetingValue]
    inclusions: _list[TargetingValue]
    key: str

@typing.type_check_only
class TargetingValue(typing.TypedDict, total=False):
    creativeSizeValue: CreativeSize
    dayPartTargetingValue: DayPartTargeting
    longValue: str
    stringValue: str

@typing.type_check_only
class TechnologyTargeting(typing.TypedDict, total=False):
    deviceCapabilityTargeting: CriteriaTargeting
    deviceCategoryTargeting: CriteriaTargeting
    operatingSystemTargeting: OperatingSystemTargeting

@typing.type_check_only
class TimeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UrlTargeting(typing.TypedDict, total=False):
    excludedUrls: _list[str]
    targetedUrls: _list[str]

@typing.type_check_only
class VideoContent(typing.TypedDict, total=False):
    videoUrl: str
    videoVastXml: str

@typing.type_check_only
class VideoTargeting(typing.TypedDict, total=False):
    excludedPositionTypes: _list[
        typing.Literal["POSITION_TYPE_UNSPECIFIED", "PREROLL", "MIDROLL", "POSTROLL"]
    ]
    targetedPositionTypes: _list[
        typing.Literal["POSITION_TYPE_UNSPECIFIED", "PREROLL", "MIDROLL", "POSTROLL"]
    ]

@typing.type_check_only
class WatchCreativeRequest(typing.TypedDict, total=False):
    topic: str
