import typing

_list = list

@typing.type_check_only
class Ack(typing.TypedDict, total=False):
    ignoreNotFound: bool
    key: _list[typing.Any]
    queue: str

@typing.type_check_only
class AdaptMessageRequest(typing.TypedDict, total=False):
    attachments: dict[str, typing.Any]
    payload: str
    protocol: str

@typing.type_check_only
class AdaptMessageResponse(typing.TypedDict, total=False):
    last: bool
    payload: str
    stateUpdates: dict[str, typing.Any]

@typing.type_check_only
class AdapterSession(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class AddSplitPointsRequest(typing.TypedDict, total=False):
    initiator: str
    splitPoints: _list[SplitPoints]

@typing.type_check_only
class AddSplitPointsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class AsymmetricAutoscalingOption(typing.TypedDict, total=False):
    overrides: AutoscalingConfigOverrides
    replicaSelection: InstanceReplicaSelection

@typing.type_check_only
class AutoscalingConfig(typing.TypedDict, total=False):
    asymmetricAutoscalingOptions: _list[AsymmetricAutoscalingOption]
    autoscalingLimits: AutoscalingLimits
    autoscalingTargets: AutoscalingTargets

@typing.type_check_only
class AutoscalingConfigOverrides(typing.TypedDict, total=False):
    autoscalingLimits: AutoscalingLimits
    autoscalingTargetHighPriorityCpuUtilizationPercent: int
    autoscalingTargetTotalCpuUtilizationPercent: int
    disableHighPriorityCpuAutoscaling: bool
    disableTotalCpuAutoscaling: bool

@typing.type_check_only
class AutoscalingLimits(typing.TypedDict, total=False):
    maxNodes: int
    maxProcessingUnits: int
    minNodes: int
    minProcessingUnits: int

@typing.type_check_only
class AutoscalingTargets(typing.TypedDict, total=False):
    highPriorityCpuUtilizationPercent: int
    storageUtilizationPercent: int
    totalCpuUtilizationPercent: int

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
    backupSchedules: _list[str]
    createTime: str
    database: str
    databaseDialect: typing.Literal[
        "DATABASE_DIALECT_UNSPECIFIED", "GOOGLE_STANDARD_SQL", "POSTGRESQL"
    ]
    encryptionInfo: EncryptionInfo
    encryptionInformation: _list[EncryptionInfo]
    exclusiveSizeBytes: str
    expireTime: str
    freeableSizeBytes: str
    incrementalBackupChainId: str
    instancePartitions: _list[BackupInstancePartition]
    maxExpireTime: str
    minimumRestorableEdition: typing.Literal[
        "EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    name: str
    oldestVersionTime: str
    referencingBackups: _list[str]
    referencingDatabases: _list[str]
    sizeBytes: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    versionTime: str

@typing.type_check_only
class BackupInfo(typing.TypedDict, total=False):
    backup: str
    createTime: str
    sourceDatabase: str
    versionTime: str

@typing.type_check_only
class BackupInstancePartition(typing.TypedDict, total=False):
    instancePartition: str

@typing.type_check_only
class BackupSchedule(typing.TypedDict, total=False):
    encryptionConfig: CreateBackupEncryptionConfig
    fullBackupSpec: FullBackupSpec
    incrementalBackupSpec: IncrementalBackupSpec
    name: str
    retentionDuration: str
    spec: BackupScheduleSpec
    updateTime: str

@typing.type_check_only
class BackupScheduleSpec(typing.TypedDict, total=False):
    cronSpec: CrontabSpec

@typing.type_check_only
class BatchCreateSessionsRequest(typing.TypedDict, total=False):
    sessionCount: int
    sessionTemplate: Session

@typing.type_check_only
class BatchCreateSessionsResponse(typing.TypedDict, total=False):
    session: _list[Session]

@typing.type_check_only
class BatchWriteRequest(typing.TypedDict, total=False):
    excludeTxnFromChangeStreams: bool
    mutationGroups: _list[MutationGroup]
    requestOptions: RequestOptions

@typing.type_check_only
class BatchWriteResponse(typing.TypedDict, total=False):
    commitTimestamp: str
    indexes: _list[int]
    status: Status

@typing.type_check_only
class BeginTransactionRequest(typing.TypedDict, total=False):
    mutationKey: Mutation
    options: TransactionOptions
    requestOptions: RequestOptions

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ChangeQuorumMetadata(typing.TypedDict, total=False):
    endTime: str
    request: ChangeQuorumRequest
    startTime: str

@typing.type_check_only
class ChangeQuorumRequest(typing.TypedDict, total=False):
    etag: str
    name: str
    quorumType: QuorumType

@typing.type_check_only
class ChangeStreamRecord(typing.TypedDict, total=False):
    dataChangeRecord: DataChangeRecord
    heartbeatRecord: HeartbeatRecord
    partitionEndRecord: PartitionEndRecord
    partitionEventRecord: PartitionEventRecord
    partitionStartRecord: PartitionStartRecord

@typing.type_check_only
class ChildLink(typing.TypedDict, total=False):
    childIndex: int
    type: str
    variable: str

@typing.type_check_only
class ClientContext(typing.TypedDict, total=False):
    secureContext: dict[str, typing.Any]

@typing.type_check_only
class ColumnMetadata(typing.TypedDict, total=False):
    isPrimaryKey: bool
    name: str
    ordinalPosition: str
    type: Type

@typing.type_check_only
class CommitRequest(typing.TypedDict, total=False):
    maxCommitDelay: str
    mutations: _list[Mutation]
    precommitToken: MultiplexedSessionPrecommitToken
    requestOptions: RequestOptions
    returnCommitStats: bool
    singleUseTransaction: TransactionOptions
    transactionId: str

@typing.type_check_only
class CommitResponse(typing.TypedDict, total=False):
    commitStats: CommitStats
    commitTimestamp: str
    isolationLevel: typing.Literal[
        "ISOLATION_LEVEL_UNSPECIFIED", "SERIALIZABLE", "REPEATABLE_READ"
    ]
    precommitToken: MultiplexedSessionPrecommitToken
    readLockMode: typing.Literal[
        "READ_LOCK_MODE_UNSPECIFIED", "PESSIMISTIC", "OPTIMISTIC"
    ]
    snapshotTimestamp: str

@typing.type_check_only
class CommitStats(typing.TypedDict, total=False):
    mutationCount: str

@typing.type_check_only
class CompactDatabaseMetadata(typing.TypedDict, total=False):
    cancelTime: str
    database: str
    progress: OperationProgress

@typing.type_check_only
class ContextValue(typing.TypedDict, total=False):
    label: LocalizedString
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "FATAL"
    ]
    unit: str
    value: float

@typing.type_check_only
class CopyBackupEncryptionConfig(typing.TypedDict, total=False):
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyName: str
    kmsKeyNames: _list[str]

@typing.type_check_only
class CopyBackupMetadata(typing.TypedDict, total=False):
    cancelTime: str
    name: str
    progress: OperationProgress
    sourceBackup: str

@typing.type_check_only
class CopyBackupRequest(typing.TypedDict, total=False):
    backupId: str
    encryptionConfig: CopyBackupEncryptionConfig
    expireTime: str
    sourceBackup: str

@typing.type_check_only
class CreateBackupEncryptionConfig(typing.TypedDict, total=False):
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "USE_DATABASE_ENCRYPTION",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyName: str
    kmsKeyNames: _list[str]

@typing.type_check_only
class CreateBackupMetadata(typing.TypedDict, total=False):
    cancelTime: str
    database: str
    name: str
    progress: OperationProgress

@typing.type_check_only
class CreateDatabaseMetadata(typing.TypedDict, total=False):
    database: str

@typing.type_check_only
class CreateDatabaseRequest(typing.TypedDict, total=False):
    createStatement: str
    databaseDialect: typing.Literal[
        "DATABASE_DIALECT_UNSPECIFIED", "GOOGLE_STANDARD_SQL", "POSTGRESQL"
    ]
    encryptionConfig: EncryptionConfig
    extraStatements: _list[str]
    protoDescriptors: str

@typing.type_check_only
class CreateInstanceConfigMetadata(typing.TypedDict, total=False):
    cancelTime: str
    instanceConfig: InstanceConfig
    progress: InstanceOperationProgress

@typing.type_check_only
class CreateInstanceConfigRequest(typing.TypedDict, total=False):
    instanceConfig: InstanceConfig
    instanceConfigId: str
    validateOnly: bool

@typing.type_check_only
class CreateInstanceMetadata(typing.TypedDict, total=False):
    cancelTime: str
    endTime: str
    expectedFulfillmentPeriod: typing.Literal[
        "FULFILLMENT_PERIOD_UNSPECIFIED",
        "FULFILLMENT_PERIOD_NORMAL",
        "FULFILLMENT_PERIOD_EXTENDED",
    ]
    instance: Instance
    startTime: str

@typing.type_check_only
class CreateInstancePartitionMetadata(typing.TypedDict, total=False):
    cancelTime: str
    endTime: str
    instancePartition: InstancePartition
    startTime: str

@typing.type_check_only
class CreateInstancePartitionRequest(typing.TypedDict, total=False):
    instancePartition: InstancePartition
    instancePartitionId: str

@typing.type_check_only
class CreateInstanceRequest(typing.TypedDict, total=False):
    instance: Instance
    instanceId: str

@typing.type_check_only
class CreateSessionRequest(typing.TypedDict, total=False):
    session: Session

@typing.type_check_only
class CrontabSpec(typing.TypedDict, total=False):
    creationWindow: str
    text: str
    timeZone: str

@typing.type_check_only
class DataChangeRecord(typing.TypedDict, total=False):
    columnMetadata: _list[ColumnMetadata]
    commitTimestamp: str
    isLastRecordInTransactionInPartition: bool
    isSystemTransaction: bool
    modType: typing.Literal["MOD_TYPE_UNSPECIFIED", "INSERT", "UPDATE", "DELETE"]
    mods: _list[Mod]
    numberOfPartitionsInTransaction: int
    numberOfRecordsInTransaction: int
    recordSequence: str
    serverTransactionId: str
    table: str
    transactionTag: str
    valueCaptureType: typing.Literal[
        "VALUE_CAPTURE_TYPE_UNSPECIFIED",
        "OLD_AND_NEW_VALUES",
        "NEW_VALUES",
        "NEW_ROW",
        "NEW_ROW_AND_OLD_VALUES",
    ]

@typing.type_check_only
class Database(typing.TypedDict, total=False):
    createTime: str
    databaseDialect: typing.Literal[
        "DATABASE_DIALECT_UNSPECIFIED", "GOOGLE_STANDARD_SQL", "POSTGRESQL"
    ]
    defaultLeader: str
    earliestVersionTime: str
    enableDropProtection: bool
    encryptionConfig: EncryptionConfig
    encryptionInfo: _list[EncryptionInfo]
    name: str
    quorumInfo: QuorumInfo
    reconciling: bool
    restoreInfo: RestoreInfo
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY", "READY_OPTIMIZING"]
    versionRetentionPeriod: str

@typing.type_check_only
class DatabaseMoveConfig(typing.TypedDict, total=False):
    databaseId: str
    encryptionConfig: InstanceEncryptionConfig

@typing.type_check_only
class DatabaseRole(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DdlStatementActionInfo(typing.TypedDict, total=False):
    action: str
    entityNames: _list[str]
    entityType: str

@typing.type_check_only
class Delete(typing.TypedDict, total=False):
    keySet: KeySet
    table: str

@typing.type_check_only
class DerivedMetric(typing.TypedDict, total=False):
    denominator: LocalizedString
    numerator: LocalizedString

@typing.type_check_only
class DiagnosticMessage(typing.TypedDict, total=False):
    info: LocalizedString
    metric: LocalizedString
    metricSpecific: bool
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR", "FATAL"
    ]
    shortMessage: LocalizedString

@typing.type_check_only
class DirectedReadOptions(typing.TypedDict, total=False):
    excludeReplicas: ExcludeReplicas
    includeReplicas: IncludeReplicas

@typing.type_check_only
class DualRegionQuorum(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyNames: _list[str]

@typing.type_check_only
class EncryptionInfo(typing.TypedDict, total=False):
    encryptionStatus: Status
    encryptionType: typing.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_DEFAULT_ENCRYPTION", "CUSTOMER_MANAGED_ENCRYPTION"
    ]
    kmsKeyVersion: str

@typing.type_check_only
class ExcludeReplicas(typing.TypedDict, total=False):
    replicaSelections: _list[ReplicaSelection]

@typing.type_check_only
class ExecuteBatchDmlRequest(typing.TypedDict, total=False):
    lastStatements: bool
    requestOptions: RequestOptions
    seqno: str
    statements: _list[Statement]
    transaction: TransactionSelector

@typing.type_check_only
class ExecuteBatchDmlResponse(typing.TypedDict, total=False):
    precommitToken: MultiplexedSessionPrecommitToken
    resultSets: _list[ResultSet]
    status: Status

@typing.type_check_only
class ExecuteSqlRequest(typing.TypedDict, total=False):
    dataBoostEnabled: bool
    directedReadOptions: DirectedReadOptions
    lastStatement: bool
    paramTypes: dict[str, typing.Any]
    params: dict[str, typing.Any]
    partitionToken: str
    queryMode: typing.Literal[
        "NORMAL", "PLAN", "PROFILE", "WITH_STATS", "WITH_PLAN_AND_STATS"
    ]
    queryOptions: QueryOptions
    requestOptions: RequestOptions
    resumeToken: str
    seqno: str
    sql: str
    transaction: TransactionSelector

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    name: str
    type: Type

@typing.type_check_only
class FreeInstanceMetadata(typing.TypedDict, total=False):
    expireBehavior: typing.Literal[
        "EXPIRE_BEHAVIOR_UNSPECIFIED",
        "FREE_TO_PROVISIONED",
        "REMOVE_AFTER_GRACE_PERIOD",
    ]
    expireTime: str
    upgradeTime: str

@typing.type_check_only
class FullBackupSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class GetDatabaseDdlResponse(typing.TypedDict, total=False):
    protoDescriptors: str
    statements: _list[str]

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class HeartbeatRecord(typing.TypedDict, total=False):
    timestamp: str

@typing.type_check_only
class IncludeReplicas(typing.TypedDict, total=False):
    autoFailoverDisabled: bool
    replicaSelections: _list[ReplicaSelection]

@typing.type_check_only
class IncrementalBackupSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class IndexAdvice(typing.TypedDict, total=False):
    ddl: _list[str]
    improvementFactor: float

@typing.type_check_only
class IndexedHotKey(typing.TypedDict, total=False):
    sparseHotKeys: dict[str, typing.Any]

@typing.type_check_only
class IndexedKeyRangeInfos(typing.TypedDict, total=False):
    keyRangeInfos: dict[str, typing.Any]

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    autoscalingConfig: AutoscalingConfig
    config: str
    createTime: str
    defaultBackupScheduleType: typing.Literal[
        "DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED", "NONE", "AUTOMATIC"
    ]
    displayName: str
    edition: typing.Literal[
        "EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    endpointUris: _list[str]
    freeInstanceMetadata: FreeInstanceMetadata
    instanceType: typing.Literal[
        "INSTANCE_TYPE_UNSPECIFIED", "PROVISIONED", "FREE_INSTANCE"
    ]
    labels: dict[str, typing.Any]
    name: str
    nodeCount: int
    processingUnits: int
    replicaComputeCapacity: _list[ReplicaComputeCapacity]
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    updateTime: str

@typing.type_check_only
class InstanceConfig(typing.TypedDict, total=False):
    baseConfig: str
    configType: typing.Literal["TYPE_UNSPECIFIED", "GOOGLE_MANAGED", "USER_MANAGED"]
    displayName: str
    etag: str
    freeInstanceAvailability: typing.Literal[
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
    quorumType: typing.Literal[
        "QUORUM_TYPE_UNSPECIFIED", "REGION", "DUAL_REGION", "MULTI_REGION"
    ]
    reconciling: bool
    replicas: _list[ReplicaInfo]
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    storageLimitPerProcessingUnit: str

@typing.type_check_only
class InstanceEncryptionConfig(typing.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyNames: _list[str]

@typing.type_check_only
class InstanceOperationProgress(typing.TypedDict, total=False):
    endTime: str
    progressPercent: int
    startTime: str

@typing.type_check_only
class InstancePartition(typing.TypedDict, total=False):
    autoscalingConfig: AutoscalingConfig
    config: str
    createTime: str
    displayName: str
    etag: str
    name: str
    nodeCount: int
    processingUnits: int
    referencingBackups: _list[str]
    referencingDatabases: _list[str]
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    updateTime: str

@typing.type_check_only
class InstanceReplicaSelection(typing.TypedDict, total=False):
    location: str

@typing.type_check_only
class Key(typing.TypedDict, total=False):
    keyParts: _list[typing.Any]

@typing.type_check_only
class KeyRange(typing.TypedDict, total=False):
    endClosed: _list[typing.Any]
    endOpen: _list[typing.Any]
    startClosed: _list[typing.Any]
    startOpen: _list[typing.Any]

@typing.type_check_only
class KeyRangeInfo(typing.TypedDict, total=False):
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
class KeyRangeInfos(typing.TypedDict, total=False):
    infos: _list[KeyRangeInfo]
    totalSize: int

@typing.type_check_only
class KeySet(typing.TypedDict, total=False):
    all: bool
    keys: _list[_list[typing.Any]]
    ranges: _list[KeyRange]

@typing.type_check_only
class ListBackupOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListBackupSchedulesResponse(typing.TypedDict, total=False):
    backupSchedules: _list[BackupSchedule]
    nextPageToken: str

@typing.type_check_only
class ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str

@typing.type_check_only
class ListDatabaseOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListDatabaseRolesResponse(typing.TypedDict, total=False):
    databaseRoles: _list[DatabaseRole]
    nextPageToken: str

@typing.type_check_only
class ListDatabasesResponse(typing.TypedDict, total=False):
    databases: _list[Database]
    nextPageToken: str

@typing.type_check_only
class ListInstanceConfigOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListInstanceConfigsResponse(typing.TypedDict, total=False):
    instanceConfigs: _list[InstanceConfig]
    nextPageToken: str

@typing.type_check_only
class ListInstancePartitionOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachableInstancePartitions: _list[str]

@typing.type_check_only
class ListInstancePartitionsResponse(typing.TypedDict, total=False):
    instancePartitions: _list[InstancePartition]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListScansResponse(typing.TypedDict, total=False):
    nextPageToken: str
    scans: _list[Scan]

@typing.type_check_only
class ListSessionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sessions: _list[Session]

@typing.type_check_only
class LocalizedString(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    message: str
    token: str

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    aggregation: typing.Literal["AGGREGATION_UNSPECIFIED", "MAX", "SUM"]
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
class MetricMatrix(typing.TypedDict, total=False):
    rows: _list[MetricMatrixRow]

@typing.type_check_only
class MetricMatrixRow(typing.TypedDict, total=False):
    cols: _list[float]

@typing.type_check_only
class Mod(typing.TypedDict, total=False):
    keys: _list[ModValue]
    newValues: _list[ModValue]
    oldValues: _list[ModValue]

@typing.type_check_only
class ModValue(typing.TypedDict, total=False):
    columnMetadataIndex: int
    value: typing.Any

@typing.type_check_only
class MoveInEvent(typing.TypedDict, total=False):
    sourcePartitionToken: str

@typing.type_check_only
class MoveInstanceRequest(typing.TypedDict, total=False):
    targetConfig: str
    targetDatabaseMoveConfigs: _list[DatabaseMoveConfig]

@typing.type_check_only
class MoveOutEvent(typing.TypedDict, total=False):
    destinationPartitionToken: str

@typing.type_check_only
class MultiplexedSessionPrecommitToken(typing.TypedDict, total=False):
    precommitToken: str
    seqNum: int

@typing.type_check_only
class Mutation(typing.TypedDict, total=False):
    ack: Ack
    delete: Delete
    insert: Write
    insertOrUpdate: Write
    replace: Write
    send: Send
    update: Write

@typing.type_check_only
class MutationGroup(typing.TypedDict, total=False):
    mutations: _list[Mutation]

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
class OptimizeRestoredDatabaseMetadata(typing.TypedDict, total=False):
    name: str
    progress: OperationProgress

@typing.type_check_only
class PartialResultSet(typing.TypedDict, total=False):
    chunkedValue: bool
    last: bool
    metadata: ResultSetMetadata
    precommitToken: MultiplexedSessionPrecommitToken
    resumeToken: str
    stats: ResultSetStats
    values: _list[typing.Any]

@typing.type_check_only
class Partition(typing.TypedDict, total=False):
    partitionToken: str

@typing.type_check_only
class PartitionEndRecord(typing.TypedDict, total=False):
    endTimestamp: str
    partitionToken: str
    recordSequence: str

@typing.type_check_only
class PartitionEventRecord(typing.TypedDict, total=False):
    commitTimestamp: str
    moveInEvents: _list[MoveInEvent]
    moveOutEvents: _list[MoveOutEvent]
    partitionToken: str
    recordSequence: str

@typing.type_check_only
class PartitionOptions(typing.TypedDict, total=False):
    maxPartitions: str
    partitionSizeBytes: str

@typing.type_check_only
class PartitionQueryRequest(typing.TypedDict, total=False):
    paramTypes: dict[str, typing.Any]
    params: dict[str, typing.Any]
    partitionOptions: PartitionOptions
    sql: str
    transaction: TransactionSelector

@typing.type_check_only
class PartitionReadRequest(typing.TypedDict, total=False):
    columns: _list[str]
    index: str
    keySet: KeySet
    partitionOptions: PartitionOptions
    table: str
    transaction: TransactionSelector

@typing.type_check_only
class PartitionResponse(typing.TypedDict, total=False):
    partitions: _list[Partition]
    transaction: Transaction

@typing.type_check_only
class PartitionStartRecord(typing.TypedDict, total=False):
    partitionTokens: _list[str]
    recordSequence: str
    startTimestamp: str

@typing.type_check_only
class PartitionedDml(typing.TypedDict, total=False): ...

@typing.type_check_only
class PlanNode(typing.TypedDict, total=False):
    childLinks: _list[ChildLink]
    displayName: str
    executionStats: dict[str, typing.Any]
    index: int
    kind: typing.Literal["KIND_UNSPECIFIED", "RELATIONAL", "SCALAR"]
    metadata: dict[str, typing.Any]
    shortRepresentation: ShortRepresentation

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrefixNode(typing.TypedDict, total=False):
    dataSourceNode: bool
    depth: int
    endIndex: int
    startIndex: int
    word: str

@typing.type_check_only
class QueryAdvisorResult(typing.TypedDict, total=False):
    indexAdvice: _list[IndexAdvice]

@typing.type_check_only
class QueryOptions(typing.TypedDict, total=False):
    optimizerStatisticsPackage: str
    optimizerVersion: str

@typing.type_check_only
class QueryPlan(typing.TypedDict, total=False):
    planNodes: _list[PlanNode]
    queryAdvice: QueryAdvisorResult

@typing.type_check_only
class QuorumInfo(typing.TypedDict, total=False):
    etag: str
    initiator: typing.Literal["INITIATOR_UNSPECIFIED", "GOOGLE", "USER"]
    quorumType: QuorumType
    startTime: str

@typing.type_check_only
class QuorumType(typing.TypedDict, total=False):
    dualRegion: DualRegionQuorum
    singleRegion: SingleRegionQuorum

@typing.type_check_only
class ReadOnly(typing.TypedDict, total=False):
    exactStaleness: str
    maxStaleness: str
    minReadTimestamp: str
    readTimestamp: str
    returnReadTimestamp: bool
    strong: bool

@typing.type_check_only
class ReadRequest(typing.TypedDict, total=False):
    columns: _list[str]
    dataBoostEnabled: bool
    directedReadOptions: DirectedReadOptions
    index: str
    keySet: KeySet
    limit: str
    lockHint: typing.Literal[
        "LOCK_HINT_UNSPECIFIED", "LOCK_HINT_SHARED", "LOCK_HINT_EXCLUSIVE"
    ]
    orderBy: typing.Literal[
        "ORDER_BY_UNSPECIFIED", "ORDER_BY_PRIMARY_KEY", "ORDER_BY_NO_ORDER"
    ]
    partitionToken: str
    requestOptions: RequestOptions
    resumeToken: str
    table: str
    transaction: TransactionSelector

@typing.type_check_only
class ReadWrite(typing.TypedDict, total=False):
    multiplexedSessionPreviousTransactionId: str
    readLockMode: typing.Literal[
        "READ_LOCK_MODE_UNSPECIFIED", "PESSIMISTIC", "OPTIMISTIC"
    ]

@typing.type_check_only
class ReplicaComputeCapacity(typing.TypedDict, total=False):
    nodeCount: int
    processingUnits: int
    replicaSelection: InstanceReplicaSelection

@typing.type_check_only
class ReplicaInfo(typing.TypedDict, total=False):
    defaultLeaderLocation: bool
    location: str
    type: typing.Literal["TYPE_UNSPECIFIED", "READ_WRITE", "READ_ONLY", "WITNESS"]

@typing.type_check_only
class ReplicaSelection(typing.TypedDict, total=False):
    location: str
    type: typing.Literal["TYPE_UNSPECIFIED", "READ_WRITE", "READ_ONLY"]

@typing.type_check_only
class RequestOptions(typing.TypedDict, total=False):
    clientContext: ClientContext
    priority: typing.Literal[
        "PRIORITY_UNSPECIFIED", "PRIORITY_LOW", "PRIORITY_MEDIUM", "PRIORITY_HIGH"
    ]
    requestTag: str
    transactionTag: str

@typing.type_check_only
class RestoreDatabaseEncryptionConfig(typing.TypedDict, total=False):
    encryptionType: typing.Literal[
        "ENCRYPTION_TYPE_UNSPECIFIED",
        "USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION",
        "GOOGLE_DEFAULT_ENCRYPTION",
        "CUSTOMER_MANAGED_ENCRYPTION",
    ]
    kmsKeyName: str
    kmsKeyNames: _list[str]

@typing.type_check_only
class RestoreDatabaseMetadata(typing.TypedDict, total=False):
    backupInfo: BackupInfo
    cancelTime: str
    name: str
    optimizeDatabaseOperationName: str
    progress: OperationProgress
    sourceType: typing.Literal["TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class RestoreDatabaseRequest(typing.TypedDict, total=False):
    backup: str
    databaseId: str
    encryptionConfig: RestoreDatabaseEncryptionConfig

@typing.type_check_only
class RestoreInfo(typing.TypedDict, total=False):
    backupInfo: BackupInfo
    sourceType: typing.Literal["TYPE_UNSPECIFIED", "BACKUP"]

@typing.type_check_only
class ResultSet(typing.TypedDict, total=False):
    metadata: ResultSetMetadata
    precommitToken: MultiplexedSessionPrecommitToken
    rows: _list[_list[typing.Any]]
    stats: ResultSetStats

@typing.type_check_only
class ResultSetMetadata(typing.TypedDict, total=False):
    rowType: StructType
    transaction: Transaction
    undeclaredParameters: StructType

@typing.type_check_only
class ResultSetStats(typing.TypedDict, total=False):
    queryPlan: QueryPlan
    queryStats: dict[str, typing.Any]
    rowCountExact: str
    rowCountLowerBound: str

@typing.type_check_only
class RollbackRequest(typing.TypedDict, total=False):
    transactionId: str

@typing.type_check_only
class Scan(typing.TypedDict, total=False):
    details: dict[str, typing.Any]
    endTime: str
    name: str
    scanData: ScanData
    startTime: str

@typing.type_check_only
class ScanData(typing.TypedDict, total=False):
    data: VisualizationData
    endTime: str
    startTime: str

@typing.type_check_only
class Send(typing.TypedDict, total=False):
    deliverTime: str
    key: _list[typing.Any]
    payload: typing.Any
    queue: str

@typing.type_check_only
class Session(typing.TypedDict, total=False):
    approximateLastUseTime: str
    createTime: str
    creatorRole: str
    labels: dict[str, typing.Any]
    multiplexed: bool
    name: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShortRepresentation(typing.TypedDict, total=False):
    description: str
    subqueries: dict[str, typing.Any]

@typing.type_check_only
class SingleRegionQuorum(typing.TypedDict, total=False):
    servingLocation: str

@typing.type_check_only
class SplitPoints(typing.TypedDict, total=False):
    expireTime: str
    index: str
    keys: _list[Key]
    table: str

@typing.type_check_only
class Statement(typing.TypedDict, total=False):
    paramTypes: dict[str, typing.Any]
    params: dict[str, typing.Any]
    sql: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructType(typing.TypedDict, total=False):
    fields: _list[Field]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Transaction(typing.TypedDict, total=False):
    id: str
    precommitToken: MultiplexedSessionPrecommitToken
    readTimestamp: str

@typing.type_check_only
class TransactionOptions(typing.TypedDict, total=False):
    excludeTxnFromChangeStreams: bool
    isolationLevel: typing.Literal[
        "ISOLATION_LEVEL_UNSPECIFIED", "SERIALIZABLE", "REPEATABLE_READ"
    ]
    partitionedDml: PartitionedDml
    readOnly: ReadOnly
    readWrite: ReadWrite

@typing.type_check_only
class TransactionSelector(typing.TypedDict, total=False):
    begin: TransactionOptions
    id: str
    singleUse: TransactionOptions

@typing.type_check_only
class Type(typing.TypedDict, total=False):
    arrayElementType: Type
    code: typing.Literal[
        "TYPE_CODE_UNSPECIFIED",
        "BOOL",
        "INT64",
        "FLOAT64",
        "FLOAT32",
        "TIMESTAMP",
        "DATE",
        "STRING",
        "BYTES",
        "ARRAY",
        "STRUCT",
        "NUMERIC",
        "JSON",
        "PROTO",
        "ENUM",
        "INTERVAL",
        "UUID",
    ]
    protoTypeFqn: str
    structType: StructType
    typeAnnotation: typing.Literal[
        "TYPE_ANNOTATION_CODE_UNSPECIFIED", "PG_NUMERIC", "PG_JSONB", "PG_OID"
    ]

@typing.type_check_only
class UpdateDatabaseDdlMetadata(typing.TypedDict, total=False):
    actions: _list[DdlStatementActionInfo]
    commitTimestamps: _list[str]
    database: str
    progress: _list[OperationProgress]
    statements: _list[str]
    throttled: bool

@typing.type_check_only
class UpdateDatabaseDdlRequest(typing.TypedDict, total=False):
    operationId: str
    protoDescriptors: str
    statements: _list[str]

@typing.type_check_only
class UpdateDatabaseMetadata(typing.TypedDict, total=False):
    cancelTime: str
    progress: OperationProgress
    request: UpdateDatabaseRequest

@typing.type_check_only
class UpdateDatabaseRequest(typing.TypedDict, total=False):
    database: Database
    updateMask: str

@typing.type_check_only
class UpdateInstanceConfigMetadata(typing.TypedDict, total=False):
    cancelTime: str
    instanceConfig: InstanceConfig
    progress: InstanceOperationProgress

@typing.type_check_only
class UpdateInstanceConfigRequest(typing.TypedDict, total=False):
    instanceConfig: InstanceConfig
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class UpdateInstanceMetadata(typing.TypedDict, total=False):
    cancelTime: str
    endTime: str
    expectedFulfillmentPeriod: typing.Literal[
        "FULFILLMENT_PERIOD_UNSPECIFIED",
        "FULFILLMENT_PERIOD_NORMAL",
        "FULFILLMENT_PERIOD_EXTENDED",
    ]
    instance: Instance
    startTime: str

@typing.type_check_only
class UpdateInstancePartitionMetadata(typing.TypedDict, total=False):
    cancelTime: str
    endTime: str
    instancePartition: InstancePartition
    startTime: str

@typing.type_check_only
class UpdateInstancePartitionRequest(typing.TypedDict, total=False):
    fieldMask: str
    instancePartition: InstancePartition

@typing.type_check_only
class UpdateInstanceRequest(typing.TypedDict, total=False):
    fieldMask: str
    instance: Instance

@typing.type_check_only
class VisualizationData(typing.TypedDict, total=False):
    dataSourceEndToken: str
    dataSourceSeparatorToken: str
    diagnosticMessages: _list[DiagnosticMessage]
    endKeyStrings: _list[str]
    hasPii: bool
    indexedKeys: _list[str]
    keySeparator: str
    keyUnit: typing.Literal["KEY_UNIT_UNSPECIFIED", "KEY", "CHUNK"]
    metrics: _list[Metric]
    prefixNodes: _list[PrefixNode]

@typing.type_check_only
class Write(typing.TypedDict, total=False):
    columns: _list[str]
    table: str
    values: _list[_list[typing.Any]]
