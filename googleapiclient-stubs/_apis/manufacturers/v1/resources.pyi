import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ManufacturerCenterResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        class ProductsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                include: typing.Union[
                    typing_extensions.Literal[
                        "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                        ]
                    ],
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProductsResponseHttpRequest: ...
            def update(
                self,
                *,
                parent: str,
                name: str,
                body: Attributes = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def delete(
                self, *, parent: str, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                parent: str,
                name: str,
                include: typing.Union[
                    typing_extensions.Literal[
                        "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "UNKNOWN", "ATTRIBUTES", "ISSUES", "DESTINATION_STATUSES"
                        ]
                    ],
                ] = ...,
                **kwargs: typing.Any
            ) -> ProductHttpRequest: ...
        def products(self) -> ProductsResource: ...
    def accounts(self) -> AccountsResource: ...

class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProductsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...
