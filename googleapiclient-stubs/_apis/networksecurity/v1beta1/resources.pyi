import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class NetworkSecurityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddressGroupsResource(googleapiclient.discovery.Resource):
                def addItems(
                    self,
                    *,
                    addressGroup: str,
                    body: AddAddressGroupItemsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def cloneItems(
                    self,
                    *,
                    addressGroup: str,
                    body: CloneAddressGroupItemsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: AddressGroup = ...,
                    addressGroupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AddressGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddressGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAddressGroupsResponseHttpRequest,
                    previous_response: ListAddressGroupsResponse,
                ) -> ListAddressGroupsResponseHttpRequest | None: ...
                def listReferences(
                    self,
                    *,
                    addressGroup: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddressGroupReferencesResponseHttpRequest: ...
                def listReferences_next(
                    self,
                    previous_request: ListAddressGroupReferencesResponseHttpRequest,
                    previous_response: ListAddressGroupReferencesResponse,
                ) -> ListAddressGroupReferencesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AddressGroup = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def removeItems(
                    self,
                    *,
                    addressGroup: str,
                    body: RemoveAddressGroupItemsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class FirewallEndpointsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: FirewallEndpoint = ...,
                    firewallEndpointId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FirewallEndpointHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListFirewallEndpointsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFirewallEndpointsResponseHttpRequest,
                    previous_response: ListFirewallEndpointsResponse,
                ) -> ListFirewallEndpointsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: FirewallEndpoint = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

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
            class SecurityProfileGroupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SecurityProfileGroup = ...,
                    securityProfileGroupId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SecurityProfileGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSecurityProfileGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSecurityProfileGroupsResponseHttpRequest,
                    previous_response: ListSecurityProfileGroupsResponse,
                ) -> ListSecurityProfileGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: SecurityProfileGroup = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class SecurityProfilesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: SecurityProfile = ...,
                    securityProfileId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SecurityProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSecurityProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSecurityProfilesResponseHttpRequest,
                    previous_response: ListSecurityProfilesResponse,
                ) -> ListSecurityProfilesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: SecurityProfile = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            def addressGroups(self) -> AddressGroupsResource: ...
            def firewallEndpoints(self) -> FirewallEndpointsResource: ...
            def operations(self) -> OperationsResource: ...
            def securityProfileGroups(self) -> SecurityProfileGroupsResource: ...
            def securityProfiles(self) -> SecurityProfilesResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddressGroupsResource(googleapiclient.discovery.Resource):
                def addItems(
                    self,
                    *,
                    addressGroup: str,
                    body: AddAddressGroupItemsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def cloneItems(
                    self,
                    *,
                    addressGroup: str,
                    body: CloneAddressGroupItemsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: AddressGroup = ...,
                    addressGroupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AddressGroupHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddressGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAddressGroupsResponseHttpRequest,
                    previous_response: ListAddressGroupsResponse,
                ) -> ListAddressGroupsResponseHttpRequest | None: ...
                def listReferences(
                    self,
                    *,
                    addressGroup: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAddressGroupReferencesResponseHttpRequest: ...
                def listReferences_next(
                    self,
                    previous_request: ListAddressGroupReferencesResponseHttpRequest,
                    previous_response: ListAddressGroupReferencesResponse,
                ) -> ListAddressGroupReferencesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AddressGroup = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def removeItems(
                    self,
                    *,
                    addressGroup: str,
                    body: RemoveAddressGroupItemsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
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
            class AuthorizationPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AuthorizationPolicy = ...,
                    authorizationPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuthorizationPolicyHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAuthorizationPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuthorizationPoliciesResponseHttpRequest,
                    previous_response: ListAuthorizationPoliciesResponse,
                ) -> ListAuthorizationPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AuthorizationPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
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
            class AuthzPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AuthzPolicy = ...,
                    authzPolicyId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AuthzPolicyHttpRequest: ...
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
                ) -> ListAuthzPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAuthzPoliciesResponseHttpRequest,
                    previous_response: ListAuthzPoliciesResponse,
                ) -> ListAuthzPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AuthzPolicy = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
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
            class ClientTlsPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ClientTlsPolicy = ...,
                    clientTlsPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ClientTlsPolicyHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListClientTlsPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClientTlsPoliciesResponseHttpRequest,
                    previous_response: ListClientTlsPoliciesResponse,
                ) -> ListClientTlsPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ClientTlsPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
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
            class FirewallEndpointAssociationsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: FirewallEndpointAssociation = ...,
                    firewallEndpointAssociationId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FirewallEndpointAssociationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListFirewallEndpointAssociationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFirewallEndpointAssociationsResponseHttpRequest,
                    previous_response: ListFirewallEndpointAssociationsResponse,
                ) -> ListFirewallEndpointAssociationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: FirewallEndpointAssociation = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class GatewaySecurityPoliciesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RulesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GatewaySecurityPolicyRule = ...,
                        gatewaySecurityPolicyRuleId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GatewaySecurityPolicyRuleHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListGatewaySecurityPolicyRulesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListGatewaySecurityPolicyRulesResponseHttpRequest,
                        previous_response: ListGatewaySecurityPolicyRulesResponse,
                    ) -> ListGatewaySecurityPolicyRulesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GatewaySecurityPolicyRule = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GatewaySecurityPolicy = ...,
                    gatewaySecurityPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GatewaySecurityPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListGatewaySecurityPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGatewaySecurityPoliciesResponseHttpRequest,
                    previous_response: ListGatewaySecurityPoliciesResponse,
                ) -> ListGatewaySecurityPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GatewaySecurityPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def rules(self) -> RulesResource: ...

            @typing.type_check_only
            class InterceptDeploymentGroupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: InterceptDeploymentGroup = ...,
                    interceptDeploymentGroupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InterceptDeploymentGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInterceptDeploymentGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInterceptDeploymentGroupsResponseHttpRequest,
                    previous_response: ListInterceptDeploymentGroupsResponse,
                ) -> ListInterceptDeploymentGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: InterceptDeploymentGroup = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class InterceptDeploymentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: InterceptDeployment = ...,
                    interceptDeploymentId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InterceptDeploymentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInterceptDeploymentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInterceptDeploymentsResponseHttpRequest,
                    previous_response: ListInterceptDeploymentsResponse,
                ) -> ListInterceptDeploymentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: InterceptDeployment = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class InterceptEndpointGroupAssociationsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: InterceptEndpointGroupAssociation = ...,
                    interceptEndpointGroupAssociationId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InterceptEndpointGroupAssociationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInterceptEndpointGroupAssociationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInterceptEndpointGroupAssociationsResponseHttpRequest,
                    previous_response: ListInterceptEndpointGroupAssociationsResponse,
                ) -> (
                    ListInterceptEndpointGroupAssociationsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: InterceptEndpointGroupAssociation = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class InterceptEndpointGroupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: InterceptEndpointGroup = ...,
                    interceptEndpointGroupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InterceptEndpointGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListInterceptEndpointGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListInterceptEndpointGroupsResponseHttpRequest,
                    previous_response: ListInterceptEndpointGroupsResponse,
                ) -> ListInterceptEndpointGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: InterceptEndpointGroup = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MirroringDeploymentGroupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: MirroringDeploymentGroup = ...,
                    mirroringDeploymentGroupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MirroringDeploymentGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListMirroringDeploymentGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMirroringDeploymentGroupsResponseHttpRequest,
                    previous_response: ListMirroringDeploymentGroupsResponse,
                ) -> ListMirroringDeploymentGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: MirroringDeploymentGroup = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MirroringDeploymentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: MirroringDeployment = ...,
                    mirroringDeploymentId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MirroringDeploymentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListMirroringDeploymentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMirroringDeploymentsResponseHttpRequest,
                    previous_response: ListMirroringDeploymentsResponse,
                ) -> ListMirroringDeploymentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: MirroringDeployment = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MirroringEndpointGroupAssociationsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: MirroringEndpointGroupAssociation = ...,
                    mirroringEndpointGroupAssociationId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MirroringEndpointGroupAssociationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListMirroringEndpointGroupAssociationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMirroringEndpointGroupAssociationsResponseHttpRequest,
                    previous_response: ListMirroringEndpointGroupAssociationsResponse,
                ) -> (
                    ListMirroringEndpointGroupAssociationsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: MirroringEndpointGroupAssociation = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class MirroringEndpointGroupsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: MirroringEndpointGroup = ...,
                    mirroringEndpointGroupId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MirroringEndpointGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListMirroringEndpointGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMirroringEndpointGroupsResponseHttpRequest,
                    previous_response: ListMirroringEndpointGroupsResponse,
                ) -> ListMirroringEndpointGroupsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: MirroringEndpointGroup = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

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
            class ServerTlsPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ServerTlsPolicy = ...,
                    serverTlsPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ServerTlsPolicyHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListServerTlsPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListServerTlsPoliciesResponseHttpRequest,
                    previous_response: ListServerTlsPoliciesResponse,
                ) -> ListServerTlsPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ServerTlsPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
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
            class TlsInspectionPoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: TlsInspectionPolicy = ...,
                    tlsInspectionPolicyId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TlsInspectionPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListTlsInspectionPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTlsInspectionPoliciesResponseHttpRequest,
                    previous_response: ListTlsInspectionPoliciesResponse,
                ) -> ListTlsInspectionPoliciesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TlsInspectionPolicy = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class UrlListsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: UrlList = ...,
                    urlListId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> UrlListHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListUrlListsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUrlListsResponseHttpRequest,
                    previous_response: ListUrlListsResponse,
                ) -> ListUrlListsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: UrlList = ...,
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
            def addressGroups(self) -> AddressGroupsResource: ...
            def authorizationPolicies(self) -> AuthorizationPoliciesResource: ...
            def authzPolicies(self) -> AuthzPoliciesResource: ...
            def clientTlsPolicies(self) -> ClientTlsPoliciesResource: ...
            def firewallEndpointAssociations(
                self,
            ) -> FirewallEndpointAssociationsResource: ...
            def gatewaySecurityPolicies(self) -> GatewaySecurityPoliciesResource: ...
            def interceptDeploymentGroups(
                self,
            ) -> InterceptDeploymentGroupsResource: ...
            def interceptDeployments(self) -> InterceptDeploymentsResource: ...
            def interceptEndpointGroupAssociations(
                self,
            ) -> InterceptEndpointGroupAssociationsResource: ...
            def interceptEndpointGroups(self) -> InterceptEndpointGroupsResource: ...
            def mirroringDeploymentGroups(
                self,
            ) -> MirroringDeploymentGroupsResource: ...
            def mirroringDeployments(self) -> MirroringDeploymentsResource: ...
            def mirroringEndpointGroupAssociations(
                self,
            ) -> MirroringEndpointGroupAssociationsResource: ...
            def mirroringEndpointGroups(self) -> MirroringEndpointGroupsResource: ...
            def operations(self) -> OperationsResource: ...
            def serverTlsPolicies(self) -> ServerTlsPoliciesResource: ...
            def tlsInspectionPolicies(self) -> TlsInspectionPoliciesResource: ...
            def urlLists(self) -> UrlListsResource: ...

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
class AddressGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddressGroup: ...

@typing.type_check_only
class AuthorizationPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuthorizationPolicy: ...

@typing.type_check_only
class AuthzPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuthzPolicy: ...

@typing.type_check_only
class ClientTlsPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ClientTlsPolicy: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FirewallEndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FirewallEndpoint: ...

@typing.type_check_only
class FirewallEndpointAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FirewallEndpointAssociation: ...

@typing.type_check_only
class GatewaySecurityPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GatewaySecurityPolicy: ...

@typing.type_check_only
class GatewaySecurityPolicyRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GatewaySecurityPolicyRule: ...

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
class InterceptDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InterceptDeployment: ...

@typing.type_check_only
class InterceptDeploymentGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InterceptDeploymentGroup: ...

@typing.type_check_only
class InterceptEndpointGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InterceptEndpointGroup: ...

@typing.type_check_only
class InterceptEndpointGroupAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InterceptEndpointGroupAssociation: ...

@typing.type_check_only
class ListAddressGroupReferencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAddressGroupReferencesResponse: ...

@typing.type_check_only
class ListAddressGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAddressGroupsResponse: ...

@typing.type_check_only
class ListAuthorizationPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuthorizationPoliciesResponse: ...

@typing.type_check_only
class ListAuthzPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAuthzPoliciesResponse: ...

@typing.type_check_only
class ListClientTlsPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListClientTlsPoliciesResponse: ...

@typing.type_check_only
class ListFirewallEndpointAssociationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFirewallEndpointAssociationsResponse: ...

@typing.type_check_only
class ListFirewallEndpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFirewallEndpointsResponse: ...

@typing.type_check_only
class ListGatewaySecurityPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGatewaySecurityPoliciesResponse: ...

@typing.type_check_only
class ListGatewaySecurityPolicyRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGatewaySecurityPolicyRulesResponse: ...

@typing.type_check_only
class ListInterceptDeploymentGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInterceptDeploymentGroupsResponse: ...

@typing.type_check_only
class ListInterceptDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInterceptDeploymentsResponse: ...

@typing.type_check_only
class ListInterceptEndpointGroupAssociationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInterceptEndpointGroupAssociationsResponse: ...

@typing.type_check_only
class ListInterceptEndpointGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInterceptEndpointGroupsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMirroringDeploymentGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMirroringDeploymentGroupsResponse: ...

@typing.type_check_only
class ListMirroringDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMirroringDeploymentsResponse: ...

@typing.type_check_only
class ListMirroringEndpointGroupAssociationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMirroringEndpointGroupAssociationsResponse: ...

@typing.type_check_only
class ListMirroringEndpointGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMirroringEndpointGroupsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListSecurityProfileGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSecurityProfileGroupsResponse: ...

@typing.type_check_only
class ListSecurityProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSecurityProfilesResponse: ...

@typing.type_check_only
class ListServerTlsPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListServerTlsPoliciesResponse: ...

@typing.type_check_only
class ListTlsInspectionPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTlsInspectionPoliciesResponse: ...

@typing.type_check_only
class ListUrlListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUrlListsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class MirroringDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MirroringDeployment: ...

@typing.type_check_only
class MirroringDeploymentGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MirroringDeploymentGroup: ...

@typing.type_check_only
class MirroringEndpointGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MirroringEndpointGroup: ...

@typing.type_check_only
class MirroringEndpointGroupAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MirroringEndpointGroupAssociation: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class SecurityProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SecurityProfile: ...

@typing.type_check_only
class SecurityProfileGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SecurityProfileGroup: ...

@typing.type_check_only
class ServerTlsPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServerTlsPolicy: ...

@typing.type_check_only
class TlsInspectionPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TlsInspectionPolicy: ...

@typing.type_check_only
class UrlListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UrlList: ...
