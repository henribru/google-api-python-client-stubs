import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessKeyCredentials(typing_extensions.TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str

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
class AwsDiskDetails(typing_extensions.TypedDict, total=False):
    diskNumber: int
    sizeGb: str
    volumeId: str

@typing.type_check_only
class AwsSecurityGroup(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AwsSourceDetails(typing_extensions.TypedDict, total=False):
    accessKeyCreds: AccessKeyCredentials
    awsRegion: str
    error: Status
    inventorySecurityGroupNames: _list[str]
    inventoryTagList: _list[Tag]
    migrationResourcesUserTags: dict[str, typing.Any]
    publicIp: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "FAILED", "ACTIVE"]

@typing.type_check_only
class AwsSourceVmDetails(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    committedStorageBytes: str
    disks: _list[AwsDiskDetails]
    firmware: typing_extensions.Literal["FIRMWARE_UNSPECIFIED", "EFI", "BIOS"]
    vmCapabilitiesInfo: VmCapabilities

@typing.type_check_only
class AwsVmDetails(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED", "I386", "X86_64", "ARM64", "X86_64_MAC"
    ]
    bootOption: typing_extensions.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    committedStorageMb: str
    cpuCount: int
    diskCount: int
    displayName: str
    instanceType: str
    memoryMb: int
    osDescription: str
    powerState: typing_extensions.Literal[
        "POWER_STATE_UNSPECIFIED", "ON", "OFF", "SUSPENDED", "PENDING"
    ]
    securityGroups: _list[AwsSecurityGroup]
    sourceDescription: str
    sourceId: str
    tags: dict[str, typing.Any]
    virtualizationType: typing_extensions.Literal[
        "VM_VIRTUALIZATION_TYPE_UNSPECIFIED", "HVM", "PARAVIRTUAL"
    ]
    vmId: str
    vpcId: str
    zone: str

@typing.type_check_only
class AwsVmsDetails(typing_extensions.TypedDict, total=False):
    details: _list[AwsVmDetails]

@typing.type_check_only
class AzureDiskDetails(typing_extensions.TypedDict, total=False):
    diskId: str
    diskNumber: int
    sizeGb: str

@typing.type_check_only
class AzureSourceDetails(typing_extensions.TypedDict, total=False):
    azureLocation: str
    clientSecretCreds: ClientSecretCredentials
    error: Status
    migrationResourcesUserTags: dict[str, typing.Any]
    resourceGroupId: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "FAILED", "ACTIVE"]
    subscriptionId: str

@typing.type_check_only
class AzureSourceVmDetails(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    committedStorageBytes: str
    disks: _list[AzureDiskDetails]
    firmware: typing_extensions.Literal["FIRMWARE_UNSPECIFIED", "EFI", "BIOS"]
    vmCapabilitiesInfo: VmCapabilities

@typing.type_check_only
class AzureVmDetails(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    bootOption: typing_extensions.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    committedStorageMb: str
    computerName: str
    cpuCount: int
    diskCount: int
    disks: _list[Disk]
    memoryMb: int
    osDescription: OSDescription
    osDisk: OSDisk
    powerState: typing_extensions.Literal[
        "POWER_STATE_UNSPECIFIED",
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "DEALLOCATING",
        "DEALLOCATED",
        "UNKNOWN",
    ]
    tags: dict[str, typing.Any]
    vmId: str
    vmSize: str

@typing.type_check_only
class AzureVmsDetails(typing_extensions.TypedDict, total=False):
    details: _list[AzureVmDetails]

@typing.type_check_only
class BootDiskDefaults(typing_extensions.TypedDict, total=False):
    deviceName: str
    diskName: str
    diskType: typing_extensions.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
    ]
    encryption: Encryption
    image: DiskImageDefaults

@typing.type_check_only
class CancelCloneJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelCutoverJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelImageImportJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClientSecretCredentials(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: str
    tenantId: str

@typing.type_check_only
class CloneJob(typing_extensions.TypedDict, total=False):
    computeEngineDisksTargetDetails: ComputeEngineDisksTargetDetails
    computeEngineTargetDetails: ComputeEngineTargetDetails
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

@typing.type_check_only
class CloneStep(typing_extensions.TypedDict, total=False):
    adaptingOs: AdaptingOSStep
    endTime: str
    instantiatingMigratedVm: InstantiatingMigratedVMStep
    preparingVmDisks: PreparingVMDisksStep
    startTime: str

@typing.type_check_only
class ComputeEngineDisksTargetDefaults(typing_extensions.TypedDict, total=False):
    disks: _list[PersistentDiskDefaults]
    disksTargetDefaults: DisksMigrationDisksTargetDefaults
    targetProject: str
    vmTargetDefaults: DisksMigrationVmTargetDefaults
    zone: str

@typing.type_check_only
class ComputeEngineDisksTargetDetails(typing_extensions.TypedDict, total=False):
    disks: _list[PersistentDisk]
    disksTargetDetails: DisksMigrationDisksTargetDetails
    vmTargetDetails: DisksMigrationVmTargetDetails

@typing.type_check_only
class ComputeEngineTargetDefaults(typing_extensions.TypedDict, total=False):
    additionalLicenses: _list[str]
    appliedLicense: AppliedLicense
    bootConversion: typing_extensions.Literal[
        "BOOT_CONVERSION_UNSPECIFIED", "NONE", "BIOS_TO_EFI"
    ]
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
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
    ]
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    encryption: Encryption
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
    bootConversion: typing_extensions.Literal[
        "BOOT_CONVERSION_UNSPECIFIED", "NONE", "BIOS_TO_EFI"
    ]
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
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
    ]
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    encryption: Encryption
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
    minNodeCpus: int
    nodeAffinities: _list[SchedulingNodeAffinity]
    onHostMaintenance: typing_extensions.Literal[
        "ON_HOST_MAINTENANCE_UNSPECIFIED", "TERMINATE", "MIGRATE"
    ]
    restartType: typing_extensions.Literal[
        "RESTART_TYPE_UNSPECIFIED", "AUTOMATIC_RESTART", "NO_AUTOMATIC_RESTART"
    ]

@typing.type_check_only
class CreatingImageStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CutoverForecast(typing_extensions.TypedDict, total=False):
    estimatedCutoverJobDuration: str

@typing.type_check_only
class CutoverJob(typing_extensions.TypedDict, total=False):
    computeEngineDisksTargetDetails: ComputeEngineDisksTargetDetails
    computeEngineTargetDetails: ComputeEngineTargetDetails
    createTime: str
    endTime: str
    error: Status
    name: str
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
class DataDiskImageImport(typing_extensions.TypedDict, total=False): ...

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
class Disk(typing_extensions.TypedDict, total=False):
    lun: int
    name: str
    sizeGb: int

@typing.type_check_only
class DiskImageDefaults(typing_extensions.TypedDict, total=False):
    sourceImage: str

@typing.type_check_only
class DiskImageTargetDetails(typing_extensions.TypedDict, total=False):
    additionalLicenses: _list[str]
    dataDiskImageImport: DataDiskImageImport
    description: str
    encryption: Encryption
    familyName: str
    imageName: str
    labels: dict[str, typing.Any]
    osAdaptationParameters: ImageImportOsAdaptationParameters
    singleRegionStorage: bool
    targetProject: str

@typing.type_check_only
class DisksMigrationDisksTargetDefaults(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DisksMigrationDisksTargetDetails(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DisksMigrationVmTargetDefaults(typing_extensions.TypedDict, total=False):
    additionalLicenses: _list[str]
    bootDiskDefaults: BootDiskDefaults
    computeScheduling: ComputeScheduling
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    encryption: Encryption
    hostname: str
    labels: dict[str, typing.Any]
    machineType: str
    machineTypeSeries: str
    metadata: dict[str, typing.Any]
    networkInterfaces: _list[NetworkInterface]
    networkTags: _list[str]
    secureBoot: bool
    serviceAccount: str
    vmName: str

@typing.type_check_only
class DisksMigrationVmTargetDetails(typing_extensions.TypedDict, total=False):
    vmUri: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Encryption(typing_extensions.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class FetchInventoryResponse(typing_extensions.TypedDict, total=False):
    awsVms: AwsVmsDetails
    azureVms: AzureVmsDetails
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
    migrationTargetType: typing_extensions.Literal[
        "MIGRATION_TARGET_TYPE_UNSPECIFIED",
        "MIGRATION_TARGET_TYPE_GCE",
        "MIGRATION_TARGET_TYPE_DISKS",
    ]
    name: str
    updateTime: str

@typing.type_check_only
class ImageImport(typing_extensions.TypedDict, total=False):
    cloudStorageUri: str
    createTime: str
    diskImageTargetDefaults: DiskImageTargetDetails
    encryption: Encryption
    machineImageTargetDefaults: MachineImageTargetDetails
    name: str
    recentImageImportJobs: _list[ImageImportJob]

@typing.type_check_only
class ImageImportJob(typing_extensions.TypedDict, total=False):
    cloudStorageUri: str
    createTime: str
    createdResources: _list[str]
    diskImageTargetDetails: DiskImageTargetDetails
    endTime: str
    errors: _list[Status]
    machineImageTargetDetails: MachineImageTargetDetails
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    ]
    steps: _list[ImageImportStep]
    warnings: _list[MigrationWarning]

@typing.type_check_only
class ImageImportOsAdaptationParameters(typing_extensions.TypedDict, total=False):
    generalize: bool
    licenseType: typing_extensions.Literal[
        "COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT",
        "COMPUTE_ENGINE_LICENSE_TYPE_PAYG",
        "COMPUTE_ENGINE_LICENSE_TYPE_BYOL",
    ]

@typing.type_check_only
class ImageImportStep(typing_extensions.TypedDict, total=False):
    adaptingOs: AdaptingOSStep
    creatingImage: CreatingImageStep
    endTime: str
    initializing: InitializingImageImportStep
    loadingSourceFiles: LoadingImageSourceFilesStep
    startTime: str

@typing.type_check_only
class InitializingImageImportStep(typing_extensions.TypedDict, total=False): ...

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
class ListImageImportJobsResponse(typing_extensions.TypedDict, total=False):
    imageImportJobs: _list[ImageImportJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImageImportsResponse(typing_extensions.TypedDict, total=False):
    imageImports: _list[ImageImport]
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
class LoadingImageSourceFilesStep(typing_extensions.TypedDict, total=False): ...

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
class MachineImageParametersOverrides(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class MachineImageTargetDetails(typing_extensions.TypedDict, total=False):
    additionalLicenses: _list[str]
    description: str
    encryption: Encryption
    labels: dict[str, typing.Any]
    machineImageName: str
    machineImageParametersOverrides: MachineImageParametersOverrides
    networkInterfaces: _list[NetworkInterface]
    osAdaptationParameters: ImageImportOsAdaptationParameters
    serviceAccount: ServiceAccount
    shieldedInstanceConfig: ShieldedInstanceConfig
    singleRegionStorage: bool
    skipOsAdaptation: SkipOsAdaptation
    tags: _list[str]
    targetProject: str

@typing.type_check_only
class MigratingVm(typing_extensions.TypedDict, total=False):
    awsSourceVmDetails: AwsSourceVmDetails
    azureSourceVmDetails: AzureSourceVmDetails
    computeEngineDisksTargetDefaults: ComputeEngineDisksTargetDefaults
    computeEngineTargetDefaults: ComputeEngineTargetDefaults
    createTime: str
    currentSyncInfo: ReplicationCycle
    cutoverForecast: CutoverForecast
    description: str
    displayName: str
    error: Status
    group: str
    labels: dict[str, typing.Any]
    lastReplicationCycle: ReplicationCycle
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
    updateTime: str
    vmwareSourceVmDetails: VmwareSourceVmDetails

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
        "IMAGE_IMPORT_ERROR",
    ]
    errorMessage: LocalizedMessage
    errorTime: str
    helpLinks: _list[Link]

@typing.type_check_only
class MigrationWarning(typing_extensions.TypedDict, total=False):
    actionItem: LocalizedMessage
    code: typing_extensions.Literal["WARNING_CODE_UNSPECIFIED", "ADAPTATION_WARNING"]
    helpLinks: _list[Link]
    warningMessage: LocalizedMessage
    warningTime: str

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    externalIp: str
    internalIp: str
    network: str
    networkTier: typing_extensions.Literal[
        "COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED",
        "NETWORK_TIER_STANDARD",
        "NETWORK_TIER_PREMIUM",
    ]
    subnetwork: str

@typing.type_check_only
class OSDescription(typing_extensions.TypedDict, total=False):
    offer: str
    plan: str
    publisher: str
    type: str

@typing.type_check_only
class OSDisk(typing_extensions.TypedDict, total=False):
    name: str
    sizeGb: int
    type: str

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
class PersistentDisk(typing_extensions.TypedDict, total=False):
    diskUri: str
    sourceDiskNumber: int

@typing.type_check_only
class PersistentDiskDefaults(typing_extensions.TypedDict, total=False):
    additionalLabels: dict[str, typing.Any]
    diskName: str
    diskType: typing_extensions.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
    ]
    encryption: Encryption
    sourceDiskNumber: int
    vmAttachmentDetails: VmAttachmentDetails

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
    progressPercent: int
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "FAILED", "SUCCEEDED"
    ]
    steps: _list[CycleStep]
    totalPauseDuration: str
    warnings: _list[MigrationWarning]

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
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    secureBoot: typing_extensions.Literal["SECURE_BOOT_UNSPECIFIED", "TRUE", "FALSE"]

@typing.type_check_only
class ShuttingDownSourceVMStep(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SkipOsAdaptation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    aws: AwsSourceDetails
    azure: AzureSourceDetails
    createTime: str
    description: str
    encryption: Encryption
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
class Tag(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class TargetProject(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    project: str
    updateTime: str

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

@typing.type_check_only
class VmAttachmentDetails(typing_extensions.TypedDict, total=False):
    deviceName: str

@typing.type_check_only
class VmCapabilities(typing_extensions.TypedDict, total=False):
    lastOsCapabilitiesUpdateTime: str
    osCapabilities: _list[
        typing_extensions.Literal[
            "OS_CAPABILITY_UNSPECIFIED",
            "OS_CAPABILITY_NVME_STORAGE_ACCESS",
            "OS_CAPABILITY_GVNIC_NETWORK_INTERFACE",
        ]
    ]

@typing.type_check_only
class VmUtilizationInfo(typing_extensions.TypedDict, total=False):
    utilization: VmUtilizationMetrics
    vmId: str
    vmwareVmDetails: VmwareVmDetails

@typing.type_check_only
class VmUtilizationMetrics(typing_extensions.TypedDict, total=False):
    cpuAveragePercent: int
    cpuMaxPercent: int
    diskIoRateAverageKbps: str
    diskIoRateMaxKbps: str
    memoryAveragePercent: int
    memoryMaxPercent: int
    networkThroughputAverageKbps: str
    networkThroughputMaxKbps: str

@typing.type_check_only
class VmwareDiskDetails(typing_extensions.TypedDict, total=False):
    diskNumber: int
    label: str
    sizeGb: str

@typing.type_check_only
class VmwareSourceDetails(typing_extensions.TypedDict, total=False):
    password: str
    resolvedVcenterHost: str
    thumbprint: str
    username: str
    vcenterIp: str

@typing.type_check_only
class VmwareSourceVmDetails(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    committedStorageBytes: str
    disks: _list[VmwareDiskDetails]
    firmware: typing_extensions.Literal["FIRMWARE_UNSPECIFIED", "EFI", "BIOS"]
    vmCapabilitiesInfo: VmCapabilities

@typing.type_check_only
class VmwareVmDetails(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    bootOption: typing_extensions.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
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
