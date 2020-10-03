import typing

import typing_extensions

class CheckConsistencyRequest(typing_extensions.TypedDict, total=False):
    consistencyToken: str

class RestoreTableRequest(typing_extensions.TypedDict, total=False):
    backup: str
    tableId: str

class Modification(typing_extensions.TypedDict, total=False):
    id: str
    create: ColumnFamily
    update: ColumnFamily
    drop: bool

class ModifyColumnFamiliesRequest(typing_extensions.TypedDict, total=False):
    modifications: typing.List[Modification]

class CreateBackupMetadata(typing_extensions.TypedDict, total=False):
    sourceTable: str
    endTime: str
    name: str
    startTime: str

class SingleClusterRouting(typing_extensions.TypedDict, total=False):
    clusterId: str
    allowTransactionalWrites: bool

class Location(typing_extensions.TypedDict, total=False):
    locationId: str
    displayName: str
    metadata: typing.Dict[str, typing.Any]
    name: str
    labels: typing.Dict[str, typing.Any]

class CheckConsistencyResponse(typing_extensions.TypedDict, total=False):
    consistent: bool

class Backup(typing_extensions.TypedDict, total=False):
    name: str
    startTime: str
    sourceTable: str
    expireTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    endTime: str
    sizeBytes: str

class UpdateClusterMetadata(typing_extensions.TypedDict, total=False):
    originalRequest: Cluster
    requestTime: str
    finishTime: str

class Intersection(typing_extensions.TypedDict, total=False):
    rules: typing.List[GcRule]

class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: typing.List[Backup]
    nextPageToken: str

class Union(typing_extensions.TypedDict, total=False):
    rules: typing.List[GcRule]

class OperationProgress(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    progressPercent: int

class RestoreTableMetadata(typing_extensions.TypedDict, total=False):
    sourceType: typing_extensions.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]
    optimizeTableOperationName: str
    progress: OperationProgress
    name: str
    backupInfo: BackupInfo

class UpdateAppProfileMetadata(typing_extensions.TypedDict, total=False): ...
class GcRule(typing.Dict[str, typing.Any]): ...
class MultiClusterRoutingUseAny(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class FailureTrace(typing_extensions.TypedDict, total=False):
    frames: typing.List[Frame]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class DropRowRangeRequest(typing_extensions.TypedDict, total=False):
    rowKeyPrefix: str
    deleteAllDataFromTable: bool

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status

class GenerateConsistencyTokenRequest(typing_extensions.TypedDict, total=False): ...

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Table(typing_extensions.TypedDict, total=False):
    clusterStates: typing.Dict[str, typing.Any]
    restoreInfo: RestoreInfo
    granularity: typing_extensions.Literal[
        "TIMESTAMP_GRANULARITY_UNSPECIFIED", "MILLIS"
    ]
    name: str
    columnFamilies: typing.Dict[str, typing.Any]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GenerateConsistencyTokenResponse(typing_extensions.TypedDict, total=False):
    consistencyToken: str

class UpdateInstanceMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateInstanceRequest
    requestTime: str

class ClusterState(typing_extensions.TypedDict, total=False):
    replicationState: typing_extensions.Literal[
        "STATE_NOT_KNOWN",
        "INITIALIZING",
        "PLANNED_MAINTENANCE",
        "UNPLANNED_MAINTENANCE",
        "READY",
        "READY_OPTIMIZING",
    ]

class CreateInstanceMetadata(typing_extensions.TypedDict, total=False):
    originalRequest: CreateInstanceRequest
    requestTime: str
    finishTime: str

class PartialUpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    updateMask: str

class BackupInfo(typing_extensions.TypedDict, total=False):
    endTime: str
    backup: str
    startTime: str
    sourceTable: str

class Split(typing_extensions.TypedDict, total=False):
    key: str

class CreateClusterMetadata(typing_extensions.TypedDict, total=False):
    finishTime: str
    requestTime: str
    tables: typing.Dict[str, typing.Any]
    originalRequest: CreateClusterRequest

class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: typing.List[Cluster]
    nextPageToken: str
    failedLocations: typing.List[str]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class RestoreInfo(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    sourceType: typing_extensions.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

class ListTablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tables: typing.List[Table]

class CreateInstanceRequest(typing_extensions.TypedDict, total=False):
    clusters: typing.Dict[str, typing.Any]
    parent: str
    instanceId: str
    instance: Instance

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class OptimizeRestoredTableMetadata(typing_extensions.TypedDict, total=False):
    progress: OperationProgress
    name: str

class Instance(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    displayName: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]
    name: str
    labels: typing.Dict[str, typing.Any]

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    failedLocations: typing.List[str]

class AppProfile(typing_extensions.TypedDict, total=False):
    name: str
    etag: str
    multiClusterRoutingUseAny: MultiClusterRoutingUseAny
    description: str
    singleClusterRouting: SingleClusterRouting

class CreateTableRequest(typing_extensions.TypedDict, total=False):
    tableId: str
    table: Table
    initialSplits: typing.List[Split]

class ColumnFamily(typing.Dict[str, typing.Any]): ...

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    expression: str
    location: str
    description: str

class Frame(typing_extensions.TypedDict, total=False):
    targetName: str
    zoneId: str
    workflowGuid: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: Cluster
    parent: str
    clusterId: str

class ListAppProfilesResponse(typing_extensions.TypedDict, total=False):
    appProfiles: typing.List[AppProfile]
    failedLocations: typing.List[str]
    nextPageToken: str

class TableProgress(typing_extensions.TypedDict, total=False):
    estimatedSizeBytes: str
    estimatedCopiedBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COPYING", "COMPLETED", "CANCELLED"
    ]

class Empty(typing_extensions.TypedDict, total=False): ...

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    role: str
    members: typing.List[str]

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    version: int
    etag: str

class Cluster(typing_extensions.TypedDict, total=False):
    location: str
    serveNodes: int
    name: str
    state: typing_extensions.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]
    defaultStorageType: typing_extensions.Literal[
        "STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"
    ]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]
