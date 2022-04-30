import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SearchConsoleResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class SearchanalyticsResource(googleapiclient.discovery.Resource):
        def query(
            self,
            *,
            siteUrl: str,
            body: SearchAnalyticsQueryRequest = ...,
            **kwargs: typing.Any
        ) -> SearchAnalyticsQueryResponseHttpRequest: ...

    @typing.type_check_only
    class SitemapsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, siteUrl: str, feedpath: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, siteUrl: str, feedpath: str, **kwargs: typing.Any
        ) -> WmxSitemapHttpRequest: ...
        def list(
            self, *, siteUrl: str, sitemapIndex: str = ..., **kwargs: typing.Any
        ) -> SitemapsListResponseHttpRequest: ...
        def submit(
            self, *, siteUrl: str, feedpath: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class SitesResource(googleapiclient.discovery.Resource):
        def add(
            self, *, siteUrl: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def delete(
            self, *, siteUrl: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(self, *, siteUrl: str, **kwargs: typing.Any) -> WmxSiteHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> SitesListResponseHttpRequest: ...

    @typing.type_check_only
    class UrlInspectionResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class IndexResource(googleapiclient.discovery.Resource):
            def inspect(
                self, *, body: InspectUrlIndexRequest = ..., **kwargs: typing.Any
            ) -> InspectUrlIndexResponseHttpRequest: ...

        def index(self) -> IndexResource: ...

    @typing.type_check_only
    class UrlTestingToolsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MobileFriendlyTestResource(googleapiclient.discovery.Resource):
            def run(
                self, *, body: RunMobileFriendlyTestRequest = ..., **kwargs: typing.Any
            ) -> RunMobileFriendlyTestResponseHttpRequest: ...

        def mobileFriendlyTest(self) -> MobileFriendlyTestResource: ...

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
    def searchanalytics(self) -> SearchanalyticsResource: ...
    def sitemaps(self) -> SitemapsResource: ...
    def sites(self) -> SitesResource: ...
    def urlInspection(self) -> UrlInspectionResource: ...
    def urlTestingTools(self) -> UrlTestingToolsResource: ...

@typing.type_check_only
class InspectUrlIndexResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InspectUrlIndexResponse: ...

@typing.type_check_only
class RunMobileFriendlyTestResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RunMobileFriendlyTestResponse: ...

@typing.type_check_only
class SearchAnalyticsQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchAnalyticsQueryResponse: ...

@typing.type_check_only
class SitemapsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SitemapsListResponse: ...

@typing.type_check_only
class SitesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SitesListResponse: ...

@typing.type_check_only
class WmxSiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WmxSite: ...

@typing.type_check_only
class WmxSitemapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WmxSitemap: ...
