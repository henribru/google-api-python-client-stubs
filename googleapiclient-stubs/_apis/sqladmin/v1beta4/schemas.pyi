import typing

import typing_extensions

_list = list

@typing.type_check_only
class AclEntry(typing_extensions.TypedDict, total=False):
    expirationTime: str
    kind: str
    name: str
    value: str

@typing.type_check_only
class AcquireSsrsLeaseContext(typing_extensions.TypedDict, total=False):
    duration: str
    reportDatabase: str
    serviceLogin: str
    setupLogin: str

@typing.type_check_only
class AdvancedMachineFeatures(typing_extensions.TypedDict, total=False):
    threadsPerCore: int

@typing.type_check_only
class ApiWarning(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "SQL_API_WARNING_CODE_UNSPECIFIED",
        "REGION_UNREACHABLE",
        "MAX_RESULTS_EXCEEDS_LIMIT",
        "COMPROMISED_CREDENTIALS",
        "INTERNAL_STATE_FAILURE",
    ]
    message: str
    region: str

@typing.type_check_only
class AvailableDatabaseVersion(typing_extensions.TypedDict, total=False):
    displayName: str
    majorVersion: str
    name: str

@typing.type_check_only
class BackupConfiguration(typing_extensions.TypedDict, total=False):
    backupRetentionSettings: BackupRetentionSettings
    binaryLogEnabled: bool
    enabled: bool
    kind: str
    location: str
    pointInTimeRecoveryEnabled: bool
    replicationLogArchivingEnabled: bool
    startTime: str
    transactionLogRetentionDays: int
    transactionalLogStorageState: typing_extensions.Literal[
        "TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED",
        "DISK",
        "SWITCHING_TO_CLOUD_STORAGE",
        "SWITCHED_TO_CLOUD_STORAGE",
        "CLOUD_STORAGE",
    ]

@typing.type_check_only
class BackupContext(typing_extensions.TypedDict, total=False):
    backupId: str
    kind: str

@typing.type_check_only
class BackupReencryptionConfig(typing_extensions.TypedDict, total=False):
    backupLimit: int
    backupType: typing_extensions.Literal[
        "BACKUP_TYPE_UNSPECIFIED", "AUTOMATED", "ON_DEMAND"
    ]

@typing.type_check_only
class BackupRetentionSettings(typing_extensions.TypedDict, total=False):
    retainedBackups: int
    retentionUnit: typing_extensions.Literal["RETENTION_UNIT_UNSPECIFIED", "COUNT"]

@typing.type_check_only
class BackupRun(typing_extensions.TypedDict, total=False):
    backupKind: typing_extensions.Literal[
        "SQL_BACKUP_KIND_UNSPECIFIED", "SNAPSHOT", "PHYSICAL"
    ]
    description: str
    diskEncryptionConfiguration: DiskEncryptionConfiguration
    diskEncryptionStatus: DiskEncryptionStatus
    endTime: str
    enqueuedTime: str
    error: OperationError
    id: str
    instance: str
    kind: str
    location: str
    maxChargeableBytes: str
    selfLink: str
    startTime: str
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
    timeZone: str
    type: typing_extensions.Literal[
        "SQL_BACKUP_RUN_TYPE_UNSPECIFIED", "AUTOMATED", "ON_DEMAND"
    ]
    windowStartTime: str

@typing.type_check_only
class BackupRunsListResponse(typing_extensions.TypedDict, total=False):
    items: _list[BackupRun]
    kind: str
    nextPageToken: str

@typing.type_check_only
class BinLogCoordinates(typing_extensions.TypedDict, total=False):
    binLogFileName: str
    binLogPosition: str
    kind: str

@typing.type_check_only
class CloneContext(typing_extensions.TypedDict, total=False):
    allocatedIpRange: str
    binLogCoordinates: BinLogCoordinates
    databaseNames: _list[str]
    destinationInstanceName: str
    kind: str
    pitrTimestampMs: str
    pointInTime: str
    preferredSecondaryZone: str
    preferredZone: str

@typing.type_check_only
class ConnectSettings(typing_extensions.TypedDict, total=False):
    backendType: typing_extensions.Literal[
        "SQL_BACKEND_TYPE_UNSPECIFIED", "FIRST_GEN", "SECOND_GEN", "EXTERNAL"
    ]
    customSubjectAlternativeNames: _list[str]
    databaseVersion: typing_extensions.Literal[
        "SQL_DATABASE_VERSION_UNSPECIFIED",
        "MYSQL_5_1",
        "MYSQL_5_5",
        "MYSQL_5_6",
        "MYSQL_5_7",
        "MYSQL_8_0",
        "MYSQL_8_0_18",
        "MYSQL_8_0_26",
        "MYSQL_8_0_27",
        "MYSQL_8_0_28",
        "MYSQL_8_0_29",
        "MYSQL_8_0_30",
        "MYSQL_8_0_31",
        "MYSQL_8_0_32",
        "MYSQL_8_0_33",
        "MYSQL_8_0_34",
        "MYSQL_8_0_35",
        "MYSQL_8_0_36",
        "MYSQL_8_0_37",
        "MYSQL_8_0_38",
        "MYSQL_8_0_39",
        "MYSQL_8_0_40",
        "MYSQL_8_0_41",
        "MYSQL_8_0_42",
        "MYSQL_8_4",
        "SQLSERVER_2017_STANDARD",
        "SQLSERVER_2017_ENTERPRISE",
        "SQLSERVER_2017_EXPRESS",
        "SQLSERVER_2017_WEB",
        "POSTGRES_9_6",
        "POSTGRES_10",
        "POSTGRES_11",
        "POSTGRES_12",
        "POSTGRES_13",
        "POSTGRES_14",
        "POSTGRES_15",
        "POSTGRES_16",
        "POSTGRES_17",
        "SQLSERVER_2019_STANDARD",
        "SQLSERVER_2019_ENTERPRISE",
        "SQLSERVER_2019_EXPRESS",
        "SQLSERVER_2019_WEB",
        "SQLSERVER_2022_STANDARD",
        "SQLSERVER_2022_ENTERPRISE",
        "SQLSERVER_2022_EXPRESS",
        "SQLSERVER_2022_WEB",
    ]
    dnsName: str
    ipAddresses: _list[IpMapping]
    kind: str
    pscEnabled: bool
    region: str
    serverCaCert: SslCert
    serverCaMode: typing_extensions.Literal[
        "CA_MODE_UNSPECIFIED", "GOOGLE_MANAGED_INTERNAL_CA", "GOOGLE_MANAGED_CAS_CA"
    ]

@typing.type_check_only
class DataCacheConfig(typing_extensions.TypedDict, total=False):
    dataCacheEnabled: bool

@typing.type_check_only
class Database(typing_extensions.TypedDict, total=False):
    charset: str
    collation: str
    etag: str
    instance: str
    kind: str
    name: str
    project: str
    selfLink: str
    sqlserverDatabaseDetails: SqlServerDatabaseDetails

@typing.type_check_only
class DatabaseFlags(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class DatabaseInstance(typing_extensions.TypedDict, total=False):
    availableMaintenanceVersions: _list[str]
    backendType: typing_extensions.Literal[
        "SQL_BACKEND_TYPE_UNSPECIFIED", "FIRST_GEN", "SECOND_GEN", "EXTERNAL"
    ]
    connectionName: str
    createTime: str
    currentDiskSize: str
    databaseInstalledVersion: str
    databaseVersion: typing_extensions.Literal[
        "SQL_DATABASE_VERSION_UNSPECIFIED",
        "MYSQL_5_1",
        "MYSQL_5_5",
        "MYSQL_5_6",
        "MYSQL_5_7",
        "MYSQL_8_0",
        "MYSQL_8_0_18",
        "MYSQL_8_0_26",
        "MYSQL_8_0_27",
        "MYSQL_8_0_28",
        "MYSQL_8_0_29",
        "MYSQL_8_0_30",
        "MYSQL_8_0_31",
        "MYSQL_8_0_32",
        "MYSQL_8_0_33",
        "MYSQL_8_0_34",
        "MYSQL_8_0_35",
        "MYSQL_8_0_36",
        "MYSQL_8_0_37",
        "MYSQL_8_0_38",
        "MYSQL_8_0_39",
        "MYSQL_8_0_40",
        "MYSQL_8_0_41",
        "MYSQL_8_0_42",
        "MYSQL_8_4",
        "SQLSERVER_2017_STANDARD",
        "SQLSERVER_2017_ENTERPRISE",
        "SQLSERVER_2017_EXPRESS",
        "SQLSERVER_2017_WEB",
        "POSTGRES_9_6",
        "POSTGRES_10",
        "POSTGRES_11",
        "POSTGRES_12",
        "POSTGRES_13",
        "POSTGRES_14",
        "POSTGRES_15",
        "POSTGRES_16",
        "POSTGRES_17",
        "SQLSERVER_2019_STANDARD",
        "SQLSERVER_2019_ENTERPRISE",
        "SQLSERVER_2019_EXPRESS",
        "SQLSERVER_2019_WEB",
        "SQLSERVER_2022_STANDARD",
        "SQLSERVER_2022_ENTERPRISE",
        "SQLSERVER_2022_EXPRESS",
        "SQLSERVER_2022_WEB",
    ]
    diskEncryptionConfiguration: DiskEncryptionConfiguration
    diskEncryptionStatus: DiskEncryptionStatus
    dnsName: str
    etag: str
    failoverReplica: dict[str, typing.Any]
    gceZone: str
    geminiConfig: GeminiInstanceConfig
    instanceType: typing_extensions.Literal[
        "SQL_INSTANCE_TYPE_UNSPECIFIED",
        "CLOUD_SQL_INSTANCE",
        "ON_PREMISES_INSTANCE",
        "READ_REPLICA_INSTANCE",
    ]
    ipAddresses: _list[IpMapping]
    ipv6Address: str
    kind: str
    maintenanceVersion: str
    masterInstanceName: str
    maxDiskSize: str
    name: str
    onPremisesConfiguration: OnPremisesConfiguration
    outOfDiskReport: SqlOutOfDiskReport
    primaryDnsName: str
    project: str
    pscServiceAttachmentLink: str
    region: str
    replicaConfiguration: ReplicaConfiguration
    replicaNames: _list[str]
    replicationCluster: ReplicationCluster
    rootPassword: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    scheduledMaintenance: SqlScheduledMaintenance
    secondaryGceZone: str
    selfLink: str
    serverCaCert: SslCert
    serviceAccountEmailAddress: str
    settings: Settings
    sqlNetworkArchitecture: typing_extensions.Literal[
        "SQL_NETWORK_ARCHITECTURE_UNSPECIFIED",
        "NEW_NETWORK_ARCHITECTURE",
        "OLD_NETWORK_ARCHITECTURE",
    ]
    state: typing_extensions.Literal[
        "SQL_INSTANCE_STATE_UNSPECIFIED",
        "RUNNABLE",
        "SUSPENDED",
        "PENDING_DELETE",
        "PENDING_CREATE",
        "MAINTENANCE",
        "FAILED",
        "ONLINE_MAINTENANCE",
    ]
    suspensionReason: _list[
        typing_extensions.Literal[
            "SQL_SUSPENSION_REASON_UNSPECIFIED",
            "BILLING_ISSUE",
            "LEGAL_ISSUE",
            "OPERATIONAL_ISSUE",
            "KMS_KEY_ISSUE",
        ]
    ]
    switchTransactionLogsToCloudStorageEnabled: bool
    tags: dict[str, typing.Any]
    upgradableDatabaseVersions: _list[AvailableDatabaseVersion]
    writeEndpoint: str

@typing.type_check_only
class DatabasesListResponse(typing_extensions.TypedDict, total=False):
    items: _list[Database]
    kind: str

@typing.type_check_only
class DemoteContext(typing_extensions.TypedDict, total=False):
    kind: str
    sourceRepresentativeInstanceName: str

@typing.type_check_only
class DemoteMasterConfiguration(typing_extensions.TypedDict, total=False):
    kind: str
    mysqlReplicaConfiguration: DemoteMasterMySqlReplicaConfiguration

@typing.type_check_only
class DemoteMasterContext(typing_extensions.TypedDict, total=False):
    kind: str
    masterInstanceName: str
    replicaConfiguration: DemoteMasterConfiguration
    skipReplicationSetup: bool
    verifyGtidConsistency: bool

@typing.type_check_only
class DemoteMasterMySqlReplicaConfiguration(typing_extensions.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str
    kind: str
    password: str
    username: str

@typing.type_check_only
class DenyMaintenancePeriod(typing_extensions.TypedDict, total=False):
    endDate: str
    startDate: str
    time: str

@typing.type_check_only
class DiskEncryptionConfiguration(typing_extensions.TypedDict, total=False):
    kind: str
    kmsKeyName: str

@typing.type_check_only
class DiskEncryptionStatus(typing_extensions.TypedDict, total=False):
    kind: str
    kmsKeyVersionName: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportContext(typing_extensions.TypedDict, total=False):
    bakExportOptions: dict[str, typing.Any]
    csvExportOptions: dict[str, typing.Any]
    databases: _list[str]
    fileType: typing_extensions.Literal[
        "SQL_FILE_TYPE_UNSPECIFIED", "SQL", "CSV", "BAK"
    ]
    kind: str
    offload: bool
    sqlExportOptions: dict[str, typing.Any]
    uri: str

@typing.type_check_only
class ExternalSyncSelectedObject(typing_extensions.TypedDict, total=False):
    database: str

@typing.type_check_only
class FailoverContext(typing_extensions.TypedDict, total=False):
    kind: str
    settingsVersion: str

@typing.type_check_only
class Flag(typing_extensions.TypedDict, total=False):
    allowedIntValues: _list[str]
    allowedStringValues: _list[str]
    appliesTo: _list[
        typing_extensions.Literal[
            "SQL_DATABASE_VERSION_UNSPECIFIED",
            "MYSQL_5_1",
            "MYSQL_5_5",
            "MYSQL_5_6",
            "MYSQL_5_7",
            "MYSQL_8_0",
            "MYSQL_8_0_18",
            "MYSQL_8_0_26",
            "MYSQL_8_0_27",
            "MYSQL_8_0_28",
            "MYSQL_8_0_29",
            "MYSQL_8_0_30",
            "MYSQL_8_0_31",
            "MYSQL_8_0_32",
            "MYSQL_8_0_33",
            "MYSQL_8_0_34",
            "MYSQL_8_0_35",
            "MYSQL_8_0_36",
            "MYSQL_8_0_37",
            "MYSQL_8_0_38",
            "MYSQL_8_0_39",
            "MYSQL_8_0_40",
            "MYSQL_8_0_41",
            "MYSQL_8_0_42",
            "MYSQL_8_4",
            "SQLSERVER_2017_STANDARD",
            "SQLSERVER_2017_ENTERPRISE",
            "SQLSERVER_2017_EXPRESS",
            "SQLSERVER_2017_WEB",
            "POSTGRES_9_6",
            "POSTGRES_10",
            "POSTGRES_11",
            "POSTGRES_12",
            "POSTGRES_13",
            "POSTGRES_14",
            "POSTGRES_15",
            "POSTGRES_16",
            "POSTGRES_17",
            "SQLSERVER_2019_STANDARD",
            "SQLSERVER_2019_ENTERPRISE",
            "SQLSERVER_2019_EXPRESS",
            "SQLSERVER_2019_WEB",
            "SQLSERVER_2022_STANDARD",
            "SQLSERVER_2022_ENTERPRISE",
            "SQLSERVER_2022_EXPRESS",
            "SQLSERVER_2022_WEB",
        ]
    ]
    inBeta: bool
    kind: str
    maxValue: str
    minValue: str
    name: str
    requiresRestart: bool
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

@typing.type_check_only
class FlagsListResponse(typing_extensions.TypedDict, total=False):
    items: _list[Flag]
    kind: str

@typing.type_check_only
class GeminiInstanceConfig(typing_extensions.TypedDict, total=False):
    activeQueryEnabled: bool
    entitled: bool
    flagRecommenderEnabled: bool
    googleVacuumMgmtEnabled: bool
    indexAdvisorEnabled: bool
    oomSessionCancelEnabled: bool

@typing.type_check_only
class GenerateEphemeralCertRequest(typing_extensions.TypedDict, total=False):
    access_token: str
    public_key: str
    readTime: str
    validDuration: str

@typing.type_check_only
class GenerateEphemeralCertResponse(typing_extensions.TypedDict, total=False):
    ephemeralCert: SslCert

@typing.type_check_only
class ImportContext(typing_extensions.TypedDict, total=False):
    bakImportOptions: dict[str, typing.Any]
    csvImportOptions: dict[str, typing.Any]
    database: str
    fileType: typing_extensions.Literal[
        "SQL_FILE_TYPE_UNSPECIFIED", "SQL", "CSV", "BAK"
    ]
    importUser: str
    kind: str
    sqlImportOptions: dict[str, typing.Any]
    uri: str

@typing.type_check_only
class InsightsConfig(typing_extensions.TypedDict, total=False):
    queryInsightsEnabled: bool
    queryPlansPerMinute: int
    queryStringLength: int
    recordApplicationTags: bool
    recordClientAddress: bool

@typing.type_check_only
class InstanceReference(typing_extensions.TypedDict, total=False):
    name: str
    project: str
    region: str

@typing.type_check_only
class InstancesAcquireSsrsLeaseRequest(typing_extensions.TypedDict, total=False):
    acquireSsrsLeaseContext: AcquireSsrsLeaseContext

@typing.type_check_only
class InstancesCloneRequest(typing_extensions.TypedDict, total=False):
    cloneContext: CloneContext

@typing.type_check_only
class InstancesDemoteMasterRequest(typing_extensions.TypedDict, total=False):
    demoteMasterContext: DemoteMasterContext

@typing.type_check_only
class InstancesDemoteRequest(typing_extensions.TypedDict, total=False):
    demoteContext: DemoteContext

@typing.type_check_only
class InstancesExportRequest(typing_extensions.TypedDict, total=False):
    exportContext: ExportContext

@typing.type_check_only
class InstancesFailoverRequest(typing_extensions.TypedDict, total=False):
    failoverContext: FailoverContext

@typing.type_check_only
class InstancesImportRequest(typing_extensions.TypedDict, total=False):
    importContext: ImportContext

@typing.type_check_only
class InstancesListResponse(typing_extensions.TypedDict, total=False):
    items: _list[DatabaseInstance]
    kind: str
    nextPageToken: str
    warnings: _list[ApiWarning]

@typing.type_check_only
class InstancesListServerCasResponse(typing_extensions.TypedDict, total=False):
    activeVersion: str
    certs: _list[SslCert]
    kind: str

@typing.type_check_only
class InstancesListServerCertificatesResponse(typing_extensions.TypedDict, total=False):
    activeVersion: str
    caCerts: _list[SslCert]
    kind: str
    serverCerts: _list[SslCert]

@typing.type_check_only
class InstancesReencryptRequest(typing_extensions.TypedDict, total=False):
    backupReencryptionConfig: BackupReencryptionConfig

@typing.type_check_only
class InstancesRestoreBackupRequest(typing_extensions.TypedDict, total=False):
    restoreBackupContext: RestoreBackupContext

@typing.type_check_only
class InstancesRotateServerCaRequest(typing_extensions.TypedDict, total=False):
    rotateServerCaContext: RotateServerCaContext

@typing.type_check_only
class InstancesRotateServerCertificateRequest(typing_extensions.TypedDict, total=False):
    rotateServerCertificateContext: RotateServerCertificateContext

@typing.type_check_only
class InstancesTruncateLogRequest(typing_extensions.TypedDict, total=False):
    truncateLogContext: TruncateLogContext

@typing.type_check_only
class IpConfiguration(typing_extensions.TypedDict, total=False):
    allocatedIpRange: str
    authorizedNetworks: _list[AclEntry]
    customSubjectAlternativeNames: _list[str]
    enablePrivatePathForGoogleCloudServices: bool
    ipv4Enabled: bool
    privateNetwork: str
    pscConfig: PscConfig
    requireSsl: bool
    serverCaMode: typing_extensions.Literal[
        "CA_MODE_UNSPECIFIED",
        "GOOGLE_MANAGED_INTERNAL_CA",
        "GOOGLE_MANAGED_CAS_CA",
        "CUSTOMER_MANAGED_CAS_CA",
    ]
    serverCaPool: str
    sslMode: typing_extensions.Literal[
        "SSL_MODE_UNSPECIFIED",
        "ALLOW_UNENCRYPTED_AND_ENCRYPTED",
        "ENCRYPTED_ONLY",
        "TRUSTED_CLIENT_CERTIFICATE_REQUIRED",
    ]

@typing.type_check_only
class IpMapping(typing_extensions.TypedDict, total=False):
    ipAddress: str
    timeToRetire: str
    type: typing_extensions.Literal[
        "SQL_IP_ADDRESS_TYPE_UNSPECIFIED",
        "PRIMARY",
        "OUTGOING",
        "PRIVATE",
        "MIGRATED_1ST_GEN",
    ]

@typing.type_check_only
class LocationPreference(typing_extensions.TypedDict, total=False):
    followGaeApplication: str
    kind: str
    secondaryZone: str
    zone: str

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    day: int
    hour: int
    kind: str
    updateTrack: typing_extensions.Literal[
        "SQL_UPDATE_TRACK_UNSPECIFIED", "canary", "stable", "week5"
    ]

@typing.type_check_only
class MySqlReplicaConfiguration(typing_extensions.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str
    connectRetryInterval: int
    dumpFilePath: str
    kind: str
    masterHeartbeatPeriod: str
    password: str
    sslCipher: str
    username: str
    verifyServerCertificate: bool

@typing.type_check_only
class MySqlSyncConfig(typing_extensions.TypedDict, total=False):
    initialSyncFlags: _list[SyncFlags]

@typing.type_check_only
class OnPremisesConfiguration(typing_extensions.TypedDict, total=False):
    caCertificate: str
    clientCertificate: str
    clientKey: str
    dumpFilePath: str
    hostPort: str
    kind: str
    password: str
    selectedObjects: _list[SelectedObjects]
    sourceInstance: InstanceReference
    sslOption: typing_extensions.Literal[
        "SSL_OPTION_UNSPECIFIED", "DISABLE", "REQUIRE", "VERIFY_CA"
    ]
    username: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    acquireSsrsLeaseContext: AcquireSsrsLeaseContext
    apiWarning: ApiWarning
    backupContext: BackupContext
    endTime: str
    error: OperationErrors
    exportContext: ExportContext
    importContext: ImportContext
    insertTime: str
    kind: str
    name: str
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
        "LOG_CLEANUP",
        "AUTO_RESTART",
        "REENCRYPT",
        "SWITCHOVER",
        "ACQUIRE_SSRS_LEASE",
        "RELEASE_SSRS_LEASE",
        "RECONFIGURE_OLD_PRIMARY",
        "CLUSTER_MAINTENANCE",
        "SELF_SERVICE_MAINTENANCE",
        "SWITCHOVER_TO_REPLICA",
        "MAJOR_VERSION_UPGRADE",
        "ADVANCED_BACKUP",
    ]
    selfLink: str
    startTime: str
    status: typing_extensions.Literal[
        "SQL_OPERATION_STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE"
    ]
    subOperationType: SqlSubOperationType
    targetId: str
    targetLink: str
    targetProject: str
    user: str

@typing.type_check_only
class OperationError(typing_extensions.TypedDict, total=False):
    code: str
    kind: str
    message: str

@typing.type_check_only
class OperationErrors(typing_extensions.TypedDict, total=False):
    errors: _list[OperationError]
    kind: str

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class OperationsListResponse(typing_extensions.TypedDict, total=False):
    items: _list[Operation]
    kind: str
    nextPageToken: str

@typing.type_check_only
class PasswordStatus(typing_extensions.TypedDict, total=False):
    locked: bool
    passwordExpirationTime: str

@typing.type_check_only
class PasswordValidationPolicy(typing_extensions.TypedDict, total=False):
    complexity: typing_extensions.Literal[
        "COMPLEXITY_UNSPECIFIED", "COMPLEXITY_DEFAULT"
    ]
    disallowCompromisedCredentials: bool
    disallowUsernameSubstring: bool
    enablePasswordPolicy: bool
    minLength: int
    passwordChangeInterval: str
    reuseInterval: int

@typing.type_check_only
class PerformDiskShrinkContext(typing_extensions.TypedDict, total=False):
    targetSizeGb: str

@typing.type_check_only
class PscAutoConnectionConfig(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    consumerNetworkStatus: str
    consumerProject: str
    ipAddress: str
    status: str

@typing.type_check_only
class PscConfig(typing_extensions.TypedDict, total=False):
    allowedConsumerProjects: _list[str]
    pscAutoConnections: _list[PscAutoConnectionConfig]
    pscEnabled: bool

@typing.type_check_only
class ReplicaConfiguration(typing_extensions.TypedDict, total=False):
    cascadableReplica: bool
    failoverTarget: bool
    kind: str
    mysqlReplicaConfiguration: MySqlReplicaConfiguration

@typing.type_check_only
class ReplicationCluster(typing_extensions.TypedDict, total=False):
    drReplica: bool
    failoverDrReplicaName: str
    psaWriteEndpoint: str

@typing.type_check_only
class Reschedule(typing_extensions.TypedDict, total=False):
    rescheduleType: typing_extensions.Literal[
        "RESCHEDULE_TYPE_UNSPECIFIED",
        "IMMEDIATE",
        "NEXT_AVAILABLE_WINDOW",
        "SPECIFIC_TIME",
    ]
    scheduleTime: str

@typing.type_check_only
class RestoreBackupContext(typing_extensions.TypedDict, total=False):
    backupRunId: str
    instanceId: str
    kind: str
    project: str

@typing.type_check_only
class RotateServerCaContext(typing_extensions.TypedDict, total=False):
    kind: str
    nextVersion: str

@typing.type_check_only
class RotateServerCertificateContext(typing_extensions.TypedDict, total=False):
    kind: str
    nextVersion: str

@typing.type_check_only
class SelectedObjects(typing_extensions.TypedDict, total=False):
    database: str

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    activationPolicy: typing_extensions.Literal[
        "SQL_ACTIVATION_POLICY_UNSPECIFIED", "ALWAYS", "NEVER", "ON_DEMAND"
    ]
    activeDirectoryConfig: SqlActiveDirectoryConfig
    advancedMachineFeatures: AdvancedMachineFeatures
    authorizedGaeApplications: _list[str]
    availabilityType: typing_extensions.Literal[
        "SQL_AVAILABILITY_TYPE_UNSPECIFIED", "ZONAL", "REGIONAL"
    ]
    backupConfiguration: BackupConfiguration
    collation: str
    connectorEnforcement: typing_extensions.Literal[
        "CONNECTOR_ENFORCEMENT_UNSPECIFIED", "NOT_REQUIRED", "REQUIRED"
    ]
    crashSafeReplicationEnabled: bool
    dataCacheConfig: DataCacheConfig
    dataDiskSizeGb: str
    dataDiskType: typing_extensions.Literal[
        "SQL_DATA_DISK_TYPE_UNSPECIFIED", "PD_SSD", "PD_HDD", "OBSOLETE_LOCAL_SSD"
    ]
    databaseFlags: _list[DatabaseFlags]
    databaseReplicationEnabled: bool
    deletionProtectionEnabled: bool
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    edition: typing_extensions.Literal[
        "EDITION_UNSPECIFIED", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    enableDataplexIntegration: bool
    enableGoogleMlIntegration: bool
    insightsConfig: InsightsConfig
    ipConfiguration: IpConfiguration
    kind: str
    locationPreference: LocationPreference
    maintenanceWindow: MaintenanceWindow
    passwordValidationPolicy: PasswordValidationPolicy
    pricingPlan: typing_extensions.Literal[
        "SQL_PRICING_PLAN_UNSPECIFIED", "PACKAGE", "PER_USE"
    ]
    replicationType: typing_extensions.Literal[
        "SQL_REPLICATION_TYPE_UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
    ]
    settingsVersion: str
    sqlServerAuditConfig: SqlServerAuditConfig
    storageAutoResize: bool
    storageAutoResizeLimit: str
    tier: str
    timeZone: str
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class SqlActiveDirectoryConfig(typing_extensions.TypedDict, total=False):
    domain: str
    kind: str

@typing.type_check_only
class SqlExternalSyncSettingError(typing_extensions.TypedDict, total=False):
    detail: str
    kind: str
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
        "UNSUPPORTED_TABLE_DEFINITION",
        "UNSUPPORTED_DEFINER",
        "SQLSERVER_SERVERNAME_MISMATCH",
        "PRIMARY_ALREADY_SETUP",
        "UNSUPPORTED_BINLOG_FORMAT",
        "BINLOG_RETENTION_SETTING",
        "UNSUPPORTED_STORAGE_ENGINE",
        "LIMITED_SUPPORT_TABLES",
        "EXISTING_DATA_IN_REPLICA",
        "MISSING_OPTIONAL_PRIVILEGES",
        "RISKY_BACKUP_ADMIN_PRIVILEGE",
        "INSUFFICIENT_GCS_PERMISSIONS",
        "INVALID_FILE_INFO",
        "UNSUPPORTED_DATABASE_SETTINGS",
        "MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE",
        "LOCAL_INFILE_OFF",
        "TURN_ON_PITR_AFTER_PROMOTE",
        "INCOMPATIBLE_DATABASE_MINOR_VERSION",
        "SOURCE_MAX_SUBSCRIPTIONS",
        "UNABLE_TO_VERIFY_DEFINERS",
        "SUBSCRIPTION_CALCULATION_STATUS",
        "PG_SUBSCRIPTION_COUNT",
        "PG_SYNC_PARALLEL_LEVEL",
        "INSUFFICIENT_DISK_SIZE",
        "INSUFFICIENT_MACHINE_TIER",
        "UNSUPPORTED_EXTENSIONS_NOT_MIGRATED",
        "EXTENSIONS_NOT_MIGRATED",
        "PG_CRON_FLAG_ENABLED_IN_REPLICA",
        "EXTENSIONS_NOT_ENABLED_IN_REPLICA",
        "UNSUPPORTED_COLUMNS",
        "USERS_NOT_CREATED_IN_REPLICA",
        "UNSUPPORTED_SYSTEM_OBJECTS",
        "UNSUPPORTED_TABLES_WITH_REPLICA_IDENTITY",
        "SELECTED_OBJECTS_NOT_EXIST_ON_SOURCE",
    ]

@typing.type_check_only
class SqlInstancesAcquireSsrsLeaseResponse(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class SqlInstancesGetDiskShrinkConfigResponse(typing_extensions.TypedDict, total=False):
    kind: str
    message: str
    minimalTargetSizeGb: str

@typing.type_check_only
class SqlInstancesGetLatestRecoveryTimeResponse(
    typing_extensions.TypedDict, total=False
):
    kind: str
    latestRecoveryTime: str

@typing.type_check_only
class SqlInstancesReleaseSsrsLeaseResponse(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class SqlInstancesRescheduleMaintenanceRequestBody(
    typing_extensions.TypedDict, total=False
):
    reschedule: Reschedule

@typing.type_check_only
class SqlInstancesResetReplicaSizeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SqlInstancesStartExternalSyncRequest(typing_extensions.TypedDict, total=False):
    migrationType: typing_extensions.Literal[
        "MIGRATION_TYPE_UNSPECIFIED", "LOGICAL", "PHYSICAL"
    ]
    mysqlSyncConfig: MySqlSyncConfig
    skipVerification: bool
    syncMode: typing_extensions.Literal[
        "EXTERNAL_SYNC_MODE_UNSPECIFIED", "ONLINE", "OFFLINE"
    ]
    syncParallelLevel: typing_extensions.Literal[
        "EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED", "MIN", "OPTIMAL", "MAX"
    ]

@typing.type_check_only
class SqlInstancesVerifyExternalSyncSettingsRequest(
    typing_extensions.TypedDict, total=False
):
    migrationType: typing_extensions.Literal[
        "MIGRATION_TYPE_UNSPECIFIED", "LOGICAL", "PHYSICAL"
    ]
    mysqlSyncConfig: MySqlSyncConfig
    selectedObjects: _list[ExternalSyncSelectedObject]
    syncMode: typing_extensions.Literal[
        "EXTERNAL_SYNC_MODE_UNSPECIFIED", "ONLINE", "OFFLINE"
    ]
    syncParallelLevel: typing_extensions.Literal[
        "EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED", "MIN", "OPTIMAL", "MAX"
    ]
    verifyConnectionOnly: bool
    verifyReplicationOnly: bool

@typing.type_check_only
class SqlInstancesVerifyExternalSyncSettingsResponse(
    typing_extensions.TypedDict, total=False
):
    errors: _list[SqlExternalSyncSettingError]
    kind: str
    warnings: _list[SqlExternalSyncSettingError]

@typing.type_check_only
class SqlOutOfDiskReport(typing_extensions.TypedDict, total=False):
    sqlMinRecommendedIncreaseSizeGb: int
    sqlOutOfDiskState: typing_extensions.Literal[
        "SQL_OUT_OF_DISK_STATE_UNSPECIFIED", "NORMAL", "SOFT_SHUTDOWN"
    ]

@typing.type_check_only
class SqlScheduledMaintenance(typing_extensions.TypedDict, total=False):
    canDefer: bool
    canReschedule: bool
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class SqlServerAuditConfig(typing_extensions.TypedDict, total=False):
    bucket: str
    kind: str
    retentionInterval: str
    uploadInterval: str

@typing.type_check_only
class SqlServerDatabaseDetails(typing_extensions.TypedDict, total=False):
    compatibilityLevel: int
    recoveryModel: str

@typing.type_check_only
class SqlServerUserDetails(typing_extensions.TypedDict, total=False):
    disabled: bool
    serverRoles: _list[str]

@typing.type_check_only
class SqlSubOperationType(typing_extensions.TypedDict, total=False):
    maintenanceType: typing_extensions.Literal[
        "SQL_MAINTENANCE_TYPE_UNSPECIFIED",
        "INSTANCE_MAINTENANCE",
        "REPLICA_INCLUDED_MAINTENANCE",
        "INSTANCE_SELF_SERVICE_MAINTENANCE",
        "REPLICA_INCLUDED_SELF_SERVICE_MAINTENANCE",
    ]

@typing.type_check_only
class SslCert(typing_extensions.TypedDict, total=False):
    cert: str
    certSerialNumber: str
    commonName: str
    createTime: str
    expirationTime: str
    instance: str
    kind: str
    selfLink: str
    sha1Fingerprint: str

@typing.type_check_only
class SslCertDetail(typing_extensions.TypedDict, total=False):
    certInfo: SslCert
    certPrivateKey: str

@typing.type_check_only
class SslCertsCreateEphemeralRequest(typing_extensions.TypedDict, total=False):
    access_token: str
    public_key: str

@typing.type_check_only
class SslCertsInsertRequest(typing_extensions.TypedDict, total=False):
    commonName: str

@typing.type_check_only
class SslCertsInsertResponse(typing_extensions.TypedDict, total=False):
    clientCert: SslCertDetail
    kind: str
    operation: Operation
    serverCaCert: SslCert

@typing.type_check_only
class SslCertsListResponse(typing_extensions.TypedDict, total=False):
    items: _list[SslCert]
    kind: str

@typing.type_check_only
class SyncFlags(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Tier(typing_extensions.TypedDict, total=False):
    DiskQuota: str
    RAM: str
    kind: str
    region: _list[str]
    tier: str

@typing.type_check_only
class TiersListResponse(typing_extensions.TypedDict, total=False):
    items: _list[Tier]
    kind: str

@typing.type_check_only
class TruncateLogContext(typing_extensions.TypedDict, total=False):
    kind: str
    logType: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    dualPasswordType: typing_extensions.Literal[
        "DUAL_PASSWORD_TYPE_UNSPECIFIED",
        "NO_MODIFY_DUAL_PASSWORD",
        "NO_DUAL_PASSWORD",
        "DUAL_PASSWORD",
    ]
    etag: str
    host: str
    instance: str
    kind: str
    name: str
    password: str
    passwordPolicy: UserPasswordValidationPolicy
    project: str
    sqlserverUserDetails: SqlServerUserDetails
    type: typing_extensions.Literal[
        "BUILT_IN",
        "CLOUD_IAM_USER",
        "CLOUD_IAM_SERVICE_ACCOUNT",
        "CLOUD_IAM_GROUP",
        "CLOUD_IAM_GROUP_USER",
        "CLOUD_IAM_GROUP_SERVICE_ACCOUNT",
    ]

@typing.type_check_only
class UserPasswordValidationPolicy(typing_extensions.TypedDict, total=False):
    allowedFailedAttempts: int
    enableFailedAttemptsCheck: bool
    enablePasswordVerification: bool
    passwordExpirationDuration: str
    status: PasswordStatus

@typing.type_check_only
class UsersListResponse(typing_extensions.TypedDict, total=False):
    items: _list[User]
    kind: str
    nextPageToken: str
