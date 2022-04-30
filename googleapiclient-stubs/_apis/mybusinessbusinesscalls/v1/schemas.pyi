import typing

import typing_extensions

_list = list

@typing.type_check_only
class AggregateMetrics(typing_extensions.TypedDict, total=False):
    answeredCallsCount: int
    endDate: Date
    hourlyMetrics: _list[HourlyMetrics]
    missedCallsCount: int
    startDate: Date
    weekdayMetrics: _list[WeekDayMetrics]

@typing.type_check_only
class BusinessCallsInsights(typing_extensions.TypedDict, total=False):
    aggregateMetrics: AggregateMetrics
    metricType: typing_extensions.Literal["METRIC_TYPE_UNSPECIFIED", "AGGREGATE_COUNT"]
    name: str

@typing.type_check_only
class BusinessCallsSettings(typing_extensions.TypedDict, total=False):
    callsState: typing_extensions.Literal[
        "CALLS_STATE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    consentTime: str
    name: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class HourlyMetrics(typing_extensions.TypedDict, total=False):
    hour: int
    missedCallsCount: int

@typing.type_check_only
class ListBusinessCallsInsightsResponse(typing_extensions.TypedDict, total=False):
    businessCallsInsights: _list[BusinessCallsInsights]
    nextPageToken: str

@typing.type_check_only
class WeekDayMetrics(typing_extensions.TypedDict, total=False):
    day: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    missedCallsCount: int
