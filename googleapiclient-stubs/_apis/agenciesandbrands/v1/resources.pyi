import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AgenciesAndBrandsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AgenciesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ResultsResource(googleapiclient.discovery.Resource):
                def fetchRows(
                    self,
                    *,
                    name: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> FetchReportResultRowsResponseHttpRequest: ...
                def fetchRows_next(
                    self,
                    previous_request: FetchReportResultRowsResponseHttpRequest,
                    previous_response: FetchReportResultRowsResponse,
                ) -> FetchReportResultRowsResponseHttpRequest | None: ...

            def create(
                self, *, parent: str, body: Report, **kwargs: typing.Any
            ) -> ReportHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ReportHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                orderBy: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                skip: int | None = ...,
                **kwargs: typing.Any,
            ) -> ListReportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListReportsResponseHttpRequest,
                previous_response: ListReportsResponse,
            ) -> ListReportsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Report,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> ReportHttpRequest: ...
            def run(
                self, *, name: str, body: RunReportRequest, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def results(self) -> ResultsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def agencies(self) -> AgenciesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FetchReportResultRowsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchReportResultRowsResponse: ...

@typing.type_check_only
class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReportsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Report: ...
