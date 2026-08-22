import typing

_list = list

@typing.type_check_only
class Authorization(typing.TypedDict, total=False):
    adminUsers: _list[ClusterUser]

@typing.type_check_only
class BareMetalAdminApiServerArgument(typing.TypedDict, total=False):
    argument: str
    value: str

@typing.type_check_only
class BareMetalAdminBgpLbConfig(typing.TypedDict, total=False):
    addressPools: _list[BareMetalAdminLoadBalancerAddressPool]
    asn: str
    bgpPeerConfigs: _list[BareMetalAdminBgpPeerConfig]
    loadBalancerNodePoolConfig: BareMetalAdminLoadBalancerNodePoolConfig

@typing.type_check_only
class BareMetalAdminBgpPeerConfig(typing.TypedDict, total=False):
    asn: str
    controlPlaneNodes: _list[str]
    ipAddress: str

@typing.type_check_only
class BareMetalAdminCluster(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    bareMetalVersion: str
    binaryAuthorization: BinaryAuthorization
    clusterOperations: BareMetalAdminClusterOperationsConfig
    controlPlane: BareMetalAdminControlPlaneConfig
    createTime: str
    deleteTime: str
    description: str
    endpoint: str
    etag: str
    fleet: Fleet
    loadBalancer: BareMetalAdminLoadBalancerConfig
    localName: str
    maintenanceConfig: BareMetalAdminMaintenanceConfig
    maintenanceStatus: BareMetalAdminMaintenanceStatus
    name: str
    networkConfig: BareMetalAdminNetworkConfig
    nodeAccessConfig: BareMetalAdminNodeAccessConfig
    nodeConfig: BareMetalAdminWorkloadNodeConfig
    osEnvironmentConfig: BareMetalAdminOsEnvironmentConfig
    proxy: BareMetalAdminProxyConfig
    reconciling: bool
    securityConfig: BareMetalAdminSecurityConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    status: ResourceStatus
    storage: BareMetalAdminStorageConfig
    uid: str
    updateTime: str
    validationCheck: ValidationCheck

@typing.type_check_only
class BareMetalAdminClusterOperationsConfig(typing.TypedDict, total=False):
    enableApplicationLogs: bool

@typing.type_check_only
class BareMetalAdminControlPlaneConfig(typing.TypedDict, total=False):
    apiServerArgs: _list[BareMetalAdminApiServerArgument]
    controlPlaneNodePoolConfig: BareMetalAdminControlPlaneNodePoolConfig

@typing.type_check_only
class BareMetalAdminControlPlaneNodePoolConfig(typing.TypedDict, total=False):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalAdminDrainedMachine(typing.TypedDict, total=False):
    nodeIp: str

@typing.type_check_only
class BareMetalAdminDrainingMachine(typing.TypedDict, total=False):
    nodeIp: str
    podCount: int

@typing.type_check_only
class BareMetalAdminIslandModeCidrConfig(typing.TypedDict, total=False):
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalAdminLoadBalancerAddressPool(typing.TypedDict, total=False):
    addresses: _list[str]
    avoidBuggyIps: bool
    manualAssign: bool
    pool: str

@typing.type_check_only
class BareMetalAdminLoadBalancerConfig(typing.TypedDict, total=False):
    bgpLbConfig: BareMetalAdminBgpLbConfig
    manualLbConfig: BareMetalAdminManualLbConfig
    portConfig: BareMetalAdminPortConfig
    vipConfig: BareMetalAdminVipConfig

@typing.type_check_only
class BareMetalAdminLoadBalancerNodePoolConfig(typing.TypedDict, total=False):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalAdminMachineDrainStatus(typing.TypedDict, total=False):
    drainedMachines: _list[BareMetalAdminDrainedMachine]
    drainingMachines: _list[BareMetalAdminDrainingMachine]

@typing.type_check_only
class BareMetalAdminMaintenanceConfig(typing.TypedDict, total=False):
    maintenanceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalAdminMaintenanceStatus(typing.TypedDict, total=False):
    machineDrainStatus: BareMetalAdminMachineDrainStatus

@typing.type_check_only
class BareMetalAdminManualLbConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalAdminMultipleNetworkInterfacesConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalAdminNetworkConfig(typing.TypedDict, total=False):
    advancedNetworking: bool
    islandModeCidr: BareMetalAdminIslandModeCidrConfig
    multipleNetworkInterfacesConfig: BareMetalAdminMultipleNetworkInterfacesConfig

@typing.type_check_only
class BareMetalAdminNodeAccessConfig(typing.TypedDict, total=False):
    loginUser: str

@typing.type_check_only
class BareMetalAdminOsEnvironmentConfig(typing.TypedDict, total=False):
    packageRepoExcluded: bool

@typing.type_check_only
class BareMetalAdminPortConfig(typing.TypedDict, total=False):
    controlPlaneLoadBalancerPort: int

@typing.type_check_only
class BareMetalAdminProxyConfig(typing.TypedDict, total=False):
    noProxy: _list[str]
    uri: str

@typing.type_check_only
class BareMetalAdminSecurityConfig(typing.TypedDict, total=False):
    authorization: Authorization

@typing.type_check_only
class BareMetalAdminStorageConfig(typing.TypedDict, total=False):
    lvpNodeMountsConfig: BareMetalLvpConfig
    lvpShareConfig: BareMetalLvpShareConfig

@typing.type_check_only
class BareMetalAdminVipConfig(typing.TypedDict, total=False):
    controlPlaneVip: str

@typing.type_check_only
class BareMetalAdminWorkloadNodeConfig(typing.TypedDict, total=False):
    maxPodsPerNode: str

@typing.type_check_only
class BareMetalApiServerArgument(typing.TypedDict, total=False):
    argument: str
    value: str

@typing.type_check_only
class BareMetalBgpLbConfig(typing.TypedDict, total=False):
    addressPools: _list[BareMetalLoadBalancerAddressPool]
    asn: str
    bgpPeerConfigs: _list[BareMetalBgpPeerConfig]
    loadBalancerNodePoolConfig: BareMetalLoadBalancerNodePoolConfig

@typing.type_check_only
class BareMetalBgpPeerConfig(typing.TypedDict, total=False):
    asn: str
    controlPlaneNodes: _list[str]
    ipAddress: str

@typing.type_check_only
class BareMetalCluster(typing.TypedDict, total=False):
    adminClusterMembership: str
    adminClusterName: str
    annotations: dict[str, typing.Any]
    bareMetalVersion: str
    binaryAuthorization: BinaryAuthorization
    clusterOperations: BareMetalClusterOperationsConfig
    controlPlane: BareMetalControlPlaneConfig
    createTime: str
    deleteTime: str
    description: str
    endpoint: str
    etag: str
    fleet: Fleet
    loadBalancer: BareMetalLoadBalancerConfig
    localName: str
    localNamespace: str
    maintenanceConfig: BareMetalMaintenanceConfig
    maintenanceStatus: BareMetalMaintenanceStatus
    name: str
    networkConfig: BareMetalNetworkConfig
    nodeAccessConfig: BareMetalNodeAccessConfig
    nodeConfig: BareMetalWorkloadNodeConfig
    osEnvironmentConfig: BareMetalOsEnvironmentConfig
    proxy: BareMetalProxyConfig
    reconciling: bool
    securityConfig: BareMetalSecurityConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    status: ResourceStatus
    storage: BareMetalStorageConfig
    uid: str
    updateTime: str
    upgradePolicy: BareMetalClusterUpgradePolicy
    validationCheck: ValidationCheck

@typing.type_check_only
class BareMetalClusterOperationsConfig(typing.TypedDict, total=False):
    enableApplicationLogs: bool

@typing.type_check_only
class BareMetalClusterUpgradePolicy(typing.TypedDict, total=False):
    pause: bool
    policy: typing.Literal["NODE_POOL_POLICY_UNSPECIFIED", "SERIAL", "CONCURRENT"]

@typing.type_check_only
class BareMetalControlPlaneConfig(typing.TypedDict, total=False):
    apiServerArgs: _list[BareMetalApiServerArgument]
    controlPlaneNodePoolConfig: BareMetalControlPlaneNodePoolConfig

@typing.type_check_only
class BareMetalControlPlaneNodePoolConfig(typing.TypedDict, total=False):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalDrainedMachine(typing.TypedDict, total=False):
    nodeIp: str

@typing.type_check_only
class BareMetalDrainingMachine(typing.TypedDict, total=False):
    nodeIp: str
    podCount: int

@typing.type_check_only
class BareMetalIslandModeCidrConfig(typing.TypedDict, total=False):
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalKubeletConfig(typing.TypedDict, total=False):
    registryBurst: int
    registryPullQps: int
    serializeImagePullsDisabled: bool

@typing.type_check_only
class BareMetalLoadBalancerAddressPool(typing.TypedDict, total=False):
    addresses: _list[str]
    avoidBuggyIps: bool
    manualAssign: bool
    pool: str

@typing.type_check_only
class BareMetalLoadBalancerConfig(typing.TypedDict, total=False):
    bgpLbConfig: BareMetalBgpLbConfig
    manualLbConfig: BareMetalManualLbConfig
    metalLbConfig: BareMetalMetalLbConfig
    portConfig: BareMetalPortConfig
    vipConfig: BareMetalVipConfig

@typing.type_check_only
class BareMetalLoadBalancerNodePoolConfig(typing.TypedDict, total=False):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalLvpConfig(typing.TypedDict, total=False):
    path: str
    storageClass: str

@typing.type_check_only
class BareMetalLvpShareConfig(typing.TypedDict, total=False):
    lvpConfig: BareMetalLvpConfig
    sharedPathPvCount: int

@typing.type_check_only
class BareMetalMachineDrainStatus(typing.TypedDict, total=False):
    drainedMachines: _list[BareMetalDrainedMachine]
    drainingMachines: _list[BareMetalDrainingMachine]

@typing.type_check_only
class BareMetalMaintenanceConfig(typing.TypedDict, total=False):
    maintenanceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalMaintenanceStatus(typing.TypedDict, total=False):
    machineDrainStatus: BareMetalMachineDrainStatus

@typing.type_check_only
class BareMetalManualLbConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalMetalLbConfig(typing.TypedDict, total=False):
    addressPools: _list[BareMetalLoadBalancerAddressPool]
    loadBalancerNodePoolConfig: BareMetalLoadBalancerNodePoolConfig

@typing.type_check_only
class BareMetalMultipleNetworkInterfacesConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalNetworkConfig(typing.TypedDict, total=False):
    advancedNetworking: bool
    islandModeCidr: BareMetalIslandModeCidrConfig
    multipleNetworkInterfacesConfig: BareMetalMultipleNetworkInterfacesConfig
    srIovConfig: BareMetalSrIovConfig

@typing.type_check_only
class BareMetalNodeAccessConfig(typing.TypedDict, total=False):
    loginUser: str

@typing.type_check_only
class BareMetalNodeConfig(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    nodeIp: str

@typing.type_check_only
class BareMetalNodePool(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    name: str
    nodePoolConfig: BareMetalNodePoolConfig
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    status: ResourceStatus
    uid: str
    updateTime: str
    upgradePolicy: BareMetalNodePoolUpgradePolicy

@typing.type_check_only
class BareMetalNodePoolConfig(typing.TypedDict, total=False):
    kubeletConfig: BareMetalKubeletConfig
    labels: dict[str, typing.Any]
    nodeConfigs: _list[BareMetalNodeConfig]
    operatingSystem: typing.Literal["OPERATING_SYSTEM_UNSPECIFIED", "LINUX"]
    taints: _list[NodeTaint]

@typing.type_check_only
class BareMetalNodePoolUpgradePolicy(typing.TypedDict, total=False):
    parallelUpgradeConfig: BareMetalParallelUpgradeConfig

@typing.type_check_only
class BareMetalOsEnvironmentConfig(typing.TypedDict, total=False):
    packageRepoExcluded: bool

@typing.type_check_only
class BareMetalParallelUpgradeConfig(typing.TypedDict, total=False):
    concurrentNodes: int
    minimumAvailableNodes: int

@typing.type_check_only
class BareMetalPortConfig(typing.TypedDict, total=False):
    controlPlaneLoadBalancerPort: int

@typing.type_check_only
class BareMetalProxyConfig(typing.TypedDict, total=False):
    noProxy: _list[str]
    uri: str

@typing.type_check_only
class BareMetalSecurityConfig(typing.TypedDict, total=False):
    authorization: Authorization

@typing.type_check_only
class BareMetalSrIovConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalStorageConfig(typing.TypedDict, total=False):
    lvpNodeMountsConfig: BareMetalLvpConfig
    lvpShareConfig: BareMetalLvpShareConfig

@typing.type_check_only
class BareMetalVersionInfo(typing.TypedDict, total=False):
    dependencies: _list[UpgradeDependency]
    hasDependencies: bool
    version: str

@typing.type_check_only
class BareMetalVipConfig(typing.TypedDict, total=False):
    controlPlaneVip: str
    ingressVip: str

@typing.type_check_only
class BareMetalWorkloadNodeConfig(typing.TypedDict, total=False):
    containerRuntime: typing.Literal["CONTAINER_RUNTIME_UNSPECIFIED", "CONTAINERD"]
    maxPodsPerNode: str

@typing.type_check_only
class BinaryAuthorization(typing.TypedDict, total=False):
    evaluationMode: typing.Literal[
        "EVALUATION_MODE_UNSPECIFIED", "DISABLED", "PROJECT_SINGLETON_POLICY_ENFORCE"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClusterUser(typing.TypedDict, total=False):
    username: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnrollBareMetalAdminClusterRequest(typing.TypedDict, total=False):
    bareMetalAdminClusterId: str
    membership: str

@typing.type_check_only
class EnrollBareMetalClusterRequest(typing.TypedDict, total=False):
    adminClusterMembership: str
    bareMetalClusterId: str
    localName: str
    localNamespace: str

@typing.type_check_only
class EnrollBareMetalNodePoolRequest(typing.TypedDict, total=False):
    bareMetalNodePoolId: str
    validateOnly: bool

@typing.type_check_only
class EnrollVmwareAdminClusterRequest(typing.TypedDict, total=False):
    membership: str
    vmwareAdminClusterId: str

@typing.type_check_only
class EnrollVmwareClusterRequest(typing.TypedDict, total=False):
    adminClusterMembership: str
    localName: str
    validateOnly: bool
    vmwareClusterId: str

@typing.type_check_only
class EnrollVmwareNodePoolRequest(typing.TypedDict, total=False):
    vmwareNodePoolId: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Fleet(typing.TypedDict, total=False):
    membership: str

@typing.type_check_only
class ListBareMetalAdminClustersResponse(typing.TypedDict, total=False):
    bareMetalAdminClusters: _list[BareMetalAdminCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBareMetalClustersResponse(typing.TypedDict, total=False):
    bareMetalClusters: _list[BareMetalCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBareMetalNodePoolsResponse(typing.TypedDict, total=False):
    bareMetalNodePools: _list[BareMetalNodePool]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListVmwareAdminClustersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareAdminClusters: _list[VmwareAdminCluster]

@typing.type_check_only
class ListVmwareClustersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareClusters: _list[VmwareCluster]

@typing.type_check_only
class ListVmwareNodePoolsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareNodePools: _list[VmwareNodePool]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    doubleValue: float
    intValue: str
    metric: typing.Literal[
        "METRIC_ID_UNSPECIFIED",
        "NODES_TOTAL",
        "NODES_DRAINING",
        "NODES_UPGRADING",
        "NODES_PENDING_UPGRADE",
        "NODES_UPGRADED",
        "NODES_FAILED",
        "NODES_HEALTHY",
        "NODES_RECONCILING",
        "NODES_IN_MAINTENANCE",
        "PREFLIGHTS_COMPLETED",
        "PREFLIGHTS_RUNNING",
        "PREFLIGHTS_FAILED",
        "PREFLIGHTS_TOTAL",
    ]
    stringValue: str

@typing.type_check_only
class NodeTaint(typing.TypedDict, total=False):
    effect: typing.Literal[
        "EFFECT_UNSPECIFIED", "NO_SCHEDULE", "PREFER_NO_SCHEDULE", "NO_EXECUTE"
    ]
    key: str
    value: str

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
    controlPlaneDisconnected: bool
    createTime: str
    endTime: str
    progress: OperationProgress
    requestedCancellation: bool
    statusMessage: str
    target: str
    type: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "CREATE",
        "DELETE",
        "UPDATE",
        "UPGRADE",
        "PLATFORM_UPGRADE",
    ]
    verb: str

@typing.type_check_only
class OperationProgress(typing.TypedDict, total=False):
    stages: _list[OperationStage]

@typing.type_check_only
class OperationStage(typing.TypedDict, total=False):
    endTime: str
    metrics: _list[Metric]
    stage: typing.Literal[
        "STAGE_UNSPECIFIED",
        "PREFLIGHT_CHECK",
        "CONFIGURE",
        "DEPLOY",
        "HEALTH_CHECK",
        "UPDATE",
    ]
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class QueryBareMetalAdminVersionConfigResponse(typing.TypedDict, total=False):
    versions: _list[BareMetalVersionInfo]

@typing.type_check_only
class QueryBareMetalVersionConfigResponse(typing.TypedDict, total=False):
    versions: _list[BareMetalVersionInfo]

@typing.type_check_only
class QueryVmwareVersionConfigResponse(typing.TypedDict, total=False):
    versions: _list[VmwareVersionInfo]

@typing.type_check_only
class ResourceCondition(typing.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "STATE_TRUE", "STATE_FALSE", "STATE_UNKNOWN"
    ]
    type: str

@typing.type_check_only
class ResourceStatus(typing.TypedDict, total=False):
    conditions: _list[ResourceCondition]
    errorMessage: str
    version: str
    versions: Versions

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpgradeDependency(typing.TypedDict, total=False):
    currentVersion: str
    membership: str
    resourceName: str
    targetVersion: str

@typing.type_check_only
class ValidationCheck(typing.TypedDict, total=False):
    option: typing.Literal[
        "OPTIONS_UNSPECIFIED", "SKIP_VALIDATION_CHECK_BLOCKING", "SKIP_VALIDATION_ALL"
    ]
    scenario: typing.Literal["SCENARIO_UNSPECIFIED", "CREATE", "UPDATE"]
    status: ValidationCheckStatus

@typing.type_check_only
class ValidationCheckResult(typing.TypedDict, total=False):
    category: str
    description: str
    details: str
    reason: str
    state: typing.Literal[
        "STATE_UNKNOWN",
        "STATE_FAILURE",
        "STATE_SKIPPED",
        "STATE_FATAL",
        "STATE_WARNING",
    ]

@typing.type_check_only
class ValidationCheckStatus(typing.TypedDict, total=False):
    result: _list[ValidationCheckResult]

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    count: str
    version: str

@typing.type_check_only
class Versions(typing.TypedDict, total=False):
    versions: _list[Version]

@typing.type_check_only
class VmwareAAGConfig(typing.TypedDict, total=False):
    aagConfigDisabled: bool

@typing.type_check_only
class VmwareAddressPool(typing.TypedDict, total=False):
    addresses: _list[str]
    avoidBuggyIps: bool
    manualAssign: bool
    pool: str

@typing.type_check_only
class VmwareAdminAddonNodeConfig(typing.TypedDict, total=False):
    autoResizeConfig: VmwareAutoResizeConfig

@typing.type_check_only
class VmwareAdminAuthorizationConfig(typing.TypedDict, total=False):
    viewerUsers: _list[ClusterUser]

@typing.type_check_only
class VmwareAdminCluster(typing.TypedDict, total=False):
    addonNode: VmwareAdminAddonNodeConfig
    annotations: dict[str, typing.Any]
    antiAffinityGroups: VmwareAAGConfig
    authorization: VmwareAdminAuthorizationConfig
    autoRepairConfig: VmwareAutoRepairConfig
    bootstrapClusterMembership: str
    controlPlaneNode: VmwareAdminControlPlaneNodeConfig
    createTime: str
    description: str
    enableAdvancedCluster: bool
    endpoint: str
    etag: str
    fleet: Fleet
    imageType: str
    loadBalancer: VmwareAdminLoadBalancerConfig
    localName: str
    name: str
    networkConfig: VmwareAdminNetworkConfig
    onPremVersion: str
    platformConfig: VmwarePlatformConfig
    preparedSecrets: VmwareAdminPreparedSecretsConfig
    privateRegistryConfig: VmwareAdminPrivateRegistryConfig
    proxy: VmwareAdminProxy
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    status: ResourceStatus
    uid: str
    updateTime: str
    validationCheck: ValidationCheck
    vcenter: VmwareAdminVCenterConfig

@typing.type_check_only
class VmwareAdminControlPlaneNodeConfig(typing.TypedDict, total=False):
    cpus: str
    memory: str
    replicas: str

@typing.type_check_only
class VmwareAdminF5BigIpConfig(typing.TypedDict, total=False):
    address: str
    partition: str
    snatPool: str

@typing.type_check_only
class VmwareAdminHAControlPlaneConfig(typing.TypedDict, total=False):
    controlPlaneIpBlock: VmwareIpBlock

@typing.type_check_only
class VmwareAdminLoadBalancerConfig(typing.TypedDict, total=False):
    f5Config: VmwareAdminF5BigIpConfig
    manualLbConfig: VmwareAdminManualLbConfig
    metalLbConfig: VmwareAdminMetalLbConfig
    seesawConfig: VmwareAdminSeesawConfig
    vipConfig: VmwareAdminVipConfig

@typing.type_check_only
class VmwareAdminManualLbConfig(typing.TypedDict, total=False):
    addonsNodePort: int
    controlPlaneNodePort: int
    ingressHttpNodePort: int
    ingressHttpsNodePort: int
    konnectivityServerNodePort: int

@typing.type_check_only
class VmwareAdminMetalLbConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareAdminNetworkConfig(typing.TypedDict, total=False):
    dhcpIpConfig: VmwareDhcpIpConfig
    haControlPlaneConfig: VmwareAdminHAControlPlaneConfig
    hostConfig: VmwareHostConfig
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]
    staticIpConfig: VmwareStaticIpConfig
    vcenterNetwork: str

@typing.type_check_only
class VmwareAdminPreparedSecretsConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareAdminPrivateRegistryConfig(typing.TypedDict, total=False):
    address: str
    caCert: str

@typing.type_check_only
class VmwareAdminProxy(typing.TypedDict, total=False):
    noProxy: str
    url: str

@typing.type_check_only
class VmwareAdminSeesawConfig(typing.TypedDict, total=False):
    enableHa: bool
    group: str
    ipBlocks: _list[VmwareIpBlock]
    masterIp: str
    stackdriverName: str
    vms: _list[str]

@typing.type_check_only
class VmwareAdminVCenterConfig(typing.TypedDict, total=False):
    address: str
    caCertData: str
    cluster: str
    dataDisk: str
    datacenter: str
    datastore: str
    folder: str
    resourcePool: str
    storagePolicyName: str

@typing.type_check_only
class VmwareAdminVipConfig(typing.TypedDict, total=False):
    addonsVip: str
    controlPlaneVip: str

@typing.type_check_only
class VmwareAutoRepairConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareAutoResizeConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareBundleConfig(typing.TypedDict, total=False):
    status: ResourceStatus
    version: str

@typing.type_check_only
class VmwareCluster(typing.TypedDict, total=False):
    adminClusterMembership: str
    adminClusterName: str
    annotations: dict[str, typing.Any]
    antiAffinityGroups: VmwareAAGConfig
    authorization: Authorization
    autoRepairConfig: VmwareAutoRepairConfig
    binaryAuthorization: BinaryAuthorization
    controlPlaneNode: VmwareControlPlaneNodeConfig
    createTime: str
    dataplaneV2: VmwareDataplaneV2Config
    deleteTime: str
    description: str
    disableBundledIngress: bool
    enableAdvancedCluster: bool
    enableControlPlaneV2: bool
    endpoint: str
    etag: str
    fleet: Fleet
    loadBalancer: VmwareLoadBalancerConfig
    localName: str
    name: str
    networkConfig: VmwareNetworkConfig
    onPremVersion: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    status: ResourceStatus
    storage: VmwareStorageConfig
    uid: str
    updateTime: str
    upgradePolicy: VmwareClusterUpgradePolicy
    validationCheck: ValidationCheck
    vcenter: VmwareVCenterConfig
    vmTrackingEnabled: bool

@typing.type_check_only
class VmwareClusterUpgradePolicy(typing.TypedDict, total=False):
    controlPlaneOnly: bool

@typing.type_check_only
class VmwareControlPlaneNodeConfig(typing.TypedDict, total=False):
    autoResizeConfig: VmwareAutoResizeConfig
    cpus: str
    memory: str
    replicas: str
    vsphereConfig: VmwareControlPlaneVsphereConfig

@typing.type_check_only
class VmwareControlPlaneV2Config(typing.TypedDict, total=False):
    controlPlaneIpBlock: VmwareIpBlock

@typing.type_check_only
class VmwareControlPlaneVsphereConfig(typing.TypedDict, total=False):
    datastore: str
    storagePolicyName: str

@typing.type_check_only
class VmwareDataplaneV2Config(typing.TypedDict, total=False):
    advancedNetworking: bool
    dataplaneV2Enabled: bool
    forwardMode: str
    windowsDataplaneV2Enabled: bool

@typing.type_check_only
class VmwareDhcpIpConfig(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareF5BigIpConfig(typing.TypedDict, total=False):
    address: str
    partition: str
    snatPool: str

@typing.type_check_only
class VmwareHostConfig(typing.TypedDict, total=False):
    dnsSearchDomains: _list[str]
    dnsServers: _list[str]
    ntpServers: _list[str]

@typing.type_check_only
class VmwareHostIp(typing.TypedDict, total=False):
    hostname: str
    ip: str

@typing.type_check_only
class VmwareIpBlock(typing.TypedDict, total=False):
    gateway: str
    ips: _list[VmwareHostIp]
    netmask: str

@typing.type_check_only
class VmwareLoadBalancerConfig(typing.TypedDict, total=False):
    f5Config: VmwareF5BigIpConfig
    manualLbConfig: VmwareManualLbConfig
    metalLbConfig: VmwareMetalLbConfig
    seesawConfig: VmwareSeesawConfig
    vipConfig: VmwareVipConfig

@typing.type_check_only
class VmwareManualLbConfig(typing.TypedDict, total=False):
    controlPlaneNodePort: int
    ingressHttpNodePort: int
    ingressHttpsNodePort: int
    konnectivityServerNodePort: int

@typing.type_check_only
class VmwareMetalLbConfig(typing.TypedDict, total=False):
    addressPools: _list[VmwareAddressPool]

@typing.type_check_only
class VmwareNetworkConfig(typing.TypedDict, total=False):
    controlPlaneV2Config: VmwareControlPlaneV2Config
    dhcpIpConfig: VmwareDhcpIpConfig
    hostConfig: VmwareHostConfig
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]
    staticIpConfig: VmwareStaticIpConfig
    vcenterNetwork: str

@typing.type_check_only
class VmwareNodeConfig(typing.TypedDict, total=False):
    bootDiskSizeGb: str
    cpus: str
    enableLoadBalancer: bool
    image: str
    imageType: str
    labels: dict[str, typing.Any]
    memoryMb: str
    replicas: str
    taints: _list[NodeTaint]
    vsphereConfig: VmwareVsphereConfig

@typing.type_check_only
class VmwareNodePool(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    config: VmwareNodeConfig
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    name: str
    nodePoolAutoscaling: VmwareNodePoolAutoscalingConfig
    onPremVersion: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PROVISIONING",
        "RUNNING",
        "RECONCILING",
        "STOPPING",
        "ERROR",
        "DEGRADED",
    ]
    status: ResourceStatus
    uid: str
    updateTime: str

@typing.type_check_only
class VmwareNodePoolAutoscalingConfig(typing.TypedDict, total=False):
    maxReplicas: int
    minReplicas: int

@typing.type_check_only
class VmwarePlatformConfig(typing.TypedDict, total=False):
    bundles: _list[VmwareBundleConfig]
    platformVersion: str
    requiredPlatformVersion: str
    status: ResourceStatus

@typing.type_check_only
class VmwareSeesawConfig(typing.TypedDict, total=False):
    enableHa: bool
    group: str
    ipBlocks: _list[VmwareIpBlock]
    masterIp: str
    stackdriverName: str
    vms: _list[str]

@typing.type_check_only
class VmwareStaticIpConfig(typing.TypedDict, total=False):
    ipBlocks: _list[VmwareIpBlock]

@typing.type_check_only
class VmwareStorageConfig(typing.TypedDict, total=False):
    vsphereCsiDisabled: bool

@typing.type_check_only
class VmwareVCenterConfig(typing.TypedDict, total=False):
    address: str
    caCertData: str
    cluster: str
    datacenter: str
    datastore: str
    folder: str
    resourcePool: str
    storagePolicyName: str

@typing.type_check_only
class VmwareVersionInfo(typing.TypedDict, total=False):
    dependencies: _list[UpgradeDependency]
    hasDependencies: bool
    isInstalled: bool
    version: str

@typing.type_check_only
class VmwareVipConfig(typing.TypedDict, total=False):
    controlPlaneVip: str
    ingressVip: str

@typing.type_check_only
class VmwareVsphereConfig(typing.TypedDict, total=False):
    datastore: str
    hostGroups: _list[str]
    tags: _list[VmwareVsphereTag]

@typing.type_check_only
class VmwareVsphereTag(typing.TypedDict, total=False):
    category: str
    tag: str
