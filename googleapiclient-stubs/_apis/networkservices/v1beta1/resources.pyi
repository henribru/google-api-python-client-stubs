import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class NetworkServicesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AgentConnectivityTemplatesResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AgentConnectivityTemplate,
                    agentConnectivityTemplateId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str | None = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AgentConnectivityTemplateHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAgentConnectivityTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAgentConnectivityTemplatesResponseHttpRequest,
                    previous_response: ListAgentConnectivityTemplatesResponse,
                ) -> ListAgentConnectivityTemplatesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AgentConnectivityTemplate,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class AgentGatewaysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AgentGateway,
                    agentGatewayId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str | None = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AgentGatewayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAgentGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAgentGatewaysResponseHttpRequest,
                    previous_response: ListAgentGatewaysResponse,
                ) -> ListAgentGatewaysResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AgentGateway,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class AuthzExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AuthzExtension,
                    authzExtensionId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuthzExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListAuthzExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuthzExtensionsResponseHttpRequest,
                    previous_response: ListAuthzExtensionsResponse,
                ) -> ListAuthzExtensionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AuthzExtension,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class EndpointPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EndpointPolicy,
                    endpointPolicyId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EndpointPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListEndpointPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEndpointPoliciesResponseHttpRequest,
                    previous_response: ListEndpointPoliciesResponse,
                ) -> ListEndpointPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: EndpointPolicy,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ExtensionBindingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ExtensionBinding,
                    extensionBindingId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str | None = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ExtensionBindingHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListExtensionBindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListExtensionBindingsResponseHttpRequest,
                    previous_response: ListExtensionBindingsResponse,
                ) -> ListExtensionBindingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ExtensionBinding,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class GatewaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RouteViewsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GatewayRouteViewHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListGatewayRouteViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListGatewayRouteViewsResponseHttpRequest,
                        previous_response: ListGatewayRouteViewsResponse,
                    ) -> ListGatewayRouteViewsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Gateway,
                    gatewayId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GatewayHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGatewaysResponseHttpRequest,
                    previous_response: ListGatewaysResponse,
                ) -> ListGatewaysResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Gateway,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def routeViews(self) -> RouteViewsResource: ...

            @typing.type_check_only
            class GrpcRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GrpcRoute,
                    grpcRouteId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GrpcRouteHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListGrpcRoutesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGrpcRoutesResponseHttpRequest,
                    previous_response: ListGrpcRoutesResponse,
                ) -> ListGrpcRoutesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GrpcRoute,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class HttpRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: HttpRoute,
                    httpRouteId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> HttpRouteHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListHttpRoutesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListHttpRoutesResponseHttpRequest,
                    previous_response: ListHttpRoutesResponse,
                ) -> ListHttpRoutesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: HttpRoute,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class LbEdgeExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LbEdgeExtension,
                    lbEdgeExtensionId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LbEdgeExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListLbEdgeExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLbEdgeExtensionsResponseHttpRequest,
                    previous_response: ListLbEdgeExtensionsResponse,
                ) -> ListLbEdgeExtensionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LbEdgeExtension,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class LbRouteExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LbRouteExtension,
                    lbRouteExtensionId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LbRouteExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListLbRouteExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLbRouteExtensionsResponseHttpRequest,
                    previous_response: ListLbRouteExtensionsResponse,
                ) -> ListLbRouteExtensionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LbRouteExtension,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class LbTcpExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LbTcpExtension,
                    lbTcpExtensionId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LbTcpExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListLbTcpExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLbTcpExtensionsResponseHttpRequest,
                    previous_response: ListLbTcpExtensionsResponse,
                ) -> ListLbTcpExtensionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LbTcpExtension,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class LbTrafficExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LbTrafficExtension,
                    lbTrafficExtensionId: str | None = ...,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LbTrafficExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str | None = ...,
                    orderBy: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListLbTrafficExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLbTrafficExtensionsResponseHttpRequest,
                    previous_response: ListLbTrafficExtensionsResponse,
                ) -> ListLbTrafficExtensionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LbTrafficExtension,
                    requestId: str | None = ...,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MeshesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RouteViewsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> MeshRouteViewHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListMeshRouteViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListMeshRouteViewsResponseHttpRequest,
                        previous_response: ListMeshRouteViewsResponse,
                    ) -> ListMeshRouteViewsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Mesh,
                    meshId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MeshHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListMeshesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMeshesResponseHttpRequest,
                    previous_response: ListMeshesResponse,
                ) -> ListMeshesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Mesh,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def routeViews(self) -> RouteViewsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ProducerExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ProducerExtension,
                    producerExtensionId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str | None = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProducerExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListProducerExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListProducerExtensionsResponseHttpRequest,
                    previous_response: ListProducerExtensionsResponse,
                ) -> ListProducerExtensionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ServiceBindingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ServiceBinding,
                    serviceBindingId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceBindingHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListServiceBindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListServiceBindingsResponseHttpRequest,
                    previous_response: ListServiceBindingsResponse,
                ) -> ListServiceBindingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ServiceBinding,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ServiceLbPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ServiceLbPolicy,
                    serviceLbPolicyId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceLbPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListServiceLbPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListServiceLbPoliciesResponseHttpRequest,
                    previous_response: ListServiceLbPoliciesResponse,
                ) -> ListServiceLbPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ServiceLbPolicy,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class TcpRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TcpRoute,
                    tcpRouteId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TcpRouteHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListTcpRoutesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTcpRoutesResponseHttpRequest,
                    previous_response: ListTcpRoutesResponse,
                ) -> ListTcpRoutesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TcpRoute,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class TlsRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TlsRoute,
                    tlsRouteId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TlsRouteHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    returnPartialSuccess: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ListTlsRoutesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTlsRoutesResponseHttpRequest,
                    previous_response: ListTlsRoutesResponse,
                ) -> ListTlsRoutesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TlsRoute,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class WasmPluginsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: WasmPluginVersion,
                        wasmPluginVersionId: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WasmPluginVersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListWasmPluginVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWasmPluginVersionsResponseHttpRequest,
                        previous_response: ListWasmPluginVersionsResponse,
                    ) -> ListWasmPluginVersionsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: WasmPlugin,
                    wasmPluginId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing.Literal[
                        "WASM_PLUGIN_VIEW_UNSPECIFIED",
                        "WASM_PLUGIN_VIEW_BASIC",
                        "WASM_PLUGIN_VIEW_FULL",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> WasmPluginHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListWasmPluginsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListWasmPluginsResponseHttpRequest,
                    previous_response: ListWasmPluginsResponse,
                ) -> ListWasmPluginsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: WasmPlugin,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def versions(self) -> VersionsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] | None = ...,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def agentConnectivityTemplates(
                self,
            ) -> AgentConnectivityTemplatesResource: ...
            def agentGateways(self) -> AgentGatewaysResource: ...
            def authzExtensions(self) -> AuthzExtensionsResource: ...
            def endpointPolicies(self) -> EndpointPoliciesResource: ...
            def extensionBindings(self) -> ExtensionBindingsResource: ...
            def gateways(self) -> GatewaysResource: ...
            def grpcRoutes(self) -> GrpcRoutesResource: ...
            def httpRoutes(self) -> HttpRoutesResource: ...
            def lbEdgeExtensions(self) -> LbEdgeExtensionsResource: ...
            def lbRouteExtensions(self) -> LbRouteExtensionsResource: ...
            def lbTcpExtensions(self) -> LbTcpExtensionsResource: ...
            def lbTrafficExtensions(self) -> LbTrafficExtensionsResource: ...
            def meshes(self) -> MeshesResource: ...
            def operations(self) -> OperationsResource: ...
            def producerExtensions(self) -> ProducerExtensionsResource: ...
            def serviceBindings(self) -> ServiceBindingsResource: ...
            def serviceLbPolicies(self) -> ServiceLbPoliciesResource: ...
            def tcpRoutes(self) -> TcpRoutesResource: ...
            def tlsRoutes(self) -> TlsRoutesResource: ...
            def wasmPlugins(self) -> WasmPluginsResource: ...

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
class AgentConnectivityTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AgentConnectivityTemplate: ...

@typing.type_check_only
class AgentGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AgentGateway: ...

@typing.type_check_only
class AuthzExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuthzExtension: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EndpointPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EndpointPolicy: ...

@typing.type_check_only
class ExtensionBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExtensionBinding: ...

@typing.type_check_only
class GatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Gateway: ...

@typing.type_check_only
class GatewayRouteViewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GatewayRouteView: ...

@typing.type_check_only
class GrpcRouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GrpcRoute: ...

@typing.type_check_only
class HttpRouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HttpRoute: ...

@typing.type_check_only
class LbEdgeExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LbEdgeExtension: ...

@typing.type_check_only
class LbRouteExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LbRouteExtension: ...

@typing.type_check_only
class LbTcpExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LbTcpExtension: ...

@typing.type_check_only
class LbTrafficExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LbTrafficExtension: ...

@typing.type_check_only
class ListAgentConnectivityTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAgentConnectivityTemplatesResponse: ...

@typing.type_check_only
class ListAgentGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAgentGatewaysResponse: ...

@typing.type_check_only
class ListAuthzExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuthzExtensionsResponse: ...

@typing.type_check_only
class ListEndpointPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEndpointPoliciesResponse: ...

@typing.type_check_only
class ListExtensionBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExtensionBindingsResponse: ...

@typing.type_check_only
class ListGatewayRouteViewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGatewayRouteViewsResponse: ...

@typing.type_check_only
class ListGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGatewaysResponse: ...

@typing.type_check_only
class ListGrpcRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGrpcRoutesResponse: ...

@typing.type_check_only
class ListHttpRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListHttpRoutesResponse: ...

@typing.type_check_only
class ListLbEdgeExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLbEdgeExtensionsResponse: ...

@typing.type_check_only
class ListLbRouteExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLbRouteExtensionsResponse: ...

@typing.type_check_only
class ListLbTcpExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLbTcpExtensionsResponse: ...

@typing.type_check_only
class ListLbTrafficExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLbTrafficExtensionsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMeshRouteViewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMeshRouteViewsResponse: ...

@typing.type_check_only
class ListMeshesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMeshesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListProducerExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProducerExtensionsResponse: ...

@typing.type_check_only
class ListServiceBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListServiceBindingsResponse: ...

@typing.type_check_only
class ListServiceLbPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListServiceLbPoliciesResponse: ...

@typing.type_check_only
class ListTcpRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTcpRoutesResponse: ...

@typing.type_check_only
class ListTlsRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTlsRoutesResponse: ...

@typing.type_check_only
class ListWasmPluginVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWasmPluginVersionsResponse: ...

@typing.type_check_only
class ListWasmPluginsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWasmPluginsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class MeshHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Mesh: ...

@typing.type_check_only
class MeshRouteViewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MeshRouteView: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class ProducerExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProducerExtension: ...

@typing.type_check_only
class ServiceBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServiceBinding: ...

@typing.type_check_only
class ServiceLbPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServiceLbPolicy: ...

@typing.type_check_only
class TcpRouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TcpRoute: ...

@typing.type_check_only
class TlsRouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TlsRoute: ...

@typing.type_check_only
class WasmPluginHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WasmPlugin: ...

@typing.type_check_only
class WasmPluginVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WasmPluginVersion: ...
