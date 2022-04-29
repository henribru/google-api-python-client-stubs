import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class VersionHistoryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PlatformsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ChannelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ReleasesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListReleasesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListReleasesResponseHttpRequest,
                        previous_response: ListReleasesResponse,
                    ) -> ListReleasesResponseHttpRequest | None: ...

                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListVersionsResponseHttpRequest,
                    previous_response: ListVersionsResponse,
                ) -> ListVersionsResponseHttpRequest | None: ...
                def releases(self) -> ReleasesResource: ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListChannelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListChannelsResponseHttpRequest,
                previous_response: ListChannelsResponse,
            ) -> ListChannelsResponseHttpRequest | None: ...
            def versions(self) -> VersionsResource: ...

        def list(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListPlatformsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPlatformsResponseHttpRequest,
            previous_response: ListPlatformsResponse,
        ) -> ListPlatformsResponseHttpRequest | None: ...
        def channels(self) -> ChannelsResource: ...

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
    def platforms(self) -> PlatformsResource: ...

@typing.type_check_only
class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListChannelsResponse: ...

@typing.type_check_only
class ListPlatformsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPlatformsResponse: ...

@typing.type_check_only
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVersionsResponse: ...
