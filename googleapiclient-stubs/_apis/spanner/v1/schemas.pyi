import typing

import typing_extensions

_list = list

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    createTime: str
    database: str
    databaseDialect: typing_extensions.Literal[
        "DATABASE_DIALECT_UNSPECIFIED", "GOOGLE_STANDARD_SQL", "POSTGRESQL"
    ]
    encryptionInfo: EncryptionInfo
    expireTime: str
    maxExpireTime: str
    name: str
    referencingBackups: _list[str]
    referencingDatabases: _list[str]
    sizeBytes: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    versionTime: str

@typing.type_check_only
class BackupInfo(typing_extensions.TypedDict, total=False):
    backup: str
    createTime: str
    sourceDatabase: str
    versionTime: str

@typing.type_check_only
class BatchCreateSessionsRequest(typing_extensions.TypedDict, total=False):
    sessionCount: int
    sessionTemplate: Session

@typing.type_check_only
class BatchCreateSessionsResponse(typing_extensions.TypedDict, total=False):
    session: _list[Session]

@typing.type_check_only
class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    options: TransactionOptions
    requestOptions: RequestOptions

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ChildLink(typing_extensions.TypedDict, total=False):
    childIndex: int
    type: str
    variable: str

@typing.type_check_only
class CommitRequest(typing_extensions.TypedDict, total=False):
    mutations: _list[Mutation]
    requestOptions: RequestOptions
    returnCommitStats: bool
    singleUseTransaction: TransactionOptions
    transactionId: str

@typing.type_check_only
class CommitResponse(typing_extensions.TypedDict, total=False):
    commitStats: CommitStats
    commitTimestamp: str

@typing.type_check_only
class CommitStats(typing_extensions.TypedDict, total=False):
    mutationCount: str

@typing.type_check_only
class ContextValue(typing_extensions.TypedDict, total=False):
    label: LocalizedString
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "FATAL"
    ]
    unit: str
    value: float

@typing.type_check_only
class CopyBackupEncryptionConfig(typing_extensions.TypedDict, total=False):
    encryptionType: typing_extensions.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyName: str

@typing.type_check_only
class CopyBackupMetadata(typing_extensions.TypedDict, total=False):
    cancelTime: str
    name: str
    progress: OperationProgress
    sourceBackup: str

@typing.type_check_only
class CopyBackupRequest(typing_extensions.TypedDict, total=False):
    backupId: str
    encryptionConfig: CopyBackupEncryptionConfig
    expireTime: str
    sourceBackup: str

@typing.type_check_only
class CreateBackupMetadata(typing_extensions.TypedDict, total=False):
    cancelTime: str
    database: str
    name: str
    progress: OperationProgress

@typing.type_check_only
class CreateDatabaseMetadata(typing_extensions.TypedDict, total=False):
    database: str

@typing.type_check_only
class CreateDatabaseRequest(typing_extensions.TypedDict, total=False):
    createStatement: str
    databaseDialect: typing_extensions.Literal[
        "DATABASE_DIALECT_UNSPECIFIED", "GOOGLE_STANDARD_SQL", "POSTGRESQL"
    ]
    encryptionConfig: EncryptionConfig
    extraStatements: _list[str]

@typing.type_check_only
class CreateInstanceConfigMetadata(typing_extensions.TypedDict, total=False):
    cancelTime: str
    instanceConfig: InstanceConfig
    progress: InstanceOperationProgress

@typing.type_check_only
class CreateInstanceConfigRequest(typing_extensions.TypedDict, total=False):
    instanceConfig: InstanceConfig
    instanceConfigId: str
    validateOnly: bool

@typing.type_check_only
class CreateInstanceMetadata(typing_extensions.TypedDict, total=False):
    cancelTime: str
    endTime: str
    instance: Instance
    startTime: str

@typing.type_check_only
class CreateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    instanceId: str

@typing.type_check_only
class CreateSessionRequest(typing_extensions.TypedDict, total=False):
    session: Session

@typing.type_check_only
class Database(typing_extensions.TypedDict, total=False):
    createTime: str
    databaseDialect: typing_extensions.Literal[
        "DATABASE_DIALECT_UNSPECIFIED", "GOOGLE_STANDARD_SQL", "POSTGRESQL"
    ]
    defaultLeader: str
    earliestVersionTime: str
    encryptionConfig: EncryptionConfig
    encryptionInfo: _list[EncryptionInfo]
    name: str
    restoreInfo: RestoreInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "READY_OPTIMIZING"
    ]
    versionRetentionPeriod: str

@typing.type_check_only
class DatabaseRole(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Delete(typing_extensions.TypedDict, total=False):
    keySet: KeySet
    table: str

@typing.type_check_only
class DerivedMetric(typing_extensions.TypedDict, total=False):
    denominator: LocalizedString
    numerator: LocalizedString

@typing.type_check_only
class DiagnosticMessage(typing_extensions.TypedDict, total=False):
    info: LocalizedString
    metric: LocalizedString
    metricSpecific: bool
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "FATAL"
    ]
    shortMessage: LocalizedString

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EncryptionInfo(typing_extensions.TypedDict, total=False):
    encryptionStatus: Status
    encryptionType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_DEFAULT_ENCRYPTION", "CUSTOMER_MANAGED_ENCRYPTION"
    ]
    kmsKeyVersion: str

@typing.type_check_only
class ExecuteBatchDmlRequest(typing_extensions.TypedDict, total=False):
    requestOptions: RequestOptions
    seqno: str
    statements: _list[Statement]
    transaction: TransactionSelector

@typing.type_check_only
class ExecuteBatchDmlResponse(typing_extensions.TypedDict, total=False):
    resultSets: _list[ResultSet]
    status: Status

@typing.type_check_only
class ExecuteSqlRequest(typing_extensions.TypedDict, total=False):
    paramTypes: dict[str, typing.Any]
    params: dict[str, typing.Any]
    partitionToken: str
    queryMode: typing_extensions.Literal["NORMAL", "PLAN", "PROFILE"]
    queryOptions: QueryOptions
    requestOptions: RequestOptions
    resumeToken: str
    seqno: str
    sql: str
    transaction: TransactionSelector

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    name: str
    type: Type

@typing.type_check_only
class FreeInstanceMetadata(typing_extensions.TypedDict, total=False):
    expireBehavior: typing_extensions.Literal[
        "EXPIRE_BEHAVIOR_UNSPECIFIED",
        "FREE_TO_PROVISIONED",
        "REMOVE_AFTER_GRACE_PERIOD",
    ]
    expireTime: str
    upgradeTime: str

@typing.type_check_only
class GetDatabaseDdlResponse(typing_extensions.TypedDict, total=False):
    statements: _list[str]

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class IndexedHotKey(typing_extensions.TypedDict, total=False):
    sparseHotKeys: dict[str, typing.Any]

@typing.type_check_only
class IndexedKeyRangeInfos(typing_extensions.TypedDict, total=False):
    keyRangeInfos: dict[str, typing.Any]

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    config: str
    createTime: str
    displayName: str
    endpointUris: _list[str]
    freeInstanceMetadata: FreeInstanceMetadata
    instanceType: typing_extensions.Literal[
        "INSTANCE_TYPE_UNSPECIFIED", "PROVISIONED", "FREE_INSTANCE"
    ]
    labels: dict[str, typing.Any]
    name: str
    nodeCount: int
    processingUnits: int
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    updateTime: str

@typing.type_check_only
class InstanceConfig(typing_extensions.TypedDict, total=False):
    baseConfig: str
    configType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_MANAGED", "USER_MANAGED"
    ]
    displayName: str
    etag: str
    freeInstanceAvailability: typing_extensions.Literal[
        "FREE_INSTANCE_AVAILABILITY_UNSPECIFIED",
        "AVAILABLE",
        "UNSUPPORTED",
        "DISABLED",
        "QUOTA_EXCEEDED",
    ]
    labels: dict[str, typing.Any]
    leaderOptions: _list[str]
    name: str
    optionalReplicas: _list[ReplicaInfo]
    reconciling: bool
    replicas: _list[ReplicaInfo]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]

@typing.type_check_only
class InstanceOperationProgress(typing_extensions.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

@typing.type_check_only
class KeyRange(typing_extensions.TypedDict, total=False):
    endClosed: _list[typing.Any]
    endOpen: _list[typing.Any]
    startClosed: _list[typing.Any]
    startOpen: _list[typing.Any]

@typing.type_check_only
class KeyRangeInfo(typing_extensions.TypedDict, total=False):
    contextValues: _list[ContextValue]
    endKeyIndex: int
    info: LocalizedString
    keysCount: str
    metric: LocalizedString
    startKeyIndex: int
    timeOffset: str
    unit: LocalizedString
    value: float

@typing.type_check_only
class KeyRangeInfos(typing_extensions.TypedDict, total=False):
    infos: _list[KeyRangeInfo]
    totalSize: int

@typing.type_check_only
class KeySet(typing_extensions.TypedDict, total=False):
    all: bool
    keys: _list[list]
    ranges: _list[KeyRange]

@typing.type_check_only
class ListBackupOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str

@typing.type_check_only
class ListDatabaseOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListDatabaseRolesResponse(typing_extensions.TypedDict, total=False):
    databaseRoles: _list[DatabaseRole]
    nextPageToken: str

@typing.type_check_only
class ListDatabasesResponse(typing_extensions.TypedDict, total=False):
    databases: _list[Database]
    nextPageToken: str

@typing.type_check_only
class ListInstanceConfigOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListInstanceConfigsResponse(typing_extensions.TypedDict, total=False):
    instanceConfigs: _list[InstanceConfig]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListScansResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scans: _list[Scan]

@typing.type_check_only
class ListSessionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[Session]

@typing.type_check_only
class LocalizedString(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    message: str
    token: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    aggregation: typing_extensions.Literal["AGGREGATION_UNSPECIFIED", "MAX", "SUM"]
    category: LocalizedString
    derived: DerivedMetric
    displayLabel: LocalizedString
    hasNonzeroData: bool
    hotValue: float
    indexedHotKeys: dict[str, typing.Any]
    indexedKeyRangeInfos: dict[str, typing.Any]
    info: LocalizedString
    matrix: MetricMatrix
    unit: LocalizedString
    visible: bool

@typing.type_check_only
class MetricMatrix(typing_extensions.TypedDict, total=False):
    rows: _list[MetricMatrixRow]

@typing.type_check_only
class MetricMatrixRow(typing_extensions.TypedDict, total=False):
    cols: _list[float]

@typing.type_check_only
class Mutation(typing_extensions.TypedDict, total=False):
    delete: Delete
    insert: Write
    insertOrUpdate: Write
    replace: Write
    update: Write

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
class OptimizeRestoredDatabaseMetadata(typing_extensions.TypedDict, total=False):
    name: str
    progress: OperationProgress

@typing.type_check_only
class PartialResultSet(typing_extensions.TypedDict, total=False):
    chunkedValue: bool
    metadata: ResultSetMetadata
    resumeToken: str
    stats: ResultSetStats
    values: _list[typing.Any]

@typing.type_check_only
class Partition(typing_extensions.TypedDict, total=False):
    partitionToken: str

@typing.type_check_only
class PartitionOptions(typing_extensions.TypedDict, total=False):
    maxPartitions: str
    partitionSizeBytes: str

@typing.type_check_only
class PartitionQueryRequest(typing_extensions.TypedDict, total=False):
    paramTypes: dict[str, typing.Any]
    params: dict[str, typing.Any]
    partitionOptions: PartitionOptions
    sql: str
    transaction: TransactionSelector

@typing.type_check_only
class PartitionReadRequest(typing_extensions.TypedDict, total=False):
    columns: _list[str]
    index: str
    keySet: KeySet
    partitionOptions: PartitionOptions
    table: str
    transaction: TransactionSelector

@typing.type_check_only
class PartitionResponse(typing_extensions.TypedDict, total=False):
    partitions: _list[Partition]
    transaction: Transaction

@typing.type_check_only
class PartitionedDml(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PlanNode(typing_extensions.TypedDict, total=False):
    childLinks: _list[ChildLink]
    displayName: str
    executionStats: dict[str, typing.Any]
    index: int
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "RELATIONAL", "SCALAR"]
    metadata: dict[str, typing.Any]
    shortRepresentation: ShortRepresentation

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrefixNode(typing_extensions.TypedDict, total=False):
    dataSourceNode: bool
    depth: int
    endIndex: int
    startIndex: int
    word: str

@typing.type_check_only
class QueryOptions(typing_extensions.TypedDict, total=False):
    optimizerStatisticsPackage: str
    optimizerVersion: str

@typing.type_check_only
class QueryPlan(typing_extensions.TypedDict, total=False):
    planNodes: _list[PlanNode]

@typing.type_check_only
class ReadOnly(typing_extensions.TypedDict, total=False):
    exactStaleness: str
    maxStaleness: str
    minReadTimestamp: str
    readTimestamp: str
    returnReadTimestamp: bool
    strong: bool

@typing.type_check_only
class ReadRequest(typing_extensions.TypedDict, total=False):
    columns: _list[str]
    index: str
    keySet: KeySet
    limit: str
    partitionToken: str
    requestOptions: RequestOptions
    resumeToken: str
    table: str
    transaction: TransactionSelector

@typing.type_check_only
class ReadWrite(typing_extensions.TypedDict, total=False):
    readLockMode: typing_extensions.Literal[
        "READ_LOCK_MODE_UNSPECIFIED", "PESSIMISTIC", "OPTIMISTIC"
    ]

@typing.type_check_only
class ReplicaInfo(typing_extensions.TypedDict, total=False):
    defaultLeaderLocation: bool
    location: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "READ_WRITE", "READ_ONLY", "WITNESS"
    ]

@typing.type_check_only
class RequestOptions(typing_extensions.TypedDict, total=False):
    priority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "PRIORITY_LOW", "PRIORITY_MEDIUM", "PRIORITY_HIGH"
    ]
    requestTag: str
    transactionTag: str

@typing.type_check_only
class RestoreDatabaseEncryptionConfig(typing_extensions.TypedDict, total=False):
    encryptionType: typing_extensions.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyName: str

@typing.type_check_only
class RestoreDatabaseMetadata(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    cancelTime: str
    name: str
    optimizeDatabaseOperationName: str
    progress: OperationProgress
    sourceType: typing_extensions.Literal["TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class RestoreDatabaseRequest(typing_extensions.TypedDict, total=False):
    backup: str
    databaseId: str
    encryptionConfig: RestoreDatabaseEncryptionConfig

@typing.type_check_only
class RestoreInfo(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    sourceType: typing_extensions.Literal["TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class ResultSet(dict[str, typing.Any]): ...

@typing.type_check_only
class ResultSetMetadata(dict[str, typing.Any]): ...

@typing.type_check_only
class ResultSetStats(typing_extensions.TypedDict, total=False):
    queryPlan: QueryPlan
    queryStats: dict[str, typing.Any]
    rowCountExact: str
    rowCountLowerBound: str

@typing.type_check_only
class RollbackRequest(typing_extensions.TypedDict, total=False):
    transactionId: str

@typing.type_check_only
class Scan(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    endTime: str
    name: str
    scanData: ScanData
    startTime: str

@typing.type_check_only
class ScanData(typing_extensions.TypedDict, total=False):
    data: VisualizationData
    endTime: str
    startTime: str

@typing.type_check_only
class Session(typing_extensions.TypedDict, total=False):
    approximateLastUseTime: str
    createTime: str
    creatorRole: str
    labels: dict[str, typing.Any]
    name: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShortRepresentation(typing_extensions.TypedDict, total=False):
    description: str
    subqueries: dict[str, typing.Any]

@typing.type_check_only
class Statement(typing_extensions.TypedDict, total=False):
    paramTypes: dict[str, typing.Any]
    params: dict[str, typing.Any]
    sql: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructType(dict[str, typing.Any]): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Transaction(typing_extensions.TypedDict, total=False):
    id: str
    readTimestamp: str

@typing.type_check_only
class TransactionOptions(typing_extensions.TypedDict, total=False):
    partitionedDml: PartitionedDml
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class TransactionSelector(typing_extensions.TypedDict, total=False):
    begin: TransactionOptions
    id: str
    singleUse: TransactionOptions

@typing.type_check_only
class Type(dict[str, typing.Any]): ...

@typing.type_check_only
class UpdateDatabaseDdlMetadata(typing_extensions.TypedDict, total=False):
    commitTimestamps: _list[str]
    database: str
    progress: _list[OperationProgress]
    statements: _list[str]
    throttled: bool

@typing.type_check_only
class UpdateDatabaseDdlRequest(typing_extensions.TypedDict, total=False):
    operationId: str
    statements: _list[str]

@typing.type_check_only
class UpdateInstanceConfigMetadata(typing_extensions.TypedDict, total=False):
    cancelTime: str
    instanceConfig: InstanceConfig
    progress: InstanceOperationProgress

@typing.type_check_only
class UpdateInstanceConfigRequest(typing_extensions.TypedDict, total=False):
    instanceConfig: InstanceConfig
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class UpdateInstanceMetadata(typing_extensions.TypedDict, total=False):
    cancelTime: str
    endTime: str
    instance: Instance
    startTime: str

@typing.type_check_only
class UpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    fieldMask: str
    instance: Instance

@typing.type_check_only
class VisualizationData(typing_extensions.TypedDict, total=False):
    dataSourceEndToken: str
    dataSourceSeparatorToken: str
    diagnosticMessages: _list[DiagnosticMessage]
    endKeyStrings: _list[str]
    hasPii: bool
    indexedKeys: _list[str]
    keySeparator: str
    keyUnit: typing_extensions.Literal["KEY_UNIT_UNSPECIFIED", "KEY", "CHUNK"]
    metrics: _list[Metric]
    prefixNodes: _list[PrefixNode]

@typing.type_check_only
class Write(typing_extensions.TypedDict, total=False):
    columns: _list[str]
    table: str
    values: _list[list]
