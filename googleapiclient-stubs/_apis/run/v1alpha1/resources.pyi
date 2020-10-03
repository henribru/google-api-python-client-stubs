import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudRunResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class ConfigurationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    fieldSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    labelSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListConfigurationsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConfigurationHttpRequest: ...
            class ServicesResource(googleapiclient.discovery.Resource):
                def replaceService(
                    self, *, name: str, body: Service = ..., **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def create(
                    self, *, parent: str, body: Service = ..., **kwargs: typing.Any
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
                    watch: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    fieldSelector: str = ...,
                    includeUninitialized: bool = ...,
                    **kwargs: typing.Any
                ) -> ListServicesResponseHttpRequest: ...
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
                    orphanDependents: bool = ...,
                    propagationPolicy: str = ...,
                    apiVersion: str = ...,
                    kind: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
            class CloudauditlogssourcesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudAuditLogsSource = ...,
                    **kwargs: typing.Any
                ) -> CloudAuditLogsSourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    watch: bool = ...,
                    resourceVersion: str = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    fieldSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListCloudAuditLogsSourcesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudAuditLogsSourceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    propagationPolicy: str = ...,
                    kind: str = ...,
                    apiVersion: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAuthorizedDomainsResponseHttpRequest: ...
            class TriggersResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    name: str,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    apiVersion: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
                def create(
                    self, *, parent: str, body: Trigger = ..., **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    watch: bool = ...,
                    resourceVersion: str = ...,
                    includeUninitialized: bool = ...,
                    limit: int = ...,
                    labelSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListTriggersResponseHttpRequest: ...
            class CloudstoragesourcesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudStorageSourceHttpRequest: ...
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
                ) -> ListCloudStorageSourcesResponseHttpRequest: ...
                def replaceCloudStorageSource(
                    self,
                    *,
                    name: str,
                    body: CloudStorageSource = ...,
                    **kwargs: typing.Any
                ) -> CloudStorageSourceHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudStorageSource = ...,
                    **kwargs: typing.Any
                ) -> CloudStorageSourceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    propagationPolicy: str = ...,
                    kind: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            class DomainmappingsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    orphanDependents: bool = ...,
                    kind: str = ...,
                    apiVersion: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    limit: int = ...,
                    fieldSelector: str = ...,
                    watch: bool = ...,
                    includeUninitialized: bool = ...,
                    resourceVersion: str = ...,
                    labelSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListDomainMappingsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: DomainMapping = ...,
                    **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
            class RevisionsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    name: str,
                    kind: str = ...,
                    orphanDependents: bool = ...,
                    apiVersion: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    resourceVersion: str = ...,
                    includeUninitialized: bool = ...,
                    watch: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    fieldSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListRevisionsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RevisionHttpRequest: ...
            class CloudpubsubsourcesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudPubSubSource = ...,
                    **kwargs: typing.Any
                ) -> CloudPubSubSourceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    propagationPolicy: str = ...,
                    apiVersion: str = ...,
                    kind: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudPubSubSourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldSelector: str = ...,
                    labelSelector: str = ...,
                    watch: bool = ...,
                    limit: int = ...,
                    includeUninitialized: bool = ...,
                    resourceVersion: str = ...,
                    **kwargs: typing.Any
                ) -> ListCloudPubSubSourcesResponseHttpRequest: ...
            class CloudschedulersourcesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudSchedulerSourceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def replaceCloudSchedulerSource(
                    self,
                    *,
                    name: str,
                    body: CloudSchedulerSource = ...,
                    **kwargs: typing.Any
                ) -> CloudSchedulerSourceHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudSchedulerSource = ...,
                    **kwargs: typing.Any
                ) -> CloudSchedulerSourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    limit: int = ...,
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    watch: bool = ...,
                    fieldSelector: str = ...,
                    resourceVersion: str = ...,
                    **kwargs: typing.Any
                ) -> ListCloudSchedulerSourcesResponseHttpRequest: ...
            class RoutesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    includeUninitialized: bool = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    limit: int = ...,
                    labelSelector: str = ...,
                    fieldSelector: str = ...,
                    **kwargs: typing.Any
                ) -> ListRoutesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RouteHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def configurations(self) -> ConfigurationsResource: ...
            def services(self) -> ServicesResource: ...
            def cloudauditlogssources(self) -> CloudauditlogssourcesResource: ...
            def authorizeddomains(self) -> AuthorizeddomainsResource: ...
            def triggers(self) -> TriggersResource: ...
            def cloudstoragesources(self) -> CloudstoragesourcesResource: ...
            def domainmappings(self) -> DomainmappingsResource: ...
            def revisions(self) -> RevisionsResource: ...
            def cloudpubsubsources(self) -> CloudpubsubsourcesResource: ...
            def cloudschedulersources(self) -> CloudschedulersourcesResource: ...
            def routes(self) -> RoutesResource: ...
        def locations(self) -> LocationsResource: ...
    class NamespacesResource(googleapiclient.discovery.Resource):
        class DomainmappingsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                resourceVersion: str = ...,
                fieldSelector: str = ...,
                watch: bool = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                **kwargs: typing.Any
            ) -> ListDomainMappingsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                apiVersion: str = ...,
                orphanDependents: bool = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: DomainMapping = ..., **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
        class CloudauditlogssourcesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudAuditLogsSourceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                propagationPolicy: str = ...,
                apiVersion: str = ...,
                kind: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CloudAuditLogsSource = ...,
                **kwargs: typing.Any
            ) -> CloudAuditLogsSourceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                limit: int = ...,
                fieldSelector: str = ...,
                labelSelector: str = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                includeUninitialized: bool = ...,
                **kwargs: typing.Any
            ) -> ListCloudAuditLogsSourcesResponseHttpRequest: ...
        class ConfigurationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                watch: bool = ...,
                resourceVersion: str = ...,
                includeUninitialized: bool = ...,
                limit: int = ...,
                labelSelector: str = ...,
                fieldSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListConfigurationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ConfigurationHttpRequest: ...
        class ServicesResource(googleapiclient.discovery.Resource):
            def replaceService(
                self, *, name: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                orphanDependents: bool = ...,
                kind: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeUninitialized: bool = ...,
                resourceVersion: str = ...,
                limit: int = ...,
                fieldSelector: str = ...,
                watch: bool = ...,
                labelSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListServicesResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
        class CloudpubsubsourcesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CloudPubSubSource = ...,
                **kwargs: typing.Any
            ) -> CloudPubSubSourceHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudPubSubSourceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                fieldSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListCloudPubSubSourcesResponseHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class CloudschedulersourcesResource(googleapiclient.discovery.Resource):
            def replaceCloudSchedulerSource(
                self,
                *,
                name: str,
                body: CloudSchedulerSource = ...,
                **kwargs: typing.Any
            ) -> CloudSchedulerSourceHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CloudSchedulerSource = ...,
                **kwargs: typing.Any
            ) -> CloudSchedulerSourceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                limit: int = ...,
                fieldSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListCloudSchedulerSourcesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudSchedulerSourceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class RevisionsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                orphanDependents: bool = ...,
                apiVersion: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> RevisionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                watch: bool = ...,
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                fieldSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListRevisionsResponseHttpRequest: ...
        class CloudstoragesourcesResource(googleapiclient.discovery.Resource):
            def replaceCloudStorageSource(
                self, *, name: str, body: CloudStorageSource = ..., **kwargs: typing.Any
            ) -> CloudStorageSourceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                watch: bool = ...,
                includeUninitialized: bool = ...,
                resourceVersion: str = ...,
                limit: int = ...,
                fieldSelector: str = ...,
                labelSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListCloudStorageSourcesResponseHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                propagationPolicy: str = ...,
                apiVersion: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudStorageSourceHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: CloudStorageSource = ...,
                **kwargs: typing.Any
            ) -> CloudStorageSourceHttpRequest: ...
        class RoutesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str = ...,
                watch: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                includeUninitialized: bool = ...,
                resourceVersion: str = ...,
                **kwargs: typing.Any
            ) -> ListRoutesResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RouteHttpRequest: ...
        class AuthorizeddomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
        class TriggersResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                labelSelector: str = ...,
                limit: int = ...,
                watch: bool = ...,
                includeUninitialized: bool = ...,
                resourceVersion: str = ...,
                fieldSelector: str = ...,
                **kwargs: typing.Any
            ) -> ListTriggersResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> TriggerHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                kind: str = ...,
                propagationPolicy: str = ...,
                apiVersion: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: Trigger = ..., **kwargs: typing.Any
            ) -> TriggerHttpRequest: ...
        def domainmappings(self) -> DomainmappingsResource: ...
        def cloudauditlogssources(self) -> CloudauditlogssourcesResource: ...
        def configurations(self) -> ConfigurationsResource: ...
        def services(self) -> ServicesResource: ...
        def cloudpubsubsources(self) -> CloudpubsubsourcesResource: ...
        def cloudschedulersources(self) -> CloudschedulersourcesResource: ...
        def revisions(self) -> RevisionsResource: ...
        def cloudstoragesources(self) -> CloudstoragesourcesResource: ...
        def routes(self) -> RoutesResource: ...
        def authorizeddomains(self) -> AuthorizeddomainsResource: ...
        def triggers(self) -> TriggersResource: ...
    def projects(self) -> ProjectsResource: ...
    def namespaces(self) -> NamespacesResource: ...

class ListAuthorizedDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAuthorizedDomainsResponse: ...

class TriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Trigger: ...

class ListCloudPubSubSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCloudPubSubSourcesResponse: ...

class ListCloudAuditLogsSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCloudAuditLogsSourcesResponse: ...

class ListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConfigurationsResponse: ...

class ListDomainMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDomainMappingsResponse: ...

class CloudSchedulerSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CloudSchedulerSource: ...

class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Configuration: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class CloudStorageSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CloudStorageSource: ...

class ListTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTriggersResponse: ...

class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Revision: ...

class ListRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRoutesResponse: ...

class CloudPubSubSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CloudPubSubSource: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Route: ...

class ListCloudSchedulerSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCloudSchedulerSourcesResponse: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRevisionsResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class CloudAuditLogsSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CloudAuditLogsSource: ...

class ListCloudStorageSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCloudStorageSourcesResponse: ...

class DomainMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DomainMapping: ...

class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Service: ...
