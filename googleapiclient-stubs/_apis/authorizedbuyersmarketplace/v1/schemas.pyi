import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceptProposalRequest(typing_extensions.TypedDict, total=False):
    proposalRevision: str

@typing.type_check_only
class ActivateClientRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ActivateClientUserRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdSize(typing_extensions.TypedDict, total=False):
    height: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"
    ]
    width: str

@typing.type_check_only
class AddCreativeRequest(typing_extensions.TypedDict, total=False):
    creative: str

@typing.type_check_only
class AddNoteRequest(typing_extensions.TypedDict, total=False):
    note: Note

@typing.type_check_only
class AuctionPackage(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    description: str
    displayName: str
    name: str
    subscribedClients: _list[str]
    updateTime: str

@typing.type_check_only
class BatchUpdateDealsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateDealRequest]

@typing.type_check_only
class BatchUpdateDealsResponse(typing_extensions.TypedDict, total=False):
    deals: _list[Deal]

@typing.type_check_only
class CancelNegotiationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Client(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    partnerClientId: str
    role: typing_extensions.Literal[
        "CLIENT_ROLE_UNSPECIFIED",
        "CLIENT_DEAL_VIEWER",
        "CLIENT_DEAL_NEGOTIATOR",
        "CLIENT_DEAL_APPROVER",
    ]
    sellerVisible: bool
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class ClientUser(typing_extensions.TypedDict, total=False):
    email: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "INVITED", "ACTIVE", "INACTIVE"
    ]

@typing.type_check_only
class Contact(typing_extensions.TypedDict, total=False):
    displayName: str
    email: str

@typing.type_check_only
class CreativeRequirements(typing_extensions.TypedDict, total=False):
    creativeFormat: typing_extensions.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "DISPLAY", "VIDEO"
    ]
    creativePreApprovalPolicy: typing_extensions.Literal[
        "CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED",
        "SELLER_PRE_APPROVAL_REQUIRED",
        "SELLER_PRE_APPROVAL_NOT_REQUIRED",
    ]
    creativeSafeFrameCompatibility: typing_extensions.Literal[
        "CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    maxAdDurationMs: str
    programmaticCreativeSource: typing_extensions.Literal[
        "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED", "ADVERTISER", "PUBLISHER"
    ]
    skippableAdType: typing_extensions.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED",
        "SKIPPABLE",
        "INSTREAM_SELECT",
        "NOT_SKIPPABLE",
        "ANY",
    ]

@typing.type_check_only
class CriteriaTargeting(typing_extensions.TypedDict, total=False):
    excludedCriteriaIds: _list[str]
    targetedCriteriaIds: _list[str]

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
        "TIME_ZONE_TYPE_UNSPECIFIED", "SELLER", "USER"
    ]

@typing.type_check_only
class DeactivateClientRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateClientUserRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Deal(typing_extensions.TypedDict, total=False):
    billedBuyer: str
    buyer: str
    client: str
    createTime: str
    creativeRequirements: CreativeRequirements
    dealType: typing_extensions.Literal[
        "DEAL_TYPE_UNSPECIFIED",
        "PREFERRED_DEAL",
        "PRIVATE_AUCTION",
        "PROGRAMMATIC_GUARANTEED",
    ]
    deliveryControl: DeliveryControl
    description: str
    displayName: str
    estimatedGrossSpend: Money
    flightEndTime: str
    flightStartTime: str
    name: str
    preferredDealTerms: PreferredDealTerms
    privateAuctionTerms: PrivateAuctionTerms
    programmaticGuaranteedTerms: ProgrammaticGuaranteedTerms
    proposalRevision: str
    publisherProfile: str
    sellerTimeZone: TimeZone
    targeting: MarketplaceTargeting
    updateTime: str

@typing.type_check_only
class DealPausingInfo(typing_extensions.TypedDict, total=False):
    pauseReason: str
    pauseRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    pausingConsented: bool

@typing.type_check_only
class DeliveryControl(typing_extensions.TypedDict, total=False):
    companionDeliveryType: typing_extensions.Literal[
        "COMPANION_DELIVERY_TYPE_UNSPECIFIED",
        "DELIVERY_OPTIONAL",
        "DELIVERY_AT_LEAST_ONE",
        "DELIVERY_ALL",
    ]
    creativeRotationType: typing_extensions.Literal[
        "CREATIVE_ROTATION_TYPE_UNSPECIFIED",
        "ROTATION_EVEN",
        "ROTATION_OPTIMIZED",
        "ROTATION_MANUAL",
        "ROTATION_SEQUENTIAL",
    ]
    deliveryRateType: typing_extensions.Literal[
        "DELIVERY_RATE_TYPE_UNSPECIFIED",
        "EVENLY",
        "FRONT_LOADED",
        "AS_FAST_AS_POSSIBLE",
    ]
    frequencyCap: _list[FrequencyCap]
    roadblockingType: typing_extensions.Literal[
        "ROADBLOCKING_TYPE_UNSPECIFIED",
        "ONLY_ONE",
        "ONE_OR_MORE",
        "AS_MANY_AS_POSSIBLE",
        "ALL_ROADBLOCK",
        "CREATIVE_SET",
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FinalizedDeal(typing_extensions.TypedDict, total=False):
    deal: Deal
    dealPausingInfo: DealPausingInfo
    dealServingStatus: typing_extensions.Literal[
        "DEAL_SERVING_STATUS_UNSPECIFIED",
        "ACTIVE",
        "ENDED",
        "PAUSED_BY_BUYER",
        "PAUSED_BY_SELLER",
    ]
    name: str
    readyToServe: bool
    rtbMetrics: RtbMetrics

@typing.type_check_only
class FirstPartyMobileApplicationTargeting(typing_extensions.TypedDict, total=False):
    excludedAppIds: _list[str]
    targetedAppIds: _list[str]

@typing.type_check_only
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
        "POD",
        "STREAM",
    ]
    timeUnitsCount: int

@typing.type_check_only
class InventorySizeTargeting(typing_extensions.TypedDict, total=False):
    excludedInventorySizes: _list[AdSize]
    targetedInventorySizes: _list[AdSize]

@typing.type_check_only
class InventoryTypeTargeting(typing_extensions.TypedDict, total=False):
    inventoryTypes: _list[str]

@typing.type_check_only
class ListAuctionPackagesResponse(typing_extensions.TypedDict, total=False):
    auctionPackages: _list[AuctionPackage]
    nextPageToken: str

@typing.type_check_only
class ListClientUsersResponse(typing_extensions.TypedDict, total=False):
    clientUsers: _list[ClientUser]
    nextPageToken: str

@typing.type_check_only
class ListClientsResponse(typing_extensions.TypedDict, total=False):
    clients: _list[Client]
    nextPageToken: str

@typing.type_check_only
class ListDealsResponse(typing_extensions.TypedDict, total=False):
    deals: _list[Deal]
    nextPageToken: str

@typing.type_check_only
class ListFinalizedDealsResponse(typing_extensions.TypedDict, total=False):
    finalizedDeals: _list[FinalizedDeal]
    nextPageToken: str

@typing.type_check_only
class ListProposalsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    proposals: _list[Proposal]

@typing.type_check_only
class ListPublisherProfilesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    publisherProfiles: _list[PublisherProfile]

@typing.type_check_only
class MarketplaceTargeting(typing_extensions.TypedDict, total=False):
    daypartTargeting: DayPartTargeting
    geoTargeting: CriteriaTargeting
    inventorySizeTargeting: InventorySizeTargeting
    inventoryTypeTargeting: InventoryTypeTargeting
    placementTargeting: PlacementTargeting
    technologyTargeting: TechnologyTargeting
    userListTargeting: CriteriaTargeting
    videoTargeting: VideoTargeting

@typing.type_check_only
class MobileApplicationTargeting(typing_extensions.TypedDict, total=False):
    firstPartyTargeting: FirstPartyMobileApplicationTargeting

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Note(typing_extensions.TypedDict, total=False):
    createTime: str
    creatorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    note: str

@typing.type_check_only
class OperatingSystemTargeting(typing_extensions.TypedDict, total=False):
    operatingSystemCriteria: CriteriaTargeting
    operatingSystemVersionCriteria: CriteriaTargeting

@typing.type_check_only
class PauseFinalizedDealRequest(typing_extensions.TypedDict, total=False):
    reason: str

@typing.type_check_only
class PlacementTargeting(typing_extensions.TypedDict, total=False):
    mobileApplicationTargeting: MobileApplicationTargeting
    uriTargeting: UriTargeting

@typing.type_check_only
class PreferredDealTerms(typing_extensions.TypedDict, total=False):
    fixedPrice: Price

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amount: Money
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "CPM", "CPD"]

@typing.type_check_only
class PrivateAuctionTerms(typing_extensions.TypedDict, total=False):
    floorPrice: Price
    openAuctionAllowed: bool

@typing.type_check_only
class PrivateData(typing_extensions.TypedDict, total=False):
    referenceId: str

@typing.type_check_only
class ProgrammaticGuaranteedTerms(typing_extensions.TypedDict, total=False):
    fixedPrice: Price
    guaranteedLooks: str
    impressionCap: str
    minimumDailyLooks: str
    percentShareOfVoice: str
    reservationType: typing_extensions.Literal[
        "RESERVATION_TYPE_UNSPECIFIED", "STANDARD", "SPONSORSHIP"
    ]

@typing.type_check_only
class Proposal(typing_extensions.TypedDict, total=False):
    billedBuyer: str
    buyer: str
    buyerContacts: _list[Contact]
    buyerPrivateData: PrivateData
    client: str
    dealType: typing_extensions.Literal[
        "DEAL_TYPE_UNSPECIFIED",
        "PREFERRED_DEAL",
        "PRIVATE_AUCTION",
        "PROGRAMMATIC_GUARANTEED",
    ]
    displayName: str
    isRenegotiating: bool
    lastUpdaterOrCommentorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    name: str
    notes: _list[Note]
    originatorRole: typing_extensions.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    pausingConsented: bool
    proposalRevision: str
    publisherProfile: str
    sellerContacts: _list[Contact]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "BUYER_REVIEW_REQUESTED",
        "SELLER_REVIEW_REQUESTED",
        "BUYER_ACCEPTANCE_REQUESTED",
        "FINALIZED",
        "TERMINATED",
    ]
    termsAndConditions: str
    updateTime: str

@typing.type_check_only
class PublisherProfile(typing_extensions.TypedDict, total=False):
    audienceDescription: str
    directDealsContact: str
    displayName: str
    domains: _list[str]
    isParent: bool
    logoUrl: str
    mediaKitUrl: str
    mobileApps: _list[PublisherProfileMobileApplication]
    name: str
    overview: str
    pitchStatement: str
    programmaticDealsContact: str
    publisherCode: str
    samplePageUrl: str
    topHeadlines: _list[str]

@typing.type_check_only
class PublisherProfileMobileApplication(typing_extensions.TypedDict, total=False):
    appStore: typing_extensions.Literal[
        "APP_STORE_TYPE_UNSPECIFIED",
        "APPLE_ITUNES",
        "GOOGLE_PLAY",
        "ROKU",
        "AMAZON_FIRE_TV",
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
class ResumeFinalizedDealRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RtbMetrics(typing_extensions.TypedDict, total=False):
    adImpressions7Days: str
    bidRate7Days: float
    bidRequests7Days: str
    bids7Days: str
    filteredBidRate7Days: float
    mustBidRateCurrentMonth: float

@typing.type_check_only
class SendRfpRequest(typing_extensions.TypedDict, total=False):
    buyerContacts: _list[Contact]
    client: str
    displayName: str
    estimatedGrossSpend: Money
    flightEndTime: str
    flightStartTime: str
    geoTargeting: CriteriaTargeting
    inventorySizeTargeting: InventorySizeTargeting
    note: str
    preferredDealTerms: PreferredDealTerms
    programmaticGuaranteedTerms: ProgrammaticGuaranteedTerms
    publisherProfile: str

@typing.type_check_only
class SetReadyToServeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SubscribeAuctionPackageRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SubscribeClientsRequest(typing_extensions.TypedDict, total=False):
    clients: _list[str]

@typing.type_check_only
class TechnologyTargeting(typing_extensions.TypedDict, total=False):
    deviceCapabilityTargeting: CriteriaTargeting
    deviceCategoryTargeting: CriteriaTargeting
    operatingSystemTargeting: OperatingSystemTargeting

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class UnsubscribeAuctionPackageRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UnsubscribeClientsRequest(typing_extensions.TypedDict, total=False):
    clients: _list[str]

@typing.type_check_only
class UpdateDealRequest(typing_extensions.TypedDict, total=False):
    deal: Deal
    updateMask: str

@typing.type_check_only
class UriTargeting(typing_extensions.TypedDict, total=False):
    excludedUris: _list[str]
    targetedUris: _list[str]

@typing.type_check_only
class VideoTargeting(typing_extensions.TypedDict, total=False):
    excludedPositionTypes: _list[str]
    targetedPositionTypes: _list[str]
