import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AnalyticsDataResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AudienceExportsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: AudienceExport = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AudienceExportHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAudienceExportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAudienceExportsResponseHttpRequest,
                previous_response: ListAudienceExportsResponse,
            ) -> ListAudienceExportsResponseHttpRequest | None: ...
            def query(
                self,
                *,
                name: str,
                body: QueryAudienceExportRequest = ...,
                **kwargs: typing.Any,
            ) -> QueryAudienceExportResponseHttpRequest: ...

        def batchRunPivotReports(
            self,
            *,
            property: str,
            body: BatchRunPivotReportsRequest = ...,
            **kwargs: typing.Any,
        ) -> BatchRunPivotReportsResponseHttpRequest: ...
        def batchRunReports(
            self,
            *,
            property: str,
            body: BatchRunReportsRequest = ...,
            **kwargs: typing.Any,
        ) -> BatchRunReportsResponseHttpRequest: ...
        def checkCompatibility(
            self,
            *,
            property: str,
            body: CheckCompatibilityRequest = ...,
            **kwargs: typing.Any,
        ) -> CheckCompatibilityResponseHttpRequest: ...
        def getMetadata(
            self, *, name: str, **kwargs: typing.Any
        ) -> MetadataHttpRequest: ...
        def runPivotReport(
            self,
            *,
            property: str,
            body: RunPivotReportRequest = ...,
            **kwargs: typing.Any,
        ) -> RunPivotReportResponseHttpRequest: ...
        def runRealtimeReport(
            self,
            *,
            property: str,
            body: RunRealtimeReportRequest = ...,
            **kwargs: typing.Any,
        ) -> RunRealtimeReportResponseHttpRequest: ...
        def runReport(
            self, *, property: str, body: RunReportRequest = ..., **kwargs: typing.Any
        ) -> RunReportResponseHttpRequest: ...
        def audienceExports(self) -> AudienceExportsResource: ...

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
    def properties(self) -> PropertiesResource: ...

@typing.type_check_only
class AudienceExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AudienceExport: ...

@typing.type_check_only
class BatchRunPivotReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchRunPivotReportsResponse: ...

@typing.type_check_only
class BatchRunReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchRunReportsResponse: ...

@typing.type_check_only
class CheckCompatibilityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckCompatibilityResponse: ...

@typing.type_check_only
class ListAudienceExportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAudienceExportsResponse: ...

@typing.type_check_only
class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Metadata: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class QueryAudienceExportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryAudienceExportResponse: ...

@typing.type_check_only
class RunPivotReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RunPivotReportResponse: ...

@typing.type_check_only
class RunRealtimeReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RunRealtimeReportResponse: ...

@typing.type_check_only
class RunReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RunReportResponse: ...
