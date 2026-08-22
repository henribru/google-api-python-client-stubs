import typing

_list = list

@typing.type_check_only
class GoogleCloudOrgpolicyV2AlternatePolicySpec(typing.TypedDict, total=False):
    launch: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2CustomConstraint(typing.TypedDict, total=False):
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
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2Policy(typing.TypedDict, total=False):
    alternate: GoogleCloudOrgpolicyV2AlternatePolicySpec
    dryRunSpec: GoogleCloudOrgpolicyV2PolicySpec
    etag: str
    name: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpec(typing.TypedDict, total=False):
    etag: str
    inheritFromParent: bool
    reset: bool
    rules: _list[GoogleCloudOrgpolicyV2PolicySpecPolicyRule]
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRule(typing.TypedDict, total=False):
    allowAll: bool
    condition: GoogleTypeExpr
    denyAll: bool
    enforce: bool
    parameters: dict[str, typing.Any]
    values: GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues(
    typing.TypedDict, total=False
):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1Replay(typing.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1ReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1ReplayResultsSummary
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayConfig(typing.TypedDict, total=False):
    logSource: typing.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayOperationMetadata(
    typing.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayResultsSummary(typing.TypedDict, total=False):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaAccessStateDiff(typing.TypedDict, total=False):
    accessChange: typing.Literal[
        "ACCESS_CHANGE_TYPE_UNSPECIFIED",
        "NO_CHANGE",
        "UNKNOWN_CHANGE",
        "ACCESS_REVOKED",
        "ACCESS_GAINED",
        "ACCESS_MAYBE_REVOKED",
        "ACCESS_MAYBE_GAINED",
    ]
    baseline: GoogleCloudPolicysimulatorV1betaExplainedAccess
    simulated: GoogleCloudPolicysimulatorV1betaExplainedAccess

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaAccessTuple(typing.TypedDict, total=False):
    fullResourceName: str
    permission: str
    principal: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaBindingExplanation(typing.TypedDict, total=False):
    access: typing.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    condition: GoogleTypeExpr
    memberships: dict[str, typing.Any]
    relevance: typing.Literal["HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"]
    role: str
    rolePermission: typing.Literal[
        "ROLE_PERMISSION_UNSPECIFIED",
        "ROLE_PERMISSION_INCLUDED",
        "ROLE_PERMISSION_NOT_INCLUDED",
        "ROLE_PERMISSION_UNKNOWN_INFO_DENIED",
    ]
    rolePermissionRelevance: typing.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaBindingExplanationAnnotatedMembership(
    typing.TypedDict, total=False
):
    membership: typing.Literal[
        "MEMBERSHIP_UNSPECIFIED",
        "MEMBERSHIP_INCLUDED",
        "MEMBERSHIP_NOT_INCLUDED",
        "MEMBERSHIP_UNKNOWN_INFO_DENIED",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]
    relevance: typing.Literal["HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaCreateOrgPolicyViolationsPreviewOperationMetadata(
    typing.TypedDict, total=False
):
    requestTime: str
    resourcesFound: int
    resourcesPending: int
    resourcesScanned: int
    startTime: str
    state: typing.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaExplainedAccess(typing.TypedDict, total=False):
    accessState: typing.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    errors: _list[GoogleRpcStatus]
    policies: _list[GoogleCloudPolicysimulatorV1betaExplainedPolicy]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaExplainedPolicy(typing.TypedDict, total=False):
    access: typing.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    bindingExplanations: _list[GoogleCloudPolicysimulatorV1betaBindingExplanation]
    fullResourceName: str
    policy: GoogleIamV1Policy
    relevance: typing.Literal["HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaGenerateOrgPolicyViolationsPreviewOperationMetadata(
    typing.TypedDict, total=False
):
    requestTime: str
    resourcesFound: int
    resourcesPending: int
    resourcesScanned: int
    startTime: str
    state: typing.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsPreviewsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    orgPolicyViolationsPreviews: _list[
        GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreview
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListOrgPolicyViolationsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    orgPolicyViolations: _list[GoogleCloudPolicysimulatorV1betaOrgPolicyViolation]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListReplayResultsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    replayResults: _list[GoogleCloudPolicysimulatorV1betaReplayResult]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaListReplaysResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    replays: _list[GoogleCloudPolicysimulatorV1betaReplay]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyOverlay(typing.TypedDict, total=False):
    customConstraints: _list[
        GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayCustomConstraintOverlay
    ]
    policies: _list[GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayPolicyOverlay]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayCustomConstraintOverlay(
    typing.TypedDict, total=False
):
    customConstraint: GoogleCloudOrgpolicyV2CustomConstraint
    customConstraintParent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyOverlayPolicyOverlay(
    typing.TypedDict, total=False
):
    policy: GoogleCloudOrgpolicyV2Policy
    policyParent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyViolation(typing.TypedDict, total=False):
    customConstraint: GoogleCloudOrgpolicyV2CustomConstraint
    error: GoogleRpcStatus
    name: str
    resource: GoogleCloudPolicysimulatorV1betaResourceContext

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreview(
    typing.TypedDict, total=False
):
    createTime: str
    customConstraints: _list[str]
    name: str
    overlay: GoogleCloudPolicysimulatorV1betaOrgPolicyOverlay
    resourceCounts: (
        GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewResourceCounts
    )
    state: typing.Literal[
        "PREVIEW_STATE_UNSPECIFIED",
        "PREVIEW_PENDING",
        "PREVIEW_RUNNING",
        "PREVIEW_SUCCEEDED",
        "PREVIEW_FAILED",
    ]
    violationsCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewResourceCounts(
    typing.TypedDict, total=False
):
    compliant: int
    errors: int
    noncompliant: int
    scanned: int
    unenforced: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaReplay(typing.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1betaReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1betaReplayResultsSummary
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaReplayConfig(typing.TypedDict, total=False):
    logSource: typing.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaReplayDiff(typing.TypedDict, total=False):
    accessDiff: GoogleCloudPolicysimulatorV1betaAccessStateDiff

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaReplayResult(typing.TypedDict, total=False):
    accessTuple: GoogleCloudPolicysimulatorV1betaAccessTuple
    diff: GoogleCloudPolicysimulatorV1betaReplayDiff
    error: GoogleRpcStatus
    lastSeenDate: GoogleTypeDate
    name: str
    parent: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaReplayResultsSummary(
    typing.TypedDict, total=False
):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1betaResourceContext(typing.TypedDict, total=False):
    ancestors: _list[str]
    assetType: str
    resource: str

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
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
