import typing

import typing_extensions
@typing.type_check_only
class AccessSelector(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
    roles: typing.List[str]

@typing.type_check_only
class AnalyzeIamPolicyLongrunningRequest(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    outputConfig: IamPolicyAnalysisOutputConfig

@typing.type_check_only
class AnalyzeIamPolicyResponse(typing_extensions.TypedDict, total=False):
    fullyExplored: bool
    mainAnalysis: IamPolicyAnalysis
    serviceAccountImpersonationAnalysis: typing.List[IamPolicyAnalysis]

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    ancestors: typing.List[str]
    assetType: str
    iamPolicy: Policy
    name: str
    orgPolicy: typing.List[GoogleCloudOrgpolicyV1Policy]
    osInventory: Inventory
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
        "OS_INVENTORY",
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
        "OS_INVENTORY",
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
class GoogleCloudAssetV1Access(typing_extensions.TypedDict, total=False):
    analysisState: IamPolicyAnalysisState
    permission: str
    role: str

@typing.type_check_only
class GoogleCloudAssetV1AccessControlList(typing_extensions.TypedDict, total=False):
    accesses: typing.List[GoogleCloudAssetV1Access]
    resourceEdges: typing.List[GoogleCloudAssetV1Edge]
    resources: typing.List[GoogleCloudAssetV1Resource]

@typing.type_check_only
class GoogleCloudAssetV1BigQueryDestination(typing_extensions.TypedDict, total=False):
    dataset: str
    partitionKey: typing_extensions.Literal["PARTITION_KEY_UNSPECIFIED", "REQUEST_TIME"]
    tablePrefix: str
    writeDisposition: str

@typing.type_check_only
class GoogleCloudAssetV1Edge(typing_extensions.TypedDict, total=False):
    sourceNode: str
    targetNode: str

@typing.type_check_only
class GoogleCloudAssetV1GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudAssetV1Identity(typing_extensions.TypedDict, total=False):
    analysisState: IamPolicyAnalysisState
    name: str

@typing.type_check_only
class GoogleCloudAssetV1IdentityList(typing_extensions.TypedDict, total=False):
    groupEdges: typing.List[GoogleCloudAssetV1Edge]
    identities: typing.List[GoogleCloudAssetV1Identity]

@typing.type_check_only
class GoogleCloudAssetV1Resource(typing_extensions.TypedDict, total=False):
    analysisState: IamPolicyAnalysisState
    fullResourceName: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1Asset(typing_extensions.TypedDict, total=False):
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    ancestors: typing.List[str]
    assetType: str
    iamPolicy: Policy
    name: str
    orgPolicy: typing.List[GoogleCloudOrgpolicyV1Policy]
    relatedAssets: GoogleCloudAssetV1p7beta1RelatedAssets
    resource: GoogleCloudAssetV1p7beta1Resource
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter
    updateTime: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelatedAsset(typing_extensions.TypedDict, total=False):
    ancestors: typing.List[str]
    asset: str
    assetType: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelatedAssets(typing_extensions.TypedDict, total=False):
    assets: typing.List[GoogleCloudAssetV1p7beta1RelatedAsset]
    relationshipAttributes: GoogleCloudAssetV1p7beta1RelationshipAttributes

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelationshipAttributes(
    typing_extensions.TypedDict, total=False
):
    action: str
    sourceResourceType: str
    targetResourceType: str
    type: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1Resource(typing_extensions.TypedDict, total=False):
    data: typing.Dict[str, typing.Any]
    discoveryDocumentUri: str
    discoveryName: str
    location: str
    parent: str
    resourceUrl: str
    version: str

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
class GoogleIdentityAccesscontextmanagerV1ApiOperation(
    typing_extensions.TypedDict, total=False
):
    methodSelectors: typing.List[GoogleIdentityAccesscontextmanagerV1MethodSelector]
    serviceName: str

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
class GoogleIdentityAccesscontextmanagerV1EgressFrom(
    typing_extensions.TypedDict, total=False
):
    identities: typing.List[str]
    identityType: typing_extensions.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressPolicy(
    typing_extensions.TypedDict, total=False
):
    egressFrom: GoogleIdentityAccesscontextmanagerV1EgressFrom
    egressTo: GoogleIdentityAccesscontextmanagerV1EgressTo

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressTo(
    typing_extensions.TypedDict, total=False
):
    operations: typing.List[GoogleIdentityAccesscontextmanagerV1ApiOperation]
    resources: typing.List[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressFrom(
    typing_extensions.TypedDict, total=False
):
    identities: typing.List[str]
    identityType: typing_extensions.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sources: typing.List[GoogleIdentityAccesscontextmanagerV1IngressSource]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressPolicy(
    typing_extensions.TypedDict, total=False
):
    ingressFrom: GoogleIdentityAccesscontextmanagerV1IngressFrom
    ingressTo: GoogleIdentityAccesscontextmanagerV1IngressTo

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressSource(
    typing_extensions.TypedDict, total=False
):
    accessLevel: str
    resource: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressTo(
    typing_extensions.TypedDict, total=False
):
    operations: typing.List[GoogleIdentityAccesscontextmanagerV1ApiOperation]
    resources: typing.List[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1MethodSelector(
    typing_extensions.TypedDict, total=False
):
    method: str
    permission: str

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
    egressPolicies: typing.List[GoogleIdentityAccesscontextmanagerV1EgressPolicy]
    ingressPolicies: typing.List[GoogleIdentityAccesscontextmanagerV1IngressPolicy]
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
class IamPolicyAnalysis(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    analysisResults: typing.List[IamPolicyAnalysisResult]
    fullyExplored: bool
    nonCriticalErrors: typing.List[IamPolicyAnalysisState]

@typing.type_check_only
class IamPolicyAnalysisOutputConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudAssetV1BigQueryDestination
    gcsDestination: GoogleCloudAssetV1GcsDestination

@typing.type_check_only
class IamPolicyAnalysisQuery(typing_extensions.TypedDict, total=False):
    accessSelector: AccessSelector
    identitySelector: IdentitySelector
    options: Options
    resourceSelector: ResourceSelector
    scope: str

@typing.type_check_only
class IamPolicyAnalysisResult(typing_extensions.TypedDict, total=False):
    accessControlLists: typing.List[GoogleCloudAssetV1AccessControlList]
    attachedResourceFullName: str
    fullyExplored: bool
    iamBinding: Binding
    identityList: GoogleCloudAssetV1IdentityList

@typing.type_check_only
class IamPolicyAnalysisState(typing_extensions.TypedDict, total=False):
    cause: str
    code: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]

@typing.type_check_only
class IamPolicySearchResult(typing_extensions.TypedDict, total=False):
    explanation: Explanation
    policy: Policy
    project: str
    resource: str

@typing.type_check_only
class IdentitySelector(typing_extensions.TypedDict, total=False):
    identity: str

@typing.type_check_only
class Inventory(typing_extensions.TypedDict, total=False):
    items: typing.Dict[str, typing.Any]
    osInfo: OsInfo

@typing.type_check_only
class Item(typing_extensions.TypedDict, total=False):
    availablePackage: SoftwarePackage
    createTime: str
    id: str
    installedPackage: SoftwarePackage
    originType: typing_extensions.Literal["ORIGIN_TYPE_UNSPECIFIED", "INVENTORY_REPORT"]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INSTALLED_PACKAGE", "AVAILABLE_PACKAGE"
    ]
    updateTime: str

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
class Options(typing_extensions.TypedDict, total=False):
    analyzeServiceAccountImpersonation: bool
    expandGroups: bool
    expandResources: bool
    expandRoles: bool
    outputGroupEdges: bool
    outputResourceEdges: bool

@typing.type_check_only
class OsInfo(typing_extensions.TypedDict, total=False):
    architecture: str
    hostname: str
    kernelRelease: str
    kernelVersion: str
    longName: str
    osconfigAgentVersion: str
    shortName: str
    version: str

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
    createTime: str
    description: str
    displayName: str
    folders: typing.List[str]
    kmsKey: str
    labels: typing.Dict[str, typing.Any]
    location: str
    name: str
    networkTags: typing.List[str]
    organization: str
    parentAssetType: str
    parentFullResourceName: str
    project: str
    state: str
    updateTime: str

@typing.type_check_only
class ResourceSelector(typing_extensions.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class SearchAllIamPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[IamPolicySearchResult]

@typing.type_check_only
class SearchAllResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[ResourceSearchResult]

@typing.type_check_only
class SoftwarePackage(typing_extensions.TypedDict, total=False):
    aptPackage: VersionedPackage
    cosPackage: VersionedPackage
    googetPackage: VersionedPackage
    qfePackage: WindowsQuickFixEngineeringPackage
    wuaPackage: WindowsUpdatePackage
    yumPackage: VersionedPackage
    zypperPackage: VersionedPackage
    zypperPatch: ZypperPatch

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

@typing.type_check_only
class VersionedPackage(typing_extensions.TypedDict, total=False):
    architecture: str
    packageName: str
    version: str

@typing.type_check_only
class WindowsQuickFixEngineeringPackage(typing_extensions.TypedDict, total=False):
    caption: str
    description: str
    hotFixId: str
    installTime: str

@typing.type_check_only
class WindowsUpdateCategory(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class WindowsUpdatePackage(typing_extensions.TypedDict, total=False):
    categories: typing.List[WindowsUpdateCategory]
    description: str
    kbArticleIds: typing.List[str]
    lastDeploymentChangeTime: str
    moreInfoUrls: typing.List[str]
    revisionNumber: int
    supportUrl: str
    title: str
    updateId: str

@typing.type_check_only
class ZypperPatch(typing_extensions.TypedDict, total=False):
    category: str
    patchName: str
    severity: str
    summary: str
