import typing

_list = list

@typing.type_check_only
class ApiservingMcpMcpToolVisibility(typing.TypedDict, total=False):
    fieldVisibility: _list[ApiservingMcpMcpToolVisibilityFieldVisibility]
    visibilityEnforcementStrategy: typing.Literal[
        "VISIBILITY_ENFORCEMENT_STRATEGY_UNSPECIFIED", "COMBINE", "OVERRIDE"
    ]
    visibilityRestriction: str

@typing.type_check_only
class ApiservingMcpMcpToolVisibilityFieldVisibility(typing.TypedDict, total=False):
    restriction: str
    selector: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1Anomaly(typing.TypedDict, total=False):
    dimensions: _list[GooglePlayDeveloperReportingV1alpha1DimensionValue]
    metric: GooglePlayDeveloperReportingV1alpha1MetricValue
    metricSet: str
    name: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1AnonRssAndSwapMemoryUsageMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1AnrRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1App(typing.TypedDict, total=False):
    displayName: str
    name: str
    packageName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1AppVersion(typing.TypedDict, total=False):
    versionCode: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1BitmapMemoryUsageMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1CrashRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DecimalConfidenceInterval(
    typing.TypedDict, total=False
):
    lowerBound: GoogleTypeDecimal
    upperBound: GoogleTypeDecimal

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DeviceId(typing.TypedDict, total=False):
    buildBrand: str
    buildDevice: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DeviceModelSummary(
    typing.TypedDict, total=False
):
    deviceId: GooglePlayDeveloperReportingV1alpha1DeviceId
    deviceUri: str
    marketingName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DimensionValue(typing.TypedDict, total=False):
    dimension: str
    int64Value: str
    stringValue: str
    valueLabel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorCountMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorIssue(typing.TypedDict, total=False):
    annotations: _list[GooglePlayDeveloperReportingV1alpha1IssueAnnotation]
    cause: str
    distinctUsers: str
    distinctUsersPercent: GoogleTypeDecimal
    errorReportCount: str
    firstAppVersion: GooglePlayDeveloperReportingV1alpha1AppVersion
    firstOsVersion: GooglePlayDeveloperReportingV1alpha1OsVersion
    issueUri: str
    lastAppVersion: GooglePlayDeveloperReportingV1alpha1AppVersion
    lastErrorReportTime: str
    lastOsVersion: GooglePlayDeveloperReportingV1alpha1OsVersion
    location: str
    name: str
    sampleErrorReports: _list[str]
    type: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorReport(typing.TypedDict, total=False):
    appVersion: GooglePlayDeveloperReportingV1alpha1AppVersion
    deviceModel: GooglePlayDeveloperReportingV1alpha1DeviceModelSummary
    eventTime: str
    issue: str
    name: str
    osVersion: GooglePlayDeveloperReportingV1alpha1OsVersion
    reportText: str
    type: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]
    vcsInformation: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ExcessiveWakeupRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1FreshnessInfo(typing.TypedDict, total=False):
    freshnesses: _list[GooglePlayDeveloperReportingV1alpha1FreshnessInfoFreshness]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1FreshnessInfoFreshness(
    typing.TypedDict, total=False
):
    aggregationPeriod: typing.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    latestEndTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1IssueAnnotation(
    typing.TypedDict, total=False
):
    body: str
    category: str
    title: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse(
    typing.TypedDict, total=False
):
    anomalies: _list[GooglePlayDeveloperReportingV1alpha1Anomaly]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1LmkRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1MetricValue(typing.TypedDict, total=False):
    decimalValue: GoogleTypeDecimal
    decimalValueConfidenceInterval: (
        GooglePlayDeveloperReportingV1alpha1DecimalConfidenceInterval
    )
    metric: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1MetricsRow(typing.TypedDict, total=False):
    aggregationPeriod: typing.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    dimensions: _list[GooglePlayDeveloperReportingV1alpha1DimensionValue]
    metrics: _list[GooglePlayDeveloperReportingV1alpha1MetricValue]
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1OsVersion(typing.TypedDict, total=False):
    apiLevel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnonRssAndSwapMemoryUsageMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnonRssAndSwapMemoryUsageMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryBitmapMemoryUsageMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryBitmapMemoryUsageMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryLmkRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryLmkRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowRenderingRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowRenderingRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowStartRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowStartRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1Release(typing.TypedDict, total=False):
    displayName: str
    versionCodes: _list[str]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ReleaseFilterOptions(
    typing.TypedDict, total=False
):
    tracks: _list[GooglePlayDeveloperReportingV1alpha1Track]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchAccessibleAppsResponse(
    typing.TypedDict, total=False
):
    apps: _list[GooglePlayDeveloperReportingV1alpha1App]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse(
    typing.TypedDict, total=False
):
    errorIssues: _list[GooglePlayDeveloperReportingV1alpha1ErrorIssue]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse(
    typing.TypedDict, total=False
):
    errorReports: _list[GooglePlayDeveloperReportingV1alpha1ErrorReport]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SlowRenderingRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SlowStartRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1TimelineSpec(typing.TypedDict, total=False):
    aggregationPeriod: typing.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    endTime: GoogleTypeDateTime
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1Track(typing.TypedDict, total=False):
    displayName: str
    servingReleases: _list[GooglePlayDeveloperReportingV1alpha1Release]
    type: str

@typing.type_check_only
class GoogleTypeDateTime(typing.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: GoogleTypeTimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class GoogleTypeDecimal(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleTypeTimeZone(typing.TypedDict, total=False):
    id: str
    version: str
