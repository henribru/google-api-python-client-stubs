import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class TravelImpactModelResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FlightsResource(googleapiclient.discovery.Resource):
        def computeFlightEmissions(
            self, *, body: ComputeFlightEmissionsRequest = ..., **kwargs: typing.Any
        ) -> ComputeFlightEmissionsResponseHttpRequest: ...
        def computeTypicalFlightEmissions(
            self,
            *,
            body: ComputeTypicalFlightEmissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> ComputeTypicalFlightEmissionsResponseHttpRequest: ...

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
    def flights(self) -> FlightsResource: ...

@typing.type_check_only
class ComputeFlightEmissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ComputeFlightEmissionsResponse: ...

@typing.type_check_only
class ComputeTypicalFlightEmissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ComputeTypicalFlightEmissionsResponse: ...
