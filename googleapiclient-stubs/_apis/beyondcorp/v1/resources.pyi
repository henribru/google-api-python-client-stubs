import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BeyondCorpResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GlobalResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PartnerTenantsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class BrowserDlpRulesResource(googleapiclient.discovery.Resource):
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1SetIamPolicyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                    @typing.type_check_only
                    class ProxyConfigsResource(googleapiclient.discovery.Resource):
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1SetIamPolicyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def browserDlpRules(self) -> BrowserDlpRulesResource: ...
                    def proxyConfigs(self) -> ProxyConfigsResource: ...

                def partnerTenants(self) -> PartnerTenantsResource: ...

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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            def global_(self) -> GlobalResource: ...
            def operations(self) -> OperationsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpAppconnectionsV1AppConnection = ...,
                    appConnectionId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectionsV1AppConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse,
                ) -> (
                    GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpAppconnectionsV1AppConnection = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolve(
                    self,
                    *,
                    parent: str,
                    appConnectorId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseHttpRequest: ...
                def resolve_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse,
                ) -> (
                    GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseHttpRequest
                    | None
                ): ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class AppConnectorsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1AppConnector = ...,
                    appConnectorId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectorsV1AppConnectorHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse,
                ) -> (
                    GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1AppConnector = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reportStatus(
                    self,
                    *,
                    appConnector: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolveInstanceConfig(
                    self, *, appConnector: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class AppGatewaysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AppGateway = ...,
                    appGatewayId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AppGatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAppGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAppGatewaysResponseHttpRequest,
                    previous_response: ListAppGatewaysResponse,
                ) -> ListAppGatewaysResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def shouldThrottle(
                    self,
                    *,
                    name: str,
                    port: int = ...,
                    requestedAmount: str = ...,
                    **kwargs: typing.Any,
                ) -> ShouldThrottleResponseHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ClientConnectorServicesResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ClientGatewaysResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class GlobalResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SecurityGatewaysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ApplicationsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudBeyondcorpSecuritygatewaysV1Application = ...,
                            applicationId: str = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudBeyondcorpSecuritygatewaysV1Application = ...,
                            requestId: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                    def applications(self) -> ApplicationsResource: ...

                def securityGateways(self) -> SecurityGatewaysResource: ...

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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class SecurityGatewaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ApplicationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        name: str,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationHttpRequest
                    ): ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponseHttpRequest,
                        previous_response: GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse,
                    ) -> (
                        GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponseHttpRequest
                        | None
                    ): ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway = ...,
                    requestId: str = ...,
                    securityGatewayId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayHttpRequest
                ): ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse,
                ) -> (
                    GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def applications(self) -> ApplicationsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
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
            def appConnections(self) -> AppConnectionsResource: ...
            def appConnectors(self) -> AppConnectorsResource: ...
            def appGateways(self) -> AppGatewaysResource: ...
            def clientConnectorServices(self) -> ClientConnectorServicesResource: ...
            def clientGateways(self) -> ClientGatewaysResource: ...
            def global_(self) -> GlobalResource: ...
            def operations(self) -> OperationsResource: ...
            def securityGateways(self) -> SecurityGatewaysResource: ...

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
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AppGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppGateway: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1AppConnection: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1AppConnector: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1Application: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway: ...

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
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

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

@typing.type_check_only
class ListAppGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppGatewaysResponse: ...

@typing.type_check_only
class ShouldThrottleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShouldThrottleResponse: ...
