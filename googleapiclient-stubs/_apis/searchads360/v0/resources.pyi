import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SA360Resource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CustomColumnsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, resourceName: str, **kwargs: typing.Any
            ) -> GoogleAdsSearchads360V0Resources__CustomColumnHttpRequest: ...
            def list(
                self, *, customerId: str, **kwargs: typing.Any
            ) -> (
                GoogleAdsSearchads360V0Services__ListCustomColumnsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class SearchAds360Resource(googleapiclient.discovery.Resource):
            def search(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V0Services__SearchSearchAds360Request = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseHttpRequest
            ): ...
            def search_next(
                self,
                previous_request: GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseHttpRequest,
                previous_response: GoogleAdsSearchads360V0Services__SearchSearchAds360Response,
            ) -> (
                GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseHttpRequest
                | None
            ): ...

        def listAccessibleCustomers(
            self, **kwargs: typing.Any
        ) -> (
            GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseHttpRequest
        ): ...
        def customColumns(self) -> CustomColumnsResource: ...
        def searchAds360(self) -> SearchAds360Resource: ...

    @typing.type_check_only
    class SearchAds360FieldsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GoogleAdsSearchads360V0Resources__SearchAds360FieldHttpRequest: ...
        def search(
            self,
            *,
            body: GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsRequest = ...,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseHttpRequest
        ): ...
        def search_next(
            self,
            previous_request: GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseHttpRequest,
            previous_response: GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponse,
        ) -> (
            GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseHttpRequest
            | None
        ): ...

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
    def customers(self) -> CustomersResource: ...
    def searchAds360Fields(self) -> SearchAds360FieldsResource: ...

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__CustomColumnHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V0Resources__CustomColumn: ...

@typing.type_check_only
class GoogleAdsSearchads360V0Resources__SearchAds360FieldHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V0Resources__SearchAds360Field: ...

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V0Services__ListAccessibleCustomersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V0Services__ListCustomColumnsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V0Services__ListCustomColumnsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V0Services__SearchSearchAds360FieldsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V0Services__SearchSearchAds360ResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V0Services__SearchSearchAds360Response: ...
