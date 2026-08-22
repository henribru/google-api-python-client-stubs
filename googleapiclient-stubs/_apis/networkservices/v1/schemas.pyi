import typing

_list = list

@typing.type_check_only
class AgentConnectivityTemplate(typing.TypedDict, total=False):
    accessPath: typing.Literal[
        "ACCESS_PATH_UNSPECIFIED", "CLIENT_TO_AGENT", "AGENT_TO_ANYWHERE"
    ]
    accessTypes: _list[typing.Literal["ACCESS_TYPE_UNSPECIFIED", "PUBLIC", "PRIVATE"]]
    agentCompute: typing.Literal[
        "AGENT_COMPUTE_UNSPECIFIED", "GKE", "CLOUD_RUN", "BORG"
    ]
    createTime: str
    deploymentModel: typing.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "CENTRALIZED", "AMBIENT"
    ]
    description: str
    egressNetworkConfig: EgressNetworkConfig
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class AgentGateway(typing.TypedDict, total=False):
    agentConnectivityTemplate: str
    agentGatewayCard: AgentGatewayAgentGatewayOutputCard
    createTime: str
    description: str
    etag: str
    googleManaged: AgentGatewayGoogleManaged
    labels: dict[str, typing.Any]
    name: str
    networkConfig: AgentGatewayNetworkConfig
    protocols: _list[typing.Literal["PROTOCOL_UNSPECIFIED", "MCP"]]
    registries: _list[str]
    selfManaged: AgentGatewaySelfManaged
    updateTime: str

@typing.type_check_only
class AgentGatewayAgentGatewayOutputCard(typing.TypedDict, total=False):
    mtlsEndpoint: str
    rootCertificates: _list[str]
    serviceExtensionsServiceAccount: str

@typing.type_check_only
class AgentGatewayGoogleManaged(typing.TypedDict, total=False):
    governedAccessPath: typing.Literal[
        "GOVERNED_ACCESS_PATH_UNSPECIFIED", "AGENT_TO_ANYWHERE", "CLIENT_TO_AGENT"
    ]

@typing.type_check_only
class AgentGatewayNetworkConfig(typing.TypedDict, total=False):
    dnsPeeringConfig: AgentGatewayNetworkConfigDnsPeeringConfig
    egress: AgentGatewayNetworkConfigEgress

@typing.type_check_only
class AgentGatewayNetworkConfigDnsPeeringConfig(typing.TypedDict, total=False):
    domains: _list[str]
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class AgentGatewayNetworkConfigEgress(typing.TypedDict, total=False):
    networkAttachment: str

@typing.type_check_only
class AgentGatewaySelfManaged(typing.TypedDict, total=False):
    resourceUri: str
    resourceUris: _list[str]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthzExtension(typing.TypedDict, total=False):
    authority: str
    createTime: str
    description: str
    failOpen: bool
    forwardAttributes: _list[str]
    forwardHeaders: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    metadata: dict[str, typing.Any]
    name: str
    service: str
    timeout: str
    updateTime: str
    wireFormat: typing.Literal[
        "WIRE_FORMAT_UNSPECIFIED", "EXT_PROC_GRPC", "EXT_AUTHZ_GRPC"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DnsPeeringConfig(typing.TypedDict, total=False):
    domain: str
    targetNetwork: str

@typing.type_check_only
class EgressNetworkConfig(typing.TypedDict, total=False):
    dnsPeeringConfig: DnsPeeringConfig
    networkAttachment: str
    trustConfig: str
    vpcEgress: typing.Literal[
        "VPC_EGRESS_UNSPECIFIED", "ALL_TRAFFIC", "PRIVATE_RANGES_ONLY"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EndpointMatcher(typing.TypedDict, total=False):
    metadataLabelMatcher: EndpointMatcherMetadataLabelMatcher

@typing.type_check_only
class EndpointMatcherMetadataLabelMatcher(typing.TypedDict, total=False):
    metadataLabelMatchCriteria: typing.Literal[
        "METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED", "MATCH_ANY", "MATCH_ALL"
    ]
    metadataLabels: _list[EndpointMatcherMetadataLabelMatcherMetadataLabels]

@typing.type_check_only
class EndpointMatcherMetadataLabelMatcherMetadataLabels(typing.TypedDict, total=False):
    labelName: str
    labelValue: str

@typing.type_check_only
class EndpointPolicy(typing.TypedDict, total=False):
    authorizationPolicy: str
    clientTlsPolicy: str
    createTime: str
    description: str
    endpointMatcher: EndpointMatcher
    labels: dict[str, typing.Any]
    name: str
    serverTlsPolicy: str
    trafficPortSelector: TrafficPortSelector
    type: typing.Literal[
        "ENDPOINT_POLICY_TYPE_UNSPECIFIED", "SIDECAR_PROXY", "GRPC_SERVER"
    ]
    updateTime: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtensionBinding(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    failOpen: bool
    labels: dict[str, typing.Any]
    matchConditions: _list[ExtensionBindingMatchCondition]
    name: str
    priority: int
    producerExtension: str
    producerMetadata: dict[str, typing.Any]
    target: ExtensionBindingTarget
    updateTime: str

@typing.type_check_only
class ExtensionBindingMatchCondition(typing.TypedDict, total=False):
    to: ExtensionBindingMatchConditionTo

@typing.type_check_only
class ExtensionBindingMatchConditionHeaderMatch(typing.TypedDict, total=False):
    name: str
    value: ExtensionBindingMatchConditionStringMatch

@typing.type_check_only
class ExtensionBindingMatchConditionStringMatch(typing.TypedDict, total=False):
    contains: str
    exact: str
    ignoreCase: bool
    prefix: str
    suffix: str

@typing.type_check_only
class ExtensionBindingMatchConditionTo(typing.TypedDict, total=False):
    destination: ExtensionBindingMatchConditionToDestination
    notDestination: ExtensionBindingMatchConditionToDestination

@typing.type_check_only
class ExtensionBindingMatchConditionToDestination(typing.TypedDict, total=False):
    headerSet: ExtensionBindingMatchConditionToDestinationHeaderSet
    hosts: _list[ExtensionBindingMatchConditionStringMatch]
    paths: _list[ExtensionBindingMatchConditionStringMatch]
    resources: _list[ExtensionBindingMatchConditionStringMatch]

@typing.type_check_only
class ExtensionBindingMatchConditionToDestinationHeaderSet(
    typing.TypedDict, total=False
):
    headers: _list[ExtensionBindingMatchConditionHeaderMatch]

@typing.type_check_only
class ExtensionBindingTarget(typing.TypedDict, total=False):
    resources: _list[str]
    scope: ExtensionBindingTargetScope

@typing.type_check_only
class ExtensionBindingTargetScope(typing.TypedDict, total=False):
    parent: str
    resourceTypes: _list[
        typing.Literal["RESOURCE_TYPE_UNSPECIFIED", "AI_APPLICATION", "AGENT_GATEWAY"]
    ]

@typing.type_check_only
class ExtensionChain(typing.TypedDict, total=False):
    extensions: _list[ExtensionChainExtension]
    matchCondition: ExtensionChainMatchCondition
    name: str

@typing.type_check_only
class ExtensionChainExtension(typing.TypedDict, total=False):
    authority: str
    failOpen: bool
    forwardAttributes: _list[str]
    forwardHeaders: _list[str]
    metadata: dict[str, typing.Any]
    name: str
    observabilityMode: bool
    requestBodySendMode: typing.Literal[
        "BODY_SEND_MODE_UNSPECIFIED",
        "BODY_SEND_MODE_STREAMED",
        "BODY_SEND_MODE_FULL_DUPLEX_STREAMED",
    ]
    responseBodySendMode: typing.Literal[
        "BODY_SEND_MODE_UNSPECIFIED",
        "BODY_SEND_MODE_STREAMED",
        "BODY_SEND_MODE_FULL_DUPLEX_STREAMED",
    ]
    service: str
    supportedEvents: _list[
        typing.Literal[
            "EVENT_TYPE_UNSPECIFIED",
            "REQUEST_HEADERS",
            "REQUEST_BODY",
            "RESPONSE_HEADERS",
            "RESPONSE_BODY",
            "REQUEST_TRAILERS",
            "RESPONSE_TRAILERS",
        ]
    ]
    timeout: str

@typing.type_check_only
class ExtensionChainMatchCondition(typing.TypedDict, total=False):
    celExpression: str

@typing.type_check_only
class Gateway(typing.TypedDict, total=False):
    addresses: _list[str]
    allPorts: bool
    allowGlobalAccess: bool
    certificateUrls: _list[str]
    createTime: str
    description: str
    envoyHeaders: typing.Literal["ENVOY_HEADERS_UNSPECIFIED", "NONE", "DEBUG_HEADERS"]
    gatewaySecurityPolicy: str
    ipVersion: typing.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    labels: dict[str, typing.Any]
    name: str
    network: str
    ports: _list[int]
    routingMode: typing.Literal["EXPLICIT_ROUTING_MODE", "NEXT_HOP_ROUTING_MODE"]
    scope: str
    selfLink: str
    serverTlsPolicy: str
    subnetwork: str
    type: typing.Literal["TYPE_UNSPECIFIED", "OPEN_MESH", "SECURE_WEB_GATEWAY"]
    updateTime: str

@typing.type_check_only
class GatewayRouteView(typing.TypedDict, total=False):
    name: str
    routeId: str
    routeLocation: str
    routeProjectNumber: str
    routeType: str

@typing.type_check_only
class GrpcRoute(typing.TypedDict, total=False):
    createTime: str
    description: str
    gateways: _list[str]
    hostnames: _list[str]
    labels: dict[str, typing.Any]
    meshes: _list[str]
    name: str
    rules: _list[GrpcRouteRouteRule]
    selfLink: str
    updateTime: str

@typing.type_check_only
class GrpcRouteDestination(typing.TypedDict, total=False):
    serviceName: str
    weight: int

@typing.type_check_only
class GrpcRouteFaultInjectionPolicy(typing.TypedDict, total=False):
    abort: GrpcRouteFaultInjectionPolicyAbort
    delay: GrpcRouteFaultInjectionPolicyDelay

@typing.type_check_only
class GrpcRouteFaultInjectionPolicyAbort(typing.TypedDict, total=False):
    httpStatus: int
    percentage: int

@typing.type_check_only
class GrpcRouteFaultInjectionPolicyDelay(typing.TypedDict, total=False):
    fixedDelay: str
    percentage: int

@typing.type_check_only
class GrpcRouteHeaderMatch(typing.TypedDict, total=False):
    key: str
    type: typing.Literal["TYPE_UNSPECIFIED", "EXACT", "REGULAR_EXPRESSION"]
    value: str

@typing.type_check_only
class GrpcRouteMethodMatch(typing.TypedDict, total=False):
    caseSensitive: bool
    grpcMethod: str
    grpcService: str
    type: typing.Literal["TYPE_UNSPECIFIED", "EXACT", "REGULAR_EXPRESSION"]

@typing.type_check_only
class GrpcRouteRetryPolicy(typing.TypedDict, total=False):
    numRetries: int
    retryConditions: _list[str]

@typing.type_check_only
class GrpcRouteRouteAction(typing.TypedDict, total=False):
    destinations: _list[GrpcRouteDestination]
    faultInjectionPolicy: GrpcRouteFaultInjectionPolicy
    idleTimeout: str
    retryPolicy: GrpcRouteRetryPolicy
    statefulSessionAffinity: GrpcRouteStatefulSessionAffinityPolicy
    timeout: str

@typing.type_check_only
class GrpcRouteRouteMatch(typing.TypedDict, total=False):
    headers: _list[GrpcRouteHeaderMatch]
    method: GrpcRouteMethodMatch

@typing.type_check_only
class GrpcRouteRouteRule(typing.TypedDict, total=False):
    action: GrpcRouteRouteAction
    matches: _list[GrpcRouteRouteMatch]

@typing.type_check_only
class GrpcRouteStatefulSessionAffinityPolicy(typing.TypedDict, total=False):
    cookieTtl: str

@typing.type_check_only
class HttpRoute(typing.TypedDict, total=False):
    createTime: str
    description: str
    gateways: _list[str]
    hostnames: _list[str]
    labels: dict[str, typing.Any]
    meshes: _list[str]
    name: str
    rules: _list[HttpRouteRouteRule]
    selfLink: str
    updateTime: str

@typing.type_check_only
class HttpRouteCorsPolicy(typing.TypedDict, total=False):
    allowCredentials: bool
    allowHeaders: _list[str]
    allowMethods: _list[str]
    allowOriginRegexes: _list[str]
    allowOrigins: _list[str]
    disabled: bool
    exposeHeaders: _list[str]
    maxAge: str

@typing.type_check_only
class HttpRouteDestination(typing.TypedDict, total=False):
    requestHeaderModifier: HttpRouteHeaderModifier
    responseHeaderModifier: HttpRouteHeaderModifier
    serviceName: str
    weight: int

@typing.type_check_only
class HttpRouteFaultInjectionPolicy(typing.TypedDict, total=False):
    abort: HttpRouteFaultInjectionPolicyAbort
    delay: HttpRouteFaultInjectionPolicyDelay

@typing.type_check_only
class HttpRouteFaultInjectionPolicyAbort(typing.TypedDict, total=False):
    httpStatus: int
    percentage: int

@typing.type_check_only
class HttpRouteFaultInjectionPolicyDelay(typing.TypedDict, total=False):
    fixedDelay: str
    percentage: int

@typing.type_check_only
class HttpRouteHeaderMatch(typing.TypedDict, total=False):
    exactMatch: str
    header: str
    invertMatch: bool
    prefixMatch: str
    presentMatch: bool
    rangeMatch: HttpRouteHeaderMatchIntegerRange
    regexMatch: str
    suffixMatch: str

@typing.type_check_only
class HttpRouteHeaderMatchIntegerRange(typing.TypedDict, total=False):
    end: int
    start: int

@typing.type_check_only
class HttpRouteHeaderModifier(typing.TypedDict, total=False):
    add: dict[str, typing.Any]
    remove: _list[str]
    set: dict[str, typing.Any]

@typing.type_check_only
class HttpRouteHttpDirectResponse(typing.TypedDict, total=False):
    bytesBody: str
    status: int
    stringBody: str

@typing.type_check_only
class HttpRouteQueryParameterMatch(typing.TypedDict, total=False):
    exactMatch: str
    presentMatch: bool
    queryParameter: str
    regexMatch: str

@typing.type_check_only
class HttpRouteRedirect(typing.TypedDict, total=False):
    hostRedirect: str
    httpsRedirect: bool
    pathRedirect: str
    portRedirect: int
    prefixRewrite: str
    responseCode: typing.Literal[
        "RESPONSE_CODE_UNSPECIFIED",
        "MOVED_PERMANENTLY_DEFAULT",
        "FOUND",
        "SEE_OTHER",
        "TEMPORARY_REDIRECT",
        "PERMANENT_REDIRECT",
    ]
    stripQuery: bool

@typing.type_check_only
class HttpRouteRequestMirrorPolicy(typing.TypedDict, total=False):
    destination: HttpRouteDestination
    mirrorPercent: float

@typing.type_check_only
class HttpRouteRetryPolicy(typing.TypedDict, total=False):
    numRetries: int
    perTryTimeout: str
    retryConditions: _list[str]

@typing.type_check_only
class HttpRouteRouteAction(typing.TypedDict, total=False):
    corsPolicy: HttpRouteCorsPolicy
    destinations: _list[HttpRouteDestination]
    directResponse: HttpRouteHttpDirectResponse
    faultInjectionPolicy: HttpRouteFaultInjectionPolicy
    idleTimeout: str
    redirect: HttpRouteRedirect
    requestHeaderModifier: HttpRouteHeaderModifier
    requestMirrorPolicy: HttpRouteRequestMirrorPolicy
    responseHeaderModifier: HttpRouteHeaderModifier
    retryPolicy: HttpRouteRetryPolicy
    statefulSessionAffinity: HttpRouteStatefulSessionAffinityPolicy
    timeout: str
    urlRewrite: HttpRouteURLRewrite

@typing.type_check_only
class HttpRouteRouteMatch(typing.TypedDict, total=False):
    fullPathMatch: str
    headers: _list[HttpRouteHeaderMatch]
    ignoreCase: bool
    prefixMatch: str
    queryParameters: _list[HttpRouteQueryParameterMatch]
    regexMatch: str

@typing.type_check_only
class HttpRouteRouteRule(typing.TypedDict, total=False):
    action: HttpRouteRouteAction
    matches: _list[HttpRouteRouteMatch]

@typing.type_check_only
class HttpRouteStatefulSessionAffinityPolicy(typing.TypedDict, total=False):
    cookieTtl: str

@typing.type_check_only
class HttpRouteURLRewrite(typing.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str

@typing.type_check_only
class LbEdgeExtension(typing.TypedDict, total=False):
    createTime: str
    description: str
    extensionChains: _list[ExtensionChain]
    forwardingRules: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    name: str
    updateTime: str

@typing.type_check_only
class LbRouteExtension(typing.TypedDict, total=False):
    createTime: str
    description: str
    extensionChains: _list[ExtensionChain]
    forwardingRules: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    metadata: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class LbTrafficExtension(typing.TypedDict, total=False):
    createTime: str
    description: str
    extensionChains: _list[ExtensionChain]
    forwardingRules: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    metadata: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class ListAgentConnectivityTemplatesResponse(typing.TypedDict, total=False):
    agentConnectivityTemplates: _list[AgentConnectivityTemplate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAgentGatewaysResponse(typing.TypedDict, total=False):
    agentGateways: _list[AgentGateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAuthzExtensionsResponse(typing.TypedDict, total=False):
    authzExtensions: _list[AuthzExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEndpointPoliciesResponse(typing.TypedDict, total=False):
    endpointPolicies: _list[EndpointPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExtensionBindingsResponse(typing.TypedDict, total=False):
    extensionBindings: _list[ExtensionBinding]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewayRouteViewsResponse(typing.TypedDict, total=False):
    gatewayRouteViews: _list[GatewayRouteView]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewaysResponse(typing.TypedDict, total=False):
    gateways: _list[Gateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGrpcRoutesResponse(typing.TypedDict, total=False):
    grpcRoutes: _list[GrpcRoute]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListHttpRoutesResponse(typing.TypedDict, total=False):
    httpRoutes: _list[HttpRoute]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLbEdgeExtensionsResponse(typing.TypedDict, total=False):
    lbEdgeExtensions: _list[LbEdgeExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLbRouteExtensionsResponse(typing.TypedDict, total=False):
    lbRouteExtensions: _list[LbRouteExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLbTrafficExtensionsResponse(typing.TypedDict, total=False):
    lbTrafficExtensions: _list[LbTrafficExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMeshRouteViewsResponse(typing.TypedDict, total=False):
    meshRouteViews: _list[MeshRouteView]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMeshesResponse(typing.TypedDict, total=False):
    meshes: _list[Mesh]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMulticastConsumerAssociationsResponse(typing.TypedDict, total=False):
    multicastConsumerAssociations: _list[MulticastConsumerAssociation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMulticastGroupConsumerActivationsResponse(typing.TypedDict, total=False):
    multicastGroupConsumerActivations: _list[MulticastGroupConsumerActivation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListProducerExtensionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    producerExtensions: _list[ProducerExtension]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceBindingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    serviceBindings: _list[ServiceBinding]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceLbPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    serviceLbPolicies: _list[ServiceLbPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListTcpRoutesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tcpRoutes: _list[TcpRoute]
    unreachable: _list[str]

@typing.type_check_only
class ListTlsRoutesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tlsRoutes: _list[TlsRoute]
    unreachable: _list[str]

@typing.type_check_only
class ListWasmPluginVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    wasmPluginVersions: _list[WasmPluginVersion]

@typing.type_check_only
class ListWasmPluginsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    wasmPlugins: _list[WasmPlugin]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LoggingConfig(typing.TypedDict, total=False):
    logSeverity: typing.Literal[
        "LOG_SEVERITY_UNSPECIFIED",
        "NONE",
        "DEBUG",
        "INFO",
        "NOTICE",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "ALERT",
        "EMERGENCY",
    ]

@typing.type_check_only
class Mesh(typing.TypedDict, total=False):
    createTime: str
    description: str
    envoyHeaders: typing.Literal["ENVOY_HEADERS_UNSPECIFIED", "NONE", "DEBUG_HEADERS"]
    interceptionPort: int
    labels: dict[str, typing.Any]
    name: str
    selfLink: str
    updateTime: str

@typing.type_check_only
class MeshRouteView(typing.TypedDict, total=False):
    name: str
    routeId: str
    routeLocation: str
    routeProjectNumber: str
    routeType: str

@typing.type_check_only
class MulticastConsumerAssociation(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    multicastDomainActivation: str
    name: str
    network: str
    placementPolicy: str
    resourceState: typing.Literal[
        "CONSUMER_RESOURCE_STATE_UNSPECIFIED", "ACTIVE", "OBSOLETE"
    ]
    state: MulticastResourceState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MulticastGroupConsumerActivation(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    logConfig: MulticastLogConfig
    multicastConsumerAssociation: str
    multicastGroup: str
    multicastGroupRangeActivation: str
    name: str
    resourceState: typing.Literal[
        "CONSUMER_RESOURCE_STATE_UNSPECIFIED", "ACTIVE", "OBSOLETE"
    ]
    state: MulticastResourceState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MulticastLogConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class MulticastResourceState(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_ENUM_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "DELETE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
        "INACTIVE",
        "OBSOLETE",
    ]

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
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProducerExtension(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    extensionSettings: ProducerExtensionExtensionSettings
    labels: dict[str, typing.Any]
    name: str
    phase: typing.Literal["PHASE_UNSPECIFIED", "TRAFFIC", "AUTHZ"]
    updateTime: str

@typing.type_check_only
class ProducerExtensionExtensionSettings(typing.TypedDict, total=False):
    authority: str
    observabilityMode: bool
    service: str
    supportedEvents: _list[
        typing.Literal[
            "EVENT_TYPE_UNSPECIFIED",
            "REQUEST_HEADERS",
            "REQUEST_BODY",
            "RESPONSE_HEADERS",
            "RESPONSE_BODY",
            "REQUEST_TRAILERS",
            "RESPONSE_TRAILERS",
        ]
    ]

@typing.type_check_only
class RetryFilterPerRouteConfig(typing.TypedDict, total=False):
    cryptoKeyName: str

@typing.type_check_only
class ServiceBinding(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    service: str
    serviceId: str
    updateTime: str

@typing.type_check_only
class ServiceLbPolicy(typing.TypedDict, total=False):
    autoCapacityDrain: ServiceLbPolicyAutoCapacityDrain
    createTime: str
    description: str
    failoverConfig: ServiceLbPolicyFailoverConfig
    isolationConfig: ServiceLbPolicyIsolationConfig
    labels: dict[str, typing.Any]
    loadBalancingAlgorithm: typing.Literal[
        "LOAD_BALANCING_ALGORITHM_UNSPECIFIED",
        "SPRAY_TO_WORLD",
        "SPRAY_TO_REGION",
        "WATERFALL_BY_REGION",
        "WATERFALL_BY_ZONE",
    ]
    name: str
    updateTime: str

@typing.type_check_only
class ServiceLbPolicyAutoCapacityDrain(typing.TypedDict, total=False):
    enable: bool

@typing.type_check_only
class ServiceLbPolicyFailoverConfig(typing.TypedDict, total=False):
    failoverHealthThreshold: int

@typing.type_check_only
class ServiceLbPolicyIsolationConfig(typing.TypedDict, total=False):
    isolationGranularity: typing.Literal["ISOLATION_GRANULARITY_UNSPECIFIED", "REGION"]
    isolationMode: typing.Literal["ISOLATION_MODE_UNSPECIFIED", "NEAREST", "STRICT"]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TcpRoute(typing.TypedDict, total=False):
    createTime: str
    description: str
    gateways: _list[str]
    labels: dict[str, typing.Any]
    meshes: _list[str]
    name: str
    rules: _list[TcpRouteRouteRule]
    selfLink: str
    updateTime: str

@typing.type_check_only
class TcpRouteRouteAction(typing.TypedDict, total=False):
    destinations: _list[TcpRouteRouteDestination]
    idleTimeout: str
    originalDestination: bool

@typing.type_check_only
class TcpRouteRouteDestination(typing.TypedDict, total=False):
    serviceName: str
    weight: int

@typing.type_check_only
class TcpRouteRouteMatch(typing.TypedDict, total=False):
    address: str
    port: str

@typing.type_check_only
class TcpRouteRouteRule(typing.TypedDict, total=False):
    action: TcpRouteRouteAction
    matches: _list[TcpRouteRouteMatch]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TlsRoute(typing.TypedDict, total=False):
    createTime: str
    description: str
    gateways: _list[str]
    labels: dict[str, typing.Any]
    meshes: _list[str]
    name: str
    rules: _list[TlsRouteRouteRule]
    selfLink: str
    targetProxies: _list[str]
    updateTime: str

@typing.type_check_only
class TlsRouteRouteAction(typing.TypedDict, total=False):
    destinations: _list[TlsRouteRouteDestination]
    idleTimeout: str

@typing.type_check_only
class TlsRouteRouteDestination(typing.TypedDict, total=False):
    serviceName: str
    weight: int

@typing.type_check_only
class TlsRouteRouteMatch(typing.TypedDict, total=False):
    alpn: _list[str]
    sniHost: _list[str]

@typing.type_check_only
class TlsRouteRouteRule(typing.TypedDict, total=False):
    action: TlsRouteRouteAction
    matches: _list[TlsRouteRouteMatch]

@typing.type_check_only
class TrafficPortSelector(typing.TypedDict, total=False):
    ports: _list[str]

@typing.type_check_only
class WasmPlugin(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    logConfig: WasmPluginLogConfig
    mainVersionId: str
    name: str
    updateTime: str
    usedBy: _list[WasmPluginUsedBy]
    versions: dict[str, typing.Any]

@typing.type_check_only
class WasmPluginLogConfig(typing.TypedDict, total=False):
    enable: bool
    minLogLevel: typing.Literal[
        "LOG_LEVEL_UNSPECIFIED", "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"
    ]
    sampleRate: float

@typing.type_check_only
class WasmPluginUsedBy(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class WasmPluginVersion(typing.TypedDict, total=False):
    createTime: str
    description: str
    imageDigest: str
    imageUri: str
    labels: dict[str, typing.Any]
    name: str
    pluginConfigData: str
    pluginConfigDigest: str
    pluginConfigUri: str
    updateTime: str

@typing.type_check_only
class WasmPluginVersionDetails(typing.TypedDict, total=False):
    createTime: str
    description: str
    imageDigest: str
    imageUri: str
    labels: dict[str, typing.Any]
    pluginConfigData: str
    pluginConfigDigest: str
    pluginConfigUri: str
    updateTime: str
