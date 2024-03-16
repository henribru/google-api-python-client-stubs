import typing

import typing_extensions

_list = list

@typing.type_check_only
class AvailabilityConfiguration(typing_extensions.TypedDict, total=False):
    availabilityType: typing_extensions.Literal[
        "AVAILABILITY_TYPE_UNSPECIFIED",
        "ZONAL",
        "REGIONAL",
        "MULTI_REGIONAL",
        "AVAILABILITY_TYPE_OTHER",
    ]
    externalReplicaConfigured: bool
    promotableReplicaConfigured: bool

@typing.type_check_only
class BackupConfiguration(typing_extensions.TypedDict, total=False):
    automatedBackupEnabled: bool
    backupRetentionSettings: RetentionSettings
    pointInTimeRecoveryEnabled: bool

@typing.type_check_only
class BackupRun(typing_extensions.TypedDict, total=False):
    endTime: str
    error: OperationError
    startTime: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "SUCCESSFUL", "FAILED"]

@typing.type_check_only
class CertChain(typing_extensions.TypedDict, total=False):
    certificates: _list[str]

@typing.type_check_only
class CertificateAuthority(typing_extensions.TypedDict, total=False):
    managedServerCa: ManagedCertificateAuthority
    name: str

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    authorizationMode: typing_extensions.Literal[
        "AUTH_MODE_UNSPECIFIED", "AUTH_MODE_IAM_AUTH", "AUTH_MODE_DISABLED"
    ]
    createTime: str
    discoveryEndpoints: _list[DiscoveryEndpoint]
    name: str
    pscConfigs: _list[PscConfig]
    pscConnections: _list[PscConnection]
    replicaCount: int
    shardCount: int
    sizeGb: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING"
    ]
    stateInfo: StateInfo
    transitEncryptionMode: typing_extensions.Literal[
        "TRANSIT_ENCRYPTION_MODE_UNSPECIFIED",
        "TRANSIT_ENCRYPTION_MODE_DISABLED",
        "TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION",
    ]
    uid: str

@typing.type_check_only
class Compliance(typing_extensions.TypedDict, total=False):
    standard: str
    version: str

@typing.type_check_only
class CustomMetadataData(typing_extensions.TypedDict, total=False):
    databaseMetadata: _list[DatabaseMetadata]

@typing.type_check_only
class DatabaseMetadata(typing_extensions.TypedDict, total=False):
    backupConfiguration: BackupConfiguration
    backupRun: BackupRun
    product: Product
    resourceId: DatabaseResourceId
    resourceName: str

@typing.type_check_only
class DatabaseResourceFeed(typing_extensions.TypedDict, total=False):
    feedTimestamp: str
    feedType: typing_extensions.Literal[
        "FEEDTYPE_UNSPECIFIED",
        "RESOURCE_METADATA",
        "OBSERVABILITY_DATA",
        "SECURITY_FINDING_DATA",
        "RECOMMENDATION_SIGNAL_DATA",
    ]
    recommendationSignalData: DatabaseResourceRecommendationSignalData
    resourceHealthSignalData: DatabaseResourceHealthSignalData
    resourceId: DatabaseResourceId
    resourceMetadata: DatabaseResourceMetadata

@typing.type_check_only
class DatabaseResourceHealthSignalData(typing_extensions.TypedDict, total=False):
    additionalMetadata: dict[str, typing.Any]
    compliance: _list[Compliance]
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
        "SIGNAL_TYPE_VIOLATES_NIST_800_53",
        "SIGNAL_TYPE_VIOLATES_ISO_27001",
        "SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1",
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
    ]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "RESOLVED", "MUTED"]

@typing.type_check_only
class DatabaseResourceId(typing_extensions.TypedDict, total=False):
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
class DatabaseResourceMetadata(typing_extensions.TypedDict, total=False):
    availabilityConfiguration: AvailabilityConfiguration
    backupConfiguration: BackupConfiguration
    backupRun: BackupRun
    creationTime: str
    currentState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "SUSPENDED",
        "DELETED",
        "STATE_OTHER",
    ]
    customMetadata: CustomMetadataData
    entitlements: _list[Entitlement]
    expectedState: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "SUSPENDED",
        "DELETED",
        "STATE_OTHER",
    ]
    id: DatabaseResourceId
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
    primaryResourceId: DatabaseResourceId
    product: Product
    resourceContainer: str
    resourceName: str
    updationTime: str
    userLabels: dict[str, typing.Any]

@typing.type_check_only
class DatabaseResourceRecommendationSignalData(
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
        "SIGNAL_TYPE_VIOLATES_NIST_800_53",
        "SIGNAL_TYPE_VIOLATES_ISO_27001",
        "SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1",
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
    ]

@typing.type_check_only
class DiscoveryEndpoint(typing_extensions.TypedDict, total=False):
    address: str
    port: int
    pscConfig: PscConfig

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entitlement(typing_extensions.TypedDict, total=False):
    entitlementState: typing_extensions.Literal[
        "ENTITLEMENT_STATE_UNSPECIFIED", "ENTITLED", "REVOKED"
    ]
    type: typing_extensions.Literal["ENTITLEMENT_TYPE_UNSPECIFIED", "DUET_AI", "GEMINI"]

@typing.type_check_only
class ExportInstanceRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

@typing.type_check_only
class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    dataProtectionMode: typing_extensions.Literal[
        "DATA_PROTECTION_MODE_UNSPECIFIED", "LIMITED_DATA_LOSS", "FORCE_DATA_LOSS"
    ]

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudRedisV1LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRedisV1OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudRedisV1ZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportInstanceRequest(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig

@typing.type_check_only
class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    alternativeLocationId: str
    authEnabled: bool
    authorizedNetwork: str
    availableMaintenanceVersions: _list[str]
    connectMode: typing_extensions.Literal[
        "CONNECT_MODE_UNSPECIFIED", "DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"
    ]
    createTime: str
    currentLocationId: str
    customerManagedKey: str
    displayName: str
    host: str
    labels: dict[str, typing.Any]
    locationId: str
    maintenancePolicy: MaintenancePolicy
    maintenanceSchedule: MaintenanceSchedule
    maintenanceVersion: str
    memorySizeGb: int
    name: str
    nodes: _list[NodeInfo]
    persistenceConfig: PersistenceConfig
    persistenceIamIdentity: str
    port: int
    readEndpoint: str
    readEndpointPort: int
    readReplicasMode: typing_extensions.Literal[
        "READ_REPLICAS_MODE_UNSPECIFIED",
        "READ_REPLICAS_DISABLED",
        "READ_REPLICAS_ENABLED",
    ]
    redisConfigs: dict[str, typing.Any]
    redisVersion: str
    replicaCount: int
    reservedIpRange: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    secondaryIpRange: str
    serverCaCerts: _list[TlsCertificate]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "MAINTENANCE",
        "IMPORTING",
        "FAILING_OVER",
    ]
    statusMessage: str
    suspensionReasons: _list[
        typing_extensions.Literal[
            "SUSPENSION_REASON_UNSPECIFIED", "CUSTOMER_MANAGED_KEY_ISSUE"
        ]
    ]
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "BASIC", "STANDARD_HA"]
    transitEncryptionMode: typing_extensions.Literal[
        "TRANSIT_ENCRYPTION_MODE_UNSPECIFIED", "SERVER_AUTHENTICATION", "DISABLED"
    ]

@typing.type_check_only
class InstanceAuthString(typing_extensions.TypedDict, total=False):
    authString: str

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
class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    updateTime: str
    weeklyMaintenanceWindow: _list[WeeklyMaintenanceWindow]

@typing.type_check_only
class MaintenanceSchedule(typing_extensions.TypedDict, total=False):
    canReschedule: bool
    endTime: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class ManagedCertificateAuthority(typing_extensions.TypedDict, total=False):
    caCerts: _list[CertChain]

@typing.type_check_only
class NodeInfo(typing_extensions.TypedDict, total=False):
    id: str
    zone: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationError(typing_extensions.TypedDict, total=False):
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
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class PersistenceConfig(typing_extensions.TypedDict, total=False):
    persistenceMode: typing_extensions.Literal[
        "PERSISTENCE_MODE_UNSPECIFIED", "DISABLED", "RDB"
    ]
    rdbNextSnapshotTime: str
    rdbSnapshotPeriod: typing_extensions.Literal[
        "SNAPSHOT_PERIOD_UNSPECIFIED",
        "ONE_HOUR",
        "SIX_HOURS",
        "TWELVE_HOURS",
        "TWENTY_FOUR_HOURS",
    ]
    rdbSnapshotStartTime: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
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
        "PRODUCT_TYPE_OTHER",
    ]
    version: str

@typing.type_check_only
class PscConfig(typing_extensions.TypedDict, total=False):
    network: str

@typing.type_check_only
class PscConnection(typing_extensions.TypedDict, total=False):
    address: str
    forwardingRule: str
    network: str
    projectId: str
    pscConnectionId: str

@typing.type_check_only
class ReconciliationOperationMetadata(typing_extensions.TypedDict, total=False):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

@typing.type_check_only
class RescheduleMaintenanceRequest(typing_extensions.TypedDict, total=False):
    rescheduleType: typing_extensions.Literal[
        "RESCHEDULE_TYPE_UNSPECIFIED",
        "IMMEDIATE",
        "NEXT_AVAILABLE_WINDOW",
        "SPECIFIC_TIME",
    ]
    scheduleTime: str

@typing.type_check_only
class RetentionSettings(typing_extensions.TypedDict, total=False):
    quantityBasedRetention: int
    retentionUnit: typing_extensions.Literal[
        "RETENTION_UNIT_UNSPECIFIED", "COUNT", "TIME", "RETENTION_UNIT_OTHER"
    ]
    timeBasedRetention: str

@typing.type_check_only
class StateInfo(typing_extensions.TypedDict, total=False):
    updateInfo: UpdateInfo

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
class TlsCertificate(typing_extensions.TypedDict, total=False):
    cert: str
    createTime: str
    expireTime: str
    serialNumber: str
    sha1Fingerprint: str

@typing.type_check_only
class UpdateInfo(typing_extensions.TypedDict, total=False):
    targetReplicaCount: int
    targetShardCount: int

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False):
    redisVersion: str

@typing.type_check_only
class WeeklyMaintenanceWindow(typing_extensions.TypedDict, total=False):
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
    duration: str
    startTime: TimeOfDay
