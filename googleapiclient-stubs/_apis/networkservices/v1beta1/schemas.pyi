import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuthzExtension(typing_extensions.TypedDict, total=False):
    authority: str
    createTime: str
    description: str
    failOpen: bool
    forwardHeaders: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing_extensions.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    metadata: dict[str, typing.Any]
    name: str
    service: str
    timeout: str
    updateTime: str
    wireFormat: typing_extensions.Literal["WIRE_FORMAT_UNSPECIFIED", "EXT_PROC_GRPC"]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EndpointMatcher(typing_extensions.TypedDict, total=False):
    metadataLabelMatcher: MetadataLabelMatcher

@typing.type_check_only
class EndpointPolicy(typing_extensions.TypedDict, total=False):
    authorizationPolicy: str
    clientTlsPolicy: str
    createTime: str
    description: str
    endpointMatcher: EndpointMatcher
    labels: dict[str, typing.Any]
    name: str
    securityPolicy: str
    serverTlsPolicy: str
    trafficPortSelector: TrafficPortSelector
    type: typing_extensions.Literal[
        "ENDPOINT_POLICY_TYPE_UNSPECIFIED", "SIDECAR_PROXY", "GRPC_SERVER"
    ]
    updateTime: str

@typing.type_check_only
class ExtensionChain(typing_extensions.TypedDict, total=False):
    extensions: _list[ExtensionChainExtension]
    matchCondition: ExtensionChainMatchCondition
    name: str

@typing.type_check_only
class ExtensionChainExtension(typing_extensions.TypedDict, total=False):
    allowDynamicForwarding: bool
    authority: str
    failOpen: bool
    forwardHeaders: _list[str]
    metadata: dict[str, typing.Any]
    name: str
    requestBodySendMode: typing_extensions.Literal[
        "BODY_SEND_MODE_UNSPECIFIED",
        "BODY_SEND_MODE_STREAMED",
        "BODY_SEND_MODE_FULL_DUPLEX_STREAMED",
    ]
    responseBodySendMode: typing_extensions.Literal[
        "BODY_SEND_MODE_UNSPECIFIED",
        "BODY_SEND_MODE_STREAMED",
        "BODY_SEND_MODE_FULL_DUPLEX_STREAMED",
    ]
    service: str
    supportedEvents: _list[
        typing_extensions.Literal[
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
class ExtensionChainMatchCondition(typing_extensions.TypedDict, total=False):
    celExpression: str

@typing.type_check_only
class Gateway(typing_extensions.TypedDict, total=False):
    addresses: _list[str]
    certificateUrls: _list[str]
    createTime: str
    description: str
    envoyHeaders: typing_extensions.Literal[
        "ENVOY_HEADERS_UNSPECIFIED", "NONE", "DEBUG_HEADERS"
    ]
    gatewaySecurityPolicy: str
    ipVersion: typing_extensions.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    labels: dict[str, typing.Any]
    name: str
    network: str
    ports: _list[int]
    routingMode: typing_extensions.Literal[
        "EXPLICIT_ROUTING_MODE", "NEXT_HOP_ROUTING_MODE"
    ]
    scope: str
    selfLink: str
    serverTlsPolicy: str
    subnetwork: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "OPEN_MESH", "SECURE_WEB_GATEWAY"
    ]
    updateTime: str

@typing.type_check_only
class GatewayRouteView(typing_extensions.TypedDict, total=False):
    name: str
    routeId: str
    routeLocation: str
    routeProjectNumber: str
    routeType: str

@typing.type_check_only
class GrpcRoute(typing_extensions.TypedDict, total=False):
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
class GrpcRouteDestination(typing_extensions.TypedDict, total=False):
    serviceName: str
    weight: int

@typing.type_check_only
class GrpcRouteFaultInjectionPolicy(typing_extensions.TypedDict, total=False):
    abort: GrpcRouteFaultInjectionPolicyAbort
    delay: GrpcRouteFaultInjectionPolicyDelay

@typing.type_check_only
class GrpcRouteFaultInjectionPolicyAbort(typing_extensions.TypedDict, total=False):
    httpStatus: int
    percentage: int

@typing.type_check_only
class GrpcRouteFaultInjectionPolicyDelay(typing_extensions.TypedDict, total=False):
    fixedDelay: str
    percentage: int

@typing.type_check_only
class GrpcRouteHeaderMatch(typing_extensions.TypedDict, total=False):
    key: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXACT", "REGULAR_EXPRESSION"]
    value: str

@typing.type_check_only
class GrpcRouteMethodMatch(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    grpcMethod: str
    grpcService: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "EXACT", "REGULAR_EXPRESSION"]

@typing.type_check_only
class GrpcRouteRetryPolicy(typing_extensions.TypedDict, total=False):
    numRetries: int
    retryConditions: _list[str]

@typing.type_check_only
class GrpcRouteRouteAction(typing_extensions.TypedDict, total=False):
    destinations: _list[GrpcRouteDestination]
    faultInjectionPolicy: GrpcRouteFaultInjectionPolicy
    idleTimeout: str
    retryPolicy: GrpcRouteRetryPolicy
    statefulSessionAffinity: GrpcRouteStatefulSessionAffinityPolicy
    timeout: str

@typing.type_check_only
class GrpcRouteRouteMatch(typing_extensions.TypedDict, total=False):
    headers: _list[GrpcRouteHeaderMatch]
    method: GrpcRouteMethodMatch

@typing.type_check_only
class GrpcRouteRouteRule(typing_extensions.TypedDict, total=False):
    action: GrpcRouteRouteAction
    matches: _list[GrpcRouteRouteMatch]

@typing.type_check_only
class GrpcRouteStatefulSessionAffinityPolicy(typing_extensions.TypedDict, total=False):
    cookieTtl: str

@typing.type_check_only
class HttpRoute(typing_extensions.TypedDict, total=False):
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
class HttpRouteCorsPolicy(typing_extensions.TypedDict, total=False):
    allowCredentials: bool
    allowHeaders: _list[str]
    allowMethods: _list[str]
    allowOriginRegexes: _list[str]
    allowOrigins: _list[str]
    disabled: bool
    exposeHeaders: _list[str]
    maxAge: str

@typing.type_check_only
class HttpRouteDestination(typing_extensions.TypedDict, total=False):
    requestHeaderModifier: HttpRouteHeaderModifier
    responseHeaderModifier: HttpRouteHeaderModifier
    serviceName: str
    weight: int

@typing.type_check_only
class HttpRouteFaultInjectionPolicy(typing_extensions.TypedDict, total=False):
    abort: HttpRouteFaultInjectionPolicyAbort
    delay: HttpRouteFaultInjectionPolicyDelay

@typing.type_check_only
class HttpRouteFaultInjectionPolicyAbort(typing_extensions.TypedDict, total=False):
    httpStatus: int
    percentage: int

@typing.type_check_only
class HttpRouteFaultInjectionPolicyDelay(typing_extensions.TypedDict, total=False):
    fixedDelay: str
    percentage: int

@typing.type_check_only
class HttpRouteHeaderMatch(typing_extensions.TypedDict, total=False):
    exactMatch: str
    header: str
    invertMatch: bool
    prefixMatch: str
    presentMatch: bool
    rangeMatch: HttpRouteHeaderMatchIntegerRange
    regexMatch: str
    suffixMatch: str

@typing.type_check_only
class HttpRouteHeaderMatchIntegerRange(typing_extensions.TypedDict, total=False):
    end: int
    start: int

@typing.type_check_only
class HttpRouteHeaderModifier(typing_extensions.TypedDict, total=False):
    add: dict[str, typing.Any]
    remove: _list[str]
    set: dict[str, typing.Any]

@typing.type_check_only
class HttpRouteHttpDirectResponse(typing_extensions.TypedDict, total=False):
    bytesBody: str
    status: int
    stringBody: str

@typing.type_check_only
class HttpRouteQueryParameterMatch(typing_extensions.TypedDict, total=False):
    exactMatch: str
    presentMatch: bool
    queryParameter: str
    regexMatch: str

@typing.type_check_only
class HttpRouteRedirect(typing_extensions.TypedDict, total=False):
    hostRedirect: str
    httpsRedirect: bool
    pathRedirect: str
    portRedirect: int
    prefixRewrite: str
    responseCode: typing_extensions.Literal[
        "RESPONSE_CODE_UNSPECIFIED",
        "MOVED_PERMANENTLY_DEFAULT",
        "FOUND",
        "SEE_OTHER",
        "TEMPORARY_REDIRECT",
        "PERMANENT_REDIRECT",
    ]
    stripQuery: bool

@typing.type_check_only
class HttpRouteRequestMirrorPolicy(typing_extensions.TypedDict, total=False):
    destination: HttpRouteDestination
    mirrorPercent: float

@typing.type_check_only
class HttpRouteRetryPolicy(typing_extensions.TypedDict, total=False):
    numRetries: int
    perTryTimeout: str
    retryConditions: _list[str]

@typing.type_check_only
class HttpRouteRouteAction(typing_extensions.TypedDict, total=False):
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
class HttpRouteRouteMatch(typing_extensions.TypedDict, total=False):
    fullPathMatch: str
    headers: _list[HttpRouteHeaderMatch]
    ignoreCase: bool
    prefixMatch: str
    queryParameters: _list[HttpRouteQueryParameterMatch]
    regexMatch: str

@typing.type_check_only
class HttpRouteRouteRule(typing_extensions.TypedDict, total=False):
    action: HttpRouteRouteAction
    matches: _list[HttpRouteRouteMatch]

@typing.type_check_only
class HttpRouteStatefulSessionAffinityPolicy(typing_extensions.TypedDict, total=False):
    cookieTtl: str

@typing.type_check_only
class HttpRouteURLRewrite(typing_extensions.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str

@typing.type_check_only
class LbEdgeExtension(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    extensionChains: _list[ExtensionChain]
    forwardingRules: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing_extensions.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    name: str
    updateTime: str

@typing.type_check_only
class LbRouteExtension(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    extensionChains: _list[ExtensionChain]
    forwardingRules: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing_extensions.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    metadata: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class LbTrafficExtension(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    extensionChains: _list[ExtensionChain]
    forwardingRules: _list[str]
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing_extensions.Literal[
        "LOAD_BALANCING_SCHEME_UNSPECIFIED", "INTERNAL_MANAGED", "EXTERNAL_MANAGED"
    ]
    metadata: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class ListAuthzExtensionsResponse(typing_extensions.TypedDict, total=False):
    authzExtensions: _list[AuthzExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListEndpointPoliciesResponse(typing_extensions.TypedDict, total=False):
    endpointPolicies: _list[EndpointPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewayRouteViewsResponse(typing_extensions.TypedDict, total=False):
    gatewayRouteViews: _list[GatewayRouteView]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGatewaysResponse(typing_extensions.TypedDict, total=False):
    gateways: _list[Gateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGrpcRoutesResponse(typing_extensions.TypedDict, total=False):
    grpcRoutes: _list[GrpcRoute]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListHttpRoutesResponse(typing_extensions.TypedDict, total=False):
    httpRoutes: _list[HttpRoute]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLbEdgeExtensionsResponse(typing_extensions.TypedDict, total=False):
    lbEdgeExtensions: _list[LbEdgeExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLbRouteExtensionsResponse(typing_extensions.TypedDict, total=False):
    lbRouteExtensions: _list[LbRouteExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLbTrafficExtensionsResponse(typing_extensions.TypedDict, total=False):
    lbTrafficExtensions: _list[LbTrafficExtension]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMeshRouteViewsResponse(typing_extensions.TypedDict, total=False):
    meshRouteViews: _list[MeshRouteView]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMeshesResponse(typing_extensions.TypedDict, total=False):
    meshes: _list[Mesh]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListServiceBindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceBindings: _list[ServiceBinding]
    unreachable: _list[str]

@typing.type_check_only
class ListServiceLbPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceLbPolicies: _list[ServiceLbPolicy]
    unreachable: _list[str]

@typing.type_check_only
class ListTcpRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tcpRoutes: _list[TcpRoute]
    unreachable: _list[str]

@typing.type_check_only
class ListTlsRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tlsRoutes: _list[TlsRoute]
    unreachable: _list[str]

@typing.type_check_only
class ListWasmPluginVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    wasmPluginVersions: _list[WasmPluginVersion]

@typing.type_check_only
class ListWasmPluginsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    wasmPlugins: _list[WasmPlugin]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LoggingConfig(typing_extensions.TypedDict, total=False):
    logSeverity: typing_extensions.Literal[
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
class Mesh(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    envoyHeaders: typing_extensions.Literal[
        "ENVOY_HEADERS_UNSPECIFIED", "NONE", "DEBUG_HEADERS"
    ]
    interceptionPort: int
    labels: dict[str, typing.Any]
    name: str
    selfLink: str
    updateTime: str

@typing.type_check_only
class MeshRouteView(typing_extensions.TypedDict, total=False):
    name: str
    routeId: str
    routeLocation: str
    routeProjectNumber: str
    routeType: str

@typing.type_check_only
class MetadataLabelMatcher(typing_extensions.TypedDict, total=False):
    metadataLabelMatchCriteria: typing_extensions.Literal[
        "METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED", "MATCH_ANY", "MATCH_ALL"
    ]
    metadataLabels: _list[MetadataLabels]

@typing.type_check_only
class MetadataLabels(typing_extensions.TypedDict, total=False):
    labelName: str
    labelValue: str

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
class RetryFilterPerRouteConfig(typing_extensions.TypedDict, total=False):
    cryptoKeyName: str

@typing.type_check_only
class ServiceBinding(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    service: str
    serviceId: str
    updateTime: str

@typing.type_check_only
class ServiceLbPolicy(typing_extensions.TypedDict, total=False):
    autoCapacityDrain: ServiceLbPolicyAutoCapacityDrain
    createTime: str
    description: str
    failoverConfig: ServiceLbPolicyFailoverConfig
    isolationConfig: ServiceLbPolicyIsolationConfig
    labels: dict[str, typing.Any]
    loadBalancingAlgorithm: typing_extensions.Literal[
        "LOAD_BALANCING_ALGORITHM_UNSPECIFIED",
        "SPRAY_TO_WORLD",
        "SPRAY_TO_REGION",
        "WATERFALL_BY_REGION",
        "WATERFALL_BY_ZONE",
    ]
    name: str
    updateTime: str

@typing.type_check_only
class ServiceLbPolicyAutoCapacityDrain(typing_extensions.TypedDict, total=False):
    enable: bool

@typing.type_check_only
class ServiceLbPolicyFailoverConfig(typing_extensions.TypedDict, total=False):
    failoverHealthThreshold: int

@typing.type_check_only
class ServiceLbPolicyIsolationConfig(typing_extensions.TypedDict, total=False):
    isolationGranularity: typing_extensions.Literal[
        "ISOLATION_GRANULARITY_UNSPECIFIED", "REGION"
    ]
    isolationMode: typing_extensions.Literal[
        "ISOLATION_MODE_UNSPECIFIED", "NEAREST", "STRICT"
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TcpRoute(typing_extensions.TypedDict, total=False):
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
class TcpRouteRouteAction(typing_extensions.TypedDict, total=False):
    destinations: _list[TcpRouteRouteDestination]
    idleTimeout: str
    originalDestination: bool

@typing.type_check_only
class TcpRouteRouteDestination(typing_extensions.TypedDict, total=False):
    serviceName: str
    weight: int

@typing.type_check_only
class TcpRouteRouteMatch(typing_extensions.TypedDict, total=False):
    address: str
    port: str

@typing.type_check_only
class TcpRouteRouteRule(typing_extensions.TypedDict, total=False):
    action: TcpRouteRouteAction
    matches: _list[TcpRouteRouteMatch]

@typing.type_check_only
class TlsRoute(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    gateways: _list[str]
    labels: dict[str, typing.Any]
    meshes: _list[str]
    name: str
    rules: _list[TlsRouteRouteRule]
    selfLink: str
    updateTime: str

@typing.type_check_only
class TlsRouteRouteAction(typing_extensions.TypedDict, total=False):
    destinations: _list[TlsRouteRouteDestination]
    idleTimeout: str

@typing.type_check_only
class TlsRouteRouteDestination(typing_extensions.TypedDict, total=False):
    serviceName: str
    weight: int

@typing.type_check_only
class TlsRouteRouteMatch(typing_extensions.TypedDict, total=False):
    alpn: _list[str]
    sniHost: _list[str]

@typing.type_check_only
class TlsRouteRouteRule(typing_extensions.TypedDict, total=False):
    action: TlsRouteRouteAction
    matches: _list[TlsRouteRouteMatch]

@typing.type_check_only
class TrafficPortSelector(typing_extensions.TypedDict, total=False):
    ports: _list[str]

@typing.type_check_only
class WasmPlugin(typing_extensions.TypedDict, total=False):
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
class WasmPluginLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    minLogLevel: typing_extensions.Literal[
        "LOG_LEVEL_UNSPECIFIED", "TRACE", "DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"
    ]
    sampleRate: float

@typing.type_check_only
class WasmPluginUsedBy(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class WasmPluginVersion(typing_extensions.TypedDict, total=False):
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
class WasmPluginVersionDetails(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    imageDigest: str
    imageUri: str
    labels: dict[str, typing.Any]
    pluginConfigData: str
    pluginConfigDigest: str
    pluginConfigUri: str
    updateTime: str
