import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudProductRegistryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LogicalProductsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class VariantsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogicalProductVariantHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListLogicalProductVariantsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLogicalProductVariantsResponseHttpRequest,
                previous_response: ListLogicalProductVariantsResponse,
            ) -> ListLogicalProductVariantsResponseHttpRequest | None: ...
            def lookupEntity(
                self, *, lookupUri: str, **kwargs: typing.Any
            ) -> LookupEntityResponseHttpRequest: ...

        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> LogicalProductHttpRequest: ...
        def list(
            self,
            *,
            filter: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListLogicalProductsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListLogicalProductsResponseHttpRequest,
            previous_response: ListLogicalProductsResponse,
        ) -> ListLogicalProductsResponseHttpRequest | None: ...
        def lookupEntity(
            self, *, lookupUri: str, **kwargs: typing.Any
        ) -> LookupEntityResponseHttpRequest: ...
        def variants(self) -> VariantsResource: ...

    @typing.type_check_only
    class ProductSuitesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> ProductSuiteHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListProductSuitesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListProductSuitesResponseHttpRequest,
            previous_response: ListProductSuitesResponse,
        ) -> ListProductSuitesResponseHttpRequest | None: ...
        def lookupEntity(
            self, *, lookupUri: str, **kwargs: typing.Any
        ) -> LookupEntityResponseHttpRequest: ...

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
    def logicalProducts(self) -> LogicalProductsResource: ...
    def productSuites(self) -> ProductSuitesResource: ...

@typing.type_check_only
class ListLogicalProductVariantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLogicalProductVariantsResponse: ...

@typing.type_check_only
class ListLogicalProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLogicalProductsResponse: ...

@typing.type_check_only
class ListProductSuitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProductSuitesResponse: ...

@typing.type_check_only
class LogicalProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogicalProduct: ...

@typing.type_check_only
class LogicalProductVariantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogicalProductVariant: ...

@typing.type_check_only
class LookupEntityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupEntityResponse: ...

@typing.type_check_only
class ProductSuiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductSuite: ...
