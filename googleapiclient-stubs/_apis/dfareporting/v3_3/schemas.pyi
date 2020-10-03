import typing

import typing_extensions

class SkippableSetting(typing_extensions.TypedDict, total=False):
    progressOffset: VideoOffset
    kind: str
    skipOffset: VideoOffset
    skippable: bool

class PlacementsGenerateTagsResponse(typing_extensions.TypedDict, total=False):
    placementTags: typing.List[PlacementTag]
    kind: str

class LastModifiedInfo(typing_extensions.TypedDict, total=False):
    time: str

class Activities(typing_extensions.TypedDict, total=False):
    filters: typing.List[DimensionValue]
    metricNames: typing.List[str]
    kind: str

class DynamicTargetingKey(typing_extensions.TypedDict, total=False):
    name: str
    objectType: typing_extensions.Literal[
        "OBJECT_ADVERTISER", "OBJECT_AD", "OBJECT_CREATIVE", "OBJECT_PLACEMENT"
    ]
    kind: str
    objectId: str

class DayPartTargeting(typing_extensions.TypedDict, total=False):
    daysOfWeek: typing.List[str]
    userLocalTime: bool
    hoursOfDay: typing.List[int]

class CampaignCreativeAssociation(typing_extensions.TypedDict, total=False):
    kind: str
    creativeId: str

class Metro(typing_extensions.TypedDict, total=False):
    countryCode: str
    metroCode: str
    dartId: str
    countryDartId: str
    dmaId: str
    kind: str
    name: str

class City(typing_extensions.TypedDict, total=False):
    regionCode: str
    countryDartId: str
    dartId: str
    regionDartId: str
    kind: str
    countryCode: str
    metroCode: str
    name: str
    metroDmaId: str

class AccountPermissionGroupsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    accountPermissionGroups: typing.List[AccountPermissionGroup]

class CustomFloodlightVariable(typing_extensions.TypedDict, total=False):
    value: str
    kind: str
    type: typing_extensions.Literal[
        "U1",
        "U2",
        "U3",
        "U4",
        "U5",
        "U6",
        "U7",
        "U8",
        "U9",
        "U10",
        "U11",
        "U12",
        "U13",
        "U14",
        "U15",
        "U16",
        "U17",
        "U18",
        "U19",
        "U20",
        "U21",
        "U22",
        "U23",
        "U24",
        "U25",
        "U26",
        "U27",
        "U28",
        "U29",
        "U30",
        "U31",
        "U32",
        "U33",
        "U34",
        "U35",
        "U36",
        "U37",
        "U38",
        "U39",
        "U40",
        "U41",
        "U42",
        "U43",
        "U44",
        "U45",
        "U46",
        "U47",
        "U48",
        "U49",
        "U50",
        "U51",
        "U52",
        "U53",
        "U54",
        "U55",
        "U56",
        "U57",
        "U58",
        "U59",
        "U60",
        "U61",
        "U62",
        "U63",
        "U64",
        "U65",
        "U66",
        "U67",
        "U68",
        "U69",
        "U70",
        "U71",
        "U72",
        "U73",
        "U74",
        "U75",
        "U76",
        "U77",
        "U78",
        "U79",
        "U80",
        "U81",
        "U82",
        "U83",
        "U84",
        "U85",
        "U86",
        "U87",
        "U88",
        "U89",
        "U90",
        "U91",
        "U92",
        "U93",
        "U94",
        "U95",
        "U96",
        "U97",
        "U98",
        "U99",
        "U100",
    ]

class PlacementStrategy(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    accountId: str
    kind: str

class DynamicTargetingKeysListResponse(typing_extensions.TypedDict, total=False):
    dynamicTargetingKeys: typing.List[DynamicTargetingKey]
    kind: str

class Site(typing_extensions.TypedDict, total=False):
    subaccountId: str
    keyName: str
    idDimensionValue: DimensionValue
    accountId: str
    id: str
    directorySiteIdDimensionValue: DimensionValue
    siteContacts: typing.List[SiteContact]
    kind: str
    directorySiteId: str
    siteSettings: SiteSettings
    videoSettings: SiteVideoSettings
    name: str
    approved: bool

class Conversion(typing_extensions.TypedDict, total=False):
    ordinal: str
    quantity: str
    floodlightActivityId: str
    childDirectedTreatment: bool
    value: float
    encryptedUserIdCandidates: typing.List[str]
    floodlightConfigurationId: str
    customVariables: typing.List[CustomFloodlightVariable]
    mobileDeviceId: str
    kind: str
    encryptedUserId: str
    limitAdTracking: bool
    gclid: str
    matchId: str
    timestampMicros: str
    nonPersonalizedAd: bool
    treatmentForUnderage: bool

class TargetWindow(typing_extensions.TypedDict, total=False):
    customHtml: str
    targetWindowOption: typing_extensions.Literal[
        "NEW_WINDOW", "CURRENT_WINDOW", "CUSTOM"
    ]

class PlacementTag(typing_extensions.TypedDict, total=False):
    placementId: str
    tagDatas: typing.List[TagData]

class FloodlightActivitiesGenerateTagResponse(typing_extensions.TypedDict, total=False):
    kind: str
    globalSiteTagGlobalSnippet: str
    floodlightActivityTag: str

class UserRolePermissionGroupsListResponse(typing_extensions.TypedDict, total=False):
    userRolePermissionGroups: typing.List[UserRolePermissionGroup]
    kind: str

class OrderDocument(typing_extensions.TypedDict, total=False):
    id: str
    signed: bool
    cancelled: bool
    advertiserId: str
    approvedByUserProfileIds: typing.List[str]
    kind: str
    type: typing_extensions.Literal[
        "PLANNING_ORDER_TYPE_INSERTION_ORDER", "PLANNING_ORDER_TYPE_CHANGE_ORDER"
    ]
    title: str
    amendedOrderDocumentId: str
    projectId: str
    effectiveDate: str
    accountId: str
    lastSentRecipients: typing.List[str]
    subaccountId: str
    createdInfo: LastModifiedInfo
    orderId: str
    lastSentTime: str

class InventoryItemsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    inventoryItems: typing.List[InventoryItem]
    nextPageToken: str

class DeliverySchedule(typing_extensions.TypedDict, total=False):
    frequencyCap: FrequencyCap
    impressionRatio: str
    hardCutoff: bool
    priority: typing_extensions.Literal[
        "AD_PRIORITY_01",
        "AD_PRIORITY_02",
        "AD_PRIORITY_03",
        "AD_PRIORITY_04",
        "AD_PRIORITY_05",
        "AD_PRIORITY_06",
        "AD_PRIORITY_07",
        "AD_PRIORITY_08",
        "AD_PRIORITY_09",
        "AD_PRIORITY_10",
        "AD_PRIORITY_11",
        "AD_PRIORITY_12",
        "AD_PRIORITY_13",
        "AD_PRIORITY_14",
        "AD_PRIORITY_15",
        "AD_PRIORITY_16",
    ]

class DimensionValue(typing_extensions.TypedDict, total=False):
    matchType: typing_extensions.Literal[
        "EXACT", "BEGINS_WITH", "CONTAINS", "WILDCARD_EXPRESSION"
    ]
    kind: str
    etag: str
    id: str
    value: str
    dimensionName: str

class ConversionError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "INVALID_ARGUMENT", "INTERNAL", "PERMISSION_DENIED", "NOT_FOUND"
    ]
    kind: str
    message: str

class EventTagOverride(typing_extensions.TypedDict, total=False):
    id: str
    enabled: bool

class CompatibleFields(typing_extensions.TypedDict, total=False):
    floodlightReportCompatibleFields: FloodlightReportCompatibleFields
    pathToConversionReportCompatibleFields: PathToConversionReportCompatibleFields
    kind: str
    reachReportCompatibleFields: ReachReportCompatibleFields
    reportCompatibleFields: ReportCompatibleFields
    crossDimensionReachReportCompatibleFields: CrossDimensionReachReportCompatibleFields

class PlacementGroup(typing_extensions.TypedDict, total=False):
    campaignId: str
    contentCategoryId: str
    placementStrategyId: str
    comment: str
    primaryPlacementIdDimensionValue: DimensionValue
    placementGroupType: typing_extensions.Literal[
        "PLACEMENT_PACKAGE", "PLACEMENT_ROADBLOCK"
    ]
    idDimensionValue: DimensionValue
    directorySiteId: str
    lastModifiedInfo: LastModifiedInfo
    archived: bool
    externalId: str
    siteId: str
    primaryPlacementId: str
    siteIdDimensionValue: DimensionValue
    advertiserId: str
    createInfo: LastModifiedInfo
    id: str
    name: str
    pricingSchedule: PricingSchedule
    campaignIdDimensionValue: DimensionValue
    kind: str
    directorySiteIdDimensionValue: DimensionValue
    subaccountId: str
    accountId: str
    childPlacementIds: typing.List[str]
    advertiserIdDimensionValue: DimensionValue

class GeoTargeting(typing_extensions.TypedDict, total=False):
    excludeCountries: bool
    regions: typing.List[Region]
    cities: typing.List[City]
    metros: typing.List[Metro]
    countries: typing.List[Country]
    postalCodes: typing.List[PostalCode]

class TranscodeSetting(typing_extensions.TypedDict, total=False):
    enabledVideoFormats: typing.List[int]
    kind: str

class DirectorySite(typing_extensions.TypedDict, total=False):
    interstitialTagFormats: typing.List[str]
    settings: DirectorySiteSettings
    active: bool
    id: str
    idDimensionValue: DimensionValue
    inpageTagFormats: typing.List[str]
    kind: str
    name: str
    url: str

class TechnologyTargeting(typing_extensions.TypedDict, total=False):
    platformTypes: typing.List[PlatformType]
    connectionTypes: typing.List[ConnectionType]
    browsers: typing.List[Browser]
    operatingSystemVersions: typing.List[OperatingSystemVersion]
    operatingSystems: typing.List[OperatingSystem]
    mobileCarriers: typing.List[MobileCarrier]

class FloodlightActivityPublisherDynamicTag(typing_extensions.TypedDict, total=False):
    dynamicTag: FloodlightActivityDynamicTag
    clickThrough: bool
    directorySiteId: str
    viewThrough: bool
    siteId: str
    siteIdDimensionValue: DimensionValue

class EncryptionInfo(typing_extensions.TypedDict, total=False):
    encryptionSource: typing_extensions.Literal[
        "ENCRYPTION_SCOPE_UNKNOWN", "AD_SERVING", "DATA_TRANSFER"
    ]
    encryptionEntityId: str
    encryptionEntityType: typing_extensions.Literal[
        "ENCRYPTION_ENTITY_TYPE_UNKNOWN",
        "DCM_ACCOUNT",
        "DCM_ADVERTISER",
        "DBM_PARTNER",
        "DBM_ADVERTISER",
        "ADWORDS_CUSTOMER",
        "DFP_NETWORK_CODE",
    ]
    kind: str

class CreativeAssetId(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "IMAGE", "FLASH", "VIDEO", "HTML", "HTML_IMAGE", "AUDIO"
    ]

class CreativeAssignment(typing_extensions.TypedDict, total=False):
    richMediaExitOverrides: typing.List[RichMediaExitOverride]
    weight: int
    creativeId: str
    clickThroughUrl: ClickThroughUrl
    startTime: str
    creativeIdDimensionValue: DimensionValue
    sslCompliant: bool
    endTime: str
    creativeGroupAssignments: typing.List[CreativeGroupAssignment]
    sequence: int
    applyEventTags: bool
    companionCreativeOverrides: typing.List[CompanionClickThroughOverride]
    active: bool

class LanguagesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    languages: typing.List[Language]

class TargetableRemarketingList(typing_extensions.TypedDict, total=False):
    subaccountId: str
    accountId: str
    listSource: typing_extensions.Literal[
        "REMARKETING_LIST_SOURCE_OTHER",
        "REMARKETING_LIST_SOURCE_ADX",
        "REMARKETING_LIST_SOURCE_DFP",
        "REMARKETING_LIST_SOURCE_XFP",
        "REMARKETING_LIST_SOURCE_DFA",
        "REMARKETING_LIST_SOURCE_GA",
        "REMARKETING_LIST_SOURCE_YOUTUBE",
        "REMARKETING_LIST_SOURCE_DBM",
        "REMARKETING_LIST_SOURCE_GPLUS",
        "REMARKETING_LIST_SOURCE_DMP",
        "REMARKETING_LIST_SOURCE_PLAY_STORE",
    ]
    active: bool
    id: str
    kind: str
    listSize: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    name: str
    lifeSpan: str
    description: str

class CreativeGroup(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    subaccountId: str
    groupNumber: int
    advertiserId: str
    kind: str
    advertiserIdDimensionValue: DimensionValue
    accountId: str

class ListPopulationRule(typing_extensions.TypedDict, total=False):
    listPopulationClauses: typing.List[ListPopulationClause]
    floodlightActivityName: str
    floodlightActivityId: str

class AccountPermissionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    accountPermissions: typing.List[AccountPermission]

class ClickThroughUrl(typing_extensions.TypedDict, total=False):
    landingPageId: str
    defaultLandingPage: bool
    customClickThroughUrl: str
    computedClickThroughUrl: str

class RemarketingListShare(typing_extensions.TypedDict, total=False):
    sharedAdvertiserIds: typing.List[str]
    kind: str
    remarketingListId: str
    sharedAccountIds: typing.List[str]

class Country(typing_extensions.TypedDict, total=False):
    sslEnabled: bool
    name: str
    kind: str
    countryCode: str
    dartId: str

class VideoOffset(typing_extensions.TypedDict, total=False):
    offsetSeconds: int
    offsetPercentage: int

class UserRolePermissionsListResponse(typing_extensions.TypedDict, total=False):
    userRolePermissions: typing.List[UserRolePermission]
    kind: str

class EventTag(typing_extensions.TypedDict, total=False):
    name: str
    campaignIdDimensionValue: DimensionValue
    siteIds: typing.List[str]
    id: str
    accountId: str
    status: typing_extensions.Literal["ENABLED", "DISABLED"]
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    type: typing_extensions.Literal[
        "IMPRESSION_IMAGE_EVENT_TAG",
        "IMPRESSION_JAVASCRIPT_EVENT_TAG",
        "CLICK_THROUGH_EVENT_TAG",
    ]
    campaignId: str
    siteFilterType: typing_extensions.Literal["WHITELIST", "BLACKLIST"]
    kind: str
    enabledByDefault: bool
    sslCompliant: bool
    excludeFromAdxRequests: bool
    subaccountId: str
    urlEscapeLevels: int
    url: str

class ListPopulationTerm(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "CUSTOM_VARIABLE_TERM", "LIST_MEMBERSHIP_TERM", "REFERRER_TERM"
    ]
    operator: typing_extensions.Literal[
        "NUM_EQUALS",
        "NUM_LESS_THAN",
        "NUM_LESS_THAN_EQUAL",
        "NUM_GREATER_THAN",
        "NUM_GREATER_THAN_EQUAL",
        "STRING_EQUALS",
        "STRING_CONTAINS",
    ]
    negation: bool
    remarketingListId: str
    variableName: str
    value: str
    contains: bool
    variableFriendlyName: str

class AdsListResponse(typing_extensions.TypedDict, total=False):
    ads: typing.List[Ad]
    nextPageToken: str
    kind: str

class AccountPermission(typing_extensions.TypedDict, total=False):
    id: str
    accountProfiles: typing.List[str]
    kind: str
    name: str
    permissionGroupId: str
    level: typing_extensions.Literal["USER", "ADMINISTRATOR"]

class CompanionSetting(typing_extensions.TypedDict, total=False):
    kind: str
    companionsDisabled: bool
    enabledSizes: typing.List[Size]
    imageOnly: bool

class AccountActiveAdSummary(typing_extensions.TypedDict, total=False):
    availableAds: str
    accountId: str
    activeAds: str
    kind: str
    activeAdsLimitTier: typing_extensions.Literal[
        "ACTIVE_ADS_TIER_40K",
        "ACTIVE_ADS_TIER_75K",
        "ACTIVE_ADS_TIER_100K",
        "ACTIVE_ADS_TIER_200K",
        "ACTIVE_ADS_TIER_300K",
        "ACTIVE_ADS_TIER_500K",
        "ACTIVE_ADS_TIER_750K",
        "ACTIVE_ADS_TIER_1M",
    ]

class File(typing_extensions.TypedDict, total=False):
    urls: typing.Dict[str, typing.Any]
    reportId: str
    etag: str
    id: str
    kind: str
    fileName: str
    format: typing_extensions.Literal["CSV", "EXCEL"]
    dateRange: DateRange
    lastModifiedTime: str
    status: typing_extensions.Literal[
        "PROCESSING", "REPORT_AVAILABLE", "FAILED", "CANCELLED"
    ]

class CampaignCreativeAssociationsListResponse(
    typing_extensions.TypedDict, total=False
):
    campaignCreativeAssociations: typing.List[CampaignCreativeAssociation]
    nextPageToken: str
    kind: str

class OperatingSystemsListResponse(typing_extensions.TypedDict, total=False):
    operatingSystems: typing.List[OperatingSystem]
    kind: str

class DeepLink(typing_extensions.TypedDict, total=False):
    fallbackUrl: str
    kind: str
    remarketingListIds: typing.List[str]
    mobileApp: MobileApp
    appUrl: str

class Flight(typing_extensions.TypedDict, total=False):
    startDate: str
    rateOrCost: str
    endDate: str
    units: str

class CreativesListResponse(typing_extensions.TypedDict, total=False):
    creatives: typing.List[Creative]
    nextPageToken: str
    kind: str

class ConnectionTypesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    connectionTypes: typing.List[ConnectionType]

class ThirdPartyAuthenticationToken(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class Project(typing_extensions.TypedDict, total=False):
    audienceGender: typing_extensions.Literal[
        "PLANNING_AUDIENCE_GENDER_MALE", "PLANNING_AUDIENCE_GENDER_FEMALE"
    ]
    audienceAgeGroup: typing_extensions.Literal[
        "PLANNING_AUDIENCE_AGE_18_24",
        "PLANNING_AUDIENCE_AGE_25_34",
        "PLANNING_AUDIENCE_AGE_35_44",
        "PLANNING_AUDIENCE_AGE_45_54",
        "PLANNING_AUDIENCE_AGE_55_64",
        "PLANNING_AUDIENCE_AGE_65_OR_MORE",
        "PLANNING_AUDIENCE_AGE_UNKNOWN",
    ]
    targetClicks: str
    targetCpmActiveViewNanos: str
    subaccountId: str
    lastModifiedInfo: LastModifiedInfo
    targetImpressions: str
    startDate: str
    targetConversions: str
    advertiserId: str
    budget: str
    endDate: str
    targetCpmNanos: str
    id: str
    kind: str
    overview: str
    accountId: str
    targetCpaNanos: str
    clientName: str
    clientBillingCode: str
    targetCpcNanos: str
    name: str

class PlacementsListResponse(typing_extensions.TypedDict, total=False):
    placements: typing.List[Placement]
    nextPageToken: str
    kind: str

class MobileAppsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    mobileApps: typing.List[MobileApp]
    kind: str

class CitiesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    cities: typing.List[City]

class FloodlightConfigurationsListResponse(typing_extensions.TypedDict, total=False):
    floodlightConfigurations: typing.List[FloodlightConfiguration]
    kind: str

class CampaignsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    campaigns: typing.List[Campaign]
    nextPageToken: str

class Ad(typing_extensions.TypedDict, total=False):
    audienceSegmentId: str
    campaignId: str
    creativeRotation: CreativeRotation
    advertiserIdDimensionValue: DimensionValue
    remarketingListExpression: ListTargetingExpression
    languageTargeting: LanguageTargeting
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    defaultClickThroughEventTagProperties: DefaultClickThroughEventTagProperties
    placementAssignments: typing.List[PlacementAssignment]
    sslRequired: bool
    comments: str
    eventTagOverrides: typing.List[EventTagOverride]
    lastModifiedInfo: LastModifiedInfo
    keyValueTargetingExpression: KeyValueTargetingExpression
    subaccountId: str
    id: str
    sslCompliant: bool
    clickThroughUrlSuffixProperties: ClickThroughUrlSuffixProperties
    dynamicClickTracker: bool
    dayPartTargeting: DayPartTargeting
    archived: bool
    campaignIdDimensionValue: DimensionValue
    clickThroughUrl: ClickThroughUrl
    accountId: str
    endTime: str
    geoTargeting: GeoTargeting
    type: typing_extensions.Literal[
        "AD_SERVING_STANDARD_AD",
        "AD_SERVING_DEFAULT_AD",
        "AD_SERVING_CLICK_TRACKER",
        "AD_SERVING_TRACKING",
        "AD_SERVING_BRAND_SAFE_AD",
    ]
    targetingTemplateId: str
    idDimensionValue: DimensionValue
    deliverySchedule: DeliverySchedule
    advertiserId: str
    kind: str
    startTime: str
    createInfo: LastModifiedInfo
    size: Size
    name: str
    creativeGroupAssignments: typing.List[CreativeGroupAssignment]
    active: bool
    technologyTargeting: TechnologyTargeting

class MobileApp(typing_extensions.TypedDict, total=False):
    id: str
    publisherName: str
    title: str
    directory: typing_extensions.Literal[
        "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_PLAY_STORE"
    ]
    kind: str

class ReportList(typing_extensions.TypedDict, total=False):
    items: typing.List[Report]
    kind: str
    etag: str
    nextPageToken: str

class CreativeCustomEvent(typing_extensions.TypedDict, total=False):
    videoReportingId: str
    popupWindowProperties: PopupWindowProperties
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    targetType: typing_extensions.Literal[
        "TARGET_BLANK", "TARGET_TOP", "TARGET_SELF", "TARGET_PARENT", "TARGET_POPUP"
    ]
    exitClickThroughUrl: CreativeClickThroughUrl
    advertiserCustomEventType: typing_extensions.Literal[
        "ADVERTISER_EVENT_TIMER", "ADVERTISER_EVENT_EXIT", "ADVERTISER_EVENT_COUNTER"
    ]
    artworkLabel: str
    advertiserCustomEventName: str
    advertiserCustomEventId: str
    id: str

class AccountsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    accounts: typing.List[Account]
    kind: str

class ConversionStatus(typing_extensions.TypedDict, total=False):
    kind: str
    errors: typing.List[ConversionError]
    conversion: Conversion

class PostalCode(typing_extensions.TypedDict, total=False):
    countryCode: str
    code: str
    kind: str
    countryDartId: str
    id: str

class CustomViewabilityMetric(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    configuration: CustomViewabilityMetricConfiguration

class FloodlightConfiguration(typing_extensions.TypedDict, total=False):
    advertiserIdDimensionValue: DimensionValue
    analyticsDataSharingEnabled: bool
    inAppAttributionTrackingEnabled: bool
    omnitureSettings: OmnitureSettings
    firstDayOfWeek: typing_extensions.Literal["MONDAY", "SUNDAY"]
    naturalSearchConversionAttributionOption: typing_extensions.Literal[
        "EXCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
        "INCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
        "INCLUDE_NATURAL_SEARCH_TIERED_CONVERSION_ATTRIBUTION",
    ]
    customViewabilityMetric: CustomViewabilityMetric
    idDimensionValue: DimensionValue
    subaccountId: str
    exposureToConversionEnabled: bool
    tagSettings: TagSettings
    id: str
    kind: str
    accountId: str
    userDefinedVariableConfigurations: typing.List[UserDefinedVariableConfiguration]
    lookbackConfiguration: LookbackConfiguration
    thirdPartyAuthenticationTokens: typing.List[ThirdPartyAuthenticationToken]
    advertiserId: str

class SortedDimension(typing_extensions.TypedDict, total=False):
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]
    name: str
    kind: str

class ConversionsBatchInsertResponse(typing_extensions.TypedDict, total=False):
    kind: str
    status: typing.List[ConversionStatus]
    hasFailures: bool

class DimensionFilter(typing_extensions.TypedDict, total=False):
    kind: str
    dimensionName: str
    value: str

class FloodlightActivity(typing_extensions.TypedDict, total=False):
    floodlightConfigurationIdDimensionValue: DimensionValue
    floodlightActivityGroupId: str
    floodlightActivityGroupName: str
    kind: str
    countingMethod: typing_extensions.Literal[
        "STANDARD_COUNTING",
        "UNIQUE_COUNTING",
        "SESSION_COUNTING",
        "TRANSACTIONS_COUNTING",
        "ITEMS_SOLD_COUNTING",
    ]
    floodlightConfigurationId: str
    id: str
    secure: bool
    tagString: str
    floodlightActivityGroupType: typing_extensions.Literal["COUNTER", "SALE"]
    tagFormat: typing_extensions.Literal["HTML", "XHTML"]
    accountId: str
    userDefinedVariableTypes: typing.List[str]
    sslCompliant: bool
    idDimensionValue: DimensionValue
    advertiserIdDimensionValue: DimensionValue
    cacheBustingType: typing_extensions.Literal[
        "JAVASCRIPT", "ACTIVE_SERVER_PAGE", "JSP", "PHP", "COLD_FUSION"
    ]
    defaultTags: typing.List[FloodlightActivityDynamicTag]
    sslRequired: bool
    expectedUrl: str
    floodlightTagType: typing_extensions.Literal["IFRAME", "IMAGE", "GLOBAL_SITE_TAG"]
    publisherTags: typing.List[FloodlightActivityPublisherDynamicTag]
    notes: str
    subaccountId: str
    advertiserId: str
    floodlightActivityGroupTagString: str
    name: str
    hidden: bool

class Rule(typing_extensions.TypedDict, total=False):
    targetingTemplateId: str
    name: str
    assetId: str

class ConnectionType(typing_extensions.TypedDict, total=False):
    kind: str
    id: str
    name: str

class DimensionValueList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    items: typing.List[DimensionValue]
    etag: str

class FileList(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    items: typing.List[File]
    nextPageToken: str

class VideoFormat(typing_extensions.TypedDict, total=False):
    fileType: typing_extensions.Literal["FLV", "THREEGPP", "MP4", "WEBM", "M3U8"]
    resolution: Size
    kind: str
    id: int
    targetBitRate: int

class SubaccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    subaccounts: typing.List[Subaccount]
    nextPageToken: str

class UserRolePermission(typing_extensions.TypedDict, total=False):
    permissionGroupId: str
    name: str
    kind: str
    id: str
    availability: typing_extensions.Literal[
        "NOT_AVAILABLE_BY_DEFAULT",
        "ACCOUNT_BY_DEFAULT",
        "SUBACCOUNT_AND_ACCOUNT_BY_DEFAULT",
        "ACCOUNT_ALWAYS",
        "SUBACCOUNT_AND_ACCOUNT_ALWAYS",
    ]

class PostalCodesListResponse(typing_extensions.TypedDict, total=False):
    postalCodes: typing.List[PostalCode]
    kind: str

class OperatingSystemVersion(typing_extensions.TypedDict, total=False):
    majorVersion: str
    operatingSystem: OperatingSystem
    name: str
    kind: str
    minorVersion: str
    id: str

class Report(typing_extensions.TypedDict, total=False):
    fileName: str
    floodlightCriteria: typing.Dict[str, typing.Any]
    accountId: str
    crossDimensionReachCriteria: typing.Dict[str, typing.Any]
    pathToConversionCriteria: typing.Dict[str, typing.Any]
    ownerProfileId: str
    id: str
    kind: str
    lastModifiedTime: str
    delivery: typing.Dict[str, typing.Any]
    type: typing_extensions.Literal[
        "STANDARD", "REACH", "PATH_TO_CONVERSION", "CROSS_DIMENSION_REACH", "FLOODLIGHT"
    ]
    schedule: typing.Dict[str, typing.Any]
    format: typing_extensions.Literal["CSV", "EXCEL"]
    etag: str
    criteria: typing.Dict[str, typing.Any]
    subAccountId: str
    name: str
    reachCriteria: typing.Dict[str, typing.Any]

class Account(typing_extensions.TypedDict, total=False):
    nielsenOcrEnabled: bool
    activeAdsLimitTier: typing_extensions.Literal[
        "ACTIVE_ADS_TIER_40K",
        "ACTIVE_ADS_TIER_75K",
        "ACTIVE_ADS_TIER_100K",
        "ACTIVE_ADS_TIER_200K",
        "ACTIVE_ADS_TIER_300K",
        "ACTIVE_ADS_TIER_500K",
        "ACTIVE_ADS_TIER_750K",
        "ACTIVE_ADS_TIER_1M",
    ]
    kind: str
    accountPermissionIds: typing.List[str]
    name: str
    activeViewOptOut: bool
    maximumImageSize: str
    reportsConfiguration: ReportsConfiguration
    defaultCreativeSizeId: str
    teaserSizeLimit: str
    countryId: str
    accountProfile: typing_extensions.Literal[
        "ACCOUNT_PROFILE_BASIC", "ACCOUNT_PROFILE_STANDARD"
    ]
    id: str
    availablePermissionIds: typing.List[str]
    active: bool
    currencyId: str
    description: str
    shareReportsWithTwitter: bool
    locale: str

class AdvertiserLandingPagesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    landingPages: typing.List[LandingPage]
    kind: str

class AccountUserProfilesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    accountUserProfiles: typing.List[AccountUserProfile]

class UserProfile(typing_extensions.TypedDict, total=False):
    accountName: str
    subAccountName: str
    profileId: str
    subAccountId: str
    etag: str
    userName: str
    kind: str
    accountId: str

class FsCommand(typing_extensions.TypedDict, total=False):
    top: int
    left: int
    windowWidth: int
    windowHeight: int
    positionOption: typing_extensions.Literal[
        "CENTERED", "DISTANCE_FROM_TOP_LEFT_CORNER"
    ]

class CustomRichMediaEvents(typing_extensions.TypedDict, total=False):
    kind: str
    filteredEventIds: typing.List[DimensionValue]

class OrderDocumentsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    orderDocuments: typing.List[OrderDocument]

class OptimizationActivity(typing_extensions.TypedDict, total=False):
    floodlightActivityIdDimensionValue: DimensionValue
    weight: int
    floodlightActivityId: str

class ThirdPartyTrackingUrl(typing_extensions.TypedDict, total=False):
    url: str
    thirdPartyUrlType: typing_extensions.Literal[
        "IMPRESSION",
        "CLICK_TRACKING",
        "VIDEO_START",
        "VIDEO_FIRST_QUARTILE",
        "VIDEO_MIDPOINT",
        "VIDEO_THIRD_QUARTILE",
        "VIDEO_COMPLETE",
        "VIDEO_MUTE",
        "VIDEO_PAUSE",
        "VIDEO_REWIND",
        "VIDEO_FULLSCREEN",
        "VIDEO_STOP",
        "VIDEO_CUSTOM",
        "SURVEY",
        "RICH_MEDIA_IMPRESSION",
        "RICH_MEDIA_RM_IMPRESSION",
        "RICH_MEDIA_BACKUP_IMPRESSION",
        "VIDEO_SKIP",
        "VIDEO_PROGRESS",
    ]

class MobileCarrier(typing_extensions.TypedDict, total=False):
    kind: str
    countryCode: str
    countryDartId: str
    id: str
    name: str

class FloodlightActivityDynamicTag(typing_extensions.TypedDict, total=False):
    tag: str
    name: str
    id: str

class EventTagsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    eventTags: typing.List[EventTag]

class FloodlightActivityGroup(typing_extensions.TypedDict, total=False):
    advertiserId: str
    floodlightConfigurationId: str
    id: str
    subaccountId: str
    type: typing_extensions.Literal["COUNTER", "SALE"]
    tagString: str
    idDimensionValue: DimensionValue
    advertiserIdDimensionValue: DimensionValue
    name: str
    kind: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    accountId: str

class VideoFormatsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    videoFormats: typing.List[VideoFormat]

class FloodlightReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[Dimension]
    kind: str
    metrics: typing.List[Metric]
    dimensionFilters: typing.List[Dimension]

class ListPopulationClause(typing_extensions.TypedDict, total=False):
    terms: typing.List[ListPopulationTerm]

class CountriesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    countries: typing.List[Country]

class UserRole(typing_extensions.TypedDict, total=False):
    kind: str
    accountId: str
    defaultUserRole: bool
    name: str
    subaccountId: str
    permissions: typing.List[UserRolePermission]
    parentUserRoleId: str
    id: str

class TargetingTemplate(typing_extensions.TypedDict, total=False):
    advertiserId: str
    kind: str
    languageTargeting: LanguageTargeting
    id: str
    subaccountId: str
    dayPartTargeting: DayPartTargeting
    name: str
    geoTargeting: GeoTargeting
    listTargetingExpression: ListTargetingExpression
    accountId: str
    technologyTargeting: TechnologyTargeting
    advertiserIdDimensionValue: DimensionValue
    keyValueTargetingExpression: KeyValueTargetingExpression

class AdBlockingConfiguration(typing_extensions.TypedDict, total=False):
    overrideClickThroughUrl: bool
    clickThroughUrl: str
    creativeBundleId: str
    enabled: bool

class MetrosListResponse(typing_extensions.TypedDict, total=False):
    metros: typing.List[Metro]
    kind: str

class ReportsConfiguration(typing_extensions.TypedDict, total=False):
    reportGenerationTimeZoneId: str
    lookbackConfiguration: LookbackConfiguration
    exposureToConversionEnabled: bool

class Dimension(typing_extensions.TypedDict, total=False):
    name: str
    kind: str

class CreativeRotation(typing_extensions.TypedDict, total=False):
    weightCalculationStrategy: typing_extensions.Literal[
        "WEIGHT_STRATEGY_EQUAL",
        "WEIGHT_STRATEGY_CUSTOM",
        "WEIGHT_STRATEGY_HIGHEST_CTR",
        "WEIGHT_STRATEGY_OPTIMIZED",
    ]
    creativeOptimizationConfigurationId: str
    creativeAssignments: typing.List[CreativeAssignment]
    type: typing_extensions.Literal[
        "CREATIVE_ROTATION_TYPE_SEQUENTIAL", "CREATIVE_ROTATION_TYPE_RANDOM"
    ]

class OffsetPosition(typing_extensions.TypedDict, total=False):
    left: int
    top: int

class PlacementGroupsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    placementGroups: typing.List[PlacementGroup]

class ObjectFilter(typing_extensions.TypedDict, total=False):
    kind: str
    status: typing_extensions.Literal["NONE", "ASSIGNED", "ALL"]
    objectIds: typing.List[str]

class ClickTag(typing_extensions.TypedDict, total=False):
    name: str
    eventName: str
    clickThroughUrl: CreativeClickThroughUrl

class AccountPermissionGroup(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    kind: str

class CreativeAsset(typing_extensions.TypedDict, total=False):
    duration: int
    mediaDuration: float
    backupImageExit: CreativeCustomEvent
    id: str
    additionalSizes: typing.List[Size]
    transparency: bool
    assetIdentifier: CreativeAssetId
    zipFilename: str
    expandedDimension: Size
    positionLeftUnit: typing_extensions.Literal[
        "OFFSET_UNIT_PIXEL", "OFFSET_UNIT_PERCENT", "OFFSET_UNIT_PIXEL_FROM_CENTER"
    ]
    streamingServingUrl: str
    alignment: typing_extensions.Literal[
        "ALIGNMENT_TOP", "ALIGNMENT_RIGHT", "ALIGNMENT_BOTTOM", "ALIGNMENT_LEFT"
    ]
    active: bool
    zIndex: int
    sslCompliant: bool
    audioBitRate: int
    progressiveServingUrl: str
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    verticallyLocked: bool
    pushdownDuration: float
    orientation: typing_extensions.Literal["LANDSCAPE", "PORTRAIT", "SQUARE"]
    windowMode: typing_extensions.Literal["OPAQUE", "WINDOW", "TRANSPARENT"]
    fileSize: str
    positionTopUnit: typing_extensions.Literal[
        "OFFSET_UNIT_PIXEL", "OFFSET_UNIT_PERCENT", "OFFSET_UNIT_PIXEL_FROM_CENTER"
    ]
    position: OffsetPosition
    customStartTimeValue: int
    offset: OffsetPosition
    collapsedSize: Size
    frameRate: float
    role: typing_extensions.Literal[
        "PRIMARY",
        "BACKUP_IMAGE",
        "ADDITIONAL_IMAGE",
        "ADDITIONAL_FLASH",
        "PARENT_VIDEO",
        "TRANSCODED_VIDEO",
        "OTHER",
        "ALTERNATE_VIDEO",
        "PARENT_AUDIO",
        "TRANSCODED_AUDIO",
    ]
    detectedFeatures: typing.List[str]
    size: Size
    bitRate: int
    originalBackup: bool
    hideSelectionBoxes: bool
    actionScript3: bool
    companionCreativeIds: typing.List[str]
    horizontallyLocked: bool
    hideFlashObjects: bool
    zipFilesize: str
    startTimeType: typing_extensions.Literal[
        "ASSET_START_TIME_TYPE_NONE", "ASSET_START_TIME_TYPE_CUSTOM"
    ]
    idDimensionValue: DimensionValue
    childAssetType: typing_extensions.Literal[
        "CHILD_ASSET_TYPE_FLASH",
        "CHILD_ASSET_TYPE_VIDEO",
        "CHILD_ASSET_TYPE_IMAGE",
        "CHILD_ASSET_TYPE_DATA",
    ]
    durationType: typing_extensions.Literal[
        "ASSET_DURATION_TYPE_AUTO",
        "ASSET_DURATION_TYPE_NONE",
        "ASSET_DURATION_TYPE_CUSTOM",
    ]
    flashVersion: int
    audioSampleRate: int
    politeLoad: bool
    mimeType: str
    pushdown: bool
    displayType: typing_extensions.Literal[
        "ASSET_DISPLAY_TYPE_INPAGE",
        "ASSET_DISPLAY_TYPE_FLOATING",
        "ASSET_DISPLAY_TYPE_OVERLAY",
        "ASSET_DISPLAY_TYPE_EXPANDING",
        "ASSET_DISPLAY_TYPE_FLASH_IN_FLASH",
        "ASSET_DISPLAY_TYPE_FLASH_IN_FLASH_EXPANDING",
        "ASSET_DISPLAY_TYPE_PEEL_DOWN",
        "ASSET_DISPLAY_TYPE_VPAID_LINEAR",
        "ASSET_DISPLAY_TYPE_VPAID_NON_LINEAR",
        "ASSET_DISPLAY_TYPE_BACKDROP",
    ]

class OmnitureSettings(typing_extensions.TypedDict, total=False):
    omnitureCostDataEnabled: bool
    omnitureIntegrationEnabled: bool

class DefaultClickThroughEventTagProperties(typing_extensions.TypedDict, total=False):
    overrideInheritedEventTag: bool
    defaultClickThroughEventTagId: str

class CreativeFieldValue(typing_extensions.TypedDict, total=False):
    value: str
    id: str
    kind: str

class Placement(typing_extensions.TypedDict, total=False):
    subaccountId: str
    comment: str
    id: str
    createInfo: LastModifiedInfo
    sslRequired: bool
    directorySiteId: str
    size: Size
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    videoSettings: VideoSettings
    lastModifiedInfo: LastModifiedInfo
    keyName: str
    name: str
    externalId: str
    directorySiteIdDimensionValue: DimensionValue
    paymentSource: typing_extensions.Literal[
        "PLACEMENT_AGENCY_PAID", "PLACEMENT_PUBLISHER_PAID"
    ]
    campaignId: str
    tagFormats: typing.List[str]
    archived: bool
    lookbackConfiguration: LookbackConfiguration
    accountId: str
    advertiserId: str
    kind: str
    tagSetting: TagSetting
    videoActiveViewOptOut: bool
    placementGroupId: str
    campaignIdDimensionValue: DimensionValue
    paymentApproved: bool
    placementGroupIdDimensionValue: DimensionValue
    placementStrategyId: str
    primary: bool
    pricingSchedule: PricingSchedule
    contentCategoryId: str
    publisherUpdateInfo: LastModifiedInfo
    siteId: str
    advertiserIdDimensionValue: DimensionValue
    vpaidAdapterChoice: typing_extensions.Literal["DEFAULT", "FLASH", "HTML5", "BOTH"]
    status: typing_extensions.Literal[
        "PENDING_REVIEW",
        "PAYMENT_ACCEPTED",
        "PAYMENT_REJECTED",
        "ACKNOWLEDGE_REJECTION",
        "ACKNOWLEDGE_ACCEPTANCE",
        "DRAFT",
    ]
    idDimensionValue: DimensionValue
    siteIdDimensionValue: DimensionValue
    additionalSizes: typing.List[Size]
    adBlockingOptOut: bool

class TagSettings(typing_extensions.TypedDict, total=False):
    imageTagEnabled: bool
    dynamicTagEnabled: bool

class Recipient(typing_extensions.TypedDict, total=False):
    kind: str
    email: str
    deliveryType: typing_extensions.Literal["LINK", "ATTACHMENT"]

class SiteContact(typing_extensions.TypedDict, total=False):
    email: str
    address: str
    lastName: str
    contactType: typing_extensions.Literal["SALES_PERSON", "TRAFFICKER"]
    id: str
    title: str
    phone: str
    firstName: str

class CreativeAssetSelection(typing_extensions.TypedDict, total=False):
    rules: typing.List[Rule]
    defaultAssetId: str

class SiteVideoSettings(typing_extensions.TypedDict, total=False):
    skippableSettings: SiteSkippableSetting
    kind: str
    transcodeSettings: SiteTranscodeSetting
    orientation: typing_extensions.Literal["ANY", "LANDSCAPE", "PORTRAIT"]
    companionSettings: SiteCompanionSetting

class LookbackConfiguration(typing_extensions.TypedDict, total=False):
    postImpressionActivitiesDuration: int
    clickDuration: int

class RemarketingListsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    remarketingLists: typing.List[RemarketingList]

class OperatingSystem(typing_extensions.TypedDict, total=False):
    desktop: bool
    dartId: str
    kind: str
    mobile: bool
    name: str

class PlacementAssignment(typing_extensions.TypedDict, total=False):
    placementId: str
    placementIdDimensionValue: DimensionValue
    sslRequired: bool
    active: bool

class PlatformTypesListResponse(typing_extensions.TypedDict, total=False):
    platformTypes: typing.List[PlatformType]
    kind: str

class InventoryItem(typing_extensions.TypedDict, total=False):
    estimatedConversionRate: str
    name: str
    orderId: str
    projectId: str
    kind: str
    placementStrategyId: str
    type: typing_extensions.Literal[
        "PLANNING_PLACEMENT_TYPE_REGULAR", "PLANNING_PLACEMENT_TYPE_CREDIT"
    ]
    rfpId: str
    lastModifiedInfo: LastModifiedInfo
    pricing: Pricing
    inPlan: bool
    siteId: str
    estimatedClickThroughRate: str
    subaccountId: str
    accountId: str
    advertiserId: str
    id: str
    contentCategoryId: str
    adSlots: typing.List[AdSlot]
    negotiationChannelId: str

class BrowsersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    browsers: typing.List[Browser]

class FrequencyCap(typing_extensions.TypedDict, total=False):
    duration: str
    impressions: str

class CreativeFieldsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    creativeFields: typing.List[CreativeField]

class ConversionsBatchUpdateResponse(typing_extensions.TypedDict, total=False):
    kind: str
    status: typing.List[ConversionStatus]
    hasFailures: bool

class UserProfileList(typing_extensions.TypedDict, total=False):
    items: typing.List[UserProfile]
    etag: str
    kind: str

class Browser(typing_extensions.TypedDict, total=False):
    kind: str
    minorVersion: str
    name: str
    dartId: str
    browserVersionId: str
    majorVersion: str

class ConversionsBatchUpdateRequest(typing_extensions.TypedDict, total=False):
    kind: str
    encryptionInfo: EncryptionInfo
    conversions: typing.List[Conversion]

class OrderContact(typing_extensions.TypedDict, total=False):
    contactInfo: str
    signatureUserProfileId: str
    contactName: str
    contactType: typing_extensions.Literal[
        "PLANNING_ORDER_CONTACT_BUYER_CONTACT",
        "PLANNING_ORDER_CONTACT_BUYER_BILLING_CONTACT",
        "PLANNING_ORDER_CONTACT_SELLER_CONTACT",
    ]
    contactTitle: str

class CreativeGroupAssignment(typing_extensions.TypedDict, total=False):
    creativeGroupNumber: typing_extensions.Literal[
        "CREATIVE_GROUP_ONE", "CREATIVE_GROUP_TWO"
    ]
    creativeGroupId: str

class SizesListResponse(typing_extensions.TypedDict, total=False):
    sizes: typing.List[Size]
    kind: str

class LandingPage(typing_extensions.TypedDict, total=False):
    archived: bool
    url: str
    id: str
    name: str
    kind: str
    deepLinks: typing.List[DeepLink]
    advertiserId: str

class ProjectsListResponse(typing_extensions.TypedDict, total=False):
    projects: typing.List[Project]
    kind: str
    nextPageToken: str

class FloodlightActivityGroupsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    floodlightActivityGroups: typing.List[FloodlightActivityGroup]

class CrossDimensionReachReportCompatibleFields(
    typing_extensions.TypedDict, total=False
):
    metrics: typing.List[Metric]
    breakdown: typing.List[Dimension]
    kind: str
    dimensionFilters: typing.List[Dimension]
    overlapMetrics: typing.List[Metric]

class ChangeLog(typing_extensions.TypedDict, total=False):
    oldValue: str
    objectType: str
    fieldName: str
    changeTime: str
    transactionId: str
    newValue: str
    objectId: str
    action: str
    id: str
    subaccountId: str
    userProfileId: str
    kind: str
    accountId: str
    userProfileName: str

class DirectorySitesListResponse(typing_extensions.TypedDict, total=False):
    directorySites: typing.List[DirectorySite]
    kind: str
    nextPageToken: str

class Metric(typing_extensions.TypedDict, total=False):
    name: str
    kind: str

class LanguageTargeting(typing_extensions.TypedDict, total=False):
    languages: typing.List[Language]

class Order(typing_extensions.TypedDict, total=False):
    sellerOrderId: str
    id: str
    projectId: str
    siteId: typing.List[str]
    buyerInvoiceId: str
    notes: str
    accountId: str
    termsAndConditions: str
    name: str
    subaccountId: str
    advertiserId: str
    contacts: typing.List[OrderContact]
    sellerOrganizationName: str
    planningTermId: str
    siteNames: typing.List[str]
    buyerOrganizationName: str
    kind: str
    comments: str
    lastModifiedInfo: LastModifiedInfo
    approverUserProfileIds: typing.List[str]

class PricingSchedulePricingPeriod(typing_extensions.TypedDict, total=False):
    pricingComment: str
    endDate: str
    startDate: str
    units: str
    rateOrCostNanos: str

class Advertiser(typing_extensions.TypedDict, total=False):
    kind: str
    originalFloodlightConfigurationId: str
    accountId: str
    defaultEmail: str
    advertiserGroupId: str
    idDimensionValue: DimensionValue
    suspended: bool
    clickThroughUrlSuffix: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    name: str
    id: str
    floodlightConfigurationId: str
    defaultClickThroughEventTagId: str
    subaccountId: str
    status: typing_extensions.Literal["APPROVED", "ON_HOLD"]

class CreativeOptimizationConfiguration(typing_extensions.TypedDict, total=False):
    optimizationActivitys: typing.List[OptimizationActivity]
    optimizationModel: typing_extensions.Literal[
        "CLICK",
        "POST_CLICK",
        "POST_IMPRESSION",
        "POST_CLICK_AND_IMPRESSION",
        "VIDEO_COMPLETION",
    ]
    name: str
    id: str

class RichMediaExitOverride(typing_extensions.TypedDict, total=False):
    enabled: bool
    exitId: str
    clickThroughUrl: ClickThroughUrl

class ConversionsBatchInsertRequest(typing_extensions.TypedDict, total=False):
    conversions: typing.List[Conversion]
    kind: str
    encryptionInfo: EncryptionInfo

class UserRolePermissionGroup(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

class SiteSkippableSetting(typing_extensions.TypedDict, total=False):
    skippable: bool
    skipOffset: VideoOffset
    kind: str
    progressOffset: VideoOffset

class Creative(typing_extensions.TypedDict, total=False):
    thirdPartyRichMediaImpressionsUrl: str
    totalFileSize: str
    backupImageClickThroughUrl: CreativeClickThroughUrl
    thirdPartyUrls: typing.List[ThirdPartyTrackingUrl]
    backupImageReportingLabel: str
    overrideCss: str
    counterCustomEvents: typing.List[CreativeCustomEvent]
    progressOffset: VideoOffset
    convertFlashToHtml5: bool
    backupImageTargetWindow: TargetWindow
    latestTraffickedCreativeId: str
    authoringSource: typing_extensions.Literal[
        "CREATIVE_AUTHORING_SOURCE_DCM",
        "CREATIVE_AUTHORING_SOURCE_DBM",
        "CREATIVE_AUTHORING_SOURCE_STUDIO",
    ]
    clickTags: typing.List[ClickTag]
    htmlCode: str
    customKeyValues: typing.List[str]
    timerCustomEvents: typing.List[CreativeCustomEvent]
    adTagKeys: typing.List[str]
    universalAdId: UniversalAdId
    subaccountId: str
    skipOffset: VideoOffset
    id: str
    creativeAssets: typing.List[CreativeAsset]
    accountId: str
    dynamicAssetSelection: bool
    allowScriptAccess: bool
    requiredFlashPluginVersion: str
    compatibility: typing.List[str]
    thirdPartyBackupImageImpressionsUrl: str
    advertiserId: str
    backupImageFeatures: typing.List[str]
    skippable: bool
    size: Size
    name: str
    active: bool
    requiredFlashVersion: int
    redirectUrl: str
    backgroundColor: str
    renderingId: str
    adParameters: str
    kind: str
    additionalSizes: typing.List[Size]
    autoAdvanceImages: bool
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    renderingIdDimensionValue: DimensionValue
    companionCreatives: typing.List[str]
    sslCompliant: bool
    mediaDuration: float
    authoringTool: typing_extensions.Literal["NINJA", "SWIFFY"]
    lastModifiedInfo: LastModifiedInfo
    fsCommand: FsCommand
    creativeFieldAssignments: typing.List[CreativeFieldAssignment]
    commercialId: str
    htmlCodeLocked: bool
    exitCustomEvents: typing.List[CreativeCustomEvent]
    studioTraffickedCreativeId: str
    type: typing_extensions.Literal[
        "IMAGE",
        "DISPLAY_REDIRECT",
        "CUSTOM_DISPLAY",
        "INTERNAL_REDIRECT",
        "CUSTOM_DISPLAY_INTERSTITIAL",
        "INTERSTITIAL_INTERNAL_REDIRECT",
        "TRACKING_TEXT",
        "RICH_MEDIA_DISPLAY_BANNER",
        "RICH_MEDIA_INPAGE_FLOATING",
        "RICH_MEDIA_IM_EXPAND",
        "RICH_MEDIA_DISPLAY_EXPANDING",
        "RICH_MEDIA_DISPLAY_INTERSTITIAL",
        "RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL",
        "RICH_MEDIA_MOBILE_IN_APP",
        "FLASH_INPAGE",
        "INSTREAM_VIDEO",
        "VPAID_LINEAR_VIDEO",
        "VPAID_NON_LINEAR_VIDEO",
        "INSTREAM_VIDEO_REDIRECT",
        "RICH_MEDIA_PEEL_DOWN",
        "HTML5_BANNER",
        "DISPLAY",
        "DISPLAY_IMAGE_GALLERY",
        "BRAND_SAFE_DEFAULT_INSTREAM_VIDEO",
        "INSTREAM_AUDIO",
    ]
    creativeAssetSelection: CreativeAssetSelection
    idDimensionValue: DimensionValue
    version: int
    studioCreativeId: str
    studioAdvertiserId: str
    archived: bool
    mediaDescription: str
    sslOverride: bool

class Campaign(typing_extensions.TypedDict, total=False):
    advertiserGroupId: str
    name: str
    defaultClickThroughEventTagProperties: DefaultClickThroughEventTagProperties
    subaccountId: str
    advertiserId: str
    startDate: str
    endDate: str
    audienceSegmentGroups: typing.List[AudienceSegmentGroup]
    adBlockingConfiguration: AdBlockingConfiguration
    accountId: str
    advertiserIdDimensionValue: DimensionValue
    creativeGroupIds: typing.List[str]
    billingInvoiceCode: str
    lastModifiedInfo: LastModifiedInfo
    id: str
    creativeOptimizationConfiguration: CreativeOptimizationConfiguration
    archived: bool
    kind: str
    defaultLandingPageId: str
    eventTagOverrides: typing.List[EventTagOverride]
    additionalCreativeOptimizationConfigurations: typing.List[
        CreativeOptimizationConfiguration
    ]
    externalId: str
    nielsenOcrEnabled: bool
    clickThroughUrlSuffixProperties: ClickThroughUrlSuffixProperties
    comment: str
    createInfo: LastModifiedInfo
    idDimensionValue: DimensionValue
    traffickerEmails: typing.List[str]

class ReportCompatibleFields(typing_extensions.TypedDict, total=False):
    pivotedActivityMetrics: typing.List[Metric]
    dimensions: typing.List[Dimension]
    dimensionFilters: typing.List[Dimension]
    kind: str
    metrics: typing.List[Metric]

class PricingSchedule(typing_extensions.TypedDict, total=False):
    floodlightActivityId: str
    endDate: str
    disregardOverdelivery: bool
    testingStartDate: str
    capCostOption: typing_extensions.Literal[
        "CAP_COST_NONE", "CAP_COST_MONTHLY", "CAP_COST_CUMULATIVE"
    ]
    pricingType: typing_extensions.Literal[
        "PRICING_TYPE_CPM",
        "PRICING_TYPE_CPC",
        "PRICING_TYPE_CPA",
        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
        "PRICING_TYPE_FLAT_RATE_CLICKS",
        "PRICING_TYPE_CPM_ACTIVEVIEW",
    ]
    startDate: str
    pricingPeriods: typing.List[PricingSchedulePricingPeriod]
    flighted: bool

class AudienceSegment(typing_extensions.TypedDict, total=False):
    name: str
    allocation: int
    id: str

class AudienceSegmentGroup(typing_extensions.TypedDict, total=False):
    audienceSegments: typing.List[AudienceSegment]
    id: str
    name: str

class Subaccount(typing_extensions.TypedDict, total=False):
    kind: str
    id: str
    name: str
    availablePermissionIds: typing.List[str]
    accountId: str

class Size(typing_extensions.TypedDict, total=False):
    kind: str
    width: int
    id: str
    iab: bool
    height: int

class OperatingSystemVersionsListResponse(typing_extensions.TypedDict, total=False):
    operatingSystemVersions: typing.List[OperatingSystemVersion]
    kind: str

class MobileCarriersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    mobileCarriers: typing.List[MobileCarrier]

class SitesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    sites: typing.List[Site]

class TargetingTemplatesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    targetingTemplates: typing.List[TargetingTemplate]
    kind: str

class UniversalAdId(typing_extensions.TypedDict, total=False):
    registry: typing_extensions.Literal["OTHER", "AD_ID.ORG", "CLEARCAST", "DCM"]
    value: str

class CustomViewabilityMetricConfiguration(typing_extensions.TypedDict, total=False):
    viewabilityPercent: int
    timePercent: int
    timeMillis: int
    audible: bool

class UserRolesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    userRoles: typing.List[UserRole]

class Language(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    languageCode: str
    kind: str

class FloodlightActivitiesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    floodlightActivities: typing.List[FloodlightActivity]
    kind: str

class CreativeFieldAssignment(typing_extensions.TypedDict, total=False):
    creativeFieldValueId: str
    creativeFieldId: str

class PlatformType(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    id: str

class KeyValueTargetingExpression(typing_extensions.TypedDict, total=False):
    expression: str

class UserDefinedVariableConfiguration(typing_extensions.TypedDict, total=False):
    variableType: typing_extensions.Literal[
        "U1",
        "U2",
        "U3",
        "U4",
        "U5",
        "U6",
        "U7",
        "U8",
        "U9",
        "U10",
        "U11",
        "U12",
        "U13",
        "U14",
        "U15",
        "U16",
        "U17",
        "U18",
        "U19",
        "U20",
        "U21",
        "U22",
        "U23",
        "U24",
        "U25",
        "U26",
        "U27",
        "U28",
        "U29",
        "U30",
        "U31",
        "U32",
        "U33",
        "U34",
        "U35",
        "U36",
        "U37",
        "U38",
        "U39",
        "U40",
        "U41",
        "U42",
        "U43",
        "U44",
        "U45",
        "U46",
        "U47",
        "U48",
        "U49",
        "U50",
        "U51",
        "U52",
        "U53",
        "U54",
        "U55",
        "U56",
        "U57",
        "U58",
        "U59",
        "U60",
        "U61",
        "U62",
        "U63",
        "U64",
        "U65",
        "U66",
        "U67",
        "U68",
        "U69",
        "U70",
        "U71",
        "U72",
        "U73",
        "U74",
        "U75",
        "U76",
        "U77",
        "U78",
        "U79",
        "U80",
        "U81",
        "U82",
        "U83",
        "U84",
        "U85",
        "U86",
        "U87",
        "U88",
        "U89",
        "U90",
        "U91",
        "U92",
        "U93",
        "U94",
        "U95",
        "U96",
        "U97",
        "U98",
        "U99",
        "U100",
    ]
    dataType: typing_extensions.Literal["STRING", "NUMBER"]
    reportName: str

class DirectorySiteSettings(typing_extensions.TypedDict, total=False):
    dfpSettings: DfpSettings
    instreamVideoPlacementAccepted: bool
    interstitialPlacementAccepted: bool
    activeViewOptOut: bool

class RemarketingList(typing_extensions.TypedDict, total=False):
    active: bool
    advertiserIdDimensionValue: DimensionValue
    lifeSpan: str
    id: str
    subaccountId: str
    name: str
    kind: str
    listPopulationRule: ListPopulationRule
    listSource: typing_extensions.Literal[
        "REMARKETING_LIST_SOURCE_OTHER",
        "REMARKETING_LIST_SOURCE_ADX",
        "REMARKETING_LIST_SOURCE_DFP",
        "REMARKETING_LIST_SOURCE_XFP",
        "REMARKETING_LIST_SOURCE_DFA",
        "REMARKETING_LIST_SOURCE_GA",
        "REMARKETING_LIST_SOURCE_YOUTUBE",
        "REMARKETING_LIST_SOURCE_DBM",
        "REMARKETING_LIST_SOURCE_GPLUS",
        "REMARKETING_LIST_SOURCE_DMP",
        "REMARKETING_LIST_SOURCE_PLAY_STORE",
    ]
    accountId: str
    description: str
    listSize: str
    advertiserId: str

class DateRange(typing_extensions.TypedDict, total=False):
    relativeDateRange: typing_extensions.Literal[
        "TODAY",
        "YESTERDAY",
        "WEEK_TO_DATE",
        "MONTH_TO_DATE",
        "QUARTER_TO_DATE",
        "YEAR_TO_DATE",
        "PREVIOUS_WEEK",
        "PREVIOUS_MONTH",
        "PREVIOUS_QUARTER",
        "PREVIOUS_YEAR",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
        "LAST_365_DAYS",
        "LAST_24_MONTHS",
        "LAST_14_DAYS",
        "LAST_60_DAYS",
    ]
    endDate: str
    startDate: str
    kind: str

class ReachReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensionFilters: typing.List[Dimension]
    kind: str
    pivotedActivityMetrics: typing.List[Metric]
    reachByFrequencyMetrics: typing.List[Metric]
    metrics: typing.List[Metric]
    dimensions: typing.List[Dimension]

class CreativeFieldValuesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    creativeFieldValues: typing.List[CreativeFieldValue]

class DfpSettings(typing_extensions.TypedDict, total=False):
    programmaticPlacementAccepted: bool
    publisherPortalOnly: bool
    dfpNetworkCode: str
    dfpNetworkName: str
    pubPaidPlacementAccepted: bool

class AccountUserProfile(typing_extensions.TypedDict, total=False):
    userRoleId: str
    comments: str
    locale: str
    siteFilter: ObjectFilter
    active: bool
    id: str
    userAccessType: typing_extensions.Literal[
        "NORMAL_USER", "SUPER_USER", "INTERNAL_ADMINISTRATOR", "READ_ONLY_SUPER_USER"
    ]
    subaccountId: str
    name: str
    email: str
    advertiserFilter: ObjectFilter
    campaignFilter: ObjectFilter
    traffickerType: typing_extensions.Literal[
        "INTERNAL_NON_TRAFFICKER", "INTERNAL_TRAFFICKER", "EXTERNAL_TRAFFICKER"
    ]
    kind: str
    userRoleFilter: ObjectFilter
    accountId: str

class CreativeAssetMetadata(typing_extensions.TypedDict, total=False):
    detectedFeatures: typing.List[str]
    idDimensionValue: DimensionValue
    kind: str
    assetIdentifier: CreativeAssetId
    clickTags: typing.List[ClickTag]
    warnedValidationRules: typing.List[str]
    id: str

class ContentCategory(typing_extensions.TypedDict, total=False):
    id: str
    accountId: str
    name: str
    kind: str

class RegionsListResponse(typing_extensions.TypedDict, total=False):
    regions: typing.List[Region]
    kind: str

class PathToConversionReportCompatibleFields(typing_extensions.TypedDict, total=False):
    conversionDimensions: typing.List[Dimension]
    kind: str
    metrics: typing.List[Metric]
    perInteractionDimensions: typing.List[Dimension]
    customFloodlightVariables: typing.List[Dimension]

class DimensionValueRequest(typing_extensions.TypedDict, total=False):
    filters: typing.List[DimensionFilter]
    dimensionName: str
    startDate: str
    endDate: str
    kind: str

class TagSetting(typing_extensions.TypedDict, total=False):
    additionalKeyValues: str
    includeClickTracking: bool
    keywordOption: typing_extensions.Literal[
        "PLACEHOLDER_WITH_LIST_OF_KEYWORDS",
        "IGNORE",
        "GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD",
    ]
    includeClickThroughUrls: bool

class TargetableRemarketingListsListResponse(typing_extensions.TypedDict, total=False):
    targetableRemarketingLists: typing.List[TargetableRemarketingList]
    kind: str
    nextPageToken: str

class AdvertiserGroupsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    advertiserGroups: typing.List[AdvertiserGroup]
    kind: str

class SiteSettings(typing_extensions.TypedDict, total=False):
    tagSetting: TagSetting
    activeViewOptOut: bool
    disableNewCookie: bool
    videoActiveViewOptOutTemplate: bool
    adBlockingOptOut: bool
    vpaidAdapterChoiceTemplate: typing_extensions.Literal[
        "DEFAULT", "FLASH", "HTML5", "BOTH"
    ]

class CreativeClickThroughUrl(typing_extensions.TypedDict, total=False):
    computedClickThroughUrl: str
    customClickThroughUrl: str
    landingPageId: str

class ContentCategoriesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    contentCategories: typing.List[ContentCategory]

class CreativeField(typing_extensions.TypedDict, total=False):
    id: str
    accountId: str
    advertiserId: str
    subaccountId: str
    kind: str
    advertiserIdDimensionValue: DimensionValue
    name: str

class OrdersListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    orders: typing.List[Order]

class CreativeGroupsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    creativeGroups: typing.List[CreativeGroup]
    nextPageToken: str

class SiteTranscodeSetting(typing_extensions.TypedDict, total=False):
    kind: str
    enabledVideoFormats: typing.List[int]

class AdvertiserGroup(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    kind: str
    accountId: str

class ChangeLogsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    changeLogs: typing.List[ChangeLog]
    nextPageToken: str

class AdvertisersListResponse(typing_extensions.TypedDict, total=False):
    advertisers: typing.List[Advertiser]
    kind: str
    nextPageToken: str

class PopupWindowProperties(typing_extensions.TypedDict, total=False):
    showAddressBar: bool
    showToolBar: bool
    showScrollBar: bool
    dimension: Size
    showMenuBar: bool
    positionType: typing_extensions.Literal["CENTER", "COORDINATES"]
    offset: OffsetPosition
    showStatusBar: bool
    title: str

class ClickThroughUrlSuffixProperties(typing_extensions.TypedDict, total=False):
    overrideInheritedSuffix: bool
    clickThroughUrlSuffix: str

class PlacementStrategiesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    placementStrategies: typing.List[PlacementStrategy]
    kind: str

class ListTargetingExpression(typing_extensions.TypedDict, total=False):
    expression: str

class SiteCompanionSetting(typing_extensions.TypedDict, total=False):
    imageOnly: bool
    kind: str
    enabledSizes: typing.List[Size]
    companionsDisabled: bool

class CompanionClickThroughOverride(typing_extensions.TypedDict, total=False):
    clickThroughUrl: ClickThroughUrl
    creativeId: str

class TagData(typing_extensions.TypedDict, total=False):
    impressionTag: str
    clickTag: str
    format: typing_extensions.Literal[
        "PLACEMENT_TAG_STANDARD",
        "PLACEMENT_TAG_IFRAME_JAVASCRIPT",
        "PLACEMENT_TAG_IFRAME_ILAYER",
        "PLACEMENT_TAG_INTERNAL_REDIRECT",
        "PLACEMENT_TAG_JAVASCRIPT",
        "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT",
        "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT",
        "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT",
        "PLACEMENT_TAG_CLICK_COMMANDS",
        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH",
        "PLACEMENT_TAG_TRACKING",
        "PLACEMENT_TAG_TRACKING_IFRAME",
        "PLACEMENT_TAG_TRACKING_JAVASCRIPT",
        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3",
        "PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY",
        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4",
    ]
    creativeId: str
    adId: str

class Region(typing_extensions.TypedDict, total=False):
    regionCode: str
    name: str
    countryCode: str
    countryDartId: str
    kind: str
    dartId: str

class AdSlot(typing_extensions.TypedDict, total=False):
    linkedPlacementId: str
    primary: bool
    name: str
    paymentSourceType: typing_extensions.Literal[
        "PLANNING_PAYMENT_SOURCE_TYPE_AGENCY_PAID",
        "PLANNING_PAYMENT_SOURCE_TYPE_PUBLISHER_PAID",
    ]
    height: str
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    width: str
    comment: str

class VideoSettings(typing_extensions.TypedDict, total=False):
    orientation: typing_extensions.Literal["ANY", "LANDSCAPE", "PORTRAIT"]
    skippableSettings: SkippableSetting
    kind: str
    transcodeSettings: TranscodeSetting
    companionSettings: CompanionSetting

class Pricing(typing_extensions.TypedDict, total=False):
    startDate: str
    endDate: str
    capCostType: typing_extensions.Literal[
        "PLANNING_PLACEMENT_CAP_COST_TYPE_NONE",
        "PLANNING_PLACEMENT_CAP_COST_TYPE_MONTHLY",
        "PLANNING_PLACEMENT_CAP_COST_TYPE_CUMULATIVE",
    ]
    pricingType: typing_extensions.Literal[
        "PLANNING_PLACEMENT_PRICING_TYPE_IMPRESSIONS",
        "PLANNING_PLACEMENT_PRICING_TYPE_CPM",
        "PLANNING_PLACEMENT_PRICING_TYPE_CLICKS",
        "PLANNING_PLACEMENT_PRICING_TYPE_CPC",
        "PLANNING_PLACEMENT_PRICING_TYPE_CPA",
        "PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
        "PLANNING_PLACEMENT_PRICING_TYPE_FLAT_RATE_CLICKS",
        "PLANNING_PLACEMENT_PRICING_TYPE_CPM_ACTIVEVIEW",
    ]
    flights: typing.List[Flight]
    groupType: typing_extensions.Literal[
        "PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE",
        "PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK",
    ]
