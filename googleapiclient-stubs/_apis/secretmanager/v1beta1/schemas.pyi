import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessSecretVersionResponse(typing_extensions.TypedDict, total=False):
    name: str
    payload: SecretPayload

@typing.type_check_only
class AddSecretVersionRequest(typing_extensions.TypedDict, total=False):
    payload: SecretPayload

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
class Automatic(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class DestroySecretVersionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DisableSecretVersionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableSecretVersionRequest(typing_extensions.TypedDict, total=False): ...

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
class ListSecretVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    versions: _list[SecretVersion]

@typing.type_check_only
class ListSecretsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    secrets: _list[Secret]
    totalSize: int

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Replica(typing_extensions.TypedDict, total=False):
    location: str

@typing.type_check_only
class Replication(typing_extensions.TypedDict, total=False):
    automatic: Automatic
    userManaged: UserManaged

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    replication: Replication

@typing.type_check_only
class SecretPayload(typing_extensions.TypedDict, total=False):
    data: str

@typing.type_check_only
class SecretVersion(typing_extensions.TypedDict, total=False):
    createTime: str
    destroyTime: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "DESTROYED"
    ]

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

@typing.type_check_only
class UserManaged(typing_extensions.TypedDict, total=False):
    replicas: _list[Replica]
