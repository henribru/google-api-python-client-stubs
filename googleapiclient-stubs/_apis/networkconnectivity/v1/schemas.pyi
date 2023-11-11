import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceptHubSpokeRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    spokeUri: str

@typing.type_check_only
class AcceptHubSpokeResponse(typing_extensions.TypedDict, total=False):
    spoke: Spoke

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ConsumerPscConfig(typing_extensions.TypedDict, total=False):
    disableGlobalAccess: bool
    network: str
    project: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "VALID",
        "CONNECTION_POLICY_MISSING",
        "POLICY_LIMIT_REACHED",
    ]

@typing.type_check_only
class ConsumerPscConnection(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    errorInfo: GoogleRpcErrorInfo
    errorType: typing_extensions.Literal[
        "CONNECTION_ERROR_TYPE_UNSPECIFIED",
        "ERROR_INTERNAL",
        "ERROR_CONSUMER_SIDE",
        "ERROR_PRODUCER_SIDE",
    ]
    forwardingRule: str
    gceOperation: str
    ip: str
    network: str
    project: str
    pscConnectionId: str
    serviceAttachmentUri: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "CREATING", "DELETING"
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    destRange: str
    ipProtocol: str
    protocolVersion: typing_extensions.Literal["PROTOCOL_VERSION_UNSPECIFIED", "IPV4"]
    srcRange: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcErrorInfo(typing_extensions.TypedDict, total=False):
    domain: str
    metadata: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ACCEPTING",
        "REJECTING",
        "UPDATING",
        "INACTIVE",
        "OBSOLETE",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class Hub(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    routeTables: _list[str]
    routingVpcs: _list[RoutingVPC]
    spokeSummary: SpokeSummary
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ACCEPTING",
        "REJECTING",
        "UPDATING",
        "INACTIVE",
        "OBSOLETE",
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class InterconnectAttachment(typing_extensions.TypedDict, total=False):
    region: str

@typing.type_check_only
class InternalRange(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    ipCidrRange: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    overlaps: _list[str]
    peering: typing_extensions.Literal[
        "PEERING_UNSPECIFIED", "FOR_SELF", "FOR_PEER", "NOT_SHARED"
    ]
    prefixLength: int
    targetCidrRange: _list[str]
    updateTime: str
    usage: typing_extensions.Literal["USAGE_UNSPECIFIED", "FOR_VPC", "EXTERNAL_TO_VPC"]
    users: _list[str]

@typing.type_check_only
class LinkedInterconnectAttachments(typing_extensions.TypedDict, total=False):
    siteToSiteDataTransfer: bool
    uris: _list[str]
    vpcNetwork: str

@typing.type_check_only
class LinkedRouterApplianceInstances(typing_extensions.TypedDict, total=False):
    instances: _list[RouterApplianceInstance]
    siteToSiteDataTransfer: bool
    vpcNetwork: str

@typing.type_check_only
class LinkedVpcNetwork(typing_extensions.TypedDict, total=False):
    excludeExportRanges: _list[str]
    uri: str

@typing.type_check_only
class LinkedVpnTunnels(typing_extensions.TypedDict, total=False):
    siteToSiteDataTransfer: bool
    uris: _list[str]
    vpcNetwork: str

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListHubSpokesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spokes: _list[Spoke]
    unreachable: _list[str]

@typing.type_check_only
class ListHubsResponse(typing_extensions.TypedDict, total=False):
    hubs: _list[Hub]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInternalRangesResponse(typing_extensions.TypedDict, total=False):
    internalRanges: _list[InternalRange]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListPolicyBasedRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policyBasedRoutes: _list[PolicyBasedRoute]
    unreachable: _list[str]

@typing.type_check_only
class ListRouteTablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    routeTables: _list[RouteTable]
    unreachable: _list[str]

@typing.type_check_only
class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    routes: _list[Route]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceClassesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceClasses: _list[ServiceClass]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceConnectionMapsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceConnectionMaps: _list[ServiceConnectionMap]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceConnectionPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceConnectionPolicies: _list[ServiceConnectionPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceConnectionTokensResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceConnectionTokens: _list[ServiceConnectionToken]
    unreachable: _list[str]

@typing.type_check_only
class ListSpokesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spokes: _list[Spoke]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    locationFeatures: _list[str]

@typing.type_check_only
class NextHopVpcNetwork(typing_extensions.TypedDict, total=False):
    uri: str

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
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyBasedRoute(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    filter: Filter
    interconnectAttachment: InterconnectAttachment
    kind: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    nextHopIlbIp: str
    nextHopOtherRoutes: typing_extensions.Literal[
        "OTHER_ROUTES_UNSPECIFIED", "DEFAULT_ROUTING"
    ]
    priority: int
    selfLink: str
    updateTime: str
    virtualMachine: VirtualMachine
    warnings: _list[Warnings]

@typing.type_check_only
class ProducerPscConfig(typing_extensions.TypedDict, total=False):
    serviceAttachmentUri: str

@typing.type_check_only
class PscConfig(typing_extensions.TypedDict, total=False):
    limit: str
    subnetworks: _list[str]

@typing.type_check_only
class PscConnection(typing_extensions.TypedDict, total=False):
    consumerAddress: str
    consumerForwardingRule: str
    consumerTargetProject: str
    error: GoogleRpcStatus
    errorInfo: GoogleRpcErrorInfo
    errorType: typing_extensions.Literal[
        "CONNECTION_ERROR_TYPE_UNSPECIFIED",
        "ERROR_INTERNAL",
        "ERROR_CONSUMER_SIDE",
        "ERROR_PRODUCER_SIDE",
    ]
    gceOperation: str
    pscConnectionId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "CREATING", "DELETING"
    ]

@typing.type_check_only
class RejectHubSpokeRequest(typing_extensions.TypedDict, total=False):
    details: str
    requestId: str
    spokeUri: str

@typing.type_check_only
class RejectHubSpokeResponse(typing_extensions.TypedDict, total=False):
    spoke: Spoke

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    ipCidrRange: str
    labels: dict[str, typing.Any]
    location: str
    name: str
    nextHopVpcNetwork: NextHopVpcNetwork
    spoke: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ACCEPTING",
        "REJECTING",
        "UPDATING",
        "INACTIVE",
        "OBSOLETE",
    ]
    type: typing_extensions.Literal[
        "ROUTE_TYPE_UNSPECIFIED", "VPC_PRIMARY_SUBNET", "VPC_SECONDARY_SUBNET"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class RouteTable(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ACCEPTING",
        "REJECTING",
        "UPDATING",
        "INACTIVE",
        "OBSOLETE",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class RouterApplianceInstance(typing_extensions.TypedDict, total=False):
    ipAddress: str
    virtualMachine: str

@typing.type_check_only
class RoutingVPC(typing_extensions.TypedDict, total=False):
    requiredForNewSiteToSiteDataTransferSpokes: bool
    uri: str

@typing.type_check_only
class ServiceClass(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    serviceClass: str
    updateTime: str

@typing.type_check_only
class ServiceConnectionMap(typing_extensions.TypedDict, total=False):
    consumerPscConfigs: _list[ConsumerPscConfig]
    consumerPscConnections: _list[ConsumerPscConnection]
    createTime: str
    description: str
    etag: str
    infrastructure: typing_extensions.Literal["INFRASTRUCTURE_UNSPECIFIED", "PSC"]
    labels: dict[str, typing.Any]
    name: str
    producerPscConfigs: _list[ProducerPscConfig]
    serviceClass: str
    serviceClassUri: str
    token: str
    updateTime: str

@typing.type_check_only
class ServiceConnectionPolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    infrastructure: typing_extensions.Literal["INFRASTRUCTURE_UNSPECIFIED", "PSC"]
    labels: dict[str, typing.Any]
    name: str
    network: str
    pscConfig: PscConfig
    pscConnections: _list[PscConnection]
    serviceClass: str
    updateTime: str

@typing.type_check_only
class ServiceConnectionToken(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    token: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Spoke(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    group: str
    hub: str
    labels: dict[str, typing.Any]
    linkedInterconnectAttachments: LinkedInterconnectAttachments
    linkedRouterApplianceInstances: LinkedRouterApplianceInstances
    linkedVpcNetwork: LinkedVpcNetwork
    linkedVpnTunnels: LinkedVpnTunnels
    name: str
    reasons: _list[StateReason]
    spokeType: typing_extensions.Literal[
        "SPOKE_TYPE_UNSPECIFIED",
        "VPN_TUNNEL",
        "INTERCONNECT_ATTACHMENT",
        "ROUTER_APPLIANCE",
        "VPC_NETWORK",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ACCEPTING",
        "REJECTING",
        "UPDATING",
        "INACTIVE",
        "OBSOLETE",
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class SpokeStateCount(typing_extensions.TypedDict, total=False):
    count: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "ACCEPTING",
        "REJECTING",
        "UPDATING",
        "INACTIVE",
        "OBSOLETE",
    ]

@typing.type_check_only
class SpokeStateReasonCount(typing_extensions.TypedDict, total=False):
    count: str
    stateReasonCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "PENDING_REVIEW", "REJECTED", "PAUSED", "FAILED"
    ]

@typing.type_check_only
class SpokeSummary(typing_extensions.TypedDict, total=False):
    spokeStateCounts: _list[SpokeStateCount]
    spokeStateReasonCounts: _list[SpokeStateReasonCount]
    spokeTypeCounts: _list[SpokeTypeCount]

@typing.type_check_only
class SpokeTypeCount(typing_extensions.TypedDict, total=False):
    count: str
    spokeType: typing_extensions.Literal[
        "SPOKE_TYPE_UNSPECIFIED",
        "VPN_TUNNEL",
        "INTERCONNECT_ATTACHMENT",
        "ROUTER_APPLIANCE",
        "VPC_NETWORK",
    ]

@typing.type_check_only
class StateReason(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "PENDING_REVIEW", "REJECTED", "PAUSED", "FAILED"
    ]
    message: str
    userDetails: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class VirtualMachine(typing_extensions.TypedDict, total=False):
    tags: _list[str]

@typing.type_check_only
class Warnings(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "WARNING_UNSPECIFIED", "RESOURCE_NOT_ACTIVE", "RESOURCE_BEING_MODIFIED"
    ]
    data: dict[str, typing.Any]
    warningMessage: str
