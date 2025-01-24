import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ChecksServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...
                def wait(
                    self,
                    *,
                    name: str,
                    body: WaitOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ReportsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, checksFilter: str = ..., **kwargs: typing.Any
                ) -> GoogleChecksReportV1alphaReportHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    checksFilter: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChecksReportV1alphaListReportsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChecksReportV1alphaListReportsResponseHttpRequest,
                    previous_response: GoogleChecksReportV1alphaListReportsResponse,
                ) -> GoogleChecksReportV1alphaListReportsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChecksAccountV1alphaAppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleChecksAccountV1alphaListAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleChecksAccountV1alphaListAppsResponseHttpRequest,
                previous_response: GoogleChecksAccountV1alphaListAppsResponse,
            ) -> GoogleChecksAccountV1alphaListAppsResponseHttpRequest | None: ...
            def operations(self) -> OperationsResource: ...
            def reports(self) -> ReportsResource: ...

        @typing.type_check_only
        class ReposResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ScansResource(googleapiclient.discovery.Resource):
                def generate(
                    self,
                    *,
                    parent: str,
                    body: GoogleChecksRepoScanV1alphaGenerateScanRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleChecksRepoScanV1alphaRepoScanHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleChecksRepoScanV1alphaListRepoScansResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleChecksRepoScanV1alphaListRepoScansResponseHttpRequest,
                    previous_response: GoogleChecksRepoScanV1alphaListRepoScansResponse,
                ) -> (
                    GoogleChecksRepoScanV1alphaListRepoScansResponseHttpRequest | None
                ): ...

            def operations(self) -> OperationsResource: ...
            def scans(self) -> ScansResource: ...

        def apps(self) -> AppsResource: ...
        def repos(self) -> ReposResource: ...

    @typing.type_check_only
    class AisafetyResource(googleapiclient.discovery.Resource):
        def classifyContent(
            self,
            *,
            body: GoogleChecksAisafetyV1alphaClassifyContentRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleChecksAisafetyV1alphaClassifyContentResponseHttpRequest: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            parent: str,
            body: GoogleChecksReportV1alphaAnalyzeUploadRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...

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
    def accounts(self) -> AccountsResource: ...
    def aisafety(self) -> AisafetyResource: ...
    def media(self) -> MediaResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleChecksAccountV1alphaAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksAccountV1alphaApp: ...

@typing.type_check_only
class GoogleChecksAccountV1alphaListAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksAccountV1alphaListAppsResponse: ...

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksAisafetyV1alphaClassifyContentResponse: ...

@typing.type_check_only
class GoogleChecksRepoScanV1alphaListRepoScansResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksRepoScanV1alphaListRepoScansResponse: ...

@typing.type_check_only
class GoogleChecksRepoScanV1alphaRepoScanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksRepoScanV1alphaRepoScan: ...

@typing.type_check_only
class GoogleChecksReportV1alphaListReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksReportV1alphaListReportsResponse: ...

@typing.type_check_only
class GoogleChecksReportV1alphaReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleChecksReportV1alphaReport: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...
