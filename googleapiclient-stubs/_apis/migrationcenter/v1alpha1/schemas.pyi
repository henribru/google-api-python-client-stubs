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
    hidden: bool
    hideReason: str
    hideTime: str
    insightList: InsightList
    labels: dict[str, typing.Any]
    name: str
    performanceData: AssetPerformanceData
    sources: _list[str]
    updateTime: str
    virtualMachineDetails: VirtualMachineDetails

@typing.type_check_only
class AssetFrame(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
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
class AwsEc2PlatformDetails(typing_extensions.TypedDict, total=False):
    location: str
    machineTypeLabel: str

@typing.type_check_only
class AzureVmPlatformDetails(typing_extensions.TypedDict, total=False):
    location: str
    machineTypeLabel: str
    provisioningState: str

@typing.type_check_only
class BatchDeleteAssetsRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
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
    storage: _list[ComputeStorageDescriptor]

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
    ]
    path: str

@typing.type_check_only
class GenericInsight(typing_extensions.TypedDict, total=False):
    additionalInformation: _list[str]
    defaultMessage: str
    messageId: str

@typing.type_check_only
class GenericPlatformDetails(typing_extensions.TypedDict, total=False):
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
    errors: _list[ImportError]
    rowNumber: int
    vmName: str
    vmUuid: str

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
class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[Asset]
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
    computeEngineTarget: ComputeEngineMigrationTarget
    fit: FitDescriptor
    gkeTarget: GoogleKubernetesEngineMigrationTarget
    vmwareEngineTarget: VmwareEngineMigrationTarget

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

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
    location: str

@typing.type_check_only
class PlatformDetails(typing_extensions.TypedDict, total=False):
    awsEc2Details: AwsEc2PlatformDetails
    azureVmDetails: AzureVmPlatformDetails
    genericDetails: GenericPlatformDetails
    physicalDetails: PhysicalPlatformDetails
    vmwareDetails: VmwarePlatformDetails

@typing.type_check_only
class PreferenceSet(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    updateTime: str
    virtualMachinePreferences: VirtualMachinePreferences

@typing.type_check_only
class RegionPreferences(typing_extensions.TypedDict, total=False):
    preferredRegions: _list[str]

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
    groupFindings: _list[ReportSummaryGroupFinding]

@typing.type_check_only
class ReportSummaryAssetAggregateStats(typing_extensions.TypedDict, total=False):
    assetAge: ReportSummaryChartData
    coreCountHistogram: ReportSummaryHistogramChartData
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
class ReportSummaryGroupFinding(typing_extensions.TypedDict, total=False):
    assetAggregateStats: ReportSummaryAssetAggregateStats
    description: str
    displayName: str
    overlappingAssetCount: str
    preferenceSetFindings: _list[ReportSummaryGroupPreferenceSetFinding]

@typing.type_check_only
class ReportSummaryGroupPreferenceSetFinding(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    machineFinding: ReportSummaryMachineFinding
    machinePreferences: VirtualMachinePreferences
    monthlyCostCompute: Money
    monthlyCostNetworkEgress: Money
    monthlyCostOsLicense: Money
    monthlyCostOther: Money
    monthlyCostStorage: Money
    monthlyCostTotal: Money
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
    allocatedDiskTypes: _list[str]
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
class Settings(typing_extensions.TypedDict, total=False):
    disableCloudLogging: bool
    name: str
    preferenceSet: str

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
    ]
    cpuOvercommitRatio: float
    hostMaintenancePolicy: typing_extensions.Literal[
        "HOST_MAINTENANCE_POLICY_UNSPECIFIED",
        "HOST_MAINTENANCE_POLICY_DEFAULT",
        "HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE",
        "HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP",
    ]
    nodeTypes: _list[SoleTenantNodeType]

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
    ]
    updateTime: str

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
    ]
    computeEnginePreferences: ComputeEnginePreferences
    networkCostParameters: VirtualMachinePreferencesNetworkCostParameters
    regionPreferences: RegionPreferences
    sizingOptimizationCustomParameters: VirtualMachinePreferencesSizingOptimizationCustomParameters
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
    ]
    cpuOvercommitRatio: float
    memoryOvercommitRatio: float
    storageDeduplicationCompressionRatio: float

@typing.type_check_only
class VmwarePlatformDetails(typing_extensions.TypedDict, total=False):
    esxVersion: str
    osid: str
    vcenterVersion: str
