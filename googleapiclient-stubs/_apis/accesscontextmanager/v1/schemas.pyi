import typing

_list = list

@typing.type_check_only
class AccessContextManagerOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class AccessLevel(typing.TypedDict, total=False):
    basic: BasicLevel
    custom: CustomLevel
    description: str
    name: str
    title: str

@typing.type_check_only
class AccessPolicy(typing.TypedDict, total=False):
    etag: str
    name: str
    parent: str
    scopes: _list[str]
    title: str

@typing.type_check_only
class AccessScope(typing.TypedDict, total=False):
    clientScope: ClientScope

@typing.type_check_only
class AccessSettings(typing.TypedDict, total=False):
    accessLevels: _list[str]
    sessionSettings: SessionSettings

@typing.type_check_only
class AddRequestHeader(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ApiOperation(typing.TypedDict, total=False):
    methodSelectors: _list[MethodSelector]
    serviceName: str

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    clientId: str
    name: str

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
class AuthorizedOrgsDesc(typing.TypedDict, total=False):
    assetType: typing.Literal[
        "ASSET_TYPE_UNSPECIFIED", "ASSET_TYPE_DEVICE", "ASSET_TYPE_CREDENTIAL_STRENGTH"
    ]
    authorizationDirection: typing.Literal[
        "AUTHORIZATION_DIRECTION_UNSPECIFIED",
        "AUTHORIZATION_DIRECTION_TO",
        "AUTHORIZATION_DIRECTION_FROM",
    ]
    authorizationType: typing.Literal[
        "AUTHORIZATION_TYPE_UNSPECIFIED", "AUTHORIZATION_TYPE_TRUST"
    ]
    name: str
    orgs: _list[str]

@typing.type_check_only
class BasicLevel(typing.TypedDict, total=False):
    combiningFunction: typing.Literal["AND", "OR"]
    conditions: _list[Condition]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClientScope(typing.TypedDict, total=False):
    restrictedClientApplication: Application
    restrictedProject: Project

@typing.type_check_only
class CommitServicePerimetersRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class CommitServicePerimetersResponse(typing.TypedDict, total=False):
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class Condition(typing.TypedDict, total=False):
    devicePolicy: DevicePolicy
    ipSubnetworks: _list[str]
    members: _list[str]
    negate: bool
    regions: _list[str]
    requiredAccessLevels: _list[str]
    vpcNetworkSources: _list[VpcNetworkSource]

@typing.type_check_only
class CustomLevel(typing.TypedDict, total=False):
    expr: Expr

@typing.type_check_only
class DevicePolicy(typing.TypedDict, total=False):
    allowedDeviceManagementLevels: _list[
        typing.Literal["MANAGEMENT_UNSPECIFIED", "NONE", "BASIC", "COMPLETE"]
    ]
    allowedEncryptionStatuses: _list[
        typing.Literal[
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
class EgressFrom(typing.TypedDict, total=False):
    identities: _list[str]
    identityType: typing.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sourceRestriction: typing.Literal[
        "SOURCE_RESTRICTION_UNSPECIFIED",
        "SOURCE_RESTRICTION_ENABLED",
        "SOURCE_RESTRICTION_DISABLED",
    ]
    sources: _list[EgressSource]

@typing.type_check_only
class EgressPolicy(typing.TypedDict, total=False):
    egressFrom: EgressFrom
    egressTo: EgressTo
    title: str

@typing.type_check_only
class EgressSource(typing.TypedDict, total=False):
    accessLevel: str
    pscEndpoint: PrivateServiceConnectEndpoint
    resource: str

@typing.type_check_only
class EgressTo(typing.TypedDict, total=False):
    externalResources: _list[str]
    operations: _list[ApiOperation]
    resources: _list[str]
    roles: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcpUserAccessBinding(typing.TypedDict, total=False):
    accessLevels: _list[str]
    dryRunAccessLevels: _list[str]
    groupKey: str
    name: str
    principal: Principal
    restrictedClientApplications: _list[Application]
    scopedAccessSettings: _list[ScopedAccessSettings]
    sessionSettings: SessionSettings

@typing.type_check_only
class GcpUserAccessBindingOperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class IngressFrom(typing.TypedDict, total=False):
    identities: _list[str]
    identityType: typing.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sources: _list[IngressSource]

@typing.type_check_only
class IngressPolicy(typing.TypedDict, total=False):
    ingressFrom: IngressFrom
    ingressTo: IngressTo
    title: str

@typing.type_check_only
class IngressSource(typing.TypedDict, total=False):
    accessLevel: str
    pscEndpoint: PrivateServiceConnectEndpoint
    resource: str

@typing.type_check_only
class IngressTo(typing.TypedDict, total=False):
    operations: _list[ApiOperation]
    resources: _list[str]
    roles: _list[str]

@typing.type_check_only
class ListAccessLevelsResponse(typing.TypedDict, total=False):
    accessLevels: _list[AccessLevel]
    nextPageToken: str

@typing.type_check_only
class ListAccessPoliciesResponse(typing.TypedDict, total=False):
    accessPolicies: _list[AccessPolicy]
    nextPageToken: str

@typing.type_check_only
class ListAuthorizedOrgsDescsResponse(typing.TypedDict, total=False):
    authorizedOrgsDescs: _list[AuthorizedOrgsDesc]
    nextPageToken: str

@typing.type_check_only
class ListGcpUserAccessBindingsResponse(typing.TypedDict, total=False):
    gcpUserAccessBindings: _list[GcpUserAccessBinding]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListServicePerimetersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class ListSupportedPermissionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    supportedPermissions: _list[str]

@typing.type_check_only
class ListSupportedServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    supportedServices: _list[SupportedService]

@typing.type_check_only
class MethodSelector(typing.TypedDict, total=False):
    method: str
    permission: str

@typing.type_check_only
class Modifier(typing.TypedDict, total=False):
    addRequestHeader: AddRequestHeader

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OsConstraint(typing.TypedDict, total=False):
    minimumVersion: str
    osType: typing.Literal[
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
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Principal(typing.TypedDict, total=False):
    federatedPrincipal: str
    serviceAccount: str
    serviceAccountProjectNumber: str

@typing.type_check_only
class PrivateServiceConnectEndpoint(typing.TypedDict, total=False):
    forwardingRule: str

@typing.type_check_only
class Project(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class ReplaceAccessLevelsRequest(typing.TypedDict, total=False):
    accessLevels: _list[AccessLevel]
    etag: str

@typing.type_check_only
class ReplaceAccessLevelsResponse(typing.TypedDict, total=False):
    accessLevels: _list[AccessLevel]

@typing.type_check_only
class ReplaceServicePerimetersRequest(typing.TypedDict, total=False):
    etag: str
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class ReplaceServicePerimetersResponse(typing.TypedDict, total=False):
    servicePerimeters: _list[ServicePerimeter]

@typing.type_check_only
class ScopedAccessSettings(typing.TypedDict, total=False):
    activeSettings: AccessSettings
    dryRunSettings: AccessSettings
    scope: AccessScope

@typing.type_check_only
class ServicePattern(typing.TypedDict, total=False):
    modifiers: _list[Modifier]
    pattern: str
    service: str

@typing.type_check_only
class ServicePerimeter(typing.TypedDict, total=False):
    description: str
    etag: str
    name: str
    perimeterType: typing.Literal["PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"]
    spec: ServicePerimeterConfig
    status: ServicePerimeterConfig
    title: str
    useExplicitDryRunSpec: bool

@typing.type_check_only
class ServicePerimeterConfig(typing.TypedDict, total=False):
    accessLevels: _list[str]
    egressPolicies: _list[EgressPolicy]
    ingressPolicies: _list[IngressPolicy]
    resources: _list[str]
    restrictedServices: _list[str]
    vpcAccessibleServices: VpcAccessibleServices

@typing.type_check_only
class SessionSettings(typing.TypedDict, total=False):
    maxInactivity: str
    sessionLength: str
    sessionLengthEnabled: bool
    sessionReauthMethod: typing.Literal[
        "SESSION_REAUTH_METHOD_UNSPECIFIED", "LOGIN", "SECURITY_KEY", "PASSWORD"
    ]
    useOidcMaxAge: bool

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
class SupportedService(typing.TypedDict, total=False):
    availableOnRestrictedVip: bool
    knownLimitations: bool
    name: str
    serviceSupportStage: typing.Literal[
        "SERVICE_SUPPORT_STAGE_UNSPECIFIED", "GA", "PREVIEW", "DEPRECATED"
    ]
    supportStage: typing.Literal[
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
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class VpcAccessibleServices(typing.TypedDict, total=False):
    allowedServicePatterns: _list[ServicePattern]
    allowedServices: _list[str]
    enableRestriction: bool
    servicePatternsEnforcementScopes: _list[
        typing.Literal[
            "SERVICE_PATTERNS_ENFORCEMENT_SCOPE_UNSPECIFIED",
            "GOOGLE_APIS_VIA_PRIVATE_PATH",
        ]
    ]

@typing.type_check_only
class VpcNetworkSource(typing.TypedDict, total=False):
    vpcSubnetwork: VpcSubNetwork

@typing.type_check_only
class VpcSubNetwork(typing.TypedDict, total=False):
    network: str
    vpcIpSubnetworks: _list[str]
