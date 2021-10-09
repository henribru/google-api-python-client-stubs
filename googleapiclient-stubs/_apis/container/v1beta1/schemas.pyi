import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str
    gpuPartitionSize: str

@typing.type_check_only
class AddonsConfig(typing_extensions.TypedDict, total=False):
    cloudRunConfig: CloudRunConfig
    configConnectorConfig: ConfigConnectorConfig
    dnsCacheConfig: DnsCacheConfig
    gcePersistentDiskCsiDriverConfig: GcePersistentDiskCsiDriverConfig
    gcpFilestoreCsiDriverConfig: GcpFilestoreCsiDriverConfig
    horizontalPodAutoscaling: HorizontalPodAutoscaling
    httpLoadBalancing: HttpLoadBalancing
    istioConfig: IstioConfig
    kalmConfig: KalmConfig
    kubernetesDashboard: KubernetesDashboard
    networkPolicyConfig: NetworkPolicyConfig

@typing.type_check_only
class AuthenticatorGroupsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    securityGroup: str

@typing.type_check_only
class AutoUpgradeOptions(typing_extensions.TypedDict, total=False):
    autoUpgradeStartTime: str
    description: str

@typing.type_check_only
class Autopilot(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AutoprovisioningNodePoolDefaults(typing_extensions.TypedDict, total=False):
    bootDiskKmsKey: str
    diskSizeGb: int
    diskType: str
    imageType: str
    management: NodeManagement
    minCpuPlatform: str
    oauthScopes: _list[str]
    serviceAccount: str
    shieldedInstanceConfig: ShieldedInstanceConfig
    upgradeSettings: UpgradeSettings

@typing.type_check_only
class AvailableVersion(typing_extensions.TypedDict, total=False):
    reason: str
    version: str

@typing.type_check_only
class BigQueryDestination(typing_extensions.TypedDict, total=False):
    datasetId: str

@typing.type_check_only
class BinaryAuthorization(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False):
    name: str
    operationId: str
    projectId: str
    zone: str

@typing.type_check_only
class CidrBlock(typing_extensions.TypedDict, total=False):
    cidrBlock: str
    displayName: str

@typing.type_check_only
class ClientCertificateConfig(typing_extensions.TypedDict, total=False):
    issueClientCertificate: bool

@typing.type_check_only
class CloudRunConfig(typing_extensions.TypedDict, total=False):
    disabled: bool
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "LOAD_BALANCER_TYPE_EXTERNAL",
        "LOAD_BALANCER_TYPE_INTERNAL",
    ]

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    addonsConfig: AddonsConfig
    authenticatorGroupsConfig: AuthenticatorGroupsConfig
    autopilot: Autopilot
    autoscaling: ClusterAutoscaling
    binaryAuthorization: BinaryAuthorization
    clusterIpv4Cidr: str
    clusterTelemetry: ClusterTelemetry
    conditions: _list[StatusCondition]
    confidentialNodes: ConfidentialNodes
    createTime: str
    currentMasterVersion: str
    currentNodeCount: int
    currentNodeVersion: str
    databaseEncryption: DatabaseEncryption
    defaultMaxPodsConstraint: MaxPodsConstraint
    description: str
    enableKubernetesAlpha: bool
    enableTpu: bool
    endpoint: str
    expireTime: str
    id: str
    identityServiceConfig: IdentityServiceConfig
    initialClusterVersion: str
    initialNodeCount: int
    instanceGroupUrls: _list[str]
    ipAllocationPolicy: IPAllocationPolicy
    labelFingerprint: str
    legacyAbac: LegacyAbac
    location: str
    locations: _list[str]
    loggingConfig: LoggingConfig
    loggingService: str
    maintenancePolicy: MaintenancePolicy
    master: Master
    masterAuth: MasterAuth
    masterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    masterIpv4CidrBlock: str
    monitoringConfig: MonitoringConfig
    monitoringService: str
    name: str
    network: str
    networkConfig: NetworkConfig
    networkPolicy: NetworkPolicy
    nodeConfig: NodeConfig
    nodeIpv4CidrSize: int
    nodePoolDefaults: NodePoolDefaults
    nodePools: _list[NodePool]
    notificationConfig: NotificationConfig
    podSecurityPolicyConfig: PodSecurityPolicyConfig
    privateCluster: bool
    privateClusterConfig: PrivateClusterConfig
    releaseChannel: ReleaseChannel
    resourceLabels: dict[str, typing.Any]
    resourceUsageExportConfig: ResourceUsageExportConfig
    selfLink: str
    servicesIpv4Cidr: str
    shieldedNodes: ShieldedNodes
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    statusMessage: str
    subnetwork: str
    tpuConfig: TpuConfig
    tpuIpv4CidrBlock: str
    verticalPodAutoscaling: VerticalPodAutoscaling
    workloadCertificates: WorkloadCertificates
    workloadIdentityConfig: WorkloadIdentityConfig
    zone: str

@typing.type_check_only
class ClusterAutoscaling(typing_extensions.TypedDict, total=False):
    autoprovisioningLocations: _list[str]
    autoprovisioningNodePoolDefaults: AutoprovisioningNodePoolDefaults
    autoscalingProfile: typing_extensions.Literal[
        "PROFILE_UNSPECIFIED", "OPTIMIZE_UTILIZATION", "BALANCED"
    ]
    enableNodeAutoprovisioning: bool
    resourceLimits: _list[ResourceLimit]

@typing.type_check_only
class ClusterTelemetry(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "DISABLED", "ENABLED", "SYSTEM_ONLY"]

@typing.type_check_only
class ClusterUpdate(typing_extensions.TypedDict, total=False):
    desiredAddonsConfig: AddonsConfig
    desiredAuthenticatorGroupsConfig: AuthenticatorGroupsConfig
    desiredAutopilot: Autopilot
    desiredBinaryAuthorization: BinaryAuthorization
    desiredClusterAutoscaling: ClusterAutoscaling
    desiredClusterTelemetry: ClusterTelemetry
    desiredDatabaseEncryption: DatabaseEncryption
    desiredDatapathProvider: typing_extensions.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    desiredDefaultSnatStatus: DefaultSnatStatus
    desiredDnsConfig: DNSConfig
    desiredIdentityServiceConfig: IdentityServiceConfig
    desiredImageType: str
    desiredIntraNodeVisibilityConfig: IntraNodeVisibilityConfig
    desiredL4ilbSubsettingConfig: ILBSubsettingConfig
    desiredLocations: _list[str]
    desiredLoggingConfig: LoggingConfig
    desiredLoggingService: str
    desiredMaster: Master
    desiredMasterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    desiredMasterVersion: str
    desiredMonitoringConfig: MonitoringConfig
    desiredMonitoringService: str
    desiredNodePoolAutoscaling: NodePoolAutoscaling
    desiredNodePoolId: str
    desiredNodeVersion: str
    desiredNotificationConfig: NotificationConfig
    desiredPodSecurityPolicyConfig: PodSecurityPolicyConfig
    desiredPrivateClusterConfig: PrivateClusterConfig
    desiredPrivateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE",
        "PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL",
    ]
    desiredReleaseChannel: ReleaseChannel
    desiredResourceUsageExportConfig: ResourceUsageExportConfig
    desiredServiceExternalIpsConfig: ServiceExternalIPsConfig
    desiredShieldedNodes: ShieldedNodes
    desiredTpuConfig: TpuConfig
    desiredVerticalPodAutoscaling: VerticalPodAutoscaling
    desiredWorkloadCertificates: WorkloadCertificates
    desiredWorkloadIdentityConfig: WorkloadIdentityConfig

@typing.type_check_only
class CompleteIPRotationRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class ConfidentialNodes(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ConfigConnectorConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ConsumptionMeteringConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    cluster: Cluster
    parent: str
    projectId: str
    zone: str

@typing.type_check_only
class CreateNodePoolRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    nodePool: NodePool
    parent: str
    projectId: str
    zone: str

@typing.type_check_only
class DNSConfig(typing_extensions.TypedDict, total=False):
    clusterDns: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED", "PLATFORM_DEFAULT", "CLOUD_DNS"
    ]
    clusterDnsDomain: str
    clusterDnsScope: typing_extensions.Literal[
        "DNS_SCOPE_UNSPECIFIED", "CLUSTER_SCOPE", "VPC_SCOPE"
    ]

@typing.type_check_only
class DailyMaintenanceWindow(typing_extensions.TypedDict, total=False):
    duration: str
    startTime: str

@typing.type_check_only
class DatabaseEncryption(typing_extensions.TypedDict, total=False):
    keyName: str
    state: typing_extensions.Literal["UNKNOWN", "ENCRYPTED", "DECRYPTED"]

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DefaultSnatStatus(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class DnsCacheConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EphemeralStorageConfig(typing_extensions.TypedDict, total=False):
    localSsdCount: int

@typing.type_check_only
class GcePersistentDiskCsiDriverConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcpFilestoreCsiDriverConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GetJSONWebKeysResponse(typing_extensions.TypedDict, total=False):
    cacheHeader: HttpCacheControlResponseHeader
    keys: _list[Jwk]

@typing.type_check_only
class GetOpenIDConfigResponse(typing_extensions.TypedDict, total=False):
    cacheHeader: HttpCacheControlResponseHeader
    claims_supported: _list[str]
    grant_types: _list[str]
    id_token_signing_alg_values_supported: _list[str]
    issuer: str
    jwks_uri: str
    response_types_supported: _list[str]
    subject_types_supported: _list[str]

@typing.type_check_only
class HorizontalPodAutoscaling(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class HttpCacheControlResponseHeader(typing_extensions.TypedDict, total=False):
    age: str
    directive: str
    expires: str

@typing.type_check_only
class HttpLoadBalancing(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class ILBSubsettingConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    allowRouteOverlap: bool
    clusterIpv4Cidr: str
    clusterIpv4CidrBlock: str
    clusterSecondaryRangeName: str
    createSubnetwork: bool
    nodeIpv4Cidr: str
    nodeIpv4CidrBlock: str
    servicesIpv4Cidr: str
    servicesIpv4CidrBlock: str
    servicesSecondaryRangeName: str
    subnetworkName: str
    tpuIpv4CidrBlock: str
    useIpAliases: bool
    useRoutes: bool

@typing.type_check_only
class IdentityServiceConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class IntraNodeVisibilityConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class IstioConfig(typing_extensions.TypedDict, total=False):
    auth: typing_extensions.Literal["AUTH_NONE", "AUTH_MUTUAL_TLS"]
    disabled: bool

@typing.type_check_only
class Jwk(typing_extensions.TypedDict, total=False):
    alg: str
    crv: str
    e: str
    kid: str
    kty: str
    n: str
    use: str
    x: str
    y: str

@typing.type_check_only
class KalmConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class KubernetesDashboard(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class LegacyAbac(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class LinuxNodeConfig(typing_extensions.TypedDict, total=False):
    sysctls: dict[str, typing.Any]

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    missingZones: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNodePoolsResponse(typing_extensions.TypedDict, total=False):
    nodePools: _list[NodePool]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    missingZones: _list[str]
    operations: _list[Operation]

@typing.type_check_only
class ListUsableSubnetworksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subnetworks: _list[UsableSubnetwork]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    name: str
    recommended: bool
    type: typing_extensions.Literal["LOCATION_TYPE_UNSPECIFIED", "ZONE", "REGION"]

@typing.type_check_only
class LoggingComponentConfig(typing_extensions.TypedDict, total=False):
    enableComponents: _list[str]

@typing.type_check_only
class LoggingConfig(typing_extensions.TypedDict, total=False):
    componentConfig: LoggingComponentConfig

@typing.type_check_only
class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    resourceVersion: str
    window: MaintenanceWindow

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    dailyMaintenanceWindow: DailyMaintenanceWindow
    maintenanceExclusions: dict[str, typing.Any]
    recurringWindow: RecurringTimeWindow

@typing.type_check_only
class Master(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MasterAuth(typing_extensions.TypedDict, total=False):
    clientCertificate: str
    clientCertificateConfig: ClientCertificateConfig
    clientKey: str
    clusterCaCertificate: str
    password: str
    username: str

@typing.type_check_only
class MasterAuthorizedNetworksConfig(typing_extensions.TypedDict, total=False):
    cidrBlocks: _list[CidrBlock]
    enabled: bool

@typing.type_check_only
class MaxPodsConstraint(typing_extensions.TypedDict, total=False):
    maxPodsPerNode: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    name: str
    stringValue: str

@typing.type_check_only
class MonitoringComponentConfig(typing_extensions.TypedDict, total=False):
    enableComponents: _list[str]

@typing.type_check_only
class MonitoringConfig(typing_extensions.TypedDict, total=False):
    componentConfig: MonitoringComponentConfig

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    datapathProvider: typing_extensions.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    defaultSnatStatus: DefaultSnatStatus
    dnsConfig: DNSConfig
    enableIntraNodeVisibility: bool
    enableL4ilbSubsetting: bool
    network: str
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE",
        "PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL",
    ]
    serviceExternalIpsConfig: ServiceExternalIPsConfig
    subnetwork: str

@typing.type_check_only
class NetworkPolicy(typing_extensions.TypedDict, total=False):
    enabled: bool
    provider: typing_extensions.Literal["PROVIDER_UNSPECIFIED", "CALICO"]

@typing.type_check_only
class NetworkPolicyConfig(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class NetworkTags(typing_extensions.TypedDict, total=False):
    tags: _list[str]

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    bootDiskKmsKey: str
    diskSizeGb: int
    diskType: str
    ephemeralStorageConfig: EphemeralStorageConfig
    gvnic: VirtualNIC
    imageType: str
    kubeletConfig: NodeKubeletConfig
    labels: dict[str, typing.Any]
    linuxNodeConfig: LinuxNodeConfig
    localSsdCount: int
    machineType: str
    metadata: dict[str, typing.Any]
    minCpuPlatform: str
    nodeGroup: str
    oauthScopes: _list[str]
    preemptible: bool
    reservationAffinity: ReservationAffinity
    sandboxConfig: SandboxConfig
    serviceAccount: str
    shieldedInstanceConfig: ShieldedInstanceConfig
    tags: _list[str]
    taints: _list[NodeTaint]
    workloadMetadataConfig: WorkloadMetadataConfig

@typing.type_check_only
class NodeConfigDefaults(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class NodeKubeletConfig(typing_extensions.TypedDict, total=False):
    cpuCfsQuota: bool
    cpuCfsQuotaPeriod: str
    cpuManagerPolicy: str

@typing.type_check_only
class NodeLabels(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class NodeManagement(typing_extensions.TypedDict, total=False):
    autoRepair: bool
    autoUpgrade: bool
    upgradeOptions: AutoUpgradeOptions

@typing.type_check_only
class NodeNetworkConfig(typing_extensions.TypedDict, total=False):
    createPodRange: bool
    podIpv4CidrBlock: str
    podRange: str

@typing.type_check_only
class NodePool(typing_extensions.TypedDict, total=False):
    autoscaling: NodePoolAutoscaling
    conditions: _list[StatusCondition]
    config: NodeConfig
    initialNodeCount: int
    instanceGroupUrls: _list[str]
    locations: _list[str]
    management: NodeManagement
    maxPodsConstraint: MaxPodsConstraint
    name: str
    networkConfig: NodeNetworkConfig
    podIpv4CidrSize: int
    selfLink: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RUNNING_WITH_ERROR",
        "RECONCILING",
        "STOPPING",
        "ERROR",
    ]
    statusMessage: str
    upgradeSettings: UpgradeSettings
    version: str

@typing.type_check_only
class NodePoolAutoscaling(typing_extensions.TypedDict, total=False):
    autoprovisioned: bool
    enabled: bool
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class NodePoolDefaults(typing_extensions.TypedDict, total=False):
    nodeConfigDefaults: NodeConfigDefaults

@typing.type_check_only
class NodeTaint(typing_extensions.TypedDict, total=False):
    effect: typing_extensions.Literal[
        "EFFECT_UNSPECIFIED", "NO_SCHEDULE", "PREFER_NO_SCHEDULE", "NO_EXECUTE"
    ]
    key: str
    value: str

@typing.type_check_only
class NodeTaints(typing_extensions.TypedDict, total=False):
    taints: _list[NodeTaint]

@typing.type_check_only
class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsub: PubSub

@typing.type_check_only
class Operation(dict[str, typing.Any]): ...

@typing.type_check_only
class OperationProgress(dict[str, typing.Any]): ...

@typing.type_check_only
class PodSecurityPolicyConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    enablePrivateEndpoint: bool
    enablePrivateNodes: bool
    masterGlobalAccessConfig: PrivateClusterMasterGlobalAccessConfig
    masterIpv4CidrBlock: str
    peeringName: str
    privateEndpoint: str
    publicEndpoint: str

@typing.type_check_only
class PrivateClusterMasterGlobalAccessConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PubSub(typing_extensions.TypedDict, total=False):
    enabled: bool
    topic: str

@typing.type_check_only
class RecurringTimeWindow(typing_extensions.TypedDict, total=False):
    recurrence: str
    window: TimeWindow

@typing.type_check_only
class ReleaseChannel(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE"]

@typing.type_check_only
class ReleaseChannelConfig(typing_extensions.TypedDict, total=False):
    availableVersions: _list[AvailableVersion]
    channel: typing_extensions.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE"]
    defaultVersion: str
    validVersions: _list[str]

@typing.type_check_only
class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResourceLimit(typing_extensions.TypedDict, total=False):
    maximum: str
    minimum: str
    resourceType: str

@typing.type_check_only
class ResourceUsageExportConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: BigQueryDestination
    consumptionMeteringConfig: ConsumptionMeteringConfig
    enableNetworkEgressMetering: bool

@typing.type_check_only
class RollbackNodePoolUpgradeRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class SandboxConfig(typing_extensions.TypedDict, total=False):
    sandboxType: str
    type: typing_extensions.Literal["UNSPECIFIED", "GVISOR"]

@typing.type_check_only
class ServerConfig(typing_extensions.TypedDict, total=False):
    channels: _list[ReleaseChannelConfig]
    defaultClusterVersion: str
    defaultImageType: str
    validImageTypes: _list[str]
    validMasterVersions: _list[str]
    validNodeVersions: _list[str]
    windowsVersionMaps: dict[str, typing.Any]

@typing.type_check_only
class ServiceExternalIPsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SetAddonsConfigRequest(typing_extensions.TypedDict, total=False):
    addonsConfig: AddonsConfig
    clusterId: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetLabelsRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    labelFingerprint: str
    name: str
    projectId: str
    resourceLabels: dict[str, typing.Any]
    zone: str

@typing.type_check_only
class SetLegacyAbacRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    enabled: bool
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetLocationsRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    locations: _list[str]
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetLoggingServiceRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    loggingService: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetMaintenancePolicyRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    maintenancePolicy: MaintenancePolicy
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetMasterAuthRequest(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "UNKNOWN", "SET_PASSWORD", "GENERATE_PASSWORD", "SET_USERNAME"
    ]
    clusterId: str
    name: str
    projectId: str
    update: MasterAuth
    zone: str

@typing.type_check_only
class SetMonitoringServiceRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    monitoringService: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetNetworkPolicyRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    networkPolicy: NetworkPolicy
    projectId: str
    zone: str

@typing.type_check_only
class SetNodePoolAutoscalingRequest(typing_extensions.TypedDict, total=False):
    autoscaling: NodePoolAutoscaling
    clusterId: str
    name: str
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class SetNodePoolManagementRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    management: NodeManagement
    name: str
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class SetNodePoolSizeRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    nodeCount: int
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool

@typing.type_check_only
class ShieldedNodes(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class StartIPRotationRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    rotateCredentials: bool
    zone: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusCondition(typing_extensions.TypedDict, total=False):
    canonicalCode: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    code: typing_extensions.Literal[
        "UNKNOWN",
        "GCE_STOCKOUT",
        "GKE_SERVICE_ACCOUNT_DELETED",
        "GCE_QUOTA_EXCEEDED",
        "SET_BY_OPERATOR",
        "CLOUD_KMS_KEY_ERROR",
        "CA_EXPIRING",
    ]
    message: str

@typing.type_check_only
class TimeWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TpuConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    ipv4CidrBlock: str
    useServiceNetworking: bool

@typing.type_check_only
class UpdateClusterRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    update: ClusterUpdate
    zone: str

@typing.type_check_only
class UpdateMasterRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    masterVersion: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class UpdateNodePoolRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    gvnic: VirtualNIC
    imageType: str
    kubeletConfig: NodeKubeletConfig
    labels: NodeLabels
    linuxNodeConfig: LinuxNodeConfig
    locations: _list[str]
    name: str
    nodePoolId: str
    nodeVersion: str
    projectId: str
    tags: NetworkTags
    taints: NodeTaints
    upgradeSettings: UpgradeSettings
    workloadMetadataConfig: WorkloadMetadataConfig
    zone: str

@typing.type_check_only
class UpgradeAvailableEvent(typing_extensions.TypedDict, total=False):
    releaseChannel: ReleaseChannel
    resource: str
    resourceType: typing_extensions.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    version: str
    windowsVersions: WindowsVersions

@typing.type_check_only
class UpgradeEvent(typing_extensions.TypedDict, total=False):
    currentVersion: str
    operation: str
    operationStartTime: str
    resource: str
    resourceType: typing_extensions.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    targetVersion: str

@typing.type_check_only
class UpgradeSettings(typing_extensions.TypedDict, total=False):
    maxSurge: int
    maxUnavailable: int

@typing.type_check_only
class UsableSubnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str
    secondaryIpRanges: _list[UsableSubnetworkSecondaryRange]
    statusMessage: str
    subnetwork: str

@typing.type_check_only
class UsableSubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str
    status: typing_extensions.Literal[
        "UNKNOWN",
        "UNUSED",
        "IN_USE_SERVICE",
        "IN_USE_SHAREABLE_POD",
        "IN_USE_MANAGED_POD",
    ]

@typing.type_check_only
class VerticalPodAutoscaling(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VirtualNIC(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class WindowsVersion(typing_extensions.TypedDict, total=False):
    imageType: str
    osVersion: str
    supportEndDate: Date

@typing.type_check_only
class WindowsVersions(typing_extensions.TypedDict, total=False):
    windowsVersions: _list[WindowsVersion]

@typing.type_check_only
class WorkloadCertificates(typing_extensions.TypedDict, total=False):
    enableCertificates: bool

@typing.type_check_only
class WorkloadIdentityConfig(typing_extensions.TypedDict, total=False):
    identityNamespace: str
    identityProvider: str
    workloadPool: str

@typing.type_check_only
class WorkloadMetadataConfig(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "GCE_METADATA", "GKE_METADATA"]
    nodeMetadata: typing_extensions.Literal[
        "UNSPECIFIED", "SECURE", "EXPOSE", "GKE_METADATA_SERVER"
    ]
