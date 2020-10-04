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
    name: str
    parent: str
    title: str

@typing.type_check_only
class BasicLevel(typing_extensions.TypedDict, total=False):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: typing.List[Condition]

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
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[AccessLevel]
    nextPageToken: str

@typing.type_check_only
class ListAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    accessPolicies: typing.List[AccessPolicy]
    nextPageToken: str

@typing.type_check_only
class ListServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    servicePerimeters: typing.List[ServicePerimeter]

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
class ServicePerimeter(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    status: ServicePerimeterConfig
    title: str

@typing.type_check_only
class ServicePerimeterConfig(typing_extensions.TypedDict, total=False):
    accessLevels: typing.List[str]
    resources: typing.List[str]
    restrictedServices: typing.List[str]
    unrestrictedServices: typing.List[str]
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
