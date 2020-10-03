import typing

import typing_extensions

class ResultSetStats(typing_extensions.TypedDict, total=False):
    rowCountLowerBound: str
    rowCountExact: str
    queryStats: typing.Dict[str, typing.Any]
    queryPlan: QueryPlan

class Delete(typing_extensions.TypedDict, total=False):
    table: str
    keySet: KeySet

class ResultSet(typing_extensions.TypedDict, total=False):
    rows: typing.List[list]
    metadata: ResultSetMetadata
    stats: ResultSetStats

class BeginTransactionRequest(typing_extensions.TypedDict, total=False):
    options: TransactionOptions

class Session(typing_extensions.TypedDict, total=False):
    name: str
    labels: typing.Dict[str, typing.Any]
    approximateLastUseTime: str
    createTime: str

class Type(typing.Dict[str, typing.Any]): ...

class Instance(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    config: str
    labels: typing.Dict[str, typing.Any]
    endpointUris: typing.List[str]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    nodeCount: int

class KeySet(typing_extensions.TypedDict, total=False):
    keys: typing.List[list]
    ranges: typing.List[KeyRange]
    all: bool

class ListSessionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sessions: typing.List[Session]

class RollbackRequest(typing_extensions.TypedDict, total=False):
    transactionId: str

class ReadWrite(typing_extensions.TypedDict, total=False): ...

class Write(typing_extensions.TypedDict, total=False):
    table: str
    columns: typing.List[str]
    values: typing.List[list]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class Backup(typing_extensions.TypedDict, total=False):
    expireTime: str
    sizeBytes: str
    createTime: str
    name: str
    referencingDatabases: typing.List[str]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "READY"]
    database: str

class BackupInfo(typing_extensions.TypedDict, total=False):
    backup: str
    sourceDatabase: str
    createTime: str

class PartitionOptions(typing_extensions.TypedDict, total=False):
    maxPartitions: str
    partitionSizeBytes: str

class BatchCreateSessionsRequest(typing_extensions.TypedDict, total=False):
    sessionCount: int
    sessionTemplate: Session

class ReplicaInfo(typing_extensions.TypedDict, total=False):
    location: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "READ_WRITE", "READ_ONLY", "WITNESS"
    ]
    defaultLeaderLocation: bool

class UpdateDatabaseDdlRequest(typing_extensions.TypedDict, total=False):
    operationId: str
    statements: typing.List[str]

class Statement(typing_extensions.TypedDict, total=False):
    paramTypes: typing.Dict[str, typing.Any]
    sql: str
    params: typing.Dict[str, typing.Any]

class ListInstanceConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    instanceConfigs: typing.List[InstanceConfig]

class TransactionSelector(typing_extensions.TypedDict, total=False):
    singleUse: TransactionOptions
    begin: TransactionOptions
    id: str

class CreateBackupMetadata(typing_extensions.TypedDict, total=False):
    progress: OperationProgress
    name: str
    database: str
    cancelTime: str

class CreateSessionRequest(typing_extensions.TypedDict, total=False):
    session: Session

class CreateInstanceRequest(typing_extensions.TypedDict, total=False):
    instance: Instance
    instanceId: str

class CommitResponse(typing_extensions.TypedDict, total=False):
    commitTimestamp: str

class UpdateInstanceRequest(typing_extensions.TypedDict, total=False):
    fieldMask: str
    instance: Instance

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class ChildLink(typing_extensions.TypedDict, total=False):
    type: str
    childIndex: int
    variable: str

class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    backups: typing.List[Backup]

class InstanceConfig(typing_extensions.TypedDict, total=False):
    name: str
    replicas: typing.List[ReplicaInfo]
    displayName: str

class OptimizeRestoredDatabaseMetadata(typing_extensions.TypedDict, total=False):
    progress: OperationProgress
    name: str

class Field(typing_extensions.TypedDict, total=False):
    name: str
    type: Type

class ListDatabasesResponse(typing_extensions.TypedDict, total=False):
    databases: typing.List[Database]
    nextPageToken: str

class UpdateInstanceMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    cancelTime: str
    instance: Instance

class GetDatabaseDdlResponse(typing_extensions.TypedDict, total=False):
    statements: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class ExecuteBatchDmlResponse(typing_extensions.TypedDict, total=False):
    resultSets: typing.List[ResultSet]
    status: Status

class Database(typing_extensions.TypedDict, total=False):
    name: str
    createTime: str
    restoreInfo: RestoreInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "READY_OPTIMIZING"
    ]

class PartitionedDml(typing_extensions.TypedDict, total=False): ...
class ResultSetMetadata(typing.Dict[str, typing.Any]): ...

class CreateDatabaseRequest(typing_extensions.TypedDict, total=False):
    extraStatements: typing.List[str]
    createStatement: str

class TransactionOptions(typing_extensions.TypedDict, total=False):
    readOnly: ReadOnly
    readWrite: ReadWrite
    partitionedDml: PartitionedDml

class ReadRequest(typing_extensions.TypedDict, total=False):
    keySet: KeySet
    table: str
    columns: typing.List[str]
    index: str
    partitionToken: str
    transaction: TransactionSelector
    resumeToken: str
    limit: str

class Mutation(typing_extensions.TypedDict, total=False):
    insertOrUpdate: Write
    delete: Delete
    replace: Write
    insert: Write
    update: Write

class RestoreDatabaseMetadata(typing_extensions.TypedDict, total=False):
    name: str
    cancelTime: str
    progress: OperationProgress
    backupInfo: BackupInfo
    optimizeDatabaseOperationName: str
    sourceType: typing_extensions.Literal["TYPE_UNSPECIFIED", "BACKUP"]

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    response: typing.Dict[str, typing.Any]
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str

class PartialResultSet(typing_extensions.TypedDict, total=False):
    stats: ResultSetStats
    chunkedValue: bool
    metadata: ResultSetMetadata
    resumeToken: str
    values: typing.List[typing.Any]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    role: str
    bindingId: str
    members: typing.List[str]

class CommitRequest(typing_extensions.TypedDict, total=False):
    mutations: typing.List[Mutation]
    singleUseTransaction: TransactionOptions
    transactionId: str

class Transaction(typing_extensions.TypedDict, total=False):
    id: str
    readTimestamp: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    expression: str
    description: str

class ListBackupOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class ExecuteSqlRequest(typing_extensions.TypedDict, total=False):
    queryOptions: QueryOptions
    partitionToken: str
    params: typing.Dict[str, typing.Any]
    seqno: str
    paramTypes: typing.Dict[str, typing.Any]
    sql: str
    transaction: TransactionSelector
    queryMode: typing_extensions.Literal["NORMAL", "PLAN", "PROFILE"]
    resumeToken: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class PartitionReadRequest(typing_extensions.TypedDict, total=False):
    index: str
    keySet: KeySet
    columns: typing.List[str]
    transaction: TransactionSelector
    partitionOptions: PartitionOptions
    table: str

class PartitionQueryRequest(typing_extensions.TypedDict, total=False):
    transaction: TransactionSelector
    sql: str
    paramTypes: typing.Dict[str, typing.Any]
    params: typing.Dict[str, typing.Any]
    partitionOptions: PartitionOptions

class PlanNode(typing_extensions.TypedDict, total=False):
    childLinks: typing.List[ChildLink]
    displayName: str
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "RELATIONAL", "SCALAR"]
    shortRepresentation: ShortRepresentation
    executionStats: typing.Dict[str, typing.Any]
    index: int
    metadata: typing.Dict[str, typing.Any]

class QueryPlan(typing_extensions.TypedDict, total=False):
    planNodes: typing.List[PlanNode]

class OperationProgress(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str
    progressPercent: int

class PartitionResponse(typing_extensions.TypedDict, total=False):
    partitions: typing.List[Partition]
    transaction: Transaction

class ListDatabaseOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class CreateInstanceMetadata(typing_extensions.TypedDict, total=False):
    startTime: str
    instance: Instance
    endTime: str
    cancelTime: str

class CreateDatabaseMetadata(typing_extensions.TypedDict, total=False):
    database: str

class ShortRepresentation(typing_extensions.TypedDict, total=False):
    subqueries: typing.Dict[str, typing.Any]
    description: str

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

class StructType(typing.Dict[str, typing.Any]): ...

class Partition(typing_extensions.TypedDict, total=False):
    partitionToken: str

class UpdateDatabaseDdlMetadata(typing_extensions.TypedDict, total=False):
    commitTimestamps: typing.List[str]
    database: str
    statements: typing.List[str]

class BatchCreateSessionsResponse(typing_extensions.TypedDict, total=False):
    session: typing.List[Session]

class RestoreInfo(typing_extensions.TypedDict, total=False):
    backupInfo: BackupInfo
    sourceType: typing_extensions.Literal["TYPE_UNSPECIFIED", "BACKUP"]

class QueryOptions(typing_extensions.TypedDict, total=False):
    optimizerVersion: str

class ExecuteBatchDmlRequest(typing_extensions.TypedDict, total=False):
    seqno: str
    transaction: TransactionSelector
    statements: typing.List[Statement]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class KeyRange(typing_extensions.TypedDict, total=False):
    endClosed: typing.List[typing.Any]
    startClosed: typing.List[typing.Any]
    endOpen: typing.List[typing.Any]
    startOpen: typing.List[typing.Any]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ReadOnly(typing_extensions.TypedDict, total=False):
    maxStaleness: str
    readTimestamp: str
    minReadTimestamp: str
    exactStaleness: str
    returnReadTimestamp: bool
    strong: bool

class RestoreDatabaseRequest(typing_extensions.TypedDict, total=False):
    databaseId: str
    backup: str
