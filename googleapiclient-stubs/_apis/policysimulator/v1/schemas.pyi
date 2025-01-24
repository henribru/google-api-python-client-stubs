import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudOrgpolicyV2AlternatePolicySpec(
    typing_extensions.TypedDict, total=False
):
    launch: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2CustomConstraint(typing_extensions.TypedDict, total=False):
    actionType: typing_extensions.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    description: str
    displayName: str
    methodTypes: _list[
        typing_extensions.Literal[
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
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2Policy(typing_extensions.TypedDict, total=False):
    alternate: GoogleCloudOrgpolicyV2AlternatePolicySpec
    dryRunSpec: GoogleCloudOrgpolicyV2PolicySpec
    etag: str
    name: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpec(typing_extensions.TypedDict, total=False):
    etag: str
    inheritFromParent: bool
    reset: bool
    rules: _list[GoogleCloudOrgpolicyV2PolicySpecPolicyRule]
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRule(
    typing_extensions.TypedDict, total=False
):
    allowAll: bool
    condition: GoogleTypeExpr
    denyAll: bool
    enforce: bool
    parameters: dict[str, typing.Any]
    values: GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues(
    typing_extensions.TypedDict, total=False
):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1AccessStateDiff(
    typing_extensions.TypedDict, total=False
):
    accessChange: typing_extensions.Literal[
        "ACCESS_CHANGE_TYPE_UNSPECIFIED",
        "NO_CHANGE",
        "UNKNOWN_CHANGE",
        "ACCESS_REVOKED",
        "ACCESS_GAINED",
        "ACCESS_MAYBE_REVOKED",
        "ACCESS_MAYBE_GAINED",
    ]
    baseline: GoogleCloudPolicysimulatorV1ExplainedAccess
    simulated: GoogleCloudPolicysimulatorV1ExplainedAccess

@typing.type_check_only
class GoogleCloudPolicysimulatorV1AccessTuple(typing_extensions.TypedDict, total=False):
    fullResourceName: str
    permission: str
    principal: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1BindingExplanation(
    typing_extensions.TypedDict, total=False
):
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    condition: GoogleTypeExpr
    memberships: dict[str, typing.Any]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    role: str
    rolePermission: typing_extensions.Literal[
        "ROLE_PERMISSION_UNSPECIFIED",
        "ROLE_PERMISSION_INCLUDED",
        "ROLE_PERMISSION_NOT_INCLUDED",
        "ROLE_PERMISSION_UNKNOWN_INFO_DENIED",
    ]
    rolePermissionRelevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembership(
    typing_extensions.TypedDict, total=False
):
    membership: typing_extensions.Literal[
        "MEMBERSHIP_UNSPECIFIED",
        "MEMBERSHIP_INCLUDED",
        "MEMBERSHIP_NOT_INCLUDED",
        "MEMBERSHIP_UNKNOWN_INFO_DENIED",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ExplainedAccess(
    typing_extensions.TypedDict, total=False
):
    accessState: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    errors: _list[GoogleRpcStatus]
    policies: _list[GoogleCloudPolicysimulatorV1ExplainedPolicy]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ExplainedPolicy(
    typing_extensions.TypedDict, total=False
):
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    bindingExplanations: _list[GoogleCloudPolicysimulatorV1BindingExplanation]
    fullResourceName: str
    policy: GoogleIamV1Policy
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ListReplayResultsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    replayResults: _list[GoogleCloudPolicysimulatorV1ReplayResult]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1Replay(typing_extensions.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1ReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1ReplayResultsSummary
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayConfig(
    typing_extensions.TypedDict, total=False
):
    logSource: typing_extensions.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayDiff(typing_extensions.TypedDict, total=False):
    accessDiff: GoogleCloudPolicysimulatorV1AccessStateDiff

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayResult(
    typing_extensions.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicysimulatorV1AccessTuple
    diff: GoogleCloudPolicysimulatorV1ReplayDiff
    error: GoogleRpcStatus
    lastSeenDate: GoogleTypeDate
    name: str
    parent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayResultsSummary(
    typing_extensions.TypedDict, total=False
):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaCreateOrgPolicyViolationsPreviewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    requestTime: str
    resourcesFound: int
    resourcesPending: int
    resourcesScanned: int
    startTime: str
    state: typing_extensions.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaGenerateOrgPolicyViolationsPreviewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    requestTime: str
    resourcesFound: int
    resourcesPending: int
    resourcesScanned: int
    startTime: str
    state: typing_extensions.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaOrgPolicyOverlay(
    typing_extensions.TypedDict, total=False
):
    customConstraints: _list[
        GoogleCloudPolicysimulatorV1alphaOrgPolicyOverlayCustomConstraintOverlay
    ]
    policies: _list[GoogleCloudPolicysimulatorV1alphaOrgPolicyOverlayPolicyOverlay]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaOrgPolicyOverlayCustomConstraintOverlay(
    typing_extensions.TypedDict, total=False
):
    customConstraint: GoogleCloudOrgpolicyV2CustomConstraint
    customConstraintParent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaOrgPolicyOverlayPolicyOverlay(
    typing_extensions.TypedDict, total=False
):
    policy: GoogleCloudOrgpolicyV2Policy
    policyParent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    customConstraints: _list[str]
    name: str
    overlay: GoogleCloudPolicysimulatorV1alphaOrgPolicyOverlay
    resourceCounts: (
        GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreviewResourceCounts
    )
    state: typing_extensions.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]
    violationsCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreviewResourceCounts(
    typing_extensions.TypedDict, total=False
):
    compliant: int
    errors: int
    noncompliant: int
    scanned: int
    unenforced: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaCreateOrgPolicyViolationsPreviewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    requestTime: str
    resourcesFound: int
    resourcesPending: int
    resourcesScanned: int
    startTime: str
    state: typing_extensions.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaGenerateOrgPolicyViolationsPreviewOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    requestTime: str
    resourcesFound: int
    resourcesPending: int
    resourcesScanned: int
    startTime: str
    state: typing_extensions.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyOverlay(
    typing_extensions.TypedDict, total=False
):
    customConstraints: _list[
        GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayCustomConstraintOverlay
    ]
    policies: _list[GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayPolicyOverlay]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayCustomConstraintOverlay(
    typing_extensions.TypedDict, total=False
):
    customConstraint: GoogleCloudOrgpolicyV2CustomConstraint
    customConstraintParent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayPolicyOverlay(
    typing_extensions.TypedDict, total=False
):
    policy: GoogleCloudOrgpolicyV2Policy
    policyParent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreview(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    customConstraints: _list[str]
    name: str
    overlay: GoogleCloudPolicysimulatorV1betaOrgPolicyOverlay
    resourceCounts: (
        GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewResourceCounts
    )
    state: typing_extensions.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]
    violationsCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewResourceCounts(
    typing_extensions.TypedDict, total=False
):
    compliant: int
    errors: int
    noncompliant: int
    scanned: int
    unenforced: int

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
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
