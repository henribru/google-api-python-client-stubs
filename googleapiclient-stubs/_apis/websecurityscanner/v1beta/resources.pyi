import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class WebSecurityScannerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ScanConfigsResource(googleapiclient.discovery.Resource):
            class ScanRunsResource(googleapiclient.discovery.Resource):
                class FindingTypeStatsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> ListFindingTypeStatsResponseHttpRequest: ...
                class FindingsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> FindingHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        filter: str = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListFindingsResponseHttpRequest: ...
                class CrawledUrlsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCrawledUrlsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ScanRunHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopScanRunRequest = ...,
                    **kwargs: typing.Any
                ) -> ScanRunHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListScanRunsResponseHttpRequest: ...
                def findingTypeStats(self) -> FindingTypeStatsResource: ...
                def findings(self) -> FindingsResource: ...
                def crawledUrls(self) -> CrawledUrlsResource: ...
            def start(
                self,
                *,
                name: str,
                body: StartScanRunRequest = ...,
                **kwargs: typing.Any
            ) -> ScanRunHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: ScanConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListScanConfigsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def create(
                self, *, parent: str, body: ScanConfig = ..., **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def scanRuns(self) -> ScanRunsResource: ...
        def scanConfigs(self) -> ScanConfigsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFindingsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListScanRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListScanRunsResponse: ...

class ListCrawledUrlsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCrawledUrlsResponse: ...

class ListScanConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListScanConfigsResponse: ...

class ScanConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ScanConfig: ...

class FindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Finding: ...

class ListFindingTypeStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFindingTypeStatsResponse: ...

class ScanRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ScanRun: ...
