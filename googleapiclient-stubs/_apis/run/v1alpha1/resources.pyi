import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
        @typing.type_check_only
        class CloudauditlogssourcesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CloudAuditLogsSource = ...,
                **kwargs: typing.Any
            ) -> CloudAuditLogsSourceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudAuditLogsSourceHttpRequest: ...
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
            ) -> ListCloudAuditLogsSourcesResponseHttpRequest: ...
        @typing.type_check_only
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
                apiVersion: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
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
                includeUninitialized: bool = ...,
                labelSelector: str = ...,
                limit: int = ...,
                resourceVersion: str = ...,
                watch: bool = ...,
                **kwargs: typing.Any
            ) -> ListCloudPubSubSourcesResponseHttpRequest: ...
        @typing.type_check_only
        class CloudschedulersourcesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CloudSchedulerSource = ...,
                **kwargs: typing.Any
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
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudSchedulerSourceHttpRequest: ...
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
            ) -> ListCloudSchedulerSourcesResponseHttpRequest: ...
            def replaceCloudSchedulerSource(
                self,
                *,
                name: str,
                body: CloudSchedulerSource = ...,
                **kwargs: typing.Any
            ) -> CloudSchedulerSourceHttpRequest: ...
        @typing.type_check_only
        class CloudstoragesourcesResource(googleapiclient.discovery.Resource):
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
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> CloudStorageSourceHttpRequest: ...
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
            ) -> ListCloudStorageSourcesResponseHttpRequest: ...
            def replaceCloudStorageSource(
                self, *, name: str, body: CloudStorageSource = ..., **kwargs: typing.Any
            ) -> CloudStorageSourceHttpRequest: ...
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
                self, *, parent: str, body: DomainMapping = ..., **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                orphanDependents: bool = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
        class RevisionsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                orphanDependents: bool = ...,
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
                self, *, parent: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                orphanDependents: bool = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
                self, *, name: str, body: Service = ..., **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
        @typing.type_check_only
        class TriggersResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Trigger = ..., **kwargs: typing.Any
            ) -> TriggerHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str = ...,
                kind: str = ...,
                propagationPolicy: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> TriggerHttpRequest: ...
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
            ) -> ListTriggersResponseHttpRequest: ...
        def authorizeddomains(self) -> AuthorizeddomainsResource: ...
        def cloudauditlogssources(self) -> CloudauditlogssourcesResource: ...
        def cloudpubsubsources(self) -> CloudpubsubsourcesResource: ...
        def cloudschedulersources(self) -> CloudschedulersourcesResource: ...
        def cloudstoragesources(self) -> CloudstoragesourcesResource: ...
        def configurations(self) -> ConfigurationsResource: ...
        def domainmappings(self) -> DomainmappingsResource: ...
        def revisions(self) -> RevisionsResource: ...
        def routes(self) -> RoutesResource: ...
        def services(self) -> ServicesResource: ...
        def triggers(self) -> TriggersResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
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
            @typing.type_check_only
            class CloudauditlogssourcesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudAuditLogsSource = ...,
                    **kwargs: typing.Any
                ) -> CloudAuditLogsSourceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudAuditLogsSourceHttpRequest: ...
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
                ) -> ListCloudAuditLogsSourcesResponseHttpRequest: ...
            @typing.type_check_only
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
                    apiVersion: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
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
                    includeUninitialized: bool = ...,
                    labelSelector: str = ...,
                    limit: int = ...,
                    resourceVersion: str = ...,
                    watch: bool = ...,
                    **kwargs: typing.Any
                ) -> ListCloudPubSubSourcesResponseHttpRequest: ...
            @typing.type_check_only
            class CloudschedulersourcesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudSchedulerSource = ...,
                    **kwargs: typing.Any
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
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudSchedulerSourceHttpRequest: ...
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
                ) -> ListCloudSchedulerSourcesResponseHttpRequest: ...
                def replaceCloudSchedulerSource(
                    self,
                    *,
                    name: str,
                    body: CloudSchedulerSource = ...,
                    **kwargs: typing.Any
                ) -> CloudSchedulerSourceHttpRequest: ...
            @typing.type_check_only
            class CloudstoragesourcesResource(googleapiclient.discovery.Resource):
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
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudStorageSourceHttpRequest: ...
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
                ) -> ListCloudStorageSourcesResponseHttpRequest: ...
                def replaceCloudStorageSource(
                    self,
                    *,
                    name: str,
                    body: CloudStorageSource = ...,
                    **kwargs: typing.Any
                ) -> CloudStorageSourceHttpRequest: ...
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
                    **kwargs: typing.Any
                ) -> DomainMappingHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    kind: str = ...,
                    orphanDependents: bool = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
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
            class RevisionsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    kind: str = ...,
                    orphanDependents: bool = ...,
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
                    self, *, parent: str, body: Service = ..., **kwargs: typing.Any
                ) -> ServiceHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    kind: str = ...,
                    orphanDependents: bool = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
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
                    self, *, name: str, body: Service = ..., **kwargs: typing.Any
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
            @typing.type_check_only
            class TriggersResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Trigger = ..., **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    apiVersion: str = ...,
                    kind: str = ...,
                    propagationPolicy: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
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
                ) -> ListTriggersResponseHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def authorizeddomains(self) -> AuthorizeddomainsResource: ...
            def cloudauditlogssources(self) -> CloudauditlogssourcesResource: ...
            def cloudpubsubsources(self) -> CloudpubsubsourcesResource: ...
            def cloudschedulersources(self) -> CloudschedulersourcesResource: ...
            def cloudstoragesources(self) -> CloudstoragesourcesResource: ...
            def configurations(self) -> ConfigurationsResource: ...
            def domainmappings(self) -> DomainmappingsResource: ...
            def revisions(self) -> RevisionsResource: ...
            def routes(self) -> RoutesResource: ...
            def services(self) -> ServicesResource: ...
            def triggers(self) -> TriggersResource: ...
        def locations(self) -> LocationsResource: ...
    def namespaces(self) -> NamespacesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class CloudAuditLogsSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CloudAuditLogsSource: ...

@typing.type_check_only
class CloudPubSubSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CloudPubSubSource: ...

@typing.type_check_only
class CloudSchedulerSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CloudSchedulerSource: ...

@typing.type_check_only
class CloudStorageSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CloudStorageSource: ...

@typing.type_check_only
class ConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Configuration: ...

@typing.type_check_only
class DomainMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DomainMapping: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListAuthorizedDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListAuthorizedDomainsResponse: ...

@typing.type_check_only
class ListCloudAuditLogsSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCloudAuditLogsSourcesResponse: ...

@typing.type_check_only
class ListCloudPubSubSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCloudPubSubSourcesResponse: ...

@typing.type_check_only
class ListCloudSchedulerSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCloudSchedulerSourcesResponse: ...

@typing.type_check_only
class ListCloudStorageSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCloudStorageSourcesResponse: ...

@typing.type_check_only
class ListConfigurationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListConfigurationsResponse: ...

@typing.type_check_only
class ListDomainMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDomainMappingsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListRevisionsResponse: ...

@typing.type_check_only
class ListRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListRoutesResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class ListTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListTriggersResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Revision: ...

@typing.type_check_only
class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Route: ...

@typing.type_check_only
class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Service: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class TriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Trigger: ...
