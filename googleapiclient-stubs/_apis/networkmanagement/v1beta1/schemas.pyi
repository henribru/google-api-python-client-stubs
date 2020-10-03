import typing

import typing_extensions

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    version: int
    etag: str
    auditConfigs: typing.List[AuditConfig]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class NetworkInfo(typing_extensions.TypedDict, total=False):
    uri: str
    displayName: str
    matchedIpRange: str

class Trace(typing_extensions.TypedDict, total=False):
    steps: typing.List[Step]
    endpointInfo: EndpointInfo

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    location: str
    expression: str
    description: str

class VpnGatewayInfo(typing_extensions.TypedDict, total=False):
    ipAddress: str
    uri: str
    region: str
    vpnTunnelUri: str
    networkUri: str
    displayName: str

class FirewallInfo(typing_extensions.TypedDict, total=False):
    direction: str
    uri: str
    networkUri: str
    priority: int
    displayName: str
    targetTags: typing.List[str]
    action: str
    targetServiceAccounts: typing.List[str]

class Step(typing_extensions.TypedDict, total=False):
    forward: ForwardInfo
    projectId: str
    route: RouteInfo
    cloudSqlInstance: CloudSQLInstanceInfo
    abort: AbortInfo
    forwardingRule: ForwardingRuleInfo
    causesDrop: bool
    loadBalancer: LoadBalancerInfo
    network: NetworkInfo
    endpoint: EndpointInfo
    vpnTunnel: VpnTunnelInfo
    vpnGateway: VpnGatewayInfo
    firewall: FirewallInfo
    deliver: DeliverInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "START_FROM_INSTANCE",
        "START_FROM_INTERNET",
        "START_FROM_PRIVATE_NETWORK",
        "START_FROM_GKE_MASTER",
        "START_FROM_CLOUD_SQL_INSTANCE",
        "APPLY_INGRESS_FIREWALL_RULE",
        "APPLY_EGRESS_FIREWALL_RULE",
        "APPLY_ROUTE",
        "APPLY_FORWARDING_RULE",
        "SPOOFING_APPROVED",
        "ARRIVE_AT_INSTANCE",
        "ARRIVE_AT_INTERNAL_LOAD_BALANCER",
        "ARRIVE_AT_EXTERNAL_LOAD_BALANCER",
        "ARRIVE_AT_VPN_GATEWAY",
        "ARRIVE_AT_VPN_TUNNEL",
        "NAT",
        "PROXY_CONNECTION",
        "DELIVER",
        "DROP",
        "FORWARD",
        "ABORT",
        "VIEWER_PERMISSION_MISSING",
    ]
    drop: DropInfo
    instance: InstanceInfo
    gkeMaster: GKEMasterInfo
    description: str

class RouteInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    routeType: typing_extensions.Literal[
        "ROUTE_TYPE_UNSPECIFIED",
        "SUBNET",
        "STATIC",
        "DYNAMIC",
        "PEERING_SUBNET",
        "PEERING_STATIC",
        "PEERING_DYNAMIC",
    ]
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
    ]
    destIpRange: str
    uri: str
    priority: int
    networkUri: str
    nextHop: str
    instanceTags: typing.List[str]

class Endpoint(typing_extensions.TypedDict, total=False):
    projectId: str
    port: int
    cloudSqlInstance: str
    network: str
    networkType: typing_extensions.Literal[
        "NETWORK_TYPE_UNSPECIFIED", "GCP_NETWORK", "NON_GCP_NETWORK"
    ]
    instance: str
    gkeMasterCluster: str
    ipAddress: str

class LoadBalancerBackend(typing_extensions.TypedDict, total=False):
    healthCheckAllowingFirewallRules: typing.List[str]
    uri: str
    displayName: str
    healthCheckFirewallState: typing_extensions.Literal[
        "HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED", "CONFIGURED", "MISCONFIGURED"
    ]
    healthCheckBlockingFirewallRules: typing.List[str]

class ConnectivityTest(typing_extensions.TypedDict, total=False):
    updateTime: str
    displayName: str
    protocol: str
    destination: Endpoint
    relatedProjects: typing.List[str]
    description: str
    reachabilityDetails: ReachabilityDetails
    createTime: str
    source: Endpoint
    probingDetails: ProbingDetails
    name: str
    labels: typing.Dict[str, typing.Any]

class RerunConnectivityTestRequest(typing_extensions.TypedDict, total=False): ...

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status

class AbortInfo(typing_extensions.TypedDict, total=False):
    resourceUri: str
    cause: typing_extensions.Literal[
        "CAUSE_UNSPECIFIED",
        "UNKNOWN_NETWORK",
        "UNKNOWN_IP",
        "UNKNOWN_PROJECT",
        "PERMISSION_DENIED",
        "NO_SOURCE_LOCATION",
        "INVALID_ARGUMENT",
        "NO_EXTERNAL_IP",
        "UNINTENDED_DESTINATION",
        "TRACE_TOO_LONG",
        "INTERNAL_ERROR",
    ]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ForwardInfo(typing_extensions.TypedDict, total=False):
    target: typing_extensions.Literal[
        "TARGET_UNSPECIFIED",
        "PEERING_VPC",
        "VPN_GATEWAY",
        "INTERCONNECT",
        "GKE_MASTER",
        "IMPORTED_CUSTOM_ROUTE_NEXT_HOP",
        "CLOUD_SQL_INSTANCE",
    ]
    resourceUri: str

class InstanceInfo(typing_extensions.TypedDict, total=False):
    networkTags: typing.List[str]
    displayName: str
    serviceAccount: str
    networkUri: str
    uri: str
    internalIp: str
    externalIp: str
    interface: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class ProbingDetails(typing_extensions.TypedDict, total=False):
    verifyTime: str
    successfulProbeCount: int
    endpointInfo: EndpointInfo
    abortCause: typing_extensions.Literal[
        "PROBING_ABORT_CAUSE_UNSPECIFIED", "PERMISSION_DENIED", "NO_SOURCE_LOCATION"
    ]
    sentProbeCount: int
    result: typing_extensions.Literal[
        "PROBING_RESULT_UNSPECIFIED",
        "REACHABLE",
        "UNREACHABLE",
        "REACHABILITY_INCONSISTENT",
        "UNDETERMINED",
    ]
    error: Status

class EndpointInfo(typing_extensions.TypedDict, total=False):
    destinationIp: str
    destinationNetworkUri: str
    sourceIp: str
    sourcePort: int
    sourceNetworkUri: str
    protocol: str
    destinationPort: int

class DeliverInfo(typing_extensions.TypedDict, total=False):
    target: typing_extensions.Literal[
        "TARGET_UNSPECIFIED",
        "INSTANCE",
        "INTERNET",
        "GOOGLE_API",
        "GKE_MASTER",
        "CLOUD_SQL_INSTANCE",
    ]
    resourceUri: str

class LoadBalancerInfo(typing_extensions.TypedDict, total=False):
    healthCheckUri: str
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "INTERNAL_TCP_UDP",
        "NETWORK_TCP_UDP",
        "HTTP_PROXY",
        "TCP_PROXY",
        "SSL_PROXY",
    ]
    backendType: typing_extensions.Literal[
        "BACKEND_TYPE_UNSPECIFIED", "BACKEND_SERVICE", "TARGET_POOL"
    ]
    backendUri: str
    backends: typing.List[LoadBalancerBackend]

class DropInfo(typing_extensions.TypedDict, total=False):
    cause: typing_extensions.Literal[
        "CAUSE_UNSPECIFIED",
        "UNKNOWN_EXTERNAL_ADDRESS",
        "FOREIGN_IP_DISALLOWED",
        "FIREWALL_RULE",
        "NO_ROUTE",
        "ROUTE_BLACKHOLE",
        "ROUTE_WRONG_NETWORK",
        "PRIVATE_TRAFFIC_TO_INTERNET",
        "PRIVATE_GOOGLE_ACCESS_DISALLOWED",
        "NO_EXTERNAL_ADDRESS",
        "UNKNOWN_INTERNAL_ADDRESS",
        "FORWARDING_RULE_MISMATCH",
        "FORWARDING_RULE_NO_INSTANCES",
        "FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK",
        "INSTANCE_NOT_RUNNING",
        "TRAFFIC_TYPE_BLOCKED",
        "GKE_MASTER_UNAUTHORIZED_ACCESS",
        "CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS",
        "DROPPED_INSIDE_GKE_SERVICE",
        "DROPPED_INSIDE_CLOUD_SQL_SERVICE",
    ]
    resourceUri: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    apiVersion: str
    cancelRequested: bool
    statusDetail: str
    verb: str
    target: str
    createTime: str

class VpnTunnelInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    remoteGatewayIp: str
    networkUri: str
    uri: str
    routingType: typing_extensions.Literal[
        "ROUTING_TYPE_UNSPECIFIED", "ROUTE_BASED", "POLICY_BASED", "DYNAMIC"
    ]
    sourceGateway: str
    region: str
    remoteGateway: str
    sourceGatewayIp: str

class Location(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    locationId: str
    labels: typing.Dict[str, typing.Any]
    displayName: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class CloudSQLInstanceInfo(typing_extensions.TypedDict, total=False):
    region: str
    internalIp: str
    networkUri: str
    displayName: str
    uri: str
    externalIp: str

class Empty(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ForwardingRuleInfo(typing_extensions.TypedDict, total=False):
    vip: str
    matchedPortRange: str
    networkUri: str
    uri: str
    displayName: str
    matchedProtocol: str
    target: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ReachabilityDetails(typing_extensions.TypedDict, total=False):
    error: Status
    traces: typing.List[Trace]
    verifyTime: str
    result: typing_extensions.Literal[
        "RESULT_UNSPECIFIED", "REACHABLE", "UNREACHABLE", "AMBIGUOUS", "UNDETERMINED"
    ]

class ListConnectivityTestsResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    resources: typing.List[ConnectivityTest]
    nextPageToken: str

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class GKEMasterInfo(typing_extensions.TypedDict, total=False):
    clusterNetworkUri: str
    internalIp: str
    externalIp: str
    clusterUri: str
