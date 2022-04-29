import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MyBusinessPlaceActionsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PlaceActionLinksResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: PlaceActionLink = ..., **kwargs: typing.Any
            ) -> PlaceActionLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PlaceActionLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPlaceActionLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPlaceActionLinksResponseHttpRequest,
                previous_response: ListPlaceActionLinksResponse,
            ) -> ListPlaceActionLinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: PlaceActionLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> PlaceActionLinkHttpRequest: ...

        def placeActionLinks(self) -> PlaceActionLinksResource: ...

    @typing.type_check_only
    class PlaceActionTypeMetadataResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            filter: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListPlaceActionTypeMetadataResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPlaceActionTypeMetadataResponseHttpRequest,
            previous_response: ListPlaceActionTypeMetadataResponse,
        ) -> ListPlaceActionTypeMetadataResponseHttpRequest | None: ...

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
    def placeActionTypeMetadata(self) -> PlaceActionTypeMetadataResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListPlaceActionLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPlaceActionLinksResponse: ...

@typing.type_check_only
class ListPlaceActionTypeMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPlaceActionTypeMetadataResponse: ...

@typing.type_check_only
class PlaceActionLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlaceActionLink: ...
