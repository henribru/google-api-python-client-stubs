import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class YouTubeReportingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class JobsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                jobId: str,
                reportId: str,
                onBehalfOfContentOwner: str = ...,
                **kwargs: typing.Any
            ) -> ReportHttpRequest: ...
            def list(
                self,
                *,
                jobId: str,
                createdAfter: str = ...,
                onBehalfOfContentOwner: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                startTimeAtOrAfter: str = ...,
                startTimeBefore: str = ...,
                **kwargs: typing.Any
            ) -> ListReportsResponseHttpRequest: ...
        def create(
            self,
            *,
            body: Job = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def delete(
            self, *, jobId: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, jobId: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def list(
            self,
            *,
            includeSystemManaged: bool = ...,
            onBehalfOfContentOwner: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListJobsResponseHttpRequest: ...
        def reports(self) -> ReportsResource: ...
    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GdataMediaHttpRequest: ...
    @typing.type_check_only
    class ReportTypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            includeSystemManaged: bool = ...,
            onBehalfOfContentOwner: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListReportTypesResponseHttpRequest: ...
    def jobs(self) -> JobsResource: ...
    def media(self) -> MediaResource: ...
    def reportTypes(self) -> ReportTypesResource: ...

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
class GdataMediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GdataMedia: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Job: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListJobsResponse: ...

@typing.type_check_only
class ListReportTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListReportTypesResponse: ...

@typing.type_check_only
class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListReportsResponse: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Report: ...
