import typing

_list = list

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
class BDRBackupPlanJobLog(typing.TypedDict, total=False):
    backupPlanName: str
    endTime: str
    errorCode: int
    errorMessage: str
    errorType: str
    jobCategory: str
    jobId: str
    jobStatus: str
    newBackupPlanRevisionId: str
    newBackupPlanRevisionName: str
    previousBackupPlanRevisionId: str
    previousBackupPlanRevisionName: str
    previousBackupRules: _list[BackupRuleDetail]
    resourceType: str
    revisedBackupRules: _list[BackupRuleDetail]
    startTime: str
    workloadsAffectedCount: int

@typing.type_check_only
class BDRBackupRestoreJobLog(typing.TypedDict, total=False):
    backupConsistencyTime: str
    backupName: str
    backupPlanName: str
    backupRetentionDays: int
    backupRule: str
    backupVaultName: str
    dataSourceName: str
    endTime: str
    errorCode: int
    errorMessage: str
    errorType: str
    incrementalBackupSizeGib: float
    jobCategory: str
    jobId: str
    jobStatus: str
    recoveryPointTime: str
    resourceType: str
    restoreResourceLocation: str
    restoreResourceName: str
    sourceResourceId: str
    sourceResourceLocation: str
    sourceResourceName: str
    startTime: str
    storageTier: str
    targetResourceType: str

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
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
    namespaceCount: int
    permissiveMode: bool
    podCount: int
    resourceCount: int
    retainDays: int
    retainExpireTime: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    selectedApplications: NamespacedNames
    selectedNamespaceLabels: ResourceLabels
    selectedNamespaces: Namespaces
    sizeBytes: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "DELETING",
    ]
    stateReason: str
    troubleshootingInfo: TroubleshootingInfo
    uid: str
    updateTime: str
    volumeCount: int

@typing.type_check_only
class BackupChannel(typing.TypedDict, total=False):
    createTime: str
    description: str
    destinationProject: str
    destinationProjectId: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class BackupConfig(typing.TypedDict, total=False):
    allNamespaces: bool
    encryptionKey: EncryptionKey
    includeSecrets: bool
    includeVolumeData: bool
    permissiveMode: bool
    selectedApplications: NamespacedNames
    selectedNamespaceLabels: ResourceLabels
    selectedNamespaces: Namespaces

@typing.type_check_only
class BackupConfigDetails(typing.TypedDict, total=False):
    allNamespaces: bool
    encryptionKey: EncryptionKey
    includeSecrets: bool
    includeVolumeData: bool
    selectedApplications: NamespacedNames
    selectedNamespaces: Namespaces

@typing.type_check_only
class BackupPlan(typing.TypedDict, total=False):
    backupChannel: str
    backupConfig: BackupConfig
    backupSchedule: Schedule
    cluster: str
    createTime: str
    deactivated: bool
    description: str
    etag: str
    labels: dict[str, typing.Any]
    lastSuccessfulBackupTime: str
    name: str
    protectedNamespaceCount: int
    protectedPodCount: int
    retentionPolicy: RetentionPolicy
    rpoRiskLevel: int
    rpoRiskReason: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CLUSTER_PENDING",
        "PROVISIONING",
        "READY",
        "FAILED",
        "DEACTIVATED",
        "DELETING",
    ]
    stateReason: str
    uid: str
    updateTime: str

@typing.type_check_only
class BackupPlanBinding(typing.TypedDict, total=False):
    backupPlan: str
    backupPlanDetails: BackupPlanDetails
    cluster: str
    createTime: str
    etag: str
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class BackupPlanDetails(typing.TypedDict, total=False):
    backupConfigDetails: BackupConfigDetails
    lastSuccessfulBackup: str
    lastSuccessfulBackupTime: str
    nextScheduledBackupTime: str
    protectedPodCount: int
    retentionPolicyDetails: RetentionPolicyDetails
    rpoRiskLevel: int
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CLUSTER_PENDING",
        "PROVISIONING",
        "READY",
        "FAILED",
        "DEACTIVATED",
        "DELETING",
    ]

@typing.type_check_only
class BackupRuleDetail(typing.TypedDict, total=False):
    backupWindow: str
    backupWindowTimezone: str
    recurrence: str
    recurrenceSchedule: str
    retentionDays: int
    ruleName: str
    storageTier: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ClusterMetadata(typing.TypedDict, total=False):
    anthosVersion: str
    backupCrdVersions: dict[str, typing.Any]
    cluster: str
    gkeVersion: str
    k8sVersion: str

@typing.type_check_only
class ClusterResourceRestoreScope(typing.TypedDict, total=False):
    allGroupKinds: bool
    excludedGroupKinds: _list[GroupKind]
    noGroupKinds: bool
    selectedGroupKinds: _list[GroupKind]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DayOfWeekList(typing.TypedDict, total=False):
    daysOfWeek: _list[
        typing.Literal[
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionKey(typing.TypedDict, total=False):
    gcpKmsEncryptionKey: str

@typing.type_check_only
class ExclusionWindow(typing.TypedDict, total=False):
    daily: bool
    daysOfWeek: DayOfWeekList
    duration: str
    singleOccurrenceDate: Date
    startTime: TimeOfDay

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    exclusionFilters: _list[ResourceSelector]
    inclusionFilters: _list[ResourceSelector]

@typing.type_check_only
class GetBackupIndexDownloadUrlResponse(typing.TypedDict, total=False):
    signedUrl: str

@typing.type_check_only
class GetTagsRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GetTagsResponse(typing.TypedDict, total=False):
    etag: str
    name: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GroupKind(typing.TypedDict, total=False):
    resourceGroup: str
    resourceKind: str

@typing.type_check_only
class GroupKindDependency(typing.TypedDict, total=False):
    requiring: GroupKind
    satisfying: GroupKind

@typing.type_check_only
class Label(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ListBackupChannelsResponse(typing.TypedDict, total=False):
    backupChannels: _list[BackupChannel]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupPlanBindingsResponse(typing.TypedDict, total=False):
    backupPlanBindings: _list[BackupPlanBinding]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupPlansResponse(typing.TypedDict, total=False):
    backupPlans: _list[BackupPlan]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListRestoreChannelsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    restoreChannels: _list[RestoreChannel]
    unreachable: _list[str]

@typing.type_check_only
class ListRestorePlanBindingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    restorePlanBindings: _list[RestorePlanBinding]
    unreachable: _list[str]

@typing.type_check_only
class ListRestorePlansResponse(typing.TypedDict, total=False):
    nextPageToken: str
    restorePlans: _list[RestorePlan]
    unreachable: _list[str]

@typing.type_check_only
class ListRestoresResponse(typing.TypedDict, total=False):
    nextPageToken: str
    restores: _list[Restore]
    unreachable: _list[str]

@typing.type_check_only
class ListVolumeBackupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    volumeBackups: _list[VolumeBackup]

@typing.type_check_only
class ListVolumeRestoresResponse(typing.TypedDict, total=False):
    nextPageToken: str
    volumeRestores: _list[VolumeRestore]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NamespacedName(typing.TypedDict, total=False):
    name: str
    namespace: str

@typing.type_check_only
class NamespacedNames(typing.TypedDict, total=False):
    namespacedNames: _list[NamespacedName]

@typing.type_check_only
class Namespaces(typing.TypedDict, total=False):
    namespaces: _list[str]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
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
class ResourceFilter(typing.TypedDict, total=False):
    groupKinds: _list[GroupKind]
    jsonPath: str
    namespaces: _list[str]

@typing.type_check_only
class ResourceLabels(typing.TypedDict, total=False):
    resourceLabels: _list[Label]

@typing.type_check_only
class ResourceSelector(typing.TypedDict, total=False):
    groupKind: GroupKind
    labels: dict[str, typing.Any]
    name: str
    namespace: str

@typing.type_check_only
class Restore(typing.TypedDict, total=False):
    backup: str
    cluster: str
    completeTime: str
    createTime: str
    description: str
    etag: str
    filter: Filter
    labels: dict[str, typing.Any]
    name: str
    resourcesExcludedCount: int
    resourcesFailedCount: int
    resourcesRestoredCount: int
    restoreConfig: RestoreConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "DELETING",
        "VALIDATING",
    ]
    stateReason: str
    troubleshootingInfo: TroubleshootingInfo
    uid: str
    updateTime: str
    volumeDataRestorePolicyOverrides: _list[VolumeDataRestorePolicyOverride]
    volumesRestoredCount: int

@typing.type_check_only
class RestoreChannel(typing.TypedDict, total=False):
    createTime: str
    description: str
    destinationProject: str
    destinationProjectId: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class RestoreConfig(typing.TypedDict, total=False):
    allNamespaces: bool
    clusterResourceConflictPolicy: typing.Literal[
        "CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED",
        "USE_EXISTING_VERSION",
        "USE_BACKUP_VERSION",
    ]
    clusterResourceRestoreScope: ClusterResourceRestoreScope
    excludedNamespaces: Namespaces
    namespacedResourceRestoreMode: typing.Literal[
        "NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED",
        "DELETE_AND_RESTORE",
        "FAIL_ON_CONFLICT",
        "MERGE_SKIP_ON_CONFLICT",
        "MERGE_REPLACE_VOLUME_ON_CONFLICT",
        "MERGE_REPLACE_ON_CONFLICT",
    ]
    noNamespaces: bool
    restoreOrder: RestoreOrder
    selectedApplications: NamespacedNames
    selectedNamespaces: Namespaces
    substitutionRules: _list[SubstitutionRule]
    transformationRules: _list[TransformationRule]
    volumeDataRestorePolicy: typing.Literal[
        "VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED",
        "RESTORE_VOLUME_DATA_FROM_BACKUP",
        "REUSE_VOLUME_HANDLE_FROM_BACKUP",
        "NO_VOLUME_DATA_RESTORATION",
    ]
    volumeDataRestorePolicyBindings: _list[VolumeDataRestorePolicyBinding]

@typing.type_check_only
class RestoreOrder(typing.TypedDict, total=False):
    groupKindDependencies: _list[GroupKindDependency]

@typing.type_check_only
class RestorePlan(typing.TypedDict, total=False):
    backupPlan: str
    cluster: str
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    restoreChannel: str
    restoreConfig: RestoreConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CLUSTER_PENDING", "READY", "FAILED", "DELETING"
    ]
    stateReason: str
    uid: str
    updateTime: str

@typing.type_check_only
class RestorePlanBinding(typing.TypedDict, total=False):
    backupPlan: str
    createTime: str
    etag: str
    name: str
    restorePlan: str
    uid: str
    updateTime: str

@typing.type_check_only
class RetentionPolicy(typing.TypedDict, total=False):
    backupDeleteLockDays: int
    backupRetainDays: int
    locked: bool

@typing.type_check_only
class RetentionPolicyDetails(typing.TypedDict, total=False):
    backupDeleteLockDays: int
    backupRetainDays: int

@typing.type_check_only
class RpoConfig(typing.TypedDict, total=False):
    exclusionWindows: _list[ExclusionWindow]
    targetRpoMinutes: int

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    cronSchedule: str
    nextScheduledBackupTime: str
    paused: bool
    rpoConfig: RpoConfig

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SetTagsRequest(typing.TypedDict, total=False):
    etag: str
    name: str
    requestId: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class SetTagsResponse(typing.TypedDict, total=False):
    etag: str
    name: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class SubstitutionRule(typing.TypedDict, total=False):
    newValue: str
    originalValuePattern: str
    targetGroupKinds: _list[GroupKind]
    targetJsonPath: str
    targetNamespaces: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TransformationRule(typing.TypedDict, total=False):
    description: str
    fieldActions: _list[TransformationRuleAction]
    resourceFilter: ResourceFilter

@typing.type_check_only
class TransformationRuleAction(typing.TypedDict, total=False):
    fromPath: str
    op: typing.Literal[
        "OP_UNSPECIFIED", "REMOVE", "MOVE", "COPY", "ADD", "TEST", "REPLACE"
    ]
    path: str
    value: str

@typing.type_check_only
class TroubleshootingInfo(typing.TypedDict, total=False):
    stateReasonCode: str
    stateReasonUri: str

@typing.type_check_only
class VolumeBackup(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    diskSizeBytes: str
    etag: str
    format: typing.Literal["VOLUME_BACKUP_FORMAT_UNSPECIFIED", "GCE_PERSISTENT_DISK"]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    sourcePvc: NamespacedName
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "SNAPSHOTTING",
        "UPLOADING",
        "SUCCEEDED",
        "FAILED",
        "DELETING",
        "CLEANED_UP",
    ]
    stateMessage: str
    storageBytes: str
    uid: str
    updateTime: str
    volumeBackupHandle: str

@typing.type_check_only
class VolumeDataRestorePolicyBinding(typing.TypedDict, total=False):
    policy: typing.Literal[
        "VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED",
        "RESTORE_VOLUME_DATA_FROM_BACKUP",
        "REUSE_VOLUME_HANDLE_FROM_BACKUP",
        "NO_VOLUME_DATA_RESTORATION",
    ]
    volumeType: typing.Literal["VOLUME_TYPE_UNSPECIFIED", "GCE_PERSISTENT_DISK"]

@typing.type_check_only
class VolumeDataRestorePolicyOverride(typing.TypedDict, total=False):
    policy: typing.Literal[
        "VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED",
        "RESTORE_VOLUME_DATA_FROM_BACKUP",
        "REUSE_VOLUME_HANDLE_FROM_BACKUP",
        "NO_VOLUME_DATA_RESTORATION",
    ]
    selectedPvcs: NamespacedNames

@typing.type_check_only
class VolumeRestore(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    etag: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "RESTORING", "SUCCEEDED", "FAILED", "DELETING"
    ]
    stateMessage: str
    targetPvc: NamespacedName
    uid: str
    updateTime: str
    volumeBackup: str
    volumeHandle: str
    volumeType: typing.Literal["VOLUME_TYPE_UNSPECIFIED", "GCE_PERSISTENT_DISK"]
