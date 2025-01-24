import typing

import typing_extensions

_list = list

@typing.type_check_only
class AppendOnly(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AvroFileFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BackfillAllStrategy(typing_extensions.TypedDict, total=False):
    mysqlExcludedObjects: MysqlRdbms
    oracleExcludedObjects: OracleRdbms
    postgresqlExcludedObjects: PostgresqlRdbms
    sqlServerExcludedObjects: SqlServerRdbms

@typing.type_check_only
class BackfillJob(typing_extensions.TypedDict, total=False):
    errors: _list[Error]
    lastEndTime: str
    lastStartTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NOT_STARTED",
        "PENDING",
        "ACTIVE",
        "STOPPED",
        "FAILED",
        "COMPLETED",
        "UNSUPPORTED",
    ]
    trigger: typing_extensions.Literal["TRIGGER_UNSPECIFIED", "AUTOMATIC", "MANUAL"]

@typing.type_check_only
class BackfillNoneStrategy(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BigQueryDestinationConfig(typing_extensions.TypedDict, total=False):
    appendOnly: AppendOnly
    dataFreshness: str
    merge: Merge
    singleTargetDataset: SingleTargetDataset
    sourceHierarchyDatasets: SourceHierarchyDatasets

@typing.type_check_only
class BigQueryProfile(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BinaryLogParser(typing_extensions.TypedDict, total=False):
    logFileDirectories: LogFileDirectories
    oracleAsmLogFileAccess: OracleAsmLogFileAccess

@typing.type_check_only
class BinaryLogPosition(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CdcStrategy(typing_extensions.TypedDict, total=False):
    mostRecentStartPosition: MostRecentStartPosition
    nextAvailableStartPosition: NextAvailableStartPosition
    specificStartPosition: SpecificStartPosition

@typing.type_check_only
class ConnectionProfile(typing_extensions.TypedDict, total=False):
    bigqueryProfile: BigQueryProfile
    createTime: str
    displayName: str
    forwardSshConnectivity: ForwardSshTunnelConnectivity
    gcsProfile: GcsProfile
    labels: dict[str, typing.Any]
    mysqlProfile: MysqlProfile
    name: str
    oracleProfile: OracleProfile
    postgresqlProfile: PostgresqlProfile
    privateConnectivity: PrivateConnectivity
    sqlServerProfile: SqlServerProfile
    staticServiceIpConnectivity: StaticServiceIpConnectivity
    updateTime: str

@typing.type_check_only
class DatasetTemplate(typing_extensions.TypedDict, total=False):
    datasetIdPrefix: str
    kmsKeyName: str
    location: str

@typing.type_check_only
class DestinationConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestinationConfig: BigQueryDestinationConfig
    destinationConnectionProfile: str
    gcsDestinationConfig: GcsDestinationConfig

@typing.type_check_only
class DiscoverConnectionProfileRequest(typing_extensions.TypedDict, total=False):
    connectionProfile: ConnectionProfile
    connectionProfileName: str
    fullHierarchy: bool
    hierarchyDepth: int
    mysqlRdbms: MysqlRdbms
    oracleRdbms: OracleRdbms
    postgresqlRdbms: PostgresqlRdbms
    sqlServerRdbms: SqlServerRdbms

@typing.type_check_only
class DiscoverConnectionProfileResponse(typing_extensions.TypedDict, total=False):
    mysqlRdbms: MysqlRdbms
    oracleRdbms: OracleRdbms
    postgresqlRdbms: PostgresqlRdbms
    sqlServerRdbms: SqlServerRdbms

@typing.type_check_only
class DropLargeObjects(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    errorTime: str
    errorUuid: str
    message: str
    reason: str

@typing.type_check_only
class FetchStaticIpsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    staticIps: _list[str]

@typing.type_check_only
class ForwardSshTunnelConnectivity(typing_extensions.TypedDict, total=False):
    hostname: str
    password: str
    port: int
    privateKey: str
    username: str

@typing.type_check_only
class GcsDestinationConfig(typing_extensions.TypedDict, total=False):
    avroFileFormat: AvroFileFormat
    fileRotationInterval: str
    fileRotationMb: int
    jsonFileFormat: JsonFileFormat
    path: str

@typing.type_check_only
class GcsProfile(typing_extensions.TypedDict, total=False):
    bucket: str
    rootPath: str

@typing.type_check_only
class Gtid(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class JsonFileFormat(typing_extensions.TypedDict, total=False):
    compression: typing_extensions.Literal[
        "JSON_COMPRESSION_UNSPECIFIED", "NO_COMPRESSION", "GZIP"
    ]
    schemaFileFormat: typing_extensions.Literal[
        "SCHEMA_FILE_FORMAT_UNSPECIFIED", "NO_SCHEMA_FILE", "AVRO_SCHEMA_FILE"
    ]

@typing.type_check_only
class ListConnectionProfilesResponse(typing_extensions.TypedDict, total=False):
    connectionProfiles: _list[ConnectionProfile]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListPrivateConnectionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    privateConnections: _list[PrivateConnection]
    unreachable: _list[str]

@typing.type_check_only
class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    routes: _list[Route]
    unreachable: _list[str]

@typing.type_check_only
class ListStreamObjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    streamObjects: _list[StreamObject]

@typing.type_check_only
class ListStreamsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    streams: _list[Stream]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogFileDirectories(typing_extensions.TypedDict, total=False):
    archivedLogDirectory: str
    onlineLogDirectory: str

@typing.type_check_only
class LogMiner(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LookupStreamObjectRequest(typing_extensions.TypedDict, total=False):
    sourceObjectIdentifier: SourceObjectIdentifier

@typing.type_check_only
class Merge(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MostRecentStartPosition(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MysqlColumn(typing_extensions.TypedDict, total=False):
    collation: str
    column: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class MysqlDatabase(typing_extensions.TypedDict, total=False):
    database: str
    mysqlTables: _list[MysqlTable]

@typing.type_check_only
class MysqlLogPosition(typing_extensions.TypedDict, total=False):
    logFile: str
    logPosition: int

@typing.type_check_only
class MysqlObjectIdentifier(typing_extensions.TypedDict, total=False):
    database: str
    table: str

@typing.type_check_only
class MysqlProfile(typing_extensions.TypedDict, total=False):
    hostname: str
    password: str
    port: int
    sslConfig: MysqlSslConfig
    username: str

@typing.type_check_only
class MysqlRdbms(typing_extensions.TypedDict, total=False):
    mysqlDatabases: _list[MysqlDatabase]

@typing.type_check_only
class MysqlSourceConfig(typing_extensions.TypedDict, total=False):
    binaryLogPosition: BinaryLogPosition
    excludeObjects: MysqlRdbms
    gtid: Gtid
    includeObjects: MysqlRdbms
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int

@typing.type_check_only
class MysqlSslConfig(typing_extensions.TypedDict, total=False):
    caCertificate: str
    caCertificateSet: bool
    clientCertificate: str
    clientCertificateSet: bool
    clientKey: str
    clientKeySet: bool

@typing.type_check_only
class MysqlTable(typing_extensions.TypedDict, total=False):
    mysqlColumns: _list[MysqlColumn]
    table: str

@typing.type_check_only
class NextAvailableStartPosition(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    validationResult: ValidationResult
    verb: str

@typing.type_check_only
class OracleAsmConfig(typing_extensions.TypedDict, total=False):
    asmService: str
    connectionAttributes: dict[str, typing.Any]
    hostname: str
    oracleSslConfig: OracleSslConfig
    password: str
    port: int
    username: str

@typing.type_check_only
class OracleAsmLogFileAccess(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class OracleColumn(typing_extensions.TypedDict, total=False):
    column: str
    dataType: str
    encoding: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class OracleObjectIdentifier(typing_extensions.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class OracleProfile(typing_extensions.TypedDict, total=False):
    connectionAttributes: dict[str, typing.Any]
    databaseService: str
    hostname: str
    oracleAsmConfig: OracleAsmConfig
    oracleSslConfig: OracleSslConfig
    password: str
    port: int
    secretManagerStoredPassword: str
    username: str

@typing.type_check_only
class OracleRdbms(typing_extensions.TypedDict, total=False):
    oracleSchemas: _list[OracleSchema]

@typing.type_check_only
class OracleSchema(typing_extensions.TypedDict, total=False):
    oracleTables: _list[OracleTable]
    schema: str

@typing.type_check_only
class OracleScnPosition(typing_extensions.TypedDict, total=False):
    scn: str

@typing.type_check_only
class OracleSourceConfig(typing_extensions.TypedDict, total=False):
    binaryLogParser: BinaryLogParser
    dropLargeObjects: DropLargeObjects
    excludeObjects: OracleRdbms
    includeObjects: OracleRdbms
    logMiner: LogMiner
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int
    streamLargeObjects: StreamLargeObjects

@typing.type_check_only
class OracleSslConfig(typing_extensions.TypedDict, total=False):
    caCertificate: str
    caCertificateSet: bool

@typing.type_check_only
class OracleTable(typing_extensions.TypedDict, total=False):
    oracleColumns: _list[OracleColumn]
    table: str

@typing.type_check_only
class PostgresqlColumn(typing_extensions.TypedDict, total=False):
    column: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class PostgresqlObjectIdentifier(typing_extensions.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class PostgresqlProfile(typing_extensions.TypedDict, total=False):
    database: str
    hostname: str
    password: str
    port: int
    sslConfig: PostgresqlSslConfig
    username: str

@typing.type_check_only
class PostgresqlRdbms(typing_extensions.TypedDict, total=False):
    postgresqlSchemas: _list[PostgresqlSchema]

@typing.type_check_only
class PostgresqlSchema(typing_extensions.TypedDict, total=False):
    postgresqlTables: _list[PostgresqlTable]
    schema: str

@typing.type_check_only
class PostgresqlSourceConfig(typing_extensions.TypedDict, total=False):
    excludeObjects: PostgresqlRdbms
    includeObjects: PostgresqlRdbms
    maxConcurrentBackfillTasks: int
    publication: str
    replicationSlot: str

@typing.type_check_only
class PostgresqlSslConfig(typing_extensions.TypedDict, total=False):
    serverAndClientVerification: ServerAndClientVerification
    serverVerification: ServerVerification

@typing.type_check_only
class PostgresqlTable(typing_extensions.TypedDict, total=False):
    postgresqlColumns: _list[PostgresqlColumn]
    table: str

@typing.type_check_only
class PrivateConnection(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    error: Error
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "CREATED",
        "FAILED",
        "DELETING",
        "FAILED_TO_DELETE",
    ]
    updateTime: str
    vpcPeeringConfig: VpcPeeringConfig

@typing.type_check_only
class PrivateConnectivity(typing_extensions.TypedDict, total=False):
    privateConnection: str

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    createTime: str
    destinationAddress: str
    destinationPort: int
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class RunStreamRequest(typing_extensions.TypedDict, total=False):
    cdcStrategy: CdcStrategy
    force: bool

@typing.type_check_only
class ServerAndClientVerification(typing_extensions.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str

@typing.type_check_only
class ServerVerification(typing_extensions.TypedDict, total=False):
    caCertificate: str

@typing.type_check_only
class SingleTargetDataset(typing_extensions.TypedDict, total=False):
    datasetId: str

@typing.type_check_only
class SourceConfig(typing_extensions.TypedDict, total=False):
    mysqlSourceConfig: MysqlSourceConfig
    oracleSourceConfig: OracleSourceConfig
    postgresqlSourceConfig: PostgresqlSourceConfig
    sourceConnectionProfile: str
    sqlServerSourceConfig: SqlServerSourceConfig

@typing.type_check_only
class SourceHierarchyDatasets(typing_extensions.TypedDict, total=False):
    datasetTemplate: DatasetTemplate

@typing.type_check_only
class SourceObjectIdentifier(typing_extensions.TypedDict, total=False):
    mysqlIdentifier: MysqlObjectIdentifier
    oracleIdentifier: OracleObjectIdentifier
    postgresqlIdentifier: PostgresqlObjectIdentifier
    sqlServerIdentifier: SqlServerObjectIdentifier

@typing.type_check_only
class SpecificStartPosition(typing_extensions.TypedDict, total=False):
    mysqlLogPosition: MysqlLogPosition
    oracleScnPosition: OracleScnPosition
    sqlServerLsnPosition: SqlServerLsnPosition

@typing.type_check_only
class SqlServerChangeTables(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SqlServerColumn(typing_extensions.TypedDict, total=False):
    column: str
    dataType: str
    length: int
    nullable: bool
    ordinalPosition: int
    precision: int
    primaryKey: bool
    scale: int

@typing.type_check_only
class SqlServerLsnPosition(typing_extensions.TypedDict, total=False):
    lsn: str

@typing.type_check_only
class SqlServerObjectIdentifier(typing_extensions.TypedDict, total=False):
    schema: str
    table: str

@typing.type_check_only
class SqlServerProfile(typing_extensions.TypedDict, total=False):
    database: str
    hostname: str
    password: str
    port: int
    username: str

@typing.type_check_only
class SqlServerRdbms(typing_extensions.TypedDict, total=False):
    schemas: _list[SqlServerSchema]

@typing.type_check_only
class SqlServerSchema(typing_extensions.TypedDict, total=False):
    schema: str
    tables: _list[SqlServerTable]

@typing.type_check_only
class SqlServerSourceConfig(typing_extensions.TypedDict, total=False):
    changeTables: SqlServerChangeTables
    excludeObjects: SqlServerRdbms
    includeObjects: SqlServerRdbms
    maxConcurrentBackfillTasks: int
    maxConcurrentCdcTasks: int
    transactionLogs: SqlServerTransactionLogs

@typing.type_check_only
class SqlServerTable(typing_extensions.TypedDict, total=False):
    columns: _list[SqlServerColumn]
    table: str

@typing.type_check_only
class SqlServerTransactionLogs(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StartBackfillJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StartBackfillJobResponse(typing_extensions.TypedDict, total=False):
    object: StreamObject

@typing.type_check_only
class StaticServiceIpConnectivity(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopBackfillJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StopBackfillJobResponse(typing_extensions.TypedDict, total=False):
    object: StreamObject

@typing.type_check_only
class Stream(typing_extensions.TypedDict, total=False):
    backfillAll: BackfillAllStrategy
    backfillNone: BackfillNoneStrategy
    createTime: str
    customerManagedEncryptionKey: str
    destinationConfig: DestinationConfig
    displayName: str
    errors: _list[Error]
    labels: dict[str, typing.Any]
    lastRecoveryTime: str
    name: str
    sourceConfig: SourceConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NOT_STARTED",
        "RUNNING",
        "PAUSED",
        "MAINTENANCE",
        "FAILED",
        "FAILED_PERMANENTLY",
        "STARTING",
        "DRAINING",
    ]
    updateTime: str

@typing.type_check_only
class StreamLargeObjects(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StreamObject(typing_extensions.TypedDict, total=False):
    backfillJob: BackfillJob
    createTime: str
    displayName: str
    errors: _list[Error]
    name: str
    sourceObject: SourceObjectIdentifier
    updateTime: str

@typing.type_check_only
class Validation(typing_extensions.TypedDict, total=False):
    code: str
    description: str
    message: _list[ValidationMessage]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_EXECUTED", "FAILED", "PASSED", "WARNING"
    ]

@typing.type_check_only
class ValidationMessage(typing_extensions.TypedDict, total=False):
    code: str
    level: typing_extensions.Literal["LEVEL_UNSPECIFIED", "WARNING", "ERROR"]
    message: str
    metadata: dict[str, typing.Any]

@typing.type_check_only
class ValidationResult(typing_extensions.TypedDict, total=False):
    validations: _list[Validation]

@typing.type_check_only
class VpcPeeringConfig(typing_extensions.TypedDict, total=False):
    subnet: str
    vpc: str
