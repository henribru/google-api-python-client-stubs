import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbortInfo(typing_extensions.TypedDict, total=False):
    cause: typing_extensions.Literal[
        "CAUSE_UNSPECIFIED",
        "UNKNOWN_NETWORK",
        "UNKNOWN_PROJECT",
        "NO_EXTERNAL_IP",
        "UNINTENDED_DESTINATION",
        "SOURCE_ENDPOINT_NOT_FOUND",
        "MISMATCHED_SOURCE_NETWORK",
        "DESTINATION_ENDPOINT_NOT_FOUND",
        "MISMATCHED_DESTINATION_NETWORK",
        "UNKNOWN_IP",
        "SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK",
        "PERMISSION_DENIED",
        "PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS",
        "PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS",
        "NO_SOURCE_LOCATION",
        "INVALID_ARGUMENT",
        "TRACE_TOO_LONG",
        "INTERNAL_ERROR",
        "UNSUPPORTED",
        "MISMATCHED_IP_VERSION",
        "GKE_KONNECTIVITY_PROXY_UNSUPPORTED",
        "RESOURCE_CONFIG_NOT_FOUND",
        "VM_INSTANCE_CONFIG_NOT_FOUND",
        "NETWORK_CONFIG_NOT_FOUND",
        "FIREWALL_CONFIG_NOT_FOUND",
        "ROUTE_CONFIG_NOT_FOUND",
        "GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT",
        "SOURCE_PSC_CLOUD_SQL_UNSUPPORTED",
        "SOURCE_FORWARDING_RULE_UNSUPPORTED",
        "NON_ROUTABLE_IP_ADDRESS",
    ]
    ipAddress: str
    projectsMissingPermission: _list[str]
    resourceUri: str

@typing.type_check_only
class AppEngineVersionEndpoint(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class AppEngineVersionInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    environment: str
    runtime: str
    uri: str

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
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudFunctionEndpoint(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class CloudFunctionInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    location: str
    uri: str
    versionId: str

@typing.type_check_only
class CloudRunRevisionEndpoint(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class CloudRunRevisionInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    location: str
    serviceName: str
    serviceUri: str
    uri: str

@typing.type_check_only
class CloudSQLInstanceInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    externalIp: str
    internalIp: str
    networkUri: str
    region: str
    uri: str

@typing.type_check_only
class ConnectivityTest(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    destination: Endpoint
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    probingDetails: ProbingDetails
    protocol: str
    reachabilityDetails: ReachabilityDetails
    relatedProjects: _list[str]
    source: Endpoint
    updateTime: str

@typing.type_check_only
class DeliverInfo(typing_extensions.TypedDict, total=False):
    ipAddress: str
    resourceUri: str
    target: typing_extensions.Literal[
        "TARGET_UNSPECIFIED",
        "INSTANCE",
        "INTERNET",
        "GOOGLE_API",
        "GKE_MASTER",
        "CLOUD_SQL_INSTANCE",
        "PSC_PUBLISHED_SERVICE",
        "PSC_GOOGLE_API",
        "PSC_VPC_SC",
        "SERVERLESS_NEG",
        "STORAGE_BUCKET",
        "PRIVATE_NETWORK",
        "CLOUD_FUNCTION",
        "APP_ENGINE_VERSION",
        "CLOUD_RUN_REVISION",
    ]

@typing.type_check_only
class DropInfo(typing_extensions.TypedDict, total=False):
    cause: typing_extensions.Literal[
        "CAUSE_UNSPECIFIED",
        "UNKNOWN_EXTERNAL_ADDRESS",
        "FOREIGN_IP_DISALLOWED",
        "FIREWALL_RULE",
        "NO_ROUTE",
        "ROUTE_BLACKHOLE",
        "ROUTE_WRONG_NETWORK",
        "ROUTE_NEXT_HOP_IP_ADDRESS_NOT_RESOLVED",
        "ROUTE_NEXT_HOP_RESOURCE_NOT_FOUND",
        "ROUTE_NEXT_HOP_INSTANCE_WRONG_NETWORK",
        "ROUTE_NEXT_HOP_INSTANCE_NON_PRIMARY_IP",
        "ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH",
        "ROUTE_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED",
        "ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID",
        "NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV6_ADDRESS",
        "VPN_TUNNEL_LOCAL_SELECTOR_MISMATCH",
        "VPN_TUNNEL_REMOTE_SELECTOR_MISMATCH",
        "PRIVATE_TRAFFIC_TO_INTERNET",
        "PRIVATE_GOOGLE_ACCESS_DISALLOWED",
        "PRIVATE_GOOGLE_ACCESS_VIA_VPN_TUNNEL_UNSUPPORTED",
        "NO_EXTERNAL_ADDRESS",
        "UNKNOWN_INTERNAL_ADDRESS",
        "FORWARDING_RULE_MISMATCH",
        "FORWARDING_RULE_NO_INSTANCES",
        "FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK",
        "INSTANCE_NOT_RUNNING",
        "GKE_CLUSTER_NOT_RUNNING",
        "CLOUD_SQL_INSTANCE_NOT_RUNNING",
        "TRAFFIC_TYPE_BLOCKED",
        "GKE_MASTER_UNAUTHORIZED_ACCESS",
        "CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS",
        "DROPPED_INSIDE_GKE_SERVICE",
        "DROPPED_INSIDE_CLOUD_SQL_SERVICE",
        "GOOGLE_MANAGED_SERVICE_NO_PEERING",
        "GOOGLE_MANAGED_SERVICE_NO_PSC_ENDPOINT",
        "GKE_PSC_ENDPOINT_MISSING",
        "CLOUD_SQL_INSTANCE_NO_IP_ADDRESS",
        "GKE_CONTROL_PLANE_REGION_MISMATCH",
        "PUBLIC_GKE_CONTROL_PLANE_TO_PRIVATE_DESTINATION",
        "GKE_CONTROL_PLANE_NO_ROUTE",
        "CLOUD_SQL_INSTANCE_NOT_CONFIGURED_FOR_EXTERNAL_TRAFFIC",
        "PUBLIC_CLOUD_SQL_INSTANCE_TO_PRIVATE_DESTINATION",
        "CLOUD_SQL_INSTANCE_NO_ROUTE",
        "CLOUD_FUNCTION_NOT_ACTIVE",
        "VPC_CONNECTOR_NOT_SET",
        "VPC_CONNECTOR_NOT_RUNNING",
        "FORWARDING_RULE_REGION_MISMATCH",
        "PSC_CONNECTION_NOT_ACCEPTED",
        "PSC_ENDPOINT_ACCESSED_FROM_PEERED_NETWORK",
        "PSC_NEG_PRODUCER_ENDPOINT_NO_GLOBAL_ACCESS",
        "PSC_NEG_PRODUCER_FORWARDING_RULE_MULTIPLE_PORTS",
        "NO_NAT_SUBNETS_FOR_PSC_SERVICE_ATTACHMENT",
        "HYBRID_NEG_NON_DYNAMIC_ROUTE_MATCHED",
        "HYBRID_NEG_NON_LOCAL_DYNAMIC_ROUTE_MATCHED",
        "CLOUD_RUN_REVISION_NOT_READY",
        "DROPPED_INSIDE_PSC_SERVICE_PRODUCER",
        "LOAD_BALANCER_HAS_NO_PROXY_SUBNET",
        "CLOUD_NAT_NO_ADDRESSES",
    ]
    destinationIp: str
    region: str
    resourceUri: str
    sourceIp: str

@typing.type_check_only
class EdgeLocation(typing_extensions.TypedDict, total=False):
    metropolitanArea: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    appEngineVersion: AppEngineVersionEndpoint
    cloudFunction: CloudFunctionEndpoint
    cloudRunRevision: CloudRunRevisionEndpoint
    cloudSqlInstance: str
    forwardingRule: str
    forwardingRuleTarget: typing_extensions.Literal[
        "FORWARDING_RULE_TARGET_UNSPECIFIED",
        "INSTANCE",
        "LOAD_BALANCER",
        "VPN_GATEWAY",
        "PSC",
    ]
    gkeMasterCluster: str
    instance: str
    ipAddress: str
    loadBalancerId: str
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "HTTPS_ADVANCED_LOAD_BALANCER",
        "HTTPS_LOAD_BALANCER",
        "REGIONAL_HTTPS_LOAD_BALANCER",
        "INTERNAL_HTTPS_LOAD_BALANCER",
        "SSL_PROXY_LOAD_BALANCER",
        "TCP_PROXY_LOAD_BALANCER",
        "INTERNAL_TCP_PROXY_LOAD_BALANCER",
        "NETWORK_LOAD_BALANCER",
        "LEGACY_NETWORK_LOAD_BALANCER",
        "TCP_UDP_INTERNAL_LOAD_BALANCER",
    ]
    network: str
    networkType: typing_extensions.Literal[
        "NETWORK_TYPE_UNSPECIFIED", "GCP_NETWORK", "NON_GCP_NETWORK"
    ]
    port: int
    projectId: str

@typing.type_check_only
class EndpointInfo(typing_extensions.TypedDict, total=False):
    destinationIp: str
    destinationNetworkUri: str
    destinationPort: int
    protocol: str
    sourceAgentUri: str
    sourceIp: str
    sourceNetworkUri: str
    sourcePort: int

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FirewallInfo(typing_extensions.TypedDict, total=False):
    action: str
    direction: str
    displayName: str
    firewallRuleType: typing_extensions.Literal[
        "FIREWALL_RULE_TYPE_UNSPECIFIED",
        "HIERARCHICAL_FIREWALL_POLICY_RULE",
        "VPC_FIREWALL_RULE",
        "IMPLIED_VPC_FIREWALL_RULE",
        "SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE",
        "NETWORK_FIREWALL_POLICY_RULE",
        "NETWORK_REGIONAL_FIREWALL_POLICY_RULE",
        "UNSUPPORTED_FIREWALL_POLICY_RULE",
        "TRACKING_STATE",
    ]
    networkUri: str
    policy: str
    priority: int
    targetServiceAccounts: _list[str]
    targetTags: _list[str]
    uri: str

@typing.type_check_only
class ForwardInfo(typing_extensions.TypedDict, total=False):
    ipAddress: str
    resourceUri: str
    target: typing_extensions.Literal[
        "TARGET_UNSPECIFIED",
        "PEERING_VPC",
        "VPN_GATEWAY",
        "INTERCONNECT",
        "GKE_MASTER",
        "IMPORTED_CUSTOM_ROUTE_NEXT_HOP",
        "CLOUD_SQL_INSTANCE",
        "ANOTHER_PROJECT",
        "NCC_HUB",
        "ROUTER_APPLIANCE",
    ]

@typing.type_check_only
class ForwardingRuleInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    matchedPortRange: str
    matchedProtocol: str
    networkUri: str
    target: str
    uri: str
    vip: str

@typing.type_check_only
class GKEMasterInfo(typing_extensions.TypedDict, total=False):
    clusterNetworkUri: str
    clusterUri: str
    externalIp: str
    internalIp: str

@typing.type_check_only
class GoogleServiceInfo(typing_extensions.TypedDict, total=False):
    googleServiceType: typing_extensions.Literal[
        "GOOGLE_SERVICE_TYPE_UNSPECIFIED",
        "IAP",
        "GFE_PROXY_OR_HEALTH_CHECK_PROBER",
        "CLOUD_DNS",
        "GOOGLE_API",
        "GOOGLE_API_PSC",
        "GOOGLE_API_VPC_SC",
    ]
    sourceIp: str

@typing.type_check_only
class InstanceInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    externalIp: str
    interface: str
    internalIp: str
    networkTags: _list[str]
    networkUri: str
    serviceAccount: str
    uri: str

@typing.type_check_only
class LatencyDistribution(typing_extensions.TypedDict, total=False):
    latencyPercentiles: _list[LatencyPercentile]

@typing.type_check_only
class LatencyPercentile(typing_extensions.TypedDict, total=False):
    latencyMicros: str
    percent: int

@typing.type_check_only
class ListConnectivityTestsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[ConnectivityTest]
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class LoadBalancerBackend(typing_extensions.TypedDict, total=False):
    displayName: str
    healthCheckAllowingFirewallRules: _list[str]
    healthCheckBlockingFirewallRules: _list[str]
    healthCheckFirewallState: typing_extensions.Literal[
        "HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED", "CONFIGURED", "MISCONFIGURED"
    ]
    uri: str

@typing.type_check_only
class LoadBalancerBackendInfo(typing_extensions.TypedDict, total=False):
    backendBucketUri: str
    backendServiceUri: str
    healthCheckFirewallsConfigState: typing_extensions.Literal[
        "HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED",
        "FIREWALLS_CONFIGURED",
        "FIREWALLS_PARTIALLY_CONFIGURED",
        "FIREWALLS_NOT_CONFIGURED",
        "FIREWALLS_UNSUPPORTED",
    ]
    healthCheckUri: str
    instanceGroupUri: str
    instanceUri: str
    name: str
    networkEndpointGroupUri: str
    pscGoogleApiTarget: str
    pscServiceAttachmentUri: str

@typing.type_check_only
class LoadBalancerInfo(typing_extensions.TypedDict, total=False):
    backendType: typing_extensions.Literal[
        "BACKEND_TYPE_UNSPECIFIED", "BACKEND_SERVICE", "TARGET_POOL", "TARGET_INSTANCE"
    ]
    backendUri: str
    backends: _list[LoadBalancerBackend]
    healthCheckUri: str
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "INTERNAL_TCP_UDP",
        "NETWORK_TCP_UDP",
        "HTTP_PROXY",
        "TCP_PROXY",
        "SSL_PROXY",
    ]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NatInfo(typing_extensions.TypedDict, total=False):
    natGatewayName: str
    networkUri: str
    newDestinationIp: str
    newDestinationPort: int
    newSourceIp: str
    newSourcePort: int
    oldDestinationIp: str
    oldDestinationPort: int
    oldSourceIp: str
    oldSourcePort: int
    protocol: str
    routerUri: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "INTERNAL_TO_EXTERNAL",
        "EXTERNAL_TO_INTERNAL",
        "CLOUD_NAT",
        "PRIVATE_SERVICE_CONNECT",
    ]

@typing.type_check_only
class NetworkInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    matchedIpRange: str
    uri: str

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
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProbingDetails(typing_extensions.TypedDict, total=False):
    abortCause: typing_extensions.Literal[
        "PROBING_ABORT_CAUSE_UNSPECIFIED", "PERMISSION_DENIED", "NO_SOURCE_LOCATION"
    ]
    destinationEgressLocation: EdgeLocation
    endpointInfo: EndpointInfo
    error: Status
    probingLatency: LatencyDistribution
    result: typing_extensions.Literal[
        "PROBING_RESULT_UNSPECIFIED",
        "REACHABLE",
        "UNREACHABLE",
        "REACHABILITY_INCONSISTENT",
        "UNDETERMINED",
    ]
    sentProbeCount: int
    successfulProbeCount: int
    verifyTime: str

@typing.type_check_only
class ProxyConnectionInfo(typing_extensions.TypedDict, total=False):
    networkUri: str
    newDestinationIp: str
    newDestinationPort: int
    newSourceIp: str
    newSourcePort: int
    oldDestinationIp: str
    oldDestinationPort: int
    oldSourceIp: str
    oldSourcePort: int
    protocol: str
    subnetUri: str

@typing.type_check_only
class ReachabilityDetails(typing_extensions.TypedDict, total=False):
    error: Status
    result: typing_extensions.Literal[
        "RESULT_UNSPECIFIED", "REACHABLE", "UNREACHABLE", "AMBIGUOUS", "UNDETERMINED"
    ]
    traces: _list[Trace]
    verifyTime: str

@typing.type_check_only
class RerunConnectivityTestRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RouteInfo(typing_extensions.TypedDict, total=False):
    destIpRange: str
    destPortRanges: _list[str]
    displayName: str
    instanceTags: _list[str]
    nccHubUri: str
    nccSpokeUri: str
    networkUri: str
    nextHop: str
    nextHopType: typing_extensions.Literal[
        "NEXT_HOP_TYPE_UNSPECIFIED",
        "NEXT_HOP_IP",
        "NEXT_HOP_INSTANCE",
        "NEXT_HOP_NETWORK",
        "NEXT_HOP_PEERING",
        "NEXT_HOP_INTERCONNECT",
        "NEXT_HOP_VPN_TUNNEL",
        "NEXT_HOP_VPN_GATEWAY",
        "NEXT_HOP_INTERNET_GATEWAY",
        "NEXT_HOP_BLACKHOLE",
        "NEXT_HOP_ILB",
        "NEXT_HOP_ROUTER_APPLIANCE",
        "NEXT_HOP_NCC_HUB",
    ]
    priority: int
    protocols: _list[str]
    routeScope: typing_extensions.Literal[
        "ROUTE_SCOPE_UNSPECIFIED", "NETWORK", "NCC_HUB"
    ]
    routeType: typing_extensions.Literal[
        "ROUTE_TYPE_UNSPECIFIED",
        "SUBNET",
        "STATIC",
        "DYNAMIC",
        "PEERING_SUBNET",
        "PEERING_STATIC",
        "PEERING_DYNAMIC",
        "POLICY_BASED",
    ]
    srcIpRange: str
    srcPortRanges: _list[str]
    uri: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Step(typing_extensions.TypedDict, total=False):
    abort: AbortInfo
    appEngineVersion: AppEngineVersionInfo
    causesDrop: bool
    cloudFunction: CloudFunctionInfo
    cloudRunRevision: CloudRunRevisionInfo
    cloudSqlInstance: CloudSQLInstanceInfo
    deliver: DeliverInfo
    description: str
    drop: DropInfo
    endpoint: EndpointInfo
    firewall: FirewallInfo
    forward: ForwardInfo
    forwardingRule: ForwardingRuleInfo
    gkeMaster: GKEMasterInfo
    googleService: GoogleServiceInfo
    instance: InstanceInfo
    loadBalancer: LoadBalancerInfo
    loadBalancerBackendInfo: LoadBalancerBackendInfo
    nat: NatInfo
    network: NetworkInfo
    projectId: str
    proxyConnection: ProxyConnectionInfo
    route: RouteInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "START_FROM_INSTANCE",
        "START_FROM_INTERNET",
        "START_FROM_GOOGLE_SERVICE",
        "START_FROM_PRIVATE_NETWORK",
        "START_FROM_GKE_MASTER",
        "START_FROM_CLOUD_SQL_INSTANCE",
        "START_FROM_CLOUD_FUNCTION",
        "START_FROM_APP_ENGINE_VERSION",
        "START_FROM_CLOUD_RUN_REVISION",
        "START_FROM_STORAGE_BUCKET",
        "START_FROM_PSC_PUBLISHED_SERVICE",
        "APPLY_INGRESS_FIREWALL_RULE",
        "APPLY_EGRESS_FIREWALL_RULE",
        "APPLY_ROUTE",
        "APPLY_FORWARDING_RULE",
        "ANALYZE_LOAD_BALANCER_BACKEND",
        "SPOOFING_APPROVED",
        "ARRIVE_AT_INSTANCE",
        "ARRIVE_AT_INTERNAL_LOAD_BALANCER",
        "ARRIVE_AT_EXTERNAL_LOAD_BALANCER",
        "ARRIVE_AT_VPN_GATEWAY",
        "ARRIVE_AT_VPN_TUNNEL",
        "ARRIVE_AT_VPC_CONNECTOR",
        "NAT",
        "PROXY_CONNECTION",
        "DELIVER",
        "DROP",
        "FORWARD",
        "ABORT",
        "VIEWER_PERMISSION_MISSING",
    ]
    storageBucket: StorageBucketInfo
    vpcConnector: VpcConnectorInfo
    vpnGateway: VpnGatewayInfo
    vpnTunnel: VpnTunnelInfo

@typing.type_check_only
class StorageBucketInfo(typing_extensions.TypedDict, total=False):
    bucket: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Trace(typing_extensions.TypedDict, total=False):
    endpointInfo: EndpointInfo
    forwardTraceId: int
    steps: _list[Step]

@typing.type_check_only
class VpcConnectorInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    location: str
    uri: str

@typing.type_check_only
class VpnGatewayInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    ipAddress: str
    networkUri: str
    region: str
    uri: str
    vpnTunnelUri: str

@typing.type_check_only
class VpnTunnelInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    networkUri: str
    region: str
    remoteGateway: str
    remoteGatewayIp: str
    routingType: typing_extensions.Literal[
        "ROUTING_TYPE_UNSPECIFIED", "ROUTE_BASED", "POLICY_BASED", "DYNAMIC"
    ]
    sourceGateway: str
    sourceGatewayIp: str
    uri: str
