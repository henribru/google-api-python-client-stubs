import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudPolicytroubleshooterV1betaAccessTuple(
    typing_extensions.TypedDict, total=False
):
    fullResourceName: str
    permission: str
    principal: str

@typing.type_check_only
class GoogleCloudPolicytroubleshooterV1betaBindingExplanation(
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
class GoogleCloudPolicytroubleshooterV1betaBindingExplanationAnnotatedMembership(
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
class GoogleCloudPolicytroubleshooterV1betaExplainedPolicy(
    typing_extensions.TypedDict, total=False
):
    access: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED",
        "GRANTED",
        "NOT_GRANTED",
        "UNKNOWN_CONDITIONAL",
        "UNKNOWN_INFO_DENIED",
    ]
    bindingExplanations: _list[GoogleCloudPolicytroubleshooterV1betaBindingExplanation]
    fullResourceName: str
    policy: GoogleIamV1Policy
    relevance: typing_extensions.Literal[
        "HEURISTIC_RELEVANCE_UNSPECIFIED", "NORMAL", "HIGH"
    ]

@typing.type_check_only
class GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    accessTuple: GoogleCloudPolicytroubleshooterV1betaAccessTuple

@typing.type_check_only
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
    explainedPolicies: _list[GoogleCloudPolicytroubleshooterV1betaExplainedPolicy]

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
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
