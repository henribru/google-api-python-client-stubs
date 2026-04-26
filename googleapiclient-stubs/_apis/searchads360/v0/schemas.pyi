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
        "DESCRIPTION_PREFIX",
        "HEADLINE_AS_SITELINK_POSITION_ONE",
        "HEADLINE_AS_SITELINK_POSITION_TWO",
        "DESCRIPTION_LINE_HEADLINE_AS_SITELINK_POSITION_ONE",
        "DESCRIPTION_LINE_HEADLINE_AS_SITELINK_POSITION_TWO",
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
class GoogleAdsSearchads360V0Common__FinalAppUrl(
    typing_extensions.TypedDict, total=False
):
    osType: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "IOS", "ANDROID"]
    url: str

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
    averageCartSize: float
    averageCost: float
    averageCpc: float
    averageCpm: float
    averageImpressionFrequencyPerUser: float
    averageOrderValueMicros: str
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
    costOfGoodsSoldMicros: str
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
    grossProfitMargin: float
    grossProfitMicros: str
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
    orders: float
    rawEventConversionMetrics: _list[GoogleAdsSearchads360V0Common__Value]
    revenueMicros: str
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
    uniqueUsers: str
    unitsSold: float
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
    adFormatType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "VERTICAL_ADS_PROMOTION",
        "VERTICAL_ADS_BOOKING_LINK",
        "TEXT",
    ]
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
    geoTargetPostalCode: str
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
    verticalAdsEventParticipantDisplayNames: str
    verticalAdsHotelClass: str
    verticalAdsListing: str
    verticalAdsListingBrand: str
    verticalAdsListingCity: str
    verticalAdsListingCountry: str
    verticalAdsListingRegion: str
    verticalAdsPartnerAccount: str
    verticalAdsVertical: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HOTELS",
        "VACATION_RENTALS",
        "RENTAL_CARS",
        "EVENTS",
        "THINGS_TO_DO",
        "FLIGHTS",
    ]
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
    conversionCustomVariableError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_NAME",
        "DUPLICATE_TAG",
        "RESERVED_TAG",
        "NOT_FOUND",
        "NOT_AVAILABLE",
        "INCOMPATIBLE_TYPE",
        "INVALID_METRIC",
        "EXCEEDS_CARDINALITY_LIMIT",
        "INVALID_DIMENSION",
        "INCOMPATIBLE_WITH_SELECTED_RESOURCE",
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
        "REQUIRED_SEGMENT_FIELD_MISSING",
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
    finalAppUrls: _list[GoogleAdsSearchads360V0Common__FinalAppUrl]
    finalMobileUrls: _list[str]
    finalUrlSuffix: str
    finalUrls: _list[str]
    id: str
    name: str
    productAd: GoogleAdsSearchads360V0Common__SearchAds360ProductAdInfo
    resourceName: str
    responsiveSearchAd: (
        GoogleAdsSearchads360V0Common__SearchAds360ResponsiveSearchAdInfo
    )
    textAd: GoogleAdsSearchads360V0Common__SearchAds360TextAdInfo
    trackingUrlTemplate: str
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
        "TRAVEL_AD",
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
    finalUrlSuffix: str
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
    trackingUrlTemplate: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH_STANDARD",
        "DISPLAY_STANDARD",
        "SHOPPING_PRODUCT_ADS",
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
    finalMobileUrls: _list[str]
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
    urlCustomParameters: _list[GoogleAdsSearchads360V0Common__CustomParameter]
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
    finalMobileUrls: _list[str]
    finalUrlSuffix: str
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
    urlCustomParameters: _list[GoogleAdsSearchads360V0Common__CustomParameter]
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
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
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
            "LONG_DESCRIPTION",
            "CALL_TO_ACTION",
        ]
    ]
    feedTypes: _list[
        typing_extensions.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "PAGE_FEED",
            "DYNAMIC_EDUCATION",
            "MERCHANT_CENTER_FEED",
            "DYNAMIC_REAL_ESTATE",
            "DYNAMIC_CUSTOM",
            "DYNAMIC_HOTELS_AND_RENTALS",
            "DYNAMIC_FLIGHTS",
            "DYNAMIC_TRAVEL",
            "DYNAMIC_LOCAL",
            "DYNAMIC_JOBS",
            "LOCATION_SYNC",
            "BUSINESS_PROFILE_DYNAMIC_LOCATION_GROUP",
            "CHAIN_DYNAMIC_LOCATION_GROUP",
            "STATIC_LOCATION_GROUP",
            "HOTEL_PROPERTY",
            "TRAVEL_FEED",
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
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
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
    accountLevel: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CLIENT_ACCOUNT_FACEBOOK",
        "CLIENT_ACCOUNT_GOOGLE_ADS",
        "CLIENT_ACCOUNT_MICROSOFT",
        "CLIENT_ACCOUNT_YAHOO_JAPAN",
        "CLIENT_ACCOUNT_ENGINE_TRACK",
        "MANAGER",
        "SUB_MANAGER",
        "ASSOCIATE_MANAGER",
    ]
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
    associateManagerDescriptiveName: str
    associateManagerId: str
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
    managerDescriptiveName: str
    managerId: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "CANCELED", "SUSPENDED", "CLOSED"
    ]
    subManagerDescriptiveName: str
    subManagerId: str
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
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
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

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraint(
    typing_extensions.TypedDict, total=False
):
    countryCriterion: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraintList(
    typing_extensions.TypedDict, total=False
):
    countries: _list[
        GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraint
    ]
    totalTargetedCountries: int

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicConstraint_ResellerConstraint(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationMismatch(
    typing_extensions.TypedDict, total=False
):
    urlTypes: _list[
        typing_extensions.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "DISPLAY_URL",
            "FINAL_URL",
            "FINAL_MOBILE_URL",
            "TRACKING_URL",
            "MOBILE_TRACKING_URL",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationNotWorking(
    typing_extensions.TypedDict, total=False
):
    device: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "DESKTOP", "ANDROID", "IOS"
    ]
    dnsErrorType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "HOSTNAME_NOT_FOUND", "GOOGLE_CRAWLER_DNS_ISSUE"
    ]
    expandedUrl: str
    httpErrorCode: str
    lastCheckedDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationTextList(
    typing_extensions.TypedDict, total=False
):
    destinationTexts: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_TextList(
    typing_extensions.TypedDict, total=False
):
    texts: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_WebsiteList(
    typing_extensions.TypedDict, total=False
):
    websites: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicyTopicConstraint(
    typing_extensions.TypedDict, total=False
):
    certificateDomainMismatchInCountryList: (
        GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraintList
    )
    certificateMissingInCountryList: (
        GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraintList
    )
    countryConstraintList: (
        GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraintList
    )
    resellerConstraint: (
        GoogleAdsSearchads360V23Common_PolicyTopicConstraint_ResellerConstraint
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicyTopicEntry(
    typing_extensions.TypedDict, total=False
):
    constraints: _list[GoogleAdsSearchads360V23Common__PolicyTopicConstraint]
    evidences: _list[GoogleAdsSearchads360V23Common__PolicyTopicEvidence]
    topic: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PROHIBITED",
        "LIMITED",
        "FULLY_LIMITED",
        "DESCRIPTIVE",
        "BROADENING",
        "AREA_OF_INTEREST_ONLY",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicyTopicEvidence(
    typing_extensions.TypedDict, total=False
):
    destinationMismatch: (
        GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationMismatch
    )
    destinationNotWorking: (
        GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationNotWorking
    )
    destinationTextList: (
        GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationTextList
    )
    languageCode: str
    textList: GoogleAdsSearchads360V23Common_PolicyTopicEvidence_TextList
    websiteList: GoogleAdsSearchads360V23Common_PolicyTopicEvidence_WebsiteList

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicyViolationKey(
    typing_extensions.TypedDict, total=False
):
    policyName: str
    violatingText: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Value(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    doubleValue: float
    floatValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors_ErrorLocation_FieldPathElement(
    typing_extensions.TypedDict, total=False
):
    fieldName: str
    index: int

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__BudgetPerDayMinimumErrorDetails(
    typing_extensions.TypedDict, total=False
):
    budgetPerDayMinimumMicros: str
    currencyCode: str
    failedBudgetAmountMicros: str
    failedBudgetTotalAmountMicros: str
    minimumBudgetAmountMicros: str
    minimumBudgetTotalAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ErrorCode(
    typing_extensions.TypedDict, total=False
):
    accessInvitationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_EMAIL_ADDRESS",
        "EMAIL_ADDRESS_ALREADY_HAS_ACCESS",
        "INVALID_INVITATION_STATUS",
        "GOOGLE_CONSUMER_ACCOUNT_NOT_ALLOWED",
        "INVALID_INVITATION_ID",
        "EMAIL_ADDRESS_ALREADY_HAS_PENDING_INVITATION",
        "PENDING_INVITATIONS_LIMIT_EXCEEDED",
        "EMAIL_DOMAIN_POLICY_VIOLATED",
    ]
    accountBudgetProposalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FIELD_MASK_NOT_ALLOWED",
        "IMMUTABLE_FIELD",
        "REQUIRED_FIELD_MISSING",
        "CANNOT_CANCEL_APPROVED_PROPOSAL",
        "CANNOT_REMOVE_UNAPPROVED_BUDGET",
        "CANNOT_REMOVE_RUNNING_BUDGET",
        "CANNOT_END_UNAPPROVED_BUDGET",
        "CANNOT_END_INACTIVE_BUDGET",
        "BUDGET_NAME_REQUIRED",
        "CANNOT_UPDATE_OLD_BUDGET",
        "CANNOT_END_IN_PAST",
        "CANNOT_EXTEND_END_TIME",
        "PURCHASE_ORDER_NUMBER_REQUIRED",
        "PENDING_UPDATE_PROPOSAL_EXISTS",
        "MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP",
        "CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET",
        "SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED",
        "UPDATE_IS_NO_OP",
        "END_TIME_MUST_FOLLOW_START_TIME",
        "BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP",
        "NOT_AUTHORIZED",
        "INVALID_BILLING_SETUP",
        "OVERLAPS_EXISTING_BUDGET",
        "CANNOT_CREATE_BUDGET_THROUGH_API",
        "INVALID_MASTER_SERVICE_AGREEMENT",
        "CANCELED_BILLING_SETUP",
    ]
    accountLinkError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_STATUS", "PERMISSION_DENIED"
    ]
    adCustomizerError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "COUNTDOWN_INVALID_DATE_FORMAT",
        "COUNTDOWN_DATE_IN_PAST",
        "COUNTDOWN_INVALID_LOCALE",
        "COUNTDOWN_INVALID_START_DAYS_BEFORE",
        "UNKNOWN_USER_LIST",
    ]
    adError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_CUSTOMIZERS_NOT_SUPPORTED_FOR_AD_TYPE",
        "APPROXIMATELY_TOO_LONG",
        "APPROXIMATELY_TOO_SHORT",
        "BAD_SNIPPET",
        "CANNOT_MODIFY_AD",
        "CANNOT_SET_BUSINESS_NAME_IF_URL_SET",
        "CANNOT_SET_FIELD",
        "CANNOT_SET_FIELD_WITH_ORIGIN_AD_ID_SET",
        "CANNOT_SET_FIELD_WITH_AD_ID_SET_FOR_SHARING",
        "CANNOT_SET_ALLOW_FLEXIBLE_COLOR_FALSE",
        "CANNOT_SET_COLOR_CONTROL_WHEN_NATIVE_FORMAT_SETTING",
        "CANNOT_SET_URL",
        "CANNOT_SET_WITHOUT_FINAL_URLS",
        "CANNOT_SET_WITH_FINAL_URLS",
        "CANNOT_SET_WITH_URL_DATA",
        "CANNOT_USE_AD_SUBCLASS_FOR_OPERATOR",
        "CUSTOMER_NOT_APPROVED_MOBILEADS",
        "CUSTOMER_NOT_APPROVED_THIRDPARTY_ADS",
        "CUSTOMER_NOT_APPROVED_THIRDPARTY_REDIRECT_ADS",
        "CUSTOMER_NOT_ELIGIBLE",
        "CUSTOMER_NOT_ELIGIBLE_FOR_UPDATING_BEACON_URL",
        "DIMENSION_ALREADY_IN_UNION",
        "DIMENSION_MUST_BE_SET",
        "DIMENSION_NOT_IN_UNION",
        "DISPLAY_URL_CANNOT_BE_SPECIFIED",
        "DOMESTIC_PHONE_NUMBER_FORMAT",
        "EMERGENCY_PHONE_NUMBER",
        "EMPTY_FIELD",
        "FEED_ATTRIBUTE_MUST_HAVE_MAPPING_FOR_TYPE_ID",
        "FEED_ATTRIBUTE_MAPPING_TYPE_MISMATCH",
        "ILLEGAL_AD_CUSTOMIZER_TAG_USE",
        "ILLEGAL_TAG_USE",
        "INCONSISTENT_DIMENSIONS",
        "INCONSISTENT_STATUS_IN_TEMPLATE_UNION",
        "INCORRECT_LENGTH",
        "INELIGIBLE_FOR_UPGRADE",
        "INVALID_AD_ADDRESS_CAMPAIGN_TARGET",
        "INVALID_AD_TYPE",
        "INVALID_ATTRIBUTES_FOR_MOBILE_IMAGE",
        "INVALID_ATTRIBUTES_FOR_MOBILE_TEXT",
        "INVALID_CALL_TO_ACTION_TEXT",
        "INVALID_CHARACTER_FOR_URL",
        "INVALID_COUNTRY_CODE",
        "INVALID_EXPANDED_DYNAMIC_SEARCH_AD_TAG",
        "INVALID_INPUT",
        "INVALID_MARKUP_LANGUAGE",
        "INVALID_MOBILE_CARRIER",
        "INVALID_MOBILE_CARRIER_TARGET",
        "INVALID_NUMBER_OF_ELEMENTS",
        "INVALID_PHONE_NUMBER_FORMAT",
        "INVALID_RICH_MEDIA_CERTIFIED_VENDOR_FORMAT_ID",
        "INVALID_TEMPLATE_DATA",
        "INVALID_TEMPLATE_ELEMENT_FIELD_TYPE",
        "INVALID_TEMPLATE_ID",
        "LINE_TOO_WIDE",
        "MISSING_AD_CUSTOMIZER_MAPPING",
        "MISSING_ADDRESS_COMPONENT",
        "MISSING_ADVERTISEMENT_NAME",
        "MISSING_BUSINESS_NAME",
        "MISSING_DESCRIPTION1",
        "MISSING_DESCRIPTION2",
        "MISSING_DESTINATION_URL_TAG",
        "MISSING_LANDING_PAGE_URL_TAG",
        "MISSING_DIMENSION",
        "MISSING_DISPLAY_URL",
        "MISSING_HEADLINE",
        "MISSING_HEIGHT",
        "MISSING_IMAGE",
        "MISSING_MARKETING_IMAGE_OR_PRODUCT_VIDEOS",
        "MISSING_MARKUP_LANGUAGES",
        "MISSING_MOBILE_CARRIER",
        "MISSING_PHONE",
        "MISSING_REQUIRED_TEMPLATE_FIELDS",
        "MISSING_TEMPLATE_FIELD_VALUE",
        "MISSING_TEXT",
        "MISSING_VISIBLE_URL",
        "MISSING_WIDTH",
        "MULTIPLE_DISTINCT_FEEDS_UNSUPPORTED",
        "MUST_USE_TEMP_AD_UNION_ID_ON_ADD",
        "TOO_LONG",
        "TOO_SHORT",
        "UNION_DIMENSIONS_CANNOT_CHANGE",
        "UNKNOWN_ADDRESS_COMPONENT",
        "UNKNOWN_FIELD_NAME",
        "UNKNOWN_UNIQUE_NAME",
        "UNSUPPORTED_DIMENSIONS",
        "URL_INVALID_SCHEME",
        "URL_INVALID_TOP_LEVEL_DOMAIN",
        "URL_MALFORMED",
        "URL_NO_HOST",
        "URL_NOT_EQUIVALENT",
        "URL_HOST_NAME_TOO_LONG",
        "URL_NO_SCHEME",
        "URL_NO_TOP_LEVEL_DOMAIN",
        "URL_PATH_NOT_ALLOWED",
        "URL_PORT_NOT_ALLOWED",
        "URL_QUERY_NOT_ALLOWED",
        "URL_SCHEME_BEFORE_EXPANDED_DYNAMIC_SEARCH_AD_TAG",
        "USER_DOES_NOT_HAVE_ACCESS_TO_TEMPLATE",
        "INCONSISTENT_EXPANDABLE_SETTINGS",
        "INVALID_FORMAT",
        "INVALID_FIELD_TEXT",
        "ELEMENT_NOT_PRESENT",
        "IMAGE_ERROR",
        "VALUE_NOT_IN_RANGE",
        "FIELD_NOT_PRESENT",
        "ADDRESS_NOT_COMPLETE",
        "ADDRESS_INVALID",
        "VIDEO_RETRIEVAL_ERROR",
        "AUDIO_ERROR",
        "INVALID_YOUTUBE_DISPLAY_URL",
        "TOO_MANY_PRODUCT_IMAGES",
        "TOO_MANY_PRODUCT_VIDEOS",
        "INCOMPATIBLE_AD_TYPE_AND_DEVICE_PREFERENCE",
        "CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY",
        "CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED",
        "DISALLOWED_NUMBER_TYPE",
        "PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY",
        "PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY",
        "PREMIUM_RATE_NUMBER_NOT_ALLOWED",
        "VANITY_PHONE_NUMBER_NOT_ALLOWED",
        "INVALID_CALL_CONVERSION_TYPE_ID",
        "CANNOT_DISABLE_CALL_CONVERSION_AND_SET_CONVERSION_TYPE_ID",
        "CANNOT_SET_PATH2_WITHOUT_PATH1",
        "MISSING_DYNAMIC_SEARCH_ADS_SETTING_DOMAIN_NAME",
        "INCOMPATIBLE_WITH_RESTRICTION_TYPE",
        "CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED",
        "MISSING_IMAGE_OR_MEDIA_BUNDLE",
        "PRODUCT_TYPE_NOT_SUPPORTED_IN_THIS_CAMPAIGN",
        "PLACEHOLDER_CANNOT_HAVE_EMPTY_DEFAULT_VALUE",
        "PLACEHOLDER_COUNTDOWN_FUNCTION_CANNOT_HAVE_DEFAULT_VALUE",
        "PLACEHOLDER_DEFAULT_VALUE_MISSING",
        "UNEXPECTED_PLACEHOLDER_DEFAULT_VALUE",
        "AD_CUSTOMIZERS_MAY_NOT_BE_ADJACENT",
        "UPDATING_AD_WITH_NO_ENABLED_ASSOCIATION",
        "CALL_AD_VERIFICATION_URL_FINAL_URL_DOES_NOT_HAVE_SAME_DOMAIN",
        "CALL_AD_FINAL_URL_AND_VERIFICATION_URL_CANNOT_BOTH_BE_EMPTY",
        "TOO_MANY_AD_CUSTOMIZERS",
        "INVALID_AD_CUSTOMIZER_FORMAT",
        "NESTED_AD_CUSTOMIZER_SYNTAX",
        "UNSUPPORTED_AD_CUSTOMIZER_SYNTAX",
        "UNPAIRED_BRACE_IN_AD_CUSTOMIZER_TAG",
        "MORE_THAN_ONE_COUNTDOWN_TAG_TYPE_EXISTS",
        "DATE_TIME_IN_COUNTDOWN_TAG_IS_INVALID",
        "DATE_TIME_IN_COUNTDOWN_TAG_IS_PAST",
        "UNRECOGNIZED_AD_CUSTOMIZER_TAG_FOUND",
        "CUSTOMIZER_TYPE_FORBIDDEN_FOR_FIELD",
        "INVALID_CUSTOMIZER_ATTRIBUTE_NAME",
        "STORE_MISMATCH",
        "MISSING_REQUIRED_IMAGE_ASPECT_RATIO",
        "MISMATCHED_ASPECT_RATIOS",
        "DUPLICATE_IMAGE_ACROSS_CAROUSEL_CARDS",
        "INVALID_YOUTUBE_VIDEO_ASSET_ID_FOR_VIDEO_ADS_SEQUENCING",
    ]
    adGroupAdError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_AD_LABEL_DOES_NOT_EXIST",
        "AD_GROUP_AD_LABEL_ALREADY_EXISTS",
        "AD_NOT_UNDER_ADGROUP",
        "CANNOT_OPERATE_ON_REMOVED_ADGROUPAD",
        "CANNOT_CREATE_DEPRECATED_ADS",
        "CANNOT_CREATE_TEXT_ADS",
        "EMPTY_FIELD",
        "RESOURCE_REFERENCED_IN_MULTIPLE_OPS",
        "AD_TYPE_CANNOT_BE_PAUSED",
        "AD_TYPE_CANNOT_BE_REMOVED",
        "CANNOT_UPDATE_DEPRECATED_ADS",
        "AD_SHARING_NOT_ALLOWED",
    ]
    adGroupBidModifierError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CRITERION_ID_NOT_SUPPORTED",
        "CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER",
    ]
    adGroupCriterionCustomizerError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "CRITERION_IS_NOT_KEYWORD"
    ]
    adGroupCriterionError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_CRITERION_LABEL_DOES_NOT_EXIST",
        "AD_GROUP_CRITERION_LABEL_ALREADY_EXISTS",
        "CANNOT_ADD_LABEL_TO_NEGATIVE_CRITERION",
        "TOO_MANY_OPERATIONS",
        "CANT_UPDATE_NEGATIVE",
        "CONCRETE_TYPE_REQUIRED",
        "BID_INCOMPATIBLE_WITH_ADGROUP",
        "CANNOT_TARGET_AND_EXCLUDE",
        "ILLEGAL_URL",
        "INVALID_KEYWORD_TEXT",
        "INVALID_DESTINATION_URL",
        "MISSING_DESTINATION_URL_TAG",
        "KEYWORD_LEVEL_BID_NOT_SUPPORTED_FOR_MANUALCPM",
        "INVALID_USER_STATUS",
        "CANNOT_ADD_CRITERIA_TYPE",
        "CANNOT_EXCLUDE_CRITERIA_TYPE",
        "CAMPAIGN_TYPE_NOT_COMPATIBLE_WITH_PARTIAL_FAILURE",
        "OPERATIONS_FOR_TOO_MANY_SHOPPING_ADGROUPS",
        "CANNOT_MODIFY_URL_FIELDS_WITH_DUPLICATE_ELEMENTS",
        "CANNOT_SET_WITHOUT_FINAL_URLS",
        "CANNOT_CLEAR_FINAL_URLS_IF_FINAL_MOBILE_URLS_EXIST",
        "CANNOT_CLEAR_FINAL_URLS_IF_FINAL_APP_URLS_EXIST",
        "CANNOT_CLEAR_FINAL_URLS_IF_TRACKING_URL_TEMPLATE_EXISTS",
        "CANNOT_CLEAR_FINAL_URLS_IF_URL_CUSTOM_PARAMETERS_EXIST",
        "CANNOT_SET_BOTH_DESTINATION_URL_AND_FINAL_URLS",
        "CANNOT_SET_BOTH_DESTINATION_URL_AND_TRACKING_URL_TEMPLATE",
        "FINAL_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE",
        "FINAL_MOBILE_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE",
    ]
    adGroupCustomizerError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN"]
    adGroupError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_ADGROUP_NAME",
        "INVALID_ADGROUP_NAME",
        "ADVERTISER_NOT_ON_CONTENT_NETWORK",
        "BID_TOO_BIG",
        "BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH",
        "MISSING_ADGROUP_NAME",
        "ADGROUP_LABEL_DOES_NOT_EXIST",
        "ADGROUP_LABEL_ALREADY_EXISTS",
        "INVALID_CONTENT_BID_CRITERION_TYPE_GROUP",
        "AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE",
        "ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY",
        "CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING",
        "PROMOTED_HOTEL_AD_GROUPS_NOT_AVAILABLE_FOR_CUSTOMER",
        "INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE",
        "INVALID_EXCLUDED_PARENT_ASSET_SET_TYPE",
        "CANNOT_ADD_AD_GROUP_FOR_CAMPAIGN_TYPE",
        "INVALID_STATUS",
        "INVALID_STEP_ID_FOR_VIDEO_ADS_SEQUENCING",
        "INVALID_AD_GROUP_TYPE_FOR_VIDEO_ADS_SEQUENCING",
        "DUPLICATE_STEP_ID",
        "INVALID_VERTICAL_ADS_FORMAT_SETTING",
        "VERTICAL_ADS_FORMAT_SETTING_NOT_SUPPORTED_FOR_CAMPAIGNS_WITHOUT_AI_MAX",
        "VERTICAL_ADS_FORMAT_SETTING_NOT_SUPPORTED_FOR_CAMPAIGNS_WITHOUT_ENABLED_TRAVEL_FEED",
    ]
    adGroupFeedError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE",
        "CANNOT_CREATE_FOR_REMOVED_FEED",
        "ADGROUP_FEED_ALREADY_EXISTS",
        "CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED",
        "INVALID_PLACEHOLDER_TYPE",
        "MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE",
        "NO_EXISTING_LOCATION_CUSTOMER_FEED",
    ]
    adParameterError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_CRITERION_MUST_BE_KEYWORD",
        "INVALID_INSERTION_TEXT_FORMAT",
    ]
    adSharingError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_ALREADY_CONTAINS_AD",
        "INCOMPATIBLE_AD_UNDER_AD_GROUP",
        "CANNOT_SHARE_INACTIVE_AD",
    ]
    adxError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "UNSUPPORTED_FEATURE"]
    assetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOMER_NOT_ON_ALLOWLIST_FOR_ASSET_TYPE",
        "DUPLICATE_ASSET",
        "DUPLICATE_ASSET_NAME",
        "ASSET_DATA_IS_MISSING",
        "CANNOT_MODIFY_ASSET_NAME",
        "FIELD_INCOMPATIBLE_WITH_ASSET_TYPE",
        "INVALID_CALL_TO_ACTION_TEXT",
        "LEAD_FORM_INVALID_FIELDS_COMBINATION",
        "LEAD_FORM_MISSING_AGREEMENT",
        "INVALID_ASSET_STATUS",
        "FIELD_CANNOT_BE_MODIFIED_FOR_ASSET_TYPE",
        "SCHEDULES_CANNOT_OVERLAP",
        "PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF",
        "PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT",
        "TOO_MANY_DECIMAL_PLACES_SPECIFIED",
        "DUPLICATE_ASSETS_WITH_DIFFERENT_FIELD_VALUE",
        "CALL_CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED",
        "CALL_CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED",
        "CALL_DISALLOWED_NUMBER_TYPE",
        "CALL_INVALID_CONVERSION_ACTION",
        "CALL_INVALID_COUNTRY_CODE",
        "CALL_INVALID_DOMESTIC_PHONE_NUMBER_FORMAT",
        "CALL_INVALID_PHONE_NUMBER",
        "CALL_PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY",
        "CALL_PREMIUM_RATE_NUMBER_NOT_ALLOWED",
        "CALL_VANITY_PHONE_NUMBER_NOT_ALLOWED",
        "PRICE_HEADER_SAME_AS_DESCRIPTION",
        "MOBILE_APP_INVALID_APP_ID",
        "MOBILE_APP_INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL",
        "NAME_REQUIRED_FOR_ASSET_TYPE",
        "LEAD_FORM_LEGACY_QUALIFYING_QUESTIONS_DISALLOWED",
        "NAME_CONFLICT_FOR_ASSET_TYPE",
        "CANNOT_MODIFY_ASSET_SOURCE",
        "CANNOT_MODIFY_AUTOMATICALLY_CREATED_ASSET",
        "LEAD_FORM_LOCATION_ANSWER_TYPE_DISALLOWED",
        "PAGE_FEED_INVALID_LABEL_TEXT",
        "CUSTOMER_NOT_ON_ALLOWLIST_FOR_WHATSAPP_MESSAGE_ASSETS",
        "CUSTOMER_NOT_ON_ALLOWLIST_FOR_APP_DEEP_LINK_ASSETS",
        "PROMOTION_BARCODE_CANNOT_CONTAIN_LINKS",
        "PROMOTION_BARCODE_INVALID_FORMAT",
        "UNSUPPORTED_BARCODE_TYPE",
        "PROMOTION_QR_CODE_CANNOT_CONTAIN_LINKS",
        "PROMOTION_QR_CODE_INVALID_FORMAT",
        "CUSTOMER_NOT_ON_ALLOWLIST_FOR_MESSAGE_ASSETS",
    ]
    assetGenerationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_ASSETS_GENERATED",
        "FINAL_URL_REQUIRED",
        "GENERATION_CONTEXT_MISSING_FINAL_URL",
        "FINAL_URL_SENSITIVE",
        "FINAL_URL_UNSUPPORTED_LANGUAGE",
        "FINAL_URL_UNAVAILABLE",
        "CAMPAIGN_TYPE_REQUIRED",
        "UNSUPPORTED_CAMPAIGN_TYPE",
        "UNSUPPORTED_FIELD_TYPE",
        "UNSUPPORTED_FIELD_TYPE_FOR_CAMPAIGN_TYPE",
        "FREEFORM_PROMPT_UNSUPPORTED_LANGUAGE",
        "FREEFORM_PROMPT_SENSITIVE",
        "INPUT_IMAGE_FILE_SIZE_TOO_LARGE",
        "INPUT_IMAGE_EMPTY",
        "GENERATION_TYPE_REQUIRED",
        "TOO_MANY_KEYWORDS",
        "KEYWORD_INVALID_LENGTH",
        "NO_VALID_KEYWORDS",
        "FREEFORM_PROMPT_INVALID_LENGTH",
        "FREEFORM_PROMPT_REFERENCES_CHILDREN",
        "FREEFORM_PROMPT_REFERENCES_SPECIFIC_PEOPLE",
        "FREEFORM_PROMPT_VIOLATES_ADS_POLICY",
        "FREEFORM_PROMPT_BRAND_CONTENT",
        "INPUT_IMAGE_DEPICTS_CHILDREN",
        "INPUT_IMAGE_CONTAINS_BRAND_CONTENT",
        "INPUT_IMAGE_SENSITIVE",
        "INPUT_IMAGE_VIOLATES_POLICY",
        "ALL_OUTPUT_IMAGES_FILTERED_OUT_CHILDREN_DEPICTION",
        "ALL_OUTPUT_IMAGES_FILTERED_OUT_SPECIFIC_PEOPLE",
        "ALL_OUTPUT_IMAGES_FILTERED_OUT",
        "INPUT_IMAGE_REQUIRED",
        "INPUT_IMAGE_UNSUPPORTED_IMAGE_TYPE",
        "CONTEXT_ASSET_GROUP_NOT_FOUND",
        "CONTEXT_AD_GROUP_AD_NOT_FOUND",
        "CONTEXT_CAMPAIGN_NOT_FOUND",
    ]
    assetGroupAssetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_RESOURCE",
        "EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION",
        "AD_CUSTOMIZER_NOT_SUPPORTED",
        "HOTEL_PROPERTY_ASSET_NOT_LINKED_TO_CAMPAIGN",
    ]
    assetGroupError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_NAME",
        "CANNOT_ADD_ASSET_GROUP_FOR_CAMPAIGN_TYPE",
        "NOT_ENOUGH_HEADLINE_ASSET",
        "NOT_ENOUGH_LONG_HEADLINE_ASSET",
        "NOT_ENOUGH_DESCRIPTION_ASSET",
        "NOT_ENOUGH_BUSINESS_NAME_ASSET",
        "NOT_ENOUGH_MARKETING_IMAGE_ASSET",
        "NOT_ENOUGH_SQUARE_MARKETING_IMAGE_ASSET",
        "NOT_ENOUGH_LOGO_ASSET",
        "FINAL_URL_SHOPPING_MERCHANT_HOME_PAGE_URL_DOMAINS_DIFFER",
        "PATH1_REQUIRED_WHEN_PATH2_IS_SET",
        "SHORT_DESCRIPTION_REQUIRED",
        "FINAL_URL_REQUIRED",
        "FINAL_URL_CONTAINS_INVALID_DOMAIN_NAME",
        "AD_CUSTOMIZER_NOT_SUPPORTED",
        "CANNOT_MUTATE_ASSET_GROUP_FOR_REMOVED_CAMPAIGN",
    ]
    assetGroupListingGroupFilterError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TREE_TOO_DEEP",
        "UNIT_CANNOT_HAVE_CHILDREN",
        "SUBDIVISION_MUST_HAVE_EVERYTHING_ELSE_CHILD",
        "DIFFERENT_DIMENSION_TYPE_BETWEEN_SIBLINGS",
        "SAME_DIMENSION_VALUE_BETWEEN_SIBLINGS",
        "SAME_DIMENSION_TYPE_BETWEEN_ANCESTORS",
        "MULTIPLE_ROOTS",
        "INVALID_DIMENSION_VALUE",
        "MUST_REFINE_HIERARCHICAL_PARENT_TYPE",
        "INVALID_PRODUCT_BIDDING_CATEGORY",
        "CHANGING_CASE_VALUE_WITH_CHILDREN",
        "SUBDIVISION_HAS_CHILDREN",
        "CANNOT_REFINE_HIERARCHICAL_EVERYTHING_ELSE",
        "DIMENSION_TYPE_NOT_ALLOWED",
        "DUPLICATE_WEBPAGE_FILTER_UNDER_ASSET_GROUP",
        "LISTING_SOURCE_NOT_ALLOWED",
        "FILTER_EXCLUSION_NOT_ALLOWED",
        "MULTIPLE_LISTING_SOURCES",
        "MULTIPLE_WEBPAGE_CONDITION_TYPES_NOT_ALLOWED",
        "MULTIPLE_WEBPAGE_TYPES_PER_ASSET_GROUP",
        "PAGE_FEED_FILTER_HAS_PARENT",
        "MULTIPLE_OPERATIONS_ON_ONE_NODE",
        "TREE_WAS_INVALID_BEFORE_MUTATION",
    ]
    assetGroupSignalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TOO_MANY_WORDS",
        "SEARCH_THEME_POLICY_VIOLATION",
        "AUDIENCE_WITH_WRONG_ASSET_GROUP_ID",
    ]
    assetLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PINNING_UNSUPPORTED",
        "UNSUPPORTED_FIELD_TYPE",
        "FIELD_TYPE_INCOMPATIBLE_WITH_ASSET_TYPE",
        "FIELD_TYPE_INCOMPATIBLE_WITH_CAMPAIGN_TYPE",
        "INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE",
        "IMAGE_NOT_WITHIN_SPECIFIED_DIMENSION_RANGE",
        "INVALID_PINNED_FIELD",
        "MEDIA_BUNDLE_ASSET_FILE_SIZE_TOO_LARGE",
        "NOT_ENOUGH_AVAILABLE_ASSET_LINKS_FOR_VALID_COMBINATION",
        "NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK",
        "NOT_ENOUGH_AVAILABLE_ASSET_LINKS_WITH_FALLBACK_FOR_VALID_COMBINATION",
        "YOUTUBE_VIDEO_REMOVED",
        "YOUTUBE_VIDEO_TOO_LONG",
        "YOUTUBE_VIDEO_TOO_SHORT",
        "EXCLUDED_PARENT_FIELD_TYPE",
        "INVALID_STATUS",
        "YOUTUBE_VIDEO_DURATION_NOT_DEFINED",
        "CANNOT_CREATE_AUTOMATICALLY_CREATED_LINKS",
        "CANNOT_LINK_TO_AUTOMATICALLY_CREATED_ASSET",
        "CANNOT_MODIFY_ASSET_LINK_SOURCE",
        "CANNOT_LINK_LOCATION_LEAD_FORM_WITHOUT_LOCATION_ASSET",
        "CUSTOMER_NOT_VERIFIED",
        "UNSUPPORTED_CALL_TO_ACTION",
        "BRAND_ASSETS_NOT_LINKED_AT_ASSET_GROUP_LEVEL",
        "BRAND_ASSETS_NOT_LINKED_AT_CAMPAIGN_LEVEL",
    ]
    assetSetAssetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_ASSET_TYPE",
        "INVALID_ASSET_SET_TYPE",
        "DUPLICATE_EXTERNAL_KEY",
        "PARENT_LINKAGE_DOES_NOT_EXIST",
    ]
    assetSetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_ASSET_SET_NAME",
        "INVALID_PARENT_ASSET_SET_TYPE",
        "ASSET_SET_SOURCE_INCOMPATIBLE_WITH_PARENT_ASSET_SET",
        "ASSET_SET_TYPE_CANNOT_BE_LINKED_TO_CUSTOMER",
        "INVALID_CHAIN_IDS",
        "LOCATION_SYNC_ASSET_SET_DOES_NOT_SUPPORT_RELATIONSHIP_TYPE",
        "NOT_UNIQUE_ENABLED_LOCATION_SYNC_TYPED_ASSET_SET",
        "INVALID_PLACE_IDS",
        "OAUTH_INFO_INVALID",
        "OAUTH_INFO_MISSING",
        "CANNOT_DELETE_AS_ENABLED_LINKAGES_EXIST",
    ]
    assetSetLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE",
        "DUPLICATE_FEED_LINK",
        "INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE",
        "DUPLICATE_ASSET_SET_LINK",
        "ASSET_SET_LINK_CANNOT_BE_REMOVED",
    ]
    audienceError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NAME_ALREADY_IN_USE",
        "DIMENSION_INVALID",
        "AUDIENCE_SEGMENT_NOT_FOUND",
        "AUDIENCE_SEGMENT_TYPE_NOT_SUPPORTED",
        "DUPLICATE_AUDIENCE_SEGMENT",
        "TOO_MANY_SEGMENTS",
        "TOO_MANY_DIMENSIONS_OF_SAME_TYPE",
        "IN_USE",
        "MISSING_ASSET_GROUP_ID",
        "CANNOT_CHANGE_FROM_CUSTOMER_TO_ASSET_GROUP_SCOPE",
    ]
    audienceInsightsError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DIMENSION_INCOMPATIBLE_WITH_TOPIC_AUDIENCE_COMBINATIONS",
    ]
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
        "INVALID_EMAIL_ADDRESS",
        "USER_ID_INVALID",
        "TWO_STEP_VERIFICATION_NOT_ENROLLED",
        "ADVANCED_PROTECTION_NOT_ENROLLED",
        "ORGANIZATION_NOT_RECOGNIZED",
        "ORGANIZATION_NOT_APPROVED",
        "ORGANIZATION_NOT_ASSOCIATED_WITH_DEVELOPER_TOKEN",
        "DEVELOPER_TOKEN_INVALID",
    ]
    authorizationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "USER_PERMISSION_DENIED",
        "DEVELOPER_TOKEN_NOT_ON_ALLOWLIST",
        "DEVELOPER_TOKEN_PROHIBITED",
        "PROJECT_DISABLED",
        "AUTHORIZATION_ERROR",
        "ACTION_NOT_PERMITTED",
        "INCOMPLETE_SIGNUP",
        "CUSTOMER_NOT_ENABLED",
        "MISSING_TOS",
        "DEVELOPER_TOKEN_NOT_APPROVED",
        "INVALID_LOGIN_CUSTOMER_ID_SERVING_CUSTOMER_ID_COMBINATION",
        "SERVICE_ACCESS_DENIED",
        "ACCESS_DENIED_FOR_ACCOUNT_TYPE",
        "METRIC_ACCESS_DENIED",
        "CLOUD_PROJECT_NOT_UNDER_ORGANIZATION",
        "ACTION_NOT_PERMITTED_FOR_SUSPENDED_ACCOUNT",
    ]
    automaticallyCreatedAssetRemovalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_DOES_NOT_EXIST",
        "INVALID_AD_TYPE",
        "ASSET_DOES_NOT_EXIST",
        "ASSET_FIELD_TYPE_DOES_NOT_MATCH",
        "NOT_AN_AUTOMATICALLY_CREATED_ASSET",
    ]
    batchJobError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING",
        "EMPTY_OPERATIONS",
        "INVALID_SEQUENCE_TOKEN",
        "RESULTS_NOT_READY",
        "INVALID_PAGE_SIZE",
        "CAN_ONLY_REMOVE_PENDING_JOB",
        "CANNOT_LIST_RESULTS",
        "ASSET_GROUP_AND_ASSET_GROUP_ASSET_TRANSACTION_FAILURE",
        "ASSET_GROUP_LISTING_GROUP_FILTER_TRANSACTION_FAILURE",
        "REQUEST_TOO_LARGE",
        "CAMPAIGN_AND_CAMPAIGN_ASSET_TRANSACTION_FAILURE",
    ]
    benchmarksError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "MAX_QUERY_COMPLEXITY_EXCEEDED"
    ]
    biddingError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED",
        "CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN",
        "INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE",
        "INVALID_BIDDING_STRATEGY_TYPE",
        "INVALID_BID",
        "BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE",
        "CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY",
        "CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY",
        "BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE",
        "PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER",
        "PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA",
        "BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS",
        "BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS",
        "BIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION",
        "BID_TOO_SMALL",
        "BID_TOO_BIG",
        "BID_TOO_MANY_FRACTIONAL_DIGITS",
        "INVALID_DOMAIN_NAME",
        "NOT_COMPATIBLE_WITH_PAYMENT_MODE",
        "BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET",
        "BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED",
        "BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ATTACHED_TO_THE_SAME_CAMPAIGNS_TO_ALIGN",
        "BIDDING_STRATEGY_AND_BUDGET_MUST_BE_REMOVED_TOGETHER",
        "CPC_BID_FLOOR_MICROS_GREATER_THAN_CPC_BID_CEILING_MICROS",
        "TARGET_ROAS_TOLERANCE_PERCENT_MILLIS_MUST_BE_INTEGER",
    ]
    biddingStrategyError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_NAME",
        "CANNOT_CHANGE_BIDDING_STRATEGY_TYPE",
        "CANNOT_REMOVE_ASSOCIATED_STRATEGY",
        "BIDDING_STRATEGY_NOT_SUPPORTED",
        "INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE",
    ]
    billingSetupError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_USE_EXISTING_AND_NEW_ACCOUNT",
        "CANNOT_REMOVE_STARTED_BILLING_SETUP",
        "CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT",
        "BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS",
        "INVALID_PAYMENTS_ACCOUNT",
        "BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY",
        "INVALID_START_TIME_TYPE",
        "THIRD_PARTY_ALREADY_HAS_BILLING",
        "BILLING_SETUP_IN_PROGRESS",
        "NO_SIGNUP_PERMISSION",
        "CHANGE_OF_BILL_TO_IN_PROGRESS",
        "PAYMENTS_PROFILE_NOT_FOUND",
        "PAYMENTS_ACCOUNT_NOT_FOUND",
        "PAYMENTS_PROFILE_INELIGIBLE",
        "PAYMENTS_ACCOUNT_INELIGIBLE",
        "CUSTOMER_NEEDS_INTERNAL_APPROVAL",
        "PAYMENTS_PROFILE_NEEDS_SERVICE_AGREEMENT_ACCEPTANCE",
        "PAYMENTS_ACCOUNT_INELIGIBLE_CURRENCY_CODE_MISMATCH",
        "FUTURE_START_TIME_PROHIBITED",
        "TOO_MANY_BILLING_SETUPS_FOR_PAYMENTS_ACCOUNT",
    ]
    brandGuidelinesMigrationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BRAND_GUIDELINES_ALREADY_ENABLED",
        "CANNOT_ENABLE_BRAND_GUIDELINES_FOR_REMOVED_CAMPAIGN",
        "BRAND_GUIDELINES_LOGO_LIMIT_EXCEEDED",
        "CANNOT_AUTO_POPULATE_BRAND_ASSETS_WHEN_BRAND_ASSETS_PROVIDED",
        "AUTO_POPULATE_BRAND_ASSETS_REQUIRED_WHEN_BRAND_ASSETS_OMITTED",
        "TOO_MANY_ENABLE_OPERATIONS",
    ]
    campaignBudgetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BUDGET_CANNOT_BE_SHARED",
        "CAMPAIGN_BUDGET_REMOVED",
        "CAMPAIGN_BUDGET_IN_USE",
        "CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE",
        "CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET",
        "CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED",
        "CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME",
        "CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED",
        "CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS",
        "DUPLICATE_NAME",
        "MONEY_AMOUNT_IN_WRONG_CURRENCY",
        "MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC",
        "MONEY_AMOUNT_TOO_LARGE",
        "NEGATIVE_MONEY_AMOUNT",
        "NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT",
        "TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY",
        "INVALID_PERIOD",
        "CANNOT_USE_ACCELERATED_DELIVERY_MODE",
        "BUDGET_AMOUNT_MUST_BE_UNSET_FOR_CUSTOM_BUDGET_PERIOD",
        "BUDGET_BELOW_PER_DAY_MINIMUM",
    ]
    campaignConversionGoalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN",
        "CANNOT_USE_STORE_SALE_GOAL_FOR_PERFORMANCE_MAX_CAMPAIGN",
    ]
    campaignCriterionError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONCRETE_TYPE_REQUIRED",
        "INVALID_PLACEMENT_URL",
        "CANNOT_EXCLUDE_CRITERIA_TYPE",
        "CANNOT_SET_STATUS_FOR_CRITERIA_TYPE",
        "CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA",
        "CANNOT_TARGET_AND_EXCLUDE",
        "TOO_MANY_OPERATIONS",
        "OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE",
        "SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL",
        "CANNOT_ADD_EXISTING_FIELD",
        "CANNOT_UPDATE_NEGATIVE_CRITERION",
        "CANNOT_SET_NEGATIVE_KEYWORD_THEME_CONSTANT_CRITERION",
        "INVALID_KEYWORD_THEME_CONSTANT",
        "MISSING_KEYWORD_THEME_CONSTANT_OR_FREE_FORM_KEYWORD_THEME",
        "CANNOT_TARGET_BOTH_PROXIMITY_AND_LOCATION_CRITERIA_FOR_SMART_CAMPAIGN",
        "CANNOT_TARGET_MULTIPLE_PROXIMITY_CRITERIA_FOR_SMART_CAMPAIGN",
        "LOCATION_NOT_LAUNCHED_FOR_LOCAL_SERVICES_CAMPAIGN",
        "LOCATION_INVALID_FOR_LOCAL_SERVICES_CAMPAIGN",
        "CANNOT_TARGET_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN",
        "LOCATION_NOT_IN_HOME_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN",
        "CANNOT_ADD_OR_REMOVE_LOCATION_FOR_LOCAL_SERVICES_CAMPAIGN",
        "AT_LEAST_ONE_POSITIVE_LOCATION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN",
        "AT_LEAST_ONE_LOCAL_SERVICE_ID_CRITERION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN",
        "LOCAL_SERVICE_ID_NOT_FOUND_FOR_CATEGORY",
        "CANNOT_ATTACH_BRAND_LIST_TO_NON_QUALIFIED_SEARCH_CAMPAIGN",
        "CANNOT_REMOVE_ALL_LOCATIONS_DUE_TO_TOO_MANY_COUNTRY_EXCLUSIONS",
        "INVALID_VIDEO_LINEUP_ID",
    ]
    campaignCustomizerError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN"]
    campaignDraftError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_DRAFT_NAME",
        "INVALID_STATUS_TRANSITION_FROM_REMOVED",
        "INVALID_STATUS_TRANSITION_FROM_PROMOTED",
        "INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED",
        "CUSTOMER_CANNOT_CREATE_DRAFT",
        "CAMPAIGN_CANNOT_CREATE_DRAFT",
        "INVALID_DRAFT_CHANGE",
        "INVALID_STATUS_TRANSITION",
        "MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED",
        "LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY",
    ]
    campaignError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_TARGET_CONTENT_NETWORK",
        "CANNOT_TARGET_SEARCH_NETWORK",
        "CANNOT_TARGET_SEARCH_NETWORK_WITHOUT_GOOGLE_SEARCH",
        "CANNOT_TARGET_GOOGLE_SEARCH_FOR_CPM_CAMPAIGN",
        "CAMPAIGN_MUST_TARGET_AT_LEAST_ONE_NETWORK",
        "CANNOT_TARGET_PARTNER_SEARCH_NETWORK",
        "CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CRITERIA_LEVEL_BIDDING_STRATEGY",
        "CAMPAIGN_DURATION_MUST_CONTAIN_ALL_RUNNABLE_TRIALS",
        "CANNOT_MODIFY_FOR_TRIAL_CAMPAIGN",
        "DUPLICATE_CAMPAIGN_NAME",
        "INCOMPATIBLE_CAMPAIGN_FIELD",
        "INVALID_CAMPAIGN_NAME",
        "INVALID_AD_SERVING_OPTIMIZATION_STATUS",
        "INVALID_TRACKING_URL",
        "CANNOT_SET_BOTH_TRACKING_URL_TEMPLATE_AND_TRACKING_SETTING",
        "MAX_IMPRESSIONS_NOT_IN_RANGE",
        "TIME_UNIT_NOT_SUPPORTED",
        "INVALID_OPERATION_IF_SERVING_STATUS_HAS_ENDED",
        "BUDGET_CANNOT_BE_SHARED",
        "CAMPAIGN_CANNOT_USE_SHARED_BUDGET",
        "CANNOT_CHANGE_BUDGET_ON_CAMPAIGN_WITH_TRIALS",
        "CAMPAIGN_LABEL_DOES_NOT_EXIST",
        "CAMPAIGN_LABEL_ALREADY_EXISTS",
        "MISSING_SHOPPING_SETTING",
        "INVALID_SHOPPING_SALES_COUNTRY",
        "ADVERTISING_CHANNEL_TYPE_NOT_AVAILABLE_FOR_ACCOUNT_TYPE",
        "INVALID_ADVERTISING_CHANNEL_SUB_TYPE",
        "AT_LEAST_ONE_CONVERSION_MUST_BE_SELECTED",
        "CANNOT_SET_AD_ROTATION_MODE",
        "CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED",
        "CANNOT_SET_DATE_TO_PAST",
        "MISSING_HOTEL_CUSTOMER_LINK",
        "INVALID_HOTEL_CUSTOMER_LINK",
        "MISSING_HOTEL_SETTING",
        "CANNOT_USE_SHARED_CAMPAIGN_BUDGET_WHILE_PART_OF_CAMPAIGN_GROUP",
        "APP_NOT_FOUND",
        "SHOPPING_ENABLE_LOCAL_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE",
        "MERCHANT_NOT_ALLOWED_FOR_COMPARISON_LISTING_ADS",
        "INSUFFICIENT_APP_INSTALLS_COUNT",
        "SENSITIVE_CATEGORY_APP",
        "HEC_AGREEMENT_REQUIRED",
        "NOT_COMPATIBLE_WITH_VIEW_THROUGH_CONVERSION_OPTIMIZATION",
        "INVALID_EXCLUDED_PARENT_ASSET_FIELD_TYPE",
        "CANNOT_CREATE_APP_PRE_REGISTRATION_FOR_NON_ANDROID_APP",
        "APP_NOT_AVAILABLE_TO_CREATE_APP_PRE_REGISTRATION_CAMPAIGN",
        "INCOMPATIBLE_BUDGET_TYPE",
        "LOCAL_SERVICES_DUPLICATE_CATEGORY_BID",
        "LOCAL_SERVICES_INVALID_CATEGORY_BID",
        "LOCAL_SERVICES_MISSING_CATEGORY_BID",
        "INVALID_STATUS_CHANGE",
        "MISSING_TRAVEL_CUSTOMER_LINK",
        "INVALID_TRAVEL_CUSTOMER_LINK",
        "INVALID_EXCLUDED_PARENT_ASSET_SET_TYPE",
        "ASSET_SET_NOT_A_HOTEL_PROPERTY_ASSET_SET",
        "HOTEL_PROPERTY_ASSET_SET_ONLY_FOR_PERFORMANCE_MAX_FOR_TRAVEL_GOALS",
        "AVERAGE_DAILY_SPEND_TOO_HIGH",
        "CANNOT_ATTACH_TO_REMOVED_CAMPAIGN_GROUP",
        "CANNOT_ATTACH_TO_BIDDING_STRATEGY",
        "CANNOT_CHANGE_BUDGET_PERIOD",
        "NOT_ENOUGH_CONVERSIONS",
        "CANNOT_SET_MORE_THAN_ONE_CONVERSION_ACTION",
        "NOT_COMPATIBLE_WITH_BUDGET_TYPE",
        "NOT_COMPATIBLE_WITH_UPLOAD_CLICKS_CONVERSION",
        "APP_ID_MUST_MATCH_CONVERSION_ACTION_APP_ID",
        "CONVERSION_ACTION_WITH_DOWNLOAD_CATEGORY_NOT_ALLOWED",
        "CONVERSION_ACTION_WITH_DOWNLOAD_CATEGORY_REQUIRED",
        "CONVERSION_TRACKING_NOT_ENABLED",
        "NOT_COMPATIBLE_WITH_BIDDING_STRATEGY_TYPE",
        "NOT_COMPATIBLE_WITH_GOOGLE_ATTRIBUTION_CONVERSIONS",
        "CONVERSION_LAG_TOO_HIGH",
        "NOT_LINKED_ADVERTISING_PARTNER",
        "INVALID_NUMBER_OF_ADVERTISING_PARTNER_IDS",
        "CANNOT_TARGET_DISPLAY_NETWORK_WITHOUT_YOUTUBE",
        "CANNOT_LINK_TO_COMPARISON_SHOPPING_SERVICE_ACCOUNT",
        "CANNOT_TARGET_NETWORK_FOR_COMPARISON_SHOPPING_SERVICE_LINKED_ACCOUNTS",
        "CANNOT_MODIFY_TEXT_ASSET_AUTOMATION_WITH_ENABLED_TRIAL",
        "DYNAMIC_TEXT_ASSET_CANNOT_OPT_OUT_WITH_FINAL_URL_EXPANSION_OPT_IN",
        "CANNOT_SET_CAMPAIGN_KEYWORD_MATCH_TYPE",
        "CANNOT_DISABLE_BROAD_MATCH_WHEN_KEYWORD_CONVERSION_IN_PROCESS",
        "CANNOT_DISABLE_BROAD_MATCH_WHEN_TARGETING_BRANDS",
        "CANNOT_ENABLE_BROAD_MATCH_FOR_BASE_CAMPAIGN_WITH_PROMOTING_TRIAL",
        "CANNOT_ENABLE_BROAD_MATCH_FOR_PROMOTING_TRIAL_CAMPAIGN",
        "REQUIRED_BUSINESS_NAME_ASSET_NOT_LINKED",
        "REQUIRED_LOGO_ASSET_NOT_LINKED",
        "BRAND_TARGETING_OVERRIDES_NOT_SUPPORTED",
        "BRAND_GUIDELINES_NOT_ENABLED_FOR_CAMPAIGN",
        "BRAND_GUIDELINES_MAIN_AND_ACCENT_COLORS_REQUIRED",
        "BRAND_GUIDELINES_COLOR_INVALID_FORMAT",
        "BRAND_GUIDELINES_UNSUPPORTED_FONT_FAMILY",
        "BRAND_GUIDELINES_UNSUPPORTED_CHANNEL",
        "CANNOT_ENABLE_BRAND_GUIDELINES_FOR_TRAVEL_GOALS",
        "CUSTOMER_NOT_ALLOWLISTED_FOR_BRAND_GUIDELINES",
        "THIRD_PARTY_INTEGRATION_PARTNER_NOT_ALLOWED",
        "THIRD_PARTY_INTEGRATION_PARTNER_SHARE_COST_NOT_ALLOWED",
        "DUPLICATE_INTERACTION_TYPE",
        "INVALID_INTERACTION_TYPE",
        "VIDEO_SEQUENCE_ERROR_SEQUENCE_DEFINITION_REQUIRED",
        "AI_MAX_MUST_BE_ENABLED",
        "DURATION_TOO_LONG_FOR_TOTAL_BUDGET",
        "END_DATE_TIME_REQUIRED_FOR_TOTAL_BUDGET",
    ]
    campaignExperimentError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_NAME",
        "INVALID_TRANSITION",
        "CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET",
        "CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN",
        "CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT",
        "CUSTOMER_CANNOT_CREATE_EXPERIMENT",
        "CAMPAIGN_CANNOT_CREATE_EXPERIMENT",
        "EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP",
        "EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION",
        "CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS",
    ]
    campaignFeedError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE",
        "CANNOT_CREATE_FOR_REMOVED_FEED",
        "CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED",
        "CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED",
        "INVALID_PLACEHOLDER_TYPE",
        "MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE",
        "NO_EXISTING_LOCATION_CUSTOMER_FEED",
        "LEGACY_FEED_TYPE_READ_ONLY",
    ]
    campaignGoalConfigError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "GOAL_NOT_FOUND",
        "CAMPAIGN_NOT_FOUND",
        "HIGH_LIFETIME_VALUE_PRESENT_BUT_VALUE_ABSENT",
        "HIGH_LIFETIME_VALUE_LESS_THAN_OR_EQUAL_TO_VALUE",
        "CUSTOMER_LIFECYCLE_OPTIMIZATION_CAMPAIGN_TYPE_NOT_SUPPORTED",
        "CUSTOMER_NOT_ALLOWLISTED_FOR_RETENTION_ONLY",
    ]
    campaignLifecycleGoalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_MISSING",
        "INVALID_CAMPAIGN",
        "CUSTOMER_ACQUISITION_INVALID_OPTIMIZATION_MODE",
        "INCOMPATIBLE_BIDDING_STRATEGY",
        "MISSING_PURCHASE_GOAL",
        "CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE",
        "CUSTOMER_ACQUISITION_UNSUPPORTED_CAMPAIGN_TYPE",
        "CUSTOMER_ACQUISITION_INVALID_VALUE",
        "CUSTOMER_ACQUISITION_VALUE_MISSING",
        "CUSTOMER_ACQUISITION_MISSING_EXISTING_CUSTOMER_DEFINITION",
        "CUSTOMER_ACQUISITION_MISSING_HIGH_VALUE_CUSTOMER_DEFINITION",
    ]
    campaignSharedSetError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "SHARED_SET_ACCESS_DENIED"
    ]
    changeEventError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "START_DATE_TOO_OLD",
        "CHANGE_DATE_RANGE_INFINITE",
        "CHANGE_DATE_RANGE_NEGATIVE",
        "LIMIT_NOT_SPECIFIED",
        "INVALID_LIMIT_CLAUSE",
    ]
    changeStatusError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "START_DATE_TOO_OLD",
        "CHANGE_DATE_RANGE_INFINITE",
        "CHANGE_DATE_RANGE_NEGATIVE",
        "LIMIT_NOT_SPECIFIED",
        "INVALID_LIMIT_CLAUSE",
    ]
    clickViewError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "EXPECTED_FILTER_ON_A_SINGLE_DAY", "DATE_TOO_OLD"
    ]
    collectionSizeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "TOO_FEW", "TOO_MANY"
    ]
    contextError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPERATION_NOT_PERMITTED_FOR_CONTEXT",
        "OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE",
    ]
    conversionActionError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_NAME",
        "DUPLICATE_APP_ID",
        "TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD",
        "BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION",
        "DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED",
        "DATA_DRIVEN_MODEL_EXPIRED",
        "DATA_DRIVEN_MODEL_STALE",
        "DATA_DRIVEN_MODEL_UNKNOWN",
        "CREATION_NOT_SUPPORTED",
        "UPDATE_NOT_SUPPORTED",
        "CANNOT_SET_RULE_BASED_ATTRIBUTION_MODELS",
    ]
    conversionAdjustmentUploadError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TOO_RECENT_CONVERSION_ACTION",
        "CONVERSION_ALREADY_RETRACTED",
        "CONVERSION_NOT_FOUND",
        "CONVERSION_EXPIRED",
        "ADJUSTMENT_PRECEDES_CONVERSION",
        "MORE_RECENT_RESTATEMENT_FOUND",
        "TOO_RECENT_CONVERSION",
        "CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE",
        "TOO_MANY_ADJUSTMENTS_IN_REQUEST",
        "TOO_MANY_ADJUSTMENTS",
        "RESTATEMENT_ALREADY_EXISTS",
        "DUPLICATE_ADJUSTMENT_IN_REQUEST",
        "CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS",
        "CONVERSION_ACTION_NOT_ELIGIBLE_FOR_ENHANCEMENT",
        "INVALID_USER_IDENTIFIER",
        "UNSUPPORTED_USER_IDENTIFIER",
        "GCLID_DATE_TIME_PAIR_AND_ORDER_ID_BOTH_SET",
        "CONVERSION_ALREADY_ENHANCED",
        "DUPLICATE_ENHANCEMENT_IN_REQUEST",
        "CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCEMENT",
        "MISSING_ORDER_ID_FOR_WEBPAGE",
        "ORDER_ID_CONTAINS_PII",
        "INVALID_JOB_ID",
        "NO_CONVERSION_ACTION_FOUND",
        "INVALID_CONVERSION_ACTION_TYPE",
    ]
    conversionCustomVariableError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_NAME", "DUPLICATE_TAG", "RESERVED_TAG"
    ]
    conversionGoalCampaignConfigError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN",
        "CUSTOM_GOAL_DOES_NOT_BELONG_TO_GOOGLE_ADS_CONVERSION_CUSTOMER",
        "CAMPAIGN_CANNOT_USE_UNIFIED_GOALS",
        "EMPTY_CONVERSION_GOALS",
        "STORE_SALE_STORE_VISIT_CANNOT_BE_BOTH_INCLUDED",
        "PERFORMANCE_MAX_CAMPAIGN_CANNOT_USE_CUSTOM_GOAL_WITH_STORE_SALES",
    ]
    conversionUploadError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TOO_MANY_CONVERSIONS_IN_REQUEST",
        "UNPARSEABLE_GCLID",
        "CONVERSION_PRECEDES_EVENT",
        "EXPIRED_EVENT",
        "TOO_RECENT_EVENT",
        "EVENT_NOT_FOUND",
        "UNAUTHORIZED_CUSTOMER",
        "TOO_RECENT_CONVERSION_ACTION",
        "CONVERSION_TRACKING_NOT_ENABLED_AT_IMPRESSION_TIME",
        "EXTERNAL_ATTRIBUTION_DATA_SET_FOR_NON_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION",
        "EXTERNAL_ATTRIBUTION_DATA_NOT_SET_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION",
        "ORDER_ID_NOT_PERMITTED_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION",
        "ORDER_ID_ALREADY_IN_USE",
        "DUPLICATE_ORDER_ID",
        "TOO_RECENT_CALL",
        "EXPIRED_CALL",
        "CALL_NOT_FOUND",
        "CONVERSION_PRECEDES_CALL",
        "CONVERSION_TRACKING_NOT_ENABLED_AT_CALL_TIME",
        "UNPARSEABLE_CALLERS_PHONE_NUMBER",
        "CLICK_CONVERSION_ALREADY_EXISTS",
        "CALL_CONVERSION_ALREADY_EXISTS",
        "DUPLICATE_CLICK_CONVERSION_IN_REQUEST",
        "DUPLICATE_CALL_CONVERSION_IN_REQUEST",
        "CUSTOM_VARIABLE_NOT_ENABLED",
        "CUSTOM_VARIABLE_VALUE_CONTAINS_PII",
        "INVALID_CUSTOMER_FOR_CLICK",
        "INVALID_CUSTOMER_FOR_CALL",
        "CONVERSION_NOT_COMPLIANT_WITH_ATT_POLICY",
        "CLICK_NOT_FOUND",
        "INVALID_USER_IDENTIFIER",
        "EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION_NOT_PERMITTED_WITH_USER_IDENTIFIER",
        "UNSUPPORTED_USER_IDENTIFIER",
        "GBRAID_WBRAID_BOTH_SET",
        "UNPARSEABLE_WBRAID",
        "UNPARSEABLE_GBRAID",
        "ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID",
        "CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS",
        "CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS",
        "ORDER_ID_CONTAINS_PII",
        "CUSTOMER_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS",
        "INVALID_JOB_ID",
        "NO_CONVERSION_ACTION_FOUND",
        "INVALID_CONVERSION_ACTION_TYPE",
    ]
    conversionValueRuleError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_GEO_TARGET_CONSTANT",
        "CONFLICTING_INCLUDED_AND_EXCLUDED_GEO_TARGET",
        "CONFLICTING_CONDITIONS",
        "CANNOT_REMOVE_IF_INCLUDED_IN_VALUE_RULE_SET",
        "CONDITION_NOT_ALLOWED",
        "FIELD_MUST_BE_UNSET",
        "CANNOT_PAUSE_UNLESS_VALUE_RULE_SET_IS_PAUSED",
        "UNTARGETABLE_GEO_TARGET",
        "INVALID_AUDIENCE_USER_LIST",
        "INACCESSIBLE_USER_LIST",
        "INVALID_AUDIENCE_USER_INTEREST",
        "CANNOT_ADD_RULE_WITH_STATUS_REMOVED",
        "NO_DAY_OF_WEEK_SELECTED",
    ]
    conversionValueRuleSetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONFLICTING_VALUE_RULE_CONDITIONS",
        "INVALID_VALUE_RULE",
        "DIMENSIONS_UPDATE_ONLY_ALLOW_APPEND",
        "CONDITION_TYPE_NOT_ALLOWED",
        "DUPLICATE_DIMENSIONS",
        "INVALID_CAMPAIGN_ID",
        "CANNOT_PAUSE_UNLESS_ALL_VALUE_RULES_ARE_PAUSED",
        "SHOULD_PAUSE_WHEN_ALL_VALUE_RULES_ARE_PAUSED",
        "VALUE_RULES_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE",
        "INELIGIBLE_CONVERSION_ACTION_CATEGORIES",
        "DIMENSION_NO_CONDITION_USED_WITH_OTHER_DIMENSIONS",
        "DIMENSION_NO_CONDITION_NOT_ALLOWED",
        "UNSUPPORTED_CONVERSION_ACTION_CATEGORIES",
        "DIMENSION_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE",
    ]
    countryCodeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_COUNTRY_CODE"
    ]
    criterionError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONCRETE_TYPE_REQUIRED",
        "INVALID_EXCLUDED_CATEGORY",
        "INVALID_KEYWORD_TEXT",
        "KEYWORD_TEXT_TOO_LONG",
        "KEYWORD_HAS_TOO_MANY_WORDS",
        "KEYWORD_HAS_INVALID_CHARS",
        "INVALID_PLACEMENT_URL",
        "INVALID_USER_LIST",
        "INVALID_USER_INTEREST",
        "INVALID_FORMAT_FOR_PLACEMENT_URL",
        "PLACEMENT_URL_IS_TOO_LONG",
        "PLACEMENT_URL_HAS_ILLEGAL_CHAR",
        "PLACEMENT_URL_HAS_MULTIPLE_SITES_IN_LINE",
        "PLACEMENT_IS_NOT_AVAILABLE_FOR_TARGETING_OR_EXCLUSION",
        "INVALID_TOPIC_PATH",
        "INVALID_YOUTUBE_CHANNEL_ID",
        "INVALID_YOUTUBE_VIDEO_ID",
        "YOUTUBE_VERTICAL_CHANNEL_DEPRECATED",
        "YOUTUBE_DEMOGRAPHIC_CHANNEL_DEPRECATED",
        "YOUTUBE_URL_UNSUPPORTED",
        "CANNOT_EXCLUDE_CRITERIA_TYPE",
        "CANNOT_ADD_CRITERIA_TYPE",
        "CANNOT_EXCLUDE_SIMILAR_USER_LIST",
        "CANNOT_ADD_CLOSED_USER_LIST",
        "CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_ONLY_CAMPAIGNS",
        "CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_CAMPAIGNS",
        "CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SHOPPING_CAMPAIGNS",
        "CANNOT_ADD_USER_INTERESTS_TO_SEARCH_CAMPAIGNS",
        "CANNOT_SET_BIDS_ON_CRITERION_TYPE_IN_SEARCH_CAMPAIGNS",
        "CANNOT_ADD_URLS_TO_CRITERION_TYPE_FOR_CAMPAIGN_TYPE",
        "INVALID_COMBINED_AUDIENCE",
        "INVALID_CUSTOM_AFFINITY",
        "INVALID_CUSTOM_INTENT",
        "INVALID_CUSTOM_AUDIENCE",
        "INVALID_IP_ADDRESS",
        "INVALID_IP_FORMAT",
        "INVALID_MOBILE_APP",
        "INVALID_MOBILE_APP_CATEGORY",
        "INVALID_CRITERION_ID",
        "CANNOT_TARGET_CRITERION",
        "CANNOT_TARGET_OBSOLETE_CRITERION",
        "CRITERION_ID_AND_TYPE_MISMATCH",
        "INVALID_PROXIMITY_RADIUS",
        "INVALID_PROXIMITY_RADIUS_UNITS",
        "INVALID_STREETADDRESS_LENGTH",
        "INVALID_CITYNAME_LENGTH",
        "INVALID_REGIONCODE_LENGTH",
        "INVALID_REGIONNAME_LENGTH",
        "INVALID_POSTALCODE_LENGTH",
        "INVALID_COUNTRY_CODE",
        "INVALID_LATITUDE",
        "INVALID_LONGITUDE",
        "PROXIMITY_GEOPOINT_AND_ADDRESS_BOTH_CANNOT_BE_NULL",
        "INVALID_PROXIMITY_ADDRESS",
        "INVALID_USER_DOMAIN_NAME",
        "CRITERION_PARAMETER_TOO_LONG",
        "AD_SCHEDULE_TIME_INTERVALS_OVERLAP",
        "AD_SCHEDULE_INTERVAL_CANNOT_SPAN_MULTIPLE_DAYS",
        "AD_SCHEDULE_INVALID_TIME_INTERVAL",
        "AD_SCHEDULE_EXCEEDED_INTERVALS_PER_DAY_LIMIT",
        "AD_SCHEDULE_CRITERION_ID_MISMATCHING_FIELDS",
        "CANNOT_BID_MODIFY_CRITERION_TYPE",
        "CANNOT_BID_MODIFY_CRITERION_CAMPAIGN_OPTED_OUT",
        "CANNOT_BID_MODIFY_NEGATIVE_CRITERION",
        "BID_MODIFIER_ALREADY_EXISTS",
        "FEED_ID_NOT_ALLOWED",
        "ACCOUNT_INELIGIBLE_FOR_CRITERIA_TYPE",
        "CRITERIA_TYPE_INVALID_FOR_BIDDING_STRATEGY",
        "CANNOT_EXCLUDE_CRITERION",
        "CANNOT_REMOVE_CRITERION",
        "INVALID_PRODUCT_BIDDING_CATEGORY",
        "MISSING_SHOPPING_SETTING",
        "INVALID_MATCHING_FUNCTION",
        "LOCATION_FILTER_NOT_ALLOWED",
        "INVALID_FEED_FOR_LOCATION_FILTER",
        "LOCATION_FILTER_INVALID",
        "CANNOT_SET_GEO_TARGET_CONSTANTS_WITH_FEED_ITEM_SETS",
        "CANNOT_SET_BOTH_ASSET_SET_AND_FEED",
        "CANNOT_SET_FEED_OR_FEED_ITEM_SETS_FOR_CUSTOMER",
        "CANNOT_SET_ASSET_SET_FIELD_FOR_CUSTOMER",
        "CANNOT_SET_GEO_TARGET_CONSTANTS_WITH_ASSET_SETS",
        "CANNOT_SET_ASSET_SETS_WITH_FEED_ITEM_SETS",
        "INVALID_LOCATION_GROUP_ASSET_SET",
        "INVALID_LOCATION_GROUP_RADIUS",
        "INVALID_LOCATION_GROUP_RADIUS_UNIT",
        "CANNOT_ATTACH_CRITERIA_AT_CAMPAIGN_AND_ADGROUP",
        "HOTEL_LENGTH_OF_STAY_OVERLAPS_WITH_EXISTING_CRITERION",
        "HOTEL_ADVANCE_BOOKING_WINDOW_OVERLAPS_WITH_EXISTING_CRITERION",
        "FIELD_INCOMPATIBLE_WITH_NEGATIVE_TARGETING",
        "INVALID_WEBPAGE_CONDITION",
        "INVALID_WEBPAGE_CONDITION_URL",
        "WEBPAGE_CONDITION_URL_CANNOT_BE_EMPTY",
        "WEBPAGE_CONDITION_URL_UNSUPPORTED_PROTOCOL",
        "WEBPAGE_CONDITION_URL_CANNOT_BE_IP_ADDRESS",
        "WEBPAGE_CONDITION_URL_DOMAIN_NOT_CONSISTENT_WITH_CAMPAIGN_SETTING",
        "WEBPAGE_CONDITION_URL_CANNOT_BE_PUBLIC_SUFFIX",
        "WEBPAGE_CONDITION_URL_INVALID_PUBLIC_SUFFIX",
        "WEBPAGE_CONDITION_URL_VALUE_TRACK_VALUE_NOT_SUPPORTED",
        "WEBPAGE_CRITERION_URL_EQUALS_CAN_HAVE_ONLY_ONE_CONDITION",
        "WEBPAGE_CRITERION_NOT_SUPPORTED_ON_NON_DSA_AD_GROUP",
        "CANNOT_TARGET_USER_LIST_FOR_SMART_DISPLAY_CAMPAIGNS",
        "CANNOT_TARGET_PLACEMENTS_FOR_SEARCH_CAMPAIGNS",
        "LISTING_SCOPE_TOO_MANY_DIMENSION_TYPES",
        "LISTING_SCOPE_TOO_MANY_IN_OPERATORS",
        "LISTING_SCOPE_IN_OPERATOR_NOT_SUPPORTED",
        "DUPLICATE_LISTING_DIMENSION_TYPE",
        "DUPLICATE_LISTING_DIMENSION_VALUE",
        "CANNOT_SET_BIDS_ON_LISTING_GROUP_SUBDIVISION",
        "LISTING_GROUP_ERROR_IN_ANOTHER_OPERATION",
        "INVALID_LISTING_GROUP_HIERARCHY",
        "LISTING_GROUP_TREE_WAS_INVALID_BEFORE_MUTATION",
        "LISTING_GROUP_UNIT_CANNOT_HAVE_CHILDREN",
        "LISTING_GROUP_SUBDIVISION_REQUIRES_OTHERS_CASE",
        "LISTING_GROUP_REQUIRES_SAME_DIMENSION_TYPE_AS_SIBLINGS",
        "LISTING_GROUP_ALREADY_EXISTS",
        "LISTING_GROUP_DOES_NOT_EXIST",
        "LISTING_GROUP_CANNOT_BE_REMOVED",
        "INVALID_LISTING_GROUP_TYPE",
        "LISTING_GROUP_ADD_MAY_ONLY_USE_TEMP_ID",
        "LISTING_SCOPE_TOO_LONG",
        "LISTING_SCOPE_TOO_MANY_DIMENSIONS",
        "LISTING_GROUP_TOO_LONG",
        "LISTING_GROUP_TREE_TOO_DEEP",
        "INVALID_LISTING_DIMENSION",
        "INVALID_LISTING_DIMENSION_TYPE",
        "ADVERTISER_NOT_ON_ALLOWLIST_FOR_COMBINED_AUDIENCE_ON_DISPLAY",
        "CANNOT_TARGET_REMOVED_COMBINED_AUDIENCE",
        "INVALID_COMBINED_AUDIENCE_ID",
        "CANNOT_TARGET_REMOVED_CUSTOM_AUDIENCE",
        "HOTEL_CHECK_IN_DATE_RANGE_OVERLAPS_WITH_EXISTING_CRITERION",
        "HOTEL_CHECK_IN_DATE_RANGE_START_DATE_TOO_EARLY",
        "HOTEL_CHECK_IN_DATE_RANGE_END_DATE_TOO_LATE",
        "HOTEL_CHECK_IN_DATE_RANGE_REVERSED",
        "BROAD_MATCH_MODIFIER_KEYWORD_NOT_ALLOWED",
        "ONE_AUDIENCE_ALLOWED_PER_ASSET_GROUP",
        "AUDIENCE_NOT_ELIGIBLE_FOR_CAMPAIGN_TYPE",
        "AUDIENCE_NOT_ALLOWED_TO_ATTACH_WHEN_AUDIENCE_GROUPED_SET_TO_FALSE",
        "CANNOT_TARGET_CUSTOMER_MATCH_USER_LIST",
        "NEGATIVE_KEYWORD_SHARED_SET_DOES_NOT_EXIST",
        "CANNOT_ADD_REMOVED_NEGATIVE_KEYWORD_SHARED_SET",
        "CANNOT_HAVE_MULTIPLE_NEGATIVE_KEYWORD_LIST_PER_ACCOUNT",
        "CUSTOMER_CANNOT_ADD_CRITERION_OF_THIS_TYPE",
        "CANNOT_TARGET_SIMILAR_USER_LIST",
        "CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET",
        "ONE_AUDIENCE_ALLOWED_PER_AD_GROUP",
        "INVALID_DETAILED_DEMOGRAPHIC",
        "CANNOT_RECOGNIZE_BRAND",
        "BRAND_SHARED_SET_DOES_NOT_EXIST",
        "CANNOT_ADD_REMOVED_BRAND_SHARED_SET",
        "ONLY_EXCLUSION_BRAND_LIST_ALLOWED_FOR_CAMPAIGN_TYPE",
        "LOCATION_TARGETING_NOT_ELIGIBLE_FOR_RESTRICTED_CAMPAIGN",
        "ONLY_INCLUSION_BRAND_LIST_ALLOWED_FOR_AD_GROUPS",
        "CANNOT_ADD_REMOVED_PLACEMENT_LIST_SHARED_SET",
        "PLACEMENT_LIST_SHARED_SET_DOES_NOT_EXIST",
        "AI_MAX_MUST_BE_ENABLED",
        "NOT_AVAILABLE_FOR_AI_MAX_CAMPAIGNS",
        "MISSING_EU_POLITICAL_ADVERTISING_SELF_DECLARATION",
        "INVALID_CAMPAIGN_TYPE_FOR_THIRD_PARTY_PARTNER_DATA_LIST",
        "CANNOT_ADD_USER_LIST_PENDING_PRIVACY_REVIEW",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST_DOES_NOT_EXIST",
        "CANNOT_ADD_REMOVED_VERTICAL_ADS_ITEM_GROUP_RULE_LIST_SHARED_SET",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST_NOT_SUPPORTED_FOR_CAMPAIGNS_WITHOUT_ENABLED_TRAVEL_FEED",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST_NOT_SUPPORTED_FOR_CAMPAIGNS_WITHOUT_AI_MAX",
        "VERTICAL_ADS_ITEM_GROUP_RULE_NOT_SUPPORTED_FOR_THE_VERTICAL_TYPE",
    ]
    currencyCodeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "UNSUPPORTED"
    ]
    currencyError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "VALUE_NOT_MULTIPLE_OF_BILLABLE_UNIT"
    ]
    customAudienceError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NAME_ALREADY_USED",
        "CANNOT_REMOVE_WHILE_IN_USE",
        "RESOURCE_ALREADY_REMOVED",
        "MEMBER_TYPE_AND_PARAMETER_ALREADY_EXISTED",
        "INVALID_MEMBER_TYPE",
        "MEMBER_TYPE_AND_VALUE_DOES_NOT_MATCH",
        "POLICY_VIOLATION",
        "INVALID_TYPE_CHANGE",
    ]
    customColumnError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOM_COLUMN_NOT_FOUND",
        "CUSTOM_COLUMN_NOT_AVAILABLE",
    ]
    customConversionGoalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_CONVERSION_ACTION",
        "CONVERSION_ACTION_NOT_ENABLED",
        "CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL",
        "CUSTOM_GOAL_DUPLICATE_NAME",
        "DUPLICATE_CONVERSION_ACTION_LIST",
        "NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL",
    ]
    customInterestError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NAME_ALREADY_USED",
        "CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE",
        "TYPE_AND_PARAMETER_NOT_FOUND",
        "TYPE_AND_PARAMETER_ALREADY_EXISTED",
        "INVALID_CUSTOM_INTEREST_MEMBER_TYPE",
        "CANNOT_REMOVE_WHILE_IN_USE",
        "CANNOT_CHANGE_TYPE",
    ]
    customerClientLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CLIENT_ALREADY_INVITED_BY_THIS_MANAGER",
        "CLIENT_ALREADY_MANAGED_IN_HIERARCHY",
        "CYCLIC_LINK_NOT_ALLOWED",
        "CUSTOMER_HAS_TOO_MANY_ACCOUNTS",
        "CLIENT_HAS_TOO_MANY_INVITATIONS",
        "CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS",
        "CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER",
        "CLIENT_HAS_TOO_MANY_MANAGERS",
    ]
    customerCustomizerError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN"]
    customerError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "STATUS_CHANGE_DISALLOWED",
        "ACCOUNT_NOT_SET_UP",
        "CREATION_DENIED_FOR_POLICY_VIOLATION",
        "CREATION_DENIED_INELIGIBLE_MCC",
    ]
    customerFeedError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE",
        "CANNOT_CREATE_FOR_REMOVED_FEED",
        "CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED",
        "CANNOT_MODIFY_REMOVED_CUSTOMER_FEED",
        "INVALID_PLACEHOLDER_TYPE",
        "MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE",
        "PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED",
    ]
    customerLifecycleGoalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOMER_ACQUISITION_VALUE_MISSING",
        "CUSTOMER_ACQUISITION_INVALID_VALUE",
        "CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE",
        "CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED",
        "CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED",
        "INVALID_EXISTING_USER_LIST",
        "INVALID_HIGH_LIFETIME_VALUE_USER_LIST",
    ]
    customerManagerLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_PENDING_INVITE",
        "SAME_CLIENT_MORE_THAN_ONCE_PER_CALL",
        "MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS",
        "CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER",
        "CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER",
        "CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER",
        "CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT",
        "DUPLICATE_CHILD_FOUND",
        "TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS",
    ]
    customerSkAdNetworkConversionValueSchemaError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_LINK_ID",
        "INVALID_APP_ID",
        "INVALID_SCHEMA",
        "LINK_CODE_NOT_FOUND",
        "INVALID_EVENT_COUNTER",
        "INVALID_EVENT_NAME",
    ]
    customerUserAccessError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_USER_ID",
        "REMOVAL_DISALLOWED",
        "DISALLOWED_ACCESS_ROLE",
        "LAST_ADMIN_USER_OF_SERVING_CUSTOMER",
        "LAST_ADMIN_USER_OF_MANAGER",
    ]
    customizerAttributeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_CUSTOMIZER_ATTRIBUTE_NAME"
    ]
    dataLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "YOUTUBE_CHANNEL_ID_INVALID",
        "YOUTUBE_VIDEO_ID_INVALID",
        "YOUTUBE_VIDEO_FROM_DIFFERENT_CHANNEL",
        "PERMISSION_DENIED",
        "INVALID_STATUS",
        "INVALID_UPDATE_STATUS",
        "INVALID_RESOURCE_NAME",
    ]
    databaseError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONCURRENT_MODIFICATION",
        "DATA_CONSTRAINT_VIOLATION",
        "REQUEST_TOO_LARGE",
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
        "DATE_RANGE_ERROR_START_TIME_MUST_BE_THE_START_OF_A_DAY",
        "DATE_RANGE_ERROR_END_TIME_MUST_BE_THE_END_OF_A_DAY",
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
    enumError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENUM_VALUE_NOT_PERMITTED"
    ]
    experimentArmError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXPERIMENT_ARM_COUNT_LIMIT_EXCEEDED",
        "INVALID_CAMPAIGN_STATUS",
        "DUPLICATE_EXPERIMENT_ARM_NAME",
        "CANNOT_SET_TREATMENT_ARM_CAMPAIGN",
        "CANNOT_MODIFY_CAMPAIGN_IDS",
        "CANNOT_MODIFY_CAMPAIGN_WITHOUT_SUFFIX_SET",
        "CANNOT_MUTATE_TRAFFIC_SPLIT_AFTER_START",
        "CANNOT_ADD_CAMPAIGN_WITH_SHARED_BUDGET",
        "CANNOT_ADD_CAMPAIGN_WITH_CUSTOM_BUDGET",
        "CANNOT_ADD_CAMPAIGNS_WITH_DYNAMIC_ASSETS_ENABLED",
        "UNSUPPORTED_CAMPAIGN_ADVERTISING_CHANNEL_SUB_TYPE",
        "CANNOT_ADD_BASE_CAMPAIGN_WITH_DATE_RANGE",
        "BIDDING_STRATEGY_NOT_SUPPORTED_IN_EXPERIMENTS",
        "TRAFFIC_SPLIT_NOT_SUPPORTED_FOR_CHANNEL_TYPE",
    ]
    experimentError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_SET_START_DATE_IN_PAST",
        "END_DATE_BEFORE_START_DATE",
        "START_DATE_TOO_FAR_IN_FUTURE",
        "DUPLICATE_EXPERIMENT_NAME",
        "CANNOT_MODIFY_REMOVED_EXPERIMENT",
        "START_DATE_ALREADY_PASSED",
        "CANNOT_SET_END_DATE_IN_PAST",
        "CANNOT_SET_STATUS_TO_REMOVED",
        "CANNOT_MODIFY_PAST_END_DATE",
        "INVALID_STATUS",
        "INVALID_CAMPAIGN_CHANNEL_TYPE",
        "OVERLAPPING_MEMBERS_AND_DATE_RANGE",
        "INVALID_TRIAL_ARM_TRAFFIC_SPLIT",
        "TRAFFIC_SPLIT_OVERLAPPING",
        "SUM_TRIAL_ARM_TRAFFIC_UNEQUALS_TO_TRIAL_TRAFFIC_SPLIT_DENOMINATOR",
        "CANNOT_MODIFY_TRAFFIC_SPLIT_AFTER_START",
        "EXPERIMENT_NOT_FOUND",
        "EXPERIMENT_NOT_YET_STARTED",
        "CANNOT_HAVE_MULTIPLE_CONTROL_ARMS",
        "IN_DESIGN_CAMPAIGNS_NOT_SET",
        "CANNOT_SET_STATUS_TO_GRADUATED",
        "CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_SHARED_BUDGET",
        "CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_CUSTOM_BUDGET",
        "STATUS_TRANSITION_INVALID",
        "DUPLICATE_EXPERIMENT_CAMPAIGN_NAME",
        "CANNOT_REMOVE_IN_CREATION_EXPERIMENT",
        "CANNOT_ADD_CAMPAIGN_WITH_DEPRECATED_AD_TYPES",
        "CANNOT_ENABLE_SYNC_FOR_UNSUPPORTED_EXPERIMENT_TYPE",
        "INVALID_DURATION_FOR_AN_EXPERIMENT",
        "MISSING_EU_POLITICAL_ADVERTISING_SELF_DECLARATION",
    ]
    extensionFeedItemError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "VALUE_OUT_OF_RANGE",
        "URL_LIST_TOO_LONG",
        "CANNOT_HAVE_RESTRICTION_ON_EMPTY_GEO_TARGETING",
        "CANNOT_SET_WITH_FINAL_URLS",
        "CANNOT_SET_WITHOUT_FINAL_URLS",
        "INVALID_PHONE_NUMBER",
        "PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY",
        "CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED",
        "PREMIUM_RATE_NUMBER_NOT_ALLOWED",
        "DISALLOWED_NUMBER_TYPE",
        "INVALID_DOMESTIC_PHONE_NUMBER_FORMAT",
        "VANITY_PHONE_NUMBER_NOT_ALLOWED",
        "INVALID_CALL_CONVERSION_ACTION",
        "CUSTOMER_NOT_ON_ALLOWLIST_FOR_CALLTRACKING",
        "CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY",
        "CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED",
        "INVALID_APP_ID",
        "QUOTES_IN_REVIEW_EXTENSION_SNIPPET",
        "HYPHENS_IN_REVIEW_EXTENSION_SNIPPET",
        "REVIEW_EXTENSION_SOURCE_INELIGIBLE",
        "SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT",
        "INCONSISTENT_CURRENCY_CODES",
        "PRICE_EXTENSION_HAS_DUPLICATED_HEADERS",
        "PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION",
        "PRICE_EXTENSION_HAS_TOO_FEW_ITEMS",
        "PRICE_EXTENSION_HAS_TOO_MANY_ITEMS",
        "UNSUPPORTED_VALUE",
        "UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE",
        "INVALID_DEVICE_PREFERENCE",
        "INVALID_SCHEDULE_END",
        "DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE",
        "INVALID_SNIPPETS_HEADER",
        "CANNOT_OPERATE_ON_REMOVED_FEED_ITEM",
        "PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY",
        "CONFLICTING_CALL_CONVERSION_SETTINGS",
        "EXTENSION_TYPE_MISMATCH",
        "EXTENSION_SUBTYPE_REQUIRED",
        "EXTENSION_TYPE_UNSUPPORTED",
        "CANNOT_OPERATE_ON_FEED_WITH_MULTIPLE_MAPPINGS",
        "CANNOT_OPERATE_ON_FEED_WITH_KEY_ATTRIBUTES",
        "INVALID_PRICE_FORMAT",
        "PROMOTION_INVALID_TIME",
        "TOO_MANY_DECIMAL_PLACES_SPECIFIED",
        "CONCRETE_EXTENSION_TYPE_REQUIRED",
        "SCHEDULE_END_NOT_AFTER_START",
    ]
    extensionSettingError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXTENSIONS_REQUIRED",
        "FEED_TYPE_EXTENSION_TYPE_MISMATCH",
        "INVALID_FEED_TYPE",
        "INVALID_FEED_TYPE_FOR_CUSTOMER_EXTENSION_SETTING",
        "CANNOT_CHANGE_FEED_ITEM_ON_CREATE",
        "CANNOT_UPDATE_NEWLY_CREATED_EXTENSION",
        "NO_EXISTING_AD_GROUP_EXTENSION_SETTING_FOR_TYPE",
        "NO_EXISTING_CAMPAIGN_EXTENSION_SETTING_FOR_TYPE",
        "NO_EXISTING_CUSTOMER_EXTENSION_SETTING_FOR_TYPE",
        "AD_GROUP_EXTENSION_SETTING_ALREADY_EXISTS",
        "CAMPAIGN_EXTENSION_SETTING_ALREADY_EXISTS",
        "CUSTOMER_EXTENSION_SETTING_ALREADY_EXISTS",
        "AD_GROUP_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE",
        "CAMPAIGN_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE",
        "CUSTOMER_FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE",
        "VALUE_OUT_OF_RANGE",
        "CANNOT_SET_FIELD_WITH_FINAL_URLS",
        "FINAL_URLS_NOT_SET",
        "INVALID_PHONE_NUMBER",
        "PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY",
        "CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED",
        "PREMIUM_RATE_NUMBER_NOT_ALLOWED",
        "DISALLOWED_NUMBER_TYPE",
        "INVALID_DOMESTIC_PHONE_NUMBER_FORMAT",
        "VANITY_PHONE_NUMBER_NOT_ALLOWED",
        "INVALID_COUNTRY_CODE",
        "INVALID_CALL_CONVERSION_TYPE_ID",
        "CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING",
        "CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY",
        "INVALID_APP_ID",
        "QUOTES_IN_REVIEW_EXTENSION_SNIPPET",
        "HYPHENS_IN_REVIEW_EXTENSION_SNIPPET",
        "REVIEW_EXTENSION_SOURCE_NOT_ELIGIBLE",
        "SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT",
        "MISSING_FIELD",
        "INCONSISTENT_CURRENCY_CODES",
        "PRICE_EXTENSION_HAS_DUPLICATED_HEADERS",
        "PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION",
        "PRICE_EXTENSION_HAS_TOO_FEW_ITEMS",
        "PRICE_EXTENSION_HAS_TOO_MANY_ITEMS",
        "UNSUPPORTED_VALUE",
        "INVALID_DEVICE_PREFERENCE",
        "INVALID_SCHEDULE_END",
        "DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE",
        "OVERLAPPING_SCHEDULES_NOT_ALLOWED",
        "SCHEDULE_END_NOT_AFTER_START",
        "TOO_MANY_SCHEDULES_PER_DAY",
        "DUPLICATE_EXTENSION_FEED_ITEM_EDIT",
        "INVALID_SNIPPETS_HEADER",
        "PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY",
        "CAMPAIGN_TARGETING_MISMATCH",
        "CANNOT_OPERATE_ON_REMOVED_FEED",
        "EXTENSION_TYPE_REQUIRED",
        "INCOMPATIBLE_UNDERLYING_MATCHING_FUNCTION",
        "START_DATE_AFTER_END_DATE",
        "INVALID_PRICE_FORMAT",
        "PROMOTION_INVALID_TIME",
        "PROMOTION_CANNOT_SET_PERCENT_DISCOUNT_AND_MONEY_DISCOUNT",
        "PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT",
        "TOO_MANY_DECIMAL_PLACES_SPECIFIED",
        "INVALID_LANGUAGE_CODE",
        "UNSUPPORTED_LANGUAGE",
        "CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED",
        "EXTENSION_SETTING_UPDATE_IS_A_NOOP",
        "DISALLOWED_TEXT",
    ]
    feedAttributeReferenceError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_REFERENCE_REMOVED_FEED",
        "INVALID_FEED_NAME",
        "INVALID_FEED_ATTRIBUTE_NAME",
    ]
    feedError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ATTRIBUTE_NAMES_NOT_UNIQUE",
        "ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES",
        "CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED",
        "CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED",
        "CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED",
        "CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE",
        "FEED_REMOVED",
        "INVALID_ORIGIN_VALUE",
        "FEED_ORIGIN_IS_NOT_USER",
        "INVALID_AUTH_TOKEN_FOR_EMAIL",
        "INVALID_EMAIL",
        "DUPLICATE_FEED_NAME",
        "INVALID_FEED_NAME",
        "MISSING_OAUTH_INFO",
        "NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY",
        "TOO_MANY_ATTRIBUTES",
        "INVALID_BUSINESS_ACCOUNT",
        "BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT",
        "INVALID_AFFILIATE_CHAIN_ID",
        "DUPLICATE_SYSTEM_FEED",
        "GMB_ACCESS_ERROR",
        "CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS",
        "LEGACY_EXTENSION_TYPE_READ_ONLY",
    ]
    feedItemError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_CONVERT_ATTRIBUTE_VALUE_FROM_STRING",
        "CANNOT_OPERATE_ON_REMOVED_FEED_ITEM",
        "DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE",
        "KEY_ATTRIBUTES_NOT_FOUND",
        "INVALID_URL",
        "MISSING_KEY_ATTRIBUTES",
        "KEY_ATTRIBUTES_NOT_UNIQUE",
        "CANNOT_MODIFY_KEY_ATTRIBUTE_VALUE",
        "SIZE_TOO_LARGE_FOR_MULTI_VALUE_ATTRIBUTE",
        "LEGACY_FEED_TYPE_READ_ONLY",
    ]
    feedItemSetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FEED_ITEM_SET_REMOVED",
        "CANNOT_CLEAR_DYNAMIC_FILTER",
        "CANNOT_CREATE_DYNAMIC_FILTER",
        "INVALID_FEED_TYPE",
        "DUPLICATE_NAME",
        "WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE",
        "DYNAMIC_FILTER_INVALID_CHAIN_IDS",
    ]
    feedItemSetLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FEED_ID_MISMATCH",
        "NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET",
    ]
    feedItemTargetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MUST_SET_TARGET_ONEOF_ON_CREATE",
        "FEED_ITEM_TARGET_ALREADY_EXISTS",
        "FEED_ITEM_SCHEDULES_CANNOT_OVERLAP",
        "TARGET_LIMIT_EXCEEDED_FOR_GIVEN_TYPE",
        "TOO_MANY_SCHEDULES_PER_DAY",
        "CANNOT_HAVE_ENABLED_CAMPAIGN_AND_ENABLED_AD_GROUP_TARGETS",
        "DUPLICATE_AD_SCHEDULE",
        "DUPLICATE_KEYWORD",
    ]
    feedItemValidationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "STRING_TOO_SHORT",
        "STRING_TOO_LONG",
        "VALUE_NOT_SPECIFIED",
        "INVALID_DOMESTIC_PHONE_NUMBER_FORMAT",
        "INVALID_PHONE_NUMBER",
        "PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY",
        "PREMIUM_RATE_NUMBER_NOT_ALLOWED",
        "DISALLOWED_NUMBER_TYPE",
        "VALUE_OUT_OF_RANGE",
        "CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY",
        "CUSTOMER_NOT_IN_ALLOWLIST_FOR_CALLTRACKING",
        "INVALID_COUNTRY_CODE",
        "INVALID_APP_ID",
        "MISSING_ATTRIBUTES_FOR_FIELDS",
        "INVALID_TYPE_ID",
        "INVALID_EMAIL_ADDRESS",
        "INVALID_HTTPS_URL",
        "MISSING_DELIVERY_ADDRESS",
        "START_DATE_AFTER_END_DATE",
        "MISSING_FEED_ITEM_START_TIME",
        "MISSING_FEED_ITEM_END_TIME",
        "MISSING_FEED_ITEM_ID",
        "VANITY_PHONE_NUMBER_NOT_ALLOWED",
        "INVALID_REVIEW_EXTENSION_SNIPPET",
        "INVALID_NUMBER_FORMAT",
        "INVALID_DATE_FORMAT",
        "INVALID_PRICE_FORMAT",
        "UNKNOWN_PLACEHOLDER_FIELD",
        "MISSING_ENHANCED_SITELINK_DESCRIPTION_LINE",
        "REVIEW_EXTENSION_SOURCE_INELIGIBLE",
        "HYPHENS_IN_REVIEW_EXTENSION_SNIPPET",
        "DOUBLE_QUOTES_IN_REVIEW_EXTENSION_SNIPPET",
        "QUOTES_IN_REVIEW_EXTENSION_SNIPPET",
        "INVALID_FORM_ENCODED_PARAMS",
        "INVALID_URL_PARAMETER_NAME",
        "NO_GEOCODING_RESULT",
        "SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT",
        "CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED",
        "INVALID_PLACEHOLDER_FIELD_ID",
        "INVALID_URL_TAG",
        "LIST_TOO_LONG",
        "INVALID_ATTRIBUTES_COMBINATION",
        "DUPLICATE_VALUES",
        "INVALID_CALL_CONVERSION_ACTION_ID",
        "CANNOT_SET_WITHOUT_FINAL_URLS",
        "APP_ID_DOESNT_EXIST_IN_APP_STORE",
        "INVALID_FINAL_URL",
        "INVALID_TRACKING_URL",
        "INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL",
        "LIST_TOO_SHORT",
        "INVALID_USER_ACTION",
        "INVALID_TYPE_NAME",
        "INVALID_EVENT_CHANGE_STATUS",
        "INVALID_SNIPPETS_HEADER",
        "INVALID_ANDROID_APP_LINK",
        "NUMBER_TYPE_WITH_CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY",
        "RESERVED_KEYWORD_OTHER",
        "DUPLICATE_OPTION_LABELS",
        "DUPLICATE_OPTION_PREFILLS",
        "UNEQUAL_LIST_LENGTHS",
        "INCONSISTENT_CURRENCY_CODES",
        "PRICE_EXTENSION_HAS_DUPLICATED_HEADERS",
        "ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION",
        "PRICE_EXTENSION_HAS_TOO_FEW_ITEMS",
        "UNSUPPORTED_VALUE",
        "INVALID_FINAL_MOBILE_URL",
        "INVALID_KEYWORDLESS_AD_RULE_LABEL",
        "VALUE_TRACK_PARAMETER_NOT_SUPPORTED",
        "UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE",
        "INVALID_IOS_APP_LINK",
        "MISSING_IOS_APP_LINK_OR_IOS_APP_STORE_ID",
        "PROMOTION_INVALID_TIME",
        "PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF",
        "PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT",
        "TOO_MANY_DECIMAL_PLACES_SPECIFIED",
        "AD_CUSTOMIZERS_NOT_ALLOWED",
        "INVALID_LANGUAGE_CODE",
        "UNSUPPORTED_LANGUAGE",
        "IF_FUNCTION_NOT_ALLOWED",
        "INVALID_FINAL_URL_SUFFIX",
        "INVALID_TAG_IN_FINAL_URL_SUFFIX",
        "INVALID_FINAL_URL_SUFFIX_FORMAT",
        "CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED",
        "ONLY_ONE_DELIVERY_OPTION_IS_ALLOWED",
        "NO_DELIVERY_OPTION_IS_SET",
        "INVALID_CONVERSION_REPORTING_STATE",
        "IMAGE_SIZE_WRONG",
        "EMAIL_DELIVERY_NOT_AVAILABLE_IN_COUNTRY",
        "AUTO_REPLY_NOT_AVAILABLE_IN_COUNTRY",
        "INVALID_LATITUDE_VALUE",
        "INVALID_LONGITUDE_VALUE",
        "TOO_MANY_LABELS",
        "INVALID_IMAGE_URL",
        "MISSING_LATITUDE_VALUE",
        "MISSING_LONGITUDE_VALUE",
        "ADDRESS_NOT_FOUND",
        "ADDRESS_NOT_TARGETABLE",
        "INVALID_ASSET_ID",
        "INCOMPATIBLE_ASSET_TYPE",
        "IMAGE_ERROR_UNEXPECTED_SIZE",
        "IMAGE_ERROR_ASPECT_RATIO_NOT_ALLOWED",
        "IMAGE_ERROR_FILE_TOO_LARGE",
        "IMAGE_ERROR_FORMAT_NOT_ALLOWED",
        "IMAGE_ERROR_CONSTRAINTS_VIOLATED",
        "IMAGE_ERROR_SERVER_ERROR",
    ]
    feedMappingError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_PLACEHOLDER_FIELD",
        "INVALID_CRITERION_FIELD",
        "INVALID_PLACEHOLDER_TYPE",
        "INVALID_CRITERION_TYPE",
        "NO_ATTRIBUTE_FIELD_MAPPINGS",
        "FEED_ATTRIBUTE_TYPE_MISMATCH",
        "CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED",
        "MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE",
        "MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE",
        "MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD",
        "MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD",
        "UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS",
        "LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS",
        "CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED",
        "INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED",
        "INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE",
        "ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD",
        "LEGACY_FEED_TYPE_READ_ONLY",
    ]
    fieldError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUIRED",
        "IMMUTABLE_FIELD",
        "INVALID_VALUE",
        "VALUE_MUST_BE_UNSET",
        "REQUIRED_NONEMPTY_LIST",
        "FIELD_CANNOT_BE_CLEARED",
        "BLOCKED_VALUE",
        "FIELD_CAN_ONLY_BE_CLEARED",
    ]
    fieldMaskError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FIELD_MASK_MISSING",
        "FIELD_MASK_NOT_ALLOWED",
        "FIELD_NOT_FOUND",
        "FIELD_HAS_SUBFIELDS",
    ]
    finalUrlExpansionAssetViewError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MISSING_REQUIRED_FILTER",
        "REQUIRES_ADVERTISING_CHANNEL_TYPE_FILTER",
        "INVALID_ADVERTISING_CHANNEL_TYPE_IN_FILTER",
        "CANNOT_SELECT_ASSET_GROUP",
        "CANNOT_SELECT_AD_GROUP",
        "REQUIRES_FILTER_BY_SINGLE_RESOURCE",
        "CANNOT_SELECT_BOTH_AD_GROUP_AND_ASSET_GROUP",
        "CANNOT_FILTER_BY_BOTH_AD_GROUP_AND_ASSET_GROUP",
    ]
    functionError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_FUNCTION_FORMAT",
        "DATA_TYPE_MISMATCH",
        "INVALID_CONJUNCTION_OPERANDS",
        "INVALID_NUMBER_OF_OPERANDS",
        "INVALID_OPERAND_TYPE",
        "INVALID_OPERATOR",
        "INVALID_REQUEST_CONTEXT_TYPE",
        "INVALID_FUNCTION_FOR_CALL_PLACEHOLDER",
        "INVALID_FUNCTION_FOR_PLACEHOLDER",
        "INVALID_OPERAND",
        "MISSING_CONSTANT_OPERAND_VALUE",
        "INVALID_CONSTANT_OPERAND_VALUE",
        "INVALID_NESTING",
        "MULTIPLE_FEED_IDS_NOT_SUPPORTED",
        "INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA",
        "INVALID_ATTRIBUTE_NAME",
    ]
    functionParsingError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_MORE_INPUT",
        "EXPECTED_CHARACTER",
        "UNEXPECTED_SEPARATOR",
        "UNMATCHED_LEFT_BRACKET",
        "UNMATCHED_RIGHT_BRACKET",
        "TOO_MANY_NESTED_FUNCTIONS",
        "MISSING_RIGHT_HAND_OPERAND",
        "INVALID_OPERATOR_NAME",
        "FEED_ATTRIBUTE_OPERAND_ARGUMENT_NOT_INTEGER",
        "NO_OPERANDS",
        "TOO_MANY_OPERANDS",
    ]
    geoTargetConstantSuggestionError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "LOCATION_NAME_SIZE_LIMIT",
        "LOCATION_NAME_LIMIT",
        "INVALID_COUNTRY_CODE",
        "REQUEST_PARAMETERS_UNSET",
    ]
    goalError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RETENTION_GOAL_ALREADY_EXISTS",
        "HIGH_LIFETIME_VALUE_PRESENT_BUT_VALUE_ABSENT",
        "HIGH_LIFETIME_VALUE_LESS_THAN_OR_EQUAL_TO_VALUE",
        "CUSTOMER_LIFECYCLE_OPTIMIZATION_ACCOUNT_TYPE_NOT_ALLOWED",
    ]
    headerError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_LOGIN_CUSTOMER_ID",
        "INVALID_LINKED_CUSTOMER_ID",
    ]
    idError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "NOT_FOUND"]
    identityVerificationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_EFFECTIVE_BILLING",
        "BILLING_NOT_ON_MONTHLY_INVOICING",
        "VERIFICATION_ALREADY_STARTED",
    ]
    imageError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_IMAGE",
        "STORAGE_ERROR",
        "BAD_REQUEST",
        "UNEXPECTED_SIZE",
        "ANIMATED_NOT_ALLOWED",
        "ANIMATION_TOO_LONG",
        "SERVER_ERROR",
        "CMYK_JPEG_NOT_ALLOWED",
        "FLASH_NOT_ALLOWED",
        "FLASH_WITHOUT_CLICKTAG",
        "FLASH_ERROR_AFTER_FIXING_CLICK_TAG",
        "ANIMATED_VISUAL_EFFECT",
        "FLASH_ERROR",
        "LAYOUT_PROBLEM",
        "PROBLEM_READING_IMAGE_FILE",
        "ERROR_STORING_IMAGE",
        "ASPECT_RATIO_NOT_ALLOWED",
        "FLASH_HAS_NETWORK_OBJECTS",
        "FLASH_HAS_NETWORK_METHODS",
        "FLASH_HAS_URL",
        "FLASH_HAS_MOUSE_TRACKING",
        "FLASH_HAS_RANDOM_NUM",
        "FLASH_SELF_TARGETS",
        "FLASH_BAD_GETURL_TARGET",
        "FLASH_VERSION_NOT_SUPPORTED",
        "FLASH_WITHOUT_HARD_CODED_CLICK_URL",
        "INVALID_FLASH_FILE",
        "FAILED_TO_FIX_CLICK_TAG_IN_FLASH",
        "FLASH_ACCESSES_NETWORK_RESOURCES",
        "FLASH_EXTERNAL_JS_CALL",
        "FLASH_EXTERNAL_FS_CALL",
        "FILE_TOO_LARGE",
        "IMAGE_DATA_TOO_LARGE",
        "IMAGE_PROCESSING_ERROR",
        "IMAGE_TOO_SMALL",
        "INVALID_INPUT",
        "PROBLEM_READING_FILE",
        "IMAGE_CONSTRAINTS_VIOLATED",
        "FORMAT_NOT_ALLOWED",
    ]
    incentiveError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_INCENTIVE_ID"
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
    invoiceError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "YEAR_MONTH_TOO_OLD",
        "NOT_INVOICED_CUSTOMER",
        "BILLING_SETUP_NOT_APPROVED",
        "BILLING_SETUP_NOT_ON_MONTHLY_INVOICING",
        "NON_SERVING_CUSTOMER",
    ]
    keywordPlanAdGroupError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_NAME", "DUPLICATE_NAME"
    ]
    keywordPlanAdGroupKeywordError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_KEYWORD_MATCH_TYPE",
        "DUPLICATE_KEYWORD",
        "KEYWORD_TEXT_TOO_LONG",
        "KEYWORD_HAS_INVALID_CHARS",
        "KEYWORD_HAS_TOO_MANY_WORDS",
        "INVALID_KEYWORD_TEXT",
        "NEGATIVE_KEYWORD_HAS_CPC_BID",
        "NEW_BMM_KEYWORDS_NOT_ALLOWED",
    ]
    keywordPlanCampaignError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_NAME",
        "INVALID_LANGUAGES",
        "INVALID_GEOS",
        "DUPLICATE_NAME",
        "MAX_GEOS_EXCEEDED",
        "MAX_LANGUAGES_EXCEEDED",
    ]
    keywordPlanCampaignKeywordError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "CAMPAIGN_KEYWORD_IS_POSITIVE"
    ]
    keywordPlanError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BID_MULTIPLIER_OUT_OF_RANGE",
        "BID_TOO_HIGH",
        "BID_TOO_LOW",
        "BID_TOO_MANY_FRACTIONAL_DIGITS",
        "DAILY_BUDGET_TOO_LOW",
        "DAILY_BUDGET_TOO_MANY_FRACTIONAL_DIGITS",
        "INVALID_VALUE",
        "KEYWORD_PLAN_HAS_NO_KEYWORDS",
        "KEYWORD_PLAN_NOT_ENABLED",
        "KEYWORD_PLAN_NOT_FOUND",
        "MISSING_BID",
        "MISSING_FORECAST_PERIOD",
        "INVALID_FORECAST_DATE_RANGE",
        "INVALID_NAME",
    ]
    keywordPlanIdeaError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "URL_CRAWL_ERROR", "INVALID_VALUE"
    ]
    labelError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_APPLY_INACTIVE_LABEL",
        "CANNOT_APPLY_LABEL_TO_DISABLED_AD_GROUP_CRITERION",
        "CANNOT_APPLY_LABEL_TO_NEGATIVE_AD_GROUP_CRITERION",
        "EXCEEDED_LABEL_LIMIT_PER_TYPE",
        "INVALID_RESOURCE_FOR_MANAGER_LABEL",
        "DUPLICATE_NAME",
        "INVALID_LABEL_NAME",
        "CANNOT_ATTACH_LABEL_TO_DRAFT",
        "CANNOT_ATTACH_NON_MANAGER_LABEL_TO_CUSTOMER",
    ]
    languageCodeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "LANGUAGE_CODE_NOT_FOUND", "INVALID_LANGUAGE_CODE"
    ]
    listOperationError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "REQUIRED_FIELD_MISSING", "DUPLICATE_VALUES"
    ]
    managerLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING",
        "TOO_MANY_MANAGERS",
        "TOO_MANY_INVITES",
        "ALREADY_INVITED_BY_THIS_MANAGER",
        "ALREADY_MANAGED_BY_THIS_MANAGER",
        "ALREADY_MANAGED_IN_HIERARCHY",
        "DUPLICATE_CHILD_FOUND",
        "CLIENT_HAS_NO_ADMIN_USER",
        "MAX_DEPTH_EXCEEDED",
        "CYCLE_NOT_ALLOWED",
        "TOO_MANY_ACCOUNTS",
        "TOO_MANY_ACCOUNTS_AT_MANAGER",
        "NON_OWNER_USER_CANNOT_MODIFY_LINK",
        "SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS",
        "CLIENT_OUTSIDE_TREE",
        "INVALID_STATUS_CHANGE",
        "INVALID_CHANGE",
        "CUSTOMER_CANNOT_MANAGE_SELF",
        "CREATING_ENABLED_LINK_NOT_ALLOWED",
    ]
    mediaBundleError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BAD_REQUEST",
        "DOUBLECLICK_BUNDLE_NOT_ALLOWED",
        "EXTERNAL_URL_NOT_ALLOWED",
        "FILE_TOO_LARGE",
        "GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED",
        "INVALID_INPUT",
        "INVALID_MEDIA_BUNDLE",
        "INVALID_MEDIA_BUNDLE_ENTRY",
        "INVALID_MIME_TYPE",
        "INVALID_PATH",
        "INVALID_URL_REFERENCE",
        "MEDIA_DATA_TOO_LARGE",
        "MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY",
        "SERVER_ERROR",
        "STORAGE_ERROR",
        "SWIFFY_BUNDLE_NOT_ALLOWED",
        "TOO_MANY_FILES",
        "UNEXPECTED_SIZE",
        "UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT",
        "UNSUPPORTED_HTML5_FEATURE",
        "URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT",
        "CUSTOM_EXIT_NOT_ALLOWED",
    ]
    mediaFileError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_CREATE_STANDARD_ICON",
        "CANNOT_SELECT_STANDARD_ICON_WITH_OTHER_TYPES",
        "CANNOT_SPECIFY_MEDIA_FILE_ID_AND_DATA",
        "DUPLICATE_MEDIA",
        "EMPTY_FIELD",
        "RESOURCE_REFERENCED_IN_MULTIPLE_OPS",
        "FIELD_NOT_SUPPORTED_FOR_MEDIA_SUB_TYPE",
        "INVALID_MEDIA_FILE_ID",
        "INVALID_MEDIA_SUB_TYPE",
        "INVALID_MEDIA_FILE_TYPE",
        "INVALID_MIME_TYPE",
        "INVALID_REFERENCE_ID",
        "INVALID_YOU_TUBE_ID",
        "MEDIA_FILE_FAILED_TRANSCODING",
        "MEDIA_NOT_TRANSCODED",
        "MEDIA_TYPE_DOES_NOT_MATCH_MEDIA_FILE_TYPE",
        "NO_FIELDS_SPECIFIED",
        "NULL_REFERENCE_ID_AND_MEDIA_ID",
        "TOO_LONG",
        "UNSUPPORTED_TYPE",
        "YOU_TUBE_SERVICE_UNAVAILABLE",
        "YOU_TUBE_VIDEO_HAS_NON_POSITIVE_DURATION",
        "YOU_TUBE_VIDEO_NOT_FOUND",
    ]
    mediaUploadError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FILE_TOO_BIG",
        "UNPARSEABLE_IMAGE",
        "ANIMATED_IMAGE_NOT_ALLOWED",
        "FORMAT_NOT_ALLOWED",
        "EXTERNAL_URL_NOT_ALLOWED",
        "INVALID_URL_REFERENCE",
        "MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY",
        "ANIMATED_VISUAL_EFFECT",
        "ANIMATION_TOO_LONG",
        "ASPECT_RATIO_NOT_ALLOWED",
        "AUDIO_NOT_ALLOWED_IN_MEDIA_BUNDLE",
        "CMYK_JPEG_NOT_ALLOWED",
        "FLASH_NOT_ALLOWED",
        "FRAME_RATE_TOO_HIGH",
        "GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED",
        "IMAGE_CONSTRAINTS_VIOLATED",
        "INVALID_MEDIA_BUNDLE",
        "INVALID_MEDIA_BUNDLE_ENTRY",
        "INVALID_MIME_TYPE",
        "INVALID_PATH",
        "LAYOUT_PROBLEM",
        "MALFORMED_URL",
        "MEDIA_BUNDLE_NOT_ALLOWED",
        "MEDIA_BUNDLE_NOT_COMPATIBLE_TO_PRODUCT_TYPE",
        "MEDIA_BUNDLE_REJECTED_BY_MULTIPLE_ASSET_SPECS",
        "TOO_MANY_FILES_IN_MEDIA_BUNDLE",
        "UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT",
        "UNSUPPORTED_HTML5_FEATURE",
        "URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT",
        "VIDEO_FILE_NAME_TOO_LONG",
        "VIDEO_MULTIPLE_FILES_WITH_SAME_NAME",
        "VIDEO_NOT_ALLOWED_IN_MEDIA_BUNDLE",
        "CANNOT_UPLOAD_MEDIA_TYPE_THROUGH_API",
        "DIMENSIONS_NOT_ALLOWED",
    ]
    merchantCenterError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MERCHANT_ID_CANNOT_BE_ACCESSED",
        "CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX",
    ]
    multiplierError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MULTIPLIER_TOO_HIGH",
        "MULTIPLIER_TOO_LOW",
        "TOO_MANY_FRACTIONAL_DIGITS",
        "MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY",
        "MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING",
        "NO_MULTIPLIER_SPECIFIED",
        "MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET",
        "MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET",
        "MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET",
        "MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID",
        "BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER",
        "MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH",
    ]
    mutateError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RESOURCE_NOT_FOUND",
        "ID_EXISTS_IN_MULTIPLE_MUTATES",
        "INCONSISTENT_FIELD_VALUES",
        "MUTATE_NOT_ALLOWED",
        "RESOURCE_NOT_IN_GOOGLE_ADS",
        "RESOURCE_ALREADY_EXISTS",
        "RESOURCE_DOES_NOT_SUPPORT_VALIDATE_ONLY",
        "OPERATION_DOES_NOT_SUPPORT_PARTIAL_FAILURE",
        "RESOURCE_READ_ONLY",
        "EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED",
    ]
    newResourceCreationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_SET_ID_FOR_CREATE",
        "DUPLICATE_TEMP_IDS",
        "TEMP_ID_RESOURCE_HAD_ERRORS",
    ]
    notAllowlistedError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE"
    ]
    notEmptyError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "EMPTY_LIST"]
    nullError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "NULL_CONTENT"]
    offlineUserDataJobError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_USER_LIST_ID",
        "INVALID_USER_LIST_TYPE",
        "NOT_ON_ALLOWLIST_FOR_USER_ID",
        "INCOMPATIBLE_UPLOAD_KEY_TYPE",
        "MISSING_USER_IDENTIFIER",
        "INVALID_MOBILE_ID_FORMAT",
        "TOO_MANY_USER_IDENTIFIERS",
        "NOT_ON_ALLOWLIST_FOR_STORE_SALES_DIRECT",
        "NOT_ON_ALLOWLIST_FOR_UNIFIED_STORE_SALES",
        "INVALID_PARTNER_ID",
        "INVALID_ENCODING",
        "INVALID_COUNTRY_CODE",
        "INCOMPATIBLE_USER_IDENTIFIER",
        "FUTURE_TRANSACTION_TIME",
        "INVALID_CONVERSION_ACTION",
        "MOBILE_ID_NOT_SUPPORTED",
        "INVALID_OPERATION_ORDER",
        "CONFLICTING_OPERATION",
        "EXTERNAL_UPDATE_ID_ALREADY_EXISTS",
        "JOB_ALREADY_STARTED",
        "REMOVE_NOT_SUPPORTED",
        "REMOVE_ALL_NOT_SUPPORTED",
        "INVALID_SHA256_FORMAT",
        "CUSTOM_KEY_DISABLED",
        "CUSTOM_KEY_NOT_PREDEFINED",
        "CUSTOM_KEY_NOT_SET",
        "CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS",
        "ATTRIBUTES_NOT_APPLICABLE_FOR_CUSTOMER_MATCH_USER_LIST",
        "LIFETIME_VALUE_BUCKET_NOT_IN_RANGE",
        "INCOMPATIBLE_USER_IDENTIFIER_FOR_ATTRIBUTES",
        "FUTURE_TIME_NOT_ALLOWED",
        "LAST_PURCHASE_TIME_LESS_THAN_ACQUISITION_TIME",
        "CUSTOMER_IDENTIFIER_NOT_ALLOWED",
        "INVALID_ITEM_ID",
        "FIRST_PURCHASE_TIME_GREATER_THAN_LAST_PURCHASE_TIME",
        "INVALID_LIFECYCLE_STAGE",
        "INVALID_EVENT_VALUE",
        "EVENT_ATTRIBUTE_ALL_FIELDS_ARE_REQUIRED",
        "OPERATION_LEVEL_CONSENT_PROVIDED",
    ]
    operationAccessDeniedError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ACTION_NOT_PERMITTED",
        "CREATE_OPERATION_NOT_PERMITTED",
        "REMOVE_OPERATION_NOT_PERMITTED",
        "UPDATE_OPERATION_NOT_PERMITTED",
        "MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT",
        "OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE",
        "CREATE_AS_REMOVED_NOT_PERMITTED",
        "OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE",
        "OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE",
        "MUTATE_NOT_PERMITTED_FOR_CUSTOMER",
    ]
    operatorError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "OPERATOR_NOT_SUPPORTED"
    ]
    partialFailureError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "PARTIAL_FAILURE_MODE_REQUIRED"
    ]
    paymentsAccountError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "NOT_SUPPORTED_FOR_MANAGER_CUSTOMER"
    ]
    policyFindingError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "POLICY_FINDING", "POLICY_TOPIC_NOT_FOUND"
    ]
    policyValidationParameterError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "UNSUPPORTED_AD_TYPE_FOR_IGNORABLE_POLICY_TOPICS",
        "UNSUPPORTED_AD_TYPE_FOR_EXEMPT_POLICY_VIOLATION_KEYS",
        "CANNOT_SET_BOTH_IGNORABLE_POLICY_TOPICS_AND_EXEMPT_POLICY_VIOLATION_KEYS",
    ]
    policyViolationError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "POLICY_ERROR"
    ]
    productLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_OPERATION",
        "CREATION_NOT_PERMITTED",
        "INVITATION_EXISTS",
        "LINK_EXISTS",
    ]
    productLinkInvitationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_STATUS",
        "PERMISSION_DENIED",
        "NO_INVITATION_REQUIRED",
        "CUSTOMER_NOT_PERMITTED_TO_CREATE_INVITATION",
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
        "PROHIBITED_FIELD_OR_SEGMENT_WITH_METRIC",
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
        "REQUIRED_SEGMENT_FIELD_MISSING",
    ]
    quotaError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RESOURCE_EXHAUSTED",
        "ACCESS_PROHIBITED",
        "RESOURCE_TEMPORARILY_EXHAUSTED",
        "EXCESSIVE_SHORT_TERM_QUERY_RESOURCE_CONSUMPTION",
        "EXCESSIVE_LONG_TERM_QUERY_RESOURCE_CONSUMPTION",
        "PAYMENTS_PROFILE_ACTIVATION_RATE_LIMIT_EXCEEDED",
    ]
    rangeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "TOO_LOW", "TOO_HIGH"
    ]
    reachPlanError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NOT_FORECASTABLE_MISSING_RATE",
        "NOT_FORECASTABLE_NOT_ENOUGH_INVENTORY",
        "NOT_FORECASTABLE_ACCOUNT_NOT_ENABLED",
    ]
    recommendationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BUDGET_AMOUNT_TOO_SMALL",
        "BUDGET_AMOUNT_TOO_LARGE",
        "INVALID_BUDGET_AMOUNT",
        "POLICY_ERROR",
        "INVALID_BID_AMOUNT",
        "ADGROUP_KEYWORD_LIMIT",
        "RECOMMENDATION_ALREADY_APPLIED",
        "RECOMMENDATION_INVALIDATED",
        "TOO_MANY_OPERATIONS",
        "NO_OPERATIONS",
        "DIFFERENT_TYPES_NOT_SUPPORTED",
        "DUPLICATE_RESOURCE_NAME",
        "RECOMMENDATION_ALREADY_DISMISSED",
        "INVALID_APPLY_REQUEST",
        "RECOMMENDATION_TYPE_APPLY_NOT_SUPPORTED",
        "INVALID_MULTIPLIER",
        "ADVERTISING_CHANNEL_TYPE_GENERATE_NOT_SUPPORTED",
        "RECOMMENDATION_TYPE_GENERATE_NOT_SUPPORTED",
        "RECOMMENDATION_TYPES_CANNOT_BE_EMPTY",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_INFO",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_STRATEGY_TYPE",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO_WITH_FINAL_URL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_COUNTRY_CODES_FOR_SEARCH_CHANNEL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_INVALID_COUNTRY_CODE_FOR_SEARCH_CHANNEL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_LANGUAGE_CODES_FOR_SEARCH_CHANNEL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_EITHER_POSITIVE_OR_NEGATIVE_LOCATION_IDS_FOR_SEARCH_CHANNEL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_AD_GROUP_INFO_FOR_SEARCH_CHANNEL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_KEYWORDS_FOR_SEARCH_CHANNEL",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_LOCATION",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_MICROS",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_TARGET_IMPRESSION_SHARE_MICROS_BETWEEN_1_AND_1000000",
        "CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_INFO",
        "MERCHANT_CENTER_ACCOUNT_ID_NOT_SUPPORTED_ADVERTISING_CHANNEL_TYPE",
    ]
    recommendationSubscriptionError: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN"]
    regionCodeError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_REGION_CODE"
    ]
    requestError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RESOURCE_NAME_MISSING",
        "RESOURCE_NAME_MALFORMED",
        "BAD_RESOURCE_ID",
        "INVALID_CUSTOMER_ID",
        "OPERATION_REQUIRED",
        "RESOURCE_NOT_FOUND",
        "INVALID_PAGE_TOKEN",
        "EXPIRED_PAGE_TOKEN",
        "INVALID_PAGE_SIZE",
        "PAGE_SIZE_NOT_SUPPORTED",
        "REQUIRED_FIELD_MISSING",
        "IMMUTABLE_FIELD",
        "TOO_MANY_MUTATE_OPERATIONS",
        "CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT",
        "CANNOT_MODIFY_FOREIGN_FIELD",
        "INVALID_ENUM_VALUE",
        "DEVELOPER_TOKEN_PARAMETER_MISSING",
        "LOGIN_CUSTOMER_ID_PARAMETER_MISSING",
        "VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN",
        "CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS",
        "CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS",
        "INCONSISTENT_RETURN_SUMMARY_ROW_VALUE",
        "TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED",
        "RPC_DEADLINE_TOO_SHORT",
        "UNSUPPORTED_VERSION",
        "CLOUD_PROJECT_NOT_FOUND",
    ]
    resourceAccessDeniedError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "WRITE_ACCESS_DENIED"
    ]
    resourceCountLimitExceededError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ACCOUNT_LIMIT",
        "CAMPAIGN_LIMIT",
        "ADGROUP_LIMIT",
        "AD_GROUP_AD_LIMIT",
        "AD_GROUP_CRITERION_LIMIT",
        "SHARED_SET_LIMIT",
        "MATCHING_FUNCTION_LIMIT",
        "RESPONSE_ROW_LIMIT_EXCEEDED",
        "RESOURCE_LIMIT",
    ]
    searchTermInsightError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FILTERING_NOT_ALLOWED_WITH_SEGMENTS",
        "LIMIT_NOT_ALLOWED_WITH_SEGMENTS",
        "MISSING_FIELD_IN_SELECT_CLAUSE",
        "REQUIRES_FILTER_BY_SINGLE_RESOURCE",
        "SORTING_NOT_ALLOWED_WITH_SEGMENTS",
        "SUMMARY_ROW_NOT_ALLOWED_WITH_SEGMENTS",
    ]
    settingError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SETTING_TYPE_IS_NOT_AVAILABLE",
        "SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN",
        "TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP",
        "TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL",
        "TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP",
        "DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT",
        "DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME",
        "DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME",
        "DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE",
        "TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN",
        "SETTING_VALUE_NOT_COMPATIBLE_WITH_CAMPAIGN",
        "BID_ONLY_IS_NOT_ALLOWED_TO_BE_MODIFIED_WITH_CUSTOMER_MATCH_TARGETING",
    ]
    shareablePreviewError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TOO_MANY_ASSET_GROUPS_IN_REQUEST",
        "ASSET_GROUP_DOES_NOT_EXIST_UNDER_THIS_CUSTOMER",
    ]
    sharedCriterionError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE"
    ]
    sharedSetError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE",
        "DUPLICATE_NAME",
        "SHARED_SET_REMOVED",
        "SHARED_SET_IN_USE",
    ]
    shoppingProductError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MISSING_CAMPAIGN_FILTER",
        "MISSING_AD_GROUP_FILTER",
        "UNSUPPORTED_DATE_SEGMENTATION",
    ]
    sizeLimitError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUEST_SIZE_LIMIT_EXCEEDED",
        "RESPONSE_SIZE_LIMIT_EXCEEDED",
    ]
    smartCampaignError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_BUSINESS_LOCATION_ID",
        "INVALID_CAMPAIGN",
        "BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING",
        "REQUIRED_SUGGESTION_FIELD_MISSING",
        "GEO_TARGETS_REQUIRED",
        "CANNOT_DETERMINE_SUGGESTION_LOCALE",
        "FINAL_URL_NOT_CRAWLABLE",
    ]
    stringFormatError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ILLEGAL_CHARS", "INVALID_FORMAT"
    ]
    stringLengthError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "EMPTY", "TOO_SHORT", "TOO_LONG"
    ]
    thirdPartyAppAnalyticsLinkError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_ANALYTICS_PROVIDER_ID",
        "INVALID_MOBILE_APP_ID",
        "MOBILE_APP_IS_NOT_ENABLED",
        "CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK",
    ]
    timeZoneError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_TIME_ZONE"
    ]
    urlFieldError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_TRACKING_URL_TEMPLATE",
        "INVALID_TAG_IN_TRACKING_URL_TEMPLATE",
        "MISSING_TRACKING_URL_TEMPLATE_TAG",
        "MISSING_PROTOCOL_IN_TRACKING_URL_TEMPLATE",
        "INVALID_PROTOCOL_IN_TRACKING_URL_TEMPLATE",
        "MALFORMED_TRACKING_URL_TEMPLATE",
        "MISSING_HOST_IN_TRACKING_URL_TEMPLATE",
        "INVALID_TLD_IN_TRACKING_URL_TEMPLATE",
        "REDUNDANT_NESTED_TRACKING_URL_TEMPLATE_TAG",
        "INVALID_FINAL_URL",
        "INVALID_TAG_IN_FINAL_URL",
        "REDUNDANT_NESTED_FINAL_URL_TAG",
        "MISSING_PROTOCOL_IN_FINAL_URL",
        "INVALID_PROTOCOL_IN_FINAL_URL",
        "MALFORMED_FINAL_URL",
        "MISSING_HOST_IN_FINAL_URL",
        "INVALID_TLD_IN_FINAL_URL",
        "INVALID_FINAL_MOBILE_URL",
        "INVALID_TAG_IN_FINAL_MOBILE_URL",
        "REDUNDANT_NESTED_FINAL_MOBILE_URL_TAG",
        "MISSING_PROTOCOL_IN_FINAL_MOBILE_URL",
        "INVALID_PROTOCOL_IN_FINAL_MOBILE_URL",
        "MALFORMED_FINAL_MOBILE_URL",
        "MISSING_HOST_IN_FINAL_MOBILE_URL",
        "INVALID_TLD_IN_FINAL_MOBILE_URL",
        "INVALID_FINAL_APP_URL",
        "INVALID_TAG_IN_FINAL_APP_URL",
        "REDUNDANT_NESTED_FINAL_APP_URL_TAG",
        "MULTIPLE_APP_URLS_FOR_OSTYPE",
        "INVALID_OSTYPE",
        "INVALID_PROTOCOL_FOR_APP_URL",
        "INVALID_PACKAGE_ID_FOR_APP_URL",
        "URL_CUSTOM_PARAMETERS_COUNT_EXCEEDS_LIMIT",
        "INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_KEY",
        "INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_VALUE",
        "INVALID_TAG_IN_URL_CUSTOM_PARAMETER_VALUE",
        "REDUNDANT_NESTED_URL_CUSTOM_PARAMETER_TAG",
        "MISSING_PROTOCOL",
        "INVALID_PROTOCOL",
        "INVALID_URL",
        "DESTINATION_URL_DEPRECATED",
        "INVALID_TAG_IN_URL",
        "MISSING_URL_TAG",
        "DUPLICATE_URL_ID",
        "INVALID_URL_ID",
        "FINAL_URL_SUFFIX_MALFORMED",
        "INVALID_TAG_IN_FINAL_URL_SUFFIX",
        "INVALID_TOP_LEVEL_DOMAIN",
        "MALFORMED_TOP_LEVEL_DOMAIN",
        "MALFORMED_URL",
        "MISSING_HOST",
        "NULL_CUSTOM_PARAMETER_VALUE",
        "VALUE_TRACK_PARAMETER_NOT_SUPPORTED",
        "UNSUPPORTED_APP_STORE",
    ]
    userDataError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED",
        "TOO_MANY_USER_IDENTIFIERS",
        "USER_LIST_NOT_APPLICABLE",
    ]
    userListCustomerTypeError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONFLICTING_CUSTOMER_TYPES",
        "NO_ACCESS_TO_USER_LIST",
        "USERLIST_NOT_ELIGIBLE",
        "CONVERSION_TRACKING_NOT_ENABLED_OR_NOT_MCC_MANAGER_ACCOUNT",
        "TOO_MANY_USER_LISTS_FOR_THE_CUSTOMER_TYPE",
    ]
    userListError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXTERNAL_REMARKETING_USER_LIST_MUTATE_NOT_SUPPORTED",
        "CONCRETE_TYPE_REQUIRED",
        "CONVERSION_TYPE_ID_REQUIRED",
        "DUPLICATE_CONVERSION_TYPES",
        "INVALID_CONVERSION_TYPE",
        "INVALID_DESCRIPTION",
        "INVALID_NAME",
        "INVALID_TYPE",
        "CAN_NOT_ADD_LOGICAL_LIST_AS_LOGICAL_LIST_OPERAND",
        "INVALID_USER_LIST_LOGICAL_RULE_OPERAND",
        "NAME_ALREADY_USED",
        "NEW_CONVERSION_TYPE_NAME_REQUIRED",
        "CONVERSION_TYPE_NAME_ALREADY_USED",
        "OWNERSHIP_REQUIRED_FOR_SET",
        "USER_LIST_MUTATE_NOT_SUPPORTED",
        "INVALID_RULE",
        "INVALID_DATE_RANGE",
        "CAN_NOT_MUTATE_SENSITIVE_USERLIST",
        "MAX_NUM_RULEBASED_USERLISTS",
        "CANNOT_MODIFY_BILLABLE_RECORD_COUNT",
        "APP_ID_NOT_SET",
        "USERLIST_NAME_IS_RESERVED_FOR_SYSTEM_LIST",
        "ADVERTISER_NOT_ON_ALLOWLIST_FOR_USING_UPLOADED_DATA",
        "RULE_TYPE_IS_NOT_SUPPORTED",
        "CAN_NOT_ADD_A_SIMILAR_USERLIST_AS_LOGICAL_LIST_OPERAND",
        "CAN_NOT_MIX_CRM_BASED_IN_LOGICAL_LIST_WITH_OTHER_LISTS",
        "APP_ID_NOT_ALLOWED",
        "CANNOT_MUTATE_SYSTEM_LIST",
        "MOBILE_APP_IS_SENSITIVE",
        "SEED_LIST_DOES_NOT_EXIST",
        "INVALID_SEED_LIST_ACCESS_REASON",
        "INVALID_SEED_LIST_TYPE",
        "INVALID_COUNTRY_CODES",
        "PARTNER_AUDIENCE_SOURCE_NOT_SUPPORTED_FOR_USER_LIST_TYPE",
        "COMMERCE_PARTNER_NOT_ALLOWED",
        "PARTNER_AUDIENCE_INFO_NOT_SUPPORTED_FOR_USER_LIST_TYPE",
        "PARTNER_MANAGER_ACCOUNT_DISALLOWED",
        "PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA",
        "ADVERTISER_TOS_NOT_ACCEPTED",
        "ADVERTISER_PARTNER_LINK_MISSING",
        "ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA",
        "ACCOUNT_SETTING_TYPE_NOT_ALLOWED",
    ]
    videoCampaignError: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "MUTATE_REQUIRES_RESERVATION"
    ]
    youtubeVideoRegistrationError: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "VIDEO_NOT_FOUND",
        "VIDEO_NOT_ACCESSIBLE",
        "VIDEO_NOT_ELIGIBLE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ErrorDetails(
    typing_extensions.TypedDict, total=False
):
    budgetPerDayMinimumErrorDetails: (
        GoogleAdsSearchads360V23Errors__BudgetPerDayMinimumErrorDetails
    )
    policyFindingDetails: GoogleAdsSearchads360V23Errors__PolicyFindingDetails
    policyViolationDetails: GoogleAdsSearchads360V23Errors__PolicyViolationDetails
    quotaErrorDetails: GoogleAdsSearchads360V23Errors__QuotaErrorDetails
    resourceCountDetails: GoogleAdsSearchads360V23Errors__ResourceCountDetails
    unpublishedErrorCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ErrorLocation(
    typing_extensions.TypedDict, total=False
):
    fieldPathElements: _list[
        GoogleAdsSearchads360V23Errors_ErrorLocation_FieldPathElement
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__PolicyFindingDetails(
    typing_extensions.TypedDict, total=False
):
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__PolicyViolationDetails(
    typing_extensions.TypedDict, total=False
):
    externalPolicyDescription: str
    externalPolicyName: str
    isExemptible: bool
    key: GoogleAdsSearchads360V23Common__PolicyViolationKey

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__QuotaErrorDetails(
    typing_extensions.TypedDict, total=False
):
    rateName: str
    rateScope: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACCOUNT", "DEVELOPER"
    ]
    retryDelay: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ResourceCountDetails(
    typing_extensions.TypedDict, total=False
):
    enclosingId: str
    enclosingResource: str
    existingCount: int
    limit: int
    limitType: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGNS_PER_CUSTOMER",
        "BASE_CAMPAIGNS_PER_CUSTOMER",
        "EXPERIMENT_CAMPAIGNS_PER_CUSTOMER",
        "HOTEL_CAMPAIGNS_PER_CUSTOMER",
        "SMART_SHOPPING_CAMPAIGNS_PER_CUSTOMER",
        "AD_GROUPS_PER_CAMPAIGN",
        "AD_GROUPS_PER_SHOPPING_CAMPAIGN",
        "AD_GROUPS_PER_HOTEL_CAMPAIGN",
        "REPORTING_AD_GROUPS_PER_LOCAL_CAMPAIGN",
        "REPORTING_AD_GROUPS_PER_APP_CAMPAIGN",
        "MANAGED_AD_GROUPS_PER_SMART_CAMPAIGN",
        "AD_GROUP_CRITERIA_PER_CUSTOMER",
        "BASE_AD_GROUP_CRITERIA_PER_CUSTOMER",
        "EXPERIMENT_AD_GROUP_CRITERIA_PER_CUSTOMER",
        "AD_GROUP_CRITERIA_PER_CAMPAIGN",
        "CAMPAIGN_CRITERIA_PER_CUSTOMER",
        "BASE_CAMPAIGN_CRITERIA_PER_CUSTOMER",
        "EXPERIMENT_CAMPAIGN_CRITERIA_PER_CUSTOMER",
        "WEBPAGE_CRITERIA_PER_CUSTOMER",
        "BASE_WEBPAGE_CRITERIA_PER_CUSTOMER",
        "EXPERIMENT_WEBPAGE_CRITERIA_PER_CUSTOMER",
        "COMBINED_AUDIENCE_CRITERIA_PER_AD_GROUP",
        "CUSTOMER_NEGATIVE_PLACEMENT_CRITERIA_PER_CUSTOMER",
        "CUSTOMER_NEGATIVE_YOUTUBE_CHANNEL_CRITERIA_PER_CUSTOMER",
        "CRITERIA_PER_AD_GROUP",
        "LISTING_GROUPS_PER_AD_GROUP",
        "EXPLICITLY_SHARED_BUDGETS_PER_CUSTOMER",
        "IMPLICITLY_SHARED_BUDGETS_PER_CUSTOMER",
        "COMBINED_AUDIENCE_CRITERIA_PER_CAMPAIGN",
        "NEGATIVE_KEYWORDS_PER_CAMPAIGN",
        "NEGATIVE_PLACEMENTS_PER_CAMPAIGN",
        "GEO_TARGETS_PER_CAMPAIGN",
        "NEGATIVE_IP_BLOCKS_PER_CAMPAIGN",
        "PROXIMITIES_PER_CAMPAIGN",
        "LISTING_SCOPES_PER_SHOPPING_CAMPAIGN",
        "LISTING_SCOPES_PER_NON_SHOPPING_CAMPAIGN",
        "NEGATIVE_KEYWORDS_PER_SHARED_SET",
        "NEGATIVE_PLACEMENTS_PER_SHARED_SET",
        "SHARED_SETS_PER_CUSTOMER_FOR_TYPE_DEFAULT",
        "SHARED_SETS_PER_CUSTOMER_FOR_NEGATIVE_PLACEMENT_LIST_LOWER",
        "HOTEL_ADVANCE_BOOKING_WINDOW_BID_MODIFIERS_PER_AD_GROUP",
        "BIDDING_STRATEGIES_PER_CUSTOMER",
        "BASIC_USER_LISTS_PER_CUSTOMER",
        "LOGICAL_USER_LISTS_PER_CUSTOMER",
        "RULE_BASED_USER_LISTS_PER_CUSTOMER",
        "BASE_AD_GROUP_ADS_PER_CUSTOMER",
        "EXPERIMENT_AD_GROUP_ADS_PER_CUSTOMER",
        "AD_GROUP_ADS_PER_CAMPAIGN",
        "TEXT_AND_OTHER_ADS_PER_AD_GROUP",
        "IMAGE_ADS_PER_AD_GROUP",
        "SHOPPING_SMART_ADS_PER_AD_GROUP",
        "RESPONSIVE_SEARCH_ADS_PER_AD_GROUP",
        "APP_ADS_PER_AD_GROUP",
        "APP_ENGAGEMENT_ADS_PER_AD_GROUP",
        "LOCAL_ADS_PER_AD_GROUP",
        "VIDEO_ADS_PER_AD_GROUP",
        "LEAD_FORM_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "PROMOTION_CUSTOMER_ASSETS_PER_CUSTOMER",
        "PROMOTION_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "PROMOTION_AD_GROUP_ASSETS_PER_AD_GROUP",
        "CALLOUT_CUSTOMER_ASSETS_PER_CUSTOMER",
        "CALLOUT_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "CALLOUT_AD_GROUP_ASSETS_PER_AD_GROUP",
        "SITELINK_CUSTOMER_ASSETS_PER_CUSTOMER",
        "SITELINK_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "SITELINK_AD_GROUP_ASSETS_PER_AD_GROUP",
        "STRUCTURED_SNIPPET_CUSTOMER_ASSETS_PER_CUSTOMER",
        "STRUCTURED_SNIPPET_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "STRUCTURED_SNIPPET_AD_GROUP_ASSETS_PER_AD_GROUP",
        "MOBILE_APP_CUSTOMER_ASSETS_PER_CUSTOMER",
        "MOBILE_APP_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "MOBILE_APP_AD_GROUP_ASSETS_PER_AD_GROUP",
        "HOTEL_CALLOUT_CUSTOMER_ASSETS_PER_CUSTOMER",
        "HOTEL_CALLOUT_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "HOTEL_CALLOUT_AD_GROUP_ASSETS_PER_AD_GROUP",
        "CALL_CUSTOMER_ASSETS_PER_CUSTOMER",
        "CALL_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "CALL_AD_GROUP_ASSETS_PER_AD_GROUP",
        "PRICE_CUSTOMER_ASSETS_PER_CUSTOMER",
        "PRICE_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "PRICE_AD_GROUP_ASSETS_PER_AD_GROUP",
        "AD_IMAGE_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "AD_IMAGE_AD_GROUP_ASSETS_PER_AD_GROUP",
        "PAGE_FEED_ASSET_SETS_PER_CUSTOMER",
        "DYNAMIC_EDUCATION_FEED_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_PAGE_FEED_ASSET_SET",
        "ASSETS_PER_DYNAMIC_EDUCATION_FEED_ASSET_SET",
        "DYNAMIC_REAL_ESTATE_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_REAL_ESTATE_ASSET_SET",
        "DYNAMIC_CUSTOM_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_CUSTOM_ASSET_SET",
        "DYNAMIC_HOTELS_AND_RENTALS_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_HOTELS_AND_RENTALS_ASSET_SET",
        "DYNAMIC_LOCAL_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_LOCAL_ASSET_SET",
        "DYNAMIC_FLIGHTS_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_FLIGHTS_ASSET_SET",
        "DYNAMIC_TRAVEL_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_TRAVEL_ASSET_SET",
        "DYNAMIC_JOBS_ASSET_SETS_PER_CUSTOMER",
        "ASSETS_PER_DYNAMIC_JOBS_ASSET_SET",
        "BUSINESS_NAME_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "BUSINESS_LOGO_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "VERSIONS_PER_AD",
        "USER_FEEDS_PER_CUSTOMER",
        "SYSTEM_FEEDS_PER_CUSTOMER",
        "FEED_ATTRIBUTES_PER_FEED",
        "FEED_ITEMS_PER_CUSTOMER",
        "CAMPAIGN_FEEDS_PER_CUSTOMER",
        "BASE_CAMPAIGN_FEEDS_PER_CUSTOMER",
        "EXPERIMENT_CAMPAIGN_FEEDS_PER_CUSTOMER",
        "AD_GROUP_FEEDS_PER_CUSTOMER",
        "BASE_AD_GROUP_FEEDS_PER_CUSTOMER",
        "EXPERIMENT_AD_GROUP_FEEDS_PER_CUSTOMER",
        "AD_GROUP_FEEDS_PER_CAMPAIGN",
        "FEED_ITEM_SETS_PER_CUSTOMER",
        "FEED_ITEMS_PER_FEED_ITEM_SET",
        "CAMPAIGN_EXPERIMENTS_PER_CUSTOMER",
        "EXPERIMENT_ARMS_PER_VIDEO_EXPERIMENT",
        "OWNED_LABELS_PER_CUSTOMER",
        "LABELS_PER_CAMPAIGN",
        "LABELS_PER_AD_GROUP",
        "LABELS_PER_AD_GROUP_AD",
        "LABELS_PER_AD_GROUP_CRITERION",
        "TARGET_CUSTOMERS_PER_LABEL",
        "KEYWORD_PLANS_PER_USER_PER_CUSTOMER",
        "KEYWORD_PLAN_AD_GROUP_KEYWORDS_PER_KEYWORD_PLAN",
        "KEYWORD_PLAN_AD_GROUPS_PER_KEYWORD_PLAN",
        "KEYWORD_PLAN_NEGATIVE_KEYWORDS_PER_KEYWORD_PLAN",
        "KEYWORD_PLAN_CAMPAIGNS_PER_KEYWORD_PLAN",
        "CONVERSION_ACTIONS_PER_CUSTOMER",
        "BATCH_JOB_OPERATIONS_PER_JOB",
        "BATCH_JOBS_PER_CUSTOMER",
        "HOTEL_CHECK_IN_DATE_RANGE_BID_MODIFIERS_PER_AD_GROUP",
        "SHARED_SETS_PER_ACCOUNT_FOR_ACCOUNT_LEVEL_NEGATIVE_KEYWORDS",
        "ACCOUNT_LEVEL_NEGATIVE_KEYWORDS_PER_SHARED_SET",
        "ENABLED_ASSET_PER_HOTEL_PROPERTY_ASSET_SET",
        "ENABLED_HOTEL_PROPERTY_ASSET_LINKS_PER_ASSET_GROUP",
        "BRANDS_PER_SHARED_SET",
        "ENABLED_BRAND_LIST_CRITERIA_PER_CAMPAIGN",
        "SHARED_SETS_PER_ACCOUNT_FOR_BRAND",
        "LOOKALIKE_USER_LISTS_PER_CUSTOMER",
        "LOGO_CAMPAIGN_ASSETS_PER_CAMPAIGN",
        "BUSINESS_MESSAGE_ASSET_LINKS_PER_CUSTOMER",
        "WHATSAPP_BUSINESS_MESSAGE_ASSET_LINKS_PER_CAMPAIGN",
        "WHATSAPP_BUSINESS_MESSAGE_ASSET_LINKS_PER_AD_GROUP",
        "BRAND_LIST_CRITERIA_PER_AD_GROUP",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__SearchAds360Error(
    typing_extensions.TypedDict, total=False
):
    details: GoogleAdsSearchads360V23Errors__ErrorDetails
    errorCode: GoogleAdsSearchads360V23Errors__ErrorCode
    location: GoogleAdsSearchads360V23Errors__ErrorLocation
    message: str
    trigger: GoogleAdsSearchads360V23Common__Value

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__SearchAds360Failure(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleAdsSearchads360V23Errors__SearchAds360Error]
    requestId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_BatchJob_BatchJobMetadata(
    typing_extensions.TypedDict, total=False
):
    completionDateTime: str
    creationDateTime: str
    estimatedCompletionRatio: float
    executedOperationCount: str
    executionLimitSeconds: int
    operationCount: str
    startDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineUserDataJobMetadata(
    typing_extensions.TypedDict, total=False
):
    matchRateRange: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MATCH_RANGE_LESS_THAN_20",
        "MATCH_RANGE_20_TO_30",
        "MATCH_RANGE_31_TO_40",
        "MATCH_RANGE_41_TO_50",
        "MATCH_RANGE_51_TO_60",
        "MATCH_RANGE_61_TO_70",
        "MATCH_RANGE_71_TO_80",
        "MATCH_RANGE_81_TO_90",
        "MATCH_RANGE_91_TO_100",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PromoteExperimentMetadata(
    typing_extensions.TypedDict, total=False
):
    experiment: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ScheduleExperimentMetadata(
    typing_extensions.TypedDict, total=False
):
    experiment: str
