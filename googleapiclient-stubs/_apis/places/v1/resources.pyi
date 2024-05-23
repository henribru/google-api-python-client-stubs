import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MapsPlacesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PlacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PhotosResource(googleapiclient.discovery.Resource):
            def getMedia(
                self,
                *,
                name: str,
                maxHeightPx: int = ...,
                maxWidthPx: int = ...,
                skipHttpRedirect: bool = ...,
                **kwargs: typing.Any,
            ) -> GoogleMapsPlacesV1PhotoMediaHttpRequest: ...

        def autocomplete(
            self,
            *,
            body: GoogleMapsPlacesV1AutocompletePlacesRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleMapsPlacesV1AutocompletePlacesResponseHttpRequest: ...
        def get(
            self,
            *,
            name: str,
            languageCode: str = ...,
            regionCode: str = ...,
            sessionToken: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleMapsPlacesV1PlaceHttpRequest: ...
        def searchNearby(
            self,
            *,
            body: GoogleMapsPlacesV1SearchNearbyRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleMapsPlacesV1SearchNearbyResponseHttpRequest: ...
        def searchText(
            self,
            *,
            body: GoogleMapsPlacesV1SearchTextRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleMapsPlacesV1SearchTextResponseHttpRequest: ...
        def searchText_next(
            self,
            previous_request: GoogleMapsPlacesV1SearchTextResponseHttpRequest,
            previous_response: GoogleMapsPlacesV1SearchTextResponse,
        ) -> GoogleMapsPlacesV1SearchTextResponseHttpRequest | None: ...
        def photos(self) -> PhotosResource: ...

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
    def places(self) -> PlacesResource: ...

@typing.type_check_only
class GoogleMapsPlacesV1AutocompletePlacesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsPlacesV1AutocompletePlacesResponse: ...

@typing.type_check_only
class GoogleMapsPlacesV1PhotoMediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsPlacesV1PhotoMedia: ...

@typing.type_check_only
class GoogleMapsPlacesV1PlaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsPlacesV1Place: ...

@typing.type_check_only
class GoogleMapsPlacesV1SearchNearbyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsPlacesV1SearchNearbyResponse: ...

@typing.type_check_only
class GoogleMapsPlacesV1SearchTextResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsPlacesV1SearchTextResponse: ...
