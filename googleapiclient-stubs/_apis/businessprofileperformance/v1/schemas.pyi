import typing

import typing_extensions

_list = list

@typing.type_check_only
class DailyMetricTimeSeries(typing_extensions.TypedDict, total=False):
    dailyMetric: typing_extensions.Literal[
        "DAILY_METRIC_UNKNOWN",
        "BUSINESS_IMPRESSIONS_DESKTOP_MAPS",
        "BUSINESS_IMPRESSIONS_DESKTOP_SEARCH",
        "BUSINESS_IMPRESSIONS_MOBILE_MAPS",
        "BUSINESS_IMPRESSIONS_MOBILE_SEARCH",
        "BUSINESS_CONVERSATIONS",
        "BUSINESS_DIRECTION_REQUESTS",
        "CALL_CLICKS",
        "WEBSITE_CLICKS",
        "BUSINESS_BOOKINGS",
        "BUSINESS_FOOD_ORDERS",
        "BUSINESS_FOOD_MENU_CLICKS",
    ]
    dailySubEntityType: DailySubEntityType
    timeSeries: TimeSeries

@typing.type_check_only
class DailySubEntityType(typing_extensions.TypedDict, total=False):
    dayOfWeek: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    timeOfDay: TimeOfDay

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DatedValue(typing_extensions.TypedDict, total=False):
    date: Date
    value: str

@typing.type_check_only
class FetchMultiDailyMetricsTimeSeriesResponse(
    typing_extensions.TypedDict, total=False
):
    multiDailyMetricTimeSeries: _list[MultiDailyMetricTimeSeries]

@typing.type_check_only
class GetDailyMetricsTimeSeriesResponse(typing_extensions.TypedDict, total=False):
    timeSeries: TimeSeries

@typing.type_check_only
class InsightsValue(typing_extensions.TypedDict, total=False):
    threshold: str
    value: str

@typing.type_check_only
class ListSearchKeywordImpressionsMonthlyResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    searchKeywordsCounts: _list[SearchKeywordCount]

@typing.type_check_only
class MultiDailyMetricTimeSeries(typing_extensions.TypedDict, total=False):
    dailyMetricTimeSeries: _list[DailyMetricTimeSeries]

@typing.type_check_only
class SearchKeywordCount(typing_extensions.TypedDict, total=False):
    insightsValue: InsightsValue
    searchKeyword: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeSeries(typing_extensions.TypedDict, total=False):
    datedValues: _list[DatedValue]
