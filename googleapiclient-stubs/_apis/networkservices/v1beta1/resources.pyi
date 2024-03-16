import collections.abc
import typing

import httplib2
import typing_extensions

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
            class EndpointPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EndpointPolicy = ...,
                    endpointPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EndpointPolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: EndpointPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class GatewaysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Gateway = ...,
                    gatewayId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Gateway = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class GrpcRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GrpcRoute = ...,
                    grpcRouteId: str = ...,
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
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: GrpcRoute = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class HttpRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: HttpRoute = ...,
                    httpRouteId: str = ...,
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
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: HttpRoute = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class LbRouteExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LbRouteExtension = ...,
                    lbRouteExtensionId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LbRouteExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: LbRouteExtension = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class LbTrafficExtensionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LbTrafficExtension = ...,
                    lbTrafficExtensionId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LbTrafficExtensionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: LbTrafficExtension = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MeshesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Mesh = ...,
                    meshId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MeshHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: Mesh = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
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
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ServiceBindingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ServiceBinding = ...,
                    serviceBindingId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceBindingHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListServiceBindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListServiceBindingsResponseHttpRequest,
                    previous_response: ListServiceBindingsResponse,
                ) -> ListServiceBindingsResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ServiceLbPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ServiceLbPolicy = ...,
                    serviceLbPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServiceLbPolicyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: ServiceLbPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class TcpRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TcpRoute = ...,
                    tcpRouteId: str = ...,
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
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: TcpRoute = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class TlsRoutesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TlsRoute = ...,
                    tlsRouteId: str = ...,
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
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    body: TlsRoute = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def endpointPolicies(self) -> EndpointPoliciesResource: ...
            def gateways(self) -> GatewaysResource: ...
            def grpcRoutes(self) -> GrpcRoutesResource: ...
            def httpRoutes(self) -> HttpRoutesResource: ...
            def lbRouteExtensions(self) -> LbRouteExtensionsResource: ...
            def lbTrafficExtensions(self) -> LbTrafficExtensionsResource: ...
            def meshes(self) -> MeshesResource: ...
            def operations(self) -> OperationsResource: ...
            def serviceBindings(self) -> ServiceBindingsResource: ...
            def serviceLbPolicies(self) -> ServiceLbPoliciesResource: ...
            def tcpRoutes(self) -> TcpRoutesResource: ...
            def tlsRoutes(self) -> TlsRoutesResource: ...

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
class EndpointPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EndpointPolicy: ...

@typing.type_check_only
class GatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Gateway: ...

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
class LbRouteExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LbRouteExtension: ...

@typing.type_check_only
class LbTrafficExtensionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LbTrafficExtension: ...

@typing.type_check_only
class ListEndpointPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEndpointPoliciesResponse: ...

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
class ListLbRouteExtensionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLbRouteExtensionsResponse: ...

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
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

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
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class TlsRouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TlsRoute: ...
