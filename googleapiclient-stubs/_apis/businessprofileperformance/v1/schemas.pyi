import typing

import typing_extensions

_list = list

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
class SearchKeywordCount(typing_extensions.TypedDict, total=False):
    insightsValue: InsightsValue
    searchKeyword: str

@typing.type_check_only
class TimeSeries(typing_extensions.TypedDict, total=False):
    datedValues: _list[DatedValue]
