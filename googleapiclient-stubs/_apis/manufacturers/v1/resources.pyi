import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ManufacturerCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LanguagesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ProductCertificationsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProductCertificationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListProductCertificationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListProductCertificationsResponseHttpRequest,
                    previous_response: ListProductCertificationsResponse,
                ) -> ListProductCertificationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ProductCertification = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> ProductCertificationHttpRequest: ...

            def productCertifications(self) -> ProductCertificationsResource: ...

        @typing.type_check_only
        class ProductsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, parent: str, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                parent: str,
                name: str,
                include: typing_extensions.Literal[
                    "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                ]
                | _list[
                    typing_extensions.Literal[
                        "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                    ]
                ] = ...,
                **kwargs: typing.Any,
            ) -> ProductHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                include: typing_extensions.Literal[
                    "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                ]
                | _list[
                    typing_extensions.Literal[
                        "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                    ]
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListProductsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProductsResponseHttpRequest,
                previous_response: ListProductsResponse,
            ) -> ListProductsResponseHttpRequest | None: ...
            def update(
                self,
                *,
                parent: str,
                name: str,
                body: Attributes = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...

        def languages(self) -> LanguagesResource: ...
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
class ListProductCertificationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProductCertificationsResponse: ...

@typing.type_check_only
class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProductsResponse: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Product: ...

@typing.type_check_only
class ProductCertificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductCertification: ...
