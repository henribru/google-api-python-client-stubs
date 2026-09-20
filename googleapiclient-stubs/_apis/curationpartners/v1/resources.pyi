import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CurationPartnersResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CuratorsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CuratedPackagesResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: ActivateCuratedPackageRequest,
                **kwargs: typing.Any,
            ) -> CuratedPackageHttpRequest: ...
            def create(
                self, *, parent: str, body: CuratedPackage, **kwargs: typing.Any
            ) -> CuratedPackageHttpRequest: ...
            def deactivate(
                self,
                *,
                name: str,
                body: DeactivateCuratedPackageRequest,
                **kwargs: typing.Any,
            ) -> CuratedPackageHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CuratedPackageHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListCuratedPackagesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCuratedPackagesResponseHttpRequest,
                previous_response: ListCuratedPackagesResponse,
            ) -> ListCuratedPackagesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: CuratedPackage,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> CuratedPackageHttpRequest: ...

        @typing.type_check_only
        class DataSegmentsResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: ActivateDataSegmentRequest,
                **kwargs: typing.Any,
            ) -> DataSegmentHttpRequest: ...
            def create(
                self, *, parent: str, body: DataSegment, **kwargs: typing.Any
            ) -> DataSegmentHttpRequest: ...
            def deactivate(
                self,
                *,
                name: str,
                body: DeactivateDataSegmentRequest,
                **kwargs: typing.Any,
            ) -> DataSegmentHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DataSegmentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListDataSegmentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDataSegmentsResponseHttpRequest,
                previous_response: ListDataSegmentsResponse,
            ) -> ListDataSegmentsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: DataSegment,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> DataSegmentHttpRequest: ...

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

        def curatedPackages(self) -> CuratedPackagesResource: ...
        def dataSegments(self) -> DataSegmentsResource: ...
        def reports(self) -> ReportsResource: ...

    @typing.type_check_only
    class MediaPlannersResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            filter: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListMediaPlannersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListMediaPlannersResponseHttpRequest,
            previous_response: ListMediaPlannersResponse,
        ) -> ListMediaPlannersResponseHttpRequest | None: ...

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
    def curators(self) -> CuratorsResource: ...
    def mediaPlanners(self) -> MediaPlannersResource: ...

@typing.type_check_only
class CuratedPackageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CuratedPackage: ...

@typing.type_check_only
class DataSegmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DataSegment: ...

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
class ListCuratedPackagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCuratedPackagesResponse: ...

@typing.type_check_only
class ListDataSegmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDataSegmentsResponse: ...

@typing.type_check_only
class ListMediaPlannersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMediaPlannersResponse: ...

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
