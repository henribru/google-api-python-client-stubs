import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessSelector(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
    roles: _list[str]

@typing.type_check_only
class AnalyzeIamPolicyLongrunningMetadata(typing_extensions.TypedDict, total=False):
    createTime: str

@typing.type_check_only
class AnalyzeIamPolicyLongrunningResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AnalyzeIamPolicyResponse(typing_extensions.TypedDict, total=False):
    fullyExplored: bool
    mainAnalysis: IamPolicyAnalysis
    nonCriticalErrors: _list[GoogleCloudAssetV1p4beta1AnalysisState]
    serviceAccountImpersonationAnalysis: _list[IamPolicyAnalysis]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ExportIamPolicyAnalysisRequest(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    options: Options
    outputConfig: IamPolicyAnalysisOutputConfig

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Access(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    permission: str
    role: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1AccessControlList(
    typing_extensions.TypedDict, total=False
):
    accesses: _list[GoogleCloudAssetV1p4beta1Access]
    resourceEdges: _list[GoogleCloudAssetV1p4beta1Edge]
    resources: _list[GoogleCloudAssetV1p4beta1Resource]

@typing.type_check_only
class GoogleCloudAssetV1p4beta1AnalysisState(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAssetV1p4beta1Edge(typing_extensions.TypedDict, total=False):
    sourceNode: str
    targetNode: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Identity(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    name: str

@typing.type_check_only
class GoogleCloudAssetV1p4beta1IdentityList(typing_extensions.TypedDict, total=False):
    groupEdges: _list[GoogleCloudAssetV1p4beta1Edge]
    identities: _list[GoogleCloudAssetV1p4beta1Identity]

@typing.type_check_only
class GoogleCloudAssetV1p4beta1Resource(typing_extensions.TypedDict, total=False):
    analysisState: GoogleCloudAssetV1p4beta1AnalysisState
    fullResourceName: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1Asset(typing_extensions.TypedDict, total=False):
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
class GoogleCloudAssetV1p7beta1RelatedAsset(typing_extensions.TypedDict, total=False):
    ancestors: _list[str]
    asset: str
    assetType: str

@typing.type_check_only
class GoogleCloudAssetV1p7beta1RelatedAssets(typing_extensions.TypedDict, total=False):
    assets: _list[GoogleCloudAssetV1p7beta1RelatedAsset]
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
    data: dict[str, typing.Any]
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
    allowedValues: _list[str]
    deniedValues: _list[str]
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
    scopes: _list[str]
    title: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1ApiOperation(
    typing_extensions.TypedDict, total=False
):
    methodSelectors: _list[GoogleIdentityAccesscontextmanagerV1MethodSelector]
    serviceName: str

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1BasicLevel(
    typing_extensions.TypedDict, total=False
):
    combiningFunction: typing_extensions.Literal["AND", "OR"]
    conditions: _list[GoogleIdentityAccesscontextmanagerV1Condition]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1Condition(
    typing_extensions.TypedDict, total=False
):
    devicePolicy: GoogleIdentityAccesscontextmanagerV1DevicePolicy
    ipSubnetworks: _list[str]
    members: _list[str]
    negate: bool
    regions: _list[str]
    requiredAccessLevels: _list[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1CustomLevel(
    typing_extensions.TypedDict, total=False
):
    expr: Expr

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1DevicePolicy(
    typing_extensions.TypedDict, total=False
):
    allowedDeviceManagementLevels: _list[str]
    allowedEncryptionStatuses: _list[str]
    osConstraints: _list[GoogleIdentityAccesscontextmanagerV1OsConstraint]
    requireAdminApproval: bool
    requireCorpOwned: bool
    requireScreenlock: bool

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1EgressFrom(
    typing_extensions.TypedDict, total=False
):
    identities: _list[str]
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
    externalResources: _list[str]
    operations: _list[GoogleIdentityAccesscontextmanagerV1ApiOperation]
    resources: _list[str]

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1IngressFrom(
    typing_extensions.TypedDict, total=False
):
    identities: _list[str]
    identityType: typing_extensions.Literal[
        "IDENTITY_TYPE_UNSPECIFIED",
        "ANY_IDENTITY",
        "ANY_USER_ACCOUNT",
        "ANY_SERVICE_ACCOUNT",
    ]
    sources: _list[GoogleIdentityAccesscontextmanagerV1IngressSource]

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
    operations: _list[GoogleIdentityAccesscontextmanagerV1ApiOperation]
    resources: _list[str]

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
    accessLevels: _list[str]
    egressPolicies: _list[GoogleIdentityAccesscontextmanagerV1EgressPolicy]
    ingressPolicies: _list[GoogleIdentityAccesscontextmanagerV1IngressPolicy]
    resources: _list[str]
    restrictedServices: _list[str]
    vpcAccessibleServices: GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices

@typing.type_check_only
class GoogleIdentityAccesscontextmanagerV1VpcAccessibleServices(
    typing_extensions.TypedDict, total=False
):
    allowedServices: _list[str]
    enableRestriction: bool

@typing.type_check_only
class IamPolicyAnalysis(typing_extensions.TypedDict, total=False):
    analysisQuery: IamPolicyAnalysisQuery
    analysisResults: _list[IamPolicyAnalysisResult]
    fullyExplored: bool

@typing.type_check_only
class IamPolicyAnalysisOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class IamPolicyAnalysisQuery(typing_extensions.TypedDict, total=False):
    accessSelector: AccessSelector
    identitySelector: IdentitySelector
    parent: str
    resourceSelector: ResourceSelector

@typing.type_check_only
class IamPolicyAnalysisResult(typing_extensions.TypedDict, total=False):
    accessControlLists: _list[GoogleCloudAssetV1p4beta1AccessControlList]
    attachedResourceFullName: str
    fullyExplored: bool
    iamBinding: Binding
    identityList: GoogleCloudAssetV1p4beta1IdentityList

@typing.type_check_only
class IdentitySelector(typing_extensions.TypedDict, total=False):
    identity: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Options(typing_extensions.TypedDict, total=False):
    analyzeServiceAccountImpersonation: bool
    expandGroups: bool
    expandResources: bool
    expandRoles: bool
    outputGroupEdges: bool
    outputResourceEdges: bool

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ResourceSelector(typing_extensions.TypedDict, total=False):
    fullResourceName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
