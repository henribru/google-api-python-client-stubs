import typing

import typing_extensions

class ListSecretsResponse(typing_extensions.TypedDict, total=False):
    secrets: typing.List[Secret]
    nextPageToken: str
    totalSize: int

class SecretVersion(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "DESTROYED"
    ]
    destroyTime: str
    createTime: str

class Automatic(typing_extensions.TypedDict, total=False): ...

class ListSecretVersionsResponse(typing_extensions.TypedDict, total=False):
    versions: typing.List[SecretVersion]
    totalSize: int
    nextPageToken: str

class Empty(typing_extensions.TypedDict, total=False): ...
class DestroySecretVersionRequest(typing_extensions.TypedDict, total=False): ...

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    title: str
    expression: str

class AccessSecretVersionResponse(typing_extensions.TypedDict, total=False):
    name: str
    payload: SecretPayload

class Replication(typing_extensions.TypedDict, total=False):
    automatic: Automatic
    userManaged: UserManaged

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class UserManaged(typing_extensions.TypedDict, total=False):
    replicas: typing.List[Replica]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    displayName: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Secret(typing_extensions.TypedDict, total=False):
    createTime: str
    labels: typing.Dict[str, typing.Any]
    replication: Replication
    name: str

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    etag: str
    bindings: typing.List[Binding]
    version: int

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class AddSecretVersionRequest(typing_extensions.TypedDict, total=False):
    payload: SecretPayload

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class Replica(typing_extensions.TypedDict, total=False):
    location: str

class SecretPayload(typing_extensions.TypedDict, total=False):
    data: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DisableSecretVersionRequest(typing_extensions.TypedDict, total=False): ...
class EnableSecretVersionRequest(typing_extensions.TypedDict, total=False): ...

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    members: typing.List[str]
    role: str
