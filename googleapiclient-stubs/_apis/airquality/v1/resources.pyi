import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AirQualityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CurrentConditionsResource(googleapiclient.discovery.Resource):
        def lookup(
            self, *, body: LookupCurrentConditionsRequest = ..., **kwargs: typing.Any
        ) -> LookupCurrentConditionsResponseHttpRequest: ...

    @typing.type_check_only
    class ForecastResource(googleapiclient.discovery.Resource):
        def lookup(
            self, *, body: LookupForecastRequest = ..., **kwargs: typing.Any
        ) -> LookupForecastResponseHttpRequest: ...
        def lookup_next(
            self,
            previous_request: LookupForecastResponseHttpRequest,
            previous_response: LookupForecastResponse,
        ) -> LookupForecastResponseHttpRequest | None: ...

    @typing.type_check_only
    class HistoryResource(googleapiclient.discovery.Resource):
        def lookup(
            self, *, body: LookupHistoryRequest = ..., **kwargs: typing.Any
        ) -> LookupHistoryResponseHttpRequest: ...
        def lookup_next(
            self,
            previous_request: LookupHistoryResponseHttpRequest,
            previous_response: LookupHistoryResponse,
        ) -> LookupHistoryResponseHttpRequest | None: ...

    @typing.type_check_only
    class MapTypesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class HeatmapTilesResource(googleapiclient.discovery.Resource):
            def lookupHeatmapTile(
                self,
                *,
                mapType: typing_extensions.Literal[
                    "MAP_TYPE_UNSPECIFIED",
                    "UAQI_RED_GREEN",
                    "UAQI_INDIGO_PERSIAN",
                    "PM25_INDIGO_PERSIAN",
                    "GBR_DEFRA",
                    "DEU_UBA",
                    "CAN_EC",
                    "FRA_ATMO",
                    "US_AQI",
                ],
                zoom: int,
                x: int,
                y: int,
                **kwargs: typing.Any,
            ) -> HttpBodyHttpRequest: ...

        def heatmapTiles(self) -> HeatmapTilesResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def currentConditions(self) -> CurrentConditionsResource: ...
    def forecast(self) -> ForecastResource: ...
    def history(self) -> HistoryResource: ...
    def mapTypes(self) -> MapTypesResource: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HttpBody: ...

@typing.type_check_only
class LookupCurrentConditionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupCurrentConditionsResponse: ...

@typing.type_check_only
class LookupForecastResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupForecastResponse: ...

@typing.type_check_only
class LookupHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupHistoryResponse: ...
