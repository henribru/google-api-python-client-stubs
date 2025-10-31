import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddAddressGroupItemsRequest(typing_extensions.TypedDict, total=False):
    items: _list[str]
    requestId: str

@typing.type_check_only
class AddressGroup(typing_extensions.TypedDict, total=False):
    capacity: int
    createTime: str
    description: str
    items: _list[str]
    labels: dict[str, typing.Any]
    name: str
    purpose: _list[
        typing_extensions.Literal["PURPOSE_UNSPECIFIED", "DEFAULT", "CLOUD_ARMOR"]
    ]
    selfLink: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "IPV4", "IPV6"]
    updateTime: str

@typing.type_check_only
class AntivirusOverride(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "THREAT_ACTION_UNSPECIFIED", "DEFAULT_ACTION", "ALLOW", "ALERT", "DENY"
    ]
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "SMTP", "SMB", "POP3", "IMAP", "HTTP2", "HTTP", "FTP"
    ]

@typing.type_check_only
class AuthorizationPolicy(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    rules: _list[Rule]
    updateTime: str

@typing.type_check_only
class AuthzPolicy(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "AUTHZ_ACTION_UNSPECIFIED", "ALLOW", "DENY", "CUSTOM"
    ]
    createTime: str
    customProvider: AuthzPolicyCustomProvider
    description: str
    httpRules: _list[AuthzPolicyAuthzRule]
    labels: dict[str, typing.Any]
    name: str
    target: AuthzPolicyTarget
    updateTime: str

AlternativeAuthzPolicyAuthzRule = typing_extensions.TypedDict(
    "AlternativeAuthzPolicyAuthzRule",
    {
        "from": AuthzPolicyAuthzRuleFrom,
        "to": AuthzPolicyAuthzRuleTo,
        "when": str,
    },
    total=False,
)

@typing.type_check_only
class AuthzPolicyAuthzRule(AlternativeAuthzPolicyAuthzRule): ...

@typing.type_check_only
class AuthzPolicyAuthzRuleFrom(typing_extensions.TypedDict, total=False):
    notSources: _list[AuthzPolicyAuthzRuleFromRequestSource]
    sources: _list[AuthzPolicyAuthzRuleFromRequestSource]

@typing.type_check_only
class AuthzPolicyAuthzRuleFromRequestSource(typing_extensions.TypedDict, total=False):
    ipBlocks: _list[AuthzPolicyAuthzRuleIpBlock]
    principals: _list[AuthzPolicyAuthzRulePrincipal]
    resources: _list[AuthzPolicyAuthzRuleRequestResource]

@typing.type_check_only
class AuthzPolicyAuthzRuleHeaderMatch(typing_extensions.TypedDict, total=False):
    name: str
    value: AuthzPolicyAuthzRuleStringMatch

@typing.type_check_only
class AuthzPolicyAuthzRuleIpBlock(typing_extensions.TypedDict, total=False):
    length: int
    prefix: str

@typing.type_check_only
class AuthzPolicyAuthzRulePrincipal(typing_extensions.TypedDict, total=False):
    principal: AuthzPolicyAuthzRuleStringMatch
    principalSelector: typing_extensions.Literal[
        "PRINCIPAL_SELECTOR_UNSPECIFIED",
        "CLIENT_CERT_URI_SAN",
        "CLIENT_CERT_DNS_NAME_SAN",
        "CLIENT_CERT_COMMON_NAME",
    ]

@typing.type_check_only
class AuthzPolicyAuthzRuleRequestResource(typing_extensions.TypedDict, total=False):
    iamServiceAccount: AuthzPolicyAuthzRuleStringMatch
    tagValueIdSet: AuthzPolicyAuthzRuleRequestResourceTagValueIdSet

@typing.type_check_only
class AuthzPolicyAuthzRuleRequestResourceTagValueIdSet(
    typing_extensions.TypedDict, total=False
):
    ids: _list[str]

@typing.type_check_only
class AuthzPolicyAuthzRuleStringMatch(typing_extensions.TypedDict, total=False):
    contains: str
    exact: str
    ignoreCase: bool
    prefix: str
    suffix: str

@typing.type_check_only
class AuthzPolicyAuthzRuleTo(typing_extensions.TypedDict, total=False):
    notOperations: _list[AuthzPolicyAuthzRuleToRequestOperation]
    operations: _list[AuthzPolicyAuthzRuleToRequestOperation]

@typing.type_check_only
class AuthzPolicyAuthzRuleToRequestOperation(typing_extensions.TypedDict, total=False):
    headerSet: AuthzPolicyAuthzRuleToRequestOperationHeaderSet
    hosts: _list[AuthzPolicyAuthzRuleStringMatch]
    methods: _list[str]
    paths: _list[AuthzPolicyAuthzRuleStringMatch]

@typing.type_check_only
class AuthzPolicyAuthzRuleToRequestOperationHeaderSet(
    typing_extensions.TypedDict, total=False
):
    headers: _list[AuthzPolicyAuthzRuleHeaderMatch]

@typing.type_check_only
class AuthzPolicyCustomProvider(typing_extensions.TypedDict, total=False):
    authzExtension: AuthzPolicyCustomProviderAuthzExtension
    cloudIap: AuthzPolicyCustomProviderCloudIap

@typing.type_check_only
class AuthzPolicyCustomProviderAuthzExtension(typing_extensions.TypedDict, total=False):
    resources: _list[str]

@typing.type_check_only
class AuthzPolicyCustomProviderCloudIap(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AuthzPolicyTarget(typing_extensions.TypedDict, total=False):
    loadBalancingScheme: typing_extensions.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED",
        "INTERNAL_MANAGED",
        "EXTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
    ]
    resources: _list[str]

@typing.type_check_only
class BackendAuthenticationConfig(typing_extensions.TypedDict, total=False):
    clientCertificate: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    trustConfig: str
    updateTime: str
    wellKnownRoots: typing_extensions.Literal[
        "WELL_KNOWN_ROOTS_UNSPECIFIED", "NONE", "PUBLIC_ROOTS"
    ]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CertificateProviderInstance(typing_extensions.TypedDict, total=False):
    pluginInstance: str

@typing.type_check_only
class ClientTlsPolicy(typing_extensions.TypedDict, total=False):
    clientCertificate: GoogleCloudNetworksecurityV1CertificateProvider
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    serverValidationCa: _list[ValidationCA]
    sni: str
    updateTime: str

@typing.type_check_only
class CloneAddressGroupItemsRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    sourceAddressGroup: str

@typing.type_check_only
class CustomInterceptProfile(typing_extensions.TypedDict, total=False):
    interceptEndpointGroup: str

@typing.type_check_only
class CustomMirroringProfile(typing_extensions.TypedDict, total=False):
    mirroringEndpointGroup: str

@typing.type_check_only
class Destination(typing_extensions.TypedDict, total=False):
    hosts: _list[str]
    httpHeaderMatch: HttpHeaderMatch
    methods: _list[str]
    ports: _list[int]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FirewallEndpoint(typing_extensions.TypedDict, total=False):
    associatedNetworks: _list[str]
    associations: _list[FirewallEndpointAssociationReference]
    billingProjectId: str
    createTime: str
    description: str
    endpointSettings: FirewallEndpointEndpointSettings
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE"
    ]
    updateTime: str

@typing.type_check_only
class FirewallEndpointAssociation(typing_extensions.TypedDict, total=False):
    createTime: str
    disabled: bool
    firewallEndpoint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE", "ORPHAN"
    ]
    tlsInspectionPolicy: str
    updateTime: str

@typing.type_check_only
class FirewallEndpointAssociationReference(typing_extensions.TypedDict, total=False):
    name: str
    network: str

@typing.type_check_only
class FirewallEndpointEndpointSettings(typing_extensions.TypedDict, total=False):
    jumboFramesEnabled: bool

@typing.type_check_only
class GatewaySecurityPolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    tlsInspectionPolicy: str
    updateTime: str

@typing.type_check_only
class GatewaySecurityPolicyRule(typing_extensions.TypedDict, total=False):
    applicationMatcher: str
    basicProfile: typing_extensions.Literal[
        "BASIC_PROFILE_UNSPECIFIED", "ALLOW", "DENY"
    ]
    createTime: str
    description: str
    enabled: bool
    name: str
    priority: int
    sessionMatcher: str
    tlsInspectionEnabled: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudNetworksecurityV1CertificateProvider(
    typing_extensions.TypedDict, total=False
):
    certificateProviderInstance: CertificateProviderInstance
    grpcEndpoint: GoogleCloudNetworksecurityV1GrpcEndpoint

@typing.type_check_only
class GoogleCloudNetworksecurityV1GrpcEndpoint(
    typing_extensions.TypedDict, total=False
):
    targetUri: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class HttpHeaderMatch(typing_extensions.TypedDict, total=False):
    headerName: str
    regexMatch: str

@typing.type_check_only
class InterceptDeployment(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    forwardingRule: str
    interceptDeploymentGroup: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class InterceptDeploymentGroup(typing_extensions.TypedDict, total=False):
    connectedEndpointGroups: _list[InterceptDeploymentGroupConnectedEndpointGroup]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    locations: _list[InterceptLocation]
    name: str
    nestedDeployments: _list[InterceptDeploymentGroupDeployment]
    network: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING"
    ]
    updateTime: str

@typing.type_check_only
class InterceptDeploymentGroupConnectedEndpointGroup(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class InterceptDeploymentGroupDeployment(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class InterceptEndpointGroup(typing_extensions.TypedDict, total=False):
    associations: _list[InterceptEndpointGroupAssociationDetails]
    connectedDeploymentGroup: InterceptEndpointGroupConnectedDeploymentGroup
    createTime: str
    description: str
    interceptDeploymentGroup: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CLOSED",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class InterceptEndpointGroupAssociation(typing_extensions.TypedDict, total=False):
    createTime: str
    interceptEndpointGroup: str
    labels: dict[str, typing.Any]
    locations: _list[InterceptLocation]
    locationsDetails: _list[InterceptEndpointGroupAssociationLocationDetails]
    name: str
    network: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "CLOSED",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class InterceptEndpointGroupAssociationDetails(
    typing_extensions.TypedDict, total=False
):
    name: str
    network: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "CLOSED",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class InterceptEndpointGroupAssociationLocationDetails(
    typing_extensions.TypedDict, total=False
):
    location: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class InterceptEndpointGroupConnectedDeploymentGroup(
    typing_extensions.TypedDict, total=False
):
    locations: _list[InterceptLocation]
    name: str

@typing.type_check_only
class InterceptLocation(typing_extensions.TypedDict, total=False):
    location: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class ListAddressGroupReferencesResponse(typing_extensions.TypedDict, total=False):
    addressGroupReferences: _list[
        ListAddressGroupReferencesResponseAddressGroupReference
    ]
    nextPageToken: str

@typing.type_check_only
class ListAddressGroupReferencesResponseAddressGroupReference(
    typing_extensions.TypedDict, total=False
):
    firewallPolicy: str
    rulePriority: int
    securityPolicy: str

@typing.type_check_only
class ListAddressGroupsResponse(typing_extensions.TypedDict, total=False):
    addressGroups: _list[AddressGroup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthorizationPoliciesResponse(typing_extensions.TypedDict, total=False):
    authorizationPolicies: _list[AuthorizationPolicy]
    nextPageToken: str

@typing.type_check_only
class ListAuthzPoliciesResponse(typing_extensions.TypedDict, total=False):
    authzPolicies: _list[AuthzPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackendAuthenticationConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    backendAuthenticationConfigs: _list[BackendAuthenticationConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClientTlsPoliciesResponse(typing_extensions.TypedDict, total=False):
    clientTlsPolicies: _list[ClientTlsPolicy]
    nextPageToken: str

@typing.type_check_only
class ListFirewallEndpointAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    firewallEndpointAssociations: _list[FirewallEndpointAssociation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFirewallEndpointsResponse(typing_extensions.TypedDict, total=False):
    firewallEndpoints: _list[FirewallEndpoint]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewaySecurityPoliciesResponse(typing_extensions.TypedDict, total=False):
    gatewaySecurityPolicies: _list[GatewaySecurityPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewaySecurityPolicyRulesResponse(typing_extensions.TypedDict, total=False):
    gatewaySecurityPolicyRules: _list[GatewaySecurityPolicyRule]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInterceptDeploymentGroupsResponse(typing_extensions.TypedDict, total=False):
    interceptDeploymentGroups: _list[InterceptDeploymentGroup]
    nextPageToken: str

@typing.type_check_only
class ListInterceptDeploymentsResponse(typing_extensions.TypedDict, total=False):
    interceptDeployments: _list[InterceptDeployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInterceptEndpointGroupAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    interceptEndpointGroupAssociations: _list[InterceptEndpointGroupAssociation]
    nextPageToken: str

@typing.type_check_only
class ListInterceptEndpointGroupsResponse(typing_extensions.TypedDict, total=False):
    interceptEndpointGroups: _list[InterceptEndpointGroup]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMirroringDeploymentGroupsResponse(typing_extensions.TypedDict, total=False):
    mirroringDeploymentGroups: _list[MirroringDeploymentGroup]
    nextPageToken: str

@typing.type_check_only
class ListMirroringDeploymentsResponse(typing_extensions.TypedDict, total=False):
    mirroringDeployments: _list[MirroringDeployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMirroringEndpointGroupAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    mirroringEndpointGroupAssociations: _list[MirroringEndpointGroupAssociation]
    nextPageToken: str

@typing.type_check_only
class ListMirroringEndpointGroupsResponse(typing_extensions.TypedDict, total=False):
    mirroringEndpointGroups: _list[MirroringEndpointGroup]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListSecurityProfileGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    securityProfileGroups: _list[SecurityProfileGroup]

@typing.type_check_only
class ListSecurityProfilesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    securityProfiles: _list[SecurityProfile]

@typing.type_check_only
class ListServerTlsPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serverTlsPolicies: _list[ServerTlsPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListTlsInspectionPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tlsInspectionPolicies: _list[TlsInspectionPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListUrlListsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    urlLists: _list[UrlList]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MTLSPolicy(typing_extensions.TypedDict, total=False):
    clientValidationCa: _list[ValidationCA]
    clientValidationMode: typing_extensions.Literal[
        "CLIENT_VALIDATION_MODE_UNSPECIFIED",
        "ALLOW_INVALID_OR_MISSING_CLIENT_CERT",
        "REJECT_INVALID",
    ]
    clientValidationTrustConfig: str

@typing.type_check_only
class MirroringDeployment(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    forwardingRule: str
    labels: dict[str, typing.Any]
    mirroringDeploymentGroup: str
    name: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class MirroringDeploymentGroup(typing_extensions.TypedDict, total=False):
    connectedEndpointGroups: _list[MirroringDeploymentGroupConnectedEndpointGroup]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    locations: _list[MirroringLocation]
    name: str
    nestedDeployments: _list[MirroringDeploymentGroupDeployment]
    network: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "CLOSED"
    ]
    updateTime: str

@typing.type_check_only
class MirroringDeploymentGroupConnectedEndpointGroup(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class MirroringDeploymentGroupDeployment(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class MirroringEndpointGroup(typing_extensions.TypedDict, total=False):
    associations: _list[MirroringEndpointGroupAssociationDetails]
    connectedDeploymentGroups: _list[MirroringEndpointGroupConnectedDeploymentGroup]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    mirroringDeploymentGroup: str
    name: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CLOSED",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class MirroringEndpointGroupAssociation(typing_extensions.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    locations: _list[MirroringLocation]
    locationsDetails: _list[MirroringEndpointGroupAssociationLocationDetails]
    mirroringEndpointGroup: str
    name: str
    network: str
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "CLOSED",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class MirroringEndpointGroupAssociationDetails(
    typing_extensions.TypedDict, total=False
):
    name: str
    network: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "CLOSED",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class MirroringEndpointGroupAssociationLocationDetails(
    typing_extensions.TypedDict, total=False
):
    location: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class MirroringEndpointGroupConnectedDeploymentGroup(
    typing_extensions.TypedDict, total=False
):
    locations: _list[MirroringLocation]
    name: str

@typing.type_check_only
class MirroringLocation(typing_extensions.TypedDict, total=False):
    location: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class RemoveAddressGroupItemsRequest(typing_extensions.TypedDict, total=False):
    items: _list[str]
    requestId: str

@typing.type_check_only
class Rule(typing_extensions.TypedDict, total=False):
    destinations: _list[Destination]
    sources: _list[Source]

@typing.type_check_only
class SecurityProfile(typing_extensions.TypedDict, total=False):
    createTime: str
    customInterceptProfile: CustomInterceptProfile
    customMirroringProfile: CustomMirroringProfile
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    threatPreventionProfile: ThreatPreventionProfile
    type: typing_extensions.Literal[
        "PROFILE_TYPE_UNSPECIFIED",
        "THREAT_PREVENTION",
        "CUSTOM_MIRRORING",
        "CUSTOM_INTERCEPT",
    ]
    updateTime: str

@typing.type_check_only
class SecurityProfileGroup(typing_extensions.TypedDict, total=False):
    createTime: str
    customInterceptProfile: str
    customMirroringProfile: str
    dataPathId: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    threatPreventionProfile: str
    updateTime: str

@typing.type_check_only
class ServerTlsPolicy(typing_extensions.TypedDict, total=False):
    allowOpen: bool
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    mtlsPolicy: MTLSPolicy
    name: str
    serverCertificate: GoogleCloudNetworksecurityV1CertificateProvider
    updateTime: str

@typing.type_check_only
class SeverityOverride(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "THREAT_ACTION_UNSPECIFIED", "DEFAULT_ACTION", "ALLOW", "ALERT", "DENY"
    ]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    ipBlocks: _list[str]
    principals: _list[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ThreatOverride(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "THREAT_ACTION_UNSPECIFIED", "DEFAULT_ACTION", "ALLOW", "ALERT", "DENY"
    ]
    threatId: str
    type: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "UNKNOWN",
        "VULNERABILITY",
        "ANTIVIRUS",
        "SPYWARE",
        "DNS",
    ]

@typing.type_check_only
class ThreatPreventionProfile(typing_extensions.TypedDict, total=False):
    antivirusOverrides: _list[AntivirusOverride]
    severityOverrides: _list[SeverityOverride]
    threatOverrides: _list[ThreatOverride]

@typing.type_check_only
class TlsInspectionPolicy(typing_extensions.TypedDict, total=False):
    caPool: str
    createTime: str
    customTlsFeatures: _list[str]
    description: str
    excludePublicCaSet: bool
    minTlsVersion: typing_extensions.Literal[
        "TLS_VERSION_UNSPECIFIED", "TLS_1_0", "TLS_1_1", "TLS_1_2", "TLS_1_3"
    ]
    name: str
    tlsFeatureProfile: typing_extensions.Literal[
        "PROFILE_UNSPECIFIED",
        "PROFILE_COMPATIBLE",
        "PROFILE_MODERN",
        "PROFILE_RESTRICTED",
        "PROFILE_CUSTOM",
    ]
    trustConfig: str
    updateTime: str

@typing.type_check_only
class UrlList(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    updateTime: str
    values: _list[str]

@typing.type_check_only
class ValidationCA(typing_extensions.TypedDict, total=False):
    certificateProviderInstance: CertificateProviderInstance
    grpcEndpoint: GoogleCloudNetworksecurityV1GrpcEndpoint
