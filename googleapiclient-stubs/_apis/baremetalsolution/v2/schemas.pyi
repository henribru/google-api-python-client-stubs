import typing

import typing_extensions

_list = list

@typing.type_check_only
class AllowedClient(typing_extensions.TypedDict, total=False):
    allowDev: bool
    allowSuid: bool
    allowedClientsCidr: str
    mountPermissions: typing_extensions.Literal[
        "MOUNT_PERMISSIONS_UNSPECIFIED", "READ", "READ_WRITE"
    ]
    network: str
    noRootSquash: bool
    shareIp: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchInstanceProvisioningSettingsResponse(
    typing_extensions.TypedDict, total=False
):
    images: _list[OSImage]

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    createTime: str
    hyperthreadingEnabled: bool
    id: str
    interactiveSerialConsoleEnabled: bool
    labels: dict[str, typing.Any]
    luns: _list[Lun]
    machineType: str
    name: str
    networks: _list[Network]
    osImage: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "RUNNING", "DELETED"
    ]
    updateTime: str

@typing.type_check_only
class InstanceConfig(typing_extensions.TypedDict, total=False):
    accountNetworksEnabled: bool
    clientNetwork: NetworkAddress
    hyperthreading: bool
    id: str
    instanceType: str
    name: str
    osImage: str
    privateNetwork: NetworkAddress
    userNote: str

@typing.type_check_only
class InstanceQuota(typing_extensions.TypedDict, total=False):
    availableMachineCount: int
    instanceType: str
    location: str
    name: str

@typing.type_check_only
class IntakeVlanAttachment(typing_extensions.TypedDict, total=False):
    id: str
    pairingKey: str

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
class ListLunsResponse(typing_extensions.TypedDict, total=False):
    luns: _list[Lun]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNetworkUsageResponse(typing_extensions.TypedDict, total=False):
    networks: _list[NetworkUsage]

@typing.type_check_only
class ListNetworksResponse(typing_extensions.TypedDict, total=False):
    networks: _list[Network]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNfsSharesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nfsShares: _list[NfsShare]
    unreachable: _list[str]

@typing.type_check_only
class ListProvisioningQuotasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    provisioningQuotas: _list[ProvisioningQuota]

@typing.type_check_only
class ListSnapshotSchedulePoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshotSchedulePolicies: _list[SnapshotSchedulePolicy]

@typing.type_check_only
class ListVolumeSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumeSnapshots: _list[VolumeSnapshot]

@typing.type_check_only
class ListVolumesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumes: _list[Volume]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogicalInterface(typing_extensions.TypedDict, total=False):
    name: str
    required: bool
    type: typing_extensions.Literal["INTERFACE_TYPE_UNSPECIFIED", "BOND", "NIC"]

@typing.type_check_only
class Lun(typing_extensions.TypedDict, total=False):
    bootLun: bool
    id: str
    multiprotocolType: typing_extensions.Literal[
        "MULTIPROTOCOL_TYPE_UNSPECIFIED", "LINUX"
    ]
    name: str
    shareable: bool
    sizeGb: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "UPDATING", "READY", "DELETING"
    ]
    storageType: typing_extensions.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]
    storageVolume: str
    wwid: str

@typing.type_check_only
class LunRange(typing_extensions.TypedDict, total=False):
    quantity: int
    sizeGb: int

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    cidr: str
    id: str
    ipAddress: str
    labels: dict[str, typing.Any]
    macAddress: _list[str]
    name: str
    servicesCidr: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PROVISIONING", "PROVISIONED"]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]
    vlanId: str
    vrf: VRF

@typing.type_check_only
class NetworkAddress(typing_extensions.TypedDict, total=False):
    address: str
    existingNetworkId: str
    networkId: str

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    bandwidth: typing_extensions.Literal[
        "BANDWIDTH_UNSPECIFIED", "BW_1_GBPS", "BW_2_GBPS", "BW_5_GBPS", "BW_10_GBPS"
    ]
    cidr: str
    gcpService: str
    id: str
    name: str
    serviceCidr: typing_extensions.Literal[
        "SERVICE_CIDR_UNSPECIFIED", "DISABLED", "HIGH_26", "HIGH_27", "HIGH_28"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]
    userNote: str
    vlanAttachments: _list[IntakeVlanAttachment]
    vlanSameProject: bool

@typing.type_check_only
class NetworkUsage(typing_extensions.TypedDict, total=False):
    network: Network
    usedIps: _list[str]

@typing.type_check_only
class NfsExport(typing_extensions.TypedDict, total=False):
    allowDev: bool
    allowSuid: bool
    cidr: str
    machineId: str
    networkId: str
    noRootSquash: bool
    permissions: typing_extensions.Literal[
        "PERMISSIONS_UNSPECIFIED", "READ_ONLY", "READ_WRITE"
    ]

@typing.type_check_only
class NfsShare(typing_extensions.TypedDict, total=False):
    allowedClients: _list[AllowedClient]
    labels: dict[str, typing.Any]
    name: str
    nfsShareId: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PROVISIONED"]
    volume: str

@typing.type_check_only
class OSImage(typing_extensions.TypedDict, total=False):
    applicableInstanceTypes: _list[str]
    code: str
    description: str
    name: str
    supportedNetworkTemplates: _list[ServerNetworkTemplate]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class ProvisioningConfig(typing_extensions.TypedDict, total=False):
    cloudConsoleUri: str
    email: str
    handoverServiceAccount: str
    instances: _list[InstanceConfig]
    location: str
    name: str
    networks: _list[NetworkConfig]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "DRAFT",
        "SUBMITTED",
        "PROVISIONING",
        "PROVISIONED",
        "VALIDATED",
        "CANCELLED",
    ]
    ticketId: str
    updateTime: str
    volumes: _list[VolumeConfig]

@typing.type_check_only
class ProvisioningQuota(typing_extensions.TypedDict, total=False):
    assetType: typing_extensions.Literal[
        "ASSET_TYPE_UNSPECIFIED",
        "ASSET_TYPE_SERVER",
        "ASSET_TYPE_STORAGE",
        "ASSET_TYPE_NETWORK",
    ]
    availableCount: int
    gcpService: str
    instanceQuota: InstanceQuota
    location: str
    name: str
    networkBandwidth: str
    serverCount: str
    storageGib: str

@typing.type_check_only
class QosPolicy(typing_extensions.TypedDict, total=False):
    bandwidthGbps: float

@typing.type_check_only
class ResetInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestoreVolumeSnapshotRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    crontabSpec: str
    prefix: str
    retentionCount: int

@typing.type_check_only
class ServerNetworkTemplate(typing_extensions.TypedDict, total=False):
    applicableInstanceTypes: _list[str]
    logicalInterfaces: _list[LogicalInterface]
    name: str

@typing.type_check_only
class SnapshotReservationDetail(typing_extensions.TypedDict, total=False):
    reservedSpaceGib: str
    reservedSpacePercent: int
    reservedSpaceRemainingGib: str
    reservedSpaceUsedPercent: int

@typing.type_check_only
class SnapshotSchedulePolicy(typing_extensions.TypedDict, total=False):
    description: str
    id: str
    labels: dict[str, typing.Any]
    name: str
    schedules: _list[Schedule]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PROVISIONED"]

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
class SubmitProvisioningConfigRequest(typing_extensions.TypedDict, total=False):
    email: str
    provisioningConfig: ProvisioningConfig

@typing.type_check_only
class SubmitProvisioningConfigResponse(typing_extensions.TypedDict, total=False):
    provisioningConfig: ProvisioningConfig

@typing.type_check_only
class VRF(typing_extensions.TypedDict, total=False):
    name: str
    qosPolicy: QosPolicy
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PROVISIONING", "PROVISIONED"]
    vlanAttachments: _list[VlanAttachment]

@typing.type_check_only
class VlanAttachment(typing_extensions.TypedDict, total=False):
    peerIp: str
    peerVlanId: str
    routerIp: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    autoGrownSizeGib: str
    currentSizeGib: str
    emergencySizeGib: str
    id: str
    labels: dict[str, typing.Any]
    name: str
    remainingSpaceGib: str
    requestedSizeGib: str
    snapshotAutoDeleteBehavior: typing_extensions.Literal[
        "SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED",
        "DISABLED",
        "OLDEST_FIRST",
        "NEWEST_FIRST",
    ]
    snapshotEnabled: bool
    snapshotReservationDetail: SnapshotReservationDetail
    snapshotSchedulePolicy: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING"
    ]
    storageType: typing_extensions.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]

@typing.type_check_only
class VolumeConfig(typing_extensions.TypedDict, total=False):
    gcpService: str
    id: str
    lunRanges: _list[LunRange]
    machineIds: _list[str]
    name: str
    nfsExports: _list[NfsExport]
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "PROTOCOL_FC", "PROTOCOL_NFS"
    ]
    sizeGb: int
    snapshotsEnabled: bool
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "FLASH", "DISK"]
    userNote: str

@typing.type_check_only
class VolumeSnapshot(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    id: str
    name: str
    sizeBytes: str
    storageVolume: str
