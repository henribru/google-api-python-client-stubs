import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    createTime: str
    management: bool
    name: str
    nodeTypeConfigs: dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "UPDATING", "DELETING", "REPAIRING"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class Credentials(typing_extensions.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Hcx(typing_extensions.TypedDict, total=False):
    fqdn: str
    internalIp: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING"]
    version: str

@typing.type_check_only
class HcxActivationKey(typing_extensions.TypedDict, total=False):
    activationKey: str
    createTime: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "AVAILABLE", "CONSUMED", "CREATING"
    ]
    uid: str

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListHcxActivationKeysResponse(typing_extensions.TypedDict, total=False):
    hcxActivationKeys: _list[HcxActivationKey]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNetworkPoliciesResponse(typing_extensions.TypedDict, total=False):
    networkPolicies: _list[NetworkPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNodeTypesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodeTypes: _list[NodeType]
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListPrivateCloudsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    privateClouds: _list[PrivateCloud]
    unreachable: _list[str]

@typing.type_check_only
class ListPrivateConnectionPeeringRoutesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    peeringRoutes: _list[PeeringRoute]

@typing.type_check_only
class ListPrivateConnectionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    privateConnections: _list[PrivateConnection]
    unreachable: _list[str]

@typing.type_check_only
class ListSubnetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subnets: _list[Subnet]
    unreachable: _list[str]

@typing.type_check_only
class ListVmwareEngineNetworksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareEngineNetworks: _list[VmwareEngineNetwork]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagementCluster(typing_extensions.TypedDict, total=False):
    clusterId: str
    nodeTypeConfigs: dict[str, typing.Any]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    managementCidr: str
    managementIpAddressLayoutVersion: int
    vmwareEngineNetwork: str
    vmwareEngineNetworkCanonical: str

@typing.type_check_only
class NetworkPolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    edgeServicesCidr: str
    externalIp: NetworkService
    internetAccess: NetworkService
    name: str
    uid: str
    updateTime: str
    vmwareEngineNetwork: str
    vmwareEngineNetworkCanonical: str

@typing.type_check_only
class NetworkService(typing_extensions.TypedDict, total=False):
    enabled: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNPROVISIONED", "RECONCILING", "ACTIVE"
    ]

@typing.type_check_only
class NodeType(typing_extensions.TypedDict, total=False):
    availableCustomCoreCounts: _list[int]
    diskSizeGb: int
    displayName: str
    memoryGb: int
    name: str
    nodeTypeId: str
    totalCoreCount: int
    virtualCpuCount: int

@typing.type_check_only
class NodeTypeConfig(typing_extensions.TypedDict, total=False):
    customCoreCount: int
    nodeCount: int

@typing.type_check_only
class Nsx(typing_extensions.TypedDict, total=False):
    fqdn: str
    internalIp: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING"]
    version: str

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
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PeeringRoute(typing_extensions.TypedDict, total=False):
    destRange: str
    direction: typing_extensions.Literal[
        "DIRECTION_UNSPECIFIED", "INCOMING", "OUTGOING"
    ]
    imported: bool
    nextHopRegion: str
    priority: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "DYNAMIC_PEERING_ROUTE",
        "STATIC_PEERING_ROUTE",
        "SUBNET_PEERING_ROUTE",
    ]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrivateCloud(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    description: str
    expireTime: str
    hcx: Hcx
    managementCluster: ManagementCluster
    name: str
    networkConfig: NetworkConfig
    nsx: Nsx
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "FAILED",
        "DELETED",
        "PURGING",
    ]
    type: typing_extensions.Literal["STANDARD", "TIME_LIMITED"]
    uid: str
    updateTime: str
    vcenter: Vcenter

@typing.type_check_only
class PrivateConnection(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    peeringId: str
    peeringState: typing_extensions.Literal[
        "PEERING_STATE_UNSPECIFIED", "PEERING_ACTIVE", "PEERING_INACTIVE"
    ]
    routingMode: typing_extensions.Literal[
        "ROUTING_MODE_UNSPECIFIED", "GLOBAL", "REGIONAL"
    ]
    serviceNetwork: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "UNPROVISIONED",
        "FAILED",
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "PRIVATE_SERVICE_ACCESS",
        "NETAPP_CLOUD_VOLUMES",
        "DELL_POWERSCALE",
        "THIRD_PARTY_SERVICE",
    ]
    uid: str
    updateTime: str
    vmwareEngineNetwork: str
    vmwareEngineNetworkCanonical: str

@typing.type_check_only
class ResetNsxCredentialsRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ResetVcenterCredentialsRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subnet(typing_extensions.TypedDict, total=False):
    gatewayIp: str
    ipCidrRange: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "DELETING",
        "RECONCILING",
        "FAILED",
    ]
    type: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UndeletePrivateCloudRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Vcenter(typing_extensions.TypedDict, total=False):
    fqdn: str
    internalIp: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING"]
    version: str

@typing.type_check_only
class VmwareEngineNetwork(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "LEGACY"]
    uid: str
    updateTime: str
    vpcNetworks: _list[VpcNetwork]

@typing.type_check_only
class VpcNetwork(typing_extensions.TypedDict, total=False):
    network: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "INTRANET", "INTERNET", "GOOGLE_CLOUD"
    ]
