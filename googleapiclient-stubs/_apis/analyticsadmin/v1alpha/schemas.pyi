import typing

_list = list

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessBetweenFilter(typing.TypedDict, total=False):
    fromValue: GoogleAnalyticsAdminV1alphaNumericValue
    toValue: GoogleAnalyticsAdminV1alphaNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessBinding(typing.TypedDict, total=False):
    name: str
    roles: _list[str]
    user: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDateRange(typing.TypedDict, total=False):
    endDate: str
    startDate: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDimension(typing.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDimensionHeader(typing.TypedDict, total=False):
    dimensionName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessDimensionValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessFilter(typing.TypedDict, total=False):
    betweenFilter: GoogleAnalyticsAdminV1alphaAccessBetweenFilter
    fieldName: str
    inListFilter: GoogleAnalyticsAdminV1alphaAccessInListFilter
    numericFilter: GoogleAnalyticsAdminV1alphaAccessNumericFilter
    stringFilter: GoogleAnalyticsAdminV1alphaAccessStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessFilterExpression(typing.TypedDict, total=False):
    accessFilter: GoogleAnalyticsAdminV1alphaAccessFilter
    andGroup: GoogleAnalyticsAdminV1alphaAccessFilterExpressionList
    notExpression: GoogleAnalyticsAdminV1alphaAccessFilterExpression
    orGroup: GoogleAnalyticsAdminV1alphaAccessFilterExpressionList

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessFilterExpressionList(
    typing.TypedDict, total=False
):
    expressions: _list[GoogleAnalyticsAdminV1alphaAccessFilterExpression]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessInListFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessMetric(typing.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessMetricHeader(typing.TypedDict, total=False):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessMetricValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessNumericFilter(typing.TypedDict, total=False):
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED",
        "EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
    ]
    value: GoogleAnalyticsAdminV1alphaNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessOrderBy(typing.TypedDict, total=False):
    desc: bool
    dimension: GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy
    metric: GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy(
    typing.TypedDict, total=False
):
    dimensionName: str
    orderType: typing.Literal[
        "ORDER_TYPE_UNSPECIFIED",
        "ALPHANUMERIC",
        "CASE_INSENSITIVE_ALPHANUMERIC",
        "NUMERIC",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy(
    typing.TypedDict, total=False
):
    metricName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessQuota(typing.TypedDict, total=False):
    concurrentRequests: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    serverErrorsPerProjectPerHour: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    tokensPerDay: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    tokensPerHour: GoogleAnalyticsAdminV1alphaAccessQuotaStatus
    tokensPerProjectPerHour: GoogleAnalyticsAdminV1alphaAccessQuotaStatus

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessQuotaStatus(typing.TypedDict, total=False):
    consumed: int
    remaining: int

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessRow(typing.TypedDict, total=False):
    dimensionValues: _list[GoogleAnalyticsAdminV1alphaAccessDimensionValue]
    metricValues: _list[GoogleAnalyticsAdminV1alphaAccessMetricValue]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessStringFilter(typing.TypedDict, total=False):
    caseSensitive: bool
    matchType: typing.Literal[
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
class GoogleAnalyticsAdminV1alphaAccount(typing.TypedDict, total=False):
    createTime: str
    deleted: bool
    displayName: str
    gmpOrganization: str
    name: str
    regionCode: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccountSummary(typing.TypedDict, total=False):
    account: str
    displayName: str
    name: str
    propertySummaries: _list[GoogleAnalyticsAdminV1alphaPropertySummary]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest(
    typing.TypedDict, total=False
):
    acknowledgement: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAdSenseLink(typing.TypedDict, total=False):
    adClientCode: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse(
    typing.TypedDict, total=False
):
    displayVideo360AdvertiserLink: (
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    )

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveAudienceRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAttributionSettings(typing.TypedDict, total=False):
    acquisitionConversionEventLookbackWindow: typing.Literal[
        "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED",
        "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS",
        "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS",
    ]
    adsWebConversionDataExportScope: typing.Literal[
        "ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED",
        "NOT_SELECTED_YET",
        "PAID_AND_ORGANIC_CHANNELS",
        "GOOGLE_PAID_CHANNELS",
    ]
    name: str
    otherConversionEventLookbackWindow: typing.Literal[
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED",
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS",
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS",
        "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS",
    ]
    reportingAttributionModel: typing.Literal[
        "REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED",
        "PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN",
        "PAID_AND_ORGANIC_CHANNELS_LAST_CLICK",
        "GOOGLE_PAID_CHANNELS_LAST_CLICK",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudience(typing.TypedDict, total=False):
    adsPersonalizationEnabled: bool
    createTime: str
    description: str
    displayName: str
    eventTrigger: GoogleAnalyticsAdminV1alphaAudienceEventTrigger
    exclusionDurationMode: typing.Literal[
        "AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED",
        "EXCLUDE_TEMPORARILY",
        "EXCLUDE_PERMANENTLY",
    ]
    filterClauses: _list[GoogleAnalyticsAdminV1alphaAudienceFilterClause]
    membershipDurationDays: int
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter(
    typing.TypedDict, total=False
):
    atAnyPointInTime: bool
    betweenFilter: (
        GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter
    )
    fieldName: str
    inAnyNDayPeriod: int
    inListFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter
    numericFilter: (
        GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter
    )
    stringFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter(
    typing.TypedDict, total=False
):
    fromValue: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue
    toValue: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter(
    typing.TypedDict, total=False
):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter(
    typing.TypedDict, total=False
):
    operation: typing.Literal[
        "OPERATION_UNSPECIFIED", "EQUAL", "LESS_THAN", "GREATER_THAN"
    ]
    value: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue(
    typing.TypedDict, total=False
):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter(
    typing.TypedDict, total=False
):
    caseSensitive: bool
    matchType: typing.Literal[
        "MATCH_TYPE_UNSPECIFIED",
        "EXACT",
        "BEGINS_WITH",
        "ENDS_WITH",
        "CONTAINS",
        "FULL_REGEXP",
    ]
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceEventFilter(typing.TypedDict, total=False):
    eventName: str
    eventParameterFilterExpression: GoogleAnalyticsAdminV1alphaAudienceFilterExpression

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceEventTrigger(typing.TypedDict, total=False):
    eventName: str
    logCondition: typing.Literal[
        "LOG_CONDITION_UNSPECIFIED", "AUDIENCE_JOINED", "AUDIENCE_MEMBERSHIP_RENEWED"
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceFilterClause(typing.TypedDict, total=False):
    clauseType: typing.Literal["AUDIENCE_CLAUSE_TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"]
    sequenceFilter: GoogleAnalyticsAdminV1alphaAudienceSequenceFilter
    simpleFilter: GoogleAnalyticsAdminV1alphaAudienceSimpleFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceFilterExpression(
    typing.TypedDict, total=False
):
    andGroup: GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList
    dimensionOrMetricFilter: GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter
    eventFilter: GoogleAnalyticsAdminV1alphaAudienceEventFilter
    notExpression: GoogleAnalyticsAdminV1alphaAudienceFilterExpression
    orGroup: GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList(
    typing.TypedDict, total=False
):
    filterExpressions: _list[GoogleAnalyticsAdminV1alphaAudienceFilterExpression]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceSequenceFilter(typing.TypedDict, total=False):
    scope: typing.Literal[
        "AUDIENCE_FILTER_SCOPE_UNSPECIFIED",
        "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT",
        "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION",
        "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
    ]
    sequenceMaximumDuration: str
    sequenceSteps: _list[
        GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep(
    typing.TypedDict, total=False
):
    constraintDuration: str
    filterExpression: GoogleAnalyticsAdminV1alphaAudienceFilterExpression
    immediatelyFollows: bool
    scope: typing.Literal[
        "AUDIENCE_FILTER_SCOPE_UNSPECIFIED",
        "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT",
        "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION",
        "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceSimpleFilter(typing.TypedDict, total=False):
    filterExpression: GoogleAnalyticsAdminV1alphaAudienceFilterExpression
    scope: typing.Literal[
        "AUDIENCE_FILTER_SCOPE_UNSPECIFIED",
        "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT",
        "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION",
        "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse(
    typing.TypedDict, total=False
):
    accessBindings: _list[GoogleAnalyticsAdminV1alphaAccessBinding]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse(
    typing.TypedDict, total=False
):
    accessBindings: _list[GoogleAnalyticsAdminV1alphaAccessBinding]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse(
    typing.TypedDict, total=False
):
    accessBindings: _list[GoogleAnalyticsAdminV1alphaAccessBinding]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBigQueryLink(typing.TypedDict, total=False):
    createTime: str
    dailyExportEnabled: bool
    datasetLocation: str
    excludedEvents: _list[str]
    exportStreams: _list[str]
    freshDailyExportEnabled: bool
    includeAdvertisingId: bool
    name: str
    project: str
    streamingExportEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCalculatedMetric(typing.TypedDict, total=False):
    calculatedMetricId: str
    description: str
    displayName: str
    formula: str
    invalidMetricReference: bool
    metricUnit: typing.Literal[
        "METRIC_UNIT_UNSPECIFIED",
        "STANDARD",
        "CURRENCY",
        "FEET",
        "MILES",
        "METERS",
        "KILOMETERS",
        "MILLISECONDS",
        "SECONDS",
        "MINUTES",
        "HOURS",
    ]
    name: str
    restrictedMetricType: _list[
        typing.Literal[
            "RESTRICTED_METRIC_TYPE_UNSPECIFIED", "COST_DATA", "REVENUE_DATA"
        ]
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryChange(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"]
    resource: str
    resourceAfterChange: (
        GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource
    )
    resourceBeforeChange: (
        GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource
    )

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource(
    typing.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    adsenseLink: GoogleAnalyticsAdminV1alphaAdSenseLink
    attributionSettings: GoogleAnalyticsAdminV1alphaAttributionSettings
    audience: GoogleAnalyticsAdminV1alphaAudience
    bigqueryLink: GoogleAnalyticsAdminV1alphaBigQueryLink
    calculatedMetric: GoogleAnalyticsAdminV1alphaCalculatedMetric
    channelGroup: GoogleAnalyticsAdminV1alphaChannelGroup
    conversionEvent: GoogleAnalyticsAdminV1alphaConversionEvent
    customDimension: GoogleAnalyticsAdminV1alphaCustomDimension
    customMetric: GoogleAnalyticsAdminV1alphaCustomMetric
    dataRedactionSettings: GoogleAnalyticsAdminV1alphaDataRedactionSettings
    dataRetentionSettings: GoogleAnalyticsAdminV1alphaDataRetentionSettings
    dataStream: GoogleAnalyticsAdminV1alphaDataStream
    displayVideo360AdvertiserLink: (
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    )
    displayVideo360AdvertiserLinkProposal: (
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
    )
    enhancedMeasurementSettings: GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings
    eventCreateRule: GoogleAnalyticsAdminV1alphaEventCreateRule
    expandedDataSet: GoogleAnalyticsAdminV1alphaExpandedDataSet
    firebaseLink: GoogleAnalyticsAdminV1alphaFirebaseLink
    googleAdsLink: GoogleAnalyticsAdminV1alphaGoogleAdsLink
    googleSignalsSettings: GoogleAnalyticsAdminV1alphaGoogleSignalsSettings
    keyEvent: GoogleAnalyticsAdminV1alphaKeyEvent
    measurementProtocolSecret: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
    property: GoogleAnalyticsAdminV1alphaProperty
    reportingDataAnnotation: GoogleAnalyticsAdminV1alphaReportingDataAnnotation
    reportingIdentitySettings: GoogleAnalyticsAdminV1alphaReportingIdentitySettings
    searchAds360Link: GoogleAnalyticsAdminV1alphaSearchAds360Link
    skadnetworkConversionValueSchema: (
        GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema
    )
    subpropertySyncConfig: GoogleAnalyticsAdminV1alphaSubpropertySyncConfig
    userProvidedDataSettings: GoogleAnalyticsAdminV1alphaUserProvidedDataSettings

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChangeHistoryEvent(typing.TypedDict, total=False):
    actorType: typing.Literal["ACTOR_TYPE_UNSPECIFIED", "USER", "SYSTEM", "SUPPORT"]
    changeTime: str
    changes: _list[GoogleAnalyticsAdminV1alphaChangeHistoryChange]
    changesFiltered: bool
    id: str
    userActorEmail: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroup(typing.TypedDict, total=False):
    description: str
    displayName: str
    groupingRule: _list[GoogleAnalyticsAdminV1alphaGroupingRule]
    name: str
    primary: bool
    systemDefined: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroupFilter(typing.TypedDict, total=False):
    fieldName: str
    inListFilter: GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter
    stringFilter: GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression(
    typing.TypedDict, total=False
):
    andGroup: GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList
    filter: GoogleAnalyticsAdminV1alphaChannelGroupFilter
    notExpression: GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression
    orGroup: GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList(
    typing.TypedDict, total=False
):
    filterExpressions: _list[GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter(
    typing.TypedDict, total=False
):
    matchType: typing.Literal[
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
class GoogleAnalyticsAdminV1alphaConversionEvent(typing.TypedDict, total=False):
    countingMethod: typing.Literal[
        "CONVERSION_COUNTING_METHOD_UNSPECIFIED", "ONCE_PER_EVENT", "ONCE_PER_SESSION"
    ]
    createTime: str
    custom: bool
    defaultConversionValue: (
        GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue
    )
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue(
    typing.TypedDict, total=False
):
    currencyCode: str
    value: float

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaConversionValues(typing.TypedDict, total=False):
    coarseValue: typing.Literal[
        "COARSE_VALUE_UNSPECIFIED",
        "COARSE_VALUE_LOW",
        "COARSE_VALUE_MEDIUM",
        "COARSE_VALUE_HIGH",
    ]
    displayName: str
    eventMappings: _list[GoogleAnalyticsAdminV1alphaEventMapping]
    fineValue: int
    lockEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest(
    typing.TypedDict, total=False
):
    accessBinding: GoogleAnalyticsAdminV1alphaAccessBinding
    parent: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest(
    typing.TypedDict, total=False
):
    rollupProperty: GoogleAnalyticsAdminV1alphaProperty
    sourceProperties: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse(
    typing.TypedDict, total=False
):
    rollupProperty: GoogleAnalyticsAdminV1alphaProperty
    rollupPropertySourceLinks: _list[
        GoogleAnalyticsAdminV1alphaRollupPropertySourceLink
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomDimension(typing.TypedDict, total=False):
    description: str
    disallowAdsPersonalization: bool
    displayName: str
    name: str
    parameterName: str
    scope: typing.Literal["DIMENSION_SCOPE_UNSPECIFIED", "EVENT", "USER", "ITEM"]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomMetric(typing.TypedDict, total=False):
    description: str
    displayName: str
    measurementUnit: typing.Literal[
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
    restrictedMetricType: _list[
        typing.Literal[
            "RESTRICTED_METRIC_TYPE_UNSPECIFIED", "COST_DATA", "REVENUE_DATA"
        ]
    ]
    scope: typing.Literal["METRIC_SCOPE_UNSPECIFIED", "EVENT"]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataRedactionSettings(typing.TypedDict, total=False):
    emailRedactionEnabled: bool
    name: str
    queryParameterKeys: _list[str]
    queryParameterRedactionEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataRetentionSettings(typing.TypedDict, total=False):
    eventDataRetention: typing.Literal[
        "RETENTION_DURATION_UNSPECIFIED",
        "TWO_MONTHS",
        "FOURTEEN_MONTHS",
        "TWENTY_SIX_MONTHS",
        "THIRTY_EIGHT_MONTHS",
        "FIFTY_MONTHS",
    ]
    name: str
    resetUserDataOnNewActivity: bool
    userDataRetention: typing.Literal[
        "RETENTION_DURATION_UNSPECIFIED",
        "TWO_MONTHS",
        "FOURTEEN_MONTHS",
        "TWENTY_SIX_MONTHS",
        "THIRTY_EIGHT_MONTHS",
        "FIFTY_MONTHS",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataSharingSettings(typing.TypedDict, total=False):
    name: str
    sharingWithGoogleAnySalesEnabled: bool
    sharingWithGoogleAssignedSalesEnabled: bool
    sharingWithGoogleProductsEnabled: bool
    sharingWithGoogleSupportEnabled: bool
    sharingWithOthersEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStream(typing.TypedDict, total=False):
    androidAppStreamData: GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData
    createTime: str
    displayName: str
    iosAppStreamData: GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData
    name: str
    type: typing.Literal[
        "DATA_STREAM_TYPE_UNSPECIFIED",
        "WEB_DATA_STREAM",
        "ANDROID_APP_DATA_STREAM",
        "IOS_APP_DATA_STREAM",
    ]
    updateTime: str
    webStreamData: GoogleAnalyticsAdminV1alphaDataStreamWebStreamData

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData(
    typing.TypedDict, total=False
):
    firebaseAppId: str
    packageName: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData(
    typing.TypedDict, total=False
):
    bundleId: str
    firebaseAppId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamWebStreamData(typing.TypedDict, total=False):
    defaultUri: str
    firebaseAppId: str
    measurementId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink(
    typing.TypedDict, total=False
):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal(
    typing.TypedDict, total=False
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
class GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings(
    typing.TypedDict, total=False
):
    fileDownloadsEnabled: bool
    formInteractionsEnabled: bool
    name: str
    outboundClicksEnabled: bool
    pageChangesEnabled: bool
    scrollsEnabled: bool
    searchQueryParameter: str
    siteSearchEnabled: bool
    streamEnabled: bool
    uriQueryParameter: str
    videoEngagementEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEventCreateRule(typing.TypedDict, total=False):
    destinationEvent: str
    eventConditions: _list[GoogleAnalyticsAdminV1alphaMatchingCondition]
    name: str
    parameterMutations: _list[GoogleAnalyticsAdminV1alphaParameterMutation]
    sourceCopyParameters: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEventEditRule(typing.TypedDict, total=False):
    displayName: str
    eventConditions: _list[GoogleAnalyticsAdminV1alphaMatchingCondition]
    name: str
    parameterMutations: _list[GoogleAnalyticsAdminV1alphaParameterMutation]
    processingOrder: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEventMapping(typing.TypedDict, total=False):
    eventName: str
    maxEventCount: str
    maxEventValue: float
    minEventCount: str
    minEventValue: float

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSet(typing.TypedDict, total=False):
    dataCollectionStartTime: str
    description: str
    dimensionFilterExpression: (
        GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression
    )
    dimensionNames: _list[str]
    displayName: str
    metricNames: _list[str]
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSetFilter(typing.TypedDict, total=False):
    fieldName: str
    inListFilter: GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter
    stringFilter: GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression(
    typing.TypedDict, total=False
):
    andGroup: GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList
    filter: GoogleAnalyticsAdminV1alphaExpandedDataSetFilter
    notExpression: GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList(
    typing.TypedDict, total=False
):
    filterExpressions: _list[GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter(
    typing.TypedDict, total=False
):
    caseSensitive: bool
    values: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter(
    typing.TypedDict, total=False
):
    caseSensitive: bool
    matchType: typing.Literal["MATCH_TYPE_UNSPECIFIED", "EXACT", "CONTAINS"]
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFirebaseLink(typing.TypedDict, total=False):
    createTime: str
    name: str
    project: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGlobalSiteTag(typing.TypedDict, total=False):
    name: str
    snippet: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleAdsLink(typing.TypedDict, total=False):
    adsPersonalizationEnabled: bool
    canManageClients: bool
    createTime: str
    creatorEmailAddress: str
    customerId: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleSignalsSettings(typing.TypedDict, total=False):
    consent: typing.Literal[
        "GOOGLE_SIGNALS_CONSENT_UNSPECIFIED",
        "GOOGLE_SIGNALS_CONSENT_CONSENTED",
        "GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED",
    ]
    name: str
    state: typing.Literal[
        "GOOGLE_SIGNALS_STATE_UNSPECIFIED",
        "GOOGLE_SIGNALS_ENABLED",
        "GOOGLE_SIGNALS_DISABLED",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGroupingRule(typing.TypedDict, total=False):
    displayName: str
    expression: GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaKeyEvent(typing.TypedDict, total=False):
    countingMethod: typing.Literal[
        "COUNTING_METHOD_UNSPECIFIED", "ONCE_PER_EVENT", "ONCE_PER_SESSION"
    ]
    createTime: str
    custom: bool
    defaultValue: GoogleAnalyticsAdminV1alphaKeyEventDefaultValue
    deletable: bool
    eventName: str
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaKeyEventDefaultValue(typing.TypedDict, total=False):
    currencyCode: str
    numericValue: float

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails(
    typing.TypedDict, total=False
):
    linkProposalInitiatingProduct: typing.Literal[
        "LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED",
        "GOOGLE_ANALYTICS",
        "LINKED_PRODUCT",
    ]
    linkProposalState: typing.Literal[
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
class GoogleAnalyticsAdminV1alphaListAccessBindingsResponse(
    typing.TypedDict, total=False
):
    accessBindings: _list[GoogleAnalyticsAdminV1alphaAccessBinding]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountSummariesResponse(
    typing.TypedDict, total=False
):
    accountSummaries: _list[GoogleAnalyticsAdminV1alphaAccountSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[GoogleAnalyticsAdminV1alphaAccount]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse(
    typing.TypedDict, total=False
):
    adsenseLinks: _list[GoogleAnalyticsAdminV1alphaAdSenseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAudiencesResponse(typing.TypedDict, total=False):
    audiences: _list[GoogleAnalyticsAdminV1alphaAudience]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse(
    typing.TypedDict, total=False
):
    bigqueryLinks: _list[GoogleAnalyticsAdminV1alphaBigQueryLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse(
    typing.TypedDict, total=False
):
    calculatedMetrics: _list[GoogleAnalyticsAdminV1alphaCalculatedMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListChannelGroupsResponse(
    typing.TypedDict, total=False
):
    channelGroups: _list[GoogleAnalyticsAdminV1alphaChannelGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListConversionEventsResponse(
    typing.TypedDict, total=False
):
    conversionEvents: _list[GoogleAnalyticsAdminV1alphaConversionEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse(
    typing.TypedDict, total=False
):
    customDimensions: _list[GoogleAnalyticsAdminV1alphaCustomDimension]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomMetricsResponse(
    typing.TypedDict, total=False
):
    customMetrics: _list[GoogleAnalyticsAdminV1alphaCustomMetric]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDataStreamsResponse(typing.TypedDict, total=False):
    dataStreams: _list[GoogleAnalyticsAdminV1alphaDataStream]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse(
    typing.TypedDict, total=False
):
    displayVideo360AdvertiserLinkProposals: _list[
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse(
    typing.TypedDict, total=False
):
    displayVideo360AdvertiserLinks: _list[
        GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse(
    typing.TypedDict, total=False
):
    eventCreateRules: _list[GoogleAnalyticsAdminV1alphaEventCreateRule]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListEventEditRulesResponse(
    typing.TypedDict, total=False
):
    eventEditRules: _list[GoogleAnalyticsAdminV1alphaEventEditRule]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse(
    typing.TypedDict, total=False
):
    expandedDataSets: _list[GoogleAnalyticsAdminV1alphaExpandedDataSet]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse(
    typing.TypedDict, total=False
):
    firebaseLinks: _list[GoogleAnalyticsAdminV1alphaFirebaseLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse(
    typing.TypedDict, total=False
):
    googleAdsLinks: _list[GoogleAnalyticsAdminV1alphaGoogleAdsLink]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListKeyEventsResponse(typing.TypedDict, total=False):
    keyEvents: _list[GoogleAnalyticsAdminV1alphaKeyEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse(
    typing.TypedDict, total=False
):
    measurementProtocolSecrets: _list[
        GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListPropertiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    properties: _list[GoogleAnalyticsAdminV1alphaProperty]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    reportingDataAnnotations: _list[GoogleAnalyticsAdminV1alphaReportingDataAnnotation]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rollupPropertySourceLinks: _list[
        GoogleAnalyticsAdminV1alphaRollupPropertySourceLink
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    skadnetworkConversionValueSchemas: _list[
        GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    searchAds360Links: _list[GoogleAnalyticsAdminV1alphaSearchAds360Link]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    subpropertyEventFilters: _list[GoogleAnalyticsAdminV1alphaSubpropertyEventFilter]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    subpropertySyncConfigs: _list[GoogleAnalyticsAdminV1alphaSubpropertySyncConfig]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaMatchingCondition(typing.TypedDict, total=False):
    comparisonType: typing.Literal[
        "COMPARISON_TYPE_UNSPECIFIED",
        "EQUALS",
        "EQUALS_CASE_INSENSITIVE",
        "CONTAINS",
        "CONTAINS_CASE_INSENSITIVE",
        "STARTS_WITH",
        "STARTS_WITH_CASE_INSENSITIVE",
        "ENDS_WITH",
        "ENDS_WITH_CASE_INSENSITIVE",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "REGULAR_EXPRESSION",
        "REGULAR_EXPRESSION_CASE_INSENSITIVE",
    ]
    field: str
    negated: bool
    value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    secretValue: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaNumericValue(typing.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaParameterMutation(typing.TypedDict, total=False):
    parameter: str
    parameterValue: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaPostbackWindow(typing.TypedDict, total=False):
    conversionValues: _list[GoogleAnalyticsAdminV1alphaConversionValues]
    postbackWindowSettingsEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProperty(typing.TypedDict, total=False):
    account: str
    createTime: str
    currencyCode: str
    deleteTime: str
    displayName: str
    expireTime: str
    industryCategory: typing.Literal[
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
    propertyType: typing.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]
    serviceLevel: typing.Literal[
        "SERVICE_LEVEL_UNSPECIFIED", "GOOGLE_ANALYTICS_STANDARD", "GOOGLE_ANALYTICS_360"
    ]
    timeZone: str
    updateTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaPropertySummary(typing.TypedDict, total=False):
    canEdit: bool
    displayName: str
    parent: str
    property: str
    propertyType: typing.Literal[
        "PROPERTY_TYPE_UNSPECIFIED",
        "PROPERTY_TYPE_ORDINARY",
        "PROPERTY_TYPE_SUBPROPERTY",
        "PROPERTY_TYPE_ROLLUP",
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest(
    typing.TypedDict, total=False
):
    account: GoogleAnalyticsAdminV1alphaAccount
    redirectUri: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse(
    typing.TypedDict, total=False
):
    accountTicketId: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest(
    typing.TypedDict, total=False
):
    customDimensionAndMetricSynchronizationMode: typing.Literal[
        "SYNCHRONIZATION_MODE_UNSPECIFIED", "NONE", "ALL"
    ]
    subproperty: GoogleAnalyticsAdminV1alphaProperty
    subpropertyEventFilter: GoogleAnalyticsAdminV1alphaSubpropertyEventFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse(
    typing.TypedDict, total=False
):
    subproperty: GoogleAnalyticsAdminV1alphaProperty
    subpropertyEventFilter: GoogleAnalyticsAdminV1alphaSubpropertyEventFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest(
    typing.TypedDict, total=False
):
    eventEditRules: _list[str]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaReportingDataAnnotation(typing.TypedDict, total=False):
    annotationDate: GoogleTypeDate
    annotationDateRange: GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange
    color: typing.Literal[
        "COLOR_UNSPECIFIED", "PURPLE", "BROWN", "BLUE", "GREEN", "RED", "CYAN", "ORANGE"
    ]
    description: str
    name: str
    systemGenerated: bool
    title: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange(
    typing.TypedDict, total=False
):
    endDate: GoogleTypeDate
    startDate: GoogleTypeDate

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaReportingIdentitySettings(
    typing.TypedDict, total=False
):
    name: str
    reportingIdentity: typing.Literal[
        "IDENTITY_BLENDING_STRATEGY_UNSPECIFIED", "BLENDED", "OBSERVED", "DEVICE_BASED"
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRollupPropertySourceLink(
    typing.TypedDict, total=False
):
    name: str
    sourceProperty: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRunAccessReportRequest(typing.TypedDict, total=False):
    dateRanges: _list[GoogleAnalyticsAdminV1alphaAccessDateRange]
    dimensionFilter: GoogleAnalyticsAdminV1alphaAccessFilterExpression
    dimensions: _list[GoogleAnalyticsAdminV1alphaAccessDimension]
    expandGroups: bool
    includeAllUsers: bool
    limit: str
    metricFilter: GoogleAnalyticsAdminV1alphaAccessFilterExpression
    metrics: _list[GoogleAnalyticsAdminV1alphaAccessMetric]
    offset: str
    orderBys: _list[GoogleAnalyticsAdminV1alphaAccessOrderBy]
    returnEntityQuota: bool
    timeZone: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRunAccessReportResponse(typing.TypedDict, total=False):
    dimensionHeaders: _list[GoogleAnalyticsAdminV1alphaAccessDimensionHeader]
    metricHeaders: _list[GoogleAnalyticsAdminV1alphaAccessMetricHeader]
    quota: GoogleAnalyticsAdminV1alphaAccessQuota
    rowCount: int
    rows: _list[GoogleAnalyticsAdminV1alphaAccessRow]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema(
    typing.TypedDict, total=False
):
    applyConversionValues: bool
    name: str
    postbackWindowOne: GoogleAnalyticsAdminV1alphaPostbackWindow
    postbackWindowThree: GoogleAnalyticsAdminV1alphaPostbackWindow
    postbackWindowTwo: GoogleAnalyticsAdminV1alphaPostbackWindow

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchAds360Link(typing.TypedDict, total=False):
    adsPersonalizationEnabled: bool
    advertiserDisplayName: str
    advertiserId: str
    campaignDataSharingEnabled: bool
    costDataSharingEnabled: bool
    name: str
    siteStatsSharingEnabled: bool

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest(
    typing.TypedDict, total=False
):
    action: _list[
        typing.Literal["ACTION_TYPE_UNSPECIFIED", "CREATED", "UPDATED", "DELETED"]
    ]
    actorEmail: _list[str]
    earliestChangeTime: str
    latestChangeTime: str
    pageSize: int
    pageToken: str
    property: str
    resourceType: _list[
        typing.Literal[
            "CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED",
            "ACCOUNT",
            "PROPERTY",
            "FIREBASE_LINK",
            "GOOGLE_ADS_LINK",
            "GOOGLE_SIGNALS_SETTINGS",
            "CONVERSION_EVENT",
            "MEASUREMENT_PROTOCOL_SECRET",
            "CUSTOM_DIMENSION",
            "CUSTOM_METRIC",
            "DATA_RETENTION_SETTINGS",
            "DISPLAY_VIDEO_360_ADVERTISER_LINK",
            "DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL",
            "SEARCH_ADS_360_LINK",
            "DATA_STREAM",
            "ATTRIBUTION_SETTINGS",
            "EXPANDED_DATA_SET",
            "CHANNEL_GROUP",
            "BIGQUERY_LINK",
            "ENHANCED_MEASUREMENT_SETTINGS",
            "DATA_REDACTION_SETTINGS",
            "SKADNETWORK_CONVERSION_VALUE_SCHEMA",
            "ADSENSE_LINK",
            "AUDIENCE",
            "EVENT_CREATE_RULE",
            "KEY_EVENT",
            "CALCULATED_METRIC",
            "REPORTING_DATA_ANNOTATION",
            "SUBPROPERTY_SYNC_CONFIG",
            "REPORTING_IDENTITY_SETTINGS",
            "USER_PROVIDED_DATA_SETTINGS",
        ]
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse(
    typing.TypedDict, total=False
):
    changeHistoryEvents: _list[GoogleAnalyticsAdminV1alphaChangeHistoryEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest(
    typing.TypedDict, total=False
):
    appInstanceId: str
    clientId: str
    userId: str
    userProvidedData: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse(
    typing.TypedDict, total=False
):
    deletionRequestTime: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilter(typing.TypedDict, total=False):
    applyToProperty: str
    filterClauses: _list[GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause]
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause(
    typing.TypedDict, total=False
):
    filterClauseType: typing.Literal[
        "FILTER_CLAUSE_TYPE_UNSPECIFIED", "INCLUDE", "EXCLUDE"
    ]
    filterExpression: GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition(
    typing.TypedDict, total=False
):
    fieldName: str
    nullFilter: bool
    stringFilter: GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter(
    typing.TypedDict, total=False
):
    caseSensitive: bool
    matchType: typing.Literal[
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
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression(
    typing.TypedDict, total=False
):
    filterCondition: GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition
    notExpression: GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression
    orGroup: GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList(
    typing.TypedDict, total=False
):
    filterExpressions: _list[
        GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression
    ]

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertySyncConfig(typing.TypedDict, total=False):
    applyToProperty: str
    customDimensionAndMetricSyncMode: typing.Literal[
        "SYNCHRONIZATION_MODE_UNSPECIFIED", "NONE", "ALL"
    ]
    name: str

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest(
    typing.TypedDict, total=False
):
    accessBinding: GoogleAnalyticsAdminV1alphaAccessBinding

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaUserProvidedDataSettings(
    typing.TypedDict, total=False
):
    automaticallyDetectedDataCollectionEnabled: bool
    name: str
    userProvidedDataCollectionEnabled: bool

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int
