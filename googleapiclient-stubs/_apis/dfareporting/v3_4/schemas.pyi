import typing

import typing_extensions

class PostalCode(typing_extensions.TypedDict, total=False):
    countryCode: str
    countryDartId: str
    id: str
    code: str
    kind: str

class PlacementsGenerateTagsResponse(typing_extensions.TypedDict, total=False):
    placementTags: typing.List[PlacementTag]
    kind: str

class City(typing_extensions.TypedDict, total=False):
    dartId: str
    kind: str
    countryDartId: str
    metroDmaId: str
    metroCode: str
    regionDartId: str
    regionCode: str
    name: str
    countryCode: str

class EventTag(typing_extensions.TypedDict, total=False):
    siteFilterType: typing_extensions.Literal["WHITELIST", "BLACKLIST"]
    accountId: str
    excludeFromAdxRequests: bool
    sslCompliant: bool
    status: typing_extensions.Literal["ENABLED", "DISABLED"]
    enabledByDefault: bool
    campaignId: str
    name: str
    siteIds: typing.List[str]
    id: str
    subaccountId: str
    url: str
    advertiserIdDimensionValue: DimensionValue
    type: typing_extensions.Literal[
        "IMPRESSION_IMAGE_EVENT_TAG",
        "IMPRESSION_JAVASCRIPT_EVENT_TAG",
        "CLICK_THROUGH_EVENT_TAG",
    ]
    advertiserId: str
    urlEscapeLevels: int
    campaignIdDimensionValue: DimensionValue
    kind: str

class Placement(typing_extensions.TypedDict, total=False):
    primary: bool
    placementGroupId: str
    campaignId: str
    keyName: str
    externalId: str
    kind: str
    pricingSchedule: PricingSchedule
    archived: bool
    paymentApproved: bool
    id: str
    idDimensionValue: DimensionValue
    advertiserId: str
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    siteIdDimensionValue: DimensionValue
    subaccountId: str
    lookbackConfiguration: LookbackConfiguration
    size: Size
    advertiserIdDimensionValue: DimensionValue
    videoActiveViewOptOut: bool
    directorySiteIdDimensionValue: DimensionValue
    placementStrategyId: str
    paymentSource: typing_extensions.Literal[
        "PLACEMENT_AGENCY_PAID", "PLACEMENT_PUBLISHER_PAID"
    ]
    vpaidAdapterChoice: typing_extensions.Literal["DEFAULT", "FLASH", "HTML5", "BOTH"]
    contentCategoryId: str
    name: str
    createInfo: LastModifiedInfo
    siteId: str
    sslRequired: bool
    status: typing_extensions.Literal[
        "PENDING_REVIEW",
        "PAYMENT_ACCEPTED",
        "PAYMENT_REJECTED",
        "ACKNOWLEDGE_REJECTION",
        "ACKNOWLEDGE_ACCEPTANCE",
        "DRAFT",
    ]
    videoSettings: VideoSettings
    tagSetting: TagSetting
    placementGroupIdDimensionValue: DimensionValue
    publisherUpdateInfo: LastModifiedInfo
    directorySiteId: str
    adBlockingOptOut: bool
    accountId: str
    lastModifiedInfo: LastModifiedInfo
    additionalSizes: typing.List[Size]
    comment: str
    tagFormats: typing.List[str]
    campaignIdDimensionValue: DimensionValue

class ConnectionType(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    id: str

class CrossDimensionReachReportCompatibleFields(
    typing_extensions.TypedDict, total=False
):
    kind: str
    breakdown: typing.List[Dimension]
    dimensionFilters: typing.List[Dimension]
    overlapMetrics: typing.List[Metric]
    metrics: typing.List[Metric]

class VideoOffset(typing_extensions.TypedDict, total=False):
    offsetSeconds: int
    offsetPercentage: int

class SiteTranscodeSetting(typing_extensions.TypedDict, total=False):
    enabledVideoFormats: typing.List[int]
    kind: str

class PricingSchedulePricingPeriod(typing_extensions.TypedDict, total=False):
    units: str
    endDate: str
    startDate: str
    rateOrCostNanos: str
    pricingComment: str

class OrderContact(typing_extensions.TypedDict, total=False):
    contactType: typing_extensions.Literal[
        "PLANNING_ORDER_CONTACT_BUYER_CONTACT",
        "PLANNING_ORDER_CONTACT_BUYER_BILLING_CONTACT",
        "PLANNING_ORDER_CONTACT_SELLER_CONTACT",
    ]
    signatureUserProfileId: str
    contactTitle: str
    contactName: str
    contactInfo: str

class ConversionError(typing_extensions.TypedDict, total=False):
    kind: str
    code: typing_extensions.Literal[
        "INVALID_ARGUMENT", "INTERNAL", "PERMISSION_DENIED", "NOT_FOUND"
    ]
    message: str

class LanguageTargeting(typing_extensions.TypedDict, total=False):
    languages: typing.List[Language]

class Activities(typing_extensions.TypedDict, total=False):
    metricNames: typing.List[str]
    kind: str
    filters: typing.List[DimensionValue]

class DynamicTargetingKey(typing_extensions.TypedDict, total=False):
    kind: str
    objectId: str
    name: str
    objectType: typing_extensions.Literal[
        "OBJECT_ADVERTISER", "OBJECT_AD", "OBJECT_CREATIVE", "OBJECT_PLACEMENT"
    ]

class UserRolePermissionGroup(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    id: str

class RemarketingList(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    lifeSpan: str
    listPopulationRule: ListPopulationRule
    id: str
    advertiserId: str
    accountId: str
    subaccountId: str
    active: bool
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
    listSize: str
    advertiserIdDimensionValue: DimensionValue
    description: str

class FloodlightActivityPublisherDynamicTag(typing_extensions.TypedDict, total=False):
    siteId: str
    directorySiteId: str
    clickThrough: bool
    siteIdDimensionValue: DimensionValue
    dynamicTag: FloodlightActivityDynamicTag
    viewThrough: bool

class MetrosListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    metros: typing.List[Metro]

class FsCommand(typing_extensions.TypedDict, total=False):
    left: int
    windowHeight: int
    windowWidth: int
    top: int
    positionOption: typing_extensions.Literal[
        "CENTERED", "DISTANCE_FROM_TOP_LEFT_CORNER"
    ]

class Creative(typing_extensions.TypedDict, total=False):
    backupImageReportingLabel: str
    adTagKeys: typing.List[str]
    skippable: bool
    counterCustomEvents: typing.List[CreativeCustomEvent]
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    universalAdId: UniversalAdId
    redirectUrl: str
    skipOffset: VideoOffset
    clickTags: typing.List[ClickTag]
    allowScriptAccess: bool
    latestTraffickedCreativeId: str
    size: Size
    commercialId: str
    sslCompliant: bool
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
    renderingIdDimensionValue: DimensionValue
    creativeAssetSelection: CreativeAssetSelection
    autoAdvanceImages: bool
    exitCustomEvents: typing.List[CreativeCustomEvent]
    thirdPartyUrls: typing.List[ThirdPartyTrackingUrl]
    lastModifiedInfo: LastModifiedInfo
    accountId: str
    studioAdvertiserId: str
    backupImageFeatures: typing.List[str]
    thirdPartyBackupImageImpressionsUrl: str
    additionalSizes: typing.List[Size]
    mediaDuration: float
    htmlCodeLocked: bool
    studioCreativeId: str
    mediaDescription: str
    version: int
    sslOverride: bool
    thirdPartyRichMediaImpressionsUrl: str
    companionCreatives: typing.List[str]
    authoringSource: typing_extensions.Literal[
        "CREATIVE_AUTHORING_SOURCE_DCM",
        "CREATIVE_AUTHORING_SOURCE_DBM",
        "CREATIVE_AUTHORING_SOURCE_STUDIO",
    ]
    fsCommand: FsCommand
    progressOffset: VideoOffset
    requiredFlashVersion: int
    backupImageTargetWindow: TargetWindow
    backupImageClickThroughUrl: CreativeClickThroughUrl
    htmlCode: str
    kind: str
    id: str
    dynamicAssetSelection: bool
    backgroundColor: str
    compatibility: typing.List[str]
    name: str
    overrideCss: str
    adParameters: str
    timerCustomEvents: typing.List[CreativeCustomEvent]
    creativeAssets: typing.List[CreativeAsset]
    authoringTool: typing_extensions.Literal["NINJA", "SWIFFY"]
    active: bool
    advertiserId: str
    customKeyValues: typing.List[str]
    convertFlashToHtml5: bool
    subaccountId: str
    studioTraffickedCreativeId: str
    requiredFlashPluginVersion: str
    obaIcon: ObaIcon
    totalFileSize: str
    creativeFieldAssignments: typing.List[CreativeFieldAssignment]
    idDimensionValue: DimensionValue
    archived: bool
    renderingId: str

class SiteSettings(typing_extensions.TypedDict, total=False):
    disableNewCookie: bool
    adBlockingOptOut: bool
    activeViewOptOut: bool
    tagSetting: TagSetting
    vpaidAdapterChoiceTemplate: typing_extensions.Literal[
        "DEFAULT", "FLASH", "HTML5", "BOTH"
    ]
    videoActiveViewOptOutTemplate: bool

class DimensionFilter(typing_extensions.TypedDict, total=False):
    kind: str
    dimensionName: str
    value: str

class ReachReportCompatibleFields(typing_extensions.TypedDict, total=False):
    kind: str
    pivotedActivityMetrics: typing.List[Metric]
    metrics: typing.List[Metric]
    reachByFrequencyMetrics: typing.List[Metric]
    dimensionFilters: typing.List[Dimension]
    dimensions: typing.List[Dimension]

class ContentCategoriesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    contentCategories: typing.List[ContentCategory]

class DirectorySitesListResponse(typing_extensions.TypedDict, total=False):
    directorySites: typing.List[DirectorySite]
    nextPageToken: str
    kind: str

class SiteCompanionSetting(typing_extensions.TypedDict, total=False):
    imageOnly: bool
    kind: str
    enabledSizes: typing.List[Size]
    companionsDisabled: bool

class CampaignCreativeAssociationsListResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    campaignCreativeAssociations: typing.List[CampaignCreativeAssociation]
    kind: str

class UserRolesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    userRoles: typing.List[UserRole]

class AdsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    ads: typing.List[Ad]

class CreativeFieldValue(typing_extensions.TypedDict, total=False):
    value: str
    kind: str
    id: str

class UniversalAdId(typing_extensions.TypedDict, total=False):
    registry: typing_extensions.Literal["OTHER", "AD_ID_OFFICIAL", "CLEARCAST", "DCM"]
    value: str

class ProjectsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projects: typing.List[Project]
    kind: str

class PlatformTypesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    platformTypes: typing.List[PlatformType]

class FloodlightReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[Dimension]
    metrics: typing.List[Metric]
    dimensionFilters: typing.List[Dimension]
    kind: str

class ListPopulationClause(typing_extensions.TypedDict, total=False):
    terms: typing.List[ListPopulationTerm]

class GeoTargeting(typing_extensions.TypedDict, total=False):
    countries: typing.List[Country]
    cities: typing.List[City]
    postalCodes: typing.List[PostalCode]
    excludeCountries: bool
    regions: typing.List[Region]
    metros: typing.List[Metro]

class ReportsConfiguration(typing_extensions.TypedDict, total=False):
    exposureToConversionEnabled: bool
    lookbackConfiguration: LookbackConfiguration
    reportGenerationTimeZoneId: str

class ClickThroughUrlSuffixProperties(typing_extensions.TypedDict, total=False):
    overrideInheritedSuffix: bool
    clickThroughUrlSuffix: str

class Site(typing_extensions.TypedDict, total=False):
    id: str
    subaccountId: str
    accountId: str
    siteSettings: SiteSettings
    approved: bool
    directorySiteId: str
    videoSettings: SiteVideoSettings
    keyName: str
    idDimensionValue: DimensionValue
    name: str
    siteContacts: typing.List[SiteContact]
    directorySiteIdDimensionValue: DimensionValue
    kind: str

class LanguagesListResponse(typing_extensions.TypedDict, total=False):
    languages: typing.List[Language]
    kind: str

class AdvertiserGroupsListResponse(typing_extensions.TypedDict, total=False):
    advertiserGroups: typing.List[AdvertiserGroup]
    kind: str
    nextPageToken: str

class OrderDocument(typing_extensions.TypedDict, total=False):
    approvedByUserProfileIds: typing.List[str]
    lastSentTime: str
    cancelled: bool
    advertiserId: str
    amendedOrderDocumentId: str
    subaccountId: str
    title: str
    effectiveDate: str
    accountId: str
    projectId: str
    kind: str
    lastSentRecipients: typing.List[str]
    id: str
    orderId: str
    type: typing_extensions.Literal[
        "PLANNING_ORDER_TYPE_INSERTION_ORDER", "PLANNING_ORDER_TYPE_CHANGE_ORDER"
    ]
    createdInfo: LastModifiedInfo
    signed: bool

class ConversionsBatchInsertResponse(typing_extensions.TypedDict, total=False):
    hasFailures: bool
    kind: str
    status: typing.List[ConversionStatus]

class ChangeLog(typing_extensions.TypedDict, total=False):
    action: str
    transactionId: str
    kind: str
    subaccountId: str
    objectId: str
    userProfileId: str
    oldValue: str
    userProfileName: str
    accountId: str
    changeTime: str
    id: str
    objectType: str
    newValue: str
    fieldName: str

class Ad(typing_extensions.TypedDict, total=False):
    targetingTemplateId: str
    size: Size
    kind: str
    comments: str
    advertiserId: str
    active: bool
    name: str
    audienceSegmentId: str
    campaignIdDimensionValue: DimensionValue
    keyValueTargetingExpression: KeyValueTargetingExpression
    placementAssignments: typing.List[PlacementAssignment]
    campaignId: str
    eventTagOverrides: typing.List[EventTagOverride]
    defaultClickThroughEventTagProperties: DefaultClickThroughEventTagProperties
    id: str
    creativeGroupAssignments: typing.List[CreativeGroupAssignment]
    clickThroughUrl: ClickThroughUrl
    sslCompliant: bool
    endTime: str
    dynamicClickTracker: bool
    geoTargeting: GeoTargeting
    deliverySchedule: DeliverySchedule
    sslRequired: bool
    dayPartTargeting: DayPartTargeting
    clickThroughUrlSuffixProperties: ClickThroughUrlSuffixProperties
    idDimensionValue: DimensionValue
    type: typing_extensions.Literal[
        "AD_SERVING_STANDARD_AD",
        "AD_SERVING_DEFAULT_AD",
        "AD_SERVING_CLICK_TRACKER",
        "AD_SERVING_TRACKING",
        "AD_SERVING_BRAND_SAFE_AD",
    ]
    subaccountId: str
    lastModifiedInfo: LastModifiedInfo
    technologyTargeting: TechnologyTargeting
    createInfo: LastModifiedInfo
    creativeRotation: CreativeRotation
    startTime: str
    accountId: str
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
    archived: bool
    advertiserIdDimensionValue: DimensionValue

class FloodlightActivitiesGenerateTagResponse(typing_extensions.TypedDict, total=False):
    globalSiteTagGlobalSnippet: str
    floodlightActivityTag: str
    kind: str

class CreativeGroup(typing_extensions.TypedDict, total=False):
    subaccountId: str
    accountId: str
    advertiserId: str
    kind: str
    advertiserIdDimensionValue: DimensionValue
    name: str
    id: str
    groupNumber: int

class ObaIcon(typing_extensions.TypedDict, total=False):
    yPosition: str
    resourceUrl: str
    iconClickTrackingUrl: str
    size: Size
    program: str
    iconViewTrackingUrl: str
    iconClickThroughUrl: str
    xPosition: str

class CreativeAssetId(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "IMAGE", "FLASH", "VIDEO", "HTML", "HTML_IMAGE", "AUDIO"
    ]

class UserProfileList(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[UserProfile]
    etag: str

class SubaccountsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    subaccounts: typing.List[Subaccount]

class AccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    accounts: typing.List[Account]
    nextPageToken: str

class Pricing(typing_extensions.TypedDict, total=False):
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
    groupType: typing_extensions.Literal[
        "PLANNING_PLACEMENT_GROUP_TYPE_PACKAGE",
        "PLANNING_PLACEMENT_GROUP_TYPE_ROADBLOCK",
    ]
    capCostType: typing_extensions.Literal[
        "PLANNING_PLACEMENT_CAP_COST_TYPE_NONE",
        "PLANNING_PLACEMENT_CAP_COST_TYPE_MONTHLY",
        "PLANNING_PLACEMENT_CAP_COST_TYPE_CUMULATIVE",
    ]
    flights: typing.List[Flight]
    endDate: str
    startDate: str

class ConversionStatus(typing_extensions.TypedDict, total=False):
    errors: typing.List[ConversionError]
    kind: str
    conversion: Conversion

class CitiesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    cities: typing.List[City]

class CreativeAssignment(typing_extensions.TypedDict, total=False):
    endTime: str
    richMediaExitOverrides: typing.List[RichMediaExitOverride]
    startTime: str
    sequence: int
    companionCreativeOverrides: typing.List[CompanionClickThroughOverride]
    sslCompliant: bool
    clickThroughUrl: ClickThroughUrl
    active: bool
    creativeIdDimensionValue: DimensionValue
    applyEventTags: bool
    weight: int
    creativeId: str
    creativeGroupAssignments: typing.List[CreativeGroupAssignment]

class Size(typing_extensions.TypedDict, total=False):
    iab: bool
    kind: str
    id: str
    height: int
    width: int

class ListPopulationTerm(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "CUSTOM_VARIABLE_TERM", "LIST_MEMBERSHIP_TERM", "REFERRER_TERM"
    ]
    negation: bool
    operator: typing_extensions.Literal[
        "NUM_EQUALS",
        "NUM_LESS_THAN",
        "NUM_LESS_THAN_EQUAL",
        "NUM_GREATER_THAN",
        "NUM_GREATER_THAN_EQUAL",
        "STRING_EQUALS",
        "STRING_CONTAINS",
    ]
    variableFriendlyName: str
    variableName: str
    remarketingListId: str
    contains: bool
    value: str

class CustomVariable(typing_extensions.TypedDict, total=False):
    kind: str
    index: str
    value: str

class RichMediaExitOverride(typing_extensions.TypedDict, total=False):
    clickThroughUrl: ClickThroughUrl
    enabled: bool
    exitId: str

class VideoFormatsListResponse(typing_extensions.TypedDict, total=False):
    videoFormats: typing.List[VideoFormat]
    kind: str

class PlacementAssignment(typing_extensions.TypedDict, total=False):
    placementIdDimensionValue: DimensionValue
    active: bool
    placementId: str
    sslRequired: bool

class AccountPermissionGroup(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    kind: str

class SortedDimension(typing_extensions.TypedDict, total=False):
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]
    name: str
    kind: str

class CreativesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    creatives: typing.List[Creative]
    nextPageToken: str

class FloodlightActivityGroup(typing_extensions.TypedDict, total=False):
    floodlightConfigurationIdDimensionValue: DimensionValue
    name: str
    subaccountId: str
    advertiserIdDimensionValue: DimensionValue
    id: str
    idDimensionValue: DimensionValue
    advertiserId: str
    floodlightConfigurationId: str
    accountId: str
    tagString: str
    type: typing_extensions.Literal["COUNTER", "SALE"]
    kind: str

class MobileApp(typing_extensions.TypedDict, total=False):
    kind: str
    directory: typing_extensions.Literal[
        "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_PLAY_STORE"
    ]
    publisherName: str
    title: str
    id: str

class EventTagOverride(typing_extensions.TypedDict, total=False):
    id: str
    enabled: bool

class TargetWindow(typing_extensions.TypedDict, total=False):
    customHtml: str
    targetWindowOption: typing_extensions.Literal[
        "NEW_WINDOW", "CURRENT_WINDOW", "CUSTOM"
    ]

class KeyValueTargetingExpression(typing_extensions.TypedDict, total=False):
    expression: str

class BrowsersListResponse(typing_extensions.TypedDict, total=False):
    browsers: typing.List[Browser]
    kind: str

class DeliverySchedule(typing_extensions.TypedDict, total=False):
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
    frequencyCap: FrequencyCap
    impressionRatio: str

class CustomEvent(typing_extensions.TypedDict, total=False):
    floodlightConfigurationId: str
    annotateClickEvent: CustomEventClickAnnotation
    eventType: typing_extensions.Literal["UNKNOWN", "INSERT", "ANNOTATE"]
    kind: str
    timestampMicros: str
    annotateImpressionEvent: CustomEventImpressionAnnotation
    ordinal: str
    customVariables: typing.List[CustomVariable]
    insertEvent: CustomEventInsert

class PlacementGroupsListResponse(typing_extensions.TypedDict, total=False):
    placementGroups: typing.List[PlacementGroup]
    nextPageToken: str
    kind: str

class OperatingSystem(typing_extensions.TypedDict, total=False):
    kind: str
    desktop: bool
    dartId: str
    mobile: bool
    name: str

class Rule(typing_extensions.TypedDict, total=False):
    name: str
    targetingTemplateId: str
    assetId: str

class DimensionValue(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    value: str
    dimensionName: str
    matchType: typing_extensions.Literal[
        "EXACT", "BEGINS_WITH", "CONTAINS", "WILDCARD_EXPRESSION"
    ]
    id: str

class OffsetPosition(typing_extensions.TypedDict, total=False):
    top: int
    left: int

class Flight(typing_extensions.TypedDict, total=False):
    units: str
    rateOrCost: str
    startDate: str
    endDate: str

class Region(typing_extensions.TypedDict, total=False):
    kind: str
    countryCode: str
    countryDartId: str
    regionCode: str
    name: str
    dartId: str

class UserRolePermissionGroupsListResponse(typing_extensions.TypedDict, total=False):
    userRolePermissionGroups: typing.List[UserRolePermissionGroup]
    kind: str

class PlacementStrategiesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    placementStrategies: typing.List[PlacementStrategy]
    nextPageToken: str

class CreativeClickThroughUrl(typing_extensions.TypedDict, total=False):
    customClickThroughUrl: str
    computedClickThroughUrl: str
    landingPageId: str

class FloodlightActivitiesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    floodlightActivities: typing.List[FloodlightActivity]

class Country(typing_extensions.TypedDict, total=False):
    sslEnabled: bool
    countryCode: str
    dartId: str
    kind: str
    name: str

class DayPartTargeting(typing_extensions.TypedDict, total=False):
    daysOfWeek: typing.List[str]
    hoursOfDay: typing.List[int]
    userLocalTime: bool

class CreativeFieldAssignment(typing_extensions.TypedDict, total=False):
    creativeFieldValueId: str
    creativeFieldId: str

class FloodlightConfigurationsListResponse(typing_extensions.TypedDict, total=False):
    floodlightConfigurations: typing.List[FloodlightConfiguration]
    kind: str

class CreativeFieldsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    creativeFields: typing.List[CreativeField]

class SiteVideoSettings(typing_extensions.TypedDict, total=False):
    skippableSettings: SiteSkippableSetting
    obaSettings: ObaIcon
    transcodeSettings: SiteTranscodeSetting
    obaEnabled: bool
    kind: str
    companionSettings: SiteCompanionSetting
    orientation: typing_extensions.Literal["ANY", "LANDSCAPE", "PORTRAIT"]

class CreativeFieldValuesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    creativeFieldValues: typing.List[CreativeFieldValue]
    nextPageToken: str

class Campaign(typing_extensions.TypedDict, total=False):
    audienceSegmentGroups: typing.List[AudienceSegmentGroup]
    startDate: str
    adBlockingConfiguration: AdBlockingConfiguration
    creativeOptimizationConfiguration: CreativeOptimizationConfiguration
    archived: bool
    endDate: str
    traffickerEmails: typing.List[str]
    accountId: str
    additionalCreativeOptimizationConfigurations: typing.List[
        CreativeOptimizationConfiguration
    ]
    externalId: str
    comment: str
    advertiserId: str
    eventTagOverrides: typing.List[EventTagOverride]
    kind: str
    name: str
    createInfo: LastModifiedInfo
    clickThroughUrlSuffixProperties: ClickThroughUrlSuffixProperties
    subaccountId: str
    idDimensionValue: DimensionValue
    advertiserIdDimensionValue: DimensionValue
    defaultLandingPageId: str
    lastModifiedInfo: LastModifiedInfo
    advertiserGroupId: str
    nielsenOcrEnabled: bool
    creativeGroupIds: typing.List[str]
    id: str
    billingInvoiceCode: str
    defaultClickThroughEventTagProperties: DefaultClickThroughEventTagProperties

class CreativeOptimizationConfiguration(typing_extensions.TypedDict, total=False):
    id: str
    optimizationModel: typing_extensions.Literal[
        "CLICK",
        "POST_CLICK",
        "POST_IMPRESSION",
        "POST_CLICK_AND_IMPRESSION",
        "VIDEO_COMPLETION",
    ]
    optimizationActivitys: typing.List[OptimizationActivity]
    name: str

class CreativeRotation(typing_extensions.TypedDict, total=False):
    creativeAssignments: typing.List[CreativeAssignment]
    creativeOptimizationConfigurationId: str
    weightCalculationStrategy: typing_extensions.Literal[
        "WEIGHT_STRATEGY_EQUAL",
        "WEIGHT_STRATEGY_CUSTOM",
        "WEIGHT_STRATEGY_HIGHEST_CTR",
        "WEIGHT_STRATEGY_OPTIMIZED",
    ]
    type: typing_extensions.Literal[
        "CREATIVE_ROTATION_TYPE_SEQUENTIAL", "CREATIVE_ROTATION_TYPE_RANDOM"
    ]

class FloodlightActivity(typing_extensions.TypedDict, total=False):
    floodlightActivityGroupName: str
    subaccountId: str
    idDimensionValue: DimensionValue
    tagFormat: typing_extensions.Literal["HTML", "XHTML"]
    accountId: str
    floodlightActivityGroupTagString: str
    floodlightActivityGroupId: str
    kind: str
    attributionEnabled: bool
    sslRequired: bool
    floodlightTagType: typing_extensions.Literal["IFRAME", "IMAGE", "GLOBAL_SITE_TAG"]
    secure: bool
    sslCompliant: bool
    advertiserIdDimensionValue: DimensionValue
    countingMethod: typing_extensions.Literal[
        "STANDARD_COUNTING",
        "UNIQUE_COUNTING",
        "SESSION_COUNTING",
        "TRANSACTIONS_COUNTING",
        "ITEMS_SOLD_COUNTING",
    ]
    cacheBustingType: typing_extensions.Literal[
        "JAVASCRIPT", "ACTIVE_SERVER_PAGE", "JSP", "PHP", "COLD_FUSION"
    ]
    defaultTags: typing.List[FloodlightActivityDynamicTag]
    expectedUrl: str
    notes: str
    floodlightActivityGroupType: typing_extensions.Literal["COUNTER", "SALE"]
    tagString: str
    floodlightConfigurationId: str
    id: str
    status: typing_extensions.Literal[
        "ACTIVE", "ARCHIVED_AND_DISABLED", "ARCHIVED", "DISABLED_POLICY"
    ]
    name: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    userDefinedVariableTypes: typing.List[str]
    publisherTags: typing.List[FloodlightActivityPublisherDynamicTag]
    advertiserId: str

class Order(typing_extensions.TypedDict, total=False):
    buyerOrganizationName: str
    termsAndConditions: str
    kind: str
    buyerInvoiceId: str
    contacts: typing.List[OrderContact]
    advertiserId: str
    accountId: str
    approverUserProfileIds: typing.List[str]
    name: str
    notes: str
    comments: str
    planningTermId: str
    subaccountId: str
    lastModifiedInfo: LastModifiedInfo
    sellerOrganizationName: str
    id: str
    siteNames: typing.List[str]
    sellerOrderId: str
    siteId: typing.List[str]
    projectId: str

class DirectorySite(typing_extensions.TypedDict, total=False):
    url: str
    idDimensionValue: DimensionValue
    settings: DirectorySiteSettings
    kind: str
    inpageTagFormats: typing.List[str]
    id: str
    name: str
    interstitialTagFormats: typing.List[str]

class Metric(typing_extensions.TypedDict, total=False):
    kind: str
    name: str

class CreativeAsset(typing_extensions.TypedDict, total=False):
    positionTopUnit: typing_extensions.Literal[
        "OFFSET_UNIT_PIXEL", "OFFSET_UNIT_PERCENT", "OFFSET_UNIT_PIXEL_FROM_CENTER"
    ]
    childAssetType: typing_extensions.Literal[
        "CHILD_ASSET_TYPE_FLASH",
        "CHILD_ASSET_TYPE_VIDEO",
        "CHILD_ASSET_TYPE_IMAGE",
        "CHILD_ASSET_TYPE_DATA",
    ]
    detectedFeatures: typing.List[str]
    hideSelectionBoxes: bool
    additionalSizes: typing.List[Size]
    audioBitRate: int
    assetIdentifier: CreativeAssetId
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
    zipFilename: str
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    streamingServingUrl: str
    idDimensionValue: DimensionValue
    zipFilesize: str
    size: Size
    audioSampleRate: int
    id: str
    zIndex: int
    mimeType: str
    alignment: typing_extensions.Literal[
        "ALIGNMENT_TOP", "ALIGNMENT_RIGHT", "ALIGNMENT_BOTTOM", "ALIGNMENT_LEFT"
    ]
    fileSize: str
    duration: int
    positionLeftUnit: typing_extensions.Literal[
        "OFFSET_UNIT_PIXEL", "OFFSET_UNIT_PERCENT", "OFFSET_UNIT_PIXEL_FROM_CENTER"
    ]
    active: bool
    backupImageExit: CreativeCustomEvent
    startTimeType: typing_extensions.Literal[
        "ASSET_START_TIME_TYPE_NONE", "ASSET_START_TIME_TYPE_CUSTOM"
    ]
    windowMode: typing_extensions.Literal["OPAQUE", "WINDOW", "TRANSPARENT"]
    verticallyLocked: bool
    offset: OffsetPosition
    originalBackup: bool
    orientation: typing_extensions.Literal["LANDSCAPE", "PORTRAIT", "SQUARE"]
    horizontallyLocked: bool
    hideFlashObjects: bool
    frameRate: float
    progressiveServingUrl: str
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
    expandedDimension: Size
    customStartTimeValue: int
    flashVersion: int
    politeLoad: bool
    transparency: bool
    actionScript3: bool
    companionCreativeIds: typing.List[str]
    sslCompliant: bool
    mediaDuration: float
    pushdown: bool
    pushdownDuration: float
    durationType: typing_extensions.Literal[
        "ASSET_DURATION_TYPE_AUTO",
        "ASSET_DURATION_TYPE_NONE",
        "ASSET_DURATION_TYPE_CUSTOM",
    ]
    collapsedSize: Size
    bitRate: int
    position: OffsetPosition

class CustomEventsBatchInsertResponse(typing_extensions.TypedDict, total=False):
    kind: str
    hasFailures: bool
    status: typing.List[CustomEventStatus]

class AdvertiserLandingPagesListResponse(typing_extensions.TypedDict, total=False):
    landingPages: typing.List[LandingPage]
    kind: str
    nextPageToken: str

class CustomEventImpressionAnnotation(typing_extensions.TypedDict, total=False):
    kind: str
    pathImpressionId: str

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

class CustomFloodlightVariable(typing_extensions.TypedDict, total=False):
    kind: str
    value: str
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

class FrequencyCap(typing_extensions.TypedDict, total=False):
    impressions: str
    duration: str

class UserRolePermissionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    userRolePermissions: typing.List[UserRolePermission]

class PlatformType(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    kind: str

class Browser(typing_extensions.TypedDict, total=False):
    dartId: str
    name: str
    majorVersion: str
    browserVersionId: str
    kind: str
    minorVersion: str

class Report(typing_extensions.TypedDict, total=False):
    ownerProfileId: str
    lastModifiedTime: str
    etag: str
    id: str
    kind: str
    accountId: str
    pathAttributionCriteria: typing.Dict[str, typing.Any]
    crossDimensionReachCriteria: typing.Dict[str, typing.Any]
    subAccountId: str
    name: str
    delivery: typing.Dict[str, typing.Any]
    pathCriteria: typing.Dict[str, typing.Any]
    reachCriteria: typing.Dict[str, typing.Any]
    format: typing_extensions.Literal["CSV", "EXCEL"]
    schedule: typing.Dict[str, typing.Any]
    floodlightCriteria: typing.Dict[str, typing.Any]
    fileName: str
    pathToConversionCriteria: typing.Dict[str, typing.Any]
    criteria: typing.Dict[str, typing.Any]
    type: typing_extensions.Literal[
        "STANDARD",
        "REACH",
        "PATH_TO_CONVERSION",
        "CROSS_DIMENSION_REACH",
        "FLOODLIGHT",
        "PATH",
        "PATH_ATTRIBUTION",
    ]

class DimensionValueRequest(typing_extensions.TypedDict, total=False):
    endDate: str
    kind: str
    startDate: str
    filters: typing.List[DimensionFilter]
    dimensionName: str

class CampaignCreativeAssociation(typing_extensions.TypedDict, total=False):
    creativeId: str
    kind: str

class TranscodeSetting(typing_extensions.TypedDict, total=False):
    enabledVideoFormats: typing.List[int]
    kind: str

class PostalCodesListResponse(typing_extensions.TypedDict, total=False):
    postalCodes: typing.List[PostalCode]
    kind: str

class Language(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    languageCode: str
    kind: str

class ConversionsBatchUpdateResponse(typing_extensions.TypedDict, total=False):
    kind: str
    status: typing.List[ConversionStatus]
    hasFailures: bool

class MobileCarriersListResponse(typing_extensions.TypedDict, total=False):
    mobileCarriers: typing.List[MobileCarrier]
    kind: str

class DimensionValueList(typing_extensions.TypedDict, total=False):
    etag: str
    nextPageToken: str
    kind: str
    items: typing.List[DimensionValue]

class OperatingSystemVersionsListResponse(typing_extensions.TypedDict, total=False):
    operatingSystemVersions: typing.List[OperatingSystemVersion]
    kind: str

class ListTargetingExpression(typing_extensions.TypedDict, total=False):
    expression: str

class FloodlightActivityDynamicTag(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    tag: str

class TargetableRemarketingList(typing_extensions.TypedDict, total=False):
    advertiserIdDimensionValue: DimensionValue
    advertiserId: str
    name: str
    lifeSpan: str
    id: str
    active: bool
    kind: str
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
    subaccountId: str
    description: str
    listSize: str

class CustomRichMediaEvents(typing_extensions.TypedDict, total=False):
    filteredEventIds: typing.List[DimensionValue]
    kind: str

class MobileCarrier(typing_extensions.TypedDict, total=False):
    id: str
    countryCode: str
    countryDartId: str
    name: str
    kind: str

class TargetableRemarketingListsListResponse(typing_extensions.TypedDict, total=False):
    targetableRemarketingLists: typing.List[TargetableRemarketingList]
    nextPageToken: str
    kind: str

class File(typing_extensions.TypedDict, total=False):
    etag: str
    status: typing_extensions.Literal[
        "PROCESSING", "REPORT_AVAILABLE", "FAILED", "CANCELLED"
    ]
    lastModifiedTime: str
    reportId: str
    dateRange: DateRange
    id: str
    kind: str
    urls: typing.Dict[str, typing.Any]
    fileName: str
    format: typing_extensions.Literal["CSV", "EXCEL"]

class ContentCategory(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    kind: str
    accountId: str

class ThirdPartyAuthenticationToken(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class InventoryItem(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "PLANNING_PLACEMENT_TYPE_REGULAR", "PLANNING_PLACEMENT_TYPE_CREDIT"
    ]
    kind: str
    projectId: str
    negotiationChannelId: str
    orderId: str
    estimatedClickThroughRate: str
    id: str
    advertiserId: str
    estimatedConversionRate: str
    adSlots: typing.List[AdSlot]
    rfpId: str
    accountId: str
    placementStrategyId: str
    contentCategoryId: str
    pricing: Pricing
    lastModifiedInfo: LastModifiedInfo
    siteId: str
    inPlan: bool
    subaccountId: str
    name: str

class ChannelGroupingRule(typing_extensions.TypedDict, total=False):
    disjunctiveMatchStatements: typing.List[DisjunctiveMatchStatement]
    name: str
    kind: str

class DV3Ids(typing_extensions.TypedDict, total=False):
    dvLineItemId: str
    dvSiteId: str
    kind: str
    dvInsertionOrderId: str
    dvCampaignId: str
    dvCreativeId: str

class ChangeLogsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    changeLogs: typing.List[ChangeLog]
    kind: str

class PricingSchedule(typing_extensions.TypedDict, total=False):
    capCostOption: typing_extensions.Literal[
        "CAP_COST_NONE", "CAP_COST_MONTHLY", "CAP_COST_CUMULATIVE"
    ]
    testingStartDate: str
    pricingPeriods: typing.List[PricingSchedulePricingPeriod]
    pricingType: typing_extensions.Literal[
        "PRICING_TYPE_CPM",
        "PRICING_TYPE_CPC",
        "PRICING_TYPE_CPA",
        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
        "PRICING_TYPE_FLAT_RATE_CLICKS",
        "PRICING_TYPE_CPM_ACTIVEVIEW",
    ]
    flighted: bool
    endDate: str
    floodlightActivityId: str
    startDate: str

class TagData(typing_extensions.TypedDict, total=False):
    clickTag: str
    creativeId: str
    impressionTag: str
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
    adId: str

class CreativeAssetSelection(typing_extensions.TypedDict, total=False):
    rules: typing.List[Rule]
    defaultAssetId: str

class Metro(typing_extensions.TypedDict, total=False):
    kind: str
    dartId: str
    metroCode: str
    countryDartId: str
    countryCode: str
    name: str
    dmaId: str

class AccountActiveAdSummary(typing_extensions.TypedDict, total=False):
    kind: str
    availableAds: str
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
    accountId: str
    activeAds: str

class ChannelGrouping(typing_extensions.TypedDict, total=False):
    kind: str
    fallbackName: str
    rules: typing.List[ChannelGroupingRule]
    name: str

class Account(typing_extensions.TypedDict, total=False):
    kind: str
    description: str
    teaserSizeLimit: str
    currencyId: str
    availablePermissionIds: typing.List[str]
    reportsConfiguration: ReportsConfiguration
    defaultCreativeSizeId: str
    accountProfile: typing_extensions.Literal[
        "ACCOUNT_PROFILE_BASIC", "ACCOUNT_PROFILE_STANDARD"
    ]
    locale: str
    activeViewOptOut: bool
    name: str
    shareReportsWithTwitter: bool
    countryId: str
    maximumImageSize: str
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
    id: str
    active: bool
    accountPermissionIds: typing.List[str]

class AccountPermissionsListResponse(typing_extensions.TypedDict, total=False):
    accountPermissions: typing.List[AccountPermission]
    kind: str

class TechnologyTargeting(typing_extensions.TypedDict, total=False):
    browsers: typing.List[Browser]
    operatingSystemVersions: typing.List[OperatingSystemVersion]
    mobileCarriers: typing.List[MobileCarrier]
    platformTypes: typing.List[PlatformType]
    operatingSystems: typing.List[OperatingSystem]
    connectionTypes: typing.List[ConnectionType]

class Recipient(typing_extensions.TypedDict, total=False):
    deliveryType: typing_extensions.Literal["LINK", "ATTACHMENT"]
    kind: str
    email: str

class UserRolePermission(typing_extensions.TypedDict, total=False):
    permissionGroupId: str
    availability: typing_extensions.Literal[
        "NOT_AVAILABLE_BY_DEFAULT",
        "ACCOUNT_BY_DEFAULT",
        "SUBACCOUNT_AND_ACCOUNT_BY_DEFAULT",
        "ACCOUNT_ALWAYS",
        "SUBACCOUNT_AND_ACCOUNT_ALWAYS",
    ]
    name: str
    kind: str
    id: str

class DirectorySiteSettings(typing_extensions.TypedDict, total=False):
    dfpSettings: DfpSettings
    activeViewOptOut: bool
    interstitialPlacementAccepted: bool
    instreamVideoPlacementAccepted: bool

class TagSetting(typing_extensions.TypedDict, total=False):
    includeClickThroughUrls: bool
    additionalKeyValues: str
    keywordOption: typing_extensions.Literal[
        "PLACEHOLDER_WITH_LIST_OF_KEYWORDS",
        "IGNORE",
        "GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD",
    ]
    includeClickTracking: bool

class CustomViewabilityMetric(typing_extensions.TypedDict, total=False):
    name: str
    configuration: CustomViewabilityMetricConfiguration
    id: str

class SitesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    sites: typing.List[Site]
    nextPageToken: str

class CustomEventsBatchInsertRequest(typing_extensions.TypedDict, total=False):
    kind: str
    customEvents: typing.List[CustomEvent]

class RemarketingListShare(typing_extensions.TypedDict, total=False):
    remarketingListId: str
    sharedAccountIds: typing.List[str]
    sharedAdvertiserIds: typing.List[str]
    kind: str

class OperatingSystemVersion(typing_extensions.TypedDict, total=False):
    majorVersion: str
    name: str
    operatingSystem: OperatingSystem
    kind: str
    id: str
    minorVersion: str

class CustomEventClickAnnotation(typing_extensions.TypedDict, total=False):
    kind: str
    gclid: str

class ReportCompatibleFields(typing_extensions.TypedDict, total=False):
    pivotedActivityMetrics: typing.List[Metric]
    dimensions: typing.List[Dimension]
    kind: str
    metrics: typing.List[Metric]
    dimensionFilters: typing.List[Dimension]

class AdvertiserGroup(typing_extensions.TypedDict, total=False):
    id: str
    accountId: str
    kind: str
    name: str

class CampaignManagerIds(typing_extensions.TypedDict, total=False):
    siteId: str
    adId: str
    campaignId: str
    kind: str
    placementId: str
    creativeId: str

class TagSettings(typing_extensions.TypedDict, total=False):
    dynamicTagEnabled: bool
    imageTagEnabled: bool

class SkippableSetting(typing_extensions.TypedDict, total=False):
    skippable: bool
    skipOffset: VideoOffset
    kind: str
    progressOffset: VideoOffset

class DeepLink(typing_extensions.TypedDict, total=False):
    appUrl: str
    remarketingListIds: typing.List[str]
    fallbackUrl: str
    mobileApp: MobileApp
    kind: str

class LookbackConfiguration(typing_extensions.TypedDict, total=False):
    postImpressionActivitiesDuration: int
    clickDuration: int

class AdSlot(typing_extensions.TypedDict, total=False):
    paymentSourceType: typing_extensions.Literal[
        "PLANNING_PAYMENT_SOURCE_TYPE_AGENCY_PAID",
        "PLANNING_PAYMENT_SOURCE_TYPE_PUBLISHER_PAID",
    ]
    primary: bool
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    linkedPlacementId: str
    width: str
    name: str
    comment: str
    height: str

class DynamicTargetingKeysListResponse(typing_extensions.TypedDict, total=False):
    dynamicTargetingKeys: typing.List[DynamicTargetingKey]
    kind: str

class FloodlightConfiguration(typing_extensions.TypedDict, total=False):
    advertiserId: str
    customViewabilityMetric: CustomViewabilityMetric
    idDimensionValue: DimensionValue
    accountId: str
    omnitureSettings: OmnitureSettings
    thirdPartyAuthenticationTokens: typing.List[ThirdPartyAuthenticationToken]
    lookbackConfiguration: LookbackConfiguration
    analyticsDataSharingEnabled: bool
    userDefinedVariableConfigurations: typing.List[UserDefinedVariableConfiguration]
    kind: str
    naturalSearchConversionAttributionOption: typing_extensions.Literal[
        "EXCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
        "INCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
        "INCLUDE_NATURAL_SEARCH_TIERED_CONVERSION_ATTRIBUTION",
    ]
    subaccountId: str
    exposureToConversionEnabled: bool
    advertiserIdDimensionValue: DimensionValue
    id: str
    inAppAttributionTrackingEnabled: bool
    firstDayOfWeek: typing_extensions.Literal["MONDAY", "SUNDAY"]
    tagSettings: TagSettings

class Project(typing_extensions.TypedDict, total=False):
    id: str
    subaccountId: str
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
    targetImpressions: str
    endDate: str
    audienceGender: typing_extensions.Literal[
        "PLANNING_AUDIENCE_GENDER_MALE", "PLANNING_AUDIENCE_GENDER_FEMALE"
    ]
    startDate: str
    accountId: str
    targetCpmActiveViewNanos: str
    targetCpaNanos: str
    clientBillingCode: str
    name: str
    budget: str
    kind: str
    lastModifiedInfo: LastModifiedInfo
    clientName: str
    advertiserId: str
    targetConversions: str
    targetCpcNanos: str
    targetCpmNanos: str
    overview: str

class Advertiser(typing_extensions.TypedDict, total=False):
    suspended: bool
    subaccountId: str
    kind: str
    clickThroughUrlSuffix: str
    name: str
    status: typing_extensions.Literal["APPROVED", "ON_HOLD"]
    defaultEmail: str
    id: str
    accountId: str
    defaultClickThroughEventTagId: str
    idDimensionValue: DimensionValue
    originalFloodlightConfigurationId: str
    advertiserGroupId: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    floodlightConfigurationId: str

class Conversion(typing_extensions.TypedDict, total=False):
    childDirectedTreatment: bool
    floodlightActivityId: str
    encryptedUserId: str
    floodlightConfigurationId: str
    matchId: str
    timestampMicros: str
    nonPersonalizedAd: bool
    kind: str
    treatmentForUnderage: bool
    limitAdTracking: bool
    ordinal: str
    gclid: str
    quantity: str
    encryptedUserIdCandidates: typing.List[str]
    customVariables: typing.List[CustomFloodlightVariable]
    value: float
    mobileDeviceId: str
    dclid: str

class Dimension(typing_extensions.TypedDict, total=False):
    name: str
    kind: str

class PathFilter(typing_extensions.TypedDict, total=False):
    kind: str
    pathMatchPosition: typing_extensions.Literal[
        "PATH_MATCH_POSITION_UNSPECIFIED", "ANY", "FIRST", "LAST"
    ]
    eventFilters: typing.List[EventFilter]

class ReportList(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Report]
    etag: str
    kind: str

class OrdersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    orders: typing.List[Order]

class ListPopulationRule(typing_extensions.TypedDict, total=False):
    floodlightActivityName: str
    listPopulationClauses: typing.List[ListPopulationClause]
    floodlightActivityId: str

class AudienceSegmentGroup(typing_extensions.TypedDict, total=False):
    id: str
    audienceSegments: typing.List[AudienceSegment]
    name: str

class PlacementStrategy(typing_extensions.TypedDict, total=False):
    accountId: str
    kind: str
    name: str
    id: str

class FloodlightActivityGroupsListResponse(typing_extensions.TypedDict, total=False):
    floodlightActivityGroups: typing.List[FloodlightActivityGroup]
    kind: str
    nextPageToken: str

class ConnectionTypesListResponse(typing_extensions.TypedDict, total=False):
    connectionTypes: typing.List[ConnectionType]
    kind: str

class CountriesListResponse(typing_extensions.TypedDict, total=False):
    countries: typing.List[Country]
    kind: str

class EventFilter(typing_extensions.TypedDict, total=False):
    kind: str
    dimensionFilter: PathReportDimensionValue

class ObjectFilter(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal["NONE", "ASSIGNED", "ALL"]
    objectIds: typing.List[str]
    kind: str

class VideoSettings(typing_extensions.TypedDict, total=False):
    orientation: typing_extensions.Literal["ANY", "LANDSCAPE", "PORTRAIT"]
    obaEnabled: bool
    transcodeSettings: TranscodeSetting
    skippableSettings: SkippableSetting
    obaSettings: ObaIcon
    kind: str
    companionSettings: CompanionSetting

class EventTagsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    eventTags: typing.List[EventTag]

class CampaignsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    campaigns: typing.List[Campaign]
    kind: str

class AdBlockingConfiguration(typing_extensions.TypedDict, total=False):
    creativeBundleId: str
    clickThroughUrl: str
    enabled: bool
    overrideClickThroughUrl: bool

class CustomEventInsert(typing_extensions.TypedDict, total=False):
    matchId: str
    cmDimensions: CampaignManagerIds
    insertEventType: typing_extensions.Literal["UNKNOWN", "IMPRESSION", "CLICK"]
    dv3Dimensions: DV3Ids
    mobileDeviceId: str
    kind: str

class CreativeGroupAssignment(typing_extensions.TypedDict, total=False):
    creativeGroupId: str
    creativeGroupNumber: typing_extensions.Literal[
        "CREATIVE_GROUP_ONE", "CREATIVE_GROUP_TWO"
    ]

class PathReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensions: typing.List[Dimension]
    pathFilters: typing.List[Dimension]
    channelGroupings: typing.List[Dimension]
    kind: str
    metrics: typing.List[Metric]

class SiteSkippableSetting(typing_extensions.TypedDict, total=False):
    skipOffset: VideoOffset
    progressOffset: VideoOffset
    skippable: bool
    kind: str

class SiteContact(typing_extensions.TypedDict, total=False):
    address: str
    email: str
    phone: str
    title: str
    id: str
    lastName: str
    contactType: typing_extensions.Literal["SALES_PERSON", "TRAFFICKER"]
    firstName: str

class CreativeField(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    accountId: str
    kind: str
    subaccountId: str

class CustomViewabilityMetricConfiguration(typing_extensions.TypedDict, total=False):
    timePercent: int
    viewabilityPercent: int
    timeMillis: int
    audible: bool

class ConversionsBatchInsertRequest(typing_extensions.TypedDict, total=False):
    conversions: typing.List[Conversion]
    kind: str
    encryptionInfo: EncryptionInfo

class OperatingSystemsListResponse(typing_extensions.TypedDict, total=False):
    operatingSystems: typing.List[OperatingSystem]
    kind: str

class TargetingTemplatesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    targetingTemplates: typing.List[TargetingTemplate]
    nextPageToken: str

class AdvertisersListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    advertisers: typing.List[Advertiser]
    kind: str

class AccountUserProfile(typing_extensions.TypedDict, total=False):
    name: str
    accountId: str
    kind: str
    subaccountId: str
    active: bool
    userRoleFilter: ObjectFilter
    advertiserFilter: ObjectFilter
    email: str
    id: str
    traffickerType: typing_extensions.Literal[
        "INTERNAL_NON_TRAFFICKER", "INTERNAL_TRAFFICKER", "EXTERNAL_TRAFFICKER"
    ]
    userAccessType: typing_extensions.Literal[
        "NORMAL_USER", "SUPER_USER", "INTERNAL_ADMINISTRATOR", "READ_ONLY_SUPER_USER"
    ]
    locale: str
    siteFilter: ObjectFilter
    campaignFilter: ObjectFilter
    userRoleId: str
    comments: str

class AccountUserProfilesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    accountUserProfiles: typing.List[AccountUserProfile]
    nextPageToken: str

class DefaultClickThroughEventTagProperties(typing_extensions.TypedDict, total=False):
    overrideInheritedEventTag: bool
    defaultClickThroughEventTagId: str

class FileList(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    items: typing.List[File]
    nextPageToken: str

class CreativeGroupsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    creativeGroups: typing.List[CreativeGroup]
    nextPageToken: str

class PlacementsListResponse(typing_extensions.TypedDict, total=False):
    placements: typing.List[Placement]
    nextPageToken: str
    kind: str

class AccountPermission(typing_extensions.TypedDict, total=False):
    name: str
    kind: str
    permissionGroupId: str
    accountProfiles: typing.List[str]
    level: typing_extensions.Literal["USER", "ADMINISTRATOR"]
    id: str

class MobileAppsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    mobileApps: typing.List[MobileApp]
    kind: str

class OrderDocumentsListResponse(typing_extensions.TypedDict, total=False):
    orderDocuments: typing.List[OrderDocument]
    nextPageToken: str
    kind: str

class CompanionClickThroughOverride(typing_extensions.TypedDict, total=False):
    creativeId: str
    clickThroughUrl: ClickThroughUrl

class ClickThroughUrl(typing_extensions.TypedDict, total=False):
    defaultLandingPage: bool
    computedClickThroughUrl: str
    customClickThroughUrl: str
    landingPageId: str

class PathReportDimensionValue(typing_extensions.TypedDict, total=False):
    dimensionName: str
    matchType: typing_extensions.Literal[
        "EXACT", "BEGINS_WITH", "CONTAINS", "WILDCARD_EXPRESSION"
    ]
    values: typing.List[str]
    kind: str
    ids: typing.List[str]

class CreativeCustomEvent(typing_extensions.TypedDict, total=False):
    exitClickThroughUrl: CreativeClickThroughUrl
    id: str
    popupWindowProperties: PopupWindowProperties
    videoReportingId: str
    artworkLabel: str
    advertiserCustomEventType: typing_extensions.Literal[
        "ADVERTISER_EVENT_TIMER", "ADVERTISER_EVENT_EXIT", "ADVERTISER_EVENT_COUNTER"
    ]
    targetType: typing_extensions.Literal[
        "TARGET_BLANK", "TARGET_TOP", "TARGET_SELF", "TARGET_PARENT", "TARGET_POPUP"
    ]
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    advertiserCustomEventName: str
    advertiserCustomEventId: str

class UserProfile(typing_extensions.TypedDict, total=False):
    subAccountId: str
    subAccountName: str
    accountId: str
    accountName: str
    kind: str
    profileId: str
    etag: str
    userName: str

class AccountPermissionGroupsListResponse(typing_extensions.TypedDict, total=False):
    accountPermissionGroups: typing.List[AccountPermissionGroup]
    kind: str

class RemarketingListsListResponse(typing_extensions.TypedDict, total=False):
    remarketingLists: typing.List[RemarketingList]
    nextPageToken: str
    kind: str

class OptimizationActivity(typing_extensions.TypedDict, total=False):
    weight: int
    floodlightActivityId: str
    floodlightActivityIdDimensionValue: DimensionValue

class CustomEventStatus(typing_extensions.TypedDict, total=False):
    kind: str
    errors: typing.List[CustomEventError]
    customEvent: CustomEvent

class VideoFormat(typing_extensions.TypedDict, total=False):
    fileType: typing_extensions.Literal["FLV", "THREEGPP", "MP4", "WEBM", "M3U8"]
    kind: str
    targetBitRate: int
    id: int
    resolution: Size

class PlacementGroup(typing_extensions.TypedDict, total=False):
    kind: str
    contentCategoryId: str
    siteId: str
    directorySiteId: str
    accountId: str
    siteIdDimensionValue: DimensionValue
    name: str
    advertiserId: str
    subaccountId: str
    advertiserIdDimensionValue: DimensionValue
    idDimensionValue: DimensionValue
    directorySiteIdDimensionValue: DimensionValue
    campaignId: str
    createInfo: LastModifiedInfo
    placementGroupType: typing_extensions.Literal[
        "PLACEMENT_PACKAGE", "PLACEMENT_ROADBLOCK"
    ]
    primaryPlacementId: str
    primaryPlacementIdDimensionValue: DimensionValue
    pricingSchedule: PricingSchedule
    id: str
    lastModifiedInfo: LastModifiedInfo
    placementStrategyId: str
    campaignIdDimensionValue: DimensionValue
    comment: str
    archived: bool
    childPlacementIds: typing.List[str]
    externalId: str

class OmnitureSettings(typing_extensions.TypedDict, total=False):
    omnitureIntegrationEnabled: bool
    omnitureCostDataEnabled: bool

class LandingPage(typing_extensions.TypedDict, total=False):
    url: str
    archived: bool
    advertiserId: str
    kind: str
    name: str
    deepLinks: typing.List[DeepLink]
    id: str

class CreativeAssetMetadata(typing_extensions.TypedDict, total=False):
    timerCustomEvents: typing.List[CreativeCustomEvent]
    kind: str
    id: str
    assetIdentifier: CreativeAssetId
    idDimensionValue: DimensionValue
    warnedValidationRules: typing.List[str]
    richMedia: bool
    exitCustomEvents: typing.List[CreativeCustomEvent]
    detectedFeatures: typing.List[str]
    clickTags: typing.List[ClickTag]
    counterCustomEvents: typing.List[CreativeCustomEvent]

class UserDefinedVariableConfiguration(typing_extensions.TypedDict, total=False):
    reportName: str
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

class Subaccount(typing_extensions.TypedDict, total=False):
    accountId: str
    name: str
    id: str
    availablePermissionIds: typing.List[str]
    kind: str

class TargetingTemplate(typing_extensions.TypedDict, total=False):
    listTargetingExpression: ListTargetingExpression
    accountId: str
    languageTargeting: LanguageTargeting
    advertiserId: str
    subaccountId: str
    geoTargeting: GeoTargeting
    dayPartTargeting: DayPartTargeting
    kind: str
    name: str
    keyValueTargetingExpression: KeyValueTargetingExpression
    advertiserIdDimensionValue: DimensionValue
    technologyTargeting: TechnologyTargeting
    id: str

class UserRole(typing_extensions.TypedDict, total=False):
    accountId: str
    defaultUserRole: bool
    name: str
    parentUserRoleId: str
    id: str
    subaccountId: str
    kind: str
    permissions: typing.List[UserRolePermission]

class CompanionSetting(typing_extensions.TypedDict, total=False):
    imageOnly: bool
    companionsDisabled: bool
    kind: str
    enabledSizes: typing.List[Size]

class PathToConversionReportCompatibleFields(typing_extensions.TypedDict, total=False):
    kind: str
    customFloodlightVariables: typing.List[Dimension]
    perInteractionDimensions: typing.List[Dimension]
    metrics: typing.List[Metric]
    conversionDimensions: typing.List[Dimension]

class ClickTag(typing_extensions.TypedDict, total=False):
    name: str
    eventName: str
    clickThroughUrl: CreativeClickThroughUrl

class ConversionsBatchUpdateRequest(typing_extensions.TypedDict, total=False):
    encryptionInfo: EncryptionInfo
    kind: str
    conversions: typing.List[Conversion]

class SizesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    sizes: typing.List[Size]

class PlacementTag(typing_extensions.TypedDict, total=False):
    placementId: str
    tagDatas: typing.List[TagData]

class RegionsListResponse(typing_extensions.TypedDict, total=False):
    regions: typing.List[Region]
    kind: str

class CompatibleFields(typing_extensions.TypedDict, total=False):
    reportCompatibleFields: ReportCompatibleFields
    crossDimensionReachReportCompatibleFields: CrossDimensionReachReportCompatibleFields
    pathReportCompatibleFields: PathReportCompatibleFields
    kind: str
    reachReportCompatibleFields: ReachReportCompatibleFields
    floodlightReportCompatibleFields: FloodlightReportCompatibleFields
    pathToConversionReportCompatibleFields: PathToConversionReportCompatibleFields
    pathAttributionReportCompatibleFields: PathReportCompatibleFields

class CustomEventError(typing_extensions.TypedDict, total=False):
    kind: str
    message: str
    code: typing_extensions.Literal[
        "UNKNOWN", "INVALID_ARGUMENT", "INTERNAL", "PERMISSION_DENIED", "NOT_FOUND"
    ]

class DfpSettings(typing_extensions.TypedDict, total=False):
    programmaticPlacementAccepted: bool
    pubPaidPlacementAccepted: bool
    dfpNetworkCode: str
    publisherPortalOnly: bool
    dfpNetworkName: str

class DisjunctiveMatchStatement(typing_extensions.TypedDict, total=False):
    eventFilters: typing.List[EventFilter]
    kind: str

class LastModifiedInfo(typing_extensions.TypedDict, total=False):
    time: str

class PopupWindowProperties(typing_extensions.TypedDict, total=False):
    title: str
    showScrollBar: bool
    positionType: typing_extensions.Literal["CENTER", "COORDINATES"]
    showAddressBar: bool
    dimension: Size
    showStatusBar: bool
    offset: OffsetPosition
    showMenuBar: bool
    showToolBar: bool

class DateRange(typing_extensions.TypedDict, total=False):
    kind: str
    startDate: str
    endDate: str
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

class AudienceSegment(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    allocation: int

class EncryptionInfo(typing_extensions.TypedDict, total=False):
    encryptionSource: typing_extensions.Literal[
        "ENCRYPTION_SCOPE_UNKNOWN", "AD_SERVING", "DATA_TRANSFER"
    ]
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
    encryptionEntityId: str

class InventoryItemsListResponse(typing_extensions.TypedDict, total=False):
    inventoryItems: typing.List[InventoryItem]
    nextPageToken: str
    kind: str
