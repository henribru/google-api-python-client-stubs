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
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CloudSqlCredential(typing_extensions.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class CloudSqlProperties(typing_extensions.TypedDict, total=False):
    credential: CloudSqlCredential
    database: str
    instanceId: str
    serviceAccountId: str
    type: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    cloudSql: CloudSqlProperties
    creationTime: str
    description: str
    friendlyName: str
    hasCredential: bool
    lastModifiedTime: str
    name: str

@typing.type_check_only
class ConnectionCredential(typing_extensions.TypedDict, total=False):
    cloudSql: CloudSqlCredential

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
