import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class DoubleClickBidManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LineitemsResource(googleapiclient.discovery.Resource):
        def downloadlineitems(
            self, *, body: DownloadLineItemsRequest = ..., **kwargs: typing.Any
        ) -> DownloadLineItemsResponseHttpRequest: ...
        def uploadlineitems(
            self, *, body: UploadLineItemsRequest = ..., **kwargs: typing.Any
        ) -> UploadLineItemsResponseHttpRequest: ...
    @typing.type_check_only
    class QueriesResource(googleapiclient.discovery.Resource):
        def createquery(
            self, *, body: Query = ..., asynchronous: bool = ..., **kwargs: typing.Any
        ) -> QueryHttpRequest: ...
        def deletequery(
            self, *, queryId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def getquery(
            self, *, queryId: str, **kwargs: typing.Any
        ) -> QueryHttpRequest: ...
        def listqueries(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListQueriesResponseHttpRequest: ...
        def runquery(
            self,
            *,
            queryId: str,
            body: RunQueryRequest = ...,
            asynchronous: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def listreports(
            self,
            *,
            queryId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListReportsResponseHttpRequest: ...
    @typing.type_check_only
    class SdfResource(googleapiclient.discovery.Resource):
        def download(
            self, *, body: DownloadRequest = ..., **kwargs: typing.Any
        ) -> DownloadResponseHttpRequest: ...
    def lineitems(self) -> LineitemsResource: ...
    def queries(self) -> QueriesResource: ...
    def reports(self) -> ReportsResource: ...
    def sdf(self) -> SdfResource: ...

@typing.type_check_only
class DownloadLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DownloadLineItemsResponse: ...

@typing.type_check_only
class DownloadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DownloadResponse: ...

@typing.type_check_only
class ListQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListQueriesResponse: ...

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
class QueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Query: ...

@typing.type_check_only
class UploadLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UploadLineItemsResponse: ...
