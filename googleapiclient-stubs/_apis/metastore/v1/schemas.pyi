import typing

_list = list

@typing.type_check_only
class AlterMetadataResourceLocationRequest(typing.TypedDict, total=False):
    locationUri: str
    resourceName: str

@typing.type_check_only
class AlterMetadataResourceLocationResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class AlterTablePropertiesRequest(typing.TypedDict, total=False):
    properties: dict[str, typing.Any]
    tableName: str
    updateMask: str

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
class AutoscalingConfig(typing.TypedDict, total=False):
    autoscalingEnabled: bool
    autoscalingFactor: float
    limitConfig: LimitConfig

@typing.type_check_only
class AuxiliaryVersionConfig(typing.TypedDict, total=False):
    configOverrides: dict[str, typing.Any]
    networkConfig: NetworkConfig
    version: str

@typing.type_check_only
class BackendMetastore(typing.TypedDict, total=False):
    metastoreType: typing.Literal[
        "METASTORE_TYPE_UNSPECIFIED", "BIGQUERY", "DATAPROC_METASTORE"
    ]
    name: str

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
    createTime: str
    description: str
    endTime: str
    name: str
    restoringServices: _list[str]
    serviceRevision: Service
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "ACTIVE", "FAILED", "RESTORING"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CdcConfig(typing.TypedDict, total=False):
    bucket: str
    password: str
    reverseProxySubnet: str
    rootPath: str
    subnetIpRange: str
    username: str
    vpcNetwork: str

@typing.type_check_only
class CloudSQLConnectionConfig(typing.TypedDict, total=False):
    hiveDatabaseName: str
    instanceConnectionName: str
    ipAddress: str
    natSubnet: str
    password: str
    port: int
    proxySubnet: str
    username: str

@typing.type_check_only
class CloudSQLMigrationConfig(typing.TypedDict, total=False):
    cdcConfig: CdcConfig
    cloudSqlConnectionConfig: CloudSQLConnectionConfig

@typing.type_check_only
class CompleteMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Consumer(typing.TypedDict, total=False):
    endpointLocation: str
    endpointUri: str
    subnetwork: str

@typing.type_check_only
class CustomRegionMetadata(typing.TypedDict, total=False):
    optionalReadOnlyRegions: _list[str]
    requiredReadWriteRegions: _list[str]
    witnessRegion: str

@typing.type_check_only
class DataCatalogConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class DatabaseDump(typing.TypedDict, total=False):
    databaseType: typing.Literal["DATABASE_TYPE_UNSPECIFIED", "MYSQL"]
    gcsUri: str
    sourceDatabase: str
    type: typing.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class ErrorDetails(typing.TypedDict, total=False):
    details: dict[str, typing.Any]

@typing.type_check_only
class ExportMetadataRequest(typing.TypedDict, total=False):
    databaseDumpType: typing.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsFolder: str
    requestId: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Federation(typing.TypedDict, total=False):
    backendMetastores: dict[str, typing.Any]
    createTime: str
    endpointUri: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING", "ERROR"
    ]
    stateMessage: str
    tags: dict[str, typing.Any]
    uid: str
    updateTime: str
    version: str

@typing.type_check_only
class HiveMetastoreConfig(typing.TypedDict, total=False):
    auxiliaryVersions: dict[str, typing.Any]
    configOverrides: dict[str, typing.Any]
    endpointProtocol: typing.Literal["ENDPOINT_PROTOCOL_UNSPECIFIED", "THRIFT", "GRPC"]
    kerberosConfig: KerberosConfig
    version: str

@typing.type_check_only
class HiveMetastoreVersion(typing.TypedDict, total=False):
    isDefault: bool
    version: str

@typing.type_check_only
class KerberosConfig(typing.TypedDict, total=False):
    keytab: Secret
    krb5ConfigGcsUri: str
    principal: str

@typing.type_check_only
class LatestBackup(typing.TypedDict, total=False):
    backupId: str
    duration: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"]

@typing.type_check_only
class LimitConfig(typing.TypedDict, total=False):
    maxScalingFactor: float
    minScalingFactor: float

@typing.type_check_only
class ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFederationsResponse(typing.TypedDict, total=False):
    federations: _list[Federation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMetadataImportsResponse(typing.TypedDict, total=False):
    metadataImports: _list[MetadataImport]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMigrationExecutionsResponse(typing.TypedDict, total=False):
    migrationExecutions: _list[MigrationExecution]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    customRegionMetadata: _list[CustomRegionMetadata]
    multiRegionMetadata: MultiRegionMetadata
    supportedHiveMetastoreVersions: _list[HiveMetastoreVersion]

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    hourOfDay: int

@typing.type_check_only
class MessageSet(typing.TypedDict, total=False): ...

@typing.type_check_only
class MetadataExport(typing.TypedDict, total=False):
    databaseDumpType: typing.Literal["TYPE_UNSPECIFIED", "MYSQL", "AVRO"]
    destinationGcsUri: str
    endTime: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]

@typing.type_check_only
class MetadataImport(typing.TypedDict, total=False):
    createTime: str
    databaseDump: DatabaseDump
    description: str
    endTime: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "UPDATING", "FAILED"
    ]
    updateTime: str

@typing.type_check_only
class MetadataIntegration(typing.TypedDict, total=False):
    dataCatalogConfig: DataCatalogConfig

@typing.type_check_only
class MetadataManagementActivity(typing.TypedDict, total=False):
    metadataExports: _list[MetadataExport]
    restores: _list[Restore]

@typing.type_check_only
class MigrationExecution(typing.TypedDict, total=False):
    cloudSqlMigrationConfig: CloudSQLMigrationConfig
    createTime: str
    endTime: str
    name: str
    phase: typing.Literal["PHASE_UNSPECIFIED", "REPLICATION", "CUTOVER"]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "RUNNING",
        "CANCELLING",
        "AWAITING_USER_ACTION",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "DELETING",
        "ROLLED_BACK",
    ]
    stateMessage: str

@typing.type_check_only
class MoveTableToDatabaseRequest(typing.TypedDict, total=False):
    dbName: str
    destinationDbName: str
    tableName: str

@typing.type_check_only
class MoveTableToDatabaseResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class MultiRegionMetadata(typing.TypedDict, total=False):
    constituentRegions: _list[str]
    continent: str
    witnessRegion: str

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    consumers: _list[Consumer]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class QueryMetadataRequest(typing.TypedDict, total=False):
    query: str

@typing.type_check_only
class QueryMetadataResponse(typing.TypedDict, total=False):
    resultManifestUri: str

@typing.type_check_only
class Restore(typing.TypedDict, total=False):
    backup: str
    backupLocation: str
    details: str
    endTime: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    type: typing.Literal["RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"]

@typing.type_check_only
class RestoreServiceRequest(typing.TypedDict, total=False):
    backup: str
    backupLocation: str
    requestId: str
    restoreType: typing.Literal["RESTORE_TYPE_UNSPECIFIED", "FULL", "METADATA_ONLY"]

@typing.type_check_only
class ScalingConfig(typing.TypedDict, total=False):
    autoscalingConfig: AutoscalingConfig
    instanceSize: typing.Literal[
        "INSTANCE_SIZE_UNSPECIFIED",
        "EXTRA_SMALL",
        "SMALL",
        "MEDIUM",
        "LARGE",
        "EXTRA_LARGE",
    ]
    scalingFactor: float

@typing.type_check_only
class ScheduledBackup(typing.TypedDict, total=False):
    backupLocation: str
    cronSchedule: str
    enabled: bool
    latestBackup: LatestBackup
    nextScheduledTime: str
    timeZone: str

@typing.type_check_only
class Secret(typing.TypedDict, total=False):
    cloudSecret: str

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    artifactGcsUri: str
    createTime: str
    databaseType: typing.Literal["DATABASE_TYPE_UNSPECIFIED", "MYSQL", "SPANNER"]
    deletionProtection: bool
    encryptionConfig: EncryptionConfig
    endpointUri: str
    hiveMetastoreConfig: HiveMetastoreConfig
    labels: dict[str, typing.Any]
    maintenanceWindow: MaintenanceWindow
    metadataIntegration: MetadataIntegration
    metadataManagementActivity: MetadataManagementActivity
    name: str
    network: str
    networkConfig: NetworkConfig
    port: int
    releaseChannel: typing.Literal["RELEASE_CHANNEL_UNSPECIFIED", "CANARY", "STABLE"]
    scalingConfig: ScalingConfig
    scheduledBackup: ScheduledBackup
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "SUSPENDING",
        "SUSPENDED",
        "UPDATING",
        "DELETING",
        "ERROR",
        "AUTOSCALING",
        "MIGRATING",
        "PROXY",
    ]
    stateMessage: str
    tags: dict[str, typing.Any]
    telemetryConfig: TelemetryConfig
    tier: typing.Literal["TIER_UNSPECIFIED", "DEVELOPER", "ENTERPRISE"]
    uid: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class StartMigrationRequest(typing.TypedDict, total=False):
    migrationExecution: MigrationExecution
    requestId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusProto(typing.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: MessageSet
    space: str

@typing.type_check_only
class TelemetryConfig(typing.TypedDict, total=False):
    logFormat: typing.Literal["LOG_FORMAT_UNSPECIFIED", "LEGACY", "JSON"]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
