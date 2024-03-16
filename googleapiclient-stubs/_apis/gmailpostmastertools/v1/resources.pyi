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
    class DomainsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TrafficStatsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TrafficStatsHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                endDate_day: int = ...,
                endDate_month: int = ...,
                endDate_year: int = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                startDate_day: int = ...,
                startDate_month: int = ...,
                startDate_year: int = ...,
                **kwargs: typing.Any,
            ) -> ListTrafficStatsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTrafficStatsResponseHttpRequest,
                previous_response: ListTrafficStatsResponse,
            ) -> ListTrafficStatsResponseHttpRequest | None: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> DomainHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListDomainsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListDomainsResponseHttpRequest,
            previous_response: ListDomainsResponse,
        ) -> ListDomainsResponseHttpRequest | None: ...
        def trafficStats(self) -> TrafficStatsResource: ...

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
    def domains(self) -> DomainsResource: ...

@typing.type_check_only
class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Domain: ...

@typing.type_check_only
class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDomainsResponse: ...

@typing.type_check_only
class ListTrafficStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTrafficStatsResponse: ...

@typing.type_check_only
class TrafficStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TrafficStats: ...
