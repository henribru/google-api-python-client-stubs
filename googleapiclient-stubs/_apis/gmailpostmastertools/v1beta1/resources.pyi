import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PostmasterToolsResource(googleapiclient.discovery.Resource):
    class DomainsResource(googleapiclient.discovery.Resource):
        class TrafficStatsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                endDate_year: int = ...,
                endDate_month: int = ...,
                endDate_day: int = ...,
                pageToken: str = ...,
                startDate_day: int = ...,
                startDate_year: int = ...,
                startDate_month: int = ...,
                **kwargs: typing.Any
            ) -> ListTrafficStatsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TrafficStatsHttpRequest: ...
        def list(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> ListDomainsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> DomainHttpRequest: ...
        def trafficStats(self) -> TrafficStatsResource: ...
    def domains(self) -> DomainsResource: ...

class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Domain: ...

class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDomainsResponse: ...

class TrafficStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TrafficStats: ...

class ListTrafficStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTrafficStatsResponse: ...
