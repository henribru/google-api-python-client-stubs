import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str
    gpuDriverInstallationConfig: GPUDriverInstallationConfig
    gpuPartitionSize: str
    gpuSharingConfig: GPUSharingConfig
    maxTimeSharedClientsPerGpu: str

@typing.type_check_only
class AdditionalNodeNetworkConfig(typing_extensions.TypedDict, total=False):
    network: str
    subnetwork: str

@typing.type_check_only
class AdditionalPodNetworkConfig(typing_extensions.TypedDict, total=False):
    maxPodsPerNode: MaxPodsConstraint
    networkAttachment: str
    secondaryPodRange: str
    subnetwork: str

@typing.type_check_only
class AdditionalPodRangesConfig(typing_extensions.TypedDict, total=False):
    podRangeInfo: _list[RangeInfo]
    podRangeNames: _list[str]

@typing.type_check_only
class AddonsConfig(typing_extensions.TypedDict, total=False):
    cloudRunConfig: CloudRunConfig
    configConnectorConfig: ConfigConnectorConfig
    dnsCacheConfig: DnsCacheConfig
    gcePersistentDiskCsiDriverConfig: GcePersistentDiskCsiDriverConfig
    gcpFilestoreCsiDriverConfig: GcpFilestoreCsiDriverConfig
    gcsFuseCsiDriverConfig: GcsFuseCsiDriverConfig
    gkeBackupAgentConfig: GkeBackupAgentConfig
    horizontalPodAutoscaling: HorizontalPodAutoscaling
    httpLoadBalancing: HttpLoadBalancing
    istioConfig: IstioConfig
    kalmConfig: KalmConfig
    kubernetesDashboard: KubernetesDashboard
    networkPolicyConfig: NetworkPolicyConfig
    parallelstoreCsiDriverConfig: ParallelstoreCsiDriverConfig
    rayOperatorConfig: RayOperatorConfig
    statefulHaConfig: StatefulHAConfig

@typing.type_check_only
class AdvancedDatapathObservabilityConfig(typing_extensions.TypedDict, total=False):
    enableMetrics: bool
    enableRelay: bool
    relayMode: typing_extensions.Literal[
        "RELAY_MODE_UNSPECIFIED", "DISABLED", "INTERNAL_VPC_LB", "EXTERNAL_LB"
    ]

@typing.type_check_only
class AdvancedMachineFeatures(typing_extensions.TypedDict, total=False):
    enableNestedVirtualization: bool
    threadsPerCore: str

@typing.type_check_only
class AuthenticatorGroupsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    securityGroup: str

@typing.type_check_only
class AutoMonitoringConfig(typing_extensions.TypedDict, total=False):
    scope: typing_extensions.Literal["SCOPE_UNSPECIFIED", "ALL", "NONE"]

@typing.type_check_only
class AutoUpgradeOptions(typing_extensions.TypedDict, total=False):
    autoUpgradeStartTime: str
    description: str

@typing.type_check_only
class Autopilot(typing_extensions.TypedDict, total=False):
    conversionStatus: AutopilotConversionStatus
    enabled: bool
    workloadPolicyConfig: WorkloadPolicyConfig

@typing.type_check_only
class AutopilotCompatibilityIssue(typing_extensions.TypedDict, total=False):
    constraintType: str
    description: str
    documentationUrl: str
    incompatibilityType: typing_extensions.Literal[
        "UNSPECIFIED",
        "INCOMPATIBILITY",
        "ADDITIONAL_CONFIG_REQUIRED",
        "PASSED_WITH_OPTIONAL_CONFIG",
    ]
    lastObservation: str
    subjects: _list[str]

@typing.type_check_only
class AutopilotConversionStatus(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DONE"]

@typing.type_check_only
class AutoprovisioningNodePoolDefaults(typing_extensions.TypedDict, total=False):
    bootDiskKmsKey: str
    diskSizeGb: int
    diskType: str
    imageType: str
    insecureKubeletReadonlyPortEnabled: bool
    management: NodeManagement
    minCpuPlatform: str
    oauthScopes: _list[str]
    serviceAccount: str
    shieldedInstanceConfig: ShieldedInstanceConfig
    upgradeSettings: UpgradeSettings

@typing.type_check_only
class AutoscaledRolloutPolicy(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AvailableVersion(typing_extensions.TypedDict, total=False):
    reason: str
    version: str

@typing.type_check_only
class BestEffortProvisioning(typing_extensions.TypedDict, total=False):
    enabled: bool
    minProvisionNodes: int

@typing.type_check_only
class BigQueryDestination(typing_extensions.TypedDict, total=False):
    datasetId: str

@typing.type_check_only
class BinaryAuthorization(typing_extensions.TypedDict, total=False):
    enabled: bool
    evaluationMode: typing_extensions.Literal[
        "EVALUATION_MODE_UNSPECIFIED",
        "DISABLED",
        "PROJECT_SINGLETON_POLICY_ENFORCE",
        "POLICY_BINDINGS",
        "POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE",
    ]
    policyBindings: _list[PolicyBinding]

@typing.type_check_only
class BlueGreenInfo(typing_extensions.TypedDict, total=False):
    blueInstanceGroupUrls: _list[str]
    bluePoolDeletionStartTime: str
    greenInstanceGroupUrls: _list[str]
    greenPoolVersion: str
    phase: typing_extensions.Literal[
        "PHASE_UNSPECIFIED",
        "UPDATE_STARTED",
        "CREATING_GREEN_POOL",
        "CORDONING_BLUE_POOL",
        "WAITING_TO_DRAIN_BLUE_POOL",
        "DRAINING_BLUE_POOL",
        "NODE_POOL_SOAKING",
        "DELETING_BLUE_POOL",
        "ROLLBACK_STARTED",
    ]

@typing.type_check_only
class BlueGreenSettings(typing_extensions.TypedDict, total=False):
    autoscaledRolloutPolicy: AutoscaledRolloutPolicy
    nodePoolSoakDuration: str
    standardRolloutPolicy: StandardRolloutPolicy

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False):
    name: str
    operationId: str
    projectId: str
    zone: str

@typing.type_check_only
class CertificateAuthorityDomainConfig(typing_extensions.TypedDict, total=False):
    fqdns: _list[str]
    gcpSecretManagerCertificateConfig: GCPSecretManagerCertificateConfig

@typing.type_check_only
class CheckAutopilotCompatibilityResponse(typing_extensions.TypedDict, total=False):
    issues: _list[AutopilotCompatibilityIssue]
    summary: str

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
    compliancePostureConfig: CompliancePostureConfig
    conditions: _list[StatusCondition]
    confidentialNodes: ConfidentialNodes
    controlPlaneEndpointsConfig: ControlPlaneEndpointsConfig
    costManagementConfig: CostManagementConfig
    createTime: str
    currentMasterVersion: str
    currentNodeCount: int
    currentNodeVersion: str
    databaseEncryption: DatabaseEncryption
    defaultMaxPodsConstraint: MaxPodsConstraint
    description: str
    enableK8sBetaApis: K8sBetaAPIConfig
    enableKubernetesAlpha: bool
    enableTpu: bool
    endpoint: str
    enterpriseConfig: EnterpriseConfig
    etag: str
    expireTime: str
    fleet: Fleet
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
    meshCertificates: MeshCertificates
    monitoringConfig: MonitoringConfig
    monitoringService: str
    name: str
    network: str
    networkConfig: NetworkConfig
    networkPolicy: NetworkPolicy
    nodeConfig: NodeConfig
    nodeIpv4CidrSize: int
    nodePoolAutoConfig: NodePoolAutoConfig
    nodePoolDefaults: NodePoolDefaults
    nodePools: _list[NodePool]
    notificationConfig: NotificationConfig
    parentProductConfig: ParentProductConfig
    podAutoscaling: PodAutoscaling
    podSecurityPolicyConfig: PodSecurityPolicyConfig
    privateCluster: bool
    privateClusterConfig: PrivateClusterConfig
    protectConfig: ProtectConfig
    rbacBindingConfig: RBACBindingConfig
    releaseChannel: ReleaseChannel
    resourceLabels: dict[str, typing.Any]
    resourceUsageExportConfig: ResourceUsageExportConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    secretManagerConfig: SecretManagerConfig
    securityPostureConfig: SecurityPostureConfig
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
    userManagedKeysConfig: UserManagedKeysConfig
    verticalPodAutoscaling: VerticalPodAutoscaling
    workloadAltsConfig: WorkloadALTSConfig
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
class ClusterNetworkPerformanceConfig(typing_extensions.TypedDict, total=False):
    totalEgressBandwidthTier: typing_extensions.Literal["TIER_UNSPECIFIED", "TIER_1"]

@typing.type_check_only
class ClusterTelemetry(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "DISABLED", "ENABLED", "SYSTEM_ONLY"]

@typing.type_check_only
class ClusterUpdate(typing_extensions.TypedDict, total=False):
    additionalPodRangesConfig: AdditionalPodRangesConfig
    desiredAddonsConfig: AddonsConfig
    desiredAuthenticatorGroupsConfig: AuthenticatorGroupsConfig
    desiredAutopilotWorkloadPolicyConfig: WorkloadPolicyConfig
    desiredBinaryAuthorization: BinaryAuthorization
    desiredClusterAutoscaling: ClusterAutoscaling
    desiredClusterTelemetry: ClusterTelemetry
    desiredCompliancePostureConfig: CompliancePostureConfig
    desiredContainerdConfig: ContainerdConfig
    desiredControlPlaneEndpointsConfig: ControlPlaneEndpointsConfig
    desiredCostManagementConfig: CostManagementConfig
    desiredDatabaseEncryption: DatabaseEncryption
    desiredDatapathProvider: typing_extensions.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    desiredDefaultEnablePrivateNodes: bool
    desiredDefaultSnatStatus: DefaultSnatStatus
    desiredDisableL4LbFirewallReconciliation: bool
    desiredDnsConfig: DNSConfig
    desiredEnableCiliumClusterwideNetworkPolicy: bool
    desiredEnableFqdnNetworkPolicy: bool
    desiredEnableMultiNetworking: bool
    desiredEnablePrivateEndpoint: bool
    desiredEnterpriseConfig: DesiredEnterpriseConfig
    desiredFleet: Fleet
    desiredGatewayApiConfig: GatewayAPIConfig
    desiredGcfsConfig: GcfsConfig
    desiredHostMaintenancePolicy: HostMaintenancePolicy
    desiredIdentityServiceConfig: IdentityServiceConfig
    desiredImageType: str
    desiredInTransitEncryptionConfig: typing_extensions.Literal[
        "IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED",
        "IN_TRANSIT_ENCRYPTION_DISABLED",
        "IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT",
    ]
    desiredIntraNodeVisibilityConfig: IntraNodeVisibilityConfig
    desiredK8sBetaApis: K8sBetaAPIConfig
    desiredL4ilbSubsettingConfig: ILBSubsettingConfig
    desiredLocations: _list[str]
    desiredLoggingConfig: LoggingConfig
    desiredLoggingService: str
    desiredMaster: Master
    desiredMasterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    desiredMasterVersion: str
    desiredMeshCertificates: MeshCertificates
    desiredMonitoringConfig: MonitoringConfig
    desiredMonitoringService: str
    desiredNetworkPerformanceConfig: ClusterNetworkPerformanceConfig
    desiredNodeKubeletConfig: NodeKubeletConfig
    desiredNodePoolAutoConfigKubeletConfig: NodeKubeletConfig
    desiredNodePoolAutoConfigLinuxNodeConfig: LinuxNodeConfig
    desiredNodePoolAutoConfigNetworkTags: NetworkTags
    desiredNodePoolAutoConfigResourceManagerTags: ResourceManagerTags
    desiredNodePoolAutoscaling: NodePoolAutoscaling
    desiredNodePoolId: str
    desiredNodePoolLoggingConfig: NodePoolLoggingConfig
    desiredNodeVersion: str
    desiredNotificationConfig: NotificationConfig
    desiredParentProductConfig: ParentProductConfig
    desiredPodAutoscaling: PodAutoscaling
    desiredPodSecurityPolicyConfig: PodSecurityPolicyConfig
    desiredPrivateClusterConfig: PrivateClusterConfig
    desiredPrivateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE",
        "PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL",
    ]
    desiredProtectConfig: ProtectConfig
    desiredRbacBindingConfig: RBACBindingConfig
    desiredReleaseChannel: ReleaseChannel
    desiredResourceUsageExportConfig: ResourceUsageExportConfig
    desiredSecretManagerConfig: SecretManagerConfig
    desiredSecurityPostureConfig: SecurityPostureConfig
    desiredServiceExternalIpsConfig: ServiceExternalIPsConfig
    desiredShieldedNodes: ShieldedNodes
    desiredStackType: typing_extensions.Literal[
        "STACK_TYPE_UNSPECIFIED", "IPV4", "IPV4_IPV6"
    ]
    desiredTpuConfig: TpuConfig
    desiredVerticalPodAutoscaling: VerticalPodAutoscaling
    desiredWorkloadAltsConfig: WorkloadALTSConfig
    desiredWorkloadCertificates: WorkloadCertificates
    desiredWorkloadIdentityConfig: WorkloadIdentityConfig
    enableK8sBetaApis: K8sBetaAPIConfig
    etag: str
    privateClusterConfig: PrivateClusterConfig
    removedAdditionalPodRangesConfig: AdditionalPodRangesConfig
    userManagedKeysConfig: UserManagedKeysConfig

@typing.type_check_only
class ClusterUpgradeInfo(typing_extensions.TypedDict, total=False):
    autoUpgradeStatus: _list[
        typing_extensions.Literal[
            "UNKNOWN", "ACTIVE", "MINOR_UPGRADE_PAUSED", "UPGRADE_PAUSED"
        ]
    ]
    endOfExtendedSupportTimestamp: str
    endOfStandardSupportTimestamp: str
    minorTargetVersion: str
    patchTargetVersion: str
    pausedReason: _list[
        typing_extensions.Literal[
            "AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED",
            "MAINTENANCE_WINDOW",
            "MAINTENANCE_EXCLUSION_NO_UPGRADES",
            "MAINTENANCE_EXCLUSION_NO_MINOR_UPGRADES",
            "CLUSTER_DISRUPTION_BUDGET",
            "CLUSTER_DISRUPTION_BUDGET_MINOR_UPGRADE",
            "SYSTEM_CONFIG",
        ]
    ]
    upgradeDetails: _list[UpgradeDetails]

@typing.type_check_only
class CompleteIPRotationRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class CompleteNodePoolUpgradeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CompliancePostureConfig(typing_extensions.TypedDict, total=False):
    complianceStandards: _list[ComplianceStandard]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class ComplianceStandard(typing_extensions.TypedDict, total=False):
    standard: str

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
class ContainerdConfig(typing_extensions.TypedDict, total=False):
    privateRegistryAccessConfig: PrivateRegistryAccessConfig

@typing.type_check_only
class ControlPlaneEndpointsConfig(typing_extensions.TypedDict, total=False):
    dnsEndpointConfig: DNSEndpointConfig
    ipEndpointsConfig: IPEndpointsConfig

@typing.type_check_only
class CostManagementConfig(typing_extensions.TypedDict, total=False):
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
    additiveVpcScopeDnsDomain: str
    clusterDns: typing_extensions.Literal[
        "PROVIDER_UNSPECIFIED", "PLATFORM_DEFAULT", "CLOUD_DNS", "KUBE_DNS"
    ]
    clusterDnsDomain: str
    clusterDnsScope: typing_extensions.Literal[
        "DNS_SCOPE_UNSPECIFIED", "CLUSTER_SCOPE", "VPC_SCOPE"
    ]

@typing.type_check_only
class DNSEndpointConfig(typing_extensions.TypedDict, total=False):
    allowExternalTraffic: bool
    endpoint: str

@typing.type_check_only
class DailyMaintenanceWindow(typing_extensions.TypedDict, total=False):
    duration: str
    startTime: str

@typing.type_check_only
class DatabaseEncryption(typing_extensions.TypedDict, total=False):
    currentState: typing_extensions.Literal[
        "CURRENT_STATE_UNSPECIFIED",
        "CURRENT_STATE_ENCRYPTED",
        "CURRENT_STATE_DECRYPTED",
        "CURRENT_STATE_ENCRYPTION_PENDING",
        "CURRENT_STATE_ENCRYPTION_ERROR",
        "CURRENT_STATE_DECRYPTION_PENDING",
        "CURRENT_STATE_DECRYPTION_ERROR",
    ]
    decryptionKeys: _list[str]
    keyName: str
    lastOperationErrors: _list[OperationError]
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
class DesiredEnterpriseConfig(typing_extensions.TypedDict, total=False):
    desiredTier: typing_extensions.Literal[
        "CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"
    ]

@typing.type_check_only
class DnsCacheConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnterpriseConfig(typing_extensions.TypedDict, total=False):
    clusterTier: typing_extensions.Literal[
        "CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"
    ]
    desiredTier: typing_extensions.Literal[
        "CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"
    ]

@typing.type_check_only
class EphemeralStorageConfig(typing_extensions.TypedDict, total=False):
    localSsdCount: int

@typing.type_check_only
class EphemeralStorageLocalSsdConfig(typing_extensions.TypedDict, total=False):
    localSsdCount: int

@typing.type_check_only
class FastSocket(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Filter(typing_extensions.TypedDict, total=False):
    eventType: _list[
        typing_extensions.Literal[
            "EVENT_TYPE_UNSPECIFIED",
            "UPGRADE_AVAILABLE_EVENT",
            "UPGRADE_EVENT",
            "SECURITY_BULLETIN_EVENT",
        ]
    ]

@typing.type_check_only
class Fleet(typing_extensions.TypedDict, total=False):
    membership: str
    preRegistered: bool
    project: str

@typing.type_check_only
class GCPSecretManagerCertificateConfig(typing_extensions.TypedDict, total=False):
    secretUri: str

@typing.type_check_only
class GPUDriverInstallationConfig(typing_extensions.TypedDict, total=False):
    gpuDriverVersion: typing_extensions.Literal[
        "GPU_DRIVER_VERSION_UNSPECIFIED", "INSTALLATION_DISABLED", "DEFAULT", "LATEST"
    ]

@typing.type_check_only
class GPUSharingConfig(typing_extensions.TypedDict, total=False):
    gpuSharingStrategy: typing_extensions.Literal[
        "GPU_SHARING_STRATEGY_UNSPECIFIED", "TIME_SHARING", "MPS"
    ]
    maxSharedClientsPerGpu: str

@typing.type_check_only
class GatewayAPIConfig(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "CHANNEL_UNSPECIFIED",
        "CHANNEL_DISABLED",
        "CHANNEL_EXPERIMENTAL",
        "CHANNEL_STANDARD",
    ]

@typing.type_check_only
class GcePersistentDiskCsiDriverConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcfsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcpFilestoreCsiDriverConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcsFuseCsiDriverConfig(typing_extensions.TypedDict, total=False):
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
class GkeBackupAgentConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class HorizontalPodAutoscaling(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class HostMaintenancePolicy(typing_extensions.TypedDict, total=False):
    maintenanceInterval: typing_extensions.Literal[
        "MAINTENANCE_INTERVAL_UNSPECIFIED", "AS_NEEDED", "PERIODIC"
    ]
    opportunisticMaintenanceStrategy: OpportunisticMaintenanceStrategy

@typing.type_check_only
class HttpCacheControlResponseHeader(typing_extensions.TypedDict, total=False):
    age: str
    directive: str
    expires: str

@typing.type_check_only
class HttpLoadBalancing(typing_extensions.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class HugepagesConfig(typing_extensions.TypedDict, total=False):
    hugepageSize1g: int
    hugepageSize2m: int

@typing.type_check_only
class ILBSubsettingConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class IPAllocationPolicy(typing_extensions.TypedDict, total=False):
    additionalPodRangesConfig: AdditionalPodRangesConfig
    allowRouteOverlap: bool
    clusterIpv4Cidr: str
    clusterIpv4CidrBlock: str
    clusterSecondaryRangeName: str
    createSubnetwork: bool
    defaultPodIpv4RangeUtilization: float
    ipv6AccessType: typing_extensions.Literal[
        "IPV6_ACCESS_TYPE_UNSPECIFIED", "INTERNAL", "EXTERNAL"
    ]
    nodeIpv4Cidr: str
    nodeIpv4CidrBlock: str
    podCidrOverprovisionConfig: PodCIDROverprovisionConfig
    servicesIpv4Cidr: str
    servicesIpv4CidrBlock: str
    servicesIpv6CidrBlock: str
    servicesSecondaryRangeName: str
    stackType: typing_extensions.Literal["STACK_TYPE_UNSPECIFIED", "IPV4", "IPV4_IPV6"]
    subnetIpv6CidrBlock: str
    subnetworkName: str
    tpuIpv4CidrBlock: str
    useIpAliases: bool
    useRoutes: bool

@typing.type_check_only
class IPEndpointsConfig(typing_extensions.TypedDict, total=False):
    authorizedNetworksConfig: MasterAuthorizedNetworksConfig
    enablePublicEndpoint: bool
    enabled: bool
    globalAccess: bool
    privateEndpoint: str
    privateEndpointSubnetwork: str
    publicEndpoint: str

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
class K8sBetaAPIConfig(typing_extensions.TypedDict, total=False):
    enabledApis: _list[str]

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
    cgroupMode: typing_extensions.Literal[
        "CGROUP_MODE_UNSPECIFIED", "CGROUP_MODE_V1", "CGROUP_MODE_V2"
    ]
    hugepages: HugepagesConfig
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
class LocalNvmeSsdBlockConfig(typing_extensions.TypedDict, total=False):
    localSsdCount: int

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    name: str
    recommended: bool
    type: typing_extensions.Literal["LOCATION_TYPE_UNSPECIFIED", "ZONE", "REGION"]

@typing.type_check_only
class LoggingComponentConfig(typing_extensions.TypedDict, total=False):
    enableComponents: _list[
        typing_extensions.Literal[
            "COMPONENT_UNSPECIFIED",
            "SYSTEM_COMPONENTS",
            "WORKLOADS",
            "APISERVER",
            "SCHEDULER",
            "CONTROLLER_MANAGER",
            "KCP_SSHD",
            "KCP_CONNECTION",
        ]
    ]

@typing.type_check_only
class LoggingConfig(typing_extensions.TypedDict, total=False):
    componentConfig: LoggingComponentConfig

@typing.type_check_only
class LoggingVariantConfig(typing_extensions.TypedDict, total=False):
    variant: typing_extensions.Literal[
        "VARIANT_UNSPECIFIED", "DEFAULT", "MAX_THROUGHPUT"
    ]

@typing.type_check_only
class MaintenanceExclusionOptions(typing_extensions.TypedDict, total=False):
    scope: typing_extensions.Literal[
        "NO_UPGRADES", "NO_MINOR_UPGRADES", "NO_MINOR_OR_NODE_UPGRADES"
    ]

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
class ManagedPrometheusConfig(typing_extensions.TypedDict, total=False):
    autoMonitoringConfig: AutoMonitoringConfig
    enabled: bool

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
    gcpPublicCidrsAccessEnabled: bool
    privateEndpointEnforcementEnabled: bool

@typing.type_check_only
class MaxPodsConstraint(typing_extensions.TypedDict, total=False):
    maxPodsPerNode: str

@typing.type_check_only
class MeshCertificates(typing_extensions.TypedDict, total=False):
    enableCertificates: bool

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    name: str
    stringValue: str

@typing.type_check_only
class MonitoringComponentConfig(typing_extensions.TypedDict, total=False):
    enableComponents: _list[
        typing_extensions.Literal[
            "COMPONENT_UNSPECIFIED",
            "SYSTEM_COMPONENTS",
            "WORKLOADS",
            "APISERVER",
            "SCHEDULER",
            "CONTROLLER_MANAGER",
            "STORAGE",
            "HPA",
            "POD",
            "DAEMONSET",
            "DEPLOYMENT",
            "STATEFULSET",
            "CADVISOR",
            "KUBELET",
            "DCGM",
        ]
    ]

@typing.type_check_only
class MonitoringConfig(typing_extensions.TypedDict, total=False):
    advancedDatapathObservabilityConfig: AdvancedDatapathObservabilityConfig
    componentConfig: MonitoringComponentConfig
    managedPrometheusConfig: ManagedPrometheusConfig

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    datapathProvider: typing_extensions.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    defaultEnablePrivateNodes: bool
    defaultSnatStatus: DefaultSnatStatus
    disableL4LbFirewallReconciliation: bool
    dnsConfig: DNSConfig
    enableCiliumClusterwideNetworkPolicy: bool
    enableFqdnNetworkPolicy: bool
    enableIntraNodeVisibility: bool
    enableL4ilbSubsetting: bool
    enableMultiNetworking: bool
    gatewayApiConfig: GatewayAPIConfig
    inTransitEncryptionConfig: typing_extensions.Literal[
        "IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED",
        "IN_TRANSIT_ENCRYPTION_DISABLED",
        "IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT",
    ]
    network: str
    networkPerformanceConfig: ClusterNetworkPerformanceConfig
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE",
        "PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL",
    ]
    serviceExternalIpsConfig: ServiceExternalIPsConfig
    subnetwork: str

@typing.type_check_only
class NetworkPerformanceConfig(typing_extensions.TypedDict, total=False):
    externalIpEgressBandwidthTier: typing_extensions.Literal[
        "TIER_UNSPECIFIED", "TIER_1"
    ]
    totalEgressBandwidthTier: typing_extensions.Literal["TIER_UNSPECIFIED", "TIER_1"]

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
class NodeAffinity(typing_extensions.TypedDict, total=False):
    key: str
    operator: typing_extensions.Literal["OPERATOR_UNSPECIFIED", "IN", "NOT_IN"]
    values: _list[str]

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    advancedMachineFeatures: AdvancedMachineFeatures
    bootDiskKmsKey: str
    confidentialNodes: ConfidentialNodes
    containerdConfig: ContainerdConfig
    diskSizeGb: int
    diskType: str
    effectiveCgroupMode: typing_extensions.Literal[
        "EFFECTIVE_CGROUP_MODE_UNSPECIFIED",
        "EFFECTIVE_CGROUP_MODE_V1",
        "EFFECTIVE_CGROUP_MODE_V2",
    ]
    enableConfidentialStorage: bool
    ephemeralStorageConfig: EphemeralStorageConfig
    ephemeralStorageLocalSsdConfig: EphemeralStorageLocalSsdConfig
    fastSocket: FastSocket
    gcfsConfig: GcfsConfig
    gvnic: VirtualNIC
    hostMaintenancePolicy: HostMaintenancePolicy
    imageType: str
    kubeletConfig: NodeKubeletConfig
    labels: dict[str, typing.Any]
    linuxNodeConfig: LinuxNodeConfig
    localNvmeSsdBlockConfig: LocalNvmeSsdBlockConfig
    localSsdCount: int
    localSsdEncryptionMode: typing_extensions.Literal[
        "LOCAL_SSD_ENCRYPTION_MODE_UNSPECIFIED",
        "STANDARD_ENCRYPTION",
        "EPHEMERAL_KEY_ENCRYPTION",
    ]
    loggingConfig: NodePoolLoggingConfig
    machineType: str
    maxRunDuration: str
    metadata: dict[str, typing.Any]
    minCpuPlatform: str
    nodeGroup: str
    oauthScopes: _list[str]
    preemptible: bool
    reservationAffinity: ReservationAffinity
    resourceLabels: dict[str, typing.Any]
    resourceManagerTags: ResourceManagerTags
    sandboxConfig: SandboxConfig
    secondaryBootDiskUpdateStrategy: SecondaryBootDiskUpdateStrategy
    secondaryBootDisks: _list[SecondaryBootDisk]
    serviceAccount: str
    shieldedInstanceConfig: ShieldedInstanceConfig
    soleTenantConfig: SoleTenantConfig
    spot: bool
    storagePools: _list[str]
    tags: _list[str]
    taints: _list[NodeTaint]
    windowsNodeConfig: WindowsNodeConfig
    workloadMetadataConfig: WorkloadMetadataConfig

@typing.type_check_only
class NodeConfigDefaults(typing_extensions.TypedDict, total=False):
    containerdConfig: ContainerdConfig
    gcfsConfig: GcfsConfig
    hostMaintenancePolicy: HostMaintenancePolicy
    loggingConfig: NodePoolLoggingConfig
    nodeKubeletConfig: NodeKubeletConfig

@typing.type_check_only
class NodeKubeletConfig(typing_extensions.TypedDict, total=False):
    cpuCfsQuota: bool
    cpuCfsQuotaPeriod: str
    cpuManagerPolicy: str
    insecureKubeletReadonlyPortEnabled: bool
    podPidsLimit: str

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
    additionalNodeNetworkConfigs: _list[AdditionalNodeNetworkConfig]
    additionalPodNetworkConfigs: _list[AdditionalPodNetworkConfig]
    createPodRange: bool
    enablePrivateNodes: bool
    networkPerformanceConfig: NetworkPerformanceConfig
    podCidrOverprovisionConfig: PodCIDROverprovisionConfig
    podIpv4CidrBlock: str
    podIpv4RangeUtilization: float
    podRange: str

@typing.type_check_only
class NodePool(typing_extensions.TypedDict, total=False):
    autoscaling: NodePoolAutoscaling
    bestEffortProvisioning: BestEffortProvisioning
    conditions: _list[StatusCondition]
    config: NodeConfig
    etag: str
    initialNodeCount: int
    instanceGroupUrls: _list[str]
    locations: _list[str]
    management: NodeManagement
    maxPodsConstraint: MaxPodsConstraint
    name: str
    networkConfig: NodeNetworkConfig
    placementPolicy: PlacementPolicy
    podIpv4CidrSize: int
    queuedProvisioning: QueuedProvisioning
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
    updateInfo: UpdateInfo
    upgradeSettings: UpgradeSettings
    version: str

@typing.type_check_only
class NodePoolAutoConfig(typing_extensions.TypedDict, total=False):
    linuxNodeConfig: LinuxNodeConfig
    networkTags: NetworkTags
    nodeKubeletConfig: NodeKubeletConfig
    resourceManagerTags: ResourceManagerTags

@typing.type_check_only
class NodePoolAutoscaling(typing_extensions.TypedDict, total=False):
    autoprovisioned: bool
    enabled: bool
    locationPolicy: typing_extensions.Literal[
        "LOCATION_POLICY_UNSPECIFIED", "BALANCED", "ANY"
    ]
    maxNodeCount: int
    minNodeCount: int
    totalMaxNodeCount: int
    totalMinNodeCount: int

@typing.type_check_only
class NodePoolDefaults(typing_extensions.TypedDict, total=False):
    nodeConfigDefaults: NodeConfigDefaults

@typing.type_check_only
class NodePoolLoggingConfig(typing_extensions.TypedDict, total=False):
    variantConfig: LoggingVariantConfig

@typing.type_check_only
class NodePoolUpgradeInfo(typing_extensions.TypedDict, total=False):
    autoUpgradeStatus: _list[
        typing_extensions.Literal[
            "UNKNOWN", "ACTIVE", "MINOR_UPGRADE_PAUSED", "UPGRADE_PAUSED"
        ]
    ]
    endOfExtendedSupportTimestamp: str
    endOfStandardSupportTimestamp: str
    minorTargetVersion: str
    patchTargetVersion: str
    pausedReason: _list[
        typing_extensions.Literal[
            "AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED",
            "MAINTENANCE_WINDOW",
            "MAINTENANCE_EXCLUSION_NO_UPGRADES",
            "MAINTENANCE_EXCLUSION_NO_MINOR_UPGRADES",
            "SYSTEM_CONFIG",
        ]
    ]
    upgradeDetails: _list[UpgradeDetails]

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
class Operation(typing_extensions.TypedDict, total=False):
    clusterConditions: _list[StatusCondition]
    detail: str
    endTime: str
    error: Status
    location: str
    name: str
    nodepoolConditions: _list[StatusCondition]
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
        "RESIZE_CLUSTER",
        "FLEET_FEATURE_UPGRADE",
    ]
    progress: OperationProgress
    selfLink: str
    startTime: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "ABORTING"
    ]
    statusMessage: str
    targetLink: str
    zone: str

@typing.type_check_only
class OperationError(typing_extensions.TypedDict, total=False):
    errorMessage: str
    keyName: str
    timestamp: str

@typing.type_check_only
class OperationProgress(typing_extensions.TypedDict, total=False):
    metrics: _list[Metric]
    name: str
    stages: _list[OperationProgress]
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "ABORTING"
    ]

@typing.type_check_only
class OpportunisticMaintenanceStrategy(typing_extensions.TypedDict, total=False):
    maintenanceAvailabilityWindow: str
    minNodesPerPool: str
    nodeIdleTimeWindow: str

@typing.type_check_only
class ParallelstoreCsiDriverConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ParentProductConfig(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    productName: str

@typing.type_check_only
class PlacementPolicy(typing_extensions.TypedDict, total=False):
    policyName: str
    tpuTopology: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "COMPACT"]

@typing.type_check_only
class PodAutoscaling(typing_extensions.TypedDict, total=False):
    hpaProfile: typing_extensions.Literal[
        "HPA_PROFILE_UNSPECIFIED", "NONE", "PERFORMANCE"
    ]

@typing.type_check_only
class PodCIDROverprovisionConfig(typing_extensions.TypedDict, total=False):
    disable: bool

@typing.type_check_only
class PodSecurityPolicyConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PolicyBinding(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class PrivateClusterConfig(typing_extensions.TypedDict, total=False):
    enablePrivateEndpoint: bool
    enablePrivateNodes: bool
    masterGlobalAccessConfig: PrivateClusterMasterGlobalAccessConfig
    masterIpv4CidrBlock: str
    peeringName: str
    privateEndpoint: str
    privateEndpointSubnetwork: str
    publicEndpoint: str

@typing.type_check_only
class PrivateClusterMasterGlobalAccessConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PrivateRegistryAccessConfig(typing_extensions.TypedDict, total=False):
    certificateAuthorityDomainConfig: _list[CertificateAuthorityDomainConfig]
    enabled: bool

@typing.type_check_only
class ProtectConfig(typing_extensions.TypedDict, total=False):
    workloadConfig: WorkloadConfig
    workloadVulnerabilityMode: typing_extensions.Literal[
        "WORKLOAD_VULNERABILITY_MODE_UNSPECIFIED", "DISABLED", "BASIC"
    ]

@typing.type_check_only
class PubSub(typing_extensions.TypedDict, total=False):
    enabled: bool
    filter: Filter
    topic: str

@typing.type_check_only
class QueuedProvisioning(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RBACBindingConfig(typing_extensions.TypedDict, total=False):
    enableInsecureBindingSystemAuthenticated: bool
    enableInsecureBindingSystemUnauthenticated: bool

@typing.type_check_only
class RangeInfo(typing_extensions.TypedDict, total=False):
    rangeName: str
    utilization: float

@typing.type_check_only
class RayClusterLoggingConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RayClusterMonitoringConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RayOperatorConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    rayClusterLoggingConfig: RayClusterLoggingConfig
    rayClusterMonitoringConfig: RayClusterMonitoringConfig

@typing.type_check_only
class RecurringTimeWindow(typing_extensions.TypedDict, total=False):
    recurrence: str
    window: TimeWindow

@typing.type_check_only
class ReleaseChannel(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "UNSPECIFIED", "RAPID", "REGULAR", "STABLE", "EXTENDED"
    ]

@typing.type_check_only
class ReleaseChannelConfig(typing_extensions.TypedDict, total=False):
    availableVersions: _list[AvailableVersion]
    channel: typing_extensions.Literal[
        "UNSPECIFIED", "RAPID", "REGULAR", "STABLE", "EXTENDED"
    ]
    defaultVersion: str
    upgradeTargetVersion: str
    validVersions: _list[str]

@typing.type_check_only
class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "UNSPECIFIED", "NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResourceLabels(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class ResourceLimit(typing_extensions.TypedDict, total=False):
    maximum: str
    minimum: str
    resourceType: str

@typing.type_check_only
class ResourceManagerTags(typing_extensions.TypedDict, total=False):
    tags: dict[str, typing.Any]

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
    respectPdb: bool
    zone: str

@typing.type_check_only
class SandboxConfig(typing_extensions.TypedDict, total=False):
    sandboxType: str
    type: typing_extensions.Literal["UNSPECIFIED", "GVISOR"]

@typing.type_check_only
class SecondaryBootDisk(typing_extensions.TypedDict, total=False):
    diskImage: str
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "CONTAINER_IMAGE_CACHE"]

@typing.type_check_only
class SecondaryBootDiskUpdateStrategy(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SecretManagerConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SecurityBulletinEvent(typing_extensions.TypedDict, total=False):
    affectedSupportedMinors: _list[str]
    briefDescription: str
    bulletinId: str
    bulletinUri: str
    cveIds: _list[str]
    manualStepsRequired: bool
    patchedVersions: _list[str]
    resourceTypeAffected: str
    severity: str
    suggestedUpgradeTarget: str

@typing.type_check_only
class SecurityPostureConfig(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "BASIC", "ENTERPRISE"
    ]
    vulnerabilityMode: typing_extensions.Literal[
        "VULNERABILITY_MODE_UNSPECIFIED",
        "VULNERABILITY_DISABLED",
        "VULNERABILITY_BASIC",
        "VULNERABILITY_ENTERPRISE",
    ]

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
class SoleTenantConfig(typing_extensions.TypedDict, total=False):
    nodeAffinities: _list[NodeAffinity]

@typing.type_check_only
class StandardRolloutPolicy(typing_extensions.TypedDict, total=False):
    batchNodeCount: int
    batchPercentage: float
    batchSoakDuration: str

@typing.type_check_only
class StartIPRotationRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    rotateCredentials: bool
    zone: str

@typing.type_check_only
class StatefulHAConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

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
    maintenanceExclusionOptions: MaintenanceExclusionOptions
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
class UpdateInfo(typing_extensions.TypedDict, total=False):
    blueGreenInfo: BlueGreenInfo

@typing.type_check_only
class UpdateMasterRequest(typing_extensions.TypedDict, total=False):
    clusterId: str
    masterVersion: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class UpdateNodePoolRequest(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    clusterId: str
    confidentialNodes: ConfidentialNodes
    containerdConfig: ContainerdConfig
    diskSizeGb: str
    diskType: str
    etag: str
    fastSocket: FastSocket
    gcfsConfig: GcfsConfig
    gvnic: VirtualNIC
    imageType: str
    kubeletConfig: NodeKubeletConfig
    labels: NodeLabels
    linuxNodeConfig: LinuxNodeConfig
    locations: _list[str]
    loggingConfig: NodePoolLoggingConfig
    machineType: str
    maxRunDuration: str
    name: str
    nodeNetworkConfig: NodeNetworkConfig
    nodePoolId: str
    nodeVersion: str
    projectId: str
    queuedProvisioning: QueuedProvisioning
    resourceLabels: ResourceLabels
    resourceManagerTags: ResourceManagerTags
    storagePools: _list[str]
    tags: NetworkTags
    taints: NodeTaints
    upgradeSettings: UpgradeSettings
    windowsNodeConfig: WindowsNodeConfig
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
class UpgradeDetails(typing_extensions.TypedDict, total=False):
    endTime: str
    initialVersion: str
    startTime: str
    state: typing_extensions.Literal[
        "UNKNOWN", "FAILED", "SUCCEEDED", "CANCELED", "RUNNING"
    ]
    targetVersion: str

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
class UpgradeInfoEvent(typing_extensions.TypedDict, total=False):
    currentVersion: str
    description: str
    endTime: str
    eventType: typing_extensions.Literal["EVENT_TYPE_UNSPECIFIED", "END_OF_SUPPORT"]
    extendedSupportEndTime: str
    operation: str
    resource: str
    resourceType: typing_extensions.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    standardSupportEndTime: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STARTED", "SUCCEEDED", "FAILED", "CANCELED"
    ]
    targetVersion: str

@typing.type_check_only
class UpgradeSettings(typing_extensions.TypedDict, total=False):
    blueGreenSettings: BlueGreenSettings
    maxSurge: int
    maxUnavailable: int
    strategy: typing_extensions.Literal[
        "NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED", "BLUE_GREEN", "SURGE"
    ]

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
class UserManagedKeysConfig(typing_extensions.TypedDict, total=False):
    aggregationCa: str
    clusterCa: str
    controlPlaneDiskEncryptionKey: str
    etcdApiCa: str
    etcdPeerCa: str
    gkeopsEtcdBackupEncryptionKey: str
    serviceAccountSigningKeys: _list[str]
    serviceAccountVerificationKeys: _list[str]

@typing.type_check_only
class VerticalPodAutoscaling(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VirtualNIC(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class WindowsNodeConfig(typing_extensions.TypedDict, total=False):
    osVersion: typing_extensions.Literal[
        "OS_VERSION_UNSPECIFIED", "OS_VERSION_LTSC2019", "OS_VERSION_LTSC2022"
    ]

@typing.type_check_only
class WindowsVersion(typing_extensions.TypedDict, total=False):
    imageType: str
    osVersion: str
    supportEndDate: Date

@typing.type_check_only
class WindowsVersions(typing_extensions.TypedDict, total=False):
    windowsVersions: _list[WindowsVersion]

@typing.type_check_only
class WorkloadALTSConfig(typing_extensions.TypedDict, total=False):
    enableAlts: bool

@typing.type_check_only
class WorkloadCertificates(typing_extensions.TypedDict, total=False):
    enableCertificates: bool

@typing.type_check_only
class WorkloadConfig(typing_extensions.TypedDict, total=False):
    auditMode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "BASIC", "BASELINE", "RESTRICTED"
    ]

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

@typing.type_check_only
class WorkloadPolicyConfig(typing_extensions.TypedDict, total=False):
    allowNetAdmin: bool
