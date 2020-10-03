import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PolyServiceResource(googleapiclient.discovery.Resource):
    class UsersResource(googleapiclient.discovery.Resource):
        class LikedassetsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                format: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                **kwargs: typing.Any
            ) -> ListLikedAssetsResponseHttpRequest: ...
        class AssetsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                visibility: typing_extensions.Literal[
                    "VISIBILITY_UNSPECIFIED", "PUBLISHED", "PRIVATE"
                ] = ...,
                format: str = ...,
                **kwargs: typing.Any
            ) -> ListUserAssetsResponseHttpRequest: ...
        def likedassets(self) -> LikedassetsResource: ...
        def assets(self) -> AssetsResource: ...
    class AssetsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            keywords: str = ...,
            orderBy: str = ...,
            category: str = ...,
            maxComplexity: typing_extensions.Literal[
                "COMPLEXITY_UNSPECIFIED", "COMPLEX", "MEDIUM", "SIMPLE"
            ] = ...,
            pageSize: int = ...,
            curated: bool = ...,
            pageToken: str = ...,
            format: str = ...,
            **kwargs: typing.Any
        ) -> ListAssetsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> AssetHttpRequest: ...
    def users(self) -> UsersResource: ...
    def assets(self) -> AssetsResource: ...

class ListLikedAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLikedAssetsResponse: ...

class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssetsResponse: ...

class ListUserAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUserAssetsResponse: ...

class AssetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Asset: ...
