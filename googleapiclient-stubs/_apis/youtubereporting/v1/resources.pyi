import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class YouTubeReportingResource(googleapiclient.discovery.Resource):
    class ReportTypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            includeSystemManaged: bool = ...,
            pageToken: str = ...,
            onBehalfOfContentOwner: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListReportTypesResponseHttpRequest: ...
    class JobsResource(googleapiclient.discovery.Resource):
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
                pageToken: str = ...,
                startTimeAtOrAfter: str = ...,
                startTimeBefore: str = ...,
                pageSize: int = ...,
                onBehalfOfContentOwner: str = ...,
                **kwargs: typing.Any
            ) -> ListReportsResponseHttpRequest: ...
        def get(
            self, *, jobId: str, onBehalfOfContentOwner: str = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            includeSystemManaged: bool = ...,
            pageToken: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ListJobsResponseHttpRequest: ...
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
        def reports(self) -> ReportsResource: ...
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GdataMediaHttpRequest: ...
    def reportTypes(self) -> ReportTypesResource: ...
    def jobs(self) -> JobsResource: ...
    def media(self) -> MediaResource: ...

class ListReportTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReportTypesResponse: ...

class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListJobsResponse: ...

class GdataMediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GdataMedia: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Job: ...

class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReportsResponse: ...

class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Report: ...
