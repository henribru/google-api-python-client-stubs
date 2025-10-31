import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MerchantResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProductsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocalInventoriesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def insert(
                    self,
                    *,
                    parent: str,
                    body: LocalInventory = ...,
                    **kwargs: typing.Any,
                ) -> LocalInventoryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListLocalInventoriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLocalInventoriesResponseHttpRequest,
                    previous_response: ListLocalInventoriesResponse,
                ) -> ListLocalInventoriesResponseHttpRequest | None: ...

            @typing.type_check_only
            class RegionalInventoriesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def insert(
                    self,
                    *,
                    parent: str,
                    body: RegionalInventory = ...,
                    **kwargs: typing.Any,
                ) -> RegionalInventoryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRegionalInventoriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRegionalInventoriesResponseHttpRequest,
                    previous_response: ListRegionalInventoriesResponse,
                ) -> ListRegionalInventoriesResponseHttpRequest | None: ...

            def localInventories(self) -> LocalInventoriesResource: ...
            def regionalInventories(self) -> RegionalInventoriesResource: ...

        def products(self) -> ProductsResource: ...

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

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListLocalInventoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocalInventoriesResponse: ...

@typing.type_check_only
class ListRegionalInventoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRegionalInventoriesResponse: ...

@typing.type_check_only
class LocalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LocalInventory: ...

@typing.type_check_only
class RegionalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RegionalInventory: ...
