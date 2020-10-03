import typing

import typing_extensions

class ListFeedsResponse(typing_extensions.TypedDict, total=False):
    feeds: typing.List[Feed]

class Empty(typing_extensions.TypedDict, total=False): ...

class BigQueryDestination(typing_extensions.TypedDict, total=False):
    force: bool
    separateTablesPerAssetType: bool
    dataset: str
    table: str
    partitionSpec: PartitionSpec

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class Explanation(typing_extensions.TypedDict, total=False):
    matchedPermissions: typing.Dict[str, typing.Any]

class FeedOutputConfig(typing_extensions.TypedDict, total=False):
    pubsubDestination: PubsubDestination

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class SearchAllResourcesResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[ResourceSearchResult]
    nextPageToken: str

class GoogleIdentityAccesscontextmanagerV1CustomLevel(
    typing_extensions.TypedDict, total=False
):
    expr: Expr

class GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig(
    typing_extensions.TypedDict, total=False
):
    restrictedServices: typing.List[str]
    vpcAccessibleServices: GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices
    accessLevels: typing.List[str]
    resources: typing.List[str]

class GoogleCloudOrgpolicyV1Policy(typing_extensions.TypedDict, total=False):
    updateTime: str
    booleanPolicy: GoogleCloudOrgpolicyV1BooleanPolicy
    listPolicy: GoogleCloudOrgpolicyV1ListPolicy
    etag: str
    version: int
    constraint: str
    restoreDefault: GoogleCloudOrgpolicyV1RestoreDefault

class GoogleIdentityAccesscontextmanagerV1AccessLevel(
    typing_extensions.TypedDict, total=False
):
    custom: GoogleIdentityAccesscontextmanagerV1CustomLevel
    name: str
    title: str
    description: str
    basic: GoogleIdentityAccesscontextmanagerV1BasicLevel

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class TimeWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class PartitionSpec(typing_extensions.TypedDict, total=False):
    partitionKey: typing_extensions.Literal[
        "PARTITION_KEY_UNSPECIFIED", "READ_TIME", "REQUEST_TIME"
    ]

class GoogleCloudOrgpolicyV1RestoreDefault(
    typing_extensions.TypedDict, total=False
): ...

class Feed(typing_extensions.TypedDict, total=False):
    assetNames: typing.List[str]
    condition: Expr
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED",
        "RESOURCE",
        "IAM_POLICY",
        "ORG_POLICY",
        "ACCESS_POLICY",
    ]
    feedOutputConfig: FeedOutputConfig
    assetTypes: typing.List[str]
    name: str

class Permissions(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    title: str
    location: str
    description: str

class BatchGetAssetsHistoryResponse(typing_extensions.TypedDict, total=False):
    assets: typing.List[TemporalAsset]

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    auditConfigs: typing.List[AuditConfig]
    version: int
    bindings: typing.List[Binding]

class GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices(
    typing_extensions.TypedDict, total=False
):
    allowedServices: typing.List[str]
    enableRestriction: bool

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    error: Status

class GoogleIdentityAccesscontextmanagerV1BasicLevel(
    typing_extensions.TypedDict, total=False
):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: typing.List[GoogleIdentityAccesscontextmanagerV1Condition]

class PubsubDestination(typing_extensions.TypedDict, total=False):
    topic: str

class GcsDestination(typing_extensions.TypedDict, total=False):
    uriPrefix: str
    uri: str

class GoogleIdentityAccesscontextmanagerV1DevicePolicy(
    typing_extensions.TypedDict, total=False
):
    requireAdminApproval: bool
    allowedDeviceManagementLevels: typing.List[str]
    requireScreenlock: bool
    requireCorpOwned: bool
    osConstraints: typing.List[GoogleIdentityAccesscontextmanagerV1OsConstraint]
    allowedEncryptionStatuses: typing.List[str]

class GoogleCloudOrgpolicyV1BooleanPolicy(typing_extensions.TypedDict, total=False):
    enforced: bool

class Resource(typing_extensions.TypedDict, total=False):
    discoveryDocumentUri: str
    parent: str
    discoveryName: str
    resourceUrl: str
    location: str
    version: str
    data: typing.Dict[str, typing.Any]

class GoogleIdentityAccesscontextmanagerV1ServicePerimeter(
    typing_extensions.TypedDict, total=False
):
    spec: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    title: str
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    status: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    name: str
    description: str
    useExplicitDryRunSpec: bool

class SearchAllIamPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[IamPolicySearchResult]

class ExportAssetsRequest(typing_extensions.TypedDict, total=False):
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED",
        "RESOURCE",
        "IAM_POLICY",
        "ORG_POLICY",
        "ACCESS_POLICY",
    ]
    readTime: str
    assetTypes: typing.List[str]
    outputConfig: OutputConfig

class GoogleIdentityAccesscontextmanagerV1Condition(
    typing_extensions.TypedDict, total=False
):
    requiredAccessLevels: typing.List[str]
    devicePolicy: GoogleIdentityAccesscontextmanagerV1DevicePolicy
    members: typing.List[str]
    negate: bool
    ipSubnetworks: typing.List[str]
    regions: typing.List[str]

class TemporalAsset(typing_extensions.TypedDict, total=False):
    priorAssetState: typing_extensions.Literal[
        "PRIOR_ASSET_STATE_UNSPECIFIED",
        "PRESENT",
        "INVALID",
        "DOES_NOT_EXIST",
        "DELETED",
    ]
    asset: Asset
    window: TimeWindow
    priorAsset: Asset
    deleted: bool

class UpdateFeedRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    feed: Feed

class Asset(typing_extensions.TypedDict, total=False):
    name: str
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    updateTime: str
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter
    ancestors: typing.List[str]
    resource: Resource
    assetType: str
    orgPolicy: typing.List[GoogleCloudOrgpolicyV1Policy]
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    iamPolicy: Policy

class CreateFeedRequest(typing_extensions.TypedDict, total=False):
    feedId: str
    feed: Feed

class IamPolicySearchResult(typing_extensions.TypedDict, total=False):
    explanation: Explanation
    project: str
    resource: str
    policy: Policy

class GoogleCloudOrgpolicyV1ListPolicy(typing_extensions.TypedDict, total=False):
    allowedValues: typing.List[str]
    deniedValues: typing.List[str]
    inheritFromParent: bool
    allValues: typing_extensions.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]
    suggestedValue: str

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination
    bigqueryDestination: BigQueryDestination

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class ResourceSearchResult(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    displayName: str
    description: str
    networkTags: typing.List[str]
    location: str
    name: str
    project: str
    assetType: str
    additionalAttributes: typing.Dict[str, typing.Any]

class GoogleIdentityAccesscontextmanagerV1AccessPolicy(
    typing_extensions.TypedDict, total=False
):
    etag: str
    title: str
    name: str
    parent: str

class GoogleIdentityAccesscontextmanagerV1OsConstraint(
    typing_extensions.TypedDict, total=False
):
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
    requireVerifiedChromeOs: bool
