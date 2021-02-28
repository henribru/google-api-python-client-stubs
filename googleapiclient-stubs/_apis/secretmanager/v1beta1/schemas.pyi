import typing

import typing_extensions
@typing.type_check_only
class AccessSecretVersionResponse(typing_extensions.TypedDict, total=False):
    name: str
    payload: SecretPayload

@typing.type_check_only
class AddSecretVersionRequest(typing_extensions.TypedDict, total=False):
    payload: SecretPayload

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Automatic(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
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
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListSecretVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    versions: typing.List[SecretVersion]

@typing.type_check_only
class ListSecretsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    secrets: typing.List[Secret]
    totalSize: int

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
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
    labels: typing.Dict[str, typing.Any]
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
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class UserManaged(typing_extensions.TypedDict, total=False):
    replicas: typing.List[Replica]
