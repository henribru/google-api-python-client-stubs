import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DiscoveryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ApisResource(googleapiclient.discovery.Resource):
        def getRest(
            self, *, api: str, version: str, **kwargs: typing.Any
        ) -> RestDescriptionHttpRequest: ...
        def list(
            self, *, name: str = ..., preferred: bool = ..., **kwargs: typing.Any
        ) -> DirectoryListHttpRequest: ...

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
    def apis(self) -> ApisResource: ...

@typing.type_check_only
class DirectoryListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectoryList: ...

@typing.type_check_only
class RestDescriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RestDescription: ...
