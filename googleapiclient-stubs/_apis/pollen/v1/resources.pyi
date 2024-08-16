import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class PollenResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ForecastResource(googleapiclient.discovery.Resource):
        def lookup(
            self,
            *,
            days: int = ...,
            languageCode: str = ...,
            location_latitude: float = ...,
            location_longitude: float = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            plantsDescription: bool = ...,
            **kwargs: typing.Any,
        ) -> LookupForecastResponseHttpRequest: ...
        def lookup_next(
            self,
            previous_request: LookupForecastResponseHttpRequest,
            previous_response: LookupForecastResponse,
        ) -> LookupForecastResponseHttpRequest | None: ...

    @typing.type_check_only
    class MapTypesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class HeatmapTilesResource(googleapiclient.discovery.Resource):
            def lookupHeatmapTile(
                self,
                *,
                mapType: typing_extensions.Literal[
                    "MAP_TYPE_UNSPECIFIED", "TREE_UPI", "GRASS_UPI", "WEED_UPI"
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
    def forecast(self) -> ForecastResource: ...
    def mapTypes(self) -> MapTypesResource: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HttpBody: ...

@typing.type_check_only
class LookupForecastResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupForecastResponse: ...
