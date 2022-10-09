import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdaptingOSStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AddGroupMigrationRequest(typing_extensions.TypedDict, total=False):
    migratingVm: str

@typing.type_check_only
class ApplianceVersion(typing_extensions.TypedDict, total=False):
    critical: bool
    releaseNotesUri: str
    uri: str
    version: str

@typing.type_check_only
class AppliedLicense(typing_extensions.TypedDict, total=False):
    osLicense: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "NONE", "PAYG", "BYOL"]

@typing.type_check_only
class AvailableUpdates(typing_extensions.TypedDict, total=False):
    inPlaceUpdate: ApplianceVersion
    newDeployableAppliance: ApplianceVersion

@typing.type_check_only
class CancelCloneJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelCutoverJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloneJob(typing_extensions.TypedDict, total=False):
    computeEngineTargetDetails: ComputeEngineTargetDetails
    computeEngineVmDetails: TargetVMDetails
    createTime: str
    endTime: str
    error: Status
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "ACTIVE",
        "FAILED",
        "SUCCEEDED",
        "CANCELLED",
        "CANCELLING",
        "ADAPTING_OS",
    ]
    stateTime: str
    steps: _list[CloneStep]
    targetDetails: TargetVMDetails

@typing.type_check_only
class CloneStep(typing_extensions.TypedDict, total=False):
    adaptingOs: AdaptingOSStep
    endTime: str
    instantiatingMigratedVm: InstantiatingMigratedVMStep
    preparingVmDisks: PreparingVMDisksStep
    startTime: str

@typing.type_check_only
class ComputeEngineTargetDefaults(typing_extensions.TypedDict, total=False):
    additionalLicenses: _list[str]
    appliedLicense: AppliedLicense
    bootOption: typing_extensions.Literal[
        "COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED",
        "COMPUTE_ENGINE_BOOT_OPTION_EFI",
        "COMPUTE_ENGINE_BOOT_OPTION_BIOS",
    ]
    computeScheduling: ComputeScheduling
    diskType: typing_extensions.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
    ]
    hostname: str
    labels: dict[str, typing.Any]
    licenseType: typing_extensions.Literal[
        "COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT",
        "COMPUTE_ENGINE_LICENSE_TYPE_PAYG",
        "COMPUTE_ENGINE_LICENSE_TYPE_BYOL",
    ]
    machineType: str
    machineTypeSeries: str
    metadata: dict[str, typing.Any]
    networkInterfaces: _list[NetworkInterface]
    networkTags: _list[str]
    secureBoot: bool
    serviceAccount: str
    targetProject: str
    vmName: str
    zone: str

@typing.type_check_only
class ComputeEngineTargetDetails(typing_extensions.TypedDict, total=False):
    additionalLicenses: _list[str]
    appliedLicense: AppliedLicense
    bootOption: typing_extensions.Literal[
        "COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED",
        "COMPUTE_ENGINE_BOOT_OPTION_EFI",
        "COMPUTE_ENGINE_BOOT_OPTION_BIOS",
    ]
    computeScheduling: ComputeScheduling
    diskType: typing_extensions.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
    ]
    hostname: str
    labels: dict[str, typing.Any]
    licenseType: typing_extensions.Literal[
        "COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT",
        "COMPUTE_ENGINE_LICENSE_TYPE_PAYG",
        "COMPUTE_ENGINE_LICENSE_TYPE_BYOL",
    ]
    machineType: str
    machineTypeSeries: str
    metadata: dict[str, typing.Any]
    networkInterfaces: _list[NetworkInterface]
    networkTags: _list[str]
    project: str
    secureBoot: bool
    serviceAccount: str
    vmName: str
    zone: str

@typing.type_check_only
class ComputeScheduling(typing_extensions.TypedDict, total=False):
    automaticRestart: bool
    minNodeCpus: int
    nodeAffinities: _list[SchedulingNodeAffinity]
    onHostMaintenance: typing_extensions.Literal[
        "ON_HOST_MAINTENANCE_UNSPECIFIED", "TERMINATE", "MIGRATE"
    ]
    restartType: typing_extensions.Literal[
        "RESTART_TYPE_UNSPECIFIED", "AUTOMATIC_RESTART", "NO_AUTOMATIC_RESTART"
    ]

@typing.type_check_only
class CutoverJob(typing_extensions.TypedDict, total=False):
    computeEngineTargetDetails: ComputeEngineTargetDetails
    computeEngineVmDetails: TargetVMDetails
    createTime: str
    endTime: str
    error: Status
    name: str
    progress: int
    progressPercent: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "FAILED",
        "SUCCEEDED",
        "CANCELLED",
        "CANCELLING",
        "ACTIVE",
        "ADAPTING_OS",
    ]
    stateMessage: str
    stateTime: str
    steps: _list[CutoverStep]
    targetDetails: TargetVMDetails

@typing.type_check_only
class CutoverStep(typing_extensions.TypedDict, total=False):
    endTime: str
    finalSync: ReplicationCycle
    instantiatingMigratedVm: InstantiatingMigratedVMStep
    preparingVmDisks: PreparingVMDisksStep
    previousReplicationCycle: ReplicationCycle
    shuttingDownSourceVm: ShuttingDownSourceVMStep
    startTime: str

@typing.type_check_only
class CycleStep(typing_extensions.TypedDict, total=False):
    endTime: str
    initializingReplication: InitializingReplicationStep
    postProcessing: PostProcessingStep
    replicating: ReplicatingStep
    startTime: str

@typing.type_check_only
class DatacenterConnector(typing_extensions.TypedDict, total=False):
    applianceInfrastructureVersion: str
    applianceSoftwareVersion: str
    availableVersions: AvailableUpdates
    bucket: str
    createTime: str
    error: Status
    name: str
    registrationId: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "OFFLINE", "FAILED", "ACTIVE"
    ]
    stateTime: str
    updateTime: str
    upgradeStatus: UpgradeStatus
    version: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchInventoryResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    updateTime: str
    vmwareVms: VmwareVmsDetails

@typing.type_check_only
class FinalizeMigrationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class InitializingReplicationStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InstantiatingMigratedVMStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Link(typing_extensions.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class ListCloneJobsResponse(typing_extensions.TypedDict, total=False):
    cloneJobs: _list[CloneJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCutoverJobsResponse(typing_extensions.TypedDict, total=False):
    cutoverJobs: _list[CutoverJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDatacenterConnectorsResponse(typing_extensions.TypedDict, total=False):
    datacenterConnectors: _list[DatacenterConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMigratingVmsResponse(typing_extensions.TypedDict, total=False):
    migratingVms: _list[MigratingVm]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListReplicationCyclesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    replicationCycles: _list[ReplicationCycle]
    unreachable: _list[str]

@typing.type_check_only
class ListSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]
    unreachable: _list[str]

@typing.type_check_only
class ListTargetProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    targetProjects: _list[TargetProject]
    unreachable: _list[str]

@typing.type_check_only
class ListUtilizationReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    utilizationReports: _list[UtilizationReport]

@typing.type_check_only
class LocalizedMessage(typing_extensions.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MigratingVm(typing_extensions.TypedDict, total=False):
    computeEngineTargetDefaults: ComputeEngineTargetDefaults
    computeEngineVmDefaults: TargetVMDetails
    createTime: str
    currentSyncInfo: ReplicationCycle
    description: str
    displayName: str
    error: Status
    group: str
    labels: dict[str, typing.Any]
    lastSync: ReplicationSync
    name: str
    policy: SchedulePolicy
    recentCloneJobs: _list[CloneJob]
    recentCutoverJobs: _list[CutoverJob]
    sourceVmId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "READY",
        "FIRST_SYNC",
        "ACTIVE",
        "CUTTING_OVER",
        "CUTOVER",
        "FINAL_SYNC",
        "PAUSED",
        "FINALIZING",
        "FINALIZED",
        "ERROR",
    ]
    stateTime: str
    targetDefaults: TargetVMDetails
    updateTime: str

@typing.type_check_only
class MigrationError(typing_extensions.TypedDict, total=False):
    actionItem: LocalizedMessage
    code: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "UNKNOWN_ERROR",
        "SOURCE_VALIDATION_ERROR",
        "SOURCE_REPLICATION_ERROR",
        "TARGET_REPLICATION_ERROR",
        "OS_ADAPTATION_ERROR",
        "CLONE_ERROR",
        "CUTOVER_ERROR",
        "UTILIZATION_REPORT_ERROR",
        "APPLIANCE_UPGRADE_ERROR",
    ]
    errorMessage: LocalizedMessage
    errorTime: str
    helpLinks: _list[Link]

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    externalIp: str
    internalIp: str
    network: str
    subnetwork: str

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
class PauseMigrationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PostProcessingStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PreparingVMDisksStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveGroupMigrationRequest(typing_extensions.TypedDict, total=False):
    migratingVm: str

@typing.type_check_only
class ReplicatingStep(typing_extensions.TypedDict, total=False):
    lastThirtyMinutesAverageBytesPerSecond: str
    lastTwoMinutesAverageBytesPerSecond: str
    replicatedBytes: str
    totalBytes: str

@typing.type_check_only
class ReplicationCycle(typing_extensions.TypedDict, total=False):
    cycleNumber: int
    endTime: str
    error: Status
    name: str
    progress: int
    progressPercent: int
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "FAILED", "SUCCEEDED"
    ]
    steps: _list[CycleStep]
    totalPauseDuration: str

@typing.type_check_only
class ReplicationSync(typing_extensions.TypedDict, total=False):
    lastSyncTime: str

@typing.type_check_only
class ResumeMigrationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SchedulePolicy(typing_extensions.TypedDict, total=False):
    idleDuration: str
    skipOsAdaptation: bool

@typing.type_check_only
class SchedulingNodeAffinity(typing_extensions.TypedDict, total=False):
    key: str
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "IN", "NOT_IN"]
    values: _list[str]

@typing.type_check_only
class ShuttingDownSourceVMStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    error: Status
    labels: dict[str, typing.Any]
    name: str
    updateTime: str
    vmware: VmwareSourceDetails

@typing.type_check_only
class StartMigrationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetProject(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    project: str
    updateTime: str

@typing.type_check_only
class TargetVMDetails(typing_extensions.TypedDict, total=False):
    appliedLicense: AppliedLicense
    bootOption: typing_extensions.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    computeScheduling: ComputeScheduling
    diskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "STANDARD", "BALANCED", "SSD"
    ]
    externalIp: str
    internalIp: str
    labels: dict[str, typing.Any]
    licenseType: typing_extensions.Literal["DEFAULT", "PAYG", "BYOL"]
    machineType: str
    machineTypeSeries: str
    metadata: dict[str, typing.Any]
    name: str
    network: str
    networkInterfaces: _list[NetworkInterface]
    networkTags: _list[str]
    project: str
    secureBoot: bool
    serviceAccount: str
    subnetwork: str
    targetProject: str
    zone: str

@typing.type_check_only
class UpgradeApplianceRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class UpgradeStatus(typing_extensions.TypedDict, total=False):
    error: Status
    previousVersion: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "FAILED", "SUCCEEDED"
    ]
    version: str

@typing.type_check_only
class UtilizationReport(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    error: Status
    frameEndTime: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "SUCCEEDED", "FAILED"
    ]
    stateTime: str
    timeFrame: typing_extensions.Literal[
        "TIME_FRAME_UNSPECIFIED", "WEEK", "MONTH", "YEAR"
    ]
    vmCount: int
    vms: _list[VmUtilizationInfo]
    vmsCount: int

@typing.type_check_only
class VmUtilizationInfo(typing_extensions.TypedDict, total=False):
    utilization: VmUtilizationMetrics
    vmId: str
    vmwareVmDetails: VmwareVmDetails

@typing.type_check_only
class VmUtilizationMetrics(typing_extensions.TypedDict, total=False):
    cpuAverage: int
    cpuAveragePercent: int
    cpuMax: int
    cpuMaxPercent: int
    diskIoRateAverage: str
    diskIoRateAverageKbps: str
    diskIoRateMax: str
    diskIoRateMaxKbps: str
    memoryAverage: int
    memoryAveragePercent: int
    memoryMax: int
    memoryMaxPercent: int
    networkThroughputAverage: str
    networkThroughputAverageKbps: str
    networkThroughputMax: str
    networkThroughputMaxKbps: str

@typing.type_check_only
class VmwareSourceDetails(typing_extensions.TypedDict, total=False):
    password: str
    thumbprint: str
    username: str
    vcenterIp: str

@typing.type_check_only
class VmwareVmDetails(typing_extensions.TypedDict, total=False):
    bootOption: typing_extensions.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    committedStorage: str
    committedStorageMb: str
    cpuCount: int
    datacenterDescription: str
    datacenterId: str
    diskCount: int
    displayName: str
    guestDescription: str
    memoryMb: int
    powerState: typing_extensions.Literal[
        "POWER_STATE_UNSPECIFIED", "ON", "OFF", "SUSPENDED"
    ]
    uuid: str
    vmId: str

@typing.type_check_only
class VmwareVmsDetails(typing_extensions.TypedDict, total=False):
    details: _list[VmwareVmDetails]
