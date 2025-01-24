import typing

import typing_extensions

_list = list

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1Anomaly(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[GooglePlayDeveloperReportingV1beta1DimensionValue]
    metric: GooglePlayDeveloperReportingV1beta1MetricValue
    metricSet: str
    name: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1AnrRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1App(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    packageName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1AppVersion(
    typing_extensions.TypedDict, total=False
):
    versionCode: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1CrashRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DecimalConfidenceInterval(
    typing_extensions.TypedDict, total=False
):
    lowerBound: GoogleTypeDecimal
    upperBound: GoogleTypeDecimal

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DeviceId(
    typing_extensions.TypedDict, total=False
):
    buildBrand: str
    buildDevice: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DeviceModelSummary(
    typing_extensions.TypedDict, total=False
):
    deviceId: GooglePlayDeveloperReportingV1beta1DeviceId
    deviceUri: str
    marketingName: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DimensionValue(
    typing_extensions.TypedDict, total=False
):
    dimension: str
    int64Value: str
    stringValue: str
    valueLabel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorCountMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorIssue(
    typing_extensions.TypedDict, total=False
):
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
    type: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ErrorReport(
    typing_extensions.TypedDict, total=False
):
    appVersion: GooglePlayDeveloperReportingV1beta1AppVersion
    deviceModel: GooglePlayDeveloperReportingV1beta1DeviceModelSummary
    eventTime: str
    issue: str
    name: str
    osVersion: GooglePlayDeveloperReportingV1beta1OsVersion
    reportText: str
    type: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH", "NON_FATAL"
    ]
    vcsInformation: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ExcessiveWakeupRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1FreshnessInfo(
    typing_extensions.TypedDict, total=False
):
    freshnesses: _list[GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshness]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1FreshnessInfoFreshness(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    latestEndTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1IssueAnnotation(
    typing_extensions.TypedDict, total=False
):
    body: str
    category: str
    title: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ListAnomaliesResponse(
    typing_extensions.TypedDict, total=False
):
    anomalies: _list[GooglePlayDeveloperReportingV1beta1Anomaly]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1MetricValue(
    typing_extensions.TypedDict, total=False
):
    decimalValue: GoogleTypeDecimal
    decimalValueConfidenceInterval: (
        GooglePlayDeveloperReportingV1beta1DecimalConfidenceInterval
    )
    metric: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1MetricsRow(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    dimensions: _list[GooglePlayDeveloperReportingV1beta1DimensionValue]
    metrics: _list[GooglePlayDeveloperReportingV1beta1MetricValue]
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1OsVersion(
    typing_extensions.TypedDict, total=False
):
    apiLevel: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryAnrRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryErrorCountMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowRenderingRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QuerySlowStartRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetRequest(
    typing_extensions.TypedDict, total=False
):
    dimensions: _list[str]
    filter: str
    metrics: _list[str]
    pageSize: int
    pageToken: str
    timelineSpec: GooglePlayDeveloperReportingV1beta1TimelineSpec
    userCohort: typing_extensions.Literal[
        "USER_COHORT_UNSPECIFIED", "OS_PUBLIC", "OS_BETA", "APP_TESTERS"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1Release(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    versionCodes: _list[str]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1ReleaseFilterOptions(
    typing_extensions.TypedDict, total=False
):
    tracks: _list[GooglePlayDeveloperReportingV1beta1Track]

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchAccessibleAppsResponse(
    typing_extensions.TypedDict, total=False
):
    apps: _list[GooglePlayDeveloperReportingV1beta1App]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchErrorIssuesResponse(
    typing_extensions.TypedDict, total=False
):
    errorIssues: _list[GooglePlayDeveloperReportingV1beta1ErrorIssue]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SearchErrorReportsResponse(
    typing_extensions.TypedDict, total=False
):
    errorReports: _list[GooglePlayDeveloperReportingV1beta1ErrorReport]
    nextPageToken: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SlowRenderingRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1SlowStartRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1StuckBackgroundWakelockRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1TimelineSpec(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY", "FULL_RANGE"
    ]
    endTime: GoogleTypeDateTime
    startTime: GoogleTypeDateTime

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1Track(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    servingReleases: _list[GooglePlayDeveloperReportingV1beta1Release]
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
