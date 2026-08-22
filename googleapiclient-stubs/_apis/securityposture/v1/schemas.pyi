import typing

_list = list

@typing.type_check_only
class AssetDetails(typing.TypedDict, total=False):
    asset: str
    assetType: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ComplianceStandard(typing.TypedDict, total=False):
    control: str
    standard: str

@typing.type_check_only
class Constraint(typing.TypedDict, total=False):
    orgPolicyConstraint: OrgPolicyConstraint
    orgPolicyConstraintCustom: OrgPolicyConstraintCustom
    securityHealthAnalyticsCustomModule: SecurityHealthAnalyticsCustomModule
    securityHealthAnalyticsModule: SecurityHealthAnalyticsModule

@typing.type_check_only
class CreateIaCValidationReportRequest(typing.TypedDict, total=False):
    iac: IaC

@typing.type_check_only
class CustomConfig(typing.TypedDict, total=False):
    customOutput: CustomOutputSpec
    description: str
    predicate: Expr
    recommendation: str
    resourceSelector: ResourceSelector
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class CustomOutputSpec(typing.TypedDict, total=False):
    properties: _list[Property]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtractPostureRequest(typing.TypedDict, total=False):
    postureId: str
    workload: str

@typing.type_check_only
class GoogleCloudSecuritypostureV1CustomConstraint(typing.TypedDict, total=False):
    actionType: typing.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    description: str
    displayName: str
    methodTypes: _list[
        typing.Literal["METHOD_TYPE_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"]
    ]
    name: str
    resourceTypes: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudSecuritypostureV1PolicyRule(typing.TypedDict, total=False):
    allowAll: bool
    condition: Expr
    denyAll: bool
    enforce: bool
    parameters: dict[str, typing.Any]
    resourceTypes: ResourceTypes
    values: GoogleCloudSecuritypostureV1PolicyRuleStringValues

@typing.type_check_only
class GoogleCloudSecuritypostureV1PolicyRuleStringValues(typing.TypedDict, total=False):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class IaC(typing.TypedDict, total=False):
    tfPlan: str

@typing.type_check_only
class IaCValidationReport(typing.TypedDict, total=False):
    note: str
    violations: _list[Violation]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPostureDeploymentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    postureDeployments: _list[PostureDeployment]
    unreachable: _list[str]

@typing.type_check_only
class ListPostureRevisionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[Posture]

@typing.type_check_only
class ListPostureTemplatesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    postureTemplates: _list[PostureTemplate]

@typing.type_check_only
class ListPosturesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    postures: _list[Posture]
    unreachable: _list[str]

@typing.type_check_only
class ListReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    errorMessage: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class OrgPolicyConstraint(typing.TypedDict, total=False):
    cannedConstraintId: str
    policyRules: _list[GoogleCloudSecuritypostureV1PolicyRule]

@typing.type_check_only
class OrgPolicyConstraintCustom(typing.TypedDict, total=False):
    customConstraint: GoogleCloudSecuritypostureV1CustomConstraint
    policyRules: _list[GoogleCloudSecuritypostureV1PolicyRule]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    complianceStandards: _list[ComplianceStandard]
    constraint: Constraint
    description: str
    policyId: str

@typing.type_check_only
class PolicyDetails(typing.TypedDict, total=False):
    complianceStandards: _list[str]
    constraint: str
    constraintType: typing.Literal[
        "CONSTRAINT_TYPE_UNSPECIFIED",
        "SECURITY_HEALTH_ANALYTICS_CUSTOM_MODULE",
        "ORG_POLICY_CUSTOM",
        "SECURITY_HEALTH_ANALYTICS_MODULE",
        "ORG_POLICY",
        "REGO_POLICY",
    ]
    description: str

@typing.type_check_only
class PolicySet(typing.TypedDict, total=False):
    description: str
    policies: _list[Policy]
    policySetId: str

@typing.type_check_only
class Posture(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    categories: _list[
        typing.Literal["CATEGORY_UNSPECIFIED", "AI", "AWS", "GCP", "AZURE"]
    ]
    createTime: str
    description: str
    etag: str
    name: str
    policySets: _list[PolicySet]
    reconciling: bool
    revisionId: str
    state: typing.Literal["STATE_UNSPECIFIED", "DEPRECATED", "DRAFT", "ACTIVE"]
    updateTime: str

@typing.type_check_only
class PostureDeployment(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    categories: _list[
        typing.Literal["CATEGORY_UNSPECIFIED", "AI", "AWS", "GCP", "AZURE"]
    ]
    createTime: str
    description: str
    desiredPostureId: str
    desiredPostureRevisionId: str
    etag: str
    failureMessage: str
    name: str
    postureId: str
    postureRevisionId: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "DELETING",
        "UPDATING",
        "ACTIVE",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETE_FAILED",
    ]
    targetResource: str
    updateTime: str

@typing.type_check_only
class PostureDetails(typing.TypedDict, total=False):
    policySet: str
    posture: str
    postureDeployment: str
    postureDeploymentTargetResource: str
    postureRevisionId: str

@typing.type_check_only
class PostureTemplate(typing.TypedDict, total=False):
    categories: _list[
        typing.Literal["CATEGORY_UNSPECIFIED", "AI", "AWS", "GCP", "AZURE"]
    ]
    description: str
    name: str
    policySets: _list[PolicySet]
    revisionId: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED"]

@typing.type_check_only
class Property(typing.TypedDict, total=False):
    name: str
    valueExpression: Expr

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    createTime: str
    iacValidationReport: IaCValidationReport
    name: str
    updateTime: str

@typing.type_check_only
class ResourceSelector(typing.TypedDict, total=False):
    resourceTypes: _list[str]

@typing.type_check_only
class ResourceTypes(typing.TypedDict, total=False):
    included: _list[str]

@typing.type_check_only
class SecurityHealthAnalyticsCustomModule(typing.TypedDict, total=False):
    config: CustomConfig
    displayName: str
    id: str
    moduleEnablementState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]

@typing.type_check_only
class SecurityHealthAnalyticsModule(typing.TypedDict, total=False):
    moduleEnablementState: typing.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]
    moduleName: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Violation(typing.TypedDict, total=False):
    assetId: str
    nextSteps: str
    policyId: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    violatedAsset: AssetDetails
    violatedPolicy: PolicyDetails
    violatedPosture: PostureDetails
