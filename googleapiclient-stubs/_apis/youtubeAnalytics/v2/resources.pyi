import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class YouTubeAnalyticsResource(googleapiclient.discovery.Resource):
    class GroupsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            onBehalfOfContentOwner: str = ...,
            id: str = ...,
            **kwargs: typing.Any
        ) -> EmptyResponseHttpRequest: ...
        def update(
            self,
            *,
            body: Group = ...,
            onBehalfOfContentOwner: str = ...,
            **kwargs: typing.Any
        ) -> GroupHttpRequest: ...
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
            onBehalfOfContentOwner: str = ...,
            id: str = ...,
            mine: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListGroupsResponseHttpRequest: ...
    class ReportsResource(googleapiclient.discovery.Resource):
        def query(
            self,
            *,
            currency: str = ...,
            sort: str = ...,
            includeHistoricalChannelData: bool = ...,
            maxResults: int = ...,
            startDate: str = ...,
            filters: str = ...,
            startIndex: int = ...,
            ids: str = ...,
            metrics: str = ...,
            endDate: str = ...,
            dimensions: str = ...,
            **kwargs: typing.Any
        ) -> QueryResponseHttpRequest: ...
    class GroupItemsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            onBehalfOfContentOwner: str = ...,
            groupId: str = ...,
            **kwargs: typing.Any
        ) -> ListGroupItemsResponseHttpRequest: ...
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
    def groups(self) -> GroupsResource: ...
    def reports(self) -> ReportsResource: ...
    def groupItems(self) -> GroupItemsResource: ...

class GroupItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GroupItem: ...

class ListGroupItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupItemsResponse: ...

class GroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Group: ...

class ListGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupsResponse: ...

class EmptyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EmptyResponse: ...

class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryResponse: ...
