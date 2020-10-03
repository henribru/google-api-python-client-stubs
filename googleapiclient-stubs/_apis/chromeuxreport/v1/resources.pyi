import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ChromeUXReportResource(googleapiclient.discovery.Resource):
    class RecordsResource(googleapiclient.discovery.Resource):
        def queryRecord(
            self, *, body: QueryRequest = ..., **kwargs: typing.Any
        ) -> QueryResponseHttpRequest: ...
    def records(self) -> RecordsResource: ...

class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryResponse: ...
