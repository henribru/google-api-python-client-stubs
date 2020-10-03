import typing

import typing_extensions

class GoogleCloudPolicytroubleshooterV1BindingExplanation(
    typing_extensions.TypedDict, total=False
):
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
    role: str
    rolePermissionRelevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    condition: GoogleTypeExpr
    memberships: typing.Dict[str, typing.Any]

class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[GoogleIamV1AuditLogConfig]
    service: str

class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    title: str
    expression: str

class GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterV1AccessTuple

class GoogleCloudPolicytroubleshooterV1AccessTuple(
    typing_extensions.TypedDict, total=False
):
    permission: str
    fullResourceName: str
    principal: str

class GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponse(
    typing_extensions.TypedDict, total=False
):
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    explainedPolicies: typing.List[GoogleCloudPolicytroubleshooterV1ExplainedPolicy]

class GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembership(
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

class GoogleCloudPolicytroubleshooterV1ExplainedPolicy(
    typing_extensions.TypedDict, total=False
):
    policy: GoogleIamV1Policy
    bindingExplanations: typing.List[
        GoogleCloudPolicytroubleshooterV1BindingExplanation
    ]
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]
    fullResourceName: str

class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[GoogleIamV1Binding]
    etag: str
    auditConfigs: typing.List[GoogleIamV1AuditConfig]

class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    role: str
    members: typing.List[str]

class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
