import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AnalyticsDataResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        def getMetadata(
            self, *, name: str, **kwargs: typing.Any
        ) -> MetadataHttpRequest: ...
        def runRealtimeReport(
            self,
            *,
            property: str,
            body: RunRealtimeReportRequest = ...,
            **kwargs: typing.Any
        ) -> RunRealtimeReportResponseHttpRequest: ...

    @typing.type_check_only
    class V1alphaResource(googleapiclient.discovery.Resource):
        def batchRunPivotReports(
            self, *, body: BatchRunPivotReportsRequest = ..., **kwargs: typing.Any
        ) -> BatchRunPivotReportsResponseHttpRequest: ...
        def batchRunReports(
            self, *, body: BatchRunReportsRequest = ..., **kwargs: typing.Any
        ) -> BatchRunReportsResponseHttpRequest: ...
        def runPivotReport(
            self, *, body: RunPivotReportRequest = ..., **kwargs: typing.Any
        ) -> RunPivotReportResponseHttpRequest: ...
        def runReport(
            self, *, body: RunReportRequest = ..., **kwargs: typing.Any
        ) -> RunReportResponseHttpRequest: ...

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
    def properties(self) -> PropertiesResource: ...
    def v1alpha(self) -> V1alphaResource: ...

@typing.type_check_only
class BatchRunPivotReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchRunPivotReportsResponse: ...

@typing.type_check_only
class BatchRunReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchRunReportsResponse: ...

@typing.type_check_only
class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Metadata: ...

@typing.type_check_only
class RunPivotReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RunPivotReportResponse: ...

@typing.type_check_only
class RunRealtimeReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RunRealtimeReportResponse: ...

@typing.type_check_only
class RunReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RunReportResponse: ...
