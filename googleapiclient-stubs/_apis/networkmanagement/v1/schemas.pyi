import typing

import typing_extensions

class NetworkInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    matchedIpRange: str
    uri: str

class LoadBalancerInfo(typing_extensions.TypedDict, total=False):
    backendType: typing_extensions.Literal[
        "BACKEND_TYPE_UNSPECIFIED", "BACKEND_SERVICE", "TARGET_POOL"
    ]
    healthCheckUri: str
    backends: typing.List[LoadBalancerBackend]
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "INTERNAL_TCP_UDP",
        "NETWORK_TCP_UDP",
        "HTTP_PROXY",
        "TCP_PROXY",
        "SSL_PROXY",
    ]
    backendUri: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class LoadBalancerBackend(typing_extensions.TypedDict, total=False):
    healthCheckAllowingFirewallRules: typing.List[str]
    healthCheckBlockingFirewallRules: typing.List[str]
    uri: str
    displayName: str
    healthCheckFirewallState: typing_extensions.Literal[
        "HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED", "CONFIGURED", "MISCONFIGURED"
    ]

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    role: str
    members: typing.List[str]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class ForwardInfo(typing_extensions.TypedDict, total=False):
    resourceUri: str
    target: typing_extensions.Literal[
        "TARGET_UNSPECIFIED",
        "PEERING_VPC",
        "VPN_GATEWAY",
        "INTERCONNECT",
        "GKE_MASTER",
        "IMPORTED_CUSTOM_ROUTE_NEXT_HOP",
    ]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class VpnTunnelInfo(typing_extensions.TypedDict, total=False):
    networkUri: str
    sourceGatewayIp: str
    remoteGateway: str
    displayName: str
    region: str
    routingType: typing_extensions.Literal[
        "ROUTING_TYPE_UNSPECIFIED", "ROUTE_BASED", "POLICY_BASED", "DYNAMIC"
    ]
    sourceGateway: str
    uri: str
    remoteGatewayIp: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    error: Status
    response: typing.Dict[str, typing.Any]
    done: bool
    metadata: typing.Dict[str, typing.Any]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class InstanceInfo(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    interface: str
    networkTags: typing.List[str]
    networkUri: str
    uri: str
    internalIp: str
    displayName: str
    externalIp: str

class Trace(typing_extensions.TypedDict, total=False):
    endpointInfo: EndpointInfo
    steps: typing.List[Step]

class DeliverInfo(typing_extensions.TypedDict, total=False):
    target: typing_extensions.Literal[
        "TARGET_UNSPECIFIED", "INSTANCE", "INTERNET", "GOOGLE_API"
    ]
    resourceUri: str

class RerunConnectivityTestRequest(typing_extensions.TypedDict, total=False): ...

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    version: int
    bindings: typing.List[Binding]
    auditConfigs: typing.List[AuditConfig]

class FirewallInfo(typing_extensions.TypedDict, total=False):
    direction: str
    targetServiceAccounts: typing.List[str]
    networkUri: str
    targetTags: typing.List[str]
    priority: int
    action: str
    displayName: str
    uri: str

class Step(typing_extensions.TypedDict, total=False):
    endpoint: EndpointInfo
    causesDrop: bool
    vpnGateway: VpnGatewayInfo
    abort: AbortInfo
    deliver: DeliverInfo
    drop: DropInfo
    description: str
    vpnTunnel: VpnTunnelInfo
    instance: InstanceInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "START_FROM_INSTANCE",
        "START_FROM_INTERNET",
        "START_FROM_PRIVATE_NETWORK",
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
    network: NetworkInfo
    loadBalancer: LoadBalancerInfo
    forwardingRule: ForwardingRuleInfo
    forward: ForwardInfo
    firewall: FirewallInfo
    projectId: str
    route: RouteInfo

class ReachabilityDetails(typing_extensions.TypedDict, total=False):
    error: Status
    verifyTime: str
    traces: typing.List[Trace]
    result: typing_extensions.Literal[
        "RESULT_UNSPECIFIED", "REACHABLE", "UNREACHABLE", "AMBIGUOUS", "UNDETERMINED"
    ]

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
    ]
    resourceUri: str

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    displayName: str
    name: str
    locationId: str

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    expression: str
    description: str

class VpnGatewayInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    networkUri: str
    vpnTunnelUri: str
    region: str
    ipAddress: str
    uri: str

class ForwardingRuleInfo(typing_extensions.TypedDict, total=False):
    target: str
    displayName: str
    matchedPortRange: str
    networkUri: str
    matchedProtocol: str
    vip: str
    uri: str

class ConnectivityTest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    createTime: str
    description: str
    name: str
    protocol: str
    source: Endpoint
    destination: Endpoint
    reachabilityDetails: ReachabilityDetails
    displayName: str
    relatedProjects: typing.List[str]
    updateTime: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ListConnectivityTestsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[ConnectivityTest]
    unreachable: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class OperationMetadata(typing_extensions.TypedDict, total=False):
    cancelRequested: bool
    verb: str
    target: str
    endTime: str
    statusDetail: str
    createTime: str
    apiVersion: str

class RouteInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    priority: int
    nextHop: str
    routeType: typing_extensions.Literal[
        "ROUTE_TYPE_UNSPECIFIED",
        "SUBNET",
        "STATIC",
        "DYNAMIC",
        "PEERING_SUBNET",
        "PEERING_STATIC",
        "PEERING_DYNAMIC",
    ]
    networkUri: str
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
    instanceTags: typing.List[str]

class Endpoint(typing_extensions.TypedDict, total=False):
    port: int
    ipAddress: str
    network: str
    instance: str
    projectId: str
    networkType: typing_extensions.Literal[
        "NETWORK_TYPE_UNSPECIFIED", "GCP_NETWORK", "NON_GCP_NETWORK"
    ]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AbortInfo(typing_extensions.TypedDict, total=False):
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
    resourceUri: str

class EndpointInfo(typing_extensions.TypedDict, total=False):
    destinationIp: str
    sourceNetworkUri: str
    destinationNetworkUri: str
    sourcePort: int
    destinationPort: int
    sourceIp: str
    protocol: str
