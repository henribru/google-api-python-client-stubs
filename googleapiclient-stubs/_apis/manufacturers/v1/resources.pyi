import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class ManufacturerCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
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
        def products(self) -> ProductsResource: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListProductsResponse: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Product: ...
