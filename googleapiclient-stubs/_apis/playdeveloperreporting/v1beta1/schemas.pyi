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
class GooglePlayDeveloperReportingV1beta1Anomaly(typing.TypedDict, total=False):
    dimensions: _list[GooglePlayDeveloperReportingV1beta1DimensionValue]
    metric: GooglePlayDeveloperReportingV1beta1MetricValue
    metricSet: str
    name: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1AnonRssAndSwapMemoryUsageMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1AnrRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1App(typing.TypedDict, total=False):
    displayName: str
    name: str
    packageName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1AppVersion(typing.TypedDict, total=False):
    versionCode: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1BitmapMemoryUsageMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1CrashRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DecimalConfidenceInterval(
    typing.TypedDict, total=False
):
    lowerBound: GoogleTypeDecimal
    upperBound: GoogleTypeDecimal

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DeviceId(typing.TypedDict, total=False):
    buildBrand: str
    buildDevice: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DeviceModelSummary(
    typing.TypedDict, total=False
):
    deviceId: GooglePlayDeveloperReportingV1beta1DeviceId
    deviceUri: str
    marketingName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DimensionValue(typing.TypedDict, total=False):
    dimension: str
    int64Value: str
    stringValue: str
    valueLabel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorCountMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorIssue(typing.TypedDict, total=False):
    annotations: _list[GooglePlayDeveloperReportingV1beta1IssueAnnotation]
    cause: str
    distinctUsers: str
    distinctUsersPercent: GoogleTypeDecimal
    errorReportCount: str
    firstAppVersion: GooglePlayDeveloperReportingV1beta1AppVersion
    firstOsVersion: GooglePlayDeveloperReportingV1beta1OsVersion
    issueUri: str
    lastAppVersion: GooglePlayDeveloperReportingV1beta1AppVersion
    lastErrorReportTime: str
    lastOsVersion: GooglePlayDeveloperReportingV1beta1OsVersion
    location: str
    name: str
    sampleErrorReports: _list[str]
    type: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorReport(typing.TypedDict, total=False):
    appVersion: GooglePlayDeveloperReportingV1beta1AppVersion
    deviceModel: GooglePlayDeveloperReportingV1beta1DeviceModelSummary
    eventTime: str
    issue: str
    name: str
    osVersion: GooglePlayDeveloperReportingV1beta1OsVersion
    reportText: str
    type: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]
    vcsInformation: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1FreshnessInfo(typing.TypedDict, total=False):
    freshnesses: _list[GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshness]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshness(
    typing.TypedDict, total=False
):
    aggregationPeriod: typing.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    latestEndTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1IssueAnnotation(typing.TypedDict, total=False):
    body: str
    category: str
    title: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ListAnomaliesResponse(
    typing.TypedDict, total=False
):
    anomalies: _list[GooglePlayDeveloperReportingV1beta1Anomaly]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1LmkRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1MetricValue(typing.TypedDict, total=False):
    decimalValue: GoogleTypeDecimal
    decimalValueConfidenceInterval: (
        GooglePlayDeveloperReportingV1beta1DecimalConfidenceInterval
    )
    metric: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1MetricsRow(typing.TypedDict, total=False):
    aggregationPeriod: typing.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    dimensions: _list[GooglePlayDeveloperReportingV1beta1DimensionValue]
    metrics: _list[GooglePlayDeveloperReportingV1beta1MetricValue]
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1OsVersion(typing.TypedDict, total=False):
    apiLevel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnonRssAndSwapMemoryUsageMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnonRssAndSwapMemoryUsageMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryBitmapMemoryUsageMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryBitmapMemoryUsageMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryLmkRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryLmkRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequest(
    typing.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1Release(typing.TypedDict, total=False):
    displayName: str
    versionCodes: _list[str]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ReleaseFilterOptions(
    typing.TypedDict, total=False
):
    tracks: _list[GooglePlayDeveloperReportingV1beta1Track]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponse(
    typing.TypedDict, total=False
):
    apps: _list[GooglePlayDeveloperReportingV1beta1App]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponse(
    typing.TypedDict, total=False
):
    errorIssues: _list[GooglePlayDeveloperReportingV1beta1ErrorIssue]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponse(
    typing.TypedDict, total=False
):
    errorReports: _list[GooglePlayDeveloperReportingV1beta1ErrorReport]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSet(
    typing.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1TimelineSpec(typing.TypedDict, total=False):
    aggregationPeriod: typing.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    endTime: GoogleTypeDateTime
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1Track(typing.TypedDict, total=False):
    displayName: str
    servingReleases: _list[GooglePlayDeveloperReportingV1beta1Release]
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
