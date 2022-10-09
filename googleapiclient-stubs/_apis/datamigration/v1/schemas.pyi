import typing

import typing_extensions

_list = list

@typing.type_check_only
class AlloyDbConnectionProfile(typing_extensions.TypedDict, total=False):
    clusterId: str
    settings: AlloyDbSettings

@typing.type_check_only
class AlloyDbSettings(typing_extensions.TypedDict, total=False):
    initialUser: UserPassword
    labels: dict[str, typing.Any]
    primaryInstanceSettings: PrimaryInstanceSettings
    vpcNetwork: str

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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudSqlConnectionProfile(typing_extensions.TypedDict, total=False):
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
    sourceId: str
    storageAutoResizeLimit: str
    tier: str
    userLabels: dict[str, typing.Any]
    zone: str

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
class DatabaseType(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal[
        "DATABASE_ENGINE_UNSPECIFIED", "MYSQL", "POSTGRESQL"
    ]
    provider: typing_extensions.Literal[
        "DATABASE_PROVIDER_UNSPECIFIED", "CLOUDSQL", "RDS", "AURORA", "ALLOYDB"
    ]

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
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
class ListConnectionProfilesResponse(typing_extensions.TypedDict, total=False):
    connectionProfiles: _list[ConnectionProfile]
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
    createTime: str
    destination: str
    destinationDatabase: DatabaseType
    displayName: str
    dumpFlags: DumpFlags
    dumpPath: str
    duration: str
    endTime: str
    error: Status
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
    ssl: SslConfig
    username: str

@typing.type_check_only
class PrimaryInstanceSettings(typing_extensions.TypedDict, total=False):
    databaseFlags: dict[str, typing.Any]
    id: str
    labels: dict[str, typing.Any]
    machineConfig: MachineConfig
    privateIp: str

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UserPassword(typing_extensions.TypedDict, total=False):
    password: str
    passwordSet: bool
    user: str

@typing.type_check_only
class VerifyMigrationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VmCreationConfig(typing_extensions.TypedDict, total=False):
    subnet: str
    vmMachineType: str
    vmZone: str

@typing.type_check_only
class VmSelectionConfig(typing_extensions.TypedDict, total=False):
    vmZone: str

@typing.type_check_only
class VpcPeeringConnectivity(typing_extensions.TypedDict, total=False):
    vpc: str
