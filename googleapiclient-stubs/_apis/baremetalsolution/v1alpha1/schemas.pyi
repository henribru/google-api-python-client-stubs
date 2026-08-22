import typing

_list = list

@typing.type_check_only
class InstanceConfig(typing.TypedDict, total=False):
    clientNetwork: NetworkAddress
    hyperthreading: bool
    id: str
    instanceType: str
    location: str
    osImage: str
    privateNetwork: NetworkAddress
    userNote: str

@typing.type_check_only
class InstanceQuota(typing.TypedDict, total=False):
    availableMachineCount: int
    instanceType: str
    location: str

@typing.type_check_only
class ListProvisioningQuotasResponse(typing.TypedDict, total=False):
    nextPageToken: str
    provisioningQuotas: _list[ProvisioningQuota]

@typing.type_check_only
class LunRange(typing.TypedDict, total=False):
    quantity: int
    sizeGb: int

@typing.type_check_only
class NetworkAddress(typing.TypedDict, total=False):
    address: str
    existingNetworkId: str
    networkId: str

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    bandwidth: typing.Literal[
        "BANDWIDTH_UNSPECIFIED", "BW_1_GBPS", "BW_2_GBPS", "BW_5_GBPS", "BW_10_GBPS"
    ]
    cidr: str
    id: str
    location: str
    serviceCidr: typing.Literal[
        "SERVICE_CIDR_UNSPECIFIED", "DISABLED", "HIGH_26", "HIGH_27", "HIGH_28"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "CLIENT", "PRIVATE"]
    userNote: str
    vlanAttachments: _list[VlanAttachment]

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
class ProvisioningConfig(typing.TypedDict, total=False):
    instances: _list[InstanceConfig]
    networks: _list[NetworkConfig]
    ticketId: str
    volumes: _list[VolumeConfig]

@typing.type_check_only
class ProvisioningQuota(typing.TypedDict, total=False):
    instanceQuota: InstanceQuota

@typing.type_check_only
class SubmitProvisioningConfigRequest(typing.TypedDict, total=False):
    email: str
    provisioningConfig: ProvisioningConfig

@typing.type_check_only
class VlanAttachment(typing.TypedDict, total=False):
    id: str
    pairingKey: str

@typing.type_check_only
class VolumeConfig(typing.TypedDict, total=False):
    id: str
    location: str
    lunRanges: _list[LunRange]
    machineIds: _list[str]
    nfsExports: _list[NfsExport]
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "PROTOCOL_FC", "PROTOCOL_NFS"]
    sizeGb: int
    snapshotsEnabled: bool
    type: typing.Literal["TYPE_UNSPECIFIED", "FLASH", "DISK"]
    userNote: str
