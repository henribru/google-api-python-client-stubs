import typing

_list = list

@typing.type_check_only
class AllConnectionStrings(typing.TypedDict, total=False):
    high: str
    low: str
    medium: str

@typing.type_check_only
class AmazonS3IcebergStorage(typing.TypedDict, total=False):
    accessKeyId: str
    bucket: str
    endpoint: str
    region: str
    schemeType: typing.Literal["SCHEME_TYPE_UNSPECIFIED", "S3", "S3A"]
    secretAccessKeySecret: str

@typing.type_check_only
class AutonomousDatabase(typing.TypedDict, total=False):
    adminPassword: str
    adminPasswordSecretVersion: str
    cidr: str
    createTime: str
    database: str
    disasterRecoverySupportedLocations: _list[str]
    displayName: str
    entitlementId: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    odbNetwork: str
    odbSubnet: str
    peerAutonomousDatabases: _list[str]
    properties: AutonomousDatabaseProperties
    sourceConfig: SourceConfig

@typing.type_check_only
class AutonomousDatabaseApex(typing.TypedDict, total=False):
    apexVersion: str
    ordsVersion: str

@typing.type_check_only
class AutonomousDatabaseBackup(typing.TypedDict, total=False):
    autonomousDatabase: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    properties: AutonomousDatabaseBackupProperties

@typing.type_check_only
class AutonomousDatabaseBackupProperties(typing.TypedDict, total=False):
    availableTillTime: str
    compartmentId: str
    databaseSizeTb: float
    dbVersion: str
    endTime: str
    isAutomaticBackup: bool
    isLongTermBackup: bool
    isRestorable: bool
    keyStoreId: str
    keyStoreWallet: str
    kmsKeyId: str
    kmsKeyVersionId: str
    lifecycleDetails: str
    lifecycleState: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "DELETING",
        "DELETED",
        "FAILED",
        "UPDATING",
    ]
    ocid: str
    retentionPeriodDays: int
    sizeTb: float
    startTime: str
    type: typing.Literal["TYPE_UNSPECIFIED", "INCREMENTAL", "FULL", "LONG_TERM"]
    vaultId: str

@typing.type_check_only
class AutonomousDatabaseCharacterSet(typing.TypedDict, total=False):
    characterSet: str
    characterSetType: typing.Literal[
        "CHARACTER_SET_TYPE_UNSPECIFIED", "DATABASE", "NATIONAL"
    ]
    name: str

@typing.type_check_only
class AutonomousDatabaseConnectionStrings(typing.TypedDict, total=False):
    allConnectionStrings: AllConnectionStrings
    dedicated: str
    high: str
    low: str
    medium: str
    profiles: _list[DatabaseConnectionStringProfile]

@typing.type_check_only
class AutonomousDatabaseConnectionUrls(typing.TypedDict, total=False):
    apexUri: str
    databaseTransformsUri: str
    graphStudioUri: str
    machineLearningNotebookUri: str
    machineLearningUserManagementUri: str
    mongoDbUri: str
    ordsUri: str
    sqlDevWebUri: str

@typing.type_check_only
class AutonomousDatabaseProperties(typing.TypedDict, total=False):
    actualUsedDataStorageSizeTb: float
    allocatedStorageSizeTb: float
    allowlistedIps: _list[str]
    apexDetails: AutonomousDatabaseApex
    arePrimaryAllowlistedIpsUsed: bool
    autonomousContainerDatabaseId: str
    availableUpgradeVersions: _list[str]
    backupRetentionPeriodDays: int
    characterSet: str
    computeCount: float
    connectionStrings: AutonomousDatabaseConnectionStrings
    connectionUrls: AutonomousDatabaseConnectionUrls
    cpuCoreCount: int
    customerContacts: _list[CustomerContact]
    dataGuardRoleChangedTime: str
    dataSafeState: typing.Literal[
        "DATA_SAFE_STATE_UNSPECIFIED",
        "REGISTERING",
        "REGISTERED",
        "DEREGISTERING",
        "NOT_REGISTERED",
        "FAILED",
    ]
    dataStorageSizeGb: int
    dataStorageSizeTb: int
    databaseManagementState: typing.Literal[
        "DATABASE_MANAGEMENT_STATE_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    ]
    dbEdition: typing.Literal[
        "DATABASE_EDITION_UNSPECIFIED", "STANDARD_EDITION", "ENTERPRISE_EDITION"
    ]
    dbVersion: str
    dbWorkload: typing.Literal["DB_WORKLOAD_UNSPECIFIED", "OLTP", "DW", "AJD", "APEX"]
    disasterRecoveryRoleChangedTime: str
    encryptionKey: EncryptionKey
    encryptionKeyHistoryEntries: _list[EncryptionKeyHistoryEntry]
    failedDataRecoveryDuration: str
    isAutoScalingEnabled: bool
    isLocalDataGuardEnabled: bool
    isStorageAutoScalingEnabled: bool
    licenseType: typing.Literal[
        "LICENSE_TYPE_UNSPECIFIED", "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
    ]
    lifecycleDetails: str
    localAdgAutoFailoverMaxDataLossLimit: int
    localAdgAutoFailoverMaxDataLossLimitDuration: int
    localDataGuardEnabled: bool
    localDisasterRecoveryType: typing.Literal[
        "LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED",
        "ADG",
        "BACKUP_BASED",
        "NOT_AVAILABLE",
    ]
    localStandbyDb: AutonomousDatabaseStandbySummary
    maintenanceBeginTime: str
    maintenanceEndTime: str
    maintenanceScheduleType: typing.Literal[
        "MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED", "EARLY", "REGULAR"
    ]
    memoryPerOracleComputeUnitGbs: int
    memoryTableGbs: int
    mtlsConnectionRequired: bool
    nCharacterSet: str
    nextLongTermBackupTime: str
    ociUrl: str
    ocid: str
    openMode: typing.Literal["OPEN_MODE_UNSPECIFIED", "READ_ONLY", "READ_WRITE"]
    operationsInsightsState: typing.Literal[
        "OPERATIONS_INSIGHTS_STATE_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    ]
    peerDbIds: _list[str]
    permissionLevel: typing.Literal[
        "PERMISSION_LEVEL_UNSPECIFIED", "RESTRICTED", "UNRESTRICTED"
    ]
    privateEndpoint: str
    privateEndpointIp: str
    privateEndpointLabel: str
    refreshableClone: bool
    refreshableMode: typing.Literal[
        "REFRESHABLE_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    refreshableState: typing.Literal[
        "REFRESHABLE_STATE_UNSPECIFIED", "REFRESHING", "NOT_REFRESHING"
    ]
    role: typing.Literal[
        "ROLE_UNSPECIFIED",
        "PRIMARY",
        "STANDBY",
        "DISABLED_STANDBY",
        "BACKUP_COPY",
        "SNAPSHOT_STANDBY",
    ]
    scheduledOperationDetails: _list[ScheduledOperationDetails]
    secretId: str
    serviceAgentEmail: str
    sqlWebDeveloperUrl: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "STOPPING",
        "STOPPED",
        "STARTING",
        "TERMINATING",
        "TERMINATED",
        "UNAVAILABLE",
        "RESTORE_IN_PROGRESS",
        "RESTORE_FAILED",
        "BACKUP_IN_PROGRESS",
        "SCALE_IN_PROGRESS",
        "AVAILABLE_NEEDS_ATTENTION",
        "UPDATING",
        "MAINTENANCE_IN_PROGRESS",
        "RESTARTING",
        "RECREATING",
        "ROLE_CHANGE_IN_PROGRESS",
        "UPGRADING",
        "INACCESSIBLE",
        "STANDBY",
    ]
    supportedCloneRegions: _list[str]
    totalAutoBackupStorageSizeGbs: float
    usedDataStorageSizeTbs: int
    vaultId: str

@typing.type_check_only
class AutonomousDatabaseRefreshableClone(typing.TypedDict, total=False):
    name: str
    region: str

@typing.type_check_only
class AutonomousDatabaseRefreshableClones(typing.TypedDict, total=False):
    autonomousDatabaseRefreshableClones: _list[AutonomousDatabaseRefreshableClone]

@typing.type_check_only
class AutonomousDatabaseStandbySummary(typing.TypedDict, total=False):
    dataGuardRoleChangedTime: str
    disasterRecoveryRoleChangedTime: str
    lagTimeDuration: str
    lifecycleDetails: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "STOPPING",
        "STOPPED",
        "STARTING",
        "TERMINATING",
        "TERMINATED",
        "UNAVAILABLE",
        "RESTORE_IN_PROGRESS",
        "RESTORE_FAILED",
        "BACKUP_IN_PROGRESS",
        "SCALE_IN_PROGRESS",
        "AVAILABLE_NEEDS_ATTENTION",
        "UPDATING",
        "MAINTENANCE_IN_PROGRESS",
        "RESTARTING",
        "RECREATING",
        "ROLE_CHANGE_IN_PROGRESS",
        "UPGRADING",
        "INACCESSIBLE",
        "STANDBY",
    ]

@typing.type_check_only
class AutonomousDbVersion(typing.TypedDict, total=False):
    dbWorkload: typing.Literal["DB_WORKLOAD_UNSPECIFIED", "OLTP", "DW", "AJD", "APEX"]
    name: str
    version: str
    workloadUri: str

@typing.type_check_only
class AzureDataLakeStorageIcebergStorage(typing.TypedDict, total=False):
    accountKeySecret: str
    azureAccount: str
    container: str
    endpoint: str

@typing.type_check_only
class BackupDestinationDetails(typing.TypedDict, total=False):
    type: typing.Literal[
        "BACKUP_DESTINATION_TYPE_UNSPECIFIED",
        "NFS",
        "RECOVERY_APPLIANCE",
        "OBJECT_STORE",
        "LOCAL",
        "DBRS",
    ]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloudAccountDetails(typing.TypedDict, total=False):
    accountCreationUri: str
    cloudAccount: str
    cloudAccountHomeRegion: str
    linkExistingAccountUri: str

@typing.type_check_only
class CloudExadataInfrastructure(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    entitlementId: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    properties: CloudExadataInfrastructureProperties

@typing.type_check_only
class CloudExadataInfrastructureProperties(typing.TypedDict, total=False):
    activatedStorageCount: int
    additionalStorageCount: int
    availableStorageSizeGb: int
    computeCount: int
    computeModel: typing.Literal[
        "COMPUTE_MODEL_UNSPECIFIED", "COMPUTE_MODEL_ECPU", "COMPUTE_MODEL_OCPU"
    ]
    cpuCount: int
    customerContacts: _list[CustomerContact]
    dataStorageSizeTb: float
    databaseServerType: str
    dbNodeStorageSizeGb: int
    dbServerVersion: str
    exascaleConfig: ExascaleConfig
    maintenanceWindow: MaintenanceWindow
    maxCpuCount: int
    maxDataStorageTb: float
    maxDbNodeStorageSizeGb: int
    maxMemoryGb: int
    memorySizeGb: int
    monthlyDbServerVersion: str
    monthlyStorageServerVersion: str
    nextMaintenanceRunId: str
    nextMaintenanceRunTime: str
    nextSecurityMaintenanceRunTime: str
    ociUrl: str
    ocid: str
    shape: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
        "MAINTENANCE_IN_PROGRESS",
    ]
    storageCount: int
    storageServerType: str
    storageServerVersion: str
    totalStorageSizeGb: int

@typing.type_check_only
class CloudVmCluster(typing.TypedDict, total=False):
    backupOdbSubnet: str
    backupSubnetCidr: str
    cidr: str
    createTime: str
    displayName: str
    exadataInfrastructure: str
    exascaleDbStorageVault: str
    gcpOracleZone: str
    identityConnector: IdentityConnector
    labels: dict[str, typing.Any]
    name: str
    network: str
    odbNetwork: str
    odbSubnet: str
    properties: CloudVmClusterProperties

@typing.type_check_only
class CloudVmClusterProperties(typing.TypedDict, total=False):
    clusterName: str
    compartmentId: str
    computeModel: typing.Literal[
        "COMPUTE_MODEL_UNSPECIFIED", "COMPUTE_MODEL_ECPU", "COMPUTE_MODEL_OCPU"
    ]
    cpuCoreCount: int
    dataStorageSizeTb: float
    dbNodeStorageSizeGb: int
    dbServerOcids: _list[str]
    diagnosticsDataCollectionOptions: DataCollectionOptions
    diskRedundancy: typing.Literal["DISK_REDUNDANCY_UNSPECIFIED", "HIGH", "NORMAL"]
    dnsListenerIp: str
    domain: str
    giVersion: str
    hostname: str
    hostnamePrefix: str
    licenseType: typing.Literal[
        "LICENSE_TYPE_UNSPECIFIED", "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
    ]
    localBackupEnabled: bool
    memorySizeGb: int
    nodeCount: int
    ociUrl: str
    ocid: str
    ocpuCount: float
    scanDns: str
    scanDnsRecordId: str
    scanIpIds: _list[str]
    scanListenerPortTcp: int
    scanListenerPortTcpSsl: int
    shape: str
    sparseDiskgroupEnabled: bool
    sshPublicKeys: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
        "MAINTENANCE_IN_PROGRESS",
    ]
    storageManagementType: typing.Literal[
        "STORAGE_MANAGEMENT_TYPE_UNSPECIFIED", "ASM", "EXASCALE"
    ]
    storageSizeGb: int
    systemVersion: str
    timeZone: TimeZone
    vmBackupStorageType: typing.Literal[
        "VM_BACKUP_STORAGE_TYPE_UNSPECIFIED",
        "VM_BACKUP_STORAGE_TYPE_LOCAL",
        "VM_BACKUP_STORAGE_TYPE_EXASCALE",
    ]
    vmFileSystemStorageType: typing.Literal[
        "VM_FILE_SYSTEM_STORAGE_TYPE_UNSPECIFIED",
        "VM_FILE_SYSTEM_STORAGE_TYPE_LOCAL",
        "VM_FILE_SYSTEM_STORAGE_TYPE_EXASCALE",
    ]

@typing.type_check_only
class ConfigureExascaleCloudExadataInfrastructureRequest(typing.TypedDict, total=False):
    requestId: str
    totalStorageSizeGb: int
    totalVmStorageSizeGb: int

@typing.type_check_only
class CustomerContact(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class DataCollectionOptions(typing.TypedDict, total=False):
    diagnosticsEventsEnabled: bool
    healthMonitoringEnabled: bool
    incidentLogsEnabled: bool

@typing.type_check_only
class DataCollectionOptionsCommon(typing.TypedDict, total=False):
    isDiagnosticsEventsEnabled: bool
    isHealthMonitoringEnabled: bool
    isIncidentLogsEnabled: bool

@typing.type_check_only
class DataCollectionOptionsDbSystem(typing.TypedDict, total=False):
    isDiagnosticsEventsEnabled: bool
    isIncidentLogsEnabled: bool

@typing.type_check_only
class Database(typing.TypedDict, total=False):
    adminPassword: str
    adminPasswordSecretVersion: str
    characterSet: str
    createTime: str
    databaseId: str
    dbHomeName: str
    dbName: str
    dbUniqueName: str
    gcpOracleZone: str
    name: str
    ncharacterSet: str
    ociUrl: str
    opsInsightsStatus: typing.Literal[
        "OPERATIONS_INSIGHTS_STATUS_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    ]
    pluggableDatabaseId: str
    pluggableDatabaseName: str
    properties: DatabaseProperties
    tdeWalletPassword: str
    tdeWalletPasswordSecretVersion: str

@typing.type_check_only
class DatabaseCharacterSet(typing.TypedDict, total=False):
    characterSet: str
    characterSetType: typing.Literal[
        "CHARACTER_SET_TYPE_UNSPECIFIED", "DATABASE", "NATIONAL"
    ]
    name: str

@typing.type_check_only
class DatabaseConnectionStringProfile(typing.TypedDict, total=False):
    consumerGroup: typing.Literal[
        "CONSUMER_GROUP_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "TP", "TPURGENT"
    ]
    displayName: str
    hostFormat: typing.Literal["HOST_FORMAT_UNSPECIFIED", "FQDN", "IP"]
    isRegional: bool
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "TCP", "TCPS"]
    sessionMode: typing.Literal["SESSION_MODE_UNSPECIFIED", "DIRECT", "INDIRECT"]
    syntaxFormat: typing.Literal[
        "SYNTAX_FORMAT_UNSPECIFIED", "LONG", "EZCONNECT", "EZCONNECTPLUS"
    ]
    tlsAuthentication: typing.Literal[
        "TLS_AUTHENTICATION_UNSPECIFIED", "SERVER", "MUTUAL"
    ]
    value: str

@typing.type_check_only
class DatabaseManagementConfig(typing.TypedDict, total=False):
    managementState: typing.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
        "UPDATING",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
        "FAILED_UPDATING",
    ]
    managementType: typing.Literal["MANAGEMENT_TYPE_UNSPECIFIED", "BASIC", "ADVANCED"]

@typing.type_check_only
class DatabaseProperties(typing.TypedDict, total=False):
    databaseManagementConfig: DatabaseManagementConfig
    dbBackupConfig: DbBackupConfig
    dbVersion: str
    state: typing.Literal[
        "DATABASE_LIFECYCLE_STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "BACKUP_IN_PROGRESS",
        "UPGRADING",
        "CONVERTING",
        "TERMINATING",
        "TERMINATED",
        "RESTORE_FAILED",
        "FAILED",
    ]

@typing.type_check_only
class DbBackupConfig(typing.TypedDict, total=False):
    autoBackupEnabled: bool
    autoFullBackupDay: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    autoFullBackupWindow: typing.Literal[
        "BACKUP_WINDOW_UNSPECIFIED",
        "SLOT_ONE",
        "SLOT_TWO",
        "SLOT_THREE",
        "SLOT_FOUR",
        "SLOT_FIVE",
        "SLOT_SIX",
        "SLOT_SEVEN",
        "SLOT_EIGHT",
        "SLOT_NINE",
        "SLOT_TEN",
        "SLOT_ELEVEN",
        "SLOT_TWELVE",
    ]
    autoIncrementalBackupWindow: typing.Literal[
        "BACKUP_WINDOW_UNSPECIFIED",
        "SLOT_ONE",
        "SLOT_TWO",
        "SLOT_THREE",
        "SLOT_FOUR",
        "SLOT_FIVE",
        "SLOT_SIX",
        "SLOT_SEVEN",
        "SLOT_EIGHT",
        "SLOT_NINE",
        "SLOT_TEN",
        "SLOT_ELEVEN",
        "SLOT_TWELVE",
    ]
    backupDeletionPolicy: typing.Literal[
        "BACKUP_DELETION_POLICY_UNSPECIFIED",
        "DELETE_IMMEDIATELY",
        "DELETE_AFTER_RETENTION_PERIOD",
    ]
    backupDestinationDetails: _list[BackupDestinationDetails]
    retentionPeriodDays: int

@typing.type_check_only
class DbHome(typing.TypedDict, total=False):
    database: Database
    dbVersion: str
    displayName: str
    isUnifiedAuditingEnabled: bool

@typing.type_check_only
class DbNode(typing.TypedDict, total=False):
    name: str
    properties: DbNodeProperties

@typing.type_check_only
class DbNodeProperties(typing.TypedDict, total=False):
    createTime: str
    dbNodeStorageSizeGb: int
    dbServerOcid: str
    hostname: str
    memorySizeGb: int
    ocid: str
    ocpuCount: int
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "STOPPING",
        "STOPPED",
        "STARTING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
    ]
    totalCpuCoreCount: int

@typing.type_check_only
class DbServer(typing.TypedDict, total=False):
    displayName: str
    name: str
    properties: DbServerProperties

@typing.type_check_only
class DbServerProperties(typing.TypedDict, total=False):
    dbNodeIds: _list[str]
    dbNodeStorageSizeGb: int
    maxDbNodeStorageSizeGb: int
    maxMemorySizeGb: int
    maxOcpuCount: int
    memorySizeGb: int
    ocid: str
    ocpuCount: int
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "AVAILABLE",
        "UNAVAILABLE",
        "DELETING",
        "DELETED",
    ]
    vmCount: int

@typing.type_check_only
class DbSystem(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    entitlementId: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    ociUrl: str
    odbNetwork: str
    odbSubnet: str
    properties: DbSystemProperties

@typing.type_check_only
class DbSystemInitialStorageSize(typing.TypedDict, total=False):
    name: str
    properties: DbSystemInitialStorageSizeProperties

@typing.type_check_only
class DbSystemInitialStorageSizeProperties(typing.TypedDict, total=False):
    launchFromBackupStorageSizeDetails: _list[StorageSizeDetails]
    shapeType: typing.Literal["SHAPE_TYPE_UNSPECIFIED", "STANDARD_X86"]
    storageManagement: typing.Literal["STORAGE_MANAGEMENT_UNSPECIFIED", "ASM", "LVM"]
    storageSizeDetails: _list[StorageSizeDetails]

@typing.type_check_only
class DbSystemOptions(typing.TypedDict, total=False):
    storageManagement: typing.Literal["STORAGE_MANAGEMENT_UNSPECIFIED", "ASM", "LVM"]

@typing.type_check_only
class DbSystemProperties(typing.TypedDict, total=False):
    computeCount: int
    computeModel: typing.Literal["COMPUTE_MODEL_UNSPECIFIED", "ECPU", "OCPU"]
    dataCollectionOptions: DataCollectionOptionsDbSystem
    dataStorageSizeGb: int
    databaseEdition: typing.Literal[
        "DB_SYSTEM_DATABASE_EDITION_UNSPECIFIED",
        "STANDARD_EDITION",
        "ENTERPRISE_EDITION",
        "ENTERPRISE_EDITION_HIGH_PERFORMANCE",
    ]
    dbHome: DbHome
    dbSystemOptions: DbSystemOptions
    domain: str
    hostname: str
    hostnamePrefix: str
    initialDataStorageSizeGb: int
    licenseModel: typing.Literal[
        "LICENSE_MODEL_UNSPECIFIED", "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
    ]
    lifecycleState: typing.Literal[
        "DB_SYSTEM_LIFECYCLE_STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
        "MIGRATED",
        "MAINTENANCE_IN_PROGRESS",
        "NEEDS_ATTENTION",
        "UPGRADING",
    ]
    memorySizeGb: int
    nodeCount: int
    ocid: str
    privateIp: str
    recoStorageSizeGb: int
    shape: str
    sshPublicKeys: _list[str]
    timeZone: TimeZone

@typing.type_check_only
class DbSystemShape(typing.TypedDict, total=False):
    availableCoreCount: int
    availableCoreCountPerNode: int
    availableDataStorageTb: int
    availableMemoryPerNodeGb: int
    coreCountIncrement: int
    maxNodeCount: int
    maxStorageCount: int
    minCoreCountPerNode: int
    minDbNodeStoragePerNodeGb: int
    minMemoryPerNodeGb: int
    minNodeCount: int
    minStorageCount: int
    minimumCoreCount: int
    name: str
    shape: str

@typing.type_check_only
class DbVersion(typing.TypedDict, total=False):
    name: str
    properties: DbVersionProperties

@typing.type_check_only
class DbVersionProperties(typing.TypedDict, total=False):
    isLatestForMajorVersion: bool
    isPreviewDbVersion: bool
    isUpgradeSupported: bool
    supportsPdb: bool
    version: str

@typing.type_check_only
class DefinedTagValue(typing.TypedDict, total=False):
    tags: dict[str, typing.Any]

@typing.type_check_only
class DeploymentDiagnosticData(typing.TypedDict, total=False):
    bucket: str
    diagnosticEndTime: str
    diagnosticStartTime: str
    diagnosticState: typing.Literal[
        "DIAGNOSTIC_STATE_UNSPECIFIED", "IN_PROGRESS", "SUCCEEDED", "FAILED"
    ]
    namespace: str
    object: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionKey(typing.TypedDict, total=False):
    kmsKey: str
    provider: typing.Literal["PROVIDER_UNSPECIFIED", "GOOGLE_MANAGED", "ORACLE_MANAGED"]

@typing.type_check_only
class EncryptionKeyHistoryEntry(typing.TypedDict, total=False):
    activationTime: str
    encryptionKey: EncryptionKey

@typing.type_check_only
class Entitlement(typing.TypedDict, total=False):
    cloudAccountDetails: CloudAccountDetails
    entitlementId: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACCOUNT_NOT_LINKED",
        "ACCOUNT_NOT_ACTIVE",
        "ACTIVE",
        "ACCOUNT_SUSPENDED",
        "NOT_APPROVED_IN_PRIVATE_MARKETPLACE",
    ]

@typing.type_check_only
class ExadbVmCluster(typing.TypedDict, total=False):
    backupOdbSubnet: str
    createTime: str
    displayName: str
    entitlementId: str
    gcpOracleZone: str
    identityConnector: IdentityConnector
    labels: dict[str, typing.Any]
    name: str
    odbNetwork: str
    odbSubnet: str
    properties: ExadbVmClusterProperties

@typing.type_check_only
class ExadbVmClusterProperties(typing.TypedDict, total=False):
    additionalEcpuCountPerNode: int
    clusterName: str
    dataCollectionOptions: DataCollectionOptionsCommon
    enabledEcpuCountPerNode: int
    exascaleDbStorageVault: str
    giVersion: str
    gridImageId: str
    hostname: str
    hostnamePrefix: str
    licenseModel: typing.Literal[
        "LICENSE_MODEL_UNSPECIFIED", "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
    ]
    lifecycleState: typing.Literal[
        "EXADB_VM_CLUSTER_LIFECYCLE_STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
        "MAINTENANCE_IN_PROGRESS",
    ]
    memorySizeGb: int
    nodeCount: int
    ociUri: str
    scanListenerPortTcp: int
    shapeAttribute: typing.Literal[
        "SHAPE_ATTRIBUTE_UNSPECIFIED", "SMART_STORAGE", "BLOCK_STORAGE"
    ]
    sshPublicKeys: _list[str]
    timeZone: TimeZone
    vmFileSystemStorage: ExadbVmClusterStorageDetails

@typing.type_check_only
class ExadbVmClusterStorageDetails(typing.TypedDict, total=False):
    sizeInGbsPerNode: int

@typing.type_check_only
class ExascaleConfig(typing.TypedDict, total=False):
    availableStorageSizeGb: int
    availableVmStorageSizeGb: int
    totalStorageSizeGb: int
    totalVmStorageSizeGb: int

@typing.type_check_only
class ExascaleDbStorageDetails(typing.TypedDict, total=False):
    availableSizeGbs: int
    totalSizeGbs: int

@typing.type_check_only
class ExascaleDbStorageVault(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    entitlementId: str
    exadataInfrastructure: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    properties: ExascaleDbStorageVaultProperties

@typing.type_check_only
class ExascaleDbStorageVaultProperties(typing.TypedDict, total=False):
    additionalFlashCachePercent: int
    attachedShapeAttributes: _list[
        typing.Literal["SHAPE_ATTRIBUTE_UNSPECIFIED", "SMART_STORAGE", "BLOCK_STORAGE"]
    ]
    availableShapeAttributes: _list[
        typing.Literal["SHAPE_ATTRIBUTE_UNSPECIFIED", "SMART_STORAGE", "BLOCK_STORAGE"]
    ]
    description: str
    exascaleDbStorageDetails: ExascaleDbStorageDetails
    ociUri: str
    ocid: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
    ]
    timeZone: TimeZone
    vmClusterCount: int
    vmClusterIds: _list[str]

@typing.type_check_only
class FailoverAutonomousDatabaseRequest(typing.TypedDict, total=False):
    peerAutonomousDatabase: str

@typing.type_check_only
class GenerateAutonomousDatabaseWalletRequest(typing.TypedDict, total=False):
    isRegional: bool
    password: str
    type: typing.Literal["GENERATE_TYPE_UNSPECIFIED", "ALL", "SINGLE"]

@typing.type_check_only
class GenerateAutonomousDatabaseWalletResponse(typing.TypedDict, total=False):
    archiveContent: str

@typing.type_check_only
class GiVersion(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class GlueIcebergCatalog(typing.TypedDict, total=False):
    glueId: str

@typing.type_check_only
class GoldengateAmazonKinesisConnectionProperties(typing.TypedDict, total=False):
    accessKeyId: str
    awsRegion: str
    endpoint: str
    secretAccessKeySecret: str
    technologyType: str

@typing.type_check_only
class GoldengateAmazonRedshiftConnectionProperties(typing.TypedDict, total=False):
    connectionUrl: str
    password: str
    passwordSecretVersion: str
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateAmazonS3ConnectionProperties(typing.TypedDict, total=False):
    accessKeyId: str
    endpoint: str
    region: str
    secretAccessKeySecret: str
    technologyType: str

@typing.type_check_only
class GoldengateAzureDataLakeStorageConnectionProperties(typing.TypedDict, total=False):
    account: str
    accountKeySecret: str
    authenticationType: typing.Literal[
        "AUTHENTICATION_TYPE_UNSPECIFIED",
        "SHARED_KEY",
        "SHARED_ACCESS_SIGNATURE",
        "AZURE_ACTIVE_DIRECTORY",
    ]
    azureAuthorityHost: str
    azureTenantId: str
    clientId: str
    clientSecret: str
    endpoint: str
    sasTokenSecret: str
    technologyType: str

@typing.type_check_only
class GoldengateAzureSynapseAnalyticsConnectionProperties(
    typing.TypedDict, total=False
):
    connectionString: str
    password: str
    passwordSecretVersion: str
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateBackupSchedule(typing.TypedDict, total=False):
    backupScheduledTime: str
    bucket: str
    compartmentId: str
    frequencyBackupScheduled: typing.Literal[
        "FREQUENCY_BACKUP_SCHEDULED_UNSPECIFIED", "DAILY", "WEEKLY", "MONTHLY"
    ]
    metadataOnly: bool
    namespace: str

@typing.type_check_only
class GoldengateConnection(typing.TypedDict, total=False):
    createTime: str
    entitlementId: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    ociUrl: str
    odbNetwork: str
    odbSubnet: str
    properties: GoldengateConnectionProperties

@typing.type_check_only
class GoldengateConnectionAssignment(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    entitlementId: str
    labels: dict[str, typing.Any]
    name: str
    properties: GoldengateConnectionAssignmentProperties

@typing.type_check_only
class GoldengateConnectionAssignmentProperties(typing.TypedDict, total=False):
    alias: str
    goldengateConnection: str
    goldengateDeployment: str
    ocid: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING"
    ]

@typing.type_check_only
class GoldengateConnectionProperties(typing.TypedDict, total=False):
    amazonKinesisConnectionProperties: GoldengateAmazonKinesisConnectionProperties
    amazonRedshiftConnectionProperties: GoldengateAmazonRedshiftConnectionProperties
    amazonS3ConnectionProperties: GoldengateAmazonS3ConnectionProperties
    azureDataLakeStorageConnectionProperties: (
        GoldengateAzureDataLakeStorageConnectionProperties
    )
    azureSynapseAnalyticsConnectionProperties: (
        GoldengateAzureSynapseAnalyticsConnectionProperties
    )
    connectionType: typing.Literal[
        "GOLDENGATE_CONNECTION_TYPE_UNSPECIFIED",
        "GOLDENGATE",
        "KAFKA",
        "KAFKA_SCHEMA_REGISTRY",
        "MYSQL",
        "JAVA_MESSAGE_SERVICE",
        "MICROSOFT_SQLSERVER",
        "OCI_OBJECT_STORAGE",
        "ORACLE",
        "AZURE_DATA_LAKE_STORAGE",
        "POSTGRESQL",
        "AZURE_SYNAPSE_ANALYTICS",
        "SNOWFLAKE",
        "AMAZON_S3",
        "HDFS",
        "ORACLE_AI_DATA_PLATFORM",
        "ORACLE_NOSQL",
        "MONGODB",
        "AMAZON_KINESIS",
        "AMAZON_REDSHIFT",
        "DB2",
        "REDIS",
        "ELASTICSEARCH",
        "GENERIC",
        "GOOGLE_CLOUD_STORAGE",
        "GOOGLE_BIGQUERY",
        "DATABRICKS",
        "GOOGLE_PUBSUB",
        "MICROSOFT_FABRIC",
        "ICEBERG",
    ]
    databricksConnectionProperties: GoldengateDatabricksConnectionProperties
    db2ConnectionProperties: GoldengateDb2ConnectionProperties
    description: str
    displayName: str
    elasticsearchConnectionProperties: GoldengateElasticsearchConnectionProperties
    genericConnectionProperties: GoldengateGenericConnectionProperties
    goldengateConnectionProperties: GoldengateGoldengateConnectionProperties
    googleBigQueryConnectionProperties: GoldengateGoogleBigQueryConnectionProperties
    googleCloudStorageConnectionProperties: (
        GoldengateGoogleCloudStorageConnectionProperties
    )
    googlePubsubConnectionProperties: GoldengateGooglePubsubConnectionProperties
    hdfsConnectionProperties: GoldengateHdfsConnectionProperties
    icebergConnectionProperties: GoldengateIcebergConnectionProperties
    ingressIpAddresses: _list[str]
    javaMessageServiceConnectionProperties: (
        GoldengateJavaMessageServiceConnectionProperties
    )
    kafkaConnectionProperties: GoldengateKafkaConnectionProperties
    kafkaSchemaRegistryConnectionProperties: (
        GoldengateKafkaSchemaRegistryConnectionProperties
    )
    lifecycleDetails: str
    lifecycleState: typing.Literal[
        "GOLDENGATE_CONNECTION_LIFECYCLE_STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "DELETED",
        "FAILED",
    ]
    microsoftFabricConnectionProperties: GoldengateMicrosoftFabricConnectionProperties
    microsoftSqlserverConnectionProperties: (
        GoldengateMicrosoftSqlserverConnectionProperties
    )
    mongodbConnectionProperties: GoldengateMongodbConnectionProperties
    mysqlConnectionProperties: GoldengateMysqlConnectionProperties
    ociObjectStorageConnectionProperties: GoldengateOciObjectStorageConnectionProperties
    ocid: str
    oracleAiDataPlatformConnectionProperties: (
        GoldengateOracleAIDataPlatformConnectionProperties
    )
    oracleConnectionProperties: GoldengateOracleConnectionProperties
    oracleNosqlConnectionProperties: GoldengateOracleNosqlConnectionProperties
    postgresqlConnectionProperties: GoldengatePostgresqlConnectionProperties
    redisConnectionProperties: GoldengateRedisConnectionProperties
    routingMethod: typing.Literal[
        "GOLDENGATE_CONNECTION_ROUTING_METHOD_UNSPECIFIED",
        "SHARED_DEPLOYMENT_ENDPOINT",
        "DEDICATED_ENDPOINT",
    ]
    snowflakeConnectionProperties: GoldengateSnowflakeConnectionProperties
    updateTime: str

@typing.type_check_only
class GoldengateConnectionType(typing.TypedDict, total=False):
    connectionType: typing.Literal[
        "CONNECTION_TYPE_UNSPECIFIED",
        "GOLDENGATE",
        "KAFKA",
        "KAFKA_SCHEMA_REGISTRY",
        "MYSQL",
        "JAVA_MESSAGE_SERVICE",
        "MICROSOFT_SQLSERVER",
        "OCI_OBJECT_STORAGE",
        "ORACLE",
        "AZURE_DATA_LAKE_STORAGE",
        "POSTGRESQL",
        "AZURE_SYNAPSE_ANALYTICS",
        "SNOWFLAKE",
        "AMAZON_S3",
        "HDFS",
        "ORACLE_AI_DATA_PLATFORM",
        "ORACLE_NOSQL",
        "MONGODB",
        "AMAZON_KINESIS",
        "AMAZON_REDSHIFT",
        "DB2",
        "REDIS",
        "ELASTICSEARCH",
        "GENERIC",
        "GOOGLE_CLOUD_STORAGE",
        "GOOGLE_BIGQUERY",
        "DATABRICKS",
        "GOOGLE_PUBSUB",
        "MICROSOFT_FABRIC",
        "ICEBERG",
    ]
    name: str
    technologyTypes: _list[str]

@typing.type_check_only
class GoldengateDatabricksConnectionProperties(typing.TypedDict, total=False):
    authenticationType: typing.Literal[
        "DATABRICKS_AUTHENTICATION_TYPE_UNSPECIFIED",
        "PERSONAL_ACCESS_TOKEN",
        "OAUTH_M2M",
    ]
    clientId: str
    clientSecret: str
    connectionUrl: str
    password: str
    passwordSecretVersion: str
    storageCredential: str
    technologyType: str

@typing.type_check_only
class GoldengateDb2ConnectionProperties(typing.TypedDict, total=False):
    additionalAttributes: _list[NameValuePair]
    database: str
    host: str
    password: str
    passwordSecretVersion: str
    port: int
    securityProtocol: typing.Literal[
        "DB2_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS"
    ]
    sslClientKeystashFile: str
    sslClientKeystoredbFile: str
    sslServerCertificateFile: str
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateDeployment(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    entitlementId: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    ociUrl: str
    odbNetwork: str
    odbSubnet: str
    properties: GoldengateDeploymentProperties

@typing.type_check_only
class GoldengateDeploymentEnvironment(typing.TypedDict, total=False):
    autoScalingEnabled: bool
    category: typing.Literal[
        "DEPLOYMENT_CATEGORY_UNSPECIFIED",
        "DATA_REPLICATION_CATEGORY",
        "DATA_TRANSFORMS_CATEGORY",
    ]
    defaultCpuCoreCount: int
    displayName: str
    environmentType: typing.Literal[
        "DEPLOYMENT_ENVIRONMENT_TYPE_UNSPECIFIED",
        "PRODUCTION",
        "DEVELOPMENT_OR_TESTING",
    ]
    maxCpuCoreCount: int
    memoryGbPerCpuCore: int
    minCpuCoreCount: int
    name: str
    networkBandwidthGbpsPerCpuCore: int
    storageUsageLimitGbPerCpuCore: int

@typing.type_check_only
class GoldengateDeploymentLock(typing.TypedDict, total=False):
    compartmentId: str
    createTime: str
    message: str
    relatedResourceId: str
    type: typing.Literal["LOCK_TYPE_UNSPECIFIED", "FULL", "DELETE"]

@typing.type_check_only
class GoldengateDeploymentProperties(typing.TypedDict, total=False):
    backupSchedule: GoldengateBackupSchedule
    category: typing.Literal[
        "GOLDENGATE_DEPLOYMENT_CATEGORY_UNSPECIFIED",
        "DATA_REPLICATION",
        "DATA_TRANSFORMS",
    ]
    cpuCoreCount: int
    deploymentBackupId: str
    deploymentDiagnosticData: DeploymentDiagnosticData
    deploymentRole: typing.Literal[
        "GOLDENGATE_DEPLOYMENT_ROLE_TYPE_UNSPECIFIED", "PRIMARY", "STANDBY"
    ]
    deploymentType: str
    deploymentUrl: str
    description: str
    environmentType: str
    fqdn: str
    healthy: bool
    ingressIps: _list[IngressIp]
    isAutoScalingEnabled: bool
    isLatestVersion: bool
    isPublic: bool
    isStorageUtilizationLimitExceeded: bool
    lastBackupScheduleTime: str
    licenseModel: typing.Literal[
        "LICENSE_MODEL_UNSPECIFIED", "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
    ]
    lifecycleDetails: str
    lifecycleState: typing.Literal[
        "GOLDENGATE_DEPLOYMENT_LIFECYCLE_STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "ACTIVE",
        "INACTIVE",
        "DELETING",
        "DELETED",
        "FAILED",
        "NEEDS_ATTENTION",
        "IN_PROGRESS",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
        "WAITING",
    ]
    lifecycleSubState: typing.Literal[
        "GOLDENGATE_DEPLOYMENT_LIFECYCLE_SUB_STATE_UNSPECIFIED",
        "RECOVERING",
        "STARTING",
        "STOPPING",
        "MOVING",
        "UPGRADING",
        "RESTORING",
        "BACKING_UP",
        "ROLLING_BACK",
    ]
    loadBalancerId: str
    loadBalancerSubnetId: str
    locks: _list[GoldengateDeploymentLock]
    maintenanceConfig: GoldengateMaintenanceConfig
    maintenanceWindow: GoldengateMaintenanceWindow
    nextBackupScheduleTime: str
    nextMaintenanceActionType: typing.Literal[
        "NEXT_MAINTENANCE_ACTION_TYPE_UNSPECIFIED", "UPGRADE"
    ]
    nextMaintenanceDescription: str
    nextMaintenanceTime: str
    nsgIds: _list[str]
    ocid: str
    oggData: GoldengateOggDeployment
    oggVersionSupportEndTime: str
    placements: _list[GoldengatePlacement]
    privateIpAddress: str
    publicIpAddress: str
    roleChangeTime: str
    storageUtilizationBytes: str
    updateTime: str
    upgradeRequiredTime: str

@typing.type_check_only
class GoldengateDeploymentType(typing.TypedDict, total=False):
    category: typing.Literal[
        "DEPLOYMENT_CATEGORY_UNSPECIFIED",
        "DATA_REPLICATION_CATEGORY",
        "DATA_TRANSFORMS_CATEGORY",
    ]
    connectionTypes: _list[str]
    defaultUsername: str
    deploymentType: typing.Literal[
        "DEPLOYMENT_TYPE_UNSPECIFIED",
        "OGG",
        "DATABASE_ORACLE",
        "BIGDATA",
        "DATABASE_MICROSOFT_SQLSERVER",
        "DATABASE_MYSQL",
        "DATABASE_POSTGRESQL",
        "DATABASE_DB2ZOS",
        "DATABASE_DB2I",
        "GGSA",
        "DATA_TRANSFORMS",
    ]
    displayName: str
    name: str
    oggVersion: str
    sourceTechnologies: _list[str]
    supportedCapabilities: _list[str]
    supportedTechnologiesUrl: str
    targetTechnologies: _list[str]

@typing.type_check_only
class GoldengateDeploymentVersion(typing.TypedDict, total=False):
    name: str
    ocid: str
    properties: GoldengateDeploymentVersionProperties

@typing.type_check_only
class GoldengateDeploymentVersionProperties(typing.TypedDict, total=False):
    deploymentType: typing.Literal[
        "DEPLOYMENT_TYPE_UNSPECIFIED",
        "OGG",
        "DATABASE_ORACLE",
        "BIGDATA",
        "DATABASE_MICROSOFT_SQLSERVER",
        "DATABASE_MYSQL",
        "DATABASE_POSTGRESQL",
        "DATABASE_DB2ZOS",
        "DATABASE_DB2I",
        "GGSA",
        "DATA_TRANSFORMS",
    ]
    oggVersion: str
    releaseTime: str
    releaseType: typing.Literal[
        "DEPLOYMENT_RELEASE_TYPE_UNSPECIFIED", "MAJOR", "BUNDLE", "MINOR"
    ]
    securityFix: bool
    supportEndTime: str

@typing.type_check_only
class GoldengateElasticsearchConnectionProperties(typing.TypedDict, total=False):
    authenticationType: typing.Literal[
        "ELASTICSEARCH_AUTHENTICATION_TYPE_UNSPECIFIED", "NONE", "BASIC"
    ]
    fingerprint: str
    password: str
    passwordSecretVersion: str
    securityProtocol: typing.Literal[
        "ELASTICSEARCH_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS"
    ]
    servers: str
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateGenericConnectionProperties(typing.TypedDict, total=False):
    host: str
    technologyType: str

@typing.type_check_only
class GoldengateGoldengateConnectionProperties(typing.TypedDict, total=False):
    goldengateDeploymentId: str
    host: str
    password: str
    passwordSecretVersion: str
    port: int
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateGoogleBigQueryConnectionProperties(typing.TypedDict, total=False):
    serviceAccountKeyFile: str
    technologyType: str

@typing.type_check_only
class GoldengateGoogleCloudStorageConnectionProperties(typing.TypedDict, total=False):
    serviceAccountKeyFile: str
    technologyType: str

@typing.type_check_only
class GoldengateGooglePubsubConnectionProperties(typing.TypedDict, total=False):
    serviceAccountKeyFile: str
    technologyType: str

@typing.type_check_only
class GoldengateGroupToRolesMapping(typing.TypedDict, total=False):
    administratorGroupId: str
    operatorGroupId: str
    securityGroupId: str
    userGroupId: str

@typing.type_check_only
class GoldengateHdfsConnectionProperties(typing.TypedDict, total=False):
    coreSiteXml: str
    technologyType: str

@typing.type_check_only
class GoldengateIcebergConnectionProperties(typing.TypedDict, total=False):
    catalog: IcebergCatalog
    storage: IcebergStorage
    technologyType: str

@typing.type_check_only
class GoldengateJavaMessageServiceConnectionProperties(typing.TypedDict, total=False):
    authenticationType: typing.Literal[
        "JMS_AUTHENTICATION_TYPE_UNSPECIFIED", "NONE", "BASIC"
    ]
    connectionFactory: str
    connectionUrl: str
    jndiConnectionFactory: str
    jndiInitialContextFactory: str
    jndiProviderUrl: str
    jndiSecurityCredentialsSecret: str
    jndiSecurityPrincipal: str
    keyStoreFile: str
    keyStorePassword: str
    keyStorePasswordSecretVersion: str
    password: str
    passwordSecretVersion: str
    securityProtocol: typing.Literal[
        "JMS_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS", "MTLS"
    ]
    sslKeyPassword: str
    sslKeyPasswordSecretVersion: str
    technologyType: str
    trustStoreFile: str
    trustStorePassword: str
    trustStorePasswordSecretVersion: str
    useJndi: bool
    username: str

@typing.type_check_only
class GoldengateKafkaConnectionProperties(typing.TypedDict, total=False):
    bootstrapServers: _list[KafkaBootstrapServer]
    clusterId: str
    consumerPropertiesFile: str
    keyStoreFile: str
    keyStorePassword: str
    keyStorePasswordSecretVersion: str
    password: str
    passwordSecretVersion: str
    producerPropertiesFile: str
    securityProtocol: typing.Literal[
        "KAFKA_SECURITY_PROTOCOL_UNSPECIFIED",
        "SSL",
        "SASL_SSL",
        "PLAINTEXT",
        "SASL_PLAINTEXT",
    ]
    sslKeyPassword: str
    sslKeyPasswordSecretVersion: str
    streamPoolId: str
    technologyType: str
    trustStoreFile: str
    trustStorePassword: str
    trustStorePasswordSecretVersion: str
    useResourcePrincipal: bool
    username: str

@typing.type_check_only
class GoldengateKafkaSchemaRegistryConnectionProperties(typing.TypedDict, total=False):
    authenticationType: typing.Literal[
        "AUTHENTICATION_TYPE_UNSPECIFIED", "NONE", "BASIC", "MUTUAL"
    ]
    keyStoreFile: str
    keyStorePassword: str
    keyStorePasswordSecretVersion: str
    password: str
    passwordSecretVersion: str
    sslKeyPassword: str
    sslKeyPasswordSecretVersion: str
    technologyType: str
    trustStoreFile: str
    trustStorePassword: str
    trustStorePasswordSecretVersion: str
    url: str
    username: str

@typing.type_check_only
class GoldengateMaintenanceConfig(typing.TypedDict, total=False):
    bundleReleaseUpgradePeriodDays: int
    interimReleaseUpgradePeriodDays: int
    isInterimReleaseAutoUpgradeEnabled: bool
    majorReleaseUpgradePeriodDays: int
    securityPatchUpgradePeriodDays: int

@typing.type_check_only
class GoldengateMaintenanceWindow(typing.TypedDict, total=False):
    day: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    startHour: int

@typing.type_check_only
class GoldengateMicrosoftFabricConnectionProperties(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    endpoint: str
    technologyType: str
    tenantId: str

@typing.type_check_only
class GoldengateMicrosoftSqlserverConnectionProperties(typing.TypedDict, total=False):
    additionalAttributes: _list[NameValuePair]
    database: str
    host: str
    password: str
    passwordSecretVersion: str
    port: int
    securityProtocol: typing.Literal[
        "MICROSOFT_SQLSERVER_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS"
    ]
    serverCertificateValidationRequired: bool
    sslCaFile: str
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateMongodbConnectionProperties(typing.TypedDict, total=False):
    connectionString: str
    databaseId: str
    password: str
    passwordSecretVersion: str
    securityProtocol: typing.Literal[
        "MONGODB_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS", "MTLS"
    ]
    technologyType: str
    tlsCaFile: str
    tlsCertificateKeyFile: str
    tlsCertificateKeyFilePassword: str
    tlsCertificateKeyFilePasswordSecretVersion: str
    username: str

@typing.type_check_only
class GoldengateMysqlConnectionProperties(typing.TypedDict, total=False):
    additionalAttributes: _list[NameValuePair]
    database: str
    dbSystemId: str
    host: str
    password: str
    passwordSecretVersion: str
    port: int
    securityProtocol: typing.Literal[
        "MYSQL_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS", "MTLS"
    ]
    sslCaFile: str
    sslCertFile: str
    sslCrlFile: str
    sslKeyFile: str
    sslMode: typing.Literal[
        "SSL_MODE_UNSPECIFIED",
        "DISABLED",
        "PREFERRED",
        "REQUIRED",
        "VERIFY_CA",
        "VERIFY_IDENTITY",
    ]
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateOciObjectStorageConnectionProperties(typing.TypedDict, total=False):
    privateKeyFile: str
    privateKeyPassphraseSecret: str
    publicKeyFingerprint: str
    region: str
    technologyType: str
    tenancyId: str
    useResourcePrincipal: bool
    userId: str

@typing.type_check_only
class GoldengateOggDeployment(typing.TypedDict, total=False):
    adminPassword: str
    adminPasswordSecretVersion: str
    adminUsername: str
    certificate: str
    credentialStore: typing.Literal["CREDENTIAL_STORE_UNSPECIFIED", "GOLDENGATE", "IAM"]
    deployment: str
    groupRolesMapping: GoldengateGroupToRolesMapping
    identityDomainId: str
    oggVersion: str
    passwordSecretId: str

@typing.type_check_only
class GoldengateOracleAIDataPlatformConnectionProperties(typing.TypedDict, total=False):
    connectionUrl: str
    privateKeyFile: str
    privateKeyPassphraseSecret: str
    publicKeyFingerprint: str
    region: str
    technologyType: str
    tenancyId: str
    useResourcePrincipal: bool
    userId: str

@typing.type_check_only
class GoldengateOracleConnectionProperties(typing.TypedDict, total=False):
    authenticationMode: typing.Literal[
        "ORACLE_AUTHENTICATION_MODE_UNSPECIFIED", "TLS", "MTLS"
    ]
    connectionString: str
    gcpOracleDatabaseId: str
    password: str
    passwordSecretVersion: str
    sessionMode: typing.Literal["SESSION_MODE_UNSPECIFIED", "DIRECT", "REDIRECT"]
    technologyType: str
    username: str
    walletFile: str

@typing.type_check_only
class GoldengateOracleNosqlConnectionProperties(typing.TypedDict, total=False):
    privateKeyFile: str
    privateKeyPassphraseSecret: str
    publicKeyFingerprint: str
    region: str
    technologyType: str
    tenancyId: str
    useResourcePrincipal: bool
    userId: str

@typing.type_check_only
class GoldengatePlacement(typing.TypedDict, total=False):
    availabilityDomain: str
    faultDomain: str

@typing.type_check_only
class GoldengatePostgresqlConnectionProperties(typing.TypedDict, total=False):
    additionalAttributes: _list[NameValuePair]
    database: str
    dbSystemId: str
    host: str
    password: str
    passwordSecretVersion: str
    port: int
    securityProtocol: typing.Literal[
        "POSTGRESQL_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS", "MTLS"
    ]
    sslCaFile: str
    sslCertFile: str
    sslCrlFile: str
    sslKeyFile: str
    sslMode: typing.Literal[
        "POSTGRESQL_SSL_MODE_UNSPECIFIED",
        "PREFER",
        "REQUIRE",
        "VERIFY_CA",
        "VERIFY_FULL",
    ]
    technologyType: str
    username: str

@typing.type_check_only
class GoldengateRedisConnectionProperties(typing.TypedDict, total=False):
    authenticationType: typing.Literal[
        "REDIS_AUTHENTICATION_TYPE_UNSPECIFIED", "NONE", "BASIC"
    ]
    keyStoreFile: str
    keyStorePassword: str
    keyStorePasswordSecretVersion: str
    password: str
    passwordSecretVersion: str
    redisClusterId: str
    securityProtocol: typing.Literal[
        "REDIS_SECURITY_PROTOCOL_UNSPECIFIED", "PLAIN", "TLS", "MTLS"
    ]
    servers: str
    technologyType: str
    trustStoreFile: str
    trustStorePassword: str
    trustStorePasswordSecretVersion: str
    username: str

@typing.type_check_only
class GoldengateSnowflakeConnectionProperties(typing.TypedDict, total=False):
    authenticationType: typing.Literal[
        "AUTHENTICATION_TYPE_UNSPECIFIED", "BASIC", "KEY_PAIR"
    ]
    connectionUrl: str
    password: str
    passwordSecretVersion: str
    privateKeyFile: str
    privateKeyPassphraseSecret: str
    technologyType: str
    username: str

@typing.type_check_only
class GoogleCloudStorageIcebergStorage(typing.TypedDict, total=False):
    bucket: str
    projectId: str
    serviceAccountKeyFile: str

@typing.type_check_only
class IcebergCatalog(typing.TypedDict, total=False):
    catalogType: typing.Literal[
        "CATALOG_TYPE_UNSPECIFIED", "GLUE", "HADOOP", "NESSIE", "POLARIS", "REST"
    ]
    glueIcebergCatalog: GlueIcebergCatalog
    nessieIcebergCatalog: NessieIcebergCatalog
    polarisIcebergCatalog: PolarisIcebergCatalog
    restIcebergCatalog: RestIcebergCatalog

@typing.type_check_only
class IcebergStorage(typing.TypedDict, total=False):
    amazonS3IcebergStorage: AmazonS3IcebergStorage
    azureDataLakeStorageIcebergStorage: AzureDataLakeStorageIcebergStorage
    googleCloudStorageIcebergStorage: GoogleCloudStorageIcebergStorage
    storageType: typing.Literal[
        "STORAGE_TYPE_UNSPECIFIED",
        "AMAZON_S3",
        "GOOGLE_CLOUD_STORAGE",
        "AZURE_DATA_LAKE_STORAGE",
    ]

@typing.type_check_only
class IdentityConnector(typing.TypedDict, total=False):
    connectionState: typing.Literal[
        "CONNECTION_STATE_UNSPECIFIED",
        "CONNECTED",
        "PARTIALLY_CONNECTED",
        "DISCONNECTED",
        "UNKNOWN",
    ]
    serviceAgentEmail: str

@typing.type_check_only
class IngressIp(typing.TypedDict, total=False):
    ingressIpAddress: str

@typing.type_check_only
class KafkaBootstrapServer(typing.TypedDict, total=False):
    host: str
    port: int
    privateIpAddress: str

@typing.type_check_only
class ListAutonomousDatabaseBackupsResponse(typing.TypedDict, total=False):
    autonomousDatabaseBackups: _list[AutonomousDatabaseBackup]
    nextPageToken: str

@typing.type_check_only
class ListAutonomousDatabaseCharacterSetsResponse(typing.TypedDict, total=False):
    autonomousDatabaseCharacterSets: _list[AutonomousDatabaseCharacterSet]
    nextPageToken: str

@typing.type_check_only
class ListAutonomousDatabasesResponse(typing.TypedDict, total=False):
    autonomousDatabases: _list[AutonomousDatabase]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListAutonomousDbVersionsResponse(typing.TypedDict, total=False):
    autonomousDbVersions: _list[AutonomousDbVersion]
    nextPageToken: str

@typing.type_check_only
class ListCloudExadataInfrastructuresResponse(typing.TypedDict, total=False):
    cloudExadataInfrastructures: _list[CloudExadataInfrastructure]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCloudVmClustersResponse(typing.TypedDict, total=False):
    cloudVmClusters: _list[CloudVmCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDatabaseCharacterSetsResponse(typing.TypedDict, total=False):
    databaseCharacterSets: _list[DatabaseCharacterSet]
    nextPageToken: str

@typing.type_check_only
class ListDatabasesResponse(typing.TypedDict, total=False):
    databases: _list[Database]
    nextPageToken: str

@typing.type_check_only
class ListDbNodesResponse(typing.TypedDict, total=False):
    dbNodes: _list[DbNode]
    nextPageToken: str

@typing.type_check_only
class ListDbServersResponse(typing.TypedDict, total=False):
    dbServers: _list[DbServer]
    nextPageToken: str

@typing.type_check_only
class ListDbSystemInitialStorageSizesResponse(typing.TypedDict, total=False):
    dbSystemInitialStorageSizes: _list[DbSystemInitialStorageSize]
    nextPageToken: str

@typing.type_check_only
class ListDbSystemShapesResponse(typing.TypedDict, total=False):
    dbSystemShapes: _list[DbSystemShape]
    nextPageToken: str

@typing.type_check_only
class ListDbSystemsResponse(typing.TypedDict, total=False):
    dbSystems: _list[DbSystem]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDbVersionsResponse(typing.TypedDict, total=False):
    dbVersions: _list[DbVersion]
    nextPageToken: str

@typing.type_check_only
class ListEntitlementsResponse(typing.TypedDict, total=False):
    entitlements: _list[Entitlement]
    nextPageToken: str

@typing.type_check_only
class ListExadbVmClustersResponse(typing.TypedDict, total=False):
    exadbVmClusters: _list[ExadbVmCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExascaleDbStorageVaultsResponse(typing.TypedDict, total=False):
    exascaleDbStorageVaults: _list[ExascaleDbStorageVault]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGiVersionsResponse(typing.TypedDict, total=False):
    giVersions: _list[GiVersion]
    nextPageToken: str

@typing.type_check_only
class ListGoldengateConnectionAssignmentsResponse(typing.TypedDict, total=False):
    goldengateConnectionAssignments: _list[GoldengateConnectionAssignment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoldengateConnectionTypesResponse(typing.TypedDict, total=False):
    goldengateConnectionTypes: _list[GoldengateConnectionType]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoldengateConnectionsResponse(typing.TypedDict, total=False):
    goldengateConnections: _list[GoldengateConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoldengateDeploymentEnvironmentsResponse(typing.TypedDict, total=False):
    goldengateDeploymentEnvironments: _list[GoldengateDeploymentEnvironment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoldengateDeploymentTypesResponse(typing.TypedDict, total=False):
    goldengateDeploymentTypes: _list[GoldengateDeploymentType]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoldengateDeploymentVersionsResponse(typing.TypedDict, total=False):
    goldengateDeploymentVersions: _list[GoldengateDeploymentVersion]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGoldengateDeploymentsResponse(typing.TypedDict, total=False):
    goldengateDeployments: _list[GoldengateDeployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMinorVersionsResponse(typing.TypedDict, total=False):
    minorVersions: _list[MinorVersion]
    nextPageToken: str

@typing.type_check_only
class ListOdbNetworksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    odbNetworks: _list[OdbNetwork]
    unreachable: _list[str]

@typing.type_check_only
class ListOdbSubnetsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    odbSubnets: _list[OdbSubnet]
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPluggableDatabasesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    pluggableDatabases: _list[PluggableDatabase]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    gcpOracleZones: _list[str]

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    customActionTimeoutMins: int
    daysOfWeek: _list[
        typing.Literal[
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]
    hoursOfDay: _list[int]
    isCustomActionTimeoutEnabled: bool
    leadTimeWeek: int
    months: _list[
        typing.Literal[
            "MONTH_UNSPECIFIED",
            "JANUARY",
            "FEBRUARY",
            "MARCH",
            "APRIL",
            "MAY",
            "JUNE",
            "JULY",
            "AUGUST",
            "SEPTEMBER",
            "OCTOBER",
            "NOVEMBER",
            "DECEMBER",
        ]
    ]
    patchingMode: typing.Literal["PATCHING_MODE_UNSPECIFIED", "ROLLING", "NON_ROLLING"]
    preference: typing.Literal[
        "MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED",
        "CUSTOM_PREFERENCE",
        "NO_PREFERENCE",
    ]
    weeksOfMonth: _list[int]

@typing.type_check_only
class MinorVersion(typing.TypedDict, total=False):
    gridImageId: str
    name: str
    version: str

@typing.type_check_only
class NameValuePair(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class NessieIcebergCatalog(typing.TypedDict, total=False):
    branch: str
    uri: str

@typing.type_check_only
class OdbNetwork(typing.TypedDict, total=False):
    createTime: str
    entitlementId: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "AVAILABLE", "TERMINATING", "FAILED"
    ]

@typing.type_check_only
class OdbSubnet(typing.TypedDict, total=False):
    cidrRange: str
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    purpose: typing.Literal["PURPOSE_UNSPECIFIED", "CLIENT_SUBNET", "BACKUP_SUBNET"]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "AVAILABLE", "TERMINATING", "FAILED"
    ]

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
    percentComplete: float
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PluggableDatabase(typing.TypedDict, total=False):
    createTime: str
    name: str
    ociUrl: str
    properties: PluggableDatabaseProperties

@typing.type_check_only
class PluggableDatabaseConnectionStrings(typing.TypedDict, total=False):
    allConnectionStrings: dict[str, typing.Any]
    pdbDefault: str
    pdbIpDefault: str

@typing.type_check_only
class PluggableDatabaseNodeLevelDetails(typing.TypedDict, total=False):
    nodeName: str
    openMode: typing.Literal[
        "PLUGGABLE_DATABASE_OPEN_MODE_UNSPECIFIED",
        "READ_ONLY",
        "READ_WRITE",
        "MOUNTED",
        "MIGRATE",
    ]
    pluggableDatabaseId: str

@typing.type_check_only
class PluggableDatabaseProperties(typing.TypedDict, total=False):
    compartmentId: str
    connectionStrings: PluggableDatabaseConnectionStrings
    containerDatabaseOcid: str
    databaseManagementConfig: DatabaseManagementConfig
    definedTags: dict[str, typing.Any]
    freeformTags: dict[str, typing.Any]
    isRestricted: bool
    lifecycleDetails: str
    lifecycleState: typing.Literal[
        "PLUGGABLE_DATABASE_LIFECYCLE_STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "TERMINATING",
        "TERMINATED",
        "UPDATING",
        "FAILED",
        "RELOCATING",
        "RELOCATED",
        "REFRESHING",
        "RESTORE_IN_PROGRESS",
        "RESTORE_FAILED",
        "BACKUP_IN_PROGRESS",
        "DISABLED",
    ]
    ocid: str
    operationsInsightsState: typing.Literal[
        "OPERATIONS_INSIGHTS_STATE_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    ]
    pdbName: str
    pdbNodeLevelDetails: _list[PluggableDatabaseNodeLevelDetails]

@typing.type_check_only
class PolarisIcebergCatalog(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    polarisCatalog: str
    principalRole: str
    uri: str

@typing.type_check_only
class RefreshAutonomousDatabaseRequest(typing.TypedDict, total=False):
    refreshCutoffTime: str

@typing.type_check_only
class RemoveVirtualMachineExadbVmClusterRequest(typing.TypedDict, total=False):
    hostnames: _list[str]
    requestId: str

@typing.type_check_only
class RestIcebergCatalog(typing.TypedDict, total=False):
    properties: str
    uri: str

@typing.type_check_only
class RestartAutonomousDatabaseRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RestoreAutonomousDatabaseRequest(typing.TypedDict, total=False):
    restoreTime: str

@typing.type_check_only
class ScheduledOperationDetails(typing.TypedDict, total=False):
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
    startTime: TimeOfDay
    stopTime: TimeOfDay

@typing.type_check_only
class SourceConfig(typing.TypedDict, total=False):
    autoRefreshFrequencySeconds: int
    autoRefreshPointLagSeconds: int
    autoRefreshStartTime: str
    automaticBackupsReplicationEnabled: bool
    autonomousDatabase: str
    autonomousDatabaseBackup: str
    backupTime: str
    cloneType: typing.Literal["CLONE_TYPE_UNSPECIFIED", "FULL", "METADATA"]
    refreshableMode: typing.Literal[
        "REFRESHABLE_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    sourceType: typing.Literal[
        "SOURCE_TYPE_UNSPECIFIED",
        "CLONE_DATABASE",
        "CROSS_REGION_DISASTER_RECOVERY",
        "CLONE_TO_REFRESHABLE",
        "BACKUP_FROM_ID",
        "BACKUP_FROM_TIMESTAMP",
    ]
    useLatestAvailableBackup: bool

@typing.type_check_only
class StartAutonomousDatabaseRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StartGoldengateDeploymentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopAutonomousDatabaseRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StopGoldengateDeploymentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StorageSizeDetails(typing.TypedDict, total=False):
    dataStorageSizeInGbs: int
    recoStorageSizeInGbs: int

@typing.type_check_only
class SwitchoverAutonomousDatabaseRequest(typing.TypedDict, total=False):
    peerAutonomousDatabase: str

@typing.type_check_only
class TestConnectionAssignmentError(typing.TypedDict, total=False):
    action: str
    code: str
    issue: str
    message: str

@typing.type_check_only
class TestGoldengateConnectionAssignmentRequest(typing.TypedDict, total=False):
    type: typing.Literal["TEST_TYPE_UNSPECIFIED", "DEFAULT"]

@typing.type_check_only
class TestGoldengateConnectionAssignmentResponse(typing.TypedDict, total=False):
    error: TestConnectionAssignmentError
    errors: _list[TestConnectionAssignmentError]
    resultType: typing.Literal[
        "RESULT_TYPE_UNSPECIFIED", "SUCCEEDED", "FAILED", "TIMED_OUT"
    ]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str
