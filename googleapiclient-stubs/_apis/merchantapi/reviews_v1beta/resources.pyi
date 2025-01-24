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
        class MerchantReviewsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MerchantReviewHttpRequest: ...
            def insert(
                self,
                *,
                parent: str,
                body: MerchantReview = ...,
                dataSource: str = ...,
                **kwargs: typing.Any,
            ) -> MerchantReviewHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListMerchantReviewsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMerchantReviewsResponseHttpRequest,
                previous_response: ListMerchantReviewsResponse,
            ) -> ListMerchantReviewsResponseHttpRequest | None: ...

        @typing.type_check_only
        class ProductReviewsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ProductReviewHttpRequest: ...
            def insert(
                self,
                *,
                parent: str,
                body: ProductReview = ...,
                dataSource: str = ...,
                **kwargs: typing.Any,
            ) -> ProductReviewHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListProductReviewsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProductReviewsResponseHttpRequest,
                previous_response: ListProductReviewsResponse,
            ) -> ListProductReviewsResponseHttpRequest | None: ...

        def merchantReviews(self) -> MerchantReviewsResource: ...
        def productReviews(self) -> ProductReviewsResource: ...

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
class ListMerchantReviewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMerchantReviewsResponse: ...

@typing.type_check_only
class ListProductReviewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProductReviewsResponse: ...

@typing.type_check_only
class MerchantReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MerchantReview: ...

@typing.type_check_only
class ProductReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductReview: ...
