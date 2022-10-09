import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DoubleClickBidManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class QueriesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, queryId: str, reportId: str, **kwargs: typing.Any
            ) -> ReportHttpRequest: ...
            def list(
                self,
                *,
                queryId: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListReportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListReportsResponseHttpRequest,
                previous_response: ListReportsResponse,
            ) -> ListReportsResponseHttpRequest | None: ...

        def create(
            self, *, body: Query = ..., **kwargs: typing.Any
        ) -> QueryHttpRequest: ...
        def delete(
            self, *, queryId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(self, *, queryId: str, **kwargs: typing.Any) -> QueryHttpRequest: ...
        def list(
            self,
            *,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListQueriesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListQueriesResponseHttpRequest,
            previous_response: ListQueriesResponse,
        ) -> ListQueriesResponseHttpRequest | None: ...
        def run(
            self,
            *,
            queryId: str,
            body: RunQueryRequest = ...,
            synchronous: bool = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def reports(self) -> ReportsResource: ...

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
    def queries(self) -> QueriesResource: ...

@typing.type_check_only
class ListQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListQueriesResponse: ...

@typing.type_check_only
class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReportsResponse: ...

@typing.type_check_only
class QueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Query: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Report: ...
