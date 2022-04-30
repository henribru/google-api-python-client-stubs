import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AnalyticsReportingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self, *, body: GetReportsRequest = ..., **kwargs: typing.Any
        ) -> GetReportsResponseHttpRequest: ...

    @typing.type_check_only
    class UserActivityResource(googleapiclient.discovery.Resource):
        def search(
            self, *, body: SearchUserActivityRequest = ..., **kwargs: typing.Any
        ) -> SearchUserActivityResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchUserActivityResponseHttpRequest,
            previous_response: SearchUserActivityResponse,
        ) -> SearchUserActivityResponseHttpRequest | None: ...

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
    def reports(self) -> ReportsResource: ...
    def userActivity(self) -> UserActivityResource: ...

@typing.type_check_only
class GetReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetReportsResponse: ...

@typing.type_check_only
class SearchUserActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchUserActivityResponse: ...
