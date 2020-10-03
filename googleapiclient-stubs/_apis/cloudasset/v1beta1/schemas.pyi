import typing

import typing_extensions

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class TimeWindow(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class GoogleCloudOrgpolicyV1ListPolicy(typing_extensions.TypedDict, total=False):
    suggestedValue: str
    allValues: typing_extensions.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]
    deniedValues: typing.List[str]
    allowedValues: typing.List[str]
    inheritFromParent: bool

class GcsDestination(typing_extensions.TypedDict, total=False):
    uriPrefix: str
    uri: str

class GoogleIdentityAccesscontextmanagerV1Condition(
    typing_extensions.TypedDict, total=False
):
    requiredAccessLevels: typing.List[str]
    members: typing.List[str]
    ipSubnetworks: typing.List[str]
    negate: bool
    devicePolicy: GoogleIdentityAccesscontextmanagerV1DevicePolicy
    regions: typing.List[str]

class GoogleIdentityAccesscontextmanagerV1ServicePerimeter(
    typing_extensions.TypedDict, total=False
):
    description: str
    useExplicitDryRunSpec: bool
    status: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    title: str
    name: str
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    spec: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class ExportAssetsRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig
    assetTypes: typing.List[str]
    readTime: str
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "RESOURCE", "IAM_POLICY"
    ]

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    done: bool
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str

class Asset(typing_extensions.TypedDict, total=False):
    resource: Resource
    name: str
    orgPolicy: typing.List[GoogleCloudOrgpolicyV1Policy]
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter
    assetType: str
    iamPolicy: Policy
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class BatchGetAssetsHistoryResponse(typing_extensions.TypedDict, total=False):
    assets: typing.List[TemporalAsset]

class GoogleIdentityAccesscontextmanagerV1AccessLevel(
    typing_extensions.TypedDict, total=False
):
    custom: GoogleIdentityAccesscontextmanagerV1CustomLevel
    basic: GoogleIdentityAccesscontextmanagerV1BasicLevel
    description: str
    name: str
    title: str

class GoogleCloudOrgpolicyV1BooleanPolicy(typing_extensions.TypedDict, total=False):
    enforced: bool

class GoogleCloudOrgpolicyV1Policy(typing_extensions.TypedDict, total=False):
    updateTime: str
    listPolicy: GoogleCloudOrgpolicyV1ListPolicy
    booleanPolicy: GoogleCloudOrgpolicyV1BooleanPolicy
    restoreDefault: GoogleCloudOrgpolicyV1RestoreDefault
    version: int
    etag: str
    constraint: str

class GoogleIdentityAccesscontextmanagerV1DevicePolicy(
    typing_extensions.TypedDict, total=False
):
    allowedDeviceManagementLevels: typing.List[str]
    requireScreenlock: bool
    requireCorpOwned: bool
    osConstraints: typing.List[GoogleIdentityAccesscontextmanagerV1OsConstraint]
    allowedEncryptionStatuses: typing.List[str]
    requireAdminApproval: bool

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    auditConfigs: typing.List[AuditConfig]
    version: int

class GoogleIdentityAccesscontextmanagerV1CustomLevel(
    typing_extensions.TypedDict, total=False
):
    expr: Expr

class GoogleIdentityAccesscontextmanagerV1OsConstraint(
    typing_extensions.TypedDict, total=False
):
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

class GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices(
    typing_extensions.TypedDict, total=False
):
    allowedServices: typing.List[str]
    enableRestriction: bool

class TemporalAsset(typing_extensions.TypedDict, total=False):
    asset: Asset
    window: TimeWindow
    deleted: bool

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class GoogleIdentityAccesscontextmanagerV1AccessPolicy(
    typing_extensions.TypedDict, total=False
):
    name: str
    etag: str
    title: str
    parent: str

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

class Resource(typing_extensions.TypedDict, total=False):
    version: str
    parent: str
    data: typing.Dict[str, typing.Any]
    resourceUrl: str
    discoveryName: str
    discoveryDocumentUri: str

class GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig(
    typing_extensions.TypedDict, total=False
):
    restrictedServices: typing.List[str]
    accessLevels: typing.List[str]
    resources: typing.List[str]
    vpcAccessibleServices: GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices

class GoogleCloudOrgpolicyV1RestoreDefault(
    typing_extensions.TypedDict, total=False
): ...

class GoogleIdentityAccesscontextmanagerV1BasicLevel(
    typing_extensions.TypedDict, total=False
):
    conditions: typing.List[GoogleIdentityAccesscontextmanagerV1Condition]
    combiningFunction: typing_extensions.Literal["AND", "OR"]
