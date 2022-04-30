import typing

import typing_extensions

_list = list

@typing.type_check_only
class Api(typing_extensions.TypedDict, total=False):
    operation: str
    protocol: str
    service: str
    version: str

@typing.type_check_only
class AttributeContext(typing_extensions.TypedDict, total=False):
    api: Api
    destination: Peer
    extensions: _list[dict[str, typing.Any]]
    origin: Peer
    request: Request
    resource: Resource
    response: Response
    source: Peer

@typing.type_check_only
class AuditLog(typing_extensions.TypedDict, total=False):
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
class Auth(typing_extensions.TypedDict, total=False):
    accessLevels: _list[str]
    audiences: _list[str]
    claims: dict[str, typing.Any]
    presenter: str
    principal: str

@typing.type_check_only
class AuthenticationInfo(typing_extensions.TypedDict, total=False):
    authoritySelector: str
    principalEmail: str
    principalSubject: str
    serviceAccountDelegationInfo: _list[ServiceAccountDelegationInfo]
    serviceAccountKeyName: str
    thirdPartyPrincipal: dict[str, typing.Any]

@typing.type_check_only
class AuthorizationInfo(typing_extensions.TypedDict, total=False):
    granted: bool
    permission: str
    resource: str
    resourceAttributes: Resource

@typing.type_check_only
class CheckRequest(typing_extensions.TypedDict, total=False):
    attributes: AttributeContext
    flags: str
    resources: _list[ResourceInfo]
    serviceConfigId: str

@typing.type_check_only
class CheckResponse(typing_extensions.TypedDict, total=False):
    headers: dict[str, typing.Any]
    status: Status

@typing.type_check_only
class FirstPartyPrincipal(typing_extensions.TypedDict, total=False):
    principalEmail: str
    serviceMetadata: dict[str, typing.Any]

@typing.type_check_only
class OrgPolicyViolationInfo(typing_extensions.TypedDict, total=False):
    payload: dict[str, typing.Any]
    resourceTags: dict[str, typing.Any]
    resourceType: str
    violationInfo: _list[ViolationInfo]

@typing.type_check_only
class Peer(typing_extensions.TypedDict, total=False):
    ip: str
    labels: dict[str, typing.Any]
    port: str
    principal: str
    regionCode: str

@typing.type_check_only
class PolicyViolationInfo(typing_extensions.TypedDict, total=False):
    orgPolicyViolationInfo: OrgPolicyViolationInfo

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    operations: _list[AttributeContext]
    serviceConfigId: str

@typing.type_check_only
class ReportResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Request(typing_extensions.TypedDict, total=False):
    auth: Auth
    headers: dict[str, typing.Any]
    host: str
    id: str
    method: str
    path: str
    protocol: str
    query: str
    reason: str
    scheme: str
    size: str
    time: str

@typing.type_check_only
class RequestMetadata(typing_extensions.TypedDict, total=False):
    callerIp: str
    callerNetwork: str
    callerSuppliedUserAgent: str
    destinationAttributes: Peer
    requestAttributes: Request

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
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
class ResourceInfo(typing_extensions.TypedDict, total=False):
    container: str
    location: str
    name: str
    permission: str
    type: str

@typing.type_check_only
class ResourceLocation(typing_extensions.TypedDict, total=False):
    currentLocations: _list[str]
    originalLocations: _list[str]

@typing.type_check_only
class Response(typing_extensions.TypedDict, total=False):
    backendLatency: str
    code: str
    headers: dict[str, typing.Any]
    size: str
    time: str

@typing.type_check_only
class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    firstPartyPrincipal: FirstPartyPrincipal
    principalSubject: str
    thirdPartyPrincipal: ThirdPartyPrincipal

@typing.type_check_only
class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ThirdPartyPrincipal(typing_extensions.TypedDict, total=False):
    thirdPartyClaims: dict[str, typing.Any]

@typing.type_check_only
class V2HttpRequest(typing_extensions.TypedDict, total=False):
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
class V2LogEntry(typing_extensions.TypedDict, total=False):
    httpRequest: V2HttpRequest
    insertId: str
    labels: dict[str, typing.Any]
    monitoredResourceLabels: dict[str, typing.Any]
    name: str
    operation: V2LogEntryOperation
    protoPayload: dict[str, typing.Any]
    severity: typing_extensions.Literal[
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
class V2LogEntryOperation(typing_extensions.TypedDict, total=False):
    first: bool
    id: str
    last: bool
    producer: str

@typing.type_check_only
class V2LogEntrySourceLocation(typing_extensions.TypedDict, total=False):
    file: str
    function: str
    line: str

@typing.type_check_only
class ViolationInfo(typing_extensions.TypedDict, total=False):
    checkedValue: str
    constraint: str
    errorMessage: str
    policyType: typing_extensions.Literal[
        "POLICY_TYPE_UNSPECIFIED",
        "BOOLEAN_CONSTRAINT",
        "LIST_CONSTRAINT",
        "CUSTOM_CONSTRAINT",
    ]
