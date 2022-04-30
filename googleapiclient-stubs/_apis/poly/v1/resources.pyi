import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PolyServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AssetsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> AssetHttpRequest: ...
        def list(
            self,
            *,
            category: str = ...,
            curated: bool = ...,
            format: str = ...,
            keywords: str = ...,
            maxComplexity: typing_extensions.Literal[
                "COMPLEXITY_UNSPECIFIED", "COMPLEX", "MEDIUM", "SIMPLE"
            ] = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListAssetsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAssetsResponseHttpRequest,
            previous_response: ListAssetsResponse,
        ) -> ListAssetsResponseHttpRequest | None: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                format: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                visibility: typing_extensions.Literal[
                    "VISIBILITY_UNSPECIFIED", "PUBLISHED", "PRIVATE"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListUserAssetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListUserAssetsResponseHttpRequest,
                previous_response: ListUserAssetsResponse,
            ) -> ListUserAssetsResponseHttpRequest | None: ...

        @typing.type_check_only
        class LikedassetsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                format: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLikedAssetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLikedAssetsResponseHttpRequest,
                previous_response: ListLikedAssetsResponse,
            ) -> ListLikedAssetsResponseHttpRequest | None: ...

        def assets(self) -> AssetsResource: ...
        def likedassets(self) -> LikedassetsResource: ...

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
    def assets(self) -> AssetsResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class AssetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Asset: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAssetsResponse: ...

@typing.type_check_only
class ListLikedAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLikedAssetsResponse: ...

@typing.type_check_only
class ListUserAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUserAssetsResponse: ...
