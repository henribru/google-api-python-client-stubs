import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class RealTimeBiddingResource(googleapiclient.discovery.Resource):
    class BuyersResource(googleapiclient.discovery.Resource):
        class CreativesResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: Creative = ..., **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Creative = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
        class UserListsResource(googleapiclient.discovery.Resource):
            def close(self, *, name: str, body: CloseUserListRequest = ..., **kwargs: typing.Any) -> UserListHttpRequest: ...  # type: ignore
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def create(
                self, *, parent: str, body: UserList = ..., **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def update(
                self, *, name: str, body: UserList = ..., **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def getRemarketingTag(
                self, *, name: str, **kwargs: typing.Any
            ) -> GetRemarketingTagResponseHttpRequest: ...
            def open(
                self,
                *,
                name: str,
                body: OpenUserListRequest = ...,
                **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListUserListsResponseHttpRequest: ...
        def getRemarketingTag(
            self, *, name: str, **kwargs: typing.Any
        ) -> GetRemarketingTagResponseHttpRequest: ...
        def creatives(self) -> CreativesResource: ...
        def userLists(self) -> UserListsResource: ...
    class BiddersResource(googleapiclient.discovery.Resource):
        class CreativesResource(googleapiclient.discovery.Resource):
            def watch(
                self,
                *,
                parent: str,
                body: WatchCreativesRequest = ...,
                **kwargs: typing.Any
            ) -> WatchCreativesResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
        def creatives(self) -> CreativesResource: ...
    def buyers(self) -> BuyersResource: ...
    def bidders(self) -> BiddersResource: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class UserListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserList: ...

class ListUserListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUserListsResponse: ...

class GetRemarketingTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetRemarketingTagResponse: ...

class WatchCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WatchCreativesResponse: ...

class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativesResponse: ...
