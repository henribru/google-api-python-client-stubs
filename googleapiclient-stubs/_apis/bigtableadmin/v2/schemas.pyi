import typing

_list = list

@typing.type_check_only
class AppProfile(typing.TypedDict, total=False):
    dataBoostIsolationReadOnly: DataBoostIsolationReadOnly
    description: str
    etag: str
    multiClusterRoutingUseAny: MultiClusterRoutingUseAny
    name: str
    priority: typing.Literal[
        "PRIORITY_UNSPECIFIED", "PRIORITY_LOW", "PRIORITY_MEDIUM", "PRIORITY_HIGH"
    ]
    singleClusterRouting: SingleClusterRouting
    standardIsolation: StandardIsolation

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
class AuthorizedView(typing.TypedDict, total=False):
    deletionProtection: bool
    etag: str
    name: str
    subsetView: GoogleBigtableAdminV2AuthorizedViewSubsetView

@typing.type_check_only
class AutomatedBackupPolicy(typing.TypedDict, total=False):
    frequency: str
    locations: _list[str]
    retentionPeriod: str

@typing.type_check_only
class AutoscalingLimits(typing.TypedDict, total=False):
    maxServeNodes: int
    minServeNodes: int

@typing.type_check_only
class AutoscalingTargets(typing.TypedDict, total=False):
    cpuUtilizationPercent: int
    storageUtilizationGibPerNode: int

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
    backupType: typing.Literal["BACKUP_TYPE_UNSPECIFIED", "STANDARD", "HOT"]
    encryptionInfo: EncryptionInfo
    endTime: str
    expireTime: str
    hotToStandardTime: str
    name: str
    sizeBytes: str
    sourceBackup: str
    sourceTable: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]

@typing.type_check_only
class BackupInfo(typing.TypedDict, total=False):
    backup: str
    endTime: str
    sourceBackup: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ChangeStreamConfig(typing.TypedDict, total=False):
    retentionPeriod: str

@typing.type_check_only
class CheckConsistencyRequest(typing.TypedDict, total=False):
    consistencyToken: str
    dataBoostReadLocalWrites: DataBoostReadLocalWrites
    standardReadRemoteWrites: StandardReadRemoteWrites

@typing.type_check_only
class CheckConsistencyResponse(typing.TypedDict, total=False):
    consistent: bool

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    clusterConfig: ClusterConfig
    defaultStorageType: typing.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]
    encryptionConfig: EncryptionConfig
    location: str
    name: str
    nodeScalingFactor: typing.Literal[
        "NODE_SCALING_FACTOR_UNSPECIFIED",
        "NODE_SCALING_FACTOR_1X",
        "NODE_SCALING_FACTOR_2X",
    ]
    serveNodes: int
    state: typing.Literal[
        "STATE_NOT_KNOWN", "READY", "CREATING", "RESIZING", "DISABLED"
    ]

@typing.type_check_only
class ClusterAutoscalingConfig(typing.TypedDict, total=False):
    autoscalingLimits: AutoscalingLimits
    autoscalingTargets: AutoscalingTargets

@typing.type_check_only
class ClusterConfig(typing.TypedDict, total=False):
    clusterAutoscalingConfig: ClusterAutoscalingConfig

@typing.type_check_only
class ClusterState(typing.TypedDict, total=False):
    encryptionInfo: _list[EncryptionInfo]
    replicationState: typing.Literal[
        "STATE_NOT_KNOWN",
        "INITIALIZING",
        "PLANNED_MAINTENANCE",
        "UNPLANNED_MAINTENANCE",
        "READY",
        "READY_OPTIMIZING",
    ]

@typing.type_check_only
class ColumnFamily(typing.TypedDict, total=False):
    gcRule: GcRule
    stats: ColumnFamilyStats
    valueType: Type

@typing.type_check_only
class ColumnFamilyStats(typing.TypedDict, total=False):
    averageCellsPerColumn: float
    averageColumnsPerRow: float
    logicalDataBytes: str
    logicalDataHddBytes: str
    logicalDataSsdBytes: str

@typing.type_check_only
class CopyBackupMetadata(typing.TypedDict, total=False):
    name: str
    progress: OperationProgress
    sourceBackupInfo: BackupInfo

@typing.type_check_only
class CopyBackupRequest(typing.TypedDict, total=False):
    backupId: str
    expireTime: str
    sourceBackup: str

@typing.type_check_only
class CreateAuthorizedViewMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateAuthorizedViewRequest
    requestTime: str

@typing.type_check_only
class CreateAuthorizedViewRequest(typing.TypedDict, total=False):
    authorizedView: AuthorizedView
    authorizedViewId: str
    parent: str

@typing.type_check_only
class CreateBackupMetadata(typing.TypedDict, total=False):
    endTime: str
    finishTime: str
    name: str
    requestTime: str
    sourceTable: str
    startTime: str

@typing.type_check_only
class CreateClusterMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateClusterRequest
    requestTime: str
    tables: dict[str, typing.Any]

@typing.type_check_only
class CreateClusterRequest(typing.TypedDict, total=False):
    cluster: Cluster
    clusterId: str
    parent: str

@typing.type_check_only
class CreateInstanceMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: CreateInstanceRequest
    requestTime: str

@typing.type_check_only
class CreateInstanceRequest(typing.TypedDict, total=False):
    clusters: dict[str, typing.Any]
    instance: Instance
    instanceId: str
    parent: str

@typing.type_check_only
class CreateLogicalViewMetadata(typing.TypedDict, total=False):
    endTime: str
    finishTime: str
    originalRequest: CreateLogicalViewRequest
    requestTime: str
    startTime: str

@typing.type_check_only
class CreateLogicalViewRequest(typing.TypedDict, total=False):
    logicalView: LogicalView
    logicalViewId: str
    parent: str

@typing.type_check_only
class CreateMaterializedViewMetadata(typing.TypedDict, total=False):
    endTime: str
    finishTime: str
    originalRequest: CreateMaterializedViewRequest
    requestTime: str
    startTime: str

@typing.type_check_only
class CreateMaterializedViewRequest(typing.TypedDict, total=False):
    ignoreWarnings: bool
    materializedView: MaterializedView
    materializedViewId: str
    parent: str

@typing.type_check_only
class CreateSchemaBundleMetadata(typing.TypedDict, total=False):
    finishTime: str
    name: str
    requestTime: str

@typing.type_check_only
class CreateTableRequest(typing.TypedDict, total=False):
    initialSplits: _list[Split]
    table: Table
    tableId: str

@typing.type_check_only
class DataBoostIsolationReadOnly(typing.TypedDict, total=False):
    computeBillingOwner: typing.Literal[
        "COMPUTE_BILLING_OWNER_UNSPECIFIED", "HOST_PAYS"
    ]

@typing.type_check_only
class DataBoostReadLocalWrites(typing.TypedDict, total=False): ...

@typing.type_check_only
class DropRowRangeRequest(typing.TypedDict, total=False):
    deleteAllDataFromTable: bool
    rowKeyPrefix: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EncryptionInfo(typing.TypedDict, total=False):
    encryptionStatus: Status
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyVersion: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GcRule(typing.TypedDict, total=False):
    intersection: Intersection
    maxAge: str
    maxNumVersions: int
    union: Union

@typing.type_check_only
class GenerateConsistencyTokenRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenerateConsistencyTokenResponse(typing.TypedDict, total=False):
    consistencyToken: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleBigtableAdminV2AuthorizedViewFamilySubsets(typing.TypedDict, total=False):
    qualifierPrefixes: _list[str]
    qualifiers: _list[str]

@typing.type_check_only
class GoogleBigtableAdminV2AuthorizedViewSubsetView(typing.TypedDict, total=False):
    familySubsets: dict[str, typing.Any]
    rowPrefixes: _list[str]

@typing.type_check_only
class GoogleBigtableAdminV2MaterializedViewClusterState(typing.TypedDict, total=False):
    replicationState: typing.Literal["STATE_NOT_KNOWN", "INITIALIZING", "READY"]

@typing.type_check_only
class GoogleBigtableAdminV2MemoryLayerMemoryConfig(typing.TypedDict, total=False):
    storageSizeGib: int

@typing.type_check_only
class GoogleBigtableAdminV2TypeAggregate(typing.TypedDict, total=False):
    hllppUniqueCount: GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount
    inputType: Type
    max: GoogleBigtableAdminV2TypeAggregateMax
    min: GoogleBigtableAdminV2TypeAggregateMin
    stateType: Type
    sum: GoogleBigtableAdminV2TypeAggregateSum

@typing.type_check_only
class GoogleBigtableAdminV2TypeAggregateHyperLogLogPlusPlusUniqueCount(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeAggregateMax(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeAggregateMin(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeAggregateSum(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeArray(typing.TypedDict, total=False):
    elementType: Type

@typing.type_check_only
class GoogleBigtableAdminV2TypeBool(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeBoolEncoding

@typing.type_check_only
class GoogleBigtableAdminV2TypeBoolEncoding(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeBytes(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeBytesEncoding

@typing.type_check_only
class GoogleBigtableAdminV2TypeBytesEncoding(typing.TypedDict, total=False):
    raw: GoogleBigtableAdminV2TypeBytesEncodingRaw

@typing.type_check_only
class GoogleBigtableAdminV2TypeBytesEncodingRaw(typing.TypedDict, total=False):
    escapeNulls: bool

@typing.type_check_only
class GoogleBigtableAdminV2TypeDate(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeEnum(typing.TypedDict, total=False):
    enumName: str
    schemaBundleId: str

@typing.type_check_only
class GoogleBigtableAdminV2TypeFloat32(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeFloat64(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeGeography(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt32(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeInt32Encoding

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt32Encoding(typing.TypedDict, total=False):
    bigEndianBytes: GoogleBigtableAdminV2TypeInt32EncodingBigEndianBytes
    orderedCodeBytes: GoogleBigtableAdminV2TypeInt32EncodingOrderedCodeBytes

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt32EncodingBigEndianBytes(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt32EncodingOrderedCodeBytes(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt64(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeInt64Encoding

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt64Encoding(typing.TypedDict, total=False):
    bigEndianBytes: GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes
    orderedCodeBytes: GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt64EncodingBigEndianBytes(
    typing.TypedDict, total=False
):
    bytesType: GoogleBigtableAdminV2TypeBytes

@typing.type_check_only
class GoogleBigtableAdminV2TypeInt64EncodingOrderedCodeBytes(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeMap(typing.TypedDict, total=False):
    keyType: Type
    valueType: Type

@typing.type_check_only
class GoogleBigtableAdminV2TypeProto(typing.TypedDict, total=False):
    messageName: str
    schemaBundleId: str

@typing.type_check_only
class GoogleBigtableAdminV2TypeString(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeStringEncoding

@typing.type_check_only
class GoogleBigtableAdminV2TypeStringEncoding(typing.TypedDict, total=False):
    utf8Bytes: GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes
    utf8Raw: GoogleBigtableAdminV2TypeStringEncodingUtf8Raw

@typing.type_check_only
class GoogleBigtableAdminV2TypeStringEncodingUtf8Bytes(typing.TypedDict, total=False):
    nullEscapeChar: str

@typing.type_check_only
class GoogleBigtableAdminV2TypeStringEncodingUtf8Raw(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeStruct(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeStructEncoding
    fields: _list[GoogleBigtableAdminV2TypeStructField]

@typing.type_check_only
class GoogleBigtableAdminV2TypeStructEncoding(typing.TypedDict, total=False):
    delimitedBytes: GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes
    orderedCodeBytes: GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes
    singleton: GoogleBigtableAdminV2TypeStructEncodingSingleton

@typing.type_check_only
class GoogleBigtableAdminV2TypeStructEncodingDelimitedBytes(
    typing.TypedDict, total=False
):
    delimiter: str

@typing.type_check_only
class GoogleBigtableAdminV2TypeStructEncodingOrderedCodeBytes(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeStructEncodingSingleton(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleBigtableAdminV2TypeStructField(typing.TypedDict, total=False):
    fieldName: str
    type: Type

@typing.type_check_only
class GoogleBigtableAdminV2TypeTimestamp(typing.TypedDict, total=False):
    encoding: GoogleBigtableAdminV2TypeTimestampEncoding

@typing.type_check_only
class GoogleBigtableAdminV2TypeTimestampEncoding(typing.TypedDict, total=False):
    unixMicrosInt64: GoogleBigtableAdminV2TypeInt64Encoding

@typing.type_check_only
class HotTablet(typing.TypedDict, total=False):
    endKey: str
    endTime: str
    name: str
    nodeCpuUsagePercent: float
    startKey: str
    startTime: str
    tableName: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    edition: typing.Literal["EDITION_UNSPECIFIED", "ENTERPRISE", "ENTERPRISE_PLUS"]
    knowledgeCatalogRegion: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal["STATE_NOT_KNOWN", "READY", "CREATING"]
    tags: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"]

@typing.type_check_only
class Intersection(typing.TypedDict, total=False):
    rules: _list[GcRule]

@typing.type_check_only
class ListAppProfilesResponse(typing.TypedDict, total=False):
    appProfiles: _list[AppProfile]
    failedLocations: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListAuthorizedViewsResponse(typing.TypedDict, total=False):
    authorizedViews: _list[AuthorizedView]
    nextPageToken: str

@typing.type_check_only
class ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str

@typing.type_check_only
class ListClustersResponse(typing.TypedDict, total=False):
    clusters: _list[Cluster]
    failedLocations: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListHotTabletsResponse(typing.TypedDict, total=False):
    hotTablets: _list[HotTablet]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    failedLocations: _list[str]
    instances: _list[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListLogicalViewsResponse(typing.TypedDict, total=False):
    logicalViews: _list[LogicalView]
    nextPageToken: str

@typing.type_check_only
class ListMaterializedViewsResponse(typing.TypedDict, total=False):
    materializedViews: _list[MaterializedView]
    nextPageToken: str

@typing.type_check_only
class ListMemoryLayersResponse(typing.TypedDict, total=False):
    failedLocations: _list[str]
    memoryLayers: _list[MemoryLayer]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListSchemaBundlesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schemaBundles: _list[SchemaBundle]

@typing.type_check_only
class ListTablesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tables: _list[Table]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogicalView(typing.TypedDict, total=False):
    deletionProtection: bool
    etag: str
    name: str
    query: str

@typing.type_check_only
class MaterializedView(typing.TypedDict, total=False):
    clusterStates: dict[str, typing.Any]
    deletionProtection: bool
    etag: str
    name: str
    query: str

@typing.type_check_only
class MemoryConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class MemoryLayer(typing.TypedDict, total=False):
    etag: str
    memoryConfig: GoogleBigtableAdminV2MemoryLayerMemoryConfig
    name: str
    state: typing.Literal[
        "STATE_NOT_KNOWN", "READY", "ENABLING", "RESIZING", "DISABLED"
    ]

@typing.type_check_only
class Modification(typing.TypedDict, total=False):
    create: ColumnFamily
    drop: bool
    id: str
    update: ColumnFamily
    updateMask: str

@typing.type_check_only
class ModifyColumnFamiliesRequest(typing.TypedDict, total=False):
    ignoreWarnings: bool
    modifications: _list[Modification]

@typing.type_check_only
class MultiClusterRoutingUseAny(typing.TypedDict, total=False):
    clusterIds: _list[str]
    rowAffinity: RowAffinity

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationProgress(typing.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

@typing.type_check_only
class OptimizeRestoredTableMetadata(typing.TypedDict, total=False):
    name: str
    progress: OperationProgress

@typing.type_check_only
class PartialUpdateClusterMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateClusterRequest
    requestTime: str

@typing.type_check_only
class PartialUpdateClusterRequest(typing.TypedDict, total=False):
    cluster: Cluster
    updateMask: str

@typing.type_check_only
class PartialUpdateInstanceRequest(typing.TypedDict, total=False):
    instance: Instance
    updateMask: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProtoSchema(typing.TypedDict, total=False):
    protoDescriptors: str

@typing.type_check_only
class RestoreInfo(typing.TypedDict, total=False):
    backupInfo: BackupInfo
    sourceType: typing.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class RestoreTableMetadata(typing.TypedDict, total=False):
    backupInfo: BackupInfo
    name: str
    optimizeTableOperationName: str
    progress: OperationProgress
    sourceType: typing.Literal["RESTORE_SOURCE_TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class RestoreTableRequest(typing.TypedDict, total=False):
    backup: str
    tableId: str

@typing.type_check_only
class RowAffinity(typing.TypedDict, total=False): ...

@typing.type_check_only
class SchemaBundle(typing.TypedDict, total=False):
    etag: str
    name: str
    protoSchema: ProtoSchema

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SingleClusterRouting(typing.TypedDict, total=False):
    allowTransactionalWrites: bool
    clusterId: str

@typing.type_check_only
class Split(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class StandardIsolation(typing.TypedDict, total=False):
    memoryConfig: MemoryConfig
    priority: typing.Literal[
        "PRIORITY_UNSPECIFIED", "PRIORITY_LOW", "PRIORITY_MEDIUM", "PRIORITY_HIGH"
    ]

@typing.type_check_only
class StandardReadRemoteWrites(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    automatedBackupPolicy: AutomatedBackupPolicy
    changeStreamConfig: ChangeStreamConfig
    clusterStates: dict[str, typing.Any]
    columnFamilies: dict[str, typing.Any]
    deletionProtection: bool
    granularity: typing.Literal["TIMESTAMP_GRANULARITY_UNSPECIFIED", "MILLIS"]
    name: str
    restoreInfo: RestoreInfo
    rowKeySchema: GoogleBigtableAdminV2TypeStruct
    stats: TableStats
    tieredStorageConfig: TieredStorageConfig

@typing.type_check_only
class TableProgress(typing.TypedDict, total=False):
    estimatedCopiedBytes: str
    estimatedSizeBytes: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "COPYING", "COMPLETED", "CANCELLED"
    ]

@typing.type_check_only
class TableStats(typing.TypedDict, total=False):
    averageCellsPerColumn: float
    averageColumnsPerRow: float
    logicalDataBytes: str
    rowCount: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TieredStorageConfig(typing.TypedDict, total=False):
    infrequentAccess: TieredStorageRule

@typing.type_check_only
class TieredStorageRule(typing.TypedDict, total=False):
    includeIfOlderThan: str

@typing.type_check_only
class Type(typing.TypedDict, total=False):
    aggregateType: GoogleBigtableAdminV2TypeAggregate
    arrayType: GoogleBigtableAdminV2TypeArray
    boolType: GoogleBigtableAdminV2TypeBool
    bytesType: GoogleBigtableAdminV2TypeBytes
    dateType: GoogleBigtableAdminV2TypeDate
    enumType: GoogleBigtableAdminV2TypeEnum
    float32Type: GoogleBigtableAdminV2TypeFloat32
    float64Type: GoogleBigtableAdminV2TypeFloat64
    geographyType: GoogleBigtableAdminV2TypeGeography
    int32Type: GoogleBigtableAdminV2TypeInt32
    int64Type: GoogleBigtableAdminV2TypeInt64
    mapType: GoogleBigtableAdminV2TypeMap
    protoType: GoogleBigtableAdminV2TypeProto
    stringType: GoogleBigtableAdminV2TypeString
    structType: GoogleBigtableAdminV2TypeStruct
    timestampType: GoogleBigtableAdminV2TypeTimestamp

@typing.type_check_only
class UndeleteTableMetadata(typing.TypedDict, total=False):
    endTime: str
    finishTime: str
    name: str
    requestTime: str
    startTime: str

@typing.type_check_only
class UndeleteTableRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Union(typing.TypedDict, total=False):
    rules: _list[GcRule]

@typing.type_check_only
class UpdateAppProfileMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateAuthorizedViewMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: UpdateAuthorizedViewRequest
    requestTime: str

@typing.type_check_only
class UpdateAuthorizedViewRequest(typing.TypedDict, total=False):
    authorizedView: AuthorizedView
    ignoreWarnings: bool
    updateMask: str

@typing.type_check_only
class UpdateClusterMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: Cluster
    requestTime: str

@typing.type_check_only
class UpdateInstanceMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: PartialUpdateInstanceRequest
    requestTime: str

@typing.type_check_only
class UpdateLogicalViewMetadata(typing.TypedDict, total=False):
    endTime: str
    finishTime: str
    originalRequest: UpdateLogicalViewRequest
    requestTime: str
    startTime: str

@typing.type_check_only
class UpdateLogicalViewRequest(typing.TypedDict, total=False):
    logicalView: LogicalView
    updateMask: str

@typing.type_check_only
class UpdateMemoryLayerMetadata(typing.TypedDict, total=False):
    finishTime: str
    originalRequest: UpdateMemoryLayerRequest
    requestTime: str

@typing.type_check_only
class UpdateMemoryLayerRequest(typing.TypedDict, total=False):
    memoryLayer: MemoryLayer
    updateMask: str

@typing.type_check_only
class UpdateSchemaBundleMetadata(typing.TypedDict, total=False):
    finishTime: str
    name: str
    requestTime: str

@typing.type_check_only
class UpdateTableMetadata(typing.TypedDict, total=False):
    endTime: str
    finishTime: str
    name: str
    requestTime: str
    startTime: str
