import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MonitoringResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class GlobalResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MetricsScopesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ProjectsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: MonitoredProject = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MetricsScopeHttpRequest: ...
                def listMetricsScopesByMonitoredProject(
                    self, *, monitoredResourceContainer: str = ..., **kwargs: typing.Any
                ) -> ListMetricsScopesByMonitoredProjectResponseHttpRequest: ...
                def projects(self) -> ProjectsResource: ...
            def metricsScopes(self) -> MetricsScopesResource: ...
        def global_(self) -> GlobalResource: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DashboardsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Dashboard = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> DashboardHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DashboardHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDashboardsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDashboardsResponseHttpRequest,
                previous_response: ListDashboardsResponse,
            ) -> ListDashboardsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Dashboard = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any
            ) -> DashboardHttpRequest: ...
        def dashboards(self) -> DashboardsResource: ...
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
    def locations(self) -> LocationsResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DashboardHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Dashboard: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListDashboardsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDashboardsResponse: ...

@typing.type_check_only
class ListMetricsScopesByMonitoredProjectResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMetricsScopesByMonitoredProjectResponse: ...

@typing.type_check_only
class MetricsScopeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MetricsScope: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...
