import typing

import typing_extensions

class ListSecretsResponse(typing_extensions.TypedDict, total=False):
    secrets: typing.List[Secret]
    totalSize: int
    nextPageToken: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DestroySecretVersionRequest(typing_extensions.TypedDict, total=False): ...

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AddSecretVersionRequest(typing_extensions.TypedDict, total=False):
    payload: SecretPayload

class Location(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    displayName: str
    locationId: str
    labels: typing.Dict[str, typing.Any]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]
    bindingId: str
    condition: Expr

class AccessSecretVersionResponse(typing_extensions.TypedDict, total=False):
    payload: SecretPayload
    name: str

class DisableSecretVersionRequest(typing_extensions.TypedDict, total=False): ...

class SecretPayload(typing_extensions.TypedDict, total=False):
    data: str

class EnableSecretVersionRequest(typing_extensions.TypedDict, total=False): ...

class ReplicationStatus(typing_extensions.TypedDict, total=False):
    automatic: AutomaticStatus
    userManaged: UserManagedStatus

class UserManagedStatus(typing_extensions.TypedDict, total=False):
    replicas: typing.List[ReplicaStatus]

class Automatic(typing_extensions.TypedDict, total=False):
    customerManagedEncryption: CustomerManagedEncryption

class Replication(typing_extensions.TypedDict, total=False):
    userManaged: UserManaged
    automatic: Automatic

class Replica(typing_extensions.TypedDict, total=False):
    location: str
    customerManagedEncryption: CustomerManagedEncryption

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class CustomerManagedEncryptionStatus(typing_extensions.TypedDict, total=False):
    kmsKeyVersionName: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    version: int
    etag: str
    auditConfigs: typing.List[AuditConfig]

class UserManaged(typing_extensions.TypedDict, total=False):
    replicas: typing.List[Replica]

class AutomaticStatus(typing_extensions.TypedDict, total=False):
    customerManagedEncryption: CustomerManagedEncryptionStatus

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class ReplicaStatus(typing_extensions.TypedDict, total=False):
    location: str
    customerManagedEncryption: CustomerManagedEncryptionStatus

class ListSecretVersionsResponse(typing_extensions.TypedDict, total=False):
    totalSize: int
    versions: typing.List[SecretVersion]
    nextPageToken: str

class CustomerManagedEncryption(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    expression: str
    title: str

class Empty(typing_extensions.TypedDict, total=False): ...

class SecretVersion(typing_extensions.TypedDict, total=False):
    replicationStatus: ReplicationStatus
    createTime: str
    destroyTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "DESTROYED"
    ]
    name: str

class Secret(typing_extensions.TypedDict, total=False):
    createTime: str
    replication: Replication
    name: str
    labels: typing.Dict[str, typing.Any]
