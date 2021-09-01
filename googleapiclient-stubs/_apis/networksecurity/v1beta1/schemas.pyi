import typing

import typing_extensions

@typing.type_check_only
class AuthorizationPolicy(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    createTime: str
    description: str
    labels: typing.Dict[str, typing.Any]
    name: str
    rules: typing.List[Rule]
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CertificateProviderInstance(typing_extensions.TypedDict, total=False):
    pluginInstance: str

@typing.type_check_only
class ClientTlsPolicy(typing_extensions.TypedDict, total=False):
    clientCertificate: GoogleCloudNetworksecurityV1beta1CertificateProvider
    createTime: str
    description: str
    labels: typing.Dict[str, typing.Any]
    name: str
    serverValidationCa: typing.List[ValidationCA]
    sni: str
    updateTime: str

@typing.type_check_only
class Destination(typing_extensions.TypedDict, total=False):
    hosts: typing.List[str]
    httpHeaderMatch: HttpHeaderMatch
    methods: typing.List[str]
    ports: typing.List[int]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleCloudNetworksecurityV1beta1CertificateProvider(
    typing_extensions.TypedDict, total=False
):
    certificateProviderInstance: CertificateProviderInstance
    grpcEndpoint: GoogleCloudNetworksecurityV1beta1GrpcEndpoint

@typing.type_check_only
class GoogleCloudNetworksecurityV1beta1GrpcEndpoint(
    typing_extensions.TypedDict, total=False
):
    targetUri: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[GoogleIamV1AuditConfig]
    bindings: typing.List[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class HttpHeaderMatch(typing_extensions.TypedDict, total=False):
    headerName: str
    regexMatch: str

@typing.type_check_only
class ListAuthorizationPoliciesResponse(typing_extensions.TypedDict, total=False):
    authorizationPolicies: typing.List[AuthorizationPolicy]
    nextPageToken: str

@typing.type_check_only
class ListClientTlsPoliciesResponse(typing_extensions.TypedDict, total=False):
    clientTlsPolicies: typing.List[ClientTlsPolicy]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListServerTlsPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serverTlsPolicies: typing.List[ServerTlsPolicy]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class MTLSPolicy(typing_extensions.TypedDict, total=False):
    clientValidationCa: typing.List[ValidationCA]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
class Rule(typing_extensions.TypedDict, total=False):
    destinations: typing.List[Destination]
    sources: typing.List[Source]

@typing.type_check_only
class ServerTlsPolicy(typing_extensions.TypedDict, total=False):
    allowOpen: bool
    createTime: str
    description: str
    labels: typing.Dict[str, typing.Any]
    mtlsPolicy: MTLSPolicy
    name: str
    serverCertificate: GoogleCloudNetworksecurityV1beta1CertificateProvider
    updateTime: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    ipBlocks: typing.List[str]
    principals: typing.List[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ValidationCA(typing_extensions.TypedDict, total=False):
    certificateProviderInstance: CertificateProviderInstance
    grpcEndpoint: GoogleCloudNetworksecurityV1beta1GrpcEndpoint
