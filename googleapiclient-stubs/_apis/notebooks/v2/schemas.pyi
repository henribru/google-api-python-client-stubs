import typing

_list = list

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    coreCount: str
    type: typing.Literal[
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
        "NVIDIA_H200_141GB",
        "NVIDIA_TESLA_T4_VWS",
        "NVIDIA_TESLA_P100_VWS",
        "NVIDIA_TESLA_P4_VWS",
        "NVIDIA_B200",
        "NVIDIA_RTX6000",
    ]

@typing.type_check_only
class AccessConfig(typing.TypedDict, total=False):
    externalIp: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BootDisk(typing.TypedDict, total=False):
    diskEncryption: typing.Literal["DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"]
    diskSizeGb: str
    diskType: typing.Literal[
        "DISK_TYPE_UNSPECIFIED",
        "PD_STANDARD",
        "PD_SSD",
        "PD_BALANCED",
        "PD_EXTREME",
        "HYPERDISK_BALANCED",
        "HYPERDISK_EXTREME",
        "HYPERDISK_THROUGHPUT",
        "HYPERDISK_BALANCED_HIGH_AVAILABILITY",
        "HYPERDISK_ML",
    ]
    kmsKey: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckAuthorizationRequest(typing.TypedDict, total=False):
    authorizationDetails: dict[str, typing.Any]

@typing.type_check_only
class CheckAuthorizationResponse(typing.TypedDict, total=False):
    createTime: str
    oauth_uri: str
    success: bool

@typing.type_check_only
class CheckInstanceUpgradabilityResponse(typing.TypedDict, total=False):
    upgradeImage: str
    upgradeInfo: str
    upgradeVersion: str
    upgradeable: bool

@typing.type_check_only
class ConfidentialInstanceConfig(typing.TypedDict, total=False):
    confidentialInstanceType: typing.Literal[
        "CONFIDENTIAL_INSTANCE_TYPE_UNSPECIFIED", "SEV"
    ]

@typing.type_check_only
class Config(typing.TypedDict, total=False):
    availableImages: _list[ImageRelease]
    defaultValues: DefaultValues
    disableWorkbenchLegacyCreation: bool
    supportedValues: SupportedValues

@typing.type_check_only
class ContainerImage(typing.TypedDict, total=False):
    repository: str
    tag: str

@typing.type_check_only
class DataDisk(typing.TypedDict, total=False):
    diskEncryption: typing.Literal["DISK_ENCRYPTION_UNSPECIFIED", "GMEK", "CMEK"]
    diskSizeGb: str
    diskType: typing.Literal[
        "DISK_TYPE_UNSPECIFIED",
        "PD_STANDARD",
        "PD_SSD",
        "PD_BALANCED",
        "PD_EXTREME",
        "HYPERDISK_BALANCED",
        "HYPERDISK_EXTREME",
        "HYPERDISK_THROUGHPUT",
        "HYPERDISK_BALANCED_HIGH_AVAILABILITY",
        "HYPERDISK_ML",
    ]
    kmsKey: str
    resourcePolicies: _list[str]

@typing.type_check_only
class DefaultValues(typing.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class DiagnoseInstanceRequest(typing.TypedDict, total=False):
    diagnosticConfig: DiagnosticConfig
    timeoutMinutes: int

@typing.type_check_only
class DiagnosticConfig(typing.TypedDict, total=False):
    enableCopyHomeFilesFlag: bool
    enablePacketCaptureFlag: bool
    enableRepairFlag: bool
    gcsBucket: str
    relativePath: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing.TypedDict, total=False):
    details: dict[str, typing.Any]
    reportTime: str
    type: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "IDLE",
        "HEARTBEAT",
        "HEALTH",
        "MAINTENANCE",
        "METADATA_CHANGE",
    ]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GPUDriverConfig(typing.TypedDict, total=False):
    customGpuDriverPath: str
    enableGpuDriver: bool

@typing.type_check_only
class GceSetup(typing.TypedDict, total=False):
    acceleratorConfigs: _list[AcceleratorConfig]
    bootDisk: BootDisk
    confidentialInstanceConfig: ConfidentialInstanceConfig
    containerImage: ContainerImage
    dataDisks: _list[DataDisk]
    disablePublicIp: bool
    enableIpForwarding: bool
    gpuDriverConfig: GPUDriverConfig
    instanceId: str
    machineType: str
    metadata: dict[str, typing.Any]
    minCpuPlatform: str
    networkInterfaces: _list[NetworkInterface]
    reservationAffinity: ReservationAffinity
    serviceAccounts: _list[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    tags: _list[str]
    vmImage: VmImage

@typing.type_check_only
class GenerateAccessTokenRequest(typing.TypedDict, total=False):
    vmToken: str

@typing.type_check_only
class GenerateAccessTokenResponse(typing.TypedDict, total=False):
    access_token: str
    expires_in: int
    scope: str
    token_type: str

@typing.type_check_only
class ImageRelease(typing.TypedDict, total=False):
    description: str
    imageFamily: str
    imageName: str
    releaseName: str

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    createTime: str
    creator: str
    disableProxyAccess: bool
    enableDeletionProtection: bool
    enableManagedEuc: bool
    enableThirdPartyIdentity: bool
    gceSetup: GceSetup
    healthInfo: dict[str, typing.Any]
    healthState: typing.Literal[
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
        "SUSPENDING",
        "SUSPENDED",
    ]
    thirdPartyProxyUrl: str
    updateTime: str
    upgradeHistory: _list[UpgradeHistoryEntry]

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
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NetworkInterface(typing.TypedDict, total=False):
    accessConfigs: _list[AccessConfig]
    network: str
    nicType: typing.Literal["NIC_TYPE_UNSPECIFIED", "VIRTIO_NET", "GVNIC"]
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
class ReportInstanceInfoSystemRequest(typing.TypedDict, total=False):
    event: Event
    vmId: str

@typing.type_check_only
class ReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "RESERVATION_UNSPECIFIED",
        "RESERVATION_NONE",
        "RESERVATION_ANY",
        "RESERVATION_SPECIFIC",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResetInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResizeDiskRequest(typing.TypedDict, total=False):
    bootDisk: BootDisk
    dataDisk: DataDisk

@typing.type_check_only
class RestoreInstanceRequest(typing.TypedDict, total=False):
    snapshot: Snapshot

@typing.type_check_only
class RollbackInstanceRequest(typing.TypedDict, total=False):
    revisionId: str
    targetSnapshot: str

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class Snapshot(typing.TypedDict, total=False):
    projectId: str
    snapshotId: str

@typing.type_check_only
class StartInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SupportedValues(typing.TypedDict, total=False):
    acceleratorTypes: _list[str]
    machineTypes: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpgradeHistoryEntry(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "UPGRADE", "ROLLBACK"]
    containerImage: str
    createTime: str
    framework: str
    snapshot: str
    state: typing.Literal["STATE_UNSPECIFIED", "STARTED", "SUCCEEDED", "FAILED"]
    targetVersion: str
    version: str
    vmImage: str

@typing.type_check_only
class UpgradeInstanceRequest(typing.TypedDict, total=False):
    imageFamily: str

@typing.type_check_only
class UpgradeInstanceSystemRequest(typing.TypedDict, total=False):
    vmId: str

@typing.type_check_only
class VmImage(typing.TypedDict, total=False):
    family: str
    name: str
    project: str
