import typing

import typing_extensions
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
    members: typing.List[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ContainerImage(typing_extensions.TypedDict, total=False):
    repository: str
    tag: str

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskSizeGb: str
    guestOsFeatures: typing.List[GuestOsFeature]
    index: str
    interface: str
    kind: str
    licenses: typing.List[str]
    mode: str
    source: str
    type: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

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
class Execution(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    executionTemplate: ExecutionTemplate
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
    ]
    updateTime: str

@typing.type_check_only
class ExecutionTemplate(typing_extensions.TypedDict, total=False):
    acceleratorConfig: SchedulerAcceleratorConfig
    containerImageUri: str
    inputNotebookFile: str
    labels: typing.Dict[str, typing.Any]
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

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetInstanceHealthResponse(typing_extensions.TypedDict, total=False):
    healthInfo: typing.Dict[str, typing.Any]
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
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED"
    ]
    containerImage: ContainerImage
    createTime: str
    customGpuDriverPath: str
    dataDiskSizeGb: str
    dataDiskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED"
    ]
    diskEncryption: typing_extensions.Literal[
        "DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"
    ]
    disks: typing.List[Disk]
    installGpuDriver: bool
    instanceOwners: typing.List[str]
    kmsKey: str
    labels: typing.Dict[str, typing.Any]
    machineType: str
    metadata: typing.Dict[str, typing.Any]
    name: str
    network: str
    noProxyAccess: bool
    noPublicIp: bool
    noRemoveDataDisk: bool
    postStartupScript: str
    proxyUri: str
    serviceAccount: str
    serviceAccountScopes: typing.List[str]
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
    ]
    subnet: str
    tags: typing.List[str]
    updateTime: str
    upgradeHistory: typing.List[UpgradeHistoryEntry]
    vmImage: VmImage

@typing.type_check_only
class IsInstanceUpgradeableResponse(typing_extensions.TypedDict, total=False):
    upgradeInfo: str
    upgradeVersion: str
    upgradeable: bool

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: typing.List[Environment]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: typing.List[Execution]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListSchedulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    schedules: typing.List[Schedule]
    unreachable: typing.List[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class RegisterInstanceRequest(typing_extensions.TypedDict, total=False):
    instanceId: str

@typing.type_check_only
class ReportInstanceInfoRequest(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    vmId: str

@typing.type_check_only
class ResetInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    createTime: str
    cronSchedule: str
    description: str
    displayName: str
    executionTemplate: ExecutionTemplate
    name: str
    recentExecutions: typing.List[Execution]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "PAUSED", "DISABLED", "UPDATE_FAILED"
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
    labels: typing.Dict[str, typing.Any]

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TriggerScheduleRequest(typing_extensions.TypedDict, total=False): ...

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
    vmId: str

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class VmImage(typing_extensions.TypedDict, total=False):
    imageFamily: str
    imageName: str
    project: str
