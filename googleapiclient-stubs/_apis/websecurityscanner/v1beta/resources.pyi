import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class WebSecurityScannerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ScanConfigsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ScanRunsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CrawledUrlsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCrawledUrlsResponseHttpRequest: ...
                @typing.type_check_only
                class FindingTypeStatsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> ListFindingTypeStatsResponseHttpRequest: ...
                @typing.type_check_only
                class FindingsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> FindingHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListFindingsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ScanRunHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListScanRunsResponseHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopScanRunRequest = ...,
                    **kwargs: typing.Any
                ) -> ScanRunHttpRequest: ...
                def crawledUrls(self) -> CrawledUrlsResource: ...
                def findingTypeStats(self) -> FindingTypeStatsResource: ...
                def findings(self) -> FindingsResource: ...
            def create(
                self, *, parent: str, body: ScanConfig = ..., **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListScanConfigsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: ScanConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def start(
                self,
                *,
                name: str,
                body: StartScanRunRequest = ...,
                **kwargs: typing.Any
            ) -> ScanRunHttpRequest: ...
            def scanRuns(self) -> ScanRunsResource: ...
        def scanConfigs(self) -> ScanConfigsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Finding: ...

@typing.type_check_only
class ListCrawledUrlsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCrawledUrlsResponse: ...

@typing.type_check_only
class ListFindingTypeStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListFindingTypeStatsResponse: ...

@typing.type_check_only
class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListFindingsResponse: ...

@typing.type_check_only
class ListScanConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListScanConfigsResponse: ...

@typing.type_check_only
class ListScanRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListScanRunsResponse: ...

@typing.type_check_only
class ScanConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ScanConfig: ...

@typing.type_check_only
class ScanRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ScanRun: ...
