import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DoubleClickBidManagerResource(googleapiclient.discovery.Resource):
    class QueriesResource(googleapiclient.discovery.Resource):
        def deletequery(
            self, *, queryId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def createquery(
            self, *, body: Query = ..., asynchronous: bool = ..., **kwargs: typing.Any
        ) -> QueryHttpRequest: ...
        def listqueries(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> ListQueriesResponseHttpRequest: ...
        def getquery(
            self, *, queryId: str, **kwargs: typing.Any
        ) -> QueryHttpRequest: ...
        def runquery(
            self,
            *,
            queryId: str,
            body: RunQueryRequest = ...,
            asynchronous: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class ReportsResource(googleapiclient.discovery.Resource):
        def listreports(
            self,
            *,
            queryId: str,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListReportsResponseHttpRequest: ...
    class SdfResource(googleapiclient.discovery.Resource):
        def download(
            self, *, body: DownloadRequest = ..., **kwargs: typing.Any
        ) -> DownloadResponseHttpRequest: ...
    class LineitemsResource(googleapiclient.discovery.Resource):
        def downloadlineitems(
            self, *, body: DownloadLineItemsRequest = ..., **kwargs: typing.Any
        ) -> DownloadLineItemsResponseHttpRequest: ...
        def uploadlineitems(
            self, *, body: UploadLineItemsRequest = ..., **kwargs: typing.Any
        ) -> UploadLineItemsResponseHttpRequest: ...
    def queries(self) -> QueriesResource: ...
    def reports(self) -> ReportsResource: ...
    def sdf(self) -> SdfResource: ...
    def lineitems(self) -> LineitemsResource: ...

class DownloadLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DownloadLineItemsResponse: ...

class DownloadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DownloadResponse: ...

class ListQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListQueriesResponse: ...

class QueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Query: ...

class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReportsResponse: ...

class UploadLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UploadLineItemsResponse: ...
