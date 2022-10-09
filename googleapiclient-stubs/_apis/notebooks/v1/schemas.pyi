import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    coreCount: str
    type: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
        "TPU_V2",
        "TPU_V3",
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BootImage(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ContainerImage(typing_extensions.TypedDict, total=False):
    repository: str
    tag: str

@typing.type_check_only
class DataprocParameters(typing_extensions.TypedDict, total=False):
    cluster: str

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing_extensions.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    containerImage: ContainerImage
    createTime: str
    description: str
    displayName: str
    name: str
    postStartupScript: str
    vmImage: VmImage

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    reportTime: str
    type: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED", "IDLE", "HEARTBEAT", "HEALTH", "MAINTENANCE"
    ]

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    executionTemplate: ExecutionTemplate
    jobUri: str
    name: str
    outputNotebookFile: str
    state: typing_extensions.Literal[
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
class ExecutionTemplate(typing_extensions.TypedDict, total=False):
    acceleratorConfig: SchedulerAcceleratorConfig
    containerImageUri: str
    dataprocParameters: DataprocParameters
    inputNotebookFile: str
    jobType: typing_extensions.Literal["JOB_TYPE_UNSPECIFIED", "VERTEX_AI", "DATAPROC"]
    kernelSpec: str
    labels: dict[str, typing.Any]
    masterType: str
    outputNotebookFolder: str
    parameters: str
    paramsYamlFile: str
    scaleTier: typing_extensions.Literal[
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
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetInstanceHealthResponse(typing_extensions.TypedDict, total=False):
    healthInfo: dict[str, typing.Any]
    healthState: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "AGENT_NOT_INSTALLED",
        "AGENT_NOT_RUNNING",
    ]

@typing.type_check_only
class GuestOsFeature(typing_extensions.TypedDict, total=False):
    type: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    acceleratorConfig: AcceleratorConfig
    bootDiskSizeGb: str
    bootDiskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    canIpForward: bool
    containerImage: ContainerImage
    createTime: str
    creator: str
    customGpuDriverPath: str
    dataDiskSizeGb: str
    dataDiskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    diskEncryption: typing_extensions.Literal[
        "DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"
    ]
    disks: _list[Disk]
    installGpuDriver: bool
    instanceOwners: _list[str]
    kmsKey: str
    labels: dict[str, typing.Any]
    machineType: str
    metadata: dict[str, typing.Any]
    name: str
    network: str
    nicType: typing_extensions.Literal["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"]
    noProxyAccess: bool
    noPublicIp: bool
    noRemoveDataDisk: bool
    postStartupScript: str
    proxyUri: str
    reservationAffinity: ReservationAffinity
    serviceAccount: str
    serviceAccountScopes: _list[str]
    shieldedInstanceConfig: ShieldedInstanceConfig
    state: typing_extensions.Literal[
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
class InstanceConfig(typing_extensions.TypedDict, total=False):
    enableHealthMonitoring: bool
    notebookUpgradeSchedule: str

@typing.type_check_only
class IsInstanceUpgradeableResponse(typing_extensions.TypedDict, total=False):
    upgradeImage: str
    upgradeInfo: str
    upgradeVersion: str
    upgradeable: bool

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: _list[Environment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: _list[Execution]
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
class ListRuntimesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    runtimes: _list[Runtime]
    unreachable: _list[str]

@typing.type_check_only
class ListSchedulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    schedules: _list[Schedule]
    unreachable: _list[str]

@typing.type_check_only
class LocalDisk(typing_extensions.TypedDict, total=False):
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
class LocalDiskInitializeParams(typing_extensions.TypedDict, total=False):
    description: str
    diskName: str
    diskSizeGb: str
    diskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    labels: dict[str, typing.Any]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
    endpoint: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RefreshRuntimeTokenInternalRequest(typing_extensions.TypedDict, total=False):
    vmId: str

@typing.type_check_only
class RefreshRuntimeTokenInternalResponse(typing_extensions.TypedDict, total=False):
    accessToken: str
    expireTime: str

@typing.type_check_only
class RegisterInstanceRequest(typing_extensions.TypedDict, total=False):
    instanceId: str

@typing.type_check_only
class ReportInstanceInfoRequest(typing_extensions.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    vmId: str

@typing.type_check_only
class ReportRuntimeEventRequest(typing_extensions.TypedDict, total=False):
    event: Event
    vmId: str

@typing.type_check_only
class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResetInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResetRuntimeRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RollbackInstanceRequest(typing_extensions.TypedDict, total=False):
    targetSnapshot: str

@typing.type_check_only
class Runtime(typing_extensions.TypedDict, total=False):
    accessConfig: RuntimeAccessConfig
    createTime: str
    healthState: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "AGENT_NOT_INSTALLED",
        "AGENT_NOT_RUNNING",
    ]
    metrics: RuntimeMetrics
    name: str
    softwareConfig: RuntimeSoftwareConfig
    state: typing_extensions.Literal[
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
class RuntimeAcceleratorConfig(typing_extensions.TypedDict, total=False):
    coreCount: str
    type: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "TPU_V2",
        "TPU_V3",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
    ]

@typing.type_check_only
class RuntimeAccessConfig(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal[
        "RUNTIME_ACCESS_TYPE_UNSPECIFIED", "SINGLE_USER", "SERVICE_ACCOUNT"
    ]
    proxyUri: str
    runtimeOwner: str

@typing.type_check_only
class RuntimeGuestOsFeature(typing_extensions.TypedDict, total=False):
    type: str

@typing.type_check_only
class RuntimeMetrics(typing_extensions.TypedDict, total=False):
    systemMetrics: dict[str, typing.Any]

@typing.type_check_only
class RuntimeShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class RuntimeSoftwareConfig(typing_extensions.TypedDict, total=False):
    customGpuDriverPath: str
    disableTerminal: bool
    enableHealthMonitoring: bool
    idleShutdown: bool
    idleShutdownTimeout: int
    installGpuDriver: bool
    kernels: _list[ContainerImage]
    notebookUpgradeSchedule: str
    postStartupScript: str
    postStartupScriptBehavior: typing_extensions.Literal[
        "POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED",
        "RUN_EVERY_START",
        "DOWNLOAD_AND_RUN_EVERY_START",
    ]
    upgradeable: bool

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    createTime: str
    cronSchedule: str
    description: str
    displayName: str
    executionTemplate: ExecutionTemplate
    name: str
    recentExecutions: _list[Execution]
    state: typing_extensions.Literal[
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
class SchedulerAcceleratorConfig(typing_extensions.TypedDict, total=False):
    coreCount: str
    type: typing_extensions.Literal[
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
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class SetInstanceAcceleratorRequest(typing_extensions.TypedDict, total=False):
    coreCount: str
    type: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
        "TPU_V2",
        "TPU_V3",
    ]

@typing.type_check_only
class SetInstanceLabelsRequest(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class SetInstanceMachineTypeRequest(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class StartInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StartRuntimeRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StopRuntimeRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class SwitchRuntimeRequest(typing_extensions.TypedDict, total=False):
    acceleratorConfig: RuntimeAcceleratorConfig
    machineType: str
    requestId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TriggerScheduleRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpdateInstanceConfigRequest(typing_extensions.TypedDict, total=False):
    config: InstanceConfig

@typing.type_check_only
class UpdateInstanceMetadataItemsRequest(typing_extensions.TypedDict, total=False):
    items: dict[str, typing.Any]

@typing.type_check_only
class UpdateInstanceMetadataItemsResponse(typing_extensions.TypedDict, total=False):
    items: dict[str, typing.Any]

@typing.type_check_only
class UpdateShieldedInstanceConfigRequest(typing_extensions.TypedDict, total=False):
    shieldedInstanceConfig: ShieldedInstanceConfig

@typing.type_check_only
class UpgradeHistoryEntry(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "UPGRADE", "ROLLBACK"]
    containerImage: str
    createTime: str
    framework: str
    snapshot: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STARTED", "SUCCEEDED", "FAILED"
    ]
    targetImage: str
    targetVersion: str
    version: str
    vmImage: str

@typing.type_check_only
class UpgradeInstanceInternalRequest(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UPGRADE_TYPE_UNSPECIFIED",
        "UPGRADE_FRAMEWORK",
        "UPGRADE_OS",
        "UPGRADE_CUDA",
        "UPGRADE_ALL",
    ]
    vmId: str

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UPGRADE_TYPE_UNSPECIFIED",
        "UPGRADE_FRAMEWORK",
        "UPGRADE_OS",
        "UPGRADE_CUDA",
        "UPGRADE_ALL",
    ]

@typing.type_check_only
class VertexAIParameters(typing_extensions.TypedDict, total=False):
    env: dict[str, typing.Any]
    network: str

@typing.type_check_only
class VirtualMachine(typing_extensions.TypedDict, total=False):
    instanceId: str
    instanceName: str
    virtualMachineConfig: VirtualMachineConfig

@typing.type_check_only
class VirtualMachineConfig(typing_extensions.TypedDict, total=False):
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
    nicType: typing_extensions.Literal["UNSPECIFIED_NIC_TYPE", "VIRTIO_NET", "GVNIC"]
    reservedIpRange: str
    shieldedInstanceConfig: RuntimeShieldedInstanceConfig
    subnet: str
    tags: _list[str]
    zone: str

@typing.type_check_only
class VmImage(typing_extensions.TypedDict, total=False):
    imageFamily: str
    imageName: str
    project: str
