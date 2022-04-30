import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
                **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def createOffline(
                self, *, parent: str, body: Profile = ..., **kwargs: typing.Any
            ) -> ProfileHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Profile = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Profile: ...
