import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaAccessTuple(
    typing_extensions.TypedDict, total=False
):
    conditionContext: GoogleCloudPolicytroubleshooterIamV3betaConditionContext
    fullResourceName: str
    permission: str
    permissionFqdn: str
    principal: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaAllowBindingExplanation(
    typing_extensions.TypedDict, total=False
):
    allowAccessState: typing_extensions.Literal[
        "ALLOW_ACCESS_STATE_UNSPECIFIED",
        "ALLOW_ACCESS_STATE_GRANTED",
        "ALLOW_ACCESS_STATE_NOT_GRANTED",
        "ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "ALLOW_ACCESS_STATE_UNKNOWN_INFO",
    ]
    combinedMembership: GoogleCloudPolicytroubleshooterIamV3betaAllowBindingExplanationAnnotatedAllowMembership
    condition: GoogleTypeExpr
    conditionExplanation: GoogleCloudPolicytroubleshooterIamV3betaConditionExplanation
    memberships: dict[str, typing.Any]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]
    role: str
    rolePermission: typing_extensions.Literal[
        "ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED",
        "ROLE_PERMISSION_INCLUDED",
        "ROLE_PERMISSION_NOT_INCLUDED",
        "ROLE_PERMISSION_UNKNOWN_INFO",
    ]
    rolePermissionRelevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaAllowBindingExplanationAnnotatedAllowMembership(
    typing_extensions.TypedDict, total=False
):
    membership: typing_extensions.Literal[
        "MEMBERSHIP_MATCHING_STATE_UNSPECIFIED",
        "MEMBERSHIP_MATCHED",
        "MEMBERSHIP_NOT_MATCHED",
        "MEMBERSHIP_UNKNOWN_INFO",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaAllowPolicyExplanation(
    typing_extensions.TypedDict, total=False
):
    allowAccessState: typing_extensions.Literal[
        "ALLOW_ACCESS_STATE_UNSPECIFIED",
        "ALLOW_ACCESS_STATE_GRANTED",
        "ALLOW_ACCESS_STATE_NOT_GRANTED",
        "ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "ALLOW_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedPolicies: _list[
        GoogleCloudPolicytroubleshooterIamV3betaExplainedAllowPolicy
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionContext(
    typing_extensions.TypedDict, total=False
):
    destination: GoogleCloudPolicytroubleshooterIamV3betaConditionContextPeer
    effectiveTags: _list[
        GoogleCloudPolicytroubleshooterIamV3betaConditionContextEffectiveTag
    ]
    request: GoogleCloudPolicytroubleshooterIamV3betaConditionContextRequest
    resource: GoogleCloudPolicytroubleshooterIamV3betaConditionContextResource

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionContextEffectiveTag(
    typing_extensions.TypedDict, total=False
):
    inherited: bool
    namespacedTagKey: str
    namespacedTagValue: str
    tagKey: str
    tagKeyParentName: str
    tagValue: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionContextPeer(
    typing_extensions.TypedDict, total=False
):
    ip: str
    port: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionContextRequest(
    typing_extensions.TypedDict, total=False
):
    receiveTime: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionContextResource(
    typing_extensions.TypedDict, total=False
):
    name: str
    service: str
    type: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionExplanation(
    typing_extensions.TypedDict, total=False
):
    errors: _list[GoogleRpcStatus]
    evaluationStates: _list[
        GoogleCloudPolicytroubleshooterIamV3betaConditionExplanationEvaluationState
    ]
    value: typing.Any

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaConditionExplanationEvaluationState(
    typing_extensions.TypedDict, total=False
):
    end: int
    errors: _list[GoogleRpcStatus]
    start: int
    value: typing.Any

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaDenyPolicyExplanation(
    typing_extensions.TypedDict, total=False
):
    denyAccessState: typing_extensions.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedResources: _list[
        GoogleCloudPolicytroubleshooterIamV3betaExplainedDenyResource
    ]
    permissionDeniable: bool
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanation(
    typing_extensions.TypedDict, total=False
):
    combinedDeniedPermission: GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanationAnnotatedPermissionMatching
    combinedDeniedPrincipal: GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanationAnnotatedDenyPrincipalMatching
    combinedExceptionPermission: GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanationAnnotatedPermissionMatching
    combinedExceptionPrincipal: GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanationAnnotatedDenyPrincipalMatching
    condition: GoogleTypeExpr
    conditionExplanation: GoogleCloudPolicytroubleshooterIamV3betaConditionExplanation
    deniedPermissions: dict[str, typing.Any]
    deniedPrincipals: dict[str, typing.Any]
    denyAccessState: typing_extensions.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    exceptionPermissions: dict[str, typing.Any]
    exceptionPrincipals: dict[str, typing.Any]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanationAnnotatedDenyPrincipalMatching(
    typing_extensions.TypedDict, total=False
):
    membership: typing_extensions.Literal[
        "MEMBERSHIP_MATCHING_STATE_UNSPECIFIED",
        "MEMBERSHIP_MATCHED",
        "MEMBERSHIP_NOT_MATCHED",
        "MEMBERSHIP_UNKNOWN_INFO",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanationAnnotatedPermissionMatching(
    typing_extensions.TypedDict, total=False
):
    permissionMatchingState: typing_extensions.Literal[
        "PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED",
        "PERMISSION_PATTERN_MATCHED",
        "PERMISSION_PATTERN_NOT_MATCHED",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedAllowPolicy(
    typing_extensions.TypedDict, total=False
):
    allowAccessState: typing_extensions.Literal[
        "ALLOW_ACCESS_STATE_UNSPECIFIED",
        "ALLOW_ACCESS_STATE_GRANTED",
        "ALLOW_ACCESS_STATE_NOT_GRANTED",
        "ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "ALLOW_ACCESS_STATE_UNKNOWN_INFO",
    ]
    bindingExplanations: _list[
        GoogleCloudPolicytroubleshooterIamV3betaAllowBindingExplanation
    ]
    fullResourceName: str
    policy: GoogleIamV1Policy
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedDenyPolicy(
    typing_extensions.TypedDict, total=False
):
    denyAccessState: typing_extensions.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    policy: GoogleIamV2Policy
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]
    ruleExplanations: _list[GoogleCloudPolicytroubleshooterIamV3betaDenyRuleExplanation]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedDenyResource(
    typing_extensions.TypedDict, total=False
):
    denyAccessState: typing_extensions.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedPolicies: _list[
        GoogleCloudPolicytroubleshooterIamV3betaExplainedDenyPolicy
    ]
    fullResourceName: str
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedPABBindingAndPolicy(
    typing_extensions.TypedDict, total=False
):
    bindingAndPolicyAccessState: typing_extensions.Literal[
        "PAB_ACCESS_STATE_UNSPECIFIED",
        "PAB_ACCESS_STATE_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ENFORCED",
        "PAB_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedPolicy: GoogleCloudPolicytroubleshooterIamV3betaExplainedPABPolicy
    explainedPolicyBinding: (
        GoogleCloudPolicytroubleshooterIamV3betaExplainedPolicyBinding
    )
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedPABPolicy(
    typing_extensions.TypedDict, total=False
):
    explainedRules: _list[GoogleCloudPolicytroubleshooterIamV3betaExplainedPABRule]
    policy: GoogleIamV3PrincipalAccessBoundaryPolicy
    policyAccessState: typing_extensions.Literal[
        "PAB_ACCESS_STATE_UNSPECIFIED",
        "PAB_ACCESS_STATE_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ENFORCED",
        "PAB_ACCESS_STATE_UNKNOWN_INFO",
    ]
    policyVersion: GoogleCloudPolicytroubleshooterIamV3betaExplainedPABPolicyVersion
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedPABPolicyVersion(
    typing_extensions.TypedDict, total=False
):
    enforcementState: typing_extensions.Literal[
        "PAB_POLICY_ENFORCEMENT_STATE_UNSPECIFIED",
        "PAB_POLICY_ENFORCEMENT_STATE_ENFORCED",
        "PAB_POLICY_ENFORCEMENT_STATE_NOT_ENFORCED",
    ]
    version: int

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedPABRule(
    typing_extensions.TypedDict, total=False
):
    combinedResourceInclusionState: typing_extensions.Literal[
        "RESOURCE_INCLUSION_STATE_UNSPECIFIED",
        "RESOURCE_INCLUSION_STATE_INCLUDED",
        "RESOURCE_INCLUSION_STATE_NOT_INCLUDED",
        "RESOURCE_INCLUSION_STATE_UNKNOWN_INFO",
        "RESOURCE_INCLUSION_STATE_UNKNOWN_UNSUPPORTED",
    ]
    effect: typing_extensions.Literal["EFFECT_UNSPECIFIED", "ALLOW"]
    explainedResources: _list[
        GoogleCloudPolicytroubleshooterIamV3betaExplainedPABRuleExplainedResource
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]
    ruleAccessState: typing_extensions.Literal[
        "PAB_ACCESS_STATE_UNSPECIFIED",
        "PAB_ACCESS_STATE_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ENFORCED",
        "PAB_ACCESS_STATE_UNKNOWN_INFO",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedPABRuleExplainedResource(
    typing_extensions.TypedDict, total=False
):
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]
    resource: str
    resourceInclusionState: typing_extensions.Literal[
        "RESOURCE_INCLUSION_STATE_UNSPECIFIED",
        "RESOURCE_INCLUSION_STATE_INCLUDED",
        "RESOURCE_INCLUSION_STATE_NOT_INCLUDED",
        "RESOURCE_INCLUSION_STATE_UNKNOWN_INFO",
        "RESOURCE_INCLUSION_STATE_UNKNOWN_UNSUPPORTED",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaExplainedPolicyBinding(
    typing_extensions.TypedDict, total=False
):
    conditionExplanation: GoogleCloudPolicytroubleshooterIamV3betaConditionExplanation
    policyBinding: GoogleIamV3PolicyBinding
    policyBindingState: typing_extensions.Literal[
        "POLICY_BINDING_STATE_UNSPECIFIED",
        "POLICY_BINDING_STATE_ENFORCED",
        "POLICY_BINDING_STATE_NOT_ENFORCED",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaPABPolicyExplanation(
    typing_extensions.TypedDict, total=False
):
    explainedBindingsAndPolicies: _list[
        GoogleCloudPolicytroubleshooterIamV3betaExplainedPABBindingAndPolicy
    ]
    principalAccessBoundaryAccessState: typing_extensions.Literal[
        "PAB_ACCESS_STATE_UNSPECIFIED",
        "PAB_ACCESS_STATE_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ALLOWED",
        "PAB_ACCESS_STATE_NOT_ENFORCED",
        "PAB_ACCESS_STATE_UNKNOWN_INFO",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaTroubleshootIamPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterIamV3betaAccessTuple

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3betaTroubleshootIamPolicyResponse(
    typing_extensions.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterIamV3betaAccessTuple
    allowPolicyExplanation: (
        GoogleCloudPolicytroubleshooterIamV3betaAllowPolicyExplanation
    )
    denyPolicyExplanation: GoogleCloudPolicytroubleshooterIamV3betaDenyPolicyExplanation
    overallAccessState: typing_extensions.Literal[
        "OVERALL_ACCESS_STATE_UNSPECIFIED",
        "CAN_ACCESS",
        "CANNOT_ACCESS",
        "UNKNOWN_INFO",
        "UNKNOWN_CONDITIONAL",
    ]
    pabPolicyExplanation: GoogleCloudPolicytroubleshooterIamV3betaPABPolicyExplanation

@typing.type_check_only
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV2DenyRule(typing_extensions.TypedDict, total=False):
    denialCondition: GoogleTypeExpr
    deniedPermissions: _list[str]
    deniedPrincipals: _list[str]
    exceptionPermissions: _list[str]
    exceptionPrincipals: _list[str]

@typing.type_check_only
class GoogleIamV2Policy(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    kind: str
    name: str
    rules: _list[GoogleIamV2PolicyRule]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleIamV2PolicyRule(typing_extensions.TypedDict, total=False):
    denyRule: GoogleIamV2DenyRule
    description: str

@typing.type_check_only
class GoogleIamV3PolicyBinding(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    condition: GoogleTypeExpr
    createTime: str
    displayName: str
    etag: str
    name: str
    policy: str
    policyKind: typing_extensions.Literal[
        "POLICY_KIND_UNSPECIFIED", "PRINCIPAL_ACCESS_BOUNDARY", "ACCESS"
    ]
    policyUid: str
    target: GoogleIamV3PolicyBindingTarget
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleIamV3PolicyBindingTarget(typing_extensions.TypedDict, total=False):
    principalSet: str
    resource: str

@typing.type_check_only
class GoogleIamV3PrincipalAccessBoundaryPolicy(
    typing_extensions.TypedDict, total=False
):
    annotations: dict[str, typing.Any]
    createTime: str
    details: GoogleIamV3PrincipalAccessBoundaryPolicyDetails
    displayName: str
    etag: str
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleIamV3PrincipalAccessBoundaryPolicyDetails(
    typing_extensions.TypedDict, total=False
):
    enforcementVersion: str
    rules: _list[GoogleIamV3PrincipalAccessBoundaryPolicyRule]

@typing.type_check_only
class GoogleIamV3PrincipalAccessBoundaryPolicyRule(
    typing_extensions.TypedDict, total=False
):
    description: str
    effect: typing_extensions.Literal["EFFECT_UNSPECIFIED", "ALLOW"]
    resources: _list[str]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
