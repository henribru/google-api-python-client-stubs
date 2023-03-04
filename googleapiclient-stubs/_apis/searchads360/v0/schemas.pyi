import typing

import typing_extensions

_list = list

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
    clicks: str
    clientAccountConversions: float
    clientAccountConversionsValue: float
    clientAccountViewThroughConversions: str
    contentBudgetLostImpressionShare: float
    contentImpressionShare: float
    contentRankLostImpressionShare: float
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
    crossDeviceConversionsValue: float
    ctr: float
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
    interactionEventTypes: _list[str]
    interactionRate: float
    interactions: str
    invalidClickRate: float
    invalidClicks: str
    mobileFriendlyClicksPercentage: float
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
class GoogleAdsSearchads360V0Common__Segments(typing_extensions.TypedDict, total=False):
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
    month: str
    quarter: str
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
        "UNSPECIFIED",
        "UNKNOWN",
        "RESOURCE_EXHAUSTED",
        "ACCESS_PROHIBITED",
        "RESOURCE_TEMPORARILY_EXHAUSTED",
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
    optimizationGoalTypes: _list[str]

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
class GoogleAdsSearchads360V0Resources__AdGroup(
    typing_extensions.TypedDict, total=False
):
    adRotationMode: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "OPTIMIZE", "ROTATE_FOREVER"
    ]
    cpcBidMicros: str
    id: str
    name: str
    resourceName: str
    status: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"
    ]
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
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupBidModifier(
    typing_extensions.TypedDict, total=False
):
    bidModifier: float
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__AdGroupCriterion(
    typing_extensions.TypedDict, total=False
):
    adGroup: str
    ageRange: GoogleAdsSearchads360V0Common__AgeRangeInfo
    bidModifier: float
    cpcBidMicros: str
    criterionId: str
    effectiveCpcBidMicros: str
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
    lastModifiedTime: str
    listingGroup: GoogleAdsSearchads360V0Common__ListingGroupInfo
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
    ]
    webpage: GoogleAdsSearchads360V0Common__WebpageInfo

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
    dynamicSearchAdsSetting: GoogleAdsSearchads360V0Resources_Campaign_DynamicSearchAdsSetting
    endDate: str
    engineId: str
    excludedParentAssetFieldTypes: _list[str]
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
    optimizationGoalSetting: GoogleAdsSearchads360V0Resources_Campaign_OptimizationGoalSetting
    percentCpc: GoogleAdsSearchads360V0Common__PercentCpc
    realTimeBiddingSetting: GoogleAdsSearchads360V0Common__RealTimeBiddingSetting
    resourceName: str
    selectiveOptimization: GoogleAdsSearchads360V0Resources_Campaign_SelectiveOptimization
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
    bidModifier: float
    criterionId: str
    device: GoogleAdsSearchads360V0Common__DeviceInfo
    displayName: str
    language: GoogleAdsSearchads360V0Common__LanguageInfo
    location: GoogleAdsSearchads360V0Common__LocationInfo
    locationGroup: GoogleAdsSearchads360V0Common__LocationGroupInfo
    negative: bool
    resourceName: str
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
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__ConversionAction(
    typing_extensions.TypedDict, total=False
):
    appId: str
    attributionModelSettings: GoogleAdsSearchads360V0Resources_ConversionAction_AttributionModelSettings
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
    floodlightSettings: GoogleAdsSearchads360V0Resources_ConversionAction_FloodlightSettings
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
    ]
    valueSettings: GoogleAdsSearchads360V0Resources_ConversionAction_ValueSettings

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
    resourceName: str
    valueType: typing_extensions.Literal[
        "UNSPECIFIED", "UNKNOWN", "STRING", "INT64", "DOUBLE", "BOOLEAN"
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
    conversionTrackingSetting: GoogleAdsSearchads360V0Resources__ConversionTrackingSetting
    currencyCode: str
    descriptiveName: str
    doubleClickCampaignManagerSetting: GoogleAdsSearchads360V0Resources__DoubleClickCampaignManagerSetting
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
class GoogleAdsSearchads360V0Resources__KeywordView(
    typing_extensions.TypedDict, total=False
):
    resourceName: str

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
class GoogleAdsSearchads360V0Services__CustomColumnHeader(
    typing_extensions.TypedDict, total=False
):
    id: str
    name: str
    referencesMetrics: bool

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ListCustomColumnsResponse(
    typing_extensions.TypedDict, total=False
):
    customColumns: _list[GoogleAdsSearchads360V0Resources__CustomColumn]

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchAds360Row(
    typing_extensions.TypedDict, total=False
):
    adGroup: GoogleAdsSearchads360V0Resources__AdGroup
    adGroupBidModifier: GoogleAdsSearchads360V0Resources__AdGroupBidModifier
    adGroupCriterion: GoogleAdsSearchads360V0Resources__AdGroupCriterion
    biddingStrategy: GoogleAdsSearchads360V0Resources__BiddingStrategy
    campaign: GoogleAdsSearchads360V0Resources__Campaign
    campaignBudget: GoogleAdsSearchads360V0Resources__CampaignBudget
    campaignCriterion: GoogleAdsSearchads360V0Resources__CampaignCriterion
    conversionAction: GoogleAdsSearchads360V0Resources__ConversionAction
    customColumns: _list[GoogleAdsSearchads360V0Common__Value]
    customer: GoogleAdsSearchads360V0Resources__Customer
    customerClient: GoogleAdsSearchads360V0Resources__CustomerClient
    customerManagerLink: GoogleAdsSearchads360V0Resources__CustomerManagerLink
    keywordView: GoogleAdsSearchads360V0Resources__KeywordView
    metrics: GoogleAdsSearchads360V0Common__Metrics
    productGroupView: GoogleAdsSearchads360V0Resources__ProductGroupView
    segments: GoogleAdsSearchads360V0Common__Segments

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
    customColumnHeaders: _list[GoogleAdsSearchads360V0Services__CustomColumnHeader]
    fieldMask: str
    nextPageToken: str
    results: _list[GoogleAdsSearchads360V0Services__SearchAds360Row]
    summaryRow: GoogleAdsSearchads360V0Services__SearchAds360Row
    totalResultsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360StreamRequest(
    typing_extensions.TypedDict, total=False
):
    batchSize: int
    query: str
    summaryRowSetting: typing_extensions.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_SUMMARY_ROW",
        "SUMMARY_ROW_WITH_RESULTS",
        "SUMMARY_ROW_ONLY",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360StreamResponse(
    typing_extensions.TypedDict, total=False
):
    customColumnHeaders: _list[GoogleAdsSearchads360V0Services__CustomColumnHeader]
    fieldMask: str
    requestId: str
    results: _list[GoogleAdsSearchads360V0Services__SearchAds360Row]
    summaryRow: GoogleAdsSearchads360V0Services__SearchAds360Row
