import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AnalyticsReportingResource(googleapiclient.discovery.Resource):
    class ReportsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self, *, body: GetReportsRequest = ..., **kwargs: typing.Any
        ) -> GetReportsResponseHttpRequest: ...
    class UserActivityResource(googleapiclient.discovery.Resource):
        def search(
            self, *, body: SearchUserActivityRequest = ..., **kwargs: typing.Any
        ) -> SearchUserActivityResponseHttpRequest: ...
    def reports(self) -> ReportsResource: ...
    def userActivity(self) -> UserActivityResource: ...

class GetReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetReportsResponse: ...

class SearchUserActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchUserActivityResponse: ...
