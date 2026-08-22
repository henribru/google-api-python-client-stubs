import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MyBusinessBusinessInformationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Location,
                requestId: str | None = ...,
                validateOnly: bool | None = ...,
                **kwargs: typing.Any,
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                readMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class AttributesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            categoryName: str | None = ...,
            languageCode: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            parent: str | None = ...,
            regionCode: str | None = ...,
            showAll: bool | None = ...,
            **kwargs: typing.Any,
        ) -> ListAttributeMetadataResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAttributeMetadataResponseHttpRequest,
            previous_response: ListAttributeMetadataResponse,
        ) -> ListAttributeMetadataResponseHttpRequest | None: ...

    @typing.type_check_only
    class CategoriesResource(googleapiclient.discovery.Resource):
        def batchGet(
            self,
            *,
            languageCode: str | None = ...,
            names: str | _list[str] | None = ...,
            regionCode: str | None = ...,
            view: typing.Literal["CATEGORY_VIEW_UNSPECIFIED", "BASIC", "FULL"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> BatchGetCategoriesResponseHttpRequest: ...
        def list(
            self,
            *,
            filter: str | None = ...,
            languageCode: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            regionCode: str | None = ...,
            view: typing.Literal["CATEGORY_VIEW_UNSPECIFIED", "BASIC", "FULL"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> ListCategoriesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCategoriesResponseHttpRequest,
            previous_response: ListCategoriesResponse,
        ) -> ListCategoriesResponseHttpRequest | None: ...

    @typing.type_check_only
    class ChainsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> ChainHttpRequest: ...
        def search(
            self,
            *,
            chainName: str | None = ...,
            pageSize: int | None = ...,
            **kwargs: typing.Any,
        ) -> SearchChainsResponseHttpRequest: ...

    @typing.type_check_only
    class GoogleLocationsResource(googleapiclient.discovery.Resource):
        def search(
            self, *, body: SearchGoogleLocationsRequest, **kwargs: typing.Any
        ) -> SearchGoogleLocationsResponseHttpRequest: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AttributesResource(googleapiclient.discovery.Resource):
            def getGoogleUpdated(
                self, *, name: str, **kwargs: typing.Any
            ) -> AttributesHttpRequest: ...

        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(
            self, *, name: str, readMask: str | None = ..., **kwargs: typing.Any
        ) -> LocationHttpRequest: ...
        def getAttributes(
            self, *, name: str, **kwargs: typing.Any
        ) -> AttributesHttpRequest: ...
        def getGoogleUpdated(
            self, *, name: str, readMask: str | None = ..., **kwargs: typing.Any
        ) -> GoogleUpdatedLocationHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Location,
            updateMask: str | None = ...,
            validateOnly: bool | None = ...,
            **kwargs: typing.Any,
        ) -> LocationHttpRequest: ...
        def updateAttributes(
            self,
            *,
            name: str,
            body: Attributes,
            attributeMask: str | None = ...,
            **kwargs: typing.Any,
        ) -> AttributesHttpRequest: ...
        def attributes(self) -> AttributesResource: ...

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
    def accounts(self) -> AccountsResource: ...
    def attributes(self) -> AttributesResource: ...
    def categories(self) -> CategoriesResource: ...
    def chains(self) -> ChainsResource: ...
    def googleLocations(self) -> GoogleLocationsResource: ...
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class AttributesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Attributes: ...

@typing.type_check_only
class BatchGetCategoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetCategoriesResponse: ...

@typing.type_check_only
class ChainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Chain: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleUpdatedLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleUpdatedLocation: ...

@typing.type_check_only
class ListAttributeMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAttributeMetadataResponse: ...

@typing.type_check_only
class ListCategoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCategoriesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class SearchChainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchChainsResponse: ...

@typing.type_check_only
class SearchGoogleLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchGoogleLocationsResponse: ...
