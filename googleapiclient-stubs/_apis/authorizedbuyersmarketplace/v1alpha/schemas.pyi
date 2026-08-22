import typing

_list = list

@typing.type_check_only
class AcceptProposalRequest(typing.TypedDict, total=False):
    proposalRevision: str

@typing.type_check_only
class AccessControlSettings(typing.TypedDict, total=False):
    allowlistedMediaPlanners: _list[str]

@typing.type_check_only
class ActivateClientRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ActivateClientUserRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ActivateCuratedPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ActivateDataSegmentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class AdSize(typing.TypedDict, total=False):
    height: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"]
    width: str

@typing.type_check_only
class AddCreativeRequest(typing.TypedDict, total=False):
    creative: str

@typing.type_check_only
class AddNoteRequest(typing.TypedDict, total=False):
    note: Note

@typing.type_check_only
class AuctionPackage(typing.TypedDict, total=False):
    createTime: str
    creator: str
    dealOwnerSeatId: str
    description: str
    displayName: str
    eligibleSeatIds: _list[str]
    floorPriceCpm: Money
    name: str
    subscribedBuyers: _list[str]
    subscribedClients: _list[str]
    subscribedMediaPlanners: _list[MediaPlanner]
    updateTime: str

@typing.type_check_only
class BatchUpdateDealsRequest(typing.TypedDict, total=False):
    requests: _list[UpdateDealRequest]

@typing.type_check_only
class BatchUpdateDealsResponse(typing.TypedDict, total=False):
    deals: _list[Deal]

@typing.type_check_only
class CancelNegotiationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Client(typing.TypedDict, total=False):
    displayName: str
    name: str
    partnerClientId: str
    role: typing.Literal[
        "CLIENT_ROLE_UNSPECIFIED",
        "CLIENT_DEAL_VIEWER",
        "CLIENT_DEAL_NEGOTIATOR",
        "CLIENT_DEAL_APPROVER",
    ]
    sellerVisible: bool
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class ClientUser(typing.TypedDict, total=False):
    email: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "INVITED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class Contact(typing.TypedDict, total=False):
    displayName: str
    email: str

@typing.type_check_only
class CreativeRequirements(typing.TypedDict, total=False):
    creativeFormat: typing.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED", "DISPLAY", "VIDEO", "AUDIO"
    ]
    creativePreApprovalPolicy: typing.Literal[
        "CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED",
        "SELLER_PRE_APPROVAL_REQUIRED",
        "SELLER_PRE_APPROVAL_NOT_REQUIRED",
    ]
    creativeSafeFrameCompatibility: typing.Literal[
        "CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED", "COMPATIBLE", "INCOMPATIBLE"
    ]
    maxAdDurationMs: str
    programmaticCreativeSource: typing.Literal[
        "PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED", "ADVERTISER", "PUBLISHER"
    ]
    skippableAdType: typing.Literal[
        "SKIPPABLE_AD_TYPE_UNSPECIFIED",
        "SKIPPABLE",
        "INSTREAM_SELECT",
        "NOT_SKIPPABLE",
        "ANY",
    ]

@typing.type_check_only
class CriteriaTargeting(typing.TypedDict, total=False):
    excludedCriteriaIds: _list[str]
    targetedCriteriaIds: _list[str]

@typing.type_check_only
class CuratedPackage(typing.TypedDict, total=False):
    accessSettings: AccessControlSettings
    createTime: str
    curationFeeVisibility: typing.Literal[
        "CURATION_FEE_VISIBILITY_UNSPECIFIED", "DISCLOSED", "NON_DISCLOSED"
    ]
    description: str
    displayName: str
    feeCpm: Money
    floorPriceCpm: Money
    millipercentOfMediaFee: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    targeting: PackageTargeting
    updateTime: str

@typing.type_check_only
class DataSegment(typing.TypedDict, total=False):
    cpmFee: Money
    createTime: str
    millipercentOfMediaFee: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "SUSPENDED"]
    updateTime: str

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
    timeZoneType: typing.Literal["TIME_ZONE_TYPE_UNSPECIFIED", "SELLER", "USER"]

@typing.type_check_only
class DeactivateClientRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateClientUserRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateCuratedPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateDataSegmentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Deal(typing.TypedDict, total=False):
    billedBuyer: str
    buyer: str
    buyerPermissionType: typing.Literal[
        "BUYER_PERMISSION_TYPE_UNSPECIFIED", "NEGOTIATOR_ONLY", "BIDDER"
    ]
    client: str
    createTime: str
    creativeRequirements: CreativeRequirements
    dealType: typing.Literal[
        "DEAL_TYPE_UNSPECIFIED",
        "PREFERRED_DEAL",
        "PRIVATE_AUCTION",
        "PROGRAMMATIC_GUARANTEED",
    ]
    deliveryControl: DeliveryControl
    description: str
    displayName: str
    eligibleSeatIds: _list[str]
    estimatedGrossSpend: Money
    flightEndTime: str
    flightStartTime: str
    mediaPlanner: MediaPlanner
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
class DealPausingInfo(typing.TypedDict, total=False):
    pauseReason: str
    pauseRole: typing.Literal["BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"]
    pausingConsented: bool

@typing.type_check_only
class DeliveryControl(typing.TypedDict, total=False):
    companionDeliveryType: typing.Literal[
        "COMPANION_DELIVERY_TYPE_UNSPECIFIED",
        "DELIVERY_OPTIONAL",
        "DELIVERY_AT_LEAST_ONE",
        "DELIVERY_ALL",
    ]
    creativeRotationType: typing.Literal[
        "CREATIVE_ROTATION_TYPE_UNSPECIFIED",
        "ROTATION_EVEN",
        "ROTATION_OPTIMIZED",
        "ROTATION_MANUAL",
        "ROTATION_SEQUENTIAL",
    ]
    deliveryRateType: typing.Literal[
        "DELIVERY_RATE_TYPE_UNSPECIFIED",
        "EVENLY",
        "FRONT_LOADED",
        "AS_FAST_AS_POSSIBLE",
    ]
    frequencyCap: _list[FrequencyCap]
    roadblockingType: typing.Literal[
        "ROADBLOCKING_TYPE_UNSPECIFIED",
        "ONLY_ONE",
        "ONE_OR_MORE",
        "AS_MANY_AS_POSSIBLE",
        "ALL_ROADBLOCK",
        "CREATIVE_SET",
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FinalizedDeal(typing.TypedDict, total=False):
    deal: Deal
    dealPausingInfo: DealPausingInfo
    dealServingStatus: typing.Literal[
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
class FirstPartyMobileApplicationTargeting(typing.TypedDict, total=False):
    excludedAppIds: _list[str]
    targetedAppIds: _list[str]

@typing.type_check_only
class FrequencyCap(typing.TypedDict, total=False):
    maxImpressions: int
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
    timeUnitsCount: int

@typing.type_check_only
class InventorySizeTargeting(typing.TypedDict, total=False):
    excludedInventorySizes: _list[AdSize]
    targetedInventorySizes: _list[AdSize]

@typing.type_check_only
class InventoryTypeTargeting(typing.TypedDict, total=False):
    inventoryTypes: _list[
        typing.Literal[
            "INVENTORY_TYPE_UNSPECIFIED", "BROWSER", "MOBILE_APP", "VIDEO_PLAYER"
        ]
    ]

@typing.type_check_only
class ListAuctionPackagesResponse(typing.TypedDict, total=False):
    auctionPackages: _list[AuctionPackage]
    nextPageToken: str

@typing.type_check_only
class ListClientUsersResponse(typing.TypedDict, total=False):
    clientUsers: _list[ClientUser]
    nextPageToken: str

@typing.type_check_only
class ListClientsResponse(typing.TypedDict, total=False):
    clients: _list[Client]
    nextPageToken: str

@typing.type_check_only
class ListCuratedPackagesResponse(typing.TypedDict, total=False):
    curatedPackages: _list[CuratedPackage]
    nextPageToken: str

@typing.type_check_only
class ListDataSegmentsResponse(typing.TypedDict, total=False):
    dataSegments: _list[DataSegment]
    nextPageToken: str

@typing.type_check_only
class ListDealsResponse(typing.TypedDict, total=False):
    deals: _list[Deal]
    nextPageToken: str

@typing.type_check_only
class ListFinalizedDealsResponse(typing.TypedDict, total=False):
    finalizedDeals: _list[FinalizedDeal]
    nextPageToken: str

@typing.type_check_only
class ListMediaPlannersResponse(typing.TypedDict, total=False):
    mediaPlanners: _list[MediaPlanner]
    nextPageToken: str

@typing.type_check_only
class ListProposalsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    proposals: _list[Proposal]

@typing.type_check_only
class ListPublisherProfilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    publisherProfiles: _list[PublisherProfile]

@typing.type_check_only
class MarketplaceTargeting(typing.TypedDict, total=False):
    daypartTargeting: DayPartTargeting
    excludedSensitiveCategoryIds: _list[str]
    geoTargeting: CriteriaTargeting
    inventorySizeTargeting: InventorySizeTargeting
    inventoryTypeTargeting: InventoryTypeTargeting
    placementTargeting: PlacementTargeting
    technologyTargeting: TechnologyTargeting
    userListTargeting: CriteriaTargeting
    verticalTargeting: CriteriaTargeting
    videoTargeting: VideoTargeting

@typing.type_check_only
class MediaPlanner(typing.TypedDict, total=False):
    accountId: str
    ancestorNames: _list[str]
    displayName: str
    name: str

@typing.type_check_only
class MobileApplicationTargeting(typing.TypedDict, total=False):
    firstPartyTargeting: FirstPartyMobileApplicationTargeting

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Note(typing.TypedDict, total=False):
    createTime: str
    creatorRole: typing.Literal["BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"]
    note: str

@typing.type_check_only
class OperatingSystemTargeting(typing.TypedDict, total=False):
    operatingSystemCriteria: CriteriaTargeting
    operatingSystemVersionCriteria: CriteriaTargeting

@typing.type_check_only
class PackagePlacementTargeting(typing.TypedDict, total=False):
    includedMobileAppCategoryTargeting: _list[str]
    mobileAppTargeting: StringTargetingDimension
    uriTargeting: StringTargetingDimension

@typing.type_check_only
class PackagePublisherProvidedSignalsTargeting(typing.TypedDict, total=False):
    audienceTargeting: TaxonomyTargeting
    contentTargeting: TaxonomyTargeting
    videoAndAudioSignalsTargeting: StringTargetingDimension

@typing.type_check_only
class PackageTargeting(typing.TypedDict, total=False):
    geoTargeting: CriteriaTargeting
    includedAcceleratedMobilePageType: typing.Literal[
        "ACCELERATED_MOBILE_PAGE_TYPE_UNSPECIFIED",
        "ACCELERATED_MOBILE_PAGE_TYPE_NON_AMP",
        "ACCELERATED_MOBILE_PAGE_TYPE_AMP",
        "ACCELERATED_MOBILE_PAGE_TYPE_AMP_STORY",
    ]
    includedAdSizes: _list[AdSize]
    includedAuthorizedSellerStatuses: _list[
        typing.Literal[
            "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
            "AUTHORIZED_SELLER_STATUS_DIRECT",
            "AUTHORIZED_SELLER_STATUS_RESELLER",
        ]
    ]
    includedCreativeFormat: typing.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED",
        "CREATIVE_FORMAT_DISPLAY",
        "CREATIVE_FORMAT_VIDEO",
        "CREATIVE_FORMAT_AUDIO",
    ]
    includedDataSegments: _list[str]
    includedDeviceTypes: _list[
        typing.Literal[
            "DEVICE_TYPE_UNSPECIFIED",
            "DEVICE_TYPE_PERSONAL_COMPUTER",
            "DEVICE_TYPE_CONNECTED_TV",
            "DEVICE_TYPE_PHONE",
            "DEVICE_TYPE_TABLET",
        ]
    ]
    includedEnvironment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED", "ENVIRONMENT_SITE", "ENVIRONMENT_APP"
    ]
    includedNativeInventoryTypes: _list[
        typing.Literal[
            "NATIVE_INVENTORY_TYPE_UNSPECIFIED",
            "NATIVE_INVENTORY_TYPE_NATIVE_ONLY",
            "NATIVE_INVENTORY_TYPE_NATIVE_OR_BANNER",
        ]
    ]
    includedOpenMeasurementTypes: _list[
        typing.Literal[
            "OPEN_MEASUREMENT_TYPE_UNSPECIFIED", "OPEN_MEASUREMENT_TYPE_OMID_V1"
        ]
    ]
    includedRestrictedCategories: _list[
        typing.Literal[
            "RESTRICTED_CATEGORY_UNSPECIFIED",
            "RESTRICTED_CATEGORY_ALCOHOL",
            "RESTRICTED_CATEGORY_GAMBLING",
        ]
    ]
    includedRewardedType: typing.Literal[
        "REWARDED_TYPE_UNSPECIFIED",
        "REWARDED_TYPE_NON_REWARDED",
        "REWARDED_TYPE_REWARDED",
    ]
    languageTargeting: StringTargetingDimension
    minimumPredictedClickThroughRatePercentageMillis: str
    minimumPredictedViewabilityPercentage: str
    placementTargeting: PackagePlacementTargeting
    publisherProvidedSignalsTargeting: PackagePublisherProvidedSignalsTargeting
    publisherTargeting: StringTargetingDimension
    verticalTargeting: CriteriaTargeting
    videoTargeting: PackageVideoTargeting

@typing.type_check_only
class PackageVideoTargeting(typing.TypedDict, total=False):
    includedContentDeliveryMethod: typing.Literal[
        "CONTENT_DELIVERY_METHOD_UNSPECIFIED",
        "CONTENT_DELIVERY_METHOD_STREAMING",
        "CONTENT_DELIVERY_METHOD_PROGRESSIVE",
    ]
    includedMaximumAdDurationTargeting: typing.Literal[
        "MAXIMUM_VIDEO_AD_DURATION_UNSPECIFIED",
        "MAXIMUM_VIDEO_AD_DURATION_FIFTEEN_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_TWENTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_THIRTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_SIXTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_NINETY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_ONE_HUNDRED_TWENTY_SECONDS",
    ]
    includedMimeTypes: _list[
        typing.Literal[
            "VIDEO_MIME_TYPE_UNSPECIFIED",
            "VIDEO_MIME_TYPE_THREEGPP",
            "VIDEO_MIME_TYPE_APPLICATION_MPEGURL",
            "VIDEO_MIME_TYPE_MP4",
            "VIDEO_MIME_TYPE_APPLICATION_MPEGDASH",
            "VIDEO_MIME_TYPE_APPLICATION_JAVASCRIPT",
            "VIDEO_MIME_TYPE_WEBM",
        ]
    ]
    includedPlaybackMethods: _list[
        typing.Literal[
            "PLAYBACK_METHOD_UNSPECIFIED",
            "PLAYBACK_METHOD_AUTO_PLAY_SOUND_ON",
            "PLAYBACK_METHOD_AUTO_PLAY_SOUND_OFF",
            "PLAYBACK_METHOD_CLICK_TO_PLAY",
        ]
    ]
    includedPlayerSizeTargeting: VideoPlayerSizeTargeting
    includedPositionTypes: _list[
        typing.Literal[
            "POSITION_TYPE_UNSPECIFIED",
            "POSITION_TYPE_MIDROLL",
            "POSITION_TYPE_POSTROLL",
            "POSITION_TYPE_PREROLL",
        ]
    ]
    minimumPredictedCompletionRatePercentage: str
    plcmtTargeting: VideoPlcmtTargeting

@typing.type_check_only
class PauseFinalizedDealRequest(typing.TypedDict, total=False):
    reason: str

@typing.type_check_only
class PlacementTargeting(typing.TypedDict, total=False):
    mobileApplicationTargeting: MobileApplicationTargeting
    uriTargeting: UriTargeting

@typing.type_check_only
class PreferredDealTerms(typing.TypedDict, total=False):
    fixedPrice: Price

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    amount: Money
    type: typing.Literal["TYPE_UNSPECIFIED", "CPM", "CPD"]

@typing.type_check_only
class PrivateAuctionTerms(typing.TypedDict, total=False):
    floorPrice: Price
    openAuctionAllowed: bool

@typing.type_check_only
class PrivateData(typing.TypedDict, total=False):
    referenceId: str

@typing.type_check_only
class ProgrammaticGuaranteedTerms(typing.TypedDict, total=False):
    fixedPrice: Price
    guaranteedLooks: str
    impressionCap: str
    minimumDailyLooks: str
    percentShareOfVoice: str
    reservationType: typing.Literal[
        "RESERVATION_TYPE_UNSPECIFIED", "STANDARD", "SPONSORSHIP"
    ]

@typing.type_check_only
class Proposal(typing.TypedDict, total=False):
    billedBuyer: str
    buyer: str
    buyerContacts: _list[Contact]
    buyerPrivateData: PrivateData
    client: str
    dealType: typing.Literal[
        "DEAL_TYPE_UNSPECIFIED",
        "PREFERRED_DEAL",
        "PRIVATE_AUCTION",
        "PROGRAMMATIC_GUARANTEED",
    ]
    displayName: str
    isRenegotiating: bool
    lastUpdaterOrCommentorRole: typing.Literal[
        "BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"
    ]
    name: str
    notes: _list[Note]
    originatorRole: typing.Literal["BUYER_SELLER_ROLE_UNSPECIFIED", "BUYER", "SELLER"]
    pausingConsented: bool
    proposalRevision: str
    publisherProfile: str
    sellerContacts: _list[Contact]
    state: typing.Literal[
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
class PublisherProfile(typing.TypedDict, total=False):
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
class PublisherProfileMobileApplication(typing.TypedDict, total=False):
    appStore: typing.Literal[
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
        "LG_TV",
    ]
    externalAppId: str
    name: str

@typing.type_check_only
class ResumeFinalizedDealRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RtbMetrics(typing.TypedDict, total=False):
    adImpressions7Days: str
    bidRate7Days: float
    bidRequests7Days: str
    bids7Days: str
    filteredBidRate7Days: float
    mustBidRateCurrentMonth: float

@typing.type_check_only
class SendRfpRequest(typing.TypedDict, total=False):
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
class SetReadyToServeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StringTargetingDimension(typing.TypedDict, total=False):
    selectionType: typing.Literal[
        "SELECTION_TYPE_UNSPECIFIED", "SELECTION_TYPE_INCLUDE", "SELECTION_TYPE_EXCLUDE"
    ]
    values: _list[str]

@typing.type_check_only
class SubscribeAuctionPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SubscribeClientsRequest(typing.TypedDict, total=False):
    clients: _list[str]

@typing.type_check_only
class TaxonomyTargeting(typing.TypedDict, total=False):
    excludedTaxonomyIds: _list[str]
    targetedTaxonomyIds: _list[str]

@typing.type_check_only
class TechnologyTargeting(typing.TypedDict, total=False):
    deviceCapabilityTargeting: CriteriaTargeting
    deviceCategoryTargeting: CriteriaTargeting
    operatingSystemTargeting: OperatingSystemTargeting

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class UnsubscribeAuctionPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UnsubscribeClientsRequest(typing.TypedDict, total=False):
    clients: _list[str]

@typing.type_check_only
class UpdateDealRequest(typing.TypedDict, total=False):
    deal: Deal
    updateMask: str

@typing.type_check_only
class UriTargeting(typing.TypedDict, total=False):
    excludedUris: _list[str]
    targetedUris: _list[str]

@typing.type_check_only
class VideoPlayerSizeTargeting(typing.TypedDict, total=False):
    minimumHeight: str
    minimumWidth: str

@typing.type_check_only
class VideoPlcmtTargeting(typing.TypedDict, total=False):
    selectionType: typing.Literal[
        "SELECTION_TYPE_UNSPECIFIED", "SELECTION_TYPE_INCLUDE", "SELECTION_TYPE_EXCLUDE"
    ]
    videoPlcmtTypes: _list[
        typing.Literal[
            "VIDEO_PLCMT_TYPE_UNSPECIFIED",
            "INSTREAM",
            "ACCOMPANYING_CONTENT",
            "INTERSTITIAL",
            "NO_CONTENT",
        ]
    ]

@typing.type_check_only
class VideoTargeting(typing.TypedDict, total=False):
    excludedPositionTypes: _list[
        typing.Literal["POSITION_TYPE_UNSPECIFIED", "PREROLL", "MIDROLL", "POSTROLL"]
    ]
    targetedPositionTypes: _list[
        typing.Literal["POSITION_TYPE_UNSPECIFIED", "PREROLL", "MIDROLL", "POSTROLL"]
    ]
