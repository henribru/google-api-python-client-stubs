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
class Backup(typing_extensions.TypedDict, total=False):
    allNamespaces: bool
    clusterMetadata: ClusterMetadata
    completeTime: str
    configBackupSizeBytes: str
    containsSecrets: bool
    containsVolumeData: bool
    createTime: str
    deleteLockDays: int
    deleteLockExpireTime: str
    description: str
    encryptionKey: EncryptionKey
    etag: str
    labels: dict[str, typing.Any]
    manual: bool
    name: str
    podCount: int
    resourceCount: int
    retainDays: int
    retainExpireTime: str
    selectedApplications: NamespacedNames
    selectedNamespaces: Namespaces
    sizeBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "DELETING",
    ]
    stateReason: str
    uid: str
    updateTime: str
    volumeCount: int

@typing.type_check_only
class BackupConfig(typing_extensions.TypedDict, total=False):
    allNamespaces: bool
    encryptionKey: EncryptionKey
    includeSecrets: bool
    includeVolumeData: bool
    selectedApplications: NamespacedNames
    selectedNamespaces: Namespaces

@typing.type_check_only
class BackupPlan(typing_extensions.TypedDict, total=False):
    backupConfig: BackupConfig
    backupSchedule: Schedule
    cluster: str
    createTime: str
    deactivated: bool
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    protectedPodCount: int
    retentionPolicy: RetentionPolicy
    uid: str
    updateTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ClusterMetadata(typing_extensions.TypedDict, total=False):
    anthosVersion: str
    backupCrdVersions: dict[str, typing.Any]
    cluster: str
    gkeVersion: str
    k8sVersion: str

@typing.type_check_only
class ClusterResourceRestoreScope(typing_extensions.TypedDict, total=False):
    selectedGroupKinds: _list[GroupKind]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionKey(typing_extensions.TypedDict, total=False):
    gcpKmsEncryptionKey: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GroupKind(typing_extensions.TypedDict, total=False):
    resourceGroup: str
    resourceKind: str

@typing.type_check_only
class ListBackupPlansResponse(typing_extensions.TypedDict, total=False):
    backupPlans: _list[BackupPlan]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListRestorePlansResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    restorePlans: _list[RestorePlan]
    unreachable: _list[str]

@typing.type_check_only
class ListRestoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    restores: _list[Restore]
    unreachable: _list[str]

@typing.type_check_only
class ListVolumeBackupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    volumeBackups: _list[VolumeBackup]

@typing.type_check_only
class ListVolumeRestoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    volumeRestores: _list[VolumeRestore]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NamespacedName(typing_extensions.TypedDict, total=False):
    name: str
    namespace: str

@typing.type_check_only
class NamespacedNames(typing_extensions.TypedDict, total=False):
    namespacedNames: _list[NamespacedName]

@typing.type_check_only
class Namespaces(typing_extensions.TypedDict, total=False):
    namespaces: _list[str]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Restore(typing_extensions.TypedDict, total=False):
    backup: str
    cluster: str
    completeTime: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    resourcesExcludedCount: int
    resourcesFailedCount: int
    resourcesRestoredCount: int
    restoreConfig: RestoreConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "DELETING",
    ]
    stateReason: str
    uid: str
    updateTime: str
    volumesRestoredCount: int

@typing.type_check_only
class RestoreConfig(typing_extensions.TypedDict, total=False):
    allNamespaces: bool
    clusterResourceConflictPolicy: typing_extensions.Literal[
        "CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED",
        "USE_EXISTING_VERSION",
        "USE_BACKUP_VERSION",
    ]
    clusterResourceRestoreScope: ClusterResourceRestoreScope
    namespacedResourceRestoreMode: typing_extensions.Literal[
        "NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED",
        "DELETE_AND_RESTORE",
        "FAIL_ON_CONFLICT",
    ]
    selectedApplications: NamespacedNames
    selectedNamespaces: Namespaces
    substitutionRules: _list[SubstitutionRule]
    volumeDataRestorePolicy: typing_extensions.Literal[
        "VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED",
        "RESTORE_VOLUME_DATA_FROM_BACKUP",
        "REUSE_VOLUME_HANDLE_FROM_BACKUP",
        "NO_VOLUME_DATA_RESTORATION",
    ]

@typing.type_check_only
class RestorePlan(typing_extensions.TypedDict, total=False):
    backupPlan: str
    cluster: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    restoreConfig: RestoreConfig
    uid: str
    updateTime: str

@typing.type_check_only
class RetentionPolicy(typing_extensions.TypedDict, total=False):
    backupDeleteLockDays: int
    backupRetainDays: int
    locked: bool

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    cronSchedule: str
    paused: bool

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SubstitutionRule(typing_extensions.TypedDict, total=False):
    newValue: str
    originalValuePattern: str
    targetGroupKinds: _list[GroupKind]
    targetJsonPath: str
    targetNamespaces: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class VolumeBackup(typing_extensions.TypedDict, total=False):
    completeTime: str
    createTime: str
    diskSizeBytes: str
    etag: str
    format: typing_extensions.Literal[
        "VOLUME_BACKUP_FORMAT_UNSPECIFIED", "GCE_PERSISTENT_DISK"
    ]
    name: str
    sourcePvc: NamespacedName
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "SNAPSHOTTING",
        "UPLOADING",
        "SUCCEEDED",
        "FAILED",
        "DELETING",
    ]
    stateMessage: str
    storageBytes: str
    uid: str
    updateTime: str
    volumeBackupHandle: str

@typing.type_check_only
class VolumeRestore(typing_extensions.TypedDict, total=False):
    completeTime: str
    createTime: str
    etag: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RESTORING", "SUCCEEDED", "FAILED", "DELETING"
    ]
    stateMessage: str
    targetPvc: NamespacedName
    uid: str
    updateTime: str
    volumeBackup: str
    volumeHandle: str
    volumeType: typing_extensions.Literal[
        "VOLUME_TYPE_UNSPECIFIED", "GCE_PERSISTENT_DISK"
    ]
