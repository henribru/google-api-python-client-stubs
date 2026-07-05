import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdditionalDetail(typing_extensions.TypedDict, total=False):
    automatedBackupPolicyInfo: AutomatedBackupPolicyInfo
    backupRunInfo: BackupRunInfo
    deletionProtectionInfo: DeletionProtectionInfo
    inefficientQueryInfo: InefficientQueryInfo
    maintenanceRecommendationInfo: MaintenanceRecommendationInfo
    outdatedMinorVersionInfo: OutdatedMinorVersionInfo
    recommendationInfo: RecommendationInfo
    resourceSuspensionInfo: ResourceSuspensionInfo
    sccInfo: SCCInfo
    shortBackupRetentionInfo: RetentionSettingsInfo
    signalEventTime: str
    signalSource: typing_extensions.Literal[
        "SIGNAL_SOURCE_UNSPECIFIED",
        "SIGNAL_SOURCE_RESOURCE_METADATA",
        "SIGNAL_SOURCE_SECURITY_FINDINGS",
        "SIGNAL_SOURCE_RECOMMENDER",
        "SIGNAL_SOURCE_MODERN_OBSERVABILITY",
    ]
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED",
        "SIGNAL_TYPE_GROUP_MULTIREGIONAL",
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
        "SIGNAL_TYPE_QUERY_STATS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
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
        "SIGNAL_TYPE_HOT_NODE",
        "SIGNAL_TYPE_NO_DELETION_PROTECTION",
        "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY",
        "SIGNAL_TYPE_RESOURCE_SUSPENDED",
        "SIGNAL_TYPE_EXPENSIVE_COMMANDS",
        "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED",
        "SIGNAL_TYPE_INEFFICIENT_QUERY",
        "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD",
        "SIGNAL_TYPE_MEMORY_LIMIT",
        "SIGNAL_TYPE_MAX_SERVER_MEMORY",
        "SIGNAL_TYPE_LARGE_ROWS",
        "SIGNAL_TYPE_HIGH_WRITE_PRESSURE",
        "SIGNAL_TYPE_HIGH_READ_PRESSURE",
        "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_OUTDATED_MINOR_VERSION",
        "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED",
        "SIGNAL_TYPE_REPLICATION_LAG",
        "SIGNAL_TYPE_OUTDATED_CLIENT",
        "SIGNAL_TYPE_DATABOOST_DISABLED",
        "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES",
        "SIGNAL_TYPE_EXTENDED_SUPPORT",
        "SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE",
        "SIGNAL_TYPE_HIGH_MAINTENANCE_DOWNTIME_RISK",
        "SIGNAL_TYPE_LOW_CACHE_HIT_AND_MAINTENANCE_DOWNTIME",
    ]

@typing.type_check_only
class Affiliation(typing_extensions.TypedDict, total=False):
    fullResourceName: str
    lineages: _list[Lineage]
    resourceId: str

@typing.type_check_only
class AggregateFleetResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resourceGroupsTotalCount: int
    resourceTotalCount: int
    rows: _list[AggregateFleetRow]
    totalSize: str
    unreachable: _list[str]

@typing.type_check_only
class AggregateFleetRow(typing_extensions.TypedDict, total=False):
    deltaDetails: DeltaDetails
    dimension: _list[Dimension]
    resourceGroupsCount: int
    resourcesCount: int

@typing.type_check_only
class AggregateIssueStatsRequest(typing_extensions.TypedDict, total=False):
    baselineDate: Date
    filter: str
    parent: str
    signalTypeGroups: _list[SignalTypeGroup]

@typing.type_check_only
class AggregateIssueStatsResponse(typing_extensions.TypedDict, total=False):
    issueGroupStats: _list[IssueGroupStats]
    totalResourceGroupsCount: int
    totalResourcesCount: int
    unreachable: _list[str]

@typing.type_check_only
class AggregateQueryStatsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class AggregateQueryStatsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queryStats: _list[QueryStatsInfo]
    unreachable: _list[str]

@typing.type_check_only
class AutomatedBackupPolicyInfo(typing_extensions.TypedDict, total=False):
    isEnabled: bool
    subResource: SubResource

@typing.type_check_only
class BackupDRConfig(typing_extensions.TypedDict, total=False):
    backupdrManaged: bool

@typing.type_check_only
class BackupRunInfo(typing_extensions.TypedDict, total=False):
    endTime: str
    errorMessage: str
    operationErrorType: typing_extensions.Literal[
        "OPERATION_ERROR_TYPE_UNSPECIFIED",
        "KMS_KEY_ERROR",
        "DATABASE_ERROR",
        "STOCKOUT_ERROR",
        "CANCELLATION_ERROR",
        "SQLSERVER_ERROR",
        "INTERNAL_ERROR",
    ]
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    subResource: SubResource

@typing.type_check_only
class DatabaseResource(typing_extensions.TypedDict, total=False):
    affiliations: _list[Affiliation]
    backupdrConfig: BackupDRConfig
    childResources: _list[DatabaseResource]
    container: str
    edition: typing_extensions.Literal[
        "EDITION_UNSPECIFIED",
        "EDITION_ENTERPRISE",
        "EDITION_ENTERPRISE_PLUS",
        "EDITION_STANDARD",
    ]
    fullResourceName: str
    labels: _list[Label]
    location: str
    machineConfig: MachineConfig
    maintenanceInfo: MaintenanceInfo
    metrics: Metrics
    product: Product
    resourceCategory: typing_extensions.Literal[
        "RESOURCE_CATEGORY_UNSPECIFIED",
        "INSTANCE",
        "CLUSTER",
        "DATABASE",
        "DATASET",
        "RESERVATION",
    ]
    resourceName: str
    resourceType: str
    signalGroups: _list[SignalGroup]
    subResourceType: typing_extensions.Literal[
        "SUB_RESOURCE_TYPE_UNSPECIFIED",
        "SUB_RESOURCE_TYPE_PRIMARY",
        "SUB_RESOURCE_TYPE_SECONDARY",
        "SUB_RESOURCE_TYPE_READ_REPLICA",
        "SUB_RESOURCE_TYPE_EXTERNAL_PRIMARY",
        "SUB_RESOURCE_TYPE_READ_POOL",
        "SUB_RESOURCE_TYPE_RESERVATION",
        "SUB_RESOURCE_TYPE_DATASET",
        "SUB_RESOURCE_TYPE_OTHER",
    ]
    tags: _list[Tag]

@typing.type_check_only
class DatabaseResourceGroup(typing_extensions.TypedDict, total=False):
    rootResources: _list[DatabaseResource]
    signalGroups: _list[IssueCount]

@typing.type_check_only
class DatabaseResourceIssue(typing_extensions.TypedDict, total=False):
    resource: DatabaseResource
    signal: Signal

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeletionProtectionInfo(typing_extensions.TypedDict, total=False):
    deletionProtectionEnabled: bool
    subResource: SubResource

@typing.type_check_only
class DeltaDetails(typing_extensions.TypedDict, total=False):
    decreasedResources: _list[ResourceDetails]
    increasedResources: _list[ResourceDetails]

@typing.type_check_only
class Dimension(typing_extensions.TypedDict, total=False):
    container: str
    edition: typing_extensions.Literal[
        "EDITION_UNSPECIFIED",
        "EDITION_ENTERPRISE",
        "EDITION_ENTERPRISE_PLUS",
        "EDITION_STANDARD",
    ]
    hasDenyMaintenanceSchedules: bool
    hasMaintenanceSchedule: bool
    labelKey: str
    labelSource: str
    labelValue: str
    location: str
    managementType: typing_extensions.Literal[
        "MANAGEMENT_TYPE_UNSPECIFIED",
        "MANAGEMENT_TYPE_GCP_MANAGED",
        "MANAGEMENT_TYPE_SELF_MANAGED",
    ]
    productEngine: typing_extensions.Literal[
        "ENGINE_UNSPECIFIED",
        "ENGINE_MYSQL",
        "ENGINE_POSTGRES",
        "ENGINE_SQL_SERVER",
        "ENGINE_NATIVE",
        "ENGINE_MEMORYSTORE_FOR_REDIS",
        "ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER",
        "ENGINE_MEMORSTORE_FOR_VALKEY",
        "ENGINE_MEMORYSTORE_FOR_VALKEY",
        "ENGINE_FIRESTORE_WITH_NATIVE_MODE",
        "ENGINE_FIRESTORE_WITH_DATASTORE_MODE",
        "ENGINE_EXADATA_ORACLE",
        "ENGINE_ADB_SERVERLESS_ORACLE",
        "ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE",
        "ENGINE_OTHER",
    ]
    productType: typing_extensions.Literal[
        "PRODUCT_TYPE_UNSPECIFIED",
        "PRODUCT_TYPE_CLOUD_SQL",
        "PRODUCT_TYPE_ALLOYDB",
        "PRODUCT_TYPE_SPANNER",
        "PRODUCT_TYPE_BIGTABLE",
        "PRODUCT_TYPE_MEMORYSTORE",
        "PRODUCT_TYPE_FIRESTORE",
        "PRODUCT_TYPE_COMPUTE_ENGINE",
        "PRODUCT_TYPE_ORACLE_ON_GCP",
        "PRODUCT_TYPE_BIGQUERY",
        "PRODUCT_TYPE_OTHER",
    ]
    productVersion: str
    resourceCategory: typing_extensions.Literal[
        "RESOURCE_CATEGORY_UNSPECIFIED",
        "INSTANCE",
        "CLUSTER",
        "DATABASE",
        "DATASET",
        "RESERVATION",
    ]
    resourceType: str
    subResourceType: typing_extensions.Literal[
        "SUB_RESOURCE_TYPE_UNSPECIFIED",
        "SUB_RESOURCE_TYPE_PRIMARY",
        "SUB_RESOURCE_TYPE_SECONDARY",
        "SUB_RESOURCE_TYPE_READ_REPLICA",
        "SUB_RESOURCE_TYPE_EXTERNAL_PRIMARY",
        "SUB_RESOURCE_TYPE_READ_POOL",
        "SUB_RESOURCE_TYPE_RESERVATION",
        "SUB_RESOURCE_TYPE_DATASET",
        "SUB_RESOURCE_TYPE_OTHER",
    ]
    tagInherited: bool
    tagKey: str
    tagSource: str
    tagValue: str

@typing.type_check_only
class InefficientQueryInfo(typing_extensions.TypedDict, total=False):
    database: str
    impactedQueriesCount: str
    sqlIndexStatement: str
    storageCostBytes: str
    table: str

@typing.type_check_only
class IssueCount(typing_extensions.TypedDict, total=False):
    displayName: str
    issueCount: int

@typing.type_check_only
class IssueGroupStats(typing_extensions.TypedDict, total=False):
    displayName: str
    healthyResourceGroupsCount: int
    healthyResourcesCount: int
    issueStats: _list[IssueStats]
    resourceGroupsCount: int
    resourcesCount: int

@typing.type_check_only
class IssueStats(typing_extensions.TypedDict, total=False):
    deltaDetails: DeltaDetails
    issueSeverity: typing_extensions.Literal[
        "ISSUE_SEVERITY_UNSPECIFIED",
        "ISSUE_SEVERITY_LOW",
        "ISSUE_SEVERITY_MEDIUM",
        "ISSUE_SEVERITY_HIGH",
        "ISSUE_SEVERITY_CRITICAL",
        "ISSUE_SEVERITY_IRRELEVANT",
    ]
    resourceCount: int
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED",
        "SIGNAL_TYPE_GROUP_MULTIREGIONAL",
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
        "SIGNAL_TYPE_QUERY_STATS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
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
        "SIGNAL_TYPE_HOT_NODE",
        "SIGNAL_TYPE_NO_DELETION_PROTECTION",
        "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY",
        "SIGNAL_TYPE_RESOURCE_SUSPENDED",
        "SIGNAL_TYPE_EXPENSIVE_COMMANDS",
        "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED",
        "SIGNAL_TYPE_INEFFICIENT_QUERY",
        "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD",
        "SIGNAL_TYPE_MEMORY_LIMIT",
        "SIGNAL_TYPE_MAX_SERVER_MEMORY",
        "SIGNAL_TYPE_LARGE_ROWS",
        "SIGNAL_TYPE_HIGH_WRITE_PRESSURE",
        "SIGNAL_TYPE_HIGH_READ_PRESSURE",
        "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_OUTDATED_MINOR_VERSION",
        "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED",
        "SIGNAL_TYPE_REPLICATION_LAG",
        "SIGNAL_TYPE_OUTDATED_CLIENT",
        "SIGNAL_TYPE_DATABOOST_DISABLED",
        "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES",
        "SIGNAL_TYPE_EXTENDED_SUPPORT",
        "SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE",
        "SIGNAL_TYPE_HIGH_MAINTENANCE_DOWNTIME_RISK",
        "SIGNAL_TYPE_LOW_CACHE_HIT_AND_MAINTENANCE_DOWNTIME",
    ]

@typing.type_check_only
class Label(typing_extensions.TypedDict, total=False):
    key: str
    source: str
    value: str

@typing.type_check_only
class Lineage(typing_extensions.TypedDict, total=False):
    processFqn: str
    processType: typing_extensions.Literal[
        "PROCESS_TYPE_UNSPECIFIED",
        "COMPOSER",
        "DATASTREAM",
        "DATAFLOW",
        "BIGQUERY",
        "DATA_FUSION",
        "DATAPROC",
    ]
    sourceFqn: str
    targetFqn: str

@typing.type_check_only
class MachineConfig(typing_extensions.TypedDict, total=False):
    baselineSlotCount: str
    maxReservationSlotCount: str
    memorySizeBytes: str
    shardCount: int
    vcpuCount: float

@typing.type_check_only
class MaintenanceInfo(typing_extensions.TypedDict, total=False):
    currentVersionReleaseDate: Date
    denyMaintenanceSchedules: _list[ResourceMaintenanceDenySchedule]
    maintenanceSchedule: ResourceMaintenanceSchedule
    maintenanceVersion: str
    possibleFailureReasons: _list[
        typing_extensions.Literal[
            "POSSIBLE_FAILURE_REASON_UNSPECIFIED",
            "POSSIBLE_FAILURE_REASON_DENY_POLICY_CONFLICT",
            "POSSIBLE_FAILURE_REASON_INSTANCE_IN_STOPPED_STATE",
        ]
    ]
    previousMaintenanceVersion: str
    state: typing_extensions.Literal[
        "MAINTENANCE_STATE_UNSPECIFIED",
        "MAINTENANCE_STATE_SCHEDULED",
        "MAINTENANCE_STATE_IN_PROGRESS",
        "MAINTENANCE_STATE_COMPLETED",
        "MAINTENANCE_STATE_FAILED",
    ]
    upcomingMaintenance: UpcomingMaintenance

@typing.type_check_only
class MaintenanceRecommendationInfo(typing_extensions.TypedDict, total=False):
    resourceMaintenanceSchedules: _list[ResourceMaintenanceSchedule]

@typing.type_check_only
class MetricData(typing_extensions.TypedDict, total=False):
    observationTime: str
    value: TypedValue

@typing.type_check_only
class Metrics(typing_extensions.TypedDict, total=False):
    currentMemoryUsedBytes: MetricData
    currentStorageUsedBytes: MetricData
    nodeCount: MetricData
    p95CpuUtilization: MetricData
    p99CpuUtilization: MetricData
    peakMemoryUtilization: MetricData
    peakNumberConnections: MetricData
    peakStorageUtilization: MetricData
    processingUnitCount: MetricData

@typing.type_check_only
class OutdatedMinorVersionInfo(typing_extensions.TypedDict, total=False):
    recommendedMinorVersion: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal[
        "ENGINE_UNSPECIFIED",
        "ENGINE_MYSQL",
        "ENGINE_POSTGRES",
        "ENGINE_SQL_SERVER",
        "ENGINE_NATIVE",
        "ENGINE_MEMORYSTORE_FOR_REDIS",
        "ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER",
        "ENGINE_MEMORSTORE_FOR_VALKEY",
        "ENGINE_MEMORYSTORE_FOR_VALKEY",
        "ENGINE_FIRESTORE_WITH_NATIVE_MODE",
        "ENGINE_FIRESTORE_WITH_DATASTORE_MODE",
        "ENGINE_EXADATA_ORACLE",
        "ENGINE_ADB_SERVERLESS_ORACLE",
        "ENGINE_FIRESTORE_WITH_MONGODB_COMPATIBILITY_MODE",
        "ENGINE_OTHER",
    ]
    minorVersion: str
    type: typing_extensions.Literal[
        "PRODUCT_TYPE_UNSPECIFIED",
        "PRODUCT_TYPE_CLOUD_SQL",
        "PRODUCT_TYPE_ALLOYDB",
        "PRODUCT_TYPE_SPANNER",
        "PRODUCT_TYPE_BIGTABLE",
        "PRODUCT_TYPE_MEMORYSTORE",
        "PRODUCT_TYPE_FIRESTORE",
        "PRODUCT_TYPE_COMPUTE_ENGINE",
        "PRODUCT_TYPE_ORACLE_ON_GCP",
        "PRODUCT_TYPE_BIGQUERY",
        "PRODUCT_TYPE_OTHER",
    ]
    version: str

@typing.type_check_only
class QueryDatabaseResourceGroupsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    parent: str
    signalFilters: _list[SignalFilter]
    signalTypeGroups: _list[SignalTypeGroup]

@typing.type_check_only
class QueryDatabaseResourceGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resourceGroups: _list[DatabaseResourceGroup]
    totalSize: str
    unreachable: _list[str]

@typing.type_check_only
class QueryIssuesRequest(typing_extensions.TypedDict, total=False):
    filter: str
    orderBy: str
    pageSize: int
    pageToken: str
    parent: str
    signalProductsFilters: _list[SignalProductsFilters]

@typing.type_check_only
class QueryIssuesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resourceIssues: _list[DatabaseResourceIssue]
    unreachable: _list[str]

@typing.type_check_only
class QueryMetrics(typing_extensions.TypedDict, total=False):
    avgCpuTime: str
    executionCount: str
    metricsWindow: typing_extensions.Literal[
        "METRICS_WINDOW_UNSPECIFIED", "LAST_ONE_DAY", "LAST_ONE_WEEK", "LAST_TWO_WEEKS"
    ]
    rowsProcessed: str
    totalCpuTime: str

@typing.type_check_only
class QueryProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]
    unreachable: _list[str]

@typing.type_check_only
class QueryStats(typing_extensions.TypedDict, total=False):
    inefficientQueryInfo: InefficientQueryInfo
    normalizedQuery: str
    queryHash: str
    queryMetrics: QueryMetrics
    resourceIds: _list[ResourceId]
    resourceType: str

@typing.type_check_only
class QueryStatsInfo(typing_extensions.TypedDict, total=False):
    aggregatedQueryStats: QueryStats
    queryStats: _list[QueryStats]

@typing.type_check_only
class RecommendationInfo(typing_extensions.TypedDict, total=False):
    recommender: str
    recommenderId: str
    recommenderSubtype: str

@typing.type_check_only
class RegulatoryStandard(typing_extensions.TypedDict, total=False):
    standard: str
    version: str

@typing.type_check_only
class ResourceDetails(typing_extensions.TypedDict, total=False):
    container: str
    fullResourceName: str
    location: str
    product: Product

@typing.type_check_only
class ResourceId(typing_extensions.TypedDict, total=False):
    fullResourceName: str
    product: Product
    resourceType: str

@typing.type_check_only
class ResourceMaintenanceDenySchedule(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date
    time: TimeOfDay

@typing.type_check_only
class ResourceMaintenanceSchedule(typing_extensions.TypedDict, total=False):
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
    phase: typing_extensions.Literal[
        "PHASE_UNSPECIFIED", "PHASE_WEEK1", "PHASE_WEEK2", "PHASE_WEEK5", "PHASE_ANY"
    ]
    startTime: TimeOfDay

@typing.type_check_only
class ResourceSuspensionInfo(typing_extensions.TypedDict, total=False):
    resourceSuspended: bool
    suspensionReason: typing_extensions.Literal[
        "SUSPENSION_REASON_UNSPECIFIED",
        "WIPEOUT_HIDE_EVENT",
        "WIPEOUT_PURGE_EVENT",
        "BILLING_DISABLED",
        "ABUSER_DETECTED",
        "ENCRYPTION_KEY_INACCESSIBLE",
        "REPLICATED_CLUSTER_ENCRYPTION_KEY_INACCESSIBLE",
    ]

@typing.type_check_only
class RetentionSettingsInfo(typing_extensions.TypedDict, total=False):
    durationBasedRetention: str
    quantityBasedRetention: int
    subResource: SubResource
    timestampBasedRetentionTime: str

@typing.type_check_only
class SCCInfo(typing_extensions.TypedDict, total=False):
    category: str
    externalUri: str
    regulatoryStandards: _list[RegulatoryStandard]
    signal: str

@typing.type_check_only
class Signal(typing_extensions.TypedDict, total=False):
    additionalDetails: _list[AdditionalDetail]
    issueCreateTime: str
    issueSeverity: typing_extensions.Literal[
        "ISSUE_SEVERITY_UNSPECIFIED",
        "ISSUE_SEVERITY_LOW",
        "ISSUE_SEVERITY_MEDIUM",
        "ISSUE_SEVERITY_HIGH",
        "ISSUE_SEVERITY_CRITICAL",
        "ISSUE_SEVERITY_IRRELEVANT",
    ]
    signalStatus: typing_extensions.Literal[
        "SIGNAL_STATUS_UNSPECIFIED",
        "SIGNAL_STATUS_NOT_APPLICABLE",
        "SIGNAL_STATUS_OK",
        "SIGNAL_STATUS_ISSUE",
        "SIGNAL_STATUS_NOT_ENABLED",
    ]
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED",
        "SIGNAL_TYPE_GROUP_MULTIREGIONAL",
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
        "SIGNAL_TYPE_QUERY_STATS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
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
        "SIGNAL_TYPE_HOT_NODE",
        "SIGNAL_TYPE_NO_DELETION_PROTECTION",
        "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY",
        "SIGNAL_TYPE_RESOURCE_SUSPENDED",
        "SIGNAL_TYPE_EXPENSIVE_COMMANDS",
        "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED",
        "SIGNAL_TYPE_INEFFICIENT_QUERY",
        "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD",
        "SIGNAL_TYPE_MEMORY_LIMIT",
        "SIGNAL_TYPE_MAX_SERVER_MEMORY",
        "SIGNAL_TYPE_LARGE_ROWS",
        "SIGNAL_TYPE_HIGH_WRITE_PRESSURE",
        "SIGNAL_TYPE_HIGH_READ_PRESSURE",
        "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_OUTDATED_MINOR_VERSION",
        "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED",
        "SIGNAL_TYPE_REPLICATION_LAG",
        "SIGNAL_TYPE_OUTDATED_CLIENT",
        "SIGNAL_TYPE_DATABOOST_DISABLED",
        "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES",
        "SIGNAL_TYPE_EXTENDED_SUPPORT",
        "SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE",
        "SIGNAL_TYPE_HIGH_MAINTENANCE_DOWNTIME_RISK",
        "SIGNAL_TYPE_LOW_CACHE_HIT_AND_MAINTENANCE_DOWNTIME",
    ]

@typing.type_check_only
class SignalFilter(typing_extensions.TypedDict, total=False):
    signalStatus: typing_extensions.Literal[
        "SIGNAL_STATUS_UNSPECIFIED",
        "SIGNAL_STATUS_NOT_APPLICABLE",
        "SIGNAL_STATUS_OK",
        "SIGNAL_STATUS_ISSUE",
        "SIGNAL_STATUS_NOT_ENABLED",
    ]
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED",
        "SIGNAL_TYPE_GROUP_MULTIREGIONAL",
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
        "SIGNAL_TYPE_QUERY_STATS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
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
        "SIGNAL_TYPE_HOT_NODE",
        "SIGNAL_TYPE_NO_DELETION_PROTECTION",
        "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY",
        "SIGNAL_TYPE_RESOURCE_SUSPENDED",
        "SIGNAL_TYPE_EXPENSIVE_COMMANDS",
        "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED",
        "SIGNAL_TYPE_INEFFICIENT_QUERY",
        "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD",
        "SIGNAL_TYPE_MEMORY_LIMIT",
        "SIGNAL_TYPE_MAX_SERVER_MEMORY",
        "SIGNAL_TYPE_LARGE_ROWS",
        "SIGNAL_TYPE_HIGH_WRITE_PRESSURE",
        "SIGNAL_TYPE_HIGH_READ_PRESSURE",
        "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_OUTDATED_MINOR_VERSION",
        "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED",
        "SIGNAL_TYPE_REPLICATION_LAG",
        "SIGNAL_TYPE_OUTDATED_CLIENT",
        "SIGNAL_TYPE_DATABOOST_DISABLED",
        "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES",
        "SIGNAL_TYPE_EXTENDED_SUPPORT",
        "SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE",
        "SIGNAL_TYPE_HIGH_MAINTENANCE_DOWNTIME_RISK",
        "SIGNAL_TYPE_LOW_CACHE_HIT_AND_MAINTENANCE_DOWNTIME",
    ]

@typing.type_check_only
class SignalGroup(typing_extensions.TypedDict, total=False):
    displayName: str
    issueCount: int
    signals: _list[Signal]

@typing.type_check_only
class SignalProductsFilters(typing_extensions.TypedDict, total=False):
    products: _list[Product]
    signalType: typing_extensions.Literal[
        "SIGNAL_TYPE_UNSPECIFIED",
        "SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED",
        "SIGNAL_TYPE_GROUP_MULTIREGIONAL",
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
        "SIGNAL_TYPE_QUERY_STATS_LOGGED",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS",
        "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
        "SIGNAL_TYPE_LOGGING_QUERY_STATS",
        "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
        "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
        "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
        "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
        "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
        "SIGNAL_TYPE_NO_ROOT_PASSWORD",
        "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
        "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
        "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
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
        "SIGNAL_TYPE_HOT_NODE",
        "SIGNAL_TYPE_NO_DELETION_PROTECTION",
        "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY",
        "SIGNAL_TYPE_RESOURCE_SUSPENDED",
        "SIGNAL_TYPE_EXPENSIVE_COMMANDS",
        "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED",
        "SIGNAL_TYPE_INEFFICIENT_QUERY",
        "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD",
        "SIGNAL_TYPE_MEMORY_LIMIT",
        "SIGNAL_TYPE_MAX_SERVER_MEMORY",
        "SIGNAL_TYPE_LARGE_ROWS",
        "SIGNAL_TYPE_HIGH_WRITE_PRESSURE",
        "SIGNAL_TYPE_HIGH_READ_PRESSURE",
        "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED",
        "SIGNAL_TYPE_OUTDATED_MINOR_VERSION",
        "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED",
        "SIGNAL_TYPE_REPLICATION_LAG",
        "SIGNAL_TYPE_OUTDATED_CLIENT",
        "SIGNAL_TYPE_DATABOOST_DISABLED",
        "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES",
        "SIGNAL_TYPE_EXTENDED_SUPPORT",
        "SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE",
        "SIGNAL_TYPE_HIGH_MAINTENANCE_DOWNTIME_RISK",
        "SIGNAL_TYPE_LOW_CACHE_HIT_AND_MAINTENANCE_DOWNTIME",
    ]

@typing.type_check_only
class SignalTypeGroup(typing_extensions.TypedDict, total=False):
    displayName: str
    signalTypes: _list[
        typing_extensions.Literal[
            "SIGNAL_TYPE_UNSPECIFIED",
            "SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED",
            "SIGNAL_TYPE_GROUP_MULTIREGIONAL",
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
            "SIGNAL_TYPE_QUERY_STATS_LOGGED",
            "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME",
            "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS",
            "SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS",
            "SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS",
            "SIGNAL_TYPE_LOGGING_QUERY_STATS",
            "SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES",
            "SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED",
            "SIGNAL_TYPE_USER_OPTIONS_CONFIGURED",
            "SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS",
            "SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS",
            "SIGNAL_TYPE_NO_ROOT_PASSWORD",
            "SIGNAL_TYPE_WEAK_ROOT_PASSWORD",
            "SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED",
            "SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED",
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
            "SIGNAL_TYPE_HOT_NODE",
            "SIGNAL_TYPE_NO_DELETION_PROTECTION",
            "SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY",
            "SIGNAL_TYPE_RESOURCE_SUSPENDED",
            "SIGNAL_TYPE_EXPENSIVE_COMMANDS",
            "SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED",
            "SIGNAL_TYPE_INEFFICIENT_QUERY",
            "SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD",
            "SIGNAL_TYPE_MEMORY_LIMIT",
            "SIGNAL_TYPE_MAX_SERVER_MEMORY",
            "SIGNAL_TYPE_LARGE_ROWS",
            "SIGNAL_TYPE_HIGH_WRITE_PRESSURE",
            "SIGNAL_TYPE_HIGH_READ_PRESSURE",
            "SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED",
            "SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED",
            "SIGNAL_TYPE_OUTDATED_MINOR_VERSION",
            "SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED",
            "SIGNAL_TYPE_REPLICATION_LAG",
            "SIGNAL_TYPE_OUTDATED_CLIENT",
            "SIGNAL_TYPE_DATABOOST_DISABLED",
            "SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES",
            "SIGNAL_TYPE_EXTENDED_SUPPORT",
            "SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE",
            "SIGNAL_TYPE_HIGH_MAINTENANCE_DOWNTIME_RISK",
            "SIGNAL_TYPE_LOW_CACHE_HIT_AND_MAINTENANCE_DOWNTIME",
        ]
    ]

@typing.type_check_only
class SubResource(typing_extensions.TypedDict, total=False):
    container: str
    fullResourceName: str
    product: Product
    resourceType: str

@typing.type_check_only
class Tag(typing_extensions.TypedDict, total=False):
    inherited: bool
    key: str
    source: str
    value: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TypedValue(typing_extensions.TypedDict, total=False):
    doubleValue: float
    int64Value: str

@typing.type_check_only
class UpcomingMaintenance(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
