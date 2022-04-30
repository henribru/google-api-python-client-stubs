import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class TrafficDirectorServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DiscoveryResource(googleapiclient.discovery.Resource):
        def client_status(
            self, *, body: ClientStatusRequest = ..., **kwargs: typing.Any
        ) -> ClientStatusResponseHttpRequest: ...

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
    def discovery(self) -> DiscoveryResource: ...

@typing.type_check_only
class ClientStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClientStatusResponse: ...
