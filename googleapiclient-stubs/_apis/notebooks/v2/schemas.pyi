import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    coreCount: str
    type: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_A100_80GB",
        "NVIDIA_L4",
        "NVIDIA_H100_80GB",
        "NVIDIA_H100_MEGA_80GB",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
    ]

@typing.type_check_only
class AccessConfig(typing_extensions.TypedDict, total=False):
    externalIp: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BootDisk(typing_extensions.TypedDict, total=False):
    diskEncryption: typing_extensions.Literal[
        "DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"
    ]
    diskSizeGb: str
    diskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    kmsKey: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckInstanceUpgradabilityResponse(typing_extensions.TypedDict, total=False):
    upgradeImage: str
    upgradeInfo: str
    upgradeVersion: str
    upgradeable: bool

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    availableImages: _list[ImageRelease]
    defaultValues: DefaultValues
    supportedValues: SupportedValues

@typing.type_check_only
class ContainerImage(typing_extensions.TypedDict, total=False):
    repository: str
    tag: str

@typing.type_check_only
class DataDisk(typing_extensions.TypedDict, total=False):
    diskEncryption: typing_extensions.Literal[
        "DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"
    ]
    diskSizeGb: str
    diskType: typing_extensions.Literal[
        "DISK_TYPE_UNSPECIFIED", "PD_STANDARD", "PD_SSD", "PD_BALANCED", "PD_EXTREME"
    ]
    kmsKey: str

@typing.type_check_only
class DefaultValues(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class DiagnoseInstanceRequest(typing_extensions.TypedDict, total=False):
    diagnosticConfig: DiagnosticConfig
    timeoutMinutes: int

@typing.type_check_only
class DiagnosticConfig(typing_extensions.TypedDict, total=False):
    enableCopyHomeFilesFlag: bool
    enablePacketCaptureFlag: bool
    enableRepairFlag: bool
    gcsBucket: str
    relativePath: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    reportTime: str
    type: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "IDLE",
        "HEARTBEAT",
        "HEALTH",
        "MAINTENANCE",
        "METADATA_CHANGE",
    ]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GPUDriverConfig(typing_extensions.TypedDict, total=False):
    customGpuDriverPath: str
    enableGpuDriver: bool

@typing.type_check_only
class GceSetup(typing_extensions.TypedDict, total=False):
    acceleratorConfigs: _list[AcceleratorConfig]
    bootDisk: BootDisk
    containerImage: ContainerImage
    dataDisks: _list[DataDisk]
    disablePublicIp: bool
    enableIpForwarding: bool
    gpuDriverConfig: GPUDriverConfig
    machineType: str
    metadata: dict[str, typing.Any]
    minCpuPlatform: str
    networkInterfaces: _list[NetworkInterface]
    serviceAccounts: _list[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    tags: _list[str]
    vmImage: VmImage

@typing.type_check_only
class ImageRelease(typing_extensions.TypedDict, total=False):
    imageName: str
    releaseName: str

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    disableProxyAccess: bool
    enableThirdPartyIdentity: bool
    gceSetup: GceSetup
    healthInfo: dict[str, typing.Any]
    healthState: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED",
        "HEALTHY",
        "UNHEALTHY",
        "AGENT_NOT_INSTALLED",
        "AGENT_NOT_RUNNING",
    ]
    id: str
    instanceOwners: _list[str]
    labels: dict[str, typing.Any]
    name: str
    proxyUri: str
    satisfiesPzi: bool
    satisfiesPzs: bool
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
        "SUSPENDING",
        "SUSPENDED",
    ]
    thirdPartyProxyUrl: str
    updateTime: str
    upgradeHistory: _list[UpgradeHistoryEntry]

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
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    accessConfigs: _list[AccessConfig]
    network: str
    nicType: typing_extensions.Literal["NIC_TYPE_UNSPECIFIED", "VIRTIO_NET", "GVNIC"]
    subnet: str

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
class ReportInstanceInfoSystemRequest(typing_extensions.TypedDict, total=False):
    event: Event
    vmId: str

@typing.type_check_only
class ResetInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResizeDiskRequest(typing_extensions.TypedDict, total=False):
    bootDisk: BootDisk
    dataDisk: DataDisk

@typing.type_check_only
class RestoreInstanceRequest(typing_extensions.TypedDict, total=False):
    snapshot: Snapshot

@typing.type_check_only
class RollbackInstanceRequest(typing_extensions.TypedDict, total=False):
    revisionId: str
    targetSnapshot: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    projectId: str
    snapshotId: str

@typing.type_check_only
class StartInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SupportedValues(typing_extensions.TypedDict, total=False):
    acceleratorTypes: _list[str]
    machineTypes: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

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
    targetVersion: str
    version: str
    vmImage: str

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UpgradeInstanceSystemRequest(typing_extensions.TypedDict, total=False):
    vmId: str

@typing.type_check_only
class VmImage(typing_extensions.TypedDict, total=False):
    family: str
    name: str
    project: str
