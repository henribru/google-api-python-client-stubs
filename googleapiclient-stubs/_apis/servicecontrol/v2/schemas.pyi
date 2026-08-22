import typing

_list = list

@typing.type_check_only
class Api(typing.TypedDict, total=False):
    operation: str
    protocol: str
    service: str
    version: str

@typing.type_check_only
class AttributeContext(typing.TypedDict, total=False):
    api: Api
    destination: Peer
    extensions: _list[dict[str, typing.Any]]
    origin: Peer
    request: Request
    resource: Resource
    response: Response
    source: Peer

@typing.type_check_only
class AuditLog(typing.TypedDict, total=False):
    apiVersionIdentifier: str
    authenticationInfo: AuthenticationInfo
    authorizationInfo: _list[AuthorizationInfo]
    metadata: dict[str, typing.Any]
    methodName: str
    numResponseItems: str
    policyViolationInfo: PolicyViolationInfo
    request: dict[str, typing.Any]
    requestMetadata: RequestMetadata
    resourceLocation: ResourceLocation
    resourceName: str
    resourceOriginalState: dict[str, typing.Any]
    response: dict[str, typing.Any]
    serviceData: dict[str, typing.Any]
    serviceName: str
    status: Status

@typing.type_check_only
class Auth(typing.TypedDict, total=False):
    accessLevels: _list[str]
    audiences: _list[str]
    claims: dict[str, typing.Any]
    credentialId: str
    oauth: Oauth
    presenter: str
    principal: str

@typing.type_check_only
class AuthenticationInfo(typing.TypedDict, total=False):
    authoritySelector: str
    loggableShortLivedCredential: dict[str, typing.Any]
    oauthInfo: OAuthInfo
    principalEmail: str
    principalSubject: str
    serviceAccountDelegationInfo: _list[ServiceAccountDelegationInfo]
    serviceAccountKeyName: str
    serviceDelegationHistory: ServiceDelegationHistory
    thirdPartyPrincipal: dict[str, typing.Any]

@typing.type_check_only
class AuthorizationInfo(typing.TypedDict, total=False):
    granted: bool
    permission: str
    permissionType: typing.Literal[
        "PERMISSION_TYPE_UNSPECIFIED",
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
    ]
    resource: str
    resourceAttributes: Resource

@typing.type_check_only
class CheckRequest(typing.TypedDict, total=False):
    attributes: AttributeContext
    flags: str
    resources: _list[ResourceInfo]
    serviceConfigId: str

@typing.type_check_only
class CheckResponse(typing.TypedDict, total=False):
    dynamicMetadata: dict[str, typing.Any]
    headers: dict[str, typing.Any]
    status: Status

@typing.type_check_only
class FirstPartyPrincipal(typing.TypedDict, total=False):
    principalEmail: str
    serviceMetadata: dict[str, typing.Any]

@typing.type_check_only
class OAuthInfo(typing.TypedDict, total=False):
    oauthClientId: str

@typing.type_check_only
class Oauth(typing.TypedDict, total=False):
    clientId: str

@typing.type_check_only
class OrgPolicyViolationInfo(typing.TypedDict, total=False):
    payload: dict[str, typing.Any]
    resourceTags: dict[str, typing.Any]
    resourceType: str
    violationInfo: _list[ViolationInfo]

@typing.type_check_only
class Peer(typing.TypedDict, total=False):
    ip: str
    labels: dict[str, typing.Any]
    port: str
    principal: str
    regionCode: str

@typing.type_check_only
class PolicyViolationInfo(typing.TypedDict, total=False):
    orgPolicyViolationInfo: OrgPolicyViolationInfo

@typing.type_check_only
class ReportRequest(typing.TypedDict, total=False):
    operations: _list[AttributeContext]
    serviceConfigId: str

@typing.type_check_only
class ReportResponse(typing.TypedDict, total=False):
    extensions: dict[str, typing.Any]

@typing.type_check_only
class Request(typing.TypedDict, total=False):
    auth: Auth
    headers: dict[str, typing.Any]
    host: str
    id: str
    method: str
    origin: str
    path: str
    protocol: str
    query: str
    reason: str
    scheme: str
    size: str
    time: str

@typing.type_check_only
class RequestMetadata(typing.TypedDict, total=False):
    callerIp: str
    callerNetwork: str
    callerSuppliedUserAgent: str
    destinationAttributes: Peer
    requestAttributes: Request

@typing.type_check_only
class Resource(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    location: str
    name: str
    service: str
    type: str
    uid: str
    updateTime: str

@typing.type_check_only
class ResourceInfo(typing.TypedDict, total=False):
    container: str
    location: str
    name: str
    permission: str
    type: str

@typing.type_check_only
class ResourceLocation(typing.TypedDict, total=False):
    currentLocations: _list[str]
    originalLocations: _list[str]

@typing.type_check_only
class Response(typing.TypedDict, total=False):
    backendLatency: str
    code: str
    headers: dict[str, typing.Any]
    size: str
    time: str

@typing.type_check_only
class ServiceAccountDelegationInfo(typing.TypedDict, total=False):
    firstPartyPrincipal: FirstPartyPrincipal
    principalSubject: str
    thirdPartyPrincipal: ThirdPartyPrincipal

@typing.type_check_only
class ServiceDelegationHistory(typing.TypedDict, total=False):
    originalPrincipal: str
    serviceMetadata: _list[ServiceMetadata]

@typing.type_check_only
class ServiceMetadata(typing.TypedDict, total=False):
    jobMetadata: dict[str, typing.Any]
    principalSubject: str
    serviceDomain: str

@typing.type_check_only
class SpanContext(typing.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ThirdPartyPrincipal(typing.TypedDict, total=False):
    thirdPartyClaims: dict[str, typing.Any]

@typing.type_check_only
class V2HttpRequest(typing.TypedDict, total=False):
    cacheFillBytes: str
    cacheHit: bool
    cacheLookup: bool
    cacheValidatedWithOriginServer: bool
    latency: str
    protocol: str
    referer: str
    remoteIp: str
    requestMethod: str
    requestSize: str
    requestUrl: str
    responseSize: str
    serverIp: str
    status: int
    userAgent: str

@typing.type_check_only
class V2LogEntry(typing.TypedDict, total=False):
    httpRequest: V2HttpRequest
    insertId: str
    labels: dict[str, typing.Any]
    monitoredResourceLabels: dict[str, typing.Any]
    name: str
    operation: V2LogEntryOperation
    protoPayload: dict[str, typing.Any]
    severity: typing.Literal[
        "DEFAULT",
        "DEBUG",
        "INFO",
        "NOTICE",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "ALERT",
        "EMERGENCY",
    ]
    sourceLocation: V2LogEntrySourceLocation
    structPayload: dict[str, typing.Any]
    textPayload: str
    timestamp: str
    trace: str

@typing.type_check_only
class V2LogEntryOperation(typing.TypedDict, total=False):
    first: bool
    id: str
    last: bool
    producer: str

@typing.type_check_only
class V2LogEntrySourceLocation(typing.TypedDict, total=False):
    file: str
    function: str
    line: str

@typing.type_check_only
class V2ResourceEvent(typing.TypedDict, total=False):
    contextId: str
    destinations: str
    parent: Resource
    path: typing.Literal["API_PATH_UNSPECIFIED", "REQUEST", "RESPONSE"]
    payload: dict[str, typing.Any]
    resource: Resource
    type: typing.Literal["TYPE_UNSPECIFIED", "CREATE", "UPDATE", "DELETE", "UNDELETE"]

@typing.type_check_only
class ViolationInfo(typing.TypedDict, total=False):
    checkedValue: str
    constraint: str
    constraintViolationInfo: dict[str, typing.Any]
    errorMessage: str
    policyType: typing.Literal[
        "POLICY_TYPE_UNSPECIFIED",
        "BOOLEAN_CONSTRAINT",
        "LIST_CONSTRAINT",
        "CUSTOM_CONSTRAINT",
    ]
