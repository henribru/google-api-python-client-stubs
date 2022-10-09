import typing

import typing_extensions

_list = list

@typing.type_check_only
class AppProfile(typing_extensions.TypedDict, total=False):
    description: str
    etag: str
    multiClusterRoutingUseAny: MultiClusterRoutingUseAny
    name: str
    singleClusterRouting: SingleClusterRouting

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
class AutoscalingLimits(typing_extensions.TypedDict, total=False):
    maxServeNodes: int
    minServeNodes: int

@typing.type_check_only
class AutoscalingTargets(typing_extensions.TypedDict, total=False):
    cpuUtilizationPercent: int
    storageUtilizationGibPerNode: int

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    encryptionInfo: EncryptionInfo
    endTime: str
    expireTime: str
    name: str
    sizeBytes: str
    sourceTable: str
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]

@typing.type_check_only
class BackupInfo(typing_extensions.TypedDict, total=False):
    backup: str
    endTime: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CheckConsistencyRequest(typing_extensions.TypedDict, total=False):
    consistencyToken: str

@typing.type_check_only
class CheckConsistencyResponse(typing_extensions.TypedDict, total=False):
    consistent: bool

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    clusterConfig: ClusterConfig
    defaultStorageType: typing_extensions.Literal[
        "STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"
    ]
    encryptionConfig: EncryptionConfig
    location: str
    name: str
    serveNodes: int
    state: typing_extensions.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]

@typing.type_check_only
class ClusterAutoscalingConfig(typing_extensions.TypedDict, total=False):
    autoscalingLimits: AutoscalingLimits
    autoscalingTargets: AutoscalingTargets

@typing.type_check_only
class ClusterConfig(typing_extensions.TypedDict, total=False):
    clusterAutoscalingConfig: ClusterAutoscalingConfig

@typing.type_check_only
class ClusterState(typing_extensions.TypedDict, total=False):
    encryptionInfo: _list[EncryptionInfo]
    replicationState: typing_extensions.Literal[
        "STATE_NOT_KNOWN",
        "INITIALIZING",
        "PLANNED_MAINTENANCE",
        "UNPLANNED_MAINTENANCE",
        "READY",
        "READY_OPTIMIZING",
    ]

@typing.type_check_only
class ColumnFamily(typing_extensions.TypedDict, total=False):
    gcRule: GcRule

@typing.type_check_only
class CreateBackupMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    name: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class CreateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateClusterRequest
    requestTime: str
    tables: dict[str, typing.Any]

@typing.type_check_only
class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: Cluster
    clusterId: str
    parent: str

@typing.type_check_only
class CreateInstanceMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateInstanceRequest
    requestTime: str

@typing.type_check_only
class CreateInstanceRequest(typing_extensions.TypedDict, total=False):
    clusters: dict[str, typing.Any]
    instance: Instance
    instanceId: str
    parent: str

@typing.type_check_only
class CreateTableRequest(typing_extensions.TypedDict, total=False):
    initialSplits: _list[Split]
    table: Table
    tableId: str

@typing.type_check_only
class DropRowRangeRequest(typing_extensions.TypedDict, total=False):
    deleteAllDataFromTable: bool
    rowKeyPrefix: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EncryptionInfo(typing_extensions.TypedDict, total=False):
    encryptionStatus: Status
    encryptionType: typing_extensions.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyVersion: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcRule(dict[str, typing.Any]): ...

@typing.type_check_only
class GenerateConsistencyTokenRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GenerateConsistencyTokenResponse(typing_extensions.TypedDict, total=False):
    consistencyToken: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class HotTablet(typing_extensions.TypedDict, total=False):
    endKey: str
    endTime: str
    name: str
    nodeCpuUsagePercent: float
    startKey: str
    startTime: str
    tableName: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzs: bool
    state: typing_extensions.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]

@typing.type_check_only
class Intersection(dict[str, typing.Any]): ...

@typing.type_check_only
class ListAppProfilesResponse(typing_extensions.TypedDict, total=False):
    appProfiles: _list[AppProfile]
    failedLocations: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    failedLocations: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListHotTabletsResponse(typing_extensions.TypedDict, total=False):
    hotTablets: _list[HotTablet]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    failedLocations: _list[str]
    instances: _list[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListTablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tables: _list[Table]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Modification(typing_extensions.TypedDict, total=False):
    create: ColumnFamily
    drop: bool
    id: str
    update: ColumnFamily

@typing.type_check_only
class ModifyColumnFamiliesRequest(typing_extensions.TypedDict, total=False):
    modifications: _list[Modification]

@typing.type_check_only
class MultiClusterRoutingUseAny(typing_extensions.TypedDict, total=False):
    clusterIds: _list[str]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationProgress(typing_extensions.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

@typing.type_check_only
class OptimizeRestoredTableMetadata(typing_extensions.TypedDict, total=False):
    name: str
    progress: OperationProgress

@typing.type_check_only
class PartialUpdateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateClusterRequest
    requestTime: str

@typing.type_check_only
class PartialUpdateClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: Cluster
    updateMask: str

@typing.type_check_only
class PartialUpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    updateMask: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RestoreInfo(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    sourceType: typing_extensions.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class RestoreTableMetadata(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    name: str
    optimizeTableOperationName: str
    progress: OperationProgress
    sourceType: typing_extensions.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class RestoreTableRequest(typing_extensions.TypedDict, total=False):
    backup: str
    tableId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SingleClusterRouting(typing_extensions.TypedDict, total=False):
    allowTransactionalWrites: bool
    clusterId: str

@typing.type_check_only
class Split(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    clusterStates: dict[str, typing.Any]
    columnFamilies: dict[str, typing.Any]
    granularity: typing_extensions.Literal[
        "TIMESTAMP_GRANULARITY_UNSPECIFIED", "MILLIS"
    ]
    name: str
    restoreInfo: RestoreInfo

@typing.type_check_only
class TableProgress(typing_extensions.TypedDict, total=False):
    estimatedCopiedBytes: str
    estimatedSizeBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COPYING", "COMPLETED", "CANCELLED"
    ]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeleteTableMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    name: str
    startTime: str

@typing.type_check_only
class UndeleteTableRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Union(dict[str, typing.Any]): ...

@typing.type_check_only
class UpdateAppProfileMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: Cluster
    requestTime: str

@typing.type_check_only
class UpdateInstanceMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateInstanceRequest
    requestTime: str
