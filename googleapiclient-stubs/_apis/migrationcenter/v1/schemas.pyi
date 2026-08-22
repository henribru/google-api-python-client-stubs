import typing

_list = list

@typing.type_check_only
class AddAssetsToGroupRequest(typing.TypedDict, total=False):
    allowExisting: bool
    assets: AssetList
    requestId: str

@typing.type_check_only
class AggregateAssetsValuesRequest(typing.TypedDict, total=False):
    aggregations: _list[Aggregation]
    filter: str
    showHidden: bool

@typing.type_check_only
class AggregateAssetsValuesResponse(typing.TypedDict, total=False):
    results: _list[AggregationResult]

@typing.type_check_only
class Aggregation(typing.TypedDict, total=False):
    count: AggregationCount
    field: str
    frequency: AggregationFrequency
    histogram: AggregationHistogram
    sum: AggregationSum

@typing.type_check_only
class AggregationCount(typing.TypedDict, total=False): ...

@typing.type_check_only
class AggregationFrequency(typing.TypedDict, total=False): ...

@typing.type_check_only
class AggregationHistogram(typing.TypedDict, total=False):
    lowerBounds: _list[float]

@typing.type_check_only
class AggregationResult(typing.TypedDict, total=False):
    count: AggregationResultCount
    field: str
    frequency: AggregationResultFrequency
    histogram: AggregationResultHistogram
    sum: AggregationResultSum

@typing.type_check_only
class AggregationResultCount(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class AggregationResultFrequency(typing.TypedDict, total=False):
    values: dict[str, typing.Any]

@typing.type_check_only
class AggregationResultHistogram(typing.TypedDict, total=False):
    buckets: _list[AggregationResultHistogramBucket]

@typing.type_check_only
class AggregationResultHistogramBucket(typing.TypedDict, total=False):
    count: str
    lowerBound: float
    upperBound: float

@typing.type_check_only
class AggregationResultSum(typing.TypedDict, total=False):
    value: float

@typing.type_check_only
class AggregationSum(typing.TypedDict, total=False): ...

@typing.type_check_only
class Asset(typing.TypedDict, total=False):
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
    machineDetails: MachineDetails
    name: str
    performanceData: AssetPerformanceData
    sources: _list[str]
    title: str
    updateTime: str

@typing.type_check_only
class AssetFrame(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    collectionType: typing.Literal[
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
    machineDetails: MachineDetails
    performanceSamples: _list[PerformanceSample]
    reportTime: str
    traceToken: str

@typing.type_check_only
class AssetList(typing.TypedDict, total=False):
    assetIds: _list[str]

@typing.type_check_only
class AssetPerformanceData(typing.TypedDict, total=False):
    dailyResourceUsageAggregations: _list[DailyResourceUsageAggregation]

@typing.type_check_only
class AssetsExportJob(typing.TypedDict, total=False):
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
class AssetsExportJobExecution(typing.TypedDict, total=False):
    endTime: str
    executionId: str
    expireTime: str
    requestedAssetCount: int
    result: AssetsExportJobExecutionResult
    startTime: str

@typing.type_check_only
class AssetsExportJobExecutionResult(typing.TypedDict, total=False):
    error: Status
    outputFiles: OutputFileList
    signedUris: SignedUris

@typing.type_check_only
class AssetsExportJobExportCondition(typing.TypedDict, total=False):
    filter: str

@typing.type_check_only
class AssetsExportJobInventory(typing.TypedDict, total=False): ...

@typing.type_check_only
class AssetsExportJobNetworkDependencies(typing.TypedDict, total=False): ...

@typing.type_check_only
class AssetsExportJobPerformanceData(typing.TypedDict, total=False):
    maxDays: int

@typing.type_check_only
class AwsEc2PlatformDetails(typing.TypedDict, total=False):
    hyperthreading: typing.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str
    machineTypeLabel: str

@typing.type_check_only
class AwsRds(typing.TypedDict, total=False): ...

@typing.type_check_only
class AzureVmPlatformDetails(typing.TypedDict, total=False):
    hyperthreading: typing.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str
    machineTypeLabel: str
    provisioningState: str

@typing.type_check_only
class BatchDeleteAssetsRequest(typing.TypedDict, total=False):
    allowMissing: bool
    cascadingRules: _list[CascadingRule]
    names: _list[str]

@typing.type_check_only
class BatchUpdateAssetsRequest(typing.TypedDict, total=False):
    requests: _list[UpdateAssetRequest]

@typing.type_check_only
class BatchUpdateAssetsResponse(typing.TypedDict, total=False):
    assets: _list[Asset]

@typing.type_check_only
class BiosDetails(typing.TypedDict, total=False):
    biosName: str
    id: str
    manufacturer: str
    releaseDate: Date
    smbiosUuid: str
    version: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CascadeLogicalDBsRule(typing.TypedDict, total=False): ...

@typing.type_check_only
class CascadingRule(typing.TypedDict, total=False):
    cascadeLogicalDbs: CascadeLogicalDBsRule

@typing.type_check_only
class ComputeEngineMigrationTarget(typing.TypedDict, total=False):
    shape: ComputeEngineShapeDescriptor

@typing.type_check_only
class ComputeEnginePreferences(typing.TypedDict, total=False):
    licenseType: typing.Literal[
        "LICENSE_TYPE_UNSPECIFIED",
        "LICENSE_TYPE_DEFAULT",
        "LICENSE_TYPE_BRING_YOUR_OWN_LICENSE",
    ]
    machinePreferences: MachinePreferences
    persistentDiskType: typing.Literal[
        "PERSISTENT_DISK_TYPE_UNSPECIFIED",
        "PERSISTENT_DISK_TYPE_STANDARD",
        "PERSISTENT_DISK_TYPE_BALANCED",
        "PERSISTENT_DISK_TYPE_SSD",
    ]

@typing.type_check_only
class ComputeEngineShapeDescriptor(typing.TypedDict, total=False):
    logicalCoreCount: int
    machineType: str
    memoryMb: int
    physicalCoreCount: int
    series: str
    storage: _list[ComputeStorageDescriptor]

@typing.type_check_only
class ComputeStorageDescriptor(typing.TypedDict, total=False):
    sizeGb: int
    type: typing.Literal[
        "PERSISTENT_DISK_TYPE_UNSPECIFIED",
        "PERSISTENT_DISK_TYPE_STANDARD",
        "PERSISTENT_DISK_TYPE_BALANCED",
        "PERSISTENT_DISK_TYPE_SSD",
    ]

@typing.type_check_only
class CpuUsageSample(typing.TypedDict, total=False):
    utilizedPercentage: float

@typing.type_check_only
class CsvOutputFile(typing.TypedDict, total=False):
    columnsCount: int
    rowCount: int
    signedUri: SignedUri

@typing.type_check_only
class DailyResourceUsageAggregation(typing.TypedDict, total=False):
    cpu: DailyResourceUsageAggregationCPU
    date: Date
    disk: DailyResourceUsageAggregationDisk
    memory: DailyResourceUsageAggregationMemory
    network: DailyResourceUsageAggregationNetwork

@typing.type_check_only
class DailyResourceUsageAggregationCPU(typing.TypedDict, total=False):
    utilizationPercentage: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationDisk(typing.TypedDict, total=False):
    iops: DailyResourceUsageAggregationStats
    readIops: DailyResourceUsageAggregationStats
    writeIops: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationMemory(typing.TypedDict, total=False):
    utilizationPercentage: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationNetwork(typing.TypedDict, total=False):
    egressBps: DailyResourceUsageAggregationStats
    ingressBps: DailyResourceUsageAggregationStats

@typing.type_check_only
class DailyResourceUsageAggregationStats(typing.TypedDict, total=False):
    average: float
    median: float
    ninteyFifthPercentile: float
    peak: float

@typing.type_check_only
class DatabaseDeploymentDetails(typing.TypedDict, total=False):
    aggregatedStats: DatabaseDeploymentDetailsAggregatedStats
    awsRds: AwsRds
    edition: str
    generatedId: str
    manualUniqueId: str
    mysql: MysqlDatabaseDeployment
    postgresql: PostgreSqlDatabaseDeployment
    sqlServer: SqlServerDatabaseDeployment
    topology: DatabaseDeploymentTopology
    version: str

@typing.type_check_only
class DatabaseDeploymentDetailsAggregatedStats(typing.TypedDict, total=False):
    databaseCount: int

@typing.type_check_only
class DatabaseDeploymentTopology(typing.TypedDict, total=False):
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
class DatabaseDetails(typing.TypedDict, total=False):
    allocatedStorageBytes: str
    databaseName: str
    parentDatabaseDeployment: DatabaseDetailsParentDatabaseDeployment
    schemas: _list[DatabaseSchema]

@typing.type_check_only
class DatabaseDetailsParentDatabaseDeployment(typing.TypedDict, total=False):
    generatedId: str
    manualUniqueId: str

@typing.type_check_only
class DatabaseInstance(typing.TypedDict, total=False):
    instanceName: str
    network: DatabaseInstanceNetwork
    role: typing.Literal["ROLE_UNSPECIFIED", "PRIMARY", "SECONDARY", "ARBITER"]

@typing.type_check_only
class DatabaseInstanceNetwork(typing.TypedDict, total=False):
    hostNames: _list[str]
    ipAddresses: _list[str]
    primaryMacAddress: str

@typing.type_check_only
class DatabaseObjects(typing.TypedDict, total=False):
    category: typing.Literal[
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
class DatabaseSchema(typing.TypedDict, total=False):
    mysql: MySqlSchemaDetails
    objects: _list[DatabaseObjects]
    postgresql: PostgreSqlSchemaDetails
    schemaName: str
    sqlServer: SqlServerSchemaDetails
    tablesSizeBytes: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DiscoveryClient(typing.TypedDict, total=False):
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
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "OFFLINE", "DEGRADED", "EXPIRED"
    ]
    ttl: str
    updateTime: str
    version: str

@typing.type_check_only
class DiskEntry(typing.TypedDict, total=False):
    capacityBytes: str
    diskLabel: str
    diskLabelType: str
    freeBytes: str
    hwAddress: str
    interfaceType: typing.Literal[
        "INTERFACE_TYPE_UNSPECIFIED",
        "IDE",
        "SATA",
        "SAS",
        "SCSI",
        "NVME",
        "FC",
        "ISCSI",
    ]
    partitions: DiskPartitionList
    vmware: VmwareDiskConfig

@typing.type_check_only
class DiskEntryList(typing.TypedDict, total=False):
    entries: _list[DiskEntry]

@typing.type_check_only
class DiskPartition(typing.TypedDict, total=False):
    capacityBytes: str
    fileSystem: str
    freeBytes: str
    mountPoint: str
    subPartitions: DiskPartitionList
    type: str
    uuid: str

@typing.type_check_only
class DiskPartitionDetails(typing.TypedDict, total=False):
    freeSpaceBytes: str
    partitions: DiskPartitionList
    totalCapacityBytes: str

@typing.type_check_only
class DiskPartitionList(typing.TypedDict, total=False):
    entries: _list[DiskPartition]

@typing.type_check_only
class DiskUsageSample(typing.TypedDict, total=False):
    averageIops: float
    averageReadIops: float
    averageWriteIops: float

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ErrorFrame(typing.TypedDict, total=False):
    ingestionTime: str
    name: str
    originalFrame: AssetFrame
    violations: _list[FrameViolationEntry]

@typing.type_check_only
class ExecutionReport(typing.TypedDict, total=False):
    executionErrors: ValidationReport
    framesReported: int
    totalRowsCount: int

@typing.type_check_only
class FileValidationReport(typing.TypedDict, total=False):
    fileErrors: _list[ImportError]
    fileName: str
    partialReport: bool
    rowErrors: _list[ImportRowError]

@typing.type_check_only
class FitDescriptor(typing.TypedDict, total=False):
    fitLevel: typing.Literal[
        "FIT_LEVEL_UNSPECIFIED", "FIT", "NO_FIT", "REQUIRES_EFFORT"
    ]

@typing.type_check_only
class FrameViolationEntry(typing.TypedDict, total=False):
    field: str
    violation: str

@typing.type_check_only
class Frames(typing.TypedDict, total=False):
    framesData: _list[AssetFrame]

@typing.type_check_only
class FstabEntry(typing.TypedDict, total=False):
    file: str
    freq: int
    mntops: str
    passno: int
    spec: str
    vfstype: str

@typing.type_check_only
class FstabEntryList(typing.TypedDict, total=False):
    entries: _list[FstabEntry]

@typing.type_check_only
class GenericInsight(typing.TypedDict, total=False):
    additionalInformation: _list[str]
    defaultMessage: str
    messageId: str

@typing.type_check_only
class GenericPlatformDetails(typing.TypedDict, total=False):
    hyperthreading: typing.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GuestConfigDetails(typing.TypedDict, total=False):
    fstab: FstabEntryList
    hosts: HostsEntryList
    issue: str
    nfsExports: NfsExportList
    selinuxMode: typing.Literal[
        "SE_LINUX_MODE_UNSPECIFIED",
        "SE_LINUX_MODE_DISABLED",
        "SE_LINUX_MODE_PERMISSIVE",
        "SE_LINUX_MODE_ENFORCING",
    ]

@typing.type_check_only
class GuestInstalledApplication(typing.TypedDict, total=False):
    applicationName: str
    installTime: str
    licenses: _list[str]
    path: str
    vendor: str
    version: str

@typing.type_check_only
class GuestInstalledApplicationList(typing.TypedDict, total=False):
    entries: _list[GuestInstalledApplication]

@typing.type_check_only
class GuestOsDetails(typing.TypedDict, total=False):
    config: GuestConfigDetails
    family: typing.Literal[
        "OS_FAMILY_UNKNOWN", "OS_FAMILY_WINDOWS", "OS_FAMILY_LINUX", "OS_FAMILY_UNIX"
    ]
    osName: str
    runtime: GuestRuntimeDetails
    version: str

@typing.type_check_only
class GuestRuntimeDetails(typing.TypedDict, total=False):
    domain: str
    installedApps: GuestInstalledApplicationList
    lastBootTime: str
    machineName: str
    network: RuntimeNetworkInfo
    openFileList: OpenFileList
    processes: RunningProcessList
    services: RunningServiceList

@typing.type_check_only
class HostsEntry(typing.TypedDict, total=False):
    hostNames: _list[str]
    ip: str

@typing.type_check_only
class HostsEntryList(typing.TypedDict, total=False):
    entries: _list[HostsEntry]

@typing.type_check_only
class ImportDataFile(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    format: typing.Literal[
        "IMPORT_JOB_FORMAT_UNSPECIFIED",
        "IMPORT_JOB_FORMAT_RVTOOLS_XLSX",
        "IMPORT_JOB_FORMAT_RVTOOLS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV",
        "IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV",
        "IMPORT_JOB_FORMAT_STRATOZONE_CSV",
        "IMPORT_JOB_FORMAT_DATABASE_ZIP",
    ]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE"]
    uploadFileInfo: UploadFileInfo

@typing.type_check_only
class ImportError(typing.TypedDict, total=False):
    errorDetails: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"]

@typing.type_check_only
class ImportJob(typing.TypedDict, total=False):
    assetSource: str
    completeTime: str
    createTime: str
    displayName: str
    executionReport: ExecutionReport
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
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
class ImportRowError(typing.TypedDict, total=False):
    archiveError: ImportRowErrorArchiveErrorDetails
    assetTitle: str
    csvError: ImportRowErrorCsvErrorDetails
    errors: _list[ImportError]
    rowNumber: int
    vmName: str
    vmUuid: str
    xlsxError: ImportRowErrorXlsxErrorDetails

@typing.type_check_only
class ImportRowErrorArchiveErrorDetails(typing.TypedDict, total=False):
    csvError: ImportRowErrorCsvErrorDetails
    filePath: str

@typing.type_check_only
class ImportRowErrorCsvErrorDetails(typing.TypedDict, total=False):
    rowNumber: int

@typing.type_check_only
class ImportRowErrorXlsxErrorDetails(typing.TypedDict, total=False):
    rowNumber: int
    sheet: str

@typing.type_check_only
class Insight(typing.TypedDict, total=False):
    genericInsight: GenericInsight
    migrationInsight: MigrationInsight

@typing.type_check_only
class InsightList(typing.TypedDict, total=False):
    insights: _list[Insight]
    updateTime: str

@typing.type_check_only
class ListAssetsExportJobsResponse(typing.TypedDict, total=False):
    assetsExportJobs: _list[AssetsExportJob]
    nextPageToken: str

@typing.type_check_only
class ListAssetsResponse(typing.TypedDict, total=False):
    assets: _list[Asset]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveryClientsResponse(typing.TypedDict, total=False):
    discoveryClients: _list[DiscoveryClient]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListErrorFramesResponse(typing.TypedDict, total=False):
    errorFrames: _list[ErrorFrame]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGroupsResponse(typing.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImportDataFilesResponse(typing.TypedDict, total=False):
    importDataFiles: _list[ImportDataFile]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImportJobsResponse(typing.TypedDict, total=False):
    importJobs: _list[ImportJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPreferenceSetsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    preferenceSets: _list[PreferenceSet]
    unreachable: _list[str]

@typing.type_check_only
class ListRelationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    relations: _list[Relation]

@typing.type_check_only
class ListReportConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reportConfigs: _list[ReportConfig]
    unreachable: _list[str]

@typing.type_check_only
class ListReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]
    unreachable: _list[str]

@typing.type_check_only
class ListSourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MachineArchitectureDetails(typing.TypedDict, total=False):
    bios: BiosDetails
    cpuArchitecture: str
    cpuManufacturer: str
    cpuName: str
    cpuSocketCount: int
    cpuThreadCount: int
    firmwareType: typing.Literal["FIRMWARE_TYPE_UNSPECIFIED", "BIOS", "EFI"]
    hyperthreading: typing.Literal[
        "CPU_HYPER_THREADING_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    vendor: str

@typing.type_check_only
class MachineDetails(typing.TypedDict, total=False):
    architecture: MachineArchitectureDetails
    coreCount: int
    createTime: str
    diskPartitions: DiskPartitionDetails
    disks: MachineDiskDetails
    guestOs: GuestOsDetails
    machineName: str
    memoryMb: int
    network: MachineNetworkDetails
    platform: PlatformDetails
    powerState: typing.Literal[
        "POWER_STATE_UNSPECIFIED",
        "PENDING",
        "ACTIVE",
        "SUSPENDING",
        "SUSPENDED",
        "DELETING",
        "DELETED",
    ]
    uuid: str

@typing.type_check_only
class MachineDiskDetails(typing.TypedDict, total=False):
    disks: DiskEntryList
    totalCapacityBytes: str
    totalFreeBytes: str

@typing.type_check_only
class MachineNetworkDetails(typing.TypedDict, total=False):
    adapters: NetworkAdapterList
    defaultGateway: str
    primaryIpAddress: str
    primaryMacAddress: str
    publicIpAddress: str

@typing.type_check_only
class MachinePreferences(typing.TypedDict, total=False):
    allowedMachineSeries: _list[MachineSeries]

@typing.type_check_only
class MachineSeries(typing.TypedDict, total=False):
    code: str

@typing.type_check_only
class MemoryUsageSample(typing.TypedDict, total=False):
    utilizedPercentage: float

@typing.type_check_only
class MigrationInsight(typing.TypedDict, total=False):
    computeEngineTarget: ComputeEngineMigrationTarget
    fit: FitDescriptor

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MySqlPlugin(typing.TypedDict, total=False):
    enabled: bool
    plugin: str
    version: str

@typing.type_check_only
class MySqlProperty(typing.TypedDict, total=False):
    enabled: bool
    numericValue: str
    property: str

@typing.type_check_only
class MySqlSchemaDetails(typing.TypedDict, total=False):
    storageEngines: _list[MySqlStorageEngineDetails]

@typing.type_check_only
class MySqlStorageEngineDetails(typing.TypedDict, total=False):
    encryptedTableCount: int
    engine: typing.Literal[
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
class MySqlVariable(typing.TypedDict, total=False):
    category: str
    value: str
    variable: str

@typing.type_check_only
class MysqlDatabaseDeployment(typing.TypedDict, total=False):
    plugins: _list[MySqlPlugin]
    properties: _list[MySqlProperty]
    resourceGroupsCount: int
    variables: _list[MySqlVariable]

@typing.type_check_only
class NetworkAdapterDetails(typing.TypedDict, total=False):
    adapterType: str
    addresses: NetworkAddressList
    macAddress: str

@typing.type_check_only
class NetworkAdapterList(typing.TypedDict, total=False):
    entries: _list[NetworkAdapterDetails]

@typing.type_check_only
class NetworkAddress(typing.TypedDict, total=False):
    assignment: typing.Literal[
        "ADDRESS_ASSIGNMENT_UNSPECIFIED",
        "ADDRESS_ASSIGNMENT_STATIC",
        "ADDRESS_ASSIGNMENT_DHCP",
    ]
    bcast: str
    fqdn: str
    ipAddress: str
    subnetMask: str

@typing.type_check_only
class NetworkAddressList(typing.TypedDict, total=False):
    entries: _list[NetworkAddress]

@typing.type_check_only
class NetworkConnection(typing.TypedDict, total=False):
    localIpAddress: str
    localPort: int
    pid: str
    processName: str
    protocol: str
    remoteIpAddress: str
    remotePort: int
    state: typing.Literal[
        "STATE_UNSPECIFIED", "OPENING", "OPEN", "LISTEN", "CLOSING", "CLOSED"
    ]

@typing.type_check_only
class NetworkConnectionList(typing.TypedDict, total=False):
    entries: _list[NetworkConnection]

@typing.type_check_only
class NetworkUsageSample(typing.TypedDict, total=False):
    averageEgressBps: float
    averageIngressBps: float

@typing.type_check_only
class NfsExport(typing.TypedDict, total=False):
    exportDirectory: str
    hosts: _list[str]

@typing.type_check_only
class NfsExportList(typing.TypedDict, total=False):
    entries: _list[NfsExport]

@typing.type_check_only
class OpenFileDetails(typing.TypedDict, total=False):
    command: str
    filePath: str
    fileType: str
    user: str

@typing.type_check_only
class OpenFileList(typing.TypedDict, total=False):
    entries: _list[OpenFileDetails]

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
class OutputFile(typing.TypedDict, total=False):
    csvOutputFile: CsvOutputFile
    fileSizeBytes: str
    xlsxOutputFile: XlsxOutputFile

@typing.type_check_only
class OutputFileList(typing.TypedDict, total=False):
    entries: _list[OutputFile]

@typing.type_check_only
class PerformanceSample(typing.TypedDict, total=False):
    cpu: CpuUsageSample
    disk: DiskUsageSample
    memory: MemoryUsageSample
    network: NetworkUsageSample
    sampleTime: str

@typing.type_check_only
class PhysicalPlatformDetails(typing.TypedDict, total=False):
    hyperthreading: typing.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    location: str

@typing.type_check_only
class PlatformDetails(typing.TypedDict, total=False):
    awsEc2Details: AwsEc2PlatformDetails
    azureVmDetails: AzureVmPlatformDetails
    genericDetails: GenericPlatformDetails
    physicalDetails: PhysicalPlatformDetails
    vmwareDetails: VmwarePlatformDetails

@typing.type_check_only
class PostgreSqlDatabaseDeployment(typing.TypedDict, total=False):
    properties: _list[PostgreSqlProperty]
    settings: _list[PostgreSqlSetting]

@typing.type_check_only
class PostgreSqlExtension(typing.TypedDict, total=False):
    extension: str
    version: str

@typing.type_check_only
class PostgreSqlProperty(typing.TypedDict, total=False):
    enabled: bool
    numericValue: str
    property: str

@typing.type_check_only
class PostgreSqlSchemaDetails(typing.TypedDict, total=False):
    foreignTablesCount: int
    postgresqlExtensions: _list[PostgreSqlExtension]

@typing.type_check_only
class PostgreSqlSetting(typing.TypedDict, total=False):
    boolValue: bool
    intValue: str
    realValue: float
    setting: str
    source: str
    stringValue: str
    unit: str

@typing.type_check_only
class PreferenceSet(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    updateTime: str
    virtualMachinePreferences: VirtualMachinePreferences

@typing.type_check_only
class RegionPreferences(typing.TypedDict, total=False):
    preferredRegions: _list[str]

@typing.type_check_only
class Relation(typing.TypedDict, total=False):
    createTime: str
    dstAsset: str
    name: str
    srcAsset: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "LOGICAL_DATABASE", "DATABASE_DEPLOYMENT_HOSTING_SERVER"
    ]

@typing.type_check_only
class RemoveAssetsFromGroupRequest(typing.TypedDict, total=False):
    allowMissing: bool
    assets: AssetList
    requestId: str

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "SUCCEEDED", "FAILED"]
    summary: ReportSummary
    type: typing.Literal["TYPE_UNSPECIFIED", "TOTAL_COST_OF_OWNERSHIP"]
    updateTime: str

@typing.type_check_only
class ReportAssetFramesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ReportConfig(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    groupPreferencesetAssignments: _list[ReportConfigGroupPreferenceSetAssignment]
    name: str
    updateTime: str

@typing.type_check_only
class ReportConfigGroupPreferenceSetAssignment(typing.TypedDict, total=False):
    group: str
    preferenceSet: str

@typing.type_check_only
class ReportSummary(typing.TypedDict, total=False):
    allAssetsStats: ReportSummaryAssetAggregateStats
    groupFindings: _list[ReportSummaryGroupFinding]

@typing.type_check_only
class ReportSummaryAssetAggregateStats(typing.TypedDict, total=False):
    coreCountHistogram: ReportSummaryHistogramChartData
    memoryBytesHistogram: ReportSummaryHistogramChartData
    memoryUtilizationChart: ReportSummaryUtilizationChartData
    operatingSystem: ReportSummaryChartData
    softwareInstances: ReportSummaryChartData
    storageBytesHistogram: ReportSummaryHistogramChartData
    storageUtilizationChart: ReportSummaryUtilizationChartData
    totalAssets: str
    totalCores: str
    totalMemoryBytes: str
    totalStorageBytes: str

@typing.type_check_only
class ReportSummaryChartData(typing.TypedDict, total=False):
    dataPoints: _list[ReportSummaryChartDataDataPoint]

@typing.type_check_only
class ReportSummaryChartDataDataPoint(typing.TypedDict, total=False):
    label: str
    value: float

@typing.type_check_only
class ReportSummaryComputeEngineFinding(typing.TypedDict, total=False):
    allocatedAssetCount: str
    allocatedDiskTypes: _list[
        typing.Literal[
            "PERSISTENT_DISK_TYPE_UNSPECIFIED",
            "PERSISTENT_DISK_TYPE_STANDARD",
            "PERSISTENT_DISK_TYPE_BALANCED",
            "PERSISTENT_DISK_TYPE_SSD",
        ]
    ]
    allocatedRegions: _list[str]
    machineSeriesAllocations: _list[ReportSummaryMachineSeriesAllocation]

@typing.type_check_only
class ReportSummaryGroupFinding(typing.TypedDict, total=False):
    assetAggregateStats: ReportSummaryAssetAggregateStats
    description: str
    displayName: str
    overlappingAssetCount: str
    preferenceSetFindings: _list[ReportSummaryGroupPreferenceSetFinding]

@typing.type_check_only
class ReportSummaryGroupPreferenceSetFinding(typing.TypedDict, total=False):
    computeEngineFinding: ReportSummaryComputeEngineFinding
    description: str
    displayName: str
    machinePreferences: VirtualMachinePreferences
    monthlyCostCompute: Money
    monthlyCostNetworkEgress: Money
    monthlyCostOsLicense: Money
    monthlyCostOther: Money
    monthlyCostStorage: Money
    monthlyCostTotal: Money
    soleTenantFinding: ReportSummarySoleTenantFinding
    vmwareEngineFinding: ReportSummaryVmwareEngineFinding

@typing.type_check_only
class ReportSummaryHistogramChartData(typing.TypedDict, total=False):
    buckets: _list[ReportSummaryHistogramChartDataBucket]

@typing.type_check_only
class ReportSummaryHistogramChartDataBucket(typing.TypedDict, total=False):
    count: str
    lowerBound: str
    upperBound: str

@typing.type_check_only
class ReportSummaryMachineSeriesAllocation(typing.TypedDict, total=False):
    allocatedAssetCount: str
    machineSeries: MachineSeries

@typing.type_check_only
class ReportSummarySoleTenantFinding(typing.TypedDict, total=False):
    allocatedAssetCount: str
    allocatedRegions: _list[str]
    nodeAllocations: _list[ReportSummarySoleTenantNodeAllocation]

@typing.type_check_only
class ReportSummarySoleTenantNodeAllocation(typing.TypedDict, total=False):
    allocatedAssetCount: str
    node: SoleTenantNodeType
    nodeCount: str

@typing.type_check_only
class ReportSummaryUtilizationChartData(typing.TypedDict, total=False):
    free: str
    used: str

@typing.type_check_only
class ReportSummaryVmwareEngineFinding(typing.TypedDict, total=False):
    allocatedAssetCount: str
    allocatedRegions: _list[str]
    nodeAllocations: _list[ReportSummaryVmwareNodeAllocation]

@typing.type_check_only
class ReportSummaryVmwareNode(typing.TypedDict, total=False):
    code: str

@typing.type_check_only
class ReportSummaryVmwareNodeAllocation(typing.TypedDict, total=False):
    allocatedAssetCount: str
    nodeCount: str
    vmwareNode: ReportSummaryVmwareNode

@typing.type_check_only
class RunAssetsExportJobRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RunAssetsExportJobResponse(typing.TypedDict, total=False):
    assetsExportJobExecution: AssetsExportJobExecution

@typing.type_check_only
class RunImportJobRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RunningProcess(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    cmdline: str
    exePath: str
    pid: str
    user: str

@typing.type_check_only
class RunningProcessList(typing.TypedDict, total=False):
    entries: _list[RunningProcess]

@typing.type_check_only
class RunningService(typing.TypedDict, total=False):
    cmdline: str
    exePath: str
    pid: str
    serviceName: str
    startMode: typing.Literal[
        "START_MODE_UNSPECIFIED", "BOOT", "SYSTEM", "AUTO", "MANUAL", "DISABLED"
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "PAUSED", "STOPPED"]

@typing.type_check_only
class RunningServiceList(typing.TypedDict, total=False):
    entries: _list[RunningService]

@typing.type_check_only
class RuntimeNetworkInfo(typing.TypedDict, total=False):
    connections: NetworkConnectionList
    scanTime: str

@typing.type_check_only
class SendDiscoveryClientHeartbeatRequest(typing.TypedDict, total=False):
    errors: _list[Status]
    version: str

@typing.type_check_only
class Settings(typing.TypedDict, total=False):
    disableCloudLogging: bool
    name: str
    preferenceSet: str

@typing.type_check_only
class SignedUri(typing.TypedDict, total=False):
    file: str
    uri: str

@typing.type_check_only
class SignedUriDestination(typing.TypedDict, total=False):
    fileFormat: typing.Literal["FILE_FORMAT_UNSPECIFIED", "CSV", "XLSX"]

@typing.type_check_only
class SignedUris(typing.TypedDict, total=False):
    signedUris: _list[SignedUri]

@typing.type_check_only
class SoleTenancyPreferences(typing.TypedDict, total=False):
    commitmentPlan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "ON_DEMAND",
        "COMMITMENT_1_YEAR",
        "COMMITMENT_3_YEAR",
    ]
    cpuOvercommitRatio: float
    hostMaintenancePolicy: typing.Literal[
        "HOST_MAINTENANCE_POLICY_UNSPECIFIED",
        "HOST_MAINTENANCE_POLICY_DEFAULT",
        "HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE",
        "HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP",
    ]
    nodeTypes: _list[SoleTenantNodeType]

@typing.type_check_only
class SoleTenantNodeType(typing.TypedDict, total=False):
    nodeName: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    errorFrameCount: int
    managed: bool
    name: str
    pendingFrameCount: int
    priority: int
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETING", "INVALID"]
    type: typing.Literal[
        "SOURCE_TYPE_UNKNOWN",
        "SOURCE_TYPE_UPLOAD",
        "SOURCE_TYPE_GUEST_OS_SCAN",
        "SOURCE_TYPE_INVENTORY_SCAN",
        "SOURCE_TYPE_CUSTOM",
        "SOURCE_TYPE_DISCOVERY_CLIENT",
    ]
    updateTime: str

@typing.type_check_only
class SqlServerDatabaseDeployment(typing.TypedDict, total=False):
    features: _list[SqlServerFeature]
    serverFlags: _list[SqlServerServerFlag]
    traceFlags: _list[SqlServerTraceFlag]

@typing.type_check_only
class SqlServerFeature(typing.TypedDict, total=False):
    enabled: bool
    featureName: str

@typing.type_check_only
class SqlServerSchemaDetails(typing.TypedDict, total=False):
    clrObjectCount: int

@typing.type_check_only
class SqlServerServerFlag(typing.TypedDict, total=False):
    serverFlagName: str
    value: str
    valueInUse: str

@typing.type_check_only
class SqlServerTraceFlag(typing.TypedDict, total=False):
    scope: typing.Literal["SCOPE_UNSPECIFIED", "OFF", "GLOBAL", "SESSION"]
    traceFlagName: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UpdateAssetRequest(typing.TypedDict, total=False):
    asset: Asset
    requestId: str
    updateMask: str

@typing.type_check_only
class UploadFileInfo(typing.TypedDict, total=False):
    headers: dict[str, typing.Any]
    signedUri: str
    uriExpirationTime: str

@typing.type_check_only
class ValidateImportJobRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ValidationReport(typing.TypedDict, total=False):
    fileValidations: _list[FileValidationReport]
    jobErrors: _list[ImportError]

@typing.type_check_only
class VirtualMachinePreferences(typing.TypedDict, total=False):
    commitmentPlan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "COMMITMENT_PLAN_NONE",
        "COMMITMENT_PLAN_ONE_YEAR",
        "COMMITMENT_PLAN_THREE_YEARS",
    ]
    computeEnginePreferences: ComputeEnginePreferences
    regionPreferences: RegionPreferences
    sizingOptimizationStrategy: typing.Literal[
        "SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED",
        "SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE",
        "SIZING_OPTIMIZATION_STRATEGY_MODERATE",
        "SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE",
    ]
    soleTenancyPreferences: SoleTenancyPreferences
    targetProduct: typing.Literal[
        "COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED",
        "COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE",
        "COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE",
        "COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY",
    ]
    vmwareEnginePreferences: VmwareEnginePreferences

@typing.type_check_only
class VmwareDiskConfig(typing.TypedDict, total=False):
    backingType: typing.Literal[
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
    rdmCompatibility: typing.Literal[
        "RDM_COMPATIBILITY_UNSPECIFIED",
        "PHYSICAL_COMPATIBILITY",
        "VIRTUAL_COMPATIBILITY",
    ]
    shared: bool
    vmdkMode: typing.Literal[
        "VMDK_MODE_UNSPECIFIED",
        "DEPENDENT",
        "INDEPENDENT_PERSISTENT",
        "INDEPENDENT_NONPERSISTENT",
    ]

@typing.type_check_only
class VmwareEnginePreferences(typing.TypedDict, total=False):
    commitmentPlan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "ON_DEMAND",
        "COMMITMENT_1_YEAR_MONTHLY_PAYMENTS",
        "COMMITMENT_3_YEAR_MONTHLY_PAYMENTS",
        "COMMITMENT_1_YEAR_UPFRONT_PAYMENT",
        "COMMITMENT_3_YEAR_UPFRONT_PAYMENT",
    ]
    cpuOvercommitRatio: float
    memoryOvercommitRatio: float
    storageDeduplicationCompressionRatio: float

@typing.type_check_only
class VmwarePlatformDetails(typing.TypedDict, total=False):
    esxHyperthreading: typing.Literal[
        "HYPERTHREADING_STATUS_UNSPECIFIED",
        "HYPERTHREADING_STATUS_DISABLED",
        "HYPERTHREADING_STATUS_ENABLED",
    ]
    esxVersion: str
    osid: str
    vcenterFolder: str
    vcenterUri: str
    vcenterVersion: str
    vcenterVmId: str

@typing.type_check_only
class XlsxOutputFile(typing.TypedDict, total=False):
    signedUri: SignedUri
