import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessBetweenFilter(
    typing_extensions.TypedDict, total=False
):
    fromValue: GoogleAnalyticsAdminV1alphaNumericValue
    toValue: GoogleAnalyticsAdminV1alphaNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDateRange(
    typing_extensions.TypedDict, total=False
):
    endDate: str
    startDate: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDimension(
    typing_extensions.TypedDict, total=False
):
    dimensionName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDimensionHeader(
    typing_extensions.TypedDict, total=False
):
    dimensionName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDimensionValue(
    typing_extensions.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessFilter(typing_extensions.TypedDict, total=False):
    betweenFilter: GoogleAnalyticsAdminV1alphaAccessBetweenFilter
    fieldName: str
    inListFilter: GoogleAnalyticsAdminV1alphaAccessInListFilter
    numericFilter: GoogleAnalyticsAdminV1alphaAccessNumericFilter
    stringFilter: GoogleAnalyticsAdminV1alphaAccessStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessFilterExpression(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessFilterExpressionList(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessInListFilter(
    typing_extensions.TypedDict, total=False
):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessMetric(typing_extensions.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessMetricHeader(
    typing_extensions.TypedDict, total=False
):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessMetricValue(
    typing_extensions.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessNumericFilter(
    typing_extensions.TypedDict, total=False
):
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED",
        "EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
    ]
    value: GoogleAnalyticsAdminV1alphaNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessOrderBy(
    typing_extensions.TypedDict, total=False
):
    desc: bool
    dimension: GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy
    metric: GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy(
    typing_extensions.TypedDict, total=False
):
    dimensionName: str
    orderType: typing_extensions.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy(
    typing_extensions.TypedDict, total=False
):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessQuota(typing_extensions.TypedDict, total=False):
    concurrentRequests: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    serverErrorsPerProjectPerHour: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    tokensPerDay: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    tokensPerHour: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    tokensPerProjectPerHour: GoogleAnalyticsAdminV1alphaAccessQuotaStatus

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessQuotaStatus(
    typing_extensions.TypedDict, total=False
):
    consumed: int
    remaining: int

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessRow(typing_extensions.TypedDict, total=False):
    dimensionValues: _list[GoogleAnalyticsAdminV1alphaAccessDimensionValue]
    metricValues: _list[GoogleAnalyticsAdminV1alphaAccessMetricValue]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessStringFilter(
    typing_extensions.TypedDict, total=False
):
    caseSensitive: bool
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
        "PARTIAL_REGEXP",
    ]
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccount(typing_extensions.TypedDict, total=False):
    createTime: str
    deleted: bool
    displayName: str
    name: str
    regionCode: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccountSummary(
    typing_extensions.TypedDict, total=False
):
    account: str
    displayName: str
    name: str
    propertySummaries: _list[GoogleAnalyticsAdminV1alphaPropertySummary]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest(
    typing_extensions.TypedDict, total=False
):
    acknowledgement: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse(
    typing_extensions.TypedDict, total=False
):
    displayVideo360AdvertiserLink: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveAudienceRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAttributionSettings(
    typing_extensions.TypedDict, total=False
):
    acquisitionConversionEventLookbackWindow: typing_extensions.Literal[
        "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED",
        "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS",
        "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS",
    ]
    name: str
    otherConversionEventLookbackWindow: typing_extensions.Literal[
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED",
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS",
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS",
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS",
    ]
    reportingAttributionModel: typing_extensions.Literal[
        "REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED",
        "CROSS_CHANNEL_DATA_DRIVEN",
        "CROSS_CHANNEL_LAST_CLICK",
        "CROSS_CHANNEL_FIRST_CLICK",
        "CROSS_CHANNEL_LINEAR",
        "CROSS_CHANNEL_POSITION_BASED",
        "CROSS_CHANNEL_TIME_DECAY",
        "ADS_PREFERRED_LAST_CLICK",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudience(typing_extensions.TypedDict, total=False):
    adsPersonalizationEnabled: bool
    description: str
    displayName: str
    eventTrigger: GoogleAnalyticsAdminV1alphaAudienceEventTrigger
    exclusionDurationMode: typing_extensions.Literal[
        "AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED",
        "EXCLUDE_TEMPORARILY",
        "EXCLUDE_PERMANENTLY",
    ]
    filterClauses: _list[GoogleAnalyticsAdminV1alphaAudienceFilterClause]
    membershipDurationDays: int
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter(
    typing_extensions.TypedDict, total=False
):
    atAnyPointInTime: bool
    betweenFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter
    fieldName: str
    inAnyNDayPeriod: int
    inListFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter
    numericFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter
    stringFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter(
    typing_extensions.TypedDict, total=False
):
    fromValue: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue
    toValue: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter(
    typing_extensions.TypedDict, total=False
):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter(
    typing_extensions.TypedDict, total=False
):
    operation: typing_extensions.Literal[
        "OPERATION_UNSPECIFIED", "EQUAL", "LESS_THAN", "GREATER_THAN"
    ]
    value: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue(
    typing_extensions.TypedDict, total=False
):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter(
    typing_extensions.TypedDict, total=False
):
    caseSensitive: bool
    matchType: typing_extensions.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
    ]
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceEventFilter(
    typing_extensions.TypedDict, total=False
):
    eventName: str
    eventParameterFilterExpression: GoogleAnalyticsAdminV1alphaAudienceFilterExpression

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceEventTrigger(
    typing_extensions.TypedDict, total=False
):
    eventName: str
    logCondition: typing_extensions.Literal[
        "LOG_CONDITION_UNSPECIFIED", "AUDIENCE_JOINED", "AUDIENCE_MEMBERSHIP_RENEWED"
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceFilterClause(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceFilterExpression(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList(
    dict[str, typing.Any]
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceSequenceFilter(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep(
    dict[str, typing.Any]
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceSimpleFilter(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLink(
    typing_extensions.TypedDict, total=False
):
    directRoles: _list[str]
    effectiveRoles: _list[str]
    emailAddress: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAuditUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userLinks: _list[GoogleAnalyticsAdminV1alphaAuditUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUsers: bool
    requests: _list[GoogleAnalyticsAdminV1alphaCreateUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryChange(
    typing_extensions.TypedDict, total=False
):
    action: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"
    ]
    resource: str
    resourceAfterChange: GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource
    resourceBeforeChange: GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource(
    typing_extensions.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    attributionSettings: GoogleAnalyticsAdminV1alphaAttributionSettings
    conversionEvent: GoogleAnalyticsAdminV1alphaConversionEvent
    customDimension: GoogleAnalyticsAdminV1alphaCustomDimension
    customMetric: GoogleAnalyticsAdminV1alphaCustomMetric
    dataRetentionSettings: GoogleAnalyticsAdminV1alphaDataRetentionSettings
    dataStream: GoogleAnalyticsAdminV1alphaDataStream
    displayVideo360AdvertiserLink: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    displayVideo360AdvertiserLinkProposal: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
    firebaseLink: GoogleAnalyticsAdminV1alphaFirebaseLink
    googleAdsLink: GoogleAnalyticsAdminV1alphaGoogleAdsLink
    googleSignalsSettings: GoogleAnalyticsAdminV1alphaGoogleSignalsSettings
    measurementProtocolSecret: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
    property: GoogleAnalyticsAdminV1alphaProperty
    searchAds360Link: GoogleAnalyticsAdminV1alphaSearchAds360Link

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryEvent(
    typing_extensions.TypedDict, total=False
):
    actorType: typing_extensions.Literal[
        "ACTOR_TYPE_UNSPECIFIED", "USER", "SYSTEM", "SUPPORT"
    ]
    changeTime: str
    changes: _list[GoogleAnalyticsAdminV1alphaChangeHistoryChange]
    changesFiltered: bool
    id: str
    userActorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaConversionEvent(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    custom: bool
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    notifyNewUser: bool
    parent: str
    userLink: GoogleAnalyticsAdminV1alphaUserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomDimension(
    typing_extensions.TypedDict, total=False
):
    description: str
    disallowAdsPersonalization: bool
    displayName: str
    name: str
    parameterName: str
    scope: typing_extensions.Literal["DIMENSION_SCOPE_UNSPECIFIED", "EVENT", "USER"]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomMetric(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    measurementUnit: typing_extensions.Literal[
        "MEASUREMENT_UNIT_UNSPECIFIED",
        "STANDARD",
        "CURRENCY",
        "FEET",
        "METERS",
        "KILOMETERS",
        "MILES",
        "MILLISECONDS",
        "SECONDS",
        "MINUTES",
        "HOURS",
    ]
    name: str
    parameterName: str
    restrictedMetricType: _list[str]
    scope: typing_extensions.Literal["METRIC_SCOPE_UNSPECIFIED", "EVENT"]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataRetentionSettings(
    typing_extensions.TypedDict, total=False
):
    eventDataRetention: typing_extensions.Literal[
        "RETENTION_DURATION_UNSPECIFIED",
        "TWO_MONTHS",
        "FOURTEEN_MONTHS",
        "TWENTY_SIX_MONTHS",
        "THIRTY_EIGHT_MONTHS",
        "FIFTY_MONTHS",
    ]
    name: str
    resetUserDataOnNewActivity: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataSharingSettings(
    typing_extensions.TypedDict, total=False
):
    name: str
    sharingWithGoogleAnySalesEnabled: bool
    sharingWithGoogleAssignedSalesEnabled: bool
    sharingWithGoogleProductsEnabled: bool
    sharingWithGoogleSupportEnabled: bool
    sharingWithOthersEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStream(typing_extensions.TypedDict, total=False):
    androidAppStreamData: GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData
    createTime: str
    displayName: str
    iosAppStreamData: GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData
    name: str
    type: typing_extensions.Literal[
        "DATA_STREAM_TYPE_UNSPECIFIED",
        "WEB_DATA_STREAM",
        "ANDROID_APP_DATA_STREAM",
        "IOS_APP_DATA_STREAM",
    ]
    updateTime: str
    webStreamData: GoogleAnalyticsAdminV1alphaDataStreamWebStreamData

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData(
    typing_extensions.TypedDict, total=False
):
    firebaseAppId: str
    packageName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData(
    typing_extensions.TypedDict, total=False
):
    bundleId: str
    firebaseAppId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamWebStreamData(
    typing_extensions.TypedDict, total=False
):
    defaultUri: str
    firebaseAppId: str
    measurementId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDeleteUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    linkProposalStatusDetails: GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails
    name: str
    validationEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFirebaseLink(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    project: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGlobalSiteTag(
    typing_extensions.TypedDict, total=False
):
    name: str
    snippet: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleAdsLink(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    canManageClients: bool
    createTime: str
    creatorEmailAddress: str
    customerId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleSignalsSettings(
    typing_extensions.TypedDict, total=False
):
    consent: typing_extensions.Literal[
        "GOOGLE_SIGNALS_CONSENT_UNSPECIFIED",
        "GOOGLE_SIGNALS_CONSENT_CONSENTED",
        "GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED",
    ]
    name: str
    state: typing_extensions.Literal[
        "GOOGLE_SIGNALS_STATE_UNSPECIFIED",
        "GOOGLE_SIGNALS_ENABLED",
        "GOOGLE_SIGNALS_DISABLED",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails(
    typing_extensions.TypedDict, total=False
):
    linkProposalInitiatingProduct: typing_extensions.Literal[
        "LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED",
        "GOOGLE_ANALYTICS",
        "LINKED_PRODUCT",
    ]
    linkProposalState: typing_extensions.Literal[
        "LINK_PROPOSAL_STATE_UNSPECIFIED",
        "AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS",
        "AWAITING_REVIEW_FROM_LINKED_PRODUCT",
        "WITHDRAWN",
        "DECLINED",
        "EXPIRED",
        "OBSOLETE",
    ]
    requestorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountSummariesResponse(
    typing_extensions.TypedDict, total=False
):
    accountSummaries: _list[GoogleAnalyticsAdminV1alphaAccountSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountsResponse(
    typing_extensions.TypedDict, total=False
):
    accounts: _list[GoogleAnalyticsAdminV1alphaAccount]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAudiencesResponse(
    typing_extensions.TypedDict, total=False
):
    audiences: _list[GoogleAnalyticsAdminV1alphaAudience]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListConversionEventsResponse(
    typing_extensions.TypedDict, total=False
):
    conversionEvents: _list[GoogleAnalyticsAdminV1alphaConversionEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse(
    typing_extensions.TypedDict, total=False
):
    customDimensions: _list[GoogleAnalyticsAdminV1alphaCustomDimension]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomMetricsResponse(
    typing_extensions.TypedDict, total=False
):
    customMetrics: _list[GoogleAnalyticsAdminV1alphaCustomMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDataStreamsResponse(
    typing_extensions.TypedDict, total=False
):
    dataStreams: _list[GoogleAnalyticsAdminV1alphaDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse(
    typing_extensions.TypedDict, total=False
):
    displayVideo360AdvertiserLinkProposals: _list[
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    displayVideo360AdvertiserLinks: _list[
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse(
    typing_extensions.TypedDict, total=False
):
    firebaseLinks: _list[GoogleAnalyticsAdminV1alphaFirebaseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse(
    typing_extensions.TypedDict, total=False
):
    googleAdsLinks: _list[GoogleAnalyticsAdminV1alphaGoogleAdsLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse(
    typing_extensions.TypedDict, total=False
):
    measurementProtocolSecrets: _list[
        GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListPropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    properties: _list[GoogleAnalyticsAdminV1alphaProperty]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    searchAds360Links: _list[GoogleAnalyticsAdminV1alphaSearchAds360Link]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListUserLinksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    userLinks: _list[GoogleAnalyticsAdminV1alphaUserLink]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    secretValue: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaNumericValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProperty(typing_extensions.TypedDict, total=False):
    account: str
    createTime: str
    currencyCode: str
    deleteTime: str
    displayName: str
    expireTime: str
    industryCategory: typing_extensions.Literal[
        "INDUSTRY_CATEGORY_UNSPECIFIED",
        "AUTOMOTIVE",
        "BUSINESS_AND_INDUSTRIAL_MARKETS",
        "FINANCE",
        "HEALTHCARE",
        "TECHNOLOGY",
        "TRAVEL",
        "OTHER",
        "ARTS_AND_ENTERTAINMENT",
        "BEAUTY_AND_FITNESS",
        "BOOKS_AND_LITERATURE",
        "FOOD_AND_DRINK",
        "GAMES",
        "HOBBIES_AND_LEISURE",
        "HOME_AND_GARDEN",
        "INTERNET_AND_TELECOM",
        "LAW_AND_GOVERNMENT",
        "NEWS",
        "ONLINE_COMMUNITIES",
        "PEOPLE_AND_SOCIETY",
        "PETS_AND_ANIMALS",
        "REAL_ESTATE",
        "REFERENCE",
        "SCIENCE",
        "SPORTS",
        "JOBS_AND_EDUCATION",
        "SHOPPING",
    ]
    name: str
    parent: str
    propertyType: typing_extensions.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]
    serviceLevel: typing_extensions.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "GOOGLE_ANALYTICS_STANDARD", "GOOGLE_ANALYTICS_360"
    ]
    timeZone: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaPropertySummary(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    parent: str
    property: str
    propertyType: typing_extensions.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest(
    typing_extensions.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    redirectUri: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse(
    typing_extensions.TypedDict, total=False
):
    accountTicketId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRunAccessReportRequest(
    typing_extensions.TypedDict, total=False
):
    dateRanges: _list[GoogleAnalyticsAdminV1alphaAccessDateRange]
    dimensionFilter: GoogleAnalyticsAdminV1alphaAccessFilterExpression
    dimensions: _list[GoogleAnalyticsAdminV1alphaAccessDimension]
    limit: str
    metricFilter: GoogleAnalyticsAdminV1alphaAccessFilterExpression
    metrics: _list[GoogleAnalyticsAdminV1alphaAccessMetric]
    offset: str
    orderBys: _list[GoogleAnalyticsAdminV1alphaAccessOrderBy]
    returnEntityQuota: bool
    timeZone: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRunAccessReportResponse(
    typing_extensions.TypedDict, total=False
):
    dimensionHeaders: _list[GoogleAnalyticsAdminV1alphaAccessDimensionHeader]
    metricHeaders: _list[GoogleAnalyticsAdminV1alphaAccessMetricHeader]
    quota: GoogleAnalyticsAdminV1alphaAccessQuota
    rowCount: int
    rows: _list[GoogleAnalyticsAdminV1alphaAccessRow]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchAds360Link(
    typing_extensions.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    name: str
    siteStatsSharingEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest(
    typing_extensions.TypedDict, total=False
):
    action: _list[str]
    actorEmail: _list[str]
    earliestChangeTime: str
    latestChangeTime: str
    pageSize: int
    pageToken: str
    property: str
    resourceType: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse(
    typing_extensions.TypedDict, total=False
):
    changeHistoryEvents: _list[GoogleAnalyticsAdminV1alphaChangeHistoryEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUpdateUserLinkRequest(
    typing_extensions.TypedDict, total=False
):
    userLink: GoogleAnalyticsAdminV1alphaUserLink

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUserLink(typing_extensions.TypedDict, total=False):
    directRoles: _list[str]
    emailAddress: str
    name: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...
