import typing

import typing_extensions

class ReplaceServicePerimetersRequest(typing_extensions.TypedDict, total=False):
    etag: str
    servicePerimeters: typing.List[ServicePerimeter]

class VpcAccessibleServices(typing_extensions.TypedDict, total=False):
    allowedServices: typing.List[str]
    enableRestriction: bool

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

class BasicLevel(typing_extensions.TypedDict, total=False):
    conditions: typing.List[Condition]
    combiningFunction: typing_extensions.Literal["AND", "OR"]

class AccessLevel(typing_extensions.TypedDict, total=False):
    description: str
    basic: BasicLevel
    name: str
    custom: CustomLevel
    title: str

class ReplaceServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: typing.List[ServicePerimeter]

class ReplaceAccessLevelsRequest(typing_extensions.TypedDict, total=False):
    etag: str
    accessLevels: typing.List[AccessLevel]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class CommitServicePerimetersRequest(typing_extensions.TypedDict, total=False):
    etag: str

class CustomLevel(typing_extensions.TypedDict, total=False):
    expr: Expr

class AccessPolicy(typing_extensions.TypedDict, total=False):
    title: str
    etag: str
    name: str
    parent: str

class CommitServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: typing.List[ServicePerimeter]

class ServicePerimeterConfig(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[str]
    restrictedServices: typing.List[str]
    resources: typing.List[str]
    vpcAccessibleServices: VpcAccessibleServices

class ReplaceAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[AccessLevel]

class GcpUserAccessBinding(typing_extensions.TypedDict, total=False):
    groupKey: str
    name: str
    accessLevels: typing.List[str]

class ListAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    accessPolicies: typing.List[AccessPolicy]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class DevicePolicy(typing_extensions.TypedDict, total=False):
    osConstraints: typing.List[OsConstraint]
    requireCorpOwned: bool
    requireScreenlock: bool
    allowedEncryptionStatuses: typing.List[str]
    allowedDeviceManagementLevels: typing.List[str]
    requireAdminApproval: bool

class ListServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: typing.List[ServicePerimeter]
    nextPageToken: str

class Condition(typing_extensions.TypedDict, total=False):
    ipSubnetworks: typing.List[str]
    requiredAccessLevels: typing.List[str]
    members: typing.List[str]
    devicePolicy: DevicePolicy
    regions: typing.List[str]
    negate: bool

class ListGcpUserAccessBindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    gcpUserAccessBindings: typing.List[GcpUserAccessBinding]

class ListAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[AccessLevel]
    nextPageToken: str

class ServicePerimeter(typing_extensions.TypedDict, total=False):
    title: str
    spec: ServicePerimeterConfig
    description: str
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    useExplicitDryRunSpec: bool
    status: ServicePerimeterConfig
    name: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Empty(typing_extensions.TypedDict, total=False): ...

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    location: str
    title: str
