import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudRunResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class ConfigurationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConfigurationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    watch: bool = ...,
                    fieldSelector: str = ...,
                    resourceVersion: str = ...,
                    **kwargs: typing.Any
                ) -> ListConfigurationsResponseHttpRequest: ...
            class DomainmappingsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    watch: bool = ...,
                    limit: int = ...,
                    fieldSelector: str = ...,
                    labelSelector: str = ...,
                    resourceVersion: str = ...,
                    **kwargs: typing.Any
                ) -> ListDomainMappingsResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    apiVersion: str = ...,
                    **kwargs: typing.Any
                ) -> StatusHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: DomainMapping = ...,
                    **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
            class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAuthorizedDomainsResponseHttpRequest: ...
            class ServicesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Service = ..., **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    apiVersion: str = ...,
                    **kwargs: typing.Any
                ) -> StatusHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
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
                    parent: str,
                    resourceVersion: str = ...,
                    fieldSelector: str = ...,
                    labelSelector: str = ...,
                    includeUninitialized: bool = ...,
                    watch: bool = ...,
                    limit: int = ...,
                    **kwargs: typing.Any
                ) -> ListServicesResponseHttpRequest: ...
                def replaceService(
                    self, *, name: str, body: Service = ..., **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
            class RevisionsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RevisionHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    kind: str = ...,
                    apiVersion: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> StatusHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    watch: bool = ...,
                    resourceVersion: str = ...,
                    limit: int = ...,
                    labelSelector: str = ...,
                    fieldSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListRevisionsResponseHttpRequest: ...
            class RoutesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    limit: int = ...,
                    labelSelector: str = ...,
                    includeUninitialized: bool = ...,
                    resourceVersion: str = ...,
                    fieldSelector: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListRoutesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RouteHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def configurations(self) -> ConfigurationsResource: ...
            def domainmappings(self) -> DomainmappingsResource: ...
            def authorizeddomains(self) -> AuthorizeddomainsResource: ...
            def services(self) -> ServicesResource: ...
            def revisions(self) -> RevisionsResource: ...
            def routes(self) -> RoutesResource: ...
        def authorizeddomains(self) -> AuthorizeddomainsResource: ...
        def locations(self) -> LocationsResource: ...
    class NamespacesResource(googleapiclient.discovery.Resource):
        class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
        class ConfigurationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                fieldSelector: str = ...,
                resourceVersion: str = ...,
                limit: int = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListConfigurationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
        class ServicesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                limit: int = ...,
                labelSelector: str = ...,
                includeUninitialized: bool = ...,
                resourceVersion: str = ...,
                fieldSelector: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListServicesResponseHttpRequest: ...
            def replaceService(
                self, *, name: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
        class DomainmappingsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                kind: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                watch: bool = ...,
                labelSelector: str = ...,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                **kwargs: typing.Any
            ) -> ListDomainMappingsResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: DomainMapping = ..., **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
        class RevisionsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                kind: str = ...,
                **kwargs: typing.Any
            ) -> StatusHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> RevisionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                labelSelector: str = ...,
                limit: int = ...,
                watch: bool = ...,
                fieldSelector: str = ...,
                includeUninitialized: bool = ...,
                resourceVersion: str = ...,
                **kwargs: typing.Any
            ) -> ListRevisionsResponseHttpRequest: ...
        class RoutesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                resourceVersion: str = ...,
                labelSelector: str = ...,
                includeUninitialized: bool = ...,
                watch: bool = ...,
                limit: int = ...,
                fieldSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListRoutesResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RouteHttpRequest: ...
        def authorizeddomains(self) -> AuthorizeddomainsResource: ...
        def configurations(self) -> ConfigurationsResource: ...
        def services(self) -> ServicesResource: ...
        def domainmappings(self) -> DomainmappingsResource: ...
        def revisions(self) -> RevisionsResource: ...
        def routes(self) -> RoutesResource: ...
    def projects(self) -> ProjectsResource: ...
    def namespaces(self) -> NamespacesResource: ...

class ListAuthorizedDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAuthorizedDomainsResponse: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class ListRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRevisionsResponse: ...

class StatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Status: ...

class ListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConfigurationsResponse: ...

class ListDomainMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDomainMappingsResponse: ...

class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Configuration: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Revision: ...

class ListRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRoutesResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Route: ...

class DomainMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DomainMapping: ...

class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Service: ...
