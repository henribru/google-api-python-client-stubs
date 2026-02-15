import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class APIHubResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddonsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1AddonHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListAddonsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListAddonsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListAddonsResponse,
                ) -> GoogleCloudApihubV1ListAddonsResponseHttpRequest | None: ...
                def manageConfig(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1ManageAddonConfigRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class ApiHubInstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1ApiHubInstance = ...,
                    apiHubInstanceId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1ApiHubInstanceHttpRequest: ...
                def lookup(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1LookupApiHubInstanceResponseHttpRequest: ...

            @typing.type_check_only
            class ApisResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class DefinitionsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApihubV1DefinitionHttpRequest: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApihubV1ApiOperation = ...,
                            apiOperationId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApihubV1ApiOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApihubV1ApiOperationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudApihubV1ListApiOperationsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudApihubV1ListApiOperationsResponseHttpRequest,
                            previous_response: GoogleCloudApihubV1ListApiOperationsResponse,
                        ) -> (
                            GoogleCloudApihubV1ListApiOperationsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudApihubV1ApiOperation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApihubV1ApiOperationHttpRequest: ...

                    @typing.type_check_only
                    class SpecsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApihubV1Spec = ...,
                            specId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApihubV1SpecHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def fetchAdditionalSpecContent(
                            self,
                            *,
                            name: str,
                            specContentType: typing_extensions.Literal[
                                "SPEC_CONTENT_TYPE_UNSPECIFIED",
                                "BOOSTED_SPEC_CONTENT",
                                "GATEWAY_OPEN_API_SPEC",
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApihubV1FetchAdditionalSpecContentResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApihubV1SpecHttpRequest: ...
                        def getContents(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApihubV1SpecContentsHttpRequest: ...
                        def lint(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudApihubV1LintSpecRequest = ...,
                            **kwargs: typing.Any,
                        ) -> EmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApihubV1ListSpecsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudApihubV1ListSpecsResponseHttpRequest,
                            previous_response: GoogleCloudApihubV1ListSpecsResponse,
                        ) -> GoogleCloudApihubV1ListSpecsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudApihubV1Spec = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApihubV1SpecHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApihubV1Version = ...,
                        versionId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1VersionHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApihubV1VersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1ListVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudApihubV1ListVersionsResponseHttpRequest,
                        previous_response: GoogleCloudApihubV1ListVersionsResponse,
                    ) -> GoogleCloudApihubV1ListVersionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApihubV1Version = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1VersionHttpRequest: ...
                    def definitions(self) -> DefinitionsResource: ...
                    def operations(self) -> OperationsResource: ...
                    def specs(self) -> SpecsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1Api = ...,
                    apiId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ApiHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1ApiHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListApisResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListApisResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListApisResponse,
                ) -> GoogleCloudApihubV1ListApisResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1Api = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ApiHttpRequest: ...
                def versions(self) -> VersionsResource: ...

            @typing.type_check_only
            class AttributesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1Attribute = ...,
                    attributeId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1AttributeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1AttributeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListAttributesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListAttributesResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListAttributesResponse,
                ) -> GoogleCloudApihubV1ListAttributesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1Attribute = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1AttributeHttpRequest: ...

            @typing.type_check_only
            class CurationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1Curation = ...,
                    curationId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1CurationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1CurationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListCurationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListCurationsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListCurationsResponse,
                ) -> GoogleCloudApihubV1ListCurationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1Curation = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1CurationHttpRequest: ...

            @typing.type_check_only
            class DependenciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1Dependency = ...,
                    dependencyId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1DependencyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1DependencyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListDependenciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListDependenciesResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListDependenciesResponse,
                ) -> GoogleCloudApihubV1ListDependenciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1Dependency = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1DependencyHttpRequest: ...

            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1Deployment = ...,
                    deploymentId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1DeploymentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1DeploymentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListDeploymentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListDeploymentsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListDeploymentsResponse,
                ) -> GoogleCloudApihubV1ListDeploymentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1Deployment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1DeploymentHttpRequest: ...

            @typing.type_check_only
            class DiscoveredApiObservationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DiscoveredApiOperationsResource(
                    googleapiclient.discovery.Resource
                ):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApihubV1DiscoveredApiOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1ListDiscoveredApiOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudApihubV1ListDiscoveredApiOperationsResponseHttpRequest,
                        previous_response: GoogleCloudApihubV1ListDiscoveredApiOperationsResponse,
                    ) -> (
                        GoogleCloudApihubV1ListDiscoveredApiOperationsResponseHttpRequest
                        | None
                    ): ...

                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1DiscoveredApiObservationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudApihubV1ListDiscoveredApiObservationsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListDiscoveredApiObservationsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListDiscoveredApiObservationsResponse,
                ) -> (
                    GoogleCloudApihubV1ListDiscoveredApiObservationsResponseHttpRequest
                    | None
                ): ...
                def discoveredApiOperations(
                    self,
                ) -> DiscoveredApiOperationsResource: ...

            @typing.type_check_only
            class ExternalApisResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1ExternalApi = ...,
                    externalApiId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ExternalApiHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1ExternalApiHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListExternalApisResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListExternalApisResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListExternalApisResponse,
                ) -> GoogleCloudApihubV1ListExternalApisResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1ExternalApi = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ExternalApiHttpRequest: ...

            @typing.type_check_only
            class HostProjectRegistrationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1HostProjectRegistration = ...,
                    hostProjectRegistrationId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1HostProjectRegistrationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1HostProjectRegistrationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudApihubV1ListHostProjectRegistrationsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListHostProjectRegistrationsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListHostProjectRegistrationsResponse,
                ) -> (
                    GoogleCloudApihubV1ListHostProjectRegistrationsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    returnPartialSuccess: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PluginsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class InstancesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApihubV1PluginInstance = ...,
                        pluginInstanceId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def disableAction(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApihubV1DisablePluginInstanceActionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def enableAction(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApihubV1EnablePluginInstanceActionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def executeAction(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApihubV1ExecutePluginInstanceActionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApihubV1PluginInstanceHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1ListPluginInstancesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudApihubV1ListPluginInstancesResponseHttpRequest,
                        previous_response: GoogleCloudApihubV1ListPluginInstancesResponse,
                    ) -> (
                        GoogleCloudApihubV1ListPluginInstancesResponseHttpRequest | None
                    ): ...
                    def manageSourceData(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApihubV1ManagePluginInstanceSourceDataRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1ManagePluginInstanceSourceDataResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApihubV1PluginInstance = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApihubV1PluginInstanceHttpRequest: ...

                @typing.type_check_only
                class StyleGuideResource(googleapiclient.discovery.Resource):
                    def getContents(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApihubV1StyleGuideContentsHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1Plugin = ...,
                    pluginId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1PluginHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1DisablePluginRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1PluginHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1EnablePluginRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1PluginHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1PluginHttpRequest: ...
                def getStyleGuide(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1StyleGuideHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1ListPluginsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListPluginsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListPluginsResponse,
                ) -> GoogleCloudApihubV1ListPluginsResponseHttpRequest | None: ...
                def updateStyleGuide(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApihubV1StyleGuide = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1StyleGuideHttpRequest: ...
                def instances(self) -> InstancesResource: ...
                def styleGuide(self) -> StyleGuideResource: ...

            @typing.type_check_only
            class RuntimeProjectAttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApihubV1RuntimeProjectAttachment = ...,
                    runtimeProjectAttachmentId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApihubV1RuntimeProjectAttachmentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApihubV1RuntimeProjectAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponseHttpRequest,
                    previous_response: GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse,
                ) -> (
                    GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponseHttpRequest
                    | None
                ): ...

            def collectApiData(
                self,
                *,
                location: str,
                body: GoogleCloudApihubV1CollectApiDataRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def lookupRuntimeProjectAttachment(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponseHttpRequest
            ): ...
            def retrieveApiViews(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "API_VIEW_TYPE_UNSPECIFIED", "MCP_SERVER", "MCP_TOOL"
                ] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApihubV1RetrieveApiViewsResponseHttpRequest: ...
            def retrieveApiViews_next(
                self,
                previous_request: GoogleCloudApihubV1RetrieveApiViewsResponseHttpRequest,
                previous_response: GoogleCloudApihubV1RetrieveApiViewsResponse,
            ) -> GoogleCloudApihubV1RetrieveApiViewsResponseHttpRequest | None: ...
            def searchResources(
                self,
                *,
                location: str,
                body: GoogleCloudApihubV1SearchResourcesRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApihubV1SearchResourcesResponseHttpRequest: ...
            def searchResources_next(
                self,
                previous_request: GoogleCloudApihubV1SearchResourcesResponseHttpRequest,
                previous_response: GoogleCloudApihubV1SearchResourcesResponse,
            ) -> GoogleCloudApihubV1SearchResourcesResponseHttpRequest | None: ...
            def addons(self) -> AddonsResource: ...
            def apiHubInstances(self) -> ApiHubInstancesResource: ...
            def apis(self) -> ApisResource: ...
            def attributes(self) -> AttributesResource: ...
            def curations(self) -> CurationsResource: ...
            def dependencies(self) -> DependenciesResource: ...
            def deployments(self) -> DeploymentsResource: ...
            def discoveredApiObservations(
                self,
            ) -> DiscoveredApiObservationsResource: ...
            def externalApis(self) -> ExternalApisResource: ...
            def hostProjectRegistrations(self) -> HostProjectRegistrationsResource: ...
            def operations(self) -> OperationsResource: ...
            def plugins(self) -> PluginsResource: ...
            def runtimeProjectAttachments(
                self,
            ) -> RuntimeProjectAttachmentsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudApihubV1AddonHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Addon: ...

@typing.type_check_only
class GoogleCloudApihubV1ApiHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Api: ...

@typing.type_check_only
class GoogleCloudApihubV1ApiHubInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ApiHubInstance: ...

@typing.type_check_only
class GoogleCloudApihubV1ApiOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ApiOperation: ...

@typing.type_check_only
class GoogleCloudApihubV1AttributeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Attribute: ...

@typing.type_check_only
class GoogleCloudApihubV1CurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Curation: ...

@typing.type_check_only
class GoogleCloudApihubV1DefinitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Definition: ...

@typing.type_check_only
class GoogleCloudApihubV1DependencyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Dependency: ...

@typing.type_check_only
class GoogleCloudApihubV1DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Deployment: ...

@typing.type_check_only
class GoogleCloudApihubV1DiscoveredApiObservationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1DiscoveredApiObservation: ...

@typing.type_check_only
class GoogleCloudApihubV1DiscoveredApiOperationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1DiscoveredApiOperation: ...

@typing.type_check_only
class GoogleCloudApihubV1ExternalApiHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ExternalApi: ...

@typing.type_check_only
class GoogleCloudApihubV1FetchAdditionalSpecContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1FetchAdditionalSpecContentResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1HostProjectRegistrationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1HostProjectRegistration: ...

@typing.type_check_only
class GoogleCloudApihubV1ListAddonsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListAddonsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListApiOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListApiOperationsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListApisResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListApisResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListAttributesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListAttributesResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListCurationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListCurationsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListDependenciesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListDependenciesResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListDeploymentsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListDiscoveredApiObservationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListDiscoveredApiObservationsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListDiscoveredApiOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListDiscoveredApiOperationsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListExternalApisResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListExternalApisResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListHostProjectRegistrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListHostProjectRegistrationsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListPluginInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListPluginInstancesResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListPluginsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListPluginsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListRuntimeProjectAttachmentsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListSpecsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListSpecsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1LookupApiHubInstanceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1LookupApiHubInstanceResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1LookupRuntimeProjectAttachmentResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1ManagePluginInstanceSourceDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1ManagePluginInstanceSourceDataResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1PluginHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Plugin: ...

@typing.type_check_only
class GoogleCloudApihubV1PluginInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1PluginInstance: ...

@typing.type_check_only
class GoogleCloudApihubV1RetrieveApiViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1RetrieveApiViewsResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1RuntimeProjectAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1RuntimeProjectAttachment: ...

@typing.type_check_only
class GoogleCloudApihubV1SearchResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1SearchResourcesResponse: ...

@typing.type_check_only
class GoogleCloudApihubV1SpecHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Spec: ...

@typing.type_check_only
class GoogleCloudApihubV1SpecContentsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1SpecContents: ...

@typing.type_check_only
class GoogleCloudApihubV1StyleGuideHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1StyleGuide: ...

@typing.type_check_only
class GoogleCloudApihubV1StyleGuideContentsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1StyleGuideContents: ...

@typing.type_check_only
class GoogleCloudApihubV1VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApihubV1Version: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...
