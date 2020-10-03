import typing

import typing_extensions

class ReportResponse(typing_extensions.TypedDict, total=False): ...

class Peer(typing_extensions.TypedDict, total=False):
    principal: str
    ip: str
    labels: typing.Dict[str, typing.Any]
    port: str
    regionCode: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class AttributeContext(typing_extensions.TypedDict, total=False):
    extensions: typing.List[typing.Dict[str, typing.Any]]
    source: Peer
    api: Api
    response: Response
    origin: Peer
    destination: Peer
    request: Request
    resource: Resource

class RequestMetadata(typing_extensions.TypedDict, total=False):
    destinationAttributes: Peer
    requestAttributes: Request
    callerNetwork: str
    callerSuppliedUserAgent: str
    callerIp: str

class CheckRequest(typing_extensions.TypedDict, total=False):
    attributes: AttributeContext
    serviceConfigId: str
    resources: typing.List[ResourceInfo]

class AuthenticationInfo(typing_extensions.TypedDict, total=False):
    serviceAccountDelegationInfo: typing.List[ServiceAccountDelegationInfo]
    authoritySelector: str
    principalSubject: str
    principalEmail: str
    serviceAccountKeyName: str
    thirdPartyPrincipal: typing.Dict[str, typing.Any]

class Api(typing_extensions.TypedDict, total=False):
    operation: str
    service: str
    version: str
    protocol: str

class AuthorizationInfo(typing_extensions.TypedDict, total=False):
    permission: str
    resource: str
    granted: bool
    resourceAttributes: Resource

class ResourceLocation(typing_extensions.TypedDict, total=False):
    originalLocations: typing.List[str]
    currentLocations: typing.List[str]

class Response(typing_extensions.TypedDict, total=False):
    size: str
    headers: typing.Dict[str, typing.Any]
    time: str
    code: str

class Resource(typing_extensions.TypedDict, total=False):
    service: str
    labels: typing.Dict[str, typing.Any]
    type: str
    name: str

class Request(typing_extensions.TypedDict, total=False):
    size: str
    protocol: str
    host: str
    auth: Auth
    time: str
    reason: str
    query: str
    id: str
    method: str
    scheme: str
    path: str
    headers: typing.Dict[str, typing.Any]

class AuditLog(typing_extensions.TypedDict, total=False):
    authorizationInfo: typing.List[AuthorizationInfo]
    status: Status
    resourceLocation: ResourceLocation
    response: typing.Dict[str, typing.Any]
    authenticationInfo: AuthenticationInfo
    methodName: str
    numResponseItems: str
    serviceName: str
    resourceName: str
    serviceData: typing.Dict[str, typing.Any]
    resourceOriginalState: typing.Dict[str, typing.Any]
    requestMetadata: RequestMetadata
    metadata: typing.Dict[str, typing.Any]
    request: typing.Dict[str, typing.Any]

class SpanContext(typing_extensions.TypedDict, total=False):
    spanName: str

class FirstPartyPrincipal(typing_extensions.TypedDict, total=False):
    serviceMetadata: typing.Dict[str, typing.Any]
    principalEmail: str

class ServiceAccountDelegationInfo(typing_extensions.TypedDict, total=False):
    firstPartyPrincipal: FirstPartyPrincipal
    thirdPartyPrincipal: ThirdPartyPrincipal

class ThirdPartyPrincipal(typing_extensions.TypedDict, total=False):
    thirdPartyClaims: typing.Dict[str, typing.Any]

class ReportRequest(typing_extensions.TypedDict, total=False):
    operations: typing.List[AttributeContext]
    serviceConfigId: str

class Auth(typing_extensions.TypedDict, total=False):
    principal: str
    presenter: str
    claims: typing.Dict[str, typing.Any]
    accessLevels: typing.List[str]
    audiences: typing.List[str]

class ResourceInfo(typing_extensions.TypedDict, total=False):
    name: str
    permission: str
    type: str

class CheckResponse(typing_extensions.TypedDict, total=False):
    status: Status
    headers: typing.Dict[str, typing.Any]
