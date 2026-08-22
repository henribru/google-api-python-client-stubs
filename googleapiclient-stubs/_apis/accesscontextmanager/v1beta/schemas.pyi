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
    name: str
    parent: str
    title: str

@typing.type_check_only
class BasicLevel(typing.TypedDict, total=False):
    combiningFunction: typing.Literal["AND", "OR"]
    conditions: _list[Condition]

@typing.type_check_only
class Condition(typing.TypedDict, total=False):
    devicePolicy: DevicePolicy
    ipSubnetworks: _list[str]
    members: _list[str]
    negate: bool
    regions: _list[str]
    requiredAccessLevels: _list[str]

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
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListAccessLevelsResponse(typing.TypedDict, total=False):
    accessLevels: _list[AccessLevel]
    nextPageToken: str

@typing.type_check_only
class ListAccessPoliciesResponse(typing.TypedDict, total=False):
    accessPolicies: _list[AccessPolicy]
    nextPageToken: str

@typing.type_check_only
class ListServicePerimetersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    servicePerimeters: _list[ServicePerimeter]

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
class ServicePerimeter(typing.TypedDict, total=False):
    description: str
    name: str
    perimeterType: typing.Literal["PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"]
    status: ServicePerimeterConfig
    title: str

@typing.type_check_only
class ServicePerimeterConfig(typing.TypedDict, total=False):
    accessLevels: _list[str]
    resources: _list[str]
    restrictedServices: _list[str]
    unrestrictedServices: _list[str]
    vpcAccessibleServices: VpcAccessibleServices

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class VpcAccessibleServices(typing.TypedDict, total=False):
    allowedServices: _list[str]
    enableRestriction: bool
