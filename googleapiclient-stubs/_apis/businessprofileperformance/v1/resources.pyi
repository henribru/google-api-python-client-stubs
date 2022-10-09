import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BusinessProfilePerformanceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SearchkeywordsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ImpressionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class MonthlyResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        monthlyRange_endMonth_day: int = ...,
                        monthlyRange_endMonth_month: int = ...,
                        monthlyRange_endMonth_year: int = ...,
                        monthlyRange_startMonth_day: int = ...,
                        monthlyRange_startMonth_month: int = ...,
                        monthlyRange_startMonth_year: int = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListSearchKeywordImpressionsMonthlyResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListSearchKeywordImpressionsMonthlyResponseHttpRequest,
                        previous_response: ListSearchKeywordImpressionsMonthlyResponse,
                    ) -> ListSearchKeywordImpressionsMonthlyResponseHttpRequest | None: ...

                def monthly(self) -> MonthlyResource: ...

            def impressions(self) -> ImpressionsResource: ...

        def getDailyMetricsTimeSeries(
            self,
            *,
            name: str,
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
            ] = ...,
            dailyRange_endDate_day: int = ...,
            dailyRange_endDate_month: int = ...,
            dailyRange_endDate_year: int = ...,
            dailyRange_startDate_day: int = ...,
            dailyRange_startDate_month: int = ...,
            dailyRange_startDate_year: int = ...,
            dailySubEntityType_dayOfWeek: typing_extensions.Literal[
                "DAY_OF_WEEK_UNSPECIFIED",
                "MONDAY",
                "TUESDAY",
                "WEDNESDAY",
                "THURSDAY",
                "FRIDAY",
                "SATURDAY",
                "SUNDAY",
            ] = ...,
            dailySubEntityType_timeOfDay_hours: int = ...,
            dailySubEntityType_timeOfDay_minutes: int = ...,
            dailySubEntityType_timeOfDay_nanos: int = ...,
            dailySubEntityType_timeOfDay_seconds: int = ...,
            **kwargs: typing.Any
        ) -> GetDailyMetricsTimeSeriesResponseHttpRequest: ...
        def searchkeywords(self) -> SearchkeywordsResource: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class GetDailyMetricsTimeSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetDailyMetricsTimeSeriesResponse: ...

@typing.type_check_only
class ListSearchKeywordImpressionsMonthlyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSearchKeywordImpressionsMonthlyResponse: ...
