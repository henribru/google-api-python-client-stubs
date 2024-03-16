import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudProfilerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProfilesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateProfileRequest = ...,
                **kwargs: typing.Any,
            ) -> ProfileHttpRequest: ...
            def createOffline(
                self, *, parent: str, body: Profile = ..., **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListProfilesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProfilesResponseHttpRequest,
                previous_response: ListProfilesResponse,
            ) -> ListProfilesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Profile = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> ProfileHttpRequest: ...

        def profiles(self) -> ProfilesResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ListProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProfilesResponse: ...

@typing.type_check_only
class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Profile: ...
