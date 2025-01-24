import typing

import typing_extensions

_list = list

@typing.type_check_only
class AllConnectionStrings(typing_extensions.TypedDict, total=False):
    high: str
    low: str
    medium: str

@typing.type_check_only
class AutonomousDatabase(typing_extensions.TypedDict, total=False):
    adminPassword: str
    cidr: str
    createTime: str
    database: str
    displayName: str
    entitlementId: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    properties: AutonomousDatabaseProperties

@typing.type_check_only
class AutonomousDatabaseApex(typing_extensions.TypedDict, total=False):
    apexVersion: str
    ordsVersion: str

@typing.type_check_only
class AutonomousDatabaseBackup(typing_extensions.TypedDict, total=False):
    autonomousDatabase: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    properties: AutonomousDatabaseBackupProperties

@typing.type_check_only
class AutonomousDatabaseBackupProperties(typing_extensions.TypedDict, total=False):
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
    lifecycleState: typing_extensions.Literal[
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
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INCREMENTAL", "FULL", "LONG_TERM"
    ]
    vaultId: str

@typing.type_check_only
class AutonomousDatabaseCharacterSet(typing_extensions.TypedDict, total=False):
    characterSet: str
    characterSetType: typing_extensions.Literal[
        "CHARACTER_SET_TYPE_UNSPECIFIED", "DATABASE", "NATIONAL"
    ]
    name: str

@typing.type_check_only
class AutonomousDatabaseConnectionStrings(typing_extensions.TypedDict, total=False):
    allConnectionStrings: AllConnectionStrings
    dedicated: str
    high: str
    low: str
    medium: str
    profiles: _list[DatabaseConnectionStringProfile]

@typing.type_check_only
class AutonomousDatabaseConnectionUrls(typing_extensions.TypedDict, total=False):
    apexUri: str
    databaseTransformsUri: str
    graphStudioUri: str
    machineLearningNotebookUri: str
    machineLearningUserManagementUri: str
    mongoDbUri: str
    ordsUri: str
    sqlDevWebUri: str

@typing.type_check_only
class AutonomousDatabaseProperties(typing_extensions.TypedDict, total=False):
    actualUsedDataStorageSizeTb: float
    allocatedStorageSizeTb: float
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
    dataSafeState: typing_extensions.Literal[
        "DATA_SAFE_STATE_UNSPECIFIED",
        "REGISTERING",
        "REGISTERED",
        "DEREGISTERING",
        "NOT_REGISTERED",
        "FAILED",
    ]
    dataStorageSizeGb: int
    dataStorageSizeTb: int
    databaseManagementState: typing_extensions.Literal[
        "DATABASE_MANAGEMENT_STATE_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    ]
    dbEdition: typing_extensions.Literal[
        "DATABASE_EDITION_UNSPECIFIED", "STANDARD_EDITION", "ENTERPRISE_EDITION"
    ]
    dbVersion: str
    dbWorkload: typing_extensions.Literal[
        "DB_WORKLOAD_UNSPECIFIED", "OLTP", "DW", "AJD", "APEX"
    ]
    failedDataRecoveryDuration: str
    isAutoScalingEnabled: bool
    isLocalDataGuardEnabled: bool
    isStorageAutoScalingEnabled: bool
    licenseType: typing_extensions.Literal[
        "LICENSE_TYPE_UNSPECIFIED", "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
    ]
    lifecycleDetails: str
    localAdgAutoFailoverMaxDataLossLimit: int
    localDisasterRecoveryType: typing_extensions.Literal[
        "LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED", "ADG", "BACKUP_BASED"
    ]
    localStandbyDb: AutonomousDatabaseStandbySummary
    maintenanceBeginTime: str
    maintenanceEndTime: str
    maintenanceScheduleType: typing_extensions.Literal[
        "MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED", "EARLY", "REGULAR"
    ]
    memoryPerOracleComputeUnitGbs: int
    memoryTableGbs: int
    mtlsConnectionRequired: bool
    nCharacterSet: str
    nextLongTermBackupTime: str
    ociUrl: str
    ocid: str
    openMode: typing_extensions.Literal[
        "OPEN_MODE_UNSPECIFIED", "READ_ONLY", "READ_WRITE"
    ]
    operationsInsightsState: typing_extensions.Literal[
        "OPERATIONS_INSIGHTS_STATE_UNSPECIFIED",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    ]
    peerDbIds: _list[str]
    permissionLevel: typing_extensions.Literal[
        "PERMISSION_LEVEL_UNSPECIFIED", "RESTRICTED", "UNRESTRICTED"
    ]
    privateEndpoint: str
    privateEndpointIp: str
    privateEndpointLabel: str
    refreshableMode: typing_extensions.Literal[
        "REFRESHABLE_MODE_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    refreshableState: typing_extensions.Literal[
        "REFRESHABLE_STATE_UNSPECIFIED", "REFRESHING", "NOT_REFRESHING"
    ]
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED",
        "PRIMARY",
        "STANDBY",
        "DISABLED_STANDBY",
        "BACKUP_COPY",
        "SNAPSHOT_STANDBY",
    ]
    scheduledOperationDetails: _list[ScheduledOperationDetails]
    secretId: str
    sqlWebDeveloperUrl: str
    state: typing_extensions.Literal[
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
class AutonomousDatabaseStandbySummary(typing_extensions.TypedDict, total=False):
    dataGuardRoleChangedTime: str
    disasterRecoveryRoleChangedTime: str
    lagTimeDuration: str
    lifecycleDetails: str
    state: typing_extensions.Literal[
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
class AutonomousDbVersion(typing_extensions.TypedDict, total=False):
    dbWorkload: typing_extensions.Literal[
        "DB_WORKLOAD_UNSPECIFIED", "OLTP", "DW", "AJD", "APEX"
    ]
    name: str
    version: str
    workloadUri: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudAccountDetails(typing_extensions.TypedDict, total=False):
    accountCreationUri: str
    cloudAccount: str
    cloudAccountHomeRegion: str
    linkExistingAccountUri: str

@typing.type_check_only
class CloudExadataInfrastructure(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    entitlementId: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    properties: CloudExadataInfrastructureProperties

@typing.type_check_only
class CloudExadataInfrastructureProperties(typing_extensions.TypedDict, total=False):
    activatedStorageCount: int
    additionalStorageCount: int
    availableStorageSizeGb: int
    computeCount: int
    cpuCount: int
    customerContacts: _list[CustomerContact]
    dataStorageSizeTb: float
    dbNodeStorageSizeGb: int
    dbServerVersion: str
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
    state: typing_extensions.Literal[
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
    storageServerVersion: str
    totalStorageSizeGb: int

@typing.type_check_only
class CloudVmCluster(typing_extensions.TypedDict, total=False):
    backupSubnetCidr: str
    cidr: str
    createTime: str
    displayName: str
    exadataInfrastructure: str
    gcpOracleZone: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    properties: CloudVmClusterProperties

@typing.type_check_only
class CloudVmClusterProperties(typing_extensions.TypedDict, total=False):
    clusterName: str
    compartmentId: str
    cpuCoreCount: int
    dataStorageSizeTb: float
    dbNodeStorageSizeGb: int
    dbServerOcids: _list[str]
    diagnosticsDataCollectionOptions: DataCollectionOptions
    diskRedundancy: typing_extensions.Literal[
        "DISK_REDUNDANCY_UNSPECIFIED", "HIGH", "NORMAL"
    ]
    dnsListenerIp: str
    domain: str
    giVersion: str
    hostname: str
    hostnamePrefix: str
    licenseType: typing_extensions.Literal[
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "AVAILABLE",
        "UPDATING",
        "TERMINATING",
        "TERMINATED",
        "FAILED",
        "MAINTENANCE_IN_PROGRESS",
    ]
    storageSizeGb: int
    systemVersion: str
    timeZone: TimeZone

@typing.type_check_only
class CustomerContact(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class DataCollectionOptions(typing_extensions.TypedDict, total=False):
    diagnosticsEventsEnabled: bool
    healthMonitoringEnabled: bool
    incidentLogsEnabled: bool

@typing.type_check_only
class DatabaseConnectionStringProfile(typing_extensions.TypedDict, total=False):
    consumerGroup: typing_extensions.Literal[
        "CONSUMER_GROUP_UNSPECIFIED", "HIGH", "MEDIUM", "LOW", "TP", "TPURGENT"
    ]
    displayName: str
    hostFormat: typing_extensions.Literal["HOST_FORMAT_UNSPECIFIED", "FQDN", "IP"]
    isRegional: bool
    protocol: typing_extensions.Literal["PROTOCOL_UNSPECIFIED", "TCP", "TCPS"]
    sessionMode: typing_extensions.Literal[
        "SESSION_MODE_UNSPECIFIED", "DIRECT", "INDIRECT"
    ]
    syntaxFormat: typing_extensions.Literal[
        "SYNTAX_FORMAT_UNSPECIFIED", "LONG", "EZCONNECT", "EZCONNECTPLUS"
    ]
    tlsAuthentication: typing_extensions.Literal[
        "TLS_AUTHENTICATION_UNSPECIFIED", "SERVER", "MUTUAL"
    ]
    value: str

@typing.type_check_only
class DbNode(typing_extensions.TypedDict, total=False):
    name: str
    properties: DbNodeProperties

@typing.type_check_only
class DbNodeProperties(typing_extensions.TypedDict, total=False):
    dbNodeStorageSizeGb: int
    dbServerOcid: str
    hostname: str
    memorySizeGb: int
    ocid: str
    ocpuCount: int
    state: typing_extensions.Literal[
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
class DbServer(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    properties: DbServerProperties

@typing.type_check_only
class DbServerProperties(typing_extensions.TypedDict, total=False):
    dbNodeIds: _list[str]
    dbNodeStorageSizeGb: int
    maxDbNodeStorageSizeGb: int
    maxMemorySizeGb: int
    maxOcpuCount: int
    memorySizeGb: int
    ocid: str
    ocpuCount: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "AVAILABLE",
        "UNAVAILABLE",
        "DELETING",
        "DELETED",
    ]
    vmCount: int

@typing.type_check_only
class DbSystemShape(typing_extensions.TypedDict, total=False):
    availableCoreCountPerNode: int
    availableDataStorageTb: int
    availableMemoryPerNodeGb: int
    maxNodeCount: int
    maxStorageCount: int
    minCoreCountPerNode: int
    minDbNodeStoragePerNodeGb: int
    minMemoryPerNodeGb: int
    minNodeCount: int
    minStorageCount: int
    name: str
    shape: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entitlement(typing_extensions.TypedDict, total=False):
    cloudAccountDetails: CloudAccountDetails
    entitlementId: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACCOUNT_NOT_LINKED",
        "ACCOUNT_NOT_ACTIVE",
        "ACTIVE",
        "ACCOUNT_SUSPENDED",
    ]

@typing.type_check_only
class GenerateAutonomousDatabaseWalletRequest(typing_extensions.TypedDict, total=False):
    isRegional: bool
    password: str
    type: typing_extensions.Literal["GENERATE_TYPE_UNSPECIFIED", "ALL", "SINGLE"]

@typing.type_check_only
class GenerateAutonomousDatabaseWalletResponse(
    typing_extensions.TypedDict, total=False
):
    archiveContent: str

@typing.type_check_only
class GiVersion(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ListAutonomousDatabaseBackupsResponse(typing_extensions.TypedDict, total=False):
    autonomousDatabaseBackups: _list[AutonomousDatabaseBackup]
    nextPageToken: str

@typing.type_check_only
class ListAutonomousDatabaseCharacterSetsResponse(
    typing_extensions.TypedDict, total=False
):
    autonomousDatabaseCharacterSets: _list[AutonomousDatabaseCharacterSet]
    nextPageToken: str

@typing.type_check_only
class ListAutonomousDatabasesResponse(typing_extensions.TypedDict, total=False):
    autonomousDatabases: _list[AutonomousDatabase]
    nextPageToken: str

@typing.type_check_only
class ListAutonomousDbVersionsResponse(typing_extensions.TypedDict, total=False):
    autonomousDbVersions: _list[AutonomousDbVersion]
    nextPageToken: str

@typing.type_check_only
class ListCloudExadataInfrastructuresResponse(typing_extensions.TypedDict, total=False):
    cloudExadataInfrastructures: _list[CloudExadataInfrastructure]
    nextPageToken: str

@typing.type_check_only
class ListCloudVmClustersResponse(typing_extensions.TypedDict, total=False):
    cloudVmClusters: _list[CloudVmCluster]
    nextPageToken: str

@typing.type_check_only
class ListDbNodesResponse(typing_extensions.TypedDict, total=False):
    dbNodes: _list[DbNode]
    nextPageToken: str

@typing.type_check_only
class ListDbServersResponse(typing_extensions.TypedDict, total=False):
    dbServers: _list[DbServer]
    nextPageToken: str

@typing.type_check_only
class ListDbSystemShapesResponse(typing_extensions.TypedDict, total=False):
    dbSystemShapes: _list[DbSystemShape]
    nextPageToken: str

@typing.type_check_only
class ListEntitlementsResponse(typing_extensions.TypedDict, total=False):
    entitlements: _list[Entitlement]
    nextPageToken: str

@typing.type_check_only
class ListGiVersionsResponse(typing_extensions.TypedDict, total=False):
    giVersions: _list[GiVersion]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

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
class LocationMetadata(typing_extensions.TypedDict, total=False):
    gcpOracleZones: _list[str]

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    customActionTimeoutMins: int
    daysOfWeek: _list[
        typing_extensions.Literal[
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
        typing_extensions.Literal[
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
    patchingMode: typing_extensions.Literal[
        "PATCHING_MODE_UNSPECIFIED", "ROLLING", "NON_ROLLING"
    ]
    preference: typing_extensions.Literal[
        "MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED",
        "CUSTOM_PREFERENCE",
        "NO_PREFERENCE",
    ]
    weeksOfMonth: _list[int]

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
    percentComplete: float
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class RestoreAutonomousDatabaseRequest(typing_extensions.TypedDict, total=False):
    restoreTime: str

@typing.type_check_only
class ScheduledOperationDetails(typing_extensions.TypedDict, total=False):
    dayOfWeek: typing_extensions.Literal[
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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str
