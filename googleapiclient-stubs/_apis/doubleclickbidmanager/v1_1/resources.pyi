import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class DoubleClickBidManagerResource(googleapiclient.discovery.Resource):
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
    def queries(self) -> QueriesResource: ...
    def reports(self) -> ReportsResource: ...

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
