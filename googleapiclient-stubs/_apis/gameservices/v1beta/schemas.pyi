import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    ignoreChildExemptions: bool
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: typing_extensions.Literal[
        "PERMISSION_TYPE_UNSPECIFIED",
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudAuditOptions(typing_extensions.TypedDict, total=False):
    authorizationLoggingOptions: AuthorizationLoggingOptions
    logName: typing_extensions.Literal[
        "UNSPECIFIED_LOG_NAME", "ADMIN_ACTIVITY", "DATA_ACCESS"
    ]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    iam: typing_extensions.Literal[
        "NO_ATTR",
        "AUTHORITY",
        "ATTRIBUTION",
        "SECURITY_REALM",
        "APPROVER",
        "JUSTIFICATION_TYPE",
        "CREDENTIALS_TYPE",
        "CREDS_ASSERTION",
    ]
    op: typing_extensions.Literal[
        "NO_OP", "EQUALS", "NOT_EQUALS", "IN", "NOT_IN", "DISCHARGED"
    ]
    svc: str
    sys: typing_extensions.Literal["NO_ATTR", "REGION", "SERVICE", "NAME", "IP"]
    values: _list[str]

@typing.type_check_only
class CounterOptions(typing_extensions.TypedDict, total=False):
    customFields: _list[CustomField]
    field: str
    metric: str

@typing.type_check_only
class CustomField(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class DataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: typing_extensions.Literal["LOG_MODE_UNSPECIFIED", "LOG_FAIL_CLOSED"]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogConfig(typing_extensions.TypedDict, total=False):
    cloudAudit: CloudAuditOptions
    counter: CounterOptions
    dataAccess: DataAccessOptions

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    rules: _list[Rule]
    version: int

AlternativeRule = typing_extensions.TypedDict(
    "AlternativeRule",
    {
        "action": typing_extensions.Literal[
            "NO_ACTION", "ALLOW", "ALLOW_WITH_LOG", "DENY", "DENY_WITH_LOG", "LOG"
        ],
        "conditions": _list[Condition],
        "description": str,
        "in": _list[str],
        "logConfig": _list[LogConfig],
        "notIn": _list[str],
        "permissions": _list[str],
    },
    total=False,
)

@typing.type_check_only
class Rule(AlternativeRule): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
