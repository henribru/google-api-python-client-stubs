import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DatabaseCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def aggregateQueryStats(
            self, *, parent: str, body: AggregateQueryStatsRequest, **kwargs: typing.Any
        ) -> AggregateQueryStatsResponseHttpRequest: ...
        def aggregateQueryStats_next(
            self,
            previous_request: AggregateQueryStatsResponseHttpRequest,
            previous_response: AggregateQueryStatsResponse,
        ) -> AggregateQueryStatsResponseHttpRequest | None: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        def aggregateQueryStats(
            self, *, parent: str, body: AggregateQueryStatsRequest, **kwargs: typing.Any
        ) -> AggregateQueryStatsResponseHttpRequest: ...
        def aggregateQueryStats_next(
            self,
            previous_request: AggregateQueryStatsResponseHttpRequest,
            previous_response: AggregateQueryStatsResponse,
        ) -> AggregateQueryStatsResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def aggregateQueryStats(
            self, *, parent: str, body: AggregateQueryStatsRequest, **kwargs: typing.Any
        ) -> AggregateQueryStatsResponseHttpRequest: ...
        def aggregateQueryStats_next(
            self,
            previous_request: AggregateQueryStatsResponseHttpRequest,
            previous_response: AggregateQueryStatsResponse,
        ) -> AggregateQueryStatsResponseHttpRequest | None: ...

    @typing.type_check_only
    class V1betaResource(googleapiclient.discovery.Resource):
        def aggregateFleet(
            self,
            *,
            baselineDate_day: int | None = ...,
            baselineDate_month: int | None = ...,
            baselineDate_year: int | None = ...,
            filter: str | None = ...,
            groupBy: str | None = ...,
            orderBy: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            parent: str | None = ...,
            **kwargs: typing.Any,
        ) -> AggregateFleetResponseHttpRequest: ...
        def aggregateFleet_next(
            self,
            previous_request: AggregateFleetResponseHttpRequest,
            previous_response: AggregateFleetResponse,
        ) -> AggregateFleetResponseHttpRequest | None: ...
        def aggregateIssueStats(
            self, *, body: AggregateIssueStatsRequest, **kwargs: typing.Any
        ) -> AggregateIssueStatsResponseHttpRequest: ...
        def queryDatabaseResourceGroups(
            self, *, body: QueryDatabaseResourceGroupsRequest, **kwargs: typing.Any
        ) -> QueryDatabaseResourceGroupsResponseHttpRequest: ...
        def queryDatabaseResourceGroups_next(
            self,
            previous_request: QueryDatabaseResourceGroupsResponseHttpRequest,
            previous_response: QueryDatabaseResourceGroupsResponse,
        ) -> QueryDatabaseResourceGroupsResponseHttpRequest | None: ...
        def queryIssues(
            self, *, body: QueryIssuesRequest, **kwargs: typing.Any
        ) -> QueryIssuesResponseHttpRequest: ...
        def queryIssues_next(
            self,
            previous_request: QueryIssuesResponseHttpRequest,
            previous_response: QueryIssuesResponse,
        ) -> QueryIssuesResponseHttpRequest | None: ...
        def queryProducts(
            self,
            *,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            parent: str | None = ...,
            **kwargs: typing.Any,
        ) -> QueryProductsResponseHttpRequest: ...
        def queryProducts_next(
            self,
            previous_request: QueryProductsResponseHttpRequest,
            previous_response: QueryProductsResponse,
        ) -> QueryProductsResponseHttpRequest | None: ...

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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def v1beta(self) -> V1betaResource: ...

@typing.type_check_only
class AggregateFleetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AggregateFleetResponse: ...

@typing.type_check_only
class AggregateIssueStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AggregateIssueStatsResponse: ...

@typing.type_check_only
class AggregateQueryStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AggregateQueryStatsResponse: ...

@typing.type_check_only
class QueryDatabaseResourceGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryDatabaseResourceGroupsResponse: ...

@typing.type_check_only
class QueryIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryIssuesResponse: ...

@typing.type_check_only
class QueryProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryProductsResponse: ...
