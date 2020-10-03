import typing

import typing_extensions

class GetJSONWebKeysResponse(typing_extensions.TypedDict, total=False):
    keys: typing.List[Jwk]
    cacheHeader: HttpCacheControlResponseHeader

class NodeConfig(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    machineType: str
    taints: typing.List[NodeTaint]
    linuxNodeConfig: LinuxNodeConfig
    tags: typing.List[str]
    preemptible: bool
    workloadMetadataConfig: WorkloadMetadataConfig
    oauthScopes: typing.List[str]
    sandboxConfig: SandboxConfig
    kubeletConfig: NodeKubeletConfig
    labels: typing.Dict[str, typing.Any]
    imageType: str
    bootDiskKmsKey: str
    nodeGroup: str
    accelerators: typing.List[AcceleratorConfig]
    minCpuPlatform: str
    metadata: typing.Dict[str, typing.Any]
    diskType: str
    localSsdCount: int
    shieldedInstanceConfig: ShieldedInstanceConfig
    diskSizeGb: int
    reservationAffinity: ReservationAffinity

class ClientCertificateConfig(typing_extensions.TypedDict, total=False):
    issueClientCertificate: bool

class SetLoggingServiceRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    loggingService: str
    zone: str
    name: str
    clusterId: str

class NodePool(typing_extensions.TypedDict, total=False):
    upgradeSettings: UpgradeSettings
    locations: typing.List[str]
    version: str
    initialNodeCount: int
    config: NodeConfig
    podIpv4CidrSize: int
    name: str
    conditions: typing.List[StatusCondition]
    statusMessage: str
    instanceGroupUrls: typing.List[str]
    autoscaling: NodePoolAutoscaling
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RUNNING_WITH_ERROR",
        "RECONCILING",
        "STOPPING",
        "ERROR",
    ]
    maxPodsConstraint: MaxPodsConstraint
    management: NodeManagement
    selfLink: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    missingZones: typing.List[str]
    operations: typing.List[Operation]

class CancelOperationRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    name: str
    operationId: str
    zone: str

class UpgradeSettings(typing_extensions.TypedDict, total=False):
    maxUnavailable: int
    maxSurge: int

class DnsCacheConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class MaxPodsConstraint(typing_extensions.TypedDict, total=False):
    maxPodsPerNode: str

class TpuConfig(typing_extensions.TypedDict, total=False):
    useServiceNetworking: bool
    ipv4CidrBlock: str
    enabled: bool

class SetMonitoringServiceRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    name: str
    monitoringService: str
    clusterId: str
    zone: str

class ClusterAutoscaling(typing_extensions.TypedDict, total=False):
    autoprovisioningLocations: typing.List[str]
    enableNodeAutoprovisioning: bool
    autoprovisioningNodePoolDefaults: AutoprovisioningNodePoolDefaults
    resourceLimits: typing.List[ResourceLimit]
    autoscalingProfile: typing_extensions.Literal[
        "PROFILE_UNSPECIFIED", "OPTIMIZE_UTILIZATION", "BALANCED"
    ]

class NodeTaint(typing_extensions.TypedDict, total=False):
    key: str
    value: str
    effect: typing_extensions.Literal[
        "EFFECT_UNSPECIFIED", "NO_SCHEDULE", "PREFER_NO_SCHEDULE", "NO_EXECUTE"
    ]

class CreateNodePoolRequest(typing_extensions.TypedDict, total=False):
    nodePool: NodePool
    clusterId: str
    projectId: str
    zone: str
    parent: str

class IstioConfig(typing_extensions.TypedDict, total=False):
    disabled: bool
    auth: typing_extensions.Literal["AUTH_NONE", "AUTH_MUTUAL_TLS"]

class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool

class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    window: MaintenanceWindow
    resourceVersion: str

class NetworkPolicy(typing_extensions.TypedDict, total=False):
    provider: typing_extensions.Literal["PROVIDER_UNSPECIFIED", "CALICO"]
    enabled: bool

class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsub: PubSub

class SetMaintenancePolicyRequest(typing_extensions.TypedDict, total=False):
    maintenancePolicy: MaintenancePolicy
    name: str
    clusterId: str
    zone: str
    projectId: str

class KubernetesDashboard(typing_extensions.TypedDict, total=False):
    disabled: bool

class Empty(typing_extensions.TypedDict, total=False): ...

class GcePersistentDiskCsiDriverConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class NodeManagement(typing_extensions.TypedDict, total=False):
    autoUpgrade: bool
    autoRepair: bool
    upgradeOptions: AutoUpgradeOptions

class Operation(typing.Dict[str, typing.Any]): ...

class ConfigConnectorConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class AvailableVersion(typing_extensions.TypedDict, total=False):
    reason: str
    version: str

class StartIPRotationRequest(typing_extensions.TypedDict, total=False):
    name: str
    projectId: str
    rotateCredentials: bool
    clusterId: str
    zone: str

class DatabaseEncryption(typing_extensions.TypedDict, total=False):
    keyName: str
    state: typing_extensions.Literal["UNKNOWN", "ENCRYPTED", "DECRYPTED"]

class SetNodePoolSizeRequest(typing_extensions.TypedDict, total=False):
    nodeCount: int
    clusterId: str
    name: str
    nodePoolId: str
    projectId: str
    zone: str

class ServerConfig(typing_extensions.TypedDict, total=False):
    validMasterVersions: typing.List[str]
    defaultClusterVersion: str
    channels: typing.List[ReleaseChannelConfig]
    validImageTypes: typing.List[str]
    defaultImageType: str
    validNodeVersions: typing.List[str]

class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorType: str
    acceleratorCount: str

class MasterAuth(typing_extensions.TypedDict, total=False):
    clientCertificateConfig: ClientCertificateConfig
    username: str
    clusterCaCertificate: str
    clientCertificate: str
    password: str
    clientKey: str

class NodePoolAutoscaling(typing_extensions.TypedDict, total=False):
    maxNodeCount: int
    enabled: bool
    minNodeCount: int
    autoprovisioned: bool

class SetLabelsRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    labelFingerprint: str
    resourceLabels: typing.Dict[str, typing.Any]
    zone: str
    projectId: str
    name: str

class IntraNodeVisibilityConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class SetNetworkPolicyRequest(typing_extensions.TypedDict, total=False):
    networkPolicy: NetworkPolicy
    zone: str
    clusterId: str
    name: str
    projectId: str

class ClusterTelemetry(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "DISABLED", "ENABLED", "SYSTEM_ONLY"]

class LegacyAbac(typing_extensions.TypedDict, total=False):
    enabled: bool

class ReleaseChannel(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE"]

class Metric(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    name: str
    stringValue: str

class BinaryAuthorization(typing_extensions.TypedDict, total=False):
    enabled: bool

class SetMasterAuthRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    zone: str
    update: MasterAuth
    name: str
    clusterId: str
    action: typing_extensions.Literal[
        "UNKNOWN", "SET_PASSWORD", "GENERATE_PASSWORD", "SET_USERNAME"
    ]

class TimeWindow(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class LinuxNodeConfig(typing_extensions.TypedDict, total=False):
    sysctls: typing.Dict[str, typing.Any]

class DailyMaintenanceWindow(typing_extensions.TypedDict, total=False):
    startTime: str
    duration: str

class WorkloadMetadataConfig(typing_extensions.TypedDict, total=False):
    nodeMetadata: typing_extensions.Literal[
        "UNSPECIFIED", "SECURE", "EXPOSE", "GKE_METADATA_SERVER"
    ]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "GCE_METADATA", "GKE_METADATA"]

class PubSub(typing_extensions.TypedDict, total=False):
    topic: str
    enabled: bool

class ListUsableSubnetworksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subnetworks: typing.List[UsableSubnetwork]

class ReleaseChannelConfig(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE"]
    defaultVersion: str
    validVersions: typing.List[str]
    availableVersions: typing.List[AvailableVersion]

class UpdateNodePoolRequest(typing_extensions.TypedDict, total=False):
    kubeletConfig: NodeKubeletConfig
    zone: str
    imageType: str
    clusterId: str
    name: str
    upgradeSettings: UpgradeSettings
    nodeVersion: str
    nodePoolId: str
    workloadMetadataConfig: WorkloadMetadataConfig
    locations: typing.List[str]
    projectId: str
    linuxNodeConfig: LinuxNodeConfig

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: typing.List[Cluster]
    missingZones: typing.List[str]

class SandboxConfig(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "GVISOR"]
    sandboxType: str

class UsableSubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    status: typing_extensions.Literal[
        "UNKNOWN",
        "UNUSED",
        "IN_USE_SERVICE",
        "IN_USE_SHAREABLE_POD",
        "IN_USE_MANAGED_POD",
    ]
    rangeName: str

class CidrBlock(typing_extensions.TypedDict, total=False):
    displayName: str
    cidrBlock: str

class ResourceLimit(typing_extensions.TypedDict, total=False):
    resourceType: str
    minimum: str
    maximum: str

class SetNodePoolAutoscalingRequest(typing_extensions.TypedDict, total=False):
    nodePoolId: str
    autoscaling: NodePoolAutoscaling
    name: str
    clusterId: str
    zone: str
    projectId: str

class HttpCacheControlResponseHeader(typing_extensions.TypedDict, total=False):
    directive: str
    expires: str
    age: str

class ReservationAffinity(typing_extensions.TypedDict, total=False):
    key: str
    values: typing.List[str]
    consumeReservationType: typing_extensions.Literal[
        "UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]

class CloudRunConfig(typing_extensions.TypedDict, total=False):
    disabled: bool
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "LOAD_BALANCER_TYPE_EXTERNAL",
        "LOAD_BALANCER_TYPE_INTERNAL",
    ]

class GetOpenIDConfigResponse(typing_extensions.TypedDict, total=False):
    issuer: str
    response_types_supported: typing.List[str]
    id_token_signing_alg_values_supported: typing.List[str]
    jwks_uri: str
    subject_types_supported: typing.List[str]
    claims_supported: typing.List[str]
    cacheHeader: HttpCacheControlResponseHeader
    grant_types: typing.List[str]

class CompleteIPRotationRequest(typing_extensions.TypedDict, total=False):
    name: str
    projectId: str
    clusterId: str
    zone: str

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
    ]
    message: str

class UpgradeEvent(typing_extensions.TypedDict, total=False):
    operationStartTime: str
    targetVersion: str
    currentVersion: str
    resourceType: typing_extensions.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    resource: str
    operation: str

class MasterAuthorizedNetworksConfig(typing_extensions.TypedDict, total=False):
    cidrBlocks: typing.List[CidrBlock]
    enabled: bool

class AddonsConfig(typing_extensions.TypedDict, total=False):
    gcePersistentDiskCsiDriverConfig: GcePersistentDiskCsiDriverConfig
    dnsCacheConfig: DnsCacheConfig
    networkPolicyConfig: NetworkPolicyConfig
    configConnectorConfig: ConfigConnectorConfig
    horizontalPodAutoscaling: HorizontalPodAutoscaling
    kalmConfig: KalmConfig
    kubernetesDashboard: KubernetesDashboard
    httpLoadBalancing: HttpLoadBalancing
    istioConfig: IstioConfig
    cloudRunConfig: CloudRunConfig

class WorkloadIdentityConfig(typing_extensions.TypedDict, total=False):
    workloadPool: str
    identityProvider: str
    identityNamespace: str

class HttpLoadBalancing(typing_extensions.TypedDict, total=False):
    disabled: bool

class Jwk(typing_extensions.TypedDict, total=False):
    kid: str
    crv: str
    use: str
    e: str
    x: str
    kty: str
    n: str
    alg: str
    y: str

class Master(typing_extensions.TypedDict, total=False): ...

class SetLocationsRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    zone: str
    locations: typing.List[str]
    name: str
    clusterId: str

class AutoUpgradeOptions(typing_extensions.TypedDict, total=False):
    autoUpgradeStartTime: str
    description: str

class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    privateEndpoint: str
    enablePrivateNodes: bool
    peeringName: str
    masterGlobalAccessConfig: PrivateClusterMasterGlobalAccessConfig
    masterIpv4CidrBlock: str
    publicEndpoint: str
    enablePrivateEndpoint: bool

class ResourceUsageExportConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: BigQueryDestination
    consumptionMeteringConfig: ConsumptionMeteringConfig
    enableNetworkEgressMetering: bool

class PodSecurityPolicyConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class AutoprovisioningNodePoolDefaults(typing_extensions.TypedDict, total=False):
    upgradeSettings: UpgradeSettings
    oauthScopes: typing.List[str]
    management: NodeManagement
    minCpuPlatform: str
    diskType: str
    diskSizeGb: int
    serviceAccount: str
    shieldedInstanceConfig: ShieldedInstanceConfig
    bootDiskKmsKey: str

class ClusterUpdate(typing_extensions.TypedDict, total=False):
    desiredMasterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    desiredDefaultSnatStatus: DefaultSnatStatus
    desiredNodeVersion: str
    desiredPodSecurityPolicyConfig: PodSecurityPolicyConfig
    desiredAddonsConfig: AddonsConfig
    desiredVerticalPodAutoscaling: VerticalPodAutoscaling
    desiredNodePoolAutoscaling: NodePoolAutoscaling
    desiredImageType: str
    desiredWorkloadIdentityConfig: WorkloadIdentityConfig
    desiredTpuConfig: TpuConfig
    desiredMonitoringService: str
    desiredBinaryAuthorization: BinaryAuthorization
    desiredIntraNodeVisibilityConfig: IntraNodeVisibilityConfig
    desiredDatapathProvider: typing_extensions.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    desiredClusterTelemetry: ClusterTelemetry
    desiredPrivateClusterConfig: PrivateClusterConfig
    desiredLocations: typing.List[str]
    desiredMasterVersion: str
    desiredDatabaseEncryption: DatabaseEncryption
    desiredShieldedNodes: ShieldedNodes
    desiredNotificationConfig: NotificationConfig
    desiredNodePoolId: str
    desiredResourceUsageExportConfig: ResourceUsageExportConfig
    desiredMaster: Master
    desiredClusterAutoscaling: ClusterAutoscaling
    desiredLoggingService: str
    desiredReleaseChannel: ReleaseChannel

class SetLegacyAbacRequest(typing_extensions.TypedDict, total=False):
    enabled: bool
    name: str
    projectId: str
    clusterId: str
    zone: str

class VerticalPodAutoscaling(typing_extensions.TypedDict, total=False):
    enabled: bool

class NetworkConfig(typing_extensions.TypedDict, total=False):
    subnetwork: str
    datapathProvider: typing_extensions.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    defaultSnatStatus: DefaultSnatStatus
    enableIntraNodeVisibility: bool
    network: str

class HorizontalPodAutoscaling(typing_extensions.TypedDict, total=False):
    disabled: bool

class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    recurringWindow: RecurringTimeWindow
    maintenanceExclusions: typing.Dict[str, typing.Any]
    dailyMaintenanceWindow: DailyMaintenanceWindow

class SetAddonsConfigRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    projectId: str
    name: str
    addonsConfig: AddonsConfig
    zone: str

class UpdateClusterRequest(typing_extensions.TypedDict, total=False):
    update: ClusterUpdate
    name: str
    clusterId: str
    zone: str
    projectId: str

class SetNodePoolManagementRequest(typing_extensions.TypedDict, total=False):
    management: NodeManagement
    zone: str
    nodePoolId: str
    clusterId: str
    name: str
    projectId: str

class Cluster(typing_extensions.TypedDict, total=False):
    enableTpu: bool
    network: str
    tpuConfig: TpuConfig
    ipAllocationPolicy: IPAllocationPolicy
    servicesIpv4Cidr: str
    expireTime: str
    currentNodeVersion: str
    location: str
    autoscaling: ClusterAutoscaling
    defaultMaxPodsConstraint: MaxPodsConstraint
    notificationConfig: NotificationConfig
    currentNodeCount: int
    privateCluster: bool
    labelFingerprint: str
    nodeIpv4CidrSize: int
    masterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    locations: typing.List[str]
    name: str
    podSecurityPolicyConfig: PodSecurityPolicyConfig
    verticalPodAutoscaling: VerticalPodAutoscaling
    shieldedNodes: ShieldedNodes
    monitoringService: str
    legacyAbac: LegacyAbac
    confidentialNodes: ConfidentialNodes
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    currentMasterVersion: str
    masterAuth: MasterAuth
    nodeConfig: NodeConfig
    conditions: typing.List[StatusCondition]
    initialClusterVersion: str
    workloadIdentityConfig: WorkloadIdentityConfig
    binaryAuthorization: BinaryAuthorization
    privateClusterConfig: PrivateClusterConfig
    resourceLabels: typing.Dict[str, typing.Any]
    selfLink: str
    instanceGroupUrls: typing.List[str]
    databaseEncryption: DatabaseEncryption
    endpoint: str
    loggingService: str
    nodePools: typing.List[NodePool]
    masterIpv4CidrBlock: str
    releaseChannel: ReleaseChannel
    addonsConfig: AddonsConfig
    subnetwork: str
    description: str
    zone: str
    clusterTelemetry: ClusterTelemetry
    networkConfig: NetworkConfig
    initialNodeCount: int
    createTime: str
    statusMessage: str
    master: Master
    authenticatorGroupsConfig: AuthenticatorGroupsConfig
    clusterIpv4Cidr: str
    maintenancePolicy: MaintenancePolicy
    networkPolicy: NetworkPolicy
    tpuIpv4CidrBlock: str
    resourceUsageExportConfig: ResourceUsageExportConfig
    enableKubernetesAlpha: bool

class KalmConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class NetworkPolicyConfig(typing_extensions.TypedDict, total=False):
    disabled: bool

class RollbackNodePoolUpgradeRequest(typing_extensions.TypedDict, total=False):
    name: str
    clusterId: str
    projectId: str
    zone: str
    nodePoolId: str

class ShieldedNodes(typing_extensions.TypedDict, total=False):
    enabled: bool

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class AuthenticatorGroupsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    securityGroup: str

class ConsumptionMeteringConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class UpdateMasterRequest(typing_extensions.TypedDict, total=False):
    zone: str
    projectId: str
    masterVersion: str
    name: str
    clusterId: str

class BigQueryDestination(typing_extensions.TypedDict, total=False):
    datasetId: str

class ListNodePoolsResponse(typing_extensions.TypedDict, total=False):
    nodePools: typing.List[NodePool]

class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    tpuIpv4CidrBlock: str
    subnetworkName: str
    clusterIpv4CidrBlock: str
    useRoutes: bool
    clusterIpv4Cidr: str
    servicesIpv4CidrBlock: str
    createSubnetwork: bool
    servicesSecondaryRangeName: str
    clusterSecondaryRangeName: str
    useIpAliases: bool
    nodeIpv4CidrBlock: str
    servicesIpv4Cidr: str
    allowRouteOverlap: bool
    nodeIpv4Cidr: str

class OperationProgress(typing.Dict[str, typing.Any]): ...

class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    parent: str
    projectId: str
    cluster: Cluster
    zone: str

class UsableSubnetwork(typing_extensions.TypedDict, total=False):
    secondaryIpRanges: typing.List[UsableSubnetworkSecondaryRange]
    statusMessage: str
    ipCidrRange: str
    network: str
    subnetwork: str

class DefaultSnatStatus(typing_extensions.TypedDict, total=False):
    disabled: bool

class ConfidentialNodes(typing_extensions.TypedDict, total=False):
    enabled: bool

class Location(typing_extensions.TypedDict, total=False):
    name: str
    recommended: bool
    type: typing_extensions.Literal["LOCATION_TYPE_UNSPECIFIED", "ZONE", "REGION"]

class NodeKubeletConfig(typing_extensions.TypedDict, total=False):
    cpuCfsQuotaPeriod: str
    cpuCfsQuota: bool
    cpuManagerPolicy: str

class RecurringTimeWindow(typing_extensions.TypedDict, total=False):
    recurrence: str
    window: TimeWindow

class PrivateClusterMasterGlobalAccessConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
