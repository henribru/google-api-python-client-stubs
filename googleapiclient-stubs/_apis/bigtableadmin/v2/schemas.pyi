import typing

import typing_extensions
@typing.type_check_only
class AppProfile(typing_extensions.TypedDict, total=False):
    description: str
    etag: str
    multiClusterRoutingUseAny: MultiClusterRoutingUseAny
    name: str
    singleClusterRouting: SingleClusterRouting

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
class Backup(typing_extensions.TypedDict, total=False):
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
    members: typing.List[str]
    role: str

@typing.type_check_only
class CheckConsistencyRequest(typing_extensions.TypedDict, total=False):
    consistencyToken: str

@typing.type_check_only
class CheckConsistencyResponse(typing_extensions.TypedDict, total=False):
    consistent: bool

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    defaultStorageType: typing_extensions.Literal[
        "STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"
    ]
    location: str
    name: str
    serveNodes: int
    state: typing_extensions.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]

@typing.type_check_only
class ClusterState(typing_extensions.TypedDict, total=False):
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
    tables: typing.Dict[str, typing.Any]

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
    clusters: typing.Dict[str, typing.Any]
    instance: Instance
    instanceId: str
    parent: str

@typing.type_check_only
class CreateTableRequest(typing_extensions.TypedDict, total=False):
    initialSplits: typing.List[Split]
    table: Table
    tableId: str

@typing.type_check_only
class DropRowRangeRequest(typing_extensions.TypedDict, total=False):
    deleteAllDataFromTable: bool
    rowKeyPrefix: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FailureTrace(typing_extensions.TypedDict, total=False):
    frames: typing.List[Frame]

@typing.type_check_only
class Frame(typing_extensions.TypedDict, total=False):
    targetName: str
    workflowGuid: str
    zoneId: str

@typing.type_check_only
class GcRule(typing.Dict[str, typing.Any]): ...

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
class Instance(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]

@typing.type_check_only
class Intersection(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ListAppProfilesResponse(typing_extensions.TypedDict, total=False):
    appProfiles: typing.List[AppProfile]
    failedLocations: typing.List[str]
    nextPageToken: str

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: typing.List[Backup]
    nextPageToken: str

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: typing.List[Cluster]
    failedLocations: typing.List[str]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    failedLocations: typing.List[str]
    instances: typing.List[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListTablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tables: typing.List[Table]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Modification(typing_extensions.TypedDict, total=False):
    create: ColumnFamily
    drop: bool
    id: str
    update: ColumnFamily

@typing.type_check_only
class ModifyColumnFamiliesRequest(typing_extensions.TypedDict, total=False):
    modifications: typing.List[Modification]

@typing.type_check_only
class MultiClusterRoutingUseAny(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
class PartialUpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    updateMask: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
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
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    clusterStates: typing.Dict[str, typing.Any]
    columnFamilies: typing.Dict[str, typing.Any]
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
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Union(typing.Dict[str, typing.Any]): ...

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
