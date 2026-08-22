import typing

_list = list

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3AccessTuple(typing.TypedDict, total=False):
    conditionContext: GoogleCloudPolicytroubleshooterIamV3ConditionContext
    fullResourceName: str
    permission: str
    permissionFqdn: str
    principal: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3AllowBindingExplanation(
    typing.TypedDict, total=False
):
    allowAccessState: typing.Literal[
        "ALLOW_ACCESS_STATE_UNSPECIFIED",
        "ALLOW_ACCESS_STATE_GRANTED",
        "ALLOW_ACCESS_STATE_NOT_GRANTED",
        "ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "ALLOW_ACCESS_STATE_UNKNOWN_INFO",
    ]
    combinedMembership: GoogleCloudPolicytroubleshooterIamV3AllowBindingExplanationAnnotatedAllowMembership
    condition: GoogleTypeExpr
    conditionExplanation: GoogleCloudPolicytroubleshooterIamV3ConditionExplanation
    memberships: dict[str, typing.Any]
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]
    role: str
    rolePermission: typing.Literal[
        "ROLE_PERMISSION_INCLUSION_STATE_UNSPECIFIED",
        "ROLE_PERMISSION_INCLUDED",
        "ROLE_PERMISSION_NOT_INCLUDED",
        "ROLE_PERMISSION_UNKNOWN_INFO",
    ]
    rolePermissionRelevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3AllowBindingExplanationAnnotatedAllowMembership(
    typing.TypedDict, total=False
):
    membership: typing.Literal[
        "MEMBERSHIP_MATCHING_STATE_UNSPECIFIED",
        "MEMBERSHIP_MATCHED",
        "MEMBERSHIP_NOT_MATCHED",
        "MEMBERSHIP_UNKNOWN_INFO",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3AllowPolicyExplanation(
    typing.TypedDict, total=False
):
    allowAccessState: typing.Literal[
        "ALLOW_ACCESS_STATE_UNSPECIFIED",
        "ALLOW_ACCESS_STATE_GRANTED",
        "ALLOW_ACCESS_STATE_NOT_GRANTED",
        "ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "ALLOW_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedPolicies: _list[GoogleCloudPolicytroubleshooterIamV3ExplainedAllowPolicy]
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionContext(
    typing.TypedDict, total=False
):
    destination: GoogleCloudPolicytroubleshooterIamV3ConditionContextPeer
    effectiveTags: _list[
        GoogleCloudPolicytroubleshooterIamV3ConditionContextEffectiveTag
    ]
    request: GoogleCloudPolicytroubleshooterIamV3ConditionContextRequest
    resource: GoogleCloudPolicytroubleshooterIamV3ConditionContextResource

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionContextEffectiveTag(
    typing.TypedDict, total=False
):
    inherited: bool
    namespacedTagKey: str
    namespacedTagValue: str
    tagKey: str
    tagKeyParentName: str
    tagValue: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionContextPeer(
    typing.TypedDict, total=False
):
    ip: str
    port: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionContextRequest(
    typing.TypedDict, total=False
):
    receiveTime: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionContextResource(
    typing.TypedDict, total=False
):
    name: str
    service: str
    type: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionExplanation(
    typing.TypedDict, total=False
):
    errors: _list[GoogleRpcStatus]
    evaluationStates: _list[
        GoogleCloudPolicytroubleshooterIamV3ConditionExplanationEvaluationState
    ]
    value: typing.Any

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ConditionExplanationEvaluationState(
    typing.TypedDict, total=False
):
    end: int
    errors: _list[GoogleRpcStatus]
    start: int
    value: typing.Any

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3DenyPolicyExplanation(
    typing.TypedDict, total=False
):
    denyAccessState: typing.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedResources: _list[GoogleCloudPolicytroubleshooterIamV3ExplainedDenyResource]
    permissionDeniable: bool
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanation(
    typing.TypedDict, total=False
):
    combinedDeniedPermission: GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanationAnnotatedPermissionMatching
    combinedDeniedPrincipal: GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanationAnnotatedDenyPrincipalMatching
    combinedExceptionPermission: GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanationAnnotatedPermissionMatching
    combinedExceptionPrincipal: GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanationAnnotatedDenyPrincipalMatching
    condition: GoogleTypeExpr
    conditionExplanation: GoogleCloudPolicytroubleshooterIamV3ConditionExplanation
    deniedPermissions: dict[str, typing.Any]
    deniedPrincipals: dict[str, typing.Any]
    denyAccessState: typing.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    exceptionPermissions: dict[str, typing.Any]
    exceptionPrincipals: dict[str, typing.Any]
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanationAnnotatedDenyPrincipalMatching(
    typing.TypedDict, total=False
):
    membership: typing.Literal[
        "MEMBERSHIP_MATCHING_STATE_UNSPECIFIED",
        "MEMBERSHIP_MATCHED",
        "MEMBERSHIP_NOT_MATCHED",
        "MEMBERSHIP_UNKNOWN_INFO",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanationAnnotatedPermissionMatching(
    typing.TypedDict, total=False
):
    permissionMatchingState: typing.Literal[
        "PERMISSION_PATTERN_MATCHING_STATE_UNSPECIFIED",
        "PERMISSION_PATTERN_MATCHED",
        "PERMISSION_PATTERN_NOT_MATCHED",
    ]
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ExplainedAllowPolicy(
    typing.TypedDict, total=False
):
    allowAccessState: typing.Literal[
        "ALLOW_ACCESS_STATE_UNSPECIFIED",
        "ALLOW_ACCESS_STATE_GRANTED",
        "ALLOW_ACCESS_STATE_NOT_GRANTED",
        "ALLOW_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "ALLOW_ACCESS_STATE_UNKNOWN_INFO",
    ]
    bindingExplanations: _list[
        GoogleCloudPolicytroubleshooterIamV3AllowBindingExplanation
    ]
    fullResourceName: str
    policy: GoogleIamV1Policy
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ExplainedDenyPolicy(
    typing.TypedDict, total=False
):
    denyAccessState: typing.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    policy: GoogleIamV2Policy
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]
    ruleExplanations: _list[GoogleCloudPolicytroubleshooterIamV3DenyRuleExplanation]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3ExplainedDenyResource(
    typing.TypedDict, total=False
):
    denyAccessState: typing.Literal[
        "DENY_ACCESS_STATE_UNSPECIFIED",
        "DENY_ACCESS_STATE_DENIED",
        "DENY_ACCESS_STATE_NOT_DENIED",
        "DENY_ACCESS_STATE_UNKNOWN_CONDITIONAL",
        "DENY_ACCESS_STATE_UNKNOWN_INFO",
    ]
    explainedPolicies: _list[GoogleCloudPolicytroubleshooterIamV3ExplainedDenyPolicy]
    fullResourceName: str
    relevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED",
        "HEURISTIC_RELEVANCE_NORMAL",
        "HEURISTIC_RELEVANCE_HIGH",
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3TroubleshootIamPolicyRequest(
    typing.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterIamV3AccessTuple

@typing.type_check_only
class GoogleCloudPolicytroubleshooterIamV3TroubleshootIamPolicyResponse(
    typing.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterIamV3AccessTuple
    allowPolicyExplanation: GoogleCloudPolicytroubleshooterIamV3AllowPolicyExplanation
    denyPolicyExplanation: GoogleCloudPolicytroubleshooterIamV3DenyPolicyExplanation
    overallAccessState: typing.Literal[
        "OVERALL_ACCESS_STATE_UNSPECIFIED",
        "CAN_ACCESS",
        "CANNOT_ACCESS",
        "UNKNOWN_INFO",
        "UNKNOWN_CONDITIONAL",
    ]

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV2DenyRule(typing.TypedDict, total=False):
    denialCondition: GoogleTypeExpr
    deniedPermissions: _list[str]
    deniedPrincipals: _list[str]
    exceptionPermissions: _list[str]
    exceptionPrincipals: _list[str]

@typing.type_check_only
class GoogleIamV2Policy(typing.TypedDict, total=False):
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
class GoogleIamV2PolicyRule(typing.TypedDict, total=False):
    denyRule: GoogleIamV2DenyRule
    description: str

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
