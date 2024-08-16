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
        class LfpInventoriesResource(googleapiclient.discovery.Resource):
            def insert(
                self, *, parent: str, body: LfpInventory = ..., **kwargs: typing.Any
            ) -> LfpInventoryHttpRequest: ...

        @typing.type_check_only
        class LfpSalesResource(googleapiclient.discovery.Resource):
            def insert(
                self, *, parent: str, body: LfpSale = ..., **kwargs: typing.Any
            ) -> LfpSaleHttpRequest: ...

        @typing.type_check_only
        class LfpStoresResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LfpStoreHttpRequest: ...
            def insert(
                self, *, parent: str, body: LfpStore = ..., **kwargs: typing.Any
            ) -> LfpStoreHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                targetAccount: str = ...,
                **kwargs: typing.Any,
            ) -> ListLfpStoresResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLfpStoresResponseHttpRequest,
                previous_response: ListLfpStoresResponse,
            ) -> ListLfpStoresResponseHttpRequest | None: ...

        def lfpInventories(self) -> LfpInventoriesResource: ...
        def lfpSales(self) -> LfpSalesResource: ...
        def lfpStores(self) -> LfpStoresResource: ...

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
class LfpInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LfpInventory: ...

@typing.type_check_only
class LfpSaleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LfpSale: ...

@typing.type_check_only
class LfpStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LfpStore: ...

@typing.type_check_only
class ListLfpStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLfpStoresResponse: ...
