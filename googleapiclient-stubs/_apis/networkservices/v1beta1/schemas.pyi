import typing

import typing_extensions

_list = list

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
    serverTlsPolicy: str
    trafficPortSelector: TrafficPortSelector
    type: typing_extensions.Literal[
        "ENDPOINT_POLICY_TYPE_UNSPECIFIED", "SIDECAR_PROXY", "GRPC_SERVER"
    ]
    updateTime: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Gateway(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    ports: _list[int]
    scope: str
    selfLink: str
    serverTlsPolicy: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "OPEN_MESH", "SECURE_WEB_GATEWAY"
    ]
    updateTime: str

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
    retryPolicy: GrpcRouteRetryPolicy
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

@typing.type_check_only
class HttpRouteRetryPolicy(typing_extensions.TypedDict, total=False):
    numRetries: int
    perTryTimeout: str
    retryConditions: _list[str]

@typing.type_check_only
class HttpRouteRouteAction(typing_extensions.TypedDict, total=False):
    corsPolicy: HttpRouteCorsPolicy
    destinations: _list[HttpRouteDestination]
    faultInjectionPolicy: HttpRouteFaultInjectionPolicy
    redirect: HttpRouteRedirect
    requestHeaderModifier: HttpRouteHeaderModifier
    requestMirrorPolicy: HttpRouteRequestMirrorPolicy
    responseHeaderModifier: HttpRouteHeaderModifier
    retryPolicy: HttpRouteRetryPolicy
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
class HttpRouteURLRewrite(typing_extensions.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str

@typing.type_check_only
class ListEndpointPoliciesResponse(typing_extensions.TypedDict, total=False):
    endpointPolicies: _list[EndpointPolicy]
    nextPageToken: str

@typing.type_check_only
class ListGatewaysResponse(typing_extensions.TypedDict, total=False):
    gateways: _list[Gateway]
    nextPageToken: str

@typing.type_check_only
class ListGrpcRoutesResponse(typing_extensions.TypedDict, total=False):
    grpcRoutes: _list[GrpcRoute]
    nextPageToken: str

@typing.type_check_only
class ListHttpRoutesResponse(typing_extensions.TypedDict, total=False):
    httpRoutes: _list[HttpRoute]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMeshesResponse(typing_extensions.TypedDict, total=False):
    meshes: _list[Mesh]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListServiceBindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceBindings: _list[ServiceBinding]

@typing.type_check_only
class ListTcpRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tcpRoutes: _list[TcpRoute]

@typing.type_check_only
class ListTlsRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tlsRoutes: _list[TlsRoute]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Mesh(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    interceptionPort: int
    labels: dict[str, typing.Any]
    name: str
    selfLink: str
    updateTime: str

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
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ServiceBinding(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    service: str
    updateTime: str

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
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TlsRoute(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    gateways: _list[str]
    meshes: _list[str]
    name: str
    rules: _list[TlsRouteRouteRule]
    selfLink: str
    updateTime: str

@typing.type_check_only
class TlsRouteRouteAction(typing_extensions.TypedDict, total=False):
    destinations: _list[TlsRouteRouteDestination]

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
