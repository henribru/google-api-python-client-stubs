import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudRunResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class NamespacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAuthorizedDomainsResponseHttpRequest,
                previous_response: ListAuthorizedDomainsResponse,
            ) -> ListAuthorizedDomainsResponseHttpRequest | None: ...

        @typing.type_check_only
        class ConfigurationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListConfigurationsResponseHttpRequest: ...

        @typing.type_check_only
        class DomainmappingsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: DomainMapping = ...,
                dryRun: str = ...,
                **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                dryRun: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListDomainMappingsResponseHttpRequest: ...

        @typing.type_check_only
        class ExecutionsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: CancelExecutionRequest = ...,
                **kwargs: typing.Any
            ) -> ExecutionHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ExecutionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListExecutionsResponseHttpRequest: ...

        @typing.type_check_only
        class JobsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Job = ..., **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListJobsResponseHttpRequest: ...
            def replaceJob(
                self, *, name: str, body: Job = ..., **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def run(
                self, *, name: str, body: RunJobRequest = ..., **kwargs: typing.Any
            ) -> ExecutionHttpRequest: ...

        @typing.type_check_only
        class RevisionsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                dryRun: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> RevisionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListRevisionsResponseHttpRequest: ...

        @typing.type_check_only
        class RoutesResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> RouteHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListRoutesResponseHttpRequest: ...

        @typing.type_check_only
        class ServicesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Service = ...,
                dryRun: str = ...,
                **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                dryRun: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListServicesResponseHttpRequest: ...
            def replaceService(
                self,
                *,
                name: str,
                body: Service = ...,
                dryRun: str = ...,
                **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...

        @typing.type_check_only
        class TasksResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> TaskHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListTasksResponseHttpRequest: ...

        def authorizeddomains(self) -> AuthorizeddomainsResource: ...
        def configurations(self) -> ConfigurationsResource: ...
        def domainmappings(self) -> DomainmappingsResource: ...
        def executions(self) -> ExecutionsResource: ...
        def jobs(self) -> JobsResource: ...
        def revisions(self) -> RevisionsResource: ...
        def routes(self) -> RoutesResource: ...
        def services(self) -> ServicesResource: ...
        def tasks(self) -> TasksResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAuthorizedDomainsResponseHttpRequest,
                previous_response: ListAuthorizedDomainsResponse,
            ) -> ListAuthorizedDomainsResponseHttpRequest | None: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAuthorizedDomainsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuthorizedDomainsResponseHttpRequest,
                    previous_response: ListAuthorizedDomainsResponse,
                ) -> ListAuthorizedDomainsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ConfigurationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConfigurationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListConfigurationsResponseHttpRequest: ...

            @typing.type_check_only
            class DomainmappingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: DomainMapping = ...,
                    dryRun: str = ...,
                    **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    dryRun: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> StatusHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListDomainMappingsResponseHttpRequest: ...

            @typing.type_check_only
            class JobsResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class RevisionsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    dryRun: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> StatusHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RevisionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListRevisionsResponseHttpRequest: ...

            @typing.type_check_only
            class RoutesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RouteHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListRoutesResponseHttpRequest: ...

            @typing.type_check_only
            class ServicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Service = ...,
                    dryRun: str = ...,
                    **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    dryRun: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> StatusHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListServicesResponseHttpRequest: ...
                def replaceService(
                    self,
                    *,
                    name: str,
                    body: Service = ...,
                    dryRun: str = ...,
                    **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def authorizeddomains(self) -> AuthorizeddomainsResource: ...
            def configurations(self) -> ConfigurationsResource: ...
            def domainmappings(self) -> DomainmappingsResource: ...
            def jobs(self) -> JobsResource: ...
            def revisions(self) -> RevisionsResource: ...
            def routes(self) -> RoutesResource: ...
            def services(self) -> ServicesResource: ...

        def authorizeddomains(self) -> AuthorizeddomainsResource: ...
        def locations(self) -> LocationsResource: ...

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
    def namespaces(self) -> NamespacesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Configuration: ...

@typing.type_check_only
class DomainMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DomainMapping: ...

@typing.type_check_only
class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Execution: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Job: ...

@typing.type_check_only
class ListAuthorizedDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAuthorizedDomainsResponse: ...

@typing.type_check_only
class ListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConfigurationsResponse: ...

@typing.type_check_only
class ListDomainMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDomainMappingsResponse: ...

@typing.type_check_only
class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListExecutionsResponse: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListJobsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRevisionsResponse: ...

@typing.type_check_only
class ListRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRoutesResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class ListTasksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTasksResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Revision: ...

@typing.type_check_only
class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Route: ...

@typing.type_check_only
class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Service: ...

@typing.type_check_only
class StatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Status: ...

@typing.type_check_only
class TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Task: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
