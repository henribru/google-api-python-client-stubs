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
class GooglePlayDeveloperReportingV1alpha1CrashRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1alpha1FreshnessInfo
    name: str

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
    cause: str
    location: str
    name: str
    type: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH"
    ]

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1ErrorReport(
    typing_extensions.TypedDict, total=False
):
    issue: str
    name: str
    reportText: str
    type: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED", "APPLICATION_NOT_RESPONDING", "CRASH"
    ]

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
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY"
    ]
    latestEndTime: GoogleTypeDateTime

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
    metric: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1MetricsRow(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY"
    ]
    dimensions: _list[GooglePlayDeveloperReportingV1alpha1DimensionValue]
    metrics: _list[GooglePlayDeveloperReportingV1alpha1MetricValue]
    startTime: GoogleTypeDateTime

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

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryExcessiveWakeupRateMetricSetResponse(
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

@typing.type_check_only
class GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1alpha1MetricsRow]

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
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY"
    ]
    endTime: GoogleTypeDateTime
    startTime: GoogleTypeDateTime

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
