import typing

import typing_extensions
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
    title: str

@typing.type_check_only
class ApiOperation(typing_extensions.TypedDict, total=False):
    methodSelectors: typing.List[MethodSelector]
    serviceName: str

@typing.type_check_only
class BasicLevel(typing_extensions.TypedDict, total=False):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: typing.List[Condition]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CommitServicePerimetersRequest(typing_extensions.TypedDict, total=False):
    etag: str

@typing.type_check_only
class CommitServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: typing.List[ServicePerimeter]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    devicePolicy: DevicePolicy
    ipSubnetworks: typing.List[str]
    members: typing.List[str]
    negate: bool
    regions: typing.List[str]
    requiredAccessLevels: typing.List[str]

@typing.type_check_only
class CustomLevel(typing_extensions.TypedDict, total=False):
    expr: Expr

@typing.type_check_only
class DevicePolicy(typing_extensions.TypedDict, total=False):
    allowedDeviceManagementLevels: typing.List[str]
    allowedEncryptionStatuses: typing.List[str]
    osConstraints: typing.List[OsConstraint]
    requireAdminApproval: bool
    requireCorpOwned: bool
    requireScreenlock: bool

@typing.type_check_only
class EgressFrom(typing_extensions.TypedDict, total=False):
    identities: typing.List[str]
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
    operations: typing.List[ApiOperation]
    resources: typing.List[str]

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
    accessLevels: typing.List[str]
    groupKey: str
    name: str

@typing.type_check_only
class IngressFrom(typing_extensions.TypedDict, total=False):
    identities: typing.List[str]
    identityType: typing_extensions.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sources: typing.List[IngressSource]

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
    operations: typing.List[ApiOperation]
    resources: typing.List[str]

@typing.type_check_only
class ListAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[AccessLevel]
    nextPageToken: str

@typing.type_check_only
class ListAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    accessPolicies: typing.List[AccessPolicy]
    nextPageToken: str

@typing.type_check_only
class ListGcpUserAccessBindingsResponse(typing_extensions.TypedDict, total=False):
    gcpUserAccessBindings: typing.List[GcpUserAccessBinding]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    servicePerimeters: typing.List[ServicePerimeter]

@typing.type_check_only
class MethodSelector(typing_extensions.TypedDict, total=False):
    method: str
    permission: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
class ReplaceAccessLevelsRequest(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[AccessLevel]
    etag: str

@typing.type_check_only
class ReplaceAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[AccessLevel]

@typing.type_check_only
class ReplaceServicePerimetersRequest(typing_extensions.TypedDict, total=False):
    etag: str
    servicePerimeters: typing.List[ServicePerimeter]

@typing.type_check_only
class ReplaceServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: typing.List[ServicePerimeter]

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
    accessLevels: typing.List[str]
    egressPolicies: typing.List[EgressPolicy]
    ingressPolicies: typing.List[IngressPolicy]
    resources: typing.List[str]
    restrictedServices: typing.List[str]
    vpcAccessibleServices: VpcAccessibleServices

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class VpcAccessibleServices(typing_extensions.TypedDict, total=False):
    allowedServices: typing.List[str]
    enableRestriction: bool
