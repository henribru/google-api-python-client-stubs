import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DataManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AudienceMembersResource(googleapiclient.discovery.Resource):
        def ingest(
            self, *, body: IngestAudienceMembersRequest = ..., **kwargs: typing.Any
        ) -> IngestAudienceMembersResponseHttpRequest: ...
        def remove(
            self, *, body: RemoveAudienceMembersRequest = ..., **kwargs: typing.Any
        ) -> RemoveAudienceMembersResponseHttpRequest: ...

    @typing.type_check_only
    class EventsResource(googleapiclient.discovery.Resource):
        def ingest(
            self, *, body: IngestEventsRequest = ..., **kwargs: typing.Any
        ) -> IngestEventsResponseHttpRequest: ...

    @typing.type_check_only
    class RequestStatusResource(googleapiclient.discovery.Resource):
        def retrieve(
            self, *, requestId: str = ..., **kwargs: typing.Any
        ) -> RetrieveRequestStatusResponseHttpRequest: ...

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
    def audienceMembers(self) -> AudienceMembersResource: ...
    def events(self) -> EventsResource: ...
    def requestStatus(self) -> RequestStatusResource: ...

@typing.type_check_only
class IngestAudienceMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IngestAudienceMembersResponse: ...

@typing.type_check_only
class IngestEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IngestEventsResponse: ...

@typing.type_check_only
class RemoveAudienceMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemoveAudienceMembersResponse: ...

@typing.type_check_only
class RetrieveRequestStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RetrieveRequestStatusResponse: ...
