import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PlayableLocationsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V3Resource(googleapiclient.discovery.Resource):
        def logImpressions(
            self,
            *,
            body: GoogleMapsPlayablelocationsV3LogImpressionsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleMapsPlayablelocationsV3LogImpressionsResponseHttpRequest: ...
        def logPlayerReports(
            self,
            *,
            body: GoogleMapsPlayablelocationsV3LogPlayerReportsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleMapsPlayablelocationsV3LogPlayerReportsResponseHttpRequest: ...
        def samplePlayableLocations(
            self,
            *,
            body: GoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponseHttpRequest: ...

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
    def v3(self) -> V3Resource: ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogImpressionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleMapsPlayablelocationsV3LogImpressionsResponse: ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3LogPlayerReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleMapsPlayablelocationsV3LogPlayerReportsResponse: ...

@typing.type_check_only
class GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse: ...
