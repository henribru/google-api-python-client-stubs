import typing

_list = list

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    acceleratorCount: str
    acceleratorType: str
    gpuDriverInstallationConfig: GPUDriverInstallationConfig
    gpuPartitionSize: str
    gpuSharingConfig: GPUSharingConfig
    maxTimeSharedClientsPerGpu: str

@typing.type_check_only
class AccurateTimeConfig(typing.TypedDict, total=False):
    enablePtpKvmTimeSync: bool

@typing.type_check_only
class AdditionalIPRangesConfig(typing.TypedDict, total=False):
    podIpv4RangeNames: _list[str]
    status: typing.Literal["STATUS_UNSPECIFIED", "ACTIVE", "DRAINING"]
    subnetwork: str

@typing.type_check_only
class AdditionalNodeNetworkConfig(typing.TypedDict, total=False):
    network: str
    subnetwork: str

@typing.type_check_only
class AdditionalPodNetworkConfig(typing.TypedDict, total=False):
    maxPodsPerNode: MaxPodsConstraint
    networkAttachment: str
    secondaryPodRange: str
    subnetwork: str

@typing.type_check_only
class AdditionalPodRangesConfig(typing.TypedDict, total=False):
    podRangeInfo: _list[RangeInfo]
    podRangeNames: _list[str]

@typing.type_check_only
class AddonsConfig(typing.TypedDict, total=False):
    agentSandboxConfig: AgentSandboxConfig
    cloudRunConfig: CloudRunConfig
    configConnectorConfig: ConfigConnectorConfig
    dnsCacheConfig: DnsCacheConfig
    gcePersistentDiskCsiDriverConfig: GcePersistentDiskCsiDriverConfig
    gcpFilestoreCsiDriverConfig: GcpFilestoreCsiDriverConfig
    gcsFuseCsiDriverConfig: GcsFuseCsiDriverConfig
    gkeBackupAgentConfig: GkeBackupAgentConfig
    highScaleCheckpointingConfig: HighScaleCheckpointingConfig
    horizontalPodAutoscaling: HorizontalPodAutoscaling
    httpLoadBalancing: HttpLoadBalancing
    istioConfig: IstioConfig
    kalmConfig: KalmConfig
    kubernetesDashboard: KubernetesDashboard
    lustreCsiDriverConfig: LustreCsiDriverConfig
    networkPolicyConfig: NetworkPolicyConfig
    nodeReadinessConfig: NodeReadinessConfig
    parallelstoreCsiDriverConfig: ParallelstoreCsiDriverConfig
    podSnapshotConfig: PodSnapshotConfig
    rayOperatorConfig: RayOperatorConfig
    sliceControllerConfig: SliceControllerConfig
    slurmOperatorConfig: SlurmOperatorConfig
    statefulHaConfig: StatefulHAConfig

@typing.type_check_only
class AdvancedDatapathObservabilityConfig(typing.TypedDict, total=False):
    enableMetrics: bool
    enableRelay: bool
    relayMode: typing.Literal[
        "RELAY_MODE_UNSPECIFIED", "DISABLED", "INTERNAL_VPC_LB", "EXTERNAL_LB"
    ]

@typing.type_check_only
class AdvancedMachineFeatures(typing.TypedDict, total=False):
    enableNestedVirtualization: bool
    performanceMonitoringUnit: typing.Literal[
        "PERFORMANCE_MONITORING_UNIT_UNSPECIFIED",
        "ARCHITECTURAL",
        "STANDARD",
        "ENHANCED",
    ]
    threadsPerCore: str

@typing.type_check_only
class AgentSandboxConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AnonymousAuthenticationConfig(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "ENABLED", "LIMITED"]

@typing.type_check_only
class AuthenticatorGroupsConfig(typing.TypedDict, total=False):
    enabled: bool
    securityGroup: str

@typing.type_check_only
class AutoIpamConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AutoMonitoringConfig(typing.TypedDict, total=False):
    scope: typing.Literal["SCOPE_UNSPECIFIED", "ALL", "NONE"]

@typing.type_check_only
class AutoUpgradeOptions(typing.TypedDict, total=False):
    autoUpgradeStartTime: str
    description: str

@typing.type_check_only
class Autopilot(typing.TypedDict, total=False):
    clusterPolicyConfig: ClusterPolicyConfig
    conversionStatus: AutopilotConversionStatus
    enabled: bool
    privilegedAdmissionConfig: PrivilegedAdmissionConfig
    workloadPolicyConfig: WorkloadPolicyConfig

@typing.type_check_only
class AutopilotCompatibilityIssue(typing.TypedDict, total=False):
    constraintType: str
    description: str
    documentationUrl: str
    incompatibilityType: typing.Literal[
        "UNSPECIFIED",
        "INCOMPATIBILITY",
        "ADDITIONAL_CONFIG_REQUIRED",
        "PASSED_WITH_OPTIONAL_CONFIG",
    ]
    lastObservation: str
    subjects: _list[str]

@typing.type_check_only
class AutopilotConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class AutopilotConversionStatus(typing.TypedDict, total=False):
    state: typing.Literal["STATE_UNSPECIFIED", "DONE"]

@typing.type_check_only
class AutoprovisioningNodePoolDefaults(typing.TypedDict, total=False):
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
class AutoscaledRolloutPolicy(typing.TypedDict, total=False):
    waitForDrainDuration: str

@typing.type_check_only
class AvailableVersion(typing.TypedDict, total=False):
    reason: str
    version: str

@typing.type_check_only
class BestEffortProvisioning(typing.TypedDict, total=False):
    enabled: bool
    minProvisionNodes: int

@typing.type_check_only
class BigQueryDestination(typing.TypedDict, total=False):
    datasetId: str

@typing.type_check_only
class BinaryAuthorization(typing.TypedDict, total=False):
    enabled: bool
    evaluationMode: typing.Literal[
        "EVALUATION_MODE_UNSPECIFIED",
        "DISABLED",
        "PROJECT_SINGLETON_POLICY_ENFORCE",
        "POLICY_BINDINGS",
        "POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE",
    ]
    policyBindings: _list[PolicyBinding]

@typing.type_check_only
class BlueGreenInfo(typing.TypedDict, total=False):
    blueInstanceGroupUrls: _list[str]
    bluePoolDeletionStartTime: str
    greenInstanceGroupUrls: _list[str]
    greenPoolVersion: str
    phase: typing.Literal[
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
class BlueGreenSettings(typing.TypedDict, total=False):
    autoscaledRolloutPolicy: AutoscaledRolloutPolicy
    nodePoolSoakDuration: str
    standardRolloutPolicy: StandardRolloutPolicy

@typing.type_check_only
class BootDisk(typing.TypedDict, total=False):
    diskType: str
    provisionedIops: str
    provisionedThroughput: str
    sizeGb: str

@typing.type_check_only
class BootDiskProfile(typing.TypedDict, total=False):
    swapSizeGib: str
    swapSizePercent: int

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False):
    name: str
    operationId: str
    projectId: str
    zone: str

@typing.type_check_only
class CertificateAuthorityDomainConfig(typing.TypedDict, total=False):
    fqdns: _list[str]
    gcpSecretManagerCertificateConfig: GCPSecretManagerCertificateConfig

@typing.type_check_only
class CertificateConfig(typing.TypedDict, total=False):
    gcpSecretManagerSecretUri: str

@typing.type_check_only
class CertificateConfigPair(typing.TypedDict, total=False):
    cert: CertificateConfig
    key: CertificateConfig

@typing.type_check_only
class CheckAutopilotCompatibilityResponse(typing.TypedDict, total=False):
    issues: _list[AutopilotCompatibilityIssue]
    summary: str

@typing.type_check_only
class CidrBlock(typing.TypedDict, total=False):
    cidrBlock: str
    displayName: str

@typing.type_check_only
class ClientCertificateConfig(typing.TypedDict, total=False):
    issueClientCertificate: bool

@typing.type_check_only
class CloudRunConfig(typing.TypedDict, total=False):
    disabled: bool
    loadBalancerType: typing.Literal[
        "LOAD_BALANCER_TYPE_UNSPECIFIED",
        "LOAD_BALANCER_TYPE_EXTERNAL",
        "LOAD_BALANCER_TYPE_INTERNAL",
    ]

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    addonsConfig: AddonsConfig
    alphaClusterFeatureGates: _list[str]
    anonymousAuthenticationConfig: AnonymousAuthenticationConfig
    authenticatorGroupsConfig: AuthenticatorGroupsConfig
    autopilot: Autopilot
    autoscaling: ClusterAutoscaling
    binaryAuthorization: BinaryAuthorization
    clusterIpv4Cidr: str
    clusterTelemetry: ClusterTelemetry
    compliancePostureConfig: CompliancePostureConfig
    conditions: _list[StatusCondition]
    confidentialNodes: ConfidentialNodes
    controlPlaneEgress: ControlPlaneEgress
    controlPlaneEndpointsConfig: ControlPlaneEndpointsConfig
    costManagementConfig: CostManagementConfig
    createTime: str
    currentEmulatedVersion: str
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
    gkeAutoUpgradeConfig: GkeAutoUpgradeConfig
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
    managedMachineLearningDiagnosticsConfig: ManagedMachineLearningDiagnosticsConfig
    managedOpentelemetryConfig: ManagedOpenTelemetryConfig
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
    nodeCreationConfig: NodeCreationConfig
    nodeIpv4CidrSize: int
    nodePoolAutoConfig: NodePoolAutoConfig
    nodePoolDefaults: NodePoolDefaults
    nodePoolUpgradeConcurrencyConfig: NodePoolUpgradeConcurrencyConfig
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
    rollbackSafeUpgrade: RollbackSafeUpgrade
    satisfiesPzi: bool
    satisfiesPzs: bool
    scheduleUpgradeConfig: ScheduleUpgradeConfig
    secretManagerConfig: SecretManagerConfig
    secretSyncConfig: SecretSyncConfig
    securityPostureConfig: SecurityPostureConfig
    selfLink: str
    servicesIpv4Cidr: str
    shieldedNodes: ShieldedNodes
    status: typing.Literal[
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
class ClusterAutoscaling(typing.TypedDict, total=False):
    autopilotGeneralProfile: typing.Literal[
        "AUTOPILOT_GENERAL_PROFILE_UNSPECIFIED", "NO_PERFORMANCE", "NONE"
    ]
    autoprovisioningLocations: _list[str]
    autoprovisioningNodePoolDefaults: AutoprovisioningNodePoolDefaults
    autoscalingProfile: typing.Literal[
        "PROFILE_UNSPECIFIED", "OPTIMIZE_UTILIZATION", "BALANCED"
    ]
    defaultComputeClassConfig: DefaultComputeClassConfig
    enableNodeAutoprovisioning: bool
    resourceLimits: _list[ResourceLimit]

@typing.type_check_only
class ClusterNetworkPerformanceConfig(typing.TypedDict, total=False):
    totalEgressBandwidthTier: typing.Literal["TIER_UNSPECIFIED", "TIER_1"]

@typing.type_check_only
class ClusterPolicyConfig(typing.TypedDict, total=False):
    noStandardNodePools: bool
    noSystemImpersonation: bool
    noSystemMutation: bool
    noUnsafeWebhooks: bool

@typing.type_check_only
class ClusterTelemetry(typing.TypedDict, total=False):
    type: typing.Literal["UNSPECIFIED", "DISABLED", "ENABLED", "SYSTEM_ONLY"]

@typing.type_check_only
class ClusterUpdate(typing.TypedDict, total=False):
    additionalPodRangesConfig: AdditionalPodRangesConfig
    desiredAdditionalIpRangesConfig: DesiredAdditionalIPRangesConfig
    desiredAddonsConfig: AddonsConfig
    desiredAnonymousAuthenticationConfig: AnonymousAuthenticationConfig
    desiredAuthenticatorGroupsConfig: AuthenticatorGroupsConfig
    desiredAutoIpamConfig: AutoIpamConfig
    desiredAutopilotClusterPolicyConfig: ClusterPolicyConfig
    desiredAutopilotWorkloadPolicyConfig: WorkloadPolicyConfig
    desiredBinaryAuthorization: BinaryAuthorization
    desiredClusterAutoscaling: ClusterAutoscaling
    desiredClusterTelemetry: ClusterTelemetry
    desiredCompliancePostureConfig: CompliancePostureConfig
    desiredContainerdConfig: ContainerdConfig
    desiredControlPlaneEgress: ControlPlaneEgress
    desiredControlPlaneEndpointsConfig: ControlPlaneEndpointsConfig
    desiredCostManagementConfig: CostManagementConfig
    desiredDatabaseEncryption: DatabaseEncryption
    desiredDatapathProvider: typing.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    desiredDefaultEnablePrivateNodes: bool
    desiredDefaultSnatStatus: DefaultSnatStatus
    desiredDisableL4LbFirewallReconciliation: bool
    desiredDnsConfig: DNSConfig
    desiredEmulatedVersion: str
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
    desiredImage: str
    desiredImageProject: str
    desiredImageType: str
    desiredInTransitEncryptionConfig: typing.Literal[
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
    desiredManagedMachineLearningDiagnosticsConfig: (
        ManagedMachineLearningDiagnosticsConfig
    )
    desiredManagedOpentelemetryConfig: ManagedOpenTelemetryConfig
    desiredMaster: Master
    desiredMasterAuthorizedNetworksConfig: MasterAuthorizedNetworksConfig
    desiredMasterVersion: str
    desiredMeshCertificates: MeshCertificates
    desiredMonitoringConfig: MonitoringConfig
    desiredMonitoringService: str
    desiredNetworkPerformanceConfig: ClusterNetworkPerformanceConfig
    desiredNetworkTierConfig: NetworkTierConfig
    desiredNodeCreationConfig: NodeCreationConfig
    desiredNodeKubeletConfig: NodeKubeletConfig
    desiredNodePoolAutoConfigKubeletConfig: NodeKubeletConfig
    desiredNodePoolAutoConfigLinuxNodeConfig: LinuxNodeConfig
    desiredNodePoolAutoConfigNetworkTags: NetworkTags
    desiredNodePoolAutoConfigResourceManagerTags: ResourceManagerTags
    desiredNodePoolAutoscaling: NodePoolAutoscaling
    desiredNodePoolId: str
    desiredNodePoolLoggingConfig: NodePoolLoggingConfig
    desiredNodePoolUpgradeConcurrencyConfig: NodePoolUpgradeConcurrencyConfig
    desiredNodeVersion: str
    desiredNotificationConfig: NotificationConfig
    desiredParentProductConfig: ParentProductConfig
    desiredPodAutoscaling: PodAutoscaling
    desiredPodSecurityPolicyConfig: PodSecurityPolicyConfig
    desiredPrivateClusterConfig: PrivateClusterConfig
    desiredPrivateIpv6GoogleAccess: typing.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE",
        "PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL",
    ]
    desiredPrivilegedAdmissionConfig: PrivilegedAdmissionConfig
    desiredProtectConfig: ProtectConfig
    desiredRbacBindingConfig: RBACBindingConfig
    desiredReleaseChannel: ReleaseChannel
    desiredResourceUsageExportConfig: ResourceUsageExportConfig
    desiredRollbackSafeUpgrade: RollbackSafeUpgrade
    desiredScheduleUpgradeConfig: ScheduleUpgradeConfig
    desiredSecretManagerConfig: SecretManagerConfig
    desiredSecretSyncConfig: SecretSyncConfig
    desiredSecurityPostureConfig: SecurityPostureConfig
    desiredServiceExternalIpsConfig: ServiceExternalIPsConfig
    desiredShieldedNodes: ShieldedNodes
    desiredStackType: typing.Literal["STACK_TYPE_UNSPECIFIED", "IPV4", "IPV4_IPV6"]
    desiredTpuConfig: TpuConfig
    desiredUserManagedKeysConfig: UserManagedKeysConfig
    desiredVerticalPodAutoscaling: VerticalPodAutoscaling
    desiredWorkloadAltsConfig: WorkloadALTSConfig
    desiredWorkloadCertificates: WorkloadCertificates
    desiredWorkloadIdentityConfig: WorkloadIdentityConfig
    enableK8sBetaApis: K8sBetaAPIConfig
    etag: str
    gkeAutoUpgradeConfig: GkeAutoUpgradeConfig
    privateClusterConfig: PrivateClusterConfig
    removedAdditionalPodRangesConfig: AdditionalPodRangesConfig
    userManagedKeysConfig: UserManagedKeysConfig

@typing.type_check_only
class ClusterUpgradeInfo(typing.TypedDict, total=False):
    autoUpgradeStatus: _list[
        typing.Literal["UNKNOWN", "ACTIVE", "MINOR_UPGRADE_PAUSED", "UPGRADE_PAUSED"]
    ]
    endOfExtendedSupportTimestamp: str
    endOfStandardSupportTimestamp: str
    minorTargetVersion: str
    patchTargetVersion: str
    pausedReason: _list[
        typing.Literal[
            "AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED",
            "MAINTENANCE_WINDOW",
            "MAINTENANCE_EXCLUSION_NO_UPGRADES",
            "MAINTENANCE_EXCLUSION_NO_MINOR_UPGRADES",
            "CLUSTER_DISRUPTION_BUDGET",
            "CLUSTER_DISRUPTION_BUDGET_MINOR_UPGRADE",
            "SYSTEM_CONFIG",
        ]
    ]
    rollbackSafeUpgradeStatus: RollbackSafeUpgradeStatus
    upgradeDetails: _list[UpgradeDetails]

@typing.type_check_only
class CompatibilityStatus(typing.TypedDict, total=False):
    downgradableVersion: str
    emulatedVersionTime: str

@typing.type_check_only
class CompleteControlPlaneUpgradeRequest(typing.TypedDict, total=False):
    version: str

@typing.type_check_only
class CompleteIPRotationRequest(typing.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class CompleteNodePoolUpgradeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CompliancePostureConfig(typing.TypedDict, total=False):
    complianceStandards: _list[ComplianceStandard]
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class ComplianceStandard(typing.TypedDict, total=False):
    standard: str

@typing.type_check_only
class ConfidentialNodes(typing.TypedDict, total=False):
    confidentialInstanceType: typing.Literal[
        "CONFIDENTIAL_INSTANCE_TYPE_UNSPECIFIED", "SEV", "SEV_SNP", "TDX"
    ]
    enabled: bool

@typing.type_check_only
class ConfigConnectorConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ConsumptionMeteringConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ContainerdConfig(typing.TypedDict, total=False):
    privateRegistryAccessConfig: PrivateRegistryAccessConfig
    registryHosts: _list[RegistryHostConfig]
    writableCgroups: WritableCgroups

@typing.type_check_only
class ControlPlaneEgress(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "VIA_CONTROL_PLANE", "NONE"]

@typing.type_check_only
class ControlPlaneEndpointsConfig(typing.TypedDict, total=False):
    dnsEndpointConfig: DNSEndpointConfig
    ipEndpointsConfig: IPEndpointsConfig

@typing.type_check_only
class CostManagementConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class CrashLoopBackOffConfig(typing.TypedDict, total=False):
    maxContainerRestartPeriod: str

@typing.type_check_only
class CreateClusterRequest(typing.TypedDict, total=False):
    cluster: Cluster
    parent: str
    projectId: str
    zone: str

@typing.type_check_only
class CreateNodePoolRequest(typing.TypedDict, total=False):
    clusterId: str
    nodePool: NodePool
    parent: str
    projectId: str
    zone: str

@typing.type_check_only
class CustomImageConfig(typing.TypedDict, total=False):
    image: str
    imageProject: str

@typing.type_check_only
class CustomImageInfo(typing.TypedDict, total=False):
    upgradeMessage: str

@typing.type_check_only
class CustomNodeInit(typing.TypedDict, total=False):
    initScript: InitScript

@typing.type_check_only
class DNSConfig(typing.TypedDict, total=False):
    additiveVpcScopeDnsDomain: str
    clusterDns: typing.Literal[
        "PROVIDER_UNSPECIFIED", "PLATFORM_DEFAULT", "CLOUD_DNS", "KUBE_DNS"
    ]
    clusterDnsDomain: str
    clusterDnsScope: typing.Literal[
        "DNS_SCOPE_UNSPECIFIED", "CLUSTER_SCOPE", "VPC_SCOPE"
    ]

@typing.type_check_only
class DNSEndpointConfig(typing.TypedDict, total=False):
    allowExternalTraffic: bool
    enableK8sCertsViaDns: bool
    enableK8sTokensViaDns: bool
    endpoint: str

@typing.type_check_only
class DailyMaintenanceWindow(typing.TypedDict, total=False):
    duration: str
    startTime: str

@typing.type_check_only
class DatabaseEncryption(typing.TypedDict, total=False):
    currentState: typing.Literal[
        "CURRENT_STATE_UNSPECIFIED",
        "CURRENT_STATE_ENCRYPTED",
        "CURRENT_STATE_DECRYPTED",
        "CURRENT_STATE_ENCRYPTION_PENDING",
        "CURRENT_STATE_ENCRYPTION_ERROR",
        "CURRENT_STATE_DECRYPTION_PENDING",
        "CURRENT_STATE_DECRYPTION_ERROR",
        "CURRENT_STATE_ALL_OBJECTS_ENCRYPTION_ENABLED",
        "CURRENT_STATE_ALL_OBJECTS_ENCRYPTION_PENDING",
        "CURRENT_STATE_ALL_OBJECTS_ENCRYPTION_ERROR",
    ]
    decryptionKeys: _list[str]
    keyName: str
    lastOperationErrors: _list[OperationError]
    state: typing.Literal[
        "UNKNOWN", "ENCRYPTED", "DECRYPTED", "ALL_OBJECTS_ENCRYPTION_ENABLED"
    ]

@typing.type_check_only
class DataplaneV2Config(typing.TypedDict, total=False):
    scalabilityMode: typing.Literal[
        "SCALABILITY_MODE_UNSPECIFIED", "DISABLED", "SCALE_OPTIMIZED"
    ]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DedicatedLocalSsdProfile(typing.TypedDict, total=False):
    diskCount: str

@typing.type_check_only
class DefaultComputeClassConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class DefaultSnatStatus(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class DesiredAdditionalIPRangesConfig(typing.TypedDict, total=False):
    additionalIpRangesConfigs: _list[AdditionalIPRangesConfig]

@typing.type_check_only
class DesiredEnterpriseConfig(typing.TypedDict, total=False):
    desiredTier: typing.Literal["CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"]

@typing.type_check_only
class DiskIoScheduler(typing.TypedDict, total=False):
    nodeAttachedDiskIoScheduler: str
    nodeSystemIoScheduler: str

@typing.type_check_only
class DisruptionBudget(typing.TypedDict, total=False):
    lastDisruptionTime: str
    lastMinorVersionDisruptionTime: str
    minorVersionDisruptionInterval: str
    patchVersionDisruptionInterval: str

@typing.type_check_only
class DisruptionEvent(typing.TypedDict, total=False):
    disruptionType: typing.Literal[
        "DISRUPTION_TYPE_UNSPECIFIED", "POD_NOT_ENOUGH_PDB", "POD_PDB_VIOLATION"
    ]
    pdbBlockedNode: str
    pdbBlockedPod: _list[PdbBlockedPod]
    pdbViolationTimeout: str

@typing.type_check_only
class DnsCacheConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfig(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class EnterpriseConfig(typing.TypedDict, total=False):
    clusterTier: typing.Literal["CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"]
    desiredTier: typing.Literal["CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"]

@typing.type_check_only
class EphemeralLocalSsdProfile(typing.TypedDict, total=False):
    swapSizeGib: str
    swapSizePercent: int

@typing.type_check_only
class EphemeralStorageConfig(typing.TypedDict, total=False):
    localSsdCount: int

@typing.type_check_only
class EphemeralStorageLocalSsdConfig(typing.TypedDict, total=False):
    dataCacheCount: int
    localSsdCount: int

@typing.type_check_only
class EvictionGracePeriod(typing.TypedDict, total=False):
    imagefsAvailable: str
    imagefsInodesFree: str
    memoryAvailable: str
    nodefsAvailable: str
    nodefsInodesFree: str
    pidAvailable: str

@typing.type_check_only
class EvictionMinimumReclaim(typing.TypedDict, total=False):
    imagefsAvailable: str
    imagefsInodesFree: str
    memoryAvailable: str
    nodefsAvailable: str
    nodefsInodesFree: str
    pidAvailable: str

@typing.type_check_only
class EvictionSignals(typing.TypedDict, total=False):
    imagefsAvailable: str
    imagefsInodesFree: str
    memoryAvailable: str
    nodefsAvailable: str
    nodefsInodesFree: str
    pidAvailable: str

@typing.type_check_only
class ExclusionUntilEndOfSupport(typing.TypedDict, total=False):
    enabled: bool
    endTime: str
    startTime: str

@typing.type_check_only
class FastSocket(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    eventType: _list[
        typing.Literal[
            "EVENT_TYPE_UNSPECIFIED",
            "UPGRADE_AVAILABLE_EVENT",
            "UPGRADE_EVENT",
            "SECURITY_BULLETIN_EVENT",
            "UPGRADE_INFO_EVENT",
        ]
    ]

@typing.type_check_only
class Fleet(typing.TypedDict, total=False):
    membership: str
    membershipType: typing.Literal["MEMBERSHIP_TYPE_UNSPECIFIED", "LIGHTWEIGHT"]
    preRegistered: bool
    project: str

@typing.type_check_only
class GCPSecretManagerCertificateConfig(typing.TypedDict, total=False):
    secretUri: str

@typing.type_check_only
class GPUDirectConfig(typing.TypedDict, total=False):
    gpuDirectStrategy: typing.Literal["GPU_DIRECT_STRATEGY_UNSPECIFIED", "RDMA"]

@typing.type_check_only
class GPUDriverInstallationConfig(typing.TypedDict, total=False):
    gpuDriverVersion: typing.Literal[
        "GPU_DRIVER_VERSION_UNSPECIFIED", "INSTALLATION_DISABLED", "DEFAULT", "LATEST"
    ]

@typing.type_check_only
class GPUSharingConfig(typing.TypedDict, total=False):
    gpuSharingStrategy: typing.Literal[
        "GPU_SHARING_STRATEGY_UNSPECIFIED", "TIME_SHARING", "MPS"
    ]
    maxSharedClientsPerGpu: str

@typing.type_check_only
class GatewayAPIConfig(typing.TypedDict, total=False):
    channel: typing.Literal[
        "CHANNEL_UNSPECIFIED",
        "CHANNEL_DISABLED",
        "CHANNEL_EXPERIMENTAL",
        "CHANNEL_STANDARD",
    ]

@typing.type_check_only
class GcePersistentDiskCsiDriverConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcfsConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcpFilestoreCsiDriverConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GcsFuseCsiDriverConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GetJSONWebKeysResponse(typing.TypedDict, total=False):
    cacheHeader: HttpCacheControlResponseHeader
    keys: _list[Jwk]

@typing.type_check_only
class GetOpenIDConfigResponse(typing.TypedDict, total=False):
    cacheHeader: HttpCacheControlResponseHeader
    claims_supported: _list[str]
    grant_types: _list[str]
    id_token_signing_alg_values_supported: _list[str]
    issuer: str
    jwks_uri: str
    response_types_supported: _list[str]
    subject_types_supported: _list[str]

@typing.type_check_only
class GkeAutoUpgradeConfig(typing.TypedDict, total=False):
    patchMode: typing.Literal["PATCH_MODE_UNSPECIFIED", "ACCELERATED"]

@typing.type_check_only
class GkeBackupAgentConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class HighScaleCheckpointingConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class HorizontalPodAutoscaling(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class HostConfig(typing.TypedDict, total=False):
    ca: _list[CertificateConfig]
    capabilities: _list[
        typing.Literal[
            "HOST_CAPABILITY_UNSPECIFIED",
            "HOST_CAPABILITY_PULL",
            "HOST_CAPABILITY_RESOLVE",
            "HOST_CAPABILITY_PUSH",
        ]
    ]
    client: _list[CertificateConfigPair]
    dialTimeout: str
    header: _list[RegistryHeader]
    host: str
    overridePath: bool

@typing.type_check_only
class HostMaintenancePolicy(typing.TypedDict, total=False):
    maintenanceInterval: typing.Literal[
        "MAINTENANCE_INTERVAL_UNSPECIFIED", "AS_NEEDED", "PERIODIC"
    ]
    opportunisticMaintenanceStrategy: OpportunisticMaintenanceStrategy

@typing.type_check_only
class HttpCacheControlResponseHeader(typing.TypedDict, total=False):
    age: str
    directive: str
    expires: str

@typing.type_check_only
class HttpLoadBalancing(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class HugepagesConfig(typing.TypedDict, total=False):
    hugepageSize1g: int
    hugepageSize2m: int

@typing.type_check_only
class ILBSubsettingConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class IPAllocationPolicy(typing.TypedDict, total=False):
    additionalIpRangesConfigs: _list[AdditionalIPRangesConfig]
    additionalPodRangesConfig: AdditionalPodRangesConfig
    allowRouteOverlap: bool
    autoIpamConfig: AutoIpamConfig
    clusterIpv4Cidr: str
    clusterIpv4CidrBlock: str
    clusterSecondaryRangeName: str
    createSubnetwork: bool
    defaultPodIpv4RangeUtilization: float
    ipv6AccessType: typing.Literal[
        "IPV6_ACCESS_TYPE_UNSPECIFIED", "INTERNAL", "EXTERNAL"
    ]
    networkTierConfig: NetworkTierConfig
    nodeIpv4Cidr: str
    nodeIpv4CidrBlock: str
    podCidrOverprovisionConfig: PodCIDROverprovisionConfig
    servicesIpv4Cidr: str
    servicesIpv4CidrBlock: str
    servicesIpv6CidrBlock: str
    servicesSecondaryRangeName: str
    stackType: typing.Literal["STACK_TYPE_UNSPECIFIED", "IPV4", "IPV4_IPV6"]
    subnetIpv6CidrBlock: str
    subnetworkName: str
    tpuIpv4CidrBlock: str
    useIpAliases: bool
    useRoutes: bool

@typing.type_check_only
class IPEndpointsConfig(typing.TypedDict, total=False):
    authorizedNetworksConfig: MasterAuthorizedNetworksConfig
    enablePublicEndpoint: bool
    enabled: bool
    globalAccess: bool
    privateEndpoint: str
    privateEndpointSubnetwork: str
    publicEndpoint: str

@typing.type_check_only
class IdentityServiceConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class InitScript(typing.TypedDict, total=False):
    args: _list[str]
    gcpSecretManagerSecretUri: str
    gcsGeneration: str
    gcsUri: str

@typing.type_check_only
class IntraNodeVisibilityConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class IstioConfig(typing.TypedDict, total=False):
    auth: typing.Literal["AUTH_NONE", "AUTH_MUTUAL_TLS"]
    disabled: bool

@typing.type_check_only
class Jwk(typing.TypedDict, total=False):
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
class K8sBetaAPIConfig(typing.TypedDict, total=False):
    enabledApis: _list[str]

@typing.type_check_only
class KalmConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class KubeletCertInfo(typing.TypedDict, total=False):
    nonTpmBootstrapCertExpireTime: str
    tpmBootstrapCertExpireTime: str

@typing.type_check_only
class KubernetesDashboard(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class LegacyAbac(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class LinuxNodeConfig(typing.TypedDict, total=False):
    accurateTimeConfig: AccurateTimeConfig
    cgroupMode: typing.Literal[
        "CGROUP_MODE_UNSPECIFIED", "CGROUP_MODE_V1", "CGROUP_MODE_V2"
    ]
    customNodeInit: CustomNodeInit
    diskIoScheduler: DiskIoScheduler
    hugepages: HugepagesConfig
    nodeKernelModuleLoading: NodeKernelModuleLoading
    nodeVfioConfig: NodeVfioConfig
    swapConfig: SwapConfig
    sysctls: dict[str, typing.Any]
    transparentHugepageDefrag: typing.Literal[
        "TRANSPARENT_HUGEPAGE_DEFRAG_UNSPECIFIED",
        "TRANSPARENT_HUGEPAGE_DEFRAG_ALWAYS",
        "TRANSPARENT_HUGEPAGE_DEFRAG_DEFER",
        "TRANSPARENT_HUGEPAGE_DEFRAG_DEFER_WITH_MADVISE",
        "TRANSPARENT_HUGEPAGE_DEFRAG_MADVISE",
        "TRANSPARENT_HUGEPAGE_DEFRAG_NEVER",
    ]
    transparentHugepageEnabled: typing.Literal[
        "TRANSPARENT_HUGEPAGE_ENABLED_UNSPECIFIED",
        "TRANSPARENT_HUGEPAGE_ENABLED_ALWAYS",
        "TRANSPARENT_HUGEPAGE_ENABLED_MADVISE",
        "TRANSPARENT_HUGEPAGE_ENABLED_NEVER",
    ]

@typing.type_check_only
class ListClustersResponse(typing.TypedDict, total=False):
    clusters: _list[Cluster]
    missingZones: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNodePoolsResponse(typing.TypedDict, total=False):
    nodePools: _list[NodePool]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    missingZones: _list[str]
    operations: _list[Operation]

@typing.type_check_only
class ListUsableSubnetworksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subnetworks: _list[UsableSubnetwork]

@typing.type_check_only
class LocalNvmeSsdBlockConfig(typing.TypedDict, total=False):
    localSsdCount: int

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    name: str
    recommended: bool
    type: typing.Literal["LOCATION_TYPE_UNSPECIFIED", "ZONE", "REGION"]

@typing.type_check_only
class LoggingComponentConfig(typing.TypedDict, total=False):
    enableComponents: _list[
        typing.Literal[
            "COMPONENT_UNSPECIFIED",
            "SYSTEM_COMPONENTS",
            "WORKLOADS",
            "APISERVER",
            "SCHEDULER",
            "CONTROLLER_MANAGER",
            "KCP_SSHD",
            "KCP_CONNECTION",
            "KCP_HPA",
            "KCP_VPA",
        ]
    ]

@typing.type_check_only
class LoggingConfig(typing.TypedDict, total=False):
    componentConfig: LoggingComponentConfig

@typing.type_check_only
class LoggingVariantConfig(typing.TypedDict, total=False):
    variant: typing.Literal["VARIANT_UNSPECIFIED", "DEFAULT", "MAX_THROUGHPUT"]

@typing.type_check_only
class LustreCsiDriverConfig(typing.TypedDict, total=False):
    disableMultiNic: bool
    enableLegacyLustrePort: bool
    enabled: bool

@typing.type_check_only
class MaintenanceExclusionOptions(typing.TypedDict, total=False):
    endTimeBehavior: typing.Literal[
        "END_TIME_BEHAVIOR_UNSPECIFIED", "UNTIL_END_OF_SUPPORT"
    ]
    scope: typing.Literal[
        "NO_UPGRADES", "NO_MINOR_UPGRADES", "NO_MINOR_OR_NODE_UPGRADES"
    ]

@typing.type_check_only
class MaintenancePolicy(typing.TypedDict, total=False):
    disruptionBudget: DisruptionBudget
    resourceVersion: str
    window: MaintenanceWindow

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    dailyMaintenanceWindow: DailyMaintenanceWindow
    maintenanceExclusions: dict[str, typing.Any]
    recurringMaintenanceWindow: RecurringMaintenanceWindow
    recurringWindow: RecurringTimeWindow

@typing.type_check_only
class ManagedMachineLearningDiagnosticsConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ManagedOpenTelemetryConfig(typing.TypedDict, total=False):
    scope: typing.Literal[
        "SCOPE_UNSPECIFIED", "NONE", "COLLECTION_AND_INSTRUMENTATION_COMPONENTS"
    ]

@typing.type_check_only
class ManagedPrometheusConfig(typing.TypedDict, total=False):
    autoMonitoringConfig: AutoMonitoringConfig
    enabled: bool

@typing.type_check_only
class Master(typing.TypedDict, total=False):
    compatibilityStatus: CompatibilityStatus

@typing.type_check_only
class MasterAuth(typing.TypedDict, total=False):
    clientCertificate: str
    clientCertificateConfig: ClientCertificateConfig
    clientKey: str
    clusterCaCertificate: str
    password: str
    username: str

@typing.type_check_only
class MasterAuthorizedNetworksConfig(typing.TypedDict, total=False):
    cidrBlocks: _list[CidrBlock]
    enabled: bool
    gcpPublicCidrsAccessEnabled: bool
    privateEndpointEnforcementEnabled: bool

@typing.type_check_only
class MaxPodsConstraint(typing.TypedDict, total=False):
    maxPodsPerNode: str

@typing.type_check_only
class MemoryManager(typing.TypedDict, total=False):
    policy: str

@typing.type_check_only
class MeshCertificates(typing.TypedDict, total=False):
    enableCertificates: bool

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    doubleValue: float
    intValue: str
    name: str
    stringValue: str

@typing.type_check_only
class MonitoringComponentConfig(typing.TypedDict, total=False):
    enableComponents: _list[
        typing.Literal[
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
            "JOBSET",
        ]
    ]

@typing.type_check_only
class MonitoringConfig(typing.TypedDict, total=False):
    advancedDatapathObservabilityConfig: AdvancedDatapathObservabilityConfig
    componentConfig: MonitoringComponentConfig
    managedPrometheusConfig: ManagedPrometheusConfig

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    datapathProvider: typing.Literal[
        "DATAPATH_PROVIDER_UNSPECIFIED", "LEGACY_DATAPATH", "ADVANCED_DATAPATH"
    ]
    dataplaneV2Config: DataplaneV2Config
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
    inTransitEncryptionConfig: typing.Literal[
        "IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED",
        "IN_TRANSIT_ENCRYPTION_DISABLED",
        "IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT",
    ]
    network: str
    networkPerformanceConfig: ClusterNetworkPerformanceConfig
    privateIpv6GoogleAccess: typing.Literal[
        "PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED",
        "PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE",
        "PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL",
    ]
    serviceExternalIpsConfig: ServiceExternalIPsConfig
    subnetwork: str

@typing.type_check_only
class NetworkPerformanceConfig(typing.TypedDict, total=False):
    externalIpEgressBandwidthTier: typing.Literal["TIER_UNSPECIFIED", "TIER_1"]
    totalEgressBandwidthTier: typing.Literal["TIER_UNSPECIFIED", "TIER_1"]

@typing.type_check_only
class NetworkPolicy(typing.TypedDict, total=False):
    enabled: bool
    provider: typing.Literal["PROVIDER_UNSPECIFIED", "CALICO"]

@typing.type_check_only
class NetworkPolicyConfig(typing.TypedDict, total=False):
    disabled: bool

@typing.type_check_only
class NetworkTags(typing.TypedDict, total=False):
    tags: _list[str]

@typing.type_check_only
class NetworkTierConfig(typing.TypedDict, total=False):
    networkTier: typing.Literal[
        "NETWORK_TIER_UNSPECIFIED",
        "NETWORK_TIER_DEFAULT",
        "NETWORK_TIER_PREMIUM",
        "NETWORK_TIER_STANDARD",
    ]

@typing.type_check_only
class NodeAffinity(typing.TypedDict, total=False):
    key: str
    operator: typing.Literal["OPERATOR_UNSPECIFIED", "IN", "NOT_IN"]
    values: _list[str]

@typing.type_check_only
class NodeConfig(typing.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    advancedMachineFeatures: AdvancedMachineFeatures
    bootDisk: BootDisk
    bootDiskKmsKey: str
    confidentialNodes: ConfidentialNodes
    consolidationDelay: str
    containerdConfig: ContainerdConfig
    diskSizeGb: int
    diskType: str
    effectiveCgroupMode: typing.Literal[
        "EFFECTIVE_CGROUP_MODE_UNSPECIFIED",
        "EFFECTIVE_CGROUP_MODE_V1",
        "EFFECTIVE_CGROUP_MODE_V2",
    ]
    enableConfidentialStorage: bool
    ephemeralStorageConfig: EphemeralStorageConfig
    ephemeralStorageLocalSsdConfig: EphemeralStorageLocalSsdConfig
    fastSocket: FastSocket
    flexStart: bool
    gcfsConfig: GcfsConfig
    gpuDirectConfig: GPUDirectConfig
    gvnic: VirtualNIC
    hostMaintenancePolicy: HostMaintenancePolicy
    imageType: str
    kubeletConfig: NodeKubeletConfig
    labels: dict[str, typing.Any]
    linuxNodeConfig: LinuxNodeConfig
    localNvmeSsdBlockConfig: LocalNvmeSsdBlockConfig
    localSsdCount: int
    localSsdEncryptionMode: typing.Literal[
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
    nodeImageConfig: CustomImageConfig
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
    taintConfig: TaintConfig
    taints: _list[NodeTaint]
    windowsNodeConfig: WindowsNodeConfig
    workloadMetadataConfig: WorkloadMetadataConfig

@typing.type_check_only
class NodeConfigDefaults(typing.TypedDict, total=False):
    containerdConfig: ContainerdConfig
    gcfsConfig: GcfsConfig
    hostMaintenancePolicy: HostMaintenancePolicy
    loggingConfig: NodePoolLoggingConfig
    nodeKubeletConfig: NodeKubeletConfig

@typing.type_check_only
class NodeCreationConfig(typing.TypedDict, total=False):
    nodeCreationMode: typing.Literal[
        "MODE_UNSPECIFIED", "VIA_KUBELET", "VIA_CONTROL_PLANE"
    ]

@typing.type_check_only
class NodeDrainConfig(typing.TypedDict, total=False):
    graceTerminationDuration: str
    pdbTimeoutDuration: str
    respectPdbDuringNodePoolDeletion: bool

@typing.type_check_only
class NodeKernelModuleLoading(typing.TypedDict, total=False):
    policy: typing.Literal[
        "POLICY_UNSPECIFIED", "ENFORCE_SIGNED_MODULES", "DO_NOT_ENFORCE_SIGNED_MODULES"
    ]

@typing.type_check_only
class NodeKubeletConfig(typing.TypedDict, total=False):
    allowedUnsafeSysctls: _list[str]
    containerLogMaxFiles: int
    containerLogMaxSize: str
    cpuCfsQuota: bool
    cpuCfsQuotaPeriod: str
    cpuManagerPolicy: str
    crashLoopBackOff: CrashLoopBackOffConfig
    evictionMaxPodGracePeriodSeconds: int
    evictionMinimumReclaim: EvictionMinimumReclaim
    evictionSoft: EvictionSignals
    evictionSoftGracePeriod: EvictionGracePeriod
    imageGcHighThresholdPercent: int
    imageGcLowThresholdPercent: int
    imageMaximumGcAge: str
    imageMinimumGcAge: str
    insecureKubeletReadonlyPortEnabled: bool
    maxParallelImagePulls: int
    memoryManager: MemoryManager
    podPidsLimit: str
    shutdownGracePeriodCriticalPodsSeconds: int
    shutdownGracePeriodSeconds: int
    singleProcessOomKill: bool
    topologyManager: TopologyManager

@typing.type_check_only
class NodeLabels(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class NodeManagement(typing.TypedDict, total=False):
    autoRepair: bool
    autoUpgrade: bool
    upgradeOptions: AutoUpgradeOptions

@typing.type_check_only
class NodeNetworkConfig(typing.TypedDict, total=False):
    acceleratorNetworkProfile: str
    additionalNodeNetworkConfigs: _list[AdditionalNodeNetworkConfig]
    additionalPodNetworkConfigs: _list[AdditionalPodNetworkConfig]
    createPodRange: bool
    enablePrivateNodes: bool
    network: str
    networkPerformanceConfig: NetworkPerformanceConfig
    networkTierConfig: NetworkTierConfig
    podCidrOverprovisionConfig: PodCIDROverprovisionConfig
    podIpv4CidrBlock: str
    podIpv4RangeUtilization: float
    podRange: str
    subnetwork: str

@typing.type_check_only
class NodePool(typing.TypedDict, total=False):
    autopilotConfig: AutopilotConfig
    autoscaling: NodePoolAutoscaling
    bestEffortProvisioning: BestEffortProvisioning
    conditions: _list[StatusCondition]
    config: NodeConfig
    etag: str
    initialNodeCount: int
    instanceGroupUrls: _list[str]
    kubeletCertInfo: KubeletCertInfo
    locations: _list[str]
    maintenancePolicy: NodePoolMaintenancePolicy
    management: NodeManagement
    maxPodsConstraint: MaxPodsConstraint
    name: str
    networkConfig: NodeNetworkConfig
    nodeDrainConfig: NodeDrainConfig
    placementPolicy: PlacementPolicy
    podIpv4CidrSize: int
    queuedProvisioning: QueuedProvisioning
    selfLink: str
    status: typing.Literal[
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
class NodePoolAutoConfig(typing.TypedDict, total=False):
    linuxNodeConfig: LinuxNodeConfig
    networkTags: NetworkTags
    nodeKubeletConfig: NodeKubeletConfig
    resourceManagerTags: ResourceManagerTags

@typing.type_check_only
class NodePoolAutoscaling(typing.TypedDict, total=False):
    autoprovisioned: bool
    enabled: bool
    locationPolicy: typing.Literal["LOCATION_POLICY_UNSPECIFIED", "BALANCED", "ANY"]
    maxNodeCount: int
    minNodeCount: int
    totalMaxNodeCount: int
    totalMinNodeCount: int

@typing.type_check_only
class NodePoolDefaults(typing.TypedDict, total=False):
    nodeConfigDefaults: NodeConfigDefaults

@typing.type_check_only
class NodePoolLoggingConfig(typing.TypedDict, total=False):
    variantConfig: LoggingVariantConfig

@typing.type_check_only
class NodePoolMaintenancePolicy(typing.TypedDict, total=False):
    exclusionUntilEndOfSupport: ExclusionUntilEndOfSupport

@typing.type_check_only
class NodePoolUpgradeConcurrencyConfig(typing.TypedDict, total=False):
    maxCount: str

@typing.type_check_only
class NodePoolUpgradeInfo(typing.TypedDict, total=False):
    autoUpgradeStatus: _list[
        typing.Literal["UNKNOWN", "ACTIVE", "MINOR_UPGRADE_PAUSED", "UPGRADE_PAUSED"]
    ]
    customImageInfo: CustomImageInfo
    endOfExtendedSupportTimestamp: str
    endOfStandardSupportTimestamp: str
    minorTargetVersion: str
    patchTargetVersion: str
    pausedReason: _list[
        typing.Literal[
            "AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED",
            "MAINTENANCE_WINDOW",
            "MAINTENANCE_EXCLUSION_NO_UPGRADES",
            "MAINTENANCE_EXCLUSION_NO_MINOR_UPGRADES",
            "SYSTEM_CONFIG",
        ]
    ]
    upgradeDetails: _list[UpgradeDetails]

@typing.type_check_only
class NodeReadinessConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class NodeTaint(typing.TypedDict, total=False):
    effect: typing.Literal[
        "EFFECT_UNSPECIFIED", "NO_SCHEDULE", "PREFER_NO_SCHEDULE", "NO_EXECUTE"
    ]
    key: str
    value: str

@typing.type_check_only
class NodeTaints(typing.TypedDict, total=False):
    taints: _list[NodeTaint]

@typing.type_check_only
class NodeVfioConfig(typing.TypedDict, total=False):
    dmaEntryLimit: int

@typing.type_check_only
class NotificationConfig(typing.TypedDict, total=False):
    pubsub: PubSub

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    clusterConditions: _list[StatusCondition]
    detail: str
    endTime: str
    error: Status
    location: str
    name: str
    nodepoolConditions: _list[StatusCondition]
    operationType: typing.Literal[
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
    status: typing.Literal[
        "STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "ABORTING"
    ]
    statusMessage: str
    targetLink: str
    zone: str

@typing.type_check_only
class OperationError(typing.TypedDict, total=False):
    errorMessage: str
    keyName: str
    timestamp: str

@typing.type_check_only
class OperationProgress(typing.TypedDict, total=False):
    metrics: _list[Metric]
    name: str
    stages: _list[OperationProgress]
    status: typing.Literal[
        "STATUS_UNSPECIFIED", "PENDING", "RUNNING", "DONE", "ABORTING"
    ]

@typing.type_check_only
class OpportunisticMaintenanceStrategy(typing.TypedDict, total=False):
    maintenanceAvailabilityWindow: str
    minNodesPerPool: str
    nodeIdleTimeWindow: str

@typing.type_check_only
class ParallelstoreCsiDriverConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ParentProductConfig(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    productName: str

@typing.type_check_only
class PdbBlockedPod(typing.TypedDict, total=False):
    name: str
    namespace: str

@typing.type_check_only
class PlacementPolicy(typing.TypedDict, total=False):
    policyName: str
    tpuTopology: str
    type: typing.Literal["TYPE_UNSPECIFIED", "COMPACT"]

@typing.type_check_only
class PodAutoscaling(typing.TypedDict, total=False):
    hpaProfile: typing.Literal["HPA_PROFILE_UNSPECIFIED", "NONE", "PERFORMANCE"]

@typing.type_check_only
class PodCIDROverprovisionConfig(typing.TypedDict, total=False):
    disable: bool

@typing.type_check_only
class PodSecurityPolicyConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PodSnapshotConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PolicyBinding(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class PrivateClusterConfig(typing.TypedDict, total=False):
    enablePrivateEndpoint: bool
    enablePrivateNodes: bool
    masterGlobalAccessConfig: PrivateClusterMasterGlobalAccessConfig
    masterIpv4CidrBlock: str
    peeringName: str
    privateEndpoint: str
    privateEndpointSubnetwork: str
    publicEndpoint: str

@typing.type_check_only
class PrivateClusterMasterGlobalAccessConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class PrivateRegistryAccessConfig(typing.TypedDict, total=False):
    certificateAuthorityDomainConfig: _list[CertificateAuthorityDomainConfig]
    enabled: bool

@typing.type_check_only
class PrivilegedAdmissionConfig(typing.TypedDict, total=False):
    allowlistPaths: _list[str]

@typing.type_check_only
class ProtectConfig(typing.TypedDict, total=False):
    workloadConfig: WorkloadConfig
    workloadVulnerabilityMode: typing.Literal[
        "WORKLOAD_VULNERABILITY_MODE_UNSPECIFIED", "DISABLED", "BASIC"
    ]

@typing.type_check_only
class PubSub(typing.TypedDict, total=False):
    enabled: bool
    filter: Filter
    topic: str

@typing.type_check_only
class QueuedProvisioning(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RBACBindingConfig(typing.TypedDict, total=False):
    enableInsecureBindingSystemAuthenticated: bool
    enableInsecureBindingSystemUnauthenticated: bool

@typing.type_check_only
class RangeInfo(typing.TypedDict, total=False):
    rangeName: str
    utilization: float

@typing.type_check_only
class RayClusterLoggingConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RayClusterMonitoringConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RayOperatorConfig(typing.TypedDict, total=False):
    enabled: bool
    rayClusterLoggingConfig: RayClusterLoggingConfig
    rayClusterMonitoringConfig: RayClusterMonitoringConfig

@typing.type_check_only
class RecurringMaintenanceWindow(typing.TypedDict, total=False):
    delayUntil: Date
    recurrence: str
    windowDuration: str
    windowStartTime: TimeOfDay

@typing.type_check_only
class RecurringTimeWindow(typing.TypedDict, total=False):
    recurrence: str
    window: TimeWindow

@typing.type_check_only
class RegistryHeader(typing.TypedDict, total=False):
    key: str
    value: _list[str]

@typing.type_check_only
class RegistryHostConfig(typing.TypedDict, total=False):
    hosts: _list[HostConfig]
    server: str

@typing.type_check_only
class ReleaseChannel(typing.TypedDict, total=False):
    channel: typing.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE", "EXTENDED"]

@typing.type_check_only
class ReleaseChannelConfig(typing.TypedDict, total=False):
    availableVersions: _list[AvailableVersion]
    channel: typing.Literal["UNSPECIFIED", "RAPID", "REGULAR", "STABLE", "EXTENDED"]
    customVersions: _list[str]
    defaultVersion: str
    upgradeTargetVersion: str
    validVersions: _list[str]

@typing.type_check_only
class ReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "UNSPECIFIED",
        "NO_RESERVATION",
        "ANY_RESERVATION",
        "SPECIFIC_RESERVATION",
        "ANY_RESERVATION_THEN_FAIL",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ResourceLabels(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class ResourceLimit(typing.TypedDict, total=False):
    maximum: str
    minimum: str
    resourceType: str

@typing.type_check_only
class ResourceManagerTags(typing.TypedDict, total=False):
    tags: dict[str, typing.Any]

@typing.type_check_only
class ResourceUsageExportConfig(typing.TypedDict, total=False):
    bigqueryDestination: BigQueryDestination
    consumptionMeteringConfig: ConsumptionMeteringConfig
    enableNetworkEgressMetering: bool

@typing.type_check_only
class RollbackNodePoolUpgradeRequest(typing.TypedDict, total=False):
    clusterId: str
    name: str
    nodePoolId: str
    projectId: str
    respectPdb: bool
    zone: str

@typing.type_check_only
class RollbackSafeUpgrade(typing.TypedDict, total=False):
    controlPlaneSoakDuration: str

@typing.type_check_only
class RollbackSafeUpgradeStatus(typing.TypedDict, total=False):
    controlPlaneUpgradeRollbackEndTime: str
    mode: typing.Literal["MODE_UNSPECIFIED", "KCP_MINOR_UPGRADE_ROLLBACK_SAFE_MODE"]
    previousVersion: str

@typing.type_check_only
class RotationConfig(typing.TypedDict, total=False):
    enabled: bool
    rotationInterval: str

@typing.type_check_only
class SandboxConfig(typing.TypedDict, total=False):
    sandboxType: str
    type: typing.Literal["UNSPECIFIED", "GVISOR"]

@typing.type_check_only
class ScheduleUpgradeConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SecondaryBootDisk(typing.TypedDict, total=False):
    diskImage: str
    mode: typing.Literal["MODE_UNSPECIFIED", "CONTAINER_IMAGE_CACHE"]

@typing.type_check_only
class SecondaryBootDiskUpdateStrategy(typing.TypedDict, total=False): ...

@typing.type_check_only
class SecretManagerConfig(typing.TypedDict, total=False):
    enabled: bool
    rotationConfig: RotationConfig

@typing.type_check_only
class SecretSyncConfig(typing.TypedDict, total=False):
    enabled: bool
    rotationConfig: SyncRotationConfig

@typing.type_check_only
class SecurityBulletinEvent(typing.TypedDict, total=False):
    affectedSupportedMinors: _list[str]
    briefDescription: str
    bulletinId: str
    bulletinUri: str
    cveIds: _list[str]
    manualStepsRequired: bool
    mitigatedVersions: _list[str]
    patchedVersions: _list[str]
    resourceTypeAffected: str
    severity: str
    suggestedUpgradeTarget: str

@typing.type_check_only
class SecurityPostureConfig(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "BASIC", "ENTERPRISE"]
    vulnerabilityMode: typing.Literal[
        "VULNERABILITY_MODE_UNSPECIFIED",
        "VULNERABILITY_DISABLED",
        "VULNERABILITY_BASIC",
        "VULNERABILITY_ENTERPRISE",
    ]

@typing.type_check_only
class ServerConfig(typing.TypedDict, total=False):
    channels: _list[ReleaseChannelConfig]
    defaultClusterVersion: str
    defaultImageType: str
    validImageTypes: _list[str]
    validMasterVersions: _list[str]
    validNodeVersions: _list[str]
    windowsVersionMaps: dict[str, typing.Any]

@typing.type_check_only
class ServiceExternalIPsConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SetAddonsConfigRequest(typing.TypedDict, total=False):
    addonsConfig: AddonsConfig
    clusterId: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetLabelsRequest(typing.TypedDict, total=False):
    clusterId: str
    labelFingerprint: str
    name: str
    projectId: str
    resourceLabels: dict[str, typing.Any]
    zone: str

@typing.type_check_only
class SetLegacyAbacRequest(typing.TypedDict, total=False):
    clusterId: str
    enabled: bool
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetLocationsRequest(typing.TypedDict, total=False):
    clusterId: str
    locations: _list[str]
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetLoggingServiceRequest(typing.TypedDict, total=False):
    clusterId: str
    loggingService: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetMaintenancePolicyRequest(typing.TypedDict, total=False):
    clusterId: str
    maintenancePolicy: MaintenancePolicy
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetMasterAuthRequest(typing.TypedDict, total=False):
    action: typing.Literal[
        "UNKNOWN", "SET_PASSWORD", "GENERATE_PASSWORD", "SET_USERNAME"
    ]
    clusterId: str
    name: str
    projectId: str
    update: MasterAuth
    zone: str

@typing.type_check_only
class SetMonitoringServiceRequest(typing.TypedDict, total=False):
    clusterId: str
    monitoringService: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class SetNetworkPolicyRequest(typing.TypedDict, total=False):
    clusterId: str
    name: str
    networkPolicy: NetworkPolicy
    projectId: str
    zone: str

@typing.type_check_only
class SetNodePoolAutoscalingRequest(typing.TypedDict, total=False):
    autoscaling: NodePoolAutoscaling
    clusterId: str
    name: str
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class SetNodePoolManagementRequest(typing.TypedDict, total=False):
    clusterId: str
    management: NodeManagement
    name: str
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class SetNodePoolSizeRequest(typing.TypedDict, total=False):
    clusterId: str
    name: str
    nodeCount: int
    nodePoolId: str
    projectId: str
    zone: str

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool

@typing.type_check_only
class ShieldedNodes(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SliceControllerConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SlurmOperatorConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class SoleTenantConfig(typing.TypedDict, total=False):
    minNodeCpus: int
    nodeAffinities: _list[NodeAffinity]

@typing.type_check_only
class StandardRolloutPolicy(typing.TypedDict, total=False):
    batchNodeCount: int
    batchPercentage: float
    batchSoakDuration: str

@typing.type_check_only
class StartIPRotationRequest(typing.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    rotateCredentials: bool
    zone: str

@typing.type_check_only
class StatefulHAConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusCondition(typing.TypedDict, total=False):
    canonicalCode: typing.Literal[
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
    code: typing.Literal[
        "UNKNOWN",
        "GCE_STOCKOUT",
        "GKE_SERVICE_ACCOUNT_DELETED",
        "GCE_QUOTA_EXCEEDED",
        "SET_BY_OPERATOR",
        "CLOUD_KMS_KEY_ERROR",
        "CA_EXPIRING",
        "NODE_SERVICE_ACCOUNT_MISSING_PERMISSIONS",
        "CLOUD_KMS_KEY_DESTROYED",
    ]
    message: str

@typing.type_check_only
class SwapConfig(typing.TypedDict, total=False):
    bootDiskProfile: BootDiskProfile
    dedicatedLocalSsdProfile: DedicatedLocalSsdProfile
    enabled: bool
    encryptionConfig: EncryptionConfig
    ephemeralLocalSsdProfile: EphemeralLocalSsdProfile

@typing.type_check_only
class SyncRotationConfig(typing.TypedDict, total=False):
    enabled: bool
    rotationInterval: str

@typing.type_check_only
class TaintConfig(typing.TypedDict, total=False):
    architectureTaintBehavior: typing.Literal[
        "ARCHITECTURE_TAINT_BEHAVIOR_UNSPECIFIED", "NONE", "ARM"
    ]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TimeWindow(typing.TypedDict, total=False):
    endTime: str
    maintenanceExclusionOptions: MaintenanceExclusionOptions
    startTime: str

@typing.type_check_only
class TopologyManager(typing.TypedDict, total=False):
    policy: str
    scope: str

@typing.type_check_only
class TpuConfig(typing.TypedDict, total=False):
    enabled: bool
    ipv4CidrBlock: str
    useServiceNetworking: bool

@typing.type_check_only
class UpdateClusterRequest(typing.TypedDict, total=False):
    clusterId: str
    name: str
    projectId: str
    update: ClusterUpdate
    zone: str

@typing.type_check_only
class UpdateInfo(typing.TypedDict, total=False):
    blueGreenInfo: BlueGreenInfo

@typing.type_check_only
class UpdateMasterRequest(typing.TypedDict, total=False):
    clusterId: str
    masterVersion: str
    name: str
    projectId: str
    zone: str

@typing.type_check_only
class UpdateNodePoolRequest(typing.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    bootDisk: BootDisk
    clusterId: str
    confidentialNodes: ConfidentialNodes
    consolidationDelay: str
    containerdConfig: ContainerdConfig
    diskSizeGb: str
    diskType: str
    etag: str
    fastSocket: FastSocket
    flexStart: bool
    gcfsConfig: GcfsConfig
    gvnic: VirtualNIC
    image: str
    imageProject: str
    imageType: str
    kubeletConfig: NodeKubeletConfig
    labels: NodeLabels
    linuxNodeConfig: LinuxNodeConfig
    locations: _list[str]
    loggingConfig: NodePoolLoggingConfig
    machineType: str
    maintenancePolicy: NodePoolMaintenancePolicy
    maxRunDuration: str
    name: str
    nodeDrainConfig: NodeDrainConfig
    nodeNetworkConfig: NodeNetworkConfig
    nodePoolId: str
    nodeVersion: str
    projectId: str
    queuedProvisioning: QueuedProvisioning
    resourceLabels: ResourceLabels
    resourceManagerTags: ResourceManagerTags
    storagePools: _list[str]
    tags: NetworkTags
    taintConfig: TaintConfig
    taints: NodeTaints
    upgradeSettings: UpgradeSettings
    windowsNodeConfig: WindowsNodeConfig
    workloadMetadataConfig: WorkloadMetadataConfig
    zone: str

@typing.type_check_only
class UpgradeAvailableEvent(typing.TypedDict, total=False):
    releaseChannel: ReleaseChannel
    resource: str
    resourceType: typing.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    version: str
    windowsVersions: WindowsVersions

@typing.type_check_only
class UpgradeDetails(typing.TypedDict, total=False):
    endTime: str
    initialEmulatedVersion: str
    initialVersion: str
    startTime: str
    startType: typing.Literal["START_TYPE_UNSPECIFIED", "AUTOMATIC", "MANUAL"]
    state: typing.Literal["UNKNOWN", "FAILED", "SUCCEEDED", "CANCELED", "RUNNING"]
    targetEmulatedVersion: str
    targetVersion: str

@typing.type_check_only
class UpgradeEvent(typing.TypedDict, total=False):
    currentEmulatedVersion: str
    currentVersion: str
    operation: str
    operationStartTime: str
    resource: str
    resourceType: typing.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    targetEmulatedVersion: str
    targetVersion: str

@typing.type_check_only
class UpgradeInfoEvent(typing.TypedDict, total=False):
    currentEmulatedVersion: str
    currentVersion: str
    description: str
    disruptionEvent: DisruptionEvent
    endTime: str
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "END_OF_SUPPORT",
        "COS_MILESTONE_VERSION_UPDATE",
        "UPGRADE_LIFECYCLE",
        "DISRUPTION_EVENT",
    ]
    extendedSupportEndTime: str
    operation: str
    resource: str
    resourceType: typing.Literal[
        "UPGRADE_RESOURCE_TYPE_UNSPECIFIED", "MASTER", "NODE_POOL"
    ]
    standardSupportEndTime: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SCHEDULED", "STARTED", "SUCCEEDED", "FAILED", "CANCELED"
    ]
    targetEmulatedVersion: str
    targetVersion: str

@typing.type_check_only
class UpgradeSettings(typing.TypedDict, total=False):
    blueGreenSettings: BlueGreenSettings
    maxSurge: int
    maxUnavailable: int
    strategy: typing.Literal[
        "NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED", "BLUE_GREEN", "SURGE", "SHORT_LIVED"
    ]

@typing.type_check_only
class UsableSubnetwork(typing.TypedDict, total=False):
    ipCidrRange: str
    network: str
    secondaryIpRanges: _list[UsableSubnetworkSecondaryRange]
    statusMessage: str
    subnetwork: str

@typing.type_check_only
class UsableSubnetworkSecondaryRange(typing.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str
    status: typing.Literal[
        "UNKNOWN",
        "UNUSED",
        "IN_USE_SERVICE",
        "IN_USE_SHAREABLE_POD",
        "IN_USE_MANAGED_POD",
    ]

@typing.type_check_only
class UserManagedKeysConfig(typing.TypedDict, total=False):
    aggregationCa: str
    clusterCa: str
    controlPlaneDiskEncryptionKey: str
    controlPlaneDiskEncryptionKeyVersions: _list[str]
    etcdApiCa: str
    etcdPeerCa: str
    gkeopsEtcdBackupEncryptionKey: str
    serviceAccountSigningKeys: _list[str]
    serviceAccountVerificationKeys: _list[str]

@typing.type_check_only
class VerticalPodAutoscaling(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VirtualNIC(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class WindowsNodeConfig(typing.TypedDict, total=False):
    osVersion: typing.Literal[
        "OS_VERSION_UNSPECIFIED", "OS_VERSION_LTSC2019", "OS_VERSION_LTSC2022"
    ]

@typing.type_check_only
class WindowsVersion(typing.TypedDict, total=False):
    imageType: str
    osVersion: str
    supportEndDate: Date

@typing.type_check_only
class WindowsVersions(typing.TypedDict, total=False):
    windowsVersions: _list[WindowsVersion]

@typing.type_check_only
class WorkloadALTSConfig(typing.TypedDict, total=False):
    enableAlts: bool

@typing.type_check_only
class WorkloadCertificates(typing.TypedDict, total=False):
    enableCertificates: bool

@typing.type_check_only
class WorkloadConfig(typing.TypedDict, total=False):
    auditMode: typing.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "BASIC", "BASELINE", "RESTRICTED"
    ]

@typing.type_check_only
class WorkloadIdentityConfig(typing.TypedDict, total=False):
    identityNamespace: str
    identityProvider: str
    workloadPool: str

@typing.type_check_only
class WorkloadMetadataConfig(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "GCE_METADATA", "GKE_METADATA"]
    nodeMetadata: typing.Literal[
        "UNSPECIFIED", "SECURE", "EXPOSE", "GKE_METADATA_SERVER"
    ]

@typing.type_check_only
class WorkloadPolicyConfig(typing.TypedDict, total=False):
    allowNetAdmin: bool
    autopilotCompatibilityAuditingEnabled: bool

@typing.type_check_only
class WritableCgroups(typing.TypedDict, total=False):
    enabled: bool
