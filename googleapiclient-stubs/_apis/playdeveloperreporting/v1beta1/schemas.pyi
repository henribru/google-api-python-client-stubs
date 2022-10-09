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
class GooglePlayDeveloperReportingV1beta1CrashRateMetricSet(
    typing_extensions.TypedDict, total=False
):
    freshnessInfo: GooglePlayDeveloperReportingV1beta1FreshnessInfo
    name: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1DimensionValue(
    typing_extensions.TypedDict, total=False
):
    dimension: str
    int64Value: str
    stringValue: str
    valueLabel: str

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
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY"
    ]
    latestEndTime: GoogleTypeDateTime

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
    metric: str

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1MetricsRow(
    typing_extensions.TypedDict, total=False
):
    aggregationPeriod: typing_extensions.Literal[
        "AGGREGATION_PERIOD_UNSPECIFIED", "HOURLY", "DAILY"
    ]
    dimensions: _list[GooglePlayDeveloperReportingV1beta1DimensionValue]
    metrics: _list[GooglePlayDeveloperReportingV1beta1MetricValue]
    startTime: GoogleTypeDateTime

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

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryCrashRateMetricSetResponse(
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

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryExcessiveWakeupRateMetricSetResponse(
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

@typing.type_check_only
class GooglePlayDeveloperReportingV1beta1QueryStuckBackgroundWakelockRateMetricSetResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rows: _list[GooglePlayDeveloperReportingV1beta1MetricsRow]

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
