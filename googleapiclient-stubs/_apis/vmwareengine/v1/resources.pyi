import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class VMwareEngineResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DnsBindPermissionResource(googleapiclient.discovery.Resource):
                def grant(
                    self,
                    *,
                    name: str,
                    body: GrantDnsBindPermissionRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def revoke(
                    self,
                    *,
                    name: str,
                    body: RevokeDnsBindPermissionRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class NetworkPeeringsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PeeringRoutesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPeeringRoutesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListPeeringRoutesResponseHttpRequest,
                        previous_response: ListPeeringRoutesResponse,
                    ) -> ListPeeringRoutesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: NetworkPeering = ...,
                    networkPeeringId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> NetworkPeeringHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNetworkPeeringsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNetworkPeeringsResponseHttpRequest,
                    previous_response: ListNetworkPeeringsResponse,
                ) -> ListNetworkPeeringsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: NetworkPeering = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def peeringRoutes(self) -> PeeringRoutesResource: ...

            @typing.type_check_only
            class NetworkPoliciesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExternalAccessRulesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ExternalAccessRule = ...,
                        externalAccessRuleId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ExternalAccessRuleHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListExternalAccessRulesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListExternalAccessRulesResponseHttpRequest,
                        previous_response: ListExternalAccessRulesResponse,
                    ) -> ListExternalAccessRulesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ExternalAccessRule = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: NetworkPolicy = ...,
                    networkPolicyId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def fetchExternalAddresses(
                    self,
                    *,
                    networkPolicy: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> FetchNetworkPolicyExternalAddressesResponseHttpRequest: ...
                def fetchExternalAddresses_next(
                    self,
                    previous_request: FetchNetworkPolicyExternalAddressesResponseHttpRequest,
                    previous_response: FetchNetworkPolicyExternalAddressesResponse,
                ) -> FetchNetworkPolicyExternalAddressesResponseHttpRequest | None: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> NetworkPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNetworkPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNetworkPoliciesResponseHttpRequest,
                    previous_response: ListNetworkPoliciesResponse,
                ) -> ListNetworkPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: NetworkPolicy = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def externalAccessRules(self) -> ExternalAccessRulesResource: ...

            @typing.type_check_only
            class NodeTypesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> NodeTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNodeTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNodeTypesResponseHttpRequest,
                    previous_response: ListNodeTypesResponse,
                ) -> ListNodeTypesResponseHttpRequest | None: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
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
            class PrivateCloudsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ClustersResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class NodesResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> NodeHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListNodesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListNodesResponseHttpRequest,
                            previous_response: ListNodesResponse,
                        ) -> ListNodesResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: Cluster = ...,
                        clusterId: str = ...,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ClusterHttpRequest: ...
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
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListClustersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListClustersResponseHttpRequest,
                        previous_response: ListClustersResponse,
                    ) -> ListClustersResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Cluster = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
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
                    def nodes(self) -> NodesResource: ...

                @typing.type_check_only
                class ExternalAddressesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ExternalAddress = ...,
                        externalAddressId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ExternalAddressHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListExternalAddressesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListExternalAddressesResponseHttpRequest,
                        previous_response: ListExternalAddressesResponse,
                    ) -> ListExternalAddressesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ExternalAddress = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class HcxActivationKeysResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: HcxActivationKey = ...,
                        hcxActivationKeyId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> HcxActivationKeyHttpRequest: ...
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
                    ) -> ListHcxActivationKeysResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListHcxActivationKeysResponseHttpRequest,
                        previous_response: ListHcxActivationKeysResponse,
                    ) -> ListHcxActivationKeysResponseHttpRequest | None: ...
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
                class LoggingServersResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: LoggingServer = ...,
                        loggingServerId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LoggingServerHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLoggingServersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLoggingServersResponseHttpRequest,
                        previous_response: ListLoggingServersResponse,
                    ) -> ListLoggingServersResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LoggingServer = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class ManagementDnsZoneBindingsResource(
                    googleapiclient.discovery.Resource
                ):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ManagementDnsZoneBinding = ...,
                        managementDnsZoneBindingId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ManagementDnsZoneBindingHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListManagementDnsZoneBindingsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListManagementDnsZoneBindingsResponseHttpRequest,
                        previous_response: ListManagementDnsZoneBindingsResponse,
                    ) -> ListManagementDnsZoneBindingsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ManagementDnsZoneBinding = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def repair(
                        self,
                        *,
                        name: str,
                        body: RepairManagementDnsZoneBindingRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class SubnetsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SubnetHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListSubnetsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListSubnetsResponseHttpRequest,
                        previous_response: ListSubnetsResponse,
                    ) -> ListSubnetsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Subnet = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: PrivateCloud = ...,
                    privateCloudId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    delayHours: int = ...,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PrivateCloudHttpRequest: ...
                def getDnsForwarding(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DnsForwardingHttpRequest: ...
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
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListPrivateCloudsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPrivateCloudsResponseHttpRequest,
                    previous_response: ListPrivateCloudsResponse,
                ) -> ListPrivateCloudsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: PrivateCloud = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def resetNsxCredentials(
                    self,
                    *,
                    privateCloud: str,
                    body: ResetNsxCredentialsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def resetVcenterCredentials(
                    self,
                    *,
                    privateCloud: str,
                    body: ResetVcenterCredentialsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def showNsxCredentials(
                    self, *, privateCloud: str, **kwargs: typing.Any
                ) -> CredentialsHttpRequest: ...
                def showVcenterCredentials(
                    self,
                    *,
                    privateCloud: str,
                    username: str = ...,
                    **kwargs: typing.Any,
                ) -> CredentialsHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeletePrivateCloudRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def updateDnsForwarding(
                    self,
                    *,
                    name: str,
                    body: DnsForwarding = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def clusters(self) -> ClustersResource: ...
                def externalAddresses(self) -> ExternalAddressesResource: ...
                def hcxActivationKeys(self) -> HcxActivationKeysResource: ...
                def loggingServers(self) -> LoggingServersResource: ...
                def managementDnsZoneBindings(
                    self,
                ) -> ManagementDnsZoneBindingsResource: ...
                def subnets(self) -> SubnetsResource: ...

            @typing.type_check_only
            class PrivateConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PeeringRoutesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPrivateConnectionPeeringRoutesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListPrivateConnectionPeeringRoutesResponseHttpRequest,
                        previous_response: ListPrivateConnectionPeeringRoutesResponse,
                    ) -> (
                        ListPrivateConnectionPeeringRoutesResponseHttpRequest | None
                    ): ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: PrivateConnection = ...,
                    privateConnectionId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PrivateConnectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListPrivateConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPrivateConnectionsResponseHttpRequest,
                    previous_response: ListPrivateConnectionsResponse,
                ) -> ListPrivateConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: PrivateConnection = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def peeringRoutes(self) -> PeeringRoutesResource: ...

            @typing.type_check_only
            class VmwareEngineNetworksResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: VmwareEngineNetwork = ...,
                    requestId: str = ...,
                    vmwareEngineNetworkId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    etag: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> VmwareEngineNetworkHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListVmwareEngineNetworksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListVmwareEngineNetworksResponseHttpRequest,
                    previous_response: ListVmwareEngineNetworksResponse,
                ) -> ListVmwareEngineNetworksResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: VmwareEngineNetwork = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getDnsBindPermission(
                self, *, name: str, **kwargs: typing.Any
            ) -> DnsBindPermissionHttpRequest: ...
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
            def dnsBindPermission(self) -> DnsBindPermissionResource: ...
            def networkPeerings(self) -> NetworkPeeringsResource: ...
            def networkPolicies(self) -> NetworkPoliciesResource: ...
            def nodeTypes(self) -> NodeTypesResource: ...
            def operations(self) -> OperationsResource: ...
            def privateClouds(self) -> PrivateCloudsResource: ...
            def privateConnections(self) -> PrivateConnectionsResource: ...
            def vmwareEngineNetworks(self) -> VmwareEngineNetworksResource: ...

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
class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Cluster: ...

@typing.type_check_only
class CredentialsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Credentials: ...

@typing.type_check_only
class DnsBindPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DnsBindPermission: ...

@typing.type_check_only
class DnsForwardingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DnsForwarding: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ExternalAccessRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExternalAccessRule: ...

@typing.type_check_only
class ExternalAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExternalAddress: ...

@typing.type_check_only
class FetchNetworkPolicyExternalAddressesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchNetworkPolicyExternalAddressesResponse: ...

@typing.type_check_only
class HcxActivationKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HcxActivationKey: ...

@typing.type_check_only
class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListClustersResponse: ...

@typing.type_check_only
class ListExternalAccessRulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExternalAccessRulesResponse: ...

@typing.type_check_only
class ListExternalAddressesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExternalAddressesResponse: ...

@typing.type_check_only
class ListHcxActivationKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListHcxActivationKeysResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListLoggingServersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLoggingServersResponse: ...

@typing.type_check_only
class ListManagementDnsZoneBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListManagementDnsZoneBindingsResponse: ...

@typing.type_check_only
class ListNetworkPeeringsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNetworkPeeringsResponse: ...

@typing.type_check_only
class ListNetworkPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNetworkPoliciesResponse: ...

@typing.type_check_only
class ListNodeTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNodeTypesResponse: ...

@typing.type_check_only
class ListNodesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNodesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPeeringRoutesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPeeringRoutesResponse: ...

@typing.type_check_only
class ListPrivateCloudsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPrivateCloudsResponse: ...

@typing.type_check_only
class ListPrivateConnectionPeeringRoutesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPrivateConnectionPeeringRoutesResponse: ...

@typing.type_check_only
class ListPrivateConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPrivateConnectionsResponse: ...

@typing.type_check_only
class ListSubnetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSubnetsResponse: ...

@typing.type_check_only
class ListVmwareEngineNetworksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVmwareEngineNetworksResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class LoggingServerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoggingServer: ...

@typing.type_check_only
class ManagementDnsZoneBindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ManagementDnsZoneBinding: ...

@typing.type_check_only
class NetworkPeeringHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NetworkPeering: ...

@typing.type_check_only
class NetworkPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NetworkPolicy: ...

@typing.type_check_only
class NodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Node: ...

@typing.type_check_only
class NodeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NodeType: ...

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
class PrivateCloudHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PrivateCloud: ...

@typing.type_check_only
class PrivateConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PrivateConnection: ...

@typing.type_check_only
class SubnetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subnet: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class VmwareEngineNetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VmwareEngineNetwork: ...
