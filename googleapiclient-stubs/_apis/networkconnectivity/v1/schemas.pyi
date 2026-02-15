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
class AcceptSpokeUpdateRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    spokeEtag: str
    spokeUri: str

@typing.type_check_only
class AllocationOptions(typing_extensions.TypedDict, total=False):
    allocationStrategy: typing_extensions.Literal[
        "ALLOCATION_STRATEGY_UNSPECIFIED",
        "RANDOM",
        "FIRST_AVAILABLE",
        "RANDOM_FIRST_N_AVAILABLE",
        "FIRST_SMALLEST_FITTING",
    ]
    firstAvailableRangesLookupSize: int

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
class AutoAccept(typing_extensions.TypedDict, total=False):
    autoAcceptProjects: _list[str]

@typing.type_check_only
class AutoCreatedSubnetworkInfo(typing_extensions.TypedDict, total=False):
    delinked: bool
    internalRange: str
    internalRangeRef: str
    subnetwork: str
    subnetworkRef: str

@typing.type_check_only
class AutomatedDnsCreationSpec(typing_extensions.TypedDict, total=False):
    dnsSuffix: str
    hostname: str
    ttl: str

@typing.type_check_only
class AutomatedDnsRecord(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    createTime: str
    creationMode: typing_extensions.Literal[
        "CREATION_MODE_UNSPECIFIED", "CONSUMER_API", "SERVICE_CONNECTION_MAP"
    ]
    currentConfig: Config
    description: str
    dnsSuffix: str
    dnsZone: str
    etag: str
    fqdn: str
    hostname: str
    labels: dict[str, typing.Any]
    name: str
    originalConfig: Config
    recordType: typing_extensions.Literal[
        "RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "TXT", "CNAME"
    ]
    serviceClass: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PROGRAMMED",
        "FAILED_DEPROGRAMMING",
        "CREATING",
        "DELETING",
    ]
    stateDetails: str
    updateTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CheckConsumerConfigRequest(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    endpointProject: str
    requestedIpVersion: typing_extensions.Literal[
        "IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"
    ]
    serviceClass: str

@typing.type_check_only
class CheckConsumerConfigResponse(typing_extensions.TypedDict, total=False):
    errors: _list[
        typing_extensions.Literal[
            "ERROR_UNSPECIFIED",
            "NETWORK_PROJECT_INVALID",
            "NETWORK_PROJECT_APIS_NOT_ENABLED",
            "NETWORK_INVALID",
            "CONNECTION_POLICY_MISSING",
            "IP_VERSION_NOT_SUPPORTED",
            "NETWORK_PROJECT_SERVICE_AGENT_NOT_FOUND",
            "ENDPOINT_PROJECT_INVALID",
            "ENDPOINT_PROJECT_API_NOT_ENABLED",
            "ENDPOINT_PROJECT_IS_NOT_SERVICE_PROJECT",
        ]
    ]

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    rrdatas: _list[str]
    ttl: str

@typing.type_check_only
class ConsumerPscConfig(typing_extensions.TypedDict, total=False):
    consumerInstanceProject: str
    disableGlobalAccess: bool
    ipVersion: typing_extensions.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    network: str
    producerInstanceId: str
    producerInstanceMetadata: dict[str, typing.Any]
    project: str
    serviceAttachmentIpAddressMap: dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "VALID",
        "CONNECTION_POLICY_MISSING",
        "POLICY_LIMIT_REACHED",
        "CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED",
    ]

@typing.type_check_only
class ConsumerPscConnection(typing_extensions.TypedDict, total=False):
    dnsAutomationStatus: DnsAutomationStatus
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
    ipVersion: typing_extensions.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    network: str
    producerInstanceId: str
    producerInstanceMetadata: dict[str, typing.Any]
    project: str
    pscConnectionId: str
    selectedSubnetwork: str
    serviceAttachmentUri: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "FAILED",
        "CREATING",
        "DELETING",
        "CREATE_REPAIRING",
        "DELETE_REPAIRING",
    ]

@typing.type_check_only
class Destination(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endpoints: _list[DestinationEndpoint]
    etag: str
    ipPrefix: str
    labels: dict[str, typing.Any]
    name: str
    stateTimeline: StateTimeline
    uid: str
    updateTime: str

@typing.type_check_only
class DestinationEndpoint(typing_extensions.TypedDict, total=False):
    asn: str
    csp: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "VALID", "INVALID"]
    updateTime: str

@typing.type_check_only
class DnsAutomationStatus(typing_extensions.TypedDict, total=False):
    error: GoogleRpcStatus
    fqdn: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING_CREATE",
        "ACTIVE",
        "PENDING_DELETE",
        "CREATE_FAILED",
        "DELETE_FAILED",
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
    protocolVersion: typing_extensions.Literal[
        "PROTOCOL_VERSION_UNSPECIFIED", "IPV4", "IPV6"
    ]
    srcRange: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

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
    autoAccept: AutoAccept
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    routeTable: str
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
        "FAILED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class Hub(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    exportPsc: bool
    labels: dict[str, typing.Any]
    name: str
    policyMode: typing_extensions.Literal["POLICY_MODE_UNSPECIFIED", "PRESET"]
    presetTopology: typing_extensions.Literal[
        "PRESET_TOPOLOGY_UNSPECIFIED", "MESH", "STAR"
    ]
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
        "FAILED",
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class HubStatusEntry(typing_extensions.TypedDict, total=False):
    count: int
    groupBy: str
    pscPropagationStatus: PscPropagationStatus

@typing.type_check_only
class InterconnectAttachment(typing_extensions.TypedDict, total=False):
    region: str

@typing.type_check_only
class InternalRange(typing_extensions.TypedDict, total=False):
    allocationOptions: AllocationOptions
    createTime: str
    description: str
    excludeCidrRanges: _list[str]
    immutable: bool
    ipCidrRange: str
    labels: dict[str, typing.Any]
    migration: Migration
    name: str
    network: str
    overlaps: _list[
        typing_extensions.Literal[
            "OVERLAP_UNSPECIFIED",
            "OVERLAP_ROUTE_RANGE",
            "OVERLAP_EXISTING_SUBNET_RANGE",
        ]
    ]
    peering: typing_extensions.Literal[
        "PEERING_UNSPECIFIED", "FOR_SELF", "FOR_PEER", "NOT_SHARED"
    ]
    prefixLength: int
    targetCidrRange: _list[str]
    updateTime: str
    usage: typing_extensions.Literal[
        "USAGE_UNSPECIFIED", "FOR_VPC", "EXTERNAL_TO_VPC", "FOR_MIGRATION"
    ]
    users: _list[str]

@typing.type_check_only
class LinkedInterconnectAttachments(typing_extensions.TypedDict, total=False):
    includeImportRanges: _list[str]
    siteToSiteDataTransfer: bool
    uris: _list[str]
    vpcNetwork: str

@typing.type_check_only
class LinkedProducerVpcNetwork(typing_extensions.TypedDict, total=False):
    excludeExportRanges: _list[str]
    includeExportRanges: _list[str]
    network: str
    peering: str
    producerNetwork: str
    proposedExcludeExportRanges: _list[str]
    proposedIncludeExportRanges: _list[str]
    serviceConsumerVpcSpoke: str

@typing.type_check_only
class LinkedRouterApplianceInstances(typing_extensions.TypedDict, total=False):
    includeImportRanges: _list[str]
    instances: _list[RouterApplianceInstance]
    siteToSiteDataTransfer: bool
    vpcNetwork: str

@typing.type_check_only
class LinkedVpcNetwork(typing_extensions.TypedDict, total=False):
    excludeExportRanges: _list[str]
    includeExportRanges: _list[str]
    producerVpcSpokes: _list[str]
    proposedExcludeExportRanges: _list[str]
    proposedIncludeExportRanges: _list[str]
    uri: str

@typing.type_check_only
class LinkedVpnTunnels(typing_extensions.TypedDict, total=False):
    includeImportRanges: _list[str]
    siteToSiteDataTransfer: bool
    uris: _list[str]
    vpcNetwork: str

@typing.type_check_only
class ListAutomatedDnsRecordsResponse(typing_extensions.TypedDict, total=False):
    automatedDnsRecords: _list[AutomatedDnsRecord]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDestinationsResponse(typing_extensions.TypedDict, total=False):
    destinations: _list[Destination]
    nextPageToken: str
    unreachable: _list[str]

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
class ListMulticloudDataTransferConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    multicloudDataTransferConfigs: _list[MulticloudDataTransferConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMulticloudDataTransferSupportedServicesResponse(
    typing_extensions.TypedDict, total=False
):
    multicloudDataTransferSupportedServices: _list[
        MulticloudDataTransferSupportedService
    ]
    nextPageToken: str

@typing.type_check_only
class ListPolicyBasedRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policyBasedRoutes: _list[PolicyBasedRoute]
    unreachable: _list[str]

@typing.type_check_only
class ListRegionalEndpointsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    regionalEndpoints: _list[RegionalEndpoint]
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
    locationFeatures: _list[
        typing_extensions.Literal[
            "LOCATION_FEATURE_UNSPECIFIED",
            "SITE_TO_CLOUD_SPOKES",
            "SITE_TO_SITE_SPOKES",
            "GATEWAY_SPOKES",
        ]
    ]

@typing.type_check_only
class Migration(typing_extensions.TypedDict, total=False):
    source: str
    target: str

@typing.type_check_only
class MulticloudDataTransferConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    destinationsActiveCount: int
    destinationsCount: int
    etag: str
    labels: dict[str, typing.Any]
    name: str
    services: dict[str, typing.Any]
    uid: str
    updateTime: str

@typing.type_check_only
class MulticloudDataTransferSupportedService(typing_extensions.TypedDict, total=False):
    name: str
    serviceConfigs: _list[ServiceConfig]

@typing.type_check_only
class NextHopInterconnectAttachment(typing_extensions.TypedDict, total=False):
    siteToSiteDataTransfer: bool
    uri: str
    vpcNetwork: str

@typing.type_check_only
class NextHopRouterApplianceInstance(typing_extensions.TypedDict, total=False):
    siteToSiteDataTransfer: bool
    uri: str
    vpcNetwork: str

@typing.type_check_only
class NextHopSpoke(typing_extensions.TypedDict, total=False):
    siteToSiteDataTransfer: bool
    uri: str

@typing.type_check_only
class NextHopVPNTunnel(typing_extensions.TypedDict, total=False):
    siteToSiteDataTransfer: bool
    uri: str
    vpcNetwork: str

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
    automatedDnsCreationSpec: AutomatedDnsCreationSpec
    serviceAttachmentUri: str

@typing.type_check_only
class PscConfig(typing_extensions.TypedDict, total=False):
    allowedGoogleProducersResourceHierarchyLevel: _list[str]
    limit: str
    producerInstanceLocation: typing_extensions.Literal[
        "PRODUCER_INSTANCE_LOCATION_UNSPECIFIED", "CUSTOM_RESOURCE_HIERARCHY_LEVELS"
    ]
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
    ipVersion: typing_extensions.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    producerInstanceId: str
    producerInstanceMetadata: dict[str, typing.Any]
    pscConnectionId: str
    selectedSubnetwork: str
    serviceClass: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "FAILED",
        "CREATING",
        "DELETING",
        "CREATE_REPAIRING",
        "DELETE_REPAIRING",
    ]

@typing.type_check_only
class PscPropagationStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "READY",
        "PROPAGATING",
        "ERROR_PRODUCER_PROPAGATED_CONNECTION_LIMIT_EXCEEDED",
        "ERROR_PRODUCER_NAT_IP_SPACE_EXHAUSTED",
        "ERROR_PRODUCER_QUOTA_EXCEEDED",
        "ERROR_CONSUMER_QUOTA_EXCEEDED",
    ]
    message: str
    sourceForwardingRule: str
    sourceGroup: str
    sourceSpoke: str
    targetGroup: str
    targetSpoke: str

@typing.type_check_only
class QueryHubStatusResponse(typing_extensions.TypedDict, total=False):
    hubStatusEntries: _list[HubStatusEntry]
    nextPageToken: str

@typing.type_check_only
class RegionalEndpoint(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "GLOBAL", "REGIONAL"
    ]
    address: str
    createTime: str
    description: str
    ipAddress: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    pscForwardingRule: str
    subnetwork: str
    targetGoogleApi: str
    updateTime: str

@typing.type_check_only
class RejectHubSpokeRequest(typing_extensions.TypedDict, total=False):
    details: str
    requestId: str
    spokeUri: str

@typing.type_check_only
class RejectHubSpokeResponse(typing_extensions.TypedDict, total=False):
    spoke: Spoke

@typing.type_check_only
class RejectSpokeUpdateRequest(typing_extensions.TypedDict, total=False):
    details: str
    requestId: str
    spokeEtag: str
    spokeUri: str

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    ipCidrRange: str
    labels: dict[str, typing.Any]
    location: str
    name: str
    nextHopInterconnectAttachment: NextHopInterconnectAttachment
    nextHopRouterApplianceInstance: NextHopRouterApplianceInstance
    nextHopSpoke: NextHopSpoke
    nextHopVpcNetwork: NextHopVpcNetwork
    nextHopVpnTunnel: NextHopVPNTunnel
    priority: str
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
        "FAILED",
    ]
    type: typing_extensions.Literal[
        "ROUTE_TYPE_UNSPECIFIED",
        "VPC_PRIMARY_SUBNET",
        "VPC_SECONDARY_SUBNET",
        "DYNAMIC_ROUTE",
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
        "FAILED",
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
class ServiceConfig(typing_extensions.TypedDict, total=False):
    eligibilityCriteria: typing_extensions.Literal[
        "ELIGIBILITY_CRITERIA_UNSPECIFIED",
        "NETWORK_SERVICE_TIER_PREMIUM_ONLY",
        "NETWORK_SERVICE_TIER_STANDARD_ONLY",
        "REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY",
    ]
    supportEndTime: str

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
    autoCreatedSubnetInfo: AutoCreatedSubnetworkInfo
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
    etag: str
    fieldPathsPendingUpdate: _list[str]
    group: str
    hub: str
    labels: dict[str, typing.Any]
    linkedInterconnectAttachments: LinkedInterconnectAttachments
    linkedProducerVpcNetwork: LinkedProducerVpcNetwork
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
        "PRODUCER_VPC_NETWORK",
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
        "FAILED",
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
        "FAILED",
    ]

@typing.type_check_only
class SpokeStateReasonCount(typing_extensions.TypedDict, total=False):
    count: str
    stateReasonCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "PENDING_REVIEW",
        "REJECTED",
        "PAUSED",
        "FAILED",
        "UPDATE_PENDING_REVIEW",
        "UPDATE_REJECTED",
        "UPDATE_FAILED",
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
        "PRODUCER_VPC_NETWORK",
    ]

@typing.type_check_only
class StateMetadata(typing_extensions.TypedDict, total=False):
    effectiveTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ADDING", "ACTIVE", "DELETING", "SUSPENDING", "SUSPENDED"
    ]

@typing.type_check_only
class StateReason(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "PENDING_REVIEW",
        "REJECTED",
        "PAUSED",
        "FAILED",
        "UPDATE_PENDING_REVIEW",
        "UPDATE_REJECTED",
        "UPDATE_FAILED",
    ]
    message: str
    userDetails: str

@typing.type_check_only
class StateTimeline(typing_extensions.TypedDict, total=False):
    states: _list[StateMetadata]

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
