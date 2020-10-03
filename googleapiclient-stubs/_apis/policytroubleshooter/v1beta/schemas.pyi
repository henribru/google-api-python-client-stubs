import typing

import typing_extensions

class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[GoogleIamV1AuditConfig]
    etag: str
    bindings: typing.List[GoogleIamV1Binding]
    version: int

class GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterV1betaAccessTuple

class GoogleCloudPolicytroubleshooterV1betaBindingExplanationAnnotatedMembership(
    typing_extensions.TypedDict, total=False
):
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    membership: typing_extensions.Literal[
        "MEMBERSHIP_UNSPECIFIED",
        "MEMBERSHIP_INCLUDED",
        "MEMBERSHIP_NOT_INCLUDED",
        "MEMBERSHIP_UNKNOWN_INFO_DENIED",
        "MEMBERSHIP_UNKNOWN_UNSUPPORTED",
    ]

class GoogleCloudPolicytroubleshooterV1betaBindingExplanation(
    typing_extensions.TypedDict, total=False
):
    role: str
    memberships: typing.Dict[str, typing.Any]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    rolePermissionRelevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    condition: GoogleTypeExpr
    rolePermission: typing_extensions.Literal[
        "ROLE_PERMISSION_UNSPECIFIED",
        "ROLE_PERMISSION_INCLUDED",
        "ROLE_PERMISSION_NOT_INCLUDED",
        "ROLE_PERMISSION_UNKNOWN_INFO_DENIED",
    ]
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]

class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    title: str
    location: str
    description: str
    expression: str

class GoogleCloudPolicytroubleshooterV1betaAccessTuple(
    typing_extensions.TypedDict, total=False
):
    fullResourceName: str
    permission: str
    principal: str

class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: GoogleTypeExpr
    role: str

class GoogleCloudPolicytroubleshooterV1betaExplainedPolicy(
    typing_extensions.TypedDict, total=False
):
    fullResourceName: str
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    policy: GoogleIamV1Policy
    bindingExplanations: typing.List[
        GoogleCloudPolicytroubleshooterV1betaBindingExplanation
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]

class GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponse(
    typing_extensions.TypedDict, total=False
):
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    explainedPolicies: typing.List[GoogleCloudPolicytroubleshooterV1betaExplainedPolicy]

class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[GoogleIamV1AuditLogConfig]
    service: str

class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
