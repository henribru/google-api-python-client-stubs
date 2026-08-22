import typing

_list = list

@typing.type_check_only
class AllowedClient(typing.TypedDict, total=False):
    allowDev: bool
    allowSuid: bool
    allowedClientsCidr: str
    mountPermissions: typing.Literal[
        "MOUNT_PERMISSIONS_UNSPECIFIED", "READ", "READ_WRITE"
    ]
    network: str
    nfsPath: str
    noRootSquash: bool
    shareIp: str

@typing.type_check_only
class DetachLunRequest(typing.TypedDict, total=False):
    lun: str
    skipReboot: bool

@typing.type_check_only
class DisableHyperthreadingRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DisableInteractiveSerialConsoleRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DisableInteractiveSerialConsoleResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableHyperthreadingRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableInteractiveSerialConsoleRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableInteractiveSerialConsoleResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class EvictLunRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class EvictVolumeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudBaremetalsolutionV2LogicalInterface(typing.TypedDict, total=False):
    interfaceIndex: int
    logicalNetworkInterfaces: _list[LogicalNetworkInterface]
    name: str

@typing.type_check_only
class GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface(
    typing.TypedDict, total=False
):
    name: str
    required: bool
    type: typing.Literal["INTERFACE_TYPE_UNSPECIFIED", "BOND", "NIC"]

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    createTime: str
    firmwareVersion: str
    hyperthreadingEnabled: bool
    id: str
    interactiveSerialConsoleEnabled: bool
    kmsKeyVersion: str
    labels: dict[str, typing.Any]
    logicalInterfaces: _list[GoogleCloudBaremetalsolutionV2LogicalInterface]
    loginInfo: str
    luns: _list[Lun]
    machineType: str
    name: str
    networkTemplate: str
    networks: _list[Network]
    osImage: str
    pod: str
    sshKeys: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "DELETED",
        "UPDATING",
        "STARTING",
        "STOPPING",
        "SHUTDOWN",
    ]
    updateTime: str
    volumes: _list[Volume]
    workloadProfile: typing.Literal[
        "WORKLOAD_PROFILE_UNSPECIFIED",
        "WORKLOAD_PROFILE_GENERIC",
        "WORKLOAD_PROFILE_HANA",
    ]

@typing.type_check_only
class InstanceConfig(typing.TypedDict, total=False):
    accountNetworksEnabled: bool
    clientNetwork: NetworkAddress
    hyperthreading: bool
    id: str
    instanceType: str
    kmsKeyVersion: str
    logicalInterfaces: _list[GoogleCloudBaremetalsolutionV2LogicalInterface]
    name: str
    networkConfig: typing.Literal[
        "NETWORKCONFIG_UNSPECIFIED", "SINGLE_VLAN", "MULTI_VLAN"
    ]
    networkTemplate: str
    osImage: str
    privateNetwork: NetworkAddress
    sshKeyNames: _list[str]
    userNote: str

@typing.type_check_only
class InstanceQuota(typing.TypedDict, total=False):
    availableMachineCount: int
    gcpService: str
    instanceType: str
    location: str
    name: str

@typing.type_check_only
class IntakeVlanAttachment(typing.TypedDict, total=False):
    id: str
    pairingKey: str

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
class ListLunsResponse(typing.TypedDict, total=False):
    luns: _list[Lun]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNetworkUsageResponse(typing.TypedDict, total=False):
    networks: _list[NetworkUsage]

@typing.type_check_only
class ListNetworksResponse(typing.TypedDict, total=False):
    networks: _list[Network]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNfsSharesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nfsShares: _list[NfsShare]
    unreachable: _list[str]

@typing.type_check_only
class ListOSImagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    osImages: _list[OSImage]

@typing.type_check_only
class ListProvisioningQuotasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    provisioningQuotas: _list[ProvisioningQuota]

@typing.type_check_only
class ListSSHKeysResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sshKeys: _list[SSHKey]

@typing.type_check_only
class ListVolumeSnapshotsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumeSnapshots: _list[VolumeSnapshot]

@typing.type_check_only
class ListVolumesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    volumes: _list[Volume]

@typing.type_check_only
class LoadInstanceAuthInfoResponse(typing.TypedDict, total=False):
    sshKeys: _list[SSHKey]
    userAccounts: dict[str, typing.Any]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogicalNetworkInterface(typing.TypedDict, total=False):
    defaultGateway: bool
    id: str
    ipAddress: str
    network: str
    networkType: typing.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]

@typing.type_check_only
class Lun(typing.TypedDict, total=False):
    bootLun: bool
    expireTime: str
    id: str
    instances: _list[str]
    multiprotocolType: typing.Literal["MULTIPROTOCOL_TYPE_UNSPECIFIED", "LINUX"]
    name: str
    shareable: bool
    sizeGb: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "UPDATING", "READY", "DELETING", "COOL_OFF"
    ]
    storageType: typing.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]
    storageVolume: str
    wwid: str

@typing.type_check_only
class LunRange(typing.TypedDict, total=False):
    quantity: int
    sizeGb: int

@typing.type_check_only
class Network(typing.TypedDict, total=False):
    cidr: str
    gatewayIp: str
    id: str
    ipAddress: str
    jumboFramesEnabled: bool
    labels: dict[str, typing.Any]
    macAddress: _list[str]
    mountPoints: _list[NetworkMountPoint]
    name: str
    pod: str
    reservations: _list[NetworkAddressReservation]
    servicesCidr: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "PROVISIONED", "DEPROVISIONING", "UPDATING"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]
    vlanId: str
    vrf: VRF
    vrfAttachment: str

@typing.type_check_only
class NetworkAddress(typing.TypedDict, total=False):
    address: str
    existingNetworkId: str
    networkId: str

@typing.type_check_only
class NetworkAddressReservation(typing.TypedDict, total=False):
    endAddress: str
    note: str
    startAddress: str

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    bandwidth: typing.Literal[
        "BANDWIDTH_UNSPECIFIED", "BW_1_GBPS", "BW_2_GBPS", "BW_5_GBPS", "BW_10_GBPS"
    ]
    cidr: str
    gcpService: str
    id: str
    jumboFramesEnabled: bool
    name: str
    serviceCidr: typing.Literal[
        "SERVICE_CIDR_UNSPECIFIED", "DISABLED", "HIGH_26", "HIGH_27", "HIGH_28"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]
    userNote: str
    vlanAttachments: _list[IntakeVlanAttachment]
    vlanSameProject: bool
    vrf: str

@typing.type_check_only
class NetworkMountPoint(typing.TypedDict, total=False):
    defaultGateway: bool
    instance: str
    ipAddress: str
    logicalInterface: str

@typing.type_check_only
class NetworkUsage(typing.TypedDict, total=False):
    network: Network
    usedIps: _list[str]

@typing.type_check_only
class NfsExport(typing.TypedDict, total=False):
    allowDev: bool
    allowSuid: bool
    cidr: str
    machineId: str
    networkId: str
    noRootSquash: bool
    permissions: typing.Literal["PERMISSIONS_UNSPECIFIED", "READ_ONLY", "READ_WRITE"]

@typing.type_check_only
class NfsShare(typing.TypedDict, total=False):
    allowedClients: _list[AllowedClient]
    id: str
    labels: dict[str, typing.Any]
    name: str
    nfsShareId: str
    pod: str
    requestedSizeGib: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PROVISIONED", "CREATING", "UPDATING", "DELETING"
    ]
    storageType: typing.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]
    volume: str

@typing.type_check_only
class OSImage(typing.TypedDict, total=False):
    applicableInstanceTypes: _list[str]
    code: str
    description: str
    name: str
    supportedNetworkTemplates: _list[str]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class ProvisioningConfig(typing.TypedDict, total=False):
    cloudConsoleUri: str
    customId: str
    email: str
    handoverServiceAccount: str
    instances: _list[InstanceConfig]
    location: str
    name: str
    networks: _list[NetworkConfig]
    pod: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "DRAFT",
        "SUBMITTED",
        "PROVISIONING",
        "PROVISIONED",
        "VALIDATED",
        "CANCELLED",
        "FAILED",
    ]
    statusMessage: str
    ticketId: str
    updateTime: str
    volumes: _list[VolumeConfig]
    vpcScEnabled: bool

@typing.type_check_only
class ProvisioningQuota(typing.TypedDict, total=False):
    assetType: typing.Literal[
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
class QosPolicy(typing.TypedDict, total=False):
    bandwidthGbps: float

@typing.type_check_only
class ReimageInstanceRequest(typing.TypedDict, total=False):
    kmsKeyVersion: str
    osImage: str
    sshKeys: _list[str]

@typing.type_check_only
class RenameInstanceRequest(typing.TypedDict, total=False):
    newInstanceId: str

@typing.type_check_only
class RenameNetworkRequest(typing.TypedDict, total=False):
    newNetworkId: str

@typing.type_check_only
class RenameNfsShareRequest(typing.TypedDict, total=False):
    newNfsshareId: str

@typing.type_check_only
class RenameVolumeRequest(typing.TypedDict, total=False):
    newVolumeId: str

@typing.type_check_only
class ResetInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResetInstanceResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResizeVolumeRequest(typing.TypedDict, total=False):
    sizeGib: str

@typing.type_check_only
class RestoreVolumeSnapshotRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SSHKey(typing.TypedDict, total=False):
    name: str
    publicKey: str

@typing.type_check_only
class ServerNetworkTemplate(typing.TypedDict, total=False):
    applicableInstanceTypes: _list[str]
    logicalInterfaces: _list[
        GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterface
    ]
    name: str

@typing.type_check_only
class SnapshotReservationDetail(typing.TypedDict, total=False):
    reservedSpaceGib: str
    reservedSpacePercent: int
    reservedSpaceRemainingGib: str
    reservedSpaceUsedPercent: int

@typing.type_check_only
class StartInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StartInstanceResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StopInstanceResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SubmitProvisioningConfigRequest(typing.TypedDict, total=False):
    email: str
    provisioningConfig: ProvisioningConfig

@typing.type_check_only
class SubmitProvisioningConfigResponse(typing.TypedDict, total=False):
    provisioningConfig: ProvisioningConfig

@typing.type_check_only
class UserAccount(typing.TypedDict, total=False):
    encryptedPassword: str
    kmsKeyVersion: str

@typing.type_check_only
class VRF(typing.TypedDict, total=False):
    name: str
    qosPolicy: QosPolicy
    state: typing.Literal["STATE_UNSPECIFIED", "PROVISIONING", "PROVISIONED"]
    vlanAttachments: _list[VlanAttachment]

@typing.type_check_only
class VlanAttachment(typing.TypedDict, total=False):
    id: str
    interconnectAttachment: str
    pairingKey: str
    peerIp: str
    peerVlanId: str
    qosPolicy: QosPolicy
    routerIp: str

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    attached: bool
    autoGrownSizeGib: str
    bootVolume: bool
    currentSizeGib: str
    emergencySizeGib: str
    expireTime: str
    id: str
    instances: _list[str]
    labels: dict[str, typing.Any]
    maxSizeGib: str
    name: str
    notes: str
    originallyRequestedSizeGib: str
    performanceTier: typing.Literal[
        "VOLUME_PERFORMANCE_TIER_UNSPECIFIED",
        "VOLUME_PERFORMANCE_TIER_SHARED",
        "VOLUME_PERFORMANCE_TIER_ASSIGNED",
        "VOLUME_PERFORMANCE_TIER_HT",
        "VOLUME_PERFORMANCE_TIER_QOS2_PERFORMANCE",
    ]
    pod: str
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "FIBRE_CHANNEL", "NFS"]
    remainingSpaceGib: str
    requestedSizeGib: str
    snapshotAutoDeleteBehavior: typing.Literal[
        "SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED",
        "DISABLED",
        "OLDEST_FIRST",
        "NEWEST_FIRST",
    ]
    snapshotEnabled: bool
    snapshotReservationDetail: SnapshotReservationDetail
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING", "COOL_OFF"
    ]
    storageType: typing.Literal["STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"]
    workloadProfile: typing.Literal["WORKLOAD_PROFILE_UNSPECIFIED", "GENERIC", "HANA"]

@typing.type_check_only
class VolumeConfig(typing.TypedDict, total=False):
    gcpService: str
    id: str
    lunRanges: _list[LunRange]
    machineIds: _list[str]
    name: str
    nfsExports: _list[NfsExport]
    performanceTier: typing.Literal[
        "VOLUME_PERFORMANCE_TIER_UNSPECIFIED",
        "VOLUME_PERFORMANCE_TIER_SHARED",
        "VOLUME_PERFORMANCE_TIER_ASSIGNED",
        "VOLUME_PERFORMANCE_TIER_HT",
        "VOLUME_PERFORMANCE_TIER_QOS2_PERFORMANCE",
    ]
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "PROTOCOL_FC", "PROTOCOL_NFS"]
    sizeGb: int
    snapshotsEnabled: bool
    type: typing.Literal["TYPE_UNSPECIFIED", "FLASH", "DISK"]
    userNote: str

@typing.type_check_only
class VolumeSnapshot(typing.TypedDict, total=False):
    createTime: str
    description: str
    id: str
    name: str
    storageVolume: str
    type: typing.Literal["SNAPSHOT_TYPE_UNSPECIFIED", "AD_HOC", "SCHEDULED"]
