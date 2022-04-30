import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ServiceControlResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        def check(
            self, *, serviceName: str, body: CheckRequest = ..., **kwargs: typing.Any
        ) -> CheckResponseHttpRequest: ...
        def report(
            self, *, serviceName: str, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportResponseHttpRequest: ...

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
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class CheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CheckResponse: ...

@typing.type_check_only
class ReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReportResponse: ...
