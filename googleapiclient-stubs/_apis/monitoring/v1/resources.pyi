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

        @typing.type_check_only
        class LocationResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class PrometheusResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ApiResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class V1Resource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class LabelResource(googleapiclient.discovery.Resource):
                            def values(
                                self,
                                *,
                                name: str,
                                location: str,
                                label: str,
                                end: str = ...,
                                match: str = ...,
                                start: str = ...,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...

                        @typing.type_check_only
                        class LabelsResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                name: str,
                                location: str,
                                end: str = ...,
                                match: str = ...,
                                start: str = ...,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...

                        @typing.type_check_only
                        class MetadataResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                name: str,
                                location: str,
                                limit: str = ...,
                                metric: str = ...,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...

                        def query(
                            self,
                            *,
                            name: str,
                            location: str,
                            body: QueryInstantRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def query_range(
                            self,
                            *,
                            name: str,
                            location: str,
                            body: QueryRangeRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def series(
                            self,
                            *,
                            name: str,
                            location: str,
                            body: QuerySeriesRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def label(self) -> LabelResource: ...
                        def labels(self) -> LabelsResource: ...
                        def metadata(self) -> MetadataResource: ...

                    def v1(self) -> V1Resource: ...

                def api(self) -> ApiResource: ...

            def prometheus(self) -> PrometheusResource: ...

        def dashboards(self) -> DashboardsResource: ...
        def location(self) -> LocationResource: ...

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
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpBody: ...

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
