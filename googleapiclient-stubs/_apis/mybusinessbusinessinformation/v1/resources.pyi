import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
                body: Location = ...,
                requestId: str = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readMask: str = ...,
                **kwargs: typing.Any
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
            categoryName: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            regionCode: str = ...,
            showAll: bool = ...,
            **kwargs: typing.Any
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
            languageCode: str = ...,
            names: str | _list[str] = ...,
            regionCode: str = ...,
            view: typing_extensions.Literal[
                "CATEGORY_VIEW_UNSPECIFIED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> BatchGetCategoriesResponseHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            regionCode: str = ...,
            view: typing_extensions.Literal[
                "CATEGORY_VIEW_UNSPECIFIED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
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
            self, *, chainName: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> SearchChainsResponseHttpRequest: ...

    @typing.type_check_only
    class GoogleLocationsResource(googleapiclient.discovery.Resource):
        def search(
            self, *, body: SearchGoogleLocationsRequest = ..., **kwargs: typing.Any
        ) -> SearchGoogleLocationsResponseHttpRequest: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AttributesResource(googleapiclient.discovery.Resource):
            def getGoogleUpdated(
                self, *, name: str, **kwargs: typing.Any
            ) -> AttributesHttpRequest: ...

        def associate(
            self,
            *,
            name: str,
            body: AssociateLocationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def clearLocationAssociation(
            self,
            *,
            name: str,
            body: ClearLocationAssociationRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(
            self, *, name: str, readMask: str = ..., **kwargs: typing.Any
        ) -> LocationHttpRequest: ...
        def getAttributes(
            self, *, name: str, **kwargs: typing.Any
        ) -> AttributesHttpRequest: ...
        def getGoogleUpdated(
            self, *, name: str, readMask: str = ..., **kwargs: typing.Any
        ) -> GoogleUpdatedLocationHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Location = ...,
            updateMask: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any
        ) -> LocationHttpRequest: ...
        def updateAttributes(
            self,
            *,
            name: str,
            body: Attributes = ...,
            attributeMask: str = ...,
            **kwargs: typing.Any
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
        | None = ...,
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
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Attributes: ...

@typing.type_check_only
class BatchGetCategoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetCategoriesResponse: ...

@typing.type_check_only
class ChainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Chain: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleUpdatedLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleUpdatedLocation: ...

@typing.type_check_only
class ListAttributeMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAttributeMetadataResponse: ...

@typing.type_check_only
class ListCategoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCategoriesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class SearchChainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchChainsResponse: ...

@typing.type_check_only
class SearchGoogleLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchGoogleLocationsResponse: ...
