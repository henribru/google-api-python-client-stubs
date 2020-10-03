import typing

import typing_extensions

class NodeConfig(typing_extensions.TypedDict, total=False):
    minCpuPlatform: str
    preemptible: bool
    localSsdCount: int
    sandboxConfig: SandboxConfig
    tags: typing.List[str]
    machineType: str
    taints: typing.List[NodeTaint]
    imageType: str
    oauthScopes: typing.List[str]
    metadata: typing.Dict[str, typing.Any]
    reservationAffinity: ReservationAffinity
    serviceAccount: str
    nodeGroup: str
    workloadMetadataConfig: WorkloadMetadataConfig
    labels: typing.Dict[str, typing.Any]
    bootDiskKmsKey: str
    diskSizeGb: int
    diskType: str
    shieldedInstanceConfig: ShieldedInstanceConfig
    accelerators: typing.List[AcceleratorConfig]

class DailyMaintenanceWindow(typing_extensions.TypedDict, total=False):
    startTime: str
    duration: str

class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: typing.List[str]

class UpdateMasterRequest(typing_extensions.TypedDict, total=False):
    name: str
    masterVersion: str
    projectId: str
    clusterId: str
    zone: str

class ResourceLimit(typing_extensions.TypedDict, total=False):
    resourceType: str
    minimum: str
    maximum: str

class WorkloadIdentityConfig(typing_extensions.TypedDict, total=False):
    workloadPool: str

class PrivateClusterMasterGlobalAccessConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class SetLabelsRequest(typing_extensions.TypedDict, total=False):
    name: str
    clusterId: str
    zone: str
    projectId: str
    labelFingerprint: str
    resourceLabels: typing.Dict[str, typing.Any]

class ConsumptionMeteringConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class ClusterAutoscaling(typing_extensions.TypedDict, total=False):
    autoprovisioningNodePoolDefaults: AutoprovisioningNodePoolDefaults
    resourceLimits: typing.List[ResourceLimit]
    autoprovisioningLocations: typing.List[str]
    enableNodeAutoprovisioning: bool

class WorkloadMetadataConfig(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "GCE_METADATA", "GKE_METADATA"]

class CloudRunConfig(typing_extensions.TypedDict, total=False):
    loadBalancerType: typing_extensions.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "LOAD_BALANCER_TYPE_EXTERNAL",
        "LOAD_BALANCER_TYPE_INTERNAL",
    ]
    disabled: bool

class LegacyAbac(typing_extensions.TypedDict, total=False):
    enabled: bool

class ConfigConnectorConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class ReleaseChannel(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE"]

class VerticalPodAutoscaling(typing_extensions.TypedDict, total=False):
    enabled: bool

class RollbackNodePoolUpgradeRequest(typing_extensions.TypedDict, total=False):
    zone: str
    name: str
    nodePoolId: str
    projectId: str
    clusterId: str

class KubernetesDashboard(typing_extensions.TypedDict, total=False):
    disabled: bool

class StartIPRotationRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    rotateCredentials: bool
    zone: str
    clusterId: str
    name: str

class ClientCertificateConfig(typing_extensions.TypedDict, total=False):
    issueClientCertificate: bool

class UsableSubnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    subnetwork: str
    secondaryIpRanges: typing.List[UsableSubnetworkSecondaryRange]
    statusMessage: str
    network: str

class SandboxConfig(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "GVISOR"]

class SetMonitoringServiceRequest(typing_extensions.TypedDict, total=False):
    monitoringService: str
    zone: str
    name: str
    projectId: str
    clusterId: str

class CompleteIPRotationRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    projectId: str
    zone: str
    name: str

class Operation(typing_extensions.TypedDict, total=False):
    selfLink: str
    endTime: str
    name: str
    startTime: str
    progress: OperationProgress
    location: str
    clusterConditions: typing.List[StatusCondition]
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "ABORTING"
    ]
    statusMessage: str
    nodepoolConditions: typing.List[StatusCondition]
    targetLink: str
    operationType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CREATE_CLUSTER",
        "DELETE_CLUSTER",
        "UPGRADE_MASTER",
        "UPGRADE_NODES",
        "REPAIR_CLUSTER",
        "UPDATE_CLUSTER",
        "CREATE_NODE_POOL",
        "DELETE_NODE_POOL",
        "SET_NODE_POOL_MANAGEMENT",
        "AUTO_REPAIR_NODES",
        "AUTO_UPGRADE_NODES",
        "SET_LABELS",
        "SET_MASTER_AUTH",
        "SET_NODE_POOL_SIZE",
        "SET_NETWORK_POLICY",
        "SET_MAINTENANCE_POLICY",
    ]
    detail: str
    zone: str

class GetOpenIDConfigResponse(typing_extensions.TypedDict, total=False):
    id_token_signing_alg_values_supported: typing.List[str]
    grant_types: typing.List[str]
    claims_supported: typing.List[str]
    issuer: str
    subject_types_supported: typing.List[str]
    cacheHeader: HttpCacheControlResponseHeader
    response_types_supported: typing.List[str]
    jwks_uri: str

class RecurringTimeWindow(typing_extensions.TypedDict, total=False):
    window: TimeWindow
    recurrence: str

class SetNodePoolAutoscalingRequest(typing_extensions.TypedDict, total=False):
    zone: str
    projectId: str
    name: str
    autoscaling: NodePoolAutoscaling
    nodePoolId: str
    clusterId: str

class DatabaseEncryption(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["UNKNOWN", "ENCRYPTED", "DECRYPTED"]
    keyName: str

class ShieldedNodes(typing_extensions.TypedDict, total=False):
    enabled: bool

class MaxPodsConstraint(typing_extensions.TypedDict, total=False):
    maxPodsPerNode: str

class CreateClusterRequest(typing_extensions.TypedDict, total=False):
    parent: str
    cluster: Cluster
    projectId: str
    zone: str

class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str

class UpdateNodePoolRequest(typing_extensions.TypedDict, total=False):
    name: str
    nodePoolId: str
    upgradeSettings: UpgradeSettings
    imageType: str
    nodeVersion: str
    workloadMetadataConfig: WorkloadMetadataConfig
    projectId: str
    locations: typing.List[str]
    clusterId: str
    zone: str

class SetMaintenancePolicyRequest(typing_extensions.TypedDict, total=False):
    zone: str
    maintenancePolicy: MaintenancePolicy
    name: str
    projectId: str
    clusterId: str

class MasterAuthorizedNetworksConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    cidrBlocks: typing.List[CidrBlock]

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

class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    enablePrivateEndpoint: bool
    peeringName: str
    publicEndpoint: str
    masterIpv4CidrBlock: str
    enablePrivateNodes: bool
    masterGlobalAccessConfig: PrivateClusterMasterGlobalAccessConfig
    privateEndpoint: str

class SetLocationsRequest(typing_extensions.TypedDict, total=False):
    locations: typing.List[str]
    zone: str
    name: str
    clusterId: str
    projectId: str

class CidrBlock(typing_extensions.TypedDict, total=False):
    displayName: str
    cidrBlock: str

class ServerConfig(typing_extensions.TypedDict, total=False):
    defaultClusterVersion: str
    validNodeVersions: typing.List[str]
    channels: typing.List[ReleaseChannelConfig]
    validMasterVersions: typing.List[str]
    validImageTypes: typing.List[str]
    defaultImageType: str

class NodePool(typing_extensions.TypedDict, total=False):
    upgradeSettings: UpgradeSettings
    initialNodeCount: int
    autoscaling: NodePoolAutoscaling
    statusMessage: str
    selfLink: str
    version: str
    management: NodeManagement
    podIpv4CidrSize: int
    instanceGroupUrls: typing.List[str]
    config: NodeConfig
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RUNNING_WITH_ERROR",
        "RECONCILING",
        "STOPPING",
        "ERROR",
    ]
    conditions: typing.List[StatusCondition]
    maxPodsConstraint: MaxPodsConstraint
    locations: typing.List[str]
    name: str

class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    subnetworkName: str
    nodeIpv4CidrBlock: str
    clusterIpv4CidrBlock: str
    servicesIpv4Cidr: str
    clusterIpv4Cidr: str
    servicesSecondaryRangeName: str
    clusterSecondaryRangeName: str
    useRoutes: bool
    useIpAliases: bool
    servicesIpv4CidrBlock: str
    nodeIpv4Cidr: str
    createSubnetwork: bool
    tpuIpv4CidrBlock: str

class NetworkPolicy(typing_extensions.TypedDict, total=False):
    enabled: bool
    provider: typing_extensions.Literal["PROVIDER_UNSPECIFIED", "CALICO"]

class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    resourceVersion: str
    window: MaintenanceWindow

class Metric(typing_extensions.TypedDict, total=False):
    intValue: str
    stringValue: str
    name: str
    doubleValue: float

class NetworkPolicyConfig(typing_extensions.TypedDict, total=False):
    disabled: bool

class ReleaseChannelConfig(typing_extensions.TypedDict, total=False):
    validVersions: typing.List[str]
    defaultVersion: str
    channel: typing_extensions.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE"]

class MasterAuth(typing_extensions.TypedDict, total=False):
    clientCertificate: str
    clusterCaCertificate: str
    password: str
    username: str
    clientKey: str
    clientCertificateConfig: ClientCertificateConfig

class SetAddonsConfigRequest(typing_extensions.TypedDict, total=False):
    addonsConfig: AddonsConfig
    projectId: str
    zone: str
    name: str
    clusterId: str

class UpdateClusterRequest(typing_extensions.TypedDict, total=False):
    zone: str
    update: ClusterUpdate
    projectId: str
    name: str
    clusterId: str

class AddonsConfig(typing_extensions.TypedDict, total=False):
    horizontalPodAutoscaling: HorizontalPodAutoscaling
    httpLoadBalancing: HttpLoadBalancing
    kubernetesDashboard: KubernetesDashboard
    cloudRunConfig: CloudRunConfig
    networkPolicyConfig: NetworkPolicyConfig
    dnsCacheConfig: DnsCacheConfig
    configConnectorConfig: ConfigConnectorConfig

class AutoUpgradeOptions(typing_extensions.TypedDict, total=False):
    description: str
    autoUpgradeStartTime: str

class HorizontalPodAutoscaling(typing_extensions.TypedDict, total=False):
    disabled: bool

class SetNetworkPolicyRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    networkPolicy: NetworkPolicy
    name: str
    zone: str
    clusterId: str

class NodePoolAutoscaling(typing_extensions.TypedDict, total=False):
    maxNodeCount: int
    enabled: bool
    minNodeCount: int
    autoprovisioned: bool

class GetJSONWebKeysResponse(typing_extensions.TypedDict, total=False):
    cacheHeader: HttpCacheControlResponseHeader
    keys: typing.List[Jwk]

class Cluster(typing_extensions.TypedDict, total=False):
    subnetwork: str
    location: str
    databaseEncryption: DatabaseEncryption
    enableTpu: bool
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    releaseChannel: ReleaseChannel
    selfLink: str
    locations: typing.List[str]
    statusMessage: str
    loggingService: str
    conditions: typing.List[StatusCondition]
    resourceUsageExportConfig: ResourceUsageExportConfig
    legacyAbac: LegacyAbac
    createTime: str
    nodePools: typing.List[NodePool]
    endpoint: str
    networkPolicy: NetworkPolicy
    networkConfig: NetworkConfig
    addonsConfig: AddonsConfig
    initialNodeCount: int
    monitoringService: str
    workloadIdentityConfig: WorkloadIdentityConfig
    nodeIpv4CidrSize: int
    masterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    shieldedNodes: ShieldedNodes
    servicesIpv4Cidr: str
    autoscaling: ClusterAutoscaling
    currentNodeVersion: str
    zone: str
    privateClusterConfig: PrivateClusterConfig
    authenticatorGroupsConfig: AuthenticatorGroupsConfig
    resourceLabels: typing.Dict[str, typing.Any]
    nodeConfig: NodeConfig
    clusterIpv4Cidr: str
    currentMasterVersion: str
    instanceGroupUrls: typing.List[str]
    tpuIpv4CidrBlock: str
    enableKubernetesAlpha: bool
    masterAuth: MasterAuth
    labelFingerprint: str
    ipAllocationPolicy: IPAllocationPolicy
    network: str
    name: str
    initialClusterVersion: str
    defaultMaxPodsConstraint: MaxPodsConstraint
    verticalPodAutoscaling: VerticalPodAutoscaling
    maintenancePolicy: MaintenancePolicy
    description: str
    expireTime: str
    currentNodeCount: int
    binaryAuthorization: BinaryAuthorization

class DefaultSnatStatus(typing_extensions.TypedDict, total=False):
    disabled: bool

class NetworkConfig(typing_extensions.TypedDict, total=False):
    network: str
    enableIntraNodeVisibility: bool
    defaultSnatStatus: DefaultSnatStatus
    subnetwork: str

class ListNodePoolsResponse(typing_extensions.TypedDict, total=False):
    nodePools: typing.List[NodePool]

class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    recurringWindow: RecurringTimeWindow
    dailyMaintenanceWindow: DailyMaintenanceWindow
    maintenanceExclusions: typing.Dict[str, typing.Any]

class ResourceUsageExportConfig(typing_extensions.TypedDict, total=False):
    consumptionMeteringConfig: ConsumptionMeteringConfig
    enableNetworkEgressMetering: bool
    bigqueryDestination: BigQueryDestination

class IntraNodeVisibilityConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class BigQueryDestination(typing_extensions.TypedDict, total=False):
    datasetId: str

class NodeTaint(typing_extensions.TypedDict, total=False):
    value: str
    key: str
    effect: typing_extensions.Literal[
        "EFFECT_UNSPECIFIED", "NO_SCHEDULE", "PREFER_NO_SCHEDULE", "NO_EXECUTE"
    ]

class TimeWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class UpgradeSettings(typing_extensions.TypedDict, total=False):
    maxUnavailable: int
    maxSurge: int

class SetNodePoolManagementRequest(typing_extensions.TypedDict, total=False):
    nodePoolId: str
    projectId: str
    zone: str
    management: NodeManagement
    clusterId: str
    name: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ClusterUpdate(typing_extensions.TypedDict, total=False):
    desiredLocations: typing.List[str]
    desiredMonitoringService: str
    desiredDefaultSnatStatus: DefaultSnatStatus
    desiredAddonsConfig: AddonsConfig
    desiredImageType: str
    desiredLoggingService: str
    desiredMasterVersion: str
    desiredBinaryAuthorization: BinaryAuthorization
    desiredNodePoolId: str
    desiredClusterAutoscaling: ClusterAutoscaling
    desiredNodePoolAutoscaling: NodePoolAutoscaling
    desiredDatabaseEncryption: DatabaseEncryption
    desiredShieldedNodes: ShieldedNodes
    desiredNodeVersion: str
    desiredVerticalPodAutoscaling: VerticalPodAutoscaling
    desiredWorkloadIdentityConfig: WorkloadIdentityConfig
    desiredIntraNodeVisibilityConfig: IntraNodeVisibilityConfig
    desiredResourceUsageExportConfig: ResourceUsageExportConfig
    desiredReleaseChannel: ReleaseChannel
    desiredPrivateClusterConfig: PrivateClusterConfig
    desiredMasterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    missingZones: typing.List[str]
    operations: typing.List[Operation]

class CancelOperationRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    zone: str
    name: str
    operationId: str

class ListClustersResponse(typing_extensions.TypedDict, total=False):
    missingZones: typing.List[str]
    clusters: typing.List[Cluster]

class SetNodePoolSizeRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    nodePoolId: str
    name: str
    nodeCount: int
    clusterId: str
    zone: str

class AutoprovisioningNodePoolDefaults(typing_extensions.TypedDict, total=False):
    diskType: str
    diskSizeGb: int
    bootDiskKmsKey: str
    upgradeSettings: UpgradeSettings
    oauthScopes: typing.List[str]
    minCpuPlatform: str
    serviceAccount: str
    management: NodeManagement
    shieldedInstanceConfig: ShieldedInstanceConfig

class CreateNodePoolRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    zone: str
    clusterId: str
    nodePool: NodePool
    parent: str

class NodeManagement(typing_extensions.TypedDict, total=False):
    autoUpgrade: bool
    autoRepair: bool
    upgradeOptions: AutoUpgradeOptions

class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool

class SetLegacyAbacRequest(typing_extensions.TypedDict, total=False):
    zone: str
    clusterId: str
    projectId: str
    name: str
    enabled: bool

class SetMasterAuthRequest(typing_extensions.TypedDict, total=False):
    update: MasterAuth
    name: str
    zone: str
    action: typing_extensions.Literal[
        "UNKNOWN", "SET_PASSWORD", "GENERATE_PASSWORD", "SET_USERNAME"
    ]
    projectId: str
    clusterId: str

class SetLoggingServiceRequest(typing_extensions.TypedDict, total=False):
    loggingService: str
    projectId: str
    zone: str
    clusterId: str
    name: str

class Jwk(typing_extensions.TypedDict, total=False):
    e: str
    n: str
    alg: str
    x: str
    y: str
    kid: str
    kty: str
    use: str
    crv: str

class HttpCacheControlResponseHeader(typing_extensions.TypedDict, total=False):
    directive: str
    expires: str
    age: str

class StatusCondition(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "UNKNOWN",
        "GCE_STOCKOUT",
        "GKE_SERVICE_ACCOUNT_DELETED",
        "GCE_QUOTA_EXCEEDED",
        "SET_BY_OPERATOR",
        "CLOUD_KMS_KEY_ERROR",
    ]
    message: str

class BinaryAuthorization(typing_extensions.TypedDict, total=False):
    enabled: bool

class HttpLoadBalancing(typing_extensions.TypedDict, total=False):
    disabled: bool

class UpgradeEvent(typing_extensions.TypedDict, total=False):
    targetVersion: str
    currentVersion: str
    resource: str
    operation: str
    operationStartTime: str
    resourceType: typing_extensions.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]

class DnsCacheConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

class AuthenticatorGroupsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    securityGroup: str

class OperationProgress(typing.Dict[str, typing.Any]): ...

class ListUsableSubnetworksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subnetworks: typing.List[UsableSubnetwork]
