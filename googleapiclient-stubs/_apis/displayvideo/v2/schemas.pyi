import typing

_list = list

@typing.type_check_only
class ActivateManualTriggerRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ActiveViewVideoViewabilityMetricConfig(typing.TypedDict, total=False):
    displayName: str
    minimumDuration: typing.Literal[
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
    minimumQuartile: typing.Literal[
        "VIDEO_DURATION_QUARTILE_UNSPECIFIED",
        "VIDEO_DURATION_QUARTILE_NONE",
        "VIDEO_DURATION_QUARTILE_FIRST",
        "VIDEO_DURATION_QUARTILE_SECOND",
        "VIDEO_DURATION_QUARTILE_THIRD",
        "VIDEO_DURATION_QUARTILE_FOURTH",
    ]
    minimumViewability: typing.Literal[
        "VIEWABILITY_PERCENT_UNSPECIFIED",
        "VIEWABILITY_PERCENT_0",
        "VIEWABILITY_PERCENT_25",
        "VIEWABILITY_PERCENT_50",
        "VIEWABILITY_PERCENT_75",
        "VIEWABILITY_PERCENT_100",
    ]
    minimumVolume: typing.Literal[
        "VIDEO_VOLUME_PERCENT_UNSPECIFIED",
        "VIDEO_VOLUME_PERCENT_0",
        "VIDEO_VOLUME_PERCENT_10",
    ]

@typing.type_check_only
class AdUrl(typing.TypedDict, total=False):
    type: typing.Literal[
        "AD_URL_TYPE_UNSPECIFIED",
        "AD_URL_TYPE_BEACON_IMPRESSION",
        "AD_URL_TYPE_BEACON_EXPANDABLE_DCM_IMPRESSION",
        "AD_URL_TYPE_BEACON_CLICK",
        "AD_URL_TYPE_BEACON_SKIP",
    ]
    url: str

@typing.type_check_only
class Adloox(typing.TypedDict, total=False):
    excludedAdlooxCategories: _list[
        typing.Literal[
            "ADLOOX_UNSPECIFIED",
            "ADULT_CONTENT_HARD",
            "ADULT_CONTENT_SOFT",
            "ILLEGAL_CONTENT",
            "BORDERLINE_CONTENT",
            "DISCRIMINATORY_CONTENT",
            "VIOLENT_CONTENT_WEAPONS",
            "LOW_VIEWABILITY_DOMAINS",
            "FRAUD",
        ]
    ]

@typing.type_check_only
class Advertiser(typing.TypedDict, total=False):
    adServerConfig: AdvertiserAdServerConfig
    advertiserId: str
    containsEuPoliticalAds: typing.Literal[
        "EU_POLITICAL_ADVERTISING_STATUS_UNKNOWN",
        "CONTAINS_EU_POLITICAL_ADVERTISING",
        "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    ]
    creativeConfig: AdvertiserCreativeConfig
    dataAccessConfig: AdvertiserDataAccessConfig
    defaultBusinessName: str
    defaultLogoAssetId: str
    displayName: str
    entityStatus: typing.Literal[
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
class AdvertiserAdServerConfig(typing.TypedDict, total=False):
    cmHybridConfig: CmHybridConfig
    thirdPartyOnlyConfig: ThirdPartyOnlyConfig

@typing.type_check_only
class AdvertiserCreativeConfig(typing.TypedDict, total=False):
    dynamicCreativeEnabled: bool
    iasClientId: str
    obaComplianceDisabled: bool
    videoCreativeDataSharingAuthorized: bool

@typing.type_check_only
class AdvertiserDataAccessConfig(typing.TypedDict, total=False):
    sdfConfig: AdvertiserSdfConfig

@typing.type_check_only
class AdvertiserGeneralConfig(typing.TypedDict, total=False):
    currencyCode: str
    domainUrl: str
    timeZone: str

@typing.type_check_only
class AdvertiserSdfConfig(typing.TypedDict, total=False):
    overridePartnerSdfConfig: bool
    sdfConfig: SdfConfig

@typing.type_check_only
class AdvertiserTargetingConfig(typing.TypedDict, total=False):
    exemptTvFromViewabilityTargeting: bool

@typing.type_check_only
class AgeRangeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    ageRange: typing.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_PLUS",
        "AGE_RANGE_UNKNOWN",
        "AGE_RANGE_18_20",
        "AGE_RANGE_21_24",
        "AGE_RANGE_25_29",
        "AGE_RANGE_30_34",
        "AGE_RANGE_35_39",
        "AGE_RANGE_40_44",
        "AGE_RANGE_45_49",
        "AGE_RANGE_50_54",
        "AGE_RANGE_55_59",
        "AGE_RANGE_60_64",
    ]

@typing.type_check_only
class AgeRangeTargetingOptionDetails(typing.TypedDict, total=False):
    ageRange: typing.Literal[
        "AGE_RANGE_UNSPECIFIED",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_PLUS",
        "AGE_RANGE_UNKNOWN",
        "AGE_RANGE_18_20",
        "AGE_RANGE_21_24",
        "AGE_RANGE_25_29",
        "AGE_RANGE_30_34",
        "AGE_RANGE_35_39",
        "AGE_RANGE_40_44",
        "AGE_RANGE_45_49",
        "AGE_RANGE_50_54",
        "AGE_RANGE_55_59",
        "AGE_RANGE_60_64",
    ]

@typing.type_check_only
class AppAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    appId: str
    appPlatform: typing.Literal[
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
        "APP_PLATFORM_LG_TV",
        "APP_PLATFORM_VIZIO_TV",
        "APP_PLATFORM_VIDAA",
    ]
    displayName: str
    negative: bool

@typing.type_check_only
class AppCategoryAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class AppCategoryTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Asset(typing.TypedDict, total=False):
    content: str
    mediaId: str

@typing.type_check_only
class AssetAssociation(typing.TypedDict, total=False):
    asset: Asset
    role: typing.Literal[
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
        "ASSET_ROLE_BACKGROUND_COLOR",
        "ASSET_ROLE_ACCENT_COLOR",
        "ASSET_ROLE_REQUIRE_LOGO",
        "ASSET_ROLE_REQUIRE_IMAGE",
        "ASSET_ROLE_ENABLE_ASSET_ENHANCEMENTS",
    ]

@typing.type_check_only
class AssignedInventorySource(typing.TypedDict, total=False):
    assignedInventorySourceId: str
    inventorySourceId: str
    name: str

@typing.type_check_only
class AssignedLocation(typing.TypedDict, total=False):
    assignedLocationId: str
    name: str
    targetingOptionId: str

@typing.type_check_only
class AssignedTargetingOption(typing.TypedDict, total=False):
    ageRangeDetails: AgeRangeAssignedTargetingOptionDetails
    appCategoryDetails: AppCategoryAssignedTargetingOptionDetails
    appDetails: AppAssignedTargetingOptionDetails
    assignedTargetingOptionId: str
    assignedTargetingOptionIdAlias: str
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
    contentInstreamPositionDetails: (
        ContentInstreamPositionAssignedTargetingOptionDetails
    )
    contentOutstreamPositionDetails: (
        ContentOutstreamPositionAssignedTargetingOptionDetails
    )
    contentStreamTypeDetails: ContentStreamTypeAssignedTargetingOptionDetails
    dayAndTimeDetails: DayAndTimeAssignedTargetingOptionDetails
    deviceMakeModelDetails: DeviceMakeModelAssignedTargetingOptionDetails
    deviceTypeDetails: DeviceTypeAssignedTargetingOptionDetails
    digitalContentLabelExclusionDetails: (
        DigitalContentLabelAssignedTargetingOptionDetails
    )
    environmentDetails: EnvironmentAssignedTargetingOptionDetails
    exchangeDetails: ExchangeAssignedTargetingOptionDetails
    genderDetails: GenderAssignedTargetingOptionDetails
    geoRegionDetails: GeoRegionAssignedTargetingOptionDetails
    householdIncomeDetails: HouseholdIncomeAssignedTargetingOptionDetails
    inheritance: typing.Literal[
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
    sessionPositionDetails: SessionPositionAssignedTargetingOptionDetails
    subExchangeDetails: SubExchangeAssignedTargetingOptionDetails
    targetingType: typing.Literal[
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
        "TARGETING_TYPE_YOUTUBE_VIDEO",
        "TARGETING_TYPE_YOUTUBE_CHANNEL",
        "TARGETING_TYPE_SESSION_POSITION",
        "TARGETING_TYPE_YOUTUBE_CHANNEL_PACK",
    ]
    thirdPartyVerifierDetails: ThirdPartyVerifierAssignedTargetingOptionDetails
    urlDetails: UrlAssignedTargetingOptionDetails
    userRewardedContentDetails: UserRewardedContentAssignedTargetingOptionDetails
    videoPlayerSizeDetails: VideoPlayerSizeAssignedTargetingOptionDetails
    viewabilityDetails: ViewabilityAssignedTargetingOptionDetails
    youtubeChannelDetails: YoutubeChannelAssignedTargetingOptionDetails
    youtubeChannelPackDetails: YoutubeChannelPackAssignedTargetingOptionDetails
    youtubeVideoDetails: YoutubeVideoAssignedTargetingOptionDetails

@typing.type_check_only
class AssignedUserRole(typing.TypedDict, total=False):
    advertiserId: str
    assignedUserRoleId: str
    partnerId: str
    userRole: typing.Literal[
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
class AudienceGroupAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    excludedGoogleAudienceGroup: GoogleAudienceGroup
    includedCombinedAudienceGroup: CombinedAudienceGroup
    includedCustomListGroup: CustomListGroup
    includedGoogleAudienceGroup: GoogleAudienceGroup

@typing.type_check_only
class AudioAd(typing.TypedDict, total=False):
    displayUrl: str
    finalUrl: str
    trackingUrl: str
    video: YoutubeVideoDetails

@typing.type_check_only
class AudioContentTypeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    audioContentType: typing.Literal[
        "AUDIO_CONTENT_TYPE_UNSPECIFIED",
        "AUDIO_CONTENT_TYPE_UNKNOWN",
        "AUDIO_CONTENT_TYPE_MUSIC",
        "AUDIO_CONTENT_TYPE_BROADCAST",
        "AUDIO_CONTENT_TYPE_PODCAST",
        "AUDIO_CONTENT_TYPE_CATCH_UP_RADIO",
        "AUDIO_CONTENT_TYPE_WEB_RADIO",
        "AUDIO_CONTENT_TYPE_VIDEO_GAME",
        "AUDIO_CONTENT_TYPE_TEXT_TO_SPEECH",
    ]

@typing.type_check_only
class AudioContentTypeTargetingOptionDetails(typing.TypedDict, total=False):
    audioContentType: typing.Literal[
        "AUDIO_CONTENT_TYPE_UNSPECIFIED",
        "AUDIO_CONTENT_TYPE_UNKNOWN",
        "AUDIO_CONTENT_TYPE_MUSIC",
        "AUDIO_CONTENT_TYPE_BROADCAST",
        "AUDIO_CONTENT_TYPE_PODCAST",
        "AUDIO_CONTENT_TYPE_CATCH_UP_RADIO",
        "AUDIO_CONTENT_TYPE_WEB_RADIO",
        "AUDIO_CONTENT_TYPE_VIDEO_GAME",
        "AUDIO_CONTENT_TYPE_TEXT_TO_SPEECH",
    ]

@typing.type_check_only
class AudioVideoOffset(typing.TypedDict, total=False):
    percentage: str
    seconds: str

@typing.type_check_only
class AuditAdvertiserResponse(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    authorizedSellerStatus: typing.Literal[
        "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS",
    ]
    targetingOptionId: str

@typing.type_check_only
class AuthorizedSellerStatusTargetingOptionDetails(typing.TypedDict, total=False):
    authorizedSellerStatus: typing.Literal[
        "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_DIRECT_SELLERS_ONLY",
        "AUTHORIZED_SELLER_STATUS_AUTHORIZED_AND_NON_PARTICIPATING_PUBLISHERS",
    ]

@typing.type_check_only
class BiddingStrategy(typing.TypedDict, total=False):
    demandGenBid: DemandGenBiddingStrategy
    fixedBid: FixedBidStrategy
    maximizeSpendAutoBid: MaximizeSpendBidStrategy
    performanceGoalAutoBid: PerformanceGoalBidStrategy

@typing.type_check_only
class BrowserAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class BrowserTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class BudgetSummary(typing.TypedDict, total=False):
    externalBudgetId: str
    preTaxAmountMicros: str
    prismaCpeCode: PrismaCpeCode
    taxAmountMicros: str
    totalAmountMicros: str

@typing.type_check_only
class BulkEditAdvertiserAssignedTargetingOptionsRequest(typing.TypedDict, total=False):
    createRequests: _list[CreateAssignedTargetingOptionsRequest]
    deleteRequests: _list[DeleteAssignedTargetingOptionsRequest]

@typing.type_check_only
class BulkEditAdvertiserAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    createdAssignedTargetingOptions: _list[AssignedTargetingOption]

@typing.type_check_only
class BulkEditAssignedInventorySourcesRequest(typing.TypedDict, total=False):
    advertiserId: str
    createdAssignedInventorySources: _list[AssignedInventorySource]
    deletedAssignedInventorySources: _list[str]
    partnerId: str

@typing.type_check_only
class BulkEditAssignedInventorySourcesResponse(typing.TypedDict, total=False):
    assignedInventorySources: _list[AssignedInventorySource]

@typing.type_check_only
class BulkEditAssignedLocationsRequest(typing.TypedDict, total=False):
    createdAssignedLocations: _list[AssignedLocation]
    deletedAssignedLocations: _list[str]

@typing.type_check_only
class BulkEditAssignedLocationsResponse(typing.TypedDict, total=False):
    assignedLocations: _list[AssignedLocation]

@typing.type_check_only
class BulkEditAssignedTargetingOptionsRequest(typing.TypedDict, total=False):
    createRequests: _list[CreateAssignedTargetingOptionsRequest]
    deleteRequests: _list[DeleteAssignedTargetingOptionsRequest]
    lineItemIds: _list[str]

@typing.type_check_only
class BulkEditAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    errors: _list[Status]
    failedLineItemIds: _list[str]
    updatedLineItemIds: _list[str]

@typing.type_check_only
class BulkEditAssignedUserRolesRequest(typing.TypedDict, total=False):
    createdAssignedUserRoles: _list[AssignedUserRole]
    deletedAssignedUserRoles: _list[str]

@typing.type_check_only
class BulkEditAssignedUserRolesResponse(typing.TypedDict, total=False):
    createdAssignedUserRoles: _list[AssignedUserRole]

@typing.type_check_only
class BulkEditNegativeKeywordsRequest(typing.TypedDict, total=False):
    createdNegativeKeywords: _list[NegativeKeyword]
    deletedNegativeKeywords: _list[str]

@typing.type_check_only
class BulkEditNegativeKeywordsResponse(typing.TypedDict, total=False):
    negativeKeywords: _list[NegativeKeyword]

@typing.type_check_only
class BulkEditPartnerAssignedTargetingOptionsRequest(typing.TypedDict, total=False):
    createRequests: _list[CreateAssignedTargetingOptionsRequest]
    deleteRequests: _list[DeleteAssignedTargetingOptionsRequest]

@typing.type_check_only
class BulkEditPartnerAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    createdAssignedTargetingOptions: _list[AssignedTargetingOption]

@typing.type_check_only
class BulkEditSitesRequest(typing.TypedDict, total=False):
    advertiserId: str
    createdSites: _list[Site]
    deletedSites: _list[str]
    partnerId: str

@typing.type_check_only
class BulkEditSitesResponse(typing.TypedDict, total=False):
    sites: _list[Site]

@typing.type_check_only
class BulkListAdGroupAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    youtubeAdGroupAssignedTargetingOptions: _list[YoutubeAdGroupAssignedTargetingOption]

@typing.type_check_only
class BulkListAdvertiserAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class BulkListAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    lineItemAssignedTargetingOptions: _list[LineItemAssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class BulkUpdateLineItemsRequest(typing.TypedDict, total=False):
    lineItemIds: _list[str]
    targetLineItem: LineItem
    updateMask: str

@typing.type_check_only
class BulkUpdateLineItemsResponse(typing.TypedDict, total=False):
    errors: _list[Status]
    failedLineItemIds: _list[str]
    skippedLineItemIds: _list[str]
    updatedLineItemIds: _list[str]

@typing.type_check_only
class BumperAd(typing.TypedDict, total=False):
    commonInStreamAttribute: CommonInStreamAttribute

@typing.type_check_only
class BusinessChainAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    proximityRadiusAmount: float
    proximityRadiusUnit: typing.Literal[
        "DISTANCE_UNIT_UNSPECIFIED", "DISTANCE_UNIT_MILES", "DISTANCE_UNIT_KILOMETERS"
    ]
    targetingOptionId: str

@typing.type_check_only
class BusinessChainSearchTerms(typing.TypedDict, total=False):
    businessChainQuery: str
    regionQuery: str

@typing.type_check_only
class BusinessChainTargetingOptionDetails(typing.TypedDict, total=False):
    businessChain: str
    geoRegion: str
    geoRegionType: typing.Literal[
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
        "GEO_REGION_TYPE_NATIONAL_PARK",
        "GEO_REGION_TYPE_BARRIO",
        "GEO_REGION_TYPE_SUB_WARD",
        "GEO_REGION_TYPE_MUNICIPALITY_DISTRICT",
        "GEO_REGION_TYPE_SUB_DISTRICT",
        "GEO_REGION_TYPE_QUARTER",
        "GEO_REGION_TYPE_DIVISION",
        "GEO_REGION_TYPE_COMMUNE",
        "GEO_REGION_TYPE_COLLOQUIAL_AREA",
        "GEO_REGION_TYPE_POST_TOWN",
        "GEO_REGION_TYPE_WARD",
        "GEO_REGION_TYPE_TOWN",
        "GEO_REGION_TYPE_VILLAGE",
        "GEO_REGION_TYPE_CITY_DISTRICT",
        "GEO_REGION_TYPE_SUBURB",
        "GEO_REGION_TYPE_HAMLET",
        "GEO_REGION_TYPE_MUNICIPAL_DISTRICT",
        "GEO_REGION_TYPE_COMMUNITY",
        "GEO_REGION_TYPE_TOWNSHIP",
        "GEO_REGION_TYPE_URBAN_DISTRICT",
        "GEO_REGION_TYPE_RESIDENTIAL_AREA",
        "GEO_REGION_TYPE_INDEPENDENT_CITY",
        "GEO_REGION_TYPE_SECTOR",
        "GEO_REGION_TYPE_AREA",
        "GEO_REGION_TYPE_ESTATE",
        "GEO_REGION_TYPE_PARISH",
        "GEO_REGION_TYPE_SETTLEMENT",
        "GEO_REGION_TYPE_ZONE",
        "GEO_REGION_TYPE_COLONY",
        "GEO_REGION_TYPE_INDUSTRIAL_AREA",
        "GEO_REGION_TYPE_PROVINCIAL_CITY",
        "GEO_REGION_TYPE_RURAL_DISTRICT",
    ]

@typing.type_check_only
class Campaign(typing.TypedDict, total=False):
    advertiserId: str
    campaignBudgets: _list[CampaignBudget]
    campaignFlight: CampaignFlight
    campaignGoal: CampaignGoal
    campaignId: str
    displayName: str
    entityStatus: typing.Literal[
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
class CampaignBudget(typing.TypedDict, total=False):
    budgetAmountMicros: str
    budgetId: str
    budgetUnit: typing.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]
    dateRange: DateRange
    displayName: str
    externalBudgetId: str
    externalBudgetSource: typing.Literal[
        "EXTERNAL_BUDGET_SOURCE_UNSPECIFIED",
        "EXTERNAL_BUDGET_SOURCE_NONE",
        "EXTERNAL_BUDGET_SOURCE_MEDIA_OCEAN",
    ]
    invoiceGroupingId: str
    prismaConfig: PrismaConfig

@typing.type_check_only
class CampaignFlight(typing.TypedDict, total=False):
    plannedDates: DateRange
    plannedSpendAmountMicros: str

@typing.type_check_only
class CampaignGoal(typing.TypedDict, total=False):
    campaignGoalType: typing.Literal[
        "CAMPAIGN_GOAL_TYPE_UNSPECIFIED",
        "CAMPAIGN_GOAL_TYPE_APP_INSTALL",
        "CAMPAIGN_GOAL_TYPE_BRAND_AWARENESS",
        "CAMPAIGN_GOAL_TYPE_OFFLINE_ACTION",
        "CAMPAIGN_GOAL_TYPE_ONLINE_ACTION",
    ]
    performanceGoal: PerformanceGoal

@typing.type_check_only
class CarrierAndIspAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class CarrierAndIspTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    type: typing.Literal[
        "CARRIER_AND_ISP_TYPE_UNSPECIFIED",
        "CARRIER_AND_ISP_TYPE_ISP",
        "CARRIER_AND_ISP_TYPE_CARRIER",
    ]

@typing.type_check_only
class CategoryAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class CategoryTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Channel(typing.TypedDict, total=False):
    advertiserId: str
    channelId: str
    displayName: str
    name: str
    negativelyTargetedLineItemCount: str
    partnerId: str
    positivelyTargetedLineItemCount: str

@typing.type_check_only
class ChannelAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    channelId: str
    negative: bool

@typing.type_check_only
class CmHybridConfig(typing.TypedDict, total=False):
    cmAccountId: str
    cmAdvertiserIds: _list[str]
    cmFloodlightConfigId: str
    cmFloodlightLinkingAuthorized: bool
    cmSyncableSiteIds: _list[str]
    dv360ToCmCostReportingEnabled: bool
    dv360ToCmDataSharingEnabled: bool

@typing.type_check_only
class CmTrackingAd(typing.TypedDict, total=False):
    cmAdId: str
    cmCreativeId: str
    cmPlacementId: str

@typing.type_check_only
class CombinedAudience(typing.TypedDict, total=False):
    combinedAudienceId: str
    displayName: str
    name: str

@typing.type_check_only
class CombinedAudienceGroup(typing.TypedDict, total=False):
    settings: _list[CombinedAudienceTargetingSetting]

@typing.type_check_only
class CombinedAudienceTargetingSetting(typing.TypedDict, total=False):
    combinedAudienceId: str

@typing.type_check_only
class CommonInStreamAttribute(typing.TypedDict, total=False):
    actionButtonLabel: str
    actionHeadline: str
    companionBanner: ImageAsset
    displayUrl: str
    finalUrl: str
    trackingUrl: str
    video: YoutubeVideoDetails

@typing.type_check_only
class ContentDurationAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    contentDuration: typing.Literal[
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
class ContentDurationTargetingOptionDetails(typing.TypedDict, total=False):
    contentDuration: typing.Literal[
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
class ContentGenreAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class ContentGenreTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class ContentInstreamPositionAssignedTargetingOptionDetails(
    typing.TypedDict, total=False
):
    adType: typing.Literal[
        "AD_TYPE_UNSPECIFIED", "AD_TYPE_DISPLAY", "AD_TYPE_VIDEO", "AD_TYPE_AUDIO"
    ]
    contentInstreamPosition: typing.Literal[
        "CONTENT_INSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_INSTREAM_POSITION_PRE_ROLL",
        "CONTENT_INSTREAM_POSITION_MID_ROLL",
        "CONTENT_INSTREAM_POSITION_POST_ROLL",
        "CONTENT_INSTREAM_POSITION_UNKNOWN",
    ]

@typing.type_check_only
class ContentInstreamPositionTargetingOptionDetails(typing.TypedDict, total=False):
    contentInstreamPosition: typing.Literal[
        "CONTENT_INSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_INSTREAM_POSITION_PRE_ROLL",
        "CONTENT_INSTREAM_POSITION_MID_ROLL",
        "CONTENT_INSTREAM_POSITION_POST_ROLL",
        "CONTENT_INSTREAM_POSITION_UNKNOWN",
    ]

@typing.type_check_only
class ContentOutstreamPositionAssignedTargetingOptionDetails(
    typing.TypedDict, total=False
):
    adType: typing.Literal[
        "AD_TYPE_UNSPECIFIED", "AD_TYPE_DISPLAY", "AD_TYPE_VIDEO", "AD_TYPE_AUDIO"
    ]
    contentOutstreamPosition: typing.Literal[
        "CONTENT_OUTSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_OUTSTREAM_POSITION_UNKNOWN",
        "CONTENT_OUTSTREAM_POSITION_IN_ARTICLE",
        "CONTENT_OUTSTREAM_POSITION_IN_BANNER",
        "CONTENT_OUTSTREAM_POSITION_IN_FEED",
        "CONTENT_OUTSTREAM_POSITION_INTERSTITIAL",
    ]

@typing.type_check_only
class ContentOutstreamPositionTargetingOptionDetails(typing.TypedDict, total=False):
    contentOutstreamPosition: typing.Literal[
        "CONTENT_OUTSTREAM_POSITION_UNSPECIFIED",
        "CONTENT_OUTSTREAM_POSITION_UNKNOWN",
        "CONTENT_OUTSTREAM_POSITION_IN_ARTICLE",
        "CONTENT_OUTSTREAM_POSITION_IN_BANNER",
        "CONTENT_OUTSTREAM_POSITION_IN_FEED",
        "CONTENT_OUTSTREAM_POSITION_INTERSTITIAL",
    ]

@typing.type_check_only
class ContentStreamTypeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    contentStreamType: typing.Literal[
        "CONTENT_STREAM_TYPE_UNSPECIFIED", "CONTENT_LIVE_STREAM", "CONTENT_ON_DEMAND"
    ]
    targetingOptionId: str

@typing.type_check_only
class ContentStreamTypeTargetingOptionDetails(typing.TypedDict, total=False):
    contentStreamType: typing.Literal[
        "CONTENT_STREAM_TYPE_UNSPECIFIED", "CONTENT_LIVE_STREAM", "CONTENT_ON_DEMAND"
    ]

@typing.type_check_only
class ConversionCountingConfig(typing.TypedDict, total=False):
    floodlightActivityConfigs: _list[TrackingFloodlightActivityConfig]
    postViewCountPercentageMillis: str
    primaryAttributionModelId: str

@typing.type_check_only
class CounterEvent(typing.TypedDict, total=False):
    name: str
    reportingName: str

@typing.type_check_only
class CreateAssetRequest(typing.TypedDict, total=False):
    filename: str

@typing.type_check_only
class CreateAssetResponse(typing.TypedDict, total=False):
    asset: Asset

@typing.type_check_only
class CreateAssignedTargetingOptionsRequest(typing.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    targetingType: typing.Literal[
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
        "TARGETING_TYPE_YOUTUBE_VIDEO",
        "TARGETING_TYPE_YOUTUBE_CHANNEL",
        "TARGETING_TYPE_SESSION_POSITION",
        "TARGETING_TYPE_YOUTUBE_CHANNEL_PACK",
    ]

@typing.type_check_only
class CreateSdfDownloadTaskRequest(typing.TypedDict, total=False):
    advertiserId: str
    idFilter: IdFilter
    inventorySourceFilter: InventorySourceFilter
    parentEntityFilter: ParentEntityFilter
    partnerId: str
    version: typing.Literal[
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
        "SDF_VERSION_6",
        "SDF_VERSION_7",
        "SDF_VERSION_7_1",
        "SDF_VERSION_8",
        "SDF_VERSION_8_1",
        "SDF_VERSION_9",
        "SDF_VERSION_9_1",
        "SDF_VERSION_9_2",
        "SDF_VERSION_10",
        "SDF_VERSION_10_1",
    ]

@typing.type_check_only
class Creative(typing.TypedDict, total=False):
    additionalDimensions: _list[Dimensions]
    advertiserId: str
    appendedTag: str
    assets: _list[AssetAssociation]
    cmPlacementId: str
    cmTrackingAd: CmTrackingAd
    companionCreativeIds: _list[str]
    counterEvents: _list[CounterEvent]
    createTime: str
    creativeAttributes: _list[
        typing.Literal[
            "CREATIVE_ATTRIBUTE_UNSPECIFIED",
            "CREATIVE_ATTRIBUTE_VAST",
            "CREATIVE_ATTRIBUTE_VPAID_LINEAR",
            "CREATIVE_ATTRIBUTE_VPAID_NON_LINEAR",
        ]
    ]
    creativeId: str
    creativeType: typing.Literal[
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
        "CREATIVE_TYPE_ASSET_BASED_CREATIVE",
    ]
    dimensions: Dimensions
    displayName: str
    dynamic: bool
    entityStatus: typing.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    exitEvents: _list[ExitEvent]
    expandOnHover: bool
    expandingDirection: typing.Literal[
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
    hostingSource: typing.Literal[
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
    syntheticContentAttestationStatus: typing.Literal[
        "SYNTHETIC_CONTENT_ATTESTATION_STATUS_UNSPECIFIED",
        "NOT_SYNTHETIC",
        "IS_SYNTHETIC",
    ]
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
class CustomBiddingAlgorithm(typing.TypedDict, total=False):
    advertiserId: str
    customBiddingAlgorithmId: str
    customBiddingAlgorithmType: typing.Literal[
        "CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED", "SCRIPT_BASED"
    ]
    displayName: str
    entityStatus: typing.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    modelDetails: _list[CustomBiddingModelDetails]
    name: str
    partnerId: str
    sharedAdvertiserIds: _list[str]

@typing.type_check_only
class CustomBiddingModelDetails(typing.TypedDict, total=False):
    advertiserId: str
    readinessState: typing.Literal[
        "READINESS_STATE_UNSPECIFIED",
        "READINESS_STATE_ACTIVE",
        "READINESS_STATE_INSUFFICIENT_DATA",
        "READINESS_STATE_TRAINING",
        "READINESS_STATE_NO_VALID_SCRIPT",
    ]
    suspensionState: typing.Literal[
        "SUSPENSION_STATE_UNSPECIFIED",
        "SUSPENSION_STATE_ENABLED",
        "SUSPENSION_STATE_DORMANT",
        "SUSPENSION_STATE_SUSPENDED",
    ]

@typing.type_check_only
class CustomBiddingScript(typing.TypedDict, total=False):
    active: bool
    createTime: str
    customBiddingAlgorithmId: str
    customBiddingScriptId: str
    errors: _list[ScriptError]
    name: str
    script: CustomBiddingScriptRef
    state: typing.Literal["STATE_UNSPECIFIED", "ACCEPTED", "REJECTED", "PENDING"]

@typing.type_check_only
class CustomBiddingScriptRef(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class CustomLabel(typing.TypedDict, total=False):
    key: typing.Literal[
        "CUSTOM_LABEL_KEY_UNSPECIFIED",
        "CUSTOM_LABEL_KEY_0",
        "CUSTOM_LABEL_KEY_1",
        "CUSTOM_LABEL_KEY_2",
        "CUSTOM_LABEL_KEY_3",
        "CUSTOM_LABEL_KEY_4",
    ]
    value: str

@typing.type_check_only
class CustomList(typing.TypedDict, total=False):
    customListId: str
    displayName: str
    name: str

@typing.type_check_only
class CustomListGroup(typing.TypedDict, total=False):
    settings: _list[CustomListTargetingSetting]

@typing.type_check_only
class CustomListTargetingSetting(typing.TypedDict, total=False):
    customListId: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class DayAndTimeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
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
    endHour: int
    startHour: int
    timeZoneResolution: typing.Literal[
        "TIME_ZONE_RESOLUTION_UNSPECIFIED",
        "TIME_ZONE_RESOLUTION_END_USER",
        "TIME_ZONE_RESOLUTION_ADVERTISER",
    ]

@typing.type_check_only
class DeactivateManualTriggerRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteAssignedTargetingOptionsRequest(typing.TypedDict, total=False):
    assignedTargetingOptionIds: _list[str]
    targetingType: typing.Literal[
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
        "TARGETING_TYPE_YOUTUBE_VIDEO",
        "TARGETING_TYPE_YOUTUBE_CHANNEL",
        "TARGETING_TYPE_SESSION_POSITION",
        "TARGETING_TYPE_YOUTUBE_CHANNEL_PACK",
    ]

@typing.type_check_only
class DemandGenBiddingStrategy(typing.TypedDict, total=False):
    effectiveBiddingValue: str
    effectiveBiddingValueSource: typing.Literal[
        "BIDDING_SOURCE_UNSPECIFIED",
        "BIDDING_SOURCE_LINE_ITEM",
        "BIDDING_SOURCE_AD_GROUP",
    ]
    type: typing.Literal[
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_UNSPECIFIED",
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_TARGET_CPA",
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_TARGET_ROAS",
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSIONS",
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSION_VALUE",
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_MAXIMIZE_CLICKS",
        "DEMAND_GEN_BIDDING_STRATEGY_TYPE_TARGET_CPC",
    ]
    value: str

@typing.type_check_only
class DemandGenSettings(typing.TypedDict, total=False):
    geoLanguageTargetingEnabled: bool
    linkedMerchantId: str
    thirdPartyMeasurementConfigs: ThirdPartyMeasurementConfigs

@typing.type_check_only
class DeviceMakeModelAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class DeviceMakeModelTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class DeviceTypeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    deviceType: typing.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "DEVICE_TYPE_COMPUTER",
        "DEVICE_TYPE_CONNECTED_TV",
        "DEVICE_TYPE_SMART_PHONE",
        "DEVICE_TYPE_TABLET",
        "DEVICE_TYPE_CONNECTED_DEVICE",
    ]
    youtubeAndPartnersBidMultiplier: float

@typing.type_check_only
class DeviceTypeTargetingOptionDetails(typing.TypedDict, total=False):
    deviceType: typing.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "DEVICE_TYPE_COMPUTER",
        "DEVICE_TYPE_CONNECTED_TV",
        "DEVICE_TYPE_SMART_PHONE",
        "DEVICE_TYPE_TABLET",
        "DEVICE_TYPE_CONNECTED_DEVICE",
    ]

@typing.type_check_only
class DigitalContentLabelAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    excludedContentRatingTier: typing.Literal[
        "CONTENT_RATING_TIER_UNSPECIFIED",
        "CONTENT_RATING_TIER_UNRATED",
        "CONTENT_RATING_TIER_GENERAL",
        "CONTENT_RATING_TIER_PARENTAL_GUIDANCE",
        "CONTENT_RATING_TIER_TEENS",
        "CONTENT_RATING_TIER_MATURE",
        "CONTENT_RATING_TIER_FAMILIES",
    ]

@typing.type_check_only
class DigitalContentLabelTargetingOptionDetails(typing.TypedDict, total=False):
    contentRatingTier: typing.Literal[
        "CONTENT_RATING_TIER_UNSPECIFIED",
        "CONTENT_RATING_TIER_UNRATED",
        "CONTENT_RATING_TIER_GENERAL",
        "CONTENT_RATING_TIER_PARENTAL_GUIDANCE",
        "CONTENT_RATING_TIER_TEENS",
        "CONTENT_RATING_TIER_MATURE",
        "CONTENT_RATING_TIER_FAMILIES",
    ]

@typing.type_check_only
class Dimensions(typing.TypedDict, total=False):
    heightPixels: int
    widthPixels: int

@typing.type_check_only
class DisplayVideoSourceAd(typing.TypedDict, total=False):
    creativeId: str

@typing.type_check_only
class DoubleVerify(typing.TypedDict, total=False):
    appStarRating: DoubleVerifyAppStarRating
    avoidedAgeRatings: _list[
        typing.Literal[
            "AGE_RATING_UNSPECIFIED",
            "APP_AGE_RATE_UNKNOWN",
            "APP_AGE_RATE_4_PLUS",
            "APP_AGE_RATE_9_PLUS",
            "APP_AGE_RATE_12_PLUS",
            "APP_AGE_RATE_17_PLUS",
            "APP_AGE_RATE_18_PLUS",
        ]
    ]
    brandSafetyCategories: DoubleVerifyBrandSafetyCategories
    customSegmentId: str
    displayViewability: DoubleVerifyDisplayViewability
    fraudInvalidTraffic: DoubleVerifyFraudInvalidTraffic
    videoViewability: DoubleVerifyVideoViewability

@typing.type_check_only
class DoubleVerifyAppStarRating(typing.TypedDict, total=False):
    avoidInsufficientStarRating: bool
    avoidedStarRating: typing.Literal[
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
class DoubleVerifyBrandSafetyCategories(typing.TypedDict, total=False):
    avoidUnknownBrandSafetyCategory: bool
    avoidedHighSeverityCategories: _list[
        typing.Literal[
            "HIGHER_SEVERITY_UNSPECIFIED",
            "ADULT_CONTENT_PORNOGRAPHY",
            "COPYRIGHT_INFRINGEMENT",
            "SUBSTANCE_ABUSE",
            "GRAPHIC_VIOLENCE_WEAPONS",
            "HATE_PROFANITY",
            "CRIMINAL_SKILLS",
            "NUISANCE_INCENTIVIZED_MALWARE_CLUTTER",
        ]
    ]
    avoidedMediumSeverityCategories: _list[
        typing.Literal[
            "MEDIUM_SEVERITY_UNSPECIFIED",
            "AD_SERVERS",
            "ADULT_CONTENT_SWIMSUIT",
            "ALTERNATIVE_LIFESTYLES",
            "CELEBRITY_GOSSIP",
            "GAMBLING",
            "OCCULT",
            "SEX_EDUCATION",
            "DISASTER_AVIATION",
            "DISASTER_MAN_MADE",
            "DISASTER_NATURAL",
            "DISASTER_TERRORIST_EVENTS",
            "DISASTER_VEHICLE",
            "ALCOHOL",
            "SMOKING",
            "NEGATIVE_NEWS_FINANCIAL",
            "NON_ENGLISH",
            "PARKING_PAGE",
            "UNMODERATED_UGC",
            "INFLAMMATORY_POLITICS_AND_NEWS",
            "NEGATIVE_NEWS_PHARMACEUTICAL",
        ]
    ]

@typing.type_check_only
class DoubleVerifyDisplayViewability(typing.TypedDict, total=False):
    iab: typing.Literal[
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
    viewableDuring: typing.Literal[
        "AVERAGE_VIEW_DURATION_UNSPECIFIED",
        "AVERAGE_VIEW_DURATION_5_SEC",
        "AVERAGE_VIEW_DURATION_10_SEC",
        "AVERAGE_VIEW_DURATION_15_SEC",
    ]

@typing.type_check_only
class DoubleVerifyFraudInvalidTraffic(typing.TypedDict, total=False):
    avoidInsufficientOption: bool
    avoidedFraudOption: typing.Literal[
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
class DoubleVerifyVideoViewability(typing.TypedDict, total=False):
    playerImpressionRate: typing.Literal[
        "PLAYER_SIZE_400X300_UNSPECIFIED",
        "PLAYER_SIZE_400X300_95",
        "PLAYER_SIZE_400X300_70",
        "PLAYER_SIZE_400X300_25",
        "PLAYER_SIZE_400X300_5",
    ]
    videoIab: typing.Literal[
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
    videoViewableRate: typing.Literal[
        "VIDEO_VIEWABLE_RATE_UNSPECIFIED",
        "VIEWED_PERFORMANCE_40_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_35_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_30_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_25_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_20_PERCENT_HIGHER",
        "VIEWED_PERFORMANCE_10_PERCENT_HIGHER",
    ]

@typing.type_check_only
class DuplicateLineItemRequest(typing.TypedDict, total=False):
    containsEuPoliticalAds: typing.Literal[
        "EU_POLITICAL_ADVERTISING_STATUS_UNKNOWN",
        "CONTAINS_EU_POLITICAL_ADVERTISING",
        "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    ]
    targetDisplayName: str

@typing.type_check_only
class DuplicateLineItemResponse(typing.TypedDict, total=False):
    duplicateLineItemId: str

@typing.type_check_only
class EditGuaranteedOrderReadAccessorsRequest(typing.TypedDict, total=False):
    addedAdvertisers: _list[str]
    partnerId: str
    readAccessInherited: bool
    removedAdvertisers: _list[str]

@typing.type_check_only
class EditGuaranteedOrderReadAccessorsResponse(typing.TypedDict, total=False):
    readAccessInherited: bool
    readAdvertiserIds: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnvironmentAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    environment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_WEB_OPTIMIZED",
        "ENVIRONMENT_WEB_NOT_OPTIMIZED",
        "ENVIRONMENT_APP",
    ]

@typing.type_check_only
class EnvironmentTargetingOptionDetails(typing.TypedDict, total=False):
    environment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED",
        "ENVIRONMENT_WEB_OPTIMIZED",
        "ENVIRONMENT_WEB_NOT_OPTIMIZED",
        "ENVIRONMENT_APP",
    ]

@typing.type_check_only
class ExchangeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    exchange: typing.Literal[
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
        "EXCHANGE_JCD",
        "EXCHANGE_PLACE_EXCHANGE",
        "EXCHANGE_APPLOVIN",
        "EXCHANGE_CONNATIX",
        "EXCHANGE_RESET_DIGITAL",
        "EXCHANGE_HIVESTACK",
        "EXCHANGE_DRAX",
        "EXCHANGE_APPLOVIN_GBID",
        "EXCHANGE_FYBER_GBID",
        "EXCHANGE_UNITY_GBID",
        "EXCHANGE_CHARTBOOST_GBID",
        "EXCHANGE_ADMOST_GBID",
        "EXCHANGE_TOPON_GBID",
        "EXCHANGE_NETFLIX",
        "EXCHANGE_CORE",
        "EXCHANGE_COMMERCE_GRID",
        "EXCHANGE_SPOTIFY",
        "EXCHANGE_TUBI",
        "EXCHANGE_SNAP",
        "EXCHANGE_CADENT",
        "EXCHANGE_EXTE",
    ]

@typing.type_check_only
class ExchangeConfig(typing.TypedDict, total=False):
    enabledExchanges: _list[ExchangeConfigEnabledExchange]

@typing.type_check_only
class ExchangeConfigEnabledExchange(typing.TypedDict, total=False):
    exchange: typing.Literal[
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
        "EXCHANGE_JCD",
        "EXCHANGE_PLACE_EXCHANGE",
        "EXCHANGE_APPLOVIN",
        "EXCHANGE_CONNATIX",
        "EXCHANGE_RESET_DIGITAL",
        "EXCHANGE_HIVESTACK",
        "EXCHANGE_DRAX",
        "EXCHANGE_APPLOVIN_GBID",
        "EXCHANGE_FYBER_GBID",
        "EXCHANGE_UNITY_GBID",
        "EXCHANGE_CHARTBOOST_GBID",
        "EXCHANGE_ADMOST_GBID",
        "EXCHANGE_TOPON_GBID",
        "EXCHANGE_NETFLIX",
        "EXCHANGE_CORE",
        "EXCHANGE_COMMERCE_GRID",
        "EXCHANGE_SPOTIFY",
        "EXCHANGE_TUBI",
        "EXCHANGE_SNAP",
        "EXCHANGE_CADENT",
        "EXCHANGE_EXTE",
    ]
    googleAdManagerAgencyId: str
    googleAdManagerBuyerNetworkId: str
    seatId: str

@typing.type_check_only
class ExchangeReviewStatus(typing.TypedDict, total=False):
    exchange: typing.Literal[
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
        "EXCHANGE_JCD",
        "EXCHANGE_PLACE_EXCHANGE",
        "EXCHANGE_APPLOVIN",
        "EXCHANGE_CONNATIX",
        "EXCHANGE_RESET_DIGITAL",
        "EXCHANGE_HIVESTACK",
        "EXCHANGE_DRAX",
        "EXCHANGE_APPLOVIN_GBID",
        "EXCHANGE_FYBER_GBID",
        "EXCHANGE_UNITY_GBID",
        "EXCHANGE_CHARTBOOST_GBID",
        "EXCHANGE_ADMOST_GBID",
        "EXCHANGE_TOPON_GBID",
        "EXCHANGE_NETFLIX",
        "EXCHANGE_CORE",
        "EXCHANGE_COMMERCE_GRID",
        "EXCHANGE_SPOTIFY",
        "EXCHANGE_TUBI",
        "EXCHANGE_SNAP",
        "EXCHANGE_CADENT",
        "EXCHANGE_EXTE",
    ]
    status: typing.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]

@typing.type_check_only
class ExchangeTargetingOptionDetails(typing.TypedDict, total=False):
    exchange: typing.Literal[
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
        "EXCHANGE_JCD",
        "EXCHANGE_PLACE_EXCHANGE",
        "EXCHANGE_APPLOVIN",
        "EXCHANGE_CONNATIX",
        "EXCHANGE_RESET_DIGITAL",
        "EXCHANGE_HIVESTACK",
        "EXCHANGE_DRAX",
        "EXCHANGE_APPLOVIN_GBID",
        "EXCHANGE_FYBER_GBID",
        "EXCHANGE_UNITY_GBID",
        "EXCHANGE_CHARTBOOST_GBID",
        "EXCHANGE_ADMOST_GBID",
        "EXCHANGE_TOPON_GBID",
        "EXCHANGE_NETFLIX",
        "EXCHANGE_CORE",
        "EXCHANGE_COMMERCE_GRID",
        "EXCHANGE_SPOTIFY",
        "EXCHANGE_TUBI",
        "EXCHANGE_SNAP",
        "EXCHANGE_CADENT",
        "EXCHANGE_EXTE",
    ]

@typing.type_check_only
class ExitEvent(typing.TypedDict, total=False):
    name: str
    reportingName: str
    type: typing.Literal[
        "EXIT_EVENT_TYPE_UNSPECIFIED",
        "EXIT_EVENT_TYPE_DEFAULT",
        "EXIT_EVENT_TYPE_BACKUP",
    ]
    url: str

@typing.type_check_only
class FixedBidStrategy(typing.TypedDict, total=False):
    bidAmountMicros: str

@typing.type_check_only
class FloodlightActivity(typing.TypedDict, total=False):
    advertiserIds: _list[str]
    displayName: str
    floodlightActivityId: str
    floodlightGroupId: str
    name: str
    remarketingConfigs: _list[RemarketingConfig]
    servingStatus: typing.Literal[
        "FLOODLIGHT_ACTIVITY_SERVING_STATUS_UNSPECIFIED",
        "FLOODLIGHT_ACTIVITY_SERVING_STATUS_ENABLED",
        "FLOODLIGHT_ACTIVITY_SERVING_STATUS_DISABLED",
    ]
    sslRequired: bool

@typing.type_check_only
class FloodlightGroup(typing.TypedDict, total=False):
    activeViewConfig: ActiveViewVideoViewabilityMetricConfig
    customVariables: dict[str, typing.Any]
    displayName: str
    floodlightGroupId: str
    lookbackWindow: LookbackWindow
    name: str
    webTagType: typing.Literal[
        "WEB_TAG_TYPE_UNSPECIFIED",
        "WEB_TAG_TYPE_NONE",
        "WEB_TAG_TYPE_IMAGE",
        "WEB_TAG_TYPE_DYNAMIC",
    ]

@typing.type_check_only
class FrequencyCap(typing.TypedDict, total=False):
    maxImpressions: int
    maxViews: int
    timeUnit: typing.Literal[
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
class GenderAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    gender: typing.Literal[
        "GENDER_UNSPECIFIED", "GENDER_MALE", "GENDER_FEMALE", "GENDER_UNKNOWN"
    ]

@typing.type_check_only
class GenderTargetingOptionDetails(typing.TypedDict, total=False):
    gender: typing.Literal[
        "GENDER_UNSPECIFIED", "GENDER_MALE", "GENDER_FEMALE", "GENDER_UNKNOWN"
    ]

@typing.type_check_only
class GeoRegionAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    geoRegionType: typing.Literal[
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
        "GEO_REGION_TYPE_NATIONAL_PARK",
        "GEO_REGION_TYPE_BARRIO",
        "GEO_REGION_TYPE_SUB_WARD",
        "GEO_REGION_TYPE_MUNICIPALITY_DISTRICT",
        "GEO_REGION_TYPE_SUB_DISTRICT",
        "GEO_REGION_TYPE_QUARTER",
        "GEO_REGION_TYPE_DIVISION",
        "GEO_REGION_TYPE_COMMUNE",
        "GEO_REGION_TYPE_COLLOQUIAL_AREA",
        "GEO_REGION_TYPE_POST_TOWN",
        "GEO_REGION_TYPE_WARD",
        "GEO_REGION_TYPE_TOWN",
        "GEO_REGION_TYPE_VILLAGE",
        "GEO_REGION_TYPE_CITY_DISTRICT",
        "GEO_REGION_TYPE_SUBURB",
        "GEO_REGION_TYPE_HAMLET",
        "GEO_REGION_TYPE_MUNICIPAL_DISTRICT",
        "GEO_REGION_TYPE_COMMUNITY",
        "GEO_REGION_TYPE_TOWNSHIP",
        "GEO_REGION_TYPE_URBAN_DISTRICT",
        "GEO_REGION_TYPE_RESIDENTIAL_AREA",
        "GEO_REGION_TYPE_INDEPENDENT_CITY",
        "GEO_REGION_TYPE_SECTOR",
        "GEO_REGION_TYPE_AREA",
        "GEO_REGION_TYPE_ESTATE",
        "GEO_REGION_TYPE_PARISH",
        "GEO_REGION_TYPE_SETTLEMENT",
        "GEO_REGION_TYPE_ZONE",
        "GEO_REGION_TYPE_COLONY",
        "GEO_REGION_TYPE_INDUSTRIAL_AREA",
        "GEO_REGION_TYPE_PROVINCIAL_CITY",
        "GEO_REGION_TYPE_RURAL_DISTRICT",
    ]
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class GeoRegionSearchTerms(typing.TypedDict, total=False):
    geoRegionQuery: str

@typing.type_check_only
class GeoRegionTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    geoRegionType: typing.Literal[
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
        "GEO_REGION_TYPE_NATIONAL_PARK",
        "GEO_REGION_TYPE_BARRIO",
        "GEO_REGION_TYPE_SUB_WARD",
        "GEO_REGION_TYPE_MUNICIPALITY_DISTRICT",
        "GEO_REGION_TYPE_SUB_DISTRICT",
        "GEO_REGION_TYPE_QUARTER",
        "GEO_REGION_TYPE_DIVISION",
        "GEO_REGION_TYPE_COMMUNE",
        "GEO_REGION_TYPE_COLLOQUIAL_AREA",
        "GEO_REGION_TYPE_POST_TOWN",
        "GEO_REGION_TYPE_WARD",
        "GEO_REGION_TYPE_TOWN",
        "GEO_REGION_TYPE_VILLAGE",
        "GEO_REGION_TYPE_CITY_DISTRICT",
        "GEO_REGION_TYPE_SUBURB",
        "GEO_REGION_TYPE_HAMLET",
        "GEO_REGION_TYPE_MUNICIPAL_DISTRICT",
        "GEO_REGION_TYPE_COMMUNITY",
        "GEO_REGION_TYPE_TOWNSHIP",
        "GEO_REGION_TYPE_URBAN_DISTRICT",
        "GEO_REGION_TYPE_RESIDENTIAL_AREA",
        "GEO_REGION_TYPE_INDEPENDENT_CITY",
        "GEO_REGION_TYPE_SECTOR",
        "GEO_REGION_TYPE_AREA",
        "GEO_REGION_TYPE_ESTATE",
        "GEO_REGION_TYPE_PARISH",
        "GEO_REGION_TYPE_SETTLEMENT",
        "GEO_REGION_TYPE_ZONE",
        "GEO_REGION_TYPE_COLONY",
        "GEO_REGION_TYPE_INDUSTRIAL_AREA",
        "GEO_REGION_TYPE_PROVINCIAL_CITY",
        "GEO_REGION_TYPE_RURAL_DISTRICT",
    ]

@typing.type_check_only
class GoogleAudience(typing.TypedDict, total=False):
    displayName: str
    googleAudienceId: str
    googleAudienceType: typing.Literal[
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
class GoogleAudienceGroup(typing.TypedDict, total=False):
    settings: _list[GoogleAudienceTargetingSetting]

@typing.type_check_only
class GoogleAudienceTargetingSetting(typing.TypedDict, total=False):
    googleAudienceId: str

@typing.type_check_only
class GoogleBytestreamMedia(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GuaranteedOrder(typing.TypedDict, total=False):
    defaultAdvertiserId: str
    defaultCampaignId: str
    displayName: str
    exchange: typing.Literal[
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
        "EXCHANGE_JCD",
        "EXCHANGE_PLACE_EXCHANGE",
        "EXCHANGE_APPLOVIN",
        "EXCHANGE_CONNATIX",
        "EXCHANGE_RESET_DIGITAL",
        "EXCHANGE_HIVESTACK",
        "EXCHANGE_DRAX",
        "EXCHANGE_APPLOVIN_GBID",
        "EXCHANGE_FYBER_GBID",
        "EXCHANGE_UNITY_GBID",
        "EXCHANGE_CHARTBOOST_GBID",
        "EXCHANGE_ADMOST_GBID",
        "EXCHANGE_TOPON_GBID",
        "EXCHANGE_NETFLIX",
        "EXCHANGE_CORE",
        "EXCHANGE_COMMERCE_GRID",
        "EXCHANGE_SPOTIFY",
        "EXCHANGE_TUBI",
        "EXCHANGE_SNAP",
        "EXCHANGE_CADENT",
        "EXCHANGE_EXTE",
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
class GuaranteedOrderStatus(typing.TypedDict, total=False):
    configStatus: typing.Literal[
        "GUARANTEED_ORDER_CONFIG_STATUS_UNSPECIFIED", "PENDING", "COMPLETED"
    ]
    entityPauseReason: str
    entityStatus: typing.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]

@typing.type_check_only
class HouseholdIncomeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    householdIncome: typing.Literal[
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
class HouseholdIncomeTargetingOptionDetails(typing.TypedDict, total=False):
    householdIncome: typing.Literal[
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
class IdFilter(typing.TypedDict, total=False):
    adGroupAdIds: _list[str]
    adGroupIds: _list[str]
    campaignIds: _list[str]
    insertionOrderIds: _list[str]
    lineItemIds: _list[str]
    mediaProductIds: _list[str]

@typing.type_check_only
class ImageAsset(typing.TypedDict, total=False):
    assetId: str
    fileSize: str
    fullSize: Dimensions
    mimeType: str

@typing.type_check_only
class InStreamAd(typing.TypedDict, total=False):
    commonInStreamAttribute: CommonInStreamAttribute
    customParameters: dict[str, typing.Any]

@typing.type_check_only
class InsertionOrder(typing.TypedDict, total=False):
    advertiserId: str
    bidStrategy: BiddingStrategy
    billableOutcome: typing.Literal[
        "BILLABLE_OUTCOME_UNSPECIFIED",
        "BILLABLE_OUTCOME_PAY_PER_IMPRESSION",
        "BILLABLE_OUTCOME_PAY_PER_CLICK",
        "BILLABLE_OUTCOME_PAY_PER_VIEWABLE_IMPRESSION",
    ]
    budget: InsertionOrderBudget
    campaignId: str
    displayName: str
    entityStatus: typing.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    frequencyCap: FrequencyCap
    insertionOrderId: str
    insertionOrderType: typing.Literal[
        "INSERTION_ORDER_TYPE_UNSPECIFIED", "RTB", "OVER_THE_TOP"
    ]
    integrationDetails: IntegrationDetails
    name: str
    pacing: Pacing
    partnerCosts: _list[PartnerCost]
    performanceGoal: PerformanceGoal
    reservationType: typing.Literal[
        "RESERVATION_TYPE_UNSPECIFIED",
        "RESERVATION_TYPE_NOT_GUARANTEED",
        "RESERVATION_TYPE_PROGRAMMATIC_GUARANTEED",
        "RESERVATION_TYPE_TAG_GUARANTEED",
        "RESERVATION_TYPE_PETRA_VIRAL",
        "RESERVATION_TYPE_INSTANT_RESERVE",
    ]
    updateTime: str

@typing.type_check_only
class InsertionOrderBudget(typing.TypedDict, total=False):
    automationType: typing.Literal[
        "INSERTION_ORDER_AUTOMATION_TYPE_UNSPECIFIED",
        "INSERTION_ORDER_AUTOMATION_TYPE_BUDGET",
        "INSERTION_ORDER_AUTOMATION_TYPE_NONE",
        "INSERTION_ORDER_AUTOMATION_TYPE_BID_BUDGET",
    ]
    budgetSegments: _list[InsertionOrderBudgetSegment]
    budgetUnit: typing.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]

@typing.type_check_only
class InsertionOrderBudgetSegment(typing.TypedDict, total=False):
    budgetAmountMicros: str
    campaignBudgetId: str
    dateRange: DateRange
    description: str

@typing.type_check_only
class IntegralAdScience(typing.TypedDict, total=False):
    customSegmentId: _list[str]
    displayViewability: typing.Literal[
        "PERFORMANCE_VIEWABILITY_UNSPECIFIED",
        "PERFORMANCE_VIEWABILITY_40",
        "PERFORMANCE_VIEWABILITY_50",
        "PERFORMANCE_VIEWABILITY_60",
        "PERFORMANCE_VIEWABILITY_70",
    ]
    excludeUnrateable: bool
    excludedAdFraudRisk: typing.Literal[
        "SUSPICIOUS_ACTIVITY_UNSPECIFIED",
        "SUSPICIOUS_ACTIVITY_HR",
        "SUSPICIOUS_ACTIVITY_HMR",
        "SUSPICIOUS_ACTIVITY_FD",
    ]
    excludedAdultRisk: typing.Literal["ADULT_UNSPECIFIED", "ADULT_HR", "ADULT_HMR"]
    excludedAlcoholRisk: typing.Literal[
        "ALCOHOL_UNSPECIFIED", "ALCOHOL_HR", "ALCOHOL_HMR"
    ]
    excludedDrugsRisk: typing.Literal["DRUGS_UNSPECIFIED", "DRUGS_HR", "DRUGS_HMR"]
    excludedGamblingRisk: typing.Literal[
        "GAMBLING_UNSPECIFIED", "GAMBLING_HR", "GAMBLING_HMR"
    ]
    excludedHateSpeechRisk: typing.Literal[
        "HATE_SPEECH_UNSPECIFIED", "HATE_SPEECH_HR", "HATE_SPEECH_HMR"
    ]
    excludedIllegalDownloadsRisk: typing.Literal[
        "ILLEGAL_DOWNLOADS_UNSPECIFIED", "ILLEGAL_DOWNLOADS_HR", "ILLEGAL_DOWNLOADS_HMR"
    ]
    excludedOffensiveLanguageRisk: typing.Literal[
        "OFFENSIVE_LANGUAGE_UNSPECIFIED",
        "OFFENSIVE_LANGUAGE_HR",
        "OFFENSIVE_LANGUAGE_HMR",
    ]
    excludedViolenceRisk: typing.Literal[
        "VIOLENCE_UNSPECIFIED", "VIOLENCE_HR", "VIOLENCE_HMR"
    ]
    traqScoreOption: typing.Literal[
        "TRAQ_UNSPECIFIED",
        "TRAQ_250",
        "TRAQ_500",
        "TRAQ_600",
        "TRAQ_700",
        "TRAQ_750",
        "TRAQ_875",
        "TRAQ_1000",
    ]
    videoViewability: typing.Literal[
        "VIDEO_VIEWABILITY_UNSPECIFIED",
        "VIDEO_VIEWABILITY_40",
        "VIDEO_VIEWABILITY_50",
        "VIDEO_VIEWABILITY_60",
        "VIDEO_VIEWABILITY_70",
    ]

@typing.type_check_only
class IntegrationDetails(typing.TypedDict, total=False):
    details: str
    integrationCode: str

@typing.type_check_only
class InventorySourceAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    inventorySourceId: str

@typing.type_check_only
class InventorySourceFilter(typing.TypedDict, total=False):
    inventorySourceIds: _list[str]

@typing.type_check_only
class InventorySourceGroup(typing.TypedDict, total=False):
    displayName: str
    inventorySourceGroupId: str
    name: str

@typing.type_check_only
class InventorySourceGroupAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    inventorySourceGroupId: str

@typing.type_check_only
class Invoice(typing.TypedDict, total=False):
    budgetInvoiceGroupingId: str
    budgetSummaries: _list[BudgetSummary]
    correctedInvoiceId: str
    currencyCode: str
    displayName: str
    dueDate: Date
    invoiceId: str
    invoiceType: typing.Literal[
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
class KeywordAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    exemptedPolicyNames: _list[str]
    keyword: str
    negative: bool

@typing.type_check_only
class LanguageAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class LanguageTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class LineItem(typing.TypedDict, total=False):
    advertiserId: str
    bidStrategy: BiddingStrategy
    budget: LineItemBudget
    campaignId: str
    containsEuPoliticalAds: typing.Literal[
        "EU_POLITICAL_ADVERTISING_STATUS_UNKNOWN",
        "CONTAINS_EU_POLITICAL_ADVERTISING",
        "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    ]
    conversionCounting: ConversionCountingConfig
    creativeIds: _list[str]
    demandGenSettings: DemandGenSettings
    displayName: str
    entityStatus: typing.Literal[
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
    lineItemId: str
    lineItemType: typing.Literal[
        "LINE_ITEM_TYPE_UNSPECIFIED",
        "LINE_ITEM_TYPE_DISPLAY_DEFAULT",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_VIDEO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INSTALL",
        "LINE_ITEM_TYPE_DISPLAY_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_VIDEO_MOBILE_APP_INVENTORY",
        "LINE_ITEM_TYPE_AUDIO_DEFAULT",
        "LINE_ITEM_TYPE_VIDEO_OVER_THE_TOP",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_ACTION",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_NON_SKIPPABLE",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIDEO_SEQUENCE",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_AUDIO",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_REACH",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_SIMPLE",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_NON_SKIPPABLE_OVER_THE_TOP",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_REACH_OVER_THE_TOP",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_SIMPLE_OVER_THE_TOP",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_TARGET_FREQUENCY",
        "LINE_ITEM_TYPE_YOUTUBE_AND_PARTNERS_VIEW",
        "LINE_ITEM_TYPE_DISPLAY_OUT_OF_HOME",
        "LINE_ITEM_TYPE_VIDEO_OUT_OF_HOME",
        "LINE_ITEM_TYPE_DEMAND_GEN",
    ]
    mobileApp: MobileApp
    name: str
    optimizeFixedBidding: bool
    pacing: Pacing
    partnerCosts: _list[PartnerCost]
    partnerRevenueModel: PartnerRevenueModel
    reservationType: typing.Literal[
        "RESERVATION_TYPE_UNSPECIFIED",
        "RESERVATION_TYPE_NOT_GUARANTEED",
        "RESERVATION_TYPE_PROGRAMMATIC_GUARANTEED",
        "RESERVATION_TYPE_TAG_GUARANTEED",
        "RESERVATION_TYPE_PETRA_VIRAL",
        "RESERVATION_TYPE_INSTANT_RESERVE",
    ]
    targetingExpansion: TargetingExpansionConfig
    updateTime: str
    warningMessages: _list[
        typing.Literal[
            "LINE_ITEM_WARNING_MESSAGE_UNSPECIFIED",
            "INVALID_FLIGHT_DATES",
            "EXPIRED",
            "PENDING_FLIGHT",
            "ALL_PARTNER_ENABLED_EXCHANGES_NEGATIVELY_TARGETED",
            "INVALID_INVENTORY_SOURCE",
            "APP_INVENTORY_INVALID_SITE_TARGETING",
            "APP_INVENTORY_INVALID_AUDIENCE_LISTS",
            "NO_VALID_CREATIVE",
            "PARENT_INSERTION_ORDER_PAUSED",
            "PARENT_INSERTION_ORDER_EXPIRED",
            "DEPRECATED_FIRST_PARTY_AUDIENCE_EXCLUSION",
        ]
    ]
    youtubeAndPartnersSettings: YoutubeAndPartnersSettings

@typing.type_check_only
class LineItemAssignedTargetingOption(typing.TypedDict, total=False):
    assignedTargetingOption: AssignedTargetingOption
    lineItemId: str

@typing.type_check_only
class LineItemBudget(typing.TypedDict, total=False):
    budgetAllocationType: typing.Literal[
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNSPECIFIED",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_AUTOMATIC",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_FIXED",
        "LINE_ITEM_BUDGET_ALLOCATION_TYPE_UNLIMITED",
    ]
    budgetUnit: typing.Literal[
        "BUDGET_UNIT_UNSPECIFIED", "BUDGET_UNIT_CURRENCY", "BUDGET_UNIT_IMPRESSIONS"
    ]
    maxAmount: str

@typing.type_check_only
class LineItemFlight(typing.TypedDict, total=False):
    dateRange: DateRange
    flightDateType: typing.Literal[
        "LINE_ITEM_FLIGHT_DATE_TYPE_UNSPECIFIED",
        "LINE_ITEM_FLIGHT_DATE_TYPE_INHERITED",
        "LINE_ITEM_FLIGHT_DATE_TYPE_CUSTOM",
    ]

@typing.type_check_only
class ListAdvertiserAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListAdvertisersResponse(typing.TypedDict, total=False):
    advertisers: _list[Advertiser]
    nextPageToken: str

@typing.type_check_only
class ListAssignedInventorySourcesResponse(typing.TypedDict, total=False):
    assignedInventorySources: _list[AssignedInventorySource]
    nextPageToken: str

@typing.type_check_only
class ListAssignedLocationsResponse(typing.TypedDict, total=False):
    assignedLocations: _list[AssignedLocation]
    nextPageToken: str

@typing.type_check_only
class ListCampaignsResponse(typing.TypedDict, total=False):
    campaigns: _list[Campaign]
    nextPageToken: str

@typing.type_check_only
class ListChannelsResponse(typing.TypedDict, total=False):
    channels: _list[Channel]
    nextPageToken: str

@typing.type_check_only
class ListCombinedAudiencesResponse(typing.TypedDict, total=False):
    combinedAudiences: _list[CombinedAudience]
    nextPageToken: str

@typing.type_check_only
class ListCreativesResponse(typing.TypedDict, total=False):
    creatives: _list[Creative]
    nextPageToken: str

@typing.type_check_only
class ListCustomBiddingAlgorithmsResponse(typing.TypedDict, total=False):
    customBiddingAlgorithms: _list[CustomBiddingAlgorithm]
    nextPageToken: str

@typing.type_check_only
class ListCustomBiddingScriptsResponse(typing.TypedDict, total=False):
    customBiddingScripts: _list[CustomBiddingScript]
    nextPageToken: str

@typing.type_check_only
class ListCustomListsResponse(typing.TypedDict, total=False):
    customLists: _list[CustomList]
    nextPageToken: str

@typing.type_check_only
class ListFloodlightActivitiesResponse(typing.TypedDict, total=False):
    floodlightActivities: _list[FloodlightActivity]
    nextPageToken: str

@typing.type_check_only
class ListGoogleAudiencesResponse(typing.TypedDict, total=False):
    googleAudiences: _list[GoogleAudience]
    nextPageToken: str

@typing.type_check_only
class ListGuaranteedOrdersResponse(typing.TypedDict, total=False):
    guaranteedOrders: _list[GuaranteedOrder]
    nextPageToken: str

@typing.type_check_only
class ListInsertionOrdersResponse(typing.TypedDict, total=False):
    insertionOrders: _list[InsertionOrder]
    nextPageToken: str

@typing.type_check_only
class ListInventorySourceGroupsResponse(typing.TypedDict, total=False):
    inventorySourceGroups: _list[InventorySourceGroup]
    nextPageToken: str

@typing.type_check_only
class ListInvoicesResponse(typing.TypedDict, total=False):
    invoices: _list[Invoice]
    nextPageToken: str

@typing.type_check_only
class ListLineItemAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListLineItemsResponse(typing.TypedDict, total=False):
    lineItems: _list[LineItem]
    nextPageToken: str

@typing.type_check_only
class ListLocationListsResponse(typing.TypedDict, total=False):
    locationLists: _list[LocationList]
    nextPageToken: str

@typing.type_check_only
class ListManualTriggersResponse(typing.TypedDict, total=False):
    manualTriggers: _list[ManualTrigger]
    nextPageToken: str

@typing.type_check_only
class ListNegativeKeywordListsResponse(typing.TypedDict, total=False):
    negativeKeywordLists: _list[NegativeKeywordList]
    nextPageToken: str

@typing.type_check_only
class ListNegativeKeywordsResponse(typing.TypedDict, total=False):
    negativeKeywords: _list[NegativeKeyword]
    nextPageToken: str

@typing.type_check_only
class ListPartnerAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListPartnersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    partners: _list[Partner]

@typing.type_check_only
class ListSitesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class ListTargetingOptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    targetingOptions: _list[TargetingOption]

@typing.type_check_only
class ListUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class ListYoutubeAdGroupAdsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    youtubeAdGroupAds: _list[YoutubeAdGroupAd]

@typing.type_check_only
class ListYoutubeAdGroupAssignedTargetingOptionsResponse(typing.TypedDict, total=False):
    assignedTargetingOptions: _list[AssignedTargetingOption]
    nextPageToken: str

@typing.type_check_only
class ListYoutubeAdGroupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    youtubeAdGroups: _list[YoutubeAdGroup]

@typing.type_check_only
class LocationList(typing.TypedDict, total=False):
    advertiserId: str
    displayName: str
    locationListId: str
    locationType: typing.Literal[
        "TARGETING_LOCATION_TYPE_UNSPECIFIED",
        "TARGETING_LOCATION_TYPE_PROXIMITY",
        "TARGETING_LOCATION_TYPE_REGIONAL",
    ]
    name: str

@typing.type_check_only
class LookbackWindow(typing.TypedDict, total=False):
    clickDays: int
    impressionDays: int

@typing.type_check_only
class LookupInvoiceCurrencyResponse(typing.TypedDict, total=False):
    currencyCode: str

@typing.type_check_only
class ManualTrigger(typing.TypedDict, total=False):
    activationDurationMinutes: str
    advertiserId: str
    displayName: str
    latestActivationTime: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "INACTIVE", "ACTIVE"]
    triggerId: str

@typing.type_check_only
class MastheadAd(typing.TypedDict, total=False):
    autoplayVideoDuration: str
    autoplayVideoStartMillisecond: str
    callToActionButtonLabel: str
    callToActionFinalUrl: str
    callToActionTrackingUrl: str
    companionYoutubeVideos: _list[YoutubeVideoDetails]
    description: str
    headline: str
    showChannelArt: bool
    video: YoutubeVideoDetails
    videoAspectRatio: typing.Literal[
        "VIDEO_ASPECT_RATIO_UNSPECIFIED",
        "VIDEO_ASPECT_RATIO_WIDESCREEN",
        "VIDEO_ASPECT_RATIO_FIXED_16_9",
    ]

@typing.type_check_only
class MaximizeSpendBidStrategy(typing.TypedDict, total=False):
    customBiddingAlgorithmId: str
    maxAverageCpmBidAmountMicros: str
    performanceGoalType: typing.Literal[
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
class MeasurementConfig(typing.TypedDict, total=False):
    dv360ToCmCostReportingEnabled: bool
    dv360ToCmDataSharingEnabled: bool

@typing.type_check_only
class MobileApp(typing.TypedDict, total=False):
    appId: str
    displayName: str
    platform: typing.Literal["PLATFORM_UNSPECIFIED", "IOS", "ANDROID"]
    publisher: str

@typing.type_check_only
class NativeContentPositionAssignedTargetingOptionDetails(
    typing.TypedDict, total=False
):
    contentPosition: typing.Literal[
        "NATIVE_CONTENT_POSITION_UNSPECIFIED",
        "NATIVE_CONTENT_POSITION_UNKNOWN",
        "NATIVE_CONTENT_POSITION_IN_ARTICLE",
        "NATIVE_CONTENT_POSITION_IN_FEED",
        "NATIVE_CONTENT_POSITION_PERIPHERAL",
        "NATIVE_CONTENT_POSITION_RECOMMENDATION",
    ]

@typing.type_check_only
class NativeContentPositionTargetingOptionDetails(typing.TypedDict, total=False):
    contentPosition: typing.Literal[
        "NATIVE_CONTENT_POSITION_UNSPECIFIED",
        "NATIVE_CONTENT_POSITION_UNKNOWN",
        "NATIVE_CONTENT_POSITION_IN_ARTICLE",
        "NATIVE_CONTENT_POSITION_IN_FEED",
        "NATIVE_CONTENT_POSITION_PERIPHERAL",
        "NATIVE_CONTENT_POSITION_RECOMMENDATION",
    ]

@typing.type_check_only
class NegativeKeyword(typing.TypedDict, total=False):
    keywordValue: str
    name: str

@typing.type_check_only
class NegativeKeywordList(typing.TypedDict, total=False):
    advertiserId: str
    displayName: str
    name: str
    negativeKeywordListId: str
    targetedLineItemCount: str

@typing.type_check_only
class NegativeKeywordListAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    negativeKeywordListId: str

@typing.type_check_only
class NonSkippableAd(typing.TypedDict, total=False):
    commonInStreamAttribute: CommonInStreamAttribute
    customParameters: dict[str, typing.Any]

@typing.type_check_only
class ObaIcon(typing.TypedDict, total=False):
    clickTrackingUrl: str
    dimensions: Dimensions
    landingPageUrl: str
    position: typing.Literal[
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
class OmidAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    omid: typing.Literal["OMID_UNSPECIFIED", "OMID_FOR_MOBILE_DISPLAY_ADS"]

@typing.type_check_only
class OmidTargetingOptionDetails(typing.TypedDict, total=False):
    omid: typing.Literal["OMID_UNSPECIFIED", "OMID_FOR_MOBILE_DISPLAY_ADS"]

@typing.type_check_only
class OnScreenPositionAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    adType: typing.Literal[
        "AD_TYPE_UNSPECIFIED", "AD_TYPE_DISPLAY", "AD_TYPE_VIDEO", "AD_TYPE_AUDIO"
    ]
    onScreenPosition: typing.Literal[
        "ON_SCREEN_POSITION_UNSPECIFIED",
        "ON_SCREEN_POSITION_UNKNOWN",
        "ON_SCREEN_POSITION_ABOVE_THE_FOLD",
        "ON_SCREEN_POSITION_BELOW_THE_FOLD",
    ]
    targetingOptionId: str

@typing.type_check_only
class OnScreenPositionTargetingOptionDetails(typing.TypedDict, total=False):
    onScreenPosition: typing.Literal[
        "ON_SCREEN_POSITION_UNSPECIFIED",
        "ON_SCREEN_POSITION_UNKNOWN",
        "ON_SCREEN_POSITION_ABOVE_THE_FOLD",
        "ON_SCREEN_POSITION_BELOW_THE_FOLD",
    ]

@typing.type_check_only
class OperatingSystemAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    negative: bool
    targetingOptionId: str

@typing.type_check_only
class OperatingSystemTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Pacing(typing.TypedDict, total=False):
    dailyMaxImpressions: str
    dailyMaxMicros: str
    pacingPeriod: typing.Literal[
        "PACING_PERIOD_UNSPECIFIED", "PACING_PERIOD_DAILY", "PACING_PERIOD_FLIGHT"
    ]
    pacingType: typing.Literal[
        "PACING_TYPE_UNSPECIFIED",
        "PACING_TYPE_AHEAD",
        "PACING_TYPE_ASAP",
        "PACING_TYPE_EVEN",
    ]

@typing.type_check_only
class ParentEntityFilter(typing.TypedDict, total=False):
    fileType: _list[
        typing.Literal[
            "FILE_TYPE_UNSPECIFIED",
            "FILE_TYPE_CAMPAIGN",
            "FILE_TYPE_MEDIA_PRODUCT",
            "FILE_TYPE_INSERTION_ORDER",
            "FILE_TYPE_LINE_ITEM",
            "FILE_TYPE_AD_GROUP",
            "FILE_TYPE_AD",
        ]
    ]
    filterIds: _list[str]
    filterType: typing.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "FILTER_TYPE_NONE",
        "FILTER_TYPE_ADVERTISER_ID",
        "FILTER_TYPE_CAMPAIGN_ID",
        "FILTER_TYPE_MEDIA_PRODUCT_ID",
        "FILTER_TYPE_INSERTION_ORDER_ID",
        "FILTER_TYPE_LINE_ITEM_ID",
    ]

@typing.type_check_only
class ParentalStatusAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    parentalStatus: typing.Literal[
        "PARENTAL_STATUS_UNSPECIFIED",
        "PARENTAL_STATUS_PARENT",
        "PARENTAL_STATUS_NOT_A_PARENT",
        "PARENTAL_STATUS_UNKNOWN",
    ]

@typing.type_check_only
class ParentalStatusTargetingOptionDetails(typing.TypedDict, total=False):
    parentalStatus: typing.Literal[
        "PARENTAL_STATUS_UNSPECIFIED",
        "PARENTAL_STATUS_PARENT",
        "PARENTAL_STATUS_NOT_A_PARENT",
        "PARENTAL_STATUS_UNKNOWN",
    ]

@typing.type_check_only
class Partner(typing.TypedDict, total=False):
    adServerConfig: PartnerAdServerConfig
    dataAccessConfig: PartnerDataAccessConfig
    displayName: str
    entityStatus: typing.Literal[
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
class PartnerAdServerConfig(typing.TypedDict, total=False):
    measurementConfig: MeasurementConfig

@typing.type_check_only
class PartnerCost(typing.TypedDict, total=False):
    costType: typing.Literal[
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
        "PARTNER_COST_TYPE_CUSTOM_FEE_1",
        "PARTNER_COST_TYPE_CUSTOM_FEE_2",
        "PARTNER_COST_TYPE_CUSTOM_FEE_3",
        "PARTNER_COST_TYPE_CUSTOM_FEE_4",
        "PARTNER_COST_TYPE_CUSTOM_FEE_5",
        "PARTNER_COST_TYPE_SCIBIDS_FEE",
    ]
    feeAmount: str
    feePercentageMillis: str
    feeType: typing.Literal[
        "PARTNER_COST_FEE_TYPE_UNSPECIFIED",
        "PARTNER_COST_FEE_TYPE_CPM_FEE",
        "PARTNER_COST_FEE_TYPE_MEDIA_FEE",
    ]
    invoiceType: typing.Literal[
        "PARTNER_COST_INVOICE_TYPE_UNSPECIFIED",
        "PARTNER_COST_INVOICE_TYPE_DV360",
        "PARTNER_COST_INVOICE_TYPE_PARTNER",
    ]

@typing.type_check_only
class PartnerDataAccessConfig(typing.TypedDict, total=False):
    sdfConfig: SdfConfig

@typing.type_check_only
class PartnerGeneralConfig(typing.TypedDict, total=False):
    currencyCode: str
    timeZone: str

@typing.type_check_only
class PartnerRevenueModel(typing.TypedDict, total=False):
    markupAmount: str
    markupType: typing.Literal[
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_UNSPECIFIED",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_CPM",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_MEDIA_COST_MARKUP",
        "PARTNER_REVENUE_MODEL_MARKUP_TYPE_TOTAL_MEDIA_COST_MARKUP",
    ]

@typing.type_check_only
class PerformanceGoal(typing.TypedDict, total=False):
    performanceGoalAmountMicros: str
    performanceGoalPercentageMicros: str
    performanceGoalString: str
    performanceGoalType: typing.Literal[
        "PERFORMANCE_GOAL_TYPE_UNSPECIFIED",
        "PERFORMANCE_GOAL_TYPE_CPM",
        "PERFORMANCE_GOAL_TYPE_CPC",
        "PERFORMANCE_GOAL_TYPE_CPA",
        "PERFORMANCE_GOAL_TYPE_CTR",
        "PERFORMANCE_GOAL_TYPE_VIEWABILITY",
        "PERFORMANCE_GOAL_TYPE_CPIAVC",
        "PERFORMANCE_GOAL_TYPE_CPE",
        "PERFORMANCE_GOAL_TYPE_CPV",
        "PERFORMANCE_GOAL_TYPE_CLICK_CVR",
        "PERFORMANCE_GOAL_TYPE_IMPRESSION_CVR",
        "PERFORMANCE_GOAL_TYPE_VCPM",
        "PERFORMANCE_GOAL_TYPE_VTR",
        "PERFORMANCE_GOAL_TYPE_AUDIO_COMPLETION_RATE",
        "PERFORMANCE_GOAL_TYPE_VIDEO_COMPLETION_RATE",
        "PERFORMANCE_GOAL_TYPE_OTHER",
    ]

@typing.type_check_only
class PerformanceGoalBidStrategy(typing.TypedDict, total=False):
    customBiddingAlgorithmId: str
    maxAverageCpmBidAmountMicros: str
    performanceGoalAmountMicros: str
    performanceGoalType: typing.Literal[
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
class PoiAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    latitude: float
    longitude: float
    proximityRadiusAmount: float
    proximityRadiusUnit: typing.Literal[
        "DISTANCE_UNIT_UNSPECIFIED", "DISTANCE_UNIT_MILES", "DISTANCE_UNIT_KILOMETERS"
    ]
    targetingOptionId: str

@typing.type_check_only
class PoiSearchTerms(typing.TypedDict, total=False):
    poiQuery: str

@typing.type_check_only
class PoiTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str
    latitude: float
    longitude: float

@typing.type_check_only
class PrismaConfig(typing.TypedDict, total=False):
    prismaCpeCode: PrismaCpeCode
    prismaType: typing.Literal[
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
class PrismaCpeCode(typing.TypedDict, total=False):
    prismaClientCode: str
    prismaEstimateCode: str
    prismaProductCode: str

@typing.type_check_only
class ProductFeedData(typing.TypedDict, total=False):
    isFeedDisabled: bool
    productMatchDimensions: _list[ProductMatchDimension]
    productMatchType: typing.Literal[
        "PRODUCT_MATCH_TYPE_UNSPECIFIED",
        "PRODUCT_MATCH_TYPE_ALL_PRODUCTS",
        "PRODUCT_MATCH_TYPE_SPECIFIC_PRODUCTS",
        "PRODUCT_MATCH_TYPE_CUSTOM_LABEL",
    ]

@typing.type_check_only
class ProductMatchDimension(typing.TypedDict, total=False):
    customLabel: CustomLabel
    productOfferId: str

@typing.type_check_only
class ProximityLocationListAssignedTargetingOptionDetails(
    typing.TypedDict, total=False
):
    proximityLocationListId: str
    proximityRadius: float
    proximityRadiusUnit: typing.Literal[
        "PROXIMITY_RADIUS_UNIT_UNSPECIFIED",
        "PROXIMITY_RADIUS_UNIT_MILES",
        "PROXIMITY_RADIUS_UNIT_KILOMETERS",
    ]

@typing.type_check_only
class PublisherReviewStatus(typing.TypedDict, total=False):
    publisherName: str
    status: typing.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]

@typing.type_check_only
class RegionalLocationListAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    negative: bool
    regionalLocationListId: str

@typing.type_check_only
class RemarketingConfig(typing.TypedDict, total=False):
    advertiserId: str
    remarketingEnabled: bool

@typing.type_check_only
class ReplaceNegativeKeywordsRequest(typing.TypedDict, total=False):
    newNegativeKeywords: _list[NegativeKeyword]

@typing.type_check_only
class ReplaceNegativeKeywordsResponse(typing.TypedDict, total=False):
    negativeKeywords: _list[NegativeKeyword]

@typing.type_check_only
class ReplaceSitesRequest(typing.TypedDict, total=False):
    advertiserId: str
    newSites: _list[Site]
    partnerId: str

@typing.type_check_only
class ReplaceSitesResponse(typing.TypedDict, total=False):
    sites: _list[Site]

@typing.type_check_only
class ReviewStatusInfo(typing.TypedDict, total=False):
    approvalStatus: typing.Literal[
        "APPROVAL_STATUS_UNSPECIFIED",
        "APPROVAL_STATUS_PENDING_NOT_SERVABLE",
        "APPROVAL_STATUS_PENDING_SERVABLE",
        "APPROVAL_STATUS_APPROVED_SERVABLE",
        "APPROVAL_STATUS_REJECTED_NOT_SERVABLE",
    ]
    contentAndPolicyReviewStatus: typing.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    creativeAndLandingPageReviewStatus: typing.Literal[
        "REVIEW_STATUS_UNSPECIFIED",
        "REVIEW_STATUS_APPROVED",
        "REVIEW_STATUS_REJECTED",
        "REVIEW_STATUS_PENDING",
    ]
    exchangeReviewStatuses: _list[ExchangeReviewStatus]
    publisherReviewStatuses: _list[PublisherReviewStatus]

@typing.type_check_only
class ScriptError(typing.TypedDict, total=False):
    column: str
    errorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED", "SYNTAX_ERROR", "DEPRECATED_SYNTAX", "INTERNAL_ERROR"
    ]
    errorMessage: str
    line: str

@typing.type_check_only
class SdfConfig(typing.TypedDict, total=False):
    adminEmail: str
    version: typing.Literal[
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
        "SDF_VERSION_6",
        "SDF_VERSION_7",
        "SDF_VERSION_7_1",
        "SDF_VERSION_8",
        "SDF_VERSION_8_1",
        "SDF_VERSION_9",
        "SDF_VERSION_9_1",
        "SDF_VERSION_9_2",
        "SDF_VERSION_10",
        "SDF_VERSION_10_1",
    ]

@typing.type_check_only
class SdfDownloadTask(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class SdfDownloadTaskMetadata(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    version: typing.Literal[
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
        "SDF_VERSION_6",
        "SDF_VERSION_7",
        "SDF_VERSION_7_1",
        "SDF_VERSION_8",
        "SDF_VERSION_8_1",
        "SDF_VERSION_9",
        "SDF_VERSION_9_1",
        "SDF_VERSION_9_2",
        "SDF_VERSION_10",
        "SDF_VERSION_10_1",
    ]

@typing.type_check_only
class SearchTargetingOptionsRequest(typing.TypedDict, total=False):
    advertiserId: str
    businessChainSearchTerms: BusinessChainSearchTerms
    geoRegionSearchTerms: GeoRegionSearchTerms
    pageSize: int
    pageToken: str
    poiSearchTerms: PoiSearchTerms

@typing.type_check_only
class SearchTargetingOptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    targetingOptions: _list[TargetingOption]

@typing.type_check_only
class SensitiveCategoryAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    excludedSensitiveCategory: typing.Literal[
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
        "SENSITIVE_CATEGORY_EMBEDDED_VIDEO",
        "SENSITIVE_CATEGORY_LIVE_STREAMING_VIDEO",
    ]

@typing.type_check_only
class SensitiveCategoryTargetingOptionDetails(typing.TypedDict, total=False):
    sensitiveCategory: typing.Literal[
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
        "SENSITIVE_CATEGORY_EMBEDDED_VIDEO",
        "SENSITIVE_CATEGORY_LIVE_STREAMING_VIDEO",
    ]

@typing.type_check_only
class SessionPositionAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    sessionPosition: typing.Literal[
        "SESSION_POSITION_UNSPECIFIED", "SESSION_POSITION_FIRST_IMPRESSION"
    ]

@typing.type_check_only
class Site(typing.TypedDict, total=False):
    name: str
    urlOrAppId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SubExchangeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    targetingOptionId: str

@typing.type_check_only
class SubExchangeTargetingOptionDetails(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class TargetFrequency(typing.TypedDict, total=False):
    targetCount: str
    timeUnit: typing.Literal[
        "TIME_UNIT_UNSPECIFIED",
        "TIME_UNIT_LIFETIME",
        "TIME_UNIT_MONTHS",
        "TIME_UNIT_WEEKS",
        "TIME_UNIT_DAYS",
        "TIME_UNIT_HOURS",
        "TIME_UNIT_MINUTES",
    ]
    timeUnitCount: int

@typing.type_check_only
class TargetingExpansionConfig(typing.TypedDict, total=False):
    excludeDemographicExpansion: bool
    excludeFirstPartyAudience: bool
    targetingExpansionLevel: typing.Literal[
        "TARGETING_EXPANSION_LEVEL_UNSPECIFIED",
        "NO_EXPANSION",
        "LEAST_EXPANSION",
        "SOME_EXPANSION",
        "BALANCED_EXPANSION",
        "MORE_EXPANSION",
        "MOST_EXPANSION",
    ]

@typing.type_check_only
class TargetingOption(typing.TypedDict, total=False):
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
    targetingType: typing.Literal[
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
        "TARGETING_TYPE_YOUTUBE_VIDEO",
        "TARGETING_TYPE_YOUTUBE_CHANNEL",
        "TARGETING_TYPE_SESSION_POSITION",
        "TARGETING_TYPE_YOUTUBE_CHANNEL_PACK",
    ]
    userRewardedContentDetails: UserRewardedContentTargetingOptionDetails
    videoPlayerSizeDetails: VideoPlayerSizeTargetingOptionDetails
    viewabilityDetails: ViewabilityTargetingOptionDetails

@typing.type_check_only
class ThirdPartyMeasurementConfigs(typing.TypedDict, total=False):
    brandLiftVendorConfigs: _list[ThirdPartyVendorConfig]
    brandSafetyVendorConfigs: _list[ThirdPartyVendorConfig]
    reachVendorConfigs: _list[ThirdPartyVendorConfig]
    viewabilityVendorConfigs: _list[ThirdPartyVendorConfig]

@typing.type_check_only
class ThirdPartyOnlyConfig(typing.TypedDict, total=False):
    pixelOrderIdReportingEnabled: bool

@typing.type_check_only
class ThirdPartyUrl(typing.TypedDict, total=False):
    type: typing.Literal[
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
class ThirdPartyVendorConfig(typing.TypedDict, total=False):
    placementId: str
    vendor: typing.Literal[
        "THIRD_PARTY_VENDOR_UNSPECIFIED",
        "THIRD_PARTY_VENDOR_MOAT",
        "THIRD_PARTY_VENDOR_DOUBLE_VERIFY",
        "THIRD_PARTY_VENDOR_INTEGRAL_AD_SCIENCE",
        "THIRD_PARTY_VENDOR_COMSCORE",
        "THIRD_PARTY_VENDOR_TELEMETRY",
        "THIRD_PARTY_VENDOR_MEETRICS",
        "THIRD_PARTY_VENDOR_ZEFR",
        "THIRD_PARTY_VENDOR_NIELSEN",
        "THIRD_PARTY_VENDOR_KANTAR",
        "THIRD_PARTY_VENDOR_DYNATA",
        "THIRD_PARTY_VENDOR_TRANSUNION",
        "THIRD_PARTY_VENDOR_ORIGIN",
        "THIRD_PARTY_VENDOR_GEMIUS",
        "THIRD_PARTY_VENDOR_MEDIA_SCOPE",
        "THIRD_PARTY_VENDOR_AUDIENCE_PROJECT",
        "THIRD_PARTY_VENDOR_VIDEO_AMP",
        "THIRD_PARTY_VENDOR_ISPOT_TV",
        "THIRD_PARTY_VENDOR_INTAGE",
        "THIRD_PARTY_VENDOR_MACROMILL",
        "THIRD_PARTY_VENDOR_VIDEO_RESEARCH",
    ]

@typing.type_check_only
class ThirdPartyVerifierAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    adloox: Adloox
    doubleVerify: DoubleVerify
    integralAdScience: IntegralAdScience

@typing.type_check_only
class TimerEvent(typing.TypedDict, total=False):
    name: str
    reportingName: str

@typing.type_check_only
class TrackingFloodlightActivityConfig(typing.TypedDict, total=False):
    floodlightActivityId: str
    postClickLookbackWindowDays: int
    postViewLookbackWindowDays: int

@typing.type_check_only
class Transcode(typing.TypedDict, total=False):
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
class UniversalAdId(typing.TypedDict, total=False):
    id: str
    registry: typing.Literal[
        "UNIVERSAL_AD_REGISTRY_UNSPECIFIED",
        "UNIVERSAL_AD_REGISTRY_OTHER",
        "UNIVERSAL_AD_REGISTRY_AD_ID",
        "UNIVERSAL_AD_REGISTRY_CLEARCAST",
        "UNIVERSAL_AD_REGISTRY_DV360",
        "UNIVERSAL_AD_REGISTRY_CM",
    ]

@typing.type_check_only
class UrlAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    negative: bool
    url: str

@typing.type_check_only
class User(typing.TypedDict, total=False):
    assignedUserRoles: _list[AssignedUserRole]
    displayName: str
    email: str
    lastLoginTime: str
    name: str
    userId: str

@typing.type_check_only
class UserRewardedContentAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    targetingOptionId: str
    userRewardedContent: typing.Literal[
        "USER_REWARDED_CONTENT_UNSPECIFIED",
        "USER_REWARDED_CONTENT_USER_REWARDED",
        "USER_REWARDED_CONTENT_NOT_USER_REWARDED",
    ]

@typing.type_check_only
class UserRewardedContentTargetingOptionDetails(typing.TypedDict, total=False):
    userRewardedContent: typing.Literal[
        "USER_REWARDED_CONTENT_UNSPECIFIED",
        "USER_REWARDED_CONTENT_USER_REWARDED",
        "USER_REWARDED_CONTENT_NOT_USER_REWARDED",
    ]

@typing.type_check_only
class VideoAdInventoryControl(typing.TypedDict, total=False):
    allowInFeed: bool
    allowInStream: bool
    allowNonSkippableInStream: bool
    allowShorts: bool

@typing.type_check_only
class VideoAdSequenceSettings(typing.TypedDict, total=False):
    minimumDuration: typing.Literal[
        "VIDEO_AD_SEQUENCE_MINIMUM_DURATION_UNSPECIFIED",
        "VIDEO_AD_SEQUENCE_MINIMUM_DURATION_WEEK",
        "VIDEO_AD_SEQUENCE_MINIMUM_DURATION_MONTH",
    ]
    steps: _list[VideoAdSequenceStep]

@typing.type_check_only
class VideoAdSequenceStep(typing.TypedDict, total=False):
    adGroupId: str
    interactionType: typing.Literal[
        "INTERACTION_TYPE_UNSPECIFIED",
        "INTERACTION_TYPE_PAID_VIEW",
        "INTERACTION_TYPE_SKIP",
        "INTERACTION_TYPE_IMPRESSION",
        "INTERACTION_TYPE_ENGAGED_IMPRESSION",
    ]
    previousStepId: str
    stepId: str

@typing.type_check_only
class VideoDiscoveryAd(typing.TypedDict, total=False):
    description1: str
    description2: str
    headline: str
    thumbnail: typing.Literal[
        "THUMBNAIL_UNSPECIFIED",
        "THUMBNAIL_DEFAULT",
        "THUMBNAIL_1",
        "THUMBNAIL_2",
        "THUMBNAIL_3",
    ]
    video: YoutubeVideoDetails

@typing.type_check_only
class VideoPerformanceAd(typing.TypedDict, total=False):
    actionButtonLabels: _list[str]
    companionBanners: _list[ImageAsset]
    customParameters: dict[str, typing.Any]
    descriptions: _list[str]
    displayUrlBreadcrumb1: str
    displayUrlBreadcrumb2: str
    domain: str
    finalUrl: str
    headlines: _list[str]
    longHeadlines: _list[str]
    trackingUrl: str
    videos: _list[YoutubeVideoDetails]

@typing.type_check_only
class VideoPlayerSizeAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    videoPlayerSize: typing.Literal[
        "VIDEO_PLAYER_SIZE_UNSPECIFIED",
        "VIDEO_PLAYER_SIZE_SMALL",
        "VIDEO_PLAYER_SIZE_LARGE",
        "VIDEO_PLAYER_SIZE_HD",
        "VIDEO_PLAYER_SIZE_UNKNOWN",
    ]

@typing.type_check_only
class VideoPlayerSizeTargetingOptionDetails(typing.TypedDict, total=False):
    videoPlayerSize: typing.Literal[
        "VIDEO_PLAYER_SIZE_UNSPECIFIED",
        "VIDEO_PLAYER_SIZE_SMALL",
        "VIDEO_PLAYER_SIZE_LARGE",
        "VIDEO_PLAYER_SIZE_HD",
        "VIDEO_PLAYER_SIZE_UNKNOWN",
    ]

@typing.type_check_only
class ViewabilityAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    viewability: typing.Literal[
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
class ViewabilityTargetingOptionDetails(typing.TypedDict, total=False):
    viewability: typing.Literal[
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
class YoutubeAdGroup(typing.TypedDict, total=False):
    adGroupFormat: typing.Literal[
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_UNSPECIFIED",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_IN_STREAM",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_VIDEO_DISCOVERY",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_BUMPER",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_NON_SKIPPABLE_IN_STREAM",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_AUDIO",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_ACTION",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_REACH",
        "YOUTUBE_AND_PARTNERS_AD_GROUP_FORMAT_MASTHEAD",
    ]
    adGroupId: str
    advertiserId: str
    biddingStrategy: YoutubeAndPartnersBiddingStrategy
    displayName: str
    entityStatus: typing.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    lineItemId: str
    name: str
    productFeedData: ProductFeedData
    targetingExpansion: TargetingExpansionConfig
    youtubeAdIds: _list[str]

@typing.type_check_only
class YoutubeAdGroupAd(typing.TypedDict, total=False):
    adGroupAdId: str
    adGroupId: str
    adUrls: _list[AdUrl]
    advertiserId: str
    audioAd: AudioAd
    bumperAd: BumperAd
    displayName: str
    displayVideoSourceAd: DisplayVideoSourceAd
    entityStatus: typing.Literal[
        "ENTITY_STATUS_UNSPECIFIED",
        "ENTITY_STATUS_ACTIVE",
        "ENTITY_STATUS_ARCHIVED",
        "ENTITY_STATUS_DRAFT",
        "ENTITY_STATUS_PAUSED",
        "ENTITY_STATUS_SCHEDULED_FOR_DELETION",
    ]
    inStreamAd: InStreamAd
    mastheadAd: MastheadAd
    name: str
    nonSkippableAd: NonSkippableAd
    videoDiscoverAd: VideoDiscoveryAd
    videoPerformanceAd: VideoPerformanceAd

@typing.type_check_only
class YoutubeAdGroupAssignedTargetingOption(typing.TypedDict, total=False):
    assignedTargetingOption: AssignedTargetingOption
    youtubeAdGroupId: str

@typing.type_check_only
class YoutubeAndPartnersBiddingStrategy(typing.TypedDict, total=False):
    adGroupEffectiveTargetCpaSource: typing.Literal[
        "BIDDING_SOURCE_UNSPECIFIED",
        "BIDDING_SOURCE_LINE_ITEM",
        "BIDDING_SOURCE_AD_GROUP",
    ]
    adGroupEffectiveTargetCpaValue: str
    type: typing.Literal[
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_UNSPECIFIED",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPM",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_RESERVE_CPM",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_LIFT",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSIONS",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPV",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS",
        "YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSION_VALUE",
    ]
    value: str

@typing.type_check_only
class YoutubeAndPartnersInventorySourceConfig(typing.TypedDict, total=False):
    includeGoogleTv: bool
    includeYoutubeSearch: bool
    includeYoutubeVideoPartners: bool
    includeYoutubeVideos: bool

@typing.type_check_only
class YoutubeAndPartnersSettings(typing.TypedDict, total=False):
    biddingStrategy: YoutubeAndPartnersBiddingStrategy
    contentCategory: typing.Literal[
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_UNSPECIFIED",
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_STANDARD",
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_EXPANDED",
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_LIMITED",
    ]
    effectiveContentCategory: typing.Literal[
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_UNSPECIFIED",
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_STANDARD",
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_EXPANDED",
        "YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_LIMITED",
    ]
    inventorySourceSettings: YoutubeAndPartnersInventorySourceConfig
    leadFormId: str
    linkedMerchantId: str
    relatedVideoIds: _list[str]
    targetFrequency: TargetFrequency
    thirdPartyMeasurementSettings: YoutubeAndPartnersThirdPartyMeasurementSettings
    videoAdInventoryControl: VideoAdInventoryControl
    videoAdSequenceSettings: VideoAdSequenceSettings
    viewFrequencyCap: FrequencyCap

@typing.type_check_only
class YoutubeAndPartnersThirdPartyMeasurementSettings(typing.TypedDict, total=False):
    brandLiftVendorConfigs: _list[ThirdPartyVendorConfig]
    brandSafetyVendorConfigs: _list[ThirdPartyVendorConfig]
    reachVendorConfigs: _list[ThirdPartyVendorConfig]
    viewabilityVendorConfigs: _list[ThirdPartyVendorConfig]

@typing.type_check_only
class YoutubeChannelAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    channelId: str
    negative: bool

@typing.type_check_only
class YoutubeChannelPackAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    channelPackId: str
    negative: bool

@typing.type_check_only
class YoutubeVideoAssignedTargetingOptionDetails(typing.TypedDict, total=False):
    negative: bool
    videoId: str

@typing.type_check_only
class YoutubeVideoDetails(typing.TypedDict, total=False):
    id: str
    unavailableReason: typing.Literal[
        "VIDEO_UNAVAILABLE_REASON_UNSPECIFIED",
        "VIDEO_UNAVAILABLE_REASON_PRIVATE",
        "VIDEO_UNAVAILABLE_REASON_DELETED",
    ]
    videoAssetId: str
