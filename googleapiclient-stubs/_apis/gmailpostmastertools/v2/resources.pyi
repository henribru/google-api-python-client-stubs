import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class PostmasterToolsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DomainStatsResource(googleapiclient.discovery.Resource):
        def batchQuery(
            self, *, body: BatchQueryDomainStatsRequest = ..., **kwargs: typing.Any
        ) -> BatchQueryDomainStatsResponseHttpRequest: ...

    @typing.type_check_only
    class DomainsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DomainStatsResource(googleapiclient.discovery.Resource):
            def query(
                self,
                *,
                parent: str,
                body: QueryDomainStatsRequest = ...,
                **kwargs: typing.Any,
            ) -> QueryDomainStatsResponseHttpRequest: ...
            def query_next(
                self,
                previous_request: QueryDomainStatsResponseHttpRequest,
                previous_response: QueryDomainStatsResponse,
            ) -> QueryDomainStatsResponseHttpRequest | None: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> DomainHttpRequest: ...
        def getComplianceStatus(
            self, *, name: str, **kwargs: typing.Any
        ) -> DomainComplianceStatusHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListDomainsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListDomainsResponseHttpRequest,
            previous_response: ListDomainsResponse,
        ) -> ListDomainsResponseHttpRequest | None: ...
        def domainStats(self) -> DomainStatsResource: ...

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
    def domainStats(self) -> DomainStatsResource: ...
    def domains(self) -> DomainsResource: ...

@typing.type_check_only
class BatchQueryDomainStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchQueryDomainStatsResponse: ...

@typing.type_check_only
class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Domain: ...

@typing.type_check_only
class DomainComplianceStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DomainComplianceStatus: ...

@typing.type_check_only
class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDomainsResponse: ...

@typing.type_check_only
class QueryDomainStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryDomainStatsResponse: ...
