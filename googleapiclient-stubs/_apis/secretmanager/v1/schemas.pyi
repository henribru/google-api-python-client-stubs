import typing

_list = list

@typing.type_check_only
class AccessSecretVersionResponse(typing.TypedDict, total=False):
    name: str
    payload: SecretPayload

@typing.type_check_only
class AddSecretVersionRequest(typing.TypedDict, total=False):
    payload: SecretPayload

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Automatic(typing.TypedDict, total=False):
    customerManagedEncryption: CustomerManagedEncryption

@typing.type_check_only
class AutomaticStatus(typing.TypedDict, total=False):
    customerManagedEncryption: CustomerManagedEncryptionStatus

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CloudSQLSingleUserCredentials(typing.TypedDict, total=False):
    instanceId: str
    password: str
    username: str

@typing.type_check_only
class CustomerManagedEncryption(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class CustomerManagedEncryptionStatus(typing.TypedDict, total=False):
    kmsKeyVersionName: str

@typing.type_check_only
class DestroySecretVersionRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class DisableSecretVersionRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableManagedRotationRequest(typing.TypedDict, total=False):
    cloudSqlSingleUserCredentials: CloudSQLSingleUserCredentials

@typing.type_check_only
class EnableSecretVersionRequest(typing.TypedDict, total=False):
    etag: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListSecretVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    versions: _list[SecretVersion]

@typing.type_check_only
class ListSecretsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    secrets: _list[Secret]
    totalSize: int

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagedRotationStatus(typing.TypedDict, total=False):
    error: Status
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    progress: Progress
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Progress(typing.TypedDict, total=False):
    completedVersionCount: int
    failedVersionCount: int
    totalVersionCount: int

@typing.type_check_only
class Replica(typing.TypedDict, total=False):
    customerManagedEncryption: CustomerManagedEncryption
    location: str

@typing.type_check_only
class ReplicaStatus(typing.TypedDict, total=False):
    customerManagedEncryption: CustomerManagedEncryptionStatus
    location: str

@typing.type_check_only
class Replication(typing.TypedDict, total=False):
    automatic: Automatic
    userManaged: UserManaged

@typing.type_check_only
class ReplicationStatus(typing.TypedDict, total=False):
    automatic: AutomaticStatus
    userManaged: UserManagedStatus

@typing.type_check_only
class ResourcePolicyMember(typing.TypedDict, total=False):
    iamPolicyNamePrincipal: str
    iamPolicyUidPrincipal: str

@typing.type_check_only
class RotateSecretRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Rotation(typing.TypedDict, total=False):
    managedRotationStatus: ManagedRotationStatus
    nextRotationTime: str
    rotationPeriod: str

@typing.type_check_only
class Secret(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    customerManagedEncryption: CustomerManagedEncryption
    etag: str
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    policyMember: ResourcePolicyMember
    replication: Replication
    rotation: Rotation
    secretType: typing.Literal[
        "SECRET_TYPE_UNSPECIFIED",
        "CLOUD_SQL_DB_CREDENTIALS",
        "ACCESS_KEY",
        "CERTIFICATE",
        "OTHER_DB_CREDENTIALS",
        "OTHER",
    ]
    tags: dict[str, typing.Any]
    topics: _list[Topic]
    ttl: str
    versionAliases: dict[str, typing.Any]
    versionDestroyTtl: str

@typing.type_check_only
class SecretPayload(typing.TypedDict, total=False):
    data: str
    dataCrc32c: str

@typing.type_check_only
class SecretVersion(typing.TypedDict, total=False):
    clientSpecifiedPayloadChecksum: bool
    createTime: str
    customerManagedEncryption: CustomerManagedEncryptionStatus
    destroyTime: str
    etag: str
    name: str
    replicationStatus: ReplicationStatus
    scheduledDestroyTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED", "DESTROYED"]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class UserManaged(typing.TypedDict, total=False):
    replicas: _list[Replica]

@typing.type_check_only
class UserManagedStatus(typing.TypedDict, total=False):
    replicas: _list[ReplicaStatus]
