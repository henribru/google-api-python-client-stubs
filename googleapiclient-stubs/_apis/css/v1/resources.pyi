import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CssResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CssProductInputsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, supplementalFeedId: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def insert(
                self,
                *,
                parent: str,
                body: CssProductInput = ...,
                feedId: str = ...,
                **kwargs: typing.Any,
            ) -> CssProductInputHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: CssProductInput = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> CssProductInputHttpRequest: ...

        @typing.type_check_only
        class CssProductsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CssProductHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListCssProductsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCssProductsResponseHttpRequest,
                previous_response: ListCssProductsResponse,
            ) -> ListCssProductsResponseHttpRequest | None: ...

        @typing.type_check_only
        class LabelsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: AccountLabel = ..., **kwargs: typing.Any
            ) -> AccountLabelHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAccountLabelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountLabelsResponseHttpRequest,
                previous_response: ListAccountLabelsResponse,
            ) -> ListAccountLabelsResponseHttpRequest | None: ...
            def patch(
                self, *, name: str, body: AccountLabel = ..., **kwargs: typing.Any
            ) -> AccountLabelHttpRequest: ...

        def get(
            self, *, name: str, parent: str = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def listChildAccounts(
            self,
            *,
            parent: str,
            fullName: str = ...,
            labelId: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListChildAccountsResponseHttpRequest: ...
        def listChildAccounts_next(
            self,
            previous_request: ListChildAccountsResponseHttpRequest,
            previous_response: ListChildAccountsResponse,
        ) -> ListChildAccountsResponseHttpRequest | None: ...
        def updateLabels(
            self,
            *,
            name: str,
            body: UpdateAccountLabelsRequest = ...,
            **kwargs: typing.Any,
        ) -> AccountHttpRequest: ...
        def cssProductInputs(self) -> CssProductInputsResource: ...
        def cssProducts(self) -> CssProductsResource: ...
        def labels(self) -> LabelsResource: ...

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
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Account: ...

@typing.type_check_only
class AccountLabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountLabel: ...

@typing.type_check_only
class CssProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CssProduct: ...

@typing.type_check_only
class CssProductInputHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CssProductInput: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListAccountLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountLabelsResponse: ...

@typing.type_check_only
class ListChildAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListChildAccountsResponse: ...

@typing.type_check_only
class ListCssProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCssProductsResponse: ...
