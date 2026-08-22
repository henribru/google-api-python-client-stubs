import typing

_list = list

@typing.type_check_only
class AddAddressGroupItemsRequest(typing.TypedDict, total=False):
    items: _list[str]
    requestId: str

@typing.type_check_only
class AddressGroup(typing.TypedDict, total=False):
    capacity: int
    createTime: str
    description: str
    items: _list[str]
    labels: dict[str, typing.Any]
    name: str
    purpose: _list[typing.Literal["PURPOSE_UNSPECIFIED", "DEFAULT", "CLOUD_ARMOR"]]
    selfLink: str
    type: typing.Literal["TYPE_UNSPECIFIED", "IPV4", "IPV6"]
    updateTime: str

@typing.type_check_only
class AntivirusOverride(typing.TypedDict, total=False):
    action: typing.Literal[
        "THREAT_ACTION_UNSPECIFIED", "DEFAULT_ACTION", "ALLOW", "ALERT", "DENY"
    ]
    protocol: typing.Literal[
        "PROTOCOL_UNSPECIFIED", "SMTP", "SMB", "POP3", "IMAP", "HTTP2", "HTTP", "FTP"
    ]

@typing.type_check_only
class AuthorizationPolicy(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    rules: _list[Rule]
    updateTime: str

@typing.type_check_only
class AuthzPolicy(typing.TypedDict, total=False):
    action: typing.Literal["AUTHZ_ACTION_UNSPECIFIED", "ALLOW", "DENY", "CUSTOM"]
    createTime: str
    customProvider: AuthzPolicyCustomProvider
    description: str
    httpRules: _list[AuthzPolicyAuthzRule]
    labels: dict[str, typing.Any]
    name: str
    networkRules: _list[AuthzPolicyAuthzRule]
    policyProfile: typing.Literal[
        "POLICY_PROFILE_UNSPECIFIED", "REQUEST_AUTHZ", "CONTENT_AUTHZ"
    ]
    target: AuthzPolicyTarget
    updateTime: str

AlternativeAuthzPolicyAuthzRule = typing.TypedDict(
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
class AuthzPolicyAuthzRuleFrom(typing.TypedDict, total=False):
    notSources: _list[AuthzPolicyAuthzRuleFromRequestSource]
    sources: _list[AuthzPolicyAuthzRuleFromRequestSource]

@typing.type_check_only
class AuthzPolicyAuthzRuleFromRequestSource(typing.TypedDict, total=False):
    ipBlocks: _list[AuthzPolicyAuthzRuleIpBlock]
    principals: _list[AuthzPolicyAuthzRulePrincipal]
    resources: _list[AuthzPolicyAuthzRuleRequestResource]

@typing.type_check_only
class AuthzPolicyAuthzRuleHeaderMatch(typing.TypedDict, total=False):
    name: str
    value: AuthzPolicyAuthzRuleStringMatch

@typing.type_check_only
class AuthzPolicyAuthzRuleIpBlock(typing.TypedDict, total=False):
    length: int
    prefix: str

@typing.type_check_only
class AuthzPolicyAuthzRulePrincipal(typing.TypedDict, total=False):
    principal: AuthzPolicyAuthzRuleStringMatch
    principalSelector: typing.Literal[
        "PRINCIPAL_SELECTOR_UNSPECIFIED",
        "CLIENT_CERT_URI_SAN",
        "CLIENT_CERT_DNS_NAME_SAN",
        "CLIENT_CERT_COMMON_NAME",
    ]

@typing.type_check_only
class AuthzPolicyAuthzRuleRequestResource(typing.TypedDict, total=False):
    iamServiceAccount: AuthzPolicyAuthzRuleStringMatch
    tagValueIdSet: AuthzPolicyAuthzRuleRequestResourceTagValueIdSet

@typing.type_check_only
class AuthzPolicyAuthzRuleRequestResourceTagValueIdSet(typing.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class AuthzPolicyAuthzRuleStringMatch(typing.TypedDict, total=False):
    contains: str
    exact: str
    ignoreCase: bool
    prefix: str
    suffix: str

@typing.type_check_only
class AuthzPolicyAuthzRuleTo(typing.TypedDict, total=False):
    notOperations: _list[AuthzPolicyAuthzRuleToRequestOperation]
    operations: _list[AuthzPolicyAuthzRuleToRequestOperation]

@typing.type_check_only
class AuthzPolicyAuthzRuleToRequestOperation(typing.TypedDict, total=False):
    headerSet: AuthzPolicyAuthzRuleToRequestOperationHeaderSet
    hosts: _list[AuthzPolicyAuthzRuleStringMatch]
    mcp: AuthzPolicyAuthzRuleToRequestOperationMCP
    methods: _list[str]
    paths: _list[AuthzPolicyAuthzRuleStringMatch]
    snis: _list[AuthzPolicyAuthzRuleStringMatch]

@typing.type_check_only
class AuthzPolicyAuthzRuleToRequestOperationHeaderSet(typing.TypedDict, total=False):
    headers: _list[AuthzPolicyAuthzRuleHeaderMatch]

@typing.type_check_only
class AuthzPolicyAuthzRuleToRequestOperationMCP(typing.TypedDict, total=False):
    baseProtocolMethodsOption: typing.Literal[
        "BASE_PROTOCOL_METHODS_OPTION_UNSPECIFIED",
        "SKIP_BASE_PROTOCOL_METHODS",
        "MATCH_BASE_PROTOCOL_METHODS",
    ]
    methods: _list[AuthzPolicyAuthzRuleToRequestOperationMCPMethod]

@typing.type_check_only
class AuthzPolicyAuthzRuleToRequestOperationMCPMethod(typing.TypedDict, total=False):
    name: str
    params: _list[AuthzPolicyAuthzRuleStringMatch]

@typing.type_check_only
class AuthzPolicyCustomProvider(typing.TypedDict, total=False):
    authzExtension: AuthzPolicyCustomProviderAuthzExtension
    cloudIap: AuthzPolicyCustomProviderCloudIap

@typing.type_check_only
class AuthzPolicyCustomProviderAuthzExtension(typing.TypedDict, total=False):
    resources: _list[str]

@typing.type_check_only
class AuthzPolicyCustomProviderCloudIap(typing.TypedDict, total=False): ...

@typing.type_check_only
class AuthzPolicyTarget(typing.TypedDict, total=False):
    loadBalancingScheme: typing.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED",
        "INTERNAL_MANAGED",
        "EXTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
    ]
    resources: _list[str]

@typing.type_check_only
class BackendAuthenticationConfig(typing.TypedDict, total=False):
    clientCertificate: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    trustConfig: str
    updateTime: str
    wellKnownRoots: typing.Literal[
        "WELL_KNOWN_ROOTS_UNSPECIFIED", "NONE", "PUBLIC_ROOTS"
    ]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CertificateProviderInstance(typing.TypedDict, total=False):
    pluginInstance: str

@typing.type_check_only
class ClientTlsPolicy(typing.TypedDict, total=False):
    clientCertificate: GoogleCloudNetworksecurityV1CertificateProvider
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    serverValidationCa: _list[ValidationCA]
    sni: str
    updateTime: str

@typing.type_check_only
class CloneAddressGroupItemsRequest(typing.TypedDict, total=False):
    requestId: str
    sourceAddressGroup: str

@typing.type_check_only
class CustomInterceptProfile(typing.TypedDict, total=False):
    interceptEndpointGroup: str

@typing.type_check_only
class CustomMirroringProfile(typing.TypedDict, total=False):
    mirroringEndpointGroup: str

@typing.type_check_only
class Destination(typing.TypedDict, total=False):
    hosts: _list[str]
    httpHeaderMatch: HttpHeaderMatch
    methods: _list[str]
    ports: _list[int]

@typing.type_check_only
class DnsThreatDetector(typing.TypedDict, total=False):
    createTime: str
    excludedNetworks: _list[str]
    labels: dict[str, typing.Any]
    name: str
    provider: typing.Literal["PROVIDER_UNSPECIFIED", "INFOBLOX"]
    updateTime: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FirewallEndpoint(typing.TypedDict, total=False):
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
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE"
    ]
    updateTime: str

@typing.type_check_only
class FirewallEndpointAssociation(typing.TypedDict, total=False):
    createTime: str
    disabled: bool
    firewallEndpoint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "INACTIVE", "ORPHAN"
    ]
    tlsInspectionPolicy: str
    updateTime: str

@typing.type_check_only
class FirewallEndpointAssociationReference(typing.TypedDict, total=False):
    name: str
    network: str

@typing.type_check_only
class FirewallEndpointEndpointSettings(typing.TypedDict, total=False):
    jumboFramesEnabled: bool

@typing.type_check_only
class GatewaySecurityPolicy(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    tlsInspectionPolicy: str
    updateTime: str

@typing.type_check_only
class GatewaySecurityPolicyRule(typing.TypedDict, total=False):
    applicationMatcher: str
    basicProfile: typing.Literal["BASIC_PROFILE_UNSPECIFIED", "ALLOW", "DENY"]
    createTime: str
    description: str
    enabled: bool
    name: str
    priority: int
    sessionMatcher: str
    tlsInspectionEnabled: bool
    updateTime: str

@typing.type_check_only
class GoogleCloudNetworksecurityV1CertificateProvider(typing.TypedDict, total=False):
    certificateProviderInstance: CertificateProviderInstance
    grpcEndpoint: GoogleCloudNetworksecurityV1GrpcEndpoint

@typing.type_check_only
class GoogleCloudNetworksecurityV1GrpcEndpoint(typing.TypedDict, total=False):
    targetUri: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class HttpHeaderMatch(typing.TypedDict, total=False):
    headerName: str
    regexMatch: str

@typing.type_check_only
class InterceptDeployment(typing.TypedDict, total=False):
    createTime: str
    description: str
    forwardingRule: str
    interceptDeploymentGroup: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class InterceptDeploymentGroup(typing.TypedDict, total=False):
    connectedEndpointGroups: _list[InterceptDeploymentGroupConnectedEndpointGroup]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    locations: _list[InterceptLocation]
    name: str
    nestedDeployments: _list[InterceptDeploymentGroupDeployment]
    network: str
    reconciling: bool
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING"]
    updateTime: str

@typing.type_check_only
class InterceptDeploymentGroupConnectedEndpointGroup(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class InterceptDeploymentGroupDeployment(typing.TypedDict, total=False):
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class InterceptEndpointGroup(typing.TypedDict, total=False):
    associations: _list[InterceptEndpointGroupAssociationDetails]
    connectedDeploymentGroup: InterceptEndpointGroupConnectedDeploymentGroup
    createTime: str
    description: str
    interceptDeploymentGroup: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    state: typing.Literal[
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
class InterceptEndpointGroupAssociation(typing.TypedDict, total=False):
    createTime: str
    interceptEndpointGroup: str
    labels: dict[str, typing.Any]
    locations: _list[InterceptLocation]
    locationsDetails: _list[InterceptEndpointGroupAssociationLocationDetails]
    name: str
    network: str
    networkCookie: int
    reconciling: bool
    state: typing.Literal[
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
class InterceptEndpointGroupAssociationDetails(typing.TypedDict, total=False):
    name: str
    network: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "CLOSED",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class InterceptEndpointGroupAssociationLocationDetails(typing.TypedDict, total=False):
    location: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class InterceptEndpointGroupConnectedDeploymentGroup(typing.TypedDict, total=False):
    locations: _list[InterceptLocation]
    name: str

@typing.type_check_only
class InterceptLocation(typing.TypedDict, total=False):
    location: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class ListAddressGroupReferencesResponse(typing.TypedDict, total=False):
    addressGroupReferences: _list[
        ListAddressGroupReferencesResponseAddressGroupReference
    ]
    nextPageToken: str

@typing.type_check_only
class ListAddressGroupReferencesResponseAddressGroupReference(
    typing.TypedDict, total=False
):
    firewallPolicy: str
    rulePriority: int
    securityPolicy: str

@typing.type_check_only
class ListAddressGroupsResponse(typing.TypedDict, total=False):
    addressGroups: _list[AddressGroup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthorizationPoliciesResponse(typing.TypedDict, total=False):
    authorizationPolicies: _list[AuthorizationPolicy]
    nextPageToken: str

@typing.type_check_only
class ListAuthzPoliciesResponse(typing.TypedDict, total=False):
    authzPolicies: _list[AuthzPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackendAuthenticationConfigsResponse(typing.TypedDict, total=False):
    backendAuthenticationConfigs: _list[BackendAuthenticationConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClientTlsPoliciesResponse(typing.TypedDict, total=False):
    clientTlsPolicies: _list[ClientTlsPolicy]
    nextPageToken: str

@typing.type_check_only
class ListDnsThreatDetectorsResponse(typing.TypedDict, total=False):
    dnsThreatDetectors: _list[DnsThreatDetector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFirewallEndpointAssociationsResponse(typing.TypedDict, total=False):
    firewallEndpointAssociations: _list[FirewallEndpointAssociation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFirewallEndpointsResponse(typing.TypedDict, total=False):
    firewallEndpoints: _list[FirewallEndpoint]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewaySecurityPoliciesResponse(typing.TypedDict, total=False):
    gatewaySecurityPolicies: _list[GatewaySecurityPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewaySecurityPolicyRulesResponse(typing.TypedDict, total=False):
    gatewaySecurityPolicyRules: _list[GatewaySecurityPolicyRule]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInterceptDeploymentGroupsResponse(typing.TypedDict, total=False):
    interceptDeploymentGroups: _list[InterceptDeploymentGroup]
    nextPageToken: str

@typing.type_check_only
class ListInterceptDeploymentsResponse(typing.TypedDict, total=False):
    interceptDeployments: _list[InterceptDeployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInterceptEndpointGroupAssociationsResponse(typing.TypedDict, total=False):
    interceptEndpointGroupAssociations: _list[InterceptEndpointGroupAssociation]
    nextPageToken: str

@typing.type_check_only
class ListInterceptEndpointGroupsResponse(typing.TypedDict, total=False):
    interceptEndpointGroups: _list[InterceptEndpointGroup]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMirroringDeploymentGroupsResponse(typing.TypedDict, total=False):
    mirroringDeploymentGroups: _list[MirroringDeploymentGroup]
    nextPageToken: str

@typing.type_check_only
class ListMirroringDeploymentsResponse(typing.TypedDict, total=False):
    mirroringDeployments: _list[MirroringDeployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMirroringEndpointGroupAssociationsResponse(typing.TypedDict, total=False):
    mirroringEndpointGroupAssociations: _list[MirroringEndpointGroupAssociation]
    nextPageToken: str

@typing.type_check_only
class ListMirroringEndpointGroupsResponse(typing.TypedDict, total=False):
    mirroringEndpointGroups: _list[MirroringEndpointGroup]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListSACAttachmentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sacAttachments: _list[SACAttachment]
    unreachable: _list[str]

@typing.type_check_only
class ListSACRealmsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sacRealms: _list[SACRealm]
    unreachable: _list[str]

@typing.type_check_only
class ListSecurityProfileGroupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityProfileGroups: _list[SecurityProfileGroup]

@typing.type_check_only
class ListSecurityProfilesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    securityProfiles: _list[SecurityProfile]

@typing.type_check_only
class ListServerTlsPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    serverTlsPolicies: _list[ServerTlsPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListTlsInspectionPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tlsInspectionPolicies: _list[TlsInspectionPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListUrlListsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    urlLists: _list[UrlList]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MTLSPolicy(typing.TypedDict, total=False):
    clientValidationCa: _list[ValidationCA]
    clientValidationMode: typing.Literal[
        "CLIENT_VALIDATION_MODE_UNSPECIFIED",
        "ALLOW_INVALID_OR_MISSING_CLIENT_CERT",
        "REJECT_INVALID",
    ]
    clientValidationTrustConfig: str

@typing.type_check_only
class MirroringDeployment(typing.TypedDict, total=False):
    createTime: str
    description: str
    forwardingRule: str
    labels: dict[str, typing.Any]
    mirroringDeploymentGroup: str
    name: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    updateTime: str

@typing.type_check_only
class MirroringDeploymentGroup(typing.TypedDict, total=False):
    connectedEndpointGroups: _list[MirroringDeploymentGroupConnectedEndpointGroup]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    locations: _list[MirroringLocation]
    name: str
    nestedDeployments: _list[MirroringDeploymentGroupDeployment]
    network: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "CLOSED"
    ]
    updateTime: str

@typing.type_check_only
class MirroringDeploymentGroupConnectedEndpointGroup(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class MirroringDeploymentGroupDeployment(typing.TypedDict, total=False):
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class MirroringEndpointGroup(typing.TypedDict, total=False):
    associations: _list[MirroringEndpointGroupAssociationDetails]
    connectedDeploymentGroups: _list[MirroringEndpointGroupConnectedDeploymentGroup]
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    mirroringDeploymentGroup: str
    name: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CLOSED",
        "CREATING",
        "DELETING",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "DIRECT"]
    updateTime: str

@typing.type_check_only
class MirroringEndpointGroupAssociation(typing.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    locations: _list[MirroringLocation]
    locationsDetails: _list[MirroringEndpointGroupAssociationLocationDetails]
    mirroringEndpointGroup: str
    name: str
    network: str
    networkCookie: int
    reconciling: bool
    state: typing.Literal[
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
class MirroringEndpointGroupAssociationDetails(typing.TypedDict, total=False):
    name: str
    network: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "CLOSED",
        "OUT_OF_SYNC",
        "DELETE_FAILED",
    ]

@typing.type_check_only
class MirroringEndpointGroupAssociationLocationDetails(typing.TypedDict, total=False):
    location: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class MirroringEndpointGroupConnectedDeploymentGroup(typing.TypedDict, total=False):
    locations: _list[MirroringLocation]
    name: str

@typing.type_check_only
class MirroringLocation(typing.TypedDict, total=False):
    location: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "OUT_OF_SYNC"]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class RemoveAddressGroupItemsRequest(typing.TypedDict, total=False):
    items: _list[str]
    requestId: str

@typing.type_check_only
class Rule(typing.TypedDict, total=False):
    destinations: _list[Destination]
    sources: _list[Source]

@typing.type_check_only
class SACAttachment(typing.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    nccGateway: str
    sacRealm: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING_PARTNER_ATTACHMENT",
        "PARTNER_ATTACHED",
        "PARTNER_DETACHED",
    ]
    updateTime: str

@typing.type_check_only
class SACRealm(typing.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    pairingKey: SACRealmPairingKey
    securityService: typing.Literal[
        "SECURITY_SERVICE_UNSPECIFIED", "PALO_ALTO_PRISMA_ACCESS"
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING_PARTNER_ATTACHMENT",
        "PARTNER_ATTACHED",
        "PARTNER_DETACHED",
        "KEY_EXPIRED",
    ]
    updateTime: str

@typing.type_check_only
class SACRealmPairingKey(typing.TypedDict, total=False):
    expireTime: str
    key: str

@typing.type_check_only
class SecurityProfile(typing.TypedDict, total=False):
    createTime: str
    customInterceptProfile: CustomInterceptProfile
    customMirroringProfile: CustomMirroringProfile
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    threatPreventionProfile: ThreatPreventionProfile
    type: typing.Literal[
        "PROFILE_TYPE_UNSPECIFIED",
        "THREAT_PREVENTION",
        "CUSTOM_MIRRORING",
        "CUSTOM_INTERCEPT",
        "URL_FILTERING",
    ]
    updateTime: str
    urlFilteringProfile: UrlFilteringProfile

@typing.type_check_only
class SecurityProfileGroup(typing.TypedDict, total=False):
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
    urlFilteringProfile: str

@typing.type_check_only
class ServerTlsPolicy(typing.TypedDict, total=False):
    allowOpen: bool
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    mtlsPolicy: MTLSPolicy
    name: str
    serverCertificate: GoogleCloudNetworksecurityV1CertificateProvider
    updateTime: str

@typing.type_check_only
class SeverityOverride(typing.TypedDict, total=False):
    action: typing.Literal[
        "THREAT_ACTION_UNSPECIFIED", "DEFAULT_ACTION", "ALLOW", "ALERT", "DENY"
    ]
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    ipBlocks: _list[str]
    principals: _list[str]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ThreatOverride(typing.TypedDict, total=False):
    action: typing.Literal[
        "THREAT_ACTION_UNSPECIFIED", "DEFAULT_ACTION", "ALLOW", "ALERT", "DENY"
    ]
    threatId: str
    type: typing.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "UNKNOWN",
        "VULNERABILITY",
        "ANTIVIRUS",
        "SPYWARE",
        "DNS",
    ]

@typing.type_check_only
class ThreatPreventionProfile(typing.TypedDict, total=False):
    antivirusOverrides: _list[AntivirusOverride]
    severityOverrides: _list[SeverityOverride]
    threatOverrides: _list[ThreatOverride]

@typing.type_check_only
class TlsInspectionPolicy(typing.TypedDict, total=False):
    caPool: str
    createTime: str
    customTlsFeatures: _list[str]
    description: str
    excludePublicCaSet: bool
    minTlsVersion: typing.Literal[
        "TLS_VERSION_UNSPECIFIED", "TLS_1_0", "TLS_1_1", "TLS_1_2", "TLS_1_3"
    ]
    name: str
    tlsFeatureProfile: typing.Literal[
        "PROFILE_UNSPECIFIED",
        "PROFILE_COMPATIBLE",
        "PROFILE_MODERN",
        "PROFILE_RESTRICTED",
        "PROFILE_CUSTOM",
    ]
    trustConfig: str
    updateTime: str

@typing.type_check_only
class UrlFilter(typing.TypedDict, total=False):
    filteringAction: typing.Literal["URL_FILTERING_ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    priority: int
    urls: _list[str]

@typing.type_check_only
class UrlFilteringProfile(typing.TypedDict, total=False):
    urlFilters: _list[UrlFilter]

@typing.type_check_only
class UrlList(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    updateTime: str
    values: _list[str]

@typing.type_check_only
class ValidationCA(typing.TypedDict, total=False):
    certificateProviderInstance: CertificateProviderInstance
    grpcEndpoint: GoogleCloudNetworksecurityV1GrpcEndpoint
