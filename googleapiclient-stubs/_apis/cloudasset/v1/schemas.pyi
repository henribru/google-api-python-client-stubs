import typing

_list = list

@typing.type_check_only
class AccessSelector(typing.TypedDict, total=False):
    permissions: _list[str]
    roles: _list[str]

@typing.type_check_only
class AnalyzeIamPolicyLongrunningMetadata(typing.TypedDict, total=False):
    createTime: str

@typing.type_check_only
class AnalyzeIamPolicyLongrunningRequest(typing.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    outputConfig: IamPolicyAnalysisOutputConfig
    savedAnalysisQuery: str

@typing.type_check_only
class AnalyzeIamPolicyLongrunningResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class AnalyzeIamPolicyResponse(typing.TypedDict, total=False):
    fullyExplored: bool
    mainAnalysis: IamPolicyAnalysis
    serviceAccountImpersonationAnalysis: _list[IamPolicyAnalysis]

@typing.type_check_only
class AnalyzeMoveResponse(typing.TypedDict, total=False):
    moveAnalysis: _list[MoveAnalysis]

@typing.type_check_only
class AnalyzeOrgPoliciesResponse(typing.TypedDict, total=False):
    constraint: AnalyzerOrgPolicyConstraint
    nextPageToken: str
    orgPolicyResults: _list[OrgPolicyResult]

@typing.type_check_only
class AnalyzeOrgPolicyGovernedAssetsResponse(typing.TypedDict, total=False):
    constraint: AnalyzerOrgPolicyConstraint
    governedAssets: _list[
        GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAsset
    ]
    nextPageToken: str

@typing.type_check_only
class AnalyzeOrgPolicyGovernedContainersResponse(typing.TypedDict, total=False):
    constraint: AnalyzerOrgPolicyConstraint
    governedContainers: _list[GoogleCloudAssetV1GovernedContainer]
    nextPageToken: str

@typing.type_check_only
class AnalyzerOrgPolicy(typing.TypedDict, total=False):
    appliedResource: str
    attachedResource: str
    inheritFromParent: bool
    reset: bool
    rules: _list[GoogleCloudAssetV1Rule]

@typing.type_check_only
class AnalyzerOrgPolicyConstraint(typing.TypedDict, total=False):
    customConstraint: GoogleCloudAssetV1CustomConstraint
    googleDefinedConstraint: GoogleCloudAssetV1Constraint

@typing.type_check_only
class Asset(typing.TypedDict, total=False):
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    ancestors: _list[str]
    assetExceptions: _list[AssetException]
    assetType: str
    iamPolicy: Policy
    name: str
    orgPolicy: _list[GoogleCloudOrgpolicyV1Policy]
    osInventory: Inventory
    relatedAsset: RelatedAsset
    relatedAssets: RelatedAssets
    resource: Resource
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter
    updateTime: str

@typing.type_check_only
class AssetEnrichment(typing.TypedDict, total=False):
    resourceOwners: ResourceOwners

@typing.type_check_only
class AssetException(typing.TypedDict, total=False):
    details: str
    exceptionType: typing.Literal["EXCEPTION_TYPE_UNSPECIFIED", "TRUNCATION"]

@typing.type_check_only
class AttachedResource(typing.TypedDict, total=False):
    assetType: str
    versionedResources: _list[VersionedResource]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BatchGetAssetsHistoryResponse(typing.TypedDict, total=False):
    assets: _list[TemporalAsset]

@typing.type_check_only
class BatchGetEffectiveIamPoliciesResponse(typing.TypedDict, total=False):
    policyResults: _list[EffectiveIamPolicy]

@typing.type_check_only
class BigQueryDestination(typing.TypedDict, total=False):
    dataset: str
    force: bool
    partitionSpec: PartitionSpec
    separateTablesPerAssetType: bool
    table: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ConditionContext(typing.TypedDict, total=False):
    accessTime: str

@typing.type_check_only
class ConditionEvaluation(typing.TypedDict, total=False):
    evaluationValue: typing.Literal[
        "EVALUATION_VALUE_UNSPECIFIED", "TRUE", "FALSE", "CONDITIONAL"
    ]

@typing.type_check_only
class CreateFeedRequest(typing.TypedDict, total=False):
    feed: Feed
    feedId: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class EffectiveIamPolicy(typing.TypedDict, total=False):
    fullResourceName: str
    policies: _list[PolicyInfo]

@typing.type_check_only
class EffectiveTagDetails(typing.TypedDict, total=False):
    attachedResource: str
    effectiveTags: _list[Tag]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Explanation(typing.TypedDict, total=False):
    matchedPermissions: dict[str, typing.Any]

@typing.type_check_only
class ExportAssetsRequest(typing.TypedDict, total=False):
    assetTypes: _list[str]
    contentType: typing.Literal[
        "CONTENT_TYPE_UNSPECIFIED",
        "RESOURCE",
        "IAM_POLICY",
        "ORG_POLICY",
        "ACCESS_POLICY",
        "OS_INVENTORY",
        "RELATIONSHIP",
    ]
    outputConfig: OutputConfig
    readTime: str
    relationshipTypes: _list[str]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Feed(typing.TypedDict, total=False):
    assetNames: _list[str]
    assetTypes: _list[str]
    condition: Expr
    contentType: typing.Literal[
        "CONTENT_TYPE_UNSPECIFIED",
        "RESOURCE",
        "IAM_POLICY",
        "ORG_POLICY",
        "ACCESS_POLICY",
        "OS_INVENTORY",
        "RELATIONSHIP",
    ]
    feedOutputConfig: FeedOutputConfig
    name: str
    relationshipTypes: _list[str]

@typing.type_check_only
class FeedOutputConfig(typing.TypedDict, total=False):
    pubsubDestination: PubsubDestination

@typing.type_check_only
class GcsDestination(typing.TypedDict, total=False):
    uri: str
    uriPrefix: str

@typing.type_check_only
class GoogleCloudAssetV1Access(typing.TypedDict, total=False):
    analysisState: IamPolicyAnalysisState
    permission: str
    role: str

@typing.type_check_only
class GoogleCloudAssetV1AccessControlList(typing.TypedDict, total=False):
    accesses: _list[GoogleCloudAssetV1Access]
    conditionEvaluation: ConditionEvaluation
    resourceEdges: _list[GoogleCloudAssetV1Edge]
    resources: _list[GoogleCloudAssetV1Resource]

@typing.type_check_only
class GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedAsset(
    typing.TypedDict, total=False
):
    consolidatedPolicy: AnalyzerOrgPolicy
    governedIamPolicy: (
        GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicy
    )
    governedResource: (
        GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResource
    )
    policyBundle: _list[AnalyzerOrgPolicy]

@typing.type_check_only
class GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedIamPolicy(
    typing.TypedDict, total=False
):
    assetType: str
    attachedResource: str
    folders: _list[str]
    organization: str
    policy: Policy
    project: str

@typing.type_check_only
class GoogleCloudAssetV1AnalyzeOrgPolicyGovernedAssetsResponseGovernedResource(
    typing.TypedDict, total=False
):
    assetType: str
    effectiveTags: _list[EffectiveTagDetails]
    folders: _list[str]
    fullResourceName: str
    organization: str
    parent: str
    project: str

@typing.type_check_only
class GoogleCloudAssetV1BigQueryDestination(typing.TypedDict, total=False):
    dataset: str
    partitionKey: typing.Literal["PARTITION_KEY_UNSPECIFIED", "REQUEST_TIME"]
    tablePrefix: str
    writeDisposition: str

@typing.type_check_only
class GoogleCloudAssetV1BooleanConstraint(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudAssetV1Constraint(typing.TypedDict, total=False):
    booleanConstraint: GoogleCloudAssetV1BooleanConstraint
    constraintDefault: typing.Literal["CONSTRAINT_DEFAULT_UNSPECIFIED", "ALLOW", "DENY"]
    description: str
    displayName: str
    listConstraint: GoogleCloudAssetV1ListConstraint
    name: str

@typing.type_check_only
class GoogleCloudAssetV1CustomConstraint(typing.TypedDict, total=False):
    actionType: typing.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    description: str
    displayName: str
    methodTypes: _list[
        typing.Literal[
            "METHOD_TYPE_UNSPECIFIED",
            "CREATE",
            "UPDATE",
            "DELETE",
            "REMOVE_GRANT",
            "GOVERN_TAGS",
        ]
    ]
    name: str
    resourceTypes: _list[str]

@typing.type_check_only
class GoogleCloudAssetV1Edge(typing.TypedDict, total=False):
    sourceNode: str
    targetNode: str

@typing.type_check_only
class GoogleCloudAssetV1GcsDestination(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudAssetV1GovernedContainer(typing.TypedDict, total=False):
    consolidatedPolicy: AnalyzerOrgPolicy
    effectiveTags: _list[EffectiveTagDetails]
    folders: _list[str]
    fullResourceName: str
    organization: str
    parent: str
    policyBundle: _list[AnalyzerOrgPolicy]
    project: str

@typing.type_check_only
class GoogleCloudAssetV1Identity(typing.TypedDict, total=False):
    analysisState: IamPolicyAnalysisState
    name: str

@typing.type_check_only
class GoogleCloudAssetV1IdentityList(typing.TypedDict, total=False):
    groupEdges: _list[GoogleCloudAssetV1Edge]
    identities: _list[GoogleCloudAssetV1Identity]

@typing.type_check_only
class GoogleCloudAssetV1ListConstraint(typing.TypedDict, total=False):
    supportsIn: bool
    supportsUnder: bool

@typing.type_check_only
class GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestination(
    typing.TypedDict, total=False
):
    dataset: str
    table: str
    writeDisposition: str

@typing.type_check_only
class GoogleCloudAssetV1Resource(typing.TypedDict, total=False):
    analysisState: IamPolicyAnalysisState
    fullResourceName: str

@typing.type_check_only
class GoogleCloudAssetV1Rule(typing.TypedDict, total=False):
    allowAll: bool
    condition: Expr
    conditionEvaluation: ConditionEvaluation
    denyAll: bool
    enforce: bool
    values: GoogleCloudAssetV1StringValues

@typing.type_check_only
class GoogleCloudAssetV1StringValues(typing.TypedDict, total=False):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleCloudAssetV1p7beta1Asset(typing.TypedDict, total=False):
    accessLevel: GoogleIdentityAccesscontextmanagerV1AccessLevel
    accessPolicy: GoogleIdentityAccesscontextmanagerV1AccessPolicy
    ancestors: _list[str]
    assetType: str
    iamPolicy: Policy
    name: str
    orgPolicy: _list[GoogleCloudOrgpolicyV1Policy]
    relatedAssets: GoogleCloudAssetV1p7beta1RelatedAssets
    resource: GoogleCloudAssetV1p7beta1Resource
    servicePerimeter: GoogleIdentityAccesscontextmanagerV1ServicePerimeter
    updateTime: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelatedAsset(typing.TypedDict, total=False):
    ancestors: _list[str]
    asset: str
    assetType: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelatedAssets(typing.TypedDict, total=False):
    assets: _list[GoogleCloudAssetV1p7beta1RelatedAsset]
    relationshipAttributes: GoogleCloudAssetV1p7beta1RelationshipAttributes

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelationshipAttributes(typing.TypedDict, total=False):
    action: str
    sourceResourceType: str
    targetResourceType: str
    type: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1Resource(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    discoveryDocumentUri: str
    discoveryName: str
    location: str
    parent: str
    resourceUrl: str
    version: str

@typing.type_check_only
class GoogleCloudOrgpolicyV1BooleanPolicy(typing.TypedDict, total=False):
    enforced: bool

@typing.type_check_only
class GoogleCloudOrgpolicyV1ListPolicy(typing.TypedDict, total=False):
    allValues: typing.Literal["ALL_VALUES_UNSPECIFIED", "ALLOW", "DENY"]
    allowedValues: _list[str]
    deniedValues: _list[str]
    inheritFromParent: bool
    suggestedValue: str

@typing.type_check_only
class GoogleCloudOrgpolicyV1Policy(typing.TypedDict, total=False):
    booleanPolicy: GoogleCloudOrgpolicyV1BooleanPolicy
    constraint: str
    etag: str
    listPolicy: GoogleCloudOrgpolicyV1ListPolicy
    restoreDefault: GoogleCloudOrgpolicyV1RestoreDefault
    updateTime: str
    version: int

@typing.type_check_only
class GoogleCloudOrgpolicyV1RestoreDefault(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1AccessLevel(typing.TypedDict, total=False):
    basic: GoogleIdentityAccesscontextmanagerV1BasicLevel
    custom: GoogleIdentityAccesscontextmanagerV1CustomLevel
    description: str
    name: str
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1AccessPolicy(typing.TypedDict, total=False):
    etag: str
    name: str
    parent: str
    scopes: _list[str]
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1AddRequestHeader(
    typing.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ApiOperation(typing.TypedDict, total=False):
    methodSelectors: _list[GoogleIdentityAccesscontextmanagerV1MethodSelector]
    serviceName: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1BasicLevel(typing.TypedDict, total=False):
    combiningFunction: typing.Literal["AND", "OR"]
    conditions: _list[GoogleIdentityAccesscontextmanagerV1Condition]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1Condition(typing.TypedDict, total=False):
    devicePolicy: GoogleIdentityAccesscontextmanagerV1DevicePolicy
    ipSubnetworks: _list[str]
    members: _list[str]
    negate: bool
    regions: _list[str]
    requiredAccessLevels: _list[str]
    vpcNetworkSources: _list[GoogleIdentityAccesscontextmanagerV1VpcNetworkSource]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1CustomLevel(typing.TypedDict, total=False):
    expr: Expr

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1DevicePolicy(typing.TypedDict, total=False):
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
    osConstraints: _list[GoogleIdentityAccesscontextmanagerV1OsConstraint]
    requireAdminApproval: bool
    requireCorpOwned: bool
    requireScreenlock: bool

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressFrom(typing.TypedDict, total=False):
    identities: _list[str]
    identityType: typing.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sourceRestriction: typing.Literal[
        "SOURCE_RESTRICTION_UNSPECIFIED",
        "SOURCE_RESTRICTION_ENABLED",
        "SOURCE_RESTRICTION_DISABLED",
    ]
    sources: _list[GoogleIdentityAccesscontextmanagerV1EgressSource]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressPolicy(typing.TypedDict, total=False):
    egressFrom: GoogleIdentityAccesscontextmanagerV1EgressFrom
    egressTo: GoogleIdentityAccesscontextmanagerV1EgressTo
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressSource(typing.TypedDict, total=False):
    accessLevel: str
    pscEndpoint: GoogleIdentityAccesscontextmanagerV1PrivateServiceConnectEndpoint
    resource: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressTo(typing.TypedDict, total=False):
    externalResources: _list[str]
    operations: _list[GoogleIdentityAccesscontextmanagerV1ApiOperation]
    resources: _list[str]
    roles: _list[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressFrom(typing.TypedDict, total=False):
    identities: _list[str]
    identityType: typing.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sources: _list[GoogleIdentityAccesscontextmanagerV1IngressSource]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressPolicy(typing.TypedDict, total=False):
    ingressFrom: GoogleIdentityAccesscontextmanagerV1IngressFrom
    ingressTo: GoogleIdentityAccesscontextmanagerV1IngressTo
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressSource(typing.TypedDict, total=False):
    accessLevel: str
    pscEndpoint: GoogleIdentityAccesscontextmanagerV1PrivateServiceConnectEndpoint
    resource: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressTo(typing.TypedDict, total=False):
    operations: _list[GoogleIdentityAccesscontextmanagerV1ApiOperation]
    resources: _list[str]
    roles: _list[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1MethodSelector(typing.TypedDict, total=False):
    method: str
    permission: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1Modifier(typing.TypedDict, total=False):
    addRequestHeader: GoogleIdentityAccesscontextmanagerV1AddRequestHeader

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1OsConstraint(typing.TypedDict, total=False):
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
class GoogleIdentityAccesscontextmanagerV1PrivateServiceConnectEndpoint(
    typing.TypedDict, total=False
):
    forwardingRule: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ServicePattern(typing.TypedDict, total=False):
    modifiers: _list[GoogleIdentityAccesscontextmanagerV1Modifier]
    pattern: str
    service: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ServicePerimeter(
    typing.TypedDict, total=False
):
    description: str
    etag: str
    name: str
    perimeterType: typing.Literal["PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"]
    spec: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    status: GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig
    title: str
    useExplicitDryRunSpec: bool

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ServicePerimeterConfig(
    typing.TypedDict, total=False
):
    accessLevels: _list[str]
    egressPolicies: _list[GoogleIdentityAccesscontextmanagerV1EgressPolicy]
    ingressPolicies: _list[GoogleIdentityAccesscontextmanagerV1IngressPolicy]
    resources: _list[str]
    restrictedServices: _list[str]
    vpcAccessibleServices: GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices(
    typing.TypedDict, total=False
):
    allowedServicePatterns: _list[GoogleIdentityAccesscontextmanagerV1ServicePattern]
    allowedServices: _list[str]
    enableRestriction: bool
    servicePatternsEnforcementScopes: _list[
        typing.Literal[
            "SERVICE_PATTERNS_ENFORCEMENT_SCOPE_UNSPECIFIED",
            "GOOGLE_APIS_VIA_PRIVATE_PATH",
        ]
    ]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1VpcNetworkSource(
    typing.TypedDict, total=False
):
    vpcSubnetwork: GoogleIdentityAccesscontextmanagerV1VpcSubNetwork

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1VpcSubNetwork(typing.TypedDict, total=False):
    network: str
    vpcIpSubnetworks: _list[str]

@typing.type_check_only
class IamPolicyAnalysis(typing.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    analysisResults: _list[IamPolicyAnalysisResult]
    fullyExplored: bool
    nonCriticalErrors: _list[IamPolicyAnalysisState]

@typing.type_check_only
class IamPolicyAnalysisOutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudAssetV1BigQueryDestination
    gcsDestination: GoogleCloudAssetV1GcsDestination

@typing.type_check_only
class IamPolicyAnalysisQuery(typing.TypedDict, total=False):
    accessSelector: AccessSelector
    conditionContext: ConditionContext
    identitySelector: IdentitySelector
    options: Options
    resourceSelector: ResourceSelector
    scope: str

@typing.type_check_only
class IamPolicyAnalysisResult(typing.TypedDict, total=False):
    accessControlLists: _list[GoogleCloudAssetV1AccessControlList]
    attachedResourceFullName: str
    fullyExplored: bool
    iamBinding: Binding
    identityList: GoogleCloudAssetV1IdentityList

@typing.type_check_only
class IamPolicyAnalysisState(typing.TypedDict, total=False):
    cause: str
    code: typing.Literal[
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
class IamPolicySearchResult(typing.TypedDict, total=False):
    assetType: str
    explanation: Explanation
    folders: _list[str]
    organization: str
    policy: Policy
    project: str
    resource: str

@typing.type_check_only
class IdentitySelector(typing.TypedDict, total=False):
    identity: str

@typing.type_check_only
class Inventory(typing.TypedDict, total=False):
    items: dict[str, typing.Any]
    name: str
    osInfo: OsInfo
    updateTime: str

@typing.type_check_only
class Item(typing.TypedDict, total=False):
    availablePackage: SoftwarePackage
    createTime: str
    id: str
    installedPackage: SoftwarePackage
    originType: typing.Literal["ORIGIN_TYPE_UNSPECIFIED", "INVENTORY_REPORT"]
    type: typing.Literal["TYPE_UNSPECIFIED", "INSTALLED_PACKAGE", "AVAILABLE_PACKAGE"]
    updateTime: str

@typing.type_check_only
class ListAssetsResponse(typing.TypedDict, total=False):
    assets: _list[Asset]
    nextPageToken: str
    readTime: str

@typing.type_check_only
class ListFeedsResponse(typing.TypedDict, total=False):
    feeds: _list[Feed]

@typing.type_check_only
class ListSavedQueriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    savedQueries: _list[SavedQuery]

@typing.type_check_only
class MoveAnalysis(typing.TypedDict, total=False):
    analysis: MoveAnalysisResult
    displayName: str
    error: Status

@typing.type_check_only
class MoveAnalysisResult(typing.TypedDict, total=False):
    blockers: _list[MoveImpact]
    warnings: _list[MoveImpact]

@typing.type_check_only
class MoveImpact(typing.TypedDict, total=False):
    detail: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Options(typing.TypedDict, total=False):
    analyzeServiceAccountImpersonation: bool
    expandGroups: bool
    expandResources: bool
    expandRoles: bool
    outputGroupEdges: bool
    outputResourceEdges: bool

@typing.type_check_only
class OrgPolicyResult(typing.TypedDict, total=False):
    consolidatedPolicy: AnalyzerOrgPolicy
    folders: _list[str]
    organization: str
    policyBundle: _list[AnalyzerOrgPolicy]
    project: str

@typing.type_check_only
class OsInfo(typing.TypedDict, total=False):
    architecture: str
    hostname: str
    kernelRelease: str
    kernelVersion: str
    longName: str
    osconfigAgentVersion: str
    shortName: str
    version: str

@typing.type_check_only
class OutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: BigQueryDestination
    gcsDestination: GcsDestination

@typing.type_check_only
class PartitionSpec(typing.TypedDict, total=False):
    partitionKey: typing.Literal[
        "PARTITION_KEY_UNSPECIFIED", "READ_TIME", "REQUEST_TIME"
    ]

@typing.type_check_only
class Permissions(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyInfo(typing.TypedDict, total=False):
    attachedResource: str
    policy: Policy

@typing.type_check_only
class PubsubDestination(typing.TypedDict, total=False):
    topic: str

@typing.type_check_only
class QueryAssetsOutputConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudAssetV1QueryAssetsOutputConfigBigQueryDestination

@typing.type_check_only
class QueryAssetsRequest(typing.TypedDict, total=False):
    jobReference: str
    outputConfig: QueryAssetsOutputConfig
    pageSize: int
    pageToken: str
    readTime: str
    readTimeWindow: TimeWindow
    statement: str
    timeout: str

@typing.type_check_only
class QueryAssetsResponse(typing.TypedDict, total=False):
    done: bool
    error: Status
    jobReference: str
    outputConfig: QueryAssetsOutputConfig
    queryResult: QueryResult

@typing.type_check_only
class QueryContent(typing.TypedDict, total=False):
    iamPolicyAnalysisQuery: IamPolicyAnalysisQuery

@typing.type_check_only
class QueryResult(typing.TypedDict, total=False):
    nextPageToken: str
    rows: _list[dict[str, typing.Any]]
    schema: TableSchema
    totalRows: str

@typing.type_check_only
class RelatedAsset(typing.TypedDict, total=False):
    ancestors: _list[str]
    asset: str
    assetType: str
    relationshipType: str

@typing.type_check_only
class RelatedAssets(typing.TypedDict, total=False):
    assets: _list[RelatedAsset]
    relationshipAttributes: RelationshipAttributes

@typing.type_check_only
class RelatedResource(typing.TypedDict, total=False):
    assetType: str
    fullResourceName: str

@typing.type_check_only
class RelatedResources(typing.TypedDict, total=False):
    relatedResources: _list[RelatedResource]

@typing.type_check_only
class RelationshipAttributes(typing.TypedDict, total=False):
    action: str
    sourceResourceType: str
    targetResourceType: str
    type: str

@typing.type_check_only
class Resource(typing.TypedDict, total=False):
    data: dict[str, typing.Any]
    discoveryDocumentUri: str
    discoveryName: str
    location: str
    parent: str
    resourceUrl: str
    version: str

@typing.type_check_only
class ResourceOwners(typing.TypedDict, total=False):
    resourceOwners: _list[str]

@typing.type_check_only
class ResourceSearchResult(typing.TypedDict, total=False):
    additionalAttributes: dict[str, typing.Any]
    assetType: str
    attachedResources: _list[AttachedResource]
    createTime: str
    description: str
    displayName: str
    effectiveTags: _list[EffectiveTagDetails]
    enrichments: _list[AssetEnrichment]
    folders: _list[str]
    kmsKey: str
    kmsKeys: _list[str]
    labels: dict[str, typing.Any]
    location: str
    name: str
    networkTags: _list[str]
    organization: str
    parentAssetType: str
    parentFullResourceName: str
    project: str
    relationships: dict[str, typing.Any]
    sccSecurityMarks: dict[str, typing.Any]
    state: str
    tagKeys: _list[str]
    tagValueIds: _list[str]
    tagValues: _list[str]
    tags: _list[Tag]
    updateTime: str
    versionedResources: _list[VersionedResource]

@typing.type_check_only
class ResourceSelector(typing.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class SavedQuery(typing.TypedDict, total=False):
    content: QueryContent
    createTime: str
    creator: str
    description: str
    labels: dict[str, typing.Any]
    lastUpdateTime: str
    lastUpdater: str
    name: str

@typing.type_check_only
class SearchAllIamPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[IamPolicySearchResult]

@typing.type_check_only
class SearchAllResourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[ResourceSearchResult]

@typing.type_check_only
class SoftwarePackage(typing.TypedDict, total=False):
    aptPackage: VersionedPackage
    cosPackage: VersionedPackage
    googetPackage: VersionedPackage
    qfePackage: WindowsQuickFixEngineeringPackage
    windowsApplication: WindowsApplication
    wuaPackage: WindowsUpdatePackage
    yumPackage: VersionedPackage
    zypperPackage: VersionedPackage
    zypperPatch: ZypperPatch

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TableFieldSchema(typing.TypedDict, total=False):
    field: str
    fields: _list[TableFieldSchema]
    mode: str
    type: str

@typing.type_check_only
class TableSchema(typing.TypedDict, total=False):
    fields: _list[TableFieldSchema]

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    tagKey: str
    tagKeyId: str
    tagValue: str
    tagValueId: str

@typing.type_check_only
class TemporalAsset(typing.TypedDict, total=False):
    asset: Asset
    deleted: bool
    priorAsset: Asset
    priorAssetState: typing.Literal[
        "PRIOR_ASSET_STATE_UNSPECIFIED",
        "PRESENT",
        "INVALID",
        "DOES_NOT_EXIST",
        "DELETED",
    ]
    window: TimeWindow

@typing.type_check_only
class TimeWindow(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateFeedRequest(typing.TypedDict, total=False):
    feed: Feed
    updateMask: str

@typing.type_check_only
class VersionedPackage(typing.TypedDict, total=False):
    architecture: str
    packageName: str
    version: str

@typing.type_check_only
class VersionedResource(typing.TypedDict, total=False):
    assetExceptions: _list[AssetException]
    resource: dict[str, typing.Any]
    version: str

@typing.type_check_only
class WindowsApplication(typing.TypedDict, total=False):
    displayName: str
    displayVersion: str
    helpLink: str
    installDate: Date
    publisher: str

@typing.type_check_only
class WindowsQuickFixEngineeringPackage(typing.TypedDict, total=False):
    caption: str
    description: str
    hotFixId: str
    installTime: str

@typing.type_check_only
class WindowsUpdateCategory(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class WindowsUpdatePackage(typing.TypedDict, total=False):
    categories: _list[WindowsUpdateCategory]
    description: str
    kbArticleIds: _list[str]
    lastDeploymentChangeTime: str
    moreInfoUrls: _list[str]
    revisionNumber: int
    supportUrl: str
    title: str
    updateId: str

@typing.type_check_only
class ZypperPatch(typing.TypedDict, total=False):
    category: str
    patchName: str
    severity: str
    summary: str
