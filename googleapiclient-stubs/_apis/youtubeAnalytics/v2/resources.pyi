import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class YouTubeAnalyticsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class GroupItemsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> EmptyResponseHttpRequest: ...
        def insert(
            self,
            *,
            body: GroupItem = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> GroupItemHttpRequest: ...
        def list(
            self,
            *,
            groupId: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> ListGroupItemsResponseHttpRequest: ...

    @typing.type_check_only
    class GroupsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            id: str = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> EmptyResponseHttpRequest: ...
        def insert(
            self,
            *,
            body: Group = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
        def list(
            self,
            *,
            id: str = ...,
            mine: bool = ...,
            onBehalfOfContentOwner: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListGroupsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListGroupsResponseHttpRequest,
            previous_response: ListGroupsResponse,
        ) -> ListGroupsResponseHttpRequest | None: ...
        def update(
            self,
            *,
            body: Group = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> GroupHttpRequest: ...

    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def query(
            self,
            *,
            currency: str = ...,
            dimensions: str = ...,
            endDate: str = ...,
            filters: str = ...,
            ids: str = ...,
            includeHistoricalChannelData: bool = ...,
            maxResults: int = ...,
            metrics: str = ...,
            sort: str = ...,
            startDate: str = ...,
            startIndex: int = ...,
            **kwargs: typing.Any
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def groupItems(self) -> GroupItemsResource: ...
    def groups(self) -> GroupsResource: ...
    def reports(self) -> ReportsResource: ...

@typing.type_check_only
class EmptyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EmptyResponse: ...

@typing.type_check_only
class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Group: ...

@typing.type_check_only
class GroupItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GroupItem: ...

@typing.type_check_only
class ListGroupItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGroupItemsResponse: ...

@typing.type_check_only
class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListGroupsResponse: ...

@typing.type_check_only
class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> QueryResponse: ...
