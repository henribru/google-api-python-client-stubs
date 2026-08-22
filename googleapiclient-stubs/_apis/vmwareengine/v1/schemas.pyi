import typing

_list = list

@typing.type_check_only
class AcceleratePrivateCloudDeletionRequest(typing.TypedDict, total=False):
    etag: str
    requestId: str

@typing.type_check_only
class Announcement(typing.TypedDict, total=False):
    activityType: str
    cluster: str
    code: str
    createTime: str
    description: str
    metadata: dict[str, typing.Any]
    name: str
    privateCloud: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "DELETING", "CREATING"
    ]
    targetResourceType: str
    updateTime: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AutoscalingPolicy(typing.TypedDict, total=False):
    consumedMemoryThresholds: Thresholds
    cpuThresholds: Thresholds
    grantedMemoryThresholds: Thresholds
    nodeTypeId: str
    scaleOutSize: int
    storageThresholds: Thresholds

@typing.type_check_only
class AutoscalingSettings(typing.TypedDict, total=False):
    autoscalingPolicies: dict[str, typing.Any]
    coolDownPeriod: str
    maxClusterNodeCount: int
    minClusterNodeCount: int

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    autoscalingSettings: AutoscalingSettings
    createTime: str
    datastoreMountConfig: _list[DatastoreMountConfig]
    management: bool
    name: str
    nodeTypeConfigs: dict[str, typing.Any]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "UPDATING", "DELETING", "REPAIRING"
    ]
    stretchedClusterConfig: StretchedClusterConfig
    uid: str
    updateTime: str

@typing.type_check_only
class Constraints(typing.TypedDict, total=False):
    disallowedIntervals: _list[WeeklyTimeInterval]
    minHoursDay: int
    minHoursWeek: int
    rescheduleDateRange: Interval

@typing.type_check_only
class Credentials(typing.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class Datastore(typing.TypedDict, total=False):
    clusters: _list[str]
    createTime: str
    description: str
    etag: str
    name: str
    nfsDatastore: NfsDatastore
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class DatastoreMountConfig(typing.TypedDict, total=False):
    accessMode: typing.Literal["ACCESS_MODE_UNSPECIFIED", "READ_ONLY", "READ_WRITE"]
    datastore: str
    datastoreNetwork: DatastoreNetwork
    fileShare: str
    nfsVersion: typing.Literal["NFS_VERSION_UNSPECIFIED", "NFS_V3"]
    servers: _list[str]

@typing.type_check_only
class DatastoreNetwork(typing.TypedDict, total=False):
    connectionCount: int
    mtu: int
    networkPeering: str
    subnet: str

@typing.type_check_only
class DnsBindPermission(typing.TypedDict, total=False):
    name: str
    principals: _list[Principal]

@typing.type_check_only
class DnsForwarding(typing.TypedDict, total=False):
    createTime: str
    forwardingRules: _list[ForwardingRule]
    name: str
    updateTime: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    cryptoKeyName: str
    type: typing.Literal["TYPE_UNSPECIFIED", "CMEK", "LEGACY_CMEK", "OTHER"]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalAccessRule(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ALLOW", "DENY"]
    createTime: str
    description: str
    destinationIpRanges: _list[IpRange]
    destinationPorts: _list[str]
    ipProtocol: str
    name: str
    priority: int
    sourceIpRanges: _list[IpRange]
    sourcePorts: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "UPDATING", "DELETING"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class ExternalAddress(typing.TypedDict, total=False):
    createTime: str
    description: str
    externalIp: str
    internalIp: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "UPDATING", "DELETING"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class FetchNetworkPolicyExternalAddressesResponse(typing.TypedDict, total=False):
    externalAddresses: _list[ExternalAddress]
    nextPageToken: str

@typing.type_check_only
class ForwardingRule(typing.TypedDict, total=False):
    domain: str
    nameServers: _list[str]

@typing.type_check_only
class GoogleFileService(typing.TypedDict, total=False):
    filestoreInstance: str
    netappVolume: str

@typing.type_check_only
class GoogleVmwareFileService(typing.TypedDict, total=False): ...

@typing.type_check_only
class GrantDnsBindPermissionRequest(typing.TypedDict, total=False):
    principal: Principal
    requestId: str

@typing.type_check_only
class Hcx(typing.TypedDict, total=False):
    fqdn: str
    internalIp: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING", "ACTIVATING"]
    version: str

@typing.type_check_only
class HcxActivationKey(typing.TypedDict, total=False):
    activationKey: str
    createTime: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "AVAILABLE", "CONSUMED", "CREATING"]
    uid: str

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class IpRange(typing.TypedDict, total=False):
    externalAddress: str
    ipAddress: str
    ipAddressRange: str

@typing.type_check_only
class ListAnnouncementsResponse(typing.TypedDict, total=False):
    announcements: _list[Announcement]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClustersResponse(typing.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDatastoresResponse(typing.TypedDict, total=False):
    datastores: _list[Datastore]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExternalAccessRulesResponse(typing.TypedDict, total=False):
    externalAccessRules: _list[ExternalAccessRule]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExternalAddressesResponse(typing.TypedDict, total=False):
    externalAddresses: _list[ExternalAddress]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListHcxActivationKeysResponse(typing.TypedDict, total=False):
    hcxActivationKeys: _list[HcxActivationKey]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListLoggingServersResponse(typing.TypedDict, total=False):
    loggingServers: _list[LoggingServer]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListManagementDnsZoneBindingsResponse(typing.TypedDict, total=False):
    managementDnsZoneBindings: _list[ManagementDnsZoneBinding]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNetworkPeeringsResponse(typing.TypedDict, total=False):
    networkPeerings: _list[NetworkPeering]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNetworkPoliciesResponse(typing.TypedDict, total=False):
    networkPolicies: _list[NetworkPolicy]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListNodeTypesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nodeTypes: _list[NodeType]
    unreachable: _list[str]

@typing.type_check_only
class ListNodesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nodes: _list[Node]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPeeringRoutesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    peeringRoutes: _list[PeeringRoute]

@typing.type_check_only
class ListPrivateCloudsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    privateClouds: _list[PrivateCloud]
    unreachable: _list[str]

@typing.type_check_only
class ListPrivateConnectionPeeringRoutesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    peeringRoutes: _list[PeeringRoute]

@typing.type_check_only
class ListPrivateConnectionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    privateConnections: _list[PrivateConnection]
    unreachable: _list[str]

@typing.type_check_only
class ListSubnetsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subnets: _list[Subnet]
    unreachable: _list[str]

@typing.type_check_only
class ListUpgradesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    upgrades: _list[Upgrade]

@typing.type_check_only
class ListVmwareEngineNetworksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareEngineNetworks: _list[VmwareEngineNetwork]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    capabilities: _list[typing.Literal["CAPABILITY_UNSPECIFIED", "STRETCHED_CLUSTERS"]]

@typing.type_check_only
class LoggingServer(typing.TypedDict, total=False):
    createTime: str
    hostname: str
    name: str
    port: int
    protocol: typing.Literal["PROTOCOL_UNSPECIFIED", "UDP", "TCP", "TLS", "SSL", "RELP"]
    sourceType: typing.Literal["SOURCE_TYPE_UNSPECIFIED", "ESXI", "VCSA"]
    uid: str
    updateTime: str

@typing.type_check_only
class ManagementCluster(typing.TypedDict, total=False):
    clusterId: str
    nodeTypeConfigs: dict[str, typing.Any]
    stretchedClusterConfig: StretchedClusterConfig

@typing.type_check_only
class ManagementDnsZoneBinding(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"
    ]
    uid: str
    updateTime: str
    vmwareEngineNetwork: str
    vpcNetwork: str

@typing.type_check_only
class MigrateManagementVmsRequest(typing.TypedDict, total=False):
    clusterId: str
    etag: str
    requestId: str

@typing.type_check_only
class MountDatastoreRequest(typing.TypedDict, total=False):
    datastoreMountConfig: DatastoreMountConfig
    ignoreColocation: bool
    requestId: str
    validateOnly: bool

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    dnsServerIp: str
    managementCidr: str
    managementIpAddressLayoutVersion: int
    vmwareEngineNetwork: str
    vmwareEngineNetworkCanonical: str

@typing.type_check_only
class NetworkPeering(typing.TypedDict, total=False):
    createTime: str
    description: str
    exchangeSubnetRoutes: bool
    exportCustomRoutes: bool
    exportCustomRoutesWithPublicIp: bool
    importCustomRoutes: bool
    importCustomRoutesWithPublicIp: bool
    name: str
    peerMtu: int
    peerNetwork: str
    peerNetworkType: typing.Literal[
        "PEER_NETWORK_TYPE_UNSPECIFIED",
        "STANDARD",
        "VMWARE_ENGINE_NETWORK",
        "PRIVATE_SERVICES_ACCESS",
        "NETAPP_CLOUD_VOLUMES",
        "THIRD_PARTY_SERVICE",
        "DELL_POWERSCALE",
        "GOOGLE_CLOUD_NETAPP_VOLUMES",
        "GOOGLE_CLOUD_FILESTORE_INSTANCES",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "INACTIVE", "ACTIVE", "CREATING", "DELETING"
    ]
    stateDetails: str
    uid: str
    updateTime: str
    vmwareEngineNetwork: str

@typing.type_check_only
class NetworkPolicy(typing.TypedDict, total=False):
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
class NetworkService(typing.TypedDict, total=False):
    enabled: bool
    state: typing.Literal["STATE_UNSPECIFIED", "UNPROVISIONED", "RECONCILING", "ACTIVE"]

@typing.type_check_only
class NfsDatastore(typing.TypedDict, total=False):
    googleFileService: GoogleFileService
    googleVmwareFileService: GoogleVmwareFileService
    thirdPartyFileService: ThirdPartyFileService

@typing.type_check_only
class Node(typing.TypedDict, total=False):
    customCoreCount: str
    fqdn: str
    internalIp: str
    name: str
    nodeTypeId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "FAILED", "UPGRADING"
    ]
    version: str

@typing.type_check_only
class NodeType(typing.TypedDict, total=False):
    availableCustomCoreCounts: _list[int]
    capabilities: _list[typing.Literal["CAPABILITY_UNSPECIFIED", "STRETCHED_CLUSTERS"]]
    diskSizeGb: int
    displayName: str
    families: _list[str]
    kind: typing.Literal["KIND_UNSPECIFIED", "STANDARD", "STORAGE_ONLY"]
    memoryGb: int
    name: str
    nodeTypeId: str
    totalCoreCount: int
    virtualCpuCount: int

@typing.type_check_only
class NodeTypeConfig(typing.TypedDict, total=False):
    customCoreCount: int
    nodeCount: int

@typing.type_check_only
class Nsx(typing.TypedDict, total=False):
    fqdn: str
    internalIp: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING"]
    version: str

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
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PeeringRoute(typing.TypedDict, total=False):
    destRange: str
    direction: typing.Literal["DIRECTION_UNSPECIFIED", "INCOMING", "OUTGOING"]
    imported: bool
    nextHopRegion: str
    priority: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "DYNAMIC_PEERING_ROUTE",
        "STATIC_PEERING_ROUTE",
        "SUBNET_PEERING_ROUTE",
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Principal(typing.TypedDict, total=False):
    serviceAccount: str
    user: str

@typing.type_check_only
class PrivateCloud(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    description: str
    encryptionConfig: EncryptionConfig
    expireTime: str
    hcx: Hcx
    managementCluster: ManagementCluster
    name: str
    networkConfig: NetworkConfig
    nsx: Nsx
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "FAILED",
        "DELETED",
        "PURGING",
    ]
    type: typing.Literal["STANDARD", "TIME_LIMITED", "STRETCHED"]
    uid: str
    updateTime: str
    vcenter: Vcenter

@typing.type_check_only
class PrivateConnection(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    peeringId: str
    peeringState: typing.Literal[
        "PEERING_STATE_UNSPECIFIED", "PEERING_ACTIVE", "PEERING_INACTIVE"
    ]
    routingMode: typing.Literal["ROUTING_MODE_UNSPECIFIED", "GLOBAL", "REGIONAL"]
    serviceNetwork: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "UNPROVISIONED",
        "FAILED",
    ]
    type: typing.Literal[
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
class RepairManagementDnsZoneBindingRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ResetNsxCredentialsRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ResetVcenterCredentialsRequest(typing.TypedDict, total=False):
    requestId: str
    username: str

@typing.type_check_only
class RevokeDnsBindPermissionRequest(typing.TypedDict, total=False):
    principal: Principal
    requestId: str

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    constraints: Constraints
    editWindow: Interval
    lastEditor: typing.Literal["EDITOR_UNSPECIFIED", "SYSTEM", "USER"]
    startTime: str
    weeklyWindows: _list[TimeWindow]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StretchedClusterConfig(typing.TypedDict, total=False):
    preferredLocation: str
    secondaryLocation: str

@typing.type_check_only
class Subnet(typing.TypedDict, total=False):
    gatewayIp: str
    ipCidrRange: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "DELETING",
        "RECONCILING",
        "FAILED",
    ]
    type: str
    vlanId: int

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class ThirdPartyFileService(typing.TypedDict, total=False):
    fileShare: str
    network: str
    servers: _list[str]

@typing.type_check_only
class Thresholds(typing.TypedDict, total=False):
    scaleIn: int
    scaleOut: int

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeWindow(typing.TypedDict, total=False):
    dayOfWeek: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class UndeletePrivateCloudRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class UnmountDatastoreRequest(typing.TypedDict, total=False):
    datastore: str
    requestId: str
    validateOnly: bool

@typing.type_check_only
class Upgrade(typing.TypedDict, total=False):
    componentUpgrades: _list[VmwareUpgradeComponent]
    createTime: str
    description: str
    endTime: str
    estimatedDuration: str
    etag: str
    name: str
    schedule: Schedule
    startVersion: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "SCHEDULED",
        "ONGOING",
        "SUCCEEDED",
        "PAUSED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
        "RESCHEDULING",
    ]
    targetVersion: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "VSPHERE_UPGRADE",
        "VSPHERE_PATCH",
        "WORKAROUND",
        "FIRMWARE_UPGRADE",
        "SWITCH_UPGRADE",
        "OTHER",
        "INFRASTRUCTURE_UPGRADE",
    ]
    uid: str
    updateTime: str
    version: str

@typing.type_check_only
class Vcenter(typing.TypedDict, total=False):
    fqdn: str
    internalIp: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "CREATING"]
    version: str

@typing.type_check_only
class VmwareEngineNetwork(typing.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "LEGACY", "STANDARD"]
    uid: str
    updateTime: str
    vpcNetworks: _list[VpcNetwork]

@typing.type_check_only
class VmwareUpgradeComponent(typing.TypedDict, total=False):
    componentType: typing.Literal[
        "VMWARE_COMPONENT_TYPE_UNSPECIFIED",
        "VCENTER",
        "ESXI",
        "NSXT_UC",
        "NSXT_EDGE",
        "NSXT_MGR",
        "HCX",
        "VSAN",
        "DVS",
        "NAMESERVER_VM",
        "KMS_VM",
        "WITNESS_VM",
        "NSXT",
        "CLUSTER",
        "VM_TOOLS",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "PAUSED",
        "SUCCEEDED",
        "FAILED",
        "NOT_STARTED",
        "NOT_APPLICABLE",
    ]

@typing.type_check_only
class VpcNetwork(typing.TypedDict, total=False):
    network: str
    type: typing.Literal["TYPE_UNSPECIFIED", "INTRANET", "INTERNET", "GOOGLE_CLOUD"]

@typing.type_check_only
class WeeklyTimeInterval(typing.TypedDict, total=False):
    endDay: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    endTime: TimeOfDay
    startDay: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    startTime: TimeOfDay
