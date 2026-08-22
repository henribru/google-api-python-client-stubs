import typing

_list = list

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    coreCount: str
    type: typing.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_L4",
        "NVIDIA_A100_80GB",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
        "NVIDIA_H100_80GB",
        "NVIDIA_H100_MEGA_80GB",
        "TPU_V2",
        "TPU_V3",
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BootImage(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ContainerImage(typing.TypedDict, total=False):
    repository: str
    tag: str

@typing.type_check_only
class DataprocParameters(typing.TypedDict, total=False):
    cluster: str

@typing.type_check_only
class DiagnoseInstanceRequest(typing.TypedDict, total=False):
    diagnosticConfig: DiagnosticConfig
    timeoutMinutes: int

@typing.type_check_only
class DiagnoseRuntimeRequest(typing.TypedDict, total=False):
    diagnosticConfig: DiagnosticConfig
    timeoutMinutes: int

@typing.type_check_only
class DiagnosticConfig(typing.TypedDict, total=False):
    copyHomeFilesFlagEnabled: bool
    gcsBucket: str
    packetCaptureFlagEnabled: bool
    relativePath: str
    repairFlagEnabled: bool

@typing.type_check_only
class Disk(typing.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskSizeGb: str
    guestOsFeatures: _list[GuestOsFeature]
    index: str
    interface: str
    kind: str
    licenses: _list[str]
    mode: str
    source: str
    type: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    containerImage: ContainerImage
    createTime: str
    description: str
    displayName: str
    name: str
    postStartupScript: str
    vmImage: VmImage

@typing.type_check_only
class Event(typing.TypedDict, total=False):
    details: dict[str, typing.Any]
    reportTime: str
    type: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED", "IDLE", "HEARTBEAT", "HEALTH", "MAINTENANCE"
    ]

@typing.type_check_only
class Execution(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    executionTemplate: ExecutionTemplate
    jobUri: str
    name: str
    outputNotebookFile: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PREPARING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
        "EXPIRED",
        "INITIALIZING",
    ]
    updateTime: str

@typing.type_check_only
class ExecutionTemplate(typing.TypedDict, total=False):
    acceleratorConfig: SchedulerAcceleratorConfig
    containerImageUri: str
    dataprocParameters: DataprocParameters
    inputNotebookFile: str
    jobType: typing.Literal["JOB_TYPE_UNSPECIFIED", "VERTEX_AI", "DATAPROC"]
    kernelSpec: str
    labels: dict[str, typing.Any]
    masterType: str
    outputNotebookFolder: str
    parameters: str
    paramsYamlFile: str
    scaleTier: typing.Literal[
        "SCALE_TIER_UNSPECIFIED",
        "BASIC",
        "STANDARD_1",
        "PREMIUM_1",
        "BASIC_GPU",
        "BASIC_TPU",
        "CUSTOM",
    ]
    serviceAccount: str
    tensorboard: str
    vertexAiParameters: VertexAIParameters

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetInstanceHealthResponse(typing.TypedDict, total=False):
    healthInfo: dict[str, typing.Any]
    healthState: typing.Literal[
        "HEALTH_STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "AGENT_NOT_INSTALLED",
        "AGENT_NOT_RUNNING",
    ]

@typing.type_check_only
class GuestOsFeature(typing.TypedDict, total=False):
    type: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    acceleratorConfig: AcceleratorConfig
    bootDiskSizeGb: str
    bootDiskType: typing.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    canIpForward: bool
    containerImage: ContainerImage
    createTime: str
    creator: str
    customGpuDriverPath: str
    dataDiskSizeGb: str
    dataDiskType: typing.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    diskEncryption: typing.Literal["DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"]
    disks: _list[Disk]
    installGpuDriver: bool
    instanceMigrationEligibility: InstanceMigrationEligibility
    instanceOwners: _list[str]
    kmsKey: str
    labels: dict[str, typing.Any]
    machineType: str
    metadata: dict[str, typing.Any]
    migrated: bool
    name: str
    network: str
    nicType: typing.Literal["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"]
    noProxyAccess: bool
    noPublicIp: bool
    noRemoveDataDisk: bool
    postStartupScript: str
    proxyUri: str
    reservationAffinity: ReservationAffinity
    serviceAccount: str
    serviceAccountScopes: _list[str]
    shieldedInstanceConfig: ShieldedInstanceConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "PROVISIONING",
        "ACTIVE",
        "STOPPING",
        "STOPPED",
        "DELETED",
        "UPGRADING",
        "INITIALIZING",
        "REGISTERING",
        "SUSPENDING",
        "SUSPENDED",
    ]
    subnet: str
    tags: _list[str]
    updateTime: str
    upgradeHistory: _list[UpgradeHistoryEntry]
    vmImage: VmImage

@typing.type_check_only
class InstanceConfig(typing.TypedDict, total=False):
    enableHealthMonitoring: bool
    notebookUpgradeSchedule: str

@typing.type_check_only
class InstanceMigrationEligibility(typing.TypedDict, total=False):
    errors: _list[typing.Literal["ERROR_UNSPECIFIED", "DATAPROC_HUB"]]
    warnings: _list[
        typing.Literal[
            "WARNING_UNSPECIFIED",
            "UNSUPPORTED_MACHINE_TYPE",
            "UNSUPPORTED_ACCELERATOR_TYPE",
            "UNSUPPORTED_OS",
            "NO_REMOVE_DATA_DISK",
            "GCS_BACKUP",
            "POST_STARTUP_SCRIPT",
        ]
    ]

@typing.type_check_only
class IsInstanceUpgradeableResponse(typing.TypedDict, total=False):
    upgradeImage: str
    upgradeInfo: str
    upgradeVersion: str
    upgradeable: bool

@typing.type_check_only
class ListEnvironmentsResponse(typing.TypedDict, total=False):
    environments: _list[Environment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExecutionsResponse(typing.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
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
class ListRuntimesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    runtimes: _list[Runtime]
    unreachable: _list[str]

@typing.type_check_only
class ListSchedulesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    schedules: _list[Schedule]
    unreachable: _list[str]

@typing.type_check_only
class LocalDisk(typing.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    guestOsFeatures: _list[RuntimeGuestOsFeature]
    index: int
    initializeParams: LocalDiskInitializeParams
    interface: str
    kind: str
    licenses: _list[str]
    mode: str
    source: str
    type: str

@typing.type_check_only
class LocalDiskInitializeParams(typing.TypedDict, total=False):
    description: str
    diskName: str
    diskSizeGb: str
    diskType: typing.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    labels: dict[str, typing.Any]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MigrateInstanceRequest(typing.TypedDict, total=False):
    postStartupScriptOption: typing.Literal[
        "POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED",
        "POST_STARTUP_SCRIPT_OPTION_SKIP",
        "POST_STARTUP_SCRIPT_OPTION_RERUN",
    ]

@typing.type_check_only
class MigrateRuntimeRequest(typing.TypedDict, total=False):
    network: str
    postStartupScriptOption: typing.Literal[
        "POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED",
        "POST_STARTUP_SCRIPT_OPTION_SKIP",
        "POST_STARTUP_SCRIPT_OPTION_RERUN",
    ]
    requestId: str
    serviceAccount: str
    subnet: str

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
    endpoint: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RefreshRuntimeTokenInternalRequest(typing.TypedDict, total=False):
    vmId: str

@typing.type_check_only
class RefreshRuntimeTokenInternalResponse(typing.TypedDict, total=False):
    accessToken: str
    expireTime: str

@typing.type_check_only
class RegisterInstanceRequest(typing.TypedDict, total=False):
    instanceId: str

@typing.type_check_only
class ReportInstanceEventRequest(typing.TypedDict, total=False):
    event: Event
    vmId: str

@typing.type_check_only
class ReportInstanceInfoRequest(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    vmId: str

@typing.type_check_only
class ReportRuntimeEventRequest(typing.TypedDict, total=False):
    event: Event
    vmId: str

@typing.type_check_only
class ReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResetInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResetRuntimeRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RollbackInstanceRequest(typing.TypedDict, total=False):
    targetSnapshot: str

@typing.type_check_only
class Runtime(typing.TypedDict, total=False):
    accessConfig: RuntimeAccessConfig
    createTime: str
    healthState: typing.Literal[
        "HEALTH_STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "AGENT_NOT_INSTALLED",
        "AGENT_NOT_RUNNING",
    ]
    labels: dict[str, typing.Any]
    metrics: RuntimeMetrics
    migrated: bool
    name: str
    runtimeMigrationEligibility: RuntimeMigrationEligibility
    softwareConfig: RuntimeSoftwareConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "STARTING",
        "PROVISIONING",
        "ACTIVE",
        "STOPPING",
        "STOPPED",
        "DELETING",
        "UPGRADING",
        "INITIALIZING",
    ]
    updateTime: str
    virtualMachine: VirtualMachine

@typing.type_check_only
class RuntimeAcceleratorConfig(typing.TypedDict, total=False):
    coreCount: str
    type: typing.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_L4",
        "TPU_V2",
        "TPU_V3",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
    ]

@typing.type_check_only
class RuntimeAccessConfig(typing.TypedDict, total=False):
    accessType: typing.Literal[
        "RUNTIME_ACCESS_TYPE_UNSPECIFIED", "SINGLE_USER", "SERVICE_ACCOUNT"
    ]
    proxyUri: str
    runtimeOwner: str

@typing.type_check_only
class RuntimeGuestOsFeature(typing.TypedDict, total=False):
    type: str

@typing.type_check_only
class RuntimeMetrics(typing.TypedDict, total=False):
    systemMetrics: dict[str, typing.Any]

@typing.type_check_only
class RuntimeMigrationEligibility(typing.TypedDict, total=False):
    errors: _list[typing.Literal["ERROR_UNSPECIFIED", "CUSTOM_CONTAINER"]]
    warnings: _list[
        typing.Literal[
            "WARNING_UNSPECIFIED",
            "UNSUPPORTED_ACCELERATOR_TYPE",
            "UNSUPPORTED_OS",
            "RESERVED_IP_RANGE",
            "GOOGLE_MANAGED_NETWORK",
            "POST_STARTUP_SCRIPT",
            "SINGLE_USER",
        ]
    ]

@typing.type_check_only
class RuntimeShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class RuntimeSoftwareConfig(typing.TypedDict, total=False):
    customGpuDriverPath: str
    disableTerminal: bool
    enableHealthMonitoring: bool
    idleShutdown: bool
    idleShutdownTimeout: int
    installGpuDriver: bool
    kernels: _list[ContainerImage]
    mixerDisabled: bool
    notebookUpgradeSchedule: str
    postStartupScript: str
    postStartupScriptBehavior: typing.Literal[
        "POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED",
        "RUN_EVERY_START",
        "DOWNLOAD_AND_RUN_EVERY_START",
    ]
    upgradeable: bool
    version: str

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    createTime: str
    cronSchedule: str
    description: str
    displayName: str
    executionTemplate: ExecutionTemplate
    name: str
    recentExecutions: _list[Execution]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ENABLED",
        "PAUSED",
        "DISABLED",
        "UPDATE_FAILED",
        "INITIALIZING",
        "DELETING",
    ]
    timeZone: str
    updateTime: str

@typing.type_check_only
class SchedulerAcceleratorConfig(typing.TypedDict, total=False):
    coreCount: str
    type: typing.Literal[
        "SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "TPU_V2",
        "TPU_V3",
    ]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class SetInstanceAcceleratorRequest(typing.TypedDict, total=False):
    coreCount: str
    type: typing.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_L4",
        "NVIDIA_A100_80GB",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
        "NVIDIA_H100_80GB",
        "NVIDIA_H100_MEGA_80GB",
        "TPU_V2",
        "TPU_V3",
    ]

@typing.type_check_only
class SetInstanceLabelsRequest(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class SetInstanceMachineTypeRequest(typing.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class StartInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StartRuntimeRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StopRuntimeRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class SwitchRuntimeRequest(typing.TypedDict, total=False):
    acceleratorConfig: RuntimeAcceleratorConfig
    machineType: str
    requestId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TriggerScheduleRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateInstanceConfigRequest(typing.TypedDict, total=False):
    config: InstanceConfig

@typing.type_check_only
class UpdateInstanceMetadataItemsRequest(typing.TypedDict, total=False):
    items: dict[str, typing.Any]

@typing.type_check_only
class UpdateInstanceMetadataItemsResponse(typing.TypedDict, total=False):
    items: dict[str, typing.Any]

@typing.type_check_only
class UpdateShieldedInstanceConfigRequest(typing.TypedDict, total=False):
    shieldedInstanceConfig: ShieldedInstanceConfig

@typing.type_check_only
class UpgradeHistoryEntry(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "UPGRADE", "ROLLBACK"]
    containerImage: str
    createTime: str
    framework: str
    snapshot: str
    state: typing.Literal["STATE_UNSPECIFIED", "STARTED", "SUCCEEDED", "FAILED"]
    targetImage: str
    targetVersion: str
    version: str
    vmImage: str

@typing.type_check_only
class UpgradeInstanceInternalRequest(typing.TypedDict, total=False):
    type: typing.Literal[
        "UPGRADE_TYPE_UNSPECIFIED",
        "UPGRADE_FRAMEWORK",
        "UPGRADE_OS",
        "UPGRADE_CUDA",
        "UPGRADE_ALL",
    ]
    vmId: str

@typing.type_check_only
class UpgradeInstanceRequest(typing.TypedDict, total=False):
    type: typing.Literal[
        "UPGRADE_TYPE_UNSPECIFIED",
        "UPGRADE_FRAMEWORK",
        "UPGRADE_OS",
        "UPGRADE_CUDA",
        "UPGRADE_ALL",
    ]

@typing.type_check_only
class UpgradeRuntimeRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class VertexAIParameters(typing.TypedDict, total=False):
    env: dict[str, typing.Any]
    network: str

@typing.type_check_only
class VirtualMachine(typing.TypedDict, total=False):
    instanceId: str
    instanceName: str
    virtualMachineConfig: VirtualMachineConfig

@typing.type_check_only
class VirtualMachineConfig(typing.TypedDict, total=False):
    acceleratorConfig: RuntimeAcceleratorConfig
    bootImage: BootImage
    containerImages: _list[ContainerImage]
    dataDisk: LocalDisk
    encryptionConfig: EncryptionConfig
    guestAttributes: dict[str, typing.Any]
    internalIpOnly: bool
    labels: dict[str, typing.Any]
    machineType: str
    metadata: dict[str, typing.Any]
    network: str
    nicType: typing.Literal["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"]
    reservedIpRange: str
    shieldedInstanceConfig: RuntimeShieldedInstanceConfig
    subnet: str
    tags: _list[str]
    zone: str

@typing.type_check_only
class VmImage(typing.TypedDict, total=False):
    imageFamily: str
    imageName: str
    project: str
