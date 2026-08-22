import typing

_list = list

@typing.type_check_only
class GoogleAdsSearchads360V0Common__Value(typing.TypedDict, total=False):
    booleanValue: bool
    doubleValue: float
    floatValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElement(
    typing.TypedDict, total=False
):
    fieldName: str
    index: int

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__ErrorCode(typing.TypedDict, total=False):
    authenticationError: typing.Literal[
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
    authorizationError: typing.Literal[
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
    conversionCustomVariableError: typing.Literal[
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
    customColumnError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOM_COLUMN_NOT_FOUND",
        "CUSTOM_COLUMN_NOT_AVAILABLE",
    ]
    dateError: typing.Literal[
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
    dateRangeError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_DATE",
        "START_DATE_AFTER_END_DATE",
        "CANNOT_SET_DATE_TO_PAST",
        "AFTER_MAXIMUM_ALLOWABLE_DATE",
        "CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED",
        "REQUESTED_DATE_GRANULARITY_NOT_SUPPORTED",
    ]
    distinctError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_ELEMENT", "DUPLICATE_TYPE"
    ]
    headerError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_USER_SELECTED_CUSTOMER_ID",
        "INVALID_LOGIN_CUSTOMER_ID",
    ]
    internalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INTERNAL_ERROR",
        "ERROR_CODE_NOT_PUBLISHED",
        "TRANSIENT_ERROR",
        "DEADLINE_EXCEEDED",
    ]
    invalidParameterError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_CURRENCY_CODE"
    ]
    queryError: typing.Literal[
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
    quotaError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "RESOURCE_EXHAUSTED", "RESOURCE_TEMPORARILY_EXHAUSTED"
    ]
    requestError: typing.Literal[
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
    sizeLimitError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUEST_SIZE_LIMIT_EXCEEDED",
        "RESPONSE_SIZE_LIMIT_EXCEEDED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__ErrorDetails(typing.TypedDict, total=False):
    quotaErrorDetails: GoogleAdsSearchads360V0Errors__QuotaErrorDetails
    unpublishedErrorCode: str

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__ErrorLocation(typing.TypedDict, total=False):
    fieldPathElements: _list[
        GoogleAdsSearchads360V0Errors_ErrorLocation_FieldPathElement
    ]

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__QuotaErrorDetails(typing.TypedDict, total=False):
    rateName: str
    rateScope: typing.Literal["UNSPECIFIED", "UNKNOWN", "ACCOUNT", "DEVELOPER"]
    retryDelay: str

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__SearchAds360Error(typing.TypedDict, total=False):
    details: GoogleAdsSearchads360V0Errors__ErrorDetails
    errorCode: GoogleAdsSearchads360V0Errors__ErrorCode
    location: GoogleAdsSearchads360V0Errors__ErrorLocation
    message: str
    trigger: GoogleAdsSearchads360V0Common__Value

@typing.type_check_only
class GoogleAdsSearchads360V0Errors__SearchAds360Failure(typing.TypedDict, total=False):
    errors: _list[GoogleAdsSearchads360V0Errors__SearchAds360Error]
    requestId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common_CampaignGoalSettings_CampaignLoyaltyRetentionGoalSettings(
    typing.TypedDict, total=False
):
    enableBidAdjustmentsForLoyaltyMembers: bool
    showTargetedLoyaltyMemberBenefitsInPla: bool
    valueSettingsOverride: (
        GoogleAdsSearchads360V23Common__CustomerLifecycleOptimizationValueSettings
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common_CampaignGoalSettings_CampaignNewCustomerAcquisitionGoalSettings(
    typing.TypedDict, total=False
):
    targetOption: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "TARGET_ALL", "TARGET_SPECIFIC"
    ]
    valueSettingsOverride: (
        GoogleAdsSearchads360V23Common__CustomerLifecycleOptimizationValueSettings
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common_CampaignGoalSettings_CampaignRetentionGoalSettings(
    typing.TypedDict, total=False
):
    targetOption: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "TARGET_ALL", "TARGET_SPECIFIC"
    ]
    valueSettingsOverride: (
        GoogleAdsSearchads360V23Common__CustomerLifecycleOptimizationValueSettings
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common_GoalSetting_RetentionGoal(
    typing.TypedDict, total=False
):
    valueSettings: (
        GoogleAdsSearchads360V23Common__CustomerLifecycleOptimizationValueSettings
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common_LineupAttributeMetadata_SampleChannel(
    typing.TypedDict, total=False
):
    displayName: str
    youtubeChannel: GoogleAdsSearchads360V23Common__YouTubeChannelInfo
    youtubeChannelMetadata: (
        GoogleAdsSearchads360V23Common__YouTubeChannelAttributeMetadata
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraint(
    typing.TypedDict, total=False
):
    countryCriterion: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraintList(
    typing.TypedDict, total=False
):
    countries: _list[
        GoogleAdsSearchads360V23Common_PolicyTopicConstraint_CountryConstraint
    ]
    totalTargetedCountries: int

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicConstraint_ResellerConstraint(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationMismatch(
    typing.TypedDict, total=False
):
    urlTypes: _list[
        typing.Literal[
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
    typing.TypedDict, total=False
):
    device: typing.Literal["UNSPECIFIED", "UNKNOWN", "DESKTOP", "ANDROID", "IOS"]
    dnsErrorType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "HOSTNAME_NOT_FOUND", "GOOGLE_CRAWLER_DNS_ISSUE"
    ]
    expandedUrl: str
    httpErrorCode: str
    lastCheckedDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_DestinationTextList(
    typing.TypedDict, total=False
):
    destinationTexts: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_TextList(
    typing.TypedDict, total=False
):
    texts: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common_PolicyTopicEvidence_WebsiteList(
    typing.TypedDict, total=False
):
    websites: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ActivityCityInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ActivityCountryInfo(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ActivityIdInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ActivityRatingInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ActivityStateInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdAppDeepLinkAsset(typing.TypedDict, total=False):
    asset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdAssetPolicySummary(
    typing.TypedDict, total=False
):
    approvalStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISAPPROVED",
        "APPROVED_LIMITED",
        "APPROVED",
        "AREA_OF_INTEREST_ONLY",
    ]
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]
    reviewStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REVIEW_IN_PROGRESS",
        "REVIEWED",
        "UNDER_APPEAL",
        "ELIGIBLE_MAY_SERVE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdCallToActionAsset(
    typing.TypedDict, total=False
):
    asset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdDemandGenCarouselCardAsset(
    typing.TypedDict, total=False
):
    asset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdImageAsset(typing.TypedDict, total=False):
    asset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdMediaBundleAsset(typing.TypedDict, total=False):
    asset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdScheduleInfo(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
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
    endMinute: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ZERO", "FIFTEEN", "THIRTY", "FORTY_FIVE"
    ]
    startHour: int
    startMinute: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ZERO", "FIFTEEN", "THIRTY", "FORTY_FIVE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdTextAsset(typing.TypedDict, total=False):
    assetPerformanceLabel: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "LEARNING",
        "LOW",
        "GOOD",
        "BEST",
        "NOT_APPLICABLE",
    ]
    pinnedField: typing.Literal[
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
    policySummaryInfo: GoogleAdsSearchads360V23Common__AdAssetPolicySummary
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdVideoAsset(typing.TypedDict, total=False):
    adVideoAssetInfo: GoogleAdsSearchads360V23Common__AdVideoAssetInfo
    asset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdVideoAssetInfo(typing.TypedDict, total=False):
    adVideoAssetFeatureControl: (
        GoogleAdsSearchads360V23Common__AdVideoAssetLinkFeatureControl
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdVideoAssetLinkFeatureControl(
    typing.TypedDict, total=False
):
    allowYoutubeComments: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AdditionalApplicationInfo(
    typing.TypedDict, total=False
):
    applicationId: str
    applicationInstance: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DEVELOPMENT_AND_TESTING", "PRODUCTION"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AddressInfo(typing.TypedDict, total=False):
    cityName: str
    countryCode: str
    postalCode: str
    provinceCode: str
    provinceName: str
    streetAddress: str
    streetAddress2: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AgeDimension(typing.TypedDict, total=False):
    ageRanges: _list[GoogleAdsSearchads360V23Common__AgeSegment]
    includeUndetermined: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AgeRangeInfo(typing.TypedDict, total=False):
    type: typing.Literal[
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
class GoogleAdsSearchads360V23Common__AgeSegment(typing.TypedDict, total=False):
    maxAge: int
    minAge: int

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AppAdInfo(typing.TypedDict, total=False):
    appDeepLink: GoogleAdsSearchads360V23Common__AdAppDeepLinkAsset
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    html5MediaBundles: _list[GoogleAdsSearchads360V23Common__AdMediaBundleAsset]
    images: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    mandatoryAdText: GoogleAdsSearchads360V23Common__AdTextAsset
    youtubeVideos: _list[GoogleAdsSearchads360V23Common__AdVideoAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AppDeepLinkAsset(typing.TypedDict, total=False):
    appDeepLinkUri: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AppEngagementAdInfo(
    typing.TypedDict, total=False
):
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    images: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    videos: _list[GoogleAdsSearchads360V23Common__AdVideoAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AppPaymentModelInfo(
    typing.TypedDict, total=False
):
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "PAID"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AppPreRegistrationAdInfo(
    typing.TypedDict, total=False
):
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    images: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    youtubeVideos: _list[GoogleAdsSearchads360V23Common__AdVideoAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AssetDisapproved(typing.TypedDict, total=False):
    offlineEvaluationErrorReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "PRICE_ASSET_DESCRIPTION_REPEATS_ROW_HEADER",
            "PRICE_ASSET_REPETITIVE_HEADERS",
            "PRICE_ASSET_HEADER_INCOMPATIBLE_WITH_PRICE_TYPE",
            "PRICE_ASSET_DESCRIPTION_INCOMPATIBLE_WITH_ITEM_HEADER",
            "PRICE_ASSET_DESCRIPTION_HAS_PRICE_QUALIFIER",
            "PRICE_ASSET_UNSUPPORTED_LANGUAGE",
            "PRICE_ASSET_OTHER_ERROR",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AssetInteractionTarget(
    typing.TypedDict, total=False
):
    asset: str
    interactionOnThisAsset: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AssetLinkPrimaryStatusDetails(
    typing.TypedDict, total=False
):
    assetDisapproved: GoogleAdsSearchads360V23Common__AssetDisapproved
    reason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ASSET_LINK_PAUSED",
        "ASSET_LINK_REMOVED",
        "ASSET_DISAPPROVED",
        "ASSET_UNDER_REVIEW",
        "ASSET_APPROVED_LABELED",
    ]
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "LIMITED",
        "NOT_ELIGIBLE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AssetUsage(typing.TypedDict, total=False):
    asset: str
    servedAssetFieldType: typing.Literal[
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
class GoogleAdsSearchads360V23Common__AudienceDimension(typing.TypedDict, total=False):
    age: GoogleAdsSearchads360V23Common__AgeDimension
    audienceSegments: GoogleAdsSearchads360V23Common__AudienceSegmentDimension
    gender: GoogleAdsSearchads360V23Common__GenderDimension
    householdIncome: GoogleAdsSearchads360V23Common__HouseholdIncomeDimension
    parentalStatus: GoogleAdsSearchads360V23Common__ParentalStatusDimension

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceExclusionDimension(
    typing.TypedDict, total=False
):
    exclusions: _list[GoogleAdsSearchads360V23Common__ExclusionSegment]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInfo(typing.TypedDict, total=False):
    audience: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInsightsAttribute(
    typing.TypedDict, total=False
):
    ageRange: GoogleAdsSearchads360V23Common__AgeRangeInfo
    category: GoogleAdsSearchads360V23Common__AudienceInsightsCategory
    device: GoogleAdsSearchads360V23Common__DeviceInfo
    entity: GoogleAdsSearchads360V23Common__AudienceInsightsEntity
    gender: GoogleAdsSearchads360V23Common__GenderInfo
    incomeRange: GoogleAdsSearchads360V23Common__IncomeRangeInfo
    lineup: GoogleAdsSearchads360V23Common__AudienceInsightsLineup
    location: GoogleAdsSearchads360V23Common__LocationInfo
    parentalStatus: GoogleAdsSearchads360V23Common__ParentalStatusInfo
    userInterest: GoogleAdsSearchads360V23Common__UserInterestInfo
    userList: GoogleAdsSearchads360V23Common__UserListInfo
    youtubeChannel: GoogleAdsSearchads360V23Common__YouTubeChannelInfo
    youtubeVideo: GoogleAdsSearchads360V23Common__YouTubeVideoInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata(
    typing.TypedDict, total=False
):
    attribute: GoogleAdsSearchads360V23Common__AudienceInsightsAttribute
    dimension: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CATEGORY",
        "KNOWLEDGE_GRAPH",
        "GEO_TARGET_COUNTRY",
        "SUB_COUNTRY_LOCATION",
        "YOUTUBE_CHANNEL",
        "AFFINITY_USER_INTEREST",
        "IN_MARKET_USER_INTEREST",
        "PARENTAL_STATUS",
        "INCOME_RANGE",
        "AGE_RANGE",
        "GENDER",
        "YOUTUBE_VIDEO",
        "DEVICE",
        "YOUTUBE_LINEUP",
        "USER_LIST",
        "LIFE_EVENT_USER_INTEREST",
    ]
    displayInfo: str
    displayName: str
    knowledgeGraphAttributeMetadata: (
        GoogleAdsSearchads360V23Common__KnowledgeGraphAttributeMetadata
    )
    lineupAttributeMetadata: GoogleAdsSearchads360V23Common__LineupAttributeMetadata
    locationAttributeMetadata: GoogleAdsSearchads360V23Common__LocationAttributeMetadata
    potentialYoutubeReach: str
    subscriberShare: float
    userInterestAttributeMetadata: (
        GoogleAdsSearchads360V23Common__UserInterestAttributeMetadata
    )
    userListAttributeMetadata: GoogleAdsSearchads360V23Common__UserListAttributeMetadata
    viewerShare: float
    youtubeChannelMetadata: (
        GoogleAdsSearchads360V23Common__YouTubeChannelAttributeMetadata
    )
    youtubeVideoMetadata: GoogleAdsSearchads360V23Common__YouTubeVideoAttributeMetadata

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadataGroup(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInsightsCategory(
    typing.TypedDict, total=False
):
    categoryId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInsightsEntity(
    typing.TypedDict, total=False
):
    knowledgeGraphMachineId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceInsightsLineup(
    typing.TypedDict, total=False
):
    lineupId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceSegment(typing.TypedDict, total=False):
    customAudience: GoogleAdsSearchads360V23Common__CustomAudienceSegment
    detailedDemographic: GoogleAdsSearchads360V23Common__DetailedDemographicSegment
    lifeEvent: GoogleAdsSearchads360V23Common__LifeEventSegment
    userInterest: GoogleAdsSearchads360V23Common__UserInterestSegment
    userList: GoogleAdsSearchads360V23Common__UserListSegment

@typing.type_check_only
class GoogleAdsSearchads360V23Common__AudienceSegmentDimension(
    typing.TypedDict, total=False
):
    segments: _list[GoogleAdsSearchads360V23Common__AudienceSegment]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BasicUserListInfo(typing.TypedDict, total=False):
    actions: _list[GoogleAdsSearchads360V23Common__UserListActionInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BookOnGoogleAsset(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BrandInfo(typing.TypedDict, total=False):
    displayName: str
    entityId: str
    primaryUrl: str
    rejectionReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXISTING_BRAND",
        "EXISTING_BRAND_VARIANT",
        "INCORRECT_INFORMATION",
        "NOT_A_BRAND",
    ]
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ENABLED",
        "DEPRECATED",
        "UNVERIFIED",
        "APPROVED",
        "CANCELLED",
        "REJECTED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BrandListInfo(typing.TypedDict, total=False):
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BudgetSimulationPoint(
    typing.TypedDict, total=False
):
    biddableConversions: float
    biddableConversionsValue: float
    budgetAmountMicros: str
    clicks: str
    costMicros: str
    impressions: str
    interactions: str
    requiredCpcBidCeilingMicros: str
    topSlotImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BudgetSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__BudgetSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BusinessMessageAsset(
    typing.TypedDict, total=False
):
    callToAction: GoogleAdsSearchads360V23Common__BusinessMessageCallToActionInfo
    facebookMessengerInfo: (
        GoogleAdsSearchads360V23Common__FacebookMessengerBusinessMessageInfo
    )
    messageProvider: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "WHATSAPP", "FACEBOOK_MESSENGER", "ZALO"
    ]
    starterMessage: str
    whatsappInfo: GoogleAdsSearchads360V23Common__WhatsappBusinessMessageInfo
    zaloInfo: GoogleAdsSearchads360V23Common__ZaloBusinessMessageInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BusinessMessageCallToActionInfo(
    typing.TypedDict, total=False
):
    callToActionDescription: str
    callToActionSelection: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "APPLY_NOW",
        "BOOK_NOW",
        "CONTACT_US",
        "GET_INFO",
        "GET_OFFER",
        "GET_QUOTE",
        "GET_STARTED",
        "LEARN_MORE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BusinessProfileBusinessNameFilter(
    typing.TypedDict, total=False
):
    businessName: str
    filterType: typing.Literal["UNSPECIFIED", "UNKNOWN", "EXACT"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BusinessProfileLocation(
    typing.TypedDict, total=False
):
    labels: _list[str]
    listingId: str
    storeCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BusinessProfileLocationGroup(
    typing.TypedDict, total=False
):
    dynamicBusinessProfileLocationGroupFilter: (
        GoogleAdsSearchads360V23Common__DynamicBusinessProfileLocationGroupFilter
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common__BusinessProfileLocationSet(
    typing.TypedDict, total=False
):
    businessAccountId: str
    businessNameFilter: str
    emailAddress: str
    httpAuthorizationToken: str
    labelFilters: _list[str]
    listingIdFilters: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CallAsset(typing.TypedDict, total=False):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    callConversionAction: str
    callConversionReportingState: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISABLED",
        "USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION",
        "USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION",
    ]
    countryCode: str
    phoneNumber: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CallFeedItem(typing.TypedDict, total=False):
    callConversionAction: str
    callConversionReportingState: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISABLED",
        "USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION",
        "USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION",
    ]
    callConversionTrackingDisabled: bool
    callTrackingEnabled: bool
    countryCode: str
    phoneNumber: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CallToActionAsset(typing.TypedDict, total=False):
    callToAction: typing.Literal[
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
class GoogleAdsSearchads360V23Common__CalloutAsset(typing.TypedDict, total=False):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    calloutText: str
    endDate: str
    startDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CalloutFeedItem(typing.TypedDict, total=False):
    calloutText: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CampaignThirdPartyBrandLiftIntegrationPartner(
    typing.TypedDict, total=False
):
    brandLiftIntegrationPartner: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "KANTAR_MILLWARD_BROWN",
        "DYNATA",
        "INTAGE",
        "MACROMILL",
    ]
    brandLiftIntegrationPartnerData: (
        GoogleAdsSearchads360V23Common__ThirdPartyIntegrationPartnerData
    )
    shareCost: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CampaignThirdPartyBrandSafetyIntegrationPartner(
    typing.TypedDict, total=False
):
    brandSafetyIntegrationPartner: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DOUBLE_VERIFY", "INTEGRAL_AD_SCIENCE", "ZEFR"
    ]
    brandSafetyIntegrationPartnerData: (
        GoogleAdsSearchads360V23Common__ThirdPartyIntegrationPartnerData
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CampaignThirdPartyIntegrationPartners(
    typing.TypedDict, total=False
):
    brandLiftIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CampaignThirdPartyBrandLiftIntegrationPartner
    ]
    brandSafetyIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CampaignThirdPartyBrandSafetyIntegrationPartner
    ]
    reachIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CampaignThirdPartyReachIntegrationPartner
    ]
    viewabilityIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CampaignThirdPartyViewabilityIntegrationPartner
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CampaignThirdPartyReachIntegrationPartner(
    typing.TypedDict, total=False
):
    reachIntegrationPartner: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NIELSEN",
        "COMSCORE",
        "KANTAR_MILLWARD_BROWN",
        "VIDEO_RESEARCH",
        "GEMIUS",
        "MEDIA_SCOPE",
        "AUDIENCE_PROJECT",
        "VIDEO_AMP",
        "ISPOT_TV",
    ]
    reachIntegrationPartnerData: (
        GoogleAdsSearchads360V23Common__ThirdPartyIntegrationPartnerData
    )
    shareCost: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CampaignThirdPartyViewabilityIntegrationPartner(
    typing.TypedDict, total=False
):
    shareCost: bool
    viewabilityIntegrationPartner: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DOUBLE_VERIFY", "INTEGRAL_AD_SCIENCE"
    ]
    viewabilityIntegrationPartnerData: (
        GoogleAdsSearchads360V23Common__ThirdPartyIntegrationPartnerData
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CarrierInfo(typing.TypedDict, total=False):
    carrierConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ChainFilter(typing.TypedDict, total=False):
    chainId: str
    locationAttributes: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ChainLocationGroup(typing.TypedDict, total=False):
    dynamicChainLocationGroupFilters: _list[GoogleAdsSearchads360V23Common__ChainFilter]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ChainSet(typing.TypedDict, total=False):
    chains: _list[GoogleAdsSearchads360V23Common__ChainFilter]
    relationshipType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AUTO_DEALERS", "GENERAL_RETAILERS"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ClickLocation(typing.TypedDict, total=False):
    city: str
    country: str
    metro: str
    mostSpecific: str
    region: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CombinedAudienceInfo(
    typing.TypedDict, total=False
):
    combinedAudience: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Commission(typing.TypedDict, total=False):
    commissionRateMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ConceptGroup(typing.TypedDict, total=False):
    name: str
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "BRAND", "OTHER_BRANDS", "NON_BRAND"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Consent(typing.TypedDict, total=False):
    adPersonalization: typing.Literal["UNSPECIFIED", "UNKNOWN", "GRANTED", "DENIED"]
    adUserData: typing.Literal["UNSPECIFIED", "UNKNOWN", "GRANTED", "DENIED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ContentLabelInfo(typing.TypedDict, total=False):
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEXUALLY_SUGGESTIVE",
        "BELOW_THE_FOLD",
        "PARKED_DOMAIN",
        "JUVENILE",
        "PROFANITY",
        "TRAGEDY",
        "VIDEO",
        "VIDEO_RATING_DV_G",
        "VIDEO_RATING_DV_PG",
        "VIDEO_RATING_DV_T",
        "VIDEO_RATING_DV_MA",
        "VIDEO_NOT_YET_RATED",
        "EMBEDDED_VIDEO",
        "LIVE_STREAMING_VIDEO",
        "SOCIAL_ISSUES",
        "BRAND_SUITABILITY_CONTENT_FOR_FAMILIES",
        "BRAND_SUITABILITY_GAMES_FIGHTING",
        "BRAND_SUITABILITY_GAMES_MATURE",
        "BRAND_SUITABILITY_HEALTH_SENSITIVE",
        "BRAND_SUITABILITY_HEALTH_SOURCE_UNDETERMINED",
        "BRAND_SUITABILITY_NEWS_RECENT",
        "BRAND_SUITABILITY_NEWS_SENSITIVE",
        "BRAND_SUITABILITY_NEWS_SOURCE_NOT_FEATURED",
        "BRAND_SUITABILITY_POLITICS",
        "BRAND_SUITABILITY_RELIGION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CpcBidSimulationPoint(
    typing.TypedDict, total=False
):
    biddableConversions: float
    biddableConversionsValue: float
    clicks: str
    costMicros: str
    cpcBidMicros: str
    cpcBidScalingModifier: float
    impressions: str
    requiredBudgetAmountMicros: str
    topSlotImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CpcBidSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__CpcBidSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CpvBidSimulationPoint(
    typing.TypedDict, total=False
):
    costMicros: str
    cpvBidMicros: str
    impressions: str
    views: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CpvBidSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__CpvBidSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CriterionCategoryAvailability(
    typing.TypedDict, total=False
):
    channel: GoogleAdsSearchads360V23Common__CriterionCategoryChannelAvailability
    locale: _list[GoogleAdsSearchads360V23Common__CriterionCategoryLocaleAvailability]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CriterionCategoryChannelAvailability(
    typing.TypedDict, total=False
):
    advertisingChannelSubType: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "SEARCH_MOBILE_APP",
            "DISPLAY_MOBILE_APP",
            "SEARCH_EXPRESS",
            "DISPLAY_EXPRESS",
            "SHOPPING_SMART_ADS",
            "DISPLAY_GMAIL_AD",
            "DISPLAY_SMART_CAMPAIGN",
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
    ]
    advertisingChannelType: typing.Literal[
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
        "TRAVEL",
        "DEMAND_GEN",
        "SOCIAL",
    ]
    availabilityMode: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ALL_CHANNELS",
        "CHANNEL_TYPE_AND_ALL_SUBTYPES",
        "CHANNEL_TYPE_AND_SUBSET_SUBTYPES",
    ]
    includeDefaultChannelSubType: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CriterionCategoryLocaleAvailability(
    typing.TypedDict, total=False
):
    availabilityMode: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ALL_LOCALES",
        "COUNTRY_AND_ALL_LANGUAGES",
        "LANGUAGE_AND_ALL_COUNTRIES",
        "COUNTRY_AND_LANGUAGE",
    ]
    countryCode: str
    languageCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CrmBasedUserListInfo(
    typing.TypedDict, total=False
):
    appId: str
    dataSourceType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FIRST_PARTY",
        "THIRD_PARTY_CREDIT_BUREAU",
        "THIRD_PARTY_VOTER_FILE",
        "THIRD_PARTY_PARTNER_DATA",
    ]
    uploadKeyType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CONTACT_INFO", "CRM_ID", "MOBILE_ADVERTISING_ID"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomAffinityInfo(typing.TypedDict, total=False):
    customAffinity: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomAudienceInfo(typing.TypedDict, total=False):
    customAudience: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomAudienceSegment(
    typing.TypedDict, total=False
):
    customAudience: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomIntentInfo(typing.TypedDict, total=False):
    customIntent: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomParameter(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerLifecycleOptimizationValueSettings(
    typing.TypedDict, total=False
):
    additionalHighLifetimeValue: float
    additionalValue: float

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerMatchUserListMetadata(
    typing.TypedDict, total=False
):
    consent: GoogleAdsSearchads360V23Common__Consent
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerThirdPartyBrandLiftIntegrationPartner(
    typing.TypedDict, total=False
):
    allowShareCost: bool
    brandLiftIntegrationPartner: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "KANTAR_MILLWARD_BROWN",
        "DYNATA",
        "INTAGE",
        "MACROMILL",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerThirdPartyBrandSafetyIntegrationPartner(
    typing.TypedDict, total=False
):
    brandSafetyIntegrationPartner: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DOUBLE_VERIFY", "INTEGRAL_AD_SCIENCE", "ZEFR"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerThirdPartyIntegrationPartners(
    typing.TypedDict, total=False
):
    brandLiftIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CustomerThirdPartyBrandLiftIntegrationPartner
    ]
    brandSafetyIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CustomerThirdPartyBrandSafetyIntegrationPartner
    ]
    reachIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CustomerThirdPartyReachIntegrationPartner
    ]
    viewabilityIntegrationPartners: _list[
        GoogleAdsSearchads360V23Common__CustomerThirdPartyViewabilityIntegrationPartner
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerThirdPartyReachIntegrationPartner(
    typing.TypedDict, total=False
):
    allowShareCost: bool
    reachIntegrationPartner: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NIELSEN",
        "COMSCORE",
        "KANTAR_MILLWARD_BROWN",
        "VIDEO_RESEARCH",
        "GEMIUS",
        "MEDIA_SCOPE",
        "AUDIENCE_PROJECT",
        "VIDEO_AMP",
        "ISPOT_TV",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomerThirdPartyViewabilityIntegrationPartner(
    typing.TypedDict, total=False
):
    allowShareCost: bool
    viewabilityIntegrationPartner: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DOUBLE_VERIFY", "INTEGRAL_AD_SCIENCE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__CustomizerValue(typing.TypedDict, total=False):
    stringValue: str
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "TEXT", "NUMBER", "PRICE", "PERCENT"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DateRange(typing.TypedDict, total=False):
    endDate: str
    startDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DemandGenCarouselAdInfo(
    typing.TypedDict, total=False
):
    businessName: str
    callToActionText: str
    carouselCards: _list[GoogleAdsSearchads360V23Common__AdDemandGenCarouselCardAsset]
    description: GoogleAdsSearchads360V23Common__AdTextAsset
    headline: GoogleAdsSearchads360V23Common__AdTextAsset
    logoImage: GoogleAdsSearchads360V23Common__AdImageAsset

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DemandGenCarouselCardAsset(
    typing.TypedDict, total=False
):
    callToActionText: str
    headline: str
    marketingImageAsset: str
    portraitMarketingImageAsset: str
    squareMarketingImageAsset: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DemandGenMultiAssetAdInfo(
    typing.TypedDict, total=False
):
    businessName: str
    callToActionText: str
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    logoImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    marketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    portraitMarketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    squareMarketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    tallPortraitMarketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DemandGenProductAdInfo(
    typing.TypedDict, total=False
):
    breadcrumb1: str
    breadcrumb2: str
    businessName: GoogleAdsSearchads360V23Common__AdTextAsset
    callToAction: GoogleAdsSearchads360V23Common__AdCallToActionAsset
    description: GoogleAdsSearchads360V23Common__AdTextAsset
    headline: GoogleAdsSearchads360V23Common__AdTextAsset
    logoImage: GoogleAdsSearchads360V23Common__AdImageAsset

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DemandGenVideoResponsiveAdInfo(
    typing.TypedDict, total=False
):
    breadcrumb1: str
    breadcrumb2: str
    businessName: GoogleAdsSearchads360V23Common__AdTextAsset
    callToActions: _list[GoogleAdsSearchads360V23Common__AdCallToActionAsset]
    companionBanners: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    logoImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    longHeadlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    videos: _list[GoogleAdsSearchads360V23Common__AdVideoAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DetailedDemographicSegment(
    typing.TypedDict, total=False
):
    detailedDemographic: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DeviceInfo(typing.TypedDict, total=False):
    type: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET", "DESKTOP", "CONNECTED_TV", "OTHER"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DisplayUploadAdInfo(
    typing.TypedDict, total=False
):
    displayUploadProductType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HTML5_UPLOAD_AD",
        "DYNAMIC_HTML5_EDUCATION_AD",
        "DYNAMIC_HTML5_FLIGHT_AD",
        "DYNAMIC_HTML5_HOTEL_RENTAL_AD",
        "DYNAMIC_HTML5_JOB_AD",
        "DYNAMIC_HTML5_LOCAL_AD",
        "DYNAMIC_HTML5_REAL_ESTATE_AD",
        "DYNAMIC_HTML5_CUSTOM_AD",
        "DYNAMIC_HTML5_TRAVEL_AD",
        "DYNAMIC_HTML5_HOTEL_AD",
    ]
    mediaBundle: GoogleAdsSearchads360V23Common__AdMediaBundleAsset

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicBusinessProfileLocationGroupFilter(
    typing.TypedDict, total=False
):
    businessNameFilter: (
        GoogleAdsSearchads360V23Common__BusinessProfileBusinessNameFilter
    )
    labelFilters: _list[str]
    listingIdFilters: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicCustomAsset(typing.TypedDict, total=False):
    androidAppLink: str
    contextualKeywords: _list[str]
    formattedPrice: str
    formattedSalePrice: str
    id: str
    id2: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    itemAddress: str
    itemCategory: str
    itemDescription: str
    itemSubtitle: str
    itemTitle: str
    price: str
    salePrice: str
    similarIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicEducationAsset(
    typing.TypedDict, total=False
):
    address: str
    androidAppLink: str
    contextualKeywords: _list[str]
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    locationId: str
    programDescription: str
    programId: str
    programName: str
    schoolName: str
    similarProgramIds: _list[str]
    subject: str
    thumbnailImageUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicFlightsAsset(
    typing.TypedDict, total=False
):
    androidAppLink: str
    customMapping: str
    destinationId: str
    destinationName: str
    flightDescription: str
    flightPrice: str
    flightSalePrice: str
    formattedPrice: str
    formattedSalePrice: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    originId: str
    originName: str
    similarDestinationIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicHotelsAndRentalsAsset(
    typing.TypedDict, total=False
):
    address: str
    androidAppLink: str
    category: str
    contextualKeywords: _list[str]
    description: str
    destinationName: str
    formattedPrice: str
    formattedSalePrice: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    price: str
    propertyId: str
    propertyName: str
    salePrice: str
    similarPropertyIds: _list[str]
    starRating: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicJobsAsset(typing.TypedDict, total=False):
    address: str
    androidAppLink: str
    contextualKeywords: _list[str]
    description: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    jobCategory: str
    jobId: str
    jobSubtitle: str
    jobTitle: str
    locationId: str
    salary: str
    similarJobIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicLocalAsset(typing.TypedDict, total=False):
    address: str
    androidAppLink: str
    category: str
    contextualKeywords: _list[str]
    dealId: str
    dealName: str
    description: str
    formattedPrice: str
    formattedSalePrice: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    price: str
    salePrice: str
    similarDealIds: _list[str]
    subtitle: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicRealEstateAsset(
    typing.TypedDict, total=False
):
    address: str
    androidAppLink: str
    cityName: str
    contextualKeywords: _list[str]
    description: str
    formattedPrice: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    listingId: str
    listingName: str
    listingType: str
    price: str
    propertyType: str
    similarListingIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__DynamicTravelAsset(typing.TypedDict, total=False):
    androidAppLink: str
    category: str
    contextualKeywords: _list[str]
    destinationAddress: str
    destinationId: str
    destinationName: str
    formattedPrice: str
    formattedSalePrice: str
    imageUrl: str
    iosAppLink: str
    iosAppStoreId: str
    originId: str
    originName: str
    price: str
    salePrice: str
    similarDestinationIds: _list[str]
    title: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__EnhancedCpc(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__EventAttribute(typing.TypedDict, total=False):
    event: str
    eventDateTime: str
    itemAttribute: _list[GoogleAdsSearchads360V23Common__EventItemAttribute]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__EventItemAttribute(typing.TypedDict, total=False):
    itemId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ExclusionSegment(typing.TypedDict, total=False):
    userList: GoogleAdsSearchads360V23Common__UserListSegment

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ExpandedDynamicSearchAdInfo(
    typing.TypedDict, total=False
):
    description: str
    description2: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ExpandedTextAdInfo(typing.TypedDict, total=False):
    description: str
    description2: str
    headlinePart1: str
    headlinePart2: str
    headlinePart3: str
    path1: str
    path2: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ExtendedDemographicInfo(
    typing.TypedDict, total=False
):
    extendedDemographicId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__FacebookMessengerBusinessMessageInfo(
    typing.TypedDict, total=False
):
    pageName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__FinalAppUrl(typing.TypedDict, total=False):
    osType: typing.Literal["UNSPECIFIED", "UNKNOWN", "IOS", "ANDROID"]
    url: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__FlexibleRuleOperandInfo(
    typing.TypedDict, total=False
):
    lookbackWindowDays: str
    rule: GoogleAdsSearchads360V23Common__UserListRuleInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__FlexibleRuleUserListInfo(
    typing.TypedDict, total=False
):
    exclusiveOperands: _list[GoogleAdsSearchads360V23Common__FlexibleRuleOperandInfo]
    inclusiveOperands: _list[GoogleAdsSearchads360V23Common__FlexibleRuleOperandInfo]
    inclusiveRuleOperator: typing.Literal["UNSPECIFIED", "UNKNOWN", "AND", "OR"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__FrequencyCapEntry(typing.TypedDict, total=False):
    cap: int
    key: GoogleAdsSearchads360V23Common__FrequencyCapKey

@typing.type_check_only
class GoogleAdsSearchads360V23Common__FrequencyCapKey(typing.TypedDict, total=False):
    eventType: typing.Literal["UNSPECIFIED", "UNKNOWN", "IMPRESSION", "VIDEO_VIEW"]
    level: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AD_GROUP_AD", "AD_GROUP", "CAMPAIGN"
    ]
    timeLength: int
    timeUnit: typing.Literal["UNSPECIFIED", "UNKNOWN", "DAY", "WEEK", "MONTH"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__GenderDimension(typing.TypedDict, total=False):
    genders: _list[
        typing.Literal["UNSPECIFIED", "UNKNOWN", "MALE", "FEMALE", "UNDETERMINED"]
    ]
    includeUndetermined: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__GenderInfo(typing.TypedDict, total=False):
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "MALE", "FEMALE", "UNDETERMINED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__GeoPointInfo(typing.TypedDict, total=False):
    latitudeInMicroDegrees: int
    longitudeInMicroDegrees: int

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HistoricalMetricsOptions(
    typing.TypedDict, total=False
):
    includeAverageCpc: bool
    yearMonthRange: GoogleAdsSearchads360V23Common__YearMonthRange

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelAdInfo(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelAdvanceBookingWindowInfo(
    typing.TypedDict, total=False
):
    maxDays: str
    minDays: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelCalloutAsset(typing.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelCheckInDateRangeInfo(
    typing.TypedDict, total=False
):
    endDate: str
    startDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelCheckInDayInfo(
    typing.TypedDict, total=False
):
    dayOfWeek: typing.Literal[
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

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelCityInfo(typing.TypedDict, total=False):
    cityCriterion: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelClassInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelCountryRegionInfo(
    typing.TypedDict, total=False
):
    countryRegionCriterion: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelDateSelectionTypeInfo(
    typing.TypedDict, total=False
):
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "DEFAULT_SELECTION", "USER_SELECTED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelIdInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelLengthOfStayInfo(
    typing.TypedDict, total=False
):
    maxNights: str
    minNights: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelPropertyAsset(typing.TypedDict, total=False):
    hotelAddress: str
    hotelName: str
    placeId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HotelStateInfo(typing.TypedDict, total=False):
    stateCriterion: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__HouseholdIncomeDimension(
    typing.TypedDict, total=False
):
    includeUndetermined: bool
    incomeRanges: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "INCOME_RANGE_0_50",
            "INCOME_RANGE_50_60",
            "INCOME_RANGE_60_70",
            "INCOME_RANGE_70_80",
            "INCOME_RANGE_80_90",
            "INCOME_RANGE_90_UP",
            "INCOME_RANGE_UNDETERMINED",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ImageAdInfo(typing.TypedDict, total=False):
    adIdToCopyImageFrom: str
    data: str
    imageAsset: GoogleAdsSearchads360V23Common__AdImageAsset
    imageUrl: str
    mimeType: typing.Literal[
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
    name: str
    pixelHeight: str
    pixelWidth: str
    previewImageUrl: str
    previewPixelHeight: str
    previewPixelWidth: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ImageAsset(typing.TypedDict, total=False):
    data: str
    fileSize: str
    fullSize: GoogleAdsSearchads360V23Common__ImageDimension
    mimeType: typing.Literal[
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
class GoogleAdsSearchads360V23Common__ImageDimension(typing.TypedDict, total=False):
    heightPixels: str
    url: str
    widthPixels: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__IncomeRangeInfo(typing.TypedDict, total=False):
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INCOME_RANGE_0_50",
        "INCOME_RANGE_50_60",
        "INCOME_RANGE_60_70",
        "INCOME_RANGE_70_80",
        "INCOME_RANGE_80_90",
        "INCOME_RANGE_90_UP",
        "INCOME_RANGE_UNDETERMINED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__InteractionTypeInfo(
    typing.TypedDict, total=False
):
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "CALLS"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__IpBlockInfo(typing.TypedDict, total=False):
    ipAddress: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ItemAttribute(typing.TypedDict, total=False):
    countryCode: str
    itemId: str
    languageCode: str
    merchantId: str
    quantity: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Keyword(typing.TypedDict, total=False):
    adGroupCriterion: str
    info: GoogleAdsSearchads360V23Common__KeywordInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordAnnotations(typing.TypedDict, total=False):
    concepts: _list[GoogleAdsSearchads360V23Common__KeywordConcept]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordConcept(typing.TypedDict, total=False):
    conceptGroup: GoogleAdsSearchads360V23Common__ConceptGroup
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordInfo(typing.TypedDict, total=False):
    matchType: typing.Literal["UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"]
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordPlanAggregateMetricResults(
    typing.TypedDict, total=False
):
    deviceSearches: _list[GoogleAdsSearchads360V23Common__KeywordPlanDeviceSearches]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordPlanAggregateMetrics(
    typing.TypedDict, total=False
):
    aggregateMetricTypes: _list[typing.Literal["UNSPECIFIED", "UNKNOWN", "DEVICE"]]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordPlanDeviceSearches(
    typing.TypedDict, total=False
):
    device: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET", "DESKTOP", "CONNECTED_TV", "OTHER"
    ]
    searchCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordPlanHistoricalMetrics(
    typing.TypedDict, total=False
):
    averageCpcMicros: str
    avgMonthlySearches: str
    competition: typing.Literal["UNSPECIFIED", "UNKNOWN", "LOW", "MEDIUM", "HIGH"]
    competitionIndex: str
    highTopOfPageBidMicros: str
    lowTopOfPageBidMicros: str
    monthlySearchVolumes: _list[GoogleAdsSearchads360V23Common__MonthlySearchVolume]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KeywordThemeInfo(typing.TypedDict, total=False):
    freeFormKeywordTheme: str
    keywordThemeConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__KnowledgeGraphAttributeMetadata(
    typing.TypedDict, total=False
):
    entityCapabilities: _list[
        typing.Literal[
            "UNSPECIFIED", "UNKNOWN", "CONTENT_TRENDING_INSIGHTS", "CREATOR_ATTRIBUTE"
        ]
    ]
    relatedCategories: _list[
        GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LanguageInfo(typing.TypedDict, total=False):
    languageConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LeadFormAsset(typing.TypedDict, total=False):
    backgroundImageAsset: str
    businessName: str
    callToActionDescription: str
    callToActionType: typing.Literal[
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
        "GET_OFFER",
        "REGISTER",
        "GET_INFO",
        "REQUEST_DEMO",
        "JOIN_NOW",
        "GET_STARTED",
    ]
    customDisclosure: str
    customQuestionFields: _list[
        GoogleAdsSearchads360V23Common__LeadFormCustomQuestionField
    ]
    deliveryMethods: _list[GoogleAdsSearchads360V23Common__LeadFormDeliveryMethod]
    description: str
    desiredIntent: typing.Literal["UNSPECIFIED", "UNKNOWN", "LOW_INTENT", "HIGH_INTENT"]
    fields: _list[GoogleAdsSearchads360V23Common__LeadFormField]
    headline: str
    postSubmitCallToActionType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "VISIT_SITE", "DOWNLOAD", "LEARN_MORE", "SHOP_NOW"
    ]
    postSubmitDescription: str
    postSubmitHeadline: str
    privacyPolicyUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LeadFormCustomQuestionField(
    typing.TypedDict, total=False
):
    customQuestionText: str
    hasLocationAnswer: bool
    singleChoiceAnswers: GoogleAdsSearchads360V23Common__LeadFormSingleChoiceAnswers

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LeadFormDeliveryMethod(
    typing.TypedDict, total=False
):
    webhook: GoogleAdsSearchads360V23Common__WebhookDelivery

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LeadFormField(typing.TypedDict, total=False):
    hasLocationAnswer: bool
    inputType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FULL_NAME",
        "EMAIL",
        "PHONE_NUMBER",
        "POSTAL_CODE",
        "STREET_ADDRESS",
        "CITY",
        "REGION",
        "COUNTRY",
        "WORK_EMAIL",
        "COMPANY_NAME",
        "WORK_PHONE",
        "JOB_TITLE",
        "GOVERNMENT_ISSUED_ID_CPF_BR",
        "GOVERNMENT_ISSUED_ID_DNI_AR",
        "GOVERNMENT_ISSUED_ID_DNI_PE",
        "GOVERNMENT_ISSUED_ID_RUT_CL",
        "GOVERNMENT_ISSUED_ID_CC_CO",
        "GOVERNMENT_ISSUED_ID_CI_EC",
        "GOVERNMENT_ISSUED_ID_RFC_MX",
        "FIRST_NAME",
        "LAST_NAME",
        "VEHICLE_MODEL",
        "VEHICLE_TYPE",
        "PREFERRED_DEALERSHIP",
        "VEHICLE_PURCHASE_TIMELINE",
        "VEHICLE_OWNERSHIP",
        "VEHICLE_PAYMENT_TYPE",
        "VEHICLE_CONDITION",
        "COMPANY_SIZE",
        "ANNUAL_SALES",
        "YEARS_IN_BUSINESS",
        "JOB_DEPARTMENT",
        "JOB_ROLE",
        "OVER_18_AGE",
        "OVER_19_AGE",
        "OVER_20_AGE",
        "OVER_21_AGE",
        "OVER_22_AGE",
        "OVER_23_AGE",
        "OVER_24_AGE",
        "OVER_25_AGE",
        "OVER_26_AGE",
        "OVER_27_AGE",
        "OVER_28_AGE",
        "OVER_29_AGE",
        "OVER_30_AGE",
        "OVER_31_AGE",
        "OVER_32_AGE",
        "OVER_33_AGE",
        "OVER_34_AGE",
        "OVER_35_AGE",
        "OVER_36_AGE",
        "OVER_37_AGE",
        "OVER_38_AGE",
        "OVER_39_AGE",
        "OVER_40_AGE",
        "OVER_41_AGE",
        "OVER_42_AGE",
        "OVER_43_AGE",
        "OVER_44_AGE",
        "OVER_45_AGE",
        "OVER_46_AGE",
        "OVER_47_AGE",
        "OVER_48_AGE",
        "OVER_49_AGE",
        "OVER_50_AGE",
        "OVER_51_AGE",
        "OVER_52_AGE",
        "OVER_53_AGE",
        "OVER_54_AGE",
        "OVER_55_AGE",
        "OVER_56_AGE",
        "OVER_57_AGE",
        "OVER_58_AGE",
        "OVER_59_AGE",
        "OVER_60_AGE",
        "OVER_61_AGE",
        "OVER_62_AGE",
        "OVER_63_AGE",
        "OVER_64_AGE",
        "OVER_65_AGE",
        "EDUCATION_PROGRAM",
        "EDUCATION_COURSE",
        "PRODUCT",
        "SERVICE",
        "OFFER",
        "CATEGORY",
        "PREFERRED_CONTACT_METHOD",
        "PREFERRED_LOCATION",
        "PREFERRED_CONTACT_TIME",
        "PURCHASE_TIMELINE",
        "YEARS_OF_EXPERIENCE",
        "JOB_INDUSTRY",
        "LEVEL_OF_EDUCATION",
        "PROPERTY_TYPE",
        "REALTOR_HELP_GOAL",
        "PROPERTY_COMMUNITY",
        "PRICE_RANGE",
        "NUMBER_OF_BEDROOMS",
        "FURNISHED_PROPERTY",
        "PETS_ALLOWED_PROPERTY",
        "NEXT_PLANNED_PURCHASE",
        "EVENT_SIGNUP_INTEREST",
        "PREFERRED_SHOPPING_PLACES",
        "FAVORITE_BRAND",
        "TRANSPORTATION_COMMERCIAL_LICENSE_TYPE",
        "EVENT_BOOKING_INTEREST",
        "DESTINATION_COUNTRY",
        "DESTINATION_CITY",
        "DEPARTURE_COUNTRY",
        "DEPARTURE_CITY",
        "DEPARTURE_DATE",
        "RETURN_DATE",
        "NUMBER_OF_TRAVELERS",
        "TRAVEL_BUDGET",
        "TRAVEL_ACCOMMODATION",
    ]
    singleChoiceAnswers: GoogleAdsSearchads360V23Common__LeadFormSingleChoiceAnswers

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LeadFormSingleChoiceAnswers(
    typing.TypedDict, total=False
):
    answers: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LegacyAppInstallAdInfo(
    typing.TypedDict, total=False
):
    appId: str
    appStore: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "APPLE_APP_STORE",
        "GOOGLE_PLAY",
        "WINDOWS_STORE",
        "WINDOWS_PHONE_STORE",
        "CN_APP_STORE",
    ]
    description1: str
    description2: str
    headline: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LegacyResponsiveDisplayAdInfo(
    typing.TypedDict, total=False
):
    accentColor: str
    allowFlexibleColor: bool
    businessName: str
    callToActionText: str
    description: str
    formatSetting: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ALL_FORMATS", "NON_NATIVE", "NATIVE"
    ]
    logoImage: str
    longHeadline: str
    mainColor: str
    marketingImage: str
    pricePrefix: str
    promoText: str
    shortHeadline: str
    squareLogoImage: str
    squareMarketingImage: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LifeEventInfo(typing.TypedDict, total=False):
    lifeEventId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LifeEventSegment(typing.TypedDict, total=False):
    lifeEvent: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LifecycleGoalValueSettings(
    typing.TypedDict, total=False
):
    highLifetimeValue: float
    value: float

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LineupAttributeMetadata(
    typing.TypedDict, total=False
):
    channelCountLowerBound: str
    channelCountUpperBound: str
    inventoryCountry: GoogleAdsSearchads360V23Common__LocationInfo
    medianMonthlyInventory: str
    sampleChannels: _list[
        GoogleAdsSearchads360V23Common_LineupAttributeMetadata_SampleChannel
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ListingDimensionInfo(
    typing.TypedDict, total=False
):
    activityCity: GoogleAdsSearchads360V23Common__ActivityCityInfo
    activityCountry: GoogleAdsSearchads360V23Common__ActivityCountryInfo
    activityId: GoogleAdsSearchads360V23Common__ActivityIdInfo
    activityRating: GoogleAdsSearchads360V23Common__ActivityRatingInfo
    activityState: GoogleAdsSearchads360V23Common__ActivityStateInfo
    hotelCity: GoogleAdsSearchads360V23Common__HotelCityInfo
    hotelClass: GoogleAdsSearchads360V23Common__HotelClassInfo
    hotelCountryRegion: GoogleAdsSearchads360V23Common__HotelCountryRegionInfo
    hotelId: GoogleAdsSearchads360V23Common__HotelIdInfo
    hotelState: GoogleAdsSearchads360V23Common__HotelStateInfo
    productBrand: GoogleAdsSearchads360V23Common__ProductBrandInfo
    productCategory: GoogleAdsSearchads360V23Common__ProductCategoryInfo
    productChannel: GoogleAdsSearchads360V23Common__ProductChannelInfo
    productChannelExclusivity: (
        GoogleAdsSearchads360V23Common__ProductChannelExclusivityInfo
    )
    productCondition: GoogleAdsSearchads360V23Common__ProductConditionInfo
    productCustomAttribute: GoogleAdsSearchads360V23Common__ProductCustomAttributeInfo
    productGrouping: GoogleAdsSearchads360V23Common__ProductGroupingInfo
    productItemId: GoogleAdsSearchads360V23Common__ProductItemIdInfo
    productLabels: GoogleAdsSearchads360V23Common__ProductLabelsInfo
    productLegacyCondition: GoogleAdsSearchads360V23Common__ProductLegacyConditionInfo
    productType: GoogleAdsSearchads360V23Common__ProductTypeInfo
    productTypeFull: GoogleAdsSearchads360V23Common__ProductTypeFullInfo
    unknownListingDimension: GoogleAdsSearchads360V23Common__UnknownListingDimensionInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ListingDimensionPath(
    typing.TypedDict, total=False
):
    dimensions: _list[GoogleAdsSearchads360V23Common__ListingDimensionInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ListingGroupInfo(typing.TypedDict, total=False):
    caseValue: GoogleAdsSearchads360V23Common__ListingDimensionInfo
    parentAdGroupCriterion: str
    path: GoogleAdsSearchads360V23Common__ListingDimensionPath
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "SUBDIVISION", "UNIT"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ListingScopeInfo(typing.TypedDict, total=False):
    dimensions: _list[GoogleAdsSearchads360V23Common__ListingDimensionInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocalAdInfo(typing.TypedDict, total=False):
    callToActions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    logoImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    marketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    path1: str
    path2: str
    videos: _list[GoogleAdsSearchads360V23Common__AdVideoAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocalServiceIdInfo(typing.TypedDict, total=False):
    serviceId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocalServicesDocumentReadOnly(
    typing.TypedDict, total=False
):
    documentUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocationAsset(typing.TypedDict, total=False):
    businessProfileLocations: _list[
        GoogleAdsSearchads360V23Common__BusinessProfileLocation
    ]
    locationOwnershipType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BUSINESS_OWNER", "AFFILIATE"
    ]
    placeId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocationAttributeMetadata(
    typing.TypedDict, total=False
):
    countryLocation: GoogleAdsSearchads360V23Common__LocationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocationGroupInfo(typing.TypedDict, total=False):
    enableCustomerLevelLocationAssetSet: bool
    feedItemSets: _list[str]
    geoTargetConstants: _list[str]
    locationGroupAssetSets: _list[str]
    radius: str
    radiusUnits: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "METERS", "MILES", "MILLI_MILES"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocationInfo(typing.TypedDict, total=False):
    geoTargetConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LocationSet(typing.TypedDict, total=False):
    businessProfileLocationSet: (
        GoogleAdsSearchads360V23Common__BusinessProfileLocationSet
    )
    chainLocationSet: GoogleAdsSearchads360V23Common__ChainSet
    locationOwnershipType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BUSINESS_OWNER", "AFFILIATE"
    ]
    mapsLocationSet: GoogleAdsSearchads360V23Common__MapsLocationSet

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LogicalUserListInfo(
    typing.TypedDict, total=False
):
    rules: _list[GoogleAdsSearchads360V23Common__UserListLogicalRuleInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LogicalUserListOperandInfo(
    typing.TypedDict, total=False
):
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__LookalikeUserListInfo(
    typing.TypedDict, total=False
):
    countryCodes: _list[str]
    expansionLevel: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NARROW", "BALANCED", "BROAD"
    ]
    seedUserListIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ManualCpa(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ManualCpc(typing.TypedDict, total=False):
    enhancedCpcEnabled: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ManualCpm(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ManualCpv(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MapsLocationInfo(typing.TypedDict, total=False):
    placeId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MapsLocationSet(typing.TypedDict, total=False):
    mapsLocations: _list[GoogleAdsSearchads360V23Common__MapsLocationInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MaximizeConversionValue(
    typing.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetRoas: float
    targetRoasTolerancePercentMillis: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MaximizeConversions(
    typing.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MediaBundleAsset(typing.TypedDict, total=False):
    data: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MetricGoal(typing.TypedDict, total=False):
    direction: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_CHANGE",
        "INCREASE",
        "DECREASE",
        "NO_CHANGE_OR_INCREASE",
        "NO_CHANGE_OR_DECREASE",
    ]
    metric: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CLICKS",
        "IMPRESSIONS",
        "COST",
        "CONVERSIONS_PER_INTERACTION_RATE",
        "COST_PER_CONVERSION",
        "CONVERSIONS_VALUE_PER_COST",
        "AVERAGE_CPC",
        "CTR",
        "INCREMENTAL_CONVERSIONS",
        "COMPLETED_VIDEO_VIEWS",
        "CUSTOM_ALGORITHMS",
        "CONVERSIONS",
        "CONVERSION_VALUE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Metrics(typing.TypedDict, total=False):
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
    conversionCustomMetrics: _list[GoogleAdsSearchads360V23Common__Value]
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
    historicalCreativeQualityScore: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    historicalLandingPageQualityScore: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    historicalQualityScore: str
    historicalSearchPredictedCtr: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    impressions: str
    interactionEventTypes: _list[
        typing.Literal[
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
    rawEventConversionMetrics: _list[GoogleAdsSearchads360V23Common__Value]
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
class GoogleAdsSearchads360V23Common__MobileAppAsset(typing.TypedDict, total=False):
    appId: str
    appStore: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_APP_STORE"
    ]
    endDate: str
    linkText: str
    startDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MobileAppCategoryInfo(
    typing.TypedDict, total=False
):
    mobileAppCategoryConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MobileApplicationInfo(
    typing.TypedDict, total=False
):
    appId: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MobileDeviceInfo(typing.TypedDict, total=False):
    mobileDeviceConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Money(typing.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__MonthlySearchVolume(
    typing.TypedDict, total=False
):
    month: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    monthlySearches: str
    year: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__NegativeKeywordListInfo(
    typing.TypedDict, total=False
):
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__OfflineUserAddressInfo(
    typing.TypedDict, total=False
):
    city: str
    countryCode: str
    hashedFirstName: str
    hashedLastName: str
    hashedStreetAddress: str
    postalCode: str
    state: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__OperatingSystemVersionInfo(
    typing.TypedDict, total=False
):
    operatingSystemVersionConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PageFeedAsset(typing.TypedDict, total=False):
    labels: _list[str]
    pageUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ParentalStatusDimension(
    typing.TypedDict, total=False
):
    includeUndetermined: bool
    parentalStatuses: _list[
        typing.Literal[
            "UNSPECIFIED", "UNKNOWN", "PARENT", "NOT_A_PARENT", "UNDETERMINED"
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ParentalStatusInfo(typing.TypedDict, total=False):
    type: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PARENT", "NOT_A_PARENT", "UNDETERMINED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PercentCpc(typing.TypedDict, total=False):
    cpcBidCeilingMicros: str
    enhancedCpcEnabled: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PercentCpcBidSimulationPoint(
    typing.TypedDict, total=False
):
    biddableConversions: float
    biddableConversionsValue: float
    clicks: str
    costMicros: str
    impressions: str
    percentCpcBidMicros: str
    topSlotImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PercentCpcBidSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__PercentCpcBidSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PlacementInfo(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PlacementListInfo(typing.TypedDict, total=False):
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicySummary(typing.TypedDict, total=False):
    approvalStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISAPPROVED",
        "APPROVED_LIMITED",
        "APPROVED",
        "AREA_OF_INTEREST_ONLY",
    ]
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]
    reviewStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REVIEW_IN_PROGRESS",
        "REVIEWED",
        "UNDER_APPEAL",
        "ELIGIBLE_MAY_SERVE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicyTopicConstraint(
    typing.TypedDict, total=False
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
class GoogleAdsSearchads360V23Common__PolicyTopicEntry(typing.TypedDict, total=False):
    constraints: _list[GoogleAdsSearchads360V23Common__PolicyTopicConstraint]
    evidences: _list[GoogleAdsSearchads360V23Common__PolicyTopicEvidence]
    topic: str
    type: typing.Literal[
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
    typing.TypedDict, total=False
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
class GoogleAdsSearchads360V23Common__PolicyValidationParameter(
    typing.TypedDict, total=False
):
    exemptPolicyViolationKeys: _list[GoogleAdsSearchads360V23Common__PolicyViolationKey]
    ignorablePolicyTopics: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PolicyViolationKey(typing.TypedDict, total=False):
    policyName: str
    violatingText: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PriceAsset(typing.TypedDict, total=False):
    languageCode: str
    priceOfferings: _list[GoogleAdsSearchads360V23Common__PriceOffering]
    priceQualifier: typing.Literal["UNSPECIFIED", "UNKNOWN", "FROM", "UP_TO", "AVERAGE"]
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BRANDS",
        "EVENTS",
        "LOCATIONS",
        "NEIGHBORHOODS",
        "PRODUCT_CATEGORIES",
        "PRODUCT_TIERS",
        "SERVICES",
        "SERVICE_CATEGORIES",
        "SERVICE_TIERS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PriceOffering(typing.TypedDict, total=False):
    description: str
    finalMobileUrl: str
    finalUrl: str
    header: str
    price: GoogleAdsSearchads360V23Common__Money
    unit: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PER_HOUR",
        "PER_DAY",
        "PER_WEEK",
        "PER_MONTH",
        "PER_YEAR",
        "PER_NIGHT",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductBrandInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductCategoryInfo(
    typing.TypedDict, total=False
):
    categoryId: str
    level: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductChannelExclusivityInfo(
    typing.TypedDict, total=False
):
    channelExclusivity: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SINGLE_CHANNEL", "MULTI_CHANNEL"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductChannelInfo(typing.TypedDict, total=False):
    channel: typing.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductConditionInfo(
    typing.TypedDict, total=False
):
    condition: typing.Literal["UNSPECIFIED", "UNKNOWN", "NEW", "REFURBISHED", "USED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductCustomAttributeInfo(
    typing.TypedDict, total=False
):
    index: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INDEX0", "INDEX1", "INDEX2", "INDEX3", "INDEX4"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductGroupingInfo(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductItemIdInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductLabelsInfo(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductLegacyConditionInfo(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductTypeFullInfo(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProductTypeInfo(typing.TypedDict, total=False):
    level: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PromotionAsset(typing.TypedDict, total=False):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    discountModifier: typing.Literal["UNSPECIFIED", "UNKNOWN", "UP_TO"]
    endDate: str
    languageCode: str
    moneyAmountOff: GoogleAdsSearchads360V23Common__Money
    occasion: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NEW_YEARS",
        "CHINESE_NEW_YEAR",
        "VALENTINES_DAY",
        "EASTER",
        "MOTHERS_DAY",
        "FATHERS_DAY",
        "LABOR_DAY",
        "BACK_TO_SCHOOL",
        "HALLOWEEN",
        "BLACK_FRIDAY",
        "CYBER_MONDAY",
        "CHRISTMAS",
        "BOXING_DAY",
        "INDEPENDENCE_DAY",
        "NATIONAL_DAY",
        "END_OF_SEASON",
        "WINTER_SALE",
        "SUMMER_SALE",
        "FALL_SALE",
        "SPRING_SALE",
        "RAMADAN",
        "EID_AL_FITR",
        "EID_AL_ADHA",
        "SINGLES_DAY",
        "WOMENS_DAY",
        "HOLI",
        "PARENTS_DAY",
        "ST_NICHOLAS_DAY",
        "CARNIVAL",
        "EPIPHANY",
        "ROSH_HASHANAH",
        "PASSOVER",
        "HANUKKAH",
        "DIWALI",
        "NAVRATRI",
        "SONGKRAN",
        "YEAR_END_GIFT",
    ]
    ordersOverAmount: GoogleAdsSearchads360V23Common__Money
    percentOff: str
    promotionBarcodeInfo: GoogleAdsSearchads360V23Common__PromotionBarcodeInfo
    promotionCode: str
    promotionQrCodeInfo: GoogleAdsSearchads360V23Common__PromotionQrCodeInfo
    promotionTarget: str
    redemptionEndDate: str
    redemptionStartDate: str
    startDate: str
    termsAndConditionsText: str
    termsAndConditionsUri: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PromotionBarcodeInfo(
    typing.TypedDict, total=False
):
    barcodeContent: str
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AZTEC",
        "CODABAR",
        "CODE39",
        "CODE128",
        "DATA_MATRIX",
        "EAN8",
        "EAN13",
        "ITF",
        "PDF417",
        "UPC_A",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__PromotionQrCodeInfo(
    typing.TypedDict, total=False
):
    qrCodeContent: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ProximityInfo(typing.TypedDict, total=False):
    address: GoogleAdsSearchads360V23Common__AddressInfo
    geoPoint: GoogleAdsSearchads360V23Common__GeoPointInfo
    radius: float
    radiusUnits: typing.Literal["UNSPECIFIED", "UNKNOWN", "MILES", "KILOMETERS"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__RealTimeBiddingSetting(
    typing.TypedDict, total=False
):
    optIn: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ResponsiveDisplayAdControlSpec(
    typing.TypedDict, total=False
):
    enableAssetEnhancements: bool
    enableAutogenVideo: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ResponsiveDisplayAdInfo(
    typing.TypedDict, total=False
):
    accentColor: str
    allowFlexibleColor: bool
    businessName: str
    callToActionText: str
    controlSpec: GoogleAdsSearchads360V23Common__ResponsiveDisplayAdControlSpec
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    formatSetting: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ALL_FORMATS", "NON_NATIVE", "NATIVE"
    ]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    logoImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    longHeadline: GoogleAdsSearchads360V23Common__AdTextAsset
    mainColor: str
    marketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    pricePrefix: str
    promoText: str
    squareLogoImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    squareMarketingImages: _list[GoogleAdsSearchads360V23Common__AdImageAsset]
    youtubeVideos: _list[GoogleAdsSearchads360V23Common__AdVideoAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ResponsiveSearchAdInfo(
    typing.TypedDict, total=False
):
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    path1: str
    path2: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__RuleBasedUserListInfo(
    typing.TypedDict, total=False
):
    flexibleRuleUserList: GoogleAdsSearchads360V23Common__FlexibleRuleUserListInfo
    prepopulationStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "REQUESTED", "FINISHED", "FAILED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SearchAds360ExpandedDynamicSearchAdInfo(
    typing.TypedDict, total=False
):
    adTrackingId: str
    description1: str
    description2: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SearchAds360ExpandedTextAdInfo(
    typing.TypedDict, total=False
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
class GoogleAdsSearchads360V23Common__SearchAds360ProductAdInfo(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SearchAds360ResponsiveSearchAdInfo(
    typing.TypedDict, total=False
):
    adTrackingId: str
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    path1: str
    path2: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SearchAds360TextAdInfo(
    typing.TypedDict, total=False
):
    adTrackingId: str
    description1: str
    description2: str
    displayMobileUrl: str
    displayUrl: str
    headline: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SearchThemeInfo(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Segments(typing.TypedDict, total=False):
    adFormatType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OTHER",
        "UNSEGMENTED",
        "INSTREAM_SKIPPABLE",
        "INSTREAM_NON_SKIPPABLE",
        "INFEED",
        "BUMPER",
        "OUTSTREAM",
        "MASTHEAD",
        "AUDIO",
        "SHORTS",
        "PAUSE",
        "VERTICAL_ADS_PROMOTION",
        "VERTICAL_ADS_BOOKING_LINK",
        "TEXT",
    ]
    adNetworkType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH",
        "SEARCH_PARTNERS",
        "CONTENT",
        "MIXED",
        "YOUTUBE",
        "GOOGLE_TV",
        "GOOGLE_OWNED_CHANNELS",
        "GMAIL",
        "DISCOVER",
        "MAPS",
    ]
    assetInteractionTarget: GoogleAdsSearchads360V23Common__AssetInteractionTarget
    conversionAction: str
    conversionActionCategory: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DEFAULT",
        "PAGE_VIEW",
        "PURCHASE",
        "SIGNUP",
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
    conversionCustomDimensions: _list[GoogleAdsSearchads360V23Common__Value]
    date: str
    dayOfWeek: typing.Literal[
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
    device: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET", "DESKTOP", "CONNECTED_TV", "OTHER"
    ]
    geoTargetCity: str
    geoTargetCountry: str
    geoTargetMetro: str
    geoTargetPostalCode: str
    geoTargetRegion: str
    hour: int
    keyword: GoogleAdsSearchads360V23Common__Keyword
    mobileDevicePlatform: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ANDROID", "IOS", "OTHER_MOBILE", "DESKTOP"
    ]
    month: str
    productBiddingCategoryLevel1: str
    productBiddingCategoryLevel2: str
    productBiddingCategoryLevel3: str
    productBiddingCategoryLevel4: str
    productBiddingCategoryLevel5: str
    productBrand: str
    productChannel: typing.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]
    productChannelExclusivity: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SINGLE_CHANNEL", "MULTI_CHANNEL"
    ]
    productCondition: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NEW", "REFURBISHED", "USED"
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
    productSoldCondition: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NEW", "REFURBISHED", "USED"
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
    rawEventConversionDimensions: _list[GoogleAdsSearchads360V23Common__Value]
    verticalAdsEventParticipantDisplayNames: str
    verticalAdsHotelClass: str
    verticalAdsListing: str
    verticalAdsListingBrand: str
    verticalAdsListingCity: str
    verticalAdsListingCountry: str
    verticalAdsListingRegion: str
    verticalAdsPartnerAccount: str
    verticalAdsVertical: typing.Literal[
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
class GoogleAdsSearchads360V23Common__ShoppingComparisonListingAdInfo(
    typing.TypedDict, total=False
):
    headline: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ShoppingLoyalty(typing.TypedDict, total=False):
    loyaltyTier: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ShoppingProductAdInfo(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ShoppingSmartAdInfo(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SimilarUserListInfo(
    typing.TypedDict, total=False
):
    seedUserList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SitelinkAsset(typing.TypedDict, total=False):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    description1: str
    description2: str
    endDate: str
    linkText: str
    startDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SitelinkFeedItem(typing.TypedDict, total=False):
    finalMobileUrls: _list[str]
    finalUrlSuffix: str
    finalUrls: _list[str]
    line1: str
    line2: str
    linkText: str
    trackingUrlTemplate: str
    urlCustomParameters: _list[GoogleAdsSearchads360V23Common__CustomParameter]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SmartCampaignAdInfo(
    typing.TypedDict, total=False
):
    descriptions: _list[GoogleAdsSearchads360V23Common__AdTextAsset]
    headlines: _list[GoogleAdsSearchads360V23Common__AdTextAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__StoreAttribute(typing.TypedDict, total=False):
    storeCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__StoreSalesMetadata(typing.TypedDict, total=False):
    customKey: str
    loyaltyFraction: float
    thirdPartyMetadata: GoogleAdsSearchads360V23Common__StoreSalesThirdPartyMetadata
    transactionUploadFraction: float

@typing.type_check_only
class GoogleAdsSearchads360V23Common__StoreSalesThirdPartyMetadata(
    typing.TypedDict, total=False
):
    advertiserUploadDateTime: str
    bridgeMapVersionId: str
    partnerId: str
    partnerMatchFraction: float
    partnerUploadFraction: float
    validTransactionFraction: float

@typing.type_check_only
class GoogleAdsSearchads360V23Common__StructuredSnippetAsset(
    typing.TypedDict, total=False
):
    header: str
    values: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SyntheticContentAttestation(
    typing.TypedDict, total=False
):
    source: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ADVERTISER_ATTESTED",
        "GOOGLE_GENERATED_ADVERTISER_REVIEWED",
        "GOOGLE_GENERATED_FULLY_AUTOMATED",
    ]
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOT_SYNTHETIC", "IS_SYNTHETIC"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__SyntheticContentInfo(
    typing.TypedDict, total=False
):
    advertiserAttestation: GoogleAdsSearchads360V23Common__SyntheticContentAttestation
    systemAttestation: GoogleAdsSearchads360V23Common__SyntheticContentAttestation

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TagSnippet(typing.TypedDict, total=False):
    eventSnippet: str
    globalSiteTag: str
    pageFormat: typing.Literal["UNSPECIFIED", "UNKNOWN", "HTML", "AMP"]
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBPAGE",
        "WEBPAGE_ONCLICK",
        "CLICK_TO_CALL",
        "WEBSITE_CALL",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetCpa(typing.TypedDict, total=False):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetCpaSimulationPoint(
    typing.TypedDict, total=False
):
    appInstalls: float
    biddableConversions: float
    biddableConversionsValue: float
    clicks: str
    costMicros: str
    impressions: str
    inAppActions: float
    interactions: str
    requiredBudgetAmountMicros: str
    targetCpaMicros: str
    targetCpaScalingModifier: float
    topSlotImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetCpaSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__TargetCpaSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetCpc(typing.TypedDict, total=False):
    targetCpcMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetCpm(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetImpressionShare(
    typing.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    location: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ANYWHERE_ON_PAGE",
        "TOP_OF_PAGE",
        "ABSOLUTE_TOP_OF_PAGE",
    ]
    locationFractionMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetImpressionShareSimulationPoint(
    typing.TypedDict, total=False
):
    absoluteTopImpressions: str
    biddableConversions: float
    biddableConversionsValue: float
    clicks: str
    costMicros: str
    impressions: str
    requiredBudgetAmountMicros: str
    requiredCpcBidCeilingMicros: str
    targetImpressionShareMicros: str
    topSlotImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetImpressionShareSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__TargetImpressionShareSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetRestriction(typing.TypedDict, total=False):
    bidOnly: bool
    targetingDimension: typing.Literal[
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
class GoogleAdsSearchads360V23Common__TargetRestrictionOperation(
    typing.TypedDict, total=False
):
    operator: typing.Literal["UNSPECIFIED", "UNKNOWN", "ADD", "REMOVE"]
    value: GoogleAdsSearchads360V23Common__TargetRestriction

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetRoas(typing.TypedDict, total=False):
    cpcBidCeilingMicros: str
    cpcBidFloorMicros: str
    targetRoas: float
    targetRoasTolerancePercentMillis: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetRoasSimulationPoint(
    typing.TypedDict, total=False
):
    biddableConversions: float
    biddableConversionsValue: float
    clicks: str
    costMicros: str
    impressions: str
    requiredBudgetAmountMicros: str
    targetRoas: float
    topSlotImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetRoasSimulationPointList(
    typing.TypedDict, total=False
):
    points: _list[GoogleAdsSearchads360V23Common__TargetRoasSimulationPoint]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetSpend(typing.TypedDict, total=False):
    cpcBidCeilingMicros: str
    targetSpendMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TargetingSetting(typing.TypedDict, total=False):
    targetRestrictionOperations: _list[
        GoogleAdsSearchads360V23Common__TargetRestrictionOperation
    ]
    targetRestrictions: _list[GoogleAdsSearchads360V23Common__TargetRestriction]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TextAdInfo(typing.TypedDict, total=False):
    description1: str
    description2: str
    headline: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TextAsset(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TextLabel(typing.TypedDict, total=False):
    backgroundColor: str
    description: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ThirdPartyIntegrationPartnerData(
    typing.TypedDict, total=False
):
    clientId: str
    thirdPartyPlacementId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TopicInfo(typing.TypedDict, total=False):
    path: _list[str]
    topicConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TransactionAttribute(
    typing.TypedDict, total=False
):
    conversionAction: str
    currencyCode: str
    customValue: str
    itemAttribute: GoogleAdsSearchads360V23Common__ItemAttribute
    orderId: str
    storeAttribute: GoogleAdsSearchads360V23Common__StoreAttribute
    transactionAmountMicros: float
    transactionDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__TravelAdInfo(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UnifiedCallAsset(typing.TypedDict, total=False):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    callConversionAction: str
    callConversionReportingState: typing.Literal[
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
class GoogleAdsSearchads360V23Common__UnifiedCalloutAsset(
    typing.TypedDict, total=False
):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    calloutText: str
    endDate: str
    startDate: str
    useSearcherTimeZone: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UnifiedLocationAsset(
    typing.TypedDict, total=False
):
    businessProfileLocations: _list[
        GoogleAdsSearchads360V23Common__BusinessProfileLocation
    ]
    locationOwnershipType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BUSINESS_OWNER", "AFFILIATE"
    ]
    placeId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UnifiedPageFeedAsset(
    typing.TypedDict, total=False
):
    labels: _list[str]
    pageUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UnifiedSitelinkAsset(
    typing.TypedDict, total=False
):
    adScheduleTargets: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    description1: str
    description2: str
    endDate: str
    linkText: str
    mobilePreferred: bool
    startDate: str
    trackingId: str
    useSearcherTimeZone: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UnknownListingDimensionInfo(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UrlCollection(typing.TypedDict, total=False):
    finalMobileUrls: _list[str]
    finalUrls: _list[str]
    trackingUrlTemplate: str
    urlCollectionId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserAttribute(typing.TypedDict, total=False):
    acquisitionDateTime: str
    averagePurchaseCount: int
    averagePurchaseValueMicros: str
    eventAttribute: _list[GoogleAdsSearchads360V23Common__EventAttribute]
    firstPurchaseDateTime: str
    lastPurchaseDateTime: str
    lifecycleStage: str
    lifetimeValueBucket: int
    lifetimeValueMicros: str
    shoppingLoyalty: GoogleAdsSearchads360V23Common__ShoppingLoyalty

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserData(typing.TypedDict, total=False):
    consent: GoogleAdsSearchads360V23Common__Consent
    transactionAttribute: GoogleAdsSearchads360V23Common__TransactionAttribute
    userAttribute: GoogleAdsSearchads360V23Common__UserAttribute
    userIdentifiers: _list[GoogleAdsSearchads360V23Common__UserIdentifier]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserIdentifier(typing.TypedDict, total=False):
    addressInfo: GoogleAdsSearchads360V23Common__OfflineUserAddressInfo
    hashedEmail: str
    hashedPhoneNumber: str
    mobileId: str
    thirdPartyUserId: str
    userIdentifierSource: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "FIRST_PARTY", "THIRD_PARTY"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserInterestAttributeMetadata(
    typing.TypedDict, total=False
):
    userInterestDescription: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserInterestInfo(typing.TypedDict, total=False):
    userInterestCategory: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserInterestSegment(
    typing.TypedDict, total=False
):
    userInterestCategory: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListActionInfo(typing.TypedDict, total=False):
    conversionAction: str
    remarketingAction: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListAttributeMetadata(
    typing.TypedDict, total=False
):
    userListType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REMARKETING",
        "LOGICAL",
        "EXTERNAL_REMARKETING",
        "RULE_BASED",
        "SIMILAR",
        "CRM_BASED",
        "LOOKALIKE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListDateRuleItemInfo(
    typing.TypedDict, total=False
):
    offsetInDays: str
    operator: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EQUALS", "NOT_EQUALS", "BEFORE", "AFTER"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListInfo(typing.TypedDict, total=False):
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListLogicalRuleInfo(
    typing.TypedDict, total=False
):
    operator: typing.Literal["UNSPECIFIED", "UNKNOWN", "ALL", "ANY", "NONE"]
    ruleOperands: _list[GoogleAdsSearchads360V23Common__LogicalUserListOperandInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListNumberRuleItemInfo(
    typing.TypedDict, total=False
):
    operator: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "EQUALS",
        "NOT_EQUALS",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
    ]
    value: float

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListRuleInfo(typing.TypedDict, total=False):
    ruleItemGroups: _list[GoogleAdsSearchads360V23Common__UserListRuleItemGroupInfo]
    ruleType: typing.Literal["UNSPECIFIED", "UNKNOWN", "AND_OF_ORS", "OR_OF_ANDS"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListRuleItemGroupInfo(
    typing.TypedDict, total=False
):
    ruleItems: _list[GoogleAdsSearchads360V23Common__UserListRuleItemInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListRuleItemInfo(
    typing.TypedDict, total=False
):
    dateRuleItem: GoogleAdsSearchads360V23Common__UserListDateRuleItemInfo
    name: str
    numberRuleItem: GoogleAdsSearchads360V23Common__UserListNumberRuleItemInfo
    stringRuleItem: GoogleAdsSearchads360V23Common__UserListStringRuleItemInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListSegment(typing.TypedDict, total=False):
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__UserListStringRuleItemInfo(
    typing.TypedDict, total=False
):
    operator: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONTAINS",
        "EQUALS",
        "STARTS_WITH",
        "ENDS_WITH",
        "NOT_EQUALS",
        "NOT_CONTAINS",
        "NOT_STARTS_WITH",
        "NOT_ENDS_WITH",
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__Value(typing.TypedDict, total=False):
    booleanValue: bool
    doubleValue: float
    floatValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__VerticalAdsItemGroupRuleInfo(
    typing.TypedDict, total=False
):
    cityCriterionId: str
    countryCriterionId: str
    hotelClass: str
    itemCode: str
    regionCriterionId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__VerticalAdsItemGroupRuleListInfo(
    typing.TypedDict, total=False
):
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__VideoLineupInfo(typing.TypedDict, total=False):
    videoLineupId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__WebhookDelivery(typing.TypedDict, total=False):
    advertiserWebhookUrl: str
    googleSecret: str
    payloadSchemaVersion: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__WebpageConditionInfo(
    typing.TypedDict, total=False
):
    argument: str
    operand: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "URL",
        "CATEGORY",
        "PAGE_TITLE",
        "PAGE_CONTENT",
        "CUSTOM_LABEL",
    ]
    operator: typing.Literal["UNSPECIFIED", "UNKNOWN", "EQUALS", "CONTAINS"]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__WebpageInfo(typing.TypedDict, total=False):
    conditions: _list[GoogleAdsSearchads360V23Common__WebpageConditionInfo]
    coveragePercentage: float
    criterionName: str
    sample: GoogleAdsSearchads360V23Common__WebpageSampleInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Common__WebpageListInfo(typing.TypedDict, total=False):
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__WebpageSampleInfo(typing.TypedDict, total=False):
    sampleUrls: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Common__WhatsappBusinessMessageInfo(
    typing.TypedDict, total=False
):
    countryCode: str
    phoneNumber: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YearMonth(typing.TypedDict, total=False):
    month: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    year: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YearMonthRange(typing.TypedDict, total=False):
    end: GoogleAdsSearchads360V23Common__YearMonth
    start: GoogleAdsSearchads360V23Common__YearMonth

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YouTubeChannelAttributeMetadata(
    typing.TypedDict, total=False
):
    subscriberCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YouTubeChannelInfo(typing.TypedDict, total=False):
    channelId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YouTubeVideoAttributeMetadata(
    typing.TypedDict, total=False
):
    commentsCount: str
    likesCount: str
    publishDate: str
    thumbnailUrl: str
    videoProperties: _list[
        typing.Literal["UNSPECIFIED", "UNKNOWN", "LIVE_STREAM", "SHORTS"]
    ]
    videoUrl: str
    viewsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YouTubeVideoInfo(typing.TypedDict, total=False):
    videoId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__YoutubeVideoAsset(typing.TypedDict, total=False):
    youtubeVideoId: str
    youtubeVideoTitle: str

@typing.type_check_only
class GoogleAdsSearchads360V23Common__ZaloBusinessMessageInfo(
    typing.TypedDict, total=False
):
    customName: str
    oaId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors_ErrorLocation_FieldPathElement(
    typing.TypedDict, total=False
):
    fieldName: str
    index: int

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__BudgetPerDayMinimumErrorDetails(
    typing.TypedDict, total=False
):
    budgetPerDayMinimumMicros: str
    currencyCode: str
    failedBudgetAmountMicros: str
    failedBudgetTotalAmountMicros: str
    minimumBudgetAmountMicros: str
    minimumBudgetTotalAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ErrorCode(typing.TypedDict, total=False):
    accessInvitationError: typing.Literal[
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
    accountBudgetProposalError: typing.Literal[
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
    accountLinkError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_STATUS", "PERMISSION_DENIED"
    ]
    adCustomizerError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "COUNTDOWN_INVALID_DATE_FORMAT",
        "COUNTDOWN_DATE_IN_PAST",
        "COUNTDOWN_INVALID_LOCALE",
        "COUNTDOWN_INVALID_START_DAYS_BEFORE",
        "UNKNOWN_USER_LIST",
    ]
    adError: typing.Literal[
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
    adGroupAdError: typing.Literal[
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
    adGroupBidModifierError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CRITERION_ID_NOT_SUPPORTED",
        "CANNOT_OVERRIDE_OPTED_OUT_CAMPAIGN_CRITERION_BID_MODIFIER",
    ]
    adGroupCriterionCustomizerError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CRITERION_IS_NOT_KEYWORD"
    ]
    adGroupCriterionError: typing.Literal[
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
    adGroupCustomizerError: typing.Literal["UNSPECIFIED", "UNKNOWN"]
    adGroupError: typing.Literal[
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
    adGroupFeedError: typing.Literal[
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
    adParameterError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_CRITERION_MUST_BE_KEYWORD",
        "INVALID_INSERTION_TEXT_FORMAT",
    ]
    adSharingError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP_ALREADY_CONTAINS_AD",
        "INCOMPATIBLE_AD_UNDER_AD_GROUP",
        "CANNOT_SHARE_INACTIVE_AD",
    ]
    adxError: typing.Literal["UNSPECIFIED", "UNKNOWN", "UNSUPPORTED_FEATURE"]
    assetError: typing.Literal[
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
    assetGenerationError: typing.Literal[
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
    assetGroupAssetError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_RESOURCE",
        "EXPANDABLE_TAGS_NOT_ALLOWED_IN_DESCRIPTION",
        "AD_CUSTOMIZER_NOT_SUPPORTED",
        "HOTEL_PROPERTY_ASSET_NOT_LINKED_TO_CAMPAIGN",
    ]
    assetGroupError: typing.Literal[
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
    assetGroupListingGroupFilterError: typing.Literal[
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
    assetGroupSignalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TOO_MANY_WORDS",
        "SEARCH_THEME_POLICY_VIOLATION",
        "AUDIENCE_WITH_WRONG_ASSET_GROUP_ID",
    ]
    assetLinkError: typing.Literal[
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
    assetSetAssetError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_ASSET_TYPE",
        "INVALID_ASSET_SET_TYPE",
        "DUPLICATE_EXTERNAL_KEY",
        "PARENT_LINKAGE_DOES_NOT_EXIST",
    ]
    assetSetError: typing.Literal[
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
    assetSetLinkError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE",
        "DUPLICATE_FEED_LINK",
        "INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE",
        "DUPLICATE_ASSET_SET_LINK",
        "ASSET_SET_LINK_CANNOT_BE_REMOVED",
    ]
    audienceError: typing.Literal[
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
    audienceInsightsError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DIMENSION_INCOMPATIBLE_WITH_TOPIC_AUDIENCE_COMBINATIONS",
    ]
    authenticationError: typing.Literal[
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
    authorizationError: typing.Literal[
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
        "SEARCH_ADS360_OTHER_ENGINE_MUTATE_DENIED",
        "SEARCH_ADS360_MUTATE_ALLOWLIST_DENIED",
        "SEARCH_ADS360_MUTATE_FIELD_DENIED",
    ]
    automaticallyCreatedAssetRemovalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_DOES_NOT_EXIST",
        "INVALID_AD_TYPE",
        "ASSET_DOES_NOT_EXIST",
        "ASSET_FIELD_TYPE_DOES_NOT_MATCH",
        "NOT_AN_AUTOMATICALLY_CREATED_ASSET",
    ]
    batchJobError: typing.Literal[
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
    benchmarksError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MAX_QUERY_COMPLEXITY_EXCEEDED"
    ]
    biddingError: typing.Literal[
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
    biddingStrategyError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DUPLICATE_NAME",
        "CANNOT_CHANGE_BIDDING_STRATEGY_TYPE",
        "CANNOT_REMOVE_ASSOCIATED_STRATEGY",
        "BIDDING_STRATEGY_NOT_SUPPORTED",
        "INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE",
    ]
    billingSetupError: typing.Literal[
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
    brandGuidelinesMigrationError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BRAND_GUIDELINES_ALREADY_ENABLED",
        "CANNOT_ENABLE_BRAND_GUIDELINES_FOR_REMOVED_CAMPAIGN",
        "BRAND_GUIDELINES_LOGO_LIMIT_EXCEEDED",
        "CANNOT_AUTO_POPULATE_BRAND_ASSETS_WHEN_BRAND_ASSETS_PROVIDED",
        "AUTO_POPULATE_BRAND_ASSETS_REQUIRED_WHEN_BRAND_ASSETS_OMITTED",
        "TOO_MANY_ENABLE_OPERATIONS",
    ]
    campaignBudgetError: typing.Literal[
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
    campaignConversionGoalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN",
        "CANNOT_USE_STORE_SALE_GOAL_FOR_PERFORMANCE_MAX_CAMPAIGN",
    ]
    campaignCriterionError: typing.Literal[
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
    campaignCustomizerError: typing.Literal["UNSPECIFIED", "UNKNOWN"]
    campaignDraftError: typing.Literal[
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
    campaignError: typing.Literal[
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
    campaignExperimentError: typing.Literal[
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
    campaignFeedError: typing.Literal[
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
    campaignGoalConfigError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "GOAL_NOT_FOUND",
        "CAMPAIGN_NOT_FOUND",
        "HIGH_LIFETIME_VALUE_PRESENT_BUT_VALUE_ABSENT",
        "HIGH_LIFETIME_VALUE_LESS_THAN_OR_EQUAL_TO_VALUE",
        "CUSTOMER_LIFECYCLE_OPTIMIZATION_CAMPAIGN_TYPE_NOT_SUPPORTED",
        "CUSTOMER_NOT_ALLOWLISTED_FOR_RETENTION_ONLY",
        "CAMPAIGN_OVERRIDE_VALUES_SET_FOR_NEW_CUSTOMER_ACQUISITION_TARGET_SPECIFIC_OPTION",
        "CAMPAIGN_OVERRIDE_HIGH_LIFETIME_VALUE_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE",
        "CANNOT_USE_INCOMPATIBLE_CLO_GOALS",
        "LOYALTY_RETENTION_GOAL_INVALID_MODE",
    ]
    campaignLifecycleGoalError: typing.Literal[
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
    campaignSharedSetError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SHARED_SET_ACCESS_DENIED"
    ]
    changeEventError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "START_DATE_TOO_OLD",
        "CHANGE_DATE_RANGE_INFINITE",
        "CHANGE_DATE_RANGE_NEGATIVE",
        "LIMIT_NOT_SPECIFIED",
        "INVALID_LIMIT_CLAUSE",
    ]
    changeStatusError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "START_DATE_TOO_OLD",
        "CHANGE_DATE_RANGE_INFINITE",
        "CHANGE_DATE_RANGE_NEGATIVE",
        "LIMIT_NOT_SPECIFIED",
        "INVALID_LIMIT_CLAUSE",
    ]
    clickViewError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EXPECTED_FILTER_ON_A_SINGLE_DAY", "DATE_TOO_OLD"
    ]
    collectionSizeError: typing.Literal["UNSPECIFIED", "UNKNOWN", "TOO_FEW", "TOO_MANY"]
    contextError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPERATION_NOT_PERMITTED_FOR_CONTEXT",
        "OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE",
    ]
    conversionActionError: typing.Literal[
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
    conversionAdjustmentUploadError: typing.Literal[
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
    conversionCustomVariableError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_NAME", "DUPLICATE_TAG", "RESERVED_TAG"
    ]
    conversionGoalCampaignConfigError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN",
        "CUSTOM_GOAL_DOES_NOT_BELONG_TO_GOOGLE_ADS_CONVERSION_CUSTOMER",
        "CAMPAIGN_CANNOT_USE_UNIFIED_GOALS",
        "EMPTY_CONVERSION_GOALS",
        "STORE_SALE_STORE_VISIT_CANNOT_BE_BOTH_INCLUDED",
        "PERFORMANCE_MAX_CAMPAIGN_CANNOT_USE_CUSTOM_GOAL_WITH_STORE_SALES",
    ]
    conversionUploadError: typing.Literal[
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
    conversionValueRuleError: typing.Literal[
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
    conversionValueRuleSetError: typing.Literal[
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
    countryCodeError: typing.Literal["UNSPECIFIED", "UNKNOWN", "INVALID_COUNTRY_CODE"]
    criterionError: typing.Literal[
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
    currencyCodeError: typing.Literal["UNSPECIFIED", "UNKNOWN", "UNSUPPORTED"]
    currencyError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "VALUE_NOT_MULTIPLE_OF_BILLABLE_UNIT"
    ]
    customAudienceError: typing.Literal[
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
    customColumnError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOM_COLUMN_NOT_FOUND",
        "CUSTOM_COLUMN_NOT_AVAILABLE",
    ]
    customConversionGoalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_CONVERSION_ACTION",
        "CONVERSION_ACTION_NOT_ENABLED",
        "CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL",
        "CUSTOM_GOAL_DUPLICATE_NAME",
        "DUPLICATE_CONVERSION_ACTION_LIST",
        "NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL",
    ]
    customInterestError: typing.Literal[
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
    customerClientLinkError: typing.Literal[
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
    customerCustomizerError: typing.Literal["UNSPECIFIED", "UNKNOWN"]
    customerError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "STATUS_CHANGE_DISALLOWED",
        "ACCOUNT_NOT_SET_UP",
        "CREATION_DENIED_FOR_POLICY_VIOLATION",
        "CREATION_DENIED_INELIGIBLE_MCC",
    ]
    customerFeedError: typing.Literal[
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
    customerLifecycleGoalError: typing.Literal[
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
    customerManagerLinkError: typing.Literal[
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
    customerSkAdNetworkConversionValueSchemaError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_LINK_ID",
        "INVALID_APP_ID",
        "INVALID_SCHEMA",
        "LINK_CODE_NOT_FOUND",
        "INVALID_EVENT_COUNTER",
        "INVALID_EVENT_NAME",
    ]
    customerUserAccessError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_USER_ID",
        "REMOVAL_DISALLOWED",
        "DISALLOWED_ACCESS_ROLE",
        "LAST_ADMIN_USER_OF_SERVING_CUSTOMER",
        "LAST_ADMIN_USER_OF_MANAGER",
    ]
    customizerAttributeError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_CUSTOMIZER_ATTRIBUTE_NAME"
    ]
    dataLinkError: typing.Literal[
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
    databaseError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONCURRENT_MODIFICATION",
        "DATA_CONSTRAINT_VIOLATION",
        "REQUEST_TOO_LARGE",
    ]
    dateError: typing.Literal[
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
    dateRangeError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_DATE",
        "START_DATE_AFTER_END_DATE",
        "CANNOT_SET_DATE_TO_PAST",
        "AFTER_MAXIMUM_ALLOWABLE_DATE",
        "CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED",
        "REQUESTED_DATE_GRANULARITY_NOT_SUPPORTED",
    ]
    distinctError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_ELEMENT", "DUPLICATE_TYPE"
    ]
    enumError: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENUM_VALUE_NOT_PERMITTED"]
    experimentArmError: typing.Literal[
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
    experimentError: typing.Literal[
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
    extensionFeedItemError: typing.Literal[
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
    extensionSettingError: typing.Literal[
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
    feedAttributeReferenceError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_REFERENCE_REMOVED_FEED",
        "INVALID_FEED_NAME",
        "INVALID_FEED_ATTRIBUTE_NAME",
    ]
    feedError: typing.Literal[
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
    feedItemError: typing.Literal[
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
    feedItemSetError: typing.Literal[
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
    feedItemSetLinkError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FEED_ID_MISMATCH",
        "NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET",
    ]
    feedItemTargetError: typing.Literal[
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
    feedItemValidationError: typing.Literal[
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
    feedMappingError: typing.Literal[
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
    fieldError: typing.Literal[
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
    fieldMaskError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FIELD_MASK_MISSING",
        "FIELD_MASK_NOT_ALLOWED",
        "FIELD_NOT_FOUND",
        "FIELD_HAS_SUBFIELDS",
    ]
    finalUrlExpansionAssetViewError: typing.Literal[
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
    functionError: typing.Literal[
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
    functionParsingError: typing.Literal[
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
    geoTargetConstantSuggestionError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "LOCATION_NAME_SIZE_LIMIT",
        "LOCATION_NAME_LIMIT",
        "INVALID_COUNTRY_CODE",
        "REQUEST_PARAMETERS_UNSET",
    ]
    goalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RETENTION_GOAL_ALREADY_EXISTS",
        "HIGH_LIFETIME_VALUE_PRESENT_BUT_VALUE_ABSENT",
        "HIGH_LIFETIME_VALUE_LESS_THAN_OR_EQUAL_TO_VALUE",
        "CUSTOMER_LIFECYCLE_OPTIMIZATION_ACCOUNT_TYPE_NOT_ALLOWED",
    ]
    headerError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_LOGIN_CUSTOMER_ID",
        "INVALID_LINKED_CUSTOMER_ID",
    ]
    idError: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOT_FOUND"]
    identityVerificationError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NO_EFFECTIVE_BILLING",
        "BILLING_NOT_ON_MONTHLY_INVOICING",
        "VERIFICATION_ALREADY_STARTED",
    ]
    imageError: typing.Literal[
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
    incentiveError: typing.Literal["UNSPECIFIED", "UNKNOWN", "INVALID_INCENTIVE_ID"]
    internalError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INTERNAL_ERROR",
        "ERROR_CODE_NOT_PUBLISHED",
        "TRANSIENT_ERROR",
        "DEADLINE_EXCEEDED",
    ]
    invalidParameterError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_CURRENCY_CODE"
    ]
    invoiceError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "YEAR_MONTH_TOO_OLD",
        "NOT_INVOICED_CUSTOMER",
        "BILLING_SETUP_NOT_APPROVED",
        "BILLING_SETUP_NOT_ON_MONTHLY_INVOICING",
        "NON_SERVING_CUSTOMER",
    ]
    keywordPlanAdGroupError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INVALID_NAME", "DUPLICATE_NAME"
    ]
    keywordPlanAdGroupKeywordError: typing.Literal[
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
    keywordPlanCampaignError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_NAME",
        "INVALID_LANGUAGES",
        "INVALID_GEOS",
        "DUPLICATE_NAME",
        "MAX_GEOS_EXCEEDED",
        "MAX_LANGUAGES_EXCEEDED",
    ]
    keywordPlanCampaignKeywordError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CAMPAIGN_KEYWORD_IS_POSITIVE"
    ]
    keywordPlanError: typing.Literal[
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
    keywordPlanIdeaError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "URL_CRAWL_ERROR", "INVALID_VALUE"
    ]
    labelError: typing.Literal[
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
    languageCodeError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LANGUAGE_CODE_NOT_FOUND", "INVALID_LANGUAGE_CODE"
    ]
    listOperationError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "REQUIRED_FIELD_MISSING", "DUPLICATE_VALUES"
    ]
    managerLinkError: typing.Literal[
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
    mediaBundleError: typing.Literal[
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
    mediaFileError: typing.Literal[
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
    mediaUploadError: typing.Literal[
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
    merchantCenterError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MERCHANT_ID_CANNOT_BE_ACCESSED",
        "CUSTOMER_NOT_ALLOWED_FOR_SHOPPING_PERFORMANCE_MAX",
    ]
    multiplierError: typing.Literal[
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
    mutateError: typing.Literal[
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
    newResourceCreationError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CANNOT_SET_ID_FOR_CREATE",
        "DUPLICATE_TEMP_IDS",
        "TEMP_ID_RESOURCE_HAD_ERRORS",
    ]
    notAllowlistedError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE"
    ]
    notEmptyError: typing.Literal["UNSPECIFIED", "UNKNOWN", "EMPTY_LIST"]
    nullError: typing.Literal["UNSPECIFIED", "UNKNOWN", "NULL_CONTENT"]
    offlineUserDataJobError: typing.Literal[
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
    operationAccessDeniedError: typing.Literal[
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
    operatorError: typing.Literal["UNSPECIFIED", "UNKNOWN", "OPERATOR_NOT_SUPPORTED"]
    partialFailureError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PARTIAL_FAILURE_MODE_REQUIRED"
    ]
    paymentsAccountError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NOT_SUPPORTED_FOR_MANAGER_CUSTOMER"
    ]
    policyFindingError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "POLICY_FINDING", "POLICY_TOPIC_NOT_FOUND"
    ]
    policyValidationParameterError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "UNSUPPORTED_AD_TYPE_FOR_IGNORABLE_POLICY_TOPICS",
        "UNSUPPORTED_AD_TYPE_FOR_EXEMPT_POLICY_VIOLATION_KEYS",
        "CANNOT_SET_BOTH_IGNORABLE_POLICY_TOPICS_AND_EXEMPT_POLICY_VIOLATION_KEYS",
    ]
    policyViolationError: typing.Literal["UNSPECIFIED", "UNKNOWN", "POLICY_ERROR"]
    productLinkError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_OPERATION",
        "CREATION_NOT_PERMITTED",
        "INVITATION_EXISTS",
        "LINK_EXISTS",
    ]
    productLinkInvitationError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_STATUS",
        "PERMISSION_DENIED",
        "NO_INVITATION_REQUIRED",
        "CUSTOMER_NOT_PERMITTED_TO_CREATE_INVITATION",
    ]
    queryError: typing.Literal[
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
    quotaError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RESOURCE_EXHAUSTED",
        "ACCESS_PROHIBITED",
        "RESOURCE_TEMPORARILY_EXHAUSTED",
        "EXCESSIVE_SHORT_TERM_QUERY_RESOURCE_CONSUMPTION",
        "EXCESSIVE_LONG_TERM_QUERY_RESOURCE_CONSUMPTION",
        "PAYMENTS_PROFILE_ACTIVATION_RATE_LIMIT_EXCEEDED",
    ]
    rangeError: typing.Literal["UNSPECIFIED", "UNKNOWN", "TOO_LOW", "TOO_HIGH"]
    reachPlanError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NOT_FORECASTABLE_MISSING_RATE",
        "NOT_FORECASTABLE_NOT_ENOUGH_INVENTORY",
        "NOT_FORECASTABLE_ACCOUNT_NOT_ENABLED",
    ]
    recommendationError: typing.Literal[
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
    recommendationSubscriptionError: typing.Literal["UNSPECIFIED", "UNKNOWN"]
    regionCodeError: typing.Literal["UNSPECIFIED", "UNKNOWN", "INVALID_REGION_CODE"]
    requestError: typing.Literal[
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
    resourceAccessDeniedError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "WRITE_ACCESS_DENIED"
    ]
    resourceCountLimitExceededError: typing.Literal[
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
    searchTermInsightError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FILTERING_NOT_ALLOWED_WITH_SEGMENTS",
        "LIMIT_NOT_ALLOWED_WITH_SEGMENTS",
        "MISSING_FIELD_IN_SELECT_CLAUSE",
        "REQUIRES_FILTER_BY_SINGLE_RESOURCE",
        "SORTING_NOT_ALLOWED_WITH_SEGMENTS",
        "SUMMARY_ROW_NOT_ALLOWED_WITH_SEGMENTS",
    ]
    settingError: typing.Literal[
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
    shareablePreviewError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TOO_MANY_ASSET_GROUPS_IN_REQUEST",
        "ASSET_GROUP_DOES_NOT_EXIST_UNDER_THIS_CUSTOMER",
    ]
    sharedCriterionError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE"
    ]
    sharedSetError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE",
        "DUPLICATE_NAME",
        "SHARED_SET_REMOVED",
        "SHARED_SET_IN_USE",
    ]
    shoppingProductError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MISSING_CAMPAIGN_FILTER",
        "MISSING_AD_GROUP_FILTER",
        "UNSUPPORTED_DATE_SEGMENTATION",
    ]
    sizeLimitError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUEST_SIZE_LIMIT_EXCEEDED",
        "RESPONSE_SIZE_LIMIT_EXCEEDED",
    ]
    smartCampaignError: typing.Literal[
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
    stringFormatError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ILLEGAL_CHARS", "INVALID_FORMAT"
    ]
    stringLengthError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EMPTY", "TOO_SHORT", "TOO_LONG"
    ]
    thirdPartyAppAnalyticsLinkError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INVALID_ANALYTICS_PROVIDER_ID",
        "INVALID_MOBILE_APP_ID",
        "MOBILE_APP_IS_NOT_ENABLED",
        "CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK",
    ]
    timeZoneError: typing.Literal["UNSPECIFIED", "UNKNOWN", "INVALID_TIME_ZONE"]
    urlFieldError: typing.Literal[
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
    userDataError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED",
        "TOO_MANY_USER_IDENTIFIERS",
        "USER_LIST_NOT_APPLICABLE",
    ]
    userListCustomerTypeError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONFLICTING_CUSTOMER_TYPES",
        "NO_ACCESS_TO_USER_LIST",
        "USERLIST_NOT_ELIGIBLE",
        "CONVERSION_TRACKING_NOT_ENABLED_OR_NOT_MCC_MANAGER_ACCOUNT",
        "TOO_MANY_USER_LISTS_FOR_THE_CUSTOMER_TYPE",
    ]
    userListError: typing.Literal[
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
    videoCampaignError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MUTATE_REQUIRES_RESERVATION"
    ]
    youtubeVideoRegistrationError: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "VIDEO_NOT_FOUND",
        "VIDEO_NOT_ACCESSIBLE",
        "VIDEO_NOT_ELIGIBLE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ErrorDetails(typing.TypedDict, total=False):
    budgetPerDayMinimumErrorDetails: (
        GoogleAdsSearchads360V23Errors__BudgetPerDayMinimumErrorDetails
    )
    policyFindingDetails: GoogleAdsSearchads360V23Errors__PolicyFindingDetails
    policyViolationDetails: GoogleAdsSearchads360V23Errors__PolicyViolationDetails
    quotaErrorDetails: GoogleAdsSearchads360V23Errors__QuotaErrorDetails
    resourceCountDetails: GoogleAdsSearchads360V23Errors__ResourceCountDetails
    unpublishedErrorCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ErrorLocation(typing.TypedDict, total=False):
    fieldPathElements: _list[
        GoogleAdsSearchads360V23Errors_ErrorLocation_FieldPathElement
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__PolicyFindingDetails(
    typing.TypedDict, total=False
):
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__PolicyViolationDetails(
    typing.TypedDict, total=False
):
    externalPolicyDescription: str
    externalPolicyName: str
    isExemptible: bool
    key: GoogleAdsSearchads360V23Common__PolicyViolationKey

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__QuotaErrorDetails(typing.TypedDict, total=False):
    rateName: str
    rateScope: typing.Literal["UNSPECIFIED", "UNKNOWN", "ACCOUNT", "DEVELOPER"]
    retryDelay: str

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__ResourceCountDetails(
    typing.TypedDict, total=False
):
    enclosingId: str
    enclosingResource: str
    existingCount: int
    limit: int
    limitType: typing.Literal[
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
class GoogleAdsSearchads360V23Errors__SearchAds360Error(typing.TypedDict, total=False):
    details: GoogleAdsSearchads360V23Errors__ErrorDetails
    errorCode: GoogleAdsSearchads360V23Errors__ErrorCode
    location: GoogleAdsSearchads360V23Errors__ErrorLocation
    message: str
    trigger: GoogleAdsSearchads360V23Common__Value

@typing.type_check_only
class GoogleAdsSearchads360V23Errors__SearchAds360Failure(
    typing.TypedDict, total=False
):
    errors: _list[GoogleAdsSearchads360V23Errors__SearchAds360Error]
    requestId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_MaximizeConversionValue(
    typing.TypedDict, total=False
):
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_MaximizeConversions(
    typing.TypedDict, total=False
):
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetCpa(
    typing.TypedDict, total=False
):
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetImpressionShare(
    typing.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    location: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ANYWHERE_ON_PAGE",
        "TOP_OF_PAGE",
        "ABSOLUTE_TOP_OF_PAGE",
    ]
    locationFractionMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetRoas(
    typing.TypedDict, total=False
):
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetSpend(
    typing.TypedDict, total=False
):
    cpcBidCeilingMicros: str
    targetSpendMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AccountBudget_PendingAccountBudgetProposal(
    typing.TypedDict, total=False
):
    accountBudgetProposal: str
    creationDateTime: str
    endDateTime: str
    endTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    name: str
    notes: str
    proposalType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CREATE", "UPDATE", "END", "REMOVE"
    ]
    purchaseOrderNumber: str
    spendingLimitMicros: str
    spendingLimitType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INFINITE"]
    startDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroupCriterion_PositionEstimates(
    typing.TypedDict, total=False
):
    estimatedAddClicksAtFirstPositionCpc: str
    estimatedAddCostAtFirstPositionCpc: str
    firstPageCpcMicros: str
    firstPositionCpcMicros: str
    topOfPageCpcMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroupCriterion_QualityInfo(
    typing.TypedDict, total=False
):
    creativeQualityScore: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    postClickQualityScore: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]
    qualityScore: int
    searchPredictedCtr: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BELOW_AVERAGE", "AVERAGE", "ABOVE_AVERAGE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroupDemandGenAdGroupSettingsDemandGenChannelControls_DemandGenSelectedChannels(
    typing.TypedDict, total=False
):
    discover: bool
    display: bool
    gmail: bool
    youtubeInFeed: bool
    youtubeInStream: bool
    youtubeShorts: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroupDemandGenAdGroupSettings_DemandGenChannelControls(
    typing.TypedDict, total=False
):
    channelConfig: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CHANNEL_STRATEGY", "SELECTED_CHANNELS"
    ]
    channelStrategy: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ALL_CHANNELS", "ALL_OWNED_AND_OPERATED_CHANNELS"
    ]
    selectedChannels: GoogleAdsSearchads360V23Resources_AdGroupDemandGenAdGroupSettingsDemandGenChannelControls_DemandGenSelectedChannels

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroup_AiMaxAdGroupSetting(
    typing.TypedDict, total=False
):
    disableSearchTermMatching: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroup_AudienceSetting(
    typing.TypedDict, total=False
):
    useAudienceGrouped: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroup_DemandGenAdGroupSettings(
    typing.TypedDict, total=False
):
    channelControls: GoogleAdsSearchads360V23Resources_AdGroupDemandGenAdGroupSettings_DemandGenChannelControls

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdGroup_VerticalAdsFormatSetting(
    typing.TypedDict, total=False
):
    disableTextAds: bool
    enableBookingLinks: bool
    enableVerticalPromotionAds: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AdStrengthActionItem_AddAssetDetails(
    typing.TypedDict, total=False
):
    assetCount: int
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    videoAspectRatioRequirement: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "HORIZONTAL", "SQUARE", "VERTICAL"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AssetSet_HotelPropertyData(
    typing.TypedDict, total=False
):
    hotelCenterId: str
    partnerName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_AssetSet_MerchantCenterFeed(
    typing.TypedDict, total=False
):
    feedLabel: str
    merchantId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_BatchJob_BatchJobMetadata(
    typing.TypedDict, total=False
):
    completionDateTime: str
    creationDateTime: str
    estimatedCompletionRatio: float
    executedOperationCount: str
    executionLimitSeconds: int
    operationCount: str
    startDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_BillingSetup_PaymentsAccountInfo(
    typing.TypedDict, total=False
):
    paymentsAccountId: str
    paymentsAccountName: str
    paymentsProfileId: str
    paymentsProfileName: str
    secondaryPaymentsProfileId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CampaignPmaxCampaignSettings_BrandTargetingOverrides(
    typing.TypedDict, total=False
):
    ignoreExclusionsForShoppingAds: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_AiMaxSetting(
    typing.TypedDict, total=False
):
    bundlingRequired: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NOT_REQUIRED", "REQUIRED"
    ]
    enableAiMax: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_AppCampaignSetting(
    typing.TypedDict, total=False
):
    appId: str
    appStore: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_APP_STORE"
    ]
    biddingStrategyGoalType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPTIMIZE_INSTALLS_TARGET_INSTALL_COST",
        "OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST",
        "OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST",
        "OPTIMIZE_RETURN_ON_ADVERTISING_SPEND",
        "OPTIMIZE_PRE_REGISTRATION_CONVERSION_VOLUME",
        "OPTIMIZE_INSTALLS_WITHOUT_TARGET_INSTALL_COST",
        "OPTIMIZE_IN_APP_CONVERSIONS_WITHOUT_TARGET_CPA",
        "OPTIMIZE_TOTAL_VALUE_WITHOUT_TARGET_ROAS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_AssetAutomationSetting(
    typing.TypedDict, total=False
):
    assetAutomationStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "OPTED_IN", "OPTED_OUT"
    ]
    assetAutomationType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TEXT_ASSET_AUTOMATION",
        "GENERATE_VERTICAL_YOUTUBE_VIDEOS",
        "GENERATE_SHORTER_YOUTUBE_VIDEOS",
        "GENERATE_LANDING_PAGE_PREVIEW",
        "GENERATE_LANDING_PAGE_TEXT",
        "GENERATE_ENHANCED_YOUTUBE_VIDEOS",
        "GENERATE_IMAGE_ENHANCEMENT",
        "GENERATE_IMAGE_EXTRACTION",
        "GENERATE_DESIGN_VERSIONS_FOR_IMAGES",
        "FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION",
        "GENERATE_VIDEOS_FROM_OTHER_ASSETS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_AudienceSetting(
    typing.TypedDict, total=False
):
    useAudienceGrouped: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_BrandGuidelines(
    typing.TypedDict, total=False
):
    accentColor: str
    mainColor: str
    predefinedFontFamily: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_CategoryBid(
    typing.TypedDict, total=False
):
    categoryId: str
    manualCpaBidMicros: str
    targetCpaBidMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_DemandGenCampaignSettings(
    typing.TypedDict, total=False
):
    upgradedTargeting: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_DynamicSearchAdsSetting(
    typing.TypedDict, total=False
):
    domainName: str
    languageCode: str
    useSuppliedUrlsOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_GeoTargetTypeSetting(
    typing.TypedDict, total=False
):
    negativeGeoTargetType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PRESENCE_OR_INTEREST", "PRESENCE"
    ]
    positiveGeoTargetType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PRESENCE_OR_INTEREST", "SEARCH_INTEREST", "PRESENCE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_HotelSettingInfo(
    typing.TypedDict, total=False
):
    hotelCenterId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_LocalCampaignSetting(
    typing.TypedDict, total=False
):
    locationSourceType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "GOOGLE_MY_BUSINESS", "AFFILIATE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_LocalServicesCampaignSettings(
    typing.TypedDict, total=False
):
    categoryBids: _list[GoogleAdsSearchads360V23Resources_Campaign_CategoryBid]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_NetworkSettings(
    typing.TypedDict, total=False
):
    targetContentNetwork: bool
    targetGoogleSearch: bool
    targetGoogleTvNetwork: bool
    targetPartnerSearchNetwork: bool
    targetSearchNetwork: bool
    targetYoutube: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_OptimizationGoalSetting(
    typing.TypedDict, total=False
):
    optimizationGoalTypes: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CALL_CLICKS",
            "DRIVING_DIRECTIONS",
            "APP_PRE_REGISTRATION",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_PerformanceMaxUpgrade(
    typing.TypedDict, total=False
):
    performanceMaxCampaign: str
    preUpgradeCampaign: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "UPGRADE_IN_PROGRESS",
        "UPGRADE_COMPLETE",
        "UPGRADE_FAILED",
        "UPGRADE_ELIGIBLE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_PmaxCampaignSettings(
    typing.TypedDict, total=False
):
    brandTargetingOverrides: GoogleAdsSearchads360V23Resources_CampaignPmaxCampaignSettings_BrandTargetingOverrides

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_SelectiveOptimization(
    typing.TypedDict, total=False
):
    conversionActions: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_ShoppingSetting(
    typing.TypedDict, total=False
):
    advertisingPartnerIds: _list[str]
    campaignPriority: int
    disableProductFeed: bool
    enableLocal: bool
    feedLabel: str
    merchantId: str
    useVehicleInventory: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_TrackingSetting(
    typing.TypedDict, total=False
):
    trackingUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_TravelCampaignSettings(
    typing.TypedDict, total=False
):
    travelAccountId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Campaign_VanityPharma(
    typing.TypedDict, total=False
):
    vanityPharmaDisplayUrlMode: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MANUFACTURER_WEBSITE_URL", "WEBSITE_DESCRIPTION"
    ]
    vanityPharmaText: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PRESCRIPTION_TREATMENT_WEBSITE_EN",
        "PRESCRIPTION_TREATMENT_WEBSITE_ES",
        "PRESCRIPTION_DEVICE_WEBSITE_EN",
        "PRESCRIPTION_DEVICE_WEBSITE_ES",
        "MEDICAL_DEVICE_WEBSITE_EN",
        "MEDICAL_DEVICE_WEBSITE_ES",
        "PREVENTATIVE_TREATMENT_WEBSITE_EN",
        "PREVENTATIVE_TREATMENT_WEBSITE_ES",
        "PRESCRIPTION_CONTRACEPTION_WEBSITE_EN",
        "PRESCRIPTION_CONTRACEPTION_WEBSITE_ES",
        "PRESCRIPTION_VACCINE_WEBSITE_EN",
        "PRESCRIPTION_VACCINE_WEBSITE_ES",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ChangeEvent_ChangedResource(
    typing.TypedDict, total=False
):
    ad: GoogleAdsSearchads360V23Resources__Ad
    adGroup: GoogleAdsSearchads360V23Resources__AdGroup
    adGroupAd: GoogleAdsSearchads360V23Resources__AdGroupAd
    adGroupAsset: GoogleAdsSearchads360V23Resources__AdGroupAsset
    adGroupBidModifier: GoogleAdsSearchads360V23Resources__AdGroupBidModifier
    adGroupCriterion: GoogleAdsSearchads360V23Resources__AdGroupCriterion
    asset: GoogleAdsSearchads360V23Resources__Asset
    assetSet: GoogleAdsSearchads360V23Resources__AssetSet
    assetSetAsset: GoogleAdsSearchads360V23Resources__AssetSetAsset
    campaign: GoogleAdsSearchads360V23Resources__Campaign
    campaignAsset: GoogleAdsSearchads360V23Resources__CampaignAsset
    campaignAssetSet: GoogleAdsSearchads360V23Resources__CampaignAssetSet
    campaignBudget: GoogleAdsSearchads360V23Resources__CampaignBudget
    campaignCriterion: GoogleAdsSearchads360V23Resources__CampaignCriterion
    customerAsset: GoogleAdsSearchads360V23Resources__CustomerAsset

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionAction_AttributionModelSettings(
    typing.TypedDict, total=False
):
    attributionModel: typing.Literal[
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
    dataDrivenModelStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AVAILABLE", "STALE", "EXPIRED", "NEVER_GENERATED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionAction_FirebaseSettings(
    typing.TypedDict, total=False
):
    eventName: str
    projectId: str
    propertyId: str
    propertyName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionAction_FloodlightSettings(
    typing.TypedDict, total=False
):
    activityGroupTag: str
    activityId: str
    activityTag: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionAction_GoogleAnalytics4Settings(
    typing.TypedDict, total=False
):
    eventName: str
    propertyId: str
    propertyName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionAction_ThirdPartyAppAnalyticsSettings(
    typing.TypedDict, total=False
):
    eventName: str
    providerName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionAction_ValueSettings(
    typing.TypedDict, total=False
):
    alwaysUseDefaultValue: bool
    defaultCurrencyCode: str
    defaultValue: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionCustomVariable_FloodlightConversionCustomVariableInfo(
    typing.TypedDict, total=False
):
    floodlightVariableDataType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NUMBER", "STRING"
    ]
    floodlightVariableType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DIMENSION", "METRIC", "UNSET"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleAction(
    typing.TypedDict, total=False
):
    operation: typing.Literal["UNSPECIFIED", "UNKNOWN", "ADD", "MULTIPLY", "SET"]
    value: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleAudienceCondition(
    typing.TypedDict, total=False
):
    userInterests: _list[str]
    userLists: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleDeviceCondition(
    typing.TypedDict, total=False
):
    deviceTypes: _list[
        typing.Literal["UNSPECIFIED", "UNKNOWN", "MOBILE", "DESKTOP", "TABLET"]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleGeoLocationCondition(
    typing.TypedDict, total=False
):
    excludedGeoMatchType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ANY", "LOCATION_OF_PRESENCE"
    ]
    excludedGeoTargetConstants: _list[str]
    geoMatchType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ANY", "LOCATION_OF_PRESENCE"
    ]
    geoTargetConstants: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryAdvanceBookingWindow(
    typing.TypedDict, total=False
):
    maxDays: int
    minDays: int

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryCondition(
    typing.TypedDict, total=False
):
    advanceBookingWindow: GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryAdvanceBookingWindow
    travelLength: GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryTravelLength
    travelStartDay: GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryTravelStartDay

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryTravelLength(
    typing.TypedDict, total=False
):
    maxNights: int
    minNights: int

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryTravelStartDay(
    typing.TypedDict, total=False
):
    friday: bool
    monday: bool
    saturday: bool
    sunday: bool
    thursday: bool
    tuesday: bool
    wednesday: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchemaEvent_EventOccurrenceRange(
    typing.TypedDict, total=False
):
    maxEventCount: str
    minEventCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchemaEvent_RevenueRange(
    typing.TypedDict, total=False
):
    maxEventRevenue: float
    minEventRevenue: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_CoarseGrainedConversionValueMappings(
    typing.TypedDict, total=False
):
    highConversionValueMapping: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_ConversionValueMapping
    lowConversionValueMapping: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_ConversionValueMapping
    mediumConversionValueMapping: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_ConversionValueMapping

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_ConversionValueMapping(
    typing.TypedDict, total=False
):
    mappedEvents: _list[
        GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_Event
    ]
    maxTimePostInstallHours: str
    minTimePostInstallHours: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_Event(
    typing.TypedDict, total=False
):
    currencyCode: str
    eventCounter: str
    eventOccurrenceRange: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchemaEvent_EventOccurrenceRange
    eventRevenueRange: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchemaEvent_RevenueRange
    eventRevenueValue: float
    mappedEventName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_FineGrainedConversionValueMappings(
    typing.TypedDict, total=False
):
    conversionValueMapping: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_ConversionValueMapping
    fineGrainedConversionValue: int

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_PostbackMapping(
    typing.TypedDict, total=False
):
    coarseGrainedConversionValueMappings: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_CoarseGrainedConversionValueMappings
    lockWindowCoarseConversionValue: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "UNAVAILABLE", "LOW", "MEDIUM", "HIGH", "NONE"
    ]
    lockWindowEvent: str
    lockWindowFineConversionValue: int
    postbackSequenceIndex: int

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchema_SkAdNetworkConversionValueSchema(
    typing.TypedDict, total=False
):
    appId: str
    fineGrainedConversionValueMappings: _list[
        GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_FineGrainedConversionValueMappings
    ]
    measurementWindowHours: int
    postbackMappings: _list[
        GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchemaSkAdNetworkConversionValueSchema_PostbackMapping
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ExperimentArm_AssetGroupAssetInfo(
    typing.TypedDict, total=False
):
    asset: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ExperimentArm_AssetGroupInfo(
    typing.TypedDict, total=False
):
    assetGroup: str
    assetGroupAssets: _list[
        GoogleAdsSearchads360V23Resources_ExperimentArm_AssetGroupAssetInfo
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Invoice_AccountBudgetSummary(
    typing.TypedDict, total=False
):
    accountBudget: str
    accountBudgetName: str
    billableActivityDateRange: GoogleAdsSearchads360V23Common__DateRange
    billedAmountMicros: str
    campaignSummaries: _list[GoogleAdsSearchads360V23Resources_Invoice_CampaignSummary]
    customer: str
    customerDescriptiveName: str
    invalidActivityAmountMicros: str
    invalidActivitySummaries: _list[
        GoogleAdsSearchads360V23Resources_Invoice_InvalidActivitySummary
    ]
    overdeliveryAmountMicros: str
    purchaseOrderNumber: str
    servedAmountMicros: str
    subtotalAmountMicros: str
    taxAmountMicros: str
    totalAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Invoice_AccountSummary(
    typing.TypedDict, total=False
):
    adjustmentSummaries: _list[
        GoogleAdsSearchads360V23Resources_Invoice_AdjustmentSummary
    ]
    billingCorrectionSubtotalAmountMicros: str
    billingCorrectionTaxAmountMicros: str
    billingCorrectionTotalAmountMicros: str
    couponAdjustmentSubtotalAmountMicros: str
    couponAdjustmentTaxAmountMicros: str
    couponAdjustmentTotalAmountMicros: str
    customer: str
    excessCreditAdjustmentSubtotalAmountMicros: str
    excessCreditAdjustmentTaxAmountMicros: str
    excessCreditAdjustmentTotalAmountMicros: str
    exportChargeSubtotalAmountMicros: str
    exportChargeTaxAmountMicros: str
    exportChargeTotalAmountMicros: str
    regulatoryCostSummaries: _list[
        GoogleAdsSearchads360V23Resources_Invoice_RegulatoryCostSummary
    ]
    regulatoryCostsSubtotalAmountMicros: str
    regulatoryCostsTaxAmountMicros: str
    regulatoryCostsTotalAmountMicros: str
    subtotalAmountMicros: str
    taxAmountMicros: str
    totalAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Invoice_AdjustmentSummary(
    typing.TypedDict, total=False
):
    adjustmentDescription: str
    amountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Invoice_CampaignSummary(
    typing.TypedDict, total=False
):
    amountMicros: str
    campaignDescription: str
    quantity: str
    unitOfMeasure: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CLICKS",
        "IMPRESSIONS",
        "ACQUISITIONS",
        "PHONE_CALLS",
        "VIDEO_PLAYS",
        "DAYS",
        "AUDIO_PLAYS",
        "ENGAGEMENTS",
        "SECONDS",
        "LEADS",
        "GUEST_STAYS",
        "HOURS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Invoice_InvalidActivitySummary(
    typing.TypedDict, total=False
):
    amountMicros: str
    originalAccountBudgetName: str
    originalInvoiceId: str
    originalMonthOfService: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    originalPurchaseOrderNumber: str
    originalYearOfService: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Invoice_RegulatoryCostSummary(
    typing.TypedDict, total=False
):
    amountMicros: str
    regulatoryFeeType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AUSTRIA_DST_FEE",
        "TURKIYE_REGULATORY_OPERATING_COST",
        "UK_DST_FEE",
        "SPAIN_REGULATORY_OPERATING_COST",
        "FRANCE_REGULATORY_OPERATING_COST",
        "ITALY_REGULATORY_OPERATING_COST",
        "INDIA_REGULATORY_OPERATING_COST",
        "POLAND_REGULATORY_OPERATING_COST",
        "OPERATING_CHARGES",
        "CANADA_DST_FEE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductBrand(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductCategory(
    typing.TypedDict, total=False
):
    categoryId: str
    level: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductChannel(
    typing.TypedDict, total=False
):
    channel: typing.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductCondition(
    typing.TypedDict, total=False
):
    condition: typing.Literal["UNSPECIFIED", "UNKNOWN", "NEW", "REFURBISHED", "USED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductCustomAttribute(
    typing.TypedDict, total=False
):
    index: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INDEX0", "INDEX1", "INDEX2", "INDEX3", "INDEX4"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductItemId(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductType(
    typing.TypedDict, total=False
):
    level: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_Webpage(
    typing.TypedDict, total=False
):
    conditions: _list[
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_WebpageCondition
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_WebpageCondition(
    typing.TypedDict, total=False
):
    customLabel: str
    urlContains: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ProductCategoryConstant_ProductCategoryLocalization(
    typing.TypedDict, total=False
):
    languageCode: str
    regionCode: str
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_RecommendationCampaignBudgetRecommendation_CampaignBudgetRecommendationOption(
    typing.TypedDict, total=False
):
    budgetAmountMicros: str
    impact: GoogleAdsSearchads360V23Resources_Recommendation_RecommendationImpact

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_RecommendationKeywordRecommendation_SearchTerm(
    typing.TypedDict, total=False
):
    estimatedWeeklySearchCount: str
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_RecommendationTargetCpaOptInRecommendation_TargetCpaOptInRecommendationOption(
    typing.TypedDict, total=False
):
    goal: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SAME_COST",
        "SAME_CONVERSIONS",
        "SAME_CPA",
        "CLOSEST_CPA",
    ]
    impact: GoogleAdsSearchads360V23Resources_Recommendation_RecommendationImpact
    requiredCampaignBudgetAmountMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_AccountInfo(
    typing.TypedDict, total=False
):
    customerId: str
    descriptiveName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_CallAssetRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_CalloutAssetRecommendation(
    typing.TypedDict, total=False
):
    recommendedCampaignCalloutAssets: _list[GoogleAdsSearchads360V23Resources__Asset]
    recommendedCustomerCalloutAssets: _list[GoogleAdsSearchads360V23Resources__Asset]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudget(
    typing.TypedDict, total=False
):
    currentAmountMicros: str
    newStartDate: str
    recommendedNewAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudgetRecommendation(
    typing.TypedDict, total=False
):
    budgetOptions: _list[
        GoogleAdsSearchads360V23Resources_RecommendationCampaignBudgetRecommendation_CampaignBudgetRecommendationOption
    ]
    currentBudgetAmountMicros: str
    recommendedBudgetAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_CustomAudienceOptInRecommendation(
    typing.TypedDict, total=False
):
    keywords: _list[GoogleAdsSearchads360V23Common__KeywordInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_DisplayExpansionOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_DynamicImageExtensionOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_EnhancedCpcOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ForecastingSetTargetCpaRecommendation(
    typing.TypedDict, total=False
):
    campaignBudget: GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudget
    recommendedTargetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ForecastingSetTargetRoasRecommendation(
    typing.TypedDict, total=False
):
    campaignBudget: GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudget
    recommendedTargetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ImproveDemandGenAdStrengthRecommendation(
    typing.TypedDict, total=False
):
    ad: str
    adStrength: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "NO_ADS",
        "POOR",
        "AVERAGE",
        "GOOD",
        "EXCELLENT",
    ]
    demandGenAssetActionItems: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ImproveGoogleTagCoverageRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ImprovePerformanceMaxAdStrengthRecommendation(
    typing.TypedDict, total=False
):
    adStrength: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "NO_ADS",
        "POOR",
        "AVERAGE",
        "GOOD",
        "EXCELLENT",
    ]
    assetGroup: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_KeywordMatchTypeRecommendation(
    typing.TypedDict, total=False
):
    keyword: GoogleAdsSearchads360V23Common__KeywordInfo
    recommendedMatchType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_KeywordRecommendation(
    typing.TypedDict, total=False
):
    keyword: GoogleAdsSearchads360V23Common__KeywordInfo
    recommendedCpcBidMicros: str
    searchTerms: _list[
        GoogleAdsSearchads360V23Resources_RecommendationKeywordRecommendation_SearchTerm
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_LeadFormAssetRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_LowerTargetRoasRecommendation(
    typing.TypedDict, total=False
):
    targetAdjustment: (
        GoogleAdsSearchads360V23Resources_Recommendation_TargetAdjustmentInfo
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_MaximizeClicksOptInRecommendation(
    typing.TypedDict, total=False
):
    recommendedBudgetAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_MaximizeConversionValueOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_MaximizeConversionsOptInRecommendation(
    typing.TypedDict, total=False
):
    recommendedBudgetAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo(
    typing.TypedDict, total=False
):
    id: str
    multiClient: bool
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation(
    typing.TypedDict, total=False
):
    applyLink: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_MoveUnusedBudgetRecommendation(
    typing.TypedDict, total=False
):
    budgetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudgetRecommendation
    )
    excessCampaignBudget: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_OptimizeAdRotationRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_PerformanceMaxFinalUrlOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_PerformanceMaxOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_RaiseTargetCpaBidTooLowRecommendation(
    typing.TypedDict, total=False
):
    averageTargetCpaMicros: str
    recommendedTargetMultiplier: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_RaiseTargetCpaRecommendation(
    typing.TypedDict, total=False
):
    appBiddingGoal: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME",
        "OPTIMIZE_FOR_IN_APP_CONVERSION_VOLUME",
        "OPTIMIZE_FOR_TOTAL_CONVERSION_VALUE",
        "OPTIMIZE_FOR_TARGET_IN_APP_CONVERSION",
        "OPTIMIZE_FOR_RETURN_ON_ADVERTISING_SPEND",
        "OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME_WITHOUT_TARGET_CPI",
        "OPTIMIZE_FOR_PRE_REGISTRATION_CONVERSION_VOLUME",
    ]
    targetAdjustment: (
        GoogleAdsSearchads360V23Resources_Recommendation_TargetAdjustmentInfo
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_RecommendationImpact(
    typing.TypedDict, total=False
):
    baseMetrics: GoogleAdsSearchads360V23Resources_Recommendation_RecommendationMetrics
    potentialMetrics: (
        GoogleAdsSearchads360V23Resources_Recommendation_RecommendationMetrics
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_RecommendationMetrics(
    typing.TypedDict, total=False
):
    clicks: float
    conversions: float
    conversionsValue: float
    costMicros: str
    impressions: float
    videoViews: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_RefreshCustomerMatchListRecommendation(
    typing.TypedDict, total=False
):
    daysSinceLastRefresh: str
    ownerAccount: GoogleAdsSearchads360V23Resources_Recommendation_AccountInfo
    targetingAccountsCount: str
    topSpendingAccount: _list[
        GoogleAdsSearchads360V23Resources_Recommendation_AccountInfo
    ]
    userListId: str
    userListName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ResponsiveSearchAdAssetRecommendation(
    typing.TypedDict, total=False
):
    currentAd: GoogleAdsSearchads360V23Resources__Ad
    recommendedAssets: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ResponsiveSearchAdImproveAdStrengthRecommendation(
    typing.TypedDict, total=False
):
    currentAd: GoogleAdsSearchads360V23Resources__Ad
    recommendedAd: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ResponsiveSearchAdRecommendation(
    typing.TypedDict, total=False
):
    ad: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_SearchPartnersOptInRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ShoppingAddProductsToCampaignRecommendation(
    typing.TypedDict, total=False
):
    feedLabel: str
    merchant: GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo
    reason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS",
        "MERCHANT_CENTER_ACCOUNT_HAS_NO_SUBMITTED_PRODUCTS_IN_FEED",
        "ADS_ACCOUNT_EXCLUDES_OFFERS_FROM_CAMPAIGN",
        "ALL_PRODUCTS_ARE_EXCLUDED_FROM_CAMPAIGN",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ShoppingFixDisapprovedProductsRecommendation(
    typing.TypedDict, total=False
):
    disapprovedProductsCount: str
    feedLabel: str
    merchant: GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo
    productsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ShoppingMerchantCenterAccountSuspensionRecommendation(
    typing.TypedDict, total=False
):
    feedLabel: str
    merchant: GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation(
    typing.TypedDict, total=False
):
    feedLabel: str
    merchant: GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation(
    typing.TypedDict, total=False
):
    demotedOffersCount: str
    feedLabel: str
    merchant: GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo
    offersCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_ShoppingTargetAllOffersRecommendation(
    typing.TypedDict, total=False
):
    feedLabel: str
    merchant: GoogleAdsSearchads360V23Resources_Recommendation_MerchantInfo
    untargetedOffersCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_SitelinkAssetRecommendation(
    typing.TypedDict, total=False
):
    recommendedCampaignSitelinkAssets: _list[GoogleAdsSearchads360V23Resources__Asset]
    recommendedCustomerSitelinkAssets: _list[GoogleAdsSearchads360V23Resources__Asset]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_TargetAdjustmentInfo(
    typing.TypedDict, total=False
):
    currentAverageTargetMicros: str
    recommendedTargetMultiplier: float
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_TargetCpaOptInRecommendation(
    typing.TypedDict, total=False
):
    options: _list[
        GoogleAdsSearchads360V23Resources_RecommendationTargetCpaOptInRecommendation_TargetCpaOptInRecommendationOption
    ]
    recommendedTargetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_TargetRoasOptInRecommendation(
    typing.TypedDict, total=False
):
    recommendedTargetRoas: float
    requiredCampaignBudgetAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_TextAdRecommendation(
    typing.TypedDict, total=False
):
    ad: GoogleAdsSearchads360V23Resources__Ad
    autoApplyDate: str
    creationDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_UpgradeLocalCampaignToPerformanceMaxRecommendation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation(
    typing.TypedDict, total=False
):
    merchantId: str
    salesCountryCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_Recommendation_UseBroadMatchKeywordRecommendation(
    typing.TypedDict, total=False
):
    campaignKeywordsCount: str
    campaignUsesSharedBudget: bool
    keyword: _list[GoogleAdsSearchads360V23Common__KeywordInfo]
    requiredCampaignBudgetAmountMicros: str
    suggestedKeywordsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_ShoppingProduct_ProductIssue(
    typing.TypedDict, total=False
):
    adsSeverity: typing.Literal["UNSPECIFIED", "UNKNOWN", "WARNING", "ERROR"]
    affectedRegions: _list[str]
    attributeName: str
    description: str
    detail: str
    documentation: str
    errorCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_SmartCampaignSetting_AdOptimizedBusinessProfileSetting(
    typing.TypedDict, total=False
):
    includeLeadForm: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources_SmartCampaignSetting_PhoneNumber(
    typing.TypedDict, total=False
):
    countryCode: str
    phoneNumber: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AccessibleBiddingStrategy(
    typing.TypedDict, total=False
):
    id: str
    maximizeConversionValue: GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_MaximizeConversionValue
    maximizeConversions: (
        GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_MaximizeConversions
    )
    name: str
    ownerCustomerId: str
    ownerDescriptiveName: str
    resourceName: str
    targetCpa: GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetCpa
    targetImpressionShare: GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetImpressionShare
    targetRoas: GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetRoas
    targetSpend: GoogleAdsSearchads360V23Resources_AccessibleBiddingStrategy_TargetSpend
    type: typing.Literal[
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
        "TARGET_CPC",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AccountBudget(typing.TypedDict, total=False):
    adjustedSpendingLimitMicros: str
    adjustedSpendingLimitType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INFINITE"]
    amountServedMicros: str
    approvedEndDateTime: str
    approvedEndTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    approvedSpendingLimitMicros: str
    approvedSpendingLimitType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INFINITE"]
    approvedStartDateTime: str
    billingSetup: str
    id: str
    name: str
    notes: str
    pendingProposal: (
        GoogleAdsSearchads360V23Resources_AccountBudget_PendingAccountBudgetProposal
    )
    proposedEndDateTime: str
    proposedEndTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    proposedSpendingLimitMicros: str
    proposedSpendingLimitType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INFINITE"]
    proposedStartDateTime: str
    purchaseOrderNumber: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "PENDING", "APPROVED", "CANCELLED"]
    totalAdjustmentsMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AccountBudgetProposal(
    typing.TypedDict, total=False
):
    accountBudget: str
    approvalDateTime: str
    approvedEndDateTime: str
    approvedEndTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    approvedSpendingLimitMicros: str
    approvedSpendingLimitType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INFINITE"]
    approvedStartDateTime: str
    billingSetup: str
    creationDateTime: str
    id: str
    proposalType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CREATE", "UPDATE", "END", "REMOVE"
    ]
    proposedEndDateTime: str
    proposedEndTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    proposedName: str
    proposedNotes: str
    proposedPurchaseOrderNumber: str
    proposedSpendingLimitMicros: str
    proposedSpendingLimitType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INFINITE"]
    proposedStartDateTime: str
    proposedStartTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "APPROVED_HELD",
        "APPROVED",
        "CANCELLED",
        "REJECTED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AccountLink(typing.TypedDict, total=False):
    accountLinkId: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ENABLED",
        "REMOVED",
        "REQUESTED",
        "PENDING_APPROVAL",
        "REJECTED",
        "REVOKED",
    ]
    thirdPartyAppAnalytics: (
        GoogleAdsSearchads360V23Resources__ThirdPartyAppAnalyticsLinkIdentifier
    )
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "THIRD_PARTY_APP_ANALYTICS"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Ad(typing.TypedDict, total=False):
    addedByGoogleAds: bool
    appAd: GoogleAdsSearchads360V23Common__AppAdInfo
    appEngagementAd: GoogleAdsSearchads360V23Common__AppEngagementAdInfo
    appPreRegistrationAd: GoogleAdsSearchads360V23Common__AppPreRegistrationAdInfo
    demandGenCarouselAd: GoogleAdsSearchads360V23Common__DemandGenCarouselAdInfo
    demandGenMultiAssetAd: GoogleAdsSearchads360V23Common__DemandGenMultiAssetAdInfo
    demandGenProductAd: GoogleAdsSearchads360V23Common__DemandGenProductAdInfo
    demandGenVideoResponsiveAd: (
        GoogleAdsSearchads360V23Common__DemandGenVideoResponsiveAdInfo
    )
    devicePreference: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET", "DESKTOP", "CONNECTED_TV", "OTHER"
    ]
    displayUploadAd: GoogleAdsSearchads360V23Common__DisplayUploadAdInfo
    displayUrl: str
    expandedDynamicSearchAd: GoogleAdsSearchads360V23Common__ExpandedDynamicSearchAdInfo
    expandedTextAd: GoogleAdsSearchads360V23Common__ExpandedTextAdInfo
    finalAppUrls: _list[GoogleAdsSearchads360V23Common__FinalAppUrl]
    finalMobileUrls: _list[str]
    finalUrlSuffix: str
    finalUrls: _list[str]
    hotelAd: GoogleAdsSearchads360V23Common__HotelAdInfo
    id: str
    imageAd: GoogleAdsSearchads360V23Common__ImageAdInfo
    legacyAppInstallAd: GoogleAdsSearchads360V23Common__LegacyAppInstallAdInfo
    legacyResponsiveDisplayAd: (
        GoogleAdsSearchads360V23Common__LegacyResponsiveDisplayAdInfo
    )
    localAd: GoogleAdsSearchads360V23Common__LocalAdInfo
    name: str
    productAd: GoogleAdsSearchads360V23Common__SearchAds360ProductAdInfo
    resourceName: str
    responsiveDisplayAd: GoogleAdsSearchads360V23Common__ResponsiveDisplayAdInfo
    responsiveSearchAd: GoogleAdsSearchads360V23Common__ResponsiveSearchAdInfo
    searchAds360ExpandedDynamicSearchAd: (
        GoogleAdsSearchads360V23Common__SearchAds360ExpandedDynamicSearchAdInfo
    )
    searchAds360ExpandedTextAd: (
        GoogleAdsSearchads360V23Common__SearchAds360ExpandedTextAdInfo
    )
    searchAds360ResponsiveSearchAd: (
        GoogleAdsSearchads360V23Common__SearchAds360ResponsiveSearchAdInfo
    )
    searchAds360TextAd: GoogleAdsSearchads360V23Common__SearchAds360TextAdInfo
    shoppingComparisonListingAd: (
        GoogleAdsSearchads360V23Common__ShoppingComparisonListingAdInfo
    )
    shoppingProductAd: GoogleAdsSearchads360V23Common__ShoppingProductAdInfo
    shoppingSmartAd: GoogleAdsSearchads360V23Common__ShoppingSmartAdInfo
    smartCampaignAd: GoogleAdsSearchads360V23Common__SmartCampaignAdInfo
    syntheticContentInfo: GoogleAdsSearchads360V23Common__SyntheticContentInfo
    systemManagedResourceSource: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AD_VARIATIONS"
    ]
    textAd: GoogleAdsSearchads360V23Common__TextAdInfo
    trackingUrlTemplate: str
    travelAd: GoogleAdsSearchads360V23Common__TravelAdInfo
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TEXT_AD",
        "EXPANDED_TEXT_AD",
        "EXPANDED_DYNAMIC_SEARCH_AD",
        "HOTEL_AD",
        "SHOPPING_SMART_AD",
        "SHOPPING_PRODUCT_AD",
        "VIDEO_AD",
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
        "VIDEO_TRUEVIEW_IN_STREAM_AD",
        "VIDEO_RESPONSIVE_AD",
        "SMART_CAMPAIGN_AD",
        "CALL_AD",
        "APP_PRE_REGISTRATION_AD",
        "DEMAND_GEN_MULTI_ASSET_AD",
        "DEMAND_GEN_CAROUSEL_AD",
        "TRAVEL_AD",
        "DEMAND_GEN_VIDEO_RESPONSIVE_AD",
        "DEMAND_GEN_PRODUCT_AD",
        "MULTIMEDIA_AD",
    ]
    urlCollections: _list[GoogleAdsSearchads360V23Common__UrlCollection]
    urlCustomParameters: _list[GoogleAdsSearchads360V23Common__CustomParameter]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroup(typing.TypedDict, total=False):
    adRotationMode: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "OPTIMIZE", "ROTATE_FOREVER"
    ]
    aiMaxAdGroupSetting: GoogleAdsSearchads360V23Resources_AdGroup_AiMaxAdGroupSetting
    audienceSetting: GoogleAdsSearchads360V23Resources_AdGroup_AudienceSetting
    baseAdGroup: str
    campaign: str
    cpcBidMicros: str
    cpmBidMicros: str
    cpvBidMicros: str
    creationTime: str
    demandGenAdGroupSettings: (
        GoogleAdsSearchads360V23Resources_AdGroup_DemandGenAdGroupSettings
    )
    displayCustomBidDimension: typing.Literal[
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
    effectiveCpcBidMicros: str
    effectiveLabels: _list[str]
    effectiveTargetCpaMicros: str
    effectiveTargetCpaSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    effectiveTargetCpc: str
    effectiveTargetCpcSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    effectiveTargetRoas: float
    effectiveTargetRoasSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    endDate: str
    engineId: str
    engineStatus: typing.Literal[
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
    excludeDemographicExpansion: bool
    excludedParentAssetFieldTypes: _list[
        typing.Literal[
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
            "DEMAND_GEN_CAROUSEL_CARD",
            "BUSINESS_MESSAGE",
            "TALL_PORTRAIT_MARKETING_IMAGE",
            "LANDING_PAGE_PREVIEW",
            "LONG_DESCRIPTION",
            "CALL_TO_ACTION",
        ]
    ]
    excludedParentAssetSetTypes: _list[
        typing.Literal[
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
    fixedCpmMicros: str
    id: str
    labels: _list[str]
    languageCode: str
    lastModifiedTime: str
    name: str
    optimizedTargetingEnabled: bool
    percentCpcBidMicros: str
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "NOT_ELIGIBLE",
        "LIMITED",
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CAMPAIGN_REMOVED",
            "CAMPAIGN_PAUSED",
            "CAMPAIGN_PENDING",
            "CAMPAIGN_ENDED",
            "AD_GROUP_PAUSED",
            "AD_GROUP_REMOVED",
            "AD_GROUP_INCOMPLETE",
            "KEYWORDS_PAUSED",
            "NO_KEYWORDS",
            "AD_GROUP_ADS_PAUSED",
            "NO_AD_GROUP_ADS",
            "HAS_ADS_DISAPPROVED",
            "HAS_ADS_LIMITED_BY_POLICY",
            "MOST_ADS_UNDER_REVIEW",
            "CAMPAIGN_DRAFT",
            "AD_GROUP_PAUSED_DUE_TO_LOW_ACTIVITY",
        ]
    ]
    resourceName: str
    startDate: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"]
    targetCpaMicros: str
    targetCpcMicros: str
    targetCpmMicros: str
    targetCpvMicros: str
    targetRoas: float
    targetingSetting: GoogleAdsSearchads360V23Common__TargetingSetting
    trackingUrlTemplate: str
    type: typing.Literal[
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
        "SEARCH_DYNAMIC_ADS",
        "SHOPPING_COMPARISON_LISTING_ADS",
        "PROMOTED_HOTEL_ADS",
        "VIDEO_RESPONSIVE",
        "VIDEO_EFFICIENT_REACH",
        "SMART_CAMPAIGN_ADS",
        "TRAVEL_ADS",
    ]
    urlCustomParameters: _list[GoogleAdsSearchads360V23Common__CustomParameter]
    verticalAdsFormatSetting: (
        GoogleAdsSearchads360V23Resources_AdGroup_VerticalAdsFormatSetting
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAd(typing.TypedDict, total=False):
    actionItems: _list[str]
    ad: GoogleAdsSearchads360V23Resources__Ad
    adGroup: str
    adGroupAdAssetAutomationSettings: _list[
        GoogleAdsSearchads360V23Resources__AdGroupAdAssetAutomationSetting
    ]
    adStrength: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "NO_ADS",
        "POOR",
        "AVERAGE",
        "GOOD",
        "EXCELLENT",
    ]
    creationTime: str
    effectiveLabels: _list[str]
    engineId: str
    engineStatus: typing.Literal[
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
    policySummary: GoogleAdsSearchads360V23Resources__AdGroupAdPolicySummary
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "LIMITED",
        "NOT_ELIGIBLE",
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CAMPAIGN_REMOVED",
            "CAMPAIGN_PAUSED",
            "CAMPAIGN_PENDING",
            "CAMPAIGN_ENDED",
            "AD_GROUP_PAUSED",
            "AD_GROUP_REMOVED",
            "AD_GROUP_AD_PAUSED",
            "AD_GROUP_AD_REMOVED",
            "AD_GROUP_AD_DISAPPROVED",
            "AD_GROUP_AD_UNDER_REVIEW",
            "AD_GROUP_AD_POOR_QUALITY",
            "AD_GROUP_AD_NO_ADS",
            "AD_GROUP_AD_APPROVED_LABELED",
            "AD_GROUP_AD_AREA_OF_INTEREST_ONLY",
            "AD_GROUP_AD_UNDER_APPEAL",
        ]
    ]
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdAssetAutomationSetting(
    typing.TypedDict, total=False
):
    assetAutomationStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "OPTED_IN", "OPTED_OUT"
    ]
    assetAutomationType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TEXT_ASSET_AUTOMATION",
        "GENERATE_VERTICAL_YOUTUBE_VIDEOS",
        "GENERATE_SHORTER_YOUTUBE_VIDEOS",
        "GENERATE_LANDING_PAGE_PREVIEW",
        "GENERATE_LANDING_PAGE_TEXT",
        "GENERATE_ENHANCED_YOUTUBE_VIDEOS",
        "GENERATE_IMAGE_ENHANCEMENT",
        "GENERATE_IMAGE_EXTRACTION",
        "GENERATE_DESIGN_VERSIONS_FOR_IMAGES",
        "FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION",
        "GENERATE_VIDEOS_FROM_OTHER_ASSETS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdAssetCombinationView(
    typing.TypedDict, total=False
):
    enabled: bool
    resourceName: str
    servedAssets: _list[GoogleAdsSearchads360V23Common__AssetUsage]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdAssetPolicySummary(
    typing.TypedDict, total=False
):
    approvalStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISAPPROVED",
        "APPROVED_LIMITED",
        "APPROVED",
        "AREA_OF_INTEREST_ONLY",
    ]
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]
    reviewStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REVIEW_IN_PROGRESS",
        "REVIEWED",
        "UNDER_APPEAL",
        "ELIGIBLE_MAY_SERVE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdAssetView(
    typing.TypedDict, total=False
):
    adGroupAd: str
    asset: str
    enabled: bool
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    performanceLabel: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "LEARNING",
        "LOW",
        "GOOD",
        "BEST",
        "NOT_APPLICABLE",
    ]
    pinnedField: typing.Literal[
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
    policySummary: GoogleAdsSearchads360V23Resources__AdGroupAdAssetPolicySummary
    resourceName: str
    source: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdEffectiveLabel(
    typing.TypedDict, total=False
):
    adGroupAd: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdLabel(typing.TypedDict, total=False):
    adGroupAd: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAdPolicySummary(
    typing.TypedDict, total=False
):
    approvalStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISAPPROVED",
        "APPROVED_LIMITED",
        "APPROVED",
        "AREA_OF_INTEREST_ONLY",
    ]
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]
    reviewStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REVIEW_IN_PROGRESS",
        "REVIEWED",
        "UNDER_APPEAL",
        "ELIGIBLE_MAY_SERVE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAsset(typing.TypedDict, total=False):
    adGroup: str
    asset: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "LIMITED",
        "NOT_ELIGIBLE",
    ]
    primaryStatusDetails: _list[
        GoogleAdsSearchads360V23Common__AssetLinkPrimaryStatusDetails
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "ASSET_LINK_PAUSED",
            "ASSET_LINK_REMOVED",
            "ASSET_DISAPPROVED",
            "ASSET_UNDER_REVIEW",
            "ASSET_APPROVED_LABELED",
        ]
    ]
    resourceName: str
    source: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAssetSet(typing.TypedDict, total=False):
    adGroup: str
    assetSet: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupAudienceView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupBidModifier(
    typing.TypedDict, total=False
):
    adGroup: str
    baseAdGroup: str
    bidModifier: float
    bidModifierSource: typing.Literal["UNSPECIFIED", "UNKNOWN", "CAMPAIGN", "AD_GROUP"]
    criterionId: str
    device: GoogleAdsSearchads360V23Common__DeviceInfo
    hotelAdvanceBookingWindow: (
        GoogleAdsSearchads360V23Common__HotelAdvanceBookingWindowInfo
    )
    hotelCheckInDateRange: GoogleAdsSearchads360V23Common__HotelCheckInDateRangeInfo
    hotelCheckInDay: GoogleAdsSearchads360V23Common__HotelCheckInDayInfo
    hotelDateSelectionType: GoogleAdsSearchads360V23Common__HotelDateSelectionTypeInfo
    hotelLengthOfStay: GoogleAdsSearchads360V23Common__HotelLengthOfStayInfo
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupCriterion(
    typing.TypedDict, total=False
):
    adGroup: str
    ageRange: GoogleAdsSearchads360V23Common__AgeRangeInfo
    appPaymentModel: GoogleAdsSearchads360V23Common__AppPaymentModelInfo
    approvalStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "APPROVED",
        "DISAPPROVED",
        "PENDING_REVIEW",
        "UNDER_REVIEW",
    ]
    audience: GoogleAdsSearchads360V23Common__AudienceInfo
    bidModifier: float
    brandList: GoogleAdsSearchads360V23Common__BrandListInfo
    combinedAudience: GoogleAdsSearchads360V23Common__CombinedAudienceInfo
    cpcBidMicros: str
    cpmBidMicros: str
    cpvBidMicros: str
    creationTime: str
    criterionId: str
    customAffinity: GoogleAdsSearchads360V23Common__CustomAffinityInfo
    customAudience: GoogleAdsSearchads360V23Common__CustomAudienceInfo
    customIntent: GoogleAdsSearchads360V23Common__CustomIntentInfo
    disapprovalReasons: _list[str]
    displayName: str
    effectiveCpcBidMicros: str
    effectiveCpcBidSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    effectiveCpmBidMicros: str
    effectiveCpmBidSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    effectiveCpvBidMicros: str
    effectiveCpvBidSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    effectiveLabels: _list[str]
    effectivePercentCpcBidMicros: str
    effectivePercentCpcBidSource: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BIDDING_STRATEGY",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
    ]
    engineId: str
    engineStatus: typing.Literal[
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
    extendedDemographic: GoogleAdsSearchads360V23Common__ExtendedDemographicInfo
    finalMobileUrls: _list[str]
    finalUrlSuffix: str
    finalUrls: _list[str]
    gender: GoogleAdsSearchads360V23Common__GenderInfo
    incomeRange: GoogleAdsSearchads360V23Common__IncomeRangeInfo
    keyword: GoogleAdsSearchads360V23Common__KeywordInfo
    labels: _list[str]
    language: GoogleAdsSearchads360V23Common__LanguageInfo
    lastModifiedTime: str
    lifeEvent: GoogleAdsSearchads360V23Common__LifeEventInfo
    listingGroup: GoogleAdsSearchads360V23Common__ListingGroupInfo
    location: GoogleAdsSearchads360V23Common__LocationInfo
    mobileAppCategory: GoogleAdsSearchads360V23Common__MobileAppCategoryInfo
    mobileApplication: GoogleAdsSearchads360V23Common__MobileApplicationInfo
    negative: bool
    parentalStatus: GoogleAdsSearchads360V23Common__ParentalStatusInfo
    percentCpcBidMicros: str
    placement: GoogleAdsSearchads360V23Common__PlacementInfo
    positionEstimates: (
        GoogleAdsSearchads360V23Resources_AdGroupCriterion_PositionEstimates
    )
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "NOT_ELIGIBLE",
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CAMPAIGN_PENDING",
            "CAMPAIGN_CRITERION_NEGATIVE",
            "CAMPAIGN_PAUSED",
            "CAMPAIGN_REMOVED",
            "CAMPAIGN_ENDED",
            "AD_GROUP_PAUSED",
            "AD_GROUP_REMOVED",
            "AD_GROUP_CRITERION_DISAPPROVED",
            "AD_GROUP_CRITERION_RARELY_SERVED",
            "AD_GROUP_CRITERION_LOW_QUALITY",
            "AD_GROUP_CRITERION_UNDER_REVIEW",
            "AD_GROUP_CRITERION_PENDING_REVIEW",
            "AD_GROUP_CRITERION_BELOW_FIRST_PAGE_BID",
            "AD_GROUP_CRITERION_NEGATIVE",
            "AD_GROUP_CRITERION_RESTRICTED",
            "AD_GROUP_CRITERION_PAUSED",
            "AD_GROUP_CRITERION_PAUSED_DUE_TO_LOW_ACTIVITY",
            "AD_GROUP_CRITERION_REMOVED",
        ]
    ]
    qualityInfo: GoogleAdsSearchads360V23Resources_AdGroupCriterion_QualityInfo
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"]
    systemServingStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ELIGIBLE", "RARELY_SERVED"
    ]
    topic: GoogleAdsSearchads360V23Common__TopicInfo
    trackingUrlTemplate: str
    type: typing.Literal[
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
        "NEGATIVE_KEYWORD_LIST",
        "LOCAL_SERVICE_ID",
        "SEARCH_THEME",
        "BRAND",
        "BRAND_LIST",
        "LIFE_EVENT",
        "WEBPAGE_LIST",
        "VIDEO_LINEUP",
        "PLACEMENT_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE",
    ]
    urlCustomParameters: _list[GoogleAdsSearchads360V23Common__CustomParameter]
    userInterest: GoogleAdsSearchads360V23Common__UserInterestInfo
    userList: GoogleAdsSearchads360V23Common__UserListInfo
    verticalAdsItemGroupRuleList: (
        GoogleAdsSearchads360V23Common__VerticalAdsItemGroupRuleListInfo
    )
    videoLineup: GoogleAdsSearchads360V23Common__VideoLineupInfo
    webpage: GoogleAdsSearchads360V23Common__WebpageInfo
    youtubeChannel: GoogleAdsSearchads360V23Common__YouTubeChannelInfo
    youtubeVideo: GoogleAdsSearchads360V23Common__YouTubeVideoInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupCriterionCustomizer(
    typing.TypedDict, total=False
):
    adGroupCriterion: str
    customizerAttribute: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    value: GoogleAdsSearchads360V23Common__CustomizerValue

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupCriterionEffectiveLabel(
    typing.TypedDict, total=False
):
    adGroupCriterion: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupCriterionLabel(
    typing.TypedDict, total=False
):
    adGroupCriterion: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupCriterionSimulation(
    typing.TypedDict, total=False
):
    adGroupId: str
    cpcBidPointList: GoogleAdsSearchads360V23Common__CpcBidSimulationPointList
    criterionId: str
    endDate: str
    modificationMethod: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "UNIFORM", "DEFAULT", "SCALING"
    ]
    percentCpcBidPointList: (
        GoogleAdsSearchads360V23Common__PercentCpcBidSimulationPointList
    )
    resourceName: str
    startDate: str
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CPC_BID",
        "CPV_BID",
        "TARGET_CPA",
        "BID_MODIFIER",
        "TARGET_ROAS",
        "PERCENT_CPC_BID",
        "TARGET_IMPRESSION_SHARE",
        "BUDGET",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupCustomizer(
    typing.TypedDict, total=False
):
    adGroup: str
    customizerAttribute: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    value: GoogleAdsSearchads360V23Common__CustomizerValue

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupEffectiveLabel(
    typing.TypedDict, total=False
):
    adGroup: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupLabel(typing.TypedDict, total=False):
    adGroup: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdGroupSimulation(
    typing.TypedDict, total=False
):
    adGroupId: str
    cpcBidPointList: GoogleAdsSearchads360V23Common__CpcBidSimulationPointList
    cpvBidPointList: GoogleAdsSearchads360V23Common__CpvBidSimulationPointList
    endDate: str
    modificationMethod: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "UNIFORM", "DEFAULT", "SCALING"
    ]
    resourceName: str
    startDate: str
    targetCpaPointList: GoogleAdsSearchads360V23Common__TargetCpaSimulationPointList
    targetRoasPointList: GoogleAdsSearchads360V23Common__TargetRoasSimulationPointList
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CPC_BID",
        "CPV_BID",
        "TARGET_CPA",
        "BID_MODIFIER",
        "TARGET_ROAS",
        "PERCENT_CPC_BID",
        "TARGET_IMPRESSION_SHARE",
        "BUDGET",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdParameter(typing.TypedDict, total=False):
    adGroupCriterion: str
    insertionText: str
    parameterIndex: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdScheduleView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdStrengthActionItem(
    typing.TypedDict, total=False
):
    actionItemType: typing.Literal["UNSPECIFIED", "UNKNOWN", "ADD_ASSET"]
    addAssetDetails: (
        GoogleAdsSearchads360V23Resources_AdStrengthActionItem_AddAssetDetails
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdvertisingPartnerIdentifier(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AdvertisingPartnerLinkInvitationIdentifier(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AgeRangeView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AiMaxSearchTermAdCombinationView(
    typing.TypedDict, total=False
):
    adGroup: str
    headline: str
    landingPage: str
    resourceName: str
    searchTerm: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AndroidPrivacySharedKeyGoogleAdGroup(
    typing.TypedDict, total=False
):
    adGroupId: str
    androidPrivacyInteractionDate: str
    androidPrivacyInteractionType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CLICK", "ENGAGED_VIEW", "VIEW"
    ]
    androidPrivacyNetworkType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SEARCH", "DISPLAY", "YOUTUBE"
    ]
    campaignId: str
    resourceName: str
    sharedAdGroupKey: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AndroidPrivacySharedKeyGoogleCampaign(
    typing.TypedDict, total=False
):
    androidPrivacyInteractionDate: str
    androidPrivacyInteractionType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CLICK", "ENGAGED_VIEW", "VIEW"
    ]
    campaignId: str
    resourceName: str
    sharedCampaignKey: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AndroidPrivacySharedKeyGoogleNetworkType(
    typing.TypedDict, total=False
):
    androidPrivacyInteractionDate: str
    androidPrivacyInteractionType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CLICK", "ENGAGED_VIEW", "VIEW"
    ]
    androidPrivacyNetworkType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SEARCH", "DISPLAY", "YOUTUBE"
    ]
    campaignId: str
    resourceName: str
    sharedNetworkTypeKey: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Asset(typing.TypedDict, total=False):
    appDeepLinkAsset: GoogleAdsSearchads360V23Common__AppDeepLinkAsset
    bookOnGoogleAsset: GoogleAdsSearchads360V23Common__BookOnGoogleAsset
    businessMessageAsset: GoogleAdsSearchads360V23Common__BusinessMessageAsset
    callAsset: GoogleAdsSearchads360V23Common__CallAsset
    callToActionAsset: GoogleAdsSearchads360V23Common__CallToActionAsset
    calloutAsset: GoogleAdsSearchads360V23Common__CalloutAsset
    creationTime: str
    demandGenCarouselCardAsset: (
        GoogleAdsSearchads360V23Common__DemandGenCarouselCardAsset
    )
    dynamicCustomAsset: GoogleAdsSearchads360V23Common__DynamicCustomAsset
    dynamicEducationAsset: GoogleAdsSearchads360V23Common__DynamicEducationAsset
    dynamicFlightsAsset: GoogleAdsSearchads360V23Common__DynamicFlightsAsset
    dynamicHotelsAndRentalsAsset: (
        GoogleAdsSearchads360V23Common__DynamicHotelsAndRentalsAsset
    )
    dynamicJobsAsset: GoogleAdsSearchads360V23Common__DynamicJobsAsset
    dynamicLocalAsset: GoogleAdsSearchads360V23Common__DynamicLocalAsset
    dynamicRealEstateAsset: GoogleAdsSearchads360V23Common__DynamicRealEstateAsset
    dynamicTravelAsset: GoogleAdsSearchads360V23Common__DynamicTravelAsset
    engineStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SERVING",
        "SERVING_LIMITED",
        "DISAPPROVED",
        "DISABLED",
        "REMOVED",
    ]
    fieldTypePolicySummaries: _list[
        GoogleAdsSearchads360V23Resources__AssetFieldTypePolicySummary
    ]
    finalMobileUrls: _list[str]
    finalUrlSuffix: str
    finalUrls: _list[str]
    hotelCalloutAsset: GoogleAdsSearchads360V23Common__HotelCalloutAsset
    hotelPropertyAsset: GoogleAdsSearchads360V23Common__HotelPropertyAsset
    id: str
    imageAsset: GoogleAdsSearchads360V23Common__ImageAsset
    lastModifiedTime: str
    leadFormAsset: GoogleAdsSearchads360V23Common__LeadFormAsset
    locationAsset: GoogleAdsSearchads360V23Common__LocationAsset
    mediaBundleAsset: GoogleAdsSearchads360V23Common__MediaBundleAsset
    mobileAppAsset: GoogleAdsSearchads360V23Common__MobileAppAsset
    name: str
    orientation: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LANDSCAPE", "PORTRAIT", "SQUARE"
    ]
    pageFeedAsset: GoogleAdsSearchads360V23Common__PageFeedAsset
    policySummary: GoogleAdsSearchads360V23Resources__AssetPolicySummary
    priceAsset: GoogleAdsSearchads360V23Common__PriceAsset
    promotionAsset: GoogleAdsSearchads360V23Common__PromotionAsset
    resourceName: str
    searchAds360CallAsset: GoogleAdsSearchads360V23Common__UnifiedCallAsset
    searchAds360CalloutAsset: GoogleAdsSearchads360V23Common__UnifiedCalloutAsset
    searchAds360LocationAsset: GoogleAdsSearchads360V23Common__UnifiedLocationAsset
    searchAds360PageFeedAsset: GoogleAdsSearchads360V23Common__UnifiedPageFeedAsset
    searchAds360SitelinkAsset: GoogleAdsSearchads360V23Common__UnifiedSitelinkAsset
    sitelinkAsset: GoogleAdsSearchads360V23Common__SitelinkAsset
    source: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ENABLED",
        "REMOVED",
        "ARCHIVED",
        "PENDING_SYSTEM_GENERATED",
    ]
    structuredSnippetAsset: GoogleAdsSearchads360V23Common__StructuredSnippetAsset
    syntheticContentInfo: GoogleAdsSearchads360V23Common__SyntheticContentInfo
    textAsset: GoogleAdsSearchads360V23Common__TextAsset
    trackingUrlTemplate: str
    type: typing.Literal[
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
        "DYNAMIC_TRAVEL",
        "DYNAMIC_LOCAL",
        "DYNAMIC_JOBS",
        "LOCATION",
        "HOTEL_PROPERTY",
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "APP_DEEP_LINK",
    ]
    urlCustomParameters: _list[GoogleAdsSearchads360V23Common__CustomParameter]
    youtubeVideoAsset: GoogleAdsSearchads360V23Common__YoutubeVideoAsset

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetCoverage(typing.TypedDict, total=False):
    adStrengthActionItems: _list[
        GoogleAdsSearchads360V23Resources__AdStrengthActionItem
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetFieldTypePolicySummary(
    typing.TypedDict, total=False
):
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    assetSource: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]
    policySummaryInfo: GoogleAdsSearchads360V23Resources__AssetPolicySummary

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetFieldTypeView(
    typing.TypedDict, total=False
):
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroup(typing.TypedDict, total=False):
    adStrength: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING",
        "NO_ADS",
        "POOR",
        "AVERAGE",
        "GOOD",
        "EXCELLENT",
    ]
    assetCoverage: GoogleAdsSearchads360V23Resources__AssetCoverage
    campaign: str
    finalMobileUrls: _list[str]
    finalUrls: _list[str]
    id: str
    name: str
    path1: str
    path2: str
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "NOT_ELIGIBLE",
        "LIMITED",
        "PENDING",
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "ASSET_GROUP_PAUSED",
            "ASSET_GROUP_REMOVED",
            "CAMPAIGN_REMOVED",
            "CAMPAIGN_PAUSED",
            "CAMPAIGN_PENDING",
            "CAMPAIGN_ENDED",
            "ASSET_GROUP_LIMITED",
            "ASSET_GROUP_DISAPPROVED",
            "ASSET_GROUP_UNDER_REVIEW",
        ]
    ]
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroupAsset(typing.TypedDict, total=False):
    asset: str
    assetGroup: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    policySummary: GoogleAdsSearchads360V23Common__PolicySummary
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "LIMITED",
        "NOT_ELIGIBLE",
    ]
    primaryStatusDetails: _list[
        GoogleAdsSearchads360V23Common__AssetLinkPrimaryStatusDetails
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "ASSET_LINK_PAUSED",
            "ASSET_LINK_REMOVED",
            "ASSET_DISAPPROVED",
            "ASSET_UNDER_REVIEW",
            "ASSET_APPROVED_LABELED",
        ]
    ]
    resourceName: str
    source: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroupAssetCombinationData(
    typing.TypedDict, total=False
):
    assetCombinationServedAssets: _list[GoogleAdsSearchads360V23Common__AssetUsage]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroupListingGroupFilter(
    typing.TypedDict, total=False
):
    assetGroup: str
    caseValue: GoogleAdsSearchads360V23Resources__ListingGroupFilterDimension
    id: str
    listingSource: typing.Literal["UNSPECIFIED", "UNKNOWN", "SHOPPING", "WEBPAGE"]
    parentListingGroupFilter: str
    path: GoogleAdsSearchads360V23Resources__ListingGroupFilterDimensionPath
    resourceName: str
    type: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SUBDIVISION", "UNIT_INCLUDED", "UNIT_EXCLUDED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroupProductGroupView(
    typing.TypedDict, total=False
):
    assetGroup: str
    assetGroupListingGroupFilter: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroupSignal(
    typing.TypedDict, total=False
):
    approvalStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "APPROVED", "LIMITED", "DISAPPROVED", "UNDER_REVIEW"
    ]
    assetGroup: str
    audience: GoogleAdsSearchads360V23Common__AudienceInfo
    disapprovalReasons: _list[str]
    resourceName: str
    searchTheme: GoogleAdsSearchads360V23Common__SearchThemeInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetGroupTopCombinationView(
    typing.TypedDict, total=False
):
    assetGroupTopCombinations: _list[
        GoogleAdsSearchads360V23Resources__AssetGroupAssetCombinationData
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetPolicySummary(
    typing.TypedDict, total=False
):
    approvalStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISAPPROVED",
        "APPROVED_LIMITED",
        "APPROVED",
        "AREA_OF_INTEREST_ONLY",
    ]
    policyTopicEntries: _list[GoogleAdsSearchads360V23Common__PolicyTopicEntry]
    reviewStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REVIEW_IN_PROGRESS",
        "REVIEWED",
        "UNDER_APPEAL",
        "ELIGIBLE_MAY_SERVE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetSet(typing.TypedDict, total=False):
    businessProfileLocationGroup: (
        GoogleAdsSearchads360V23Common__BusinessProfileLocationGroup
    )
    chainLocationGroup: GoogleAdsSearchads360V23Common__ChainLocationGroup
    hotelPropertyData: GoogleAdsSearchads360V23Resources_AssetSet_HotelPropertyData
    id: str
    locationGroupParentAssetSetId: str
    locationSet: GoogleAdsSearchads360V23Common__LocationSet
    merchantCenterFeed: GoogleAdsSearchads360V23Resources_AssetSet_MerchantCenterFeed
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    type: typing.Literal[
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

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetSetAsset(typing.TypedDict, total=False):
    asset: str
    assetSet: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__AssetSetTypeView(
    typing.TypedDict, total=False
):
    assetSetType: typing.Literal[
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
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Audience(typing.TypedDict, total=False):
    assetGroup: str
    description: str
    dimensions: _list[GoogleAdsSearchads360V23Common__AudienceDimension]
    exclusionDimension: GoogleAdsSearchads360V23Common__AudienceExclusionDimension
    id: str
    name: str
    resourceName: str
    scope: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER", "ASSET_GROUP"]
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BackgroundCheckVerificationArtifact(
    typing.TypedDict, total=False
):
    caseUrl: str
    finalAdjudicationDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BatchJob(typing.TypedDict, total=False):
    id: str
    longRunningOperation: str
    metadata: GoogleAdsSearchads360V23Resources_BatchJob_BatchJobMetadata
    nextAddSequenceToken: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "PENDING", "RUNNING", "DONE"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BiddingDataExclusion(
    typing.TypedDict, total=False
):
    advertisingChannelTypes: _list[
        typing.Literal[
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
            "TRAVEL",
            "DEMAND_GEN",
            "SOCIAL",
        ]
    ]
    campaigns: _list[str]
    dataExclusionId: str
    description: str
    devices: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "MOBILE",
            "TABLET",
            "DESKTOP",
            "CONNECTED_TV",
            "OTHER",
        ]
    ]
    endDateTime: str
    name: str
    resourceName: str
    scope: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER", "CAMPAIGN", "CHANNEL"]
    startDateTime: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BiddingSeasonalityAdjustment(
    typing.TypedDict, total=False
):
    advertisingChannelTypes: _list[
        typing.Literal[
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
            "TRAVEL",
            "DEMAND_GEN",
            "SOCIAL",
        ]
    ]
    campaigns: _list[str]
    conversionRateModifier: float
    description: str
    devices: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "MOBILE",
            "TABLET",
            "DESKTOP",
            "CONNECTED_TV",
            "OTHER",
        ]
    ]
    endDateTime: str
    name: str
    resourceName: str
    scope: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER", "CAMPAIGN", "CHANNEL"]
    seasonalityAdjustmentId: str
    startDateTime: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BiddingStrategy(typing.TypedDict, total=False):
    alignedCampaignBudgetId: str
    campaignCount: str
    currencyCode: str
    effectiveCurrencyCode: str
    enhancedCpc: GoogleAdsSearchads360V23Common__EnhancedCpc
    id: str
    maximizeConversionValue: GoogleAdsSearchads360V23Common__MaximizeConversionValue
    maximizeConversions: GoogleAdsSearchads360V23Common__MaximizeConversions
    name: str
    nonRemovedCampaignCount: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    targetCpa: GoogleAdsSearchads360V23Common__TargetCpa
    targetImpressionShare: GoogleAdsSearchads360V23Common__TargetImpressionShare
    targetRoas: GoogleAdsSearchads360V23Common__TargetRoas
    targetSpend: GoogleAdsSearchads360V23Common__TargetSpend
    type: typing.Literal[
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
        "TARGET_CPC",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BiddingStrategySimulation(
    typing.TypedDict, total=False
):
    biddingStrategyId: str
    endDate: str
    modificationMethod: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "UNIFORM", "DEFAULT", "SCALING"
    ]
    resourceName: str
    startDate: str
    targetCpaPointList: GoogleAdsSearchads360V23Common__TargetCpaSimulationPointList
    targetRoasPointList: GoogleAdsSearchads360V23Common__TargetRoasSimulationPointList
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CPC_BID",
        "CPV_BID",
        "TARGET_CPA",
        "BID_MODIFIER",
        "TARGET_ROAS",
        "PERCENT_CPC_BID",
        "TARGET_IMPRESSION_SHARE",
        "BUDGET",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BillingSetup(typing.TypedDict, total=False):
    endDateTime: str
    endTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    id: str
    paymentsAccount: str
    paymentsAccountInfo: (
        GoogleAdsSearchads360V23Resources_BillingSetup_PaymentsAccountInfo
    )
    resourceName: str
    startDateTime: str
    startTimeType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NOW", "FOREVER"]
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PENDING", "APPROVED_HELD", "APPROVED", "CANCELLED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BusinessRegistrationCheckVerificationArtifact(
    typing.TypedDict, total=False
):
    checkId: str
    registrationDocument: (
        GoogleAdsSearchads360V23Resources__BusinessRegistrationDocument
    )
    registrationNumber: GoogleAdsSearchads360V23Resources__BusinessRegistrationNumber
    registrationType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NUMBER", "DOCUMENT"]
    rejectionReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BUSINESS_NAME_MISMATCH",
        "BUSINESS_DETAILS_MISMATCH",
        "ID_NOT_FOUND",
        "POOR_DOCUMENT_IMAGE_QUALITY",
        "DOCUMENT_EXPIRED",
        "DOCUMENT_INVALID",
        "DOCUMENT_TYPE_MISMATCH",
        "DOCUMENT_UNVERIFIABLE",
        "OTHER",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BusinessRegistrationDocument(
    typing.TypedDict, total=False
):
    documentReadonly: GoogleAdsSearchads360V23Common__LocalServicesDocumentReadOnly

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__BusinessRegistrationNumber(
    typing.TypedDict, total=False
):
    number: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CallReportingSetting(
    typing.TypedDict, total=False
):
    callConversionAction: str
    callConversionReportingEnabled: bool
    callReportingEnabled: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CallView(typing.TypedDict, total=False):
    callDurationSeconds: str
    callStatus: typing.Literal["UNSPECIFIED", "UNKNOWN", "MISSED", "RECEIVED"]
    callTrackingDisplayLocation: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AD", "LANDING_PAGE"
    ]
    callerAreaCode: str
    callerCountryCode: str
    endCallDateTime: str
    resourceName: str
    startCallDateTime: str
    type: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MANUALLY_DIALED", "HIGH_END_MOBILE_SEARCH"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Campaign(typing.TypedDict, total=False):
    accessibleBiddingStrategy: str
    adServingOptimizationStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OPTIMIZE",
        "CONVERSION_OPTIMIZE",
        "ROTATE",
        "ROTATE_INDEFINITELY",
        "UNAVAILABLE",
    ]
    advertisingChannelSubType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SEARCH_MOBILE_APP",
        "DISPLAY_MOBILE_APP",
        "SEARCH_EXPRESS",
        "DISPLAY_EXPRESS",
        "SHOPPING_SMART_ADS",
        "DISPLAY_GMAIL_AD",
        "DISPLAY_SMART_CAMPAIGN",
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
    advertisingChannelType: typing.Literal[
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
        "TRAVEL",
        "DEMAND_GEN",
        "SOCIAL",
    ]
    aiMaxSetting: GoogleAdsSearchads360V23Resources_Campaign_AiMaxSetting
    appCampaignSetting: GoogleAdsSearchads360V23Resources_Campaign_AppCampaignSetting
    assetAutomationSettings: _list[
        GoogleAdsSearchads360V23Resources_Campaign_AssetAutomationSetting
    ]
    audienceSetting: GoogleAdsSearchads360V23Resources_Campaign_AudienceSetting
    baseCampaign: str
    biddingStrategy: str
    biddingStrategySystemStatus: typing.Literal[
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
    biddingStrategyType: typing.Literal[
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
        "TARGET_CPC",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]
    brandGuidelines: GoogleAdsSearchads360V23Resources_Campaign_BrandGuidelines
    brandGuidelinesEnabled: bool
    campaignBudget: str
    campaignGroup: str
    commission: GoogleAdsSearchads360V23Common__Commission
    containsEuPoliticalAdvertising: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONTAINS_EU_POLITICAL_ADVERTISING",
        "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    ]
    demandGenCampaignSettings: (
        GoogleAdsSearchads360V23Resources_Campaign_DemandGenCampaignSettings
    )
    dynamicSearchAdsSetting: (
        GoogleAdsSearchads360V23Resources_Campaign_DynamicSearchAdsSetting
    )
    effectiveLabels: _list[str]
    endDateTime: str
    engineId: str
    excludedParentAssetFieldTypes: _list[
        typing.Literal[
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
            "DEMAND_GEN_CAROUSEL_CARD",
            "BUSINESS_MESSAGE",
            "TALL_PORTRAIT_MARKETING_IMAGE",
            "LANDING_PAGE_PREVIEW",
            "LONG_DESCRIPTION",
            "CALL_TO_ACTION",
        ]
    ]
    excludedParentAssetSetTypes: _list[
        typing.Literal[
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
    experimentType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "BASE", "DRAFT", "EXPERIMENT"
    ]
    feedTypes: _list[
        typing.Literal[
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
    frequencyCaps: _list[GoogleAdsSearchads360V23Common__FrequencyCapEntry]
    geoTargetTypeSetting: (
        GoogleAdsSearchads360V23Resources_Campaign_GeoTargetTypeSetting
    )
    hotelPropertyAssetSet: str
    hotelSetting: GoogleAdsSearchads360V23Resources_Campaign_HotelSettingInfo
    id: str
    keywordMatchType: typing.Literal["UNSPECIFIED", "UNKNOWN", "BROAD"]
    labels: _list[str]
    lastModifiedTime: str
    listingType: typing.Literal["UNSPECIFIED", "UNKNOWN", "VEHICLES"]
    localCampaignSetting: (
        GoogleAdsSearchads360V23Resources_Campaign_LocalCampaignSetting
    )
    localServicesCampaignSettings: (
        GoogleAdsSearchads360V23Resources_Campaign_LocalServicesCampaignSettings
    )
    manualCpa: GoogleAdsSearchads360V23Common__ManualCpa
    manualCpc: GoogleAdsSearchads360V23Common__ManualCpc
    manualCpm: GoogleAdsSearchads360V23Common__ManualCpm
    manualCpv: GoogleAdsSearchads360V23Common__ManualCpv
    maximizeConversionValue: GoogleAdsSearchads360V23Common__MaximizeConversionValue
    maximizeConversions: GoogleAdsSearchads360V23Common__MaximizeConversions
    missingEuPoliticalAdvertisingDeclaration: bool
    name: str
    networkSettings: GoogleAdsSearchads360V23Resources_Campaign_NetworkSettings
    optimizationGoalSetting: (
        GoogleAdsSearchads360V23Resources_Campaign_OptimizationGoalSetting
    )
    optimizationScore: float
    paymentMode: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CLICKS",
        "CONVERSION_VALUE",
        "CONVERSIONS",
        "GUEST_STAY",
    ]
    percentCpc: GoogleAdsSearchads360V23Common__PercentCpc
    performanceMaxUpgrade: (
        GoogleAdsSearchads360V23Resources_Campaign_PerformanceMaxUpgrade
    )
    pmaxCampaignSettings: (
        GoogleAdsSearchads360V23Resources_Campaign_PmaxCampaignSettings
    )
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "ENDED",
        "PENDING",
        "MISCONFIGURED",
        "LIMITED",
        "LEARNING",
        "NOT_ELIGIBLE",
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CAMPAIGN_REMOVED",
            "CAMPAIGN_PAUSED",
            "CAMPAIGN_PENDING",
            "CAMPAIGN_ENDED",
            "CAMPAIGN_DRAFT",
            "BIDDING_STRATEGY_MISCONFIGURED",
            "BIDDING_STRATEGY_LIMITED",
            "BIDDING_STRATEGY_LEARNING",
            "BIDDING_STRATEGY_CONSTRAINED",
            "BUDGET_CONSTRAINED",
            "BUDGET_MISCONFIGURED",
            "SEARCH_VOLUME_LIMITED",
            "AD_GROUPS_PAUSED",
            "NO_AD_GROUPS",
            "KEYWORDS_PAUSED",
            "NO_KEYWORDS",
            "AD_GROUP_ADS_PAUSED",
            "NO_AD_GROUP_ADS",
            "HAS_ADS_LIMITED_BY_POLICY",
            "HAS_ADS_DISAPPROVED",
            "MOST_ADS_UNDER_REVIEW",
            "MISSING_LEAD_FORM_EXTENSION",
            "MISSING_CALL_EXTENSION",
            "LEAD_FORM_EXTENSION_UNDER_REVIEW",
            "LEAD_FORM_EXTENSION_DISAPPROVED",
            "CALL_EXTENSION_UNDER_REVIEW",
            "CALL_EXTENSION_DISAPPROVED",
            "NO_MOBILE_APPLICATION_AD_GROUP_CRITERIA",
            "CAMPAIGN_GROUP_PAUSED",
            "CAMPAIGN_GROUP_ALL_GROUP_BUDGETS_ENDED",
            "APP_NOT_RELEASED",
            "APP_PARTIALLY_RELEASED",
            "HAS_ASSET_GROUPS_DISAPPROVED",
            "HAS_ASSET_GROUPS_LIMITED_BY_POLICY",
            "MOST_ASSET_GROUPS_UNDER_REVIEW",
            "NO_ASSET_GROUPS",
            "ASSET_GROUPS_PAUSED",
            "MISSING_LOCATION_TARGETING",
        ]
    ]
    realTimeBiddingSetting: GoogleAdsSearchads360V23Common__RealTimeBiddingSetting
    resourceName: str
    selectiveOptimization: (
        GoogleAdsSearchads360V23Resources_Campaign_SelectiveOptimization
    )
    selectiveOptimizationMode: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "UNCONSTRAINED",
        "MATCHES_SEARCH_ADS360_EFFECTIVE_CAMPAIGN_LEVEL_CONFIG",
    ]
    servingStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SERVING", "NONE", "ENDED", "PENDING", "SUSPENDED"
    ]
    shoppingSetting: GoogleAdsSearchads360V23Resources_Campaign_ShoppingSetting
    startDateTime: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"]
    targetCpa: GoogleAdsSearchads360V23Common__TargetCpa
    targetCpc: GoogleAdsSearchads360V23Common__TargetCpc
    targetCpm: GoogleAdsSearchads360V23Common__TargetCpm
    targetImpressionShare: GoogleAdsSearchads360V23Common__TargetImpressionShare
    targetRoas: GoogleAdsSearchads360V23Common__TargetRoas
    targetSpend: GoogleAdsSearchads360V23Common__TargetSpend
    targetingSetting: GoogleAdsSearchads360V23Common__TargetingSetting
    thirdPartyIntegrationPartners: (
        GoogleAdsSearchads360V23Common__CampaignThirdPartyIntegrationPartners
    )
    trackingSetting: GoogleAdsSearchads360V23Resources_Campaign_TrackingSetting
    trackingUrlTemplate: str
    travelCampaignSettings: (
        GoogleAdsSearchads360V23Resources_Campaign_TravelCampaignSettings
    )
    urlCustomParameters: _list[GoogleAdsSearchads360V23Common__CustomParameter]
    vanityPharma: GoogleAdsSearchads360V23Resources_Campaign_VanityPharma
    videoBrandSafetySuitability: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXPANDED_INVENTORY",
        "STANDARD_INVENTORY",
        "LIMITED_INVENTORY",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignAsset(typing.TypedDict, total=False):
    asset: str
    campaign: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "LIMITED",
        "NOT_ELIGIBLE",
    ]
    primaryStatusDetails: _list[
        GoogleAdsSearchads360V23Common__AssetLinkPrimaryStatusDetails
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "ASSET_LINK_PAUSED",
            "ASSET_LINK_REMOVED",
            "ASSET_DISAPPROVED",
            "ASSET_UNDER_REVIEW",
            "ASSET_APPROVED_LABELED",
        ]
    ]
    resourceName: str
    source: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignAssetSet(
    typing.TypedDict, total=False
):
    assetSet: str
    campaign: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignAudienceView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignBidModifier(
    typing.TypedDict, total=False
):
    bidModifier: float
    campaign: str
    criterionId: str
    interactionType: GoogleAdsSearchads360V23Common__InteractionTypeInfo
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignBudget(typing.TypedDict, total=False):
    alignedBiddingStrategyId: str
    amountMicros: str
    deliveryMethod: typing.Literal["UNSPECIFIED", "UNKNOWN", "STANDARD", "ACCELERATED"]
    explicitlyShared: bool
    hasRecommendedBudget: bool
    id: str
    name: str
    period: typing.Literal["UNSPECIFIED", "UNKNOWN", "DAILY", "CUSTOM_PERIOD"]
    recommendedBudgetAmountMicros: str
    recommendedBudgetEstimatedChangeWeeklyClicks: str
    recommendedBudgetEstimatedChangeWeeklyCostMicros: str
    recommendedBudgetEstimatedChangeWeeklyInteractions: str
    recommendedBudgetEstimatedChangeWeeklyViews: str
    referenceCount: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    totalAmountMicros: str
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "STANDARD",
        "FIXED_CPA",
        "SMART_CAMPAIGN",
        "LOCAL_SERVICES",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignConversionGoal(
    typing.TypedDict, total=False
):
    biddable: bool
    campaign: str
    category: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DEFAULT",
        "PAGE_VIEW",
        "PURCHASE",
        "SIGNUP",
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
    origin: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "GOOGLE_HOSTED",
        "APP",
        "CALL_FROM_ADS",
        "STORE",
        "YOUTUBE_HOSTED",
        "FLOODLIGHT",
    ]
    resourceName: str
    searchAds360Biddable: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignCriterion(
    typing.TypedDict, total=False
):
    adSchedule: GoogleAdsSearchads360V23Common__AdScheduleInfo
    ageRange: GoogleAdsSearchads360V23Common__AgeRangeInfo
    bidModifier: float
    brandList: GoogleAdsSearchads360V23Common__BrandListInfo
    campaign: str
    carrier: GoogleAdsSearchads360V23Common__CarrierInfo
    combinedAudience: GoogleAdsSearchads360V23Common__CombinedAudienceInfo
    contentLabel: GoogleAdsSearchads360V23Common__ContentLabelInfo
    criterionId: str
    device: GoogleAdsSearchads360V23Common__DeviceInfo
    displayName: str
    extendedDemographic: GoogleAdsSearchads360V23Common__ExtendedDemographicInfo
    gender: GoogleAdsSearchads360V23Common__GenderInfo
    incomeRange: GoogleAdsSearchads360V23Common__IncomeRangeInfo
    ipBlock: GoogleAdsSearchads360V23Common__IpBlockInfo
    keyword: GoogleAdsSearchads360V23Common__KeywordInfo
    keywordTheme: GoogleAdsSearchads360V23Common__KeywordThemeInfo
    language: GoogleAdsSearchads360V23Common__LanguageInfo
    lastModifiedTime: str
    lifeEvent: GoogleAdsSearchads360V23Common__LifeEventInfo
    listingScope: GoogleAdsSearchads360V23Common__ListingScopeInfo
    localServiceId: GoogleAdsSearchads360V23Common__LocalServiceIdInfo
    location: GoogleAdsSearchads360V23Common__LocationInfo
    locationGroup: GoogleAdsSearchads360V23Common__LocationGroupInfo
    mobileAppCategory: GoogleAdsSearchads360V23Common__MobileAppCategoryInfo
    mobileApplication: GoogleAdsSearchads360V23Common__MobileApplicationInfo
    mobileDevice: GoogleAdsSearchads360V23Common__MobileDeviceInfo
    negative: bool
    operatingSystemVersion: GoogleAdsSearchads360V23Common__OperatingSystemVersionInfo
    parentalStatus: GoogleAdsSearchads360V23Common__ParentalStatusInfo
    placement: GoogleAdsSearchads360V23Common__PlacementInfo
    proximity: GoogleAdsSearchads360V23Common__ProximityInfo
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "REMOVED"]
    topic: GoogleAdsSearchads360V23Common__TopicInfo
    type: typing.Literal[
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
        "NEGATIVE_KEYWORD_LIST",
        "LOCAL_SERVICE_ID",
        "SEARCH_THEME",
        "BRAND",
        "BRAND_LIST",
        "LIFE_EVENT",
        "WEBPAGE_LIST",
        "VIDEO_LINEUP",
        "PLACEMENT_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE",
    ]
    userInterest: GoogleAdsSearchads360V23Common__UserInterestInfo
    userList: GoogleAdsSearchads360V23Common__UserListInfo
    videoLineup: GoogleAdsSearchads360V23Common__VideoLineupInfo
    webpage: GoogleAdsSearchads360V23Common__WebpageInfo
    webpageList: GoogleAdsSearchads360V23Common__WebpageListInfo
    youtubeChannel: GoogleAdsSearchads360V23Common__YouTubeChannelInfo
    youtubeVideo: GoogleAdsSearchads360V23Common__YouTubeVideoInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignCustomizer(
    typing.TypedDict, total=False
):
    campaign: str
    customizerAttribute: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    value: GoogleAdsSearchads360V23Common__CustomizerValue

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignDraft(typing.TypedDict, total=False):
    baseCampaign: str
    draftCampaign: str
    draftId: str
    hasExperimentRunning: bool
    longRunningOperation: str
    name: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PROPOSED",
        "REMOVED",
        "PROMOTING",
        "PROMOTED",
        "PROMOTE_FAILED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignEffectiveLabel(
    typing.TypedDict, total=False
):
    campaign: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignGoalConfig(
    typing.TypedDict, total=False
):
    campaign: str
    campaignLoyaltyRetentionSettings: GoogleAdsSearchads360V23Common_CampaignGoalSettings_CampaignLoyaltyRetentionGoalSettings
    campaignNewCustomerAcquisitionSettings: GoogleAdsSearchads360V23Common_CampaignGoalSettings_CampaignNewCustomerAcquisitionGoalSettings
    campaignRetentionSettings: GoogleAdsSearchads360V23Common_CampaignGoalSettings_CampaignRetentionGoalSettings
    goal: str
    goalType: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER_RETENTION"]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignGroup(typing.TypedDict, total=False):
    id: str
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignLabel(typing.TypedDict, total=False):
    campaign: str
    label: str
    ownerCustomerId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignLifecycleGoal(
    typing.TypedDict, total=False
):
    campaign: str
    customerAcquisitionGoalSettings: (
        GoogleAdsSearchads360V23Resources__CustomerAcquisitionGoalSettings
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignSearchTermInsight(
    typing.TypedDict, total=False
):
    campaignId: str
    categoryLabel: str
    id: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignSearchTermView(
    typing.TypedDict, total=False
):
    campaign: str
    resourceName: str
    searchTerm: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignSharedSet(
    typing.TypedDict, total=False
):
    campaign: str
    resourceName: str
    sharedSet: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CampaignSimulation(
    typing.TypedDict, total=False
):
    budgetPointList: GoogleAdsSearchads360V23Common__BudgetSimulationPointList
    campaignId: str
    cpcBidPointList: GoogleAdsSearchads360V23Common__CpcBidSimulationPointList
    endDate: str
    modificationMethod: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "UNIFORM", "DEFAULT", "SCALING"
    ]
    resourceName: str
    startDate: str
    targetCpaPointList: GoogleAdsSearchads360V23Common__TargetCpaSimulationPointList
    targetImpressionSharePointList: (
        GoogleAdsSearchads360V23Common__TargetImpressionShareSimulationPointList
    )
    targetRoasPointList: GoogleAdsSearchads360V23Common__TargetRoasSimulationPointList
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CPC_BID",
        "CPV_BID",
        "TARGET_CPA",
        "BID_MODIFIER",
        "TARGET_ROAS",
        "PERCENT_CPC_BID",
        "TARGET_IMPRESSION_SHARE",
        "BUDGET",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CarrierConstant(typing.TypedDict, total=False):
    countryCode: str
    id: str
    name: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CartDataSalesView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ChangeEvent(typing.TypedDict, total=False):
    adGroup: str
    asset: str
    campaign: str
    changeDateTime: str
    changeResourceName: str
    changeResourceType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD",
        "AD_GROUP",
        "AD_GROUP_CRITERION",
        "CAMPAIGN",
        "CAMPAIGN_BUDGET",
        "AD_GROUP_BID_MODIFIER",
        "CAMPAIGN_CRITERION",
        "FEED",
        "FEED_ITEM",
        "CAMPAIGN_FEED",
        "AD_GROUP_FEED",
        "AD_GROUP_AD",
        "ASSET",
        "CUSTOMER_ASSET",
        "CAMPAIGN_ASSET",
        "AD_GROUP_ASSET",
        "ASSET_SET",
        "ASSET_SET_ASSET",
        "CAMPAIGN_ASSET_SET",
    ]
    changedFields: str
    clientType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "GOOGLE_ADS_WEB_CLIENT",
        "GOOGLE_ADS_AUTOMATED_RULE",
        "GOOGLE_ADS_SCRIPTS",
        "GOOGLE_ADS_BULK_UPLOAD",
        "GOOGLE_ADS_API",
        "GOOGLE_ADS_EDITOR",
        "GOOGLE_ADS_MOBILE_APP",
        "GOOGLE_ADS_RECOMMENDATIONS",
        "SEARCH_ADS_360_SYNC",
        "SEARCH_ADS_360_POST",
        "INTERNAL_TOOL",
        "OTHER",
        "GOOGLE_ADS_RECOMMENDATIONS_SUBSCRIPTION",
    ]
    newResource: GoogleAdsSearchads360V23Resources_ChangeEvent_ChangedResource
    oldResource: GoogleAdsSearchads360V23Resources_ChangeEvent_ChangedResource
    resourceChangeOperation: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CREATE", "UPDATE", "REMOVE"
    ]
    resourceName: str
    userEmail: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ChangeStatus(typing.TypedDict, total=False):
    adGroup: str
    adGroupAd: str
    adGroupAsset: str
    adGroupBidModifier: str
    adGroupCriterion: str
    asset: str
    assetGroup: str
    assetSet: str
    campaign: str
    campaignAsset: str
    campaignAssetSet: str
    campaignBudget: str
    campaignCriterion: str
    campaignSharedSet: str
    combinedAudience: str
    customerAsset: str
    lastChangeDateTime: str
    resourceName: str
    resourceStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADDED", "CHANGED", "REMOVED"
    ]
    resourceType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AD_GROUP",
        "AD_GROUP_AD",
        "AD_GROUP_CRITERION",
        "CAMPAIGN",
        "CAMPAIGN_CRITERION",
        "CAMPAIGN_BUDGET",
        "FEED",
        "FEED_ITEM",
        "AD_GROUP_FEED",
        "CAMPAIGN_FEED",
        "AD_GROUP_BID_MODIFIER",
        "SHARED_SET",
        "CAMPAIGN_SHARED_SET",
        "ASSET",
        "CUSTOMER_ASSET",
        "CAMPAIGN_ASSET",
        "AD_GROUP_ASSET",
        "COMBINED_AUDIENCE",
        "ASSET_GROUP",
        "ASSET_SET",
        "CAMPAIGN_ASSET_SET",
    ]
    sharedSet: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ClickView(typing.TypedDict, total=False):
    adGroupAd: str
    areaOfInterest: GoogleAdsSearchads360V23Common__ClickLocation
    campaignLocationTarget: str
    gclid: str
    keyword: str
    keywordInfo: GoogleAdsSearchads360V23Common__KeywordInfo
    locationOfPresence: GoogleAdsSearchads360V23Common__ClickLocation
    pageNumber: str
    resourceName: str
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CombinedAudience(
    typing.TypedDict, total=False
):
    description: str
    id: str
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ContactDetails(typing.TypedDict, total=False):
    consumerName: str
    email: str
    phoneNumber: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ContentCriterionView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Conversion(typing.TypedDict, total=False):
    adId: str
    advertiserConversionId: str
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    assetId: str
    attributionType: typing.Literal["UNSPECIFIED", "UNKNOWN", "VISIT", "CRITERION_AD"]
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
    productChannel: typing.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]
    productCountryCode: str
    productId: str
    productLanguageCode: str
    productStoreId: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    visitId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ConversionAction(
    typing.TypedDict, total=False
):
    appId: str
    attributionModelSettings: (
        GoogleAdsSearchads360V23Resources_ConversionAction_AttributionModelSettings
    )
    category: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DEFAULT",
        "PAGE_VIEW",
        "PURCHASE",
        "SIGNUP",
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
    countingType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ONE_PER_CLICK", "MANY_PER_CLICK"
    ]
    creationTime: str
    firebaseSettings: (
        GoogleAdsSearchads360V23Resources_ConversionAction_FirebaseSettings
    )
    floodlightSettings: (
        GoogleAdsSearchads360V23Resources_ConversionAction_FloodlightSettings
    )
    googleAnalytics4Settings: (
        GoogleAdsSearchads360V23Resources_ConversionAction_GoogleAnalytics4Settings
    )
    id: str
    includeInClientAccountConversionsMetric: bool
    includeInConversionsMetric: bool
    mobileAppVendor: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_APP_STORE"
    ]
    name: str
    origin: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "GOOGLE_HOSTED",
        "APP",
        "CALL_FROM_ADS",
        "STORE",
        "YOUTUBE_HOSTED",
        "FLOODLIGHT",
    ]
    ownerCustomer: str
    phoneCallDurationSeconds: str
    primaryForGoal: bool
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "HIDDEN"]
    tagSnippets: _list[GoogleAdsSearchads360V23Common__TagSnippet]
    thirdPartyAppAnalyticsSettings: GoogleAdsSearchads360V23Resources_ConversionAction_ThirdPartyAppAnalyticsSettings
    type: typing.Literal[
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
    valueSettings: GoogleAdsSearchads360V23Resources_ConversionAction_ValueSettings
    viewThroughLookbackWindowDays: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ConversionCustomVariable(
    typing.TypedDict, total=False
):
    cardinality: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BELOW_ALL_LIMITS",
        "EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT",
        "APPROACHES_STATS_LIMIT",
        "EXCEEDS_STATS_LIMIT",
    ]
    customColumnIds: _list[str]
    family: typing.Literal["UNSPECIFIED", "UNKNOWN", "STANDARD", "FLOODLIGHT"]
    floodlightConversionCustomVariableInfo: GoogleAdsSearchads360V23Resources_ConversionCustomVariable_FloodlightConversionCustomVariableInfo
    id: str
    name: str
    ownerCustomer: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACTIVATION_NEEDED", "ENABLED", "PAUSED"
    ]
    tag: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ConversionGoalCampaignConfig(
    typing.TypedDict, total=False
):
    campaign: str
    customConversionGoal: str
    goalConfigLevel: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER", "CAMPAIGN"]
    resourceName: str
    searchAds360CustomConversionGoal: str
    searchAds360GoalConfigLevel: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CUSTOMER", "CAMPAIGN"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ConversionTrackingSetting(
    typing.TypedDict, total=False
):
    acceptedCustomerDataTerms: bool
    conversionTrackingId: str
    conversionTrackingStatus: typing.Literal[
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
class GoogleAdsSearchads360V23Resources__ConversionValueRule(
    typing.TypedDict, total=False
):
    action: GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleAction
    audienceCondition: (
        GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleAudienceCondition
    )
    deviceCondition: (
        GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleDeviceCondition
    )
    geoLocationCondition: GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleGeoLocationCondition
    id: str
    itineraryCondition: GoogleAdsSearchads360V23Resources_ConversionValueRule_ValueRuleItineraryCondition
    ownerCustomer: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ConversionValueRuleSet(
    typing.TypedDict, total=False
):
    attachmentType: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER", "CAMPAIGN"]
    campaign: str
    conversionActionCategories: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "DEFAULT",
            "PAGE_VIEW",
            "PURCHASE",
            "SIGNUP",
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
    ]
    conversionValueRules: _list[str]
    dimensions: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "GEO_LOCATION",
            "DEVICE",
            "AUDIENCE",
            "NO_CONDITION",
            "ITINERARY",
        ]
    ]
    id: str
    ownerCustomer: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CreditDetails(typing.TypedDict, total=False):
    creditState: typing.Literal["UNSPECIFIED", "UNKNOWN", "PENDING", "CREDITED"]
    creditStateLastUpdateDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CurrencyConstant(
    typing.TypedDict, total=False
):
    billableUnitMicros: str
    code: str
    name: str
    resourceName: str
    symbol: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomAudience(typing.TypedDict, total=False):
    description: str
    id: str
    members: _list[GoogleAdsSearchads360V23Resources__CustomAudienceMember]
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    type: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AUTO", "INTEREST", "PURCHASE_INTENT", "SEARCH"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomAudienceMember(
    typing.TypedDict, total=False
):
    app: str
    keyword: str
    memberType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "KEYWORD", "URL", "PLACE_CATEGORY", "APP"
    ]
    placeCategory: str
    url: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomColumn(typing.TypedDict, total=False):
    description: str
    id: str
    name: str
    queryable: bool
    referencedSystemColumns: _list[str]
    referencesAttributes: bool
    referencesMetrics: bool
    renderType: typing.Literal[
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
    valueType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "STRING", "INT64", "DOUBLE", "BOOLEAN", "DATE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomConversionGoal(
    typing.TypedDict, total=False
):
    conversionActions: _list[str]
    id: str
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomInterest(typing.TypedDict, total=False):
    description: str
    id: str
    members: _list[GoogleAdsSearchads360V23Resources__CustomInterestMember]
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOM_AFFINITY", "CUSTOM_INTENT"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomInterestMember(
    typing.TypedDict, total=False
):
    memberType: typing.Literal["UNSPECIFIED", "UNKNOWN", "KEYWORD", "URL"]
    parameter: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomLeadFormSubmissionField(
    typing.TypedDict, total=False
):
    fieldValue: str
    questionText: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Customer(typing.TypedDict, total=False):
    accountLevel: typing.Literal[
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
    accountStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED", "SUSPENDED", "REMOVED", "DRAFT"
    ]
    accountType: typing.Literal[
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
    callReportingSetting: GoogleAdsSearchads360V23Resources__CallReportingSetting
    containsEuPoliticalAdvertising: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CONTAINS_EU_POLITICAL_ADVERTISING",
        "DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING",
    ]
    conversionTrackingSetting: (
        GoogleAdsSearchads360V23Resources__ConversionTrackingSetting
    )
    creationTime: str
    currencyCode: str
    customerAgreementSetting: (
        GoogleAdsSearchads360V23Resources__CustomerAgreementSetting
    )
    descriptiveName: str
    doubleClickCampaignManagerSetting: (
        GoogleAdsSearchads360V23Resources__DoubleClickCampaignManagerSetting
    )
    engineId: str
    finalUrlSuffix: str
    hasPartnersBadge: bool
    id: str
    imageAssetAutoMigrationDone: bool
    imageAssetAutoMigrationDoneDateTime: str
    lastModifiedTime: str
    localServicesSettings: GoogleAdsSearchads360V23Resources__LocalServicesSettings
    locationAssetAutoMigrationDone: bool
    locationAssetAutoMigrationDoneDateTime: str
    manager: bool
    managerDescriptiveName: str
    managerId: str
    optimizationScore: float
    optimizationScoreWeight: float
    payPerConversionEligibilityFailureReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "NOT_ENOUGH_CONVERSIONS",
            "CONVERSION_LAG_TOO_HIGH",
            "HAS_CAMPAIGN_WITH_SHARED_BUDGET",
            "HAS_UPLOAD_CLICKS_CONVERSION",
            "AVERAGE_DAILY_SPEND_TOO_HIGH",
            "ANALYSIS_NOT_COMPLETE",
            "OTHER",
        ]
    ]
    remarketingSetting: GoogleAdsSearchads360V23Resources__RemarketingSetting
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "CANCELED", "SUSPENDED", "CLOSED"
    ]
    subManagerDescriptiveName: str
    subManagerId: str
    testAccount: bool
    timeZone: str
    trackingUrlTemplate: str
    videoBrandSafetySuitability: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXPANDED_INVENTORY",
        "STANDARD_INVENTORY",
        "LIMITED_INVENTORY",
    ]
    videoCustomer: GoogleAdsSearchads360V23Resources__VideoCustomer

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerAcquisitionGoalSettings(
    typing.TypedDict, total=False
):
    optimizationMode: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "TARGET_ALL_EQUALLY",
        "BID_HIGHER_FOR_NEW_CUSTOMER",
        "TARGET_NEW_CUSTOMER",
    ]
    valueSettings: GoogleAdsSearchads360V23Common__LifecycleGoalValueSettings

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerAgreementSetting(
    typing.TypedDict, total=False
):
    acceptedLeadFormTerms: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerAsset(typing.TypedDict, total=False):
    asset: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    primaryStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ELIGIBLE",
        "PAUSED",
        "REMOVED",
        "PENDING",
        "LIMITED",
        "NOT_ELIGIBLE",
    ]
    primaryStatusDetails: _list[
        GoogleAdsSearchads360V23Common__AssetLinkPrimaryStatusDetails
    ]
    primaryStatusReasons: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "ASSET_LINK_PAUSED",
            "ASSET_LINK_REMOVED",
            "ASSET_DISAPPROVED",
            "ASSET_UNDER_REVIEW",
            "ASSET_APPROVED_LABELED",
        ]
    ]
    resourceName: str
    source: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER", "AUTOMATICALLY_CREATED"
    ]
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerAssetSet(
    typing.TypedDict, total=False
):
    assetSet: str
    customer: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerClient(typing.TypedDict, total=False):
    appliedLabels: _list[str]
    clientCustomer: str
    currencyCode: str
    descriptiveName: str
    hidden: bool
    id: str
    level: str
    manager: bool
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "CANCELED", "SUSPENDED", "CLOSED"
    ]
    testAccount: bool
    timeZone: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerClientLink(
    typing.TypedDict, total=False
):
    clientCustomer: str
    hidden: bool
    managerLinkId: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACTIVE", "INACTIVE", "PENDING", "REFUSED", "CANCELED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerConversionGoal(
    typing.TypedDict, total=False
):
    biddable: bool
    category: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DEFAULT",
        "PAGE_VIEW",
        "PURCHASE",
        "SIGNUP",
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
    origin: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "GOOGLE_HOSTED",
        "APP",
        "CALL_FROM_ADS",
        "STORE",
        "YOUTUBE_HOSTED",
        "FLOODLIGHT",
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerCustomizer(
    typing.TypedDict, total=False
):
    customizerAttribute: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    value: GoogleAdsSearchads360V23Common__CustomizerValue

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerLabel(typing.TypedDict, total=False):
    customer: str
    label: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerLifecycleGoal(
    typing.TypedDict, total=False
):
    customerAcquisitionGoalValueSettings: (
        GoogleAdsSearchads360V23Common__LifecycleGoalValueSettings
    )
    ownerCustomer: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerManagerLink(
    typing.TypedDict, total=False
):
    managerCustomer: str
    managerLinkId: str
    resourceName: str
    startTime: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ACTIVE", "INACTIVE", "PENDING", "REFUSED", "CANCELED"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerNegativeCriterion(
    typing.TypedDict, total=False
):
    contentLabel: GoogleAdsSearchads360V23Common__ContentLabelInfo
    id: str
    ipBlock: GoogleAdsSearchads360V23Common__IpBlockInfo
    mobileAppCategory: GoogleAdsSearchads360V23Common__MobileAppCategoryInfo
    mobileApplication: GoogleAdsSearchads360V23Common__MobileApplicationInfo
    negativeKeywordList: GoogleAdsSearchads360V23Common__NegativeKeywordListInfo
    placement: GoogleAdsSearchads360V23Common__PlacementInfo
    placementList: GoogleAdsSearchads360V23Common__PlacementListInfo
    resourceName: str
    type: typing.Literal[
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
        "NEGATIVE_KEYWORD_LIST",
        "LOCAL_SERVICE_ID",
        "SEARCH_THEME",
        "BRAND",
        "BRAND_LIST",
        "LIFE_EVENT",
        "WEBPAGE_LIST",
        "VIDEO_LINEUP",
        "PLACEMENT_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE",
    ]
    youtubeChannel: GoogleAdsSearchads360V23Common__YouTubeChannelInfo
    youtubeVideo: GoogleAdsSearchads360V23Common__YouTubeVideoInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerSearchTermInsight(
    typing.TypedDict, total=False
):
    categoryLabel: str
    id: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerSkAdNetworkConversionValueSchema(
    typing.TypedDict, total=False
):
    resourceName: str
    schema: GoogleAdsSearchads360V23Resources_CustomerSkAdNetworkConversionValueSchema_SkAdNetworkConversionValueSchema

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerUserAccess(
    typing.TypedDict, total=False
):
    accessCreationDateTime: str
    accessRole: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADMIN", "STANDARD", "READ_ONLY", "EMAIL_ONLY"
    ]
    emailAddress: str
    inviterUserEmailAddress: str
    resourceName: str
    userId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomerUserAccessInvitation(
    typing.TypedDict, total=False
):
    accessRole: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADMIN", "STANDARD", "READ_ONLY", "EMAIL_ONLY"
    ]
    creationDateTime: str
    emailAddress: str
    invitationId: str
    invitationStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PENDING", "DECLINED", "EXPIRED"
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomizerAttribute(
    typing.TypedDict, total=False
):
    id: str
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "TEXT", "NUMBER", "PRICE", "PERCENT"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DataLink(typing.TypedDict, total=False):
    dataLinkId: str
    productLinkId: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUESTED",
        "PENDING_APPROVAL",
        "ENABLED",
        "DISABLED",
        "REVOKED",
        "REJECTED",
    ]
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "VIDEO"]
    youtubeVideo: GoogleAdsSearchads360V23Resources__YoutubeVideoIdentifier

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DataPartnerIdentifier(
    typing.TypedDict, total=False
):
    dataPartnerId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DetailContentSuitabilityPlacementView(
    typing.TypedDict, total=False
):
    displayName: str
    placement: str
    placementType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "GOOGLE_PRODUCTS",
    ]
    resourceName: str
    targetUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DetailPlacementView(
    typing.TypedDict, total=False
):
    displayName: str
    groupPlacementTargetUrl: str
    placement: str
    placementType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "GOOGLE_PRODUCTS",
    ]
    resourceName: str
    targetUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DetailedDemographic(
    typing.TypedDict, total=False
):
    availabilities: _list[GoogleAdsSearchads360V23Common__CriterionCategoryAvailability]
    id: str
    launchedToAll: bool
    name: str
    parent: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DisplayKeywordView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DistanceView(typing.TypedDict, total=False):
    distanceBucket: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WITHIN_700M",
        "WITHIN_1KM",
        "WITHIN_5KM",
        "WITHIN_10KM",
        "WITHIN_15KM",
        "WITHIN_20KM",
        "WITHIN_25KM",
        "WITHIN_30KM",
        "WITHIN_35KM",
        "WITHIN_40KM",
        "WITHIN_45KM",
        "WITHIN_50KM",
        "WITHIN_55KM",
        "WITHIN_60KM",
        "WITHIN_65KM",
        "BEYOND_65KM",
        "WITHIN_0_7MILES",
        "WITHIN_1MILE",
        "WITHIN_5MILES",
        "WITHIN_10MILES",
        "WITHIN_15MILES",
        "WITHIN_20MILES",
        "WITHIN_25MILES",
        "WITHIN_30MILES",
        "WITHIN_35MILES",
        "WITHIN_40MILES",
        "BEYOND_40MILES",
    ]
    metricSystem: bool
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DoubleClickCampaignManagerSetting(
    typing.TypedDict, total=False
):
    advertiserId: str
    networkId: str
    timeZone: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__DynamicSearchAdsSearchTermView(
    typing.TypedDict, total=False
):
    hasMatchingKeyword: bool
    hasNegativeKeyword: bool
    hasNegativeUrl: bool
    headline: str
    landingPage: str
    pageUrl: str
    resourceName: str
    searchTerm: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ExpandedLandingPageView(
    typing.TypedDict, total=False
):
    expandedFinalUrl: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Experiment(typing.TypedDict, total=False):
    description: str
    endDate: str
    experimentId: str
    goals: _list[GoogleAdsSearchads360V23Common__MetricGoal]
    longRunningOperation: str
    name: str
    promoteStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "COMPLETED_WITH_WARNING",
    ]
    resourceName: str
    startDate: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ENABLED",
        "REMOVED",
        "HALTED",
        "PROMOTED",
        "SETUP",
        "INITIATED",
        "GRADUATED",
    ]
    suffix: str
    syncEnabled: bool
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DISPLAY_AND_VIDEO_360",
        "AD_VARIATION",
        "YOUTUBE_CUSTOM",
        "DISPLAY_CUSTOM",
        "SEARCH_CUSTOM",
        "DISPLAY_AUTOMATED_BIDDING_STRATEGY",
        "SEARCH_AUTOMATED_BIDDING_STRATEGY",
        "SHOPPING_AUTOMATED_BIDDING_STRATEGY",
        "SMART_MATCHING",
        "HOTEL_CUSTOM",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ExperimentArm(typing.TypedDict, total=False):
    assetGroups: _list[GoogleAdsSearchads360V23Resources_ExperimentArm_AssetGroupInfo]
    campaigns: _list[str]
    control: bool
    experiment: str
    inDesignCampaigns: _list[str]
    name: str
    resourceName: str
    trafficSplit: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Fellowship(typing.TypedDict, total=False):
    completionYear: int
    institutionName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__FinalUrlExpansionAssetView(
    typing.TypedDict, total=False
):
    adGroup: str
    asset: str
    assetGroup: str
    campaign: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    finalUrl: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED", "PAUSED"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GenderView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GeoTargetConstant(
    typing.TypedDict, total=False
):
    canonicalName: str
    countryCode: str
    id: str
    name: str
    parentGeoTarget: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVAL_PLANNED"]
    targetType: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GeographicView(typing.TypedDict, total=False):
    countryCriterionId: str
    locationType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AREA_OF_INTEREST", "LOCATION_OF_PRESENCE"
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Goal(typing.TypedDict, total=False):
    goalId: str
    goalType: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER_RETENTION"]
    optimizationEligibility: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ELIGIBLE", "INELIGIBLE"
    ]
    ownerCustomer: str
    resourceName: str
    retentionGoalSettings: GoogleAdsSearchads360V23Common_GoalSetting_RetentionGoal

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GoogleAdsIdentifier(
    typing.TypedDict, total=False
):
    customer: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GranularInsuranceStatus(
    typing.TypedDict, total=False
):
    categoryId: str
    geoCriterionId: str
    verificationStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NEEDS_REVIEW",
        "FAILED",
        "PASSED",
        "NOT_APPLICABLE",
        "NO_SUBMISSION",
        "PARTIAL_SUBMISSION",
        "PENDING_ESCALATION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GranularLicenseStatus(
    typing.TypedDict, total=False
):
    categoryId: str
    geoCriterionId: str
    verificationStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NEEDS_REVIEW",
        "FAILED",
        "PASSED",
        "NOT_APPLICABLE",
        "NO_SUBMISSION",
        "PARTIAL_SUBMISSION",
        "PENDING_ESCALATION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GroupContentSuitabilityPlacementView(
    typing.TypedDict, total=False
):
    displayName: str
    placement: str
    placementType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "GOOGLE_PRODUCTS",
    ]
    resourceName: str
    targetUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__GroupPlacementView(
    typing.TypedDict, total=False
):
    displayName: str
    placement: str
    placementType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "GOOGLE_PRODUCTS",
    ]
    resourceName: str
    targetUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__HotelCenterLinkInvitationIdentifier(
    typing.TypedDict, total=False
):
    hotelCenterId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__HotelGroupView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__HotelPerformanceView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__HotelReconciliation(
    typing.TypedDict, total=False
):
    billed: bool
    campaign: str
    checkInDate: str
    checkOutDate: str
    commissionId: str
    hotelCenterId: str
    hotelId: str
    orderId: str
    reconciledValueMicros: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "RESERVATION_ENABLED",
        "RECONCILIATION_NEEDED",
        "RECONCILED",
        "CANCELED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__IncomeRangeView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__InsuranceVerificationArtifact(
    typing.TypedDict, total=False
):
    amountMicros: str
    expirationDateTime: str
    insuranceDocumentReadonly: (
        GoogleAdsSearchads360V23Common__LocalServicesDocumentReadOnly
    )
    rejectionReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BUSINESS_NAME_MISMATCH",
        "INSURANCE_AMOUNT_INSUFFICIENT",
        "EXPIRED",
        "NO_SIGNATURE",
        "NO_POLICY_NUMBER",
        "NO_COMMERCIAL_GENERAL_LIABILITY",
        "EDITABLE_FORMAT",
        "CATEGORY_MISMATCH",
        "MISSING_EXPIRATION_DATE",
        "POOR_QUALITY",
        "POTENTIALLY_EDITED",
        "WRONG_DOCUMENT_TYPE",
        "NON_FINAL",
        "OTHER",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Invoice(typing.TypedDict, total=False):
    accountBudgetSummaries: _list[
        GoogleAdsSearchads360V23Resources_Invoice_AccountBudgetSummary
    ]
    accountSummaries: _list[GoogleAdsSearchads360V23Resources_Invoice_AccountSummary]
    adjustmentsSubtotalAmountMicros: str
    adjustmentsTaxAmountMicros: str
    adjustmentsTotalAmountMicros: str
    billingSetup: str
    correctedInvoice: str
    currencyCode: str
    dueDate: str
    exportChargeSubtotalAmountMicros: str
    exportChargeTaxAmountMicros: str
    exportChargeTotalAmountMicros: str
    id: str
    issueDate: str
    paymentsAccountId: str
    paymentsProfileId: str
    pdfUrl: str
    regulatoryCostsSubtotalAmountMicros: str
    regulatoryCostsTaxAmountMicros: str
    regulatoryCostsTotalAmountMicros: str
    replacedInvoices: _list[str]
    resourceName: str
    serviceDateRange: GoogleAdsSearchads360V23Common__DateRange
    subtotalAmountMicros: str
    taxAmountMicros: str
    totalAmountMicros: str
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "CREDIT_MEMO", "INVOICE"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlan(typing.TypedDict, total=False):
    forecastPeriod: GoogleAdsSearchads360V23Resources__KeywordPlanForecastPeriod
    id: str
    name: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlanAdGroup(
    typing.TypedDict, total=False
):
    cpcBidMicros: str
    id: str
    keywordPlanCampaign: str
    name: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlanAdGroupKeyword(
    typing.TypedDict, total=False
):
    cpcBidMicros: str
    id: str
    keywordPlanAdGroup: str
    matchType: typing.Literal["UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"]
    negative: bool
    resourceName: str
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlanCampaign(
    typing.TypedDict, total=False
):
    cpcBidMicros: str
    geoTargets: _list[GoogleAdsSearchads360V23Resources__KeywordPlanGeoTarget]
    id: str
    keywordPlan: str
    keywordPlanNetwork: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "GOOGLE_SEARCH", "GOOGLE_SEARCH_AND_PARTNERS"
    ]
    languageConstants: _list[str]
    name: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlanCampaignKeyword(
    typing.TypedDict, total=False
):
    id: str
    keywordPlanCampaign: str
    matchType: typing.Literal["UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"]
    negative: bool
    resourceName: str
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlanForecastPeriod(
    typing.TypedDict, total=False
):
    dateInterval: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NEXT_WEEK", "NEXT_MONTH", "NEXT_QUARTER"
    ]
    dateRange: GoogleAdsSearchads360V23Common__DateRange

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordPlanGeoTarget(
    typing.TypedDict, total=False
):
    geoTargetConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordThemeConstant(
    typing.TypedDict, total=False
):
    countryCode: str
    displayName: str
    languageCode: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__KeywordView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Label(typing.TypedDict, total=False):
    id: str
    name: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    textLabel: GoogleAdsSearchads360V23Common__TextLabel

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LandingPageView(typing.TypedDict, total=False):
    resourceName: str
    unexpandedFinalUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LanguageConstant(
    typing.TypedDict, total=False
):
    code: str
    id: str
    name: str
    resourceName: str
    targetable: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LeadFormSubmissionData(
    typing.TypedDict, total=False
):
    adGroup: str
    adGroupAd: str
    asset: str
    campaign: str
    customLeadFormSubmissionFields: _list[
        GoogleAdsSearchads360V23Resources__CustomLeadFormSubmissionField
    ]
    gclid: str
    id: str
    leadFormSubmissionFields: _list[
        GoogleAdsSearchads360V23Resources__LeadFormSubmissionField
    ]
    resourceName: str
    submissionDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LeadFormSubmissionField(
    typing.TypedDict, total=False
):
    fieldType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FULL_NAME",
        "EMAIL",
        "PHONE_NUMBER",
        "POSTAL_CODE",
        "STREET_ADDRESS",
        "CITY",
        "REGION",
        "COUNTRY",
        "WORK_EMAIL",
        "COMPANY_NAME",
        "WORK_PHONE",
        "JOB_TITLE",
        "GOVERNMENT_ISSUED_ID_CPF_BR",
        "GOVERNMENT_ISSUED_ID_DNI_AR",
        "GOVERNMENT_ISSUED_ID_DNI_PE",
        "GOVERNMENT_ISSUED_ID_RUT_CL",
        "GOVERNMENT_ISSUED_ID_CC_CO",
        "GOVERNMENT_ISSUED_ID_CI_EC",
        "GOVERNMENT_ISSUED_ID_RFC_MX",
        "FIRST_NAME",
        "LAST_NAME",
        "VEHICLE_MODEL",
        "VEHICLE_TYPE",
        "PREFERRED_DEALERSHIP",
        "VEHICLE_PURCHASE_TIMELINE",
        "VEHICLE_OWNERSHIP",
        "VEHICLE_PAYMENT_TYPE",
        "VEHICLE_CONDITION",
        "COMPANY_SIZE",
        "ANNUAL_SALES",
        "YEARS_IN_BUSINESS",
        "JOB_DEPARTMENT",
        "JOB_ROLE",
        "OVER_18_AGE",
        "OVER_19_AGE",
        "OVER_20_AGE",
        "OVER_21_AGE",
        "OVER_22_AGE",
        "OVER_23_AGE",
        "OVER_24_AGE",
        "OVER_25_AGE",
        "OVER_26_AGE",
        "OVER_27_AGE",
        "OVER_28_AGE",
        "OVER_29_AGE",
        "OVER_30_AGE",
        "OVER_31_AGE",
        "OVER_32_AGE",
        "OVER_33_AGE",
        "OVER_34_AGE",
        "OVER_35_AGE",
        "OVER_36_AGE",
        "OVER_37_AGE",
        "OVER_38_AGE",
        "OVER_39_AGE",
        "OVER_40_AGE",
        "OVER_41_AGE",
        "OVER_42_AGE",
        "OVER_43_AGE",
        "OVER_44_AGE",
        "OVER_45_AGE",
        "OVER_46_AGE",
        "OVER_47_AGE",
        "OVER_48_AGE",
        "OVER_49_AGE",
        "OVER_50_AGE",
        "OVER_51_AGE",
        "OVER_52_AGE",
        "OVER_53_AGE",
        "OVER_54_AGE",
        "OVER_55_AGE",
        "OVER_56_AGE",
        "OVER_57_AGE",
        "OVER_58_AGE",
        "OVER_59_AGE",
        "OVER_60_AGE",
        "OVER_61_AGE",
        "OVER_62_AGE",
        "OVER_63_AGE",
        "OVER_64_AGE",
        "OVER_65_AGE",
        "EDUCATION_PROGRAM",
        "EDUCATION_COURSE",
        "PRODUCT",
        "SERVICE",
        "OFFER",
        "CATEGORY",
        "PREFERRED_CONTACT_METHOD",
        "PREFERRED_LOCATION",
        "PREFERRED_CONTACT_TIME",
        "PURCHASE_TIMELINE",
        "YEARS_OF_EXPERIENCE",
        "JOB_INDUSTRY",
        "LEVEL_OF_EDUCATION",
        "PROPERTY_TYPE",
        "REALTOR_HELP_GOAL",
        "PROPERTY_COMMUNITY",
        "PRICE_RANGE",
        "NUMBER_OF_BEDROOMS",
        "FURNISHED_PROPERTY",
        "PETS_ALLOWED_PROPERTY",
        "NEXT_PLANNED_PURCHASE",
        "EVENT_SIGNUP_INTEREST",
        "PREFERRED_SHOPPING_PLACES",
        "FAVORITE_BRAND",
        "TRANSPORTATION_COMMERCIAL_LICENSE_TYPE",
        "EVENT_BOOKING_INTEREST",
        "DESTINATION_COUNTRY",
        "DESTINATION_CITY",
        "DEPARTURE_COUNTRY",
        "DEPARTURE_CITY",
        "DEPARTURE_DATE",
        "RETURN_DATE",
        "NUMBER_OF_TRAVELERS",
        "TRAVEL_BUDGET",
        "TRAVEL_ACCOMMODATION",
    ]
    fieldValue: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LicenseVerificationArtifact(
    typing.TypedDict, total=False
):
    expirationDateTime: str
    licenseDocumentReadonly: (
        GoogleAdsSearchads360V23Common__LocalServicesDocumentReadOnly
    )
    licenseNumber: str
    licenseType: str
    licenseeFirstName: str
    licenseeLastName: str
    rejectionReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BUSINESS_NAME_MISMATCH",
        "UNAUTHORIZED",
        "EXPIRED",
        "POOR_QUALITY",
        "UNVERIFIABLE",
        "WRONG_DOCUMENT_OR_ID",
        "OTHER",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LifeEvent(typing.TypedDict, total=False):
    availabilities: _list[GoogleAdsSearchads360V23Common__CriterionCategoryAvailability]
    id: str
    launchedToAll: bool
    name: str
    parent: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ListingGroupFilterDimension(
    typing.TypedDict, total=False
):
    productBrand: (
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductBrand
    )
    productCategory: (
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductCategory
    )
    productChannel: (
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductChannel
    )
    productCondition: (
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductCondition
    )
    productCustomAttribute: GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductCustomAttribute
    productItemId: (
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductItemId
    )
    productType: (
        GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_ProductType
    )
    webpage: GoogleAdsSearchads360V23Resources_ListingGroupFilterDimension_Webpage

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ListingGroupFilterDimensionPath(
    typing.TypedDict, total=False
):
    dimensions: _list[GoogleAdsSearchads360V23Resources__ListingGroupFilterDimension]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocalServicesEmployee(
    typing.TypedDict, total=False
):
    categoryIds: _list[str]
    creationDateTime: str
    emailAddress: str
    fellowships: _list[GoogleAdsSearchads360V23Resources__Fellowship]
    firstName: str
    id: str
    jobTitle: str
    languagesSpoken: _list[str]
    lastName: str
    middleName: str
    nationalProviderIdNumber: str
    residencies: _list[GoogleAdsSearchads360V23Resources__Residency]
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "BUSINESS_OWNER", "EMPLOYEE"]
    universityDegrees: _list[GoogleAdsSearchads360V23Resources__UniversityDegree]
    yearStartedPracticing: int

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocalServicesLead(
    typing.TypedDict, total=False
):
    categoryId: str
    contactDetails: GoogleAdsSearchads360V23Resources__ContactDetails
    creationDateTime: str
    creditDetails: GoogleAdsSearchads360V23Resources__CreditDetails
    id: str
    leadCharged: bool
    leadFeedbackSubmitted: bool
    leadStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NEW",
        "ACTIVE",
        "BOOKED",
        "DECLINED",
        "EXPIRED",
        "DISABLED",
        "CONSUMER_DECLINED",
        "WIPED_OUT",
    ]
    leadType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "MESSAGE", "PHONE_CALL", "BOOKING"
    ]
    locale: str
    note: GoogleAdsSearchads360V23Resources__Note
    resourceName: str
    serviceId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocalServicesLeadConversation(
    typing.TypedDict, total=False
):
    conversationChannel: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EMAIL",
        "MESSAGE",
        "PHONE_CALL",
        "SMS",
        "BOOKING",
        "WHATSAPP",
        "ADS_API",
    ]
    eventDateTime: str
    id: str
    lead: str
    messageDetails: GoogleAdsSearchads360V23Resources__MessageDetails
    participantType: typing.Literal["UNSPECIFIED", "UNKNOWN", "ADVERTISER", "CONSUMER"]
    phoneCallDetails: GoogleAdsSearchads360V23Resources__PhoneCallDetails
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocalServicesSettings(
    typing.TypedDict, total=False
):
    granularInsuranceStatuses: _list[
        GoogleAdsSearchads360V23Resources__GranularInsuranceStatus
    ]
    granularLicenseStatuses: _list[
        GoogleAdsSearchads360V23Resources__GranularLicenseStatus
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocalServicesVerificationArtifact(
    typing.TypedDict, total=False
):
    artifactType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "BACKGROUND_CHECK",
        "INSURANCE",
        "LICENSE",
        "BUSINESS_REGISTRATION_CHECK",
    ]
    backgroundCheckVerificationArtifact: (
        GoogleAdsSearchads360V23Resources__BackgroundCheckVerificationArtifact
    )
    businessRegistrationCheckVerificationArtifact: (
        GoogleAdsSearchads360V23Resources__BusinessRegistrationCheckVerificationArtifact
    )
    creationDateTime: str
    id: str
    insuranceVerificationArtifact: (
        GoogleAdsSearchads360V23Resources__InsuranceVerificationArtifact
    )
    licenseVerificationArtifact: (
        GoogleAdsSearchads360V23Resources__LicenseVerificationArtifact
    )
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PASSED",
        "FAILED",
        "PENDING",
        "NO_SUBMISSION",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocationInterestView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__LocationView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ManagedPlacementView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MatchedLocationInterestView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MediaAudio(typing.TypedDict, total=False):
    adDurationMillis: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MediaBundle(typing.TypedDict, total=False):
    data: str
    url: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MediaFile(typing.TypedDict, total=False):
    audio: GoogleAdsSearchads360V23Resources__MediaAudio
    fileSize: str
    id: str
    image: GoogleAdsSearchads360V23Resources__MediaImage
    mediaBundle: GoogleAdsSearchads360V23Resources__MediaBundle
    mimeType: typing.Literal[
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
    name: str
    resourceName: str
    sourceUrl: str
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "IMAGE",
        "ICON",
        "MEDIA_BUNDLE",
        "AUDIO",
        "VIDEO",
        "DYNAMIC_IMAGE",
    ]
    video: GoogleAdsSearchads360V23Resources__MediaVideo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MediaImage(typing.TypedDict, total=False):
    data: str
    fullSizeImageUrl: str
    previewSizeImageUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MediaVideo(typing.TypedDict, total=False):
    adDurationMillis: str
    advertisingIdCode: str
    isciCode: str
    youtubeVideoId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MerchantCenterIdentifier(
    typing.TypedDict, total=False
):
    merchantCenterId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MerchantCenterLinkInvitationIdentifier(
    typing.TypedDict, total=False
):
    merchantCenterId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MessageDetails(typing.TypedDict, total=False):
    attachmentUrls: _list[str]
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MobileAppCategoryConstant(
    typing.TypedDict, total=False
):
    id: int
    name: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__MobileDeviceConstant(
    typing.TypedDict, total=False
):
    id: str
    manufacturerName: str
    name: str
    operatingSystemName: str
    resourceName: str
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "MOBILE", "TABLET"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Note(typing.TypedDict, total=False):
    description: str
    editDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineConversionAlert(
    typing.TypedDict, total=False
):
    error: GoogleAdsSearchads360V23Resources__OfflineConversionError
    errorPercentage: float

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineConversionError(
    typing.TypedDict, total=False
):
    collectionSizeError: typing.Literal["UNSPECIFIED", "UNKNOWN", "TOO_FEW", "TOO_MANY"]
    conversionAdjustmentUploadError: typing.Literal[
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
    conversionUploadError: typing.Literal[
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
    dateError: typing.Literal[
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
    distinctError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "DUPLICATE_ELEMENT", "DUPLICATE_TYPE"
    ]
    fieldError: typing.Literal[
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
    mutateError: typing.Literal[
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
    notAllowlistedError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE"
    ]
    stringFormatError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ILLEGAL_CHARS", "INVALID_FORMAT"
    ]
    stringLengthError: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EMPTY", "TOO_SHORT", "TOO_LONG"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineConversionSummary(
    typing.TypedDict, total=False
):
    failedCount: str
    jobId: str
    pendingCount: str
    successfulCount: str
    uploadDate: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineConversionUploadClientSummary(
    typing.TypedDict, total=False
):
    alerts: _list[GoogleAdsSearchads360V23Resources__OfflineConversionAlert]
    client: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "GOOGLE_ADS_API",
        "GOOGLE_ADS_WEB_CLIENT",
        "ADS_DATA_CONNECTOR",
    ]
    dailySummaries: _list[GoogleAdsSearchads360V23Resources__OfflineConversionSummary]
    jobSummaries: _list[GoogleAdsSearchads360V23Resources__OfflineConversionSummary]
    lastUploadDateTime: str
    pendingEventCount: str
    pendingRate: float
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXCELLENT",
        "GOOD",
        "NEEDS_ATTENTION",
        "NO_RECENT_UPLOAD",
    ]
    successRate: float
    successfulEventCount: str
    totalEventCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineConversionUploadConversionActionSummary(
    typing.TypedDict, total=False
):
    alerts: _list[GoogleAdsSearchads360V23Resources__OfflineConversionAlert]
    client: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "GOOGLE_ADS_API",
        "GOOGLE_ADS_WEB_CLIENT",
        "ADS_DATA_CONNECTOR",
    ]
    conversionActionId: str
    conversionActionName: str
    dailySummaries: _list[GoogleAdsSearchads360V23Resources__OfflineConversionSummary]
    jobSummaries: _list[GoogleAdsSearchads360V23Resources__OfflineConversionSummary]
    lastUploadDateTime: str
    pendingEventCount: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "EXCELLENT",
        "GOOD",
        "NEEDS_ATTENTION",
        "NO_RECENT_UPLOAD",
    ]
    successfulEventCount: str
    totalEventCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineUserDataJob(
    typing.TypedDict, total=False
):
    customerMatchUserListMetadata: (
        GoogleAdsSearchads360V23Common__CustomerMatchUserListMetadata
    )
    externalId: str
    failureReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "INSUFFICIENT_MATCHED_TRANSACTIONS",
        "INSUFFICIENT_TRANSACTIONS",
        "HIGH_AVERAGE_TRANSACTION_VALUE",
        "LOW_AVERAGE_TRANSACTION_VALUE",
        "NEWLY_OBSERVED_CURRENCY_CODE",
    ]
    id: str
    operationMetadata: GoogleAdsSearchads360V23Resources__OfflineUserDataJobMetadata
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PENDING", "RUNNING", "SUCCESS", "FAILED"
    ]
    storeSalesMetadata: GoogleAdsSearchads360V23Common__StoreSalesMetadata
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "STORE_SALES_UPLOAD_FIRST_PARTY",
        "STORE_SALES_UPLOAD_THIRD_PARTY",
        "CUSTOMER_MATCH_USER_LIST",
        "CUSTOMER_MATCH_WITH_ATTRIBUTES",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__OfflineUserDataJobMetadata(
    typing.TypedDict, total=False
):
    matchRateRange: typing.Literal[
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
class GoogleAdsSearchads360V23Resources__OperatingSystemVersionConstant(
    typing.TypedDict, total=False
):
    id: str
    name: str
    operatorType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EQUALS_TO", "GREATER_THAN_EQUALS_TO"
    ]
    osMajorVersion: int
    osMinorVersion: int
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__PaidOrganicSearchTermView(
    typing.TypedDict, total=False
):
    resourceName: str
    searchTerm: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ParentalStatusView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__PaymentsAccount(typing.TypedDict, total=False):
    currencyCode: str
    name: str
    payingManagerCustomer: str
    paymentsAccountId: str
    paymentsProfileId: str
    resourceName: str
    secondaryPaymentsProfileId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__PerStoreView(typing.TypedDict, total=False):
    address1: str
    address2: str
    businessName: str
    city: str
    countryCode: str
    phoneNumber: str
    placeId: str
    postalCode: str
    province: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__PerformanceMaxPlacementView(
    typing.TypedDict, total=False
):
    displayName: str
    placement: str
    placementType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "WEBSITE",
        "MOBILE_APP_CATEGORY",
        "MOBILE_APPLICATION",
        "YOUTUBE_VIDEO",
        "YOUTUBE_CHANNEL",
        "GOOGLE_PRODUCTS",
    ]
    resourceName: str
    targetUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__PhoneCallDetails(
    typing.TypedDict, total=False
):
    callDurationMillis: str
    callRecordingUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ProductCategoryConstant(
    typing.TypedDict, total=False
):
    categoryId: str
    level: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"
    ]
    localizations: _list[
        GoogleAdsSearchads360V23Resources_ProductCategoryConstant_ProductCategoryLocalization
    ]
    productCategoryConstantParent: str
    resourceName: str
    state: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "OBSOLETE"]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ProductGroupView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ProductLink(typing.TypedDict, total=False):
    advertisingPartner: GoogleAdsSearchads360V23Resources__AdvertisingPartnerIdentifier
    dataPartner: GoogleAdsSearchads360V23Resources__DataPartnerIdentifier
    googleAds: GoogleAdsSearchads360V23Resources__GoogleAdsIdentifier
    merchantCenter: GoogleAdsSearchads360V23Resources__MerchantCenterIdentifier
    productLinkId: str
    resourceName: str
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DATA_PARTNER",
        "GOOGLE_ADS",
        "HOTEL_CENTER",
        "MERCHANT_CENTER",
        "ADVERTISING_PARTNER",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ProductLinkInvitation(
    typing.TypedDict, total=False
):
    advertisingPartner: (
        GoogleAdsSearchads360V23Resources__AdvertisingPartnerLinkInvitationIdentifier
    )
    hotelCenter: GoogleAdsSearchads360V23Resources__HotelCenterLinkInvitationIdentifier
    merchantCenter: (
        GoogleAdsSearchads360V23Resources__MerchantCenterLinkInvitationIdentifier
    )
    productLinkInvitationId: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ACCEPTED",
        "REQUESTED",
        "PENDING_APPROVAL",
        "REVOKED",
        "REJECTED",
        "EXPIRED",
    ]
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "DATA_PARTNER",
        "GOOGLE_ADS",
        "HOTEL_CENTER",
        "MERCHANT_CENTER",
        "ADVERTISING_PARTNER",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__QualifyingQuestion(
    typing.TypedDict, total=False
):
    locale: str
    qualifyingQuestionId: str
    resourceName: str
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Recommendation(typing.TypedDict, total=False):
    adGroup: str
    callAssetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_CallAssetRecommendation
    )
    calloutAssetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_CalloutAssetRecommendation
    )
    campaign: str
    campaignBudget: str
    campaignBudgetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudgetRecommendation
    )
    campaigns: _list[str]
    customAudienceOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_CustomAudienceOptInRecommendation
    dismissed: bool
    displayExpansionOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_DisplayExpansionOptInRecommendation
    dynamicImageExtensionOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_DynamicImageExtensionOptInRecommendation
    enhancedCpcOptInRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_EnhancedCpcOptInRecommendation
    )
    forecastingCampaignBudgetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudgetRecommendation
    )
    forecastingSetTargetCpaRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ForecastingSetTargetCpaRecommendation
    forecastingSetTargetRoasRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ForecastingSetTargetRoasRecommendation
    impact: GoogleAdsSearchads360V23Resources_Recommendation_RecommendationImpact
    improveDemandGenAdStrengthRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ImproveDemandGenAdStrengthRecommendation
    improveGoogleTagCoverageRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ImproveGoogleTagCoverageRecommendation
    improvePerformanceMaxAdStrengthRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ImprovePerformanceMaxAdStrengthRecommendation
    keywordMatchTypeRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_KeywordMatchTypeRecommendation
    )
    keywordRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_KeywordRecommendation
    )
    leadFormAssetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_LeadFormAssetRecommendation
    )
    lowerTargetRoasRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_LowerTargetRoasRecommendation
    )
    marginalRoiCampaignBudgetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_CampaignBudgetRecommendation
    )
    maximizeClicksOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_MaximizeClicksOptInRecommendation
    maximizeConversionValueOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_MaximizeConversionValueOptInRecommendation
    maximizeConversionsOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_MaximizeConversionsOptInRecommendation
    migrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_MigrateDynamicSearchAdsCampaignToPerformanceMaxRecommendation
    moveUnusedBudgetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_MoveUnusedBudgetRecommendation
    )
    optimizeAdRotationRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_OptimizeAdRotationRecommendation
    performanceMaxFinalUrlOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_PerformanceMaxFinalUrlOptInRecommendation
    performanceMaxOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_PerformanceMaxOptInRecommendation
    raiseTargetCpaBidTooLowRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_RaiseTargetCpaBidTooLowRecommendation
    raiseTargetCpaRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_RaiseTargetCpaRecommendation
    )
    refreshCustomerMatchListRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_RefreshCustomerMatchListRecommendation
    resourceName: str
    responsiveSearchAdAssetRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ResponsiveSearchAdAssetRecommendation
    responsiveSearchAdImproveAdStrengthRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ResponsiveSearchAdImproveAdStrengthRecommendation
    responsiveSearchAdRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ResponsiveSearchAdRecommendation
    searchPartnersOptInRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_SearchPartnersOptInRecommendation
    setTargetCpaRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ForecastingSetTargetCpaRecommendation
    setTargetRoasRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ForecastingSetTargetRoasRecommendation
    shoppingAddAgeGroupRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation
    shoppingAddColorRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation
    shoppingAddGenderRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation
    shoppingAddGtinRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation
    shoppingAddMoreIdentifiersRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation
    shoppingAddProductsToCampaignRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingAddProductsToCampaignRecommendation
    shoppingAddSizeRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingOfferAttributeRecommendation
    shoppingFixDisapprovedProductsRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingFixDisapprovedProductsRecommendation
    shoppingFixMerchantCenterAccountSuspensionWarningRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingMerchantCenterAccountSuspensionRecommendation
    shoppingFixSuspendedMerchantCenterAccountRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingMerchantCenterAccountSuspensionRecommendation
    shoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingMigrateRegularShoppingCampaignOffersToPerformanceMaxRecommendation
    shoppingTargetAllOffersRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_ShoppingTargetAllOffersRecommendation
    sitelinkAssetRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_SitelinkAssetRecommendation
    )
    targetCpaOptInRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_TargetCpaOptInRecommendation
    )
    targetRoasOptInRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_TargetRoasOptInRecommendation
    )
    textAdRecommendation: (
        GoogleAdsSearchads360V23Resources_Recommendation_TextAdRecommendation
    )
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BUDGET",
        "KEYWORD",
        "TEXT_AD",
        "TARGET_CPA_OPT_IN",
        "MAXIMIZE_CONVERSIONS_OPT_IN",
        "ENHANCED_CPC_OPT_IN",
        "SEARCH_PARTNERS_OPT_IN",
        "MAXIMIZE_CLICKS_OPT_IN",
        "OPTIMIZE_AD_ROTATION",
        "KEYWORD_MATCH_TYPE",
        "MOVE_UNUSED_BUDGET",
        "FORECASTING_CAMPAIGN_BUDGET",
        "TARGET_ROAS_OPT_IN",
        "RESPONSIVE_SEARCH_AD",
        "MARGINAL_ROI_CAMPAIGN_BUDGET",
        "USE_BROAD_MATCH_KEYWORD",
        "RESPONSIVE_SEARCH_AD_ASSET",
        "UPGRADE_SMART_SHOPPING_CAMPAIGN_TO_PERFORMANCE_MAX",
        "RESPONSIVE_SEARCH_AD_IMPROVE_AD_STRENGTH",
        "DISPLAY_EXPANSION_OPT_IN",
        "UPGRADE_LOCAL_CAMPAIGN_TO_PERFORMANCE_MAX",
        "RAISE_TARGET_CPA_BID_TOO_LOW",
        "FORECASTING_SET_TARGET_ROAS",
        "CALLOUT_ASSET",
        "SITELINK_ASSET",
        "CALL_ASSET",
        "SHOPPING_ADD_AGE_GROUP",
        "SHOPPING_ADD_COLOR",
        "SHOPPING_ADD_GENDER",
        "SHOPPING_ADD_GTIN",
        "SHOPPING_ADD_MORE_IDENTIFIERS",
        "SHOPPING_ADD_SIZE",
        "SHOPPING_ADD_PRODUCTS_TO_CAMPAIGN",
        "SHOPPING_FIX_DISAPPROVED_PRODUCTS",
        "SHOPPING_TARGET_ALL_OFFERS",
        "SHOPPING_FIX_SUSPENDED_MERCHANT_CENTER_ACCOUNT",
        "SHOPPING_FIX_MERCHANT_CENTER_ACCOUNT_SUSPENSION_WARNING",
        "SHOPPING_MIGRATE_REGULAR_SHOPPING_CAMPAIGN_OFFERS_TO_PERFORMANCE_MAX",
        "DYNAMIC_IMAGE_EXTENSION_OPT_IN",
        "RAISE_TARGET_CPA",
        "LOWER_TARGET_ROAS",
        "PERFORMANCE_MAX_OPT_IN",
        "IMPROVE_PERFORMANCE_MAX_AD_STRENGTH",
        "MIGRATE_DYNAMIC_SEARCH_ADS_CAMPAIGN_TO_PERFORMANCE_MAX",
        "FORECASTING_SET_TARGET_CPA",
        "SET_TARGET_CPA",
        "SET_TARGET_ROAS",
        "MAXIMIZE_CONVERSION_VALUE_OPT_IN",
        "IMPROVE_GOOGLE_TAG_COVERAGE",
        "PERFORMANCE_MAX_FINAL_URL_OPT_IN",
        "REFRESH_CUSTOMER_MATCH_LIST",
        "CUSTOM_AUDIENCE_OPT_IN",
        "LEAD_FORM_ASSET",
        "IMPROVE_DEMAND_GEN_AD_STRENGTH",
    ]
    upgradeLocalCampaignToPerformanceMaxRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_UpgradeLocalCampaignToPerformanceMaxRecommendation
    upgradeSmartShoppingCampaignToPerformanceMaxRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_UpgradeSmartShoppingCampaignToPerformanceMaxRecommendation
    useBroadMatchKeywordRecommendation: GoogleAdsSearchads360V23Resources_Recommendation_UseBroadMatchKeywordRecommendation

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__RecommendationSubscription(
    typing.TypedDict, total=False
):
    createDateTime: str
    modifyDateTime: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "PAUSED"]
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CAMPAIGN_BUDGET",
        "KEYWORD",
        "TEXT_AD",
        "TARGET_CPA_OPT_IN",
        "MAXIMIZE_CONVERSIONS_OPT_IN",
        "ENHANCED_CPC_OPT_IN",
        "SEARCH_PARTNERS_OPT_IN",
        "MAXIMIZE_CLICKS_OPT_IN",
        "OPTIMIZE_AD_ROTATION",
        "KEYWORD_MATCH_TYPE",
        "MOVE_UNUSED_BUDGET",
        "FORECASTING_CAMPAIGN_BUDGET",
        "TARGET_ROAS_OPT_IN",
        "RESPONSIVE_SEARCH_AD",
        "MARGINAL_ROI_CAMPAIGN_BUDGET",
        "USE_BROAD_MATCH_KEYWORD",
        "RESPONSIVE_SEARCH_AD_ASSET",
        "UPGRADE_SMART_SHOPPING_CAMPAIGN_TO_PERFORMANCE_MAX",
        "RESPONSIVE_SEARCH_AD_IMPROVE_AD_STRENGTH",
        "DISPLAY_EXPANSION_OPT_IN",
        "UPGRADE_LOCAL_CAMPAIGN_TO_PERFORMANCE_MAX",
        "RAISE_TARGET_CPA_BID_TOO_LOW",
        "FORECASTING_SET_TARGET_ROAS",
        "CALLOUT_ASSET",
        "SITELINK_ASSET",
        "CALL_ASSET",
        "SHOPPING_ADD_AGE_GROUP",
        "SHOPPING_ADD_COLOR",
        "SHOPPING_ADD_GENDER",
        "SHOPPING_ADD_GTIN",
        "SHOPPING_ADD_MORE_IDENTIFIERS",
        "SHOPPING_ADD_SIZE",
        "SHOPPING_ADD_PRODUCTS_TO_CAMPAIGN",
        "SHOPPING_FIX_DISAPPROVED_PRODUCTS",
        "SHOPPING_TARGET_ALL_OFFERS",
        "SHOPPING_FIX_SUSPENDED_MERCHANT_CENTER_ACCOUNT",
        "SHOPPING_FIX_MERCHANT_CENTER_ACCOUNT_SUSPENSION_WARNING",
        "SHOPPING_MIGRATE_REGULAR_SHOPPING_CAMPAIGN_OFFERS_TO_PERFORMANCE_MAX",
        "DYNAMIC_IMAGE_EXTENSION_OPT_IN",
        "RAISE_TARGET_CPA",
        "LOWER_TARGET_ROAS",
        "PERFORMANCE_MAX_OPT_IN",
        "IMPROVE_PERFORMANCE_MAX_AD_STRENGTH",
        "MIGRATE_DYNAMIC_SEARCH_ADS_CAMPAIGN_TO_PERFORMANCE_MAX",
        "FORECASTING_SET_TARGET_CPA",
        "SET_TARGET_CPA",
        "SET_TARGET_ROAS",
        "MAXIMIZE_CONVERSION_VALUE_OPT_IN",
        "IMPROVE_GOOGLE_TAG_COVERAGE",
        "PERFORMANCE_MAX_FINAL_URL_OPT_IN",
        "REFRESH_CUSTOMER_MATCH_LIST",
        "CUSTOM_AUDIENCE_OPT_IN",
        "LEAD_FORM_ASSET",
        "IMPROVE_DEMAND_GEN_AD_STRENGTH",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__RemarketingAction(
    typing.TypedDict, total=False
):
    id: str
    name: str
    resourceName: str
    tagSnippets: _list[GoogleAdsSearchads360V23Common__TagSnippet]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__RemarketingSetting(
    typing.TypedDict, total=False
):
    googleGlobalSiteTag: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Residency(typing.TypedDict, total=False):
    completionYear: int
    institutionName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SearchAds360Campaign(
    typing.TypedDict, total=False
):
    productAttributionFilterType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "INHERIT", "MANUAL", "AUTO_BRAND"
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SearchAds360Field(
    typing.TypedDict, total=False
):
    attributeResources: _list[str]
    category: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "RESOURCE", "ATTRIBUTE", "SEGMENT", "METRIC"
    ]
    dataType: typing.Literal[
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
class GoogleAdsSearchads360V23Resources__SearchTermView(typing.TypedDict, total=False):
    adGroup: str
    resourceName: str
    searchTerm: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADDED", "EXCLUDED", "ADDED_EXCLUDED", "NONE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SharedCriterion(typing.TypedDict, total=False):
    brand: GoogleAdsSearchads360V23Common__BrandInfo
    criterionId: str
    keyword: GoogleAdsSearchads360V23Common__KeywordInfo
    mobileAppCategory: GoogleAdsSearchads360V23Common__MobileAppCategoryInfo
    mobileApplication: GoogleAdsSearchads360V23Common__MobileApplicationInfo
    negative: bool
    placement: GoogleAdsSearchads360V23Common__PlacementInfo
    resourceName: str
    sharedSet: str
    type: typing.Literal[
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
        "NEGATIVE_KEYWORD_LIST",
        "LOCAL_SERVICE_ID",
        "SEARCH_THEME",
        "BRAND",
        "BRAND_LIST",
        "LIFE_EVENT",
        "WEBPAGE_LIST",
        "VIDEO_LINEUP",
        "PLACEMENT_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST",
        "VERTICAL_ADS_ITEM_GROUP_RULE",
    ]
    verticalAdsItemGroupRule: (
        GoogleAdsSearchads360V23Common__VerticalAdsItemGroupRuleInfo
    )
    webpage: GoogleAdsSearchads360V23Common__WebpageInfo
    youtubeChannel: GoogleAdsSearchads360V23Common__YouTubeChannelInfo
    youtubeVideo: GoogleAdsSearchads360V23Common__YouTubeVideoInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SharedSet(typing.TypedDict, total=False):
    id: str
    memberCount: str
    name: str
    referenceCount: str
    resourceName: str
    status: typing.Literal["UNSPECIFIED", "UNKNOWN", "ENABLED", "REMOVED"]
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NEGATIVE_KEYWORDS",
        "NEGATIVE_PLACEMENTS",
        "ACCOUNT_LEVEL_NEGATIVE_KEYWORDS",
        "BRANDS",
        "WEBPAGES",
        "VERTICAL_ADS_ITEM_GROUP_RULE_LIST",
    ]
    verticalAdsItemVerticalType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "HOTELS",
        "VACATION_RENTALS",
        "RENTAL_CARS",
        "EVENTS",
        "THINGS_TO_DO",
        "FLIGHTS",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ShoppingPerformanceView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ShoppingProduct(typing.TypedDict, total=False):
    adGroup: str
    availability: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "IN_STOCK", "OUT_OF_STOCK", "PREORDER"
    ]
    brand: str
    campaign: str
    categoryLevel1: str
    categoryLevel2: str
    categoryLevel3: str
    categoryLevel4: str
    categoryLevel5: str
    channel: typing.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]
    channelExclusivity: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SINGLE_CHANNEL", "MULTI_CHANNEL"
    ]
    condition: typing.Literal["UNSPECIFIED", "UNKNOWN", "NEW", "REFURBISHED", "USED"]
    currencyCode: str
    customAttribute0: str
    customAttribute1: str
    customAttribute2: str
    customAttribute3: str
    customAttribute4: str
    effectiveMaxCpcMicros: str
    feedLabel: str
    issues: _list[GoogleAdsSearchads360V23Resources_ShoppingProduct_ProductIssue]
    itemId: str
    languageCode: str
    merchantCenterId: str
    multiClientAccountId: str
    priceMicros: str
    productImageUri: str
    productTypeLevel1: str
    productTypeLevel2: str
    productTypeLevel3: str
    productTypeLevel4: str
    productTypeLevel5: str
    resourceName: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "NOT_ELIGIBLE", "ELIGIBLE_LIMITED", "ELIGIBLE"
    ]
    targetCountries: _list[str]
    title: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SmartCampaignSearchTermView(
    typing.TypedDict, total=False
):
    campaign: str
    resourceName: str
    searchTerm: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SmartCampaignSetting(
    typing.TypedDict, total=False
):
    adOptimizedBusinessProfileSetting: GoogleAdsSearchads360V23Resources_SmartCampaignSetting_AdOptimizedBusinessProfileSetting
    advertisingLanguageCode: str
    businessName: str
    businessProfileLocation: str
    campaign: str
    finalUrl: str
    phoneNumber: GoogleAdsSearchads360V23Resources_SmartCampaignSetting_PhoneNumber
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__TargetingExpansionView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ThirdPartyAppAnalyticsLink(
    typing.TypedDict, total=False
):
    resourceName: str
    shareableLinkId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__ThirdPartyAppAnalyticsLinkIdentifier(
    typing.TypedDict, total=False
):
    appAnalyticsProviderId: str
    appId: str
    appVendor: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_APP_STORE"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__TopicConstant(typing.TypedDict, total=False):
    id: str
    path: _list[str]
    resourceName: str
    topicConstantParent: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__TopicView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__TravelActivityGroupView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__TravelActivityPerformanceView(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__UniversityDegree(
    typing.TypedDict, total=False
):
    degree: str
    graduationYear: int
    institutionName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__UserInterest(typing.TypedDict, total=False):
    availabilities: _list[GoogleAdsSearchads360V23Common__CriterionCategoryAvailability]
    launchedToAll: bool
    name: str
    resourceName: str
    taxonomyType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AFFINITY",
        "IN_MARKET",
        "MOBILE_APP_INSTALL_USER",
        "VERTICAL_GEO",
        "NEW_SMART_PHONE_USER",
    ]
    userInterestId: str
    userInterestParent: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__UserList(typing.TypedDict, total=False):
    accessReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OWNED",
        "SHARED",
        "LICENSED",
        "SUBSCRIBED",
        "AFFILIATED",
    ]
    accountUserListStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ENABLED", "DISABLED"
    ]
    basicUserList: GoogleAdsSearchads360V23Common__BasicUserListInfo
    closingReason: typing.Literal["UNSPECIFIED", "UNKNOWN", "UNUSED"]
    crmBasedUserList: GoogleAdsSearchads360V23Common__CrmBasedUserListInfo
    description: str
    eligibleForDisplay: bool
    eligibleForSearch: bool
    id: str
    integrationCode: str
    logicalUserList: GoogleAdsSearchads360V23Common__LogicalUserListInfo
    lookalikeUserList: GoogleAdsSearchads360V23Common__LookalikeUserListInfo
    matchRatePercentage: int
    membershipLifeSpan: str
    membershipStatus: typing.Literal["UNSPECIFIED", "UNKNOWN", "OPEN", "CLOSED"]
    name: str
    readOnly: bool
    resourceName: str
    ruleBasedUserList: GoogleAdsSearchads360V23Common__RuleBasedUserListInfo
    similarUserList: GoogleAdsSearchads360V23Common__SimilarUserListInfo
    sizeForDisplay: str
    sizeForSearch: str
    sizeRangeForDisplay: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "LESS_THAN_FIVE_HUNDRED",
        "LESS_THAN_ONE_THOUSAND",
        "ONE_THOUSAND_TO_TEN_THOUSAND",
        "TEN_THOUSAND_TO_FIFTY_THOUSAND",
        "FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND",
        "ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND",
        "THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND",
        "FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION",
        "ONE_MILLION_TO_TWO_MILLION",
        "TWO_MILLION_TO_THREE_MILLION",
        "THREE_MILLION_TO_FIVE_MILLION",
        "FIVE_MILLION_TO_TEN_MILLION",
        "TEN_MILLION_TO_TWENTY_MILLION",
        "TWENTY_MILLION_TO_THIRTY_MILLION",
        "THIRTY_MILLION_TO_FIFTY_MILLION",
        "OVER_FIFTY_MILLION",
    ]
    sizeRangeForSearch: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "LESS_THAN_FIVE_HUNDRED",
        "LESS_THAN_ONE_THOUSAND",
        "ONE_THOUSAND_TO_TEN_THOUSAND",
        "TEN_THOUSAND_TO_FIFTY_THOUSAND",
        "FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND",
        "ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND",
        "THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND",
        "FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION",
        "ONE_MILLION_TO_TWO_MILLION",
        "TWO_MILLION_TO_THREE_MILLION",
        "THREE_MILLION_TO_FIVE_MILLION",
        "FIVE_MILLION_TO_TEN_MILLION",
        "TEN_MILLION_TO_TWENTY_MILLION",
        "TWENTY_MILLION_TO_THIRTY_MILLION",
        "THIRTY_MILLION_TO_FIFTY_MILLION",
        "OVER_FIFTY_MILLION",
    ]
    type: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REMARKETING",
        "LOGICAL",
        "EXTERNAL_REMARKETING",
        "RULE_BASED",
        "SIMILAR",
        "CRM_BASED",
        "LOOKALIKE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__UserListCustomerType(
    typing.TypedDict, total=False
):
    customerTypeCategory: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ALL_CUSTOMERS",
        "PURCHASERS",
        "HIGH_VALUE_CUSTOMERS",
        "DISENGAGED_CUSTOMERS",
        "QUALIFIED_LEADS",
        "CONVERTED_LEADS",
        "PAID_SUBSCRIBERS",
        "LOYALTY_SIGN_UPS",
        "CART_ABANDONERS",
        "LOYALTY_TIER_1_MEMBERS",
        "LOYALTY_TIER_2_MEMBERS",
        "LOYALTY_TIER_3_MEMBERS",
        "LOYALTY_TIER_4_MEMBERS",
        "LOYALTY_TIER_5_MEMBERS",
        "LOYALTY_TIER_6_MEMBERS",
        "LOYALTY_TIER_7_MEMBERS",
    ]
    resourceName: str
    userList: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__UserLocationView(
    typing.TypedDict, total=False
):
    countryCriterionId: str
    resourceName: str
    targetingLocation: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Video(typing.TypedDict, total=False):
    channelId: str
    durationMillis: str
    id: str
    resourceName: str
    title: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__VideoCustomer(typing.TypedDict, total=False):
    thirdPartyIntegrationPartners: (
        GoogleAdsSearchads360V23Common__CustomerThirdPartyIntegrationPartners
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__Visit(typing.TypedDict, total=False):
    adId: str
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    assetId: str
    clickId: str
    criterionId: str
    id: str
    merchantId: str
    productChannel: typing.Literal["UNSPECIFIED", "UNKNOWN", "ONLINE", "LOCAL"]
    productCountryCode: str
    productId: str
    productLanguageCode: str
    productStoreId: str
    resourceName: str
    visitDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__WebpageView(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__YoutubeVideoIdentifier(
    typing.TypedDict, total=False
):
    channelId: str
    videoId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_AdAssetApplyParameters(
    typing.TypedDict, total=False
):
    existingAssets: _list[str]
    newAssets: _list[GoogleAdsSearchads360V23Resources__Asset]
    scope: typing.Literal["UNSPECIFIED", "UNKNOWN", "CUSTOMER", "CAMPAIGN"]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CallAssetParameters(
    typing.TypedDict, total=False
):
    adAssetApplyParameters: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_AdAssetApplyParameters

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CallExtensionParameters(
    typing.TypedDict, total=False
):
    callExtensions: _list[GoogleAdsSearchads360V23Common__CallFeedItem]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CalloutAssetParameters(
    typing.TypedDict, total=False
):
    adAssetApplyParameters: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_AdAssetApplyParameters

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CalloutExtensionParameters(
    typing.TypedDict, total=False
):
    calloutExtensions: _list[GoogleAdsSearchads360V23Common__CalloutFeedItem]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CampaignBudgetParameters(
    typing.TypedDict, total=False
):
    newBudgetAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ForecastingSetTargetCpaParameters(
    typing.TypedDict, total=False
):
    campaignBudgetAmountMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ForecastingSetTargetRoasParameters(
    typing.TypedDict, total=False
):
    campaignBudgetAmountMicros: str
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_KeywordParameters(
    typing.TypedDict, total=False
):
    adGroup: str
    cpcBidMicros: str
    matchType: typing.Literal["UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_LeadFormAssetParameters(
    typing.TypedDict, total=False
):
    adAssetApplyParameters: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_AdAssetApplyParameters
    setSubmitLeadFormAssetCampaignGoal: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_LowerTargetRoasParameters(
    typing.TypedDict, total=False
):
    targetRoasMultiplier: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_MoveUnusedBudgetParameters(
    typing.TypedDict, total=False
):
    budgetMicrosToMove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_RaiseTargetCpaBidTooLowParameters(
    typing.TypedDict, total=False
):
    targetMultiplier: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_RaiseTargetCpaParameters(
    typing.TypedDict, total=False
):
    targetCpaMultiplier: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ResponsiveSearchAdAssetParameters(
    typing.TypedDict, total=False
):
    updatedAd: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ResponsiveSearchAdImproveAdStrengthParameters(
    typing.TypedDict, total=False
):
    updatedAd: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ResponsiveSearchAdParameters(
    typing.TypedDict, total=False
):
    ad: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_SitelinkAssetParameters(
    typing.TypedDict, total=False
):
    adAssetApplyParameters: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_AdAssetApplyParameters

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_SitelinkExtensionParameters(
    typing.TypedDict, total=False
):
    sitelinkExtensions: _list[GoogleAdsSearchads360V23Common__SitelinkFeedItem]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_TargetCpaOptInParameters(
    typing.TypedDict, total=False
):
    newCampaignBudgetAmountMicros: str
    targetCpaMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_TargetRoasOptInParameters(
    typing.TypedDict, total=False
):
    newCampaignBudgetAmountMicros: str
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_TextAdParameters(
    typing.TypedDict, total=False
):
    ad: GoogleAdsSearchads360V23Resources__Ad

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_UseBroadMatchKeywordParameters(
    typing.TypedDict, total=False
):
    newBudgetAmountMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_CampaignToForecast_CampaignBiddingStrategy(
    typing.TypedDict, total=False
):
    manualCpcBiddingStrategy: GoogleAdsSearchads360V23Services__ManualCpcBiddingStrategy
    maximizeClicksBiddingStrategy: (
        GoogleAdsSearchads360V23Services__MaximizeClicksBiddingStrategy
    )
    maximizeConversionsBiddingStrategy: (
        GoogleAdsSearchads360V23Services__MaximizeConversionsBiddingStrategy
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Services_CartData_Item(typing.TypedDict, total=False):
    productId: str
    quantity: int
    unitPrice: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_DismissRecommendationRequest_DismissRecommendationOperation(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_DismissRecommendationResponse_DismissRecommendationResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_AdGroupInfo(
    typing.TypedDict, total=False
):
    adGroupType: typing.Literal[
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
        "SEARCH_DYNAMIC_ADS",
        "SHOPPING_COMPARISON_LISTING_ADS",
        "PROMOTED_HOTEL_ADS",
        "VIDEO_RESPONSIVE",
        "VIDEO_EFFICIENT_REACH",
        "SMART_CAMPAIGN_ADS",
        "TRAVEL_ADS",
    ]
    keywords: _list[GoogleAdsSearchads360V23Common__KeywordInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_AssetGroupInfo(
    typing.TypedDict, total=False
):
    description: _list[str]
    finalUrl: str
    headline: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_BiddingInfo(
    typing.TypedDict, total=False
):
    biddingStrategyType: typing.Literal[
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
        "TARGET_CPC",
        "TARGET_CPM",
        "TARGET_IMPRESSION_SHARE",
        "TARGET_OUTRANK_SHARE",
        "TARGET_ROAS",
        "TARGET_SPEND",
    ]
    targetCpaMicros: str
    targetImpressionShareInfo: GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_TargetImpressionShareInfo
    targetRoas: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_BudgetInfo(
    typing.TypedDict, total=False
):
    currentBudget: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_SeedInfo(
    typing.TypedDict, total=False
):
    keywordSeeds: _list[str]
    urlSeed: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_TargetImpressionShareInfo(
    typing.TypedDict, total=False
):
    location: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ANYWHERE_ON_PAGE",
        "TOP_OF_PAGE",
        "ABSOLUTE_TOP_OF_PAGE",
    ]
    maxCpcBidCeiling: str
    targetImpressionShareMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_IncentiveRequirement_Spend(
    typing.TypedDict, total=False
):
    awardAmount: GoogleType__Money
    requiredAmount: GoogleType__Money

@typing.type_check_only
class GoogleAdsSearchads360V23Services_Incentive_Requirement(
    typing.TypedDict, total=False
):
    spend: GoogleAdsSearchads360V23Services_IncentiveRequirement_Spend

@typing.type_check_only
class GoogleAdsSearchads360V23Services_MetricAttributes_Attribute(
    typing.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ProductFilter_MarketingObjectiveList(
    typing.TypedDict, total=False
):
    marketingObjectives: _list[
        typing.Literal["UNSPECIFIED", "UNKNOWN", "AWARENESS", "CONSIDERATION", "ACTION"]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_ProductFilter_ProductList(
    typing.TypedDict, total=False
):
    productCodes: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SmartCampaignSuggestionInfo_BusinessContext(
    typing.TypedDict, total=False
):
    businessName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SmartCampaignSuggestionInfo_LocationList(
    typing.TypedDict, total=False
):
    locations: _list[GoogleAdsSearchads360V23Common__LocationInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SuggestGeoTargetConstantsRequest_GeoTargets(
    typing.TypedDict, total=False
):
    geoTargetConstants: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SuggestGeoTargetConstantsRequest_LocationNames(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SuggestKeywordThemesResponse_KeywordTheme(
    typing.TypedDict, total=False
):
    freeFormKeywordTheme: str
    keywordThemeConstant: GoogleAdsSearchads360V23Resources__KeywordThemeConstant

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SuggestSmartCampaignBudgetOptionsResponse_BudgetOption(
    typing.TypedDict, total=False
):
    dailyAmountMicros: str
    metrics: GoogleAdsSearchads360V23Services_SuggestSmartCampaignBudgetOptionsResponse_Metrics

@typing.type_check_only
class GoogleAdsSearchads360V23Services_SuggestSmartCampaignBudgetOptionsResponse_Metrics(
    typing.TypedDict, total=False
):
    maxDailyClicks: str
    minDailyClicks: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AccountBudgetProposalOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AccountBudgetProposal
    remove: str
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AccountLinkOperation(
    typing.TypedDict, total=False
):
    remove: str
    update: GoogleAdsSearchads360V23Resources__AccountLink
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupAdLabelOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupAdLabel
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupAdOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupAd
    policyValidationParameter: GoogleAdsSearchads360V23Common__PolicyValidationParameter
    remove: str
    update: GoogleAdsSearchads360V23Resources__AdGroupAd
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupAssetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupAsset
    remove: str
    update: GoogleAdsSearchads360V23Resources__AdGroupAsset
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupAssetSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupAssetSet
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupBidModifierOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupBidModifier
    remove: str
    update: GoogleAdsSearchads360V23Resources__AdGroupBidModifier
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupCriterionCustomizerOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupCriterionCustomizer
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupCriterionLabelOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupCriterionLabel
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupCriterionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupCriterion
    exemptPolicyViolationKeys: _list[GoogleAdsSearchads360V23Common__PolicyViolationKey]
    remove: str
    update: GoogleAdsSearchads360V23Resources__AdGroupCriterion
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupCustomizerOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupCustomizer
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupKeywordSuggestion(
    typing.TypedDict, total=False
):
    keywordText: str
    suggestedAdGroup: str
    suggestedCampaign: str
    suggestedKeywordText: str
    suggestedMatchType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "EXACT", "PHRASE", "BROAD"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupLabelOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdGroupLabel
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdGroupOperation(typing.TypedDict, total=False):
    create: GoogleAdsSearchads360V23Resources__AdGroup
    remove: str
    update: GoogleAdsSearchads360V23Resources__AdGroup
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdOperation(typing.TypedDict, total=False):
    policyValidationParameter: GoogleAdsSearchads360V23Common__PolicyValidationParameter
    update: GoogleAdsSearchads360V23Resources__Ad
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdParameterOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AdParameter
    remove: str
    update: GoogleAdsSearchads360V23Resources__AdParameter
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AddBatchJobOperationsRequest(
    typing.TypedDict, total=False
):
    mutateOperations: _list[GoogleAdsSearchads360V23Services__MutateOperation]
    sequenceToken: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AddBatchJobOperationsResponse(
    typing.TypedDict, total=False
):
    nextSequenceToken: str
    totalOperations: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AddOfflineUserDataJobOperationsRequest(
    typing.TypedDict, total=False
):
    enablePartialFailure: bool
    enableWarnings: bool
    operations: _list[GoogleAdsSearchads360V23Services__OfflineUserDataJobOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AddOfflineUserDataJobOperationsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    warning: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AdvancedProductTargeting(
    typing.TypedDict, total=False
):
    surfaceTargetingSettings: GoogleAdsSearchads360V23Services__SurfaceTargeting
    targetFrequencySettings: GoogleAdsSearchads360V23Services__TargetFrequencySettings
    youtubeSelectSettings: GoogleAdsSearchads360V23Services__YouTubeSelectSettings

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AppendLeadConversationRequest(
    typing.TypedDict, total=False
):
    conversations: _list[GoogleAdsSearchads360V23Services__Conversation]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AppendLeadConversationResponse(
    typing.TypedDict, total=False
):
    responses: _list[GoogleAdsSearchads360V23Services__ConversationOrError]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyIncentiveRequest(
    typing.TypedDict, total=False
):
    countryCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyIncentiveResponse(
    typing.TypedDict, total=False
):
    couponCode: str
    creationTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyRecommendationOperation(
    typing.TypedDict, total=False
):
    callAsset: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CallAssetParameters
    callExtension: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CallExtensionParameters
    calloutAsset: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CalloutAssetParameters
    calloutExtension: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CalloutExtensionParameters
    campaignBudget: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_CampaignBudgetParameters
    forecastingSetTargetCpa: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ForecastingSetTargetCpaParameters
    forecastingSetTargetRoas: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ForecastingSetTargetRoasParameters
    keyword: (
        GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_KeywordParameters
    )
    leadFormAsset: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_LeadFormAssetParameters
    lowerTargetRoas: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_LowerTargetRoasParameters
    moveUnusedBudget: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_MoveUnusedBudgetParameters
    raiseTargetCpa: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_RaiseTargetCpaParameters
    raiseTargetCpaBidTooLow: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_RaiseTargetCpaBidTooLowParameters
    resourceName: str
    responsiveSearchAd: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ResponsiveSearchAdParameters
    responsiveSearchAdAsset: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ResponsiveSearchAdAssetParameters
    responsiveSearchAdImproveAdStrength: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ResponsiveSearchAdImproveAdStrengthParameters
    setTargetCpa: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ForecastingSetTargetCpaParameters
    setTargetRoas: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_ForecastingSetTargetRoasParameters
    sitelinkAsset: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_SitelinkAssetParameters
    sitelinkExtension: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_SitelinkExtensionParameters
    targetCpaOptIn: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_TargetCpaOptInParameters
    targetRoasOptIn: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_TargetRoasOptInParameters
    textAd: (
        GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_TextAdParameters
    )
    useBroadMatchKeyword: GoogleAdsSearchads360V23Services_ApplyRecommendationOperation_UseBroadMatchKeywordParameters

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyRecommendationRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__ApplyRecommendationOperation]
    partialFailure: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyRecommendationResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__ApplyRecommendationResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyRecommendationResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetGroupAssetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AssetGroupAsset
    remove: str
    update: GoogleAdsSearchads360V23Resources__AssetGroupAsset
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetGroupListingGroupFilterOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AssetGroupListingGroupFilter
    remove: str
    update: GoogleAdsSearchads360V23Resources__AssetGroupListingGroupFilter
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetGroupOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AssetGroup
    remove: str
    update: GoogleAdsSearchads360V23Resources__AssetGroup
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetGroupSignalOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AssetGroupSignal
    exemptPolicyViolationKeys: _list[GoogleAdsSearchads360V23Common__PolicyViolationKey]
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetOperation(typing.TypedDict, total=False):
    create: GoogleAdsSearchads360V23Resources__Asset
    update: GoogleAdsSearchads360V23Resources__Asset
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetSetAssetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AssetSetAsset
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__AssetSet
    remove: str
    update: GoogleAdsSearchads360V23Resources__AssetSet
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AssetsWithFieldType(
    typing.TypedDict, total=False
):
    asset: str
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceCompositionAttribute(
    typing.TypedDict, total=False
):
    attributeMetadata: GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata
    metrics: GoogleAdsSearchads360V23Services__AudienceCompositionMetrics

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceCompositionAttributeCluster(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleAdsSearchads360V23Services__AudienceCompositionAttribute]
    clusterDisplayName: str
    clusterMetrics: GoogleAdsSearchads360V23Services__AudienceCompositionMetrics

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceCompositionMetrics(
    typing.TypedDict, total=False
):
    audienceShare: float
    baselineAudienceShare: float
    index: float
    score: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceCompositionSection(
    typing.TypedDict, total=False
):
    clusteredAttributes: _list[
        GoogleAdsSearchads360V23Services__AudienceCompositionAttributeCluster
    ]
    dimension: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CATEGORY",
        "KNOWLEDGE_GRAPH",
        "GEO_TARGET_COUNTRY",
        "SUB_COUNTRY_LOCATION",
        "YOUTUBE_CHANNEL",
        "AFFINITY_USER_INTEREST",
        "IN_MARKET_USER_INTEREST",
        "PARENTAL_STATUS",
        "INCOME_RANGE",
        "AGE_RANGE",
        "GENDER",
        "YOUTUBE_VIDEO",
        "DEVICE",
        "YOUTUBE_LINEUP",
        "USER_LIST",
        "LIFE_EVENT_USER_INTEREST",
    ]
    topAttributes: _list[GoogleAdsSearchads360V23Services__AudienceCompositionAttribute]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceInsightsDimensions(
    typing.TypedDict, total=False
):
    dimensions: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CATEGORY",
            "KNOWLEDGE_GRAPH",
            "GEO_TARGET_COUNTRY",
            "SUB_COUNTRY_LOCATION",
            "YOUTUBE_CHANNEL",
            "AFFINITY_USER_INTEREST",
            "IN_MARKET_USER_INTEREST",
            "PARENTAL_STATUS",
            "INCOME_RANGE",
            "AGE_RANGE",
            "GENDER",
            "YOUTUBE_VIDEO",
            "DEVICE",
            "YOUTUBE_LINEUP",
            "USER_LIST",
            "LIFE_EVENT_USER_INTEREST",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__Audience
    update: GoogleAdsSearchads360V23Resources__Audience
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceOverlapItem(
    typing.TypedDict, total=False
):
    attributeMetadata: GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata
    potentialYoutubeReachIntersection: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AudienceTargeting(
    typing.TypedDict, total=False
):
    userInterest: _list[GoogleAdsSearchads360V23Common__UserInterestInfo]
    userLists: _list[GoogleAdsSearchads360V23Common__UserListInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BatchJobOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__BatchJob
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BatchJobResult(typing.TypedDict, total=False):
    mutateOperationResponse: GoogleAdsSearchads360V23Services__MutateOperationResponse
    operationIndex: str
    status: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BenchmarksLocation(
    typing.TypedDict, total=False
):
    locationInfo: GoogleAdsSearchads360V23Common__LocationInfo
    locationName: str
    locationType: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BenchmarksProductMetadata(
    typing.TypedDict, total=False
):
    marketingObjective: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AWARENESS", "CONSIDERATION", "ACTION"
    ]
    productCode: str
    productName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BenchmarksSource(typing.TypedDict, total=False):
    industryVerticalId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BenchmarksSourceMetadata(
    typing.TypedDict, total=False
):
    benchmarksSourceType: typing.Literal["UNSPECIFIED", "UNKNOWN", "INDUSTRY_VERTICAL"]
    industryVerticalInfo: GoogleAdsSearchads360V23Services__IndustryVerticalInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BiddableKeyword(typing.TypedDict, total=False):
    keyword: GoogleAdsSearchads360V23Common__KeywordInfo
    maxCpcBidMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BiddingDataExclusionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__BiddingDataExclusion
    remove: str
    update: GoogleAdsSearchads360V23Resources__BiddingDataExclusion
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BiddingSeasonalityAdjustmentOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__BiddingSeasonalityAdjustment
    remove: str
    update: GoogleAdsSearchads360V23Resources__BiddingSeasonalityAdjustment
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BiddingStrategyOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__BiddingStrategy
    remove: str
    update: GoogleAdsSearchads360V23Resources__BiddingStrategy
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BillingSetupOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__BillingSetup
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__BrandCampaignAssets(
    typing.TypedDict, total=False
):
    businessNameAsset: str
    landscapeLogoAsset: _list[str]
    logoAsset: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CallConversion(typing.TypedDict, total=False):
    callStartDateTime: str
    callerId: str
    consent: GoogleAdsSearchads360V23Common__Consent
    conversionAction: str
    conversionDateTime: str
    conversionValue: float
    currencyCode: str
    customVariables: _list[GoogleAdsSearchads360V23Services__CustomVariable]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CallConversionResult(
    typing.TypedDict, total=False
):
    callStartDateTime: str
    callerId: str
    conversionAction: str
    conversionDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignAssetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignAsset
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignAsset
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignAssetSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignAssetSet
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignBidModifierOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignBidModifier
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignBidModifier
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignBudgetMapping(
    typing.TypedDict, total=False
):
    campaignBudget: str
    experimentCampaign: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignBudgetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignBudget
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignBudget
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignConversionGoalOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__CampaignConversionGoal
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignCriterionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignCriterion
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignCriterion
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignCustomizerOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignCustomizer
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignDraftOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignDraft
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignDraft
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignDuration(typing.TypedDict, total=False):
    dateRange: GoogleAdsSearchads360V23Common__DateRange
    durationInDays: int

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignGoalConfigOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignGoalConfig
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignGoalConfig
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignGroupOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignGroup
    remove: str
    update: GoogleAdsSearchads360V23Resources__CampaignGroup
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignLabelOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignLabel
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignLifecycleGoalOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignLifecycleGoal
    update: GoogleAdsSearchads360V23Resources__CampaignLifecycleGoal
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__Campaign
    remove: str
    update: GoogleAdsSearchads360V23Resources__Campaign
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignSharedSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CampaignSharedSet
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CampaignToForecast(
    typing.TypedDict, total=False
):
    adGroups: _list[GoogleAdsSearchads360V23Services__ForecastAdGroup]
    biddingStrategy: (
        GoogleAdsSearchads360V23Services_CampaignToForecast_CampaignBiddingStrategy
    )
    conversionRate: float
    geoModifiers: _list[GoogleAdsSearchads360V23Services__CriterionBidModifier]
    keywordPlanNetwork: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "GOOGLE_SEARCH", "GOOGLE_SEARCH_AND_PARTNERS"
    ]
    languageConstants: _list[str]
    negativeKeywords: _list[GoogleAdsSearchads360V23Common__KeywordInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CartData(typing.TypedDict, total=False):
    feedCountryCode: str
    feedLanguageCode: str
    items: _list[GoogleAdsSearchads360V23Services_CartData_Item]
    localTransactionCost: float
    merchantId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ClickConversion(typing.TypedDict, total=False):
    cartData: GoogleAdsSearchads360V23Services__CartData
    consent: GoogleAdsSearchads360V23Common__Consent
    conversionAction: str
    conversionDateTime: str
    conversionEnvironment: typing.Literal["UNSPECIFIED", "UNKNOWN", "APP", "WEB"]
    conversionValue: float
    currencyCode: str
    customVariables: _list[GoogleAdsSearchads360V23Services__CustomVariable]
    customerType: typing.Literal["UNSPECIFIED", "UNKNOWN", "NEW", "RETURNING"]
    externalAttributionData: GoogleAdsSearchads360V23Services__ExternalAttributionData
    gbraid: str
    gclid: str
    orderId: str
    sessionAttributesEncoded: str
    sessionAttributesKeyValuePairs: (
        GoogleAdsSearchads360V23Services__SessionAttributesKeyValuePairs
    )
    userIdentifiers: _list[GoogleAdsSearchads360V23Common__UserIdentifier]
    userIpAddress: str
    wbraid: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ClickConversionResult(
    typing.TypedDict, total=False
):
    conversionAction: str
    conversionDateTime: str
    gbraid: str
    gclid: str
    userIdentifiers: _list[GoogleAdsSearchads360V23Common__UserIdentifier]
    wbraid: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__CampaignLifecycleGoalOperation
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__CustomerLifecycleGoalOperation
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__Conversation(typing.TypedDict, total=False):
    localServicesLead: str
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversationOrError(
    typing.TypedDict, total=False
):
    localServicesLeadConversation: str
    partialFailureError: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionActionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__ConversionAction
    remove: str
    update: GoogleAdsSearchads360V23Resources__ConversionAction
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionAdjustment(
    typing.TypedDict, total=False
):
    adjustmentDateTime: str
    adjustmentType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "RETRACTION", "RESTATEMENT", "ENHANCEMENT"
    ]
    conversionAction: str
    gclidDateTimePair: GoogleAdsSearchads360V23Services__GclidDateTimePair
    orderId: str
    restatementValue: GoogleAdsSearchads360V23Services__RestatementValue
    userAgent: str
    userIdentifiers: _list[GoogleAdsSearchads360V23Common__UserIdentifier]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionAdjustmentResult(
    typing.TypedDict, total=False
):
    adjustmentDateTime: str
    adjustmentType: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "RETRACTION", "RESTATEMENT", "ENHANCEMENT"
    ]
    conversionAction: str
    gclidDateTimePair: GoogleAdsSearchads360V23Services__GclidDateTimePair
    orderId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionCustomDimensionHeader(
    typing.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionCustomMetricHeader(
    typing.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionCustomVariableOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__ConversionCustomVariable
    update: GoogleAdsSearchads360V23Resources__ConversionCustomVariable
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionGoalCampaignConfigOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__ConversionGoalCampaignConfig
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionRateSuggestion(
    typing.TypedDict, total=False
):
    conversionRate: float
    conversionRateModel: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CUSTOMER_HISTORY",
        "INVENTORY_AGGRESSIVE",
        "INVENTORY_CONSERVATIVE",
        "INVENTORY_MEDIAN",
    ]
    plannableProductCode: str
    surfaceTargeting: GoogleAdsSearchads360V23Services__SurfaceTargeting

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionValueRuleOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__ConversionValueRule
    remove: str
    update: GoogleAdsSearchads360V23Resources__ConversionValueRule
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConversionValueRuleSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__ConversionValueRuleSet
    remove: str
    update: GoogleAdsSearchads360V23Resources__ConversionValueRuleSet
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateAccountLinkRequest(
    typing.TypedDict, total=False
):
    accountLink: GoogleAdsSearchads360V23Resources__AccountLink

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateAccountLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateCustomerClientRequest(
    typing.TypedDict, total=False
):
    accessRole: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADMIN", "STANDARD", "READ_ONLY", "EMAIL_ONLY"
    ]
    customerClient: GoogleAdsSearchads360V23Resources__Customer
    emailAddress: str
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateCustomerClientResponse(
    typing.TypedDict, total=False
):
    invitationLink: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateDataLinkRequest(
    typing.TypedDict, total=False
):
    dataLink: GoogleAdsSearchads360V23Resources__DataLink

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateDataLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateOfflineUserDataJobRequest(
    typing.TypedDict, total=False
):
    enableMatchRateRangePreview: bool
    job: GoogleAdsSearchads360V23Resources__OfflineUserDataJob
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateOfflineUserDataJobResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateProductLinkInvitationRequest(
    typing.TypedDict, total=False
):
    productLinkInvitation: GoogleAdsSearchads360V23Resources__ProductLinkInvitation

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateProductLinkInvitationResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateProductLinkRequest(
    typing.TypedDict, total=False
):
    productLink: GoogleAdsSearchads360V23Resources__ProductLink

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateProductLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CriterionBidModifier(
    typing.TypedDict, total=False
):
    bidModifier: float
    geoTargetConstant: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomAudienceOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomAudience
    remove: str
    update: GoogleAdsSearchads360V23Resources__CustomAudience
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomColumnHeader(
    typing.TypedDict, total=False
):
    id: str
    name: str
    referencesMetrics: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomConversionGoalOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomConversionGoal
    remove: str
    update: GoogleAdsSearchads360V23Resources__CustomConversionGoal
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomInterestOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomInterest
    update: GoogleAdsSearchads360V23Resources__CustomInterest
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomVariable(typing.TypedDict, total=False):
    conversionCustomVariable: str
    value: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerAssetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerAsset
    remove: str
    update: GoogleAdsSearchads360V23Resources__CustomerAsset
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerAssetSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerAssetSet
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerClientLinkOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerClientLink
    update: GoogleAdsSearchads360V23Resources__CustomerClientLink
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerConversionGoalOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__CustomerConversionGoal
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerCustomizerOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerCustomizer
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerLabelOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerLabel
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerLifecycleGoalOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerLifecycleGoal
    update: GoogleAdsSearchads360V23Resources__CustomerLifecycleGoal
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerManagerLinkOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__CustomerManagerLink
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerNegativeCriterionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerNegativeCriterion
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__Customer
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerSkAdNetworkConversionValueSchemaOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__CustomerSkAdNetworkConversionValueSchema

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerUserAccessInvitationOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomerUserAccessInvitation
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomerUserAccessOperation(
    typing.TypedDict, total=False
):
    remove: str
    update: GoogleAdsSearchads360V23Resources__CustomerUserAccess
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CustomizerAttributeOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__CustomizerAttribute
    remove: str
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CyoIncentives(typing.TypedDict, total=False):
    highOffer: GoogleAdsSearchads360V23Services__Incentive
    lowOffer: GoogleAdsSearchads360V23Services__Incentive
    mediumOffer: GoogleAdsSearchads360V23Services__Incentive

@typing.type_check_only
class GoogleAdsSearchads360V23Services__DimensionOverlapResult(
    typing.TypedDict, total=False
):
    dimension: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "CATEGORY",
        "KNOWLEDGE_GRAPH",
        "GEO_TARGET_COUNTRY",
        "SUB_COUNTRY_LOCATION",
        "YOUTUBE_CHANNEL",
        "AFFINITY_USER_INTEREST",
        "IN_MARKET_USER_INTEREST",
        "PARENTAL_STATUS",
        "INCOME_RANGE",
        "AGE_RANGE",
        "GENDER",
        "YOUTUBE_VIDEO",
        "DEVICE",
        "YOUTUBE_LINEUP",
        "USER_LIST",
        "LIFE_EVENT_USER_INTEREST",
    ]
    items: _list[GoogleAdsSearchads360V23Services__AudienceOverlapItem]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__DismissRecommendationRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services_DismissRecommendationRequest_DismissRecommendationOperation
    ]
    partialFailure: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__DismissRecommendationResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services_DismissRecommendationResponse_DismissRecommendationResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EffectiveFrequencyBreakdown(
    typing.TypedDict, total=False
):
    effectiveCoviewReach: str
    effectiveFrequency: int
    onTargetEffectiveCoviewReach: str
    onTargetReach: str
    totalReach: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EffectiveFrequencyLimit(
    typing.TypedDict, total=False
):
    effectiveFrequencyBreakdownLimit: int

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EnableOperation(typing.TypedDict, total=False):
    accentColor: str
    autoPopulateBrandAssets: bool
    brandAssets: GoogleAdsSearchads360V23Services__BrandCampaignAssets
    campaign: str
    finalUriDomain: str
    fontFamily: str
    mainColor: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EnablePMaxBrandGuidelinesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__EnableOperation]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EnablePMaxBrandGuidelinesResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__EnablementResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EnablementResult(typing.TypedDict, total=False):
    campaign: str
    enablementError: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EndExperimentRequest(
    typing.TypedDict, total=False
):
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ExperimentArmOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__ExperimentArm
    remove: str
    update: GoogleAdsSearchads360V23Resources__ExperimentArm
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ExperimentOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__Experiment
    remove: str
    update: GoogleAdsSearchads360V23Resources__Experiment
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ExternalAttributionData(
    typing.TypedDict, total=False
):
    externalAttributionCredit: float
    externalAttributionModel: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__FetchIncentiveResponse(
    typing.TypedDict, total=False
):
    incentiveOffer: GoogleAdsSearchads360V23Services__IncentiveOffer

@typing.type_check_only
class GoogleAdsSearchads360V23Services__Forecast(typing.TypedDict, total=False):
    conversions: float
    effectiveFrequencyBreakdowns: _list[
        GoogleAdsSearchads360V23Services__EffectiveFrequencyBreakdown
    ]
    onTargetCoviewImpressions: str
    onTargetCoviewReach: str
    onTargetImpressions: str
    onTargetReach: str
    totalCoviewImpressions: str
    totalCoviewReach: str
    totalImpressions: str
    totalReach: str
    trueviewViews: str
    viewableImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ForecastAdGroup(typing.TypedDict, total=False):
    biddableKeywords: _list[GoogleAdsSearchads360V23Services__BiddableKeyword]
    maxCpcBidMicros: str
    negativeKeywords: _list[GoogleAdsSearchads360V23Common__KeywordInfo]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ForecastMetricOptions(
    typing.TypedDict, total=False
):
    includeCoview: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__FrequencyCap(typing.TypedDict, total=False):
    impressions: int
    timeUnit: typing.Literal["UNSPECIFIED", "UNKNOWN", "DAY", "WEEK", "MONTH"]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GclidDateTimePair(
    typing.TypedDict, total=False
):
    conversionDateTime: str
    gclid: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAdGroupThemesRequest(
    typing.TypedDict, total=False
):
    adGroups: _list[str]
    keywords: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAdGroupThemesResponse(
    typing.TypedDict, total=False
):
    adGroupKeywordSuggestions: _list[
        GoogleAdsSearchads360V23Services__AdGroupKeywordSuggestion
    ]
    unusableAdGroups: _list[GoogleAdsSearchads360V23Services__UnusableAdGroup]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceCompositionInsightsRequest(
    typing.TypedDict, total=False
):
    audience: GoogleAdsSearchads360V23Services__InsightsAudience
    baselineAudience: GoogleAdsSearchads360V23Services__InsightsAudience
    customerInsightsGroup: str
    dataMonth: str
    dimensions: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CATEGORY",
            "KNOWLEDGE_GRAPH",
            "GEO_TARGET_COUNTRY",
            "SUB_COUNTRY_LOCATION",
            "YOUTUBE_CHANNEL",
            "AFFINITY_USER_INTEREST",
            "IN_MARKET_USER_INTEREST",
            "PARENTAL_STATUS",
            "INCOME_RANGE",
            "AGE_RANGE",
            "GENDER",
            "YOUTUBE_VIDEO",
            "DEVICE",
            "YOUTUBE_LINEUP",
            "USER_LIST",
            "LIFE_EVENT_USER_INTEREST",
        ]
    ]
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceCompositionInsightsResponse(
    typing.TypedDict, total=False
):
    sections: _list[GoogleAdsSearchads360V23Services__AudienceCompositionSection]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceDefinitionRequest(
    typing.TypedDict, total=False
):
    audienceDescription: GoogleAdsSearchads360V23Services__InsightsAudienceDescription
    customerInsightsGroup: str
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceDefinitionResponse(
    typing.TypedDict, total=False
):
    highRelevanceAttributes: _list[
        GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata
    ]
    mediumRelevanceAttributes: _list[
        GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceOverlapInsightsRequest(
    typing.TypedDict, total=False
):
    countryLocation: GoogleAdsSearchads360V23Common__LocationInfo
    customerInsightsGroup: str
    dimensions: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CATEGORY",
            "KNOWLEDGE_GRAPH",
            "GEO_TARGET_COUNTRY",
            "SUB_COUNTRY_LOCATION",
            "YOUTUBE_CHANNEL",
            "AFFINITY_USER_INTEREST",
            "IN_MARKET_USER_INTEREST",
            "PARENTAL_STATUS",
            "INCOME_RANGE",
            "AGE_RANGE",
            "GENDER",
            "YOUTUBE_VIDEO",
            "DEVICE",
            "YOUTUBE_LINEUP",
            "USER_LIST",
            "LIFE_EVENT_USER_INTEREST",
        ]
    ]
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    primaryAttribute: GoogleAdsSearchads360V23Common__AudienceInsightsAttribute

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceOverlapInsightsResponse(
    typing.TypedDict, total=False
):
    dimensionResults: _list[GoogleAdsSearchads360V23Services__DimensionOverlapResult]
    primaryAttributeMetadata: (
        GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateBenchmarksMetricsRequest(
    typing.TypedDict, total=False
):
    applicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    benchmarksSource: GoogleAdsSearchads360V23Services__BenchmarksSource
    currencyCode: str
    customerBenchmarksGroup: str
    dateRange: GoogleAdsSearchads360V23Common__DateRange
    location: GoogleAdsSearchads360V23Common__LocationInfo
    productFilter: GoogleAdsSearchads360V23Services__ProductFilter

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateBenchmarksMetricsResponse(
    typing.TypedDict, total=False
):
    averageBenchmarksMetrics: GoogleAdsSearchads360V23Services__Metrics
    customerMetrics: GoogleAdsSearchads360V23Services__Metrics

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateConversionRatesRequest(
    typing.TypedDict, total=False
):
    customerId: str
    customerReachGroup: str
    reachApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateConversionRatesResponse(
    typing.TypedDict, total=False
):
    conversionRateSuggestions: _list[
        GoogleAdsSearchads360V23Services__ConversionRateSuggestion
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateInsightsFinderReportRequest(
    typing.TypedDict, total=False
):
    baselineAudience: GoogleAdsSearchads360V23Services__InsightsAudience
    customerInsightsGroup: str
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    specificAudience: GoogleAdsSearchads360V23Services__InsightsAudience

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateInsightsFinderReportResponse(
    typing.TypedDict, total=False
):
    savedReportUrl: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordForecastMetricsRequest(
    typing.TypedDict, total=False
):
    campaign: GoogleAdsSearchads360V23Services__CampaignToForecast
    currencyCode: str
    forecastPeriod: GoogleAdsSearchads360V23Common__DateRange

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordForecastMetricsResponse(
    typing.TypedDict, total=False
):
    campaignForecastMetrics: GoogleAdsSearchads360V23Services__KeywordForecastMetrics

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsRequest(
    typing.TypedDict, total=False
):
    aggregateMetrics: GoogleAdsSearchads360V23Common__KeywordPlanAggregateMetrics
    geoTargetConstants: _list[str]
    historicalMetricsOptions: GoogleAdsSearchads360V23Common__HistoricalMetricsOptions
    includeAdultKeywords: bool
    keywordPlanNetwork: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "GOOGLE_SEARCH", "GOOGLE_SEARCH_AND_PARTNERS"
    ]
    keywords: _list[str]
    language: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsResponse(
    typing.TypedDict, total=False
):
    aggregateMetricResults: (
        GoogleAdsSearchads360V23Common__KeywordPlanAggregateMetricResults
    )
    results: _list[
        GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsResult(
    typing.TypedDict, total=False
):
    closeVariants: _list[str]
    keywordMetrics: GoogleAdsSearchads360V23Common__KeywordPlanHistoricalMetrics
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponse(
    typing.TypedDict, total=False
):
    aggregateMetricResults: (
        GoogleAdsSearchads360V23Common__KeywordPlanAggregateMetricResults
    )
    nextPageToken: str
    results: _list[GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResult]
    totalSize: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResult(
    typing.TypedDict, total=False
):
    closeVariants: _list[str]
    keywordAnnotations: GoogleAdsSearchads360V23Common__KeywordAnnotations
    keywordIdeaMetrics: GoogleAdsSearchads360V23Common__KeywordPlanHistoricalMetrics
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordIdeasRequest(
    typing.TypedDict, total=False
):
    aggregateMetrics: GoogleAdsSearchads360V23Common__KeywordPlanAggregateMetrics
    geoTargetConstants: _list[str]
    historicalMetricsOptions: GoogleAdsSearchads360V23Common__HistoricalMetricsOptions
    includeAdultKeywords: bool
    keywordAndUrlSeed: GoogleAdsSearchads360V23Services__KeywordAndUrlSeed
    keywordAnnotation: _list[
        typing.Literal["UNSPECIFIED", "UNKNOWN", "KEYWORD_CONCEPT"]
    ]
    keywordPlanNetwork: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "GOOGLE_SEARCH", "GOOGLE_SEARCH_AND_PARTNERS"
    ]
    keywordSeed: GoogleAdsSearchads360V23Services__KeywordSeed
    language: str
    pageSize: int
    pageToken: str
    siteSeed: GoogleAdsSearchads360V23Services__SiteSeed
    urlSeed: GoogleAdsSearchads360V23Services__UrlSeed

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateReachForecastRequest(
    typing.TypedDict, total=False
):
    campaignDuration: GoogleAdsSearchads360V23Services__CampaignDuration
    cookieFrequencyCap: int
    cookieFrequencyCapSetting: GoogleAdsSearchads360V23Services__FrequencyCap
    currencyCode: str
    customerReachGroup: str
    effectiveFrequencyLimit: GoogleAdsSearchads360V23Services__EffectiveFrequencyLimit
    forecastMetricOptions: GoogleAdsSearchads360V23Services__ForecastMetricOptions
    minEffectiveFrequency: int
    plannedProducts: _list[GoogleAdsSearchads360V23Services__PlannedProduct]
    reachApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    targeting: GoogleAdsSearchads360V23Services__Targeting

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateReachForecastResponse(
    typing.TypedDict, total=False
):
    onTargetAudienceMetrics: GoogleAdsSearchads360V23Services__OnTargetAudienceMetrics
    reachCurve: GoogleAdsSearchads360V23Services__ReachCurve

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateRecommendationsRequest(
    typing.TypedDict, total=False
):
    adGroupInfo: _list[
        GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_AdGroupInfo
    ]
    advertisingChannelType: typing.Literal[
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
        "TRAVEL",
        "DEMAND_GEN",
        "SOCIAL",
    ]
    assetGroupInfo: _list[
        GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_AssetGroupInfo
    ]
    biddingInfo: (
        GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_BiddingInfo
    )
    budgetInfo: (
        GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_BudgetInfo
    )
    campaignCallAssetCount: int
    campaignImageAssetCount: int
    campaignSitelinkCount: int
    conversionTrackingStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "NOT_CONVERSION_TRACKED",
        "CONVERSION_TRACKING_MANAGED_BY_SELF",
        "CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER",
        "CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER",
    ]
    countryCodes: _list[str]
    isNewCustomer: bool
    languageCodes: _list[str]
    merchantCenterAccountId: str
    negativeLocationsIds: _list[str]
    positiveLocationsIds: _list[str]
    recommendationTypes: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CAMPAIGN_BUDGET",
            "KEYWORD",
            "TEXT_AD",
            "TARGET_CPA_OPT_IN",
            "MAXIMIZE_CONVERSIONS_OPT_IN",
            "ENHANCED_CPC_OPT_IN",
            "SEARCH_PARTNERS_OPT_IN",
            "MAXIMIZE_CLICKS_OPT_IN",
            "OPTIMIZE_AD_ROTATION",
            "KEYWORD_MATCH_TYPE",
            "MOVE_UNUSED_BUDGET",
            "FORECASTING_CAMPAIGN_BUDGET",
            "TARGET_ROAS_OPT_IN",
            "RESPONSIVE_SEARCH_AD",
            "MARGINAL_ROI_CAMPAIGN_BUDGET",
            "USE_BROAD_MATCH_KEYWORD",
            "RESPONSIVE_SEARCH_AD_ASSET",
            "UPGRADE_SMART_SHOPPING_CAMPAIGN_TO_PERFORMANCE_MAX",
            "RESPONSIVE_SEARCH_AD_IMPROVE_AD_STRENGTH",
            "DISPLAY_EXPANSION_OPT_IN",
            "UPGRADE_LOCAL_CAMPAIGN_TO_PERFORMANCE_MAX",
            "RAISE_TARGET_CPA_BID_TOO_LOW",
            "FORECASTING_SET_TARGET_ROAS",
            "CALLOUT_ASSET",
            "SITELINK_ASSET",
            "CALL_ASSET",
            "SHOPPING_ADD_AGE_GROUP",
            "SHOPPING_ADD_COLOR",
            "SHOPPING_ADD_GENDER",
            "SHOPPING_ADD_GTIN",
            "SHOPPING_ADD_MORE_IDENTIFIERS",
            "SHOPPING_ADD_SIZE",
            "SHOPPING_ADD_PRODUCTS_TO_CAMPAIGN",
            "SHOPPING_FIX_DISAPPROVED_PRODUCTS",
            "SHOPPING_TARGET_ALL_OFFERS",
            "SHOPPING_FIX_SUSPENDED_MERCHANT_CENTER_ACCOUNT",
            "SHOPPING_FIX_MERCHANT_CENTER_ACCOUNT_SUSPENSION_WARNING",
            "SHOPPING_MIGRATE_REGULAR_SHOPPING_CAMPAIGN_OFFERS_TO_PERFORMANCE_MAX",
            "DYNAMIC_IMAGE_EXTENSION_OPT_IN",
            "RAISE_TARGET_CPA",
            "LOWER_TARGET_ROAS",
            "PERFORMANCE_MAX_OPT_IN",
            "IMPROVE_PERFORMANCE_MAX_AD_STRENGTH",
            "MIGRATE_DYNAMIC_SEARCH_ADS_CAMPAIGN_TO_PERFORMANCE_MAX",
            "FORECASTING_SET_TARGET_CPA",
            "SET_TARGET_CPA",
            "SET_TARGET_ROAS",
            "MAXIMIZE_CONVERSION_VALUE_OPT_IN",
            "IMPROVE_GOOGLE_TAG_COVERAGE",
            "PERFORMANCE_MAX_FINAL_URL_OPT_IN",
            "REFRESH_CUSTOMER_MATCH_LIST",
            "CUSTOM_AUDIENCE_OPT_IN",
            "LEAD_FORM_ASSET",
            "IMPROVE_DEMAND_GEN_AD_STRENGTH",
        ]
    ]
    seedInfo: GoogleAdsSearchads360V23Services_GenerateRecommendationsRequest_SeedInfo
    targetContentNetwork: bool
    targetPartnerSearchNetwork: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateRecommendationsResponse(
    typing.TypedDict, total=False
):
    recommendations: _list[GoogleAdsSearchads360V23Resources__Recommendation]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateSuggestedTargetingInsightsRequest(
    typing.TypedDict, total=False
):
    audienceDefinition: GoogleAdsSearchads360V23Services__InsightsAudienceDefinition
    audienceDescription: GoogleAdsSearchads360V23Services__InsightsAudienceDescription
    customerInsightsGroup: str
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateSuggestedTargetingInsightsResponse(
    typing.TypedDict, total=False
):
    suggestions: _list[GoogleAdsSearchads360V23Services__TargetingSuggestionMetrics]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateTargetingSuggestionMetricsRequest(
    typing.TypedDict, total=False
):
    audiences: _list[GoogleAdsSearchads360V23Services__InsightsAudience]
    customerInsightsGroup: str
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateTargetingSuggestionMetricsResponse(
    typing.TypedDict, total=False
):
    suggestions: _list[GoogleAdsSearchads360V23Services__TargetingSuggestionMetrics]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GeoTargetConstantSuggestion(
    typing.TypedDict, total=False
):
    geoTargetConstant: GoogleAdsSearchads360V23Resources__GeoTargetConstant
    geoTargetConstantParents: _list[
        GoogleAdsSearchads360V23Resources__GeoTargetConstant
    ]
    locale: str
    reach: str
    searchTerm: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GetIdentityVerificationResponse(
    typing.TypedDict, total=False
):
    identityVerification: _list[GoogleAdsSearchads360V23Services__IdentityVerification]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GetSmartCampaignStatusResponse(
    typing.TypedDict, total=False
):
    eligibleDetails: GoogleAdsSearchads360V23Services__SmartCampaignEligibleDetails
    endedDetails: GoogleAdsSearchads360V23Services__SmartCampaignEndedDetails
    notEligibleDetails: (
        GoogleAdsSearchads360V23Services__SmartCampaignNotEligibleDetails
    )
    pausedDetails: GoogleAdsSearchads360V23Services__SmartCampaignPausedDetails
    removedDetails: GoogleAdsSearchads360V23Services__SmartCampaignRemovedDetails
    smartCampaignStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PAUSED",
        "NOT_ELIGIBLE",
        "PENDING",
        "ELIGIBLE",
        "REMOVED",
        "ENDED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GoalOperation(typing.TypedDict, total=False):
    create: GoogleAdsSearchads360V23Resources__Goal
    update: GoogleAdsSearchads360V23Resources__Goal
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GraduateExperimentRequest(
    typing.TypedDict, total=False
):
    campaignBudgetMappings: _list[
        GoogleAdsSearchads360V23Services__CampaignBudgetMapping
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__HotelAssetSuggestion(
    typing.TypedDict, total=False
):
    callToAction: typing.Literal[
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
    finalUrl: str
    hotelName: str
    imageAssets: _list[GoogleAdsSearchads360V23Services__HotelImageAsset]
    placeId: str
    status: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "SUCCESS", "HOTEL_NOT_FOUND", "INVALID_PLACE_ID"
    ]
    textAssets: _list[GoogleAdsSearchads360V23Services__HotelTextAsset]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__HotelImageAsset(typing.TypedDict, total=False):
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    uri: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__HotelTextAsset(typing.TypedDict, total=False):
    assetFieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]
    text: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__IdentityVerification(
    typing.TypedDict, total=False
):
    identityVerificationRequirement: (
        GoogleAdsSearchads360V23Services__IdentityVerificationRequirement
    )
    verificationProgram: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER_IDENTITY_VERIFICATION"
    ]
    verificationProgress: GoogleAdsSearchads360V23Services__IdentityVerificationProgress

@typing.type_check_only
class GoogleAdsSearchads360V23Services__IdentityVerificationProgress(
    typing.TypedDict, total=False
):
    actionUrl: str
    invitationLinkExpirationTime: str
    programStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "PENDING_USER_ACTION",
        "PENDING_REVIEW",
        "SUCCESS",
        "FAILURE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__IdentityVerificationRequirement(
    typing.TypedDict, total=False
):
    verificationCompletionDeadlineTime: str
    verificationStartDeadlineTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__Incentive(typing.TypedDict, total=False):
    incentiveId: str
    incentiveTermsAndConditionsUrl: str
    requirement: GoogleAdsSearchads360V23Services_Incentive_Requirement
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "ACQUISITION"]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__IncentiveOffer(typing.TypedDict, total=False):
    consolidatedTermsAndConditionsUrl: str
    cyoIncentives: GoogleAdsSearchads360V23Services__CyoIncentives
    type: typing.Literal["UNSPECIFIED", "UNKNOWN", "NO_INCENTIVE", "CYO_INCENTIVE"]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__IndustryVerticalInfo(
    typing.TypedDict, total=False
):
    industryVerticalId: str
    industryVerticalName: str
    parentIndustryVerticalId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__InsightsAudience(typing.TypedDict, total=False):
    ageRanges: _list[GoogleAdsSearchads360V23Common__AgeRangeInfo]
    countryLocations: _list[GoogleAdsSearchads360V23Common__LocationInfo]
    gender: GoogleAdsSearchads360V23Common__GenderInfo
    incomeRanges: _list[GoogleAdsSearchads360V23Common__IncomeRangeInfo]
    lineups: _list[GoogleAdsSearchads360V23Common__AudienceInsightsLineup]
    parentalStatus: GoogleAdsSearchads360V23Common__ParentalStatusInfo
    subCountryLocations: _list[GoogleAdsSearchads360V23Common__LocationInfo]
    topicAudienceCombinations: _list[
        GoogleAdsSearchads360V23Services__InsightsAudienceAttributeGroup
    ]
    userList: GoogleAdsSearchads360V23Common__UserListInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__InsightsAudienceAttributeGroup(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleAdsSearchads360V23Common__AudienceInsightsAttribute]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__InsightsAudienceDefinition(
    typing.TypedDict, total=False
):
    audience: GoogleAdsSearchads360V23Services__InsightsAudience
    baselineAudience: GoogleAdsSearchads360V23Services__InsightsAudience
    dataMonth: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__InsightsAudienceDescription(
    typing.TypedDict, total=False
):
    audienceDescription: str
    audienceDimensions: GoogleAdsSearchads360V23Services__AudienceInsightsDimensions
    countryLocations: _list[GoogleAdsSearchads360V23Common__LocationInfo]
    marketingObjective: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "AWARENESS", "CONSIDERATION", "RESEARCH"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordAndUrlSeed(
    typing.TypedDict, total=False
):
    keywords: _list[str]
    url: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordForecastMetrics(
    typing.TypedDict, total=False
):
    averageCpaMicros: str
    averageCpcMicros: str
    clickThroughRate: float
    clicks: float
    conversionRate: float
    conversions: float
    costMicros: str
    impressions: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordPlanAdGroupKeywordOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__KeywordPlanAdGroupKeyword
    remove: str
    update: GoogleAdsSearchads360V23Resources__KeywordPlanAdGroupKeyword
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordPlanAdGroupOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__KeywordPlanAdGroup
    remove: str
    update: GoogleAdsSearchads360V23Resources__KeywordPlanAdGroup
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordPlanCampaignKeywordOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__KeywordPlanCampaignKeyword
    remove: str
    update: GoogleAdsSearchads360V23Resources__KeywordPlanCampaignKeyword
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordPlanCampaignOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__KeywordPlanCampaign
    remove: str
    update: GoogleAdsSearchads360V23Resources__KeywordPlanCampaign
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordPlanOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__KeywordPlan
    remove: str
    update: GoogleAdsSearchads360V23Resources__KeywordPlan
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__KeywordSeed(typing.TypedDict, total=False):
    keywords: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__LabelOperation(typing.TypedDict, total=False):
    create: GoogleAdsSearchads360V23Resources__Label
    remove: str
    update: GoogleAdsSearchads360V23Resources__Label
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListAccessibleCustomersResponse(
    typing.TypedDict, total=False
):
    resourceNames: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListAudienceInsightsAttributesRequest(
    typing.TypedDict, total=False
):
    customerInsightsGroup: str
    dimensions: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "CATEGORY",
            "KNOWLEDGE_GRAPH",
            "GEO_TARGET_COUNTRY",
            "SUB_COUNTRY_LOCATION",
            "YOUTUBE_CHANNEL",
            "AFFINITY_USER_INTEREST",
            "IN_MARKET_USER_INTEREST",
            "PARENTAL_STATUS",
            "INCOME_RANGE",
            "AGE_RANGE",
            "GENDER",
            "YOUTUBE_VIDEO",
            "DEVICE",
            "YOUTUBE_LINEUP",
            "USER_LIST",
            "LIFE_EVENT_USER_INTEREST",
        ]
    ]
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    locationCountryFilters: _list[GoogleAdsSearchads360V23Common__LocationInfo]
    queryText: str
    youtubeReachLocation: GoogleAdsSearchads360V23Common__LocationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListAudienceInsightsAttributesResponse(
    typing.TypedDict, total=False
):
    attributes: _list[GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBatchJobResultsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    results: _list[GoogleAdsSearchads360V23Services__BatchJobResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksAvailableDatesRequest(
    typing.TypedDict, total=False
):
    applicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksAvailableDatesResponse(
    typing.TypedDict, total=False
):
    supportedDates: GoogleAdsSearchads360V23Common__DateRange

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksLocationsRequest(
    typing.TypedDict, total=False
):
    applicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksLocationsResponse(
    typing.TypedDict, total=False
):
    benchmarksLocations: _list[GoogleAdsSearchads360V23Services__BenchmarksLocation]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksProductsRequest(
    typing.TypedDict, total=False
):
    applicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksProductsResponse(
    typing.TypedDict, total=False
):
    benchmarksProducts: _list[
        GoogleAdsSearchads360V23Services__BenchmarksProductMetadata
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksSourcesRequest(
    typing.TypedDict, total=False
):
    applicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    benchmarksSources: _list[
        typing.Literal["UNSPECIFIED", "UNKNOWN", "INDUSTRY_VERTICAL"]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksSourcesResponse(
    typing.TypedDict, total=False
):
    benchmarksSources: _list[GoogleAdsSearchads360V23Services__BenchmarksSourceMetadata]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponse(
    typing.TypedDict, total=False
):
    errors: _list[GoogleRpc__Status]
    nextPageToken: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListCustomColumnsResponse(
    typing.TypedDict, total=False
):
    customColumns: _list[GoogleAdsSearchads360V23Resources__CustomColumn]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponse(
    typing.TypedDict, total=False
):
    errors: _list[GoogleRpc__Status]
    nextPageToken: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListInsightsEligibleDatesRequest(
    typing.TypedDict, total=False
):
    insightsApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListInsightsEligibleDatesResponse(
    typing.TypedDict, total=False
):
    dataMonths: _list[str]
    lastThirtyDays: GoogleAdsSearchads360V23Common__DateRange

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListInvoicesResponse(
    typing.TypedDict, total=False
):
    invoices: _list[GoogleAdsSearchads360V23Resources__Invoice]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPaymentsAccountsResponse(
    typing.TypedDict, total=False
):
    paymentsAccounts: _list[GoogleAdsSearchads360V23Resources__PaymentsAccount]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableLocationsRequest(
    typing.TypedDict, total=False
):
    reachApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableLocationsResponse(
    typing.TypedDict, total=False
):
    plannableLocations: _list[GoogleAdsSearchads360V23Services__PlannableLocation]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableProductsRequest(
    typing.TypedDict, total=False
):
    plannableLocationId: str
    reachApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableProductsResponse(
    typing.TypedDict, total=False
):
    productMetadata: _list[GoogleAdsSearchads360V23Services__ProductMetadata]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableUserInterestsRequest(
    typing.TypedDict, total=False
):
    customerId: str
    nameQuery: str
    pathQuery: str
    reachApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo
    userInterestTaxonomyTypes: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "AFFINITY",
            "IN_MARKET",
            "MOBILE_APP_INSTALL_USER",
            "VERTICAL_GEO",
            "NEW_SMART_PHONE_USER",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableUserInterestsResponse(
    typing.TypedDict, total=False
):
    plannableUserInterests: _list[
        GoogleAdsSearchads360V23Services__PlannableUserInterest
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableUserListsRequest(
    typing.TypedDict, total=False
):
    customerId: str
    customerReachGroup: str
    reachApplicationInfo: GoogleAdsSearchads360V23Common__AdditionalApplicationInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableUserListsResponse(
    typing.TypedDict, total=False
):
    plannableUserLists: _list[GoogleAdsSearchads360V23Services__PlannableUserList]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ManualCpcBiddingStrategy(
    typing.TypedDict, total=False
):
    dailyBudgetMicros: str
    maxCpcBidMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MaximizeClicksBiddingStrategy(
    typing.TypedDict, total=False
):
    dailyTargetSpendMicros: str
    maxCpcBidCeilingMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MaximizeConversionsBiddingStrategy(
    typing.TypedDict, total=False
):
    dailyTargetSpendMicros: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MetricAttributes(typing.TypedDict, total=False):
    attributes: _list[GoogleAdsSearchads360V23Services_MetricAttributes_Attribute]
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__Metrics(typing.TypedDict, total=False):
    averageRateMetrics: GoogleAdsSearchads360V23Services__RateMetrics

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MoveManagerLinkRequest(
    typing.TypedDict, total=False
):
    newManager: str
    previousCustomerManagerLink: str
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MoveManagerLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__AccountBudgetProposalOperation
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountLinkRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__AccountLinkOperation
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountLinkResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    result: GoogleAdsSearchads360V23Services__MutateAccountLinkResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountLinkResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupAdLabelOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdResult(
    typing.TypedDict, total=False
):
    adGroupAd: GoogleAdsSearchads360V23Resources__AdGroupAd
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupAdOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupAdResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetResult(
    typing.TypedDict, total=False
):
    adGroupAsset: GoogleAdsSearchads360V23Resources__AdGroupAsset
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetResult(
    typing.TypedDict, total=False
):
    adGroupAssetSet: GoogleAdsSearchads360V23Resources__AdGroupAssetSet
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupAssetSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupAssetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupAssetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupBidModifierResult(
    typing.TypedDict, total=False
):
    adGroupBidModifier: GoogleAdsSearchads360V23Resources__AdGroupBidModifier
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupBidModifiersRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupBidModifierOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupBidModifiersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupBidModifierResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriteriaRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupCriterionOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriteriaResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupCriterionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizerResult(
    typing.TypedDict, total=False
):
    adGroupCriterionCustomizer: (
        GoogleAdsSearchads360V23Resources__AdGroupCriterionCustomizer
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizersRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__AdGroupCriterionCustomizerOperation
    ]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizerResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupCriterionLabelOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionResult(
    typing.TypedDict, total=False
):
    adGroupCriterion: GoogleAdsSearchads360V23Resources__AdGroupCriterion
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCustomizerResult(
    typing.TypedDict, total=False
):
    adGroupCustomizer: GoogleAdsSearchads360V23Resources__AdGroupCustomizer
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCustomizersRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupCustomizerOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCustomizersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupCustomizerResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupLabelResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupLabelsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupLabelOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupLabelsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupLabelResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupResult(
    typing.TypedDict, total=False
):
    adGroup: GoogleAdsSearchads360V23Resources__AdGroup
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdGroupOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdGroupResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdParameterResult(
    typing.TypedDict, total=False
):
    adParameter: GoogleAdsSearchads360V23Resources__AdParameter
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdParametersRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AdParameterOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdParametersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdParameterResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdResult(typing.TypedDict, total=False):
    ad: GoogleAdsSearchads360V23Resources__Ad
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdsRequest(typing.TypedDict, total=False):
    operations: _list[GoogleAdsSearchads360V23Services__AdOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAdResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupAssetResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupAssetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AssetGroupAssetOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupAssetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAssetGroupAssetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFilterResult(
    typing.TypedDict, total=False
):
    assetGroupListingGroupFilter: (
        GoogleAdsSearchads360V23Resources__AssetGroupListingGroupFilter
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFiltersRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__AssetGroupListingGroupFilterOperation
    ]
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFiltersResponse(
    typing.TypedDict, total=False
):
    results: _list[
        GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFilterResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupSignalResult(
    typing.TypedDict, total=False
):
    assetGroupSignal: GoogleAdsSearchads360V23Resources__AssetGroupSignal
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupSignalsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AssetGroupSignalOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupSignalsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAssetGroupSignalResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AssetGroupOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAssetGroupResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetResult(
    typing.TypedDict, total=False
):
    asset: GoogleAdsSearchads360V23Resources__Asset
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetAssetResult(
    typing.TypedDict, total=False
):
    assetSetAsset: GoogleAdsSearchads360V23Resources__AssetSetAsset
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetAssetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AssetSetAssetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetAssetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAssetSetAssetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetResult(
    typing.TypedDict, total=False
):
    assetSet: GoogleAdsSearchads360V23Resources__AssetSet
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AssetSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAssetSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AssetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAssetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAudienceResult(
    typing.TypedDict, total=False
):
    audience: GoogleAdsSearchads360V23Resources__Audience
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAudiencesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__AudienceOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAudiencesResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateAudienceResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBatchJobRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__BatchJobOperation

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBatchJobResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateBatchJobResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBatchJobResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__BiddingDataExclusionOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResult(
    typing.TypedDict, total=False
):
    biddingDataExclusion: GoogleAdsSearchads360V23Resources__BiddingDataExclusion
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__BiddingSeasonalityAdjustmentOperation
    ]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResult(
    typing.TypedDict, total=False
):
    biddingSeasonalityAdjustment: (
        GoogleAdsSearchads360V23Resources__BiddingSeasonalityAdjustment
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingStrategiesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__BiddingStrategyOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingStrategiesResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateBiddingStrategyResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingStrategyResult(
    typing.TypedDict, total=False
):
    biddingStrategy: GoogleAdsSearchads360V23Resources__BiddingStrategy
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBillingSetupRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__BillingSetupOperation

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBillingSetupResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateBillingSetupResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBillingSetupResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetResult(
    typing.TypedDict, total=False
):
    campaignAsset: GoogleAdsSearchads360V23Resources__CampaignAsset
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetSetResult(
    typing.TypedDict, total=False
):
    campaignAssetSet: GoogleAdsSearchads360V23Resources__CampaignAssetSet
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignAssetSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignAssetSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignAssetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignAssetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBidModifierResult(
    typing.TypedDict, total=False
):
    campaignBidModifier: GoogleAdsSearchads360V23Resources__CampaignBidModifier
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBidModifiersRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignBidModifierOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBidModifiersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignBidModifierResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBudgetResult(
    typing.TypedDict, total=False
):
    campaignBudget: GoogleAdsSearchads360V23Resources__CampaignBudget
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBudgetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignBudgetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBudgetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignBudgetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignConversionGoalOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalsResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCriteriaRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignCriterionOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCriteriaResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignCriterionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCriterionResult(
    typing.TypedDict, total=False
):
    campaignCriterion: GoogleAdsSearchads360V23Resources__CampaignCriterion
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCustomizerResult(
    typing.TypedDict, total=False
):
    campaignCustomizer: GoogleAdsSearchads360V23Resources__CampaignCustomizer
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCustomizersRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignCustomizerOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCustomizersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignCustomizerResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignDraftResult(
    typing.TypedDict, total=False
):
    campaignDraft: GoogleAdsSearchads360V23Resources__CampaignDraft
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignDraftsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignDraftOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignDraftsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignDraftResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignGoalConfigOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGroupResult(
    typing.TypedDict, total=False
):
    campaignGroup: GoogleAdsSearchads360V23Resources__CampaignGroup
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGroupsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignGroupOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGroupsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignGroupResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignLabelResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignLabelsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignLabelOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignLabelsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignLabelResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignResult(
    typing.TypedDict, total=False
):
    campaign: GoogleAdsSearchads360V23Resources__Campaign
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignSharedSetResult(
    typing.TypedDict, total=False
):
    campaignSharedSet: GoogleAdsSearchads360V23Resources__CampaignSharedSet
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignSharedSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignSharedSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignSharedSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignSharedSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CampaignOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCampaignResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionActionResult(
    typing.TypedDict, total=False
):
    conversionAction: GoogleAdsSearchads360V23Resources__ConversionAction
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionActionsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__ConversionActionOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionActionsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateConversionActionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionCustomVariableResult(
    typing.TypedDict, total=False
):
    conversionCustomVariable: (
        GoogleAdsSearchads360V23Resources__ConversionCustomVariable
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionCustomVariablesRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__ConversionCustomVariableOperation
    ]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionCustomVariablesResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateConversionCustomVariableResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigResult(
    typing.TypedDict, total=False
):
    conversionGoalCampaignConfig: (
        GoogleAdsSearchads360V23Resources__ConversionGoalCampaignConfig
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigsRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__ConversionGoalCampaignConfigOperation
    ]
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigsResponse(
    typing.TypedDict, total=False
):
    results: _list[
        GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRuleResult(
    typing.TypedDict, total=False
):
    conversionValueRule: GoogleAdsSearchads360V23Resources__ConversionValueRule
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetResult(
    typing.TypedDict, total=False
):
    conversionValueRuleSet: GoogleAdsSearchads360V23Resources__ConversionValueRuleSet
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__ConversionValueRuleSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRulesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__ConversionValueRuleOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRulesResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateConversionValueRuleResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomAudienceResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomAudiencesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomAudienceOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomAudiencesResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomAudienceResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomConversionGoalResult(
    typing.TypedDict, total=False
):
    customConversionGoal: GoogleAdsSearchads360V23Resources__CustomConversionGoal
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomConversionGoalsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomConversionGoalOperation]
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomConversionGoalsResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomConversionGoalResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomInterestResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomInterestsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomInterestOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomInterestsResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomInterestResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetResult(
    typing.TypedDict, total=False
):
    customerAsset: GoogleAdsSearchads360V23Resources__CustomerAsset
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetSetResult(
    typing.TypedDict, total=False
):
    customerAssetSet: GoogleAdsSearchads360V23Resources__CustomerAssetSet
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomerAssetSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomerAssetSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomerAssetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomerAssetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerClientLinkRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__CustomerClientLinkOperation
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerClientLinkResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateCustomerClientLinkResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerClientLinkResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomerConversionGoalOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalsResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerCustomizerResult(
    typing.TypedDict, total=False
):
    customerCustomizer: GoogleAdsSearchads360V23Resources__CustomerCustomizer
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerCustomizersRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomerCustomizerOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerCustomizersResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomerCustomizerResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerLabelResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerLabelsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomerLabelOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerLabelsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomerLabelResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomerManagerLinkOperation]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__CustomerNegativeCriterionOperation
    ]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResult(
    typing.TypedDict, total=False
):
    customerNegativeCriterion: (
        GoogleAdsSearchads360V23Resources__CustomerNegativeCriterion
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__CustomerOperation
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateCustomerResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerResult(
    typing.TypedDict, total=False
):
    customer: GoogleAdsSearchads360V23Resources__Customer
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaRequest(
    typing.TypedDict, total=False
):
    enableWarnings: bool
    operation: GoogleAdsSearchads360V23Services__CustomerSkAdNetworkConversionValueSchemaOperation
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaResult
    warning: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaResult(
    typing.TypedDict, total=False
):
    appId: str
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__CustomerUserAccessInvitationOperation

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessRequest(
    typing.TypedDict, total=False
):
    operation: GoogleAdsSearchads360V23Services__CustomerUserAccessOperation

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessResponse(
    typing.TypedDict, total=False
):
    result: GoogleAdsSearchads360V23Services__MutateCustomerUserAccessResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomizerAttributeResult(
    typing.TypedDict, total=False
):
    customizerAttribute: GoogleAdsSearchads360V23Resources__CustomizerAttribute
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomizerAttributesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__CustomizerAttributeOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomizerAttributesResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateCustomizerAttributeResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentArmResult(
    typing.TypedDict, total=False
):
    experimentArm: GoogleAdsSearchads360V23Resources__ExperimentArm
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentArmsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__ExperimentArmOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentArmsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateExperimentArmResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__ExperimentOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateExperimentResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateGoalResult(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateGoalsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__GoalOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateGoalsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateGoalResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordsRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__KeywordPlanAdGroupKeywordOperation
    ]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__KeywordPlanAdGroupOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordsRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__KeywordPlanCampaignKeywordOperation
    ]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__KeywordPlanCampaignOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlansRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__KeywordPlanOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlansResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateKeywordPlansResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlansResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateLabelResult(
    typing.TypedDict, total=False
):
    label: GoogleAdsSearchads360V23Resources__Label
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateLabelsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__LabelOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateLabelsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateLabelResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateOperation(typing.TypedDict, total=False):
    adGroupAdLabelOperation: GoogleAdsSearchads360V23Services__AdGroupAdLabelOperation
    adGroupAdOperation: GoogleAdsSearchads360V23Services__AdGroupAdOperation
    adGroupAssetOperation: GoogleAdsSearchads360V23Services__AdGroupAssetOperation
    adGroupBidModifierOperation: (
        GoogleAdsSearchads360V23Services__AdGroupBidModifierOperation
    )
    adGroupCriterionCustomizerOperation: (
        GoogleAdsSearchads360V23Services__AdGroupCriterionCustomizerOperation
    )
    adGroupCriterionLabelOperation: (
        GoogleAdsSearchads360V23Services__AdGroupCriterionLabelOperation
    )
    adGroupCriterionOperation: (
        GoogleAdsSearchads360V23Services__AdGroupCriterionOperation
    )
    adGroupCustomizerOperation: (
        GoogleAdsSearchads360V23Services__AdGroupCustomizerOperation
    )
    adGroupLabelOperation: GoogleAdsSearchads360V23Services__AdGroupLabelOperation
    adGroupOperation: GoogleAdsSearchads360V23Services__AdGroupOperation
    adOperation: GoogleAdsSearchads360V23Services__AdOperation
    adParameterOperation: GoogleAdsSearchads360V23Services__AdParameterOperation
    assetGroupAssetOperation: GoogleAdsSearchads360V23Services__AssetGroupAssetOperation
    assetGroupListingGroupFilterOperation: (
        GoogleAdsSearchads360V23Services__AssetGroupListingGroupFilterOperation
    )
    assetGroupOperation: GoogleAdsSearchads360V23Services__AssetGroupOperation
    assetGroupSignalOperation: (
        GoogleAdsSearchads360V23Services__AssetGroupSignalOperation
    )
    assetOperation: GoogleAdsSearchads360V23Services__AssetOperation
    assetSetAssetOperation: GoogleAdsSearchads360V23Services__AssetSetAssetOperation
    assetSetOperation: GoogleAdsSearchads360V23Services__AssetSetOperation
    audienceOperation: GoogleAdsSearchads360V23Services__AudienceOperation
    biddingDataExclusionOperation: (
        GoogleAdsSearchads360V23Services__BiddingDataExclusionOperation
    )
    biddingSeasonalityAdjustmentOperation: (
        GoogleAdsSearchads360V23Services__BiddingSeasonalityAdjustmentOperation
    )
    biddingStrategyOperation: GoogleAdsSearchads360V23Services__BiddingStrategyOperation
    campaignAssetOperation: GoogleAdsSearchads360V23Services__CampaignAssetOperation
    campaignAssetSetOperation: (
        GoogleAdsSearchads360V23Services__CampaignAssetSetOperation
    )
    campaignBidModifierOperation: (
        GoogleAdsSearchads360V23Services__CampaignBidModifierOperation
    )
    campaignBudgetOperation: GoogleAdsSearchads360V23Services__CampaignBudgetOperation
    campaignConversionGoalOperation: (
        GoogleAdsSearchads360V23Services__CampaignConversionGoalOperation
    )
    campaignCriterionOperation: (
        GoogleAdsSearchads360V23Services__CampaignCriterionOperation
    )
    campaignCustomizerOperation: (
        GoogleAdsSearchads360V23Services__CampaignCustomizerOperation
    )
    campaignDraftOperation: GoogleAdsSearchads360V23Services__CampaignDraftOperation
    campaignGroupOperation: GoogleAdsSearchads360V23Services__CampaignGroupOperation
    campaignLabelOperation: GoogleAdsSearchads360V23Services__CampaignLabelOperation
    campaignOperation: GoogleAdsSearchads360V23Services__CampaignOperation
    campaignSharedSetOperation: (
        GoogleAdsSearchads360V23Services__CampaignSharedSetOperation
    )
    conversionActionOperation: (
        GoogleAdsSearchads360V23Services__ConversionActionOperation
    )
    conversionCustomVariableOperation: (
        GoogleAdsSearchads360V23Services__ConversionCustomVariableOperation
    )
    conversionGoalCampaignConfigOperation: (
        GoogleAdsSearchads360V23Services__ConversionGoalCampaignConfigOperation
    )
    conversionValueRuleOperation: (
        GoogleAdsSearchads360V23Services__ConversionValueRuleOperation
    )
    conversionValueRuleSetOperation: (
        GoogleAdsSearchads360V23Services__ConversionValueRuleSetOperation
    )
    customConversionGoalOperation: (
        GoogleAdsSearchads360V23Services__CustomConversionGoalOperation
    )
    customerAssetOperation: GoogleAdsSearchads360V23Services__CustomerAssetOperation
    customerConversionGoalOperation: (
        GoogleAdsSearchads360V23Services__CustomerConversionGoalOperation
    )
    customerCustomizerOperation: (
        GoogleAdsSearchads360V23Services__CustomerCustomizerOperation
    )
    customerLabelOperation: GoogleAdsSearchads360V23Services__CustomerLabelOperation
    customerNegativeCriterionOperation: (
        GoogleAdsSearchads360V23Services__CustomerNegativeCriterionOperation
    )
    customerOperation: GoogleAdsSearchads360V23Services__CustomerOperation
    customizerAttributeOperation: (
        GoogleAdsSearchads360V23Services__CustomizerAttributeOperation
    )
    experimentArmOperation: GoogleAdsSearchads360V23Services__ExperimentArmOperation
    experimentOperation: GoogleAdsSearchads360V23Services__ExperimentOperation
    keywordPlanAdGroupKeywordOperation: (
        GoogleAdsSearchads360V23Services__KeywordPlanAdGroupKeywordOperation
    )
    keywordPlanAdGroupOperation: (
        GoogleAdsSearchads360V23Services__KeywordPlanAdGroupOperation
    )
    keywordPlanCampaignKeywordOperation: (
        GoogleAdsSearchads360V23Services__KeywordPlanCampaignKeywordOperation
    )
    keywordPlanCampaignOperation: (
        GoogleAdsSearchads360V23Services__KeywordPlanCampaignOperation
    )
    keywordPlanOperation: GoogleAdsSearchads360V23Services__KeywordPlanOperation
    labelOperation: GoogleAdsSearchads360V23Services__LabelOperation
    recommendationSubscriptionOperation: (
        GoogleAdsSearchads360V23Services__RecommendationSubscriptionOperation
    )
    remarketingActionOperation: (
        GoogleAdsSearchads360V23Services__RemarketingActionOperation
    )
    searchAds360CampaignOperation: (
        GoogleAdsSearchads360V23Services__SearchAds360CampaignOperation
    )
    sharedCriterionOperation: GoogleAdsSearchads360V23Services__SharedCriterionOperation
    sharedSetOperation: GoogleAdsSearchads360V23Services__SharedSetOperation
    smartCampaignSettingOperation: (
        GoogleAdsSearchads360V23Services__SmartCampaignSettingOperation
    )
    userListOperation: GoogleAdsSearchads360V23Services__UserListOperation

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateOperationResponse(
    typing.TypedDict, total=False
):
    adGroupAdLabelResult: GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelResult
    adGroupAdResult: GoogleAdsSearchads360V23Services__MutateAdGroupAdResult
    adGroupAssetResult: GoogleAdsSearchads360V23Services__MutateAdGroupAssetResult
    adGroupBidModifierResult: (
        GoogleAdsSearchads360V23Services__MutateAdGroupBidModifierResult
    )
    adGroupCriterionCustomizerResult: (
        GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizerResult
    )
    adGroupCriterionLabelResult: (
        GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelResult
    )
    adGroupCriterionResult: (
        GoogleAdsSearchads360V23Services__MutateAdGroupCriterionResult
    )
    adGroupCustomizerResult: (
        GoogleAdsSearchads360V23Services__MutateAdGroupCustomizerResult
    )
    adGroupLabelResult: GoogleAdsSearchads360V23Services__MutateAdGroupLabelResult
    adGroupResult: GoogleAdsSearchads360V23Services__MutateAdGroupResult
    adParameterResult: GoogleAdsSearchads360V23Services__MutateAdParameterResult
    adResult: GoogleAdsSearchads360V23Services__MutateAdResult
    assetGroupAssetResult: GoogleAdsSearchads360V23Services__MutateAssetGroupAssetResult
    assetGroupListingGroupFilterResult: (
        GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFilterResult
    )
    assetGroupResult: GoogleAdsSearchads360V23Services__MutateAssetGroupResult
    assetGroupSignalResult: (
        GoogleAdsSearchads360V23Services__MutateAssetGroupSignalResult
    )
    assetResult: GoogleAdsSearchads360V23Services__MutateAssetResult
    assetSetAssetResult: GoogleAdsSearchads360V23Services__MutateAssetSetAssetResult
    assetSetResult: GoogleAdsSearchads360V23Services__MutateAssetSetResult
    audienceResult: GoogleAdsSearchads360V23Services__MutateAudienceResult
    biddingDataExclusionResult: (
        GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResult
    )
    biddingSeasonalityAdjustmentResult: (
        GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResult
    )
    biddingStrategyResult: GoogleAdsSearchads360V23Services__MutateBiddingStrategyResult
    campaignAssetResult: GoogleAdsSearchads360V23Services__MutateCampaignAssetResult
    campaignAssetSetResult: (
        GoogleAdsSearchads360V23Services__MutateCampaignAssetSetResult
    )
    campaignBidModifierResult: (
        GoogleAdsSearchads360V23Services__MutateCampaignBidModifierResult
    )
    campaignBudgetResult: GoogleAdsSearchads360V23Services__MutateCampaignBudgetResult
    campaignConversionGoalResult: (
        GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalResult
    )
    campaignCriterionResult: (
        GoogleAdsSearchads360V23Services__MutateCampaignCriterionResult
    )
    campaignCustomizerResult: (
        GoogleAdsSearchads360V23Services__MutateCampaignCustomizerResult
    )
    campaignDraftResult: GoogleAdsSearchads360V23Services__MutateCampaignDraftResult
    campaignGroupResult: GoogleAdsSearchads360V23Services__MutateCampaignGroupResult
    campaignLabelResult: GoogleAdsSearchads360V23Services__MutateCampaignLabelResult
    campaignResult: GoogleAdsSearchads360V23Services__MutateCampaignResult
    campaignSharedSetResult: (
        GoogleAdsSearchads360V23Services__MutateCampaignSharedSetResult
    )
    conversionActionResult: (
        GoogleAdsSearchads360V23Services__MutateConversionActionResult
    )
    conversionCustomVariableResult: (
        GoogleAdsSearchads360V23Services__MutateConversionCustomVariableResult
    )
    conversionGoalCampaignConfigResult: (
        GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigResult
    )
    conversionValueRuleResult: (
        GoogleAdsSearchads360V23Services__MutateConversionValueRuleResult
    )
    conversionValueRuleSetResult: (
        GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetResult
    )
    customConversionGoalResult: (
        GoogleAdsSearchads360V23Services__MutateCustomConversionGoalResult
    )
    customerAssetResult: GoogleAdsSearchads360V23Services__MutateCustomerAssetResult
    customerConversionGoalResult: (
        GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalResult
    )
    customerCustomizerResult: (
        GoogleAdsSearchads360V23Services__MutateCustomerCustomizerResult
    )
    customerLabelResult: GoogleAdsSearchads360V23Services__MutateCustomerLabelResult
    customerNegativeCriterionResult: (
        GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResult
    )
    customerResult: GoogleAdsSearchads360V23Services__MutateCustomerResult
    customizerAttributeResult: (
        GoogleAdsSearchads360V23Services__MutateCustomizerAttributeResult
    )
    experimentArmResult: GoogleAdsSearchads360V23Services__MutateExperimentArmResult
    experimentResult: GoogleAdsSearchads360V23Services__MutateExperimentResult
    keywordPlanAdGroupKeywordResult: (
        GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordResult
    )
    keywordPlanAdGroupResult: (
        GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupResult
    )
    keywordPlanCampaignKeywordResult: (
        GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordResult
    )
    keywordPlanCampaignResult: (
        GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignResult
    )
    keywordPlanResult: GoogleAdsSearchads360V23Services__MutateKeywordPlansResult
    labelResult: GoogleAdsSearchads360V23Services__MutateLabelResult
    recommendationSubscriptionResult: (
        GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResult
    )
    remarketingActionResult: (
        GoogleAdsSearchads360V23Services__MutateRemarketingActionResult
    )
    searchAds360CampaignResult: (
        GoogleAdsSearchads360V23Services__MutateSearchAds360CampaignResult
    )
    sharedCriterionResult: GoogleAdsSearchads360V23Services__MutateSharedCriterionResult
    sharedSetResult: GoogleAdsSearchads360V23Services__MutateSharedSetResult
    smartCampaignSettingResult: (
        GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingResult
    )
    userListResult: GoogleAdsSearchads360V23Services__MutateUserListResult

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__RecommendationSubscriptionOperation
    ]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[
        GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResult
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResult(
    typing.TypedDict, total=False
):
    recommendationSubscription: (
        GoogleAdsSearchads360V23Resources__RecommendationSubscription
    )
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRemarketingActionResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRemarketingActionsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__RemarketingActionOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRemarketingActionsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateRemarketingActionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSearchAds360CampaignResult(
    typing.TypedDict, total=False
):
    resourceName: str
    searchAds360Campaign: GoogleAdsSearchads360V23Resources__SearchAds360Campaign

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSearchAds360CampaignsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__SearchAds360CampaignOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSearchAds360CampaignsResponse(
    typing.TypedDict, total=False
):
    results: _list[GoogleAdsSearchads360V23Services__MutateSearchAds360CampaignResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSearchAds360Request(
    typing.TypedDict, total=False
):
    mutateOperations: _list[GoogleAdsSearchads360V23Services__MutateOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSearchAds360Response(
    typing.TypedDict, total=False
):
    mutateOperationResponses: _list[
        GoogleAdsSearchads360V23Services__MutateOperationResponse
    ]
    partialFailureError: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedCriteriaRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__SharedCriterionOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedCriteriaResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateSharedCriterionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedCriterionResult(
    typing.TypedDict, total=False
):
    resourceName: str
    sharedCriterion: GoogleAdsSearchads360V23Resources__SharedCriterion

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedSetResult(
    typing.TypedDict, total=False
):
    resourceName: str
    sharedSet: GoogleAdsSearchads360V23Resources__SharedSet

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedSetsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__SharedSetOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedSetsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateSharedSetResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingResult(
    typing.TypedDict, total=False
):
    resourceName: str
    smartCampaignSetting: GoogleAdsSearchads360V23Resources__SmartCampaignSetting

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__SmartCampaignSettingOperation]
    partialFailure: bool
    responseContentType: typing.Literal[
        "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
    ]
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListCustomerTypeResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListCustomerTypesRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__UserListCustomerTypeOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListCustomerTypesResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateUserListCustomerTypeResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListResult(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListsRequest(
    typing.TypedDict, total=False
):
    operations: _list[GoogleAdsSearchads360V23Services__UserListOperation]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__MutateUserListResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__OfflineUserDataJobOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Common__UserData
    remove: GoogleAdsSearchads360V23Common__UserData
    removeAll: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__OnTargetAudienceMetrics(
    typing.TypedDict, total=False
):
    censusAudienceSize: str
    youtubeAudienceSize: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannableLocation(
    typing.TypedDict, total=False
):
    countryCode: str
    id: str
    locationType: str
    name: str
    parentCountryId: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannableTargeting(
    typing.TypedDict, total=False
):
    ageRanges: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "AGE_RANGE_18_24",
            "AGE_RANGE_18_34",
            "AGE_RANGE_18_44",
            "AGE_RANGE_18_49",
            "AGE_RANGE_18_54",
            "AGE_RANGE_18_64",
            "AGE_RANGE_18_65_UP",
            "AGE_RANGE_21_34",
            "AGE_RANGE_25_34",
            "AGE_RANGE_25_44",
            "AGE_RANGE_25_49",
            "AGE_RANGE_25_54",
            "AGE_RANGE_25_64",
            "AGE_RANGE_25_65_UP",
            "AGE_RANGE_35_44",
            "AGE_RANGE_35_49",
            "AGE_RANGE_35_54",
            "AGE_RANGE_35_64",
            "AGE_RANGE_35_65_UP",
            "AGE_RANGE_45_54",
            "AGE_RANGE_45_64",
            "AGE_RANGE_45_65_UP",
            "AGE_RANGE_50_65_UP",
            "AGE_RANGE_55_64",
            "AGE_RANGE_55_65_UP",
            "AGE_RANGE_65_UP",
        ]
    ]
    devices: _list[GoogleAdsSearchads360V23Common__DeviceInfo]
    genders: _list[GoogleAdsSearchads360V23Common__GenderInfo]
    networks: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "YOUTUBE",
            "GOOGLE_VIDEO_PARTNERS",
            "YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS",
        ]
    ]
    surfaceTargeting: GoogleAdsSearchads360V23Services__SurfaceTargetingCombinations
    youtubeSelectLineups: _list[GoogleAdsSearchads360V23Services__YouTubeSelectLineUp]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannableUserInterest(
    typing.TypedDict, total=False
):
    userInterest: GoogleAdsSearchads360V23Common__UserInterestInfo
    userInterestDisplayName: str
    userInterestPath: str
    userInterestType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AFFINITY",
        "IN_MARKET",
        "MOBILE_APP_INSTALL_USER",
        "VERTICAL_GEO",
        "NEW_SMART_PHONE_USER",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannableUserList(
    typing.TypedDict, total=False
):
    displayName: str
    plannableStatus: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "PLANNABLE", "UNPLANNABLE"
    ]
    plannableUserListMetadata: (
        GoogleAdsSearchads360V23Services__PlannableUserListMetadata
    )
    userListInfo: GoogleAdsSearchads360V23Common__UserListInfo
    userListType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REMARKETING",
        "LOGICAL",
        "EXTERNAL_REMARKETING",
        "RULE_BASED",
        "SIMILAR",
        "CRM_BASED",
        "LOOKALIKE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannableUserListMetadata(
    typing.TypedDict, total=False
):
    userListCrmDataSourceType: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "FIRST_PARTY",
        "THIRD_PARTY_CREDIT_BUREAU",
        "THIRD_PARTY_VOTER_FILE",
        "THIRD_PARTY_PARTNER_DATA",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannedProduct(typing.TypedDict, total=False):
    advancedProductTargeting: GoogleAdsSearchads360V23Services__AdvancedProductTargeting
    budgetMicros: str
    conversionRate: float
    plannableProductCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannedProductForecast(
    typing.TypedDict, total=False
):
    averageFrequency: float
    conversions: float
    onTargetCoviewImpressions: str
    onTargetCoviewReach: str
    onTargetImpressions: str
    onTargetReach: str
    totalCoviewImpressions: str
    totalCoviewReach: str
    totalImpressions: str
    totalReach: str
    trueviewViews: str
    viewableImpressions: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PlannedProductReachForecast(
    typing.TypedDict, total=False
):
    costMicros: str
    plannableProductCode: str
    plannedProductForecast: GoogleAdsSearchads360V23Services__PlannedProductForecast

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ProductFilter(typing.TypedDict, total=False):
    marketingObjectiveList: (
        GoogleAdsSearchads360V23Services_ProductFilter_MarketingObjectiveList
    )
    productList: GoogleAdsSearchads360V23Services_ProductFilter_ProductList

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ProductMetadata(typing.TypedDict, total=False):
    plannableProductCode: str
    plannableProductName: str
    plannableTargeting: GoogleAdsSearchads360V23Services__PlannableTargeting

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PromoteCampaignDraftRequest(
    typing.TypedDict, total=False
):
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PromoteExperimentMetadata(
    typing.TypedDict, total=False
):
    experiment: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__PromoteExperimentRequest(
    typing.TypedDict, total=False
):
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ProvideLeadFeedbackRequest(
    typing.TypedDict, total=False
):
    surveyAnswer: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "VERY_SATISFIED",
        "SATISFIED",
        "NEUTRAL",
        "DISSATISFIED",
        "VERY_DISSATISFIED",
    ]
    surveyDissatisfied: GoogleAdsSearchads360V23Services__SurveyDissatisfied
    surveySatisfied: GoogleAdsSearchads360V23Services__SurveySatisfied

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ProvideLeadFeedbackResponse(
    typing.TypedDict, total=False
):
    creditIssuanceDecision: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "SUCCESS_NOT_REACHED_THRESHOLD",
        "SUCCESS_REACHED_THRESHOLD",
        "FAIL_OVER_THRESHOLD",
        "FAIL_NOT_ELIGIBLE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RateMetrics(typing.TypedDict, total=False):
    activeViewViewability: float
    averageActiveViewCpm: float
    averageCpc: float
    averageCpe: float
    averageCpi: float
    averageCpm: float
    clickThroughRate: float
    engagementRate: float
    interactionRate: float
    trueviewAverageCpv: float
    trueviewViewRate: float
    videoCompletionP100Rate: float
    videoCompletionP25Rate: float
    videoCompletionP50Rate: float
    videoCompletionP75Rate: float

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RawEventConversionDimensionHeader(
    typing.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RawEventConversionMetricHeader(
    typing.TypedDict, total=False
):
    id: str
    name: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ReachCurve(typing.TypedDict, total=False):
    reachForecasts: _list[GoogleAdsSearchads360V23Services__ReachForecast]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ReachForecast(typing.TypedDict, total=False):
    costMicros: str
    forecast: GoogleAdsSearchads360V23Services__Forecast
    plannedProductReachForecasts: _list[
        GoogleAdsSearchads360V23Services__PlannedProductReachForecast
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RecommendationSubscriptionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__RecommendationSubscription
    update: GoogleAdsSearchads360V23Resources__RecommendationSubscription
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RegenerateShareableLinkIdRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RegenerateShareableLinkIdResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemarketingActionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__RemarketingAction
    update: GoogleAdsSearchads360V23Resources__RemarketingAction
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveAutomaticallyCreatedAssetsRequest(
    typing.TypedDict, total=False
):
    assetsWithFieldType: _list[GoogleAdsSearchads360V23Services__AssetsWithFieldType]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetOperation(
    typing.TypedDict, total=False
):
    asset: str
    campaign: str
    fieldType: typing.Literal[
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
        "DEMAND_GEN_CAROUSEL_CARD",
        "BUSINESS_MESSAGE",
        "TALL_PORTRAIT_MARKETING_IMAGE",
        "LANDING_PAGE_PREVIEW",
        "LONG_DESCRIPTION",
        "CALL_TO_ACTION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetRequest(
    typing.TypedDict, total=False
):
    operations: _list[
        GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetOperation
    ]
    partialFailure: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveDataLinkRequest(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveDataLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveProductLinkInvitationRequest(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveProductLinkInvitationResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveProductLinkRequest(
    typing.TypedDict, total=False
):
    resourceName: str
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveProductLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RestatementValue(typing.TypedDict, total=False):
    adjustedValue: float
    currencyCode: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RunBatchJobRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RunOfflineUserDataJobRequest(
    typing.TypedDict, total=False
):
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ScheduleExperimentMetadata(
    typing.TypedDict, total=False
):
    experiment: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ScheduleExperimentRequest(
    typing.TypedDict, total=False
):
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchAds360CampaignOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__SearchAds360Campaign
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchAds360Row(typing.TypedDict, total=False):
    accessibleBiddingStrategy: (
        GoogleAdsSearchads360V23Resources__AccessibleBiddingStrategy
    )
    accountBudget: GoogleAdsSearchads360V23Resources__AccountBudget
    accountBudgetProposal: GoogleAdsSearchads360V23Resources__AccountBudgetProposal
    accountLink: GoogleAdsSearchads360V23Resources__AccountLink
    ad: GoogleAdsSearchads360V23Resources__Ad
    adGroup: GoogleAdsSearchads360V23Resources__AdGroup
    adGroupAd: GoogleAdsSearchads360V23Resources__AdGroupAd
    adGroupAdAssetCombinationView: (
        GoogleAdsSearchads360V23Resources__AdGroupAdAssetCombinationView
    )
    adGroupAdAssetView: GoogleAdsSearchads360V23Resources__AdGroupAdAssetView
    adGroupAdEffectiveLabel: GoogleAdsSearchads360V23Resources__AdGroupAdEffectiveLabel
    adGroupAdLabel: GoogleAdsSearchads360V23Resources__AdGroupAdLabel
    adGroupAsset: GoogleAdsSearchads360V23Resources__AdGroupAsset
    adGroupAssetSet: GoogleAdsSearchads360V23Resources__AdGroupAssetSet
    adGroupAudienceView: GoogleAdsSearchads360V23Resources__AdGroupAudienceView
    adGroupBidModifier: GoogleAdsSearchads360V23Resources__AdGroupBidModifier
    adGroupCriterion: GoogleAdsSearchads360V23Resources__AdGroupCriterion
    adGroupCriterionCustomizer: (
        GoogleAdsSearchads360V23Resources__AdGroupCriterionCustomizer
    )
    adGroupCriterionEffectiveLabel: (
        GoogleAdsSearchads360V23Resources__AdGroupCriterionEffectiveLabel
    )
    adGroupCriterionLabel: GoogleAdsSearchads360V23Resources__AdGroupCriterionLabel
    adGroupCriterionSimulation: (
        GoogleAdsSearchads360V23Resources__AdGroupCriterionSimulation
    )
    adGroupCustomizer: GoogleAdsSearchads360V23Resources__AdGroupCustomizer
    adGroupEffectiveLabel: GoogleAdsSearchads360V23Resources__AdGroupEffectiveLabel
    adGroupLabel: GoogleAdsSearchads360V23Resources__AdGroupLabel
    adGroupSimulation: GoogleAdsSearchads360V23Resources__AdGroupSimulation
    adParameter: GoogleAdsSearchads360V23Resources__AdParameter
    adScheduleView: GoogleAdsSearchads360V23Resources__AdScheduleView
    ageRangeView: GoogleAdsSearchads360V23Resources__AgeRangeView
    aiMaxSearchTermAdCombinationView: (
        GoogleAdsSearchads360V23Resources__AiMaxSearchTermAdCombinationView
    )
    androidPrivacySharedKeyGoogleAdGroup: (
        GoogleAdsSearchads360V23Resources__AndroidPrivacySharedKeyGoogleAdGroup
    )
    androidPrivacySharedKeyGoogleCampaign: (
        GoogleAdsSearchads360V23Resources__AndroidPrivacySharedKeyGoogleCampaign
    )
    androidPrivacySharedKeyGoogleNetworkType: (
        GoogleAdsSearchads360V23Resources__AndroidPrivacySharedKeyGoogleNetworkType
    )
    asset: GoogleAdsSearchads360V23Resources__Asset
    assetFieldTypeView: GoogleAdsSearchads360V23Resources__AssetFieldTypeView
    assetGroup: GoogleAdsSearchads360V23Resources__AssetGroup
    assetGroupAsset: GoogleAdsSearchads360V23Resources__AssetGroupAsset
    assetGroupListingGroupFilter: (
        GoogleAdsSearchads360V23Resources__AssetGroupListingGroupFilter
    )
    assetGroupProductGroupView: (
        GoogleAdsSearchads360V23Resources__AssetGroupProductGroupView
    )
    assetGroupSignal: GoogleAdsSearchads360V23Resources__AssetGroupSignal
    assetGroupTopCombinationView: (
        GoogleAdsSearchads360V23Resources__AssetGroupTopCombinationView
    )
    assetSet: GoogleAdsSearchads360V23Resources__AssetSet
    assetSetAsset: GoogleAdsSearchads360V23Resources__AssetSetAsset
    assetSetTypeView: GoogleAdsSearchads360V23Resources__AssetSetTypeView
    audience: GoogleAdsSearchads360V23Resources__Audience
    batchJob: GoogleAdsSearchads360V23Resources__BatchJob
    biddingDataExclusion: GoogleAdsSearchads360V23Resources__BiddingDataExclusion
    biddingSeasonalityAdjustment: (
        GoogleAdsSearchads360V23Resources__BiddingSeasonalityAdjustment
    )
    biddingStrategy: GoogleAdsSearchads360V23Resources__BiddingStrategy
    biddingStrategySimulation: (
        GoogleAdsSearchads360V23Resources__BiddingStrategySimulation
    )
    billingSetup: GoogleAdsSearchads360V23Resources__BillingSetup
    callView: GoogleAdsSearchads360V23Resources__CallView
    campaign: GoogleAdsSearchads360V23Resources__Campaign
    campaignAsset: GoogleAdsSearchads360V23Resources__CampaignAsset
    campaignAssetSet: GoogleAdsSearchads360V23Resources__CampaignAssetSet
    campaignAudienceView: GoogleAdsSearchads360V23Resources__CampaignAudienceView
    campaignBidModifier: GoogleAdsSearchads360V23Resources__CampaignBidModifier
    campaignBudget: GoogleAdsSearchads360V23Resources__CampaignBudget
    campaignConversionGoal: GoogleAdsSearchads360V23Resources__CampaignConversionGoal
    campaignCriterion: GoogleAdsSearchads360V23Resources__CampaignCriterion
    campaignCustomizer: GoogleAdsSearchads360V23Resources__CampaignCustomizer
    campaignDraft: GoogleAdsSearchads360V23Resources__CampaignDraft
    campaignEffectiveLabel: GoogleAdsSearchads360V23Resources__CampaignEffectiveLabel
    campaignGoalConfig: GoogleAdsSearchads360V23Resources__CampaignGoalConfig
    campaignGroup: GoogleAdsSearchads360V23Resources__CampaignGroup
    campaignLabel: GoogleAdsSearchads360V23Resources__CampaignLabel
    campaignLifecycleGoal: GoogleAdsSearchads360V23Resources__CampaignLifecycleGoal
    campaignSearchTermInsight: (
        GoogleAdsSearchads360V23Resources__CampaignSearchTermInsight
    )
    campaignSearchTermView: GoogleAdsSearchads360V23Resources__CampaignSearchTermView
    campaignSharedSet: GoogleAdsSearchads360V23Resources__CampaignSharedSet
    campaignSimulation: GoogleAdsSearchads360V23Resources__CampaignSimulation
    carrierConstant: GoogleAdsSearchads360V23Resources__CarrierConstant
    cartDataSalesView: GoogleAdsSearchads360V23Resources__CartDataSalesView
    changeEvent: GoogleAdsSearchads360V23Resources__ChangeEvent
    changeStatus: GoogleAdsSearchads360V23Resources__ChangeStatus
    clickView: GoogleAdsSearchads360V23Resources__ClickView
    combinedAudience: GoogleAdsSearchads360V23Resources__CombinedAudience
    contentCriterionView: GoogleAdsSearchads360V23Resources__ContentCriterionView
    conversion: GoogleAdsSearchads360V23Resources__Conversion
    conversionAction: GoogleAdsSearchads360V23Resources__ConversionAction
    conversionCustomVariable: (
        GoogleAdsSearchads360V23Resources__ConversionCustomVariable
    )
    conversionGoalCampaignConfig: (
        GoogleAdsSearchads360V23Resources__ConversionGoalCampaignConfig
    )
    conversionValueRule: GoogleAdsSearchads360V23Resources__ConversionValueRule
    conversionValueRuleSet: GoogleAdsSearchads360V23Resources__ConversionValueRuleSet
    currencyConstant: GoogleAdsSearchads360V23Resources__CurrencyConstant
    customAudience: GoogleAdsSearchads360V23Resources__CustomAudience
    customColumns: _list[GoogleAdsSearchads360V23Common__Value]
    customConversionGoal: GoogleAdsSearchads360V23Resources__CustomConversionGoal
    customInterest: GoogleAdsSearchads360V23Resources__CustomInterest
    customer: GoogleAdsSearchads360V23Resources__Customer
    customerAsset: GoogleAdsSearchads360V23Resources__CustomerAsset
    customerAssetSet: GoogleAdsSearchads360V23Resources__CustomerAssetSet
    customerClient: GoogleAdsSearchads360V23Resources__CustomerClient
    customerClientLink: GoogleAdsSearchads360V23Resources__CustomerClientLink
    customerConversionGoal: GoogleAdsSearchads360V23Resources__CustomerConversionGoal
    customerCustomizer: GoogleAdsSearchads360V23Resources__CustomerCustomizer
    customerLabel: GoogleAdsSearchads360V23Resources__CustomerLabel
    customerLifecycleGoal: GoogleAdsSearchads360V23Resources__CustomerLifecycleGoal
    customerManagerLink: GoogleAdsSearchads360V23Resources__CustomerManagerLink
    customerNegativeCriterion: (
        GoogleAdsSearchads360V23Resources__CustomerNegativeCriterion
    )
    customerSearchTermInsight: (
        GoogleAdsSearchads360V23Resources__CustomerSearchTermInsight
    )
    customerUserAccess: GoogleAdsSearchads360V23Resources__CustomerUserAccess
    customerUserAccessInvitation: (
        GoogleAdsSearchads360V23Resources__CustomerUserAccessInvitation
    )
    customizerAttribute: GoogleAdsSearchads360V23Resources__CustomizerAttribute
    dataLink: GoogleAdsSearchads360V23Resources__DataLink
    detailContentSuitabilityPlacementView: (
        GoogleAdsSearchads360V23Resources__DetailContentSuitabilityPlacementView
    )
    detailPlacementView: GoogleAdsSearchads360V23Resources__DetailPlacementView
    detailedDemographic: GoogleAdsSearchads360V23Resources__DetailedDemographic
    displayKeywordView: GoogleAdsSearchads360V23Resources__DisplayKeywordView
    distanceView: GoogleAdsSearchads360V23Resources__DistanceView
    dynamicSearchAdsSearchTermView: (
        GoogleAdsSearchads360V23Resources__DynamicSearchAdsSearchTermView
    )
    expandedLandingPageView: GoogleAdsSearchads360V23Resources__ExpandedLandingPageView
    experiment: GoogleAdsSearchads360V23Resources__Experiment
    experimentArm: GoogleAdsSearchads360V23Resources__ExperimentArm
    finalUrlExpansionAssetView: (
        GoogleAdsSearchads360V23Resources__FinalUrlExpansionAssetView
    )
    genderView: GoogleAdsSearchads360V23Resources__GenderView
    geoTargetConstant: GoogleAdsSearchads360V23Resources__GeoTargetConstant
    geographicView: GoogleAdsSearchads360V23Resources__GeographicView
    goal: GoogleAdsSearchads360V23Resources__Goal
    groupContentSuitabilityPlacementView: (
        GoogleAdsSearchads360V23Resources__GroupContentSuitabilityPlacementView
    )
    groupPlacementView: GoogleAdsSearchads360V23Resources__GroupPlacementView
    hotelGroupView: GoogleAdsSearchads360V23Resources__HotelGroupView
    hotelPerformanceView: GoogleAdsSearchads360V23Resources__HotelPerformanceView
    hotelReconciliation: GoogleAdsSearchads360V23Resources__HotelReconciliation
    incomeRangeView: GoogleAdsSearchads360V23Resources__IncomeRangeView
    keywordPlan: GoogleAdsSearchads360V23Resources__KeywordPlan
    keywordPlanAdGroup: GoogleAdsSearchads360V23Resources__KeywordPlanAdGroup
    keywordPlanAdGroupKeyword: (
        GoogleAdsSearchads360V23Resources__KeywordPlanAdGroupKeyword
    )
    keywordPlanCampaign: GoogleAdsSearchads360V23Resources__KeywordPlanCampaign
    keywordPlanCampaignKeyword: (
        GoogleAdsSearchads360V23Resources__KeywordPlanCampaignKeyword
    )
    keywordThemeConstant: GoogleAdsSearchads360V23Resources__KeywordThemeConstant
    keywordView: GoogleAdsSearchads360V23Resources__KeywordView
    label: GoogleAdsSearchads360V23Resources__Label
    landingPageView: GoogleAdsSearchads360V23Resources__LandingPageView
    languageConstant: GoogleAdsSearchads360V23Resources__LanguageConstant
    leadFormSubmissionData: GoogleAdsSearchads360V23Resources__LeadFormSubmissionData
    lifeEvent: GoogleAdsSearchads360V23Resources__LifeEvent
    localServicesEmployee: GoogleAdsSearchads360V23Resources__LocalServicesEmployee
    localServicesLead: GoogleAdsSearchads360V23Resources__LocalServicesLead
    localServicesLeadConversation: (
        GoogleAdsSearchads360V23Resources__LocalServicesLeadConversation
    )
    localServicesVerificationArtifact: (
        GoogleAdsSearchads360V23Resources__LocalServicesVerificationArtifact
    )
    locationInterestView: GoogleAdsSearchads360V23Resources__LocationInterestView
    locationView: GoogleAdsSearchads360V23Resources__LocationView
    managedPlacementView: GoogleAdsSearchads360V23Resources__ManagedPlacementView
    matchedLocationInterestView: (
        GoogleAdsSearchads360V23Resources__MatchedLocationInterestView
    )
    mediaFile: GoogleAdsSearchads360V23Resources__MediaFile
    metrics: GoogleAdsSearchads360V23Common__Metrics
    mobileAppCategoryConstant: (
        GoogleAdsSearchads360V23Resources__MobileAppCategoryConstant
    )
    mobileDeviceConstant: GoogleAdsSearchads360V23Resources__MobileDeviceConstant
    offlineConversionUploadClientSummary: (
        GoogleAdsSearchads360V23Resources__OfflineConversionUploadClientSummary
    )
    offlineConversionUploadConversionActionSummary: GoogleAdsSearchads360V23Resources__OfflineConversionUploadConversionActionSummary
    offlineUserDataJob: GoogleAdsSearchads360V23Resources__OfflineUserDataJob
    operatingSystemVersionConstant: (
        GoogleAdsSearchads360V23Resources__OperatingSystemVersionConstant
    )
    paidOrganicSearchTermView: (
        GoogleAdsSearchads360V23Resources__PaidOrganicSearchTermView
    )
    parentalStatusView: GoogleAdsSearchads360V23Resources__ParentalStatusView
    perStoreView: GoogleAdsSearchads360V23Resources__PerStoreView
    performanceMaxPlacementView: (
        GoogleAdsSearchads360V23Resources__PerformanceMaxPlacementView
    )
    productCategoryConstant: GoogleAdsSearchads360V23Resources__ProductCategoryConstant
    productGroupView: GoogleAdsSearchads360V23Resources__ProductGroupView
    productLink: GoogleAdsSearchads360V23Resources__ProductLink
    productLinkInvitation: GoogleAdsSearchads360V23Resources__ProductLinkInvitation
    qualifyingQuestion: GoogleAdsSearchads360V23Resources__QualifyingQuestion
    recommendation: GoogleAdsSearchads360V23Resources__Recommendation
    recommendationSubscription: (
        GoogleAdsSearchads360V23Resources__RecommendationSubscription
    )
    remarketingAction: GoogleAdsSearchads360V23Resources__RemarketingAction
    searchAds360Campaign: GoogleAdsSearchads360V23Resources__SearchAds360Campaign
    searchTermView: GoogleAdsSearchads360V23Resources__SearchTermView
    segments: GoogleAdsSearchads360V23Common__Segments
    sharedCriterion: GoogleAdsSearchads360V23Resources__SharedCriterion
    sharedSet: GoogleAdsSearchads360V23Resources__SharedSet
    shoppingPerformanceView: GoogleAdsSearchads360V23Resources__ShoppingPerformanceView
    shoppingProduct: GoogleAdsSearchads360V23Resources__ShoppingProduct
    smartCampaignSearchTermView: (
        GoogleAdsSearchads360V23Resources__SmartCampaignSearchTermView
    )
    smartCampaignSetting: GoogleAdsSearchads360V23Resources__SmartCampaignSetting
    targetingExpansionView: GoogleAdsSearchads360V23Resources__TargetingExpansionView
    thirdPartyAppAnalyticsLink: (
        GoogleAdsSearchads360V23Resources__ThirdPartyAppAnalyticsLink
    )
    topicConstant: GoogleAdsSearchads360V23Resources__TopicConstant
    topicView: GoogleAdsSearchads360V23Resources__TopicView
    travelActivityGroupView: GoogleAdsSearchads360V23Resources__TravelActivityGroupView
    travelActivityPerformanceView: (
        GoogleAdsSearchads360V23Resources__TravelActivityPerformanceView
    )
    userInterest: GoogleAdsSearchads360V23Resources__UserInterest
    userList: GoogleAdsSearchads360V23Resources__UserList
    userListCustomerType: GoogleAdsSearchads360V23Resources__UserListCustomerType
    userLocationView: GoogleAdsSearchads360V23Resources__UserLocationView
    video: GoogleAdsSearchads360V23Resources__Video
    visit: GoogleAdsSearchads360V23Resources__Visit
    webpageView: GoogleAdsSearchads360V23Resources__WebpageView

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsRequest(
    typing.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    query: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    results: _list[GoogleAdsSearchads360V23Resources__SearchAds360Field]
    totalResultsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSearchAds360Request(
    typing.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    query: str
    searchSettings: GoogleAdsSearchads360V23Services__SearchSettings
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSearchAds360Response(
    typing.TypedDict, total=False
):
    conversionCustomDimensionHeaders: _list[
        GoogleAdsSearchads360V23Services__ConversionCustomDimensionHeader
    ]
    conversionCustomMetricHeaders: _list[
        GoogleAdsSearchads360V23Services__ConversionCustomMetricHeader
    ]
    customColumnHeaders: _list[GoogleAdsSearchads360V23Services__CustomColumnHeader]
    fieldMask: str
    metricAttributes: _list[GoogleAdsSearchads360V23Services__MetricAttributes]
    nextPageToken: str
    queryResourceConsumption: str
    rawEventConversionDimensionHeaders: _list[
        GoogleAdsSearchads360V23Services__RawEventConversionDimensionHeader
    ]
    rawEventConversionMetricHeaders: _list[
        GoogleAdsSearchads360V23Services__RawEventConversionMetricHeader
    ]
    results: _list[GoogleAdsSearchads360V23Services__SearchAds360Row]
    summaryRow: GoogleAdsSearchads360V23Services__SearchAds360Row
    totalResultsCount: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSettings(typing.TypedDict, total=False):
    omitResults: bool
    returnSummaryRow: bool
    returnTotalResultsCount: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SessionAttributeKeyValuePair(
    typing.TypedDict, total=False
):
    sessionAttributeKey: str
    sessionAttributeValue: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SessionAttributesKeyValuePairs(
    typing.TypedDict, total=False
):
    keyValuePairs: _list[GoogleAdsSearchads360V23Services__SessionAttributeKeyValuePair]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SharedCriterionOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__SharedCriterion
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SharedSetOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__SharedSet
    remove: str
    update: GoogleAdsSearchads360V23Resources__SharedSet
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SiteSeed(typing.TypedDict, total=False):
    site: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignEligibleDetails(
    typing.TypedDict, total=False
):
    endDateTime: str
    lastImpressionDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignEndedDetails(
    typing.TypedDict, total=False
):
    endDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignNotEligibleDetails(
    typing.TypedDict, total=False
):
    notEligibleReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ACCOUNT_ISSUE",
        "BILLING_ISSUE",
        "BUSINESS_PROFILE_LOCATION_REMOVED",
        "ALL_ADS_DISAPPROVED",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignPausedDetails(
    typing.TypedDict, total=False
):
    pausedDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignRemovedDetails(
    typing.TypedDict, total=False
):
    removedDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignSettingOperation(
    typing.TypedDict, total=False
):
    update: GoogleAdsSearchads360V23Resources__SmartCampaignSetting
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SmartCampaignSuggestionInfo(
    typing.TypedDict, total=False
):
    adSchedules: _list[GoogleAdsSearchads360V23Common__AdScheduleInfo]
    businessContext: (
        GoogleAdsSearchads360V23Services_SmartCampaignSuggestionInfo_BusinessContext
    )
    businessProfileLocation: str
    finalUrl: str
    keywordThemes: _list[GoogleAdsSearchads360V23Common__KeywordThemeInfo]
    languageCode: str
    locationList: (
        GoogleAdsSearchads360V23Services_SmartCampaignSuggestionInfo_LocationList
    )
    proximity: GoogleAdsSearchads360V23Common__ProximityInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__StartIdentityVerificationRequest(
    typing.TypedDict, total=False
):
    verificationProgram: typing.Literal[
        "UNSPECIFIED", "UNKNOWN", "ADVERTISER_IDENTITY_VERIFICATION"
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestGeoTargetConstantsRequest(
    typing.TypedDict, total=False
):
    countryCode: str
    geoTargets: (
        GoogleAdsSearchads360V23Services_SuggestGeoTargetConstantsRequest_GeoTargets
    )
    locale: str
    locationNames: (
        GoogleAdsSearchads360V23Services_SuggestGeoTargetConstantsRequest_LocationNames
    )

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestGeoTargetConstantsResponse(
    typing.TypedDict, total=False
):
    geoTargetConstantSuggestions: _list[
        GoogleAdsSearchads360V23Services__GeoTargetConstantSuggestion
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestKeywordThemeConstantsRequest(
    typing.TypedDict, total=False
):
    countryCode: str
    languageCode: str
    queryText: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestKeywordThemeConstantsResponse(
    typing.TypedDict, total=False
):
    keywordThemeConstants: _list[
        GoogleAdsSearchads360V23Resources__KeywordThemeConstant
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestKeywordThemesRequest(
    typing.TypedDict, total=False
):
    suggestionInfo: GoogleAdsSearchads360V23Services__SmartCampaignSuggestionInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestKeywordThemesResponse(
    typing.TypedDict, total=False
):
    keywordThemes: _list[
        GoogleAdsSearchads360V23Services_SuggestKeywordThemesResponse_KeywordTheme
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestSmartCampaignAdRequest(
    typing.TypedDict, total=False
):
    suggestionInfo: GoogleAdsSearchads360V23Services__SmartCampaignSuggestionInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestSmartCampaignAdResponse(
    typing.TypedDict, total=False
):
    adInfo: GoogleAdsSearchads360V23Common__SmartCampaignAdInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestSmartCampaignBudgetOptionsRequest(
    typing.TypedDict, total=False
):
    campaign: str
    suggestionInfo: GoogleAdsSearchads360V23Services__SmartCampaignSuggestionInfo

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestSmartCampaignBudgetOptionsResponse(
    typing.TypedDict, total=False
):
    high: GoogleAdsSearchads360V23Services_SuggestSmartCampaignBudgetOptionsResponse_BudgetOption
    low: GoogleAdsSearchads360V23Services_SuggestSmartCampaignBudgetOptionsResponse_BudgetOption
    recommended: GoogleAdsSearchads360V23Services_SuggestSmartCampaignBudgetOptionsResponse_BudgetOption

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestTravelAssetsRequest(
    typing.TypedDict, total=False
):
    languageOption: str
    placeIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestTravelAssetsResponse(
    typing.TypedDict, total=False
):
    hotelAssetSuggestions: _list[GoogleAdsSearchads360V23Services__HotelAssetSuggestion]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SurfaceTargeting(typing.TypedDict, total=False):
    surfaces: _list[
        typing.Literal[
            "UNSPECIFIED",
            "UNKNOWN",
            "DISCOVER_FEED",
            "GMAIL",
            "IN_FEED",
            "IN_STREAM_BUMPER",
            "IN_STREAM_NON_SKIPPABLE",
            "IN_STREAM_SKIPPABLE",
            "SHORTS",
        ]
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SurfaceTargetingCombinations(
    typing.TypedDict, total=False
):
    availableTargetingCombinations: _list[
        GoogleAdsSearchads360V23Services__SurfaceTargeting
    ]
    defaultTargeting: GoogleAdsSearchads360V23Services__SurfaceTargeting

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SurveyDissatisfied(
    typing.TypedDict, total=False
):
    otherReasonComment: str
    surveyDissatisfiedReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OTHER_DISSATISFIED_REASON",
        "GEO_MISMATCH",
        "JOB_TYPE_MISMATCH",
        "NOT_READY_TO_BOOK",
        "SPAM",
        "DUPLICATE",
        "SOLICITATION",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SurveySatisfied(typing.TypedDict, total=False):
    otherReasonComment: str
    surveySatisfiedReason: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "OTHER_SATISFIED_REASON",
        "BOOKED_CUSTOMER",
        "LIKELY_BOOKED_CUSTOMER",
        "SERVICE_RELATED",
        "HIGH_VALUE_SERVICE",
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__TargetFrequencySettings(
    typing.TypedDict, total=False
):
    targetFrequency: int
    timeUnit: typing.Literal["UNSPECIFIED", "UNKNOWN", "WEEKLY", "MONTHLY"]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__Targeting(typing.TypedDict, total=False):
    ageRange: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "AGE_RANGE_18_24",
        "AGE_RANGE_18_34",
        "AGE_RANGE_18_44",
        "AGE_RANGE_18_49",
        "AGE_RANGE_18_54",
        "AGE_RANGE_18_64",
        "AGE_RANGE_18_65_UP",
        "AGE_RANGE_21_34",
        "AGE_RANGE_25_34",
        "AGE_RANGE_25_44",
        "AGE_RANGE_25_49",
        "AGE_RANGE_25_54",
        "AGE_RANGE_25_64",
        "AGE_RANGE_25_65_UP",
        "AGE_RANGE_35_44",
        "AGE_RANGE_35_49",
        "AGE_RANGE_35_54",
        "AGE_RANGE_35_64",
        "AGE_RANGE_35_65_UP",
        "AGE_RANGE_45_54",
        "AGE_RANGE_45_64",
        "AGE_RANGE_45_65_UP",
        "AGE_RANGE_50_65_UP",
        "AGE_RANGE_55_64",
        "AGE_RANGE_55_65_UP",
        "AGE_RANGE_65_UP",
    ]
    audienceTargeting: GoogleAdsSearchads360V23Services__AudienceTargeting
    devices: _list[GoogleAdsSearchads360V23Common__DeviceInfo]
    genders: _list[GoogleAdsSearchads360V23Common__GenderInfo]
    network: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "YOUTUBE",
        "GOOGLE_VIDEO_PARTNERS",
        "YOUTUBE_AND_GOOGLE_VIDEO_PARTNERS",
    ]
    plannableLocationId: str
    plannableLocationIds: _list[str]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__TargetingSuggestionMetrics(
    typing.TypedDict, total=False
):
    ageRanges: _list[GoogleAdsSearchads360V23Common__AgeRangeInfo]
    coverage: float
    gender: GoogleAdsSearchads360V23Common__GenderInfo
    index: float
    locations: _list[GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadata]
    parentalStatus: GoogleAdsSearchads360V23Common__ParentalStatusInfo
    potentialYoutubeReach: str
    userInterests: _list[
        GoogleAdsSearchads360V23Common__AudienceInsightsAttributeMetadataGroup
    ]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UnusableAdGroup(typing.TypedDict, total=False):
    adGroup: str
    campaign: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UpdateDataLinkRequest(
    typing.TypedDict, total=False
):
    dataLinkStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "REQUESTED",
        "PENDING_APPROVAL",
        "ENABLED",
        "DISABLED",
        "REVOKED",
        "REJECTED",
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UpdateDataLinkResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UpdateProductLinkInvitationRequest(
    typing.TypedDict, total=False
):
    productLinkInvitationStatus: typing.Literal[
        "UNSPECIFIED",
        "UNKNOWN",
        "ACCEPTED",
        "REQUESTED",
        "PENDING_APPROVAL",
        "REVOKED",
        "REJECTED",
        "EXPIRED",
    ]
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UpdateProductLinkInvitationResponse(
    typing.TypedDict, total=False
):
    resourceName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadCallConversionsRequest(
    typing.TypedDict, total=False
):
    conversions: _list[GoogleAdsSearchads360V23Services__CallConversion]
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadCallConversionsResponse(
    typing.TypedDict, total=False
):
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__CallConversionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadClickConversionsRequest(
    typing.TypedDict, total=False
):
    conversions: _list[GoogleAdsSearchads360V23Services__ClickConversion]
    jobId: int
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadClickConversionsResponse(
    typing.TypedDict, total=False
):
    jobId: str
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__ClickConversionResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadConversionAdjustmentsRequest(
    typing.TypedDict, total=False
):
    conversionAdjustments: _list[GoogleAdsSearchads360V23Services__ConversionAdjustment]
    jobId: int
    partialFailure: bool
    validateOnly: bool

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadConversionAdjustmentsResponse(
    typing.TypedDict, total=False
):
    jobId: str
    partialFailureError: GoogleRpc__Status
    results: _list[GoogleAdsSearchads360V23Services__ConversionAdjustmentResult]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadUserDataRequest(
    typing.TypedDict, total=False
):
    customerMatchUserListMetadata: (
        GoogleAdsSearchads360V23Common__CustomerMatchUserListMetadata
    )
    operations: _list[GoogleAdsSearchads360V23Services__UserDataOperation]

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadUserDataResponse(
    typing.TypedDict, total=False
):
    receivedOperationsCount: int
    uploadDateTime: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UrlSeed(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UserDataOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Common__UserData
    remove: GoogleAdsSearchads360V23Common__UserData

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UserListCustomerTypeOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__UserListCustomerType
    remove: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UserListOperation(
    typing.TypedDict, total=False
):
    create: GoogleAdsSearchads360V23Resources__UserList
    remove: str
    update: GoogleAdsSearchads360V23Resources__UserList
    updateMask: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__YouTubeSelectLineUp(
    typing.TypedDict, total=False
):
    lineupId: str
    lineupName: str

@typing.type_check_only
class GoogleAdsSearchads360V23Services__YouTubeSelectSettings(
    typing.TypedDict, total=False
):
    lineupId: str

@typing.type_check_only
class GoogleLongrunning__Operation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpc__Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobuf__Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpc__Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleType__Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
