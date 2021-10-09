import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ChromeUXReportResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class RecordsResource(googleapiclient.discovery.Resource):
        def queryRecord(
            self, *, body: QueryRequest = ..., **kwargs: typing.Any
        ) -> QueryResponseHttpRequest: ...
    def records(self) -> RecordsResource: ...

@typing.type_check_only
class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryResponse: ...
