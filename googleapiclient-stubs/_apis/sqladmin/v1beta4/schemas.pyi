import typing

import typing_extensions

class InstancesRotateServerCaRequest(typing_extensions.TypedDict, total=False):
    rotateServerCaContext: RotateServerCaContext

class DatabaseInstance(typing_extensions.TypedDict, total=False):
    rootPassword: str
    failoverReplica: typing.Dict[str, typing.Any]
    instanceType: typing_extensions.Literal[
        "SQL_INSTANCE_TYPE_UNSPECIFIED",
        "CLOUD_SQL_INSTANCE",
        "ON_PREMISES_INSTANCE",
        "READ_REPLICA_INSTANCE",
    ]
    connectionName: str
    backendType: typing_extensions.Literal[
        "SQL_BACKEND_TYPE_UNSPECIFIED", "FIRST_GEN", "SECOND_GEN", "EXTERNAL"
    ]
    databaseVersion: typing_extensions.Literal[
        "SQL_DATABASE_VERSION_UNSPECIFIED",
        "MYSQL_5_1",
        "MYSQL_5_5",
        "MYSQL_5_6",
        "MYSQL_5_7",
        "POSTGRES_9_6",
        "POSTGRES_11",
        "SQLSERVER_2017_STANDARD",
        "SQLSERVER_2017_ENTERPRISE",
        "SQLSERVER_2017_EXPRESS",
        "SQLSERVER_2017_WEB",
        "POSTGRES_10",
        "POSTGRES_12",
        "MYSQL_8_0",
        "POSTGRES_13",
    ]
    selfLink: str
    serverCaCert: SslCert
    settings: Settings
    ipv6Address: str
    maxDiskSize: str
    etag: str
    ipAddresses: typing.List[IpMapping]
    scheduledMaintenance: SqlScheduledMaintenance
    project: str
    suspensionReason: typing.List[str]
    region: str
    onPremisesConfiguration: OnPremisesConfiguration
    diskEncryptionStatus: DiskEncryptionStatus
    name: str
    currentDiskSize: str
    masterInstanceName: str
    kind: str
    gceZone: str
    replicaConfiguration: ReplicaConfiguration
    serviceAccountEmailAddress: str
    diskEncryptionConfiguration: DiskEncryptionConfiguration
    state: typing_extensions.Literal[
        "SQL_INSTANCE_STATE_UNSPECIFIED",
        "RUNNABLE",
        "SUSPENDED",
        "PENDING_DELETE",
        "PENDING_CREATE",
        "MAINTENANCE",
        "FAILED",
    ]
    replicaNames: typing.List[str]

class SslCertsInsertResponse(typing_extensions.TypedDict, total=False):
    serverCaCert: SslCert
    kind: str
    operation: Operation
    clientCert: SslCertDetail

class InstancesCloneRequest(typing_extensions.TypedDict, total=False):
    cloneContext: CloneContext

class Flag(typing_extensions.TypedDict, total=False):
    allowedIntValues: typing.List[str]
    requiresRestart: bool
    name: str
    allowedStringValues: typing.List[str]
    kind: str
    maxValue: str
    minValue: str
    inBeta: bool
    type: typing_extensions.Literal[
        "SQL_FLAG_TYPE_UNSPECIFIED",
        "BOOLEAN",
        "STRING",
        "INTEGER",
        "NONE",
        "MYSQL_TIMEZONE_OFFSET",
        "FLOAT",
        "REPEATED_STRING",
    ]
    appliesTo: typing.List[str]

class SqlServerDatabaseDetails(typing_extensions.TypedDict, total=False):
    compatibilityLevel: int
    recoveryModel: str

class SslCertsCreateEphemeralRequest(typing_extensions.TypedDict, total=False):
    public_key: str

class DenyMaintenancePeriod(typing_extensions.TypedDict, total=False):
    endDate: str
    time: str
    startDate: str

class DiskEncryptionStatus(typing_extensions.TypedDict, total=False):
    kmsKeyVersionName: str
    kind: str

class IpMapping(typing_extensions.TypedDict, total=False):
    timeToRetire: str
    type: typing_extensions.Literal[
        "SQL_IP_ADDRESS_TYPE_UNSPECIFIED",
        "PRIMARY",
        "OUTGOING",
        "PRIVATE",
        "MIGRATED_1ST_GEN",
    ]
    ipAddress: str

class SqlInstancesVerifyExternalSyncSettingsResponse(
    typing_extensions.TypedDict, total=False
):
    errors: typing.List[SqlExternalSyncSettingError]
    kind: str

class InstancesExportRequest(typing_extensions.TypedDict, total=False):
    exportContext: ExportContext

class BackupRetentionSettings(typing_extensions.TypedDict, total=False):
    retentionUnit: typing_extensions.Literal["RETENTION_UNIT_UNSPECIFIED", "COUNT"]
    retainedBackups: int

class SqlServerUserDetails(typing_extensions.TypedDict, total=False):
    serverRoles: typing.List[str]
    disabled: bool

class User(typing_extensions.TypedDict, total=False):
    sqlserverUserDetails: SqlServerUserDetails
    password: str
    name: str
    type: typing_extensions.Literal[
        "BUILT_IN", "CLOUD_IAM_USER", "CLOUD_IAM_SERVICE_ACCOUNT"
    ]
    project: str
    host: str
    kind: str
    instance: str
    etag: str

class InstancesListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    warnings: typing.List[ApiWarning]
    items: typing.List[DatabaseInstance]

class Reschedule(typing_extensions.TypedDict, total=False):
    rescheduleType: typing_extensions.Literal[
        "RESCHEDULE_TYPE_UNSPECIFIED",
        "IMMEDIATE",
        "NEXT_AVAILABLE_WINDOW",
        "SPECIFIC_TIME",
    ]
    scheduleTime: str

class SqlInstancesRescheduleMaintenanceRequestBody(
    typing_extensions.TypedDict, total=False
):
    reschedule: Reschedule

class InstancesRestoreBackupRequest(typing_extensions.TypedDict, total=False):
    restoreBackupContext: RestoreBackupContext

class BackupRunsListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[BackupRun]
    nextPageToken: str
    kind: str

class ExportContext(typing_extensions.TypedDict, total=False):
    fileType: typing_extensions.Literal[
        "SQL_FILE_TYPE_UNSPECIFIED", "SQL", "CSV", "BAK"
    ]
    uri: str
    sqlExportOptions: typing.Dict[str, typing.Any]
    databases: typing.List[str]
    csvExportOptions: typing.Dict[str, typing.Any]
    offload: bool
    kind: str

class ApiWarning(typing_extensions.TypedDict, total=False):
    message: str
    code: typing_extensions.Literal[
        "SQL_API_WARNING_CODE_UNSPECIFIED", "REGION_UNREACHABLE"
    ]

class IpConfiguration(typing_extensions.TypedDict, total=False):
    privateNetwork: str
    ipv4Enabled: bool
    requireSsl: bool
    authorizedNetworks: typing.List[AclEntry]

class Settings(typing_extensions.TypedDict, total=False):
    kind: str
    collation: str
    databaseReplicationEnabled: bool
    denyMaintenancePeriods: typing.List[DenyMaintenancePeriod]
    authorizedGaeApplications: typing.List[str]
    storageAutoResizeLimit: str
    storageAutoResize: bool
    pricingPlan: typing_extensions.Literal[
        "SQL_PRICING_PLAN_UNSPECIFIED", "PACKAGE", "PER_USE"
    ]
    dataDiskSizeGb: str
    userLabels: typing.Dict[str, typing.Any]
    ipConfiguration: IpConfiguration
    dataDiskType: typing_extensions.Literal[
        "SQL_DATA_DISK_TYPE_UNSPECIFIED", "PD_SSD", "PD_HDD", "OBSOLETE_LOCAL_SSD"
    ]
    replicationType: typing_extensions.Literal[
        "SQL_REPLICATION_TYPE_UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
    ]
    locationPreference: LocationPreference
    settingsVersion: str
    availabilityType: typing_extensions.Literal[
        "SQL_AVAILABILITY_TYPE_UNSPECIFIED", "ZONAL", "REGIONAL"
    ]
    maintenanceWindow: MaintenanceWindow
    tier: str
    backupConfiguration: BackupConfiguration
    activationPolicy: typing_extensions.Literal[
        "SQL_ACTIVATION_POLICY_UNSPECIFIED", "ALWAYS", "NEVER", "ON_DEMAND"
    ]
    crashSafeReplicationEnabled: bool
    activeDirectoryConfig: SqlActiveDirectoryConfig
    databaseFlags: typing.List[DatabaseFlags]

class SslCert(typing_extensions.TypedDict, total=False):
    instance: str
    cert: str
    certSerialNumber: str
    expirationTime: str
    commonName: str
    kind: str
    sha1Fingerprint: str
    createTime: str
    selfLink: str

class BackupConfiguration(typing_extensions.TypedDict, total=False):
    startTime: str
    transactionLogRetentionDays: int
    backupRetentionSettings: BackupRetentionSettings
    enabled: bool
    replicationLogArchivingEnabled: bool
    kind: str
    pointInTimeRecoveryEnabled: bool
    location: str
    binaryLogEnabled: bool

class SslCertsInsertRequest(typing_extensions.TypedDict, total=False):
    commonName: str

class TiersListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Tier]

class InstancesTruncateLogRequest(typing_extensions.TypedDict, total=False):
    truncateLogContext: TruncateLogContext

class BackupRun(typing_extensions.TypedDict, total=False):
    location: str
    id: str
    enqueuedTime: str
    description: str
    diskEncryptionStatus: DiskEncryptionStatus
    selfLink: str
    status: typing_extensions.Literal[
        "SQL_BACKUP_RUN_STATUS_UNSPECIFIED",
        "ENQUEUED",
        "OVERDUE",
        "RUNNING",
        "FAILED",
        "SUCCESSFUL",
        "SKIPPED",
        "DELETION_PENDING",
        "DELETION_FAILED",
        "DELETED",
    ]
    diskEncryptionConfiguration: DiskEncryptionConfiguration
    endTime: str
    error: OperationError
    windowStartTime: str
    type: typing_extensions.Literal[
        "SQL_BACKUP_RUN_TYPE_UNSPECIFIED", "AUTOMATED", "ON_DEMAND"
    ]
    backupKind: typing_extensions.Literal[
        "SQL_BACKUP_KIND_UNSPECIFIED", "SNAPSHOT", "PHYSICAL"
    ]
    startTime: str
    kind: str
    instance: str

class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    kind: str
    updateTrack: typing_extensions.Literal[
        "SQL_UPDATE_TRACK_UNSPECIFIED", "canary", "stable"
    ]
    hour: int
    day: int

class InstancesImportRequest(typing_extensions.TypedDict, total=False):
    importContext: ImportContext

class UsersListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[User]
    kind: str
    nextPageToken: str

class OperationError(typing_extensions.TypedDict, total=False):
    code: str
    kind: str
    message: str

class DiskEncryptionConfiguration(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    kind: str

class Database(typing_extensions.TypedDict, total=False):
    charset: str
    name: str
    kind: str
    instance: str
    selfLink: str
    sqlserverDatabaseDetails: SqlServerDatabaseDetails
    collation: str
    project: str
    etag: str

class DatabaseFlags(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class Tier(typing_extensions.TypedDict, total=False):
    kind: str
    DiskQuota: str
    tier: str
    region: typing.List[str]
    RAM: str

class SslCertsListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[SslCert]
    kind: str

class DemoteMasterMySqlReplicaConfiguration(typing_extensions.TypedDict, total=False):
    password: str
    caCertificate: str
    clientKey: str
    clientCertificate: str
    username: str
    kind: str

class SslCertDetail(typing_extensions.TypedDict, total=False):
    certInfo: SslCert
    certPrivateKey: str

class RestoreBackupContext(typing_extensions.TypedDict, total=False):
    backupRunId: str
    project: str
    kind: str
    instanceId: str

class OnPremisesConfiguration(typing_extensions.TypedDict, total=False):
    dumpFilePath: str
    kind: str
    clientCertificate: str
    caCertificate: str
    password: str
    username: str
    clientKey: str
    hostPort: str

class SqlScheduledMaintenance(typing_extensions.TypedDict, total=False):
    canDefer: bool
    canReschedule: bool
    startTime: str

class DemoteMasterContext(typing_extensions.TypedDict, total=False):
    verifyGtidConsistency: bool
    kind: str
    replicaConfiguration: DemoteMasterConfiguration
    masterInstanceName: str

class OperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Operation]
    kind: str

class DatabasesListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Database]
    kind: str

class OperationErrors(typing_extensions.TypedDict, total=False):
    kind: str
    errors: typing.List[OperationError]

class MySqlReplicaConfiguration(typing_extensions.TypedDict, total=False):
    masterHeartbeatPeriod: str
    password: str
    dumpFilePath: str
    kind: str
    sslCipher: str
    clientCertificate: str
    clientKey: str
    username: str
    caCertificate: str
    connectRetryInterval: int
    verifyServerCertificate: bool

class FlagsListResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Flag]
    kind: str

class CloneContext(typing_extensions.TypedDict, total=False):
    pitrTimestampMs: str
    kind: str
    binLogCoordinates: BinLogCoordinates
    destinationInstanceName: str
    pointInTime: str

class SqlExternalSyncSettingError(typing_extensions.TypedDict, total=False):
    detail: str
    type: typing_extensions.Literal[
        "SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED",
        "CONNECTION_FAILURE",
        "BINLOG_NOT_ENABLED",
        "INCOMPATIBLE_DATABASE_VERSION",
        "REPLICA_ALREADY_SETUP",
        "INSUFFICIENT_PRIVILEGE",
        "UNSUPPORTED_MIGRATION_TYPE",
        "NO_PGLOGICAL_INSTALLED",
        "PGLOGICAL_NODE_ALREADY_EXISTS",
        "INVALID_WAL_LEVEL",
        "INVALID_SHARED_PRELOAD_LIBRARY",
        "INSUFFICIENT_MAX_REPLICATION_SLOTS",
        "INSUFFICIENT_MAX_WAL_SENDERS",
        "INSUFFICIENT_MAX_WORKER_PROCESSES",
        "UNSUPPORTED_EXTENSIONS",
        "INVALID_RDS_LOGICAL_REPLICATION",
        "INVALID_LOGGING_SETUP",
        "INVALID_DB_PARAM",
        "UNSUPPORTED_GTID_MODE",
        "SQLSERVER_AGENT_NOT_RUNNING",
    ]
    kind: str

class AclEntry(typing_extensions.TypedDict, total=False):
    expirationTime: str
    name: str
    kind: str
    value: str

class InstancesDemoteMasterRequest(typing_extensions.TypedDict, total=False):
    demoteMasterContext: DemoteMasterContext

class RotateServerCaContext(typing_extensions.TypedDict, total=False):
    nextVersion: str
    kind: str

class FailoverContext(typing_extensions.TypedDict, total=False):
    settingsVersion: str
    kind: str

class BinLogCoordinates(typing_extensions.TypedDict, total=False):
    binLogPosition: str
    binLogFileName: str
    kind: str

class DemoteMasterConfiguration(typing_extensions.TypedDict, total=False):
    mysqlReplicaConfiguration: DemoteMasterMySqlReplicaConfiguration
    kind: str

class Operation(typing_extensions.TypedDict, total=False):
    targetProject: str
    selfLink: str
    targetId: str
    status: typing_extensions.Literal[
        "SQL_OPERATION_STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE"
    ]
    insertTime: str
    exportContext: ExportContext
    targetLink: str
    importContext: ImportContext
    name: str
    endTime: str
    operationType: typing_extensions.Literal[
        "SQL_OPERATION_TYPE_UNSPECIFIED",
        "IMPORT",
        "EXPORT",
        "CREATE",
        "UPDATE",
        "DELETE",
        "RESTART",
        "BACKUP",
        "SNAPSHOT",
        "BACKUP_VOLUME",
        "DELETE_VOLUME",
        "RESTORE_VOLUME",
        "INJECT_USER",
        "CLONE",
        "STOP_REPLICA",
        "START_REPLICA",
        "PROMOTE_REPLICA",
        "CREATE_REPLICA",
        "CREATE_USER",
        "DELETE_USER",
        "UPDATE_USER",
        "CREATE_DATABASE",
        "DELETE_DATABASE",
        "UPDATE_DATABASE",
        "FAILOVER",
        "DELETE_BACKUP",
        "RECREATE_REPLICA",
        "TRUNCATE_LOG",
        "DEMOTE_MASTER",
        "MAINTENANCE",
        "ENABLE_PRIVATE_IP",
        "DEFER_MAINTENANCE",
        "CREATE_CLONE",
        "RESCHEDULE_MAINTENANCE",
        "START_EXTERNAL_SYNC",
    ]
    startTime: str
    user: str
    kind: str
    error: OperationErrors

class InstancesFailoverRequest(typing_extensions.TypedDict, total=False):
    failoverContext: FailoverContext

class LocationPreference(typing_extensions.TypedDict, total=False):
    kind: str
    zone: str
    followGaeApplication: str

class InstancesListServerCasResponse(typing_extensions.TypedDict, total=False):
    activeVersion: str
    kind: str
    certs: typing.List[SslCert]

class ImportContext(typing_extensions.TypedDict, total=False):
    kind: str
    csvImportOptions: typing.Dict[str, typing.Any]
    fileType: typing_extensions.Literal[
        "SQL_FILE_TYPE_UNSPECIFIED", "SQL", "CSV", "BAK"
    ]
    importUser: str
    uri: str
    database: str
    bakImportOptions: typing.Dict[str, typing.Any]

class TruncateLogContext(typing_extensions.TypedDict, total=False):
    logType: str
    kind: str

class SqlActiveDirectoryConfig(typing_extensions.TypedDict, total=False):
    domain: str
    kind: str

class ReplicaConfiguration(typing_extensions.TypedDict, total=False):
    failoverTarget: bool
    kind: str
    mysqlReplicaConfiguration: MySqlReplicaConfiguration
