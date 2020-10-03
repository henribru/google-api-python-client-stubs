import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PlayableLocationsResource(googleapiclient.discovery.Resource):
    class V3Resource(googleapiclient.discovery.Resource):
        def samplePlayableLocations(
            self,
            *,
            body: GoogleMapsPlayablelocationsV3SamplePlayableLocationsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponseHttpRequest: ...
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
    def v3(self) -> V3Resource: ...

class GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse: ...

class GoogleMapsPlayablelocationsV3LogImpressionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleMapsPlayablelocationsV3LogImpressionsResponse: ...

class GoogleMapsPlayablelocationsV3LogPlayerReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleMapsPlayablelocationsV3LogPlayerReportsResponse: ...
