import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class YouTubeAnalyticsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class GroupItemsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyResponseHttpRequest: ...
        def insert(
            self,
            *,
            body: GroupItem,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> GroupItemHttpRequest: ...
        def list(
            self,
            *,
            groupId: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListGroupItemsResponseHttpRequest: ...

    @typing.type_check_only
    class GroupsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyResponseHttpRequest: ...
        def insert(
            self,
            *,
            body: Group,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> GroupHttpRequest: ...
        def list(
            self,
            *,
            id: str | None = ...,
            mine: bool | None = ...,
            onBehalfOfContentOwner: str | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> ListGroupsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListGroupsResponseHttpRequest,
            previous_response: ListGroupsResponse,
        ) -> ListGroupsResponseHttpRequest | None: ...
        def update(
            self,
            *,
            body: Group,
            onBehalfOfContentOwner: str | None = ...,
            **kwargs: typing.Any,
        ) -> GroupHttpRequest: ...

    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def query(
            self,
            *,
            currency: str | None = ...,
            dimensions: str | None = ...,
            endDate: str | None = ...,
            filters: str | None = ...,
            ids: str | None = ...,
            includeHistoricalChannelData: bool | None = ...,
            maxResults: int | None = ...,
            metrics: str | None = ...,
            sort: str | None = ...,
            startDate: str | None = ...,
            startIndex: int | None = ...,
            **kwargs: typing.Any,
        ) -> QueryResponseHttpRequest: ...

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
    def groupItems(self) -> GroupItemsResource: ...
    def groups(self) -> GroupsResource: ...
    def reports(self) -> ReportsResource: ...

@typing.type_check_only
class EmptyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EmptyResponse: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Group: ...

@typing.type_check_only
class GroupItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GroupItem: ...

@typing.type_check_only
class ListGroupItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGroupItemsResponse: ...

@typing.type_check_only
class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGroupsResponse: ...

@typing.type_check_only
class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryResponse: ...
