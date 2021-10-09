import typing

import typing_extensions

_list = list

@typing.type_check_only
class DisableInteractiveSerialConsoleRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class DisableInteractiveSerialConsoleResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableInteractiveSerialConsoleRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class EnableInteractiveSerialConsoleResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    hyperthreadingEnabled: bool
    luns: _list[Lun]
    name: str
    scheduledPowerResetTime: str
    sshEnabled: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "RESERVED",
        "PROVISIONING",
        "PROVISIONED",
        "DEPROVISIONING",
        "DEPROVISIONED",
        "UPDATING",
    ]

@typing.type_check_only
class InstanceConfig(typing_extensions.TypedDict, total=False):
    clientNetwork: NetworkAddress
    hyperthreading: bool
    id: str
    instanceType: str
    location: str
    osImage: str
    privateNetwork: NetworkAddress

@typing.type_check_only
class InstanceQuota(typing_extensions.TypedDict, total=False):
    availableMachineCount: int
    instanceType: str
    location: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str

@typing.type_check_only
class ListLunsResponse(typing_extensions.TypedDict, total=False):
    luns: _list[Lun]
    nextPageToken: str

@typing.type_check_only
class ListProvisioningQuotasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    provisioningQuotas: _list[ProvisioningQuota]

@typing.type_check_only
class ListSSHKeysResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sshKeys: _list[SSHKey]

@typing.type_check_only
class ListSnapshotSchedulePoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshotSchedulePolicies: _list[SnapshotSchedulePolicy]

@typing.type_check_only
class ListVolumeSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    volumeSnapshots: _list[VolumeSnapshot]

@typing.type_check_only
class ListVolumesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    volumes: _list[Volume]

@typing.type_check_only
class Lun(typing_extensions.TypedDict, total=False):
    isBoot: bool
    multiprotocolType: str
    name: str
    remoteVolume: Volume
    shareable: bool
    sizeGb: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "RESERVED",
        "PROVISIONING",
        "PROVISIONED",
        "DEPROVISIONING",
        "DEPROVISIONED",
        "UPDATING",
    ]

@typing.type_check_only
class LunRange(typing_extensions.TypedDict, total=False):
    quantity: int
    sizeGb: int

@typing.type_check_only
class NetworkAddress(typing_extensions.TypedDict, total=False):
    address: str
    networkId: str

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    bandwidth: typing_extensions.Literal[
        "BANDWIDTH_UNSPECIFIED", "BW_1_GBPS", "BW_2_GBPS", "BW_5_GBPS", "BW_10_GBPS"
    ]
    cidr: str
    id: str
    location: str
    serviceCidr: typing_extensions.Literal[
        "SERVICE_CIDR_UNSPECIFIED", "DISABLED", "HIGH_26", "HIGH_27", "HIGH_28"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]
    vlanAttachments: _list[VlanAttachment]

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
class ProvisioningConfig(typing_extensions.TypedDict, total=False):
    instances: _list[InstanceConfig]
    networks: _list[NetworkConfig]
    ticketId: str
    volumes: _list[VolumeConfig]

@typing.type_check_only
class ProvisioningQuota(typing_extensions.TypedDict, total=False):
    instanceQuota: InstanceQuota

@typing.type_check_only
class ResetInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResetInstanceResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestoreVolumeSnapshotRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SSHKey(typing_extensions.TypedDict, total=False):
    name: str
    publicKey: str

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    crontabSpec: str
    prefix: str
    retentionCount: int

@typing.type_check_only
class SerialPortOutput(typing_extensions.TypedDict, total=False):
    contents: str
    nextStartByte: str
    start: str

@typing.type_check_only
class SetVolumeSnapshotSchedulePolicyRequest(typing_extensions.TypedDict, total=False):
    snapshotSchedulePolicy: str

@typing.type_check_only
class SetVolumeSnapshotSchedulePolicyResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class SnapshotSchedulePolicy(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    schedules: _list[Schedule]
    volumes: _list[str]

@typing.type_check_only
class SubmitProvisioningConfigRequest(typing_extensions.TypedDict, total=False):
    provisioningConfig: ProvisioningConfig

@typing.type_check_only
class VlanAttachment(typing_extensions.TypedDict, total=False):
    id: str
    pairingKey: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    autoGrownSizeGb: str
    currentSizeGb: str
    name: str
    remainingSpaceGb: str
    requestedSizeGb: str
    snapshotReservedSpacePercent: int
    snapshotReservedSpaceRemainingGb: str
    snapshotReservedSpaceUsedPercent: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONED",
        "DEPROVISIONING_REQUESTED",
        "DEPROVISIONING_COOLOFF",
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "FLASH", "DISK"]

@typing.type_check_only
class VolumeConfig(typing_extensions.TypedDict, total=False):
    id: str
    location: str
    lunRanges: _list[LunRange]
    machineIds: _list[str]
    nfsExports: _list[NfsExport]
    protocol: typing_extensions.Literal[
        "PROTOCOL_UNSPECIFIED", "PROTOCOL_FC", "PROTOCOL_NFS"
    ]
    sizeGb: int
    snapshotsEnabled: bool
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "FLASH", "DISK"]

@typing.type_check_only
class VolumeSnapshot(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    sizeBytes: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE"]
