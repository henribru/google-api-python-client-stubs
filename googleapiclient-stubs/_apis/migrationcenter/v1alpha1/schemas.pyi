import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddAssetsToGroupRequest(typing_extensions.TypedDict, total=False):
    allowExisting: bool
    assets: AssetList
    requestId: str

@typing.type_check_only
class AggregateAssetsValuesRequest(typing_extensions.TypedDict, total=False):
    aggregations: _list[Aggregation]
    filter: str
    showHidden: bool

@typing.type_check_only
class AggregateAssetsValuesResponse(typing_extensions.TypedDict, total=False):
    results: _list[AggregationResult]

@typing.type_check_only
class Aggregation(typing_extensions.TypedDict, total=False):
    count: AggregationCount
    field: str
    frequency: AggregationFrequency
    histogram: AggregationHistogram
    sum: AggregationSum

@typing.type_check_only
class AggregationCount(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AggregationFrequency(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AggregationHistogram(typing_extensions.TypedDict, total=False):
    lowerBounds: _list[float]

@typing.type_check_only
class AggregationResult(typing_extensions.TypedDict, total=False):
    count: AggregationResultCount
    field: str
    frequency: AggregationResultFrequency
    histogram: AggregationResultHistogram
    sum: AggregationResultSum

@typing.type_check_only
class AggregationResultCount(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class AggregationResultFrequency(typing_extensions.TypedDict, total=False):
    values: dict[str, typing.Any]

@typing.type_check_only
class AggregationResultHistogram(typing_extensions.TypedDict, total=False):
    buckets: _list[AggregationResultHistogramBucket]

@typing.type_check_only
class AggregationResultHistogramBucket(typing_extensions.TypedDict, total=False):
    count: str
    lowerBound: float
    upperBound: float

@typing.type_check_only
class AggregationResultSum(typing_extensions.TypedDict, total=False):
    value: float

@typing.type_check_only
class AggregationSum(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    assignedGroups: _list[str]
    attributes: dict[str, typing.Any]
    createTime: str
    databaseDeploymentDetails: DatabaseDeploymentDetails
    databaseDetails: DatabaseDetails
    hidden: bool
    hideReason: str
    hideTime: str
    insightList: InsightList
    labels: dict[str, typing.Any]
    name: str
    performanceData: AssetPerformanceData
    sources: _list[str]
    title: str
    updateTime: str
    virtualMachineDetails: VirtualMachineDetails

@typing.type_check_only
class AssetFrame(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    collectionType: typing_extensions.Literal[
        "SOURCE_TYPE_UNKNOWN",
        "SOURCE_TYPE_UPLOAD",
        "SOURCE_TYPE_GUEST_OS_SCAN",
        "SOURCE_TYPE_INVENTORY_SCAN",
        "SOURCE_TYPE_CUSTOM",
        "SOURCE_TYPE_DISCOVERY_CLIENT",
    ]
    databaseDeploymentDetails: DatabaseDeploymentDetails
    databaseDetails: DatabaseDetails
    labels: dict[str, typing.Any]
    performanceSamples: _list[PerformanceSample]
    reportTime: str
    traceToken: str
    virtualMachineDetails: VirtualMachineDetails

@typing.type_check_only
class AssetList(typing_extensions.TypedDict, total=False):
    assetIds: _list[str]

@typing.type_check_only
class AssetPerformanceData(typing_extensions.TypedDict, total=False):
    dailyResourceUsageAggregations: _list[DailyResourceUsageAggregation]

@typing.type_check_only
class AssetsExportJob(typing_extensions.TypedDict, total=False):
    condition: AssetsExportJobExportCondition
    createTime: str
    inventory: AssetsExportJobInventory
    labels: dict[str, typing.Any]
    name: str
    networkDependencies: AssetsExportJobNetworkDependencies
    performanceData: AssetsExportJobPerformanceData
    recentExecutions: _list[AssetsExportJobExecution]
    showHidden: bool
    signedUriDestination: SignedUriDestination
    updateTime: str

@typing.type_check_only
class AssetsExportJobExecution(typing_extensions.TypedDict, total=False):
    endTime: str
    executionId: str
    expireTime: str
    requestedAssetCount: int
    result: AssetsExportJobExecutionResult
    startTime: str

@typing.type_check_only
class AssetsExportJobExecutionResult(typing_extensions.TypedDict, total=False):
    error: Status
    outputFiles: OutputFileList
    signedUris: SignedUris

@typing.type_check_only
class AssetsExportJobExportCondition(typing_extensions.TypedDict, total=False):
    filter: str

@typing.type_check_only
class AssetsExportJobInventory(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AssetsExportJobNetworkDependencies(typing_extensions.TypedDict, total=False):
    maxDays: int

@typing.type_check_only
class AssetsExportJobPerformanceData(typing_extensions.TypedDict, total=False):
    maxDays: int

@typing.type_check_only
class AwsEc2PlatformDetails(typing_extensions.TypedDict, total=False):
    hyperthreading: typing_extensions.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str
    machineTypeLabel: str

@typing.type_check_only
class AzureVmPlatformDetails(typing_extensions.TypedDict, total=False):
    hyperthreading: typing_extensions.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str
    machineTypeLabel: str
    provisioningState: str

@typing.type_check_only
class BatchDeleteAssetsRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    cascadingRules: _list[CascadingRule]
    names: _list[str]

@typing.type_check_only
class BatchUpdateAssetsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateAssetRequest]

@typing.type_check_only
class BatchUpdateAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[Asset]

@typing.type_check_only
class BiosDetails(typing_extensions.TypedDict, total=False):
    biosManufacturer: str
    biosName: str
    biosReleaseDate: str
    biosVersion: str
    smbiosUuid: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CascadeLogicalDBsRule(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CascadingRule(typing_extensions.TypedDict, total=False):
    cascadeLogicalDbs: CascadeLogicalDBsRule

@typing.type_check_only
class CloudDatabaseMigrationTarget(typing_extensions.TypedDict, total=False):
    cloudSqlForMysqlShape: CloudSqlForMySqlShape
    cloudSqlForPostgresqlShape: CloudSqlForPostgreSqlShape
    cloudSqlShape: CloudSqlForSqlServerShape

@typing.type_check_only
class CloudSqlForMySqlShape(typing_extensions.TypedDict, total=False):
    backupStorageGb: int
    edition: typing_extensions.Literal[
        "CLOUD_SQL_EDITION_UNSPECIFIED",
        "CLOUD_SQL_EDITION_ENTERPRISE",
        "CLOUD_SQL_EDITION_ENTERPRISE_PLUS",
    ]
    egressGbPerMonth: str
    logicalCoreCount: int
    memoryMb: int
    storage: ComputeStorageDescriptor
    version: typing_extensions.Literal[
        "MY_SQL_VERSION_UNSPECIFIED",
        "MY_SQL_VERSION_5_6",
        "MY_SQL_VERSION_5_7",
        "MY_SQL_VERSION_8_0",
    ]
    zoneAvailability: typing_extensions.Literal[
        "CLOUD_SQL_ZONE_AVAILABILITY_UNSPECIFIED",
        "CLOUD_SQL_ZONE_AVAILABILITY_ZONAL",
        "CLOUD_SQL_ZONE_AVAILABILITY_REGIONAL",
    ]

@typing.type_check_only
class CloudSqlForPostgreSqlShape(typing_extensions.TypedDict, total=False):
    backupStorageGb: int
    edition: typing_extensions.Literal[
        "CLOUD_SQL_EDITION_UNSPECIFIED",
        "CLOUD_SQL_EDITION_ENTERPRISE",
        "CLOUD_SQL_EDITION_ENTERPRISE_PLUS",
    ]
    egressGbPerMonth: str
    logicalCoreCount: int
    memoryMb: int
    storage: ComputeStorageDescriptor
    version: typing_extensions.Literal[
        "POSTGRESQL_VERSION_UNSPECIFIED",
        "POSTGRESQL_VERSION_9_6",
        "POSTGRESQL_VERSION_10",
        "POSTGRESQL_VERSION_11",
        "POSTGRESQL_VERSION_12",
        "POSTGRESQL_VERSION_13",
        "POSTGRESQL_VERSION_14",
        "POSTGRESQL_VERSION_15",
    ]
    zoneAvailability: typing_extensions.Literal[
        "CLOUD_SQL_ZONE_AVAILABILITY_UNSPECIFIED",
        "CLOUD_SQL_ZONE_AVAILABILITY_ZONAL",
        "CLOUD_SQL_ZONE_AVAILABILITY_REGIONAL",
    ]

@typing.type_check_only
class CloudSqlForSqlServerShape(typing_extensions.TypedDict, total=False):
    backupStorageGb: int
    edition: typing_extensions.Literal[
        "CLOUD_SQL_EDITION_UNSPECIFIED",
        "CLOUD_SQL_EDITION_ENTERPRISE",
        "CLOUD_SQL_EDITION_ENTERPRISE_PLUS",
    ]
    egressGbPerMonth: str
    logicalCoreCount: int
    memoryMb: int
    smtEnabled: bool
    storage: ComputeStorageDescriptor
    version: typing_extensions.Literal[
        "SQL_SERVER_VERSION_UNSPECIFIED",
        "SQL_SERVER_VERSION_2017_EXPRESS",
        "SQL_SERVER_VERSION_2017_WEB",
        "SQL_SERVER_VERSION_2017_STANDARD",
        "SQL_SERVER_VERSION_2017_ENTERPRISE",
        "SQL_SERVER_VERSION_2019_EXPRESS",
        "SQL_SERVER_VERSION_2019_WEB",
        "SQL_SERVER_VERSION_2019_STANDARD",
        "SQL_SERVER_VERSION_2019_ENTERPRISE",
        "SQL_SERVER_VERSION_2022_EXPRESS",
        "SQL_SERVER_VERSION_2022_WEB",
        "SQL_SERVER_VERSION_2022_STANDARD",
        "SQL_SERVER_VERSION_2022_ENTERPRISE",
    ]
    zoneAvailability: typing_extensions.Literal[
        "CLOUD_SQL_ZONE_AVAILABILITY_UNSPECIFIED",
        "CLOUD_SQL_ZONE_AVAILABILITY_ZONAL",
        "CLOUD_SQL_ZONE_AVAILABILITY_REGIONAL",
    ]

@typing.type_check_only
class ComputeEngineMigrationTarget(typing_extensions.TypedDict, total=False):
    shape: ComputeEngineShapeDescriptor

@typing.type_check_only
class ComputeEnginePreferences(typing_extensions.TypedDict, total=False):
    licenseType: typing_extensions.Literal[
        "LICENSE_TYPE_UNSPECIFIED",
        "LICENSE_TYPE_DEFAULT",
        "LICENSE_TYPE_BRING_YOUR_OWN_LICENSE",
    ]
    machinePreferences: MachinePreferences
    multithreading: typing_extensions.Literal[
        "MULTITHREADING_UNSPECIFIED",
        "MULTITHREADING_DISABLED",
        "MULTITHREADING_ENABLED",
        "MULTITHREADING_DISABLED_WITH_COMPENSATION",
    ]
    osPricingPreferences: OperatingSystemPricingPreferences
    persistentDiskType: typing_extensions.Literal[
        "PERSISTENT_DISK_TYPE_UNSPECIFIED",
        "PERSISTENT_DISK_TYPE_STANDARD",
        "PERSISTENT_DISK_TYPE_BALANCED",
        "PERSISTENT_DISK_TYPE_SSD",
    ]

@typing.type_check_only
class ComputeEngineShapeDescriptor(typing_extensions.TypedDict, total=False):
    logicalCoreCount: int
    machineType: str
    memoryMb: int
    physicalCoreCount: int
    series: str
    smtEnabled: bool
    storage: _list[ComputeStorageDescriptor]

@typing.type_check_only
class ComputeEngineSoleTenantMigrationTarget(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ComputeStorageDescriptor(typing_extensions.TypedDict, total=False):
    sizeGb: int
    type: typing_extensions.Literal[
        "PERSISTENT_DISK_TYPE_UNSPECIFIED",
        "PERSISTENT_DISK_TYPE_STANDARD",
        "PERSISTENT_DISK_TYPE_BALANCED",
        "PERSISTENT_DISK_TYPE_SSD",
    ]

@typing.type_check_only
class CpuUsageSample(typing_extensions.TypedDict, total=False):
    utilizedPercentage: float

@typing.type_check_only
class CsvOutputFile(typing_extensions.TypedDict, total=False):
    columnsCount: int
    rowCount: int
    signedUri: SignedUri

@typing.type_check_only
class DailyResourceUsageAggregation(typing_extensions.TypedDict, total=False):
    cpu: DailyResourceUsageAggregationCPU
    date: Date
    disk: DailyResourceUsageAggregationDisk
    memory: DailyResourceUsageAggregationMemory
    network: DailyResourceUsageAggregationNetwork

@typing.type_check_only
class DailyResourceUsageAggregationCPU(typing_extensions.TypedDict, total=False):
    utilizationPercentage: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationDisk(typing_extensions.TypedDict, total=False):
    iops: DailyResourceUsageAggregationStats
    readIops: DailyResourceUsageAggregationStats
    writeIops: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationMemory(typing_extensions.TypedDict, total=False):
    utilizationPercentage: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationNetwork(typing_extensions.TypedDict, total=False):
    egressBps: DailyResourceUsageAggregationStats
    ingressBps: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationStats(typing_extensions.TypedDict, total=False):
    average: float
    median: float
    ninteyFifthPercentile: float
    peak: float

@typing.type_check_only
class DatabaseDeploymentDetails(typing_extensions.TypedDict, total=False):
    aggregatedStats: DatabaseDeploymentDetailsAggregatedStats
    edition: str
    generatedId: str
    manualUniqueId: str
    mysql: MysqlDatabaseDeployment
    postgresql: PostgreSqlDatabaseDeployment
    sqlServer: SqlServerDatabaseDeployment
    topology: DatabaseDeploymentTopology
    version: str

@typing.type_check_only
class DatabaseDeploymentDetailsAggregatedStats(
    typing_extensions.TypedDict, total=False
):
    databaseCount: int

@typing.type_check_only
class DatabaseDeploymentTopology(typing_extensions.TypedDict, total=False):
    coreCount: int
    coreLimit: int
    diskAllocatedBytes: str
    diskUsedBytes: str
    instances: _list[DatabaseInstance]
    memoryBytes: str
    memoryLimitBytes: str
    physicalCoreCount: int
    physicalCoreLimit: int

@typing.type_check_only
class DatabaseDetails(typing_extensions.TypedDict, total=False):
    allocatedStorageBytes: str
    databaseName: str
    parentDatabaseDeployment: DatabaseDetailsParentDatabaseDeployment
    schemas: _list[DatabaseSchema]

@typing.type_check_only
class DatabaseDetailsParentDatabaseDeployment(typing_extensions.TypedDict, total=False):
    generatedId: str
    manualUniqueId: str

@typing.type_check_only
class DatabaseInstance(typing_extensions.TypedDict, total=False):
    instanceName: str
    network: DatabaseInstanceNetwork
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED", "PRIMARY", "SECONDARY", "ARBITER"
    ]

@typing.type_check_only
class DatabaseInstanceNetwork(typing_extensions.TypedDict, total=False):
    hostNames: _list[str]
    ipAddresses: _list[str]
    primaryMacAddress: str

@typing.type_check_only
class DatabaseObjects(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED",
        "TABLE",
        "INDEX",
        "CONSTRAINTS",
        "VIEWS",
        "SOURCE_CODE",
        "OTHER",
    ]
    count: str

@typing.type_check_only
class DatabasePreferences(typing_extensions.TypedDict, total=False):
    mssqlToCloudSqlForSqlServerPreferences: DatabasePreferencesCloudSqlSqlServer
    mysqlToCloudSqlForMysqlPreferences: DatabasePreferencesCloudSqlMySql
    postgresqlToCloudSqlForPostgresqlPreferences: DatabasePreferencesCloudSqlPostgreSql

@typing.type_check_only
class DatabasePreferencesCloudSqlCommon(typing_extensions.TypedDict, total=False):
    backup: DatabasePreferencesCloudSqlCommonBackup
    commitmentPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "COMMITMENT_PLAN_NONE",
        "COMMITMENT_PLAN_ONE_YEAR",
        "COMMITMENT_PLAN_THREE_YEARS",
        "COMMITMENT_PLAN_FLEXIBLE_ONE_YEAR",
        "COMMITMENT_PLAN_FLEXIBLE_THREE_YEARS",
    ]
    edition: typing_extensions.Literal[
        "CLOUD_SQL_EDITION_UNSPECIFIED",
        "CLOUD_SQL_EDITION_ENTERPRISE",
        "CLOUD_SQL_EDITION_ENTERPRISE_PLUS",
    ]
    persistentDiskType: typing_extensions.Literal[
        "PERSISTENT_DISK_TYPE_UNSPECIFIED",
        "PERSISTENT_DISK_TYPE_STANDARD",
        "PERSISTENT_DISK_TYPE_BALANCED",
        "PERSISTENT_DISK_TYPE_SSD",
    ]
    sizingOptimizationStrategy: typing_extensions.Literal[
        "SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED",
        "SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE",
        "SIZING_OPTIMIZATION_STRATEGY_MODERATE",
        "SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE",
        "SIZING_OPTIMIZATION_STRATEGY_CUSTOM",
    ]
    zoneAvailability: typing_extensions.Literal[
        "CLOUD_SQL_ZONE_AVAILABILITY_UNSPECIFIED",
        "CLOUD_SQL_ZONE_AVAILABILITY_ZONAL",
        "CLOUD_SQL_ZONE_AVAILABILITY_REGIONAL",
    ]

@typing.type_check_only
class DatabasePreferencesCloudSqlCommonBackup(typing_extensions.TypedDict, total=False):
    backupMode: typing_extensions.Literal[
        "BACKUP_MODE_UNSPECIFIED", "BACKUP_MODE_DISABLED", "BACKUP_MODE_ENABLED"
    ]

@typing.type_check_only
class DatabasePreferencesCloudSqlMySql(typing_extensions.TypedDict, total=False):
    common: DatabasePreferencesCloudSqlCommon

@typing.type_check_only
class DatabasePreferencesCloudSqlPostgreSql(typing_extensions.TypedDict, total=False):
    common: DatabasePreferencesCloudSqlCommon

@typing.type_check_only
class DatabasePreferencesCloudSqlSqlServer(typing_extensions.TypedDict, total=False):
    common: DatabasePreferencesCloudSqlCommon
    multithreading: typing_extensions.Literal[
        "MULTITHREADING_UNSPECIFIED",
        "MULTITHREADING_DISABLED",
        "MULTITHREADING_ENABLED",
        "MULTITHREADING_DISABLED_WITH_COMPENSATION",
    ]
    versionType: typing_extensions.Literal[
        "VERSION_TYPE_UNSPECIFIED",
        "VERSION_TYPE_AUTO",
        "VERSION_TYPE_EXPRESS",
        "VERSION_TYPE_WEB",
        "VERSION_TYPE_STANDARD",
        "VERSION_TYPE_ENTERPRISE",
    ]

@typing.type_check_only
class DatabaseSchema(typing_extensions.TypedDict, total=False):
    mysql: MySqlSchemaDetails
    objects: _list[DatabaseObjects]
    postgresql: PostgreSqlSchemaDetails
    schemaName: str
    sqlServer: SqlServerSchemaDetails
    tablesSizeBytes: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateTime(typing_extensions.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: TimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class DetectedSoftware(typing_extensions.TypedDict, total=False):
    softwareFamily: str
    softwareName: str

@typing.type_check_only
class DiscoveryClient(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    errors: _list[Status]
    expireTime: str
    heartbeatTime: str
    labels: dict[str, typing.Any]
    name: str
    serviceAccount: str
    signalsEndpoint: str
    source: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "OFFLINE", "DEGRADED", "EXPIRED"
    ]
    ttl: str
    updateTime: str
    version: str

@typing.type_check_only
class DiskEntry(typing_extensions.TypedDict, total=False):
    diskLabel: str
    diskLabelType: str
    hwAddress: str
    interfaceType: str
    partitions: DiskPartitionList
    status: str
    totalCapacityBytes: str
    totalFreeBytes: str
    vmwareConfig: VmwareDiskConfig

@typing.type_check_only
class DiskEntryList(typing_extensions.TypedDict, total=False):
    entries: _list[DiskEntry]

@typing.type_check_only
class DiskPartition(typing_extensions.TypedDict, total=False):
    capacityBytes: str
    fileSystem: str
    freeBytes: str
    mountPoint: str
    subPartitions: DiskPartitionList
    type: str
    uuid: str

@typing.type_check_only
class DiskPartitionList(typing_extensions.TypedDict, total=False):
    entries: _list[DiskPartition]

@typing.type_check_only
class DiskUsageSample(typing_extensions.TypedDict, total=False):
    averageIops: float
    averageReadIops: float
    averageWriteIops: float

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ErrorFrame(typing_extensions.TypedDict, total=False):
    ingestionTime: str
    name: str
    originalFrame: AssetFrame
    violations: _list[FrameViolationEntry]

@typing.type_check_only
class ExecutionReport(typing_extensions.TypedDict, total=False):
    executionErrors: ValidationReport
    framesReported: int
    jobErrors: _list[ImportError]
    totalRowsCount: int

@typing.type_check_only
class FileValidationReport(typing_extensions.TypedDict, total=False):
    fileErrors: _list[ImportError]
    fileName: str
    partialReport: bool
    rowErrors: _list[ImportRowError]

@typing.type_check_only
class FitDescriptor(typing_extensions.TypedDict, total=False):
    fitLevel: typing_extensions.Literal[
        "FIT_LEVEL_UNSPECIFIED", "FIT", "NO_FIT", "REQUIRES_EFFORT"
    ]

@typing.type_check_only
class FrameViolationEntry(typing_extensions.TypedDict, total=False):
    field: str
    violation: str

@typing.type_check_only
class Frames(typing_extensions.TypedDict, total=False):
    framesData: _list[AssetFrame]

@typing.type_check_only
class FstabEntry(typing_extensions.TypedDict, total=False):
    file: str
    freq: int
    mntops: str
    passno: int
    spec: str
    vfstype: str

@typing.type_check_only
class FstabEntryList(typing_extensions.TypedDict, total=False):
    entries: _list[FstabEntry]

@typing.type_check_only
class GCSPayloadInfo(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "IMPORT_JOB_FORMAT_UNSPECIFIED",
        "IMPORT_JOB_FORMAT_CMDB",
        "IMPORT_JOB_FORMAT_RVTOOLS_XLSX",
        "IMPORT_JOB_FORMAT_RVTOOLS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV",
        "IMPORT_JOB_FORMAT_MANUAL_CSV",
        "IMPORT_JOB_FORMAT_DATABASE_ZIP",
    ]
    path: str

@typing.type_check_only
class GenericInsight(typing_extensions.TypedDict, total=False):
    additionalInformation: _list[str]
    defaultMessage: str
    messageId: str

@typing.type_check_only
class GenericPlatformDetails(typing_extensions.TypedDict, total=False):
    hyperthreading: typing_extensions.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str

@typing.type_check_only
class GoogleKubernetesEngineMigrationTarget(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GuestConfigDetails(typing_extensions.TypedDict, total=False):
    fstab: FstabEntryList
    hosts: HostsEntryList
    issue: str
    nfsExports: NfsExportList
    selinux: Selinux

@typing.type_check_only
class GuestInstalledApplication(typing_extensions.TypedDict, total=False):
    licenses: _list[str]
    name: str
    path: str
    time: str
    vendor: str
    version: str

@typing.type_check_only
class GuestInstalledApplicationList(typing_extensions.TypedDict, total=False):
    entries: _list[GuestInstalledApplication]

@typing.type_check_only
class GuestOsDetails(typing_extensions.TypedDict, total=False):
    config: GuestConfigDetails
    runtime: GuestRuntimeDetails

@typing.type_check_only
class GuestRuntimeDetails(typing_extensions.TypedDict, total=False):
    domain: str
    installedApps: GuestInstalledApplicationList
    lastUptime: Date
    machineName: str
    networkInfo: RuntimeNetworkInfo
    openFileList: OpenFileList
    processes: RunningProcessList
    services: RunningServiceList

@typing.type_check_only
class HostsEntry(typing_extensions.TypedDict, total=False):
    hostNames: _list[str]
    ip: str

@typing.type_check_only
class HostsEntryList(typing_extensions.TypedDict, total=False):
    entries: _list[HostsEntry]

@typing.type_check_only
class ImportDataFile(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    format: typing_extensions.Literal[
        "IMPORT_JOB_FORMAT_UNSPECIFIED",
        "IMPORT_JOB_FORMAT_CMDB",
        "IMPORT_JOB_FORMAT_RVTOOLS_XLSX",
        "IMPORT_JOB_FORMAT_RVTOOLS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV",
        "IMPORT_JOB_FORMAT_MANUAL_CSV",
        "IMPORT_JOB_FORMAT_DATABASE_ZIP",
    ]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE"]
    uploadFileInfo: UploadFileInfo

@typing.type_check_only
class ImportError(typing_extensions.TypedDict, total=False):
    errorDetails: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class ImportJob(typing_extensions.TypedDict, total=False):
    assetSource: str
    completeTime: str
    createTime: str
    displayName: str
    executionReport: ExecutionReport
    gcsPayload: GCSPayloadInfo
    inlinePayload: InlinePayloadInfo
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "IMPORT_JOB_STATE_UNSPECIFIED",
        "IMPORT_JOB_STATE_PENDING",
        "IMPORT_JOB_STATE_RUNNING",
        "IMPORT_JOB_STATE_COMPLETED",
        "IMPORT_JOB_STATE_FAILED",
        "IMPORT_JOB_STATE_VALIDATING",
        "IMPORT_JOB_STATE_FAILED_VALIDATION",
        "IMPORT_JOB_STATE_READY",
    ]
    updateTime: str
    validationReport: ValidationReport

@typing.type_check_only
class ImportRowError(typing_extensions.TypedDict, total=False):
    archiveError: ImportRowErrorArchiveErrorDetails
    assetTitle: str
    csvError: ImportRowErrorCsvErrorDetails
    errors: _list[ImportError]
    rowNumber: int
    vmName: str
    vmUuid: str
    xlsxError: ImportRowErrorXlsxErrorDetails

@typing.type_check_only
class ImportRowErrorArchiveErrorDetails(typing_extensions.TypedDict, total=False):
    csvError: ImportRowErrorCsvErrorDetails
    filePath: str

@typing.type_check_only
class ImportRowErrorCsvErrorDetails(typing_extensions.TypedDict, total=False):
    rowNumber: int

@typing.type_check_only
class ImportRowErrorXlsxErrorDetails(typing_extensions.TypedDict, total=False):
    rowNumber: int
    sheet: str

@typing.type_check_only
class InlinePayloadInfo(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "IMPORT_JOB_FORMAT_UNSPECIFIED",
        "IMPORT_JOB_FORMAT_CMDB",
        "IMPORT_JOB_FORMAT_RVTOOLS_XLSX",
        "IMPORT_JOB_FORMAT_RVTOOLS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV",
        "IMPORT_JOB_FORMAT_MANUAL_CSV",
        "IMPORT_JOB_FORMAT_DATABASE_ZIP",
    ]
    payload: _list[PayloadFile]

@typing.type_check_only
class Insight(typing_extensions.TypedDict, total=False):
    genericInsight: GenericInsight
    migrationInsight: MigrationInsight
    softwareInsight: SoftwareInsight

@typing.type_check_only
class InsightList(typing_extensions.TypedDict, total=False):
    insights: _list[Insight]
    updateTime: str

@typing.type_check_only
class Issue(typing_extensions.TypedDict, total=False):
    compatibilityIssue: IssueCompatibilityIssue
    description: str
    issueCode: str

@typing.type_check_only
class IssueCompatibilityIssue(typing_extensions.TypedDict, total=False):
    associatedObject: str
    associatedObjectType: typing_extensions.Literal[
        "OBJECT_TYPE_UNSPECIFIED", "DATABASE_DEPLOYMENT", "DATABASE", "SCHEMA"
    ]
    associatedValue: str
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "DATABASE_FLAG", "DATABASE_FEATURE"
    ]

@typing.type_check_only
class ListAssetsExportJobsResponse(typing_extensions.TypedDict, total=False):
    assetsExportJobs: _list[AssetsExportJob]
    nextPageToken: str

@typing.type_check_only
class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[Asset]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveryClientsResponse(typing_extensions.TypedDict, total=False):
    discoveryClients: _list[DiscoveryClient]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListErrorFramesResponse(typing_extensions.TypedDict, total=False):
    errorFrames: _list[ErrorFrame]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImportDataFilesResponse(typing_extensions.TypedDict, total=False):
    importDataFiles: _list[ImportDataFile]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImportJobsResponse(typing_extensions.TypedDict, total=False):
    importJobs: _list[ImportJob]
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
class ListPreferenceSetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    preferenceSets: _list[PreferenceSet]
    unreachable: _list[str]

@typing.type_check_only
class ListRelationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    relations: _list[Relation]

@typing.type_check_only
class ListReportConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reportConfigs: _list[ReportConfig]
    unreachable: _list[str]

@typing.type_check_only
class ListReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]
    unreachable: _list[str]

@typing.type_check_only
class ListSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MachinePreferences(typing_extensions.TypedDict, total=False):
    allowedMachineSeries: _list[MachineSeries]

@typing.type_check_only
class MachineSeries(typing_extensions.TypedDict, total=False):
    code: str

@typing.type_check_only
class MemoryUsageSample(typing_extensions.TypedDict, total=False):
    utilizedPercentage: float

@typing.type_check_only
class MigrationInsight(typing_extensions.TypedDict, total=False):
    cloudDatabaseTarget: CloudDatabaseMigrationTarget
    computeEngineSoleTenantTarget: ComputeEngineSoleTenantMigrationTarget
    computeEngineTarget: ComputeEngineMigrationTarget
    fit: FitDescriptor
    gkeTarget: GoogleKubernetesEngineMigrationTarget
    issues: _list[Issue]
    vmwareEngineTarget: VmwareEngineMigrationTarget

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MySqlPlugin(typing_extensions.TypedDict, total=False):
    enabled: bool
    plugin: str
    version: str

@typing.type_check_only
class MySqlProperty(typing_extensions.TypedDict, total=False):
    enabled: bool
    numericValue: str
    property: str

@typing.type_check_only
class MySqlSchemaDetails(typing_extensions.TypedDict, total=False):
    storageEngines: _list[MySqlStorageEngineDetails]

@typing.type_check_only
class MySqlStorageEngineDetails(typing_extensions.TypedDict, total=False):
    encryptedTableCount: int
    engine: typing_extensions.Literal[
        "ENGINE_UNSPECIFIED",
        "INNODB",
        "MYISAM",
        "MEMORY",
        "CSV",
        "ARCHIVE",
        "BLACKHOLE",
        "NDB",
        "MERGE",
        "FEDERATED",
        "EXAMPLE",
        "OTHER",
    ]
    tableCount: int

@typing.type_check_only
class MySqlVariable(typing_extensions.TypedDict, total=False):
    category: str
    value: str
    variable: str

@typing.type_check_only
class MysqlDatabaseDeployment(typing_extensions.TypedDict, total=False):
    plugins: _list[MySqlPlugin]
    properties: _list[MySqlProperty]
    resourceGroupsCount: int
    variables: _list[MySqlVariable]

@typing.type_check_only
class NetworkAdapterDetails(typing_extensions.TypedDict, total=False):
    adapterType: str
    addresses: NetworkAddressList
    macAddress: str

@typing.type_check_only
class NetworkAdapterList(typing_extensions.TypedDict, total=False):
    networkAdapters: _list[NetworkAdapterDetails]

@typing.type_check_only
class NetworkAddress(typing_extensions.TypedDict, total=False):
    assignment: typing_extensions.Literal[
        "ADDRESS_ASSIGNMENT_UNSPECIFIED",
        "ADDRESS_ASSIGNMENT_STATIC",
        "ADDRESS_ASSIGNMENT_DHCP",
    ]
    bcast: str
    fqdn: str
    ipAddress: str
    subnetMask: str

@typing.type_check_only
class NetworkAddressList(typing_extensions.TypedDict, total=False):
    addresses: _list[NetworkAddress]

@typing.type_check_only
class NetworkConnection(typing_extensions.TypedDict, total=False):
    localIpAddress: str
    localPort: int
    pid: str
    processName: str
    protocol: str
    remoteIpAddress: str
    remotePort: int
    state: str

@typing.type_check_only
class NetworkConnectionList(typing_extensions.TypedDict, total=False):
    entries: _list[NetworkConnection]

@typing.type_check_only
class NetworkUsageSample(typing_extensions.TypedDict, total=False):
    averageEgressBps: float
    averageIngressBps: float

@typing.type_check_only
class NfsExport(typing_extensions.TypedDict, total=False):
    exportDirectory: str
    hosts: _list[str]

@typing.type_check_only
class NfsExportList(typing_extensions.TypedDict, total=False):
    entries: _list[NfsExport]

@typing.type_check_only
class OpenFileDetails(typing_extensions.TypedDict, total=False):
    command: str
    filePath: str
    fileType: str
    user: str

@typing.type_check_only
class OpenFileList(typing_extensions.TypedDict, total=False):
    entries: _list[OpenFileDetails]

@typing.type_check_only
class OperatingSystemPricingPreferences(typing_extensions.TypedDict, total=False):
    rhel: OperatingSystemPricingPreferencesOperatingSystemPricing
    sles: OperatingSystemPricingPreferencesOperatingSystemPricing
    slesForSap: OperatingSystemPricingPreferencesOperatingSystemPricing
    windows: OperatingSystemPricingPreferencesOperatingSystemPricing

@typing.type_check_only
class OperatingSystemPricingPreferencesOperatingSystemPricing(
    typing_extensions.TypedDict, total=False
):
    commitmentPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "COMMITMENT_PLAN_ON_DEMAND",
        "COMMITMENT_PLAN_1_YEAR",
        "COMMITMENT_PLAN_3_YEAR",
    ]
    licenseType: typing_extensions.Literal[
        "LICENSE_TYPE_UNSPECIFIED",
        "LICENSE_TYPE_DEFAULT",
        "LICENSE_TYPE_BRING_YOUR_OWN_LICENSE",
    ]

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
class OutputFile(typing_extensions.TypedDict, total=False):
    csvOutputFile: CsvOutputFile
    fileSizeBytes: int
    xlsxOutputFile: XlsxOutputFile

@typing.type_check_only
class OutputFileList(typing_extensions.TypedDict, total=False):
    entries: _list[OutputFile]

@typing.type_check_only
class PayloadFile(typing_extensions.TypedDict, total=False):
    data: str
    name: str

@typing.type_check_only
class PerformanceSample(typing_extensions.TypedDict, total=False):
    cpu: CpuUsageSample
    disk: DiskUsageSample
    memory: MemoryUsageSample
    network: NetworkUsageSample
    sampleTime: str

@typing.type_check_only
class PhysicalPlatformDetails(typing_extensions.TypedDict, total=False):
    hyperthreading: typing_extensions.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str

@typing.type_check_only
class PlatformDetails(typing_extensions.TypedDict, total=False):
    awsEc2Details: AwsEc2PlatformDetails
    azureVmDetails: AzureVmPlatformDetails
    genericDetails: GenericPlatformDetails
    physicalDetails: PhysicalPlatformDetails
    vmwareDetails: VmwarePlatformDetails

@typing.type_check_only
class PostgreSqlDatabaseDeployment(typing_extensions.TypedDict, total=False):
    properties: _list[PostgreSqlProperty]
    settings: _list[PostgreSqlSetting]

@typing.type_check_only
class PostgreSqlExtension(typing_extensions.TypedDict, total=False):
    extension: str
    version: str

@typing.type_check_only
class PostgreSqlProperty(typing_extensions.TypedDict, total=False):
    enabled: bool
    numericValue: str
    property: str

@typing.type_check_only
class PostgreSqlSchemaDetails(typing_extensions.TypedDict, total=False):
    foreignTablesCount: int
    postgresqlExtensions: _list[PostgreSqlExtension]

@typing.type_check_only
class PostgreSqlSetting(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    realValue: float
    setting: str
    source: str
    stringValue: str
    unit: str

@typing.type_check_only
class PreferenceSet(typing_extensions.TypedDict, total=False):
    createTime: str
    databasePreferences: DatabasePreferences
    description: str
    displayName: str
    name: str
    regionPreferences: RegionPreferences
    updateTime: str
    virtualMachinePreferences: VirtualMachinePreferences

@typing.type_check_only
class RegionPreferences(typing_extensions.TypedDict, total=False):
    preferredRegions: _list[str]

@typing.type_check_only
class Relation(typing_extensions.TypedDict, total=False):
    createTime: str
    dstAsset: str
    name: str
    srcAsset: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "LOGICAL_DATABASE", "DATABASE_DEPLOYMENT_HOSTING_SERVER"
    ]

@typing.type_check_only
class RemoveAssetsFromGroupRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    assets: AssetList
    requestId: str

@typing.type_check_only
class Report(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "SUCCEEDED", "FAILED"
    ]
    summary: ReportSummary
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TOTAL_COST_OF_OWNERSHIP"]
    updateTime: str

@typing.type_check_only
class ReportAssetFramesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReportConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    groupPreferencesetAssignments: _list[ReportConfigGroupPreferenceSetAssignment]
    name: str
    updateTime: str

@typing.type_check_only
class ReportConfigGroupPreferenceSetAssignment(
    typing_extensions.TypedDict, total=False
):
    group: str
    preferenceSet: str

@typing.type_check_only
class ReportSummary(typing_extensions.TypedDict, total=False):
    allAssetsStats: ReportSummaryAssetAggregateStats
    databaseStats: ReportSummaryAssetAggregateStats
    groupFindings: _list[ReportSummaryGroupFinding]
    virtualMachineStats: ReportSummaryAssetAggregateStats

@typing.type_check_only
class ReportSummaryAssetAggregateStats(typing_extensions.TypedDict, total=False):
    assetAge: ReportSummaryChartData
    coreCountHistogram: ReportSummaryHistogramChartData
    databaseTypes: ReportSummaryChartData
    memoryBytesHistogram: ReportSummaryHistogramChartData
    memoryUtilization: ReportSummaryChartData
    memoryUtilizationChart: ReportSummaryUtilizationChartData
    operatingSystem: ReportSummaryChartData
    storageBytesHistogram: ReportSummaryHistogramChartData
    storageUtilization: ReportSummaryChartData
    storageUtilizationChart: ReportSummaryUtilizationChartData
    totalAssets: str
    totalCores: str
    totalMemoryBytes: str
    totalStorageBytes: str

@typing.type_check_only
class ReportSummaryChartData(typing_extensions.TypedDict, total=False):
    dataPoints: _list[ReportSummaryChartDataDataPoint]

@typing.type_check_only
class ReportSummaryChartDataDataPoint(typing_extensions.TypedDict, total=False):
    label: str
    value: float

@typing.type_check_only
class ReportSummaryDatabaseFinding(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    totalAssets: str

@typing.type_check_only
class ReportSummaryGroupFinding(typing_extensions.TypedDict, total=False):
    assetAggregateStats: ReportSummaryAssetAggregateStats
    assetType: typing_extensions.Literal[
        "ASSET_TYPE_UNSPECIFIED", "VIRTUAL_MACHINE", "DATABASE"
    ]
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED", "SQL_SERVER", "MYSQL", "POSTGRES"
    ]
    description: str
    displayName: str
    group: str
    overlappingAssetCount: str
    preferenceSetFindings: _list[ReportSummaryGroupPreferenceSetFinding]

@typing.type_check_only
class ReportSummaryGroupPreferenceSetFinding(typing_extensions.TypedDict, total=False):
    databaseFinding: ReportSummaryDatabaseFinding
    description: str
    displayName: str
    machineFinding: ReportSummaryMachineFinding
    machinePreferences: VirtualMachinePreferences
    monthlyCostCompute: Money
    monthlyCostDatabaseBackup: Money
    monthlyCostDatabaseLicensing: Money
    monthlyCostGcveProtected: Money
    monthlyCostNetworkEgress: Money
    monthlyCostOsLicense: Money
    monthlyCostOther: Money
    monthlyCostPortableVmwareLicense: Money
    monthlyCostStorage: Money
    monthlyCostTotal: Money
    preferenceSet: PreferenceSet
    preferredRegion: str
    pricingTrack: str
    soleTenantFinding: ReportSummarySoleTenantFinding
    topPriority: str
    vmwareEngineFinding: ReportSummaryVMWareEngineFinding

@typing.type_check_only
class ReportSummaryHistogramChartData(typing_extensions.TypedDict, total=False):
    buckets: _list[ReportSummaryHistogramChartDataBucket]

@typing.type_check_only
class ReportSummaryHistogramChartDataBucket(typing_extensions.TypedDict, total=False):
    count: str
    lowerBound: str
    upperBound: str

@typing.type_check_only
class ReportSummaryMachineFinding(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    allocatedDiskTypes: _list[
        typing_extensions.Literal[
            "PERSISTENT_DISK_TYPE_UNSPECIFIED",
            "PERSISTENT_DISK_TYPE_STANDARD",
            "PERSISTENT_DISK_TYPE_BALANCED",
            "PERSISTENT_DISK_TYPE_SSD",
        ]
    ]
    allocatedRegions: _list[str]
    machineSeriesAllocations: _list[ReportSummaryMachineSeriesAllocation]

@typing.type_check_only
class ReportSummaryMachineSeriesAllocation(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    machineSeries: MachineSeries

@typing.type_check_only
class ReportSummarySoleTenantFinding(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    allocatedRegions: _list[str]
    nodeAllocations: _list[ReportSummarySoleTenantNodeAllocation]

@typing.type_check_only
class ReportSummarySoleTenantNodeAllocation(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    node: SoleTenantNodeType
    nodeCount: str

@typing.type_check_only
class ReportSummaryUtilizationChartData(typing_extensions.TypedDict, total=False):
    free: str
    used: str

@typing.type_check_only
class ReportSummaryVMWareEngineFinding(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    allocatedRegions: _list[str]
    nodeAllocations: _list[ReportSummaryVMWareNodeAllocation]

@typing.type_check_only
class ReportSummaryVMWareNode(typing_extensions.TypedDict, total=False):
    code: str

@typing.type_check_only
class ReportSummaryVMWareNodeAllocation(typing_extensions.TypedDict, total=False):
    allocatedAssetCount: str
    nodeCount: str
    vmwareNode: ReportSummaryVMWareNode

@typing.type_check_only
class RunAssetsExportJobRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RunAssetsExportJobResponse(typing_extensions.TypedDict, total=False):
    assetsExportJobExecution: AssetsExportJobExecution

@typing.type_check_only
class RunImportJobRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RunningProcess(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    cmdline: str
    exePath: str
    pid: str
    user: str

@typing.type_check_only
class RunningProcessList(typing_extensions.TypedDict, total=False):
    processes: _list[RunningProcess]

@typing.type_check_only
class RunningService(typing_extensions.TypedDict, total=False):
    cmdline: str
    exePath: str
    name: str
    pid: str
    startMode: str
    state: str
    status: str

@typing.type_check_only
class RunningServiceList(typing_extensions.TypedDict, total=False):
    services: _list[RunningService]

@typing.type_check_only
class RuntimeNetworkInfo(typing_extensions.TypedDict, total=False):
    connections: NetworkConnectionList
    netstat: str
    netstatTime: DateTime

@typing.type_check_only
class Selinux(typing_extensions.TypedDict, total=False):
    enabled: bool
    mode: str

@typing.type_check_only
class SendDiscoveryClientHeartbeatRequest(typing_extensions.TypedDict, total=False):
    errors: _list[Status]
    version: str

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    customerConsentForGoogleSalesToAccessMigrationCenter: bool
    disableCloudLogging: bool
    name: str
    preferenceSet: str

@typing.type_check_only
class SignedUri(typing_extensions.TypedDict, total=False):
    file: str
    uri: str

@typing.type_check_only
class SignedUriDestination(typing_extensions.TypedDict, total=False):
    fileFormat: typing_extensions.Literal["FILE_FORMAT_UNSPECIFIED", "CSV", "XLSX"]

@typing.type_check_only
class SignedUris(typing_extensions.TypedDict, total=False):
    signedUris: _list[SignedUri]

@typing.type_check_only
class SoftwareInsight(typing_extensions.TypedDict, total=False):
    detectedSoftware: DetectedSoftware

@typing.type_check_only
class SoleTenancyPreferences(typing_extensions.TypedDict, total=False):
    commitmentPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "ON_DEMAND",
        "COMMITMENT_1_YEAR",
        "COMMITMENT_3_YEAR",
        "COMMITMENT_FLEXIBLE_1_YEAR",
        "COMMITMENT_FLEXIBLE_3_YEAR",
    ]
    cpuOvercommitRatio: float
    hostMaintenancePolicy: typing_extensions.Literal[
        "HOST_MAINTENANCE_POLICY_UNSPECIFIED",
        "HOST_MAINTENANCE_POLICY_DEFAULT",
        "HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE",
        "HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP",
    ]
    nodeTypes: _list[SoleTenantNodeType]
    osPricingPreferences: OperatingSystemPricingPreferences

@typing.type_check_only
class SoleTenantNodeType(typing_extensions.TypedDict, total=False):
    nodeName: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    errorFrameCount: int
    isManaged: bool
    name: str
    pendingFrameCount: int
    priority: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "DELETING", "INVALID"
    ]
    type: typing_extensions.Literal[
        "SOURCE_TYPE_UNKNOWN",
        "SOURCE_TYPE_UPLOAD",
        "SOURCE_TYPE_GUEST_OS_SCAN",
        "SOURCE_TYPE_INVENTORY_SCAN",
        "SOURCE_TYPE_CUSTOM",
        "SOURCE_TYPE_DISCOVERY_CLIENT",
    ]
    updateTime: str

@typing.type_check_only
class SqlServerDatabaseDeployment(typing_extensions.TypedDict, total=False):
    features: _list[SqlServerFeature]
    serverFlags: _list[SqlServerServerFlag]
    traceFlags: _list[SqlServerTraceFlag]

@typing.type_check_only
class SqlServerFeature(typing_extensions.TypedDict, total=False):
    enabled: bool
    featureName: str

@typing.type_check_only
class SqlServerSchemaDetails(typing_extensions.TypedDict, total=False):
    clrObjectCount: int

@typing.type_check_only
class SqlServerServerFlag(typing_extensions.TypedDict, total=False):
    serverFlagName: str
    value: str
    valueInUse: str

@typing.type_check_only
class SqlServerTraceFlag(typing_extensions.TypedDict, total=False):
    scope: typing_extensions.Literal["SCOPE_UNSPECIFIED", "OFF", "GLOBAL", "SESSION"]
    traceFlagName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class UpdateAssetRequest(typing_extensions.TypedDict, total=False):
    asset: Asset
    requestId: str
    updateMask: str

@typing.type_check_only
class UploadFileInfo(typing_extensions.TypedDict, total=False):
    headers: dict[str, typing.Any]
    signedUri: str
    uriExpirationTime: str

@typing.type_check_only
class VMwareEngineMachinePreferences(typing_extensions.TypedDict, total=False):
    allowedMachineSeries: _list[MachineSeries]
    protectedNodes: typing_extensions.Literal[
        "PROTECTED_NODES_UNSPECIFIED",
        "PROTECTED_NODES_ENABLED",
        "PROTECTED_NODES_DISABLED",
    ]
    storageOnlyNodes: typing_extensions.Literal[
        "STORAGE_ONLY_NODES_UNSPECIFIED",
        "STORAGE_ONLY_NODES_ENABLED",
        "STORAGE_ONLY_NODES_DISABLED",
    ]

@typing.type_check_only
class ValidateImportJobRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ValidationReport(typing_extensions.TypedDict, total=False):
    fileValidations: _list[FileValidationReport]
    jobErrors: _list[ImportError]

@typing.type_check_only
class VirtualMachineArchitectureDetails(typing_extensions.TypedDict, total=False):
    bios: BiosDetails
    cpuArchitecture: str
    cpuManufacturer: str
    cpuName: str
    cpuSocketCount: int
    cpuThreadCount: int
    firmware: str
    hyperthreading: typing_extensions.Literal[
        "HYPER_THREADING_UNSPECIFIED",
        "HYPER_THREADING_DISABLED",
        "HYPER_THREADING_ENABLED",
    ]
    vendor: str

@typing.type_check_only
class VirtualMachineDetails(typing_extensions.TypedDict, total=False):
    coreCount: int
    createTime: str
    guestOs: GuestOsDetails
    memoryMb: int
    osFamily: typing_extensions.Literal[
        "OS_FAMILY_UNKNOWN", "OS_FAMILY_WINDOWS", "OS_FAMILY_LINUX", "OS_FAMILY_UNIX"
    ]
    osName: str
    osVersion: str
    platform: PlatformDetails
    powerState: str
    vcenterFolder: str
    vcenterUrl: str
    vcenterVmId: str
    vmArchitecture: VirtualMachineArchitectureDetails
    vmDisks: VirtualMachineDiskDetails
    vmName: str
    vmNetwork: VirtualMachineNetworkDetails
    vmUuid: str

@typing.type_check_only
class VirtualMachineDiskDetails(typing_extensions.TypedDict, total=False):
    disks: DiskEntryList
    hddTotalCapacityBytes: str
    hddTotalFreeBytes: str
    lsblkJson: str

@typing.type_check_only
class VirtualMachineNetworkDetails(typing_extensions.TypedDict, total=False):
    defaultGw: str
    networkAdapters: NetworkAdapterList
    primaryIpAddress: str
    primaryMacAddress: str
    publicIpAddress: str

@typing.type_check_only
class VirtualMachinePreferences(typing_extensions.TypedDict, total=False):
    commitmentPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "COMMITMENT_PLAN_NONE",
        "COMMITMENT_PLAN_ONE_YEAR",
        "COMMITMENT_PLAN_THREE_YEARS",
        "COMMITMENT_PLAN_FLEXIBLE_ONE_YEAR",
        "COMMITMENT_PLAN_FLEXIBLE_THREE_YEARS",
    ]
    computeEnginePreferences: ComputeEnginePreferences
    networkCostParameters: VirtualMachinePreferencesNetworkCostParameters
    regionPreferences: RegionPreferences
    sizingOptimizationCustomParameters: (
        VirtualMachinePreferencesSizingOptimizationCustomParameters
    )
    sizingOptimizationStrategy: typing_extensions.Literal[
        "SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED",
        "SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE",
        "SIZING_OPTIMIZATION_STRATEGY_MODERATE",
        "SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE",
        "SIZING_OPTIMIZATION_STRATEGY_CUSTOM",
    ]
    soleTenancyPreferences: SoleTenancyPreferences
    targetProduct: typing_extensions.Literal[
        "COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED",
        "COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE",
        "COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE",
        "COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY",
    ]
    vmwareEnginePreferences: VmwareEnginePreferences

@typing.type_check_only
class VirtualMachinePreferencesNetworkCostParameters(
    typing_extensions.TypedDict, total=False
):
    estimatedEgressTrafficPercentage: int

@typing.type_check_only
class VirtualMachinePreferencesSizingOptimizationCustomParameters(
    typing_extensions.TypedDict, total=False
):
    aggregationMethod: typing_extensions.Literal[
        "AGGREGATION_METHOD_UNSPECIFIED",
        "AGGREGATION_METHOD_AVERAGE",
        "AGGREGATION_METHOD_MEDIAN",
        "AGGREGATION_METHOD_NINETY_FIFTH_PERCENTILE",
        "AGGREGATION_METHOD_PEAK",
    ]
    cpuUsagePercentage: int
    memoryUsagePercentage: int
    storageMultiplier: float

@typing.type_check_only
class VmwareDiskConfig(typing_extensions.TypedDict, total=False):
    backingType: typing_extensions.Literal[
        "BACKING_TYPE_UNSPECIFIED",
        "BACKING_TYPE_FLAT_V1",
        "BACKING_TYPE_FLAT_V2",
        "BACKING_TYPE_PMEM",
        "BACKING_TYPE_RDM_V1",
        "BACKING_TYPE_RDM_V2",
        "BACKING_TYPE_SESPARSE",
        "BACKING_TYPE_SESPARSE_V1",
        "BACKING_TYPE_SESPARSE_V2",
    ]
    rdmCompatibilityMode: str
    shared: bool
    vmdkDiskMode: str

@typing.type_check_only
class VmwareEngineMigrationTarget(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VmwareEnginePreferences(typing_extensions.TypedDict, total=False):
    commitmentPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "ON_DEMAND",
        "COMMITMENT_1_YEAR_MONTHLY_PAYMENTS",
        "COMMITMENT_3_YEAR_MONTHLY_PAYMENTS",
        "COMMITMENT_1_YEAR_UPFRONT_PAYMENT",
        "COMMITMENT_3_YEAR_UPFRONT_PAYMENT",
        "COMMITMENT_FLEXIBLE_3_YEAR_MONTHLY_PAYMENTS",
        "COMMITMENT_FLEXIBLE_3_YEAR_UPFRONT_PAYMENT",
    ]
    cpuOvercommitRatio: float
    licenseDiscountPercentage: float
    machinePreferences: VMwareEngineMachinePreferences
    memoryOvercommitRatio: float
    serviceType: typing_extensions.Literal[
        "SERVICE_TYPE_UNSPECIFIED",
        "SERVICE_TYPE_FULLY_LICENSED",
        "SERVICE_TYPE_PORTABLE_LICENSE",
    ]
    storageDeduplicationCompressionRatio: float

@typing.type_check_only
class VmwarePlatformDetails(typing_extensions.TypedDict, total=False):
    esxHyperthreading: typing_extensions.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    esxVersion: str
    osid: str
    vcenterVersion: str

@typing.type_check_only
class XlsxOutputFile(typing_extensions.TypedDict, total=False):
    signedUri: SignedUri
