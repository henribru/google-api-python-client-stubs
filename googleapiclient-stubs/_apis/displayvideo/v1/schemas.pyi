import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActivateManualTriggerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ActiveViewVideoViewabilityMetricConfig(typing_extensions.TypedDict, total=False):
    displayName: str
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
    minimumQuartile: typing_extensions.Literal[
        "VIDEO_DURATION_QUARTILE_UNSPECIFIED",
        "VIDEO_DURATION_QUARTILE_NONE",
        "VIDEO_DURATION_QUARTILE_FIRST",
        "VIDEO_DURATION_QUARTILE_SECOND",
        "VIDEO_DURATION_QUARTILE_THIRD",
        "VIDEO_DURATION_QUARTILE_FOURTH",
    ]
    minimumViewability: typing_extensions.Literal[
        "VIEWABILITY_PERCENT_UNSPECIFIED",
        "VIEWABILITY_PERCENT_0",
        "VIEWABILITY_PERCENT_25",
        "VIEWABILITY_PERCENT_50",
        "VIEWABILITY_PERCENT_75",
        "VIEWABILITY_PERCENT_100",
    ]
    minimumVolume: typing_extensions.Literal[
        "VIDEO_VOLUME_PERCENT_UNSPECIFIED",
        "VIDEO_VOLUME_PERCENT_0",
        "VIDEO_VOLUME_PERCENT_10",
    ]

@typing.type_check_only
class Adloox(typing_extensions.TypedDict, total=False):
    excludedAdlooxCategories: _list[str]

@typing.type_check_only
class Advertiser(typing_extensions.TypedDict, total=False):
    adServerConfig: AdvertiserAdServerConfig
    advertiserId: str
    creativeConfig: AdvertiserCreativeConfig
    dataAccessConfig: AdvertiserDataAccessConfig
    displayName: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    generalConfig: AdvertiserGeneralConfig
    integrationDetails: IntegrationDetails
    name: str
    partnerId: str
    prismaEnabled: bool
    servingConfig: AdvertiserTargetingConfig
    updateTime: str

@typing.type_check_only
class AdvertiserAdServerConfig(typing_extensions.TypedDict, total=False):
    cmHybridConfig: CmHybridConfig
    thirdPartyOnlyConfig: ThirdPartyOnlyConfig

@typing.type_check_only
class AdvertiserCreativeConfig(typing_extensions.TypedDict, total=False):
    dynamicCreativeEnabled: bool
    iasClientId: str
    obaComplianceDisabled: bool
    videoCreativeDataSharingAuthorized: bool

@typing.type_check_only
class AdvertiserDataAccessConfig(typing_extensions.TypedDict, total=False):
    sdfConfig: AdvertiserSdfConfig

@typing.type_check_only
class AdvertiserGeneralConfig(typing_extensions.TypedDict, total=False):
    currencyCode: str
    domainUrl: str
    timeZone: str

@typing.type_check_only
class AdvertiserSdfConfig(typing_extensions.TypedDict, total=False):
    overridePartnerSdfConfig: bool
    sdfConfig: SdfConfig

@typing.type_check_only
class AdvertiserTargetingConfig(typing_extensions.TypedDict, total=False):
    exemptTvFromViewabilityTargeting: bool

@typing.type_check_only
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

@typing.type_check_only
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

@typing.type_check_only
class AppAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    appId: str
    appPlatform: typing_extensions.Literal[
        "APP_PLATFORM_UNSPECIFIED",
        "APP_PLATFORM_IOS",
        "APP_PLATFORM_ANDROID",
        "APP_PLATFORM_ROKU",
        "APP_PLATFORM_AMAZON_FIRETV",
        "APP_PLATFORM_PLAYSTATION",
        "APP_PLATFORM_APPLE_TV",
        "APP_PLATFORM_XBOX",
        "APP_PLATFORM_SAMSUNG_TV",
        "APP_PLATFORM_ANDROID_TV",
        "APP_PLATFORM_GENERIC_CTV",
    ]
    displayName: str
    negative: bool

@typing.type_check_only
class AppCategoryAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class AppCategoryTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    content: str
    mediaId: str

@typing.type_check_only
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

@typing.type_check_only
class AssignedInventorySource(typing_extensions.TypedDict, total=False):
    assignedInventorySourceId: str
    inventorySourceId: str
    name: str

@typing.type_check_only
class AssignedLocation(typing_extensions.TypedDict, total=False):
    assignedLocationId: str
    name: str
    targetingOptionId: str

@typing.type_check_only
class AssignedTargetingOption(typing_extensions.TypedDict, total=False):
    ageRangeDetails: AgeRangeAssignedTargetingOptionDetails
    appCategoryDetails: AppCategoryAssignedTargetingOptionDetails
    appDetails: AppAssignedTargetingOptionDetails
    assignedTargetingOptionId: str
    audienceGroupDetails: AudienceGroupAssignedTargetingOptionDetails
    audioContentTypeDetails: AudioContentTypeAssignedTargetingOptionDetails
    authorizedSellerStatusDetails: AuthorizedSellerStatusAssignedTargetingOptionDetails
    browserDetails: BrowserAssignedTargetingOptionDetails
    businessChainDetails: BusinessChainAssignedTargetingOptionDetails
    carrierAndIspDetails: CarrierAndIspAssignedTargetingOptionDetails
    categoryDetails: CategoryAssignedTargetingOptionDetails
    channelDetails: ChannelAssignedTargetingOptionDetails
    contentDurationDetails: ContentDurationAssignedTargetingOptionDetails
    contentGenreDetails: ContentGenreAssignedTargetingOptionDetails
    contentInstreamPositionDetails: ContentInstreamPositionAssignedTargetingOptionDetails
    contentOutstreamPositionDetails: ContentOutstreamPositionAssignedTargetingOptionDetails
    contentStreamTypeDetails: ContentStreamTypeAssignedTargetingOptionDetails
    dayAndTimeDetails: DayAndTimeAssignedTargetingOptionDetails
    deviceMakeModelDetails: DeviceMakeModelAssignedTargetingOptionDetails
    deviceTypeDetails: DeviceTypeAssignedTargetingOptionDetails
    digitalContentLabelExclusionDetails: DigitalContentLabelAssignedTargetingOptionDetails
    environmentDetails: EnvironmentAssignedTargetingOptionDetails
    exchangeDetails: ExchangeAssignedTargetingOptionDetails
    genderDetails: GenderAssignedTargetingOptionDetails
    geoRegionDetails: GeoRegionAssignedTargetingOptionDetails
    householdIncomeDetails: HouseholdIncomeAssignedTargetingOptionDetails
    inheritance: typing_extensions.Literal[
        "INHERITANCE_UNSPECIFIED",
        "NOT_INHERITED",
        "INHERITED_FROM_PARTNER",
        "INHERITED_FROM_ADVERTISER",
    ]
    inventorySourceDetails: InventorySourceAssignedTargetingOptionDetails
    inventorySourceGroupDetails: InventorySourceGroupAssignedTargetingOptionDetails
    keywordDetails: KeywordAssignedTargetingOptionDetails
    languageDetails: LanguageAssignedTargetingOptionDetails
    name: str
    nativeContentPositionDetails: NativeContentPositionAssignedTargetingOptionDetails
    negativeKeywordListDetails: NegativeKeywordListAssignedTargetingOptionDetails
    omidDetails: OmidAssignedTargetingOptionDetails
    onScreenPositionDetails: OnScreenPositionAssignedTargetingOptionDetails
    operatingSystemDetails: OperatingSystemAssignedTargetingOptionDetails
    parentalStatusDetails: ParentalStatusAssignedTargetingOptionDetails
    poiDetails: PoiAssignedTargetingOptionDetails
    proximityLocationListDetails: ProximityLocationListAssignedTargetingOptionDetails
    regionalLocationListDetails: RegionalLocationListAssignedTargetingOptionDetails
    sensitiveCategoryExclusionDetails: SensitiveCategoryAssignedTargetingOptionDetails
    subExchangeDetails: SubExchangeAssignedTargetingOptionDetails
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
        "TARGETING_TYPE_POI",
        "TARGETING_TYPE_BUSINESS_CHAIN",
        "TARGETING_TYPE_CONTENT_DURATION",
        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
        "TARGETING_TYPE_OMID",
        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
        "TARGETING_TYPE_CONTENT_GENRE",
    ]
    thirdPartyVerifierDetails: ThirdPartyVerifierAssignedTargetingOptionDetails
    urlDetails: UrlAssignedTargetingOptionDetails
    userRewardedContentDetails: UserRewardedContentAssignedTargetingOptionDetails
    videoPlayerSizeDetails: VideoPlayerSizeAssignedTargetingOptionDetails
    viewabilityDetails: ViewabilityAssignedTargetingOptionDetails

@typing.type_check_only
class AssignedUserRole(typing_extensions.TypedDict, total=False):
    advertiserId: str
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

@typing.type_check_only
class AudienceGroupAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    excludedFirstAndThirdPartyAudienceGroup: FirstAndThirdPartyAudienceGroup
    excludedGoogleAudienceGroup: GoogleAudienceGroup
    includedCombinedAudienceGroup: CombinedAudienceGroup
    includedCustomListGroup: CustomListGroup
    includedFirstAndThirdPartyAudienceGroups: _list[FirstAndThirdPartyAudienceGroup]
    includedGoogleAudienceGroup: GoogleAudienceGroup

@typing.type_check_only
class AudioContentTypeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    audioContentType: typing_extensions.Literal[
        "AUDIO_CONTENT_TYPE_UNSPECIFIED",
        "AUDIO_CONTENT_TYPE_UNKNOWN",
        "AUDIO_CONTENT_TYPE_MUSIC",
        "AUDIO_CONTENT_TYPE_BROADCAST",
        "AUDIO_CONTENT_TYPE_PODCAST",
    ]
    targetingOptionId: str

@typing.type_check_only
class AudioContentTypeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    audioContentType: typing_extensions.Literal[
        "AUDIO_CONTENT_TYPE_UNSPECIFIED",
        "AUDIO_CONTENT_TYPE_UNKNOWN",
        "AUDIO_CONTENT_TYPE_MUSIC",
        "AUDIO_CONTENT_TYPE_BROADCAST",
        "AUDIO_CONTENT_TYPE_PODCAST",
    ]

@typing.type_check_only
class AudioVideoOffset(typing_extensions.TypedDict, total=False):
    percentage: str
    seconds: str

@typing.type_check_only
class AuditAdvertiserResponse(typing_extensions.TypedDict, total=False):
    adGroupCriteriaCount: str
    campaignCriteriaCount: str
    channelsCount: str
    negativeKeywordListsCount: str
    negativelyTargetedChannelsCount: str
    usedCampaignsCount: str
    usedInsertionOrdersCount: str
    usedLineItemsCount: str

@typing.type_check_only
class AuthorizedSellerStatusAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    authorizedSellerStatus: typing_extensions.Literal[
        "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS",
    ]
    targetingOptionId: str

@typing.type_check_only
class AuthorizedSellerStatusTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    authorizedSellerStatus: typing_extensions.Literal[
        "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS",
    ]

@typing.type_check_only
class BiddingStrategy(typing_extensions.TypedDict, total=False):
    fixedBid: FixedBidStrategy
    maximizeSpendAutoBid: MaximizeSpendBidStrategy
    performanceGoalAutoBid: PerformanceGoalBidStrategy

@typing.type_check_only
class BrowserAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class BrowserTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class BudgetSummary(typing_extensions.TypedDict, total=False):
    externalBudgetId: str
    preTaxAmountMicros: str
    prismaCpeCode: PrismaCpeCode
    taxAmountMicros: str
    totalAmountMicros: str

@typing.type_check_only
class BulkEditAdvertiserAssignedTargetingOptionsRequest(
    typing_extensions.TypedDict, total=False
):
    createRequests: _list[CreateAssignedTargetingOptionsRequest]
    deleteRequests: _list[DeleteAssignedTargetingOptionsRequest]

@typing.type_check_only
class BulkEditAdvertiserAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    createdAssignedTargetingOptions: _list[AssignedTargetingOption]

@typing.type_check_only
class BulkEditAssignedInventorySourcesRequest(typing_extensions.TypedDict, total=False):
    advertiserId: str
    createdAssignedInventorySources: _list[AssignedInventorySource]
    deletedAssignedInventorySources: _list[str]
    partnerId: str

@typing.type_check_only
class BulkEditAssignedInventorySourcesResponse(
    typing_extensions.TypedDict, total=False
):
    assignedInventorySources: _list[AssignedInventorySource]

@typing.type_check_only
class BulkEditAssignedLocationsRequest(typing_extensions.TypedDict, total=False):
    createdAssignedLocations: _list[AssignedLocation]
    deletedAssignedLocations: _list[str]

@typing.type_check_only
class BulkEditAssignedLocationsResponse(typing_extensions.TypedDict, total=False):
    assignedLocations: _list[AssignedLocation]

@typing.type_check_only
class BulkEditAssignedUserRolesRequest(typing_extensions.TypedDict, total=False):
    createdAssignedUserRoles: _list[AssignedUserRole]
    deletedAssignedUserRoles: _list[str]

@typing.type_check_only
class BulkEditAssignedUserRolesResponse(typing_extensions.TypedDict, total=False):
    createdAssignedUserRoles: _list[AssignedUserRole]

@typing.type_check_only
class BulkEditLineItemAssignedTargetingOptionsRequest(
    typing_extensions.TypedDict, total=False
):
    createRequests: _list[CreateAssignedTargetingOptionsRequest]
    deleteRequests: _list[DeleteAssignedTargetingOptionsRequest]

@typing.type_check_only
class BulkEditLineItemAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    createdAssignedTargetingOptions: _list[AssignedTargetingOption]

@typing.type_check_only
class BulkEditNegativeKeywordsRequest(typing_extensions.TypedDict, total=False):
    createdNegativeKeywords: _list[NegativeKeyword]
    deletedNegativeKeywords: _list[str]

@typing.type_check_only
class BulkEditNegativeKeywordsResponse(typing_extensions.TypedDict, total=False):
    negativeKeywords: _list[NegativeKeyword]

@typing.type_check_only
class BulkEditPartnerAssignedTargetingOptionsRequest(
    typing_extensions.TypedDict, total=False
):
    createRequests: _list[CreateAssignedTargetingOptionsRequest]
    deleteRequests: _list[DeleteAssignedTargetingOptionsRequest]

@typing.type_check_only
class BulkEditPartnerAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    createdAssignedTargetingOptions: _list[AssignedTargetingOption]

@typing.type_check_only
class BulkEditSitesRequest(typing_extensions.TypedDict, total=False):
    advertiserId: str
    createdSites: _list[Site]
    deletedSites: _list[str]
    partnerId: str

@typing.type_check_only
class BulkEditSitesResponse(typing_extensions.TypedDict, total=False):
    sites: _list[Site]

@typing.type_check_only
class BulkListAdvertiserAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class BulkListCampaignAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class BulkListInsertionOrderAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class BulkListLineItemAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class BusinessChainAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    proximityRadiusAmount: float
    proximityRadiusUnit: typing_extensions.Literal[
        "DISTANCE_UNIT_UNSPECIFIED", "DISTANCE_UNIT_MILES", "DISTANCE_UNIT_KILOMETERS"
    ]
    targetingOptionId: str

@typing.type_check_only
class BusinessChainSearchTerms(typing_extensions.TypedDict, total=False):
    businessChainQuery: str
    regionQuery: str

@typing.type_check_only
class BusinessChainTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    businessChain: str
    geoRegion: str
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

@typing.type_check_only
class Campaign(typing_extensions.TypedDict, total=False):
    advertiserId: str
    campaignBudgets: _list[CampaignBudget]
    campaignFlight: CampaignFlight
    campaignGoal: CampaignGoal
    campaignId: str
    displayName: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    frequencyCap: FrequencyCap
    name: str
    updateTime: str

@typing.type_check_only
class CampaignBudget(typing_extensions.TypedDict, total=False):
    budgetAmountMicros: str
    budgetId: str
    budgetUnit: typing_extensions.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]
    dateRange: DateRange
    displayName: str
    externalBudgetId: str
    externalBudgetSource: typing_extensions.Literal[
        "EXTERNAL_BUDGET_SOURCE_UNSPECIFIED",
        "EXTERNAL_BUDGET_SOURCE_NONE",
        "EXTERNAL_BUDGET_SOURCE_MEDIA_OCEAN",
    ]
    invoiceGroupingId: str
    prismaConfig: PrismaConfig

@typing.type_check_only
class CampaignFlight(typing_extensions.TypedDict, total=False):
    plannedDates: DateRange
    plannedSpendAmountMicros: str

@typing.type_check_only
class CampaignGoal(typing_extensions.TypedDict, total=False):
    campaignGoalType: typing_extensions.Literal[
        "CAMPAIGN_GOAL_TYPE_UNSPECIFIED",
        "CAMPAIGN_GOAL_TYPE_APP_INSTALL",
        "CAMPAIGN_GOAL_TYPE_BRAND_AWARENESS",
        "CAMPAIGN_GOAL_TYPE_OFFLINE_ACTION",
        "CAMPAIGN_GOAL_TYPE_ONLINE_ACTION",
    ]
    performanceGoal: PerformanceGoal

@typing.type_check_only
class CarrierAndIspAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class CarrierAndIspTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    type: typing_extensions.Literal[
        "CARRIER_AND_ISP_TYPE_UNSPECIFIED",
        "CARRIER_AND_ISP_TYPE_ISP",
        "CARRIER_AND_ISP_TYPE_CARRIER",
    ]

@typing.type_check_only
class CategoryAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class CategoryTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    advertiserId: str
    channelId: str
    displayName: str
    name: str
    negativelyTargetedLineItemCount: str
    partnerId: str
    positivelyTargetedLineItemCount: str

@typing.type_check_only
class ChannelAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    channelId: str
    negative: bool

@typing.type_check_only
class CmHybridConfig(typing_extensions.TypedDict, total=False):
    cmAccountId: str
    cmFloodlightConfigId: str
    cmFloodlightLinkingAuthorized: bool
    cmSyncableSiteIds: _list[str]
    dv360ToCmCostReportingEnabled: bool
    dv360ToCmDataSharingEnabled: bool

@typing.type_check_only
class CmTrackingAd(typing_extensions.TypedDict, total=False):
    cmAdId: str
    cmCreativeId: str
    cmPlacementId: str

@typing.type_check_only
class CombinedAudience(typing_extensions.TypedDict, total=False):
    combinedAudienceId: str
    displayName: str
    name: str

@typing.type_check_only
class CombinedAudienceGroup(typing_extensions.TypedDict, total=False):
    settings: _list[CombinedAudienceTargetingSetting]

@typing.type_check_only
class CombinedAudienceTargetingSetting(typing_extensions.TypedDict, total=False):
    combinedAudienceId: str

@typing.type_check_only
class ContactInfo(typing_extensions.TypedDict, total=False):
    countryCode: str
    hashedEmails: _list[str]
    hashedFirstName: str
    hashedLastName: str
    hashedPhoneNumbers: _list[str]
    zipCodes: _list[str]

@typing.type_check_only
class ContactInfoList(typing_extensions.TypedDict, total=False):
    contactInfos: _list[ContactInfo]

@typing.type_check_only
class ContentDurationAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentDuration: typing_extensions.Literal[
        "CONTENT_DURATION_UNSPECIFIED",
        "CONTENT_DURATION_UNKNOWN",
        "CONTENT_DURATION_0_TO_1_MIN",
        "CONTENT_DURATION_1_TO_5_MIN",
        "CONTENT_DURATION_5_TO_15_MIN",
        "CONTENT_DURATION_15_TO_30_MIN",
        "CONTENT_DURATION_30_TO_60_MIN",
        "CONTENT_DURATION_OVER_60_MIN",
    ]
    targetingOptionId: str

@typing.type_check_only
class ContentDurationTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    contentDuration: typing_extensions.Literal[
        "CONTENT_DURATION_UNSPECIFIED",
        "CONTENT_DURATION_UNKNOWN",
        "CONTENT_DURATION_0_TO_1_MIN",
        "CONTENT_DURATION_1_TO_5_MIN",
        "CONTENT_DURATION_5_TO_15_MIN",
        "CONTENT_DURATION_15_TO_30_MIN",
        "CONTENT_DURATION_30_TO_60_MIN",
        "CONTENT_DURATION_OVER_60_MIN",
    ]

@typing.type_check_only
class ContentGenreAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class ContentGenreTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class ContentInstreamPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    adType: typing_extensions.Literal[
        "AD_TYPE_UNSPECIFIED", "AD_TYPE_DISPLAY", "AD_TYPE_VIDEO", "AD_TYPE_AUDIO"
    ]
    contentInstreamPosition: typing_extensions.Literal[
        "CONTENT_INSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_INSTREAM_POSITION_PRE_ROLL",
        "CONTENT_INSTREAM_POSITION_MID_ROLL",
        "CONTENT_INSTREAM_POSITION_POST_ROLL",
        "CONTENT_INSTREAM_POSITION_UNKNOWN",
    ]
    targetingOptionId: str

@typing.type_check_only
class ContentInstreamPositionTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentInstreamPosition: typing_extensions.Literal[
        "CONTENT_INSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_INSTREAM_POSITION_PRE_ROLL",
        "CONTENT_INSTREAM_POSITION_MID_ROLL",
        "CONTENT_INSTREAM_POSITION_POST_ROLL",
        "CONTENT_INSTREAM_POSITION_UNKNOWN",
    ]

@typing.type_check_only
class ContentOutstreamPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    adType: typing_extensions.Literal[
        "AD_TYPE_UNSPECIFIED", "AD_TYPE_DISPLAY", "AD_TYPE_VIDEO", "AD_TYPE_AUDIO"
    ]
    contentOutstreamPosition: typing_extensions.Literal[
        "CONTENT_OUTSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_OUTSTREAM_POSITION_UNKNOWN",
        "CONTENT_OUTSTREAM_POSITION_IN_ARTICLE",
        "CONTENT_OUTSTREAM_POSITION_IN_BANNER",
        "CONTENT_OUTSTREAM_POSITION_IN_FEED",
        "CONTENT_OUTSTREAM_POSITION_INTERSTITIAL",
    ]
    targetingOptionId: str

@typing.type_check_only
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

@typing.type_check_only
class ContentStreamTypeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentStreamType: typing_extensions.Literal[
        "CONTENT_STREAM_TYPE_UNSPECIFIED", "CONTENT_LIVE_STREAM", "CONTENT_ON_DEMAND"
    ]
    targetingOptionId: str

@typing.type_check_only
class ContentStreamTypeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    contentStreamType: typing_extensions.Literal[
        "CONTENT_STREAM_TYPE_UNSPECIFIED", "CONTENT_LIVE_STREAM", "CONTENT_ON_DEMAND"
    ]

@typing.type_check_only
class ConversionCountingConfig(typing_extensions.TypedDict, total=False):
    floodlightActivityConfigs: _list[TrackingFloodlightActivityConfig]
    postViewCountPercentageMillis: str

@typing.type_check_only
class CounterEvent(typing_extensions.TypedDict, total=False):
    name: str
    reportingName: str

@typing.type_check_only
class CreateAssetRequest(typing_extensions.TypedDict, total=False):
    filename: str

@typing.type_check_only
class CreateAssetResponse(typing_extensions.TypedDict, total=False):
    asset: Asset

@typing.type_check_only
class CreateAssignedTargetingOptionsRequest(typing_extensions.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
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
        "TARGETING_TYPE_POI",
        "TARGETING_TYPE_BUSINESS_CHAIN",
        "TARGETING_TYPE_CONTENT_DURATION",
        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
        "TARGETING_TYPE_OMID",
        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
        "TARGETING_TYPE_CONTENT_GENRE",
    ]

@typing.type_check_only
class CreateSdfDownloadTaskRequest(typing_extensions.TypedDict, total=False):
    advertiserId: str
    idFilter: IdFilter
    inventorySourceFilter: InventorySourceFilter
    parentEntityFilter: ParentEntityFilter
    partnerId: str
    version: typing_extensions.Literal[
        "SDF_VERSION_UNSPECIFIED",
        "SDF_VERSION_3_1",
        "SDF_VERSION_4",
        "SDF_VERSION_4_1",
        "SDF_VERSION_4_2",
        "SDF_VERSION_5",
        "SDF_VERSION_5_1",
        "SDF_VERSION_5_2",
        "SDF_VERSION_5_3",
        "SDF_VERSION_5_4",
        "SDF_VERSION_5_5",
    ]

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    additionalDimensions: _list[Dimensions]
    advertiserId: str
    appendedTag: str
    assets: _list[AssetAssociation]
    cmPlacementId: str
    cmTrackingAd: CmTrackingAd
    companionCreativeIds: _list[str]
    counterEvents: _list[CounterEvent]
    createTime: str
    creativeAttributes: _list[str]
    creativeId: str
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
    dimensions: Dimensions
    displayName: str
    dynamic: bool
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    exitEvents: _list[ExitEvent]
    expandOnHover: bool
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
    hostingSource: typing_extensions.Literal[
        "HOSTING_SOURCE_UNSPECIFIED",
        "HOSTING_SOURCE_CM",
        "HOSTING_SOURCE_THIRD_PARTY",
        "HOSTING_SOURCE_HOSTED",
        "HOSTING_SOURCE_RICH_MEDIA",
    ]
    html5Video: bool
    iasCampaignMonitoring: bool
    integrationCode: str
    jsTrackerUrl: str
    lineItemIds: _list[str]
    mediaDuration: str
    mp3Audio: bool
    name: str
    notes: str
    obaIcon: ObaIcon
    oggAudio: bool
    progressOffset: AudioVideoOffset
    requireHtml5: bool
    requireMraid: bool
    requirePingForAttribution: bool
    reviewStatus: ReviewStatusInfo
    skipOffset: AudioVideoOffset
    skippable: bool
    thirdPartyTag: str
    thirdPartyUrls: _list[ThirdPartyUrl]
    timerEvents: _list[TimerEvent]
    trackerUrls: _list[str]
    transcodes: _list[Transcode]
    universalAdId: UniversalAdId
    updateTime: str
    vastTagUrl: str
    vpaid: bool

@typing.type_check_only
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

@typing.type_check_only
class CustomBiddingAlgorithm(typing_extensions.TypedDict, total=False):
    advertiserId: str
    customBiddingAlgorithmId: str
    customBiddingAlgorithmState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DORMANT", "SUSPENDED"
    ]
    customBiddingAlgorithmType: typing_extensions.Literal[
        "CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED",
        "SCRIPT_BASED",
        "ADS_DATA_HUB_BASED",
        "GOAL_BUILDER_BASED",
    ]
    displayName: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    modelReadiness: _list[CustomBiddingModelReadinessState]
    name: str
    partnerId: str
    sharedAdvertiserIds: _list[str]

@typing.type_check_only
class CustomBiddingModelReadinessState(typing_extensions.TypedDict, total=False):
    advertiserId: str
    readinessState: typing_extensions.Literal[
        "READINESS_STATE_UNSPECIFIED",
        "READINESS_STATE_ACTIVE",
        "READINESS_STATE_INSUFFICIENT_DATA",
        "READINESS_STATE_TRAINING",
        "READINESS_STATE_NO_VALID_SCRIPT",
    ]

@typing.type_check_only
class CustomBiddingScript(typing_extensions.TypedDict, total=False):
    active: bool
    createTime: str
    customBiddingAlgorithmId: str
    customBiddingScriptId: str
    errors: _list[ScriptError]
    name: str
    script: CustomBiddingScriptRef
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACCEPTED", "REJECTED", "PENDING"
    ]

@typing.type_check_only
class CustomBiddingScriptRef(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class CustomList(typing_extensions.TypedDict, total=False):
    customListId: str
    displayName: str
    name: str

@typing.type_check_only
class CustomListGroup(typing_extensions.TypedDict, total=False):
    settings: _list[CustomListTargetingSetting]

@typing.type_check_only
class CustomListTargetingSetting(typing_extensions.TypedDict, total=False):
    customListId: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
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
    endHour: int
    startHour: int
    timeZoneResolution: typing_extensions.Literal[
        "TIME_ZONE_RESOLUTION_UNSPECIFIED",
        "TIME_ZONE_RESOLUTION_END_USER",
        "TIME_ZONE_RESOLUTION_ADVERTISER",
    ]

@typing.type_check_only
class DeactivateManualTriggerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteAssignedTargetingOptionsRequest(typing_extensions.TypedDict, total=False):
    assignedTargetingOptionIds: _list[str]
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
        "TARGETING_TYPE_POI",
        "TARGETING_TYPE_BUSINESS_CHAIN",
        "TARGETING_TYPE_CONTENT_DURATION",
        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
        "TARGETING_TYPE_OMID",
        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
        "TARGETING_TYPE_CONTENT_GENRE",
    ]

@typing.type_check_only
class DeviceMakeModelAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class DeviceMakeModelTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
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

@typing.type_check_only
class DeviceTypeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "DEVICE_TYPE_COMPUTER",
        "DEVICE_TYPE_CONNECTED_TV",
        "DEVICE_TYPE_SMART_PHONE",
        "DEVICE_TYPE_TABLET",
    ]

@typing.type_check_only
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

@typing.type_check_only
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

@typing.type_check_only
class Dimensions(typing_extensions.TypedDict, total=False):
    heightPixels: int
    widthPixels: int

@typing.type_check_only
class DoubleVerify(typing_extensions.TypedDict, total=False):
    appStarRating: DoubleVerifyAppStarRating
    avoidedAgeRatings: _list[str]
    brandSafetyCategories: DoubleVerifyBrandSafetyCategories
    customSegmentId: str
    displayViewability: DoubleVerifyDisplayViewability
    fraudInvalidTraffic: DoubleVerifyFraudInvalidTraffic
    videoViewability: DoubleVerifyVideoViewability

@typing.type_check_only
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

@typing.type_check_only
class DoubleVerifyBrandSafetyCategories(typing_extensions.TypedDict, total=False):
    avoidUnknownBrandSafetyCategory: bool
    avoidedHighSeverityCategories: _list[str]
    avoidedMediumSeverityCategories: _list[str]

@typing.type_check_only
class DoubleVerifyDisplayViewability(typing_extensions.TypedDict, total=False):
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
    viewableDuring: typing_extensions.Literal[
        "AVERAGE_VIEW_DURATION_UNSPECIFIED",
        "AVERAGE_VIEW_DURATION_5_SEC",
        "AVERAGE_VIEW_DURATION_10_SEC",
        "AVERAGE_VIEW_DURATION_15_SEC",
    ]

@typing.type_check_only
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

@typing.type_check_only
class DoubleVerifyVideoViewability(typing_extensions.TypedDict, total=False):
    playerImpressionRate: typing_extensions.Literal[
        "PLAYER_SIZE_400X300_UNSPECIFIED",
        "PLAYER_SIZE_400X300_95",
        "PLAYER_SIZE_400X300_70",
        "PLAYER_SIZE_400X300_25",
        "PLAYER_SIZE_400X300_5",
    ]
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

@typing.type_check_only
class EditCustomerMatchMembersRequest(typing_extensions.TypedDict, total=False):
    addedContactInfoList: ContactInfoList
    addedMobileDeviceIdList: MobileDeviceIdList
    advertiserId: str

@typing.type_check_only
class EditCustomerMatchMembersResponse(typing_extensions.TypedDict, total=False):
    firstAndThirdPartyAudienceId: str

@typing.type_check_only
class EditGuaranteedOrderReadAccessorsRequest(typing_extensions.TypedDict, total=False):
    addedAdvertisers: _list[str]
    partnerId: str
    readAccessInherited: bool
    removedAdvertisers: _list[str]

@typing.type_check_only
class EditGuaranteedOrderReadAccessorsResponse(
    typing_extensions.TypedDict, total=False
):
    readAccessInherited: bool
    readAdvertiserIds: _list[str]

@typing.type_check_only
class EditInventorySourceReadWriteAccessorsRequest(
    typing_extensions.TypedDict, total=False
):
    advertisersUpdate: EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdate
    assignPartner: bool
    partnerId: str

@typing.type_check_only
class EditInventorySourceReadWriteAccessorsRequestAdvertisersUpdate(
    typing_extensions.TypedDict, total=False
):
    addedAdvertisers: _list[str]
    removedAdvertisers: _list[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnvironmentAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    environment: typing_extensions.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_WEB_OPTIMIZED",
        "ENVIRONMENT_WEB_NOT_OPTIMIZED",
        "ENVIRONMENT_APP",
    ]
    targetingOptionId: str

@typing.type_check_only
class EnvironmentTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    environment: typing_extensions.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_WEB_OPTIMIZED",
        "ENVIRONMENT_WEB_NOT_OPTIMIZED",
        "ENVIRONMENT_APP",
    ]

@typing.type_check_only
class ExchangeAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    targetingOptionId: str

@typing.type_check_only
class ExchangeConfig(typing_extensions.TypedDict, total=False):
    enabledExchanges: _list[ExchangeConfigEnabledExchange]

@typing.type_check_only
class ExchangeConfigEnabledExchange(typing_extensions.TypedDict, total=False):
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
        "EXCHANGE_SUPERSHIP",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
        "EXCHANGE_SOUNDCAST",
        "EXCHANGE_SHARETHROUGH",
        "EXCHANGE_FYBER",
        "EXCHANGE_RED_FOR_PUBLISHERS",
        "EXCHANGE_MEDIANET",
        "EXCHANGE_TAPJOY",
        "EXCHANGE_VISTAR",
        "EXCHANGE_DAX",
    ]
    googleAdManagerAgencyId: str
    googleAdManagerBuyerNetworkId: str
    seatId: str

@typing.type_check_only
class ExchangeReviewStatus(typing_extensions.TypedDict, total=False):
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
        "EXCHANGE_SUPERSHIP",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
        "EXCHANGE_SOUNDCAST",
        "EXCHANGE_SHARETHROUGH",
        "EXCHANGE_FYBER",
        "EXCHANGE_RED_FOR_PUBLISHERS",
        "EXCHANGE_MEDIANET",
        "EXCHANGE_TAPJOY",
        "EXCHANGE_VISTAR",
        "EXCHANGE_DAX",
    ]
    status: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]

@typing.type_check_only
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
        "EXCHANGE_SUPERSHIP",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
        "EXCHANGE_SOUNDCAST",
        "EXCHANGE_SHARETHROUGH",
        "EXCHANGE_FYBER",
        "EXCHANGE_RED_FOR_PUBLISHERS",
        "EXCHANGE_MEDIANET",
        "EXCHANGE_TAPJOY",
        "EXCHANGE_VISTAR",
        "EXCHANGE_DAX",
    ]

@typing.type_check_only
class ExitEvent(typing_extensions.TypedDict, total=False):
    name: str
    reportingName: str
    type: typing_extensions.Literal[
        "EXIT_EVENT_TYPE_UNSPECIFIED",
        "EXIT_EVENT_TYPE_DEFAULT",
        "EXIT_EVENT_TYPE_BACKUP",
    ]
    url: str

@typing.type_check_only
class FirstAndThirdPartyAudience(typing_extensions.TypedDict, total=False):
    activeDisplayAudienceSize: str
    appId: str
    audienceSource: typing_extensions.Literal[
        "AUDIENCE_SOURCE_UNSPECIFIED",
        "DISPLAY_VIDEO_360",
        "CAMPAIGN_MANAGER",
        "AD_MANAGER",
        "SEARCH_ADS_360",
        "YOUTUBE",
        "ADS_DATA_HUB",
    ]
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
    contactInfoList: ContactInfoList
    description: str
    displayAudienceSize: str
    displayDesktopAudienceSize: str
    displayMobileAppAudienceSize: str
    displayMobileWebAudienceSize: str
    displayName: str
    firstAndThirdPartyAudienceId: str
    firstAndThirdPartyAudienceType: typing_extensions.Literal[
        "FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_UNSPECIFIED",
        "FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_FIRST_PARTY",
        "FIRST_AND_THIRD_PARTY_AUDIENCE_TYPE_THIRD_PARTY",
    ]
    gmailAudienceSize: str
    membershipDurationDays: str
    mobileDeviceIdList: MobileDeviceIdList
    name: str
    youtubeAudienceSize: str

@typing.type_check_only
class FirstAndThirdPartyAudienceGroup(typing_extensions.TypedDict, total=False):
    settings: _list[FirstAndThirdPartyAudienceTargetingSetting]

@typing.type_check_only
class FirstAndThirdPartyAudienceTargetingSetting(
    typing_extensions.TypedDict, total=False
):
    firstAndThirdPartyAudienceId: str
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
        "RECENCY_45_DAYS",
        "RECENCY_60_DAYS",
        "RECENCY_90_DAYS",
        "RECENCY_120_DAYS",
        "RECENCY_180_DAYS",
        "RECENCY_270_DAYS",
        "RECENCY_365_DAYS",
    ]

@typing.type_check_only
class FixedBidStrategy(typing_extensions.TypedDict, total=False):
    bidAmountMicros: str

@typing.type_check_only
class FloodlightGroup(typing_extensions.TypedDict, total=False):
    activeViewConfig: ActiveViewVideoViewabilityMetricConfig
    customVariables: dict[str, typing.Any]
    displayName: str
    floodlightGroupId: str
    lookbackWindow: LookbackWindow
    name: str
    webTagType: typing_extensions.Literal[
        "WEB_TAG_TYPE_UNSPECIFIED",
        "WEB_TAG_TYPE_NONE",
        "WEB_TAG_TYPE_IMAGE",
        "WEB_TAG_TYPE_DYNAMIC",
    ]

@typing.type_check_only
class FrequencyCap(typing_extensions.TypedDict, total=False):
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
    timeUnitCount: int
    unlimited: bool

@typing.type_check_only
class GenderAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    gender: typing_extensions.Literal[
        "GENDER_UNSPECIFIED", "GENDER_MALE", "GENDER_FEMALE", "GENDER_UNKNOWN"
    ]
    targetingOptionId: str

@typing.type_check_only
class GenderTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    gender: typing_extensions.Literal[
        "GENDER_UNSPECIFIED", "GENDER_MALE", "GENDER_FEMALE", "GENDER_UNKNOWN"
    ]

@typing.type_check_only
class GenerateDefaultLineItemRequest(typing_extensions.TypedDict, total=False):
    displayName: str
    insertionOrderId: str
    lineItemType: typing_extensions.Literal[
        "LINE_ITEM_TYPE_UNSPECIFIED",
        "LINE_ITEM_TYPE_DISPLAY_DEFAULT",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_VIDEO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_AUDIO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_OVER_THE_TOP",
    ]
    mobileApp: MobileApp

@typing.type_check_only
class GeoRegionAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
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
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class GeoRegionSearchTerms(typing_extensions.TypedDict, total=False):
    geoRegionQuery: str

@typing.type_check_only
class GeoRegionTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
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

@typing.type_check_only
class GoogleAudience(typing_extensions.TypedDict, total=False):
    displayName: str
    googleAudienceId: str
    googleAudienceType: typing_extensions.Literal[
        "GOOGLE_AUDIENCE_TYPE_UNSPECIFIED",
        "GOOGLE_AUDIENCE_TYPE_AFFINITY",
        "GOOGLE_AUDIENCE_TYPE_IN_MARKET",
        "GOOGLE_AUDIENCE_TYPE_INSTALLED_APPS",
        "GOOGLE_AUDIENCE_TYPE_NEW_MOBILE_DEVICES",
        "GOOGLE_AUDIENCE_TYPE_LIFE_EVENT",
        "GOOGLE_AUDIENCE_TYPE_EXTENDED_DEMOGRAPHIC",
    ]
    name: str

@typing.type_check_only
class GoogleAudienceGroup(typing_extensions.TypedDict, total=False):
    settings: _list[GoogleAudienceTargetingSetting]

@typing.type_check_only
class GoogleAudienceTargetingSetting(typing_extensions.TypedDict, total=False):
    googleAudienceId: str

@typing.type_check_only
class GoogleBytestreamMedia(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GuaranteedOrder(typing_extensions.TypedDict, total=False):
    defaultAdvertiserId: str
    defaultCampaignId: str
    displayName: str
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
        "EXCHANGE_SUPERSHIP",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
        "EXCHANGE_SOUNDCAST",
        "EXCHANGE_SHARETHROUGH",
        "EXCHANGE_FYBER",
        "EXCHANGE_RED_FOR_PUBLISHERS",
        "EXCHANGE_MEDIANET",
        "EXCHANGE_TAPJOY",
        "EXCHANGE_VISTAR",
        "EXCHANGE_DAX",
    ]
    guaranteedOrderId: str
    legacyGuaranteedOrderId: str
    name: str
    publisherName: str
    readAccessInherited: bool
    readAdvertiserIds: _list[str]
    readWriteAdvertiserId: str
    readWritePartnerId: str
    status: GuaranteedOrderStatus
    updateTime: str

@typing.type_check_only
class GuaranteedOrderStatus(typing_extensions.TypedDict, total=False):
    configStatus: typing_extensions.Literal[
        "GUARANTEED_ORDER_CONFIG_STATUS_UNSPECIFIED", "PENDING", "COMPLETED"
    ]
    entityPauseReason: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]

@typing.type_check_only
class HouseholdIncomeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
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
    targetingOptionId: str

@typing.type_check_only
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

@typing.type_check_only
class IdFilter(typing_extensions.TypedDict, total=False):
    adGroupAdIds: _list[str]
    adGroupIds: _list[str]
    campaignIds: _list[str]
    insertionOrderIds: _list[str]
    lineItemIds: _list[str]
    mediaProductIds: _list[str]

@typing.type_check_only
class InsertionOrder(typing_extensions.TypedDict, total=False):
    advertiserId: str
    bidStrategy: BiddingStrategy
    billableOutcome: typing_extensions.Literal[
        "BILLABLE_OUTCOME_UNSPECIFIED",
        "BILLABLE_OUTCOME_PAY_PER_IMPRESSION",
        "BILLABLE_OUTCOME_PAY_PER_CLICK",
        "BILLABLE_OUTCOME_PAY_PER_VIEWABLE_IMPRESSION",
    ]
    budget: InsertionOrderBudget
    campaignId: str
    displayName: str
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
    insertionOrderType: typing_extensions.Literal[
        "INSERTION_ORDER_TYPE_UNSPECIFIED", "RTB", "OVER_THE_TOP"
    ]
    integrationDetails: IntegrationDetails
    name: str
    pacing: Pacing
    partnerCosts: _list[PartnerCost]
    performanceGoal: PerformanceGoal
    reservationType: typing_extensions.Literal[
        "RESERVATION_TYPE_UNSPECIFIED",
        "RESERVATION_TYPE_NOT_GUARANTEED",
        "RESERVATION_TYPE_PROGRAMMATIC_GUARANTEED",
        "RESERVATION_TYPE_TAG_GUARANTEED",
    ]
    updateTime: str

@typing.type_check_only
class InsertionOrderBudget(typing_extensions.TypedDict, total=False):
    automationType: typing_extensions.Literal[
        "INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED",
        "INSERTION_ORDER_AUTOMATION_TYPE_BUDGET",
        "INSERTION_ORDER_AUTOMATION_TYPE_NONE",
        "INSERTION_ORDER_AUTOMATION_TYPE_BID_BUDGET",
    ]
    budgetSegments: _list[InsertionOrderBudgetSegment]
    budgetUnit: typing_extensions.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]

@typing.type_check_only
class InsertionOrderBudgetSegment(typing_extensions.TypedDict, total=False):
    budgetAmountMicros: str
    campaignBudgetId: str
    dateRange: DateRange
    description: str

@typing.type_check_only
class IntegralAdScience(typing_extensions.TypedDict, total=False):
    customSegmentId: _list[str]
    displayViewability: typing_extensions.Literal[
        "PERFORMANCE_VIEWABILITY_UNSPECIFIED",
        "PERFORMANCE_VIEWABILITY_40",
        "PERFORMANCE_VIEWABILITY_50",
        "PERFORMANCE_VIEWABILITY_60",
        "PERFORMANCE_VIEWABILITY_70",
    ]
    excludeUnrateable: bool
    excludedAdFraudRisk: typing_extensions.Literal[
        "SUSPICIOUS_ACTIVITY_UNSPECIFIED",
        "SUSPICIOUS_ACTIVITY_HR",
        "SUSPICIOUS_ACTIVITY_HMR",
    ]
    excludedAdultRisk: typing_extensions.Literal[
        "ADULT_UNSPECIFIED", "ADULT_HR", "ADULT_HMR"
    ]
    excludedAlcoholRisk: typing_extensions.Literal[
        "ALCOHOL_UNSPECIFIED", "ALCOHOL_HR", "ALCOHOL_HMR"
    ]
    excludedDrugsRisk: typing_extensions.Literal[
        "DRUGS_UNSPECIFIED", "DRUGS_HR", "DRUGS_HMR"
    ]
    excludedGamblingRisk: typing_extensions.Literal[
        "GAMBLING_UNSPECIFIED", "GAMBLING_HR", "GAMBLING_HMR"
    ]
    excludedHateSpeechRisk: typing_extensions.Literal[
        "HATE_SPEECH_UNSPECIFIED", "HATE_SPEECH_HR", "HATE_SPEECH_HMR"
    ]
    excludedIllegalDownloadsRisk: typing_extensions.Literal[
        "ILLEGAL_DOWNLOADS_UNSPECIFIED", "ILLEGAL_DOWNLOADS_HR", "ILLEGAL_DOWNLOADS_HMR"
    ]
    excludedOffensiveLanguageRisk: typing_extensions.Literal[
        "OFFENSIVE_LANGUAGE_UNSPECIFIED",
        "OFFENSIVE_LANGUAGE_HR",
        "OFFENSIVE_LANGUAGE_HMR",
    ]
    excludedViolenceRisk: typing_extensions.Literal[
        "VIOLENCE_UNSPECIFIED", "VIOLENCE_HR", "VIOLENCE_HMR"
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
    videoViewability: typing_extensions.Literal[
        "VIDEO_VIEWABILITY_UNSPECIFIED",
        "VIDEO_VIEWABILITY_40",
        "VIDEO_VIEWABILITY_50",
        "VIDEO_VIEWABILITY_60",
        "VIDEO_VIEWABILITY_70",
    ]

@typing.type_check_only
class IntegrationDetails(typing_extensions.TypedDict, total=False):
    details: str
    integrationCode: str

@typing.type_check_only
class InventorySource(typing_extensions.TypedDict, total=False):
    commitment: typing_extensions.Literal[
        "INVENTORY_SOURCE_COMMITMENT_UNSPECIFIED",
        "INVENTORY_SOURCE_COMMITMENT_GUARANTEED",
        "INVENTORY_SOURCE_COMMITMENT_NON_GUARANTEED",
    ]
    creativeConfigs: _list[CreativeConfig]
    dealId: str
    deliveryMethod: typing_extensions.Literal[
        "INVENTORY_SOURCE_DELIVERY_METHOD_UNSPECIFIED",
        "INVENTORY_SOURCE_DELIVERY_METHOD_PROGRAMMATIC",
        "INVENTORY_SOURCE_DELIVERY_METHOD_TAG",
    ]
    displayName: str
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
        "EXCHANGE_SUPERSHIP",
        "EXCHANGE_NEXSTAR_DIGITAL",
        "EXCHANGE_WAZE",
        "EXCHANGE_SOUNDCAST",
        "EXCHANGE_SHARETHROUGH",
        "EXCHANGE_FYBER",
        "EXCHANGE_RED_FOR_PUBLISHERS",
        "EXCHANGE_MEDIANET",
        "EXCHANGE_TAPJOY",
        "EXCHANGE_VISTAR",
        "EXCHANGE_DAX",
    ]
    guaranteedOrderId: str
    inventorySourceId: str
    inventorySourceProductType: typing_extensions.Literal[
        "INVENTORY_SOURCE_PRODUCT_TYPE_UNSPECIFIED",
        "PREFERRED_DEAL",
        "PRIVATE_AUCTION",
        "PROGRAMMATIC_GUARANTEED",
        "TAG_GUARANTEED",
        "YOUTUBE_RESERVE",
        "INSTANT_RESERVE",
        "GUARANTEED_PACKAGE",
        "PROGRAMMATIC_TV",
        "AUCTION_PACKAGE",
    ]
    inventorySourceType: typing_extensions.Literal[
        "INVENTORY_SOURCE_TYPE_UNSPECIFIED",
        "INVENTORY_SOURCE_TYPE_PRIVATE",
        "INVENTORY_SOURCE_TYPE_AUCTION_PACKAGE",
    ]
    name: str
    publisherName: str
    rateDetails: RateDetails
    readAdvertiserIds: _list[str]
    readPartnerIds: _list[str]
    readWriteAccessors: InventorySourceAccessors
    status: InventorySourceStatus
    subSitePropertyId: str
    timeRange: TimeRange
    updateTime: str

@typing.type_check_only
class InventorySourceAccessors(typing_extensions.TypedDict, total=False):
    advertisers: InventorySourceAccessorsAdvertiserAccessors
    partner: InventorySourceAccessorsPartnerAccessor

@typing.type_check_only
class InventorySourceAccessorsAdvertiserAccessors(
    typing_extensions.TypedDict, total=False
):
    advertiserIds: _list[str]

@typing.type_check_only
class InventorySourceAccessorsPartnerAccessor(typing_extensions.TypedDict, total=False):
    partnerId: str

@typing.type_check_only
class InventorySourceAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    inventorySourceId: str

@typing.type_check_only
class InventorySourceDisplayCreativeConfig(typing_extensions.TypedDict, total=False):
    creativeSize: Dimensions

@typing.type_check_only
class InventorySourceFilter(typing_extensions.TypedDict, total=False):
    inventorySourceIds: _list[str]

@typing.type_check_only
class InventorySourceGroup(typing_extensions.TypedDict, total=False):
    displayName: str
    inventorySourceGroupId: str
    name: str

@typing.type_check_only
class InventorySourceGroupAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    inventorySourceGroupId: str

@typing.type_check_only
class InventorySourceStatus(typing_extensions.TypedDict, total=False):
    configStatus: typing_extensions.Literal[
        "INVENTORY_SOURCE_CONFIG_STATUS_UNSPECIFIED",
        "INVENTORY_SOURCE_CONFIG_STATUS_PENDING",
        "INVENTORY_SOURCE_CONFIG_STATUS_COMPLETED",
    ]
    entityPauseReason: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    sellerPauseReason: str
    sellerStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]

@typing.type_check_only
class InventorySourceVideoCreativeConfig(typing_extensions.TypedDict, total=False):
    duration: str

@typing.type_check_only
class Invoice(typing_extensions.TypedDict, total=False):
    budgetInvoiceGroupingId: str
    budgetSummaries: _list[BudgetSummary]
    correctedInvoiceId: str
    currencyCode: str
    displayName: str
    dueDate: Date
    invoiceId: str
    invoiceType: typing_extensions.Literal[
        "INVOICE_TYPE_UNSPECIFIED", "INVOICE_TYPE_CREDIT", "INVOICE_TYPE_INVOICE"
    ]
    issueDate: Date
    name: str
    nonBudgetMicros: str
    paymentsAccountId: str
    paymentsProfileId: str
    pdfUrl: str
    purchaseOrderNumber: str
    replacedInvoiceIds: _list[str]
    serviceDateRange: DateRange
    subtotalAmountMicros: str
    totalAmountMicros: str
    totalTaxAmountMicros: str

@typing.type_check_only
class KeywordAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    keyword: str
    negative: bool

@typing.type_check_only
class LanguageAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class LanguageTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class LineItem(typing_extensions.TypedDict, total=False):
    advertiserId: str
    bidStrategy: BiddingStrategy
    budget: LineItemBudget
    campaignId: str
    conversionCounting: ConversionCountingConfig
    creativeIds: _list[str]
    displayName: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    excludeNewExchanges: bool
    flight: LineItemFlight
    frequencyCap: FrequencyCap
    insertionOrderId: str
    integrationDetails: IntegrationDetails
    inventorySourceIds: _list[str]
    lineItemId: str
    lineItemType: typing_extensions.Literal[
        "LINE_ITEM_TYPE_UNSPECIFIED",
        "LINE_ITEM_TYPE_DISPLAY_DEFAULT",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_VIDEO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_AUDIO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_OVER_THE_TOP",
    ]
    mobileApp: MobileApp
    name: str
    pacing: Pacing
    partnerCosts: _list[PartnerCost]
    partnerRevenueModel: PartnerRevenueModel
    reservationType: typing_extensions.Literal[
        "RESERVATION_TYPE_UNSPECIFIED",
        "RESERVATION_TYPE_NOT_GUARANTEED",
        "RESERVATION_TYPE_PROGRAMMATIC_GUARANTEED",
        "RESERVATION_TYPE_TAG_GUARANTEED",
    ]
    targetingExpansion: TargetingExpansionConfig
    updateTime: str
    warningMessages: _list[str]

@typing.type_check_only
class LineItemBudget(typing_extensions.TypedDict, total=False):
    budgetAllocationType: typing_extensions.Literal[
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED",
    ]
    budgetUnit: typing_extensions.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]
    maxAmount: str

@typing.type_check_only
class LineItemFlight(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    flightDateType: typing_extensions.Literal[
        "LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED",
        "LINE_ITEM_FLIGHT_DATE_TYPE_INHERITED",
        "LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM",
        "LINE_ITEM_FLIGHT_DATE_TYPE_TRIGGER",
    ]
    triggerId: str

@typing.type_check_only
class ListAdvertiserAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListAdvertisersResponse(typing_extensions.TypedDict, total=False):
    advertisers: _list[Advertiser]
    nextPageToken: str

@typing.type_check_only
class ListAssignedInventorySourcesResponse(typing_extensions.TypedDict, total=False):
    assignedInventorySources: _list[AssignedInventorySource]
    nextPageToken: str

@typing.type_check_only
class ListAssignedLocationsResponse(typing_extensions.TypedDict, total=False):
    assignedLocations: _list[AssignedLocation]
    nextPageToken: str

@typing.type_check_only
class ListCampaignAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListCampaignsResponse(typing_extensions.TypedDict, total=False):
    campaigns: _list[Campaign]
    nextPageToken: str

@typing.type_check_only
class ListChannelsResponse(typing_extensions.TypedDict, total=False):
    channels: _list[Channel]
    nextPageToken: str

@typing.type_check_only
class ListCombinedAudiencesResponse(typing_extensions.TypedDict, total=False):
    combinedAudiences: _list[CombinedAudience]
    nextPageToken: str

@typing.type_check_only
class ListCreativesResponse(typing_extensions.TypedDict, total=False):
    creatives: _list[Creative]
    nextPageToken: str

@typing.type_check_only
class ListCustomBiddingAlgorithmsResponse(typing_extensions.TypedDict, total=False):
    customBiddingAlgorithms: _list[CustomBiddingAlgorithm]
    nextPageToken: str

@typing.type_check_only
class ListCustomBiddingScriptsResponse(typing_extensions.TypedDict, total=False):
    customBiddingScripts: _list[CustomBiddingScript]
    nextPageToken: str

@typing.type_check_only
class ListCustomListsResponse(typing_extensions.TypedDict, total=False):
    customLists: _list[CustomList]
    nextPageToken: str

@typing.type_check_only
class ListFirstAndThirdPartyAudiencesResponse(typing_extensions.TypedDict, total=False):
    firstAndThirdPartyAudiences: _list[FirstAndThirdPartyAudience]
    nextPageToken: str

@typing.type_check_only
class ListGoogleAudiencesResponse(typing_extensions.TypedDict, total=False):
    googleAudiences: _list[GoogleAudience]
    nextPageToken: str

@typing.type_check_only
class ListGuaranteedOrdersResponse(typing_extensions.TypedDict, total=False):
    guaranteedOrders: _list[GuaranteedOrder]
    nextPageToken: str

@typing.type_check_only
class ListInsertionOrderAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListInsertionOrdersResponse(typing_extensions.TypedDict, total=False):
    insertionOrders: _list[InsertionOrder]
    nextPageToken: str

@typing.type_check_only
class ListInventorySourceGroupsResponse(typing_extensions.TypedDict, total=False):
    inventorySourceGroups: _list[InventorySourceGroup]
    nextPageToken: str

@typing.type_check_only
class ListInventorySourcesResponse(typing_extensions.TypedDict, total=False):
    inventorySources: _list[InventorySource]
    nextPageToken: str

@typing.type_check_only
class ListInvoicesResponse(typing_extensions.TypedDict, total=False):
    invoices: _list[Invoice]
    nextPageToken: str

@typing.type_check_only
class ListLineItemAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListLineItemsResponse(typing_extensions.TypedDict, total=False):
    lineItems: _list[LineItem]
    nextPageToken: str

@typing.type_check_only
class ListLocationListsResponse(typing_extensions.TypedDict, total=False):
    locationLists: _list[LocationList]
    nextPageToken: str

@typing.type_check_only
class ListManualTriggersResponse(typing_extensions.TypedDict, total=False):
    manualTriggers: _list[ManualTrigger]
    nextPageToken: str

@typing.type_check_only
class ListNegativeKeywordListsResponse(typing_extensions.TypedDict, total=False):
    negativeKeywordLists: _list[NegativeKeywordList]
    nextPageToken: str

@typing.type_check_only
class ListNegativeKeywordsResponse(typing_extensions.TypedDict, total=False):
    negativeKeywords: _list[NegativeKeyword]
    nextPageToken: str

@typing.type_check_only
class ListPartnerAssignedTargetingOptionsResponse(
    typing_extensions.TypedDict, total=False
):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListPartnersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    partners: _list[Partner]

@typing.type_check_only
class ListSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class ListTargetingOptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    targetingOptions: _list[TargetingOption]

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class LocationList(typing_extensions.TypedDict, total=False):
    advertiserId: str
    displayName: str
    locationListId: str
    locationType: typing_extensions.Literal[
        "TARGETING_LOCATION_TYPE_UNSPECIFIED",
        "TARGETING_LOCATION_TYPE_PROXIMITY",
        "TARGETING_LOCATION_TYPE_REGIONAL",
    ]
    name: str

@typing.type_check_only
class LookbackWindow(typing_extensions.TypedDict, total=False):
    clickDays: int
    impressionDays: int

@typing.type_check_only
class LookupInvoiceCurrencyResponse(typing_extensions.TypedDict, total=False):
    currencyCode: str

@typing.type_check_only
class ManualTrigger(typing_extensions.TypedDict, total=False):
    activationDurationMinutes: str
    advertiserId: str
    displayName: str
    latestActivationTime: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "INACTIVE", "ACTIVE"]
    triggerId: str

@typing.type_check_only
class MaximizeSpendBidStrategy(typing_extensions.TypedDict, total=False):
    customBiddingAlgorithmId: str
    maxAverageCpmBidAmountMicros: str
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
    raiseBidForDeals: bool

@typing.type_check_only
class MeasurementConfig(typing_extensions.TypedDict, total=False):
    dv360ToCmCostReportingEnabled: bool
    dv360ToCmDataSharingEnabled: bool

@typing.type_check_only
class MobileApp(typing_extensions.TypedDict, total=False):
    appId: str
    displayName: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "IOS", "ANDROID"]
    publisher: str

@typing.type_check_only
class MobileDeviceIdList(typing_extensions.TypedDict, total=False):
    mobileDeviceIds: _list[str]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class NativeContentPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentPosition: typing_extensions.Literal[
        "NATIVE_CONTENT_POSITION_UNSPECIFIED",
        "NATIVE_CONTENT_POSITION_UNKNOWN",
        "NATIVE_CONTENT_POSITION_IN_ARTICLE",
        "NATIVE_CONTENT_POSITION_IN_FEED",
        "NATIVE_CONTENT_POSITION_PERIPHERAL",
        "NATIVE_CONTENT_POSITION_RECOMMENDATION",
    ]
    targetingOptionId: str

@typing.type_check_only
class NativeContentPositionTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    contentPosition: typing_extensions.Literal[
        "NATIVE_CONTENT_POSITION_UNSPECIFIED",
        "NATIVE_CONTENT_POSITION_UNKNOWN",
        "NATIVE_CONTENT_POSITION_IN_ARTICLE",
        "NATIVE_CONTENT_POSITION_IN_FEED",
        "NATIVE_CONTENT_POSITION_PERIPHERAL",
        "NATIVE_CONTENT_POSITION_RECOMMENDATION",
    ]

@typing.type_check_only
class NegativeKeyword(typing_extensions.TypedDict, total=False):
    keywordValue: str
    name: str

@typing.type_check_only
class NegativeKeywordList(typing_extensions.TypedDict, total=False):
    advertiserId: str
    displayName: str
    name: str
    negativeKeywordListId: str
    targetedLineItemCount: str

@typing.type_check_only
class NegativeKeywordListAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    negativeKeywordListId: str

@typing.type_check_only
class ObaIcon(typing_extensions.TypedDict, total=False):
    clickTrackingUrl: str
    dimensions: Dimensions
    landingPageUrl: str
    position: typing_extensions.Literal[
        "OBA_ICON_POSITION_UNSPECIFIED",
        "OBA_ICON_POSITION_UPPER_RIGHT",
        "OBA_ICON_POSITION_UPPER_LEFT",
        "OBA_ICON_POSITION_LOWER_RIGHT",
        "OBA_ICON_POSITION_LOWER_LEFT",
    ]
    program: str
    resourceMimeType: str
    resourceUrl: str
    viewTrackingUrl: str

@typing.type_check_only
class OmidAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    omid: typing_extensions.Literal["OMID_UNSPECIFIED", "OMID_FOR_MOBILE_DISPLAY_ADS"]
    targetingOptionId: str

@typing.type_check_only
class OmidTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    omid: typing_extensions.Literal["OMID_UNSPECIFIED", "OMID_FOR_MOBILE_DISPLAY_ADS"]

@typing.type_check_only
class OnScreenPositionAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    adType: typing_extensions.Literal[
        "AD_TYPE_UNSPECIFIED", "AD_TYPE_DISPLAY", "AD_TYPE_VIDEO", "AD_TYPE_AUDIO"
    ]
    onScreenPosition: typing_extensions.Literal[
        "ON_SCREEN_POSITION_UNSPECIFIED",
        "ON_SCREEN_POSITION_UNKNOWN",
        "ON_SCREEN_POSITION_ABOVE_THE_FOLD",
        "ON_SCREEN_POSITION_BELOW_THE_FOLD",
    ]
    targetingOptionId: str

@typing.type_check_only
class OnScreenPositionTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    onScreenPosition: typing_extensions.Literal[
        "ON_SCREEN_POSITION_UNSPECIFIED",
        "ON_SCREEN_POSITION_UNKNOWN",
        "ON_SCREEN_POSITION_ABOVE_THE_FOLD",
        "ON_SCREEN_POSITION_BELOW_THE_FOLD",
    ]

@typing.type_check_only
class OperatingSystemAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class OperatingSystemTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Pacing(typing_extensions.TypedDict, total=False):
    dailyMaxImpressions: str
    dailyMaxMicros: str
    pacingPeriod: typing_extensions.Literal[
        "PACING_PERIOD_UNSPECIFIED", "PACING_PERIOD_DAILY", "PACING_PERIOD_FLIGHT"
    ]
    pacingType: typing_extensions.Literal[
        "PACING_TYPE_UNSPECIFIED",
        "PACING_TYPE_AHEAD",
        "PACING_TYPE_ASAP",
        "PACING_TYPE_EVEN",
    ]

@typing.type_check_only
class ParentEntityFilter(typing_extensions.TypedDict, total=False):
    fileType: _list[str]
    filterIds: _list[str]
    filterType: typing_extensions.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "FILTER_TYPE_NONE",
        "FILTER_TYPE_ADVERTISER_ID",
        "FILTER_TYPE_CAMPAIGN_ID",
        "FILTER_TYPE_MEDIA_PRODUCT_ID",
        "FILTER_TYPE_INSERTION_ORDER_ID",
        "FILTER_TYPE_LINE_ITEM_ID",
    ]

@typing.type_check_only
class ParentalStatusAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    parentalStatus: typing_extensions.Literal[
        "PARENTAL_STATUS_UNSPECIFIED",
        "PARENTAL_STATUS_PARENT",
        "PARENTAL_STATUS_NOT_A_PARENT",
        "PARENTAL_STATUS_UNKNOWN",
    ]
    targetingOptionId: str

@typing.type_check_only
class ParentalStatusTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    parentalStatus: typing_extensions.Literal[
        "PARENTAL_STATUS_UNSPECIFIED",
        "PARENTAL_STATUS_PARENT",
        "PARENTAL_STATUS_NOT_A_PARENT",
        "PARENTAL_STATUS_UNKNOWN",
    ]

@typing.type_check_only
class Partner(typing_extensions.TypedDict, total=False):
    adServerConfig: PartnerAdServerConfig
    dataAccessConfig: PartnerDataAccessConfig
    displayName: str
    entityStatus: typing_extensions.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    exchangeConfig: ExchangeConfig
    generalConfig: PartnerGeneralConfig
    name: str
    partnerId: str
    updateTime: str

@typing.type_check_only
class PartnerAdServerConfig(typing_extensions.TypedDict, total=False):
    measurementConfig: MeasurementConfig

@typing.type_check_only
class PartnerCost(typing_extensions.TypedDict, total=False):
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
    feeAmount: str
    feePercentageMillis: str
    feeType: typing_extensions.Literal[
        "PARTNER_COST_FEE_TYPE_UNSPECIFIED",
        "PARTNER_COST_FEE_TYPE_CPM_FEE",
        "PARTNER_COST_FEE_TYPE_MEDIA_FEE",
    ]
    invoiceType: typing_extensions.Literal[
        "PARTNER_COST_INVOICE_TYPE_UNSPECIFIED",
        "PARTNER_COST_INVOICE_TYPE_DV360",
        "PARTNER_COST_INVOICE_TYPE_PARTNER",
    ]

@typing.type_check_only
class PartnerDataAccessConfig(typing_extensions.TypedDict, total=False):
    sdfConfig: SdfConfig

@typing.type_check_only
class PartnerGeneralConfig(typing_extensions.TypedDict, total=False):
    currencyCode: str
    timeZone: str

@typing.type_check_only
class PartnerRevenueModel(typing_extensions.TypedDict, total=False):
    markupAmount: str
    markupType: typing_extensions.Literal[
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_CPM",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_MEDIA_COST_MARKUP",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_TOTAL_MEDIA_COST_MARKUP",
    ]

@typing.type_check_only
class PerformanceGoal(typing_extensions.TypedDict, total=False):
    performanceGoalAmountMicros: str
    performanceGoalPercentageMicros: str
    performanceGoalString: str
    performanceGoalType: typing_extensions.Literal[
        "PERFORMANCE_GOAL_TYPE_UNSPECIFIED",
        "PERFORMANCE_GOAL_TYPE_CPM",
        "PERFORMANCE_GOAL_TYPE_CPC",
        "PERFORMANCE_GOAL_TYPE_CPA",
        "PERFORMANCE_GOAL_TYPE_CTR",
        "PERFORMANCE_GOAL_TYPE_VIEWABILITY",
        "PERFORMANCE_GOAL_TYPE_CPIAVC",
        "PERFORMANCE_GOAL_TYPE_CPE",
        "PERFORMANCE_GOAL_TYPE_CLICK_CVR",
        "PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR",
        "PERFORMANCE_GOAL_TYPE_VCPM",
        "PERFORMANCE_GOAL_TYPE_VTR",
        "PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE",
        "PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE",
        "PERFORMANCE_GOAL_TYPE_OTHER",
    ]

@typing.type_check_only
class PerformanceGoalBidStrategy(typing_extensions.TypedDict, total=False):
    customBiddingAlgorithmId: str
    maxAverageCpmBidAmountMicros: str
    performanceGoalAmountMicros: str
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

@typing.type_check_only
class PoiAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    latitude: float
    longitude: float
    proximityRadiusAmount: float
    proximityRadiusUnit: typing_extensions.Literal[
        "DISTANCE_UNIT_UNSPECIFIED", "DISTANCE_UNIT_MILES", "DISTANCE_UNIT_KILOMETERS"
    ]
    targetingOptionId: str

@typing.type_check_only
class PoiSearchTerms(typing_extensions.TypedDict, total=False):
    poiQuery: str

@typing.type_check_only
class PoiTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str
    latitude: float
    longitude: float

@typing.type_check_only
class PrismaConfig(typing_extensions.TypedDict, total=False):
    prismaCpeCode: PrismaCpeCode
    prismaType: typing_extensions.Literal[
        "PRISMA_TYPE_UNSPECIFIED",
        "PRISMA_TYPE_DISPLAY",
        "PRISMA_TYPE_SEARCH",
        "PRISMA_TYPE_VIDEO",
        "PRISMA_TYPE_AUDIO",
        "PRISMA_TYPE_SOCIAL",
        "PRISMA_TYPE_FEE",
    ]
    supplier: str

@typing.type_check_only
class PrismaCpeCode(typing_extensions.TypedDict, total=False):
    prismaClientCode: str
    prismaEstimateCode: str
    prismaProductCode: str

@typing.type_check_only
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

@typing.type_check_only
class PublisherReviewStatus(typing_extensions.TypedDict, total=False):
    publisherName: str
    status: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]

@typing.type_check_only
class RateDetails(typing_extensions.TypedDict, total=False):
    inventorySourceRateType: typing_extensions.Literal[
        "INVENTORY_SOURCE_RATE_TYPE_UNSPECIFIED",
        "INVENTORY_SOURCE_RATE_TYPE_CPM_FIXED",
        "INVENTORY_SOURCE_RATE_TYPE_CPM_FLOOR",
        "INVENTORY_SOURCE_RATE_TYPE_CPD",
        "INVENTORY_SOURCE_RATE_TYPE_FLAT",
    ]
    minimumSpend: Money
    rate: Money
    unitsPurchased: str

@typing.type_check_only
class RegionalLocationListAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    negative: bool
    regionalLocationListId: str

@typing.type_check_only
class ReplaceNegativeKeywordsRequest(typing_extensions.TypedDict, total=False):
    newNegativeKeywords: _list[NegativeKeyword]

@typing.type_check_only
class ReplaceNegativeKeywordsResponse(typing_extensions.TypedDict, total=False):
    negativeKeywords: _list[NegativeKeyword]

@typing.type_check_only
class ReplaceSitesRequest(typing_extensions.TypedDict, total=False):
    advertiserId: str
    newSites: _list[Site]
    partnerId: str

@typing.type_check_only
class ReplaceSitesResponse(typing_extensions.TypedDict, total=False):
    sites: _list[Site]

@typing.type_check_only
class ReviewStatusInfo(typing_extensions.TypedDict, total=False):
    approvalStatus: typing_extensions.Literal[
        "APPROVAL_STATUS_UNSPECIFIED",
        "APPROVAL_STATUS_PENDING_NOT_SERVABLE",
        "APPROVAL_STATUS_PENDING_SERVABLE",
        "APPROVAL_STATUS_APPROVED_SERVABLE",
        "APPROVAL_STATUS_REJECTED_NOT_SERVABLE",
    ]
    contentAndPolicyReviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    creativeAndLandingPageReviewStatus: typing_extensions.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    exchangeReviewStatuses: _list[ExchangeReviewStatus]
    publisherReviewStatuses: _list[PublisherReviewStatus]

@typing.type_check_only
class ScriptError(typing_extensions.TypedDict, total=False):
    column: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED", "SYNTAX_ERROR", "DEPRECATED_SYNTAX", "INTERNAL_ERROR"
    ]
    errorMessage: str
    line: str

@typing.type_check_only
class SdfConfig(typing_extensions.TypedDict, total=False):
    adminEmail: str
    version: typing_extensions.Literal[
        "SDF_VERSION_UNSPECIFIED",
        "SDF_VERSION_3_1",
        "SDF_VERSION_4",
        "SDF_VERSION_4_1",
        "SDF_VERSION_4_2",
        "SDF_VERSION_5",
        "SDF_VERSION_5_1",
        "SDF_VERSION_5_2",
        "SDF_VERSION_5_3",
        "SDF_VERSION_5_4",
        "SDF_VERSION_5_5",
    ]

@typing.type_check_only
class SdfDownloadTask(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class SdfDownloadTaskMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
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
        "SDF_VERSION_5_3",
        "SDF_VERSION_5_4",
        "SDF_VERSION_5_5",
    ]

@typing.type_check_only
class SearchTargetingOptionsRequest(typing_extensions.TypedDict, total=False):
    advertiserId: str
    businessChainSearchTerms: BusinessChainSearchTerms
    geoRegionSearchTerms: GeoRegionSearchTerms
    pageSize: int
    pageToken: str
    poiSearchTerms: PoiSearchTerms

@typing.type_check_only
class SearchTargetingOptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    targetingOptions: _list[TargetingOption]

@typing.type_check_only
class SensitiveCategoryAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    excludedTargetingOptionId: str
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

@typing.type_check_only
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

@typing.type_check_only
class Site(typing_extensions.TypedDict, total=False):
    name: str
    urlOrAppId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SubExchangeAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str

@typing.type_check_only
class SubExchangeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class TargetingExpansionConfig(typing_extensions.TypedDict, total=False):
    excludeFirstPartyAudience: bool
    targetingExpansionLevel: typing_extensions.Literal[
        "TARGETING_EXPANSION_LEVEL_UNSPECIFIED",
        "NO_EXPANSION",
        "LEAST_EXPANSION",
        "SOME_EXPANSION",
        "BALANCED_EXPANSION",
        "MORE_EXPANSION",
        "MOST_EXPANSION",
    ]

@typing.type_check_only
class TargetingOption(typing_extensions.TypedDict, total=False):
    ageRangeDetails: AgeRangeTargetingOptionDetails
    appCategoryDetails: AppCategoryTargetingOptionDetails
    audioContentTypeDetails: AudioContentTypeTargetingOptionDetails
    authorizedSellerStatusDetails: AuthorizedSellerStatusTargetingOptionDetails
    browserDetails: BrowserTargetingOptionDetails
    businessChainDetails: BusinessChainTargetingOptionDetails
    carrierAndIspDetails: CarrierAndIspTargetingOptionDetails
    categoryDetails: CategoryTargetingOptionDetails
    contentDurationDetails: ContentDurationTargetingOptionDetails
    contentGenreDetails: ContentGenreTargetingOptionDetails
    contentInstreamPositionDetails: ContentInstreamPositionTargetingOptionDetails
    contentOutstreamPositionDetails: ContentOutstreamPositionTargetingOptionDetails
    contentStreamTypeDetails: ContentStreamTypeTargetingOptionDetails
    deviceMakeModelDetails: DeviceMakeModelTargetingOptionDetails
    deviceTypeDetails: DeviceTypeTargetingOptionDetails
    digitalContentLabelDetails: DigitalContentLabelTargetingOptionDetails
    environmentDetails: EnvironmentTargetingOptionDetails
    exchangeDetails: ExchangeTargetingOptionDetails
    genderDetails: GenderTargetingOptionDetails
    geoRegionDetails: GeoRegionTargetingOptionDetails
    householdIncomeDetails: HouseholdIncomeTargetingOptionDetails
    languageDetails: LanguageTargetingOptionDetails
    name: str
    nativeContentPositionDetails: NativeContentPositionTargetingOptionDetails
    omidDetails: OmidTargetingOptionDetails
    onScreenPositionDetails: OnScreenPositionTargetingOptionDetails
    operatingSystemDetails: OperatingSystemTargetingOptionDetails
    parentalStatusDetails: ParentalStatusTargetingOptionDetails
    poiDetails: PoiTargetingOptionDetails
    sensitiveCategoryDetails: SensitiveCategoryTargetingOptionDetails
    subExchangeDetails: SubExchangeTargetingOptionDetails
    targetingOptionId: str
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
        "TARGETING_TYPE_POI",
        "TARGETING_TYPE_BUSINESS_CHAIN",
        "TARGETING_TYPE_CONTENT_DURATION",
        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
        "TARGETING_TYPE_OMID",
        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
        "TARGETING_TYPE_CONTENT_GENRE",
    ]
    userRewardedContentDetails: UserRewardedContentTargetingOptionDetails
    videoPlayerSizeDetails: VideoPlayerSizeTargetingOptionDetails
    viewabilityDetails: ViewabilityTargetingOptionDetails

@typing.type_check_only
class ThirdPartyOnlyConfig(typing_extensions.TypedDict, total=False):
    pixelOrderIdReportingEnabled: bool

@typing.type_check_only
class ThirdPartyUrl(typing_extensions.TypedDict, total=False):
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
    url: str

@typing.type_check_only
class ThirdPartyVerifierAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    adloox: Adloox
    doubleVerify: DoubleVerify
    integralAdScience: IntegralAdScience

@typing.type_check_only
class TimeRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TimerEvent(typing_extensions.TypedDict, total=False):
    name: str
    reportingName: str

@typing.type_check_only
class TrackingFloodlightActivityConfig(typing_extensions.TypedDict, total=False):
    floodlightActivityId: str
    postClickLookbackWindowDays: int
    postViewLookbackWindowDays: int

@typing.type_check_only
class Transcode(typing_extensions.TypedDict, total=False):
    audioBitRateKbps: str
    audioSampleRateHz: str
    bitRateKbps: str
    dimensions: Dimensions
    fileSizeBytes: str
    frameRate: float
    mimeType: str
    name: str
    transcoded: bool

@typing.type_check_only
class UniversalAdId(typing_extensions.TypedDict, total=False):
    id: str
    registry: typing_extensions.Literal[
        "UNIVERSAL_AD_REGISTRY_UNSPECIFIED",
        "UNIVERSAL_AD_REGISTRY_OTHER",
        "UNIVERSAL_AD_REGISTRY_AD_ID",
        "UNIVERSAL_AD_REGISTRY_CLEARCAST",
        "UNIVERSAL_AD_REGISTRY_DV360",
        "UNIVERSAL_AD_REGISTRY_CM",
    ]

@typing.type_check_only
class UrlAssignedTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    negative: bool
    url: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    assignedUserRoles: _list[AssignedUserRole]
    displayName: str
    email: str
    name: str
    userId: str

@typing.type_check_only
class UserRewardedContentAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
    userRewardedContent: typing_extensions.Literal[
        "USER_REWARDED_CONTENT_UNSPECIFIED",
        "USER_REWARDED_CONTENT_USER_REWARDED",
        "USER_REWARDED_CONTENT_NOT_USER_REWARDED",
    ]

@typing.type_check_only
class UserRewardedContentTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    userRewardedContent: typing_extensions.Literal[
        "USER_REWARDED_CONTENT_UNSPECIFIED",
        "USER_REWARDED_CONTENT_USER_REWARDED",
        "USER_REWARDED_CONTENT_NOT_USER_REWARDED",
    ]

@typing.type_check_only
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

@typing.type_check_only
class VideoPlayerSizeTargetingOptionDetails(typing_extensions.TypedDict, total=False):
    videoPlayerSize: typing_extensions.Literal[
        "VIDEO_PLAYER_SIZE_UNSPECIFIED",
        "VIDEO_PLAYER_SIZE_SMALL",
        "VIDEO_PLAYER_SIZE_LARGE",
        "VIDEO_PLAYER_SIZE_HD",
        "VIDEO_PLAYER_SIZE_UNKNOWN",
    ]

@typing.type_check_only
class ViewabilityAssignedTargetingOptionDetails(
    typing_extensions.TypedDict, total=False
):
    targetingOptionId: str
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

@typing.type_check_only
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
