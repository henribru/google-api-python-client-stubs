import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessContextManagerOperationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AccessLevel(typing_extensions.TypedDict, total=False):
    basic: BasicLevel
    custom: CustomLevel
    description: str
    name: str
    title: str

@typing.type_check_only
class AccessPolicy(typing_extensions.TypedDict, total=False):
    etag: str
    name: str
    parent: str
    scopes: _list[str]
    title: str

@typing.type_check_only
class ApiOperation(typing_extensions.TypedDict, total=False):
    methodSelectors: _list[MethodSelector]
    serviceName: str

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
class BasicLevel(typing_extensions.TypedDict, total=False):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: _list[Condition]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CommitServicePerimetersRequest(typing_extensions.TypedDict, total=False):
    etag: str

@typing.type_check_only
class CommitServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    devicePolicy: DevicePolicy
    ipSubnetworks: _list[str]
    members: _list[str]
    negate: bool
    regions: _list[str]
    requiredAccessLevels: _list[str]

@typing.type_check_only
class CustomLevel(typing_extensions.TypedDict, total=False):
    expr: Expr

@typing.type_check_only
class DevicePolicy(typing_extensions.TypedDict, total=False):
    allowedDeviceManagementLevels: _list[str]
    allowedEncryptionStatuses: _list[str]
    osConstraints: _list[OsConstraint]
    requireAdminApproval: bool
    requireCorpOwned: bool
    requireScreenlock: bool

@typing.type_check_only
class EgressFrom(typing_extensions.TypedDict, total=False):
    identities: _list[str]
    identityType: typing_extensions.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]

@typing.type_check_only
class EgressPolicy(typing_extensions.TypedDict, total=False):
    egressFrom: EgressFrom
    egressTo: EgressTo

@typing.type_check_only
class EgressTo(typing_extensions.TypedDict, total=False):
    externalResources: _list[str]
    operations: _list[ApiOperation]
    resources: _list[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcpUserAccessBinding(typing_extensions.TypedDict, total=False):
    accessLevels: _list[str]
    groupKey: str
    name: str

@typing.type_check_only
class GcpUserAccessBindingOperationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class IngressFrom(typing_extensions.TypedDict, total=False):
    identities: _list[str]
    identityType: typing_extensions.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sources: _list[IngressSource]

@typing.type_check_only
class IngressPolicy(typing_extensions.TypedDict, total=False):
    ingressFrom: IngressFrom
    ingressTo: IngressTo

@typing.type_check_only
class IngressSource(typing_extensions.TypedDict, total=False):
    accessLevel: str
    resource: str

@typing.type_check_only
class IngressTo(typing_extensions.TypedDict, total=False):
    operations: _list[ApiOperation]
    resources: _list[str]

@typing.type_check_only
class ListAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: _list[AccessLevel]
    nextPageToken: str

@typing.type_check_only
class ListAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    accessPolicies: _list[AccessPolicy]
    nextPageToken: str

@typing.type_check_only
class ListGcpUserAccessBindingsResponse(typing_extensions.TypedDict, total=False):
    gcpUserAccessBindings: _list[GcpUserAccessBinding]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class MethodSelector(typing_extensions.TypedDict, total=False):
    method: str
    permission: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OsConstraint(typing_extensions.TypedDict, total=False):
    minimumVersion: str
    osType: typing_extensions.Literal[
        "OS_UNSPECIFIED",
        "DESKTOP_MAC",
        "DESKTOP_WINDOWS",
        "DESKTOP_LINUX",
        "DESKTOP_CHROME_OS",
        "ANDROID",
        "IOS",
    ]
    requireVerifiedChromeOs: bool

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ReplaceAccessLevelsRequest(typing_extensions.TypedDict, total=False):
    accessLevels: _list[AccessLevel]
    etag: str

@typing.type_check_only
class ReplaceAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: _list[AccessLevel]

@typing.type_check_only
class ReplaceServicePerimetersRequest(typing_extensions.TypedDict, total=False):
    etag: str
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class ReplaceServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class ServicePerimeter(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    spec: ServicePerimeterConfig
    status: ServicePerimeterConfig
    title: str
    useExplicitDryRunSpec: bool

@typing.type_check_only
class ServicePerimeterConfig(typing_extensions.TypedDict, total=False):
    accessLevels: _list[str]
    egressPolicies: _list[EgressPolicy]
    ingressPolicies: _list[IngressPolicy]
    resources: _list[str]
    restrictedServices: _list[str]
    vpcAccessibleServices: VpcAccessibleServices

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
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class VpcAccessibleServices(typing_extensions.TypedDict, total=False):
    allowedServices: _list[str]
    enableRestriction: bool
