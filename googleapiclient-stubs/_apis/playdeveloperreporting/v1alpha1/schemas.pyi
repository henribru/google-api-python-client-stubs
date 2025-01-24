import typing

import typing_extensions

_list = list

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1Anomaly(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GooglePlayDeveloperReportingV1alpha1DimensionValue]
    metric: GooglePlayDeveloperReportingV1alpha1MetricValue
    metricSet: str
    name: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1AnrRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1App(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    packageName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1AppVersion(
    typing_extensions.TypedDict, total=False
):
    versionCode: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1CrashRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DecimalConfidenceInterval(
    typing_extensions.TypedDict, total=False
):
    lowerBound: GoogleTypeDecimal
    upperBound: GoogleTypeDecimal

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DeviceId(
    typing_extensions.TypedDict, total=False
):
    buildBrand: str
    buildDevice: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DeviceModelSummary(
    typing_extensions.TypedDict, total=False
):
    deviceId: GooglePlayDeveloperReportingV1alpha1DeviceId
    deviceUri: str
    marketingName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1DimensionValue(
    typing_extensions.TypedDict, total=False
):
    dimension: str
    int64Value: str
    stringValue: str
    valueLabel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorCountMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorIssue(
    typing_extensions.TypedDict, total=False
):
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
    type: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorReport(
    typing_extensions.TypedDict, total=False
):
    appVersion: GooglePlayDeveloperReportingV1alpha1AppVersion
    deviceModel: GooglePlayDeveloperReportingV1alpha1DeviceModelSummary
    eventTime: str
    issue: str
    name: str
    osVersion: GooglePlayDeveloperReportingV1alpha1OsVersion
    reportText: str
    type: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]
    vcsInformation: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ExcessiveWakeupRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1FreshnessInfo(
    typing_extensions.TypedDict, total=False
):
    freshnesses: _list[GooglePlayDeveloperReportingV1alpha1FreshnessInfoFreshness]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1FreshnessInfoFreshness(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    latestEndTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1IssueAnnotation(
    typing_extensions.TypedDict, total=False
):
    body: str
    category: str
    title: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse(
    typing_extensions.TypedDict, total=False
):
    anomalies: _list[GooglePlayDeveloperReportingV1alpha1Anomaly]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1MetricValue(
    typing_extensions.TypedDict, total=False
):
    decimalValue: GoogleTypeDecimal
    decimalValueConfidenceInterval: (
        GooglePlayDeveloperReportingV1alpha1DecimalConfidenceInterval
    )
    metric: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1MetricsRow(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    dimensions: _list[GooglePlayDeveloperReportingV1alpha1DimensionValue]
    metrics: _list[GooglePlayDeveloperReportingV1alpha1MetricValue]
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1OsVersion(
    typing_extensions.TypedDict, total=False
):
    apiLevel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryAnrRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryCrashRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryErrorCountMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowRenderingRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowRenderingRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowStartRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QuerySlowStartRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1alpha1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1Release(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    versionCodes: _list[str]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ReleaseFilterOptions(
    typing_extensions.TypedDict, total=False
):
    tracks: _list[GooglePlayDeveloperReportingV1alpha1Track]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchAccessibleAppsResponse(
    typing_extensions.TypedDict, total=False
):
    apps: _list[GooglePlayDeveloperReportingV1alpha1App]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse(
    typing_extensions.TypedDict, total=False
):
    errorIssues: _list[GooglePlayDeveloperReportingV1alpha1ErrorIssue]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse(
    typing_extensions.TypedDict, total=False
):
    errorReports: _list[GooglePlayDeveloperReportingV1alpha1ErrorReport]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SlowRenderingRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1SlowStartRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1TimelineSpec(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    endTime: GoogleTypeDateTime
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1Track(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    servingReleases: _list[GooglePlayDeveloperReportingV1alpha1Release]
    type: str

@typing.type_check_only
class GoogleTypeDateTime(typing_extensions.TypedDict, total=False):
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
class GoogleTypeDecimal(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleTypeTimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
