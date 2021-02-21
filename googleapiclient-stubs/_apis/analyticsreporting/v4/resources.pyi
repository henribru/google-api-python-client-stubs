import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AnalyticsReportingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self, *, body: GetReportsRequest = ..., **kwargs: typing.Any
        ) -> GetReportsResponseHttpRequest: ...
    @typing.type_check_only
    class UserActivityResource(googleapiclient.discovery.Resource):
        def search(
            self, *, body: SearchUserActivityRequest = ..., **kwargs: typing.Any
        ) -> SearchUserActivityResponseHttpRequest: ...
    def reports(self) -> ReportsResource: ...
    def userActivity(self) -> UserActivityResource: ...

@typing.type_check_only
class GetReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetReportsResponse: ...

@typing.type_check_only
class SearchUserActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchUserActivityResponse: ...
