import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountPermissionIds: _list[str]
    accountProfile: typing_extensions.Literal[
        "ACCOUNT_PROFILE_BASIC", "ACCOUNT_PROFILE_STANDARD"
    ]
    active: bool
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
    activeViewOptOut: bool
    availablePermissionIds: _list[str]
    countryId: str
    currencyId: str
    defaultCreativeSizeId: str
    description: str
    id: str
    kind: str
    locale: str
    maximumImageSize: str
    name: str
    nielsenOcrEnabled: bool
    reportsConfiguration: ReportsConfiguration
    shareReportsWithTwitter: bool
    teaserSizeLimit: str

@typing.type_check_only
class AccountActiveAdSummary(typing_extensions.TypedDict, total=False):
    accountId: str
    activeAds: str
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
    availableAds: str
    kind: str

@typing.type_check_only
class AccountPermission(typing_extensions.TypedDict, total=False):
    accountProfiles: _list[
        typing_extensions.Literal["ACCOUNT_PROFILE_BASIC", "ACCOUNT_PROFILE_STANDARD"]
    ]
    id: str
    kind: str
    level: typing_extensions.Literal["USER", "ADMINISTRATOR"]
    name: str
    permissionGroupId: str

@typing.type_check_only
class AccountPermissionGroup(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class AccountPermissionGroupsListResponse(typing_extensions.TypedDict, total=False):
    accountPermissionGroups: _list[AccountPermissionGroup]
    kind: str

@typing.type_check_only
class AccountPermissionsListResponse(typing_extensions.TypedDict, total=False):
    accountPermissions: _list[AccountPermission]
    kind: str

@typing.type_check_only
class AccountUserProfile(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    advertiserFilter: ObjectFilter
    campaignFilter: ObjectFilter
    comments: str
    email: str
    id: str
    kind: str
    locale: str
    name: str
    siteFilter: ObjectFilter
    subaccountId: str
    traffickerType: typing_extensions.Literal[
        "INTERNAL_NON_TRAFFICKER", "INTERNAL_TRAFFICKER", "EXTERNAL_TRAFFICKER"
    ]
    userAccessType: typing_extensions.Literal[
        "NORMAL_USER", "SUPER_USER", "INTERNAL_ADMINISTRATOR", "READ_ONLY_SUPER_USER"
    ]
    userRoleFilter: ObjectFilter
    userRoleId: str

@typing.type_check_only
class AccountUserProfilesListResponse(typing_extensions.TypedDict, total=False):
    accountUserProfiles: _list[AccountUserProfile]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AccountsListResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Activities(typing_extensions.TypedDict, total=False):
    filters: _list[DimensionValue]
    kind: str
    metricNames: _list[str]

@typing.type_check_only
class Ad(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    archived: bool
    audienceSegmentId: str
    campaignId: str
    campaignIdDimensionValue: DimensionValue
    clickThroughUrl: ClickThroughUrl
    clickThroughUrlSuffixProperties: ClickThroughUrlSuffixProperties
    comments: str
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    contextualKeywordTargeting: ContextualKeywordTargeting
    createInfo: LastModifiedInfo
    creativeGroupAssignments: _list[CreativeGroupAssignment]
    creativeRotation: CreativeRotation
    dayPartTargeting: DayPartTargeting
    defaultClickThroughEventTagProperties: DefaultClickThroughEventTagProperties
    deliverySchedule: DeliverySchedule
    dynamicClickTracker: bool
    endTime: str
    eventTagOverrides: _list[EventTagOverride]
    geoTargeting: GeoTargeting
    id: str
    idDimensionValue: DimensionValue
    keyValueTargetingExpression: KeyValueTargetingExpression
    kind: str
    languageTargeting: LanguageTargeting
    lastModifiedInfo: LastModifiedInfo
    name: str
    placementAssignments: _list[PlacementAssignment]
    remarketingListExpression: ListTargetingExpression
    size: Size
    sslCompliant: bool
    sslRequired: bool
    startTime: str
    subaccountId: str
    targetingTemplateId: str
    technologyTargeting: TechnologyTargeting
    type: typing_extensions.Literal[
        "AD_SERVING_STANDARD_AD",
        "AD_SERVING_DEFAULT_AD",
        "AD_SERVING_CLICK_TRACKER",
        "AD_SERVING_TRACKING",
        "AD_SERVING_BRAND_SAFE_AD",
    ]

@typing.type_check_only
class AdBlockingConfiguration(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AdsListResponse(typing_extensions.TypedDict, total=False):
    ads: _list[Ad]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Advertiser(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserGroupId: str
    clickThroughUrlSuffix: str
    defaultClickThroughEventTagId: str
    defaultEmail: str
    euPoliticalAdsDeclaration: typing_extensions.Literal[
        "ADVERTISER_PLANS_TO_SERVE_EU_POLITICAL_ADS",
        "ADVERTISER_DOES_NOT_PLAN_TO_SERVE_EU_POLITICAL_ADS",
    ]
    floodlightConfigurationId: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    id: str
    idDimensionValue: DimensionValue
    kind: str
    measurementPartnerLink: MeasurementPartnerAdvertiserLink
    name: str
    originalFloodlightConfigurationId: str
    status: typing_extensions.Literal["APPROVED", "ON_HOLD"]
    subaccountId: str
    suspended: bool

@typing.type_check_only
class AdvertiserGroup(typing_extensions.TypedDict, total=False):
    accountId: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class AdvertiserGroupsListResponse(typing_extensions.TypedDict, total=False):
    advertiserGroups: _list[AdvertiserGroup]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AdvertiserInvoicesListResponse(typing_extensions.TypedDict, total=False):
    invoices: _list[Invoice]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AdvertiserLandingPagesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    landingPages: _list[LandingPage]
    nextPageToken: str

@typing.type_check_only
class AdvertisersListResponse(typing_extensions.TypedDict, total=False):
    advertisers: _list[Advertiser]
    kind: str
    nextPageToken: str

@typing.type_check_only
class AudienceSegment(typing_extensions.TypedDict, total=False):
    allocation: int
    id: str
    name: str

@typing.type_check_only
class AudienceSegmentGroup(typing_extensions.TypedDict, total=False):
    audienceSegments: _list[AudienceSegment]
    id: str
    name: str

@typing.type_check_only
class BillingAssignment(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    campaignId: str
    kind: str
    subaccountId: str

@typing.type_check_only
class BillingAssignmentsListResponse(typing_extensions.TypedDict, total=False):
    billingAssignments: _list[BillingAssignment]
    kind: str

@typing.type_check_only
class BillingProfile(typing_extensions.TypedDict, total=False):
    consolidatedInvoice: bool
    countryCode: str
    currencyCode: str
    id: str
    invoiceLevel: typing_extensions.Literal[
        "ACCOUNT_LEVEL", "ADVERTISER_LEVEL", "CAMPAIGN_LEVEL"
    ]
    isDefault: bool
    kind: str
    name: str
    paymentsAccountId: str
    paymentsCustomerId: str
    purchaseOrder: str
    secondaryPaymentsCustomerId: str
    status: typing_extensions.Literal["UNDER_REVIEW", "ACTIVE", "ARCHIVED"]

@typing.type_check_only
class BillingProfilesListResponse(typing_extensions.TypedDict, total=False):
    billingProfiles: _list[BillingProfile]
    kind: str
    nextPageToken: str

@typing.type_check_only
class BillingRate(typing_extensions.TypedDict, total=False):
    currencyCode: str
    endDate: str
    id: str
    name: str
    rateInMicros: str
    startDate: str
    tieredRates: _list[BillingRateTieredRate]
    type: typing_extensions.Literal[
        "AD_SERVING",
        "CLICKS",
        "MINIMUM_SERVICE",
        "PATH_TO_CONVERSION",
        "RICH_MEDIA_INPAGE",
        "RICH_MEDIA_EXPANDING",
        "RICH_MEDIA_FLOATING",
        "RICH_MEDIA_VIDEO",
        "RICH_MEDIA_TEASER",
        "RICH_MEDIA_VPAID",
        "INSTREAM_VIDEO",
        "PIXEL",
        "TRACKING",
        "TRAFFICKING_FEATURE",
        "CUSTOM_REPORTS",
        "EXPOSURE_TO_CONVERSION",
        "DATA_TRANSFER",
        "DATA_TRANSFER_SETUP",
        "STARTUP",
        "STATEMENT_OF_WORK",
        "PROVIDED_LIST",
        "PROVIDED_LIST_SETUP",
        "ENHANCED_FORMATS",
        "TRACKING_AD_IMPRESSIONS",
        "TRACKING_AD_CLICKS",
        "NIELSEN_DIGITAL_AD_RATINGS_FEE",
        "INSTREAM_VIDEO_REDIRECT",
        "INSTREAM_VIDEO_VPAID",
        "DISPLAY_AD_SERVING",
        "VIDEO_AD_SERVING",
        "AUDIO_AD_SERVING",
        "ADVANCED_DISPLAY_AD_SERVING",
    ]
    unitOfMeasure: typing_extensions.Literal["CPM", "CPC", "EA", "P2C"]

@typing.type_check_only
class BillingRateTieredRate(typing_extensions.TypedDict, total=False):
    highValue: str
    lowValue: str
    rateInMicros: str

@typing.type_check_only
class BillingRatesListResponse(typing_extensions.TypedDict, total=False):
    billingRates: _list[BillingRate]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Browser(typing_extensions.TypedDict, total=False):
    browserVersionId: str
    dartId: str
    kind: str
    majorVersion: str
    minorVersion: str
    name: str

@typing.type_check_only
class BrowsersListResponse(typing_extensions.TypedDict, total=False):
    browsers: _list[Browser]
    kind: str

@typing.type_check_only
class Campaign(typing_extensions.TypedDict, total=False):
    accountId: str
    adBlockingConfiguration: AdBlockingConfiguration
    additionalCreativeOptimizationConfigurations: _list[
        CreativeOptimizationConfiguration
    ]
    advertiserGroupId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    archived: bool
    audienceSegmentGroups: _list[AudienceSegmentGroup]
    billingInvoiceCode: str
    clickThroughUrlSuffixProperties: ClickThroughUrlSuffixProperties
    comment: str
    createInfo: LastModifiedInfo
    creativeGroupIds: _list[str]
    creativeOptimizationConfiguration: CreativeOptimizationConfiguration
    defaultClickThroughEventTagProperties: DefaultClickThroughEventTagProperties
    defaultLandingPageId: str
    endDate: str
    euPoliticalAdsDeclaration: typing_extensions.Literal[
        "CONTAINS_EU_POLITICAL_ADS", "DOES_NOT_CONTAIN_EU_POLITICAL_ADS"
    ]
    eventTagOverrides: _list[EventTagOverride]
    externalId: str
    id: str
    idDimensionValue: DimensionValue
    kind: str
    lastModifiedInfo: LastModifiedInfo
    measurementPartnerLink: MeasurementPartnerCampaignLink
    name: str
    startDate: str
    subaccountId: str

@typing.type_check_only
class CampaignCreativeAssociation(typing_extensions.TypedDict, total=False):
    creativeId: str
    kind: str

@typing.type_check_only
class CampaignCreativeAssociationsListResponse(
    typing_extensions.TypedDict, total=False
):
    campaignCreativeAssociations: _list[CampaignCreativeAssociation]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CampaignSummary(typing_extensions.TypedDict, total=False):
    billingInvoiceCode: str
    campaignId: str
    preTaxAmountMicros: str
    taxAmountMicros: str
    totalAmountMicros: str

@typing.type_check_only
class CampaignsListResponse(typing_extensions.TypedDict, total=False):
    campaigns: _list[Campaign]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CartData(typing_extensions.TypedDict, total=False):
    items: _list[CartDataItem]
    merchantFeedLabel: str
    merchantFeedLanguage: str
    merchantId: str

@typing.type_check_only
class CartDataItem(typing_extensions.TypedDict, total=False):
    itemId: str
    quantity: int
    unitPrice: float

@typing.type_check_only
class ChangeLog(typing_extensions.TypedDict, total=False):
    accountId: str
    action: str
    changeTime: str
    fieldName: str
    id: str
    kind: str
    newValue: str
    objectId: str
    objectType: str
    oldValue: str
    subaccountId: str
    transactionId: str
    userProfileId: str
    userProfileName: str

@typing.type_check_only
class ChangeLogsListResponse(typing_extensions.TypedDict, total=False):
    changeLogs: _list[ChangeLog]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CitiesListResponse(typing_extensions.TypedDict, total=False):
    cities: _list[City]
    kind: str

@typing.type_check_only
class City(typing_extensions.TypedDict, total=False):
    countryCode: str
    countryDartId: str
    dartId: str
    kind: str
    metroCode: str
    metroDmaId: str
    name: str
    regionCode: str
    regionDartId: str

@typing.type_check_only
class ClickTag(typing_extensions.TypedDict, total=False):
    clickThroughUrl: CreativeClickThroughUrl
    eventName: str
    name: str

@typing.type_check_only
class ClickThroughUrl(typing_extensions.TypedDict, total=False):
    computedClickThroughUrl: str
    customClickThroughUrl: str
    defaultLandingPage: bool
    landingPageId: str

@typing.type_check_only
class ClickThroughUrlSuffixProperties(typing_extensions.TypedDict, total=False):
    clickThroughUrlSuffix: str
    overrideInheritedSuffix: bool

@typing.type_check_only
class CompanionClickThroughOverride(typing_extensions.TypedDict, total=False):
    clickThroughUrl: ClickThroughUrl
    creativeId: str

@typing.type_check_only
class CompanionSetting(typing_extensions.TypedDict, total=False):
    companionsDisabled: bool
    enabledSizes: _list[Size]
    imageOnly: bool
    kind: str

@typing.type_check_only
class CompatibleFields(typing_extensions.TypedDict, total=False):
    crossDimensionReachReportCompatibleFields: CrossDimensionReachReportCompatibleFields
    crossMediaReachReportCompatibleFields: CrossMediaReachReportCompatibleFields
    floodlightReportCompatibleFields: FloodlightReportCompatibleFields
    kind: str
    pathToConversionReportCompatibleFields: PathToConversionReportCompatibleFields
    reachReportCompatibleFields: ReachReportCompatibleFields
    reportCompatibleFields: ReportCompatibleFields

@typing.type_check_only
class ConnectionType(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class ConnectionTypesListResponse(typing_extensions.TypedDict, total=False):
    connectionTypes: _list[ConnectionType]
    kind: str

@typing.type_check_only
class ContentCategoriesListResponse(typing_extensions.TypedDict, total=False):
    contentCategories: _list[ContentCategory]
    kind: str
    nextPageToken: str

@typing.type_check_only
class ContentCategory(typing_extensions.TypedDict, total=False):
    accountId: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class ContentSource(typing_extensions.TypedDict, total=False):
    contentSourceName: str
    createInfo: LastModifiedInfo
    lastModifiedInfo: LastModifiedInfo
    metaData: ContentSourceMetaData
    resourceLink: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "RESOURCE_TYPE_GOOGLE_SPREADSHEET",
        "RESOURCE_TYPE_REMOTE_FILE",
    ]

@typing.type_check_only
class ContentSourceMetaData(typing_extensions.TypedDict, total=False):
    charset: str
    fieldNames: _list[str]
    rowNumber: int
    separator: str

@typing.type_check_only
class ContextualKeyword(typing_extensions.TypedDict, total=False):
    keyword: str

@typing.type_check_only
class ContextualKeywordTargeting(typing_extensions.TypedDict, total=False):
    keywords: _list[ContextualKeyword]

@typing.type_check_only
class Conversion(typing_extensions.TypedDict, total=False):
    adUserDataConsent: typing_extensions.Literal["GRANTED", "DENIED"]
    cartData: CartData
    childDirectedTreatment: bool
    customVariables: _list[CustomFloodlightVariable]
    dclid: str
    encryptedUserId: str
    encryptedUserIdCandidates: _list[str]
    floodlightActivityId: str
    floodlightConfigurationId: str
    gclid: str
    impressionId: str
    kind: str
    limitAdTracking: bool
    matchId: str
    mobileDeviceId: str
    nonPersonalizedAd: bool
    ordinal: str
    quantity: str
    sessionAttributesEncoded: str
    timestampMicros: str
    treatmentForUnderage: bool
    userIdentifiers: _list[UserIdentifier]
    value: float

@typing.type_check_only
class ConversionError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "INVALID_ARGUMENT", "INTERNAL", "PERMISSION_DENIED", "NOT_FOUND"
    ]
    kind: str
    message: str

@typing.type_check_only
class ConversionStatus(typing_extensions.TypedDict, total=False):
    conversion: Conversion
    errors: _list[ConversionError]
    kind: str

@typing.type_check_only
class ConversionsBatchInsertRequest(typing_extensions.TypedDict, total=False):
    conversions: _list[Conversion]
    encryptionInfo: EncryptionInfo
    kind: str

@typing.type_check_only
class ConversionsBatchInsertResponse(typing_extensions.TypedDict, total=False):
    hasFailures: bool
    kind: str
    status: _list[ConversionStatus]

@typing.type_check_only
class ConversionsBatchUpdateRequest(typing_extensions.TypedDict, total=False):
    conversions: _list[Conversion]
    encryptionInfo: EncryptionInfo
    kind: str

@typing.type_check_only
class ConversionsBatchUpdateResponse(typing_extensions.TypedDict, total=False):
    hasFailures: bool
    kind: str
    status: _list[ConversionStatus]

@typing.type_check_only
class CountriesListResponse(typing_extensions.TypedDict, total=False):
    countries: _list[Country]
    kind: str

@typing.type_check_only
class Country(typing_extensions.TypedDict, total=False):
    countryCode: str
    dartId: str
    kind: str
    name: str
    sslEnabled: bool
    tvDataProviders: _list[
        typing_extensions.Literal[
            "INVALID_TV_DATA_PROVIDER",
            "IBOPE_AR",
            "IBOPE_BR",
            "IBOPE_CL",
            "IBOPE_CO",
            "TNS_VN",
            "COMSCORE_NATIONAL_US",
            "COMSCORE_CA",
            "SAMBA_AU",
        ]
    ]

@typing.type_check_only
class Creative(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    adParameters: str
    adTagKeys: _list[str]
    additionalSizes: _list[Size]
    advertiserId: str
    allowScriptAccess: bool
    archived: bool
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    authoringSource: typing_extensions.Literal[
        "CREATIVE_AUTHORING_SOURCE_DCM",
        "CREATIVE_AUTHORING_SOURCE_DBM",
        "CREATIVE_AUTHORING_SOURCE_STUDIO",
        "CREATIVE_AUTHORING_SOURCE_GWD",
        "CREATIVE_AUTHORING_SOURCE_ACS",
        "CREATIVE_AUTHORING_SOURCE_ADOBE",
        "CREATIVE_AUTHORING_SOURCE_TYPEFACE_AI",
        "CREATIVE_AUTHORING_SOURCE_REMBRAND",
        "CREATIVE_AUTHORING_SOURCE_TRACKTO_STUDIO",
        "CREATIVE_AUTHORING_SOURCE_BORNLOGIC",
    ]
    authoringTool: typing_extensions.Literal["NINJA", "SWIFFY"]
    autoAdvanceImages: bool
    backgroundColor: str
    backupImageClickThroughUrl: CreativeClickThroughUrl
    backupImageFeatures: _list[
        typing_extensions.Literal[
            "CSS_FONT_FACE",
            "CSS_BACKGROUND_SIZE",
            "CSS_BORDER_IMAGE",
            "CSS_BORDER_RADIUS",
            "CSS_BOX_SHADOW",
            "CSS_FLEX_BOX",
            "CSS_HSLA",
            "CSS_MULTIPLE_BGS",
            "CSS_OPACITY",
            "CSS_RGBA",
            "CSS_TEXT_SHADOW",
            "CSS_ANIMATIONS",
            "CSS_COLUMNS",
            "CSS_GENERATED_CONTENT",
            "CSS_GRADIENTS",
            "CSS_REFLECTIONS",
            "CSS_TRANSFORMS",
            "CSS_TRANSFORMS3D",
            "CSS_TRANSITIONS",
            "APPLICATION_CACHE",
            "CANVAS",
            "CANVAS_TEXT",
            "DRAG_AND_DROP",
            "HASH_CHANGE",
            "HISTORY",
            "AUDIO",
            "VIDEO",
            "INDEXED_DB",
            "INPUT_ATTR_AUTOCOMPLETE",
            "INPUT_ATTR_AUTOFOCUS",
            "INPUT_ATTR_LIST",
            "INPUT_ATTR_PLACEHOLDER",
            "INPUT_ATTR_MAX",
            "INPUT_ATTR_MIN",
            "INPUT_ATTR_MULTIPLE",
            "INPUT_ATTR_PATTERN",
            "INPUT_ATTR_REQUIRED",
            "INPUT_ATTR_STEP",
            "INPUT_TYPE_SEARCH",
            "INPUT_TYPE_TEL",
            "INPUT_TYPE_URL",
            "INPUT_TYPE_EMAIL",
            "INPUT_TYPE_DATETIME",
            "INPUT_TYPE_DATE",
            "INPUT_TYPE_MONTH",
            "INPUT_TYPE_WEEK",
            "INPUT_TYPE_TIME",
            "INPUT_TYPE_DATETIME_LOCAL",
            "INPUT_TYPE_NUMBER",
            "INPUT_TYPE_RANGE",
            "INPUT_TYPE_COLOR",
            "LOCAL_STORAGE",
            "POST_MESSAGE",
            "SESSION_STORAGE",
            "WEB_SOCKETS",
            "WEB_SQL_DATABASE",
            "WEB_WORKERS",
            "GEO_LOCATION",
            "INLINE_SVG",
            "SMIL",
            "SVG_HREF",
            "SVG_CLIP_PATHS",
            "TOUCH",
            "WEBGL",
            "SVG_FILTERS",
            "SVG_FE_IMAGE",
        ]
    ]
    backupImageReportingLabel: str
    backupImageTargetWindow: TargetWindow
    clickTags: _list[ClickTag]
    commercialId: str
    companionCreatives: _list[str]
    compatibility: _list[
        typing_extensions.Literal[
            "DISPLAY",
            "DISPLAY_INTERSTITIAL",
            "APP",
            "APP_INTERSTITIAL",
            "IN_STREAM_VIDEO",
            "IN_STREAM_AUDIO",
        ]
    ]
    convertFlashToHtml5: bool
    counterCustomEvents: _list[CreativeCustomEvent]
    creativeAssets: _list[CreativeAsset]
    creativeFieldAssignments: _list[CreativeFieldAssignment]
    customKeyValues: _list[str]
    exitCustomEvents: _list[CreativeCustomEvent]
    fsCommand: FsCommand
    htmlCode: str
    htmlCodeLocked: bool
    id: str
    idDimensionValue: DimensionValue
    kind: str
    lastModifiedInfo: LastModifiedInfo
    latestTraffickedCreativeId: str
    mediaDescription: str
    mediaDuration: float
    name: str
    obaIcon: ObaIcon
    overrideCss: str
    progressOffset: VideoOffset
    redirectUrl: str
    renderingId: str
    renderingIdDimensionValue: DimensionValue
    requiredFlashPluginVersion: str
    requiredFlashVersion: int
    size: Size
    skipOffset: VideoOffset
    skippable: bool
    sslCompliant: bool
    sslOverride: bool
    studioAdvertiserId: str
    studioCreativeId: str
    studioTraffickedCreativeId: str
    subaccountId: str
    thirdPartyBackupImageImpressionsUrl: str
    thirdPartyRichMediaImpressionsUrl: str
    thirdPartyUrls: _list[ThirdPartyTrackingUrl]
    timerCustomEvents: _list[CreativeCustomEvent]
    totalFileSize: str
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
    universalAdId: UniversalAdId
    version: int

@typing.type_check_only
class CreativeAsset(typing_extensions.TypedDict, total=False):
    actionScript3: bool
    active: bool
    additionalSizes: _list[Size]
    alignment: typing_extensions.Literal[
        "ALIGNMENT_TOP", "ALIGNMENT_RIGHT", "ALIGNMENT_BOTTOM", "ALIGNMENT_LEFT"
    ]
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    assetIdentifier: CreativeAssetId
    audioBitRate: int
    audioSampleRate: int
    backupImageExit: CreativeCustomEvent
    bitRate: int
    childAssetType: typing_extensions.Literal[
        "CHILD_ASSET_TYPE_FLASH",
        "CHILD_ASSET_TYPE_VIDEO",
        "CHILD_ASSET_TYPE_IMAGE",
        "CHILD_ASSET_TYPE_DATA",
    ]
    collapsedSize: Size
    companionCreativeIds: _list[str]
    customStartTimeValue: int
    detectedFeatures: _list[
        typing_extensions.Literal[
            "CSS_FONT_FACE",
            "CSS_BACKGROUND_SIZE",
            "CSS_BORDER_IMAGE",
            "CSS_BORDER_RADIUS",
            "CSS_BOX_SHADOW",
            "CSS_FLEX_BOX",
            "CSS_HSLA",
            "CSS_MULTIPLE_BGS",
            "CSS_OPACITY",
            "CSS_RGBA",
            "CSS_TEXT_SHADOW",
            "CSS_ANIMATIONS",
            "CSS_COLUMNS",
            "CSS_GENERATED_CONTENT",
            "CSS_GRADIENTS",
            "CSS_REFLECTIONS",
            "CSS_TRANSFORMS",
            "CSS_TRANSFORMS3D",
            "CSS_TRANSITIONS",
            "APPLICATION_CACHE",
            "CANVAS",
            "CANVAS_TEXT",
            "DRAG_AND_DROP",
            "HASH_CHANGE",
            "HISTORY",
            "AUDIO",
            "VIDEO",
            "INDEXED_DB",
            "INPUT_ATTR_AUTOCOMPLETE",
            "INPUT_ATTR_AUTOFOCUS",
            "INPUT_ATTR_LIST",
            "INPUT_ATTR_PLACEHOLDER",
            "INPUT_ATTR_MAX",
            "INPUT_ATTR_MIN",
            "INPUT_ATTR_MULTIPLE",
            "INPUT_ATTR_PATTERN",
            "INPUT_ATTR_REQUIRED",
            "INPUT_ATTR_STEP",
            "INPUT_TYPE_SEARCH",
            "INPUT_TYPE_TEL",
            "INPUT_TYPE_URL",
            "INPUT_TYPE_EMAIL",
            "INPUT_TYPE_DATETIME",
            "INPUT_TYPE_DATE",
            "INPUT_TYPE_MONTH",
            "INPUT_TYPE_WEEK",
            "INPUT_TYPE_TIME",
            "INPUT_TYPE_DATETIME_LOCAL",
            "INPUT_TYPE_NUMBER",
            "INPUT_TYPE_RANGE",
            "INPUT_TYPE_COLOR",
            "LOCAL_STORAGE",
            "POST_MESSAGE",
            "SESSION_STORAGE",
            "WEB_SOCKETS",
            "WEB_SQL_DATABASE",
            "WEB_WORKERS",
            "GEO_LOCATION",
            "INLINE_SVG",
            "SMIL",
            "SVG_HREF",
            "SVG_CLIP_PATHS",
            "TOUCH",
            "WEBGL",
            "SVG_FILTERS",
            "SVG_FE_IMAGE",
        ]
    ]
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
    duration: int
    durationType: typing_extensions.Literal[
        "ASSET_DURATION_TYPE_AUTO",
        "ASSET_DURATION_TYPE_NONE",
        "ASSET_DURATION_TYPE_CUSTOM",
    ]
    expandedDimension: Size
    fileSize: str
    flashVersion: int
    frameRate: float
    hideFlashObjects: bool
    hideSelectionBoxes: bool
    horizontallyLocked: bool
    id: str
    idDimensionValue: DimensionValue
    mediaDuration: float
    mimeType: str
    offset: OffsetPosition
    orientation: typing_extensions.Literal["LANDSCAPE", "PORTRAIT", "SQUARE"]
    originalBackup: bool
    politeLoad: bool
    position: OffsetPosition
    positionLeftUnit: typing_extensions.Literal[
        "OFFSET_UNIT_PIXEL", "OFFSET_UNIT_PERCENT", "OFFSET_UNIT_PIXEL_FROM_CENTER"
    ]
    positionTopUnit: typing_extensions.Literal[
        "OFFSET_UNIT_PIXEL", "OFFSET_UNIT_PERCENT", "OFFSET_UNIT_PIXEL_FROM_CENTER"
    ]
    progressiveServingUrl: str
    pushdown: bool
    pushdownDuration: float
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
    size: Size
    sslCompliant: bool
    startTimeType: typing_extensions.Literal[
        "ASSET_START_TIME_TYPE_NONE", "ASSET_START_TIME_TYPE_CUSTOM"
    ]
    streamingServingUrl: str
    transparency: bool
    verticallyLocked: bool
    windowMode: typing_extensions.Literal["OPAQUE", "WINDOW", "TRANSPARENT"]
    zIndex: int
    zipFilename: str
    zipFilesize: str

@typing.type_check_only
class CreativeAssetId(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "IMAGE", "FLASH", "VIDEO", "HTML", "HTML_IMAGE", "AUDIO"
    ]

@typing.type_check_only
class CreativeAssetMetadata(typing_extensions.TypedDict, total=False):
    assetIdentifier: CreativeAssetId
    clickTags: _list[ClickTag]
    counterCustomEvents: _list[CreativeCustomEvent]
    detectedFeatures: _list[
        typing_extensions.Literal[
            "CSS_FONT_FACE",
            "CSS_BACKGROUND_SIZE",
            "CSS_BORDER_IMAGE",
            "CSS_BORDER_RADIUS",
            "CSS_BOX_SHADOW",
            "CSS_FLEX_BOX",
            "CSS_HSLA",
            "CSS_MULTIPLE_BGS",
            "CSS_OPACITY",
            "CSS_RGBA",
            "CSS_TEXT_SHADOW",
            "CSS_ANIMATIONS",
            "CSS_COLUMNS",
            "CSS_GENERATED_CONTENT",
            "CSS_GRADIENTS",
            "CSS_REFLECTIONS",
            "CSS_TRANSFORMS",
            "CSS_TRANSFORMS3D",
            "CSS_TRANSITIONS",
            "APPLICATION_CACHE",
            "CANVAS",
            "CANVAS_TEXT",
            "DRAG_AND_DROP",
            "HASH_CHANGE",
            "HISTORY",
            "AUDIO",
            "VIDEO",
            "INDEXED_DB",
            "INPUT_ATTR_AUTOCOMPLETE",
            "INPUT_ATTR_AUTOFOCUS",
            "INPUT_ATTR_LIST",
            "INPUT_ATTR_PLACEHOLDER",
            "INPUT_ATTR_MAX",
            "INPUT_ATTR_MIN",
            "INPUT_ATTR_MULTIPLE",
            "INPUT_ATTR_PATTERN",
            "INPUT_ATTR_REQUIRED",
            "INPUT_ATTR_STEP",
            "INPUT_TYPE_SEARCH",
            "INPUT_TYPE_TEL",
            "INPUT_TYPE_URL",
            "INPUT_TYPE_EMAIL",
            "INPUT_TYPE_DATETIME",
            "INPUT_TYPE_DATE",
            "INPUT_TYPE_MONTH",
            "INPUT_TYPE_WEEK",
            "INPUT_TYPE_TIME",
            "INPUT_TYPE_DATETIME_LOCAL",
            "INPUT_TYPE_NUMBER",
            "INPUT_TYPE_RANGE",
            "INPUT_TYPE_COLOR",
            "LOCAL_STORAGE",
            "POST_MESSAGE",
            "SESSION_STORAGE",
            "WEB_SOCKETS",
            "WEB_SQL_DATABASE",
            "WEB_WORKERS",
            "GEO_LOCATION",
            "INLINE_SVG",
            "SMIL",
            "SVG_HREF",
            "SVG_CLIP_PATHS",
            "TOUCH",
            "WEBGL",
            "SVG_FILTERS",
            "SVG_FE_IMAGE",
        ]
    ]
    exitCustomEvents: _list[CreativeCustomEvent]
    id: str
    idDimensionValue: DimensionValue
    kind: str
    richMedia: bool
    timerCustomEvents: _list[CreativeCustomEvent]
    warnedValidationRules: _list[
        typing_extensions.Literal[
            "CLICK_TAG_NON_TOP_LEVEL",
            "CLICK_TAG_MISSING",
            "CLICK_TAG_MORE_THAN_ONE",
            "CLICK_TAG_INVALID",
            "ORPHANED_ASSET",
            "PRIMARY_HTML_MISSING",
            "EXTERNAL_FILE_REFERENCED",
            "MRAID_REFERENCED",
            "ADMOB_REFERENCED",
            "FILE_TYPE_INVALID",
            "ZIP_INVALID",
            "LINKED_FILE_NOT_FOUND",
            "MAX_FLASH_VERSION_11",
            "NOT_SSL_COMPLIANT",
            "FILE_DETAIL_EMPTY",
            "ASSET_INVALID",
            "GWD_PROPERTIES_INVALID",
            "ENABLER_UNSUPPORTED_METHOD_DCM",
            "ASSET_FORMAT_UNSUPPORTED_DCM",
            "COMPONENT_UNSUPPORTED_DCM",
            "HTML5_FEATURE_UNSUPPORTED",
            "CLICK_TAG_IN_GWD",
            "CLICK_TAG_HARD_CODED",
            "SVG_INVALID",
            "CLICK_TAG_IN_RICH_MEDIA",
            "MISSING_ENABLER_REFERENCE",
        ]
    ]

@typing.type_check_only
class CreativeAssignment(typing_extensions.TypedDict, total=False):
    active: bool
    applyEventTags: bool
    clickThroughUrl: ClickThroughUrl
    companionCreativeOverrides: _list[CompanionClickThroughOverride]
    creativeGroupAssignments: _list[CreativeGroupAssignment]
    creativeId: str
    creativeIdDimensionValue: DimensionValue
    endTime: str
    richMediaExitOverrides: _list[RichMediaExitOverride]
    sequence: int
    sslCompliant: bool
    startTime: str
    weight: int

@typing.type_check_only
class CreativeClickThroughUrl(typing_extensions.TypedDict, total=False):
    computedClickThroughUrl: str
    customClickThroughUrl: str
    landingPageId: str

@typing.type_check_only
class CreativeCustomEvent(typing_extensions.TypedDict, total=False):
    advertiserCustomEventId: str
    advertiserCustomEventName: str
    advertiserCustomEventType: typing_extensions.Literal[
        "ADVERTISER_EVENT_TIMER", "ADVERTISER_EVENT_EXIT", "ADVERTISER_EVENT_COUNTER"
    ]
    artworkLabel: str
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    exitClickThroughUrl: CreativeClickThroughUrl
    id: str
    popupWindowProperties: PopupWindowProperties
    targetType: typing_extensions.Literal[
        "TARGET_BLANK", "TARGET_TOP", "TARGET_SELF", "TARGET_PARENT", "TARGET_POPUP"
    ]
    videoReportingId: str

@typing.type_check_only
class CreativeField(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    id: str
    kind: str
    name: str
    subaccountId: str

@typing.type_check_only
class CreativeFieldAssignment(typing_extensions.TypedDict, total=False):
    creativeFieldId: str
    creativeFieldValueId: str

@typing.type_check_only
class CreativeFieldValue(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    value: str

@typing.type_check_only
class CreativeFieldValuesListResponse(typing_extensions.TypedDict, total=False):
    creativeFieldValues: _list[CreativeFieldValue]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CreativeFieldsListResponse(typing_extensions.TypedDict, total=False):
    creativeFields: _list[CreativeField]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CreativeGroup(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    groupNumber: int
    id: str
    kind: str
    name: str
    subaccountId: str

@typing.type_check_only
class CreativeGroupAssignment(typing_extensions.TypedDict, total=False):
    creativeGroupId: str
    creativeGroupNumber: typing_extensions.Literal[
        "CREATIVE_GROUP_ONE", "CREATIVE_GROUP_TWO"
    ]

@typing.type_check_only
class CreativeGroupsListResponse(typing_extensions.TypedDict, total=False):
    creativeGroups: _list[CreativeGroup]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CreativeOptimizationConfiguration(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    optimizationActivitys: _list[OptimizationActivity]
    optimizationModel: typing_extensions.Literal[
        "CLICK",
        "POST_CLICK",
        "POST_IMPRESSION",
        "POST_CLICK_AND_IMPRESSION",
        "VIDEO_COMPLETION",
    ]

@typing.type_check_only
class CreativeRotation(typing_extensions.TypedDict, total=False):
    creativeAssignments: _list[CreativeAssignment]
    creativeOptimizationConfigurationId: str
    type: typing_extensions.Literal[
        "CREATIVE_ROTATION_TYPE_SEQUENTIAL", "CREATIVE_ROTATION_TYPE_RANDOM"
    ]
    weightCalculationStrategy: typing_extensions.Literal[
        "WEIGHT_STRATEGY_EQUAL",
        "WEIGHT_STRATEGY_CUSTOM",
        "WEIGHT_STRATEGY_HIGHEST_CTR",
        "WEIGHT_STRATEGY_OPTIMIZED",
    ]

@typing.type_check_only
class CreativesListResponse(typing_extensions.TypedDict, total=False):
    creatives: _list[Creative]
    kind: str
    nextPageToken: str

@typing.type_check_only
class CrossDimensionReachReportCompatibleFields(
    typing_extensions.TypedDict, total=False
):
    breakdown: _list[Dimension]
    dimensionFilters: _list[Dimension]
    kind: str
    metrics: _list[Metric]
    overlapMetrics: _list[Metric]

@typing.type_check_only
class CrossMediaReachReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensionFilters: _list[Dimension]
    dimensions: _list[Dimension]
    kind: str
    metrics: _list[Metric]

@typing.type_check_only
class CustomFloodlightVariable(typing_extensions.TypedDict, total=False):
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
    value: str

@typing.type_check_only
class CustomRichMediaEvents(typing_extensions.TypedDict, total=False):
    filteredEventIds: _list[DimensionValue]
    kind: str

@typing.type_check_only
class CustomRule(typing_extensions.TypedDict, total=False):
    name: str
    priority: int
    ruleBlocks: _list[RuleBlock]

@typing.type_check_only
class CustomValueField(typing_extensions.TypedDict, total=False):
    fieldId: int
    requestKey: str

@typing.type_check_only
class CustomViewabilityMetric(typing_extensions.TypedDict, total=False):
    configuration: CustomViewabilityMetricConfiguration
    id: str
    name: str

@typing.type_check_only
class CustomViewabilityMetricConfiguration(typing_extensions.TypedDict, total=False):
    audible: bool
    timeMillis: int
    timePercent: int
    viewabilityPercent: int

@typing.type_check_only
class DateRange(typing_extensions.TypedDict, total=False):
    endDate: str
    kind: str
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
    startDate: str

@typing.type_check_only
class DayPartTargeting(typing_extensions.TypedDict, total=False):
    daysOfWeek: _list[
        typing_extensions.Literal[
            "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"
        ]
    ]
    hoursOfDay: _list[int]
    userLocalTime: bool

@typing.type_check_only
class DeepLink(typing_extensions.TypedDict, total=False):
    appUrl: str
    fallbackUrl: str
    kind: str
    mobileApp: MobileApp
    remarketingListIds: _list[str]

@typing.type_check_only
class DefaultClickThroughEventTagProperties(typing_extensions.TypedDict, total=False):
    defaultClickThroughEventTagId: str
    overrideInheritedEventTag: bool

@typing.type_check_only
class DeliverySchedule(typing_extensions.TypedDict, total=False):
    frequencyCap: FrequencyCap
    hardCutoff: bool
    impressionRatio: str
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

@typing.type_check_only
class DependentFieldValue(typing_extensions.TypedDict, total=False):
    elementId: str
    fieldId: int

@typing.type_check_only
class DfareportingStudioCreativeAssetsInsertRequest(
    typing_extensions.TypedDict, total=False
):
    studioAccountId: str
    studioAdvertiserId: str
    studioCreativeId: str

@typing.type_check_only
class DfpSettings(typing_extensions.TypedDict, total=False):
    dfpNetworkCode: str
    dfpNetworkName: str
    programmaticPlacementAccepted: bool
    pubPaidPlacementAccepted: bool
    publisherPortalOnly: bool

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    kind: str
    name: str

@typing.type_check_only
class DimensionFilter(typing_extensions.TypedDict, total=False):
    dimensionName: str
    kind: str
    value: str

@typing.type_check_only
class DimensionValue(typing_extensions.TypedDict, total=False):
    dimensionName: str
    etag: str
    id: str
    kind: str
    matchType: typing_extensions.Literal[
        "EXACT", "BEGINS_WITH", "CONTAINS", "WILDCARD_EXPRESSION"
    ]
    value: str

@typing.type_check_only
class DimensionValueList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[DimensionValue]
    kind: str
    nextPageToken: str

@typing.type_check_only
class DimensionValueRequest(typing_extensions.TypedDict, total=False):
    dimensionName: str
    endDate: str
    filters: _list[DimensionFilter]
    kind: str
    startDate: str

@typing.type_check_only
class DirectorySite(typing_extensions.TypedDict, total=False):
    id: str
    idDimensionValue: DimensionValue
    inpageTagFormats: _list[
        typing_extensions.Literal[
            "STANDARD",
            "IFRAME_JAVASCRIPT_INPAGE",
            "INTERNAL_REDIRECT_INPAGE",
            "JAVASCRIPT_INPAGE",
        ]
    ]
    interstitialTagFormats: _list[
        typing_extensions.Literal[
            "IFRAME_JAVASCRIPT_INTERSTITIAL",
            "INTERNAL_REDIRECT_INTERSTITIAL",
            "JAVASCRIPT_INTERSTITIAL",
        ]
    ]
    kind: str
    name: str
    publisherSpecificationId: str
    settings: DirectorySiteSettings
    url: str

@typing.type_check_only
class DirectorySiteSettings(typing_extensions.TypedDict, total=False):
    activeViewOptOut: bool
    dfpSettings: DfpSettings
    instreamVideoPlacementAccepted: bool
    interstitialPlacementAccepted: bool

@typing.type_check_only
class DirectorySitesListResponse(typing_extensions.TypedDict, total=False):
    directorySites: _list[DirectorySite]
    kind: str
    nextPageToken: str

@typing.type_check_only
class DynamicFeed(typing_extensions.TypedDict, total=False):
    contentSource: ContentSource
    createInfo: LastModifiedInfo
    dynamicFeedId: str
    dynamicFeedName: str
    element: Element
    feedIngestionStatus: FeedIngestionStatus
    feedSchedule: FeedSchedule
    hasPublished: bool
    lastModifiedInfo: LastModifiedInfo
    status: typing_extensions.Literal["STATUS_UNKNOWN", "ACTIVE", "INACTIVE", "DELETED"]
    studioAdvertiserId: str

@typing.type_check_only
class DynamicFeedsInsertRequest(typing_extensions.TypedDict, total=False):
    dynamicFeed: DynamicFeed
    dynamicProfileId: str

@typing.type_check_only
class DynamicProfile(typing_extensions.TypedDict, total=False):
    active: DynamicProfileVersion
    archiveStatus: typing_extensions.Literal[
        "ARCHIVE_STATUS_UNKNOWN", "UNARCHIVED", "ARCHIVED"
    ]
    createInfo: LastModifiedInfo
    description: str
    draft: DynamicProfileVersion
    dynamicProfileId: str
    kind: str
    lastModifiedInfo: LastModifiedInfo
    name: str
    status: typing_extensions.Literal["STATUS_UNKNOWN", "ACTIVE", "INACTIVE", "DELETED"]
    studioAdvertiserId: str

@typing.type_check_only
class DynamicProfileFeedSettings(typing_extensions.TypedDict, total=False):
    dynamicFeedId: str
    dynamicRules: DynamicRules
    quantity: int

@typing.type_check_only
class DynamicProfileGenerateCodeResponse(typing_extensions.TypedDict, total=False):
    code: str

@typing.type_check_only
class DynamicProfileVersion(typing_extensions.TypedDict, total=False):
    dynamicProfileFeedSettings: _list[DynamicProfileFeedSettings]
    versionId: str

@typing.type_check_only
class DynamicRules(typing_extensions.TypedDict, total=False):
    autoTargetedFieldIds: _list[int]
    customRules: _list[CustomRule]
    customValueFields: _list[CustomValueField]
    proximityFilter: ProximityFilter
    remarketingValueAttributes: _list[RemarketingValueAttribute]
    rotationType: typing_extensions.Literal[
        "ROTATION_TYPE_UNKNOWN", "RANDOM", "OPTIMIZED", "WEIGHTED"
    ]
    ruleType: typing_extensions.Literal[
        "RULE_SET_TYPE_UNKNOWN", "OPEN", "AUTO", "CUSTOM", "PROXIMITY_TARGETING"
    ]
    weightFieldId: int

@typing.type_check_only
class DynamicTargetingKey(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    objectId: str
    objectType: typing_extensions.Literal[
        "OBJECT_ADVERTISER", "OBJECT_AD", "OBJECT_CREATIVE", "OBJECT_PLACEMENT"
    ]

@typing.type_check_only
class DynamicTargetingKeysListResponse(typing_extensions.TypedDict, total=False):
    dynamicTargetingKeys: _list[DynamicTargetingKey]
    kind: str

@typing.type_check_only
class Element(typing_extensions.TypedDict, total=False):
    activeFieldId: int
    createInfo: LastModifiedInfo
    defaultFieldId: int
    elementName: str
    endTimestampFieldId: int
    externalIdFieldId: int
    feedFields: _list[FeedField]
    isLocalTimestamp: bool
    lastModifiedInfo: LastModifiedInfo
    proximityTargetingFieldId: int
    reportingLabelFieldId: int
    startTimestampFieldId: int

@typing.type_check_only
class EncryptionInfo(typing_extensions.TypedDict, total=False):
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
    encryptionSource: typing_extensions.Literal[
        "ENCRYPTION_SCOPE_UNKNOWN", "AD_SERVING", "DATA_TRANSFER"
    ]
    kind: str

@typing.type_check_only
class EventTag(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    campaignId: str
    campaignIdDimensionValue: DimensionValue
    enabledByDefault: bool
    excludeFromAdxRequests: bool
    id: str
    kind: str
    name: str
    siteFilterType: typing_extensions.Literal["ALLOWLIST", "BLOCKLIST"]
    siteIds: _list[str]
    sslCompliant: bool
    status: typing_extensions.Literal["ENABLED", "DISABLED"]
    subaccountId: str
    type: typing_extensions.Literal[
        "IMPRESSION_IMAGE_EVENT_TAG",
        "IMPRESSION_JAVASCRIPT_EVENT_TAG",
        "CLICK_THROUGH_EVENT_TAG",
    ]
    url: str
    urlEscapeLevels: int

@typing.type_check_only
class EventTagOverride(typing_extensions.TypedDict, total=False):
    enabled: bool
    id: str

@typing.type_check_only
class EventTagsListResponse(typing_extensions.TypedDict, total=False):
    eventTags: _list[EventTag]
    kind: str

@typing.type_check_only
class FeedField(typing_extensions.TypedDict, total=False):
    defaultValue: str
    filterable: bool
    id: int
    name: str
    renderable: bool
    required: bool
    type: typing_extensions.Literal[
        "TYPE_UNKNOWN",
        "STRING",
        "LONG",
        "GPA_SERVED_IMAGE_URL",
        "GPA_SERVED_ASSET_URL",
        "COUNTRY_CODE_ISO",
        "FLOAT",
        "CM360_KEYWORD",
        "CM360_SITE_ID",
        "BOOL",
        "EXIT_URL",
        "DATETIME",
        "CM360_CREATIVE_ID",
        "CM360_PLACEMENT_ID",
        "CM360_AD_ID",
        "CM360_ADVERTISER_ID",
        "CM360_CAMPAIGN_ID",
        "CITY",
        "REGION",
        "POSTAL_CODE",
        "METRO",
        "CUSTOM_VALUE",
        "REMARKETING_VALUE",
        "GEO_CANONICAL",
        "WEIGHT",
        "STRING_LIST",
        "CREATIVE_DIMENSION",
        "USERLIST_ID",
        "ASSET_LIBRARY_DIRECTORY_HANDLE",
        "ASSET_LIBRARY_VIDEO_HANDLE",
        "ASSET_LIBRARY_HANDLE",
        "THIRD_PARTY_SERVED_URL",
        "CM360_DYNAMIC_TARGETING_KEY",
        "DV360_LINE_ITEM_ID",
    ]

@typing.type_check_only
class FeedIngestionStatus(typing_extensions.TypedDict, total=False):
    ingestionErrorRecords: _list[IngestionErrorRecord]
    ingestionStatus: IngestionStatus
    state: typing_extensions.Literal[
        "FEED_PROCESSING_STATE_UNKNOWN",
        "CANCELLED",
        "INGESTING_QUEUED",
        "INGESTING",
        "INGESTED_SUCCESS",
        "INGESTED_FAILURE",
        "REQUEST_TO_PUBLISH",
        "PUBLISHING",
        "PUBLISHED_SUCCESS",
        "PUBLISHED_FAILURE",
    ]

@typing.type_check_only
class FeedSchedule(typing_extensions.TypedDict, total=False):
    repeatValue: str
    scheduleEnabled: bool
    startHour: str
    startMinute: str
    timeZone: str

@typing.type_check_only
class FieldError(typing_extensions.TypedDict, total=False):
    fieldId: int
    fieldName: str
    fieldValues: _list[str]
    ingestionError: typing_extensions.Literal[
        "UNKNOWN_PARSING_ERROR",
        "MISSING_ID",
        "MISSING_REPORTING_LABEL",
        "EMPTY_VALUE",
        "ASSET_DOWNLOAD_ERROR",
        "ID_TOO_LONG",
        "DUPLICATE_ID",
        "PARSING_ERROR",
        "COUNTRY_PARSING_ERROR",
        "LONG_PARSING_ERROR",
        "BOOL_PARSING_ERROR",
        "EXPANDED_URL_PARSING_ERROR",
        "FLOAT_PARSING_ERROR",
        "DATETIME_PARSING_ERROR",
        "INVALID_PREFERENCE_VALUE",
        "GEO_NOT_FOUND_ERROR",
        "GEO_PARSING_ERROR",
        "GEO_PROXIMITY_TARGETING_MULTIPLE_LOCATION_ERROR",
        "POSTAL_CODE_PARSING_ERROR",
        "METRO_CODE_PARSING_ERROR",
        "DATETIME_WITHOUT_TIMEZONE_PARSING_ERROR",
        "WEIGHT_PARSING_ERROR",
        "CREATIVE_DIMENSION_PARSING_ERROR",
        "MULTIVALUE_ID",
        "ENDTIME_BEFORE_STARTTIME",
        "INVALID_ASSET_LIBRARY_HANDLE",
        "INVALID_ASSET_LIBRARY_VIDEO_HANDLE",
        "INVALID_ASSET_LIBRARY_DIRECTORY_HANDLE",
        "DYNAMIC_TARGETING_KEY_NOT_DEFINED_FOR_ADVERTISER",
        "USERLIST_ID_NOT_ACCESSIBLE_FOR_ADVERTISER",
        "ENDTIME_PASSED",
        "ENDTIME_TOO_SOON",
        "TEXT_ASSET_REFERENCE",
        "IMAGE_ASSET_SCS_REFERENCE",
        "AIRPORT_GEO_TARGET",
        "CANONICAL_NAME_QUERY_MISMATCH",
        "NO_DEFAULT_ROW",
        "NO_ACTIVE_DEFAULT_ROW",
        "NO_DEFAULT_ROW_IN_DATE_RANGE",
        "NO_ACTIVE_DEFAULT_ROW_IN_DATE_RANGE",
        "PAYLOAD_LIMIT_EXCEEDED",
        "SSL_NOT_COMPLIANT",
    ]
    isError: bool

@typing.type_check_only
class FieldFilter(typing_extensions.TypedDict, total=False):
    boolValue: bool
    dependentFieldValue: DependentFieldValue
    fieldId: int
    matchType: typing_extensions.Literal[
        "LHS_MATCH_TYPE_UNKNOWN",
        "EQUALS_OR_UNRESTRICTED",
        "EQUALS",
        "UNRESTRICTED",
        "NOT_EQUALS",
    ]
    requestValue: RequestValue
    stringValue: str
    valueType: typing_extensions.Literal[
        "RHS_VALUE_TYPE_UNKNOWN", "STRING", "REQUEST", "BOOL", "DEPENDENT"
    ]

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    dateRange: DateRange
    etag: str
    fileName: str
    format: typing_extensions.Literal["CSV", "EXCEL"]
    id: str
    kind: str
    lastModifiedTime: str
    reportId: str
    status: typing_extensions.Literal[
        "PROCESSING", "REPORT_AVAILABLE", "FAILED", "CANCELLED", "QUEUED"
    ]
    urls: dict[str, typing.Any]

@typing.type_check_only
class FileList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[File]
    kind: str
    nextPageToken: str

@typing.type_check_only
class FloodlightActivitiesGenerateTagResponse(typing_extensions.TypedDict, total=False):
    floodlightActivityTag: str
    globalSiteTagGlobalSnippet: str
    kind: str

@typing.type_check_only
class FloodlightActivitiesListResponse(typing_extensions.TypedDict, total=False):
    floodlightActivities: _list[FloodlightActivity]
    kind: str
    nextPageToken: str

@typing.type_check_only
class FloodlightActivity(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    attributionEnabled: bool
    cacheBustingType: typing_extensions.Literal[
        "JAVASCRIPT", "ACTIVE_SERVER_PAGE", "JSP", "PHP", "COLD_FUSION"
    ]
    conversionCategory: typing_extensions.Literal[
        "CONVERSION_CATEGORY_DEFAULT",
        "CONVERSION_CATEGORY_PURCHASE",
        "CONVERSION_CATEGORY_SIGNUP",
        "CONVERSION_CATEGORY_PAGE_VIEW",
        "CONVERSION_CATEGORY_DOWNLOAD",
        "CONVERSION_CATEGORY_BOOM_EVENT",
        "CONVERSION_CATEGORY_ADD_TO_CART",
        "CONVERSION_CATEGORY_BEGIN_CHECKOUT",
        "CONVERSION_CATEGORY_SUBSCRIBE_PAID",
        "CONVERSION_CATEGORY_SUBSCRIBE_FREE",
        "CONVERSION_CATEGORY_PHONE_CALL_LEAD",
        "CONVERSION_CATEGORY_IMPORTED_LEAD",
        "CONVERSION_CATEGORY_SUBMIT_LEAD_FORM",
        "CONVERSION_CATEGORY_BOOK_APPOINTMENT",
        "CONVERSION_CATEGORY_REQUEST_QUOTE",
        "CONVERSION_CATEGORY_GET_DIRECTIONS",
        "CONVERSION_CATEGORY_OUTBOUND_CLICK",
        "CONVERSION_CATEGORY_CONTACT",
        "CONVERSION_CATEGORY_VIEW_KEY_PAGE",
        "CONVERSION_CATEGORY_ENGAGEMENT",
        "CONVERSION_CATEGORY_STORE_VISIT",
        "CONVERSION_CATEGORY_STORE_SALE",
        "CONVERSION_CATEGORY_QUALIFIED_LEAD",
        "CONVERSION_CATEGORY_CONVERTED_LEAD",
        "CONVERSION_CATEGORY_IN_APP_AD_REVENUE",
        "CONVERSION_CATEGORY_MESSAGE_LEAD",
    ]
    countingMethod: typing_extensions.Literal[
        "STANDARD_COUNTING",
        "UNIQUE_COUNTING",
        "SESSION_COUNTING",
        "TRANSACTIONS_COUNTING",
        "ITEMS_SOLD_COUNTING",
    ]
    defaultTags: _list[FloodlightActivityDynamicTag]
    expectedUrl: str
    floodlightActivityGroupId: str
    floodlightActivityGroupName: str
    floodlightActivityGroupTagString: str
    floodlightActivityGroupType: typing_extensions.Literal["COUNTER", "SALE"]
    floodlightConfigurationId: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    floodlightTagType: typing_extensions.Literal["IFRAME", "IMAGE", "GLOBAL_SITE_TAG"]
    id: str
    idDimensionValue: DimensionValue
    kind: str
    name: str
    notes: str
    publisherTags: _list[FloodlightActivityPublisherDynamicTag]
    secure: bool
    sslCompliant: bool
    sslRequired: bool
    status: typing_extensions.Literal[
        "ACTIVE", "ARCHIVED_AND_DISABLED", "ARCHIVED", "DISABLED_POLICY"
    ]
    subaccountId: str
    tagFormat: typing_extensions.Literal["HTML", "XHTML"]
    tagString: str
    userDefinedVariableTypes: _list[
        typing_extensions.Literal[
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
    ]

@typing.type_check_only
class FloodlightActivityDynamicTag(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    tag: str

@typing.type_check_only
class FloodlightActivityGroup(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    floodlightConfigurationId: str
    floodlightConfigurationIdDimensionValue: DimensionValue
    id: str
    idDimensionValue: DimensionValue
    kind: str
    name: str
    subaccountId: str
    tagString: str
    type: typing_extensions.Literal["COUNTER", "SALE"]

@typing.type_check_only
class FloodlightActivityGroupsListResponse(typing_extensions.TypedDict, total=False):
    floodlightActivityGroups: _list[FloodlightActivityGroup]
    kind: str
    nextPageToken: str

@typing.type_check_only
class FloodlightActivityPublisherDynamicTag(typing_extensions.TypedDict, total=False):
    clickThrough: bool
    directorySiteId: str
    dynamicTag: FloodlightActivityDynamicTag
    siteId: str
    siteIdDimensionValue: DimensionValue
    viewThrough: bool

@typing.type_check_only
class FloodlightConfiguration(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    analyticsDataSharingEnabled: bool
    customViewabilityMetric: CustomViewabilityMetric
    exposureToConversionEnabled: bool
    firstDayOfWeek: typing_extensions.Literal["SUNDAY", "MONDAY"]
    id: str
    idDimensionValue: DimensionValue
    inAppAttributionTrackingEnabled: bool
    kind: str
    lookbackConfiguration: LookbackConfiguration
    naturalSearchConversionAttributionOption: typing_extensions.Literal[
        "EXCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
        "INCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION",
        "INCLUDE_NATURAL_SEARCH_TIERED_CONVERSION_ATTRIBUTION",
    ]
    omnitureSettings: OmnitureSettings
    subaccountId: str
    tagSettings: TagSettings
    thirdPartyAuthenticationTokens: _list[ThirdPartyAuthenticationToken]
    userDefinedVariableConfigurations: _list[UserDefinedVariableConfiguration]

@typing.type_check_only
class FloodlightConfigurationsListResponse(typing_extensions.TypedDict, total=False):
    floodlightConfigurations: _list[FloodlightConfiguration]
    kind: str

@typing.type_check_only
class FloodlightReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensionFilters: _list[Dimension]
    dimensions: _list[Dimension]
    kind: str
    metrics: _list[Metric]

@typing.type_check_only
class FrequencyCap(typing_extensions.TypedDict, total=False):
    duration: str
    impressions: str

@typing.type_check_only
class FsCommand(typing_extensions.TypedDict, total=False):
    left: int
    positionOption: typing_extensions.Literal[
        "CENTERED", "DISTANCE_FROM_TOP_LEFT_CORNER"
    ]
    top: int
    windowHeight: int
    windowWidth: int

@typing.type_check_only
class GeoTargeting(typing_extensions.TypedDict, total=False):
    cities: _list[City]
    countries: _list[Country]
    excludeCountries: bool
    metros: _list[Metro]
    postalCodes: _list[PostalCode]
    regions: _list[Region]

@typing.type_check_only
class IngestionErrorRecord(typing_extensions.TypedDict, total=False):
    errors: _list[FieldError]
    recordId: str

@typing.type_check_only
class IngestionStatus(typing_extensions.TypedDict, total=False):
    numActiveRows: str
    numRowsProcessed: str
    numRowsTotal: str
    numRowsWithErrors: str
    numWarningsTotal: str

@typing.type_check_only
class Invoice(typing_extensions.TypedDict, total=False):
    campaign_summaries: _list[CampaignSummary]
    correctedInvoiceId: str
    currencyCode: str
    dueDate: str
    id: str
    invoiceType: typing_extensions.Literal[
        "INVOICE_TYPE_UNSPECIFIED", "INVOICE_TYPE_CREDIT", "INVOICE_TYPE_INVOICE"
    ]
    issueDate: str
    kind: str
    paymentsAccountId: str
    paymentsProfileId: str
    pdfUrl: str
    purchaseOrderNumber: str
    replacedInvoiceIds: _list[str]
    serviceEndDate: str
    serviceStartDate: str
    subtotalAmountMicros: str
    totalAmountMicros: str
    totalTaxAmountMicros: str

@typing.type_check_only
class KeyValueTargetingExpression(typing_extensions.TypedDict, total=False):
    expression: str

@typing.type_check_only
class LandingPage(typing_extensions.TypedDict, total=False):
    advertiserId: str
    archived: bool
    deepLinks: _list[DeepLink]
    id: str
    kind: str
    name: str
    url: str

@typing.type_check_only
class Language(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    languageCode: str
    name: str

@typing.type_check_only
class LanguageTargeting(typing_extensions.TypedDict, total=False):
    languages: _list[Language]

@typing.type_check_only
class LanguagesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    languages: _list[Language]

@typing.type_check_only
class LastModifiedInfo(typing_extensions.TypedDict, total=False):
    time: str

@typing.type_check_only
class ListPopulationClause(typing_extensions.TypedDict, total=False):
    terms: _list[ListPopulationTerm]

@typing.type_check_only
class ListPopulationRule(typing_extensions.TypedDict, total=False):
    floodlightActivityId: str
    floodlightActivityName: str
    listPopulationClauses: _list[ListPopulationClause]

@typing.type_check_only
class ListPopulationTerm(typing_extensions.TypedDict, total=False):
    contains: bool
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
    remarketingListId: str
    type: typing_extensions.Literal[
        "CUSTOM_VARIABLE_TERM", "LIST_MEMBERSHIP_TERM", "REFERRER_TERM"
    ]
    value: str
    variableFriendlyName: str
    variableName: str

@typing.type_check_only
class ListTargetingExpression(typing_extensions.TypedDict, total=False):
    expression: str

@typing.type_check_only
class LookbackConfiguration(typing_extensions.TypedDict, total=False):
    clickDuration: int
    postImpressionActivitiesDuration: int

@typing.type_check_only
class MeasurementPartnerAdvertiserLink(typing_extensions.TypedDict, total=False):
    linkStatus: typing_extensions.Literal[
        "MEASUREMENT_PARTNER_UNLINKED",
        "MEASUREMENT_PARTNER_LINKED",
        "MEASUREMENT_PARTNER_LINK_PENDING",
        "MEASUREMENT_PARTNER_LINK_FAILURE",
        "MEASUREMENT_PARTNER_LINK_OPT_OUT",
        "MEASUREMENT_PARTNER_LINK_OPT_OUT_PENDING",
        "MEASUREMENT_PARTNER_LINK_WRAPPING_PENDING",
        "MEASUREMENT_PARTNER_MODE_CHANGE_PENDING",
        "MEASUREMENT_PARTNER_UNLINK_PENDING",
    ]
    measurementPartner: typing_extensions.Literal[
        "NONE", "INTEGRAL_AD_SCIENCE", "DOUBLE_VERIFY"
    ]
    partnerAdvertiserId: str

@typing.type_check_only
class MeasurementPartnerCampaignLink(typing_extensions.TypedDict, total=False):
    linkStatus: typing_extensions.Literal[
        "MEASUREMENT_PARTNER_UNLINKED",
        "MEASUREMENT_PARTNER_LINKED",
        "MEASUREMENT_PARTNER_LINK_PENDING",
        "MEASUREMENT_PARTNER_LINK_FAILURE",
        "MEASUREMENT_PARTNER_LINK_OPT_OUT",
        "MEASUREMENT_PARTNER_LINK_OPT_OUT_PENDING",
        "MEASUREMENT_PARTNER_LINK_WRAPPING_PENDING",
        "MEASUREMENT_PARTNER_MODE_CHANGE_PENDING",
        "MEASUREMENT_PARTNER_UNLINK_PENDING",
    ]
    measurementPartner: typing_extensions.Literal[
        "NONE", "INTEGRAL_AD_SCIENCE", "DOUBLE_VERIFY"
    ]
    partnerCampaignId: str

@typing.type_check_only
class MeasurementPartnerWrappingData(typing_extensions.TypedDict, total=False):
    linkStatus: typing_extensions.Literal[
        "MEASUREMENT_PARTNER_UNLINKED",
        "MEASUREMENT_PARTNER_LINKED",
        "MEASUREMENT_PARTNER_LINK_PENDING",
        "MEASUREMENT_PARTNER_LINK_FAILURE",
        "MEASUREMENT_PARTNER_LINK_OPT_OUT",
        "MEASUREMENT_PARTNER_LINK_OPT_OUT_PENDING",
        "MEASUREMENT_PARTNER_LINK_WRAPPING_PENDING",
        "MEASUREMENT_PARTNER_MODE_CHANGE_PENDING",
        "MEASUREMENT_PARTNER_UNLINK_PENDING",
    ]
    measurementPartner: typing_extensions.Literal[
        "NONE", "INTEGRAL_AD_SCIENCE", "DOUBLE_VERIFY"
    ]
    tagWrappingMode: typing_extensions.Literal[
        "NONE",
        "BLOCKING",
        "MONITORING",
        "MONITORING_READ_ONLY",
        "VIDEO_PIXEL_MONITORING",
        "TRACKING",
        "VPAID_MONITORING",
        "VPAID_BLOCKING",
        "NON_VPAID_MONITORING",
        "VPAID_ONLY_MONITORING",
        "VPAID_ONLY_BLOCKING",
        "VPAID_ONLY_FILTERING",
        "VPAID_FILTERING",
        "NON_VPAID_FILTERING",
        "BLOCKING_FILTERING_VPAID",
        "BLOCKING_FILTERING_VPAID_ONLY",
    ]
    wrappedTag: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    kind: str
    name: str

@typing.type_check_only
class Metro(typing_extensions.TypedDict, total=False):
    countryCode: str
    countryDartId: str
    dartId: str
    dmaId: str
    kind: str
    metroCode: str
    name: str

@typing.type_check_only
class MetrosListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    metros: _list[Metro]

@typing.type_check_only
class MobileApp(typing_extensions.TypedDict, total=False):
    directory: typing_extensions.Literal[
        "UNKNOWN",
        "APPLE_APP_STORE",
        "GOOGLE_PLAY_STORE",
        "ROKU_APP_STORE",
        "AMAZON_FIRETV_APP_STORE",
        "PLAYSTATION_APP_STORE",
        "APPLE_TV_APP_STORE",
        "XBOX_APP_STORE",
        "SAMSUNG_TV_APP_STORE",
        "ANDROID_TV_APP_STORE",
        "GENERIC_CTV_APP_STORE",
    ]
    id: str
    kind: str
    publisherName: str
    title: str

@typing.type_check_only
class MobileAppsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    mobileApps: _list[MobileApp]
    nextPageToken: str

@typing.type_check_only
class MobileCarrier(typing_extensions.TypedDict, total=False):
    countryCode: str
    countryDartId: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class MobileCarriersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    mobileCarriers: _list[MobileCarrier]

@typing.type_check_only
class ObaIcon(typing_extensions.TypedDict, total=False):
    iconClickThroughUrl: str
    iconClickTrackingUrl: str
    iconViewTrackingUrl: str
    program: str
    resourceUrl: str
    size: Size
    xPosition: str
    yPosition: str

@typing.type_check_only
class ObjectFilter(typing_extensions.TypedDict, total=False):
    kind: str
    objectIds: _list[str]
    status: typing_extensions.Literal["NONE", "ASSIGNED", "ALL"]

@typing.type_check_only
class OfflineUserAddressInfo(typing_extensions.TypedDict, total=False):
    city: str
    countryCode: str
    hashedFirstName: str
    hashedLastName: str
    hashedStreetAddress: str
    postalCode: str
    state: str

@typing.type_check_only
class OffsetPosition(typing_extensions.TypedDict, total=False):
    left: int
    top: int

@typing.type_check_only
class OmnitureSettings(typing_extensions.TypedDict, total=False):
    omnitureCostDataEnabled: bool
    omnitureIntegrationEnabled: bool

@typing.type_check_only
class OperatingSystem(typing_extensions.TypedDict, total=False):
    dartId: str
    desktop: bool
    kind: str
    mobile: bool
    name: str

@typing.type_check_only
class OperatingSystemVersion(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    majorVersion: str
    minorVersion: str
    name: str
    operatingSystem: OperatingSystem

@typing.type_check_only
class OperatingSystemVersionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    operatingSystemVersions: _list[OperatingSystemVersion]

@typing.type_check_only
class OperatingSystemsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    operatingSystems: _list[OperatingSystem]

@typing.type_check_only
class OptimizationActivity(typing_extensions.TypedDict, total=False):
    floodlightActivityId: str
    floodlightActivityIdDimensionValue: DimensionValue
    weight: int

@typing.type_check_only
class PathToConversionReportCompatibleFields(typing_extensions.TypedDict, total=False):
    conversionDimensions: _list[Dimension]
    customFloodlightVariables: _list[Dimension]
    kind: str
    metrics: _list[Metric]
    perInteractionDimensions: _list[Dimension]

@typing.type_check_only
class Placement(typing_extensions.TypedDict, total=False):
    accountId: str
    activeStatus: typing_extensions.Literal[
        "PLACEMENT_STATUS_UNKNOWN",
        "PLACEMENT_STATUS_ACTIVE",
        "PLACEMENT_STATUS_INACTIVE",
        "PLACEMENT_STATUS_ARCHIVED",
        "PLACEMENT_STATUS_PERMANENTLY_ARCHIVED",
    ]
    adBlockingOptOut: bool
    adServingPlatformId: str
    additionalSizes: _list[Size]
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    allowOnYoutube: bool
    campaignId: str
    campaignIdDimensionValue: DimensionValue
    comment: str
    compatibility: typing_extensions.Literal[
        "DISPLAY",
        "DISPLAY_INTERSTITIAL",
        "APP",
        "APP_INTERSTITIAL",
        "IN_STREAM_VIDEO",
        "IN_STREAM_AUDIO",
    ]
    contentCategoryId: str
    conversionDomainOverride: PlacementConversionDomainOverride
    createInfo: LastModifiedInfo
    directorySiteId: str
    directorySiteIdDimensionValue: DimensionValue
    externalId: str
    id: str
    idDimensionValue: DimensionValue
    keyName: str
    kind: str
    lastModifiedInfo: LastModifiedInfo
    lookbackConfiguration: LookbackConfiguration
    name: str
    partnerWrappingData: MeasurementPartnerWrappingData
    paymentApproved: bool
    paymentSource: typing_extensions.Literal[
        "PLACEMENT_AGENCY_PAID", "PLACEMENT_PUBLISHER_PAID"
    ]
    placementGroupId: str
    placementGroupIdDimensionValue: DimensionValue
    placementStrategyId: str
    pricingSchedule: PricingSchedule
    primary: bool
    publisherUpdateInfo: LastModifiedInfo
    siteId: str
    siteIdDimensionValue: DimensionValue
    siteServed: bool
    size: Size
    sslRequired: bool
    status: typing_extensions.Literal[
        "PENDING_REVIEW",
        "PAYMENT_ACCEPTED",
        "PAYMENT_REJECTED",
        "ACKNOWLEDGE_REJECTION",
        "ACKNOWLEDGE_ACCEPTANCE",
        "DRAFT",
    ]
    subaccountId: str
    tagFormats: _list[
        typing_extensions.Literal[
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
            "PLACEMENT_TAG_TRACKING_THIRD_PARTY_MEASUREMENT",
        ]
    ]
    tagSetting: TagSetting
    videoActiveViewOptOut: bool
    videoSettings: VideoSettings
    vpaidAdapterChoice: typing_extensions.Literal["DEFAULT", "FLASH", "HTML5", "BOTH"]
    wrappingOptOut: bool
    youtubeSettings: YoutubeSettings

@typing.type_check_only
class PlacementAssignment(typing_extensions.TypedDict, total=False):
    active: bool
    placementId: str
    placementIdDimensionValue: DimensionValue
    sslRequired: bool

@typing.type_check_only
class PlacementConversionDomainOverride(typing_extensions.TypedDict, total=False):
    conversionDomains: _list[PlacementSingleConversionDomain]

@typing.type_check_only
class PlacementGroup(typing_extensions.TypedDict, total=False):
    accountId: str
    activeStatus: typing_extensions.Literal[
        "PLACEMENT_STATUS_UNKNOWN",
        "PLACEMENT_STATUS_ACTIVE",
        "PLACEMENT_STATUS_INACTIVE",
        "PLACEMENT_STATUS_ARCHIVED",
        "PLACEMENT_STATUS_PERMANENTLY_ARCHIVED",
    ]
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    campaignId: str
    campaignIdDimensionValue: DimensionValue
    childPlacementIds: _list[str]
    comment: str
    contentCategoryId: str
    createInfo: LastModifiedInfo
    directorySiteId: str
    directorySiteIdDimensionValue: DimensionValue
    externalId: str
    id: str
    idDimensionValue: DimensionValue
    kind: str
    lastModifiedInfo: LastModifiedInfo
    name: str
    placementGroupType: typing_extensions.Literal[
        "PLACEMENT_PACKAGE", "PLACEMENT_ROADBLOCK"
    ]
    placementStrategyId: str
    pricingSchedule: PricingSchedule
    primaryPlacementId: str
    primaryPlacementIdDimensionValue: DimensionValue
    siteId: str
    siteIdDimensionValue: DimensionValue
    subaccountId: str

@typing.type_check_only
class PlacementGroupsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    placementGroups: _list[PlacementGroup]

@typing.type_check_only
class PlacementSingleConversionDomain(typing_extensions.TypedDict, total=False):
    conversionDomainId: str
    conversionDomainValue: str

@typing.type_check_only
class PlacementStrategiesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    placementStrategies: _list[PlacementStrategy]

@typing.type_check_only
class PlacementStrategy(typing_extensions.TypedDict, total=False):
    accountId: str
    id: str
    kind: str
    name: str

@typing.type_check_only
class PlacementTag(typing_extensions.TypedDict, total=False):
    placementId: str
    tagDatas: _list[TagData]

@typing.type_check_only
class PlacementsGenerateTagsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    placementTags: _list[PlacementTag]

@typing.type_check_only
class PlacementsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    placements: _list[Placement]

@typing.type_check_only
class PlatformType(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class PlatformTypesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    platformTypes: _list[PlatformType]

@typing.type_check_only
class PopupWindowProperties(typing_extensions.TypedDict, total=False):
    dimension: Size
    offset: OffsetPosition
    positionType: typing_extensions.Literal["CENTER", "COORDINATES"]
    showAddressBar: bool
    showMenuBar: bool
    showScrollBar: bool
    showStatusBar: bool
    showToolBar: bool
    title: str

@typing.type_check_only
class PostalCode(typing_extensions.TypedDict, total=False):
    code: str
    countryCode: str
    countryDartId: str
    id: str
    kind: str

@typing.type_check_only
class PostalCodesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    postalCodes: _list[PostalCode]

@typing.type_check_only
class PricingSchedule(typing_extensions.TypedDict, total=False):
    capCostOption: typing_extensions.Literal[
        "CAP_COST_NONE", "CAP_COST_MONTHLY", "CAP_COST_CUMULATIVE"
    ]
    endDate: str
    flighted: bool
    floodlightActivityId: str
    pricingPeriods: _list[PricingSchedulePricingPeriod]
    pricingType: typing_extensions.Literal[
        "PRICING_TYPE_CPM",
        "PRICING_TYPE_CPC",
        "PRICING_TYPE_CPA",
        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
        "PRICING_TYPE_FLAT_RATE_CLICKS",
        "PRICING_TYPE_CPM_ACTIVEVIEW",
    ]
    startDate: str
    testingStartDate: str

@typing.type_check_only
class PricingSchedulePricingPeriod(typing_extensions.TypedDict, total=False):
    endDate: str
    pricingComment: str
    rateOrCostNanos: str
    startDate: str
    units: str

@typing.type_check_only
class ProximityFilter(typing_extensions.TypedDict, total=False):
    fieldId: int
    radiusBucketType: typing_extensions.Literal[
        "RADIUS_BUCKET_TYPE_UNKNOWN",
        "SMALL",
        "MEDIUM",
        "LARGE",
        "MULTI_REGIONAL",
        "NATIONAL",
    ]
    radiusUnitType: typing_extensions.Literal[
        "RADIUS_UNIT_TYPE_UNKNOWN", "KILOMETERS", "MILES"
    ]
    radiusValue: int

@typing.type_check_only
class ReachReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensionFilters: _list[Dimension]
    dimensions: _list[Dimension]
    kind: str
    metrics: _list[Metric]
    pivotedActivityMetrics: _list[Metric]
    reachByFrequencyMetrics: _list[Metric]

@typing.type_check_only
class Recipient(typing_extensions.TypedDict, total=False):
    deliveryType: typing_extensions.Literal["LINK", "ATTACHMENT"]
    email: str
    kind: str

@typing.type_check_only
class Region(typing_extensions.TypedDict, total=False):
    countryCode: str
    countryDartId: str
    dartId: str
    kind: str
    name: str
    regionCode: str

@typing.type_check_only
class RegionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    regions: _list[Region]

@typing.type_check_only
class RemarketingList(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    description: str
    id: str
    kind: str
    lifeSpan: str
    listPopulationRule: ListPopulationRule
    listSize: str
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
    name: str
    subaccountId: str

@typing.type_check_only
class RemarketingListShare(typing_extensions.TypedDict, total=False):
    kind: str
    remarketingListId: str
    sharedAccountIds: _list[str]
    sharedAdvertiserIds: _list[str]

@typing.type_check_only
class RemarketingListsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    remarketingLists: _list[RemarketingList]

@typing.type_check_only
class RemarketingValueAttribute(typing_extensions.TypedDict, total=False):
    fieldId: int
    userAttributeIds: _list[str]

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    accountId: str
    criteria: dict[str, typing.Any]
    crossMediaReachCriteria: dict[str, typing.Any]
    delivery: dict[str, typing.Any]
    etag: str
    fileName: str
    floodlightCriteria: dict[str, typing.Any]
    format: typing_extensions.Literal["CSV", "EXCEL"]
    id: str
    kind: str
    lastModifiedTime: str
    name: str
    ownerProfileId: str
    pathToConversionCriteria: dict[str, typing.Any]
    reachCriteria: dict[str, typing.Any]
    schedule: dict[str, typing.Any]
    subAccountId: str
    type: typing_extensions.Literal[
        "STANDARD", "REACH", "PATH_TO_CONVERSION", "FLOODLIGHT", "CROSS_MEDIA_REACH"
    ]

@typing.type_check_only
class ReportCompatibleFields(typing_extensions.TypedDict, total=False):
    dimensionFilters: _list[Dimension]
    dimensions: _list[Dimension]
    kind: str
    metrics: _list[Metric]
    pivotedActivityMetrics: _list[Metric]

@typing.type_check_only
class ReportList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Report]
    kind: str
    nextPageToken: str

@typing.type_check_only
class ReportsConfiguration(typing_extensions.TypedDict, total=False):
    exposureToConversionEnabled: bool
    lookbackConfiguration: LookbackConfiguration
    reportGenerationTimeZoneId: str

@typing.type_check_only
class RequestValue(typing_extensions.TypedDict, total=False):
    excludeFromUserAttributeIds: _list[str]
    key: str
    userAttributeIds: _list[str]

@typing.type_check_only
class RichMediaExitOverride(typing_extensions.TypedDict, total=False):
    clickThroughUrl: ClickThroughUrl
    enabled: bool
    exitId: str

@typing.type_check_only
class RuleBlock(typing_extensions.TypedDict, total=False):
    fieldFilter: _list[FieldFilter]

@typing.type_check_only
class Site(typing_extensions.TypedDict, total=False):
    accountId: str
    adServingPlatformId: str
    approved: bool
    directorySiteId: str
    directorySiteIdDimensionValue: DimensionValue
    id: str
    idDimensionValue: DimensionValue
    keyName: str
    kind: str
    name: str
    siteContacts: _list[SiteContact]
    siteSettings: SiteSettings
    subaccountId: str
    videoSettings: SiteVideoSettings

@typing.type_check_only
class SiteCompanionSetting(typing_extensions.TypedDict, total=False):
    companionsDisabled: bool
    enabledSizes: _list[Size]
    imageOnly: bool
    kind: str

@typing.type_check_only
class SiteContact(typing_extensions.TypedDict, total=False):
    address: str
    contactType: typing_extensions.Literal["SALES_PERSON", "TRAFFICKER"]
    email: str
    firstName: str
    id: str
    lastName: str
    phone: str
    title: str

@typing.type_check_only
class SiteSettings(typing_extensions.TypedDict, total=False):
    activeViewOptOut: bool
    adBlockingOptOut: bool
    disableNewCookie: bool
    tagSetting: TagSetting
    videoActiveViewOptOutTemplate: bool
    vpaidAdapterChoiceTemplate: typing_extensions.Literal[
        "DEFAULT", "FLASH", "HTML5", "BOTH"
    ]

@typing.type_check_only
class SiteSkippableSetting(typing_extensions.TypedDict, total=False):
    kind: str
    progressOffset: VideoOffset
    skipOffset: VideoOffset
    skippable: bool

@typing.type_check_only
class SiteTranscodeSetting(typing_extensions.TypedDict, total=False):
    enabledVideoFormats: _list[int]
    kind: str

@typing.type_check_only
class SiteVideoSettings(typing_extensions.TypedDict, total=False):
    companionSettings: SiteCompanionSetting
    kind: str
    obaEnabled: bool
    obaSettings: ObaIcon
    orientation: typing_extensions.Literal["ANY", "LANDSCAPE", "PORTRAIT"]
    publisherSpecificationId: str
    skippableSettings: SiteSkippableSetting
    transcodeSettings: SiteTranscodeSetting

@typing.type_check_only
class SitesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class Size(typing_extensions.TypedDict, total=False):
    height: int
    iab: bool
    id: str
    kind: str
    width: int

@typing.type_check_only
class SizesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    sizes: _list[Size]

@typing.type_check_only
class SkippableSetting(typing_extensions.TypedDict, total=False):
    kind: str
    progressOffset: VideoOffset
    skipOffset: VideoOffset
    skippable: bool

@typing.type_check_only
class SortedDimension(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]

@typing.type_check_only
class StudioCreative(typing_extensions.TypedDict, total=False):
    assetIds: _list[str]
    backupImageAssetId: str
    createdInfo: LastModifiedInfo
    dimension: StudioCreativeDimension
    dynamicProfileId: str
    format: typing_extensions.Literal[
        "UNKNOWN", "BANNER", "EXPANDING", "INTERSTITIAL", "VPAID_LINEAR_VIDEO"
    ]
    id: str
    lastModifiedInfo: LastModifiedInfo
    name: str
    status: typing_extensions.Literal[
        "UNKNOWN_STATUS",
        "IN_DEVELOPMENT",
        "PUBLISHED",
        "QA_REJECTED",
        "QA_APPROVED",
        "TRAFFICKED",
    ]
    studioAccountId: str
    studioAdvertiserId: str
    studioCampaignId: str

@typing.type_check_only
class StudioCreativeAsset(typing_extensions.TypedDict, total=False):
    createInfo: LastModifiedInfo
    filename: str
    filesize: str
    id: str
    lastModifiedInfo: LastModifiedInfo
    studioAccountId: str
    studioAdvertiserId: str
    studioCreativeId: str
    type: typing_extensions.Literal["UNKNOWN_TYPE", "HTML", "VIDEO", "IMAGE", "FONT"]
    videoProcessingData: VideoProcessingData

@typing.type_check_only
class StudioCreativeAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[StudioCreativeAsset]

@typing.type_check_only
class StudioCreativeDimension(typing_extensions.TypedDict, total=False):
    height: int
    width: int

@typing.type_check_only
class Subaccount(typing_extensions.TypedDict, total=False):
    accountId: str
    availablePermissionIds: _list[str]
    id: str
    kind: str
    name: str

@typing.type_check_only
class SubaccountsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    subaccounts: _list[Subaccount]

@typing.type_check_only
class TagData(typing_extensions.TypedDict, total=False):
    adId: str
    clickTag: str
    creativeId: str
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
        "PLACEMENT_TAG_TRACKING_THIRD_PARTY_MEASUREMENT",
    ]
    impressionTag: str

@typing.type_check_only
class TagSetting(typing_extensions.TypedDict, total=False):
    additionalKeyValues: str
    includeClickThroughUrls: bool
    includeClickTracking: bool
    includeUnescapedlpurlMacro: bool
    keywordOption: typing_extensions.Literal[
        "PLACEHOLDER_WITH_LIST_OF_KEYWORDS",
        "IGNORE",
        "GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD",
    ]

@typing.type_check_only
class TagSettings(typing_extensions.TypedDict, total=False):
    dynamicTagEnabled: bool
    imageTagEnabled: bool

@typing.type_check_only
class TargetWindow(typing_extensions.TypedDict, total=False):
    customHtml: str
    targetWindowOption: typing_extensions.Literal[
        "NEW_WINDOW", "CURRENT_WINDOW", "CUSTOM"
    ]

@typing.type_check_only
class TargetableRemarketingList(typing_extensions.TypedDict, total=False):
    accountId: str
    active: bool
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    description: str
    id: str
    kind: str
    lifeSpan: str
    listSize: str
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
    name: str
    subaccountId: str

@typing.type_check_only
class TargetableRemarketingListsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    targetableRemarketingLists: _list[TargetableRemarketingList]

@typing.type_check_only
class TargetingTemplate(typing_extensions.TypedDict, total=False):
    accountId: str
    advertiserId: str
    advertiserIdDimensionValue: DimensionValue
    contextualKeywordTargeting: ContextualKeywordTargeting
    dayPartTargeting: DayPartTargeting
    geoTargeting: GeoTargeting
    id: str
    keyValueTargetingExpression: KeyValueTargetingExpression
    kind: str
    languageTargeting: LanguageTargeting
    listTargetingExpression: ListTargetingExpression
    name: str
    subaccountId: str
    technologyTargeting: TechnologyTargeting

@typing.type_check_only
class TargetingTemplatesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    targetingTemplates: _list[TargetingTemplate]

@typing.type_check_only
class TechnologyTargeting(typing_extensions.TypedDict, total=False):
    browsers: _list[Browser]
    connectionTypes: _list[ConnectionType]
    mobileCarriers: _list[MobileCarrier]
    operatingSystemVersions: _list[OperatingSystemVersion]
    operatingSystems: _list[OperatingSystem]
    platformTypes: _list[PlatformType]

@typing.type_check_only
class ThirdPartyAuthenticationToken(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class ThirdPartyTrackingUrl(typing_extensions.TypedDict, total=False):
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
    url: str

@typing.type_check_only
class TranscodeSetting(typing_extensions.TypedDict, total=False):
    enabledVideoFormats: _list[int]
    kind: str

@typing.type_check_only
class TvCampaignDetail(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    timepoints: _list[TvCampaignTimepoint]

@typing.type_check_only
class TvCampaignSummariesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    tvCampaignSummaries: _list[TvCampaignSummary]

@typing.type_check_only
class TvCampaignSummary(typing_extensions.TypedDict, total=False):
    endDate: str
    grp: str
    id: str
    impressions: str
    kind: str
    name: str
    spend: float
    startDate: str
    type: typing_extensions.Literal[
        "CAMPAIGN_COMPONENT_TYPE_UNSPECIFIED", "COMPANY", "BRAND", "PRODUCT", "CAMPAIGN"
    ]

@typing.type_check_only
class TvCampaignTimepoint(typing_extensions.TypedDict, total=False):
    dateWindow: typing_extensions.Literal[
        "WEEKS_UNSPECIFIED", "WEEKS_ONE", "WEEKS_FOUR", "WEEKS_EIGHT", "WEEKS_TWELVE"
    ]
    spend: float
    startDate: str

@typing.type_check_only
class UniversalAdId(typing_extensions.TypedDict, total=False):
    registry: typing_extensions.Literal[
        "OTHER", "AD_ID_OFFICIAL", "CLEARCAST", "DCM", "ARPP", "CUSV"
    ]
    value: str

@typing.type_check_only
class UserDefinedVariableConfiguration(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal["STRING", "NUMBER"]
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

@typing.type_check_only
class UserIdentifier(typing_extensions.TypedDict, total=False):
    addressInfo: OfflineUserAddressInfo
    hashedEmail: str
    hashedPhoneNumber: str

@typing.type_check_only
class UserProfile(typing_extensions.TypedDict, total=False):
    accountId: str
    accountName: str
    etag: str
    kind: str
    profileId: str
    subAccountId: str
    subAccountName: str
    userName: str

@typing.type_check_only
class UserProfileList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[UserProfile]
    kind: str

@typing.type_check_only
class UserRole(typing_extensions.TypedDict, total=False):
    accountId: str
    defaultUserRole: bool
    id: str
    kind: str
    name: str
    parentUserRoleId: str
    permissions: _list[UserRolePermission]
    subaccountId: str

@typing.type_check_only
class UserRolePermission(typing_extensions.TypedDict, total=False):
    availability: typing_extensions.Literal[
        "NOT_AVAILABLE_BY_DEFAULT",
        "ACCOUNT_BY_DEFAULT",
        "SUBACCOUNT_AND_ACCOUNT_BY_DEFAULT",
        "ACCOUNT_ALWAYS",
        "SUBACCOUNT_AND_ACCOUNT_ALWAYS",
        "USER_PROFILE_ONLY",
    ]
    id: str
    kind: str
    name: str
    permissionGroupId: str

@typing.type_check_only
class UserRolePermissionGroup(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    name: str

@typing.type_check_only
class UserRolePermissionGroupsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    userRolePermissionGroups: _list[UserRolePermissionGroup]

@typing.type_check_only
class UserRolePermissionsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    userRolePermissions: _list[UserRolePermission]

@typing.type_check_only
class UserRolesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    userRoles: _list[UserRole]

@typing.type_check_only
class VideoFormat(typing_extensions.TypedDict, total=False):
    fileType: typing_extensions.Literal["FLV", "THREEGPP", "MP4", "WEBM", "M3U8"]
    id: int
    kind: str
    resolution: Size
    targetBitRate: int

@typing.type_check_only
class VideoFormatsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    videoFormats: _list[VideoFormat]

@typing.type_check_only
class VideoOffset(typing_extensions.TypedDict, total=False):
    offsetPercentage: int
    offsetSeconds: int

@typing.type_check_only
class VideoProcessingData(typing_extensions.TypedDict, total=False):
    errorReason: str
    processingState: typing_extensions.Literal[
        "UNKNOWN", "PROCESSING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class VideoSettings(typing_extensions.TypedDict, total=False):
    companionSettings: CompanionSetting
    durationSeconds: int
    kind: str
    obaEnabled: bool
    obaSettings: ObaIcon
    orientation: typing_extensions.Literal["ANY", "LANDSCAPE", "PORTRAIT"]
    publisherSpecificationId: str
    skippableSettings: SkippableSetting
    transcodeSettings: TranscodeSetting

@typing.type_check_only
class YoutubeSettings(typing_extensions.TypedDict, total=False):
    businessLogoCreativeIds: _list[str]
    businessName: str
    callToActions: _list[
        typing_extensions.Literal[
            "CALL_TO_ACTION_UNKNOWN",
            "CALL_TO_ACTION_LEARN_MORE",
            "CALL_TO_ACTION_GET_QUOTE",
            "CALL_TO_ACTION_APPLY_NOW",
            "CALL_TO_ACTION_SIGN_UP",
            "CALL_TO_ACTION_CONTACT_US",
            "CALL_TO_ACTION_SUBSCRIBE",
            "CALL_TO_ACTION_DOWNLOAD",
            "CALL_TO_ACTION_BOOK_NOW",
            "CALL_TO_ACTION_GET_OFFER",
            "CALL_TO_ACTION_SHOP_NOW",
            "CALL_TO_ACTION_VISIT_STORE",
            "CALL_TO_ACTION_CALL_NOW",
            "CALL_TO_ACTION_VIEW_MENU",
            "CALL_TO_ACTION_TEST_DRIVE",
            "CALL_TO_ACTION_SCHEDULE_NOW",
            "CALL_TO_ACTION_BUY_NOW",
            "CALL_TO_ACTION_DONATE_NOW",
            "CALL_TO_ACTION_ORDER_NOW",
            "CALL_TO_ACTION_PLAY_NOW",
            "CALL_TO_ACTION_SEE_MORE",
            "CALL_TO_ACTION_START_NOW",
            "CALL_TO_ACTION_VISIT_SITE",
            "CALL_TO_ACTION_WATCH_NOW",
        ]
    ]
    descriptions: _list[str]
    headlines: _list[str]
    longHeadlines: _list[str]
