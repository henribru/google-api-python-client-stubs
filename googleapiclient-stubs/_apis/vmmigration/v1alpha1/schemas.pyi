import typing

_list = list

@typing.type_check_only
class AccessKeyCredentials(typing.TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str

@typing.type_check_only
class AdaptationModifier(typing.TypedDict, total=False):
    modifier: str
    value: str

@typing.type_check_only
class AdaptingOSStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class AddGroupMigrationRequest(typing.TypedDict, total=False):
    migratingVm: str

@typing.type_check_only
class ApplianceVersion(typing.TypedDict, total=False):
    critical: bool
    releaseNotesUri: str
    uri: str
    version: str

@typing.type_check_only
class AppliedLicense(typing.TypedDict, total=False):
    osLicense: str
    type: typing.Literal["TYPE_UNSPECIFIED", "NONE", "PAYG", "BYOL"]

@typing.type_check_only
class AvailableUpdates(typing.TypedDict, total=False):
    inPlaceUpdate: ApplianceVersion
    newDeployableAppliance: ApplianceVersion

@typing.type_check_only
class AwsDiskDetails(typing.TypedDict, total=False):
    diskNumber: int
    sizeGb: str
    volumeId: str

@typing.type_check_only
class AwsSecurityGroup(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class AwsSourceDetails(typing.TypedDict, total=False):
    accessKeyCreds: AccessKeyCredentials
    awsRegion: str
    error: Status
    inventorySecurityGroupNames: _list[str]
    inventoryTagList: _list[Tag]
    migrationResourcesUserTags: dict[str, typing.Any]
    publicIp: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "FAILED", "ACTIVE"]

@typing.type_check_only
class AwsSourceDiskDetails(typing.TypedDict, total=False):
    diskType: typing.Literal[
        "TYPE_UNSPECIFIED", "GP2", "GP3", "IO1", "IO2", "ST1", "SC1", "STANDARD"
    ]
    sizeGib: str
    tags: dict[str, typing.Any]
    volumeId: str

@typing.type_check_only
class AwsSourceVmDetails(typing.TypedDict, total=False):
    architecture: typing.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    committedStorageBytes: str
    disks: _list[AwsDiskDetails]
    firmware: typing.Literal["FIRMWARE_UNSPECIFIED", "EFI", "BIOS"]
    vmCapabilitiesInfo: VmCapabilities

@typing.type_check_only
class AwsVmDetails(typing.TypedDict, total=False):
    architecture: typing.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED", "I386", "X86_64", "ARM64", "X86_64_MAC"
    ]
    bootOption: typing.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    committedStorageMb: str
    cpuCount: int
    diskCount: int
    displayName: str
    instanceType: str
    memoryMb: int
    osDescription: str
    powerState: typing.Literal[
        "POWER_STATE_UNSPECIFIED", "ON", "OFF", "SUSPENDED", "PENDING"
    ]
    securityGroups: _list[AwsSecurityGroup]
    sourceDescription: str
    sourceId: str
    tags: dict[str, typing.Any]
    vcpuCount: int
    virtualizationType: typing.Literal[
        "VM_VIRTUALIZATION_TYPE_UNSPECIFIED", "HVM", "PARAVIRTUAL"
    ]
    vmId: str
    vpcId: str
    zone: str

@typing.type_check_only
class AwsVmsDetails(typing.TypedDict, total=False):
    details: _list[AwsVmDetails]

@typing.type_check_only
class AzureDiskDetails(typing.TypedDict, total=False):
    diskId: str
    diskNumber: int
    sizeGb: str

@typing.type_check_only
class AzureSourceDetails(typing.TypedDict, total=False):
    azureLocation: str
    clientSecretCreds: ClientSecretCredentials
    error: Status
    migrationResourcesUserTags: dict[str, typing.Any]
    resourceGroupId: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "FAILED", "ACTIVE"]
    subscriptionId: str

@typing.type_check_only
class AzureSourceVmDetails(typing.TypedDict, total=False):
    architecture: typing.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    committedStorageBytes: str
    disks: _list[AzureDiskDetails]
    firmware: typing.Literal["FIRMWARE_UNSPECIFIED", "EFI", "BIOS"]
    vmCapabilitiesInfo: VmCapabilities

@typing.type_check_only
class AzureVmDetails(typing.TypedDict, total=False):
    architecture: typing.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    bootOption: typing.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    committedStorageMb: str
    computerName: str
    cpuCount: int
    diskCount: int
    disks: _list[Disk]
    memoryMb: int
    osDescription: OSDescription
    osDisk: OSDisk
    powerState: typing.Literal[
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
class AzureVmsDetails(typing.TypedDict, total=False):
    details: _list[AzureVmDetails]

@typing.type_check_only
class BootDiskDefaults(typing.TypedDict, total=False):
    deviceName: str
    diskName: str
    diskType: typing.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED_HIGH_AVAILABILITY",
    ]
    encryption: Encryption
    image: DiskImageDefaults

@typing.type_check_only
class CancelCloneJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelCutoverJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelDiskMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelImageImportJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClientSecretCredentials(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    tenantId: str

@typing.type_check_only
class CloneJob(typing.TypedDict, total=False):
    computeEngineDisksTargetDetails: ComputeEngineDisksTargetDetails
    computeEngineTargetDetails: ComputeEngineTargetDetails
    computeEngineVmDetails: TargetVMDetails
    createTime: str
    endTime: str
    error: Status
    name: str
    state: typing.Literal[
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
class CloneStep(typing.TypedDict, total=False):
    adaptingOs: AdaptingOSStep
    endTime: str
    instantiatingMigratedVm: InstantiatingMigratedVMStep
    preparingVmDisks: PreparingVMDisksStep
    startTime: str

@typing.type_check_only
class ComputeEngineDisk(typing.TypedDict, total=False):
    diskId: str
    diskType: typing.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED_HIGH_AVAILABILITY",
    ]
    replicaZones: _list[str]
    zone: str

@typing.type_check_only
class ComputeEngineDisksTargetDefaults(typing.TypedDict, total=False):
    disks: _list[PersistentDiskDefaults]
    disksTargetDefaults: DisksMigrationDisksTargetDefaults
    targetProject: str
    vmTargetDefaults: DisksMigrationVmTargetDefaults
    zone: str

@typing.type_check_only
class ComputeEngineDisksTargetDetails(typing.TypedDict, total=False):
    disks: _list[PersistentDisk]
    disksTargetDetails: DisksMigrationDisksTargetDetails
    vmTargetDetails: DisksMigrationVmTargetDetails

@typing.type_check_only
class ComputeEngineTargetDefaults(typing.TypedDict, total=False):
    adaptationModifiers: _list[AdaptationModifier]
    additionalLicenses: _list[str]
    appliedLicense: AppliedLicense
    bootConversion: typing.Literal["BOOT_CONVERSION_UNSPECIFIED", "NONE", "BIOS_TO_EFI"]
    bootOption: typing.Literal[
        "COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED",
        "COMPUTE_ENGINE_BOOT_OPTION_EFI",
        "COMPUTE_ENGINE_BOOT_OPTION_BIOS",
    ]
    computeScheduling: ComputeScheduling
    diskReplicaZones: _list[str]
    diskType: typing.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED_HIGH_AVAILABILITY",
    ]
    disks: _list[PersistentDiskDefaults]
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    encryption: Encryption
    hostname: str
    labels: dict[str, typing.Any]
    licenseType: typing.Literal[
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
    storagePool: str
    targetProject: str
    vmName: str
    zone: str

@typing.type_check_only
class ComputeEngineTargetDetails(typing.TypedDict, total=False):
    adaptationModifiers: _list[AdaptationModifier]
    additionalLicenses: _list[str]
    appliedLicense: AppliedLicense
    bootConversion: typing.Literal["BOOT_CONVERSION_UNSPECIFIED", "NONE", "BIOS_TO_EFI"]
    bootOption: typing.Literal[
        "COMPUTE_ENGINE_BOOT_OPTION_UNSPECIFIED",
        "COMPUTE_ENGINE_BOOT_OPTION_EFI",
        "COMPUTE_ENGINE_BOOT_OPTION_BIOS",
    ]
    computeScheduling: ComputeScheduling
    diskReplicaZones: _list[str]
    diskType: typing.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED_HIGH_AVAILABILITY",
    ]
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    encryption: Encryption
    hostname: str
    labels: dict[str, typing.Any]
    licenseType: typing.Literal[
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
    storagePool: str
    vmName: str
    zone: str

@typing.type_check_only
class ComputeScheduling(typing.TypedDict, total=False):
    automaticRestart: bool
    minNodeCpus: int
    nodeAffinities: _list[SchedulingNodeAffinity]
    onHostMaintenance: typing.Literal[
        "ON_HOST_MAINTENANCE_UNSPECIFIED", "TERMINATE", "MIGRATE"
    ]
    restartType: typing.Literal[
        "RESTART_TYPE_UNSPECIFIED", "AUTOMATIC_RESTART", "NO_AUTOMATIC_RESTART"
    ]

@typing.type_check_only
class CopyingSourceDiskSnapshotStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreatingImageStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreatingSourceDiskSnapshotStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class CutoverForecast(typing.TypedDict, total=False):
    estimatedCutoverJobDuration: str

@typing.type_check_only
class CutoverJob(typing.TypedDict, total=False):
    computeEngineDisksTargetDetails: ComputeEngineDisksTargetDetails
    computeEngineTargetDetails: ComputeEngineTargetDetails
    computeEngineVmDetails: TargetVMDetails
    createTime: str
    endTime: str
    error: Status
    name: str
    progress: int
    progressPercent: int
    state: typing.Literal[
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
class CutoverStep(typing.TypedDict, total=False):
    endTime: str
    finalSync: ReplicationCycle
    instantiatingMigratedVm: InstantiatingMigratedVMStep
    preparingVmDisks: PreparingVMDisksStep
    previousReplicationCycle: ReplicationCycle
    shuttingDownSourceVm: ShuttingDownSourceVMStep
    startTime: str

@typing.type_check_only
class CycleStep(typing.TypedDict, total=False):
    endTime: str
    initializingReplication: InitializingReplicationStep
    postProcessing: PostProcessingStep
    replicating: ReplicatingStep
    startTime: str

@typing.type_check_only
class DataDiskImageImport(typing.TypedDict, total=False):
    guestOsFeatures: _list[str]

@typing.type_check_only
class DatacenterConnector(typing.TypedDict, total=False):
    applianceInfrastructureVersion: str
    applianceSoftwareVersion: str
    availableVersions: AvailableUpdates
    bucket: str
    createTime: str
    error: Status
    name: str
    registrationId: str
    serviceAccount: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "OFFLINE", "FAILED", "ACTIVE"]
    stateTime: str
    updateTime: str
    upgradeStatus: UpgradeStatus
    version: str

@typing.type_check_only
class Disk(typing.TypedDict, total=False):
    lun: int
    name: str
    sizeGb: int

@typing.type_check_only
class DiskImageDefaults(typing.TypedDict, total=False):
    sourceImage: str

@typing.type_check_only
class DiskImageTargetDetails(typing.TypedDict, total=False):
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
class DiskMigrationJob(typing.TypedDict, total=False):
    awsSourceDiskDetails: AwsSourceDiskDetails
    createTime: str
    errors: _list[Status]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "READY",
        "RUNNING",
        "SUCCEEDED",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
    ]
    steps: _list[DiskMigrationStep]
    targetDetails: DiskMigrationJobTargetDetails
    updateTime: str

@typing.type_check_only
class DiskMigrationJobTargetDetails(typing.TypedDict, total=False):
    encryption: Encryption
    labels: dict[str, typing.Any]
    targetDisk: ComputeEngineDisk
    targetProject: str

@typing.type_check_only
class DiskMigrationStep(typing.TypedDict, total=False):
    copyingSourceDiskSnapshot: CopyingSourceDiskSnapshotStep
    creatingSourceDiskSnapshot: CreatingSourceDiskSnapshotStep
    endTime: str
    provisioningTargetDisk: ProvisioningTargetDiskStep
    startTime: str

@typing.type_check_only
class DisksMigrationDisksTargetDefaults(typing.TypedDict, total=False): ...

@typing.type_check_only
class DisksMigrationDisksTargetDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class DisksMigrationVmTargetDefaults(typing.TypedDict, total=False):
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
class DisksMigrationVmTargetDetails(typing.TypedDict, total=False):
    vmUri: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Encryption(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class Expiration(typing.TypedDict, total=False):
    expireTime: str
    extendable: bool
    extensionCount: int

@typing.type_check_only
class ExtendMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchInventoryResponse(typing.TypedDict, total=False):
    awsVms: AwsVmsDetails
    azureVms: AzureVmsDetails
    nextPageToken: str
    updateTime: str
    vmwareVms: VmwareVmsDetails

@typing.type_check_only
class FetchStorageInventoryResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resources: _list[SourceStorageResource]
    updateTime: str

@typing.type_check_only
class FinalizeMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    migrationTargetType: typing.Literal[
        "MIGRATION_TARGET_TYPE_UNSPECIFIED",
        "MIGRATION_TARGET_TYPE_GCE",
        "MIGRATION_TARGET_TYPE_DISKS",
    ]
    name: str
    updateTime: str

@typing.type_check_only
class ImageImport(typing.TypedDict, total=False):
    cloudStorageUri: str
    createTime: str
    diskImageTargetDefaults: DiskImageTargetDetails
    encryption: Encryption
    machineImageTargetDefaults: MachineImageTargetDetails
    name: str
    recentImageImportJobs: _list[ImageImportJob]

@typing.type_check_only
class ImageImportJob(typing.TypedDict, total=False):
    cloudStorageUri: str
    createTime: str
    createdResources: _list[str]
    diskImageTargetDetails: DiskImageTargetDetails
    endTime: str
    errors: _list[Status]
    machineImageTargetDetails: MachineImageTargetDetails
    name: str
    state: typing.Literal[
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
class ImageImportOsAdaptationParameters(typing.TypedDict, total=False):
    adaptationModifiers: _list[AdaptationModifier]
    bootConversion: typing.Literal["BOOT_CONVERSION_UNSPECIFIED", "NONE", "BIOS_TO_EFI"]
    generalize: bool
    licenseType: typing.Literal[
        "COMPUTE_ENGINE_LICENSE_TYPE_DEFAULT",
        "COMPUTE_ENGINE_LICENSE_TYPE_PAYG",
        "COMPUTE_ENGINE_LICENSE_TYPE_BYOL",
    ]

@typing.type_check_only
class ImageImportStep(typing.TypedDict, total=False):
    adaptingOs: AdaptingOSStep
    creatingImage: CreatingImageStep
    endTime: str
    initializing: InitializingImageImportStep
    loadingSourceFiles: LoadingImageSourceFilesStep
    startTime: str

@typing.type_check_only
class InitializingImageImportStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class InitializingReplicationStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class InstantiatingMigratedVMStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class ListCloneJobsResponse(typing.TypedDict, total=False):
    cloneJobs: _list[CloneJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCutoverJobsResponse(typing.TypedDict, total=False):
    cutoverJobs: _list[CutoverJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDatacenterConnectorsResponse(typing.TypedDict, total=False):
    datacenterConnectors: _list[DatacenterConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiskMigrationJobsResponse(typing.TypedDict, total=False):
    diskMigrationJobs: _list[DiskMigrationJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGroupsResponse(typing.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImageImportJobsResponse(typing.TypedDict, total=False):
    imageImportJobs: _list[ImageImportJob]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListImageImportsResponse(typing.TypedDict, total=False):
    imageImports: _list[ImageImport]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMigratingVmsResponse(typing.TypedDict, total=False):
    migratingVms: _list[MigratingVm]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListReplicationCyclesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    replicationCycles: _list[ReplicationCycle]
    unreachable: _list[str]

@typing.type_check_only
class ListSourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sources: _list[Source]
    unreachable: _list[str]

@typing.type_check_only
class ListTargetProjectsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    targetProjects: _list[TargetProject]
    unreachable: _list[str]

@typing.type_check_only
class ListUtilizationReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    utilizationReports: _list[UtilizationReport]

@typing.type_check_only
class LoadingImageSourceFilesStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class LocalizedMessage(typing.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MachineImageParametersOverrides(typing.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class MachineImageTargetDetails(typing.TypedDict, total=False):
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
class MigratingVm(typing.TypedDict, total=False):
    awsSourceVmDetails: AwsSourceVmDetails
    azureSourceVmDetails: AzureSourceVmDetails
    computeEngineDisksTargetDefaults: ComputeEngineDisksTargetDefaults
    computeEngineTargetDefaults: ComputeEngineTargetDefaults
    computeEngineVmDefaults: TargetVMDetails
    createTime: str
    currentSyncInfo: ReplicationCycle
    cutoverForecast: CutoverForecast
    description: str
    displayName: str
    error: Status
    expiration: Expiration
    group: str
    labels: dict[str, typing.Any]
    lastReplicationCycle: ReplicationCycle
    lastSync: ReplicationSync
    name: str
    policy: SchedulePolicy
    recentCloneJobs: _list[CloneJob]
    recentCutoverJobs: _list[CutoverJob]
    sourceVmId: str
    state: typing.Literal[
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
        "EXPIRED",
        "FINALIZED_EXPIRED",
    ]
    stateTime: str
    targetDefaults: TargetVMDetails
    updateTime: str
    vmwareSourceVmDetails: VmwareSourceVmDetails

@typing.type_check_only
class MigrationError(typing.TypedDict, total=False):
    actionItem: LocalizedMessage
    code: typing.Literal[
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
        "DISK_MIGRATION_ERROR",
    ]
    errorMessage: LocalizedMessage
    errorTime: str
    helpLinks: _list[Link]

@typing.type_check_only
class MigrationWarning(typing.TypedDict, total=False):
    actionItem: LocalizedMessage
    code: typing.Literal["WARNING_CODE_UNSPECIFIED", "ADAPTATION_WARNING"]
    helpLinks: _list[Link]
    warningMessage: LocalizedMessage
    warningTime: str

@typing.type_check_only
class NetworkInterface(typing.TypedDict, total=False):
    externalIp: str
    internalIp: str
    network: str
    networkTier: typing.Literal[
        "COMPUTE_ENGINE_NETWORK_TIER_UNSPECIFIED",
        "NETWORK_TIER_STANDARD",
        "NETWORK_TIER_PREMIUM",
    ]
    subnetwork: str

@typing.type_check_only
class OSDescription(typing.TypedDict, total=False):
    offer: str
    plan: str
    publisher: str
    type: str

@typing.type_check_only
class OSDisk(typing.TypedDict, total=False):
    name: str
    sizeGb: int
    type: str

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
class PauseMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class PersistentDisk(typing.TypedDict, total=False):
    diskUri: str
    sourceDiskNumber: int

@typing.type_check_only
class PersistentDiskDefaults(typing.TypedDict, total=False):
    additionalLabels: dict[str, typing.Any]
    diskName: str
    diskType: typing.Literal[
        "COMPUTE_ENGINE_DISK_TYPE_UNSPECIFIED",
        "COMPUTE_ENGINE_DISK_TYPE_STANDARD",
        "COMPUTE_ENGINE_DISK_TYPE_SSD",
        "COMPUTE_ENGINE_DISK_TYPE_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED",
        "COMPUTE_ENGINE_DISK_TYPE_HYPERDISK_BALANCED_HIGH_AVAILABILITY",
    ]
    encryption: Encryption
    sourceDiskNumber: int
    vmAttachmentDetails: VmAttachmentDetails

@typing.type_check_only
class PostProcessingStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class PreparingVMDisksStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class ProvisioningTargetDiskStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveGroupMigrationRequest(typing.TypedDict, total=False):
    migratingVm: str

@typing.type_check_only
class ReplicatingStep(typing.TypedDict, total=False):
    lastThirtyMinutesAverageBytesPerSecond: str
    lastTwoMinutesAverageBytesPerSecond: str
    replicatedBytes: str
    totalBytes: str

@typing.type_check_only
class ReplicationCycle(typing.TypedDict, total=False):
    cycleNumber: int
    endTime: str
    error: Status
    name: str
    progress: int
    progressPercent: int
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "FAILED", "SUCCEEDED"
    ]
    steps: _list[CycleStep]
    totalPauseDuration: str
    warnings: _list[MigrationWarning]

@typing.type_check_only
class ReplicationSync(typing.TypedDict, total=False):
    lastSyncTime: str

@typing.type_check_only
class ResumeMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RunDiskMigrationJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SchedulePolicy(typing.TypedDict, total=False):
    idleDuration: str
    skipOsAdaptation: bool

@typing.type_check_only
class SchedulingNodeAffinity(typing.TypedDict, total=False):
    key: str
    operator: typing.Literal["OPERATOR_UNSPECIFIED", "IN", "NOT_IN"]
    values: _list[str]

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableVtpm: bool
    secureBoot: typing.Literal["SECURE_BOOT_UNSPECIFIED", "TRUE", "FALSE"]

@typing.type_check_only
class ShuttingDownSourceVMStep(typing.TypedDict, total=False): ...

@typing.type_check_only
class SkipOsAdaptation(typing.TypedDict, total=False): ...

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    aws: AwsSourceDetails
    azure: AzureSourceDetails
    createTime: str
    description: str
    encryption: Encryption
    error: Status
    labels: dict[str, typing.Any]
    name: str
    updateTime: str
    vmware: VmwareSourceDetails

@typing.type_check_only
class SourceStorageResource(typing.TypedDict, total=False):
    awsDiskDetails: AwsSourceDiskDetails

@typing.type_check_only
class StartMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class TargetProject(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    project: str
    updateTime: str

@typing.type_check_only
class TargetVMDetails(typing.TypedDict, total=False):
    appliedLicense: AppliedLicense
    bootOption: typing.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    computeScheduling: ComputeScheduling
    diskType: typing.Literal[
        "DISK_TYPE_UNSPECIFIED",
        "STANDARD",
        "BALANCED",
        "SSD",
        "HYPERDISK_BALANCED",
        "HYPERDISK_BALANCED_HIGH_AVAILABILITY",
    ]
    externalIp: str
    internalIp: str
    labels: dict[str, typing.Any]
    licenseType: typing.Literal["DEFAULT", "PAYG", "BYOL"]
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
class UpgradeApplianceRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class UpgradeStatus(typing.TypedDict, total=False):
    error: Status
    previousVersion: str
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "RUNNING", "FAILED", "SUCCEEDED"]
    version: str

@typing.type_check_only
class UtilizationReport(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    error: Status
    frameEndTime: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "SUCCEEDED", "FAILED"]
    stateTime: str
    timeFrame: typing.Literal["TIME_FRAME_UNSPECIFIED", "WEEK", "MONTH", "YEAR"]
    vmCount: int
    vms: _list[VmUtilizationInfo]
    vmsCount: int

@typing.type_check_only
class VmAttachmentDetails(typing.TypedDict, total=False):
    deviceName: str

@typing.type_check_only
class VmCapabilities(typing.TypedDict, total=False):
    lastOsCapabilitiesUpdateTime: str
    osCapabilities: _list[
        typing.Literal[
            "OS_CAPABILITY_UNSPECIFIED",
            "OS_CAPABILITY_NVME_STORAGE_ACCESS",
            "OS_CAPABILITY_GVNIC_NETWORK_INTERFACE",
            "OS_CAPABILITY_IDPF_NETWORK_INTERFACE",
        ]
    ]

@typing.type_check_only
class VmUtilizationInfo(typing.TypedDict, total=False):
    utilization: VmUtilizationMetrics
    vmId: str
    vmwareVmDetails: VmwareVmDetails

@typing.type_check_only
class VmUtilizationMetrics(typing.TypedDict, total=False):
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
class VmwareDiskDetails(typing.TypedDict, total=False):
    diskNumber: int
    label: str
    sizeGb: str

@typing.type_check_only
class VmwareSourceDetails(typing.TypedDict, total=False):
    password: str
    resolvedVcenterHost: str
    thumbprint: str
    username: str
    vcenterIp: str

@typing.type_check_only
class VmwareSourceVmDetails(typing.TypedDict, total=False):
    architecture: typing.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    committedStorageBytes: str
    disks: _list[VmwareDiskDetails]
    firmware: typing.Literal["FIRMWARE_UNSPECIFIED", "EFI", "BIOS"]
    vmCapabilitiesInfo: VmCapabilities

@typing.type_check_only
class VmwareVmDetails(typing.TypedDict, total=False):
    architecture: typing.Literal[
        "VM_ARCHITECTURE_UNSPECIFIED",
        "VM_ARCHITECTURE_X86_FAMILY",
        "VM_ARCHITECTURE_ARM64",
    ]
    bootOption: typing.Literal["BOOT_OPTION_UNSPECIFIED", "EFI", "BIOS"]
    committedStorage: str
    committedStorageMb: str
    cpuCount: int
    datacenterDescription: str
    datacenterId: str
    diskCount: int
    displayName: str
    guestDescription: str
    memoryMb: int
    powerState: typing.Literal["POWER_STATE_UNSPECIFIED", "ON", "OFF", "SUSPENDED"]
    uuid: str
    vmId: str

@typing.type_check_only
class VmwareVmsDetails(typing.TypedDict, total=False):
    details: _list[VmwareVmDetails]
