import typing

import typing_extensions

class BulkEditNegativeKeywordsResponse(typing_extensions.TypedDict, total=False):
    negativeKeywords: typing.List[NegativeKeyword]

class ParentEntityFilter(typing_extensions.TypedDict, total=False):
    fileType: typing.List[str]
    filterIds: typing.List[str]
    filterType: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "FILTER_TYPE_NONE",
        "FILTER_TYPE_ADVERTISER_ID",
        "FILTER_TYPE_CAMPAIGN_ID",
        "FILTER_TYPE_MEDIA_PRODUCT_ID",
        "FILTER_TYPE_INSERTION_ORDER_ID",
        "FILTER_TYPE_LINE_ITEM_ID",
    ]

class InventorySourceAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    inventorySourceId: str

class LocationList(typing_extensions.TypedDict, total=False):
    locationType: typing_extensions.Literal[
        "TARGETING_LOCATION_TYPE_UNSPECIFIED",
        "TARGETING_LOCATION_TYPE_PROXIMITY",
        "TARGETING_LOCATION_TYPE_REGIONAL",
    ]
    advertiserId: str
    displayName: str
    name: str
    locationListId: str

class ExchangeConfigEnabledExchange(typing_extensions.TypedDict, total=False):
    seatId: str
    googleAdManagerAgencyId: str
    exchange: typing_extensions.Literal[
        "EXCHANGE_UNSPECIFIED",
        "EXCHANGE_GOOGLE_AD_MANAGER",
        "EXCHANGE_APPNEXUS",
        "EXCHANGE_BRIGHTROLL",
        "EXCHANGE_ADFORM",
        "EXCHANGE_ADMETA",
        "EXCHANGE_ADMIXER",
        "EXCHANGE_ADSMOGO",
        "EXCHANGE_ADSWIZZ",
        "EXCHANGE_BIDSWITCH",
        "EXCHANGE_BRIGHTROLL_DISPLAY",
        "EXCHANGE_CADREON",
        "EXCHANGE_DAILYMOTION",
        "EXCHANGE_FIVE",
        "EXCHANGE_FLUCT",
        "EXCHANGE_FREEWHEEL",
        "EXCHANGE_GENIEE",
        "EXCHANGE_GUMGUM",
        "EXCHANGE_IMOBILE",
        "EXCHANGE_IBILLBOARD",
        "EXCHANGE_IMPROVE_DIGITAL",
        "EXCHANGE_INDEX",
        "EXCHANGE_KARGO",
        "EXCHANGE_MICROAD",
        "EXCHANGE_MOPUB",
        "EXCHANGE_NEND",
        "EXCHANGE_ONE_BY_AOL_DISPLAY",
        "EXCHANGE_ONE_BY_AOL_MOBILE",
        "EXCHANGE_ONE_BY_AOL_VIDEO",
        "EXCHANGE_OOYALA",
        "EXCHANGE_OPENX",
        "EXCHANGE_PERMODO",
        "EXCHANGE_PLATFORMONE",
        "EXCHANGE_PLATFORMID",
        "EXCHANGE_PUBMATIC",
        "EXCHANGE_PULSEPOINT",
        "EXCHANGE_REVENUEMAX",
        "EXCHANGE_RUBICON",
        "EXCHANGE_SMARTCLIP",
        "EXCHANGE_SMARTRTB",
        "EXCHANGE_SMARTSTREAMTV",
        "EXCHANGE_SOVRN",
        "EXCHANGE_SPOTXCHANGE",
        "EXCHANGE_STROER",
        "EXCHANGE_TEADSTV",
        "EXCHANGE_TELARIA",
        "EXCHANGE_TVN",
        "EXCHANGE_UNITED",
        "EXCHANGE_YIELDLAB",
        "EXCHANGE_YIELDMO",
        "EXCHANGE_UNRULYX",
        "EXCHANGE_OPEN8",
        "EXCHANGE_TRITON",
        "EXCHANGE_TRIPLELIFT",
        "EXCHANGE_TABOOLA",
        "EXCHANGE_INMOBI",
        "EXCHANGE_SMAATO",
        "EXCHANGE_AJA",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
    ]
    googleAdManagerBuyerNetworkId: str

class SubExchangeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str

class BulkEditAssignedInventorySourcesResponse(
    typing_extensions.TypedDict, total=False
):
    assignedInventorySources: typing.List[AssignedInventorySource]

class CampaignFlight(typing_extensions.TypedDict, total=False):
    plannedDates: DateRange
    plannedSpendAmountMicros: str

class AgeRangeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_PLUS",
        "AGE_RANGE_UNKNOWN",
    ]

class ListLocationListsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locationLists: typing.List[LocationList]

class GenderAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    targetingOptionId: str
    gender: typing_extensions.Literal[
        "GENDER_UNSPECIFIED", "GENDER_MALE", "GENDER_FEMALE", "GENDER_UNKNOWN"
    ]

class BulkEditNegativeKeywordsRequest(typing_extensions.TypedDict, total=False):
    createdNegativeKeywords: typing.List[NegativeKeyword]
    deletedNegativeKeywords: typing.List[str]

class DigitalContentLabelAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentRatingTier: typing_extensions.Literal[
        "CONTENT_RATING_TIER_UNSPECIFIED",
        "CONTENT_RATING_TIER_UNRATED",
        "CONTENT_RATING_TIER_GENERAL",
        "CONTENT_RATING_TIER_PARENTAL_GUIDANCE",
        "CONTENT_RATING_TIER_TEENS",
        "CONTENT_RATING_TIER_MATURE",
    ]
    excludedTargetingOptionId: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status
    done: bool
    response: typing.Dict[str, typing.Any]

class CreateSdfDownloadTaskRequest(typing_extensions.TypedDict, total=False):
    partnerId: str
    idFilter: IdFilter
    version: typing_extensions.Literal[
        "SDF_VERSION_UNSPECIFIED",
        "SDF_VERSION_3_1",
        "SDF_VERSION_4",
        "SDF_VERSION_4_1",
        "SDF_VERSION_4_2",
        "SDF_VERSION_5",
        "SDF_VERSION_5_1",
        "SDF_VERSION_5_2",
    ]
    inventorySourceFilter: InventorySourceFilter
    advertiserId: str
    parentEntityFilter: ParentEntityFilter

class CategoryAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

class DoubleVerify(typing_extensions.TypedDict, total=False):
    videoViewability: DoubleVerifyVideoViewability
    avoidedAgeRatings: typing.List[str]
    fraudInvalidTraffic: DoubleVerifyFraudInvalidTraffic
    displayViewability: DoubleVerifyDisplayViewability
    appStarRating: DoubleVerifyAppStarRating
    brandSafetyCategories: DoubleVerifyBrandSafetyCategories

class UserRewardedContentAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    userRewardedContent: typing_extensions.Literal[
        "USER_REWARDED_CONTENT_UNSPECIFIED",
        "USER_REWARDED_CONTENT_USER_REWARDED",
        "USER_REWARDED_CONTENT_NOT_USER_REWARDED",
    ]

class BulkEditAssignedInventorySourcesRequest(typing_extensions.TypedDict, total=False):
    createdAssignedInventorySources: typing.List[AssignedInventorySource]
    partnerId: str
    advertiserId: str
    deletedAssignedInventorySources: typing.List[str]

class OperatingSystemAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    negative: bool
    targetingOptionId: str

class CombinedAudienceTargetingSetting(typing_extensions.TypedDict, total=False):
    combinedAudienceId: str

class ParentalStatusAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    parentalStatus: typing_extensions.Literal[
        "PARENTAL_STATUS_UNSPECIFIED",
        "PARENTAL_STATUS_PARENT",
        "PARENTAL_STATUS_NOT_A_PARENT",
        "PARENTAL_STATUS_UNKNOWN",
    ]

class PartnerCost(typing_extensions.TypedDict, total=False):
    feePercentageMillis: str
    costType: typing_extensions.Literal[
        "PARTNER_COST_TYPE_UNSPECIFIED",
        "PARTNER_COST_TYPE_ADLOOX",
        "PARTNER_COST_TYPE_ADLOOX_PREBID",
        "PARTNER_COST_TYPE_ADSAFE",
        "PARTNER_COST_TYPE_ADXPOSE",
        "PARTNER_COST_TYPE_AGGREGATE_KNOWLEDGE",
        "PARTNER_COST_TYPE_AGENCY_TRADING_DESK",
        "PARTNER_COST_TYPE_DV360_FEE",
        "PARTNER_COST_TYPE_COMSCORE_VCE",
        "PARTNER_COST_TYPE_DATA_MANAGEMENT_PLATFORM",
        "PARTNER_COST_TYPE_DEFAULT",
        "PARTNER_COST_TYPE_DOUBLE_VERIFY",
        "PARTNER_COST_TYPE_DOUBLE_VERIFY_PREBID",
        "PARTNER_COST_TYPE_EVIDON",
        "PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_VIDEO",
        "PARTNER_COST_TYPE_INTEGRAL_AD_SCIENCE_PREBID",
        "PARTNER_COST_TYPE_MEDIA_COST_DATA",
        "PARTNER_COST_TYPE_MOAT_VIDEO",
        "PARTNER_COST_TYPE_NIELSEN_DAR",
        "PARTNER_COST_TYPE_SHOP_LOCAL",
        "PARTNER_COST_TYPE_TERACENT",
        "PARTNER_COST_TYPE_THIRD_PARTY_AD_SERVER",
        "PARTNER_COST_TYPE_TRUST_METRICS",
        "PARTNER_COST_TYPE_VIZU",
        "PARTNER_COST_TYPE_ADLINGO_FEE",
        "PARTNER_COST_TYPE_CUSTOM_FEE_1",
        "PARTNER_COST_TYPE_CUSTOM_FEE_2",
        "PARTNER_COST_TYPE_CUSTOM_FEE_3",
        "PARTNER_COST_TYPE_CUSTOM_FEE_4",
        "PARTNER_COST_TYPE_CUSTOM_FEE_5",
    ]
    invoiceType: typing_extensions.Literal[
        "PARTNER_COST_INVOICE_TYPE_UNSPECIFIED",
        "PARTNER_COST_INVOICE_TYPE_DV360",
        "PARTNER_COST_INVOICE_TYPE_PARTNER",
    ]
    feeAmount: str
    feeType: typing_extensions.Literal[
        "PARTNER_COST_FEE_TYPE_UNSPECIFIED",
        "PARTNER_COST_FEE_TYPE_CPM_FEE",
        "PARTNER_COST_FEE_TYPE_MEDIA_FEE",
    ]

class ListInventorySourcesResponse(typing_extensions.TypedDict, total=False):
    inventorySources: typing.List[InventorySource]
    nextPageToken: str

class AssetAssociation(typing_extensions.TypedDict, total=False):
    asset: Asset
    role: typing_extensions.Literal[
        "ASSET_ROLE_UNSPECIFIED",
        "ASSET_ROLE_MAIN",
        "ASSET_ROLE_BACKUP",
        "ASSET_ROLE_POLITE_LOAD",
        "ASSET_ROLE_HEADLINE",
        "ASSET_ROLE_LONG_HEADLINE",
        "ASSET_ROLE_BODY",
        "ASSET_ROLE_LONG_BODY",
        "ASSET_ROLE_CAPTION_URL",
        "ASSET_ROLE_CALL_TO_ACTION",
        "ASSET_ROLE_ADVERTISER_NAME",
        "ASSET_ROLE_PRICE",
        "ASSET_ROLE_ANDROID_APP_ID",
        "ASSET_ROLE_IOS_APP_ID",
        "ASSET_ROLE_RATING",
        "ASSET_ROLE_ICON",
        "ASSET_ROLE_COVER_IMAGE",
    ]

class ListLineItemsResponse(typing_extensions.TypedDict, total=False):
    lineItems: typing.List[LineItem]
    nextPageToken: str

class BulkEditSitesRequest(typing_extensions.TypedDict, total=False):
    partnerId: str
    createdSites: typing.List[Site]
    deletedSites: typing.List[str]
    advertiserId: str

class GoogleAudienceGroup(typing_extensions.TypedDict, total=False):
    settings: typing.List[GoogleAudienceTargetingSetting]

class BulkEditSitesResponse(typing_extensions.TypedDict, total=False):
    sites: typing.List[Site]

class NegativeKeywordList(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    advertiserId: str
    negativeKeywordListId: str

class UrlAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    negative: bool
    url: str

class PartnerRevenueModel(typing_extensions.TypedDict, total=False):
    markupType: typing_extensions.Literal[
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_CPM",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_MEDIA_COST_MARKUP",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_TOTAL_MEDIA_COST_MARKUP",
    ]
    markupAmount: str

class CustomBiddingAlgorithm(typing_extensions.TypedDict, total=False):
    displayName: str
    advertiserId: str
    customBiddingAlgorithmId: str
    partnerId: str
    name: str
    customBiddingAlgorithmType: typing_extensions.Literal[
        "CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED",
        "SCRIPT_BASED",
        "ADS_DATA_HUB_BASED",
    ]
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]

class AgeRangeAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    ageRange: typing_extensions.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_PLUS",
        "AGE_RANGE_UNKNOWN",
    ]
    targetingOptionId: str

class InventorySourceFilter(typing_extensions.TypedDict, total=False):
    inventorySourceIds: typing.List[str]

class ListInventorySourceGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    inventorySourceGroups: typing.List[InventorySourceGroup]

class CreateAssetRequest(typing_extensions.TypedDict, total=False):
    filename: str

class AdvertiserDataAccessConfig(typing_extensions.TypedDict, total=False):
    sdfConfig: AdvertiserSdfConfig

class GenderTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    gender: typing_extensions.Literal[
        "GENDER_UNSPECIFIED", "GENDER_MALE", "GENDER_FEMALE", "GENDER_UNKNOWN"
    ]

class Campaign(typing_extensions.TypedDict, total=False):
    updateTime: str
    frequencyCap: FrequencyCap
    campaignGoal: CampaignGoal
    advertiserId: str
    campaignFlight: CampaignFlight
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    name: str
    displayName: str
    campaignId: str

class ProximityLocationListAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    proximityLocationListId: str
    proximityRadiusRange: typing_extensions.Literal[
        "PROXIMITY_RADIUS_RANGE_UNSPECIFIED",
        "PROXIMITY_RADIUS_RANGE_SMALL",
        "PROXIMITY_RADIUS_RANGE_MEDIUM",
        "PROXIMITY_RADIUS_RANGE_LARGE",
    ]

class FrequencyCap(typing_extensions.TypedDict, total=False):
    timeUnitCount: int
    unlimited: bool
    maxImpressions: int
    timeUnit: typing_extensions.Literal[
        "TIME_UNIT_UNSPECIFIED",
        "TIME_UNIT_LIFETIME",
        "TIME_UNIT_MONTHS",
        "TIME_UNIT_WEEKS",
        "TIME_UNIT_DAYS",
        "TIME_UNIT_HOURS",
        "TIME_UNIT_MINUTES",
    ]

class BrowserTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class BulkListLineItemAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: typing.List[AssignedTargetingOption]
    nextPageToken: str

class InventorySourceStatus(typing_extensions.TypedDict, total=False):
    sellerStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    entityPauseReason: str
    sellerPauseReason: str
    configStatus: typing_extensions.Literal[
        "INVENTORY_SOURCE_CONFIG_STATUS_UNSPECIFIED",
        "INVENTORY_SOURCE_CONFIG_STATUS_PENDING",
        "INVENTORY_SOURCE_CONFIG_STATUS_COMPLETED",
    ]

class DeviceTypeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "DEVICE_TYPE_COMPUTER",
        "DEVICE_TYPE_CONNECTED_TV",
        "DEVICE_TYPE_SMART_PHONE",
        "DEVICE_TYPE_TABLET",
    ]
    targetingOptionId: str

class ListGoogleAudiencesResponse(typing_extensions.TypedDict, total=False):
    googleAudiences: typing.List[GoogleAudience]
    nextPageToken: str

class UserRewardedContentTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    userRewardedContent: typing_extensions.Literal[
        "USER_REWARDED_CONTENT_UNSPECIFIED",
        "USER_REWARDED_CONTENT_USER_REWARDED",
        "USER_REWARDED_CONTENT_NOT_USER_REWARDED",
    ]

class ListCampaignsResponse(typing_extensions.TypedDict, total=False):
    campaigns: typing.List[Campaign]
    nextPageToken: str

class BulkListAdvertiserAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: typing.List[AssignedTargetingOption]
    nextPageToken: str

class NegativeKeywordListAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    negativeKeywordListId: str

class ConversionCountingConfig(typing_extensions.TypedDict, total=False):
    postViewCountPercentageMillis: str
    floodlightActivityConfigs: typing.List[TrackingFloodlightActivityConfig]

class BulkEditAssignedUserRolesResponse(typing_extensions.TypedDict, total=False):
    createdAssignedUserRoles: typing.List[AssignedUserRole]

class AssignedUserRole(typing_extensions.TypedDict, total=False):
    assignedUserRoleId: str
    partnerId: str
    userRole: typing_extensions.Literal[
        "USER_ROLE_UNSPECIFIED",
        "ADMIN",
        "ADMIN_PARTNER_CLIENT",
        "STANDARD",
        "STANDARD_PLANNER",
        "STANDARD_PLANNER_LIMITED",
        "STANDARD_PARTNER_CLIENT",
        "READ_ONLY",
        "REPORTING_ONLY",
        "LIMITED_REPORTING_ONLY",
        "CREATIVE",
        "CREATIVE_ADMIN",
    ]
    advertiserId: str

class DoubleVerifyFraudInvalidTraffic(typing_extensions.TypedDict, total=False):
    avoidInsufficientOption: bool
    avoidedFraudOption: typing_extensions.Literal[
        "FRAUD_UNSPECIFIED",
        "AD_IMPRESSION_FRAUD_100",
        "AD_IMPRESSION_FRAUD_50",
        "AD_IMPRESSION_FRAUD_25",
        "AD_IMPRESSION_FRAUD_10",
        "AD_IMPRESSION_FRAUD_8",
        "AD_IMPRESSION_FRAUD_6",
        "AD_IMPRESSION_FRAUD_4",
        "AD_IMPRESSION_FRAUD_2",
    ]

class PerformanceGoal(typing_extensions.TypedDict, total=False):
    performanceGoalAmountMicros: str
    performanceGoalPercentageMicros: str
    performanceGoalType: typing_extensions.Literal[
        "PERFORMANCE_GOAL_TYPE_UNSPECIFIED",
        "PERFORMANCE_GOAL_TYPE_CPM",
        "PERFORMANCE_GOAL_TYPE_CPC",
        "PERFORMANCE_GOAL_TYPE_CPA",
        "PERFORMANCE_GOAL_TYPE_CTR",
        "PERFORMANCE_GOAL_TYPE_VIEWABILITY",
        "PERFORMANCE_GOAL_TYPE_CPIAVC",
        "PERFORMANCE_GOAL_TYPE_CPE",
        "PERFORMANCE_GOAL_TYPE_OTHER",
    ]
    performanceGoalString: str

class InsertionOrderBudget(typing_extensions.TypedDict, total=False):
    budgetSegments: typing.List[InsertionOrderBudgetSegment]
    budgetUnit: typing_extensions.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]
    automationType: typing_extensions.Literal[
        "INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED",
        "INSERTION_ORDER_AUTOMATION_TYPE_BUDGET",
        "INSERTION_ORDER_AUTOMATION_TYPE_NONE",
        "INSERTION_ORDER_AUTOMATION_TYPE_BID_BUDGET",
    ]

class AuthorizedSellerStatusAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    authorizedSellerStatus: typing_extensions.Literal[
        "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS",
    ]
    targetingOptionId: str

class AdvertiserTargetingConfig(typing_extensions.TypedDict, total=False):
    exemptTvFromViewabilityTargeting: bool

class ListCreativesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    creatives: typing.List[Creative]

class ListAdvertiserAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    assignedTargetingOptions: typing.List[AssignedTargetingOption]

class AudienceGroupAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    includedCombinedAudienceGroup: CombinedAudienceGroup
    includedFirstAndThirdPartyAudienceGroups: typing.List[
        FirstAndThirdPartyAudienceGroup
    ]
    excludedGoogleAudienceGroup: GoogleAudienceGroup
    excludedFirstAndThirdPartyAudienceGroup: FirstAndThirdPartyAudienceGroup
    includedCustomListGroup: CustomListGroup
    includedGoogleAudienceGroup: GoogleAudienceGroup

class ViewabilityAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    viewability: typing_extensions.Literal[
        "VIEWABILITY_UNSPECIFIED",
        "VIEWABILITY_10_PERCENT_OR_MORE",
        "VIEWABILITY_20_PERCENT_OR_MORE",
        "VIEWABILITY_30_PERCENT_OR_MORE",
        "VIEWABILITY_40_PERCENT_OR_MORE",
        "VIEWABILITY_50_PERCENT_OR_MORE",
        "VIEWABILITY_60_PERCENT_OR_MORE",
        "VIEWABILITY_70_PERCENT_OR_MORE",
        "VIEWABILITY_80_PERCENT_OR_MORE",
        "VIEWABILITY_90_PERCENT_OR_MORE",
    ]
    targetingOptionId: str

class AssignedLocation(typing_extensions.TypedDict, total=False):
    assignedLocationId: str
    targetingOptionId: str
    name: str

class CmHybridConfig(typing_extensions.TypedDict, total=False):
    cmSyncableSiteIds: typing.List[str]
    cmFloodlightConfigId: str
    dv360ToCmDataSharingEnabled: bool
    dv360ToCmCostReportingEnabled: bool
    cmFloodlightLinkingAuthorized: bool
    cmAccountId: str

class UniversalAdId(typing_extensions.TypedDict, total=False):
    registry: typing_extensions.Literal[
        "UNIVERSAL_AD_REGISTRY_UNSPECIFIED",
        "UNIVERSAL_AD_REGISTRY_OTHER",
        "UNIVERSAL_AD_REGISTRY_AD_ID",
        "UNIVERSAL_AD_REGISTRY_CLEARCAST",
        "UNIVERSAL_AD_REGISTRY_DV360",
        "UNIVERSAL_AD_REGISTRY_CM",
    ]
    id: str

class SdfConfig(typing_extensions.TypedDict, total=False):
    version: typing_extensions.Literal[
        "SDF_VERSION_UNSPECIFIED",
        "SDF_VERSION_3_1",
        "SDF_VERSION_4",
        "SDF_VERSION_4_1",
        "SDF_VERSION_4_2",
        "SDF_VERSION_5",
        "SDF_VERSION_5_1",
        "SDF_VERSION_5_2",
    ]
    adminEmail: str

class EnvironmentTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    environment: typing_extensions.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_WEB_OPTIMIZED",
        "ENVIRONMENT_WEB_NOT_OPTIMIZED",
        "ENVIRONMENT_APP",
    ]

class MaximizeSpendBidStrategy(typing_extensions.TypedDict, total=False):
    performanceGoalType: typing_extensions.Literal[
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CIVA",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_IVO_TEN",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_AV_VIEWED",
    ]
    maxAverageCpmBidAmountMicros: str
    customBiddingAlgorithmId: str

class OnScreenPositionTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    onScreenPosition: typing_extensions.Literal[
        "ON_SCREEN_POSITION_UNSPECIFIED",
        "ON_SCREEN_POSITION_UNKNOWN",
        "ON_SCREEN_POSITION_ABOVE_THE_FOLD",
        "ON_SCREEN_POSITION_BELOW_THE_FOLD",
    ]

class DeviceMakeModelTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class ThirdPartyUrl(typing_extensions.TypedDict, total=False):
    url: str
    type: typing_extensions.Literal[
        "THIRD_PARTY_URL_TYPE_UNSPECIFIED",
        "THIRD_PARTY_URL_TYPE_IMPRESSION",
        "THIRD_PARTY_URL_TYPE_CLICK_TRACKING",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_START",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_FIRST_QUARTILE",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_MIDPOINT",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_THIRD_QUARTILE",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_COMPLETE",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_MUTE",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_PAUSE",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_REWIND",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_FULLSCREEN",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_STOP",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_CUSTOM",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_SKIP",
        "THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_PROGRESS",
    ]

class TimerEvent(typing_extensions.TypedDict, total=False):
    name: str
    reportingName: str

class CreativeConfig(typing_extensions.TypedDict, total=False):
    creativeType: typing_extensions.Literal[
        "CREATIVE_TYPE_UNSPECIFIED",
        "CREATIVE_TYPE_STANDARD",
        "CREATIVE_TYPE_EXPANDABLE",
        "CREATIVE_TYPE_VIDEO",
        "CREATIVE_TYPE_NATIVE",
        "CREATIVE_TYPE_TEMPLATED_APP_INSTALL",
        "CREATIVE_TYPE_NATIVE_SITE_SQUARE",
        "CREATIVE_TYPE_TEMPLATED_APP_INSTALL_INTERSTITIAL",
        "CREATIVE_TYPE_LIGHTBOX",
        "CREATIVE_TYPE_NATIVE_APP_INSTALL",
        "CREATIVE_TYPE_NATIVE_APP_INSTALL_SQUARE",
        "CREATIVE_TYPE_AUDIO",
        "CREATIVE_TYPE_PUBLISHER_HOSTED",
        "CREATIVE_TYPE_NATIVE_VIDEO",
        "CREATIVE_TYPE_TEMPLATED_APP_INSTALL_VIDEO",
    ]
    displayCreativeConfig: InventorySourceDisplayCreativeConfig
    videoCreativeConfig: InventorySourceVideoCreativeConfig

class CustomListGroup(typing_extensions.TypedDict, total=False):
    settings: typing.List[CustomListTargetingSetting]

class PartnerDataAccessConfig(typing_extensions.TypedDict, total=False):
    sdfConfig: SdfConfig

class BulkEditPartnerAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    createdAssignedTargetingOptions: typing.List[AssignedTargetingOption]

class PublisherReviewStatus(typing_extensions.TypedDict, total=False):
    publisherName: str
    status: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]

class Money(typing_extensions.TypedDict, total=False):
    units: str
    currencyCode: str
    nanos: int

class ChannelAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    negative: bool
    channelId: str

class RegionalLocationListAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    negative: bool
    regionalLocationListId: str

class ListLineItemAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: typing.List[AssignedTargetingOption]
    nextPageToken: str

class SubExchangeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class FirstAndThirdPartyAudienceTargetingSetting(
    typing_extensions.TypedDict, total=False
):
    recency: typing_extensions.Literal[
        "RECENCY_NO_LIMIT",
        "RECENCY_1_MINUTE",
        "RECENCY_5_MINUTES",
        "RECENCY_10_MINUTES",
        "RECENCY_15_MINUTES",
        "RECENCY_30_MINUTES",
        "RECENCY_1_HOUR",
        "RECENCY_2_HOURS",
        "RECENCY_3_HOURS",
        "RECENCY_6_HOURS",
        "RECENCY_12_HOURS",
        "RECENCY_1_DAY",
        "RECENCY_2_DAYS",
        "RECENCY_3_DAYS",
        "RECENCY_5_DAYS",
        "RECENCY_7_DAYS",
        "RECENCY_10_DAYS",
        "RECENCY_14_DAYS",
        "RECENCY_15_DAYS",
        "RECENCY_21_DAYS",
        "RECENCY_28_DAYS",
        "RECENCY_30_DAYS",
        "RECENCY_40_DAYS",
        "RECENCY_60_DAYS",
        "RECENCY_90_DAYS",
        "RECENCY_120_DAYS",
        "RECENCY_180_DAYS",
        "RECENCY_270_DAYS",
        "RECENCY_365_DAYS",
    ]
    firstAndThirdPartyAudienceId: str

class LineItemBudget(typing_extensions.TypedDict, total=False):
    maxAmount: str
    budgetUnit: typing_extensions.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]
    budgetAllocationType: typing_extensions.Literal[
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED",
    ]

class Adloox(typing_extensions.TypedDict, total=False):
    excludedAdlooxCategories: typing.List[str]

class ExchangeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    exchange: typing_extensions.Literal[
        "EXCHANGE_UNSPECIFIED",
        "EXCHANGE_GOOGLE_AD_MANAGER",
        "EXCHANGE_APPNEXUS",
        "EXCHANGE_BRIGHTROLL",
        "EXCHANGE_ADFORM",
        "EXCHANGE_ADMETA",
        "EXCHANGE_ADMIXER",
        "EXCHANGE_ADSMOGO",
        "EXCHANGE_ADSWIZZ",
        "EXCHANGE_BIDSWITCH",
        "EXCHANGE_BRIGHTROLL_DISPLAY",
        "EXCHANGE_CADREON",
        "EXCHANGE_DAILYMOTION",
        "EXCHANGE_FIVE",
        "EXCHANGE_FLUCT",
        "EXCHANGE_FREEWHEEL",
        "EXCHANGE_GENIEE",
        "EXCHANGE_GUMGUM",
        "EXCHANGE_IMOBILE",
        "EXCHANGE_IBILLBOARD",
        "EXCHANGE_IMPROVE_DIGITAL",
        "EXCHANGE_INDEX",
        "EXCHANGE_KARGO",
        "EXCHANGE_MICROAD",
        "EXCHANGE_MOPUB",
        "EXCHANGE_NEND",
        "EXCHANGE_ONE_BY_AOL_DISPLAY",
        "EXCHANGE_ONE_BY_AOL_MOBILE",
        "EXCHANGE_ONE_BY_AOL_VIDEO",
        "EXCHANGE_OOYALA",
        "EXCHANGE_OPENX",
        "EXCHANGE_PERMODO",
        "EXCHANGE_PLATFORMONE",
        "EXCHANGE_PLATFORMID",
        "EXCHANGE_PUBMATIC",
        "EXCHANGE_PULSEPOINT",
        "EXCHANGE_REVENUEMAX",
        "EXCHANGE_RUBICON",
        "EXCHANGE_SMARTCLIP",
        "EXCHANGE_SMARTRTB",
        "EXCHANGE_SMARTSTREAMTV",
        "EXCHANGE_SOVRN",
        "EXCHANGE_SPOTXCHANGE",
        "EXCHANGE_STROER",
        "EXCHANGE_TEADSTV",
        "EXCHANGE_TELARIA",
        "EXCHANGE_TVN",
        "EXCHANGE_UNITED",
        "EXCHANGE_YIELDLAB",
        "EXCHANGE_YIELDMO",
        "EXCHANGE_UNRULYX",
        "EXCHANGE_OPEN8",
        "EXCHANGE_TRITON",
        "EXCHANGE_TRIPLELIFT",
        "EXCHANGE_TABOOLA",
        "EXCHANGE_INMOBI",
        "EXCHANGE_SMAATO",
        "EXCHANGE_AJA",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
    ]

class IdFilter(typing_extensions.TypedDict, total=False):
    lineItemIds: typing.List[str]
    insertionOrderIds: typing.List[str]
    campaignIds: typing.List[str]
    mediaProductIds: typing.List[str]
    adGroupIds: typing.List[str]
    adGroupAdIds: typing.List[str]

class VideoPlayerSizeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    videoPlayerSize: typing_extensions.Literal[
        "VIDEO_PLAYER_SIZE_UNSPECIFIED",
        "VIDEO_PLAYER_SIZE_SMALL",
        "VIDEO_PLAYER_SIZE_LARGE",
        "VIDEO_PLAYER_SIZE_HD",
        "VIDEO_PLAYER_SIZE_UNKNOWN",
    ]

class InventorySourceGroupAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    inventorySourceGroupId: str

class BiddingStrategy(typing_extensions.TypedDict, total=False):
    maximizeSpendAutoBid: MaximizeSpendBidStrategy
    performanceGoalAutoBid: PerformanceGoalBidStrategy
    fixedBid: FixedBidStrategy

class CmTrackingAd(typing_extensions.TypedDict, total=False):
    cmPlacementId: str
    cmAdId: str
    cmCreativeId: str

class Site(typing_extensions.TypedDict, total=False):
    name: str
    urlOrAppId: str

class InventorySource(typing_extensions.TypedDict, total=False):
    creativeConfigs: typing.List[CreativeConfig]
    publisherName: str
    inventorySourceType: typing_extensions.Literal[
        "INVENTORY_SOURCE_TYPE_UNSPECIFIED",
        "INVENTORY_SOURCE_TYPE_PRIVATE",
        "INVENTORY_SOURCE_TYPE_AUCTION_PACKAGE",
    ]
    commitment: typing_extensions.Literal[
        "INVENTORY_SOURCE_COMMITMENT_UNSPECIFIED",
        "INVENTORY_SOURCE_COMMITMENT_GUARANTEED",
        "INVENTORY_SOURCE_COMMITMENT_NON_GUARANTEED",
    ]
    name: str
    rateDetails: RateDetails
    updateTime: str
    timeRange: TimeRange
    deliveryMethod: typing_extensions.Literal[
        "INVENTORY_SOURCE_DELIVERY_METHOD_UNSPECIFIED",
        "INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC",
        "INVENTORY_SOURCE_DELIVERY_METHOD_TAG",
    ]
    status: InventorySourceStatus
    exchange: typing_extensions.Literal[
        "EXCHANGE_UNSPECIFIED",
        "EXCHANGE_GOOGLE_AD_MANAGER",
        "EXCHANGE_APPNEXUS",
        "EXCHANGE_BRIGHTROLL",
        "EXCHANGE_ADFORM",
        "EXCHANGE_ADMETA",
        "EXCHANGE_ADMIXER",
        "EXCHANGE_ADSMOGO",
        "EXCHANGE_ADSWIZZ",
        "EXCHANGE_BIDSWITCH",
        "EXCHANGE_BRIGHTROLL_DISPLAY",
        "EXCHANGE_CADREON",
        "EXCHANGE_DAILYMOTION",
        "EXCHANGE_FIVE",
        "EXCHANGE_FLUCT",
        "EXCHANGE_FREEWHEEL",
        "EXCHANGE_GENIEE",
        "EXCHANGE_GUMGUM",
        "EXCHANGE_IMOBILE",
        "EXCHANGE_IBILLBOARD",
        "EXCHANGE_IMPROVE_DIGITAL",
        "EXCHANGE_INDEX",
        "EXCHANGE_KARGO",
        "EXCHANGE_MICROAD",
        "EXCHANGE_MOPUB",
        "EXCHANGE_NEND",
        "EXCHANGE_ONE_BY_AOL_DISPLAY",
        "EXCHANGE_ONE_BY_AOL_MOBILE",
        "EXCHANGE_ONE_BY_AOL_VIDEO",
        "EXCHANGE_OOYALA",
        "EXCHANGE_OPENX",
        "EXCHANGE_PERMODO",
        "EXCHANGE_PLATFORMONE",
        "EXCHANGE_PLATFORMID",
        "EXCHANGE_PUBMATIC",
        "EXCHANGE_PULSEPOINT",
        "EXCHANGE_REVENUEMAX",
        "EXCHANGE_RUBICON",
        "EXCHANGE_SMARTCLIP",
        "EXCHANGE_SMARTRTB",
        "EXCHANGE_SMARTSTREAMTV",
        "EXCHANGE_SOVRN",
        "EXCHANGE_SPOTXCHANGE",
        "EXCHANGE_STROER",
        "EXCHANGE_TEADSTV",
        "EXCHANGE_TELARIA",
        "EXCHANGE_TVN",
        "EXCHANGE_UNITED",
        "EXCHANGE_YIELDLAB",
        "EXCHANGE_YIELDMO",
        "EXCHANGE_UNRULYX",
        "EXCHANGE_OPEN8",
        "EXCHANGE_TRITON",
        "EXCHANGE_TRIPLELIFT",
        "EXCHANGE_TABOOLA",
        "EXCHANGE_INMOBI",
        "EXCHANGE_SMAATO",
        "EXCHANGE_AJA",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
    ]
    inventorySourceId: str
    displayName: str
    dealId: str

class ContentOutstreamPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentOutstreamPosition: typing_extensions.Literal[
        "CONTENT_OUTSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_OUTSTREAM_POSITION_UNKNOWN",
        "CONTENT_OUTSTREAM_POSITION_IN_ARTICLE",
        "CONTENT_OUTSTREAM_POSITION_IN_BANNER",
        "CONTENT_OUTSTREAM_POSITION_IN_FEED",
        "CONTENT_OUTSTREAM_POSITION_INTERSTITIAL",
    ]
    targetingOptionId: str

class InventorySourceVideoCreativeConfig(typing_extensions.TypedDict, total=False):
    duration: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class Partner(typing_extensions.TypedDict, total=False):
    displayName: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    updateTime: str
    partnerId: str
    adServerConfig: PartnerAdServerConfig
    generalConfig: PartnerGeneralConfig
    name: str
    dataAccessConfig: PartnerDataAccessConfig
    exchangeConfig: ExchangeConfig

class BulkEditLineItemAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    createdAssignedTargetingOptions: typing.List[AssignedTargetingOption]

class LineItem(typing_extensions.TypedDict, total=False):
    pacing: Pacing
    displayName: str
    inventorySourceIds: typing.List[str]
    lineItemId: str
    frequencyCap: FrequencyCap
    lineItemType: typing_extensions.Literal[
        "LINE_ITEM_TYPE_UNSPECIFIED",
        "LINE_ITEM_TYPE_DISPLAY_DEFAULT",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_VIDEO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_AUDIO_DEFAULT",
    ]
    flight: LineItemFlight
    advertiserId: str
    creativeIds: typing.List[str]
    conversionCounting: ConversionCountingConfig
    insertionOrderId: str
    partnerCosts: typing.List[PartnerCost]
    name: str
    warningMessages: typing.List[str]
    bidStrategy: BiddingStrategy
    campaignId: str
    budget: LineItemBudget
    partnerRevenueModel: PartnerRevenueModel
    integrationDetails: IntegrationDetails
    updateTime: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]

class AudioVideoOffset(typing_extensions.TypedDict, total=False):
    percentage: str
    seconds: str

class NegativeKeyword(typing_extensions.TypedDict, total=False):
    keywordValue: str
    name: str

class DoubleVerifyVideoViewability(typing_extensions.TypedDict, total=False):
    videoIab: typing_extensions.Literal[
        "VIDEO_IAB_UNSPECIFIED",
        "IAB_VIEWABILITY_80_PERCENT_HIGHER",
        "IAB_VIEWABILITY_75_PERCENT_HIGHER",
        "IAB_VIEWABILITY_70_PERCENT_HIGHER",
        "IAB_VIEWABILITY_65_PERCENT_HIHGER",
        "IAB_VIEWABILITY_60_PERCENT_HIGHER",
        "IAB_VIEWABILITY_55_PERCENT_HIHGER",
        "IAB_VIEWABILITY_50_PERCENT_HIGHER",
        "IAB_VIEWABILITY_40_PERCENT_HIHGER",
        "IAB_VIEWABILITY_30_PERCENT_HIHGER",
    ]
    videoViewableRate: typing_extensions.Literal[
        "VIDEO_VIEWABLE_RATE_UNSPECIFIED",
        "VIEWED_PERFORMANCE_40_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_35_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_30_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_25_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_20_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_10_PERCENT_HIGHER",
    ]
    playerImpressionRate: typing_extensions.Literal[
        "PLAYER_SIZE_400X300_UNSPECIFIED",
        "PLAYER_SIZE_400X300_95",
        "PLAYER_SIZE_400X300_70",
        "PLAYER_SIZE_400X300_25",
        "PLAYER_SIZE_400X300_5",
    ]

class AuditAdvertiserResponse(typing_extensions.TypedDict, total=False):
    usedLineItemsCount: str
    negativelyTargetedChannelsCount: str
    usedCampaignsCount: str
    campaignCriteriaCount: str
    usedInsertionOrdersCount: str
    channelsCount: str
    negativeKeywordListsCount: str
    adGroupCriteriaCount: str

class RateDetails(typing_extensions.TypedDict, total=False):
    inventorySourceRateType: typing_extensions.Literal[
        "INVENTORY_SOURCE_RATE_TYPE_UNSPECIFIED",
        "INVENTORY_SOURCE_RATE_TYPE_CPM_FIXED",
        "INVENTORY_SOURCE_RATE_TYPE_CPM_FLOOR",
        "INVENTORY_SOURCE_RATE_TYPE_CPD",
        "INVENTORY_SOURCE_RATE_TYPE_FLAT",
    ]
    rate: Money
    minimumSpend: Money
    unitsPurchased: str

class ContentInstreamPositionTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentInstreamPosition: typing_extensions.Literal[
        "CONTENT_INSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_INSTREAM_POSITION_PRE_ROLL",
        "CONTENT_INSTREAM_POSITION_MID_ROLL",
        "CONTENT_INSTREAM_POSITION_POST_ROLL",
    ]

class ListFirstAndThirdPartyAudiencesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    firstAndThirdPartyAudiences: typing.List[FirstAndThirdPartyAudience]

class BulkEditAssignedUserRolesRequest(typing_extensions.TypedDict, total=False):
    deletedAssignedUserRoles: typing.List[str]
    createdAssignedUserRoles: typing.List[AssignedUserRole]

class DeviceMakeModelAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    negative: bool
    targetingOptionId: str
    displayName: str

class ThirdPartyOnlyConfig(typing_extensions.TypedDict, total=False):
    pixelOrderIdReportingEnabled: bool

class BulkEditAssignedLocationsResponse(typing_extensions.TypedDict, total=False):
    assignedLocations: typing.List[AssignedLocation]

class AdvertiserCreativeConfig(typing_extensions.TypedDict, total=False):
    iasClientId: str
    obaComplianceDisabled: bool
    videoCreativeDataSharingAuthorized: bool
    dynamicCreativeEnabled: bool

class AdvertiserSdfConfig(typing_extensions.TypedDict, total=False):
    sdfConfig: SdfConfig
    overridePartnerSdfConfig: bool

class BrowserAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    negative: bool
    displayName: str
    targetingOptionId: str

class ListCustomBiddingAlgorithmsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    customBiddingAlgorithms: typing.List[CustomBiddingAlgorithm]

class CarrierAndIspAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    targetingOptionId: str
    negative: bool

class KeywordAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    keyword: str
    negative: bool

class IntegralAdScience(typing_extensions.TypedDict, total=False):
    excludedDrugsRisk: typing_extensions.Literal[
        "DRUGS_UNSPECIFIED", "DRUGS_HR", "DRUGS_HMR"
    ]
    excludedHateSpeechRisk: typing_extensions.Literal[
        "HATE_SPEECH_UNSPECIFIED", "HATE_SPEECH_HR", "HATE_SPEECH_HMR"
    ]
    excludeUnrateable: bool
    excludedViolenceRisk: typing_extensions.Literal[
        "VIOLENCE_UNSPECIFIED", "VIOLENCE_HR", "VIOLENCE_HMR"
    ]
    videoViewability: typing_extensions.Literal[
        "VIDEO_VIEWABILITY_UNSPECIFIED",
        "VIDEO_VIEWABILITY_40",
        "VIDEO_VIEWABILITY_50",
        "VIDEO_VIEWABILITY_60",
        "VIDEO_VIEWABILITY_70",
    ]
    excludedAlcoholRisk: typing_extensions.Literal[
        "ALCOHOL_UNSPECIFIED", "ALCOHOL_HR", "ALCOHOL_HMR"
    ]
    displayViewability: typing_extensions.Literal[
        "PERFORMANCE_VIEWABILITY_UNSPECIFIED",
        "PERFORMANCE_VIEWABILITY_40",
        "PERFORMANCE_VIEWABILITY_50",
        "PERFORMANCE_VIEWABILITY_60",
        "PERFORMANCE_VIEWABILITY_70",
    ]
    excludedIllegalDownloadsRisk: typing_extensions.Literal[
        "ILLEGAL_DOWNLOADS_UNSPECIFIED", "ILLEGAL_DOWNLOADS_HR", "ILLEGAL_DOWNLOADS_HMR"
    ]
    excludedOffensiveLanguageRisk: typing_extensions.Literal[
        "OFFENSIVE_LANGUAGE_UNSPECIFIED",
        "OFFENSIVE_LANGUAGE_HR",
        "OFFENSIVE_LANGUAGE_HMR",
    ]
    excludedAdFraudRisk: typing_extensions.Literal[
        "SUSPICIOUS_ACTIVITY_UNSPECIFIED",
        "SUSPICIOUS_ACTIVITY_HR",
        "SUSPICIOUS_ACTIVITY_HMR",
    ]
    excludedAdultRisk: typing_extensions.Literal[
        "ADULT_UNSPECIFIED", "ADULT_HR", "ADULT_HMR"
    ]
    traqScoreOption: typing_extensions.Literal[
        "TRAQ_UNSPECIFIED",
        "TRAQ_250",
        "TRAQ_500",
        "TRAQ_600",
        "TRAQ_700",
        "TRAQ_750",
        "TRAQ_875",
        "TRAQ_1000",
    ]
    excludedGamblingRisk: typing_extensions.Literal[
        "GAMBLING_UNSPECIFIED", "GAMBLING_HR", "GAMBLING_HMR"
    ]

class BulkEditAssignedLocationsRequest(typing_extensions.TypedDict, total=False):
    createdAssignedLocations: typing.List[AssignedLocation]
    deletedAssignedLocations: typing.List[str]

class ListAssignedLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    assignedLocations: typing.List[AssignedLocation]

class ListCombinedAudiencesResponse(typing_extensions.TypedDict, total=False):
    combinedAudiences: typing.List[CombinedAudience]
    nextPageToken: str

class BulkEditAdvertiserAssignedTargetingOptionsRequest(
    typing_extensions.TypedDict, total=False
):
    createRequests: typing.List[CreateAssignedTargetingOptionsRequest]
    deleteRequests: typing.List[DeleteAssignedTargetingOptionsRequest]

class ParentalStatusTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    parentalStatus: typing_extensions.Literal[
        "PARENTAL_STATUS_UNSPECIFIED",
        "PARENTAL_STATUS_PARENT",
        "PARENTAL_STATUS_NOT_A_PARENT",
        "PARENTAL_STATUS_UNKNOWN",
    ]

class BulkEditPartnerAssignedTargetingOptionsRequest(
    typing_extensions.TypedDict, total=False
):
    createRequests: typing.List[CreateAssignedTargetingOptionsRequest]
    deleteRequests: typing.List[DeleteAssignedTargetingOptionsRequest]

class AdvertiserAdServerConfig(typing_extensions.TypedDict, total=False):
    thirdPartyOnlyConfig: ThirdPartyOnlyConfig
    cmHybridConfig: CmHybridConfig

class FixedBidStrategy(typing_extensions.TypedDict, total=False):
    bidAmountMicros: str

class ListInsertionOrdersResponse(typing_extensions.TypedDict, total=False):
    insertionOrders: typing.List[InsertionOrder]
    nextPageToken: str

class ListPartnersResponse(typing_extensions.TypedDict, total=False):
    partners: typing.List[Partner]
    nextPageToken: str

class ActiveViewVideoViewabilityMetricConfig(typing_extensions.TypedDict, total=False):
    displayName: str
    minimumVolume: typing_extensions.Literal[
        "VIDEO_VOLUME_PERCENT_UNSPECIFIED",
        "VIDEO_VOLUME_PERCENT_0",
        "VIDEO_VOLUME_PERCENT_10",
    ]
    minimumViewability: typing_extensions.Literal[
        "VIEWABILITY_PERCENT_UNSPECIFIED",
        "VIEWABILITY_PERCENT_0",
        "VIEWABILITY_PERCENT_25",
        "VIEWABILITY_PERCENT_50",
        "VIEWABILITY_PERCENT_75",
        "VIEWABILITY_PERCENT_100",
    ]
    minimumQuartile: typing_extensions.Literal[
        "VIDEO_DURATION_QUARTILE_UNSPECIFIED",
        "VIDEO_DURATION_QUARTILE_NONE",
        "VIDEO_DURATION_QUARTILE_FIRST",
        "VIDEO_DURATION_QUARTILE_SECOND",
        "VIDEO_DURATION_QUARTILE_THIRD",
        "VIDEO_DURATION_QUARTILE_FOURTH",
    ]
    minimumDuration: typing_extensions.Literal[
        "VIDEO_DURATION_UNSPECIFIED",
        "VIDEO_DURATION_SECONDS_NONE",
        "VIDEO_DURATION_SECONDS_0",
        "VIDEO_DURATION_SECONDS_1",
        "VIDEO_DURATION_SECONDS_2",
        "VIDEO_DURATION_SECONDS_3",
        "VIDEO_DURATION_SECONDS_4",
        "VIDEO_DURATION_SECONDS_5",
        "VIDEO_DURATION_SECONDS_6",
        "VIDEO_DURATION_SECONDS_7",
        "VIDEO_DURATION_SECONDS_8",
        "VIDEO_DURATION_SECONDS_9",
        "VIDEO_DURATION_SECONDS_10",
        "VIDEO_DURATION_SECONDS_11",
        "VIDEO_DURATION_SECONDS_12",
        "VIDEO_DURATION_SECONDS_13",
        "VIDEO_DURATION_SECONDS_14",
        "VIDEO_DURATION_SECONDS_15",
        "VIDEO_DURATION_SECONDS_30",
        "VIDEO_DURATION_SECONDS_45",
        "VIDEO_DURATION_SECONDS_60",
    ]

class GoogleAudienceTargetingSetting(typing_extensions.TypedDict, total=False):
    googleAudienceId: str

class DeviceTypeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "DEVICE_TYPE_COMPUTER",
        "DEVICE_TYPE_CONNECTED_TV",
        "DEVICE_TYPE_SMART_PHONE",
        "DEVICE_TYPE_TABLET",
    ]

class ListNegativeKeywordsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    negativeKeywords: typing.List[NegativeKeyword]

class CustomListTargetingSetting(typing_extensions.TypedDict, total=False):
    customListId: str

class InsertionOrderBudgetSegment(typing_extensions.TypedDict, total=False):
    description: str
    budgetAmountMicros: str
    campaignBudgetId: str
    dateRange: DateRange

class AssignedInventorySource(typing_extensions.TypedDict, total=False):
    assignedInventorySourceId: str
    name: str
    inventorySourceId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class DayAndTimeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
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
    startHour: int
    timeZoneResolution: typing_extensions.Literal[
        "TIME_ZONE_RESOLUTION_UNSPECIFIED",
        "TIME_ZONE_RESOLUTION_END_USER",
        "TIME_ZONE_RESOLUTION_ADVERTISER",
    ]
    endHour: int

class Asset(typing_extensions.TypedDict, total=False):
    content: str
    mediaId: str

class BulkEditLineItemAssignedTargetingOptionsRequest(
    typing_extensions.TypedDict, total=False
):
    createRequests: typing.List[CreateAssignedTargetingOptionsRequest]
    deleteRequests: typing.List[DeleteAssignedTargetingOptionsRequest]

class FirstAndThirdPartyAudienceGroup(typing_extensions.TypedDict, total=False):
    settings: typing.List[FirstAndThirdPartyAudienceTargetingSetting]

class OnScreenPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    onScreenPosition: typing_extensions.Literal[
        "ON_SCREEN_POSITION_UNSPECIFIED",
        "ON_SCREEN_POSITION_UNKNOWN",
        "ON_SCREEN_POSITION_ABOVE_THE_FOLD",
        "ON_SCREEN_POSITION_BELOW_THE_FOLD",
    ]
    targetingOptionId: str

class ListChannelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    channels: typing.List[Channel]

class OperatingSystemTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class SensitiveCategoryAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    sensitiveCategory: typing_extensions.Literal[
        "SENSITIVE_CATEGORY_UNSPECIFIED",
        "SENSITIVE_CATEGORY_ADULT",
        "SENSITIVE_CATEGORY_DEROGATORY",
        "SENSITIVE_CATEGORY_DOWNLOADS_SHARING",
        "SENSITIVE_CATEGORY_WEAPONS",
        "SENSITIVE_CATEGORY_GAMBLING",
        "SENSITIVE_CATEGORY_VIOLENCE",
        "SENSITIVE_CATEGORY_SUGGESTIVE",
        "SENSITIVE_CATEGORY_PROFANITY",
        "SENSITIVE_CATEGORY_ALCOHOL",
        "SENSITIVE_CATEGORY_DRUGS",
        "SENSITIVE_CATEGORY_TOBACCO",
        "SENSITIVE_CATEGORY_POLITICS",
        "SENSITIVE_CATEGORY_RELIGION",
        "SENSITIVE_CATEGORY_TRAGEDY",
        "SENSITIVE_CATEGORY_TRANSPORTATION_ACCIDENTS",
        "SENSITIVE_CATEGORY_SENSITIVE_SOCIAL_ISSUES",
        "SENSITIVE_CATEGORY_SHOCKING",
    ]
    excludedTargetingOptionId: str

class DeleteAssignedTargetingOptionsRequest(typing_extensions.TypedDict, total=False):
    assignedTargetingOptionIds: typing.List[str]
    targetingType: typing_extensions.Literal[
        "TARGETING_TYPE_UNSPECIFIED",
        "TARGETING_TYPE_CHANNEL",
        "TARGETING_TYPE_APP_CATEGORY",
        "TARGETING_TYPE_APP",
        "TARGETING_TYPE_URL",
        "TARGETING_TYPE_DAY_AND_TIME",
        "TARGETING_TYPE_AGE_RANGE",
        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
        "TARGETING_TYPE_GENDER",
        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
        "TARGETING_TYPE_USER_REWARDED_CONTENT",
        "TARGETING_TYPE_PARENTAL_STATUS",
        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
        "TARGETING_TYPE_DEVICE_TYPE",
        "TARGETING_TYPE_AUDIENCE_GROUP",
        "TARGETING_TYPE_BROWSER",
        "TARGETING_TYPE_HOUSEHOLD_INCOME",
        "TARGETING_TYPE_ON_SCREEN_POSITION",
        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
        "TARGETING_TYPE_ENVIRONMENT",
        "TARGETING_TYPE_CARRIER_AND_ISP",
        "TARGETING_TYPE_OPERATING_SYSTEM",
        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
        "TARGETING_TYPE_KEYWORD",
        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
        "TARGETING_TYPE_VIEWABILITY",
        "TARGETING_TYPE_CATEGORY",
        "TARGETING_TYPE_INVENTORY_SOURCE",
        "TARGETING_TYPE_LANGUAGE",
        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
        "TARGETING_TYPE_GEO_REGION",
        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
        "TARGETING_TYPE_EXCHANGE",
        "TARGETING_TYPE_SUB_EXCHANGE",
    ]

class ListPartnerAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    assignedTargetingOptions: typing.List[AssignedTargetingOption]

class GoogleBytestreamMedia(typing_extensions.TypedDict, total=False):
    resourceName: str

class Transcode(typing_extensions.TypedDict, total=False):
    mimeType: str
    audioSampleRateHz: str
    fileSizeBytes: str
    transcoded: bool
    bitRateKbps: str
    audioBitRateKbps: str
    name: str
    frameRate: float
    dimensions: Dimensions

class CategoryTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class FirstAndThirdPartyAudience(typing_extensions.TypedDict, total=False):
    displayName: str
    displayDesktopAudienceSize: str
    description: str
    displayMobileWebAudienceSize: str
    membershipDurationDays: str
    activeDisplayAudienceSize: str
    displayAudienceSize: str
    name: str
    audienceType: typing_extensions.Literal[
        "AUDIENCE_TYPE_UNSPECIFIED",
        "CUSTOMER_MATCH_CONTACT_INFO",
        "CUSTOMER_MATCH_DEVICE_ID",
        "CUSTOMER_MATCH_USER_ID",
        "ACTIVITY_BASED",
        "FREQUENCY_CAP",
        "TAG_BASED",
        "YOUTUBE_USERS",
        "LICENSED",
    ]
    displayMobileAppAudienceSize: str
    youtubeAudienceSize: str
    audienceSource: typing_extensions.Literal[
        "AUDIENCE_SOURCE_UNSPECIFIED",
        "DISPLAY_VIDEO_360",
        "CAMPAIGN_MANAGER",
        "AD_MANAGER",
        "SEARCH_ADS_360",
        "YOUTUBE",
        "ADS_DATA_HUB",
    ]
    firstAndThirdPartyAudienceType: typing_extensions.Literal[
        "FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_UNSPECIFIED",
        "FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_FIRST_PARTY",
        "FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_THIRD_PARTY",
    ]
    firstAndThirdPartyAudienceId: str
    gmailAudienceSize: str

class IntegrationDetails(typing_extensions.TypedDict, total=False):
    integrationCode: str
    details: str

class CombinedAudienceGroup(typing_extensions.TypedDict, total=False):
    settings: typing.List[CombinedAudienceTargetingSetting]

class GeoRegionTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    geoRegionType: typing_extensions.Literal[
        "GEO_REGION_TYPE_UNKNOWN",
        "GEO_REGION_TYPE_OTHER",
        "GEO_REGION_TYPE_COUNTRY",
        "GEO_REGION_TYPE_REGION",
        "GEO_REGION_TYPE_TERRITORY",
        "GEO_REGION_TYPE_PROVINCE",
        "GEO_REGION_TYPE_STATE",
        "GEO_REGION_TYPE_PREFECTURE",
        "GEO_REGION_TYPE_GOVERNORATE",
        "GEO_REGION_TYPE_CANTON",
        "GEO_REGION_TYPE_UNION_TERRITORY",
        "GEO_REGION_TYPE_AUTONOMOUS_COMMUNITY",
        "GEO_REGION_TYPE_DMA_REGION",
        "GEO_REGION_TYPE_METRO",
        "GEO_REGION_TYPE_CONGRESSIONAL_DISTRICT",
        "GEO_REGION_TYPE_COUNTY",
        "GEO_REGION_TYPE_MUNICIPALITY",
        "GEO_REGION_TYPE_CITY",
        "GEO_REGION_TYPE_POSTAL_CODE",
        "GEO_REGION_TYPE_DEPARTMENT",
        "GEO_REGION_TYPE_AIRPORT",
        "GEO_REGION_TYPE_TV_REGION",
        "GEO_REGION_TYPE_OKRUG",
        "GEO_REGION_TYPE_BOROUGH",
        "GEO_REGION_TYPE_CITY_REGION",
        "GEO_REGION_TYPE_ARRONDISSEMENT",
        "GEO_REGION_TYPE_NEIGHBORHOOD",
        "GEO_REGION_TYPE_UNIVERSITY",
        "GEO_REGION_TYPE_DISTRICT",
    ]
    displayName: str

class LanguageAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    negative: bool
    targetingOptionId: str
    displayName: str

class ViewabilityTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    viewability: typing_extensions.Literal[
        "VIEWABILITY_UNSPECIFIED",
        "VIEWABILITY_10_PERCENT_OR_MORE",
        "VIEWABILITY_20_PERCENT_OR_MORE",
        "VIEWABILITY_30_PERCENT_OR_MORE",
        "VIEWABILITY_40_PERCENT_OR_MORE",
        "VIEWABILITY_50_PERCENT_OR_MORE",
        "VIEWABILITY_60_PERCENT_OR_MORE",
        "VIEWABILITY_70_PERCENT_OR_MORE",
        "VIEWABILITY_80_PERCENT_OR_MORE",
        "VIEWABILITY_90_PERCENT_OR_MORE",
    ]

class InventorySourceDisplayCreativeConfig(typing_extensions.TypedDict, total=False):
    creativeSize: Dimensions

class CounterEvent(typing_extensions.TypedDict, total=False):
    reportingName: str
    name: str

class GeoRegionAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    negative: bool
    displayName: str
    targetingOptionId: str
    geoRegionType: typing_extensions.Literal[
        "GEO_REGION_TYPE_UNKNOWN",
        "GEO_REGION_TYPE_OTHER",
        "GEO_REGION_TYPE_COUNTRY",
        "GEO_REGION_TYPE_REGION",
        "GEO_REGION_TYPE_TERRITORY",
        "GEO_REGION_TYPE_PROVINCE",
        "GEO_REGION_TYPE_STATE",
        "GEO_REGION_TYPE_PREFECTURE",
        "GEO_REGION_TYPE_GOVERNORATE",
        "GEO_REGION_TYPE_CANTON",
        "GEO_REGION_TYPE_UNION_TERRITORY",
        "GEO_REGION_TYPE_AUTONOMOUS_COMMUNITY",
        "GEO_REGION_TYPE_DMA_REGION",
        "GEO_REGION_TYPE_METRO",
        "GEO_REGION_TYPE_CONGRESSIONAL_DISTRICT",
        "GEO_REGION_TYPE_COUNTY",
        "GEO_REGION_TYPE_MUNICIPALITY",
        "GEO_REGION_TYPE_CITY",
        "GEO_REGION_TYPE_POSTAL_CODE",
        "GEO_REGION_TYPE_DEPARTMENT",
        "GEO_REGION_TYPE_AIRPORT",
        "GEO_REGION_TYPE_TV_REGION",
        "GEO_REGION_TYPE_OKRUG",
        "GEO_REGION_TYPE_BOROUGH",
        "GEO_REGION_TYPE_CITY_REGION",
        "GEO_REGION_TYPE_ARRONDISSEMENT",
        "GEO_REGION_TYPE_NEIGHBORHOOD",
        "GEO_REGION_TYPE_UNIVERSITY",
        "GEO_REGION_TYPE_DISTRICT",
    ]

class CarrierAndIspTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "CARRIER_AND_ISP_TYPE_UNSPECIFIED",
        "CARRIER_AND_ISP_TYPE_ISP",
        "CARRIER_AND_ISP_TYPE_CARRIER",
    ]
    displayName: str

class Creative(typing_extensions.TypedDict, total=False):
    vpaid: bool
    progressOffset: AudioVideoOffset
    lineItemIds: typing.List[str]
    cmPlacementId: str
    assets: typing.List[AssetAssociation]
    creativeType: typing_extensions.Literal[
        "CREATIVE_TYPE_UNSPECIFIED",
        "CREATIVE_TYPE_STANDARD",
        "CREATIVE_TYPE_EXPANDABLE",
        "CREATIVE_TYPE_VIDEO",
        "CREATIVE_TYPE_NATIVE",
        "CREATIVE_TYPE_TEMPLATED_APP_INSTALL",
        "CREATIVE_TYPE_NATIVE_SITE_SQUARE",
        "CREATIVE_TYPE_TEMPLATED_APP_INSTALL_INTERSTITIAL",
        "CREATIVE_TYPE_LIGHTBOX",
        "CREATIVE_TYPE_NATIVE_APP_INSTALL",
        "CREATIVE_TYPE_NATIVE_APP_INSTALL_SQUARE",
        "CREATIVE_TYPE_AUDIO",
        "CREATIVE_TYPE_PUBLISHER_HOSTED",
        "CREATIVE_TYPE_NATIVE_VIDEO",
        "CREATIVE_TYPE_TEMPLATED_APP_INSTALL_VIDEO",
    ]
    html5Video: bool
    integrationCode: str
    appendedTag: str
    timerEvents: typing.List[TimerEvent]
    skippable: bool
    expandingDirection: typing_extensions.Literal[
        "EXPANDING_DIRECTION_UNSPECIFIED",
        "EXPANDING_DIRECTION_NONE",
        "EXPANDING_DIRECTION_UP",
        "EXPANDING_DIRECTION_DOWN",
        "EXPANDING_DIRECTION_LEFT",
        "EXPANDING_DIRECTION_RIGHT",
        "EXPANDING_DIRECTION_UP_AND_LEFT",
        "EXPANDING_DIRECTION_UP_AND_RIGHT",
        "EXPANDING_DIRECTION_DOWN_AND_LEFT",
        "EXPANDING_DIRECTION_DOWN_AND_RIGHT",
        "EXPANDING_DIRECTION_UP_OR_DOWN",
        "EXPANDING_DIRECTION_LEFT_OR_RIGHT",
        "EXPANDING_DIRECTION_ANY_DIAGONAL",
    ]
    requireMraid: bool
    companionCreativeIds: typing.List[str]
    counterEvents: typing.List[CounterEvent]
    dynamic: bool
    iasCampaignMonitoring: bool
    creativeAttributes: typing.List[str]
    expandOnHover: bool
    thirdPartyTag: str
    transcodes: typing.List[Transcode]
    trackerUrls: typing.List[str]
    creativeId: str
    jsTrackerUrl: str
    name: str
    advertiserId: str
    cmTrackingAd: CmTrackingAd
    skipOffset: AudioVideoOffset
    exitEvents: typing.List[ExitEvent]
    obaIcon: ObaIcon
    requirePingForAttribution: bool
    additionalDimensions: typing.List[Dimensions]
    notes: str
    mediaDuration: str
    hostingSource: typing_extensions.Literal[
        "HOSTING_SOURCE_UNSPECIFIED",
        "HOSTING_SOURCE_CM",
        "HOSTING_SOURCE_THIRD_PARTY",
        "HOSTING_SOURCE_HOSTED",
        "HOSTING_SOURCE_RICH_MEDIA",
    ]
    universalAdId: UniversalAdId
    vastTagUrl: str
    displayName: str
    thirdPartyUrls: typing.List[ThirdPartyUrl]
    createTime: str
    requireHtml5: bool
    reviewStatus: ReviewStatusInfo
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    dimensions: Dimensions
    updateTime: str

class DateRange(typing_extensions.TypedDict, total=False):
    startDate: Date
    endDate: Date

class ListAssignedInventorySourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    assignedInventorySources: typing.List[AssignedInventorySource]

class TrackingFloodlightActivityConfig(typing_extensions.TypedDict, total=False):
    postViewLookbackWindowDays: int
    postClickLookbackWindowDays: int
    floodlightActivityId: str

class ListCustomListsResponse(typing_extensions.TypedDict, total=False):
    customLists: typing.List[CustomList]
    nextPageToken: str

class MeasurementConfig(typing_extensions.TypedDict, total=False):
    dv360ToCmDataSharingEnabled: bool
    dv360ToCmCostReportingEnabled: bool

class ExchangeAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    targetingOptionId: str

class VideoPlayerSizeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    videoPlayerSize: typing_extensions.Literal[
        "VIDEO_PLAYER_SIZE_UNSPECIFIED",
        "VIDEO_PLAYER_SIZE_SMALL",
        "VIDEO_PLAYER_SIZE_LARGE",
        "VIDEO_PLAYER_SIZE_HD",
        "VIDEO_PLAYER_SIZE_UNKNOWN",
    ]

class HouseholdIncomeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    householdIncome: typing_extensions.Literal[
        "HOUSEHOLD_INCOME_UNSPECIFIED",
        "HOUSEHOLD_INCOME_UNKNOWN",
        "HOUSEHOLD_INCOME_LOWER_50_PERCENT",
        "HOUSEHOLD_INCOME_TOP_41_TO_50_PERCENT",
        "HOUSEHOLD_INCOME_TOP_31_TO_40_PERCENT",
        "HOUSEHOLD_INCOME_TOP_21_TO_30_PERCENT",
        "HOUSEHOLD_INCOME_TOP_11_TO_20_PERCENT",
        "HOUSEHOLD_INCOME_TOP_10_PERCENT",
    ]

class AppCategoryTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class User(typing_extensions.TypedDict, total=False):
    userId: str
    displayName: str
    name: str
    assignedUserRoles: typing.List[AssignedUserRole]
    email: str

class AssignedTargetingOption(typing_extensions.TypedDict, total=False):
    thirdPartyVerifierDetails: ThirdPartyVerifierAssignedTargetingOptionDetails
    negativeKeywordListDetails: NegativeKeywordListAssignedTargetingOptionDetails
    name: str
    keywordDetails: KeywordAssignedTargetingOptionDetails
    browserDetails: BrowserAssignedTargetingOptionDetails
    appCategoryDetails: AppCategoryAssignedTargetingOptionDetails
    deviceTypeDetails: DeviceTypeAssignedTargetingOptionDetails
    viewabilityDetails: ViewabilityAssignedTargetingOptionDetails
    ageRangeDetails: AgeRangeAssignedTargetingOptionDetails
    inventorySourceGroupDetails: InventorySourceGroupAssignedTargetingOptionDetails
    authorizedSellerStatusDetails: AuthorizedSellerStatusAssignedTargetingOptionDetails
    proximityLocationListDetails: ProximityLocationListAssignedTargetingOptionDetails
    assignedTargetingOptionId: str
    dayAndTimeDetails: DayAndTimeAssignedTargetingOptionDetails
    regionalLocationListDetails: RegionalLocationListAssignedTargetingOptionDetails
    householdIncomeDetails: HouseholdIncomeAssignedTargetingOptionDetails
    urlDetails: UrlAssignedTargetingOptionDetails
    deviceMakeModelDetails: DeviceMakeModelAssignedTargetingOptionDetails
    genderDetails: GenderAssignedTargetingOptionDetails
    operatingSystemDetails: OperatingSystemAssignedTargetingOptionDetails
    categoryDetails: CategoryAssignedTargetingOptionDetails
    inheritance: typing_extensions.Literal[
        "INHERITANCE_UNSPECIFIED",
        "NOT_INHERITED",
        "INHERITED_FROM_PARTNER",
        "INHERITED_FROM_ADVERTISER",
    ]
    parentalStatusDetails: ParentalStatusAssignedTargetingOptionDetails
    videoPlayerSizeDetails: VideoPlayerSizeAssignedTargetingOptionDetails
    languageDetails: LanguageAssignedTargetingOptionDetails
    userRewardedContentDetails: UserRewardedContentAssignedTargetingOptionDetails
    inventorySourceDetails: InventorySourceAssignedTargetingOptionDetails
    contentInstreamPositionDetails: ContentInstreamPositionAssignedTargetingOptionDetails
    contentOutstreamPositionDetails: ContentOutstreamPositionAssignedTargetingOptionDetails
    appDetails: AppAssignedTargetingOptionDetails
    targetingType: typing_extensions.Literal[
        "TARGETING_TYPE_UNSPECIFIED",
        "TARGETING_TYPE_CHANNEL",
        "TARGETING_TYPE_APP_CATEGORY",
        "TARGETING_TYPE_APP",
        "TARGETING_TYPE_URL",
        "TARGETING_TYPE_DAY_AND_TIME",
        "TARGETING_TYPE_AGE_RANGE",
        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
        "TARGETING_TYPE_GENDER",
        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
        "TARGETING_TYPE_USER_REWARDED_CONTENT",
        "TARGETING_TYPE_PARENTAL_STATUS",
        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
        "TARGETING_TYPE_DEVICE_TYPE",
        "TARGETING_TYPE_AUDIENCE_GROUP",
        "TARGETING_TYPE_BROWSER",
        "TARGETING_TYPE_HOUSEHOLD_INCOME",
        "TARGETING_TYPE_ON_SCREEN_POSITION",
        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
        "TARGETING_TYPE_ENVIRONMENT",
        "TARGETING_TYPE_CARRIER_AND_ISP",
        "TARGETING_TYPE_OPERATING_SYSTEM",
        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
        "TARGETING_TYPE_KEYWORD",
        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
        "TARGETING_TYPE_VIEWABILITY",
        "TARGETING_TYPE_CATEGORY",
        "TARGETING_TYPE_INVENTORY_SOURCE",
        "TARGETING_TYPE_LANGUAGE",
        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
        "TARGETING_TYPE_GEO_REGION",
        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
        "TARGETING_TYPE_EXCHANGE",
        "TARGETING_TYPE_SUB_EXCHANGE",
    ]
    onScreenPositionDetails: OnScreenPositionAssignedTargetingOptionDetails
    exchangeDetails: ExchangeAssignedTargetingOptionDetails
    geoRegionDetails: GeoRegionAssignedTargetingOptionDetails
    channelDetails: ChannelAssignedTargetingOptionDetails
    sensitiveCategoryExclusionDetails: SensitiveCategoryAssignedTargetingOptionDetails
    subExchangeDetails: SubExchangeAssignedTargetingOptionDetails
    audienceGroupDetails: AudienceGroupAssignedTargetingOptionDetails
    carrierAndIspDetails: CarrierAndIspAssignedTargetingOptionDetails
    digitalContentLabelExclusionDetails: DigitalContentLabelAssignedTargetingOptionDetails
    environmentDetails: EnvironmentAssignedTargetingOptionDetails

class AuthorizedSellerStatusTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    authorizedSellerStatus: typing_extensions.Literal[
        "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS",
    ]

class TargetingOption(typing_extensions.TypedDict, total=False):
    appCategoryDetails: AppCategoryTargetingOptionDetails
    targetingOptionId: str
    carrierAndIspDetails: CarrierAndIspTargetingOptionDetails
    parentalStatusDetails: ParentalStatusTargetingOptionDetails
    genderDetails: GenderTargetingOptionDetails
    onScreenPositionDetails: OnScreenPositionTargetingOptionDetails
    householdIncomeDetails: HouseholdIncomeTargetingOptionDetails
    operatingSystemDetails: OperatingSystemTargetingOptionDetails
    categoryDetails: CategoryTargetingOptionDetails
    targetingType: typing_extensions.Literal[
        "TARGETING_TYPE_UNSPECIFIED",
        "TARGETING_TYPE_CHANNEL",
        "TARGETING_TYPE_APP_CATEGORY",
        "TARGETING_TYPE_APP",
        "TARGETING_TYPE_URL",
        "TARGETING_TYPE_DAY_AND_TIME",
        "TARGETING_TYPE_AGE_RANGE",
        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
        "TARGETING_TYPE_GENDER",
        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
        "TARGETING_TYPE_USER_REWARDED_CONTENT",
        "TARGETING_TYPE_PARENTAL_STATUS",
        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
        "TARGETING_TYPE_DEVICE_TYPE",
        "TARGETING_TYPE_AUDIENCE_GROUP",
        "TARGETING_TYPE_BROWSER",
        "TARGETING_TYPE_HOUSEHOLD_INCOME",
        "TARGETING_TYPE_ON_SCREEN_POSITION",
        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
        "TARGETING_TYPE_ENVIRONMENT",
        "TARGETING_TYPE_CARRIER_AND_ISP",
        "TARGETING_TYPE_OPERATING_SYSTEM",
        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
        "TARGETING_TYPE_KEYWORD",
        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
        "TARGETING_TYPE_VIEWABILITY",
        "TARGETING_TYPE_CATEGORY",
        "TARGETING_TYPE_INVENTORY_SOURCE",
        "TARGETING_TYPE_LANGUAGE",
        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
        "TARGETING_TYPE_GEO_REGION",
        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
        "TARGETING_TYPE_EXCHANGE",
        "TARGETING_TYPE_SUB_EXCHANGE",
    ]
    name: str
    languageDetails: LanguageTargetingOptionDetails
    browserDetails: BrowserTargetingOptionDetails
    deviceTypeDetails: DeviceTypeTargetingOptionDetails
    userRewardedContentDetails: UserRewardedContentTargetingOptionDetails
    contentOutstreamPositionDetails: ContentOutstreamPositionTargetingOptionDetails
    deviceMakeModelDetails: DeviceMakeModelTargetingOptionDetails
    sensitiveCategoryDetails: SensitiveCategoryTargetingOptionDetails
    subExchangeDetails: SubExchangeTargetingOptionDetails
    videoPlayerSizeDetails: VideoPlayerSizeTargetingOptionDetails
    viewabilityDetails: ViewabilityTargetingOptionDetails
    authorizedSellerStatusDetails: AuthorizedSellerStatusTargetingOptionDetails
    ageRangeDetails: AgeRangeTargetingOptionDetails
    environmentDetails: EnvironmentTargetingOptionDetails
    exchangeDetails: ExchangeTargetingOptionDetails
    digitalContentLabelDetails: DigitalContentLabelTargetingOptionDetails
    contentInstreamPositionDetails: ContentInstreamPositionTargetingOptionDetails
    geoRegionDetails: GeoRegionTargetingOptionDetails

class ListUsersResponse(typing_extensions.TypedDict, total=False):
    users: typing.List[User]
    nextPageToken: str

class PartnerGeneralConfig(typing_extensions.TypedDict, total=False):
    timeZone: str
    currencyCode: str

class HouseholdIncomeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    householdIncome: typing_extensions.Literal[
        "HOUSEHOLD_INCOME_UNSPECIFIED",
        "HOUSEHOLD_INCOME_UNKNOWN",
        "HOUSEHOLD_INCOME_LOWER_50_PERCENT",
        "HOUSEHOLD_INCOME_TOP_41_TO_50_PERCENT",
        "HOUSEHOLD_INCOME_TOP_31_TO_40_PERCENT",
        "HOUSEHOLD_INCOME_TOP_21_TO_30_PERCENT",
        "HOUSEHOLD_INCOME_TOP_11_TO_20_PERCENT",
        "HOUSEHOLD_INCOME_TOP_10_PERCENT",
    ]

class CreateAssignedTargetingOptionsRequest(typing_extensions.TypedDict, total=False):
    assignedTargetingOptions: typing.List[AssignedTargetingOption]
    targetingType: typing_extensions.Literal[
        "TARGETING_TYPE_UNSPECIFIED",
        "TARGETING_TYPE_CHANNEL",
        "TARGETING_TYPE_APP_CATEGORY",
        "TARGETING_TYPE_APP",
        "TARGETING_TYPE_URL",
        "TARGETING_TYPE_DAY_AND_TIME",
        "TARGETING_TYPE_AGE_RANGE",
        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
        "TARGETING_TYPE_GENDER",
        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
        "TARGETING_TYPE_USER_REWARDED_CONTENT",
        "TARGETING_TYPE_PARENTAL_STATUS",
        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
        "TARGETING_TYPE_DEVICE_TYPE",
        "TARGETING_TYPE_AUDIENCE_GROUP",
        "TARGETING_TYPE_BROWSER",
        "TARGETING_TYPE_HOUSEHOLD_INCOME",
        "TARGETING_TYPE_ON_SCREEN_POSITION",
        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
        "TARGETING_TYPE_ENVIRONMENT",
        "TARGETING_TYPE_CARRIER_AND_ISP",
        "TARGETING_TYPE_OPERATING_SYSTEM",
        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
        "TARGETING_TYPE_KEYWORD",
        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
        "TARGETING_TYPE_VIEWABILITY",
        "TARGETING_TYPE_CATEGORY",
        "TARGETING_TYPE_INVENTORY_SOURCE",
        "TARGETING_TYPE_LANGUAGE",
        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
        "TARGETING_TYPE_GEO_REGION",
        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
        "TARGETING_TYPE_EXCHANGE",
        "TARGETING_TYPE_SUB_EXCHANGE",
    ]

class InventorySourceGroup(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    inventorySourceGroupId: str

class FloodlightGroup(typing_extensions.TypedDict, total=False):
    floodlightGroupId: str
    name: str
    lookbackWindow: LookbackWindow
    displayName: str
    activeViewConfig: ActiveViewVideoViewabilityMetricConfig
    customVariables: typing.Dict[str, typing.Any]
    webTagType: typing_extensions.Literal[
        "WEB_TAG_TYPE_UNSPECIFIED",
        "WEB_TAG_TYPE_NONE",
        "WEB_TAG_TYPE_IMAGE",
        "WEB_TAG_TYPE_DYNAMIC",
    ]

class SensitiveCategoryTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    sensitiveCategory: typing_extensions.Literal[
        "SENSITIVE_CATEGORY_UNSPECIFIED",
        "SENSITIVE_CATEGORY_ADULT",
        "SENSITIVE_CATEGORY_DEROGATORY",
        "SENSITIVE_CATEGORY_DOWNLOADS_SHARING",
        "SENSITIVE_CATEGORY_WEAPONS",
        "SENSITIVE_CATEGORY_GAMBLING",
        "SENSITIVE_CATEGORY_VIOLENCE",
        "SENSITIVE_CATEGORY_SUGGESTIVE",
        "SENSITIVE_CATEGORY_PROFANITY",
        "SENSITIVE_CATEGORY_ALCOHOL",
        "SENSITIVE_CATEGORY_DRUGS",
        "SENSITIVE_CATEGORY_TOBACCO",
        "SENSITIVE_CATEGORY_POLITICS",
        "SENSITIVE_CATEGORY_RELIGION",
        "SENSITIVE_CATEGORY_TRAGEDY",
        "SENSITIVE_CATEGORY_TRANSPORTATION_ACCIDENTS",
        "SENSITIVE_CATEGORY_SENSITIVE_SOCIAL_ISSUES",
        "SENSITIVE_CATEGORY_SHOCKING",
    ]

class GoogleAudience(typing_extensions.TypedDict, total=False):
    googleAudienceType: typing_extensions.Literal[
        "GOOGLE_AUDIENCE_TYPE_UNSPECIFIED",
        "GOOGLE_AUDIENCE_TYPE_AFFINITY",
        "GOOGLE_AUDIENCE_TYPE_IN_MARKET",
        "GOOGLE_AUDIENCE_TYPE_INSTALLED_APPS",
        "GOOGLE_AUDIENCE_TYPE_NEW_MOBILE_DEVICES",
    ]
    displayName: str
    googleAudienceId: str
    name: str

class ReviewStatusInfo(typing_extensions.TypedDict, total=False):
    approvalStatus: typing_extensions.Literal[
        "APPROVAL_STATUS_UNSPECIFIED",
        "APPROVAL_STATUS_PENDING_NOT_SERVABLE",
        "APPROVAL_STATUS_PENDING_SERVABLE",
        "APPROVAL_STATUS_APPROVED_SERVABLE",
        "APPROVAL_STATUS_REJECTED_NOT_SERVABLE",
    ]
    creativeAndLandingPageReviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    publisherReviewStatuses: typing.List[PublisherReviewStatus]
    contentAndPolicyReviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    exchangeReviewStatuses: typing.List[ExchangeReviewStatus]

class ExchangeReviewStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    exchange: typing_extensions.Literal[
        "EXCHANGE_UNSPECIFIED",
        "EXCHANGE_GOOGLE_AD_MANAGER",
        "EXCHANGE_APPNEXUS",
        "EXCHANGE_BRIGHTROLL",
        "EXCHANGE_ADFORM",
        "EXCHANGE_ADMETA",
        "EXCHANGE_ADMIXER",
        "EXCHANGE_ADSMOGO",
        "EXCHANGE_ADSWIZZ",
        "EXCHANGE_BIDSWITCH",
        "EXCHANGE_BRIGHTROLL_DISPLAY",
        "EXCHANGE_CADREON",
        "EXCHANGE_DAILYMOTION",
        "EXCHANGE_FIVE",
        "EXCHANGE_FLUCT",
        "EXCHANGE_FREEWHEEL",
        "EXCHANGE_GENIEE",
        "EXCHANGE_GUMGUM",
        "EXCHANGE_IMOBILE",
        "EXCHANGE_IBILLBOARD",
        "EXCHANGE_IMPROVE_DIGITAL",
        "EXCHANGE_INDEX",
        "EXCHANGE_KARGO",
        "EXCHANGE_MICROAD",
        "EXCHANGE_MOPUB",
        "EXCHANGE_NEND",
        "EXCHANGE_ONE_BY_AOL_DISPLAY",
        "EXCHANGE_ONE_BY_AOL_MOBILE",
        "EXCHANGE_ONE_BY_AOL_VIDEO",
        "EXCHANGE_OOYALA",
        "EXCHANGE_OPENX",
        "EXCHANGE_PERMODO",
        "EXCHANGE_PLATFORMONE",
        "EXCHANGE_PLATFORMID",
        "EXCHANGE_PUBMATIC",
        "EXCHANGE_PULSEPOINT",
        "EXCHANGE_REVENUEMAX",
        "EXCHANGE_RUBICON",
        "EXCHANGE_SMARTCLIP",
        "EXCHANGE_SMARTRTB",
        "EXCHANGE_SMARTSTREAMTV",
        "EXCHANGE_SOVRN",
        "EXCHANGE_SPOTXCHANGE",
        "EXCHANGE_STROER",
        "EXCHANGE_TEADSTV",
        "EXCHANGE_TELARIA",
        "EXCHANGE_TVN",
        "EXCHANGE_UNITED",
        "EXCHANGE_YIELDLAB",
        "EXCHANGE_YIELDMO",
        "EXCHANGE_UNRULYX",
        "EXCHANGE_OPEN8",
        "EXCHANGE_TRITON",
        "EXCHANGE_TRIPLELIFT",
        "EXCHANGE_TABOOLA",
        "EXCHANGE_INMOBI",
        "EXCHANGE_SMAATO",
        "EXCHANGE_AJA",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
    ]

class SdfDownloadTaskMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    version: typing_extensions.Literal[
        "SDF_VERSION_UNSPECIFIED",
        "SDF_VERSION_3_1",
        "SDF_VERSION_4",
        "SDF_VERSION_4_1",
        "SDF_VERSION_4_2",
        "SDF_VERSION_5",
        "SDF_VERSION_5_1",
        "SDF_VERSION_5_2",
    ]
    createTime: str

class LookbackWindow(typing_extensions.TypedDict, total=False):
    impressionDays: int
    clickDays: int

class ExitEvent(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "EXIT_EVENT_TYPE_UNSPECIFIED",
        "EXIT_EVENT_TYPE_DEFAULT",
        "EXIT_EVENT_TYPE_BACKUP",
    ]
    reportingName: str
    url: str
    name: str

class ListNegativeKeywordListsResponse(typing_extensions.TypedDict, total=False):
    negativeKeywordLists: typing.List[NegativeKeywordList]
    nextPageToken: str

class TimeRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class CreateAssetResponse(typing_extensions.TypedDict, total=False):
    asset: Asset

class DoubleVerifyDisplayViewability(typing_extensions.TypedDict, total=False):
    viewableDuring: typing_extensions.Literal[
        "AVERAGE_VIEW_DURATION_UNSPECIFIED",
        "AVERAGE_VIEW_DURATION_5_SEC",
        "AVERAGE_VIEW_DURATION_10_SEC",
        "AVERAGE_VIEW_DURATION_15_SEC",
    ]
    iab: typing_extensions.Literal[
        "IAB_VIEWED_RATE_UNSPECIFIED",
        "IAB_VIEWED_RATE_80_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_75_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_70_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_65_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_60_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_55_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_50_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_40_PERCENT_HIGHER",
        "IAB_VIEWED_RATE_30_PERCENT_HIGHER",
    ]

class CustomList(typing_extensions.TypedDict, total=False):
    displayName: str
    customListId: str
    name: str

class Advertiser(typing_extensions.TypedDict, total=False):
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    name: str
    integrationDetails: IntegrationDetails
    servingConfig: AdvertiserTargetingConfig
    generalConfig: AdvertiserGeneralConfig
    adServerConfig: AdvertiserAdServerConfig
    dataAccessConfig: AdvertiserDataAccessConfig
    displayName: str
    creativeConfig: AdvertiserCreativeConfig
    updateTime: str
    partnerId: str
    advertiserId: str

class DoubleVerifyBrandSafetyCategories(typing_extensions.TypedDict, total=False):
    avoidUnknownBrandSafetyCategory: bool
    avoidedMediumSeverityCategories: typing.List[str]
    avoidedHighSeverityCategories: typing.List[str]

class SdfDownloadTask(typing_extensions.TypedDict, total=False):
    resourceName: str

class AppCategoryAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    negative: bool
    displayName: str

class PerformanceGoalBidStrategy(typing_extensions.TypedDict, total=False):
    performanceGoalType: typing_extensions.Literal[
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_UNSPECIFIED",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPA",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CPC",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_VIEWABLE_CPM",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CUSTOM_ALGO",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_CIVA",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_IVO_TEN",
        "BIDDING_STRATEGY_PERFORMANCE_GOAL_TYPE_AV_VIEWED",
    ]
    maxAverageCpmBidAmountMicros: str
    performanceGoalAmountMicros: str
    customBiddingAlgorithmId: str

class BulkEditAdvertiserAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    createdAssignedTargetingOptions: typing.List[AssignedTargetingOption]

class ObaIcon(typing_extensions.TypedDict, total=False):
    position: typing_extensions.Literal[
        "OBA_ICON_POSITION_UNSPECIFIED",
        "OBA_ICON_POSITION_UPPER_RIGHT",
        "OBA_ICON_POSITION_UPPER_LEFT",
        "OBA_ICON_POSITION_LOWER_RIGHT",
        "OBA_ICON_POSITION_LOWER_LEFT",
    ]
    clickTrackingUrl: str
    resourceMimeType: str
    resourceUrl: str
    viewTrackingUrl: str
    dimensions: Dimensions
    landingPageUrl: str
    program: str

class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

class DigitalContentLabelTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentRatingTier: typing_extensions.Literal[
        "CONTENT_RATING_TIER_UNSPECIFIED",
        "CONTENT_RATING_TIER_UNRATED",
        "CONTENT_RATING_TIER_GENERAL",
        "CONTENT_RATING_TIER_PARENTAL_GUIDANCE",
        "CONTENT_RATING_TIER_TEENS",
        "CONTENT_RATING_TIER_MATURE",
    ]

class ContentInstreamPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    contentInstreamPosition: typing_extensions.Literal[
        "CONTENT_INSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_INSTREAM_POSITION_PRE_ROLL",
        "CONTENT_INSTREAM_POSITION_MID_ROLL",
        "CONTENT_INSTREAM_POSITION_POST_ROLL",
    ]

class LanguageTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

class ListSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sites: typing.List[Site]

class LineItemFlight(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    flightDateType: typing_extensions.Literal[
        "LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED",
        "LINE_ITEM_FLIGHT_DATE_TYPE_INHERITED",
        "LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM",
    ]

class ListTargetingOptionsResponse(typing_extensions.TypedDict, total=False):
    targetingOptions: typing.List[TargetingOption]
    nextPageToken: str

class Pacing(typing_extensions.TypedDict, total=False):
    pacingPeriod: typing_extensions.Literal[
        "PACING_PERIOD_UNSPECIFIED", "PACING_PERIOD_DAILY", "PACING_PERIOD_FLIGHT"
    ]
    dailyMaxImpressions: str
    dailyMaxMicros: str
    pacingType: typing_extensions.Literal[
        "PACING_TYPE_UNSPECIFIED",
        "PACING_TYPE_AHEAD",
        "PACING_TYPE_ASAP",
        "PACING_TYPE_EVEN",
    ]

class Dimensions(typing_extensions.TypedDict, total=False):
    widthPixels: int
    heightPixels: int

class ListAdvertisersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    advertisers: typing.List[Advertiser]

class Channel(typing_extensions.TypedDict, total=False):
    channelId: str
    name: str
    partnerId: str
    advertiserId: str
    displayName: str

class ContentOutstreamPositionTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentOutstreamPosition: typing_extensions.Literal[
        "CONTENT_OUTSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_OUTSTREAM_POSITION_UNKNOWN",
        "CONTENT_OUTSTREAM_POSITION_IN_ARTICLE",
        "CONTENT_OUTSTREAM_POSITION_IN_BANNER",
        "CONTENT_OUTSTREAM_POSITION_IN_FEED",
        "CONTENT_OUTSTREAM_POSITION_INTERSTITIAL",
    ]

class ThirdPartyVerifierAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    integralAdScience: IntegralAdScience
    doubleVerify: DoubleVerify
    adloox: Adloox

class InsertionOrder(typing_extensions.TypedDict, total=False):
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    frequencyCap: FrequencyCap
    insertionOrderId: str
    advertiserId: str
    bidStrategy: BiddingStrategy
    displayName: str
    partnerCosts: typing.List[PartnerCost]
    name: str
    pacing: Pacing
    integrationDetails: IntegrationDetails
    budget: InsertionOrderBudget
    performanceGoal: PerformanceGoal
    campaignId: str
    updateTime: str

class DoubleVerifyAppStarRating(typing_extensions.TypedDict, total=False):
    avoidInsufficientStarRating: bool
    avoidedStarRating: typing_extensions.Literal[
        "APP_STAR_RATE_UNSPECIFIED",
        "APP_STAR_RATE_1_POINT_5_LESS",
        "APP_STAR_RATE_2_LESS",
        "APP_STAR_RATE_2_POINT_5_LESS",
        "APP_STAR_RATE_3_LESS",
        "APP_STAR_RATE_3_POINT_5_LESS",
        "APP_STAR_RATE_4_LESS",
        "APP_STAR_RATE_4_POINT_5_LESS",
    ]

class PartnerAdServerConfig(typing_extensions.TypedDict, total=False):
    measurementConfig: MeasurementConfig

class AppAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    appId: str
    negative: bool
    displayName: str

class EnvironmentAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    environment: typing_extensions.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_WEB_OPTIMIZED",
        "ENVIRONMENT_WEB_NOT_OPTIMIZED",
        "ENVIRONMENT_APP",
    ]

class CombinedAudience(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    combinedAudienceId: str

class AdvertiserGeneralConfig(typing_extensions.TypedDict, total=False):
    domainUrl: str
    timeZone: str
    currencyCode: str

class ExchangeConfig(typing_extensions.TypedDict, total=False):
    enabledExchanges: typing.List[ExchangeConfigEnabledExchange]

class CampaignGoal(typing_extensions.TypedDict, total=False):
    campaignGoalType: typing_extensions.Literal[
        "CAMPAIGN_GOAL_TYPE_UNSPECIFIED",
        "CAMPAIGN_GOAL_TYPE_APP_INSTALL",
        "CAMPAIGN_GOAL_TYPE_BRAND_AWARENESS",
        "CAMPAIGN_GOAL_TYPE_OFFLINE_ACTION",
        "CAMPAIGN_GOAL_TYPE_ONLINE_ACTION",
    ]
    performanceGoal: PerformanceGoal
