import typing

import typing_extensions
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
    extensions: typing.List[typing.Dict[str, typing.Any]]
    origin: Peer
    request: Request
    resource: Resource
    response: Response
    source: Peer

@typing.type_check_only
class AuditLog(typing_extensions.TypedDict, total=False):
    authenticationInfo: AuthenticationInfo
    authorizationInfo: typing.List[AuthorizationInfo]
    metadata: typing.Dict[str, typing.Any]
    methodName: str
    numResponseItems: str
    request: typing.Dict[str, typing.Any]
    requestMetadata: RequestMetadata
    resourceLocation: ResourceLocation
    resourceName: str
    resourceOriginalState: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    serviceData: typing.Dict[str, typing.Any]
    serviceName: str
    status: Status

@typing.type_check_only
class Auth(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[str]
    audiences: typing.List[str]
    claims: typing.Dict[str, typing.Any]
    presenter: str
    principal: str

@typing.type_check_only
class AuthenticationInfo(typing_extensions.TypedDict, total=False):
    authoritySelector: str
    principalEmail: str
    principalSubject: str
    serviceAccountDelegationInfo: typing.List[ServiceAccountDelegationInfo]
    serviceAccountKeyName: str
    thirdPartyPrincipal: typing.Dict[str, typing.Any]

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
    resources: typing.List[ResourceInfo]
    serviceConfigId: str

@typing.type_check_only
class CheckResponse(typing_extensions.TypedDict, total=False):
    headers: typing.Dict[str, typing.Any]
    status: Status

@typing.type_check_only
class FirstPartyPrincipal(typing_extensions.TypedDict, total=False):
    principalEmail: str
    serviceMetadata: typing.Dict[str, typing.Any]

@typing.type_check_only
class Peer(typing_extensions.TypedDict, total=False):
    ip: str
    labels: typing.Dict[str, typing.Any]
    port: str
    principal: str
    regionCode: str

@typing.type_check_only
class ReportRequest(typing_extensions.TypedDict, total=False):
    operations: typing.List[AttributeContext]
    serviceConfigId: str

@typing.type_check_only
class ReportResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Request(typing_extensions.TypedDict, total=False):
    auth: Auth
    headers: typing.Dict[str, typing.Any]
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
    annotations: typing.Dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    labels: typing.Dict[str, typing.Any]
    location: str
    name: str
    service: str
    type: str
    uid: str
    updateTime: str

@typing.type_check_only
class ResourceInfo(typing_extensions.TypedDict, total=False):
    name: str
    permission: str
    type: str

@typing.type_check_only
class ResourceLocation(typing_extensions.TypedDict, total=False):
    currentLocations: typing.List[str]
    originalLocations: typing.List[str]

@typing.type_check_only
class Response(typing_extensions.TypedDict, total=False):
    backendLatency: str
    code: str
    headers: typing.Dict[str, typing.Any]
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
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ThirdPartyPrincipal(typing_extensions.TypedDict, total=False):
    thirdPartyClaims: typing.Dict[str, typing.Any]
