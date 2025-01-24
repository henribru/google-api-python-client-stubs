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
class AccessScope(typing_extensions.TypedDict, total=False):
    clientScope: ClientScope

@typing.type_check_only
class AccessSettings(typing_extensions.TypedDict, total=False):
    accessLevels: _list[str]
    sessionSettings: SessionSettings

@typing.type_check_only
class ApiOperation(typing_extensions.TypedDict, total=False):
    methodSelectors: _list[MethodSelector]
    serviceName: str

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    clientId: str
    name: str

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
class AuthorizedOrgsDesc(typing_extensions.TypedDict, total=False):
    assetType: typing_extensions.Literal[
        "ASSET_TYPE_UNSPECIFIED", "ASSET_TYPE_DEVICE", "ASSET_TYPE_CREDENTIAL_STRENGTH"
    ]
    authorizationDirection: typing_extensions.Literal[
        "AUTHORIZATION_DIRECTION_UNSPECIFIED",
        "AUTHORIZATION_DIRECTION_TO",
        "AUTHORIZATION_DIRECTION_FROM",
    ]
    authorizationType: typing_extensions.Literal[
        "AUTHORIZATION_TYPE_UNSPECIFIED", "AUTHORIZATION_TYPE_TRUST"
    ]
    name: str
    orgs: _list[str]

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
class ClientScope(typing_extensions.TypedDict, total=False):
    restrictedClientApplication: Application

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
    vpcNetworkSources: _list[VpcNetworkSource]

@typing.type_check_only
class CustomLevel(typing_extensions.TypedDict, total=False):
    expr: Expr

@typing.type_check_only
class DevicePolicy(typing_extensions.TypedDict, total=False):
    allowedDeviceManagementLevels: _list[
        typing_extensions.Literal["MANAGEMENT_UNSPECIFIED", "NONE", "BASIC", "COMPLETE"]
    ]
    allowedEncryptionStatuses: _list[
        typing_extensions.Literal[
            "ENCRYPTION_UNSPECIFIED",
            "ENCRYPTION_UNSUPPORTED",
            "UNENCRYPTED",
            "ENCRYPTED",
        ]
    ]
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
    sourceRestriction: typing_extensions.Literal[
        "SOURCE_RESTRICTION_UNSPECIFIED",
        "SOURCE_RESTRICTION_ENABLED",
        "SOURCE_RESTRICTION_DISABLED",
    ]
    sources: _list[EgressSource]

@typing.type_check_only
class EgressPolicy(typing_extensions.TypedDict, total=False):
    egressFrom: EgressFrom
    egressTo: EgressTo
    title: str

@typing.type_check_only
class EgressSource(typing_extensions.TypedDict, total=False):
    accessLevel: str
    resource: str

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
    dryRunAccessLevels: _list[str]
    groupKey: str
    name: str
    restrictedClientApplications: _list[Application]
    scopedAccessSettings: _list[ScopedAccessSettings]
    sessionSettings: SessionSettings

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
    title: str

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
class ListAuthorizedOrgsDescsResponse(typing_extensions.TypedDict, total=False):
    authorizedOrgsDescs: _list[AuthorizedOrgsDesc]
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
class ListSupportedServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    supportedServices: _list[SupportedService]

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
class ScopedAccessSettings(typing_extensions.TypedDict, total=False):
    activeSettings: AccessSettings
    dryRunSettings: AccessSettings
    scope: AccessScope

@typing.type_check_only
class ServicePerimeter(typing_extensions.TypedDict, total=False):
    description: str
    etag: str
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
class SessionSettings(typing_extensions.TypedDict, total=False):
    maxInactivity: str
    sessionLength: str
    sessionLengthEnabled: bool
    sessionReauthMethod: typing_extensions.Literal[
        "SESSION_REAUTH_METHOD_UNSPECIFIED", "LOGIN", "SECURITY_KEY", "PASSWORD"
    ]
    useOidcMaxAge: bool

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
class SupportedService(typing_extensions.TypedDict, total=False):
    availableOnRestrictedVip: bool
    knownLimitations: bool
    name: str
    serviceSupportStage: typing_extensions.Literal[
        "SERVICE_SUPPORT_STAGE_UNSPECIFIED", "GA", "PREVIEW", "DEPRECATED"
    ]
    supportStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED",
        "UNIMPLEMENTED",
        "PRELAUNCH",
        "EARLY_ACCESS",
        "ALPHA",
        "BETA",
        "GA",
        "DEPRECATED",
    ]
    supportedMethods: _list[MethodSelector]
    title: str

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

@typing.type_check_only
class VpcNetworkSource(typing_extensions.TypedDict, total=False):
    vpcSubnetwork: VpcSubNetwork

@typing.type_check_only
class VpcSubNetwork(typing_extensions.TypedDict, total=False):
    network: str
    vpcIpSubnetworks: _list[str]
