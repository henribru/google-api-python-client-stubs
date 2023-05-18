import typing

import typing_extensions

_list = list

@typing.type_check_only
class AlloyDbConnectionProfile(typing_extensions.TypedDict, total=False):
    clusterId: str
    settings: AlloyDbSettings

@typing.type_check_only
class AlloyDbSettings(typing_extensions.TypedDict, total=False):
    encryptionConfig: EncryptionConfig
    initialUser: UserPassword
    labels: dict[str, typing.Any]
    primaryInstanceSettings: PrimaryInstanceSettings
    vpcNetwork: str

@typing.type_check_only
class ApplyConversionWorkspaceRequest(typing_extensions.TypedDict, total=False):
    connectionProfile: str
    filter: str

@typing.type_check_only
class ApplyJobDetails(typing_extensions.TypedDict, total=False):
    connectionProfile: str
    filter: str

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
class BackgroundJobLogEntry(typing_extensions.TypedDict, total=False):
    applyJobDetails: ApplyJobDetails
    completionComment: str
    completionState: typing_extensions.Literal[
        "JOB_COMPLETION_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"
    ]
    convertJobDetails: ConvertJobDetails
    finishTime: str
    id: str
    importRulesJobDetails: ImportRulesJobDetails
    jobType: typing_extensions.Literal[
        "BACKGROUND_JOB_TYPE_UNSPECIFIED",
        "BACKGROUND_JOB_TYPE_SOURCE_SEED",
        "BACKGROUND_JOB_TYPE_CONVERT",
        "BACKGROUND_JOB_TYPE_APPLY_DESTINATION",
        "BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE",
    ]
    requestAutocommit: bool
    seedJobDetails: SeedJobDetails
    startTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudSqlConnectionProfile(typing_extensions.TypedDict, total=False):
    additionalPublicIp: str
    cloudSqlId: str
    privateIp: str
    publicIp: str
    settings: CloudSqlSettings

@typing.type_check_only
class CloudSqlSettings(typing_extensions.TypedDict, total=False):
    activationPolicy: typing_extensions.Literal[
        "SQL_ACTIVATION_POLICY_UNSPECIFIED", "ALWAYS", "NEVER"
    ]
    autoStorageIncrease: bool
    availabilityType: typing_extensions.Literal[
        "SQL_AVAILABILITY_TYPE_UNSPECIFIED", "ZONAL", "REGIONAL"
    ]
    cmekKeyName: str
    collation: str
    dataDiskSizeGb: str
    dataDiskType: typing_extensions.Literal[
        "SQL_DATA_DISK_TYPE_UNSPECIFIED", "PD_SSD", "PD_HDD"
    ]
    databaseFlags: dict[str, typing.Any]
    databaseVersion: typing_extensions.Literal[
        "SQL_DATABASE_VERSION_UNSPECIFIED",
        "MYSQL_5_6",
        "MYSQL_5_7",
        "POSTGRES_9_6",
        "POSTGRES_11",
        "POSTGRES_10",
        "MYSQL_8_0",
        "POSTGRES_12",
        "POSTGRES_13",
        "POSTGRES_14",
    ]
    ipConfig: SqlIpConfig
    rootPassword: str
    rootPasswordSet: bool
    secondaryZone: str
    sourceId: str
    storageAutoResizeLimit: str
    tier: str
    userLabels: dict[str, typing.Any]
    zone: str

@typing.type_check_only
class ColumnEntity(typing_extensions.TypedDict, total=False):
    array: bool
    arrayLength: int
    autoGenerated: bool
    charset: str
    collation: str
    comment: str
    customFeatures: dict[str, typing.Any]
    dataType: str
    defaultValue: str
    fractionalSecondsPrecision: int
    length: str
    name: str
    nullable: bool
    ordinalPosition: int
    precision: int
    scale: int
    setValues: _list[str]
    udt: bool

@typing.type_check_only
class CommitConversionWorkspaceRequest(typing_extensions.TypedDict, total=False):
    commitName: str

@typing.type_check_only
class ConnectionProfile(typing_extensions.TypedDict, total=False):
    alloydb: AlloyDbConnectionProfile
    cloudsql: CloudSqlConnectionProfile
    createTime: str
    displayName: str
    error: Status
    labels: dict[str, typing.Any]
    mysql: MySqlConnectionProfile
    name: str
    oracle: OracleConnectionProfile
    postgresql: PostgreSqlConnectionProfile
    provider: typing_extensions.Literal[
        "DATABASE_PROVIDER_UNSPECIFIED", "CLOUDSQL", "RDS", "AURORA", "ALLOYDB"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "DRAFT",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "DELETED",
        "FAILED",
    ]
    updateTime: str

@typing.type_check_only
class ConstraintEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    name: str
    referenceColumns: _list[str]
    referenceTable: str
    tableColumns: _list[str]
    tableName: str
    type: str

@typing.type_check_only
class ConversionWorkspace(typing_extensions.TypedDict, total=False):
    createTime: str
    destination: DatabaseEngineInfo
    displayName: str
    globalSettings: dict[str, typing.Any]
    hasUncommittedChanges: bool
    latestCommitId: str
    latestCommitTime: str
    name: str
    source: DatabaseEngineInfo
    updateTime: str

@typing.type_check_only
class ConversionWorkspaceInfo(typing_extensions.TypedDict, total=False):
    commitId: str
    name: str

@typing.type_check_only
class ConvertConversionWorkspaceRequest(typing_extensions.TypedDict, total=False):
    autoCommit: bool
    filter: str

@typing.type_check_only
class ConvertJobDetails(typing_extensions.TypedDict, total=False):
    filter: str

@typing.type_check_only
class DatabaseEngineInfo(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal[
        "DATABASE_ENGINE_UNSPECIFIED", "MYSQL", "POSTGRESQL", "ORACLE"
    ]
    version: str

@typing.type_check_only
class DatabaseEntity(typing_extensions.TypedDict, total=False):
    databaseFunction: FunctionEntity
    databasePackage: PackageEntity
    entityType: typing_extensions.Literal[
        "DATABASE_ENTITY_TYPE_UNSPECIFIED",
        "DATABASE_ENTITY_TYPE_SCHEMA",
        "DATABASE_ENTITY_TYPE_TABLE",
        "DATABASE_ENTITY_TYPE_COLUMN",
        "DATABASE_ENTITY_TYPE_CONSTRAINT",
        "DATABASE_ENTITY_TYPE_INDEX",
        "DATABASE_ENTITY_TYPE_TRIGGER",
        "DATABASE_ENTITY_TYPE_VIEW",
        "DATABASE_ENTITY_TYPE_SEQUENCE",
        "DATABASE_ENTITY_TYPE_STORED_PROCEDURE",
        "DATABASE_ENTITY_TYPE_FUNCTION",
        "DATABASE_ENTITY_TYPE_SYNONYM",
        "DATABASE_ENTITY_TYPE_DATABASE_PACKAGE",
        "DATABASE_ENTITY_TYPE_UDT",
        "DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW",
        "DATABASE_ENTITY_TYPE_DATABASE",
    ]
    mappings: _list[EntityMapping]
    parentEntity: str
    schema: SchemaEntity
    sequence: SequenceEntity
    shortName: str
    storedProcedure: StoredProcedureEntity
    synonym: SynonymEntity
    table: TableEntity
    tree: typing_extensions.Literal[
        "TREE_TYPE_UNSPECIFIED", "SOURCE", "DRAFT", "DESTINATION"
    ]
    view: ViewEntity

@typing.type_check_only
class DatabaseType(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal[
        "DATABASE_ENGINE_UNSPECIFIED", "MYSQL", "POSTGRESQL", "ORACLE"
    ]
    provider: typing_extensions.Literal[
        "DATABASE_PROVIDER_UNSPECIFIED", "CLOUDSQL", "RDS", "AURORA", "ALLOYDB"
    ]

@typing.type_check_only
class DescribeConversionWorkspaceRevisionsResponse(
    typing_extensions.TypedDict, total=False
):
    revisions: _list[ConversionWorkspace]

@typing.type_check_only
class DescribeDatabaseEntitiesResponse(typing_extensions.TypedDict, total=False):
    databaseEntities: _list[DatabaseEntity]
    nextPageToken: str

@typing.type_check_only
class DumpFlag(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class DumpFlags(typing_extensions.TypedDict, total=False):
    dumpFlags: _list[DumpFlag]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EntityMapping(typing_extensions.TypedDict, total=False):
    draftEntity: str
    draftType: typing_extensions.Literal[
        "DATABASE_ENTITY_TYPE_UNSPECIFIED",
        "DATABASE_ENTITY_TYPE_SCHEMA",
        "DATABASE_ENTITY_TYPE_TABLE",
        "DATABASE_ENTITY_TYPE_COLUMN",
        "DATABASE_ENTITY_TYPE_CONSTRAINT",
        "DATABASE_ENTITY_TYPE_INDEX",
        "DATABASE_ENTITY_TYPE_TRIGGER",
        "DATABASE_ENTITY_TYPE_VIEW",
        "DATABASE_ENTITY_TYPE_SEQUENCE",
        "DATABASE_ENTITY_TYPE_STORED_PROCEDURE",
        "DATABASE_ENTITY_TYPE_FUNCTION",
        "DATABASE_ENTITY_TYPE_SYNONYM",
        "DATABASE_ENTITY_TYPE_DATABASE_PACKAGE",
        "DATABASE_ENTITY_TYPE_UDT",
        "DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW",
        "DATABASE_ENTITY_TYPE_DATABASE",
    ]
    mappingLog: _list[EntityMappingLogEntry]
    sourceEntity: str
    sourceType: typing_extensions.Literal[
        "DATABASE_ENTITY_TYPE_UNSPECIFIED",
        "DATABASE_ENTITY_TYPE_SCHEMA",
        "DATABASE_ENTITY_TYPE_TABLE",
        "DATABASE_ENTITY_TYPE_COLUMN",
        "DATABASE_ENTITY_TYPE_CONSTRAINT",
        "DATABASE_ENTITY_TYPE_INDEX",
        "DATABASE_ENTITY_TYPE_TRIGGER",
        "DATABASE_ENTITY_TYPE_VIEW",
        "DATABASE_ENTITY_TYPE_SEQUENCE",
        "DATABASE_ENTITY_TYPE_STORED_PROCEDURE",
        "DATABASE_ENTITY_TYPE_FUNCTION",
        "DATABASE_ENTITY_TYPE_SYNONYM",
        "DATABASE_ENTITY_TYPE_DATABASE_PACKAGE",
        "DATABASE_ENTITY_TYPE_UDT",
        "DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW",
        "DATABASE_ENTITY_TYPE_DATABASE",
    ]

@typing.type_check_only
class EntityMappingLogEntry(typing_extensions.TypedDict, total=False):
    mappingComment: str
    ruleId: str
    ruleRevisionId: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
class FunctionEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    sqlCode: str

@typing.type_check_only
class GenerateSshScriptRequest(typing_extensions.TypedDict, total=False):
    vm: str
    vmCreationConfig: VmCreationConfig
    vmPort: int
    vmSelectionConfig: VmSelectionConfig

@typing.type_check_only
class GoogleCloudClouddmsV1OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ImportMappingRulesRequest(typing_extensions.TypedDict, total=False):
    autoCommit: bool
    rulesFiles: _list[RulesFile]
    rulesFormat: typing_extensions.Literal[
        "IMPORT_RULES_FILE_FORMAT_UNSPECIFIED",
        "IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE",
        "IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE",
    ]

@typing.type_check_only
class ImportRulesJobDetails(typing_extensions.TypedDict, total=False):
    fileFormat: typing_extensions.Literal[
        "IMPORT_RULES_FILE_FORMAT_UNSPECIFIED",
        "IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE",
        "IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE",
    ]
    files: _list[str]

@typing.type_check_only
class IndexEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    name: str
    tableColumns: _list[str]
    type: str
    unique: bool

@typing.type_check_only
class ListConnectionProfilesResponse(typing_extensions.TypedDict, total=False):
    connectionProfiles: _list[ConnectionProfile]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConversionWorkspacesResponse(typing_extensions.TypedDict, total=False):
    conversionWorkspaces: _list[ConversionWorkspace]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMigrationJobsResponse(typing_extensions.TypedDict, total=False):
    migrationJobs: _list[MigrationJob]
    nextPageToken: str
    unreachable: _list[str]

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
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MachineConfig(typing_extensions.TypedDict, total=False):
    cpuCount: int

@typing.type_check_only
class MigrationJob(typing_extensions.TypedDict, total=False):
    conversionWorkspace: ConversionWorkspaceInfo
    createTime: str
    destination: str
    destinationDatabase: DatabaseType
    displayName: str
    dumpFlags: DumpFlags
    dumpPath: str
    duration: str
    endTime: str
    error: Status
    filter: str
    labels: dict[str, typing.Any]
    name: str
    phase: typing_extensions.Literal[
        "PHASE_UNSPECIFIED",
        "FULL_DUMP",
        "CDC",
        "PROMOTE_IN_PROGRESS",
        "WAITING_FOR_SOURCE_WRITES_TO_STOP",
        "PREPARING_THE_DUMP",
    ]
    reverseSshConnectivity: ReverseSshConnectivity
    source: str
    sourceDatabase: DatabaseType
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "MAINTENANCE",
        "DRAFT",
        "CREATING",
        "NOT_STARTED",
        "RUNNING",
        "FAILED",
        "COMPLETED",
        "DELETING",
        "STOPPING",
        "STOPPED",
        "DELETED",
        "UPDATING",
        "STARTING",
        "RESTARTING",
        "RESUMING",
    ]
    staticIpConnectivity: StaticIpConnectivity
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ONE_TIME", "CONTINUOUS"]
    updateTime: str
    vpcPeeringConnectivity: VpcPeeringConnectivity

@typing.type_check_only
class MigrationJobVerificationError(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "CONNECTION_FAILURE",
        "AUTHENTICATION_FAILURE",
        "INVALID_CONNECTION_PROFILE_CONFIG",
        "VERSION_INCOMPATIBILITY",
        "CONNECTION_PROFILE_TYPES_INCOMPATIBILITY",
        "NO_PGLOGICAL_INSTALLED",
        "PGLOGICAL_NODE_ALREADY_EXISTS",
        "INVALID_WAL_LEVEL",
        "INVALID_SHARED_PRELOAD_LIBRARY",
        "INSUFFICIENT_MAX_REPLICATION_SLOTS",
        "INSUFFICIENT_MAX_WAL_SENDERS",
        "INSUFFICIENT_MAX_WORKER_PROCESSES",
        "UNSUPPORTED_EXTENSIONS",
        "UNSUPPORTED_MIGRATION_TYPE",
        "INVALID_RDS_LOGICAL_REPLICATION",
        "UNSUPPORTED_GTID_MODE",
        "UNSUPPORTED_TABLE_DEFINITION",
        "UNSUPPORTED_DEFINER",
        "CANT_RESTART_RUNNING_MIGRATION",
        "TABLES_WITH_LIMITED_SUPPORT",
        "UNSUPPORTED_DATABASE_LOCALE",
        "UNSUPPORTED_DATABASE_FDW_CONFIG",
        "ERROR_RDBMS",
    ]
    errorDetailMessage: str
    errorMessage: str

@typing.type_check_only
class MySqlConnectionProfile(typing_extensions.TypedDict, total=False):
    cloudSqlId: str
    host: str
    password: str
    passwordSet: bool
    port: int
    ssl: SslConfig
    username: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OracleConnectionProfile(typing_extensions.TypedDict, total=False):
    databaseService: str
    forwardSshConnectivity: ForwardSshTunnelConnectivity
    host: str
    password: str
    passwordSet: bool
    port: int
    privateConnectivity: PrivateConnectivity
    staticServiceIpConnectivity: StaticServiceIpConnectivity
    username: str

@typing.type_check_only
class PackageEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    packageBody: str
    packageSqlCode: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PostgreSqlConnectionProfile(typing_extensions.TypedDict, total=False):
    cloudSqlId: str
    host: str
    networkArchitecture: typing_extensions.Literal[
        "NETWORK_ARCHITECTURE_UNSPECIFIED",
        "NETWORK_ARCHITECTURE_OLD_CSQL_PRODUCER",
        "NETWORK_ARCHITECTURE_NEW_CSQL_PRODUCER",
    ]
    password: str
    passwordSet: bool
    port: int
    privateServiceConnectConnectivity: PrivateServiceConnectConnectivity
    ssl: SslConfig
    staticIpConnectivity: StaticIpConnectivity
    username: str

@typing.type_check_only
class PrimaryInstanceSettings(typing_extensions.TypedDict, total=False):
    databaseFlags: dict[str, typing.Any]
    id: str
    labels: dict[str, typing.Any]
    machineConfig: MachineConfig
    privateIp: str

@typing.type_check_only
class PrivateConnection(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    error: Status
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "CREATED",
        "FAILED",
        "DELETING",
        "FAILED_TO_DELETE",
        "DELETED",
    ]
    updateTime: str
    vpcPeeringConfig: VpcPeeringConfig

@typing.type_check_only
class PrivateConnectivity(typing_extensions.TypedDict, total=False):
    privateConnection: str

@typing.type_check_only
class PrivateServiceConnectConnectivity(typing_extensions.TypedDict, total=False):
    serviceAttachment: str

@typing.type_check_only
class PromoteMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestartMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResumeMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReverseSshConnectivity(typing_extensions.TypedDict, total=False):
    vm: str
    vmIp: str
    vmPort: int
    vpc: str

@typing.type_check_only
class RollbackConversionWorkspaceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RulesFile(typing_extensions.TypedDict, total=False):
    rulesContent: str
    rulesSourceFilename: str

@typing.type_check_only
class SchemaEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]

@typing.type_check_only
class SearchBackgroundJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[BackgroundJobLogEntry]

@typing.type_check_only
class SeedConversionWorkspaceRequest(typing_extensions.TypedDict, total=False):
    autoCommit: bool
    destinationConnectionProfile: str
    sourceConnectionProfile: str

@typing.type_check_only
class SeedJobDetails(typing_extensions.TypedDict, total=False):
    connectionProfile: str

@typing.type_check_only
class SequenceEntity(typing_extensions.TypedDict, total=False):
    cache: str
    customFeatures: dict[str, typing.Any]
    cycle: bool
    increment: str
    maxValue: str
    minValue: str
    startValue: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SqlAclEntry(typing_extensions.TypedDict, total=False):
    expireTime: str
    label: str
    ttl: str
    value: str

@typing.type_check_only
class SqlIpConfig(typing_extensions.TypedDict, total=False):
    authorizedNetworks: _list[SqlAclEntry]
    enableIpv4: bool
    privateNetwork: str
    requireSsl: bool

@typing.type_check_only
class SshScript(typing_extensions.TypedDict, total=False):
    script: str

@typing.type_check_only
class SslConfig(typing_extensions.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str
    type: typing_extensions.Literal[
        "SSL_TYPE_UNSPECIFIED", "SERVER_ONLY", "SERVER_CLIENT"
    ]

@typing.type_check_only
class StartMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StaticIpConnectivity(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StaticServiceIpConnectivity(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StoredProcedureEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    sqlCode: str

@typing.type_check_only
class SynonymEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    sourceEntity: str
    sourceType: typing_extensions.Literal[
        "DATABASE_ENTITY_TYPE_UNSPECIFIED",
        "DATABASE_ENTITY_TYPE_SCHEMA",
        "DATABASE_ENTITY_TYPE_TABLE",
        "DATABASE_ENTITY_TYPE_COLUMN",
        "DATABASE_ENTITY_TYPE_CONSTRAINT",
        "DATABASE_ENTITY_TYPE_INDEX",
        "DATABASE_ENTITY_TYPE_TRIGGER",
        "DATABASE_ENTITY_TYPE_VIEW",
        "DATABASE_ENTITY_TYPE_SEQUENCE",
        "DATABASE_ENTITY_TYPE_STORED_PROCEDURE",
        "DATABASE_ENTITY_TYPE_FUNCTION",
        "DATABASE_ENTITY_TYPE_SYNONYM",
        "DATABASE_ENTITY_TYPE_DATABASE_PACKAGE",
        "DATABASE_ENTITY_TYPE_UDT",
        "DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW",
        "DATABASE_ENTITY_TYPE_DATABASE",
    ]

@typing.type_check_only
class TableEntity(typing_extensions.TypedDict, total=False):
    columns: _list[ColumnEntity]
    comment: str
    constraints: _list[ConstraintEntity]
    customFeatures: dict[str, typing.Any]
    indices: _list[IndexEntity]
    triggers: _list[TriggerEntity]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TriggerEntity(typing_extensions.TypedDict, total=False):
    customFeatures: dict[str, typing.Any]
    name: str
    sqlCode: str
    triggerType: str
    triggeringEvents: _list[str]

@typing.type_check_only
class UserPassword(typing_extensions.TypedDict, total=False):
    password: str
    passwordSet: bool
    user: str

@typing.type_check_only
class VerifyMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ViewEntity(typing_extensions.TypedDict, total=False):
    constraints: _list[ConstraintEntity]
    customFeatures: dict[str, typing.Any]
    sqlCode: str

@typing.type_check_only
class VmCreationConfig(typing_extensions.TypedDict, total=False):
    subnet: str
    vmMachineType: str
    vmZone: str

@typing.type_check_only
class VmSelectionConfig(typing_extensions.TypedDict, total=False):
    vmZone: str

@typing.type_check_only
class VpcPeeringConfig(typing_extensions.TypedDict, total=False):
    subnet: str
    vpcName: str

@typing.type_check_only
class VpcPeeringConnectivity(typing_extensions.TypedDict, total=False):
    vpc: str
