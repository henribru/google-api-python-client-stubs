import typing

import typing_extensions
@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    createTime: str
    database: str
    encryptionInfo: EncryptionInfo
    expireTime: str
    name: str
    referencingDatabases: typing.List[str]
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
    session: typing.List[Session]

@typing.type_check_only
class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    options: TransactionOptions

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class ChildLink(typing_extensions.TypedDict, total=False):
    childIndex: int
    type: str
    variable: str

@typing.type_check_only
class CommitRequest(typing_extensions.TypedDict, total=False):
    mutations: typing.List[Mutation]
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
    encryptionConfig: EncryptionConfig
    extraStatements: typing.List[str]

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
    earliestVersionTime: str
    encryptionConfig: EncryptionConfig
    encryptionInfo: typing.List[EncryptionInfo]
    name: str
    restoreInfo: RestoreInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "READY_OPTIMIZING"
    ]
    versionRetentionPeriod: str

@typing.type_check_only
class Delete(typing_extensions.TypedDict, total=False):
    keySet: KeySet
    table: str

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
    seqno: str
    statements: typing.List[Statement]
    transaction: TransactionSelector

@typing.type_check_only
class ExecuteBatchDmlResponse(typing_extensions.TypedDict, total=False):
    resultSets: typing.List[ResultSet]
    status: Status

@typing.type_check_only
class ExecuteSqlRequest(typing_extensions.TypedDict, total=False):
    paramTypes: typing.Dict[str, typing.Any]
    params: typing.Dict[str, typing.Any]
    partitionToken: str
    queryMode: typing_extensions.Literal["NORMAL", "PLAN", "PROFILE"]
    queryOptions: QueryOptions
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
class GetDatabaseDdlResponse(typing_extensions.TypedDict, total=False):
    statements: typing.List[str]

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    config: str
    displayName: str
    endpointUris: typing.List[str]
    labels: typing.Dict[str, typing.Any]
    name: str
    nodeCount: int
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]

@typing.type_check_only
class InstanceConfig(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    replicas: typing.List[ReplicaInfo]

@typing.type_check_only
class KeyRange(typing_extensions.TypedDict, total=False):
    endClosed: typing.List[typing.Any]
    endOpen: typing.List[typing.Any]
    startClosed: typing.List[typing.Any]
    startOpen: typing.List[typing.Any]

@typing.type_check_only
class KeySet(typing_extensions.TypedDict, total=False):
    all: bool
    keys: typing.List[list]
    ranges: typing.List[KeyRange]

@typing.type_check_only
class ListBackupOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: typing.List[Backup]
    nextPageToken: str

@typing.type_check_only
class ListDatabaseOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListDatabasesResponse(typing_extensions.TypedDict, total=False):
    databases: typing.List[Database]
    nextPageToken: str

@typing.type_check_only
class ListInstanceConfigsResponse(typing_extensions.TypedDict, total=False):
    instanceConfigs: typing.List[InstanceConfig]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListSessionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sessions: typing.List[Session]

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
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
    values: typing.List[typing.Any]

@typing.type_check_only
class Partition(typing_extensions.TypedDict, total=False):
    partitionToken: str

@typing.type_check_only
class PartitionOptions(typing_extensions.TypedDict, total=False):
    maxPartitions: str
    partitionSizeBytes: str

@typing.type_check_only
class PartitionQueryRequest(typing_extensions.TypedDict, total=False):
    paramTypes: typing.Dict[str, typing.Any]
    params: typing.Dict[str, typing.Any]
    partitionOptions: PartitionOptions
    sql: str
    transaction: TransactionSelector

@typing.type_check_only
class PartitionReadRequest(typing_extensions.TypedDict, total=False):
    columns: typing.List[str]
    index: str
    keySet: KeySet
    partitionOptions: PartitionOptions
    table: str
    transaction: TransactionSelector

@typing.type_check_only
class PartitionResponse(typing_extensions.TypedDict, total=False):
    partitions: typing.List[Partition]
    transaction: Transaction

@typing.type_check_only
class PartitionedDml(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PlanNode(typing_extensions.TypedDict, total=False):
    childLinks: typing.List[ChildLink]
    displayName: str
    executionStats: typing.Dict[str, typing.Any]
    index: int
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "RELATIONAL", "SCALAR"]
    metadata: typing.Dict[str, typing.Any]
    shortRepresentation: ShortRepresentation

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class QueryOptions(typing_extensions.TypedDict, total=False):
    optimizerVersion: str

@typing.type_check_only
class QueryPlan(typing_extensions.TypedDict, total=False):
    planNodes: typing.List[PlanNode]

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
    columns: typing.List[str]
    index: str
    keySet: KeySet
    limit: str
    partitionToken: str
    resumeToken: str
    table: str
    transaction: TransactionSelector

@typing.type_check_only
class ReadWrite(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReplicaInfo(typing_extensions.TypedDict, total=False):
    defaultLeaderLocation: bool
    location: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "READ_WRITE", "READ_ONLY", "WITNESS"
    ]

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
class ResultSet(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ResultSetMetadata(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ResultSetStats(typing_extensions.TypedDict, total=False):
    queryPlan: QueryPlan
    queryStats: typing.Dict[str, typing.Any]
    rowCountExact: str
    rowCountLowerBound: str

@typing.type_check_only
class RollbackRequest(typing_extensions.TypedDict, total=False):
    transactionId: str

@typing.type_check_only
class Session(typing_extensions.TypedDict, total=False):
    approximateLastUseTime: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShortRepresentation(typing_extensions.TypedDict, total=False):
    description: str
    subqueries: typing.Dict[str, typing.Any]

@typing.type_check_only
class Statement(typing_extensions.TypedDict, total=False):
    paramTypes: typing.Dict[str, typing.Any]
    params: typing.Dict[str, typing.Any]
    sql: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructType(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

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
class Type(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class UpdateDatabaseDdlMetadata(typing_extensions.TypedDict, total=False):
    commitTimestamps: typing.List[str]
    database: str
    statements: typing.List[str]
    throttled: bool

@typing.type_check_only
class UpdateDatabaseDdlRequest(typing_extensions.TypedDict, total=False):
    operationId: str
    statements: typing.List[str]

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
class Write(typing_extensions.TypedDict, total=False):
    columns: typing.List[str]
    table: str
    values: typing.List[list]
