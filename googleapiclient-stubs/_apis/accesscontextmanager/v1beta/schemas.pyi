import typing

import typing_extensions

class Condition(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    requiredAccessLevels: typing.List[str]
    negate: bool
    ipSubnetworks: typing.List[str]
    regions: typing.List[str]
    devicePolicy: DevicePolicy

class DevicePolicy(typing_extensions.TypedDict, total=False):
    requireAdminApproval: bool
    requireCorpOwned: bool
    osConstraints: typing.List[OsConstraint]
    allowedEncryptionStatuses: typing.List[str]
    requireScreenlock: bool
    allowedDeviceManagementLevels: typing.List[str]

class ServicePerimeterConfig(typing_extensions.TypedDict, total=False):
    unrestrictedServices: typing.List[str]
    accessLevels: typing.List[str]
    restrictedServices: typing.List[str]
    vpcAccessibleServices: VpcAccessibleServices
    resources: typing.List[str]

class BasicLevel(typing_extensions.TypedDict, total=False):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: typing.List[Condition]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class AccessPolicy(typing_extensions.TypedDict, total=False):
    name: str
    title: str
    parent: str

class VpcAccessibleServices(typing_extensions.TypedDict, total=False):
    enableRestriction: bool
    allowedServices: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    expression: str
    description: str

class CustomLevel(typing_extensions.TypedDict, total=False):
    expr: Expr

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class ListAccessPoliciesResponse(typing_extensions.TypedDict, total=False):
    accessPolicies: typing.List[AccessPolicy]
    nextPageToken: str

class OsConstraint(typing_extensions.TypedDict, total=False):
    minimumVersion: str
    requireVerifiedChromeOs: bool
    osType: typing_extensions.Literal[
        "OS_UNSPECIFIED",
        "DESKTOP_MAC",
        "DESKTOP_WINDOWS",
        "DESKTOP_LINUX",
        "DESKTOP_CHROME_OS",
        "ANDROID",
        "IOS",
    ]

class ServicePerimeter(typing_extensions.TypedDict, total=False):
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    name: str
    description: str
    title: str
    status: ServicePerimeterConfig

class ListAccessLevelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    accessLevels: typing.List[AccessLevel]

class AccessLevel(typing_extensions.TypedDict, total=False):
    name: str
    title: str
    custom: CustomLevel
    description: str
    basic: BasicLevel

class ListServicePerimetersResponse(typing_extensions.TypedDict, total=False):
    servicePerimeters: typing.List[ServicePerimeter]
    nextPageToken: str
