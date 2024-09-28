import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SolarResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BuildingInsightsResource(googleapiclient.discovery.Resource):
        def findClosest(
            self,
            *,
            experiments: typing_extensions.Literal[
                "EXPERIMENT_UNSPECIFIED", "EXPANDED_COVERAGE"
            ]
            | _list[
                typing_extensions.Literal["EXPERIMENT_UNSPECIFIED", "EXPANDED_COVERAGE"]
            ] = ...,
            location_latitude: float = ...,
            location_longitude: float = ...,
            requiredQuality: typing_extensions.Literal[
                "IMAGERY_QUALITY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BASE"
            ] = ...,
            **kwargs: typing.Any,
        ) -> BuildingInsightsHttpRequest: ...

    @typing.type_check_only
    class DataLayersResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            exactQualityRequired: bool = ...,
            experiments: typing_extensions.Literal[
                "EXPERIMENT_UNSPECIFIED", "EXPANDED_COVERAGE"
            ]
            | _list[
                typing_extensions.Literal["EXPERIMENT_UNSPECIFIED", "EXPANDED_COVERAGE"]
            ] = ...,
            location_latitude: float = ...,
            location_longitude: float = ...,
            pixelSizeMeters: float = ...,
            radiusMeters: float = ...,
            requiredQuality: typing_extensions.Literal[
                "IMAGERY_QUALITY_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "BASE"
            ] = ...,
            view: typing_extensions.Literal[
                "DATA_LAYER_VIEW_UNSPECIFIED",
                "DSM_LAYER",
                "IMAGERY_LAYERS",
                "IMAGERY_AND_ANNUAL_FLUX_LAYERS",
                "IMAGERY_AND_ALL_FLUX_LAYERS",
                "FULL_LAYERS",
            ] = ...,
            **kwargs: typing.Any,
        ) -> DataLayersHttpRequest: ...

    @typing.type_check_only
    class GeoTiffResource(googleapiclient.discovery.Resource):
        def get(
            self, *, id: str = ..., **kwargs: typing.Any
        ) -> HttpBodyHttpRequest: ...

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
    def buildingInsights(self) -> BuildingInsightsResource: ...
    def dataLayers(self) -> DataLayersResource: ...
    def geoTiff(self) -> GeoTiffResource: ...

@typing.type_check_only
class BuildingInsightsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BuildingInsights: ...

@typing.type_check_only
class DataLayersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DataLayers: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HttpBody: ...
