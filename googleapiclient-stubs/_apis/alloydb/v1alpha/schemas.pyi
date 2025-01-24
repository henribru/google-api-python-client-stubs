import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuthorizedNetwork(typing_extensions.TypedDict, total=False):
    cidrRange: str

@typing.type_check_only
class AutomatedBackupPolicy(typing_extensions.TypedDict, total=False):
    backupWindow: str
    enabled: bool
    encryptionConfig: EncryptionConfig
    labels: dict[str, typing.Any]
    location: str
    quantityBasedRetention: QuantityBasedRetention
    timeBasedRetention: TimeBasedRetention
    weeklySchedule: WeeklySchedule

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clusterName: str
    clusterUid: str
    createTime: str
    databaseVersion: typing_extensions.Literal[
        "DATABASE_VERSION_UNSPECIFIED",
        "POSTGRES_13",
        "POSTGRES_14",
        "POSTGRES_15",
        "POSTGRES_16",
    ]
    deleteTime: str
    description: str
    displayName: str
    encryptionConfig: EncryptionConfig
    encryptionInfo: EncryptionInfo
    etag: str
    expiryQuantity: QuantityBasedExpiry
    expiryTime: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    satisfiesPzi: bool
    satisfiesPzs: bool
    sizeBytes: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "READY", "CREATING", "FAILED", "DELETING"
    ]
    tags: dict[str, typing.Any]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "ON_DEMAND", "AUTOMATED", "CONTINUOUS"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class BackupSource(typing_extensions.TypedDict, total=False):
    backupName: str
    backupUid: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClientConnectionConfig(typing_extensions.TypedDict, total=False):
    requireConnectors: bool
    sslConfig: SslConfig

@typing.type_check_only
class CloudControl2SharedOperationsReconciliationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

@typing.type_check_only
class CloudSQLBackupRunSource(typing_extensions.TypedDict, total=False):
    backupRunId: str
    instanceId: str
    project: str

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    automatedBackupPolicy: AutomatedBackupPolicy
    backupSource: BackupSource
    cloudsqlBackupRunSource: CloudSQLBackupRunSource
    clusterType: typing_extensions.Literal[
        "CLUSTER_TYPE_UNSPECIFIED", "PRIMARY", "SECONDARY"
    ]
    continuousBackupConfig: ContinuousBackupConfig
    continuousBackupInfo: ContinuousBackupInfo
    createTime: str
    databaseVersion: typing_extensions.Literal[
        "DATABASE_VERSION_UNSPECIFIED",
        "POSTGRES_13",
        "POSTGRES_14",
        "POSTGRES_15",
        "POSTGRES_16",
    ]
    deleteTime: str
    displayName: str
    encryptionConfig: EncryptionConfig
    encryptionInfo: EncryptionInfo
    etag: str
    geminiConfig: GeminiClusterConfig
    initialUser: UserPassword
    labels: dict[str, typing.Any]
    maintenanceSchedule: MaintenanceSchedule
    maintenanceUpdatePolicy: MaintenanceUpdatePolicy
    migrationSource: MigrationSource
    name: str
    network: str
    networkConfig: NetworkConfig
    primaryConfig: PrimaryConfig
    pscConfig: PscConfig
    reconciling: bool
    satisfiesPzi: bool
    satisfiesPzs: bool
    secondaryConfig: SecondaryConfig
    sslConfig: SslConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "STOPPED",
        "EMPTY",
        "CREATING",
        "DELETING",
        "FAILED",
        "BOOTSTRAPPING",
        "MAINTENANCE",
        "PROMOTING",
    ]
    subscriptionType: typing_extensions.Literal[
        "SUBSCRIPTION_TYPE_UNSPECIFIED", "STANDARD", "TRIAL"
    ]
    tags: dict[str, typing.Any]
    trialMetadata: TrialMetadata
    uid: str
    updateTime: str

@typing.type_check_only
class ClusterUpgradeDetails(typing_extensions.TypedDict, total=False):
    clusterType: typing_extensions.Literal[
        "CLUSTER_TYPE_UNSPECIFIED", "PRIMARY", "SECONDARY"
    ]
    databaseVersion: typing_extensions.Literal[
        "DATABASE_VERSION_UNSPECIFIED",
        "POSTGRES_13",
        "POSTGRES_14",
        "POSTGRES_15",
        "POSTGRES_16",
    ]
    instanceUpgradeDetails: _list[InstanceUpgradeDetails]
    name: str
    stageInfo: _list[StageInfo]
    upgradeStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_STARTED",
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "PARTIAL_SUCCESS",
        "CANCEL_IN_PROGRESS",
        "CANCELLED",
    ]

@typing.type_check_only
class ConnectionInfo(typing_extensions.TypedDict, total=False):
    instanceUid: str
    ipAddress: str
    name: str
    pemCertificateChain: _list[str]
    pscDnsName: str
    publicIpAddress: str

@typing.type_check_only
class ContinuousBackupConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    encryptionConfig: EncryptionConfig
    recoveryWindowDays: int

@typing.type_check_only
class ContinuousBackupInfo(typing_extensions.TypedDict, total=False):
    earliestRestorableTime: str
    enabledTime: str
    encryptionInfo: EncryptionInfo
    schedule: _list[
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

@typing.type_check_only
class ContinuousBackupSource(typing_extensions.TypedDict, total=False):
    cluster: str
    pointInTime: str

@typing.type_check_only
class CsvExportOptions(typing_extensions.TypedDict, total=False):
    escapeCharacter: str
    fieldDelimiter: str
    quoteCharacter: str
    selectQuery: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EncryptionInfo(typing_extensions.TypedDict, total=False):
    encryptionType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GOOGLE_DEFAULT_ENCRYPTION", "CUSTOMER_MANAGED_ENCRYPTION"
    ]
    kmsKeyVersions: _list[str]

@typing.type_check_only
class ExportClusterRequest(typing_extensions.TypedDict, total=False):
    csvExportOptions: CsvExportOptions
    database: str
    gcsDestination: GcsDestination
    sqlExportOptions: SqlExportOptions

@typing.type_check_only
class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    validateOnly: bool

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GeminiClusterConfig(typing_extensions.TypedDict, total=False):
    entitled: bool

@typing.type_check_only
class GeminiInstanceConfig(typing_extensions.TypedDict, total=False):
    entitled: bool

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleTypeTimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class InjectFaultRequest(typing_extensions.TypedDict, total=False):
    faultType: typing_extensions.Literal["FAULT_TYPE_UNSPECIFIED", "STOP_VM"]
    requestId: str
    validateOnly: bool

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    availabilityType: typing_extensions.Literal[
        "AVAILABILITY_TYPE_UNSPECIFIED", "ZONAL", "REGIONAL"
    ]
    clientConnectionConfig: ClientConnectionConfig
    createTime: str
    databaseFlags: dict[str, typing.Any]
    deleteTime: str
    displayName: str
    etag: str
    gceZone: str
    geminiConfig: GeminiInstanceConfig
    instanceType: typing_extensions.Literal[
        "INSTANCE_TYPE_UNSPECIFIED", "PRIMARY", "READ_POOL", "SECONDARY"
    ]
    ipAddress: str
    labels: dict[str, typing.Any]
    machineConfig: MachineConfig
    name: str
    networkConfig: InstanceNetworkConfig
    nodes: _list[Node]
    observabilityConfig: ObservabilityInstanceConfig
    outboundPublicIpAddresses: _list[str]
    pscInstanceConfig: PscInstanceConfig
    publicIpAddress: str
    queryInsightsConfig: QueryInsightsInstanceConfig
    readPoolConfig: ReadPoolConfig
    reconciling: bool
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "STOPPED",
        "CREATING",
        "DELETING",
        "MAINTENANCE",
        "FAILED",
        "BOOTSTRAPPING",
        "PROMOTING",
    ]
    uid: str
    updatePolicy: UpdatePolicy
    updateTime: str
    writableNode: Node

@typing.type_check_only
class InstanceNetworkConfig(typing_extensions.TypedDict, total=False):
    authorizedExternalNetworks: _list[AuthorizedNetwork]
    enableOutboundPublicIp: bool
    enablePublicIp: bool

@typing.type_check_only
class InstanceUpgradeDetails(typing_extensions.TypedDict, total=False):
    instanceType: typing_extensions.Literal[
        "INSTANCE_TYPE_UNSPECIFIED", "PRIMARY", "READ_POOL", "SECONDARY"
    ]
    name: str
    upgradeStatus: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_STARTED",
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "PARTIAL_SUCCESS",
        "CANCEL_IN_PROGRESS",
        "CANCELLED",
    ]

@typing.type_check_only
class IntegerRestrictions(typing_extensions.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSupportedDatabaseFlagsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    supportedDatabaseFlags: _list[SupportedDatabaseFlag]

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    users: _list[User]

@typing.type_check_only
class MachineConfig(typing_extensions.TypedDict, total=False):
    cpuCount: int

@typing.type_check_only
class MaintenanceSchedule(typing_extensions.TypedDict, total=False):
    startTime: str

@typing.type_check_only
class MaintenanceUpdatePolicy(typing_extensions.TypedDict, total=False):
    maintenanceWindows: _list[MaintenanceWindow]

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    day: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    startTime: GoogleTypeTimeOfDay

@typing.type_check_only
class MigrationSource(typing_extensions.TypedDict, total=False):
    hostPort: str
    referenceId: str
    sourceType: typing_extensions.Literal["MIGRATION_SOURCE_TYPE_UNSPECIFIED", "DMS"]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    allocatedIpRange: str
    network: str

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    id: str
    ip: str
    state: str
    zoneId: str

@typing.type_check_only
class ObservabilityInstanceConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    maxQueryStringLength: int
    preserveComments: bool
    queryPlansPerMinute: int
    recordApplicationTags: bool
    trackActiveQueries: bool
    trackClientAddress: bool
    trackWaitEventTypes: bool
    trackWaitEvents: bool

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
    verb: str

@typing.type_check_only
class PrimaryConfig(typing_extensions.TypedDict, total=False):
    secondaryClusterNames: _list[str]

@typing.type_check_only
class PromoteClusterRequest(typing_extensions.TypedDict, total=False):
    etag: str
    requestId: str
    validateOnly: bool

@typing.type_check_only
class PscConfig(typing_extensions.TypedDict, total=False):
    pscEnabled: bool
    serviceOwnedProjectNumber: str

@typing.type_check_only
class PscInstanceConfig(typing_extensions.TypedDict, total=False):
    allowedConsumerProjects: _list[str]
    pscDnsName: str
    pscInterfaceConfigs: _list[PscInterfaceConfig]
    serviceAttachmentLink: str

@typing.type_check_only
class PscInterfaceConfig(typing_extensions.TypedDict, total=False):
    networkAttachmentResource: str

@typing.type_check_only
class QuantityBasedExpiry(typing_extensions.TypedDict, total=False):
    retentionCount: int
    totalRetentionCount: int

@typing.type_check_only
class QuantityBasedRetention(typing_extensions.TypedDict, total=False):
    count: int

@typing.type_check_only
class QueryInsightsInstanceConfig(typing_extensions.TypedDict, total=False):
    queryPlansPerMinute: int
    queryStringLength: int
    recordApplicationTags: bool
    recordClientAddress: bool

@typing.type_check_only
class ReadPoolConfig(typing_extensions.TypedDict, total=False):
    nodeCount: int

@typing.type_check_only
class RestartInstanceRequest(typing_extensions.TypedDict, total=False):
    nodeIds: _list[str]
    requestId: str
    validateOnly: bool

@typing.type_check_only
class RestoreClusterRequest(typing_extensions.TypedDict, total=False):
    backupSource: BackupSource
    cluster: Cluster
    clusterId: str
    continuousBackupSource: ContinuousBackupSource
    requestId: str
    validateOnly: bool

@typing.type_check_only
class RestoreFromCloudSQLRequest(typing_extensions.TypedDict, total=False):
    cloudsqlBackupRunSource: CloudSQLBackupRunSource
    cluster: Cluster
    clusterId: str

@typing.type_check_only
class SecondaryConfig(typing_extensions.TypedDict, total=False):
    primaryClusterName: str

@typing.type_check_only
class SqlExportOptions(typing_extensions.TypedDict, total=False):
    cleanTargetObjects: bool
    ifExistTargetObjects: bool
    schemaOnly: bool
    tables: _list[str]

@typing.type_check_only
class SslConfig(typing_extensions.TypedDict, total=False):
    caSource: typing_extensions.Literal["CA_SOURCE_UNSPECIFIED", "CA_SOURCE_MANAGED"]
    sslMode: typing_extensions.Literal[
        "SSL_MODE_UNSPECIFIED",
        "SSL_MODE_ALLOW",
        "SSL_MODE_REQUIRE",
        "SSL_MODE_VERIFY_CA",
        "ALLOW_UNENCRYPTED_AND_ENCRYPTED",
        "ENCRYPTED_ONLY",
    ]

@typing.type_check_only
class StageInfo(typing_extensions.TypedDict, total=False):
    logsUrl: str
    stage: typing_extensions.Literal[
        "STAGE_UNSPECIFIED",
        "ALLOYDB_PRECHECK",
        "PG_UPGRADE_CHECK",
        "PREPARE_FOR_UPGRADE",
        "PRIMARY_INSTANCE_UPGRADE",
        "READ_POOL_INSTANCES_UPGRADE",
        "ROLLBACK",
        "CLEANUP",
    ]
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_STARTED",
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "PARTIAL_SUCCESS",
        "CANCEL_IN_PROGRESS",
        "CANCELLED",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration(
    typing_extensions.TypedDict, total=False
):
    automaticFailoverRoutingConfigured: bool
    availabilityType: typing_extensions.Literal[
        "AVAILABILITY_TYPE_UNSPECIFIED",
        "ZONAL",
        "REGIONAL",
        "MULTI_REGIONAL",
        "AVAILABILITY_TYPE_OTHER",
    ]
    crossRegionReplicaConfigured: bool
    externalReplicaConfigured: bool
    promotableReplicaConfigured: bool

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainBackupConfiguration(
    typing_extensions.TypedDict, total=False
):
    automatedBackupEnabled: bool
    backupRetentionSettings: StorageDatabasecenterPartnerapiV1mainRetentionSettings
    pointInTimeRecoveryEnabled: bool

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainBackupRun(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    error: StorageDatabasecenterPartnerapiV1mainOperationError
    startTime: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "SUCCESSFUL", "FAILED"]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainCompliance(
    typing_extensions.TypedDict, total=False
):
    standard: str
    version: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainCustomMetadataData(
    typing_extensions.TypedDict, total=False
):
    internalResourceMetadata: _list[
        StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata
    ]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed(
    typing_extensions.TypedDict, total=False
):
    feedTimestamp: str
    feedType: typing_extensions.Literal[
        "FEEDTYPE_UNSPECIFIED",
        "RESOURCE_METADATA",
        "OBSERVABILITY_DATA",
        "SECURITY_FINDING_DATA",
        "RECOMMENDATION_SIGNAL_DATA",
    ]
    observabilityMetricData: (
        StorageDatabasecenterPartnerapiV1mainObservabilityMetricData
    )
    recommendationSignalData: (
        StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData
    )
    resourceHealthSignalData: (
        StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData
    )
    resourceId: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    resourceMetadata: StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData(
    typing_extensions.TypedDict, total=False
):
    additionalMetadata: dict[str, typing.Any]
    compliance: _list[StorageDatabasecenterPartnerapiV1mainCompliance]
    description: str
    eventTime: str
    externalUri: str
    name: str
    provider: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED",
        "GCP",
        "AWS",
        "AZURE",
        "ONPREM",
        "SELFMANAGED",
        "PROVIDER_OTHER",
    ]
    resourceContainer: str
    resourceName: str
    signalClass: typing_extensions.Literal[
        "CLASS_UNSPECIFIED",
        "THREAT",
        "VULNERABILITY",
        "MISCONFIGURATION",
        "OBSERVATION",
        "ERROR",
    ]
    signalId: str
    signalSeverity: typing_extensions.Literal[
        "SIGNAL_SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_NOT_PROTECTED_BY_AUTOMATIC_FAILOVER",
        "SIGNAL_TYPE_GROUP_NOT_REPLICATING_ACROSS_REGIONS",
        "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_ZONES",
        "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_REGIONS",
        "SIGNAL_TYPE_NO_PROMOTABLE_REPLICA",
        "SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY",
        "SIGNAL_TYPE_SHORT_BACKUP_RETENTION",
        "SIGNAL_TYPE_LAST_BACKUP_FAILED",
        "SIGNAL_TYPE_LAST_BACKUP_OLD",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0",
        "SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0",
        "SIGNAL_TYPE_VIOLATES_NIST_800_53",
        "SIGNAL_TYPE_VIOLATES_NIST_800_53_R5",
        "SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0",
        "SIGNAL_TYPE_VIOLATES_ISO_27001",
        "SIGNAL_TYPE_VIOLATES_ISO_27001_V2022",
        "SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1",
        "SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0",
        "SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4",
        "SIGNAL_TYPE_VIOLATES_HIPAA",
        "SIGNAL_TYPE_VIOLATES_SOC2_V2017",
        "SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING",
        "SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED",
        "SIGNAL_TYPE_VERBOSE_ERROR_LOGGING",
        "SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED",
        "SIGNAL_TYPE_LOGGING_MOST_ERRORS",
        "SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS",
        "SIGNAL_TYPE_MINIMAL_ERROR_LOGGING",
        "SIGNAL_TYPE_QUERY_STATISTICS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATISTICS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATISTICS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
        "SIGNAL_TYPE_EXPOSED_BY_OWNERSHIP_CHAINING",
        "SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS",
        "SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS",
        "SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED",
        "SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED",
        "SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO",
        "SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS",
        "SIGNAL_TYPE_DATABASE_NAMES_EXPOSED",
        "SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED",
        "SIGNAL_TYPE_PUBLIC_IP_ENABLED",
        "SIGNAL_TYPE_IDLE",
        "SIGNAL_TYPE_OVERPROVISIONED",
        "SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES",
        "SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES",
        "SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION",
        "SIGNAL_TYPE_UNDERPROVISIONED",
        "SIGNAL_TYPE_OUT_OF_DISK",
        "SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY",
        "SIGNAL_TYPE_DATABASE_AUDITING_DISABLED",
        "SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS",
        "SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP",
        "SIGNAL_TYPE_QUOTA_LIMIT",
        "SIGNAL_TYPE_NO_PASSWORD_POLICY",
        "SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT",
        "SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT",
        "SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT",
        "SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES",
        "SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES",
        "SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS",
        "SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET",
        "SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET",
        "SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM",
        "SIGNAL_TYPE_NO_USER_PASSWORD_POLICY",
    ]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "RESOLVED", "MUTED"]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceId(
    typing_extensions.TypedDict, total=False
):
    provider: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED",
        "GCP",
        "AWS",
        "AZURE",
        "ONPREM",
        "SELFMANAGED",
        "PROVIDER_OTHER",
    ]
    providerDescription: str
    resourceType: str
    uniqueId: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata(
    typing_extensions.TypedDict, total=False
):
    availabilityConfiguration: (
        StorageDatabasecenterPartnerapiV1mainAvailabilityConfiguration
    )
    backupConfiguration: StorageDatabasecenterPartnerapiV1mainBackupConfiguration
    backupRun: StorageDatabasecenterPartnerapiV1mainBackupRun
    creationTime: str
    currentState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "SUSPENDED",
        "DELETED",
        "STATE_OTHER",
    ]
    customMetadata: StorageDatabasecenterPartnerapiV1mainCustomMetadataData
    edition: typing_extensions.Literal[
        "EDITION_UNSPECIFIED", "EDITION_ENTERPRISE", "EDITION_ENTERPRISE_PLUS"
    ]
    entitlements: _list[StorageDatabasecenterPartnerapiV1mainEntitlement]
    expectedState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "SUSPENDED",
        "DELETED",
        "STATE_OTHER",
    ]
    id: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    instanceType: typing_extensions.Literal[
        "INSTANCE_TYPE_UNSPECIFIED",
        "SUB_RESOURCE_TYPE_UNSPECIFIED",
        "PRIMARY",
        "SECONDARY",
        "READ_REPLICA",
        "OTHER",
        "SUB_RESOURCE_TYPE_PRIMARY",
        "SUB_RESOURCE_TYPE_SECONDARY",
        "SUB_RESOURCE_TYPE_READ_REPLICA",
        "SUB_RESOURCE_TYPE_OTHER",
    ]
    location: str
    machineConfiguration: StorageDatabasecenterPartnerapiV1mainMachineConfiguration
    primaryResourceId: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    primaryResourceLocation: str
    product: StorageDatabasecenterProtoCommonProduct
    resourceContainer: str
    resourceName: str
    tagsSet: StorageDatabasecenterPartnerapiV1mainTags
    updationTime: str
    userLabelSet: StorageDatabasecenterPartnerapiV1mainUserLabels

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData(
    typing_extensions.TypedDict, total=False
):
    additionalMetadata: dict[str, typing.Any]
    lastRefreshTime: str
    recommendationState: typing_extensions.Literal[
        "UNSPECIFIED", "ACTIVE", "CLAIMED", "SUCCEEDED", "FAILED", "DISMISSED"
    ]
    recommender: str
    recommenderId: str
    recommenderSubtype: str
    resourceName: str
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_NOT_PROTECTED_BY_AUTOMATIC_FAILOVER",
        "SIGNAL_TYPE_GROUP_NOT_REPLICATING_ACROSS_REGIONS",
        "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_ZONES",
        "SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_REGIONS",
        "SIGNAL_TYPE_NO_PROMOTABLE_REPLICA",
        "SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY",
        "SIGNAL_TYPE_SHORT_BACKUP_RETENTION",
        "SIGNAL_TYPE_LAST_BACKUP_FAILED",
        "SIGNAL_TYPE_LAST_BACKUP_OLD",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1",
        "SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0",
        "SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0",
        "SIGNAL_TYPE_VIOLATES_NIST_800_53",
        "SIGNAL_TYPE_VIOLATES_NIST_800_53_R5",
        "SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0",
        "SIGNAL_TYPE_VIOLATES_ISO_27001",
        "SIGNAL_TYPE_VIOLATES_ISO_27001_V2022",
        "SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1",
        "SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0",
        "SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4",
        "SIGNAL_TYPE_VIOLATES_HIPAA",
        "SIGNAL_TYPE_VIOLATES_SOC2_V2017",
        "SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING",
        "SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED",
        "SIGNAL_TYPE_VERBOSE_ERROR_LOGGING",
        "SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED",
        "SIGNAL_TYPE_LOGGING_MOST_ERRORS",
        "SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS",
        "SIGNAL_TYPE_MINIMAL_ERROR_LOGGING",
        "SIGNAL_TYPE_QUERY_STATISTICS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATISTICS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATISTICS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
        "SIGNAL_TYPE_EXPOSED_BY_OWNERSHIP_CHAINING",
        "SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS",
        "SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS",
        "SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED",
        "SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED",
        "SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO",
        "SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS",
        "SIGNAL_TYPE_DATABASE_NAMES_EXPOSED",
        "SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED",
        "SIGNAL_TYPE_PUBLIC_IP_ENABLED",
        "SIGNAL_TYPE_IDLE",
        "SIGNAL_TYPE_OVERPROVISIONED",
        "SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES",
        "SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES",
        "SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION",
        "SIGNAL_TYPE_UNDERPROVISIONED",
        "SIGNAL_TYPE_OUT_OF_DISK",
        "SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY",
        "SIGNAL_TYPE_DATABASE_AUDITING_DISABLED",
        "SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS",
        "SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP",
        "SIGNAL_TYPE_QUOTA_LIMIT",
        "SIGNAL_TYPE_NO_PASSWORD_POLICY",
        "SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT",
        "SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT",
        "SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT",
        "SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES",
        "SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES",
        "SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS",
        "SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET",
        "SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET",
        "SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM",
        "SIGNAL_TYPE_NO_USER_PASSWORD_POLICY",
    ]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainEntitlement(
    typing_extensions.TypedDict, total=False
):
    entitlementState: typing_extensions.Literal[
        "ENTITLEMENT_STATE_UNSPECIFIED", "ENTITLED", "REVOKED"
    ]
    type: typing_extensions.Literal["ENTITLEMENT_TYPE_UNSPECIFIED", "GEMINI"]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainInternalResourceMetadata(
    typing_extensions.TypedDict, total=False
):
    backupConfiguration: StorageDatabasecenterPartnerapiV1mainBackupConfiguration
    backupRun: StorageDatabasecenterPartnerapiV1mainBackupRun
    product: StorageDatabasecenterProtoCommonProduct
    resourceId: StorageDatabasecenterPartnerapiV1mainDatabaseResourceId
    resourceName: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainMachineConfiguration(
    typing_extensions.TypedDict, total=False
):
    cpuCount: int
    memorySizeInBytes: str
    shardCount: int
    vcpuCount: float

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainObservabilityMetricData(
    typing_extensions.TypedDict, total=False
):
    aggregationType: typing_extensions.Literal[
        "AGGREGATION_TYPE_UNSPECIFIED", "PEAK", "P99", "P95", "CURRENT"
    ]
    metricType: typing_extensions.Literal[
        "METRIC_TYPE_UNSPECIFIED",
        "CPU_UTILIZATION",
        "MEMORY_UTILIZATION",
        "NETWORK_CONNECTIONS",
        "STORAGE_UTILIZATION",
        "STORAGE_USED_BYTES",
    ]
    observationTime: str
    resourceName: str
    value: StorageDatabasecenterProtoCommonTypedValue

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainOperationError(
    typing_extensions.TypedDict, total=False
):
    code: str
    errorType: typing_extensions.Literal[
        "OPERATION_ERROR_TYPE_UNSPECIFIED",
        "KMS_KEY_ERROR",
        "DATABASE_ERROR",
        "STOCKOUT_ERROR",
        "CANCELLATION_ERROR",
        "SQLSERVER_ERROR",
        "INTERNAL_ERROR",
    ]
    message: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainRetentionSettings(
    typing_extensions.TypedDict, total=False
):
    durationBasedRetention: str
    quantityBasedRetention: int
    retentionUnit: typing_extensions.Literal[
        "RETENTION_UNIT_UNSPECIFIED",
        "COUNT",
        "TIME",
        "DURATION",
        "RETENTION_UNIT_OTHER",
    ]
    timeBasedRetention: str
    timestampBasedRetentionTime: str

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainTags(
    typing_extensions.TypedDict, total=False
):
    tags: dict[str, typing.Any]

@typing.type_check_only
class StorageDatabasecenterPartnerapiV1mainUserLabels(
    typing_extensions.TypedDict, total=False
):
    labels: dict[str, typing.Any]

@typing.type_check_only
class StorageDatabasecenterProtoCommonProduct(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal[
        "ENGINE_UNSPECIFIED",
        "ENGINE_MYSQL",
        "MYSQL",
        "ENGINE_POSTGRES",
        "POSTGRES",
        "ENGINE_SQL_SERVER",
        "SQL_SERVER",
        "ENGINE_NATIVE",
        "NATIVE",
        "ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT",
        "ENGINE_CLOUD_SPANNER_WITH_GOOGLESQL_DIALECT",
        "ENGINE_MEMORYSTORE_FOR_REDIS",
        "ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER",
        "ENGINE_OTHER",
        "ENGINE_FIRESTORE_WITH_NATIVE_MODE",
        "ENGINE_FIRESTORE_WITH_DATASTORE_MODE",
    ]
    type: typing_extensions.Literal[
        "PRODUCT_TYPE_UNSPECIFIED",
        "PRODUCT_TYPE_CLOUD_SQL",
        "CLOUD_SQL",
        "PRODUCT_TYPE_ALLOYDB",
        "ALLOYDB",
        "PRODUCT_TYPE_SPANNER",
        "PRODUCT_TYPE_ON_PREM",
        "ON_PREM",
        "PRODUCT_TYPE_MEMORYSTORE",
        "PRODUCT_TYPE_BIGTABLE",
        "PRODUCT_TYPE_OTHER",
        "PRODUCT_TYPE_FIRESTORE",
    ]
    version: str

@typing.type_check_only
class StorageDatabasecenterProtoCommonTypedValue(
    typing_extensions.TypedDict, total=False
):
    boolValue: bool
    doubleValue: float
    int64Value: str
    stringValue: str

@typing.type_check_only
class StringRestrictions(typing_extensions.TypedDict, total=False):
    allowedValues: _list[str]

@typing.type_check_only
class SupportedDatabaseFlag(typing_extensions.TypedDict, total=False):
    acceptsMultipleValues: bool
    flagName: str
    integerRestrictions: IntegerRestrictions
    name: str
    requiresDbRestart: bool
    stringRestrictions: StringRestrictions
    supportedDbVersions: _list[
        typing_extensions.Literal[
            "DATABASE_VERSION_UNSPECIFIED",
            "POSTGRES_13",
            "POSTGRES_14",
            "POSTGRES_15",
            "POSTGRES_16",
        ]
    ]
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED", "STRING", "INTEGER", "FLOAT", "NONE"
    ]

@typing.type_check_only
class SwitchoverClusterRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    validateOnly: bool

@typing.type_check_only
class TimeBasedRetention(typing_extensions.TypedDict, total=False):
    retentionPeriod: str

@typing.type_check_only
class TrialMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    graceEndTime: str
    startTime: str
    upgradeTime: str

@typing.type_check_only
class UpdatePolicy(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DEFAULT", "FORCE_APPLY"]

@typing.type_check_only
class UpgradeClusterRequest(typing_extensions.TypedDict, total=False):
    etag: str
    requestId: str
    validateOnly: bool
    version: typing_extensions.Literal[
        "DATABASE_VERSION_UNSPECIFIED",
        "POSTGRES_13",
        "POSTGRES_14",
        "POSTGRES_15",
        "POSTGRES_16",
    ]

@typing.type_check_only
class UpgradeClusterResponse(typing_extensions.TypedDict, total=False):
    clusterUpgradeDetails: _list[ClusterUpgradeDetails]
    message: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NOT_STARTED",
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
        "PARTIAL_SUCCESS",
        "CANCEL_IN_PROGRESS",
        "CANCELLED",
    ]

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    databaseRoles: _list[str]
    keepExtraRoles: bool
    name: str
    password: str
    userType: typing_extensions.Literal[
        "USER_TYPE_UNSPECIFIED", "ALLOYDB_BUILT_IN", "ALLOYDB_IAM_USER"
    ]

@typing.type_check_only
class UserPassword(typing_extensions.TypedDict, total=False):
    password: str
    user: str

@typing.type_check_only
class WeeklySchedule(typing_extensions.TypedDict, total=False):
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
    startTimes: _list[GoogleTypeTimeOfDay]
