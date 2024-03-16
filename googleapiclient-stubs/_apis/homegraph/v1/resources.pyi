import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class HomeGraphServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AgentUsersResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, agentUserId: str, requestId: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...

    @typing.type_check_only
    class DevicesResource(googleapiclient.discovery.Resource):
        def query(
            self, *, body: QueryRequest = ..., **kwargs: typing.Any
        ) -> QueryResponseHttpRequest: ...
        def reportStateAndNotification(
            self, *, body: ReportStateAndNotificationRequest = ..., **kwargs: typing.Any
        ) -> ReportStateAndNotificationResponseHttpRequest: ...
        def requestSync(
            self, *, body: RequestSyncDevicesRequest = ..., **kwargs: typing.Any
        ) -> RequestSyncDevicesResponseHttpRequest: ...
        def sync(
            self, *, body: SyncRequest = ..., **kwargs: typing.Any
        ) -> SyncResponseHttpRequest: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def agentUsers(self) -> AgentUsersResource: ...
    def devices(self) -> DevicesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryResponse: ...

@typing.type_check_only
class ReportStateAndNotificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReportStateAndNotificationResponse: ...

@typing.type_check_only
class RequestSyncDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RequestSyncDevicesResponse: ...

@typing.type_check_only
class SyncResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SyncResponse: ...
