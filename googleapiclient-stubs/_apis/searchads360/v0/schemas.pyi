import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleAdsSearchads360V0Common__AdScheduleInfo(
    typing_extensions.TypedDict, total=False
):
    dayOfWeek: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    endHour: int
    endMinute: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ZERO", "FIFTEEN", "THIRTY", "FORTY_FIVE"
    ]
    startHour: int
    startMinute: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ZERO", "FIFTEEN", "THIRTY", "FORTY_FIVE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__AdTextAsset(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__AgeRangeInfo(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AGE_RANGE_18_24",
        "AGE_RANGE_25_34",
        "AGE_RANGE_35_44",
        "AGE_RANGE_45_54",
        "AGE_RANGE_55_64",
        "AGE_RANGE_65_UP",
        "AGE_RANGE_UNDETERMINED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__AssetInteractionTarget(
    typing_extensions.TypedDict, total=False
):
    asset: str
    interactionOnThisAsset: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__AssetUsage(
    typing_extensions.TypedDict, total=False
):
    asset: str
    servedAssetFieldType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HEADLINE_1",
        "HEADLINE_2",
        "HEADLINE_3",
        "DESCRIPTION_1",
        "DESCRIPTION_2",
        "HEADLINE",
        "HEADLINE_IN_PORTRAIT",
        "LONG_HEADLINE",
        "DESCRIPTION",
        "DESCRIPTION_IN_PORTRAIT",
        "BUSINESS_NAME_IN_PORTRAIT",
        "BUSINESS_NAME",
        "MARKETING_IMAGE",
        "MARKETING_IMAGE_IN_PORTRAIT",
        "SQUARE_MARKETING_IMAGE",
        "PORTRAIT_MARKETING_IMAGE",
        "LOGO",
        "LANDSCAPE_LOGO",
        "CALL_TO_ACTION",
        "YOU_TUBE_VIDEO",
        "SITELINK",
        "CALL",
        "MOBILE_APP",
        "CALLOUT",
        "STRUCTURED_SNIPPET",
        "PRICE",
        "PROMOTION",
        "AD_IMAGE",
        "LEAD_FORM",
        "BUSINESS_LOGO",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__AudienceInfo(
    typing_extensions.TypedDict, total=False
):
    audience: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__BusinessProfileLocation(
    typing_extensions.TypedDict, total=False
):
    labels: _list[str]
    listingId: str
    storeCode: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__CallToActionAsset(
    typing_extensions.TypedDict, total=False
):
    callToAction: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "LEARN_MORE",
        "GET_QUOTE",
        "APPLY_NOW",
        "SIGN_UP",
        "CONTACT_US",
        "SUBSCRIBE",
        "DOWNLOAD",
        "BOOK_NOW",
        "SHOP_NOW",
        "BUY_NOW",
        "DONATE_NOW",
        "ORDER_NOW",
        "PLAY_NOW",
        "SEE_MORE",
        "START_NOW",
        "VISIT_SITE",
        "WATCH_NOW",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__CustomParameter(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__DeviceInfo(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET", "DESKTOP", "CONNECTED_TV", "OTHER"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__EnhancedCpc(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V0Common__FrequencyCapEntry(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V0Common__GenderInfo(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "MALE", "FEMALE", "UNDETERMINED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__ImageAsset(
    typing_extensions.TypedDict, total=False
):
    fileSize: str
    fullSize: GoogleAdsSearchads360V0Common__ImageDimension
    mimeType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "IMAGE_JPEG",
        "IMAGE_GIF",
        "IMAGE_PNG",
        "FLASH",
        "TEXT_HTML",
        "PDF",
        "MSWORD",
        "MSEXCEL",
        "RTF",
        "AUDIO_WAV",
        "AUDIO_MP3",
        "HTML5_AD_ZIP",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__ImageDimension(
    typing_extensions.TypedDict, total=False
):
    heightPixels: str
    url: str
    widthPixels: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__Keyword(typing_extensions.TypedDict, total=False):
    adGroupCriterion: str
    info: GoogleAdsSearchads360V0Common__KeywordInfo

@typing.type_check_only
class GoogleAdsSearchads360V0Common__KeywordInfo(
    typing_extensions.TypedDict, total=False
):
    matchType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"
    ]
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__LanguageInfo(
    typing_extensions.TypedDict, total=False
):
    languageConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__ListingGroupInfo(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "SUBDIVISION", "UNIT"]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__LocationGroupInfo(
    typing_extensions.TypedDict, total=False
):
    feedItemSets: _list[str]
    geoTargetConstants: _list[str]
    radius: str
    radiusUnits: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "METERS", "MILES", "MILLI_MILES"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__LocationInfo(
    typing_extensions.TypedDict, total=False
):
    geoTargetConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__ManualCpa(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V0Common__ManualCpc(
    typing_extensions.TypedDict, total=False
):
    enhancedCpcEnabled: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__ManualCpm(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V0Common__MaximizeConversionValue(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V0Common__MaximizeConversions(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__Metrics(typing_extensions.TypedDict, total=False):
    absoluteTopImpressionPercentage: float
    allConversions: float
    allConversionsByConversionDate: float
    allConversionsFromClickToCall: float
    allConversionsFromDirections: float
    allConversionsFromInteractionsRate: float
    allConversionsFromInteractionsValuePerInteraction: float
    allConversionsFromMenu: float
    allConversionsFromOrder: float
    allConversionsFromOtherEngagement: float
    allConversionsFromStoreVisit: float
    allConversionsFromStoreWebsite: float
    allConversionsValue: float
    allConversionsValueByConversionDate: float
    allConversionsValuePerCost: float
    averageCost: float
    averageCpc: float
    averageCpm: float
    averageQualityScore: float
    clicks: str
    clientAccountConversions: float
    clientAccountConversionsValue: float
    clientAccountCrossSellCostOfGoodsSoldMicros: str
    clientAccountCrossSellGrossProfitMicros: str
    clientAccountCrossSellRevenueMicros: str
    clientAccountCrossSellUnitsSold: float
    clientAccountLeadCostOfGoodsSoldMicros: str
    clientAccountLeadGrossProfitMicros: str
    clientAccountLeadRevenueMicros: str
    clientAccountLeadUnitsSold: float
    clientAccountViewThroughConversions: str
    contentBudgetLostImpressionShare: float
    contentImpressionShare: float
    contentRankLostImpressionShare: float
    conversionCustomMetrics: _list[GoogleAdsSearchads360V0Common__Value]
    conversions: float
    conversionsByConversionDate: float
    conversionsFromInteractionsRate: float
    conversionsFromInteractionsValuePerInteraction: float
    conversionsValue: float
    conversionsValueByConversionDate: float
    conversionsValuePerCost: float
    costMicros: str
    costPerAllConversions: float
    costPerConversion: float
    costPerCurrentModelAttributedConversion: float
    crossDeviceConversions: float
    crossDeviceConversionsByConversionDate: float
    crossDeviceConversionsValue: float
    crossDeviceConversionsValueByConversionDate: float
    crossSellCostOfGoodsSoldMicros: str
    crossSellGrossProfitMicros: str
    crossSellRevenueMicros: str
    crossSellUnitsSold: float
    ctr: float
    generalInvalidClickRate: float
    generalInvalidClicks: str
    historicalCreativeQualityScore: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    historicalLandingPageQualityScore: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    historicalQualityScore: str
    historicalSearchPredictedCtr: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    impressions: str
    interactionEventTypes: _list[
        typing_extensions.Literal[
            "UNSPECIFIED", "UNKNOWN", "CLICK", "ENGAGEMENT", "VIDEO_VIEW", "NONE"
        ]
    ]
    interactionRate: float
    interactions: str
    invalidClickRate: float
    invalidClicks: str
    leadCostOfGoodsSoldMicros: str
    leadGrossProfitMicros: str
    leadRevenueMicros: str
    leadUnitsSold: float
    mobileFriendlyClicksPercentage: float
    rawEventConversionMetrics: _list[GoogleAdsSearchads360V0Common__Value]
    searchAbsoluteTopImpressionShare: float
    searchBudgetLostAbsoluteTopImpressionShare: float
    searchBudgetLostImpressionShare: float
    searchBudgetLostTopImpressionShare: float
    searchClickShare: float
    searchExactMatchImpressionShare: float
    searchImpressionShare: float
    searchRankLostAbsoluteTopImpressionShare: float
    searchRankLostImpressionShare: float
    searchRankLostTopImpressionShare: float
    searchTopImpressionShare: float
    topImpressionPercentage: float
    valuePerAllConversions: float
    valuePerAllConversionsByConversionDate: float
    valuePerConversion: float
    valuePerConversionsByConversionDate: float
    visits: float

@typing.type_check_only
class GoogleAdsSearchads360V0Common__MobileAppAsset(
    typing_extensions.TypedDict, total=False
):
    appId: str
    appStore: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_APP_STORE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__PercentCpc(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    enhancedCpcEnabled: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__RealTimeBiddingSetting(
    typing_extensions.TypedDict, total=False
):
    optIn: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfo(
    typing_extensions.TypedDict, total=False
):
    adTrackingId: str
    description1: str
    description2: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfo(
    typing_extensions.TypedDict, total=False
):
    adTrackingId: str
    description1: str
    description2: str
    headline: str
    headline2: str
    headline3: str
    path1: str
    path2: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfo(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfo(
    typing_extensions.TypedDict, total=False
):
    adTrackingId: str
    descriptions: _list[GoogleAdsSearchads360V0Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V0Common__AdTextAsset]
    path1: str
    path2: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__SearchAds360TextAdInfo(
    typing_extensions.TypedDict, total=False
):
    adTrackingId: str
    description1: str
    description2: str
    displayMobileUrl: str
    displayUrl: str
    headline: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__Segments(typing_extensions.TypedDict, total=False):
    adNetworkType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH",
        "SEARCH_PARTNERS",
        "CONTENT",
        "YOUTUBE_SEARCH",
        "YOUTUBE_WATCH",
        "MIXED",
    ]
    assetInteractionTarget: GoogleAdsSearchads360V0Common__AssetInteractionTarget
    conversionAction: str
    conversionActionCategory: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DEFAULT",
        "PAGE_VIEW",
        "PURCHASE",
        "SIGNUP",
        "LEAD",
        "DOWNLOAD",
        "ADD_TO_CART",
        "BEGIN_CHECKOUT",
        "SUBSCRIBE_PAID",
        "PHONE_CALL_LEAD",
        "IMPORTED_LEAD",
        "SUBMIT_LEAD_FORM",
        "BOOK_APPOINTMENT",
        "REQUEST_QUOTE",
        "GET_DIRECTIONS",
        "OUTBOUND_CLICK",
        "CONTACT",
        "ENGAGEMENT",
        "STORE_VISIT",
        "STORE_SALE",
        "QUALIFIED_LEAD",
        "CONVERTED_LEAD",
    ]
    conversionActionName: str
    conversionCustomDimensions: _list[GoogleAdsSearchads360V0Common__Value]
    date: str
    dayOfWeek: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    device: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET", "DESKTOP", "CONNECTED_TV", "OTHER"
    ]
    geoTargetCity: str
    geoTargetCountry: str
    geoTargetMetro: str
    geoTargetRegion: str
    hour: int
    keyword: GoogleAdsSearchads360V0Common__Keyword
    month: str
    productBiddingCategoryLevel1: str
    productBiddingCategoryLevel2: str
    productBiddingCategoryLevel3: str
    productBiddingCategoryLevel4: str
    productBiddingCategoryLevel5: str
    productBrand: str
    productChannel: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"
    ]
    productChannelExclusivity: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "SINGLE_CHANNEL", "MULTI_CHANNEL"
    ]
    productCondition: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "OLD", "NEW", "REFURBISHED", "USED"
    ]
    productCountry: str
    productCustomAttribute0: str
    productCustomAttribute1: str
    productCustomAttribute2: str
    productCustomAttribute3: str
    productCustomAttribute4: str
    productItemId: str
    productLanguage: str
    productSoldBiddingCategoryLevel1: str
    productSoldBiddingCategoryLevel2: str
    productSoldBiddingCategoryLevel3: str
    productSoldBiddingCategoryLevel4: str
    productSoldBiddingCategoryLevel5: str
    productSoldBrand: str
    productSoldCondition: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "OLD", "NEW", "REFURBISHED", "USED"
    ]
    productSoldCustomAttribute0: str
    productSoldCustomAttribute1: str
    productSoldCustomAttribute2: str
    productSoldCustomAttribute3: str
    productSoldCustomAttribute4: str
    productSoldItemId: str
    productSoldTitle: str
    productSoldTypeL1: str
    productSoldTypeL2: str
    productSoldTypeL3: str
    productSoldTypeL4: str
    productSoldTypeL5: str
    productStoreId: str
    productTitle: str
    productTypeL1: str
    productTypeL2: str
    productTypeL3: str
    productTypeL4: str
    productTypeL5: str
    quarter: str
    rawEventConversionDimensions: _list[GoogleAdsSearchads360V0Common__Value]
    week: str
    year: int

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetCpa(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetCpm(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetImpressionShare(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    location: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ANYWHERE_ON_PAGE",
        "TOP_OF_PAGE",
        "ABSOLUTE_TOP_OF_PAGE",
    ]
    locationFractionMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetOutrankShare(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetRestriction(
    typing_extensions.TypedDict, total=False
):
    bidOnly: bool
    targetingDimension: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "KEYWORD",
        "AUDIENCE",
        "TOPIC",
        "GENDER",
        "AGE_RANGE",
        "PLACEMENT",
        "PARENTAL_STATUS",
        "INCOME_RANGE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetRoas(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetSpend(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    targetSpendMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TargetingSetting(
    typing_extensions.TypedDict, total=False
):
    targetRestrictions: _list[GoogleAdsSearchads360V0Common__TargetRestriction]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TextAsset(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__TextLabel(
    typing_extensions.TypedDict, total=False
):
    backgroundColor: str
    description: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__UnifiedCallAsset(
    typing_extensions.TypedDict, total=False
):
    adScheduleTargets: _list[GoogleAdsSearchads360V0Common__AdScheduleInfo]
    callConversionAction: str
    callConversionReportingState: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISABLED",
        "USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION",
        "USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION",
    ]
    callOnly: bool
    callTrackingEnabled: bool
    countryCode: str
    endDate: str
    phoneNumber: str
    startDate: str
    useSearcherTimeZone: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__UnifiedCalloutAsset(
    typing_extensions.TypedDict, total=False
):
    adScheduleTargets: _list[GoogleAdsSearchads360V0Common__AdScheduleInfo]
    calloutText: str
    endDate: str
    startDate: str
    useSearcherTimeZone: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__UnifiedLocationAsset(
    typing_extensions.TypedDict, total=False
):
    businessProfileLocations: _list[
        GoogleAdsSearchads360V0Common__BusinessProfileLocation
    ]
    locationOwnershipType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "BUSINESS_OWNER", "AFFILIATE"
    ]
    placeId: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__UnifiedPageFeedAsset(
    typing_extensions.TypedDict, total=False
):
    labels: _list[str]
    pageUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__UnifiedSitelinkAsset(
    typing_extensions.TypedDict, total=False
):
    adScheduleTargets: _list[GoogleAdsSearchads360V0Common__AdScheduleInfo]
    description1: str
    description2: str
    endDate: str
    linkText: str
    mobilePreferred: bool
    startDate: str
    trackingId: str
    useSearcherTimeZone: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Common__UserListInfo(
    typing_extensions.TypedDict, total=False
):
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__Value(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    doubleValue: float
    floatValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__WebpageConditionInfo(
    typing_extensions.TypedDict, total=False
):
    argument: str
    operand: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "URL",
        "CATEGORY",
        "PAGE_TITLE",
        "PAGE_CONTENT",
        "CUSTOM_LABEL",
    ]
    operator: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "EQUALS", "CONTAINS"]

@typing.type_check_only
class GoogleAdsSearchads360V0Common__WebpageInfo(
    typing_extensions.TypedDict, total=False
):
    conditions: _list[GoogleAdsSearchads360V0Common__WebpageConditionInfo]
    coveragePercentage: float
    criterionName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Common__YoutubeVideoAsset(
    typing_extensions.TypedDict, total=False
):
    youtubeVideoId: str
    youtubeVideoTitle: str

@typing.type_check_only
class GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElement(
    typing_extensions.TypedDict, total=False
):
    fieldName: str
    index: int

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__ErrorCode(
    typing_extensions.TypedDict, total=False
):
    authenticationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AUTHENTICATION_ERROR",
        "CLIENT_CUSTOMER_ID_INVALID",
        "CUSTOMER_NOT_FOUND",
        "GOOGLE_ACCOUNT_DELETED",
        "GOOGLE_ACCOUNT_COOKIE_INVALID",
        "GOOGLE_ACCOUNT_AUTHENTICATION_FAILED",
        "GOOGLE_ACCOUNT_USER_AND_ADS_USER_MISMATCH",
        "LOGIN_COOKIE_REQUIRED",
        "NOT_ADS_USER",
        "OAUTH_TOKEN_INVALID",
        "OAUTH_TOKEN_EXPIRED",
        "OAUTH_TOKEN_DISABLED",
        "OAUTH_TOKEN_REVOKED",
        "OAUTH_TOKEN_HEADER_INVALID",
        "LOGIN_COOKIE_INVALID",
        "USER_ID_INVALID",
        "TWO_STEP_VERIFICATION_NOT_ENROLLED",
        "ADVANCED_PROTECTION_NOT_ENROLLED",
    ]
    authorizationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "USER_PERMISSION_DENIED",
        "PROJECT_DISABLED",
        "AUTHORIZATION_ERROR",
        "ACTION_NOT_PERMITTED",
        "INCOMPLETE_SIGNUP",
        "CUSTOMER_NOT_ENABLED",
        "MISSING_TOS",
        "INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION",
        "SERVICE_ACCESS_DENIED",
        "ACCESS_DENIED_FOR_ACCOUNT_TYPE",
        "METRIC_ACCESS_DENIED",
    ]
    customColumnError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOM_COLUMN_NOT_FOUND",
        "CUSTOM_COLUMN_NOT_AVAILABLE",
    ]
    dateError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_FIELD_VALUES_IN_DATE",
        "INVALID_FIELD_VALUES_IN_DATE_TIME",
        "INVALID_STRING_DATE",
        "INVALID_STRING_DATE_TIME_MICROS",
        "INVALID_STRING_DATE_TIME_SECONDS",
        "INVALID_STRING_DATE_TIME_SECONDS_WITH_OFFSET",
        "EARLIER_THAN_MINIMUM_DATE",
        "LATER_THAN_MAXIMUM_DATE",
        "DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE",
        "DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL",
    ]
    dateRangeError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_DATE",
        "START_DATE_AFTER_END_DATE",
        "CANNOT_SET_DATE_TO_PAST",
        "AFTER_MAXIMUM_ALLOWABLE_DATE",
        "CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED",
    ]
    distinctError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_ELEMENT", "DUPLICATE_TYPE"
    ]
    headerError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_USER_SELECTED_CUSTOMER_ID",
        "INVALID_LOGIN_CUSTOMER_ID",
    ]
    internalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INTERNAL_ERROR",
        "ERROR_CODE_NOT_PUBLISHED",
        "TRANSIENT_ERROR",
        "DEADLINE_EXCEEDED",
    ]
    invalidParameterError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_CURRENCY_CODE"
    ]
    queryError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "QUERY_ERROR",
        "BAD_ENUM_CONSTANT",
        "BAD_ESCAPE_SEQUENCE",
        "BAD_FIELD_NAME",
        "BAD_LIMIT_VALUE",
        "BAD_NUMBER",
        "BAD_OPERATOR",
        "BAD_PARAMETER_NAME",
        "BAD_PARAMETER_VALUE",
        "BAD_RESOURCE_TYPE_IN_FROM_CLAUSE",
        "BAD_SYMBOL",
        "BAD_VALUE",
        "DATE_RANGE_TOO_WIDE",
        "DATE_RANGE_TOO_NARROW",
        "EXPECTED_AND",
        "EXPECTED_BY",
        "EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE",
        "EXPECTED_FILTERS_ON_DATE_RANGE",
        "EXPECTED_FROM",
        "EXPECTED_LIST",
        "EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE",
        "EXPECTED_SELECT",
        "EXPECTED_SINGLE_VALUE",
        "EXPECTED_VALUE_WITH_BETWEEN_OPERATOR",
        "INVALID_DATE_FORMAT",
        "MISALIGNED_DATE_FOR_FILTER",
        "INVALID_STRING_VALUE",
        "INVALID_VALUE_WITH_BETWEEN_OPERATOR",
        "INVALID_VALUE_WITH_DURING_OPERATOR",
        "INVALID_VALUE_WITH_LIKE_OPERATOR",
        "OPERATOR_FIELD_MISMATCH",
        "PROHIBITED_EMPTY_LIST_IN_CONDITION",
        "PROHIBITED_ENUM_CONSTANT",
        "PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE",
        "PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE",
        "PROHIBITED_FIELD_IN_SELECT_CLAUSE",
        "PROHIBITED_FIELD_IN_WHERE_CLAUSE",
        "PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE",
        "PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE",
        "PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE",
        "PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE",
        "PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE",
        "PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE",
        "LIMIT_VALUE_TOO_LOW",
        "PROHIBITED_NEWLINE_IN_STRING",
        "PROHIBITED_VALUE_COMBINATION_IN_LIST",
        "PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR",
        "STRING_NOT_TERMINATED",
        "TOO_MANY_SEGMENTS",
        "UNEXPECTED_END_OF_QUERY",
        "UNEXPECTED_FROM_CLAUSE",
        "UNRECOGNIZED_FIELD",
        "UNEXPECTED_INPUT",
        "REQUESTED_METRICS_FOR_MANAGER",
        "FILTER_HAS_TOO_MANY_VALUES",
    ]
    quotaError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "RESOURCE_EXHAUSTED", "RESOURCE_TEMPORARILY_EXHAUSTED"
    ]
    requestError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RESOURCE_NAME_MISSING",
        "RESOURCE_NAME_MALFORMED",
        "BAD_RESOURCE_ID",
        "INVALID_PRODUCT_NAME",
        "INVALID_CUSTOMER_ID",
        "OPERATION_REQUIRED",
        "RESOURCE_NOT_FOUND",
        "INVALID_PAGE_TOKEN",
        "EXPIRED_PAGE_TOKEN",
        "INVALID_PAGE_SIZE",
        "REQUIRED_FIELD_MISSING",
        "IMMUTABLE_FIELD",
        "TOO_MANY_MUTATE_OPERATIONS",
        "CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT",
        "CANNOT_MODIFY_FOREIGN_FIELD",
        "INVALID_ENUM_VALUE",
        "LOGIN_CUSTOMER_ID_PARAMETER_MISSING",
        "LOGIN_OR_LINKED_CUSTOMER_ID_PARAMETER_REQUIRED",
        "VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN",
        "CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS",
        "CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS",
        "INCONSISTENT_RETURN_SUMMARY_ROW_VALUE",
        "TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED",
        "RPC_DEADLINE_TOO_SHORT",
        "PRODUCT_NOT_SUPPORTED",
    ]
    sizeLimitError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUEST_SIZE_LIMIT_EXCEEDED",
        "RESPONSE_SIZE_LIMIT_EXCEEDED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__ErrorDetails(
    typing_extensions.TypedDict, total=False
):
    quotaErrorDetails: GoogleAdsSearchads360V0Errors__QuotaErrorDetails
    unpublishedErrorCode: str

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__ErrorLocation(
    typing_extensions.TypedDict, total=False
):
    fieldPathElements: _list[
        GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElement
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__QuotaErrorDetails(
    typing_extensions.TypedDict, total=False
):
    rateName: str
    rateScope: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACCOUNT", "DEVELOPER"
    ]
    retryDelay: str

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__SearchAds360Error(
    typing_extensions.TypedDict, total=False
):
    details: GoogleAdsSearchads360V0Errors__ErrorDetails
    errorCode: GoogleAdsSearchads360V0Errors__ErrorCode
    location: GoogleAdsSearchads360V0Errors__ErrorLocation
    message: str
    trigger: GoogleAdsSearchads360V0Common__Value

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__SearchAds360Failure(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleAdsSearchads360V0Errors__SearchAds360Error]
    requestId: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_MaximizeConversionValue(
    typing_extensions.TypedDict, total=False
):
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_MaximizeConversions(
    typing_extensions.TypedDict, total=False
):
    targetCpa: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetCpa(
    typing_extensions.TypedDict, total=False
):
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetImpressionShare(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    location: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ANYWHERE_ON_PAGE",
        "TOP_OF_PAGE",
        "ABSOLUTE_TOP_OF_PAGE",
    ]
    locationFractionMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetRoas(
    typing_extensions.TypedDict, total=False
):
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetSpend(
    typing_extensions.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    targetSpendMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AdGroupCriterion_PositionEstimates(
    typing_extensions.TypedDict, total=False
):
    topOfPageCpcMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfo(
    typing_extensions.TypedDict, total=False
):
    qualityScore: int

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSetting(
    typing_extensions.TypedDict, total=False
):
    domainName: str
    languageCode: str
    useSuppliedUrlsOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSetting(
    typing_extensions.TypedDict, total=False
):
    negativeGeoTargetType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "PRESENCE_OR_INTEREST", "PRESENCE"
    ]
    positiveGeoTargetType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "PRESENCE_OR_INTEREST", "SEARCH_INTEREST", "PRESENCE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_NetworkSettings(
    typing_extensions.TypedDict, total=False
):
    targetContentNetwork: bool
    targetGoogleSearch: bool
    targetPartnerSearchNetwork: bool
    targetSearchNetwork: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSetting(
    typing_extensions.TypedDict, total=False
):
    optimizationGoalTypes: _list[
        typing_extensions.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CALL_CLICKS",
            "DRIVING_DIRECTIONS",
            "APP_PRE_REGISTRATION",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimization(
    typing_extensions.TypedDict, total=False
):
    conversionActions: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_ShoppingSetting(
    typing_extensions.TypedDict, total=False
):
    campaignPriority: int
    enableLocal: bool
    feedLabel: str
    merchantId: str
    salesCountry: str
    useVehicleInventory: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_Campaign_TrackingSetting(
    typing_extensions.TypedDict, total=False
):
    trackingUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettings(
    typing_extensions.TypedDict, total=False
):
    attributionModel: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXTERNAL",
        "GOOGLE_ADS_LAST_CLICK",
        "GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK",
        "GOOGLE_SEARCH_ATTRIBUTION_LINEAR",
        "GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY",
        "GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED",
        "GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN",
    ]
    dataDrivenModelStatus: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "AVAILABLE", "STALE", "EXPIRED", "NEVER_GENERATED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettings(
    typing_extensions.TypedDict, total=False
):
    activityGroupTag: str
    activityId: str
    activityTag: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettings(
    typing_extensions.TypedDict, total=False
):
    alwaysUseDefaultValue: bool
    defaultCurrencyCode: str
    defaultValue: float

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ConversionCustomVariable_FloodlightConversionCustomVariableInfo(
    typing_extensions.TypedDict, total=False
):
    floodlightVariableDataType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "NUMBER", "STRING"
    ]
    floodlightVariableType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "DIMENSION", "METRIC", "UNSET"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductBiddingCategory(
    typing_extensions.TypedDict, total=False
):
    id: str
    level: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductBrand(
    typing_extensions.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductChannel(
    typing_extensions.TypedDict, total=False
):
    channel: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductCondition(
    typing_extensions.TypedDict, total=False
):
    condition: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "NEW", "REFURBISHED", "USED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductCustomAttribute(
    typing_extensions.TypedDict, total=False
):
    index: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INDEX0", "INDEX1", "INDEX2", "INDEX3", "INDEX4"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductItemId(
    typing_extensions.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductType(
    typing_extensions.TypedDict, total=False
):
    level: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AccessibleBiddingStrategy(
    typing_extensions.TypedDict, total=False
):
    id: str
    maximizeConversionValue: GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_MaximizeConversionValue
    maximizeConversions: (
        GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_MaximizeConversions
    )
    name: str
    ownerCustomerId: str
    ownerDescriptiveName: str
    resourceName: str
    targetCpa: GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetCpa
    targetImpressionShare: (
        GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetImpressionShare
    )
    targetRoas: GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetRoas
    targetSpend: GoogleAdsSearchads360V0Resources_AccessibleBiddingStrategy_TargetSpend
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "COMMISSION",
        "ENHANCED_CPC",
        "INVALID",
        "MANUAL_CPA",
        "MANUAL_CPC",
        "MANUAL_CPM",
        "MANUAL_CPV",
        "MAXIMIZE_CONVERSIONS",
        "MAXIMIZE_CONVERSION_VALUE",
        "PAGE_ONE_PROMOTED",
        "PERCENT_CPC",
        "TARGET_CPA",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Ad(typing_extensions.TypedDict, total=False):
    displayUrl: str
    expandedDynamicSearchAd: (
        GoogleAdsSearchads360V0Common__SearchAds360ExpandedDynamicSearchAdInfo
    )
    expandedTextAd: GoogleAdsSearchads360V0Common__SearchAds360ExpandedTextAdInfo
    finalUrls: _list[str]
    id: str
    name: str
    productAd: GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfo
    resourceName: str
    responsiveSearchAd: (
        GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfo
    )
    textAd: GoogleAdsSearchads360V0Common__SearchAds360TextAdInfo
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TEXT_AD",
        "EXPANDED_TEXT_AD",
        "CALL_ONLY_AD",
        "EXPANDED_DYNAMIC_SEARCH_AD",
        "HOTEL_AD",
        "SHOPPING_SMART_AD",
        "SHOPPING_PRODUCT_AD",
        "VIDEO_AD",
        "GMAIL_AD",
        "IMAGE_AD",
        "RESPONSIVE_SEARCH_AD",
        "LEGACY_RESPONSIVE_DISPLAY_AD",
        "APP_AD",
        "LEGACY_APP_INSTALL_AD",
        "RESPONSIVE_DISPLAY_AD",
        "LOCAL_AD",
        "HTML5_UPLOAD_AD",
        "DYNAMIC_HTML5_AD",
        "APP_ENGAGEMENT_AD",
        "SHOPPING_COMPARISON_LISTING_AD",
        "VIDEO_BUMPER_AD",
        "VIDEO_NON_SKIPPABLE_IN_STREAM_AD",
        "VIDEO_OUTSTREAM_AD",
        "VIDEO_TRUEVIEW_DISCOVERY_AD",
        "VIDEO_TRUEVIEW_IN_STREAM_AD",
        "VIDEO_RESPONSIVE_AD",
        "SMART_CAMPAIGN_AD",
        "APP_PRE_REGISTRATION_AD",
        "DISCOVERY_MULTI_ASSET_AD",
        "DISCOVERY_CAROUSEL_AD",
        "TRAVEL_AD",
        "DISCOVERY_VIDEO_RESPONSIVE_AD",
        "MULTIMEDIA_AD",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroup(
    typing_extensions.TypedDict, total=False
):
    adRotationMode: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "OPTIMIZE", "ROTATE_FOREVER"
    ]
    cpcBidMicros: str
    creationTime: str
    effectiveLabels: _list[str]
    endDate: str
    engineId: str
    engineStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_ELIGIBLE",
        "AD_GROUP_EXPIRED",
        "AD_GROUP_REMOVED",
        "AD_GROUP_DRAFT",
        "AD_GROUP_PAUSED",
        "AD_GROUP_SERVING",
        "AD_GROUP_SUBMITTED",
        "CAMPAIGN_PAUSED",
        "ACCOUNT_PAUSED",
    ]
    id: str
    labels: _list[str]
    languageCode: str
    lastModifiedTime: str
    name: str
    resourceName: str
    startDate: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]
    targetingSetting: GoogleAdsSearchads360V0Common__TargetingSetting
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH_STANDARD",
        "DISPLAY_STANDARD",
        "SHOPPING_PRODUCT_ADS",
        "SHOPPING_SHOWCASE_ADS",
        "HOTEL_ADS",
        "SHOPPING_SMART_ADS",
        "VIDEO_BUMPER",
        "VIDEO_TRUE_VIEW_IN_STREAM",
        "VIDEO_TRUE_VIEW_IN_DISPLAY",
        "VIDEO_NON_SKIPPABLE_IN_STREAM",
        "VIDEO_OUTSTREAM",
        "SEARCH_DYNAMIC_ADS",
        "SHOPPING_COMPARISON_LISTING_ADS",
        "PROMOTED_HOTEL_ADS",
        "VIDEO_RESPONSIVE",
        "VIDEO_EFFICIENT_REACH",
        "SMART_CAMPAIGN_ADS",
        "TRAVEL_ADS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupAd(
    typing_extensions.TypedDict, total=False
):
    ad: GoogleAdsSearchads360V0Resources__Ad
    creationTime: str
    effectiveLabels: _list[str]
    engineId: str
    engineStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_AD_ELIGIBLE",
        "AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN",
        "AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW",
        "AD_GROUP_AD_PARTIALLY_INVALID",
        "AD_GROUP_AD_TO_BE_ACTIVATED",
        "AD_GROUP_AD_NOT_REVIEWED",
        "AD_GROUP_AD_ON_HOLD",
        "AD_GROUP_AD_PAUSED",
        "AD_GROUP_AD_REMOVED",
        "AD_GROUP_AD_PENDING_REVIEW",
        "AD_GROUP_AD_UNDER_REVIEW",
        "AD_GROUP_AD_APPROVED",
        "AD_GROUP_AD_DISAPPROVED",
        "AD_GROUP_AD_SERVING",
        "AD_GROUP_AD_ACCOUNT_PAUSED",
        "AD_GROUP_AD_CAMPAIGN_PAUSED",
        "AD_GROUP_AD_AD_GROUP_PAUSED",
    ]
    labels: _list[str]
    lastModifiedTime: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupAdEffectiveLabel(
    typing_extensions.TypedDict, total=False
):
    adGroupAd: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupAdLabel(
    typing_extensions.TypedDict, total=False
):
    adGroupAd: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupAsset(
    typing_extensions.TypedDict, total=False
):
    adGroup: str
    asset: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupAssetSet(
    typing_extensions.TypedDict, total=False
):
    adGroup: str
    assetSet: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupAudienceView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupBidModifier(
    typing_extensions.TypedDict, total=False
):
    bidModifier: float
    device: GoogleAdsSearchads360V0Common__DeviceInfo
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupCriterion(
    typing_extensions.TypedDict, total=False
):
    adGroup: str
    ageRange: GoogleAdsSearchads360V0Common__AgeRangeInfo
    bidModifier: float
    cpcBidMicros: str
    creationTime: str
    criterionId: str
    effectiveCpcBidMicros: str
    effectiveLabels: _list[str]
    engineId: str
    engineStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_CRITERION_ELIGIBLE",
        "AD_GROUP_CRITERION_INAPPROPRIATE_FOR_CAMPAIGN",
        "AD_GROUP_CRITERION_INVALID_MOBILE_SEARCH",
        "AD_GROUP_CRITERION_INVALID_PC_SEARCH",
        "AD_GROUP_CRITERION_INVALID_SEARCH",
        "AD_GROUP_CRITERION_LOW_SEARCH_VOLUME",
        "AD_GROUP_CRITERION_MOBILE_URL_UNDER_REVIEW",
        "AD_GROUP_CRITERION_PARTIALLY_INVALID",
        "AD_GROUP_CRITERION_TO_BE_ACTIVATED",
        "AD_GROUP_CRITERION_UNDER_REVIEW",
        "AD_GROUP_CRITERION_NOT_REVIEWED",
        "AD_GROUP_CRITERION_ON_HOLD",
        "AD_GROUP_CRITERION_PENDING_REVIEW",
        "AD_GROUP_CRITERION_PAUSED",
        "AD_GROUP_CRITERION_REMOVED",
        "AD_GROUP_CRITERION_APPROVED",
        "AD_GROUP_CRITERION_DISAPPROVED",
        "AD_GROUP_CRITERION_SERVING",
        "AD_GROUP_CRITERION_ACCOUNT_PAUSED",
    ]
    finalUrlSuffix: str
    finalUrls: _list[str]
    gender: GoogleAdsSearchads360V0Common__GenderInfo
    keyword: GoogleAdsSearchads360V0Common__KeywordInfo
    labels: _list[str]
    lastModifiedTime: str
    listingGroup: GoogleAdsSearchads360V0Common__ListingGroupInfo
    location: GoogleAdsSearchads360V0Common__LocationInfo
    negative: bool
    positionEstimates: (
        GoogleAdsSearchads360V0Resources_AdGroupCriterion_PositionEstimates
    )
    qualityInfo: GoogleAdsSearchads360V0Resources_AdGroupCriterion_QualityInfo
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]
    trackingUrlTemplate: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "KEYWORD",
        "PLACEMENT",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "DEVICE",
        "LOCATION",
        "LISTING_GROUP",
        "AD_SCHEDULE",
        "AGE_RANGE",
        "GENDER",
        "INCOME_RANGE",
        "PARENTAL_STATUS",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "USER_LIST",
        "PROXIMITY",
        "TOPIC",
        "LISTING_SCOPE",
        "LANGUAGE",
        "IP_BLOCK",
        "CONTENT_LABEL",
        "CARRIER",
        "USER_INTEREST",
        "WEBPAGE",
        "OPERATING_SYSTEM_VERSION",
        "APP_PAYMENT_MODEL",
        "MOBILE_DEVICE",
        "CUSTOM_AFFINITY",
        "CUSTOM_INTENT",
        "LOCATION_GROUP",
        "CUSTOM_AUDIENCE",
        "COMBINED_AUDIENCE",
        "KEYWORD_THEME",
        "AUDIENCE",
        "LOCAL_SERVICE_ID",
        "BRAND",
        "BRAND_LIST",
        "LIFE_EVENT",
    ]
    userList: GoogleAdsSearchads360V0Common__UserListInfo
    webpage: GoogleAdsSearchads360V0Common__WebpageInfo

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupCriterionEffectiveLabel(
    typing_extensions.TypedDict, total=False
):
    adGroupCriterion: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupCriterionLabel(
    typing_extensions.TypedDict, total=False
):
    adGroupCriterion: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupEffectiveLabel(
    typing_extensions.TypedDict, total=False
):
    adGroup: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupLabel(
    typing_extensions.TypedDict, total=False
):
    adGroup: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AgeRangeView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Asset(typing_extensions.TypedDict, total=False):
    callAsset: GoogleAdsSearchads360V0Common__UnifiedCallAsset
    callToActionAsset: GoogleAdsSearchads360V0Common__CallToActionAsset
    calloutAsset: GoogleAdsSearchads360V0Common__UnifiedCalloutAsset
    creationTime: str
    engineStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SERVING",
        "SERVING_LIMITED",
        "DISAPPROVED",
        "DISABLED",
        "REMOVED",
    ]
    finalUrls: _list[str]
    id: str
    imageAsset: GoogleAdsSearchads360V0Common__ImageAsset
    lastModifiedTime: str
    locationAsset: GoogleAdsSearchads360V0Common__UnifiedLocationAsset
    mobileAppAsset: GoogleAdsSearchads360V0Common__MobileAppAsset
    name: str
    pageFeedAsset: GoogleAdsSearchads360V0Common__UnifiedPageFeedAsset
    resourceName: str
    sitelinkAsset: GoogleAdsSearchads360V0Common__UnifiedSitelinkAsset
    status: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ENABLED",
        "REMOVED",
        "ARCHIVED",
        "PENDING_SYSTEM_GENERATED",
    ]
    textAsset: GoogleAdsSearchads360V0Common__TextAsset
    trackingUrlTemplate: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "YOUTUBE_VIDEO",
        "MEDIA_BUNDLE",
        "IMAGE",
        "TEXT",
        "LEAD_FORM",
        "BOOK_ON_GOOGLE",
        "PROMOTION",
        "CALLOUT",
        "STRUCTURED_SNIPPET",
        "SITELINK",
        "PAGE_FEED",
        "DYNAMIC_EDUCATION",
        "MOBILE_APP",
        "HOTEL_CALLOUT",
        "CALL",
        "PRICE",
        "CALL_TO_ACTION",
        "DYNAMIC_REAL_ESTATE",
        "DYNAMIC_CUSTOM",
        "DYNAMIC_HOTELS_AND_RENTALS",
        "DYNAMIC_FLIGHTS",
        "DISCOVERY_CAROUSEL_CARD",
        "DYNAMIC_TRAVEL",
        "DYNAMIC_LOCAL",
        "DYNAMIC_JOBS",
        "LOCATION",
        "HOTEL_PROPERTY",
    ]
    youtubeVideoAsset: GoogleAdsSearchads360V0Common__YoutubeVideoAsset

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetGroup(
    typing_extensions.TypedDict, total=False
):
    adStrength: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "NO_ADS",
        "POOR",
        "AVERAGE",
        "GOOD",
        "EXCELLENT",
    ]
    campaign: str
    finalMobileUrls: _list[str]
    finalUrls: _list[str]
    id: str
    name: str
    path1: str
    path2: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetGroupAsset(
    typing_extensions.TypedDict, total=False
):
    asset: str
    assetGroup: str
    fieldType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HEADLINE",
        "DESCRIPTION",
        "MANDATORY_AD_TEXT",
        "MARKETING_IMAGE",
        "MEDIA_BUNDLE",
        "YOUTUBE_VIDEO",
        "BOOK_ON_GOOGLE",
        "LEAD_FORM",
        "PROMOTION",
        "CALLOUT",
        "STRUCTURED_SNIPPET",
        "SITELINK",
        "MOBILE_APP",
        "HOTEL_CALLOUT",
        "CALL",
        "PRICE",
        "LONG_HEADLINE",
        "BUSINESS_NAME",
        "SQUARE_MARKETING_IMAGE",
        "PORTRAIT_MARKETING_IMAGE",
        "LOGO",
        "LANDSCAPE_LOGO",
        "VIDEO",
        "CALL_TO_ACTION_SELECTION",
        "AD_IMAGE",
        "BUSINESS_LOGO",
        "HOTEL_PROPERTY",
        "DISCOVERY_CAROUSEL_CARD",
    ]
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetGroupAssetCombinationData(
    typing_extensions.TypedDict, total=False
):
    assetCombinationServedAssets: _list[GoogleAdsSearchads360V0Common__AssetUsage]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetGroupListingGroupFilter(
    typing_extensions.TypedDict, total=False
):
    assetGroup: str
    caseValue: GoogleAdsSearchads360V0Resources__ListingGroupFilterDimension
    id: str
    parentListingGroupFilter: str
    path: GoogleAdsSearchads360V0Resources__ListingGroupFilterDimensionPath
    resourceName: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "SUBDIVISION", "UNIT_INCLUDED", "UNIT_EXCLUDED"
    ]
    vertical: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "SHOPPING"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetGroupSignal(
    typing_extensions.TypedDict, total=False
):
    assetGroup: str
    audience: GoogleAdsSearchads360V0Common__AudienceInfo
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetGroupTopCombinationView(
    typing_extensions.TypedDict, total=False
):
    assetGroupTopCombinations: _list[
        GoogleAdsSearchads360V0Resources__AssetGroupAssetCombinationData
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetSet(
    typing_extensions.TypedDict, total=False
):
    id: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AssetSetAsset(
    typing_extensions.TypedDict, total=False
):
    asset: str
    assetSet: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Audience(
    typing_extensions.TypedDict, total=False
):
    description: str
    id: str
    name: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__BiddingStrategy(
    typing_extensions.TypedDict, total=False
):
    campaignCount: str
    currencyCode: str
    effectiveCurrencyCode: str
    enhancedCpc: GoogleAdsSearchads360V0Common__EnhancedCpc
    id: str
    maximizeConversionValue: GoogleAdsSearchads360V0Common__MaximizeConversionValue
    maximizeConversions: GoogleAdsSearchads360V0Common__MaximizeConversions
    name: str
    nonRemovedCampaignCount: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    targetCpa: GoogleAdsSearchads360V0Common__TargetCpa
    targetImpressionShare: GoogleAdsSearchads360V0Common__TargetImpressionShare
    targetOutrankShare: GoogleAdsSearchads360V0Common__TargetOutrankShare
    targetRoas: GoogleAdsSearchads360V0Common__TargetRoas
    targetSpend: GoogleAdsSearchads360V0Common__TargetSpend
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "COMMISSION",
        "ENHANCED_CPC",
        "INVALID",
        "MANUAL_CPA",
        "MANUAL_CPC",
        "MANUAL_CPM",
        "MANUAL_CPV",
        "MAXIMIZE_CONVERSIONS",
        "MAXIMIZE_CONVERSION_VALUE",
        "PAGE_ONE_PROMOTED",
        "PERCENT_CPC",
        "TARGET_CPA",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Campaign(
    typing_extensions.TypedDict, total=False
):
    accessibleBiddingStrategy: str
    adServingOptimizationStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPTIMIZE",
        "CONVERSION_OPTIMIZE",
        "ROTATE",
        "ROTATE_INDEFINITELY",
        "UNAVAILABLE",
    ]
    advertisingChannelSubType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH_MOBILE_APP",
        "DISPLAY_MOBILE_APP",
        "SEARCH_EXPRESS",
        "DISPLAY_EXPRESS",
        "SHOPPING_SMART_ADS",
        "DISPLAY_GMAIL_AD",
        "DISPLAY_SMART_CAMPAIGN",
        "VIDEO_OUTSTREAM",
        "VIDEO_ACTION",
        "VIDEO_NON_SKIPPABLE",
        "APP_CAMPAIGN",
        "APP_CAMPAIGN_FOR_ENGAGEMENT",
        "LOCAL_CAMPAIGN",
        "SHOPPING_COMPARISON_LISTING_ADS",
        "SMART_CAMPAIGN",
        "VIDEO_SEQUENCE",
        "APP_CAMPAIGN_FOR_PRE_REGISTRATION",
        "VIDEO_REACH_TARGET_FREQUENCY",
        "TRAVEL_ACTIVITIES",
        "SOCIAL_FACEBOOK_TRACKING_ONLY",
    ]
    advertisingChannelType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH",
        "DISPLAY",
        "SHOPPING",
        "HOTEL",
        "VIDEO",
        "MULTI_CHANNEL",
        "LOCAL",
        "SMART",
        "PERFORMANCE_MAX",
        "LOCAL_SERVICES",
        "DISCOVERY",
        "TRAVEL",
        "SOCIAL",
    ]
    biddingStrategy: str
    biddingStrategySystemStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ENABLED",
        "LEARNING_NEW",
        "LEARNING_SETTING_CHANGE",
        "LEARNING_BUDGET_CHANGE",
        "LEARNING_COMPOSITION_CHANGE",
        "LEARNING_CONVERSION_TYPE_CHANGE",
        "LEARNING_CONVERSION_SETTING_CHANGE",
        "LIMITED_BY_CPC_BID_CEILING",
        "LIMITED_BY_CPC_BID_FLOOR",
        "LIMITED_BY_DATA",
        "LIMITED_BY_BUDGET",
        "LIMITED_BY_LOW_PRIORITY_SPEND",
        "LIMITED_BY_LOW_QUALITY",
        "LIMITED_BY_INVENTORY",
        "MISCONFIGURED_ZERO_ELIGIBILITY",
        "MISCONFIGURED_CONVERSION_TYPES",
        "MISCONFIGURED_CONVERSION_SETTINGS",
        "MISCONFIGURED_SHARED_BUDGET",
        "MISCONFIGURED_STRATEGY_TYPE",
        "PAUSED",
        "UNAVAILABLE",
        "MULTIPLE_LEARNING",
        "MULTIPLE_LIMITED",
        "MULTIPLE_MISCONFIGURED",
        "MULTIPLE",
    ]
    biddingStrategyType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "COMMISSION",
        "ENHANCED_CPC",
        "INVALID",
        "MANUAL_CPA",
        "MANUAL_CPC",
        "MANUAL_CPM",
        "MANUAL_CPV",
        "MAXIMIZE_CONVERSIONS",
        "MAXIMIZE_CONVERSION_VALUE",
        "PAGE_ONE_PROMOTED",
        "PERCENT_CPC",
        "TARGET_CPA",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]
    campaignBudget: str
    createTime: str
    creationTime: str
    dynamicSearchAdsSetting: (
        GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSetting
    )
    effectiveLabels: _list[str]
    endDate: str
    engineId: str
    excludedParentAssetFieldTypes: _list[
        typing_extensions.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "HEADLINE",
            "DESCRIPTION",
            "MANDATORY_AD_TEXT",
            "MARKETING_IMAGE",
            "MEDIA_BUNDLE",
            "YOUTUBE_VIDEO",
            "BOOK_ON_GOOGLE",
            "LEAD_FORM",
            "PROMOTION",
            "CALLOUT",
            "STRUCTURED_SNIPPET",
            "SITELINK",
            "MOBILE_APP",
            "HOTEL_CALLOUT",
            "CALL",
            "PRICE",
            "LONG_HEADLINE",
            "BUSINESS_NAME",
            "SQUARE_MARKETING_IMAGE",
            "PORTRAIT_MARKETING_IMAGE",
            "LOGO",
            "LANDSCAPE_LOGO",
            "VIDEO",
            "CALL_TO_ACTION_SELECTION",
            "AD_IMAGE",
            "BUSINESS_LOGO",
            "HOTEL_PROPERTY",
            "DISCOVERY_CAROUSEL_CARD",
        ]
    ]
    finalUrlSuffix: str
    frequencyCaps: _list[GoogleAdsSearchads360V0Common__FrequencyCapEntry]
    geoTargetTypeSetting: GoogleAdsSearchads360V0Resources_Campaign_GeoTargetTypeSetting
    id: str
    labels: _list[str]
    lastModifiedTime: str
    manualCpa: GoogleAdsSearchads360V0Common__ManualCpa
    manualCpc: GoogleAdsSearchads360V0Common__ManualCpc
    manualCpm: GoogleAdsSearchads360V0Common__ManualCpm
    maximizeConversionValue: GoogleAdsSearchads360V0Common__MaximizeConversionValue
    maximizeConversions: GoogleAdsSearchads360V0Common__MaximizeConversions
    name: str
    networkSettings: GoogleAdsSearchads360V0Resources_Campaign_NetworkSettings
    optimizationGoalSetting: (
        GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSetting
    )
    percentCpc: GoogleAdsSearchads360V0Common__PercentCpc
    realTimeBiddingSetting: GoogleAdsSearchads360V0Common__RealTimeBiddingSetting
    resourceName: str
    selectiveOptimization: (
        GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimization
    )
    servingStatus: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "SERVING", "NONE", "ENDED", "PENDING", "SUSPENDED"
    ]
    shoppingSetting: GoogleAdsSearchads360V0Resources_Campaign_ShoppingSetting
    startDate: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]
    targetCpa: GoogleAdsSearchads360V0Common__TargetCpa
    targetCpm: GoogleAdsSearchads360V0Common__TargetCpm
    targetImpressionShare: GoogleAdsSearchads360V0Common__TargetImpressionShare
    targetRoas: GoogleAdsSearchads360V0Common__TargetRoas
    targetSpend: GoogleAdsSearchads360V0Common__TargetSpend
    trackingSetting: GoogleAdsSearchads360V0Resources_Campaign_TrackingSetting
    trackingUrlTemplate: str
    urlCustomParameters: _list[GoogleAdsSearchads360V0Common__CustomParameter]
    urlExpansionOptOut: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignAsset(
    typing_extensions.TypedDict, total=False
):
    asset: str
    campaign: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignAssetSet(
    typing_extensions.TypedDict, total=False
):
    assetSet: str
    campaign: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignAudienceView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignBudget(
    typing_extensions.TypedDict, total=False
):
    amountMicros: str
    deliveryMethod: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "STANDARD", "ACCELERATED"
    ]
    period: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "DAILY", "FIXED_DAILY", "CUSTOM_PERIOD"
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignCriterion(
    typing_extensions.TypedDict, total=False
):
    ageRange: GoogleAdsSearchads360V0Common__AgeRangeInfo
    bidModifier: float
    criterionId: str
    device: GoogleAdsSearchads360V0Common__DeviceInfo
    displayName: str
    gender: GoogleAdsSearchads360V0Common__GenderInfo
    keyword: GoogleAdsSearchads360V0Common__KeywordInfo
    language: GoogleAdsSearchads360V0Common__LanguageInfo
    lastModifiedTime: str
    location: GoogleAdsSearchads360V0Common__LocationInfo
    locationGroup: GoogleAdsSearchads360V0Common__LocationGroupInfo
    negative: bool
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "KEYWORD",
        "PLACEMENT",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "DEVICE",
        "LOCATION",
        "LISTING_GROUP",
        "AD_SCHEDULE",
        "AGE_RANGE",
        "GENDER",
        "INCOME_RANGE",
        "PARENTAL_STATUS",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "USER_LIST",
        "PROXIMITY",
        "TOPIC",
        "LISTING_SCOPE",
        "LANGUAGE",
        "IP_BLOCK",
        "CONTENT_LABEL",
        "CARRIER",
        "USER_INTEREST",
        "WEBPAGE",
        "OPERATING_SYSTEM_VERSION",
        "APP_PAYMENT_MODEL",
        "MOBILE_DEVICE",
        "CUSTOM_AFFINITY",
        "CUSTOM_INTENT",
        "LOCATION_GROUP",
        "CUSTOM_AUDIENCE",
        "COMBINED_AUDIENCE",
        "KEYWORD_THEME",
        "AUDIENCE",
        "LOCAL_SERVICE_ID",
        "BRAND",
        "BRAND_LIST",
        "LIFE_EVENT",
    ]
    userList: GoogleAdsSearchads360V0Common__UserListInfo
    webpage: GoogleAdsSearchads360V0Common__WebpageInfo

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignEffectiveLabel(
    typing_extensions.TypedDict, total=False
):
    campaign: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CampaignLabel(
    typing_extensions.TypedDict, total=False
):
    campaign: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CartDataSalesView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Conversion(
    typing_extensions.TypedDict, total=False
):
    adId: str
    advertiserConversionId: str
    assetFieldType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HEADLINE",
        "DESCRIPTION",
        "MANDATORY_AD_TEXT",
        "MARKETING_IMAGE",
        "MEDIA_BUNDLE",
        "YOUTUBE_VIDEO",
        "BOOK_ON_GOOGLE",
        "LEAD_FORM",
        "PROMOTION",
        "CALLOUT",
        "STRUCTURED_SNIPPET",
        "SITELINK",
        "MOBILE_APP",
        "HOTEL_CALLOUT",
        "CALL",
        "PRICE",
        "LONG_HEADLINE",
        "BUSINESS_NAME",
        "SQUARE_MARKETING_IMAGE",
        "PORTRAIT_MARKETING_IMAGE",
        "LOGO",
        "LANDSCAPE_LOGO",
        "VIDEO",
        "CALL_TO_ACTION_SELECTION",
        "AD_IMAGE",
        "BUSINESS_LOGO",
        "HOTEL_PROPERTY",
        "DISCOVERY_CAROUSEL_CARD",
    ]
    assetId: str
    attributionType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "VISIT", "CRITERION_AD"
    ]
    clickId: str
    conversionDateTime: str
    conversionLastModifiedDateTime: str
    conversionQuantity: str
    conversionRevenueMicros: str
    conversionVisitDateTime: str
    criterionId: str
    floodlightOrderId: str
    floodlightOriginalRevenue: str
    id: str
    merchantId: str
    productChannel: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"
    ]
    productCountryCode: str
    productId: str
    productLanguageCode: str
    productStoreId: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    visitId: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ConversionAction(
    typing_extensions.TypedDict, total=False
):
    appId: str
    attributionModelSettings: (
        GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettings
    )
    category: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DEFAULT",
        "PAGE_VIEW",
        "PURCHASE",
        "SIGNUP",
        "LEAD",
        "DOWNLOAD",
        "ADD_TO_CART",
        "BEGIN_CHECKOUT",
        "SUBSCRIBE_PAID",
        "PHONE_CALL_LEAD",
        "IMPORTED_LEAD",
        "SUBMIT_LEAD_FORM",
        "BOOK_APPOINTMENT",
        "REQUEST_QUOTE",
        "GET_DIRECTIONS",
        "OUTBOUND_CLICK",
        "CONTACT",
        "ENGAGEMENT",
        "STORE_VISIT",
        "STORE_SALE",
        "QUALIFIED_LEAD",
        "CONVERTED_LEAD",
    ]
    clickThroughLookbackWindowDays: str
    creationTime: str
    floodlightSettings: (
        GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettings
    )
    id: str
    includeInClientAccountConversionsMetric: bool
    includeInConversionsMetric: bool
    name: str
    ownerCustomer: str
    primaryForGoal: bool
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "HIDDEN"
    ]
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_CALL",
        "CLICK_TO_CALL",
        "GOOGLE_PLAY_DOWNLOAD",
        "GOOGLE_PLAY_IN_APP_PURCHASE",
        "UPLOAD_CALLS",
        "UPLOAD_CLICKS",
        "WEBPAGE",
        "WEBSITE_CALL",
        "STORE_SALES_DIRECT_UPLOAD",
        "STORE_SALES",
        "FIREBASE_ANDROID_FIRST_OPEN",
        "FIREBASE_ANDROID_IN_APP_PURCHASE",
        "FIREBASE_ANDROID_CUSTOM",
        "FIREBASE_IOS_FIRST_OPEN",
        "FIREBASE_IOS_IN_APP_PURCHASE",
        "FIREBASE_IOS_CUSTOM",
        "THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN",
        "THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE",
        "THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM",
        "THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN",
        "THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE",
        "THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM",
        "ANDROID_APP_PRE_REGISTRATION",
        "ANDROID_INSTALLS_ALL_OTHER_APPS",
        "FLOODLIGHT_ACTION",
        "FLOODLIGHT_TRANSACTION",
        "GOOGLE_HOSTED",
        "LEAD_FORM_SUBMIT",
        "SALESFORCE",
        "SEARCH_ADS_360",
        "SMART_CAMPAIGN_AD_CLICKS_TO_CALL",
        "SMART_CAMPAIGN_MAP_CLICKS_TO_CALL",
        "SMART_CAMPAIGN_MAP_DIRECTIONS",
        "SMART_CAMPAIGN_TRACKED_CALLS",
        "STORE_VISITS",
        "WEBPAGE_CODELESS",
        "UNIVERSAL_ANALYTICS_GOAL",
        "UNIVERSAL_ANALYTICS_TRANSACTION",
        "GOOGLE_ANALYTICS_4_CUSTOM",
        "GOOGLE_ANALYTICS_4_PURCHASE",
    ]
    valueSettings: GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettings

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ConversionCustomVariable(
    typing_extensions.TypedDict, total=False
):
    cardinality: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BELOW_ALL_LIMITS",
        "EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT",
        "APPROACHES_STATS_LIMIT",
        "EXCEEDS_STATS_LIMIT",
    ]
    customColumnIds: _list[str]
    family: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "STANDARD", "FLOODLIGHT"
    ]
    floodlightConversionCustomVariableInfo: GoogleAdsSearchads360V0Resources_ConversionCustomVariable_FloodlightConversionCustomVariableInfo
    id: str
    name: str
    ownerCustomer: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACTIVATION_NEEDED", "ENABLED", "PAUSED"
    ]
    tag: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ConversionTrackingSetting(
    typing_extensions.TypedDict, total=False
):
    acceptedCustomerDataTerms: bool
    conversionTrackingId: str
    conversionTrackingStatus: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NOT_CONVERSION_TRACKED",
        "CONVERSION_TRACKING_MANAGED_BY_SELF",
        "CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER",
        "CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER",
    ]
    crossAccountConversionTrackingId: str
    enhancedConversionsForLeadsEnabled: bool
    googleAdsConversionCustomer: str
    googleAdsCrossAccountConversionTrackingId: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CustomColumn(
    typing_extensions.TypedDict, total=False
):
    description: str
    id: str
    name: str
    queryable: bool
    referencedSystemColumns: _list[str]
    referencesAttributes: bool
    referencesMetrics: bool
    renderType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NUMBER",
        "PERCENT",
        "MONEY",
        "STRING",
        "BOOLEAN",
        "DATE",
    ]
    resourceName: str
    valueType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "STRING", "INT64", "DOUBLE", "BOOLEAN", "DATE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Customer(
    typing_extensions.TypedDict, total=False
):
    accountStatus: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "SUSPENDED", "REMOVED", "DRAFT"
    ]
    accountType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BAIDU",
        "ENGINE_TRACK",
        "FACEBOOK",
        "FACEBOOK_GATEWAY",
        "GOOGLE_ADS",
        "MICROSOFT",
        "SEARCH_ADS_360",
        "YAHOO_JAPAN",
    ]
    autoTaggingEnabled: bool
    conversionTrackingSetting: (
        GoogleAdsSearchads360V0Resources__ConversionTrackingSetting
    )
    creationTime: str
    currencyCode: str
    descriptiveName: str
    doubleClickCampaignManagerSetting: (
        GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSetting
    )
    engineId: str
    finalUrlSuffix: str
    id: str
    lastModifiedTime: str
    manager: bool
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "CANCELED", "SUSPENDED", "CLOSED"
    ]
    timeZone: str
    trackingUrlTemplate: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CustomerAsset(
    typing_extensions.TypedDict, total=False
):
    asset: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CustomerAssetSet(
    typing_extensions.TypedDict, total=False
):
    assetSet: str
    customer: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CustomerClient(
    typing_extensions.TypedDict, total=False
):
    appliedLabels: _list[str]
    clientCustomer: str
    currencyCode: str
    descriptiveName: str
    hidden: bool
    id: str
    level: str
    manager: bool
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "CANCELED", "SUSPENDED", "CLOSED"
    ]
    testAccount: bool
    timeZone: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CustomerManagerLink(
    typing_extensions.TypedDict, total=False
):
    managerCustomer: str
    managerLinkId: str
    resourceName: str
    startTime: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACTIVE", "INACTIVE", "PENDING", "REFUSED", "CANCELED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSetting(
    typing_extensions.TypedDict, total=False
):
    advertiserId: str
    networkId: str
    timeZone: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermView(
    typing_extensions.TypedDict, total=False
):
    landingPage: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__GenderView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__GeoTargetConstant(
    typing_extensions.TypedDict, total=False
):
    canonicalName: str
    countryCode: str
    id: str
    name: str
    parentGeoTarget: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVAL_PLANNED"
    ]
    targetType: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__KeywordView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Label(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    textLabel: GoogleAdsSearchads360V0Common__TextLabel

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__LanguageConstant(
    typing_extensions.TypedDict, total=False
):
    code: str
    id: str
    name: str
    resourceName: str
    targetable: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ListingGroupFilterDimension(
    typing_extensions.TypedDict, total=False
):
    productBiddingCategory: GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductBiddingCategory
    productBrand: (
        GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductBrand
    )
    productChannel: (
        GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductChannel
    )
    productCondition: (
        GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductCondition
    )
    productCustomAttribute: GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductCustomAttribute
    productItemId: (
        GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductItemId
    )
    productType: (
        GoogleAdsSearchads360V0Resources_ListingGroupFilterDimension_ProductType
    )

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ListingGroupFilterDimensionPath(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GoogleAdsSearchads360V0Resources__ListingGroupFilterDimension]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__LocationView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ProductBiddingCategoryConstant(
    typing_extensions.TypedDict, total=False
):
    countryCode: str
    id: str
    languageCode: str
    level: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]
    localizedName: str
    productBiddingCategoryConstantParent: str
    resourceName: str
    status: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ACTIVE", "OBSOLETE"]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ProductGroupView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__SearchAds360Field(
    typing_extensions.TypedDict, total=False
):
    attributeResources: _list[str]
    category: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "RESOURCE", "ATTRIBUTE", "SEGMENT", "METRIC"
    ]
    dataType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BOOLEAN",
        "DATE",
        "DOUBLE",
        "ENUM",
        "FLOAT",
        "INT32",
        "INT64",
        "MESSAGE",
        "RESOURCE_NAME",
        "STRING",
        "UINT64",
    ]
    enumValues: _list[str]
    filterable: bool
    isRepeated: bool
    metrics: _list[str]
    name: str
    resourceName: str
    segments: _list[str]
    selectable: bool
    selectableWith: _list[str]
    sortable: bool
    typeUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ShoppingPerformanceView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__UserList(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str
    resourceName: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REMARKETING",
        "LOGICAL",
        "EXTERNAL_REMARKETING",
        "RULE_BASED",
        "SIMILAR",
        "CRM_BASED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__UserLocationView(
    typing_extensions.TypedDict, total=False
):
    countryCriterionId: str
    resourceName: str
    targetingLocation: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__Visit(typing_extensions.TypedDict, total=False):
    adId: str
    assetFieldType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HEADLINE",
        "DESCRIPTION",
        "MANDATORY_AD_TEXT",
        "MARKETING_IMAGE",
        "MEDIA_BUNDLE",
        "YOUTUBE_VIDEO",
        "BOOK_ON_GOOGLE",
        "LEAD_FORM",
        "PROMOTION",
        "CALLOUT",
        "STRUCTURED_SNIPPET",
        "SITELINK",
        "MOBILE_APP",
        "HOTEL_CALLOUT",
        "CALL",
        "PRICE",
        "LONG_HEADLINE",
        "BUSINESS_NAME",
        "SQUARE_MARKETING_IMAGE",
        "PORTRAIT_MARKETING_IMAGE",
        "LOGO",
        "LANDSCAPE_LOGO",
        "VIDEO",
        "CALL_TO_ACTION_SELECTION",
        "AD_IMAGE",
        "BUSINESS_LOGO",
        "HOTEL_PROPERTY",
        "DISCOVERY_CAROUSEL_CARD",
    ]
    assetId: str
    clickId: str
    criterionId: str
    id: str
    merchantId: str
    productChannel: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"
    ]
    productCountryCode: str
    productId: str
    productLanguageCode: str
    productStoreId: str
    resourceName: str
    visitDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__WebpageView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ConversionCustomDimensionHeader(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ConversionCustomMetricHeader(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__CustomColumnHeader(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str
    referencesMetrics: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponse(
    typing_extensions.TypedDict, total=False
):
    resourceNames: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ListCustomColumnsResponse(
    typing_extensions.TypedDict, total=False
):
    customColumns: _list[GoogleAdsSearchads360V0Resources__CustomColumn]

@typing.type_check_only
class GoogleAdsSearchads360V0Services__RawEventConversionDimensionHeader(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__RawEventConversionMetricHeader(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchAds360Row(
    typing_extensions.TypedDict, total=False
):
    accessibleBiddingStrategy: (
        GoogleAdsSearchads360V0Resources__AccessibleBiddingStrategy
    )
    adGroup: GoogleAdsSearchads360V0Resources__AdGroup
    adGroupAd: GoogleAdsSearchads360V0Resources__AdGroupAd
    adGroupAdEffectiveLabel: GoogleAdsSearchads360V0Resources__AdGroupAdEffectiveLabel
    adGroupAdLabel: GoogleAdsSearchads360V0Resources__AdGroupAdLabel
    adGroupAsset: GoogleAdsSearchads360V0Resources__AdGroupAsset
    adGroupAssetSet: GoogleAdsSearchads360V0Resources__AdGroupAssetSet
    adGroupAudienceView: GoogleAdsSearchads360V0Resources__AdGroupAudienceView
    adGroupBidModifier: GoogleAdsSearchads360V0Resources__AdGroupBidModifier
    adGroupCriterion: GoogleAdsSearchads360V0Resources__AdGroupCriterion
    adGroupCriterionEffectiveLabel: (
        GoogleAdsSearchads360V0Resources__AdGroupCriterionEffectiveLabel
    )
    adGroupCriterionLabel: GoogleAdsSearchads360V0Resources__AdGroupCriterionLabel
    adGroupEffectiveLabel: GoogleAdsSearchads360V0Resources__AdGroupEffectiveLabel
    adGroupLabel: GoogleAdsSearchads360V0Resources__AdGroupLabel
    ageRangeView: GoogleAdsSearchads360V0Resources__AgeRangeView
    asset: GoogleAdsSearchads360V0Resources__Asset
    assetGroup: GoogleAdsSearchads360V0Resources__AssetGroup
    assetGroupAsset: GoogleAdsSearchads360V0Resources__AssetGroupAsset
    assetGroupListingGroupFilter: (
        GoogleAdsSearchads360V0Resources__AssetGroupListingGroupFilter
    )
    assetGroupSignal: GoogleAdsSearchads360V0Resources__AssetGroupSignal
    assetGroupTopCombinationView: (
        GoogleAdsSearchads360V0Resources__AssetGroupTopCombinationView
    )
    assetSet: GoogleAdsSearchads360V0Resources__AssetSet
    assetSetAsset: GoogleAdsSearchads360V0Resources__AssetSetAsset
    audience: GoogleAdsSearchads360V0Resources__Audience
    biddingStrategy: GoogleAdsSearchads360V0Resources__BiddingStrategy
    campaign: GoogleAdsSearchads360V0Resources__Campaign
    campaignAsset: GoogleAdsSearchads360V0Resources__CampaignAsset
    campaignAssetSet: GoogleAdsSearchads360V0Resources__CampaignAssetSet
    campaignAudienceView: GoogleAdsSearchads360V0Resources__CampaignAudienceView
    campaignBudget: GoogleAdsSearchads360V0Resources__CampaignBudget
    campaignCriterion: GoogleAdsSearchads360V0Resources__CampaignCriterion
    campaignEffectiveLabel: GoogleAdsSearchads360V0Resources__CampaignEffectiveLabel
    campaignLabel: GoogleAdsSearchads360V0Resources__CampaignLabel
    cartDataSalesView: GoogleAdsSearchads360V0Resources__CartDataSalesView
    conversion: GoogleAdsSearchads360V0Resources__Conversion
    conversionAction: GoogleAdsSearchads360V0Resources__ConversionAction
    conversionCustomVariable: GoogleAdsSearchads360V0Resources__ConversionCustomVariable
    customColumns: _list[GoogleAdsSearchads360V0Common__Value]
    customer: GoogleAdsSearchads360V0Resources__Customer
    customerAsset: GoogleAdsSearchads360V0Resources__CustomerAsset
    customerAssetSet: GoogleAdsSearchads360V0Resources__CustomerAssetSet
    customerClient: GoogleAdsSearchads360V0Resources__CustomerClient
    customerManagerLink: GoogleAdsSearchads360V0Resources__CustomerManagerLink
    dynamicSearchAdsSearchTermView: (
        GoogleAdsSearchads360V0Resources__DynamicSearchAdsSearchTermView
    )
    genderView: GoogleAdsSearchads360V0Resources__GenderView
    geoTargetConstant: GoogleAdsSearchads360V0Resources__GeoTargetConstant
    keywordView: GoogleAdsSearchads360V0Resources__KeywordView
    label: GoogleAdsSearchads360V0Resources__Label
    languageConstant: GoogleAdsSearchads360V0Resources__LanguageConstant
    locationView: GoogleAdsSearchads360V0Resources__LocationView
    metrics: GoogleAdsSearchads360V0Common__Metrics
    productBiddingCategoryConstant: (
        GoogleAdsSearchads360V0Resources__ProductBiddingCategoryConstant
    )
    productGroupView: GoogleAdsSearchads360V0Resources__ProductGroupView
    segments: GoogleAdsSearchads360V0Common__Segments
    shoppingPerformanceView: GoogleAdsSearchads360V0Resources__ShoppingPerformanceView
    userList: GoogleAdsSearchads360V0Resources__UserList
    userLocationView: GoogleAdsSearchads360V0Resources__UserLocationView
    visit: GoogleAdsSearchads360V0Resources__Visit
    webpageView: GoogleAdsSearchads360V0Resources__WebpageView

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    results: _list[GoogleAdsSearchads360V0Resources__SearchAds360Field]
    totalResultsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360Request(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    query: str
    returnTotalResultsCount: bool
    summaryRowSetting: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_SUMMARY_ROW",
        "SUMMARY_ROW_WITH_RESULTS",
        "SUMMARY_ROW_ONLY",
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360Response(
    typing_extensions.TypedDict, total=False
):
    conversionCustomDimensionHeaders: _list[
        GoogleAdsSearchads360V0Services__ConversionCustomDimensionHeader
    ]
    conversionCustomMetricHeaders: _list[
        GoogleAdsSearchads360V0Services__ConversionCustomMetricHeader
    ]
    customColumnHeaders: _list[GoogleAdsSearchads360V0Services__CustomColumnHeader]
    fieldMask: str
    nextPageToken: str
    rawEventConversionDimensionHeaders: _list[
        GoogleAdsSearchads360V0Services__RawEventConversionDimensionHeader
    ]
    rawEventConversionMetricHeaders: _list[
        GoogleAdsSearchads360V0Services__RawEventConversionMetricHeader
    ]
    results: _list[GoogleAdsSearchads360V0Services__SearchAds360Row]
    summaryRow: GoogleAdsSearchads360V0Services__SearchAds360Row
    totalResultsCount: str
