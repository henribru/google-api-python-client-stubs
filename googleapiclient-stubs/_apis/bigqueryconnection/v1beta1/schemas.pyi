import typing

import typing_extensions

class CloudSqlCredential(typing_extensions.TypedDict, total=False):
    username: str
    password: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class CloudSqlProperties(typing_extensions.TypedDict, total=False):
    database: str
    instanceId: str
    type: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]
    credential: CloudSqlCredential

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class ConnectionCredential(typing_extensions.TypedDict, total=False):
    cloudSql: CloudSqlCredential

class Connection(typing_extensions.TypedDict, total=False):
    lastModifiedTime: str
    hasCredential: bool
    cloudSql: CloudSqlProperties
    friendlyName: str
    name: str
    creationTime: str
    description: str

class Empty(typing_extensions.TypedDict, total=False): ...

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    connections: typing.List[Connection]
