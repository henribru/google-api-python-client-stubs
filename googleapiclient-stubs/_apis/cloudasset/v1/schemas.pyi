import typing

import typing_extensions
@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    ancestors: typing.List[str]
    assetType: str
    iamPolicy: Policy
    name: str
    orgPolicy: typing.List[GoogleCloudOrgpolicyV1Policy]
    resource: Resource
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter
    updateTime: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BatchGetAssetsHistoryResponse(typing_extensions.TypedDict, total=False):
    assets: typing.List[TemporalAsset]

@typing.type_check_only
class BigQueryDestination(typing_extensions.TypedDict, total=False):
    dataset: str
    force: bool
    partitionSpec: PartitionSpec
    separateTablesPerAssetType: bool
    table: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class CreateFeedRequest(typing_extensions.TypedDict, total=False):
    feed: Feed
    feedId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Explanation(typing_extensions.TypedDict, total=False):
    matchedPermissions: typing.Dict[str, typing.Any]

@typing.type_check_only
class ExportAssetsRequest(typing_extensions.TypedDict, total=False):
    assetTypes: typing.List[str]
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED",
        "RESOURCE",
        "IAM_POLICY",
        "ORG_POLICY",
        "ACCESS_POLICY",
    ]
    outputConfig: OutputConfig
    readTime: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Feed(typing_extensions.TypedDict, total=False):
    assetNames: typing.List[str]
    assetTypes: typing.List[str]
    condition: Expr
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED",
        "RESOURCE",
        "IAM_POLICY",
        "ORG_POLICY",
        "ACCESS_POLICY",
    ]
    feedOutputConfig: FeedOutputConfig
    name: str

@typing.type_check_only
class FeedOutputConfig(typing_extensions.TypedDict, total=False):
    pubsubDestination: PubsubDestination

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str
    uriPrefix: str

@typing.type_check_only
class GoogleCloudOrgpolicyV1BooleanPolicy(typing_extensions.TypedDict, total=False):
    enforced: bool

@typing.type_check_only
class GoogleCloudOrgpolicyV1ListPolicy(typing_extensions.TypedDict, total=False):
    allValues: typing_extensions.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]
    allowedValues: typing.List[str]
    deniedValues: typing.List[str]
    inheritFromParent: bool
    suggestedValue: str

@typing.type_check_only
class GoogleCloudOrgpolicyV1Policy(typing_extensions.TypedDict, total=False):
    booleanPolicy: GoogleCloudOrgpolicyV1BooleanPolicy
    constraint: str
    etag: str
    listPolicy: GoogleCloudOrgpolicyV1ListPolicy
    restoreDefault: GoogleCloudOrgpolicyV1RestoreDefault
    updateTime: str
    version: int

@typing.type_check_only
class GoogleCloudOrgpolicyV1RestoreDefault(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1AccessLevel(
    typing_extensions.TypedDict, total=False
):
    basic: GoogleIdentityAccesscontextmanagerV1BasicLevel
    custom: GoogleIdentityAccesscontextmanagerV1CustomLevel
    description: str
    name: str
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1AccessPolicy(
    typing_extensions.TypedDict, total=False
):
    etag: str
    name: str
    parent: str
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1BasicLevel(
    typing_extensions.TypedDict, total=False
):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: typing.List[GoogleIdentityAccesscontextmanagerV1Condition]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1Condition(
    typing_extensions.TypedDict, total=False
):
    devicePolicy: GoogleIdentityAccesscontextmanagerV1DevicePolicy
    ipSubnetworks: typing.List[str]
    members: typing.List[str]
    negate: bool
    regions: typing.List[str]
    requiredAccessLevels: typing.List[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1CustomLevel(
    typing_extensions.TypedDict, total=False
):
    expr: Expr

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1DevicePolicy(
    typing_extensions.TypedDict, total=False
):
    allowedDeviceManagementLevels: typing.List[str]
    allowedEncryptionStatuses: typing.List[str]
    osConstraints: typing.List[GoogleIdentityAccesscontextmanagerV1OsConstraint]
    requireAdminApproval: bool
    requireCorpOwned: bool
    requireScreenlock: bool

@typing.type_check_only
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

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ServicePerimeter(
    typing_extensions.TypedDict, total=False
):
    description: str
    name: str
    perimeterType: typing_extensions.Literal[
        "PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"
    ]
    spec: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    status: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    title: str
    useExplicitDryRunSpec: bool

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig(
    typing_extensions.TypedDict, total=False
):
    accessLevels: typing.List[str]
    resources: typing.List[str]
    restrictedServices: typing.List[str]
    vpcAccessibleServices: GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices(
    typing_extensions.TypedDict, total=False
):
    allowedServices: typing.List[str]
    enableRestriction: bool

@typing.type_check_only
class IamPolicySearchResult(typing_extensions.TypedDict, total=False):
    explanation: Explanation
    policy: Policy
    project: str
    resource: str

@typing.type_check_only
class ListFeedsResponse(typing_extensions.TypedDict, total=False):
    feeds: typing.List[Feed]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: BigQueryDestination
    gcsDestination: GcsDestination

@typing.type_check_only
class PartitionSpec(typing_extensions.TypedDict, total=False):
    partitionKey: typing_extensions.Literal[
        "PARTITION_KEY_UNSPECIFIED", "READ_TIME", "REQUEST_TIME"
    ]

@typing.type_check_only
class Permissions(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PubsubDestination(typing_extensions.TypedDict, total=False):
    topic: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    data: typing.Dict[str, typing.Any]
    discoveryDocumentUri: str
    discoveryName: str
    location: str
    parent: str
    resourceUrl: str
    version: str

@typing.type_check_only
class ResourceSearchResult(typing_extensions.TypedDict, total=False):
    additionalAttributes: typing.Dict[str, typing.Any]
    assetType: str
    description: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    location: str
    name: str
    networkTags: typing.List[str]
    project: str

@typing.type_check_only
class SearchAllIamPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[IamPolicySearchResult]

@typing.type_check_only
class SearchAllResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[ResourceSearchResult]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TemporalAsset(typing_extensions.TypedDict, total=False):
    asset: Asset
    deleted: bool
    priorAsset: Asset
    priorAssetState: typing_extensions.Literal[
        "PRIOR_ASSET_STATE_UNSPECIFIED",
        "PRESENT",
        "INVALID",
        "DOES_NOT_EXIST",
        "DELETED",
    ]
    window: TimeWindow

@typing.type_check_only
class TimeWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateFeedRequest(typing_extensions.TypedDict, total=False):
    feed: Feed
    updateMask: str
