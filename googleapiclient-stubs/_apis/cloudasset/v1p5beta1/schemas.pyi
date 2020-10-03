import typing

import typing_extensions

class GoogleIdentityAccesscontextmanagerV1BasicLevel(
    typing_extensions.TypedDict, total=False
):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: typing.List[GoogleIdentityAccesscontextmanagerV1Condition]

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: Expr
    role: str

class GoogleCloudOrgpolicyV1Policy(typing_extensions.TypedDict, total=False):
    version: int
    listPolicy: GoogleCloudOrgpolicyV1ListPolicy
    booleanPolicy: GoogleCloudOrgpolicyV1BooleanPolicy
    restoreDefault: GoogleCloudOrgpolicyV1RestoreDefault
    updateTime: str
    etag: str
    constraint: str

class GoogleIdentityAccesscontextmanagerV1DevicePolicy(
    typing_extensions.TypedDict, total=False
):
    osConstraints: typing.List[GoogleIdentityAccesscontextmanagerV1OsConstraint]
    allowedDeviceManagementLevels: typing.List[str]
    allowedEncryptionStatuses: typing.List[str]
    requireAdminApproval: bool
    requireScreenlock: bool
    requireCorpOwned: bool

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class GoogleIdentityAccesscontextmanagerV1ServicePerimeter(
    typing_extensions.TypedDict, total=False
):
    spec: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    useExplicitDryRunSpec: bool
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    status: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    name: str
    description: str
    title: str

class GoogleIdentityAccesscontextmanagerV1Condition(
    typing_extensions.TypedDict, total=False
):
    negate: bool
    regions: typing.List[str]
    requiredAccessLevels: typing.List[str]
    members: typing.List[str]
    ipSubnetworks: typing.List[str]
    devicePolicy: GoogleIdentityAccesscontextmanagerV1DevicePolicy

class GoogleIdentityAccesscontextmanagerV1CustomLevel(
    typing_extensions.TypedDict, total=False
):
    expr: Expr

class Asset(typing_extensions.TypedDict, total=False):
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    resource: Resource
    ancestors: typing.List[str]
    orgPolicy: typing.List[GoogleCloudOrgpolicyV1Policy]
    name: str
    assetType: str
    iamPolicy: Policy
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter

class GoogleIdentityAccesscontextmanagerV1AccessPolicy(
    typing_extensions.TypedDict, total=False
):
    name: str
    title: str
    etag: str
    parent: str

class GoogleIdentityAccesscontextmanagerV1AccessLevel(
    typing_extensions.TypedDict, total=False
):
    name: str
    custom: GoogleIdentityAccesscontextmanagerV1CustomLevel
    description: str
    title: str
    basic: GoogleIdentityAccesscontextmanagerV1BasicLevel

class GoogleIdentityAccesscontextmanagerV1OsConstraint(
    typing_extensions.TypedDict, total=False
):
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
    minimumVersion: str

class GoogleCloudOrgpolicyV1BooleanPolicy(typing_extensions.TypedDict, total=False):
    enforced: bool

class GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices(
    typing_extensions.TypedDict, total=False
):
    enableRestriction: bool
    allowedServices: typing.List[str]

class GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig(
    typing_extensions.TypedDict, total=False
):
    vpcAccessibleServices: GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices
    restrictedServices: typing.List[str]
    accessLevels: typing.List[str]
    resources: typing.List[str]

class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    readTime: str
    nextPageToken: str
    assets: typing.List[Asset]

class GoogleCloudOrgpolicyV1RestoreDefault(
    typing_extensions.TypedDict, total=False
): ...

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int
    auditConfigs: typing.List[AuditConfig]

class Resource(typing_extensions.TypedDict, total=False):
    parent: str
    version: str
    discoveryDocumentUri: str
    data: typing.Dict[str, typing.Any]
    resourceUrl: str
    discoveryName: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class GoogleCloudOrgpolicyV1ListPolicy(typing_extensions.TypedDict, total=False):
    suggestedValue: str
    allowedValues: typing.List[str]
    deniedValues: typing.List[str]
    inheritFromParent: bool
    allValues: typing_extensions.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    expression: str
    title: str
    description: str
