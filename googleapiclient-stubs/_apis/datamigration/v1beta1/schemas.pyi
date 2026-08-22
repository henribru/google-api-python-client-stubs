import typing

_list = list

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
class BadRequest(typing.TypedDict, total=False):
    fieldViolations: _list[FieldViolation]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloudSqlConnectionProfile(typing.TypedDict, total=False):
    cloudSqlId: str
    privateIp: str
    publicIp: str
    settings: CloudSqlSettings

@typing.type_check_only
class CloudSqlSettings(typing.TypedDict, total=False):
    activationPolicy: typing.Literal[
        "SQL_ACTIVATION_POLICY_UNSPECIFIED", "ALWAYS", "NEVER"
    ]
    autoStorageIncrease: bool
    dataDiskSizeGb: str
    dataDiskType: typing.Literal["SQL_DATA_DISK_TYPE_UNSPECIFIED", "PD_SSD", "PD_HDD"]
    databaseFlags: dict[str, typing.Any]
    databaseVersion: typing.Literal[
        "SQL_DATABASE_VERSION_UNSPECIFIED", "MYSQL_5_6", "MYSQL_5_7", "MYSQL_8_0"
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
class ConnectionProfile(typing.TypedDict, total=False):
    cloudsql: CloudSqlConnectionProfile
    createTime: str
    displayName: str
    error: Status
    labels: dict[str, typing.Any]
    mysql: MySqlConnectionProfile
    name: str
    provider: typing.Literal["DATABASE_PROVIDER_UNSPECIFIED", "CLOUDSQL", "RDS"]
    state: typing.Literal[
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
class DatabaseType(typing.TypedDict, total=False):
    engine: typing.Literal["DATABASE_ENGINE_UNSPECIFIED", "MYSQL"]
    provider: typing.Literal["DATABASE_PROVIDER_UNSPECIFIED", "CLOUDSQL", "RDS"]

@typing.type_check_only
class DebugInfo(typing.TypedDict, total=False):
    detail: str
    stackEntries: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    domain: str
    metadata: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FieldViolation(typing.TypedDict, total=False):
    description: str
    field: str
    localizedMessage: LocalizedMessage
    reason: str

@typing.type_check_only
class GenerateSshScriptRequest(typing.TypedDict, total=False):
    vm: str
    vmCreationConfig: VmCreationConfig
    vmPort: int
    vmSelectionConfig: VmSelectionConfig

@typing.type_check_only
class GoogleCloudClouddmsV1beta1OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Help(typing.TypedDict, total=False):
    links: _list[Link]

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class ListConnectionProfilesResponse(typing.TypedDict, total=False):
    connectionProfiles: _list[ConnectionProfile]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMigrationJobsResponse(typing.TypedDict, total=False):
    migrationJobs: _list[MigrationJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class LocalizedMessage(typing.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MigrationJob(typing.TypedDict, total=False):
    createTime: str
    destination: str
    destinationDatabase: DatabaseType
    displayName: str
    dumpPath: str
    duration: str
    endTime: str
    error: Status
    labels: dict[str, typing.Any]
    name: str
    phase: typing.Literal[
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
    state: typing.Literal[
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
    type: typing.Literal["TYPE_UNSPECIFIED", "ONE_TIME", "CONTINUOUS"]
    updateTime: str
    vpcPeeringConnectivity: VpcPeeringConnectivity

@typing.type_check_only
class MigrationJobVerificationError(typing.TypedDict, total=False):
    errorCode: typing.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "CONNECTION_FAILURE",
        "AUTHENTICATION_FAILURE",
        "INVALID_CONNECTION_PROFILE_CONFIG",
        "VERSION_INCOMPATIBILITY",
        "CONNECTION_PROFILE_TYPES_INCOMPATIBILITY",
        "UNSUPPORTED_GTID_MODE",
        "UNSUPPORTED_DEFINER",
        "CANT_RESTART_RUNNING_MIGRATION",
        "TABLES_WITH_LIMITED_SUPPORT",
        "UNSUPPORTED_DATABASE_LOCALE",
        "UNSUPPORTED_DATABASE_FDW_CONFIG",
        "ERROR_RDBMS",
        "SOURCE_SIZE_EXCEEDS_THRESHOLD",
        "EXISTING_CONFLICTING_DATABASES",
        "PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE",
        "EXISTING_DATA",
        "SOURCE_MAX_SUBSCRIPTIONS",
    ]
    errorDetailMessage: str
    errorMessage: str

@typing.type_check_only
class MySqlConnectionProfile(typing.TypedDict, total=False):
    cloudSqlId: str
    host: str
    password: str
    passwordSet: bool
    port: int
    ssl: SslConfig
    username: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PreconditionFailure(typing.TypedDict, total=False):
    violations: _list[PreconditionFailureViolation]

@typing.type_check_only
class PreconditionFailureViolation(typing.TypedDict, total=False):
    description: str
    subject: str
    type: str

@typing.type_check_only
class PromoteMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class QuotaFailure(typing.TypedDict, total=False):
    violations: _list[QuotaFailureViolation]

@typing.type_check_only
class QuotaFailureViolation(typing.TypedDict, total=False):
    apiService: str
    description: str
    futureQuotaValue: str
    quotaDimensions: dict[str, typing.Any]
    quotaId: str
    quotaMetric: str
    quotaValue: str
    subject: str

@typing.type_check_only
class RequestInfo(typing.TypedDict, total=False):
    requestId: str
    servingData: str

@typing.type_check_only
class ResourceInfo(typing.TypedDict, total=False):
    description: str
    owner: str
    resourceName: str
    resourceType: str

@typing.type_check_only
class RestartMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResumeMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetryInfo(typing.TypedDict, total=False):
    retryDelay: str

@typing.type_check_only
class ReverseSshConnectivity(typing.TypedDict, total=False):
    vm: str
    vmIp: str
    vmPort: int
    vpc: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SqlAclEntry(typing.TypedDict, total=False):
    expireTime: str
    label: str
    ttl: str
    value: str

@typing.type_check_only
class SqlIpConfig(typing.TypedDict, total=False):
    authorizedNetworks: _list[SqlAclEntry]
    enableIpv4: bool
    privateNetwork: str
    requireSsl: bool

@typing.type_check_only
class SshScript(typing.TypedDict, total=False):
    script: str

@typing.type_check_only
class SslConfig(typing.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str
    type: typing.Literal["SSL_TYPE_UNSPECIFIED", "SERVER_ONLY", "SERVER_CLIENT"]

@typing.type_check_only
class StartMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StaticIpConnectivity(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class VerifyMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class VmCreationConfig(typing.TypedDict, total=False):
    subnet: str
    vmMachineType: str
    vmZone: str

@typing.type_check_only
class VmSelectionConfig(typing.TypedDict, total=False):
    vmZone: str

@typing.type_check_only
class VpcPeeringConnectivity(typing.TypedDict, total=False):
    vpc: str
