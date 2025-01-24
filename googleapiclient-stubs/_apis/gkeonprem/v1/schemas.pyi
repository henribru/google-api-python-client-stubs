import typing

import typing_extensions

_list = list

@typing.type_check_only
class Authorization(typing_extensions.TypedDict, total=False):
    adminUsers: _list[ClusterUser]

@typing.type_check_only
class BareMetalAdminApiServerArgument(typing_extensions.TypedDict, total=False):
    argument: str
    value: str

@typing.type_check_only
class BareMetalAdminCluster(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
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
class BareMetalAdminClusterOperationsConfig(typing_extensions.TypedDict, total=False):
    enableApplicationLogs: bool

@typing.type_check_only
class BareMetalAdminControlPlaneConfig(typing_extensions.TypedDict, total=False):
    apiServerArgs: _list[BareMetalAdminApiServerArgument]
    controlPlaneNodePoolConfig: BareMetalAdminControlPlaneNodePoolConfig

@typing.type_check_only
class BareMetalAdminControlPlaneNodePoolConfig(
    typing_extensions.TypedDict, total=False
):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalAdminDrainedMachine(typing_extensions.TypedDict, total=False):
    nodeIp: str

@typing.type_check_only
class BareMetalAdminDrainingMachine(typing_extensions.TypedDict, total=False):
    nodeIp: str
    podCount: int

@typing.type_check_only
class BareMetalAdminIslandModeCidrConfig(typing_extensions.TypedDict, total=False):
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalAdminLoadBalancerConfig(typing_extensions.TypedDict, total=False):
    manualLbConfig: BareMetalAdminManualLbConfig
    portConfig: BareMetalAdminPortConfig
    vipConfig: BareMetalAdminVipConfig

@typing.type_check_only
class BareMetalAdminMachineDrainStatus(typing_extensions.TypedDict, total=False):
    drainedMachines: _list[BareMetalAdminDrainedMachine]
    drainingMachines: _list[BareMetalAdminDrainingMachine]

@typing.type_check_only
class BareMetalAdminMaintenanceConfig(typing_extensions.TypedDict, total=False):
    maintenanceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalAdminMaintenanceStatus(typing_extensions.TypedDict, total=False):
    machineDrainStatus: BareMetalAdminMachineDrainStatus

@typing.type_check_only
class BareMetalAdminManualLbConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalAdminNetworkConfig(typing_extensions.TypedDict, total=False):
    islandModeCidr: BareMetalAdminIslandModeCidrConfig

@typing.type_check_only
class BareMetalAdminNodeAccessConfig(typing_extensions.TypedDict, total=False):
    loginUser: str

@typing.type_check_only
class BareMetalAdminOsEnvironmentConfig(typing_extensions.TypedDict, total=False):
    packageRepoExcluded: bool

@typing.type_check_only
class BareMetalAdminPortConfig(typing_extensions.TypedDict, total=False):
    controlPlaneLoadBalancerPort: int

@typing.type_check_only
class BareMetalAdminProxyConfig(typing_extensions.TypedDict, total=False):
    noProxy: _list[str]
    uri: str

@typing.type_check_only
class BareMetalAdminSecurityConfig(typing_extensions.TypedDict, total=False):
    authorization: Authorization

@typing.type_check_only
class BareMetalAdminStorageConfig(typing_extensions.TypedDict, total=False):
    lvpNodeMountsConfig: BareMetalLvpConfig
    lvpShareConfig: BareMetalLvpShareConfig

@typing.type_check_only
class BareMetalAdminVipConfig(typing_extensions.TypedDict, total=False):
    controlPlaneVip: str

@typing.type_check_only
class BareMetalAdminWorkloadNodeConfig(typing_extensions.TypedDict, total=False):
    maxPodsPerNode: str

@typing.type_check_only
class BareMetalApiServerArgument(typing_extensions.TypedDict, total=False):
    argument: str
    value: str

@typing.type_check_only
class BareMetalBgpLbConfig(typing_extensions.TypedDict, total=False):
    addressPools: _list[BareMetalLoadBalancerAddressPool]
    asn: str
    bgpPeerConfigs: _list[BareMetalBgpPeerConfig]
    loadBalancerNodePoolConfig: BareMetalLoadBalancerNodePoolConfig

@typing.type_check_only
class BareMetalBgpPeerConfig(typing_extensions.TypedDict, total=False):
    asn: str
    controlPlaneNodes: _list[str]
    ipAddress: str

@typing.type_check_only
class BareMetalCluster(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
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
class BareMetalClusterOperationsConfig(typing_extensions.TypedDict, total=False):
    enableApplicationLogs: bool

@typing.type_check_only
class BareMetalClusterUpgradePolicy(typing_extensions.TypedDict, total=False):
    pause: bool
    policy: typing_extensions.Literal[
        "NODE_POOL_POLICY_UNSPECIFIED", "SERIAL", "CONCURRENT"
    ]

@typing.type_check_only
class BareMetalControlPlaneConfig(typing_extensions.TypedDict, total=False):
    apiServerArgs: _list[BareMetalApiServerArgument]
    controlPlaneNodePoolConfig: BareMetalControlPlaneNodePoolConfig

@typing.type_check_only
class BareMetalControlPlaneNodePoolConfig(typing_extensions.TypedDict, total=False):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalDrainedMachine(typing_extensions.TypedDict, total=False):
    nodeIp: str

@typing.type_check_only
class BareMetalDrainingMachine(typing_extensions.TypedDict, total=False):
    nodeIp: str
    podCount: int

@typing.type_check_only
class BareMetalIslandModeCidrConfig(typing_extensions.TypedDict, total=False):
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalKubeletConfig(typing_extensions.TypedDict, total=False):
    registryBurst: int
    registryPullQps: int
    serializeImagePullsDisabled: bool

@typing.type_check_only
class BareMetalLoadBalancerAddressPool(typing_extensions.TypedDict, total=False):
    addresses: _list[str]
    avoidBuggyIps: bool
    manualAssign: bool
    pool: str

@typing.type_check_only
class BareMetalLoadBalancerConfig(typing_extensions.TypedDict, total=False):
    bgpLbConfig: BareMetalBgpLbConfig
    manualLbConfig: BareMetalManualLbConfig
    metalLbConfig: BareMetalMetalLbConfig
    portConfig: BareMetalPortConfig
    vipConfig: BareMetalVipConfig

@typing.type_check_only
class BareMetalLoadBalancerNodePoolConfig(typing_extensions.TypedDict, total=False):
    nodePoolConfig: BareMetalNodePoolConfig

@typing.type_check_only
class BareMetalLvpConfig(typing_extensions.TypedDict, total=False):
    path: str
    storageClass: str

@typing.type_check_only
class BareMetalLvpShareConfig(typing_extensions.TypedDict, total=False):
    lvpConfig: BareMetalLvpConfig
    sharedPathPvCount: int

@typing.type_check_only
class BareMetalMachineDrainStatus(typing_extensions.TypedDict, total=False):
    drainedMachines: _list[BareMetalDrainedMachine]
    drainingMachines: _list[BareMetalDrainingMachine]

@typing.type_check_only
class BareMetalMaintenanceConfig(typing_extensions.TypedDict, total=False):
    maintenanceAddressCidrBlocks: _list[str]

@typing.type_check_only
class BareMetalMaintenanceStatus(typing_extensions.TypedDict, total=False):
    machineDrainStatus: BareMetalMachineDrainStatus

@typing.type_check_only
class BareMetalManualLbConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalMetalLbConfig(typing_extensions.TypedDict, total=False):
    addressPools: _list[BareMetalLoadBalancerAddressPool]
    loadBalancerNodePoolConfig: BareMetalLoadBalancerNodePoolConfig

@typing.type_check_only
class BareMetalMultipleNetworkInterfacesConfig(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class BareMetalNetworkConfig(typing_extensions.TypedDict, total=False):
    advancedNetworking: bool
    islandModeCidr: BareMetalIslandModeCidrConfig
    multipleNetworkInterfacesConfig: BareMetalMultipleNetworkInterfacesConfig
    srIovConfig: BareMetalSrIovConfig

@typing.type_check_only
class BareMetalNodeAccessConfig(typing_extensions.TypedDict, total=False):
    loginUser: str

@typing.type_check_only
class BareMetalNodeConfig(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    nodeIp: str

@typing.type_check_only
class BareMetalNodePool(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    name: str
    nodePoolConfig: BareMetalNodePoolConfig
    reconciling: bool
    state: typing_extensions.Literal[
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
class BareMetalNodePoolConfig(typing_extensions.TypedDict, total=False):
    kubeletConfig: BareMetalKubeletConfig
    labels: dict[str, typing.Any]
    nodeConfigs: _list[BareMetalNodeConfig]
    operatingSystem: typing_extensions.Literal["OPERATING_SYSTEM_UNSPECIFIED", "LINUX"]
    taints: _list[NodeTaint]

@typing.type_check_only
class BareMetalNodePoolUpgradePolicy(typing_extensions.TypedDict, total=False):
    parallelUpgradeConfig: BareMetalParallelUpgradeConfig

@typing.type_check_only
class BareMetalOsEnvironmentConfig(typing_extensions.TypedDict, total=False):
    packageRepoExcluded: bool

@typing.type_check_only
class BareMetalParallelUpgradeConfig(typing_extensions.TypedDict, total=False):
    concurrentNodes: int
    minimumAvailableNodes: int

@typing.type_check_only
class BareMetalPortConfig(typing_extensions.TypedDict, total=False):
    controlPlaneLoadBalancerPort: int

@typing.type_check_only
class BareMetalProxyConfig(typing_extensions.TypedDict, total=False):
    noProxy: _list[str]
    uri: str

@typing.type_check_only
class BareMetalSecurityConfig(typing_extensions.TypedDict, total=False):
    authorization: Authorization

@typing.type_check_only
class BareMetalSrIovConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BareMetalStorageConfig(typing_extensions.TypedDict, total=False):
    lvpNodeMountsConfig: BareMetalLvpConfig
    lvpShareConfig: BareMetalLvpShareConfig

@typing.type_check_only
class BareMetalVersionInfo(typing_extensions.TypedDict, total=False):
    dependencies: _list[UpgradeDependency]
    hasDependencies: bool
    version: str

@typing.type_check_only
class BareMetalVipConfig(typing_extensions.TypedDict, total=False):
    controlPlaneVip: str
    ingressVip: str

@typing.type_check_only
class BareMetalWorkloadNodeConfig(typing_extensions.TypedDict, total=False):
    containerRuntime: typing_extensions.Literal[
        "CONTAINER_RUNTIME_UNSPECIFIED", "CONTAINERD"
    ]
    maxPodsPerNode: str

@typing.type_check_only
class BinaryAuthorization(typing_extensions.TypedDict, total=False):
    evaluationMode: typing_extensions.Literal[
        "EVALUATION_MODE_UNSPECIFIED", "DISABLED", "PROJECT_SINGLETON_POLICY_ENFORCE"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClusterUser(typing_extensions.TypedDict, total=False):
    username: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnrollBareMetalAdminClusterRequest(typing_extensions.TypedDict, total=False):
    bareMetalAdminClusterId: str
    membership: str

@typing.type_check_only
class EnrollBareMetalClusterRequest(typing_extensions.TypedDict, total=False):
    adminClusterMembership: str
    bareMetalClusterId: str
    localName: str

@typing.type_check_only
class EnrollBareMetalNodePoolRequest(typing_extensions.TypedDict, total=False):
    bareMetalNodePoolId: str
    validateOnly: bool

@typing.type_check_only
class EnrollVmwareAdminClusterRequest(typing_extensions.TypedDict, total=False):
    membership: str
    vmwareAdminClusterId: str

@typing.type_check_only
class EnrollVmwareClusterRequest(typing_extensions.TypedDict, total=False):
    adminClusterMembership: str
    localName: str
    validateOnly: bool
    vmwareClusterId: str

@typing.type_check_only
class EnrollVmwareNodePoolRequest(typing_extensions.TypedDict, total=False):
    vmwareNodePoolId: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Fleet(typing_extensions.TypedDict, total=False):
    membership: str

@typing.type_check_only
class ListBareMetalAdminClustersResponse(typing_extensions.TypedDict, total=False):
    bareMetalAdminClusters: _list[BareMetalAdminCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBareMetalClustersResponse(typing_extensions.TypedDict, total=False):
    bareMetalClusters: _list[BareMetalCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBareMetalNodePoolsResponse(typing_extensions.TypedDict, total=False):
    bareMetalNodePools: _list[BareMetalNodePool]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListVmwareAdminClustersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareAdminClusters: _list[VmwareAdminCluster]

@typing.type_check_only
class ListVmwareClustersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareClusters: _list[VmwareCluster]

@typing.type_check_only
class ListVmwareNodePoolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    vmwareNodePools: _list[VmwareNodePool]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    doubleValue: float
    intValue: str
    metric: typing_extensions.Literal[
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
class NodeTaint(typing_extensions.TypedDict, total=False):
    effect: typing_extensions.Literal[
        "EFFECT_UNSPECIFIED", "NO_SCHEDULE", "PREFER_NO_SCHEDULE", "NO_EXECUTE"
    ]
    key: str
    value: str

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
    controlPlaneDisconnected: bool
    createTime: str
    endTime: str
    progress: OperationProgress
    requestedCancellation: bool
    statusMessage: str
    target: str
    type: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "CREATE",
        "DELETE",
        "UPDATE",
        "UPGRADE",
        "PLATFORM_UPGRADE",
    ]
    verb: str

@typing.type_check_only
class OperationProgress(typing_extensions.TypedDict, total=False):
    stages: _list[OperationStage]

@typing.type_check_only
class OperationStage(typing_extensions.TypedDict, total=False):
    endTime: str
    metrics: _list[Metric]
    stage: typing_extensions.Literal[
        "STAGE_UNSPECIFIED",
        "PREFLIGHT_CHECK",
        "CONFIGURE",
        "DEPLOY",
        "HEALTH_CHECK",
        "UPDATE",
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class QueryBareMetalAdminVersionConfigResponse(
    typing_extensions.TypedDict, total=False
):
    versions: _list[BareMetalVersionInfo]

@typing.type_check_only
class QueryBareMetalVersionConfigResponse(typing_extensions.TypedDict, total=False):
    versions: _list[BareMetalVersionInfo]

@typing.type_check_only
class QueryVmwareVersionConfigResponse(typing_extensions.TypedDict, total=False):
    versions: _list[VmwareVersionInfo]

@typing.type_check_only
class ResourceCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STATE_TRUE", "STATE_FALSE", "STATE_UNKNOWN"
    ]
    type: str

@typing.type_check_only
class ResourceStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[ResourceCondition]
    errorMessage: str
    version: str
    versions: Versions

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpgradeDependency(typing_extensions.TypedDict, total=False):
    currentVersion: str
    membership: str
    resourceName: str
    targetVersion: str

@typing.type_check_only
class ValidationCheck(typing_extensions.TypedDict, total=False):
    option: typing_extensions.Literal[
        "OPTIONS_UNSPECIFIED", "SKIP_VALIDATION_CHECK_BLOCKING", "SKIP_VALIDATION_ALL"
    ]
    scenario: typing_extensions.Literal["SCENARIO_UNSPECIFIED", "CREATE", "UPDATE"]
    status: ValidationCheckStatus

@typing.type_check_only
class ValidationCheckResult(typing_extensions.TypedDict, total=False):
    category: str
    description: str
    details: str
    reason: str
    state: typing_extensions.Literal[
        "STATE_UNKNOWN",
        "STATE_FAILURE",
        "STATE_SKIPPED",
        "STATE_FATAL",
        "STATE_WARNING",
    ]

@typing.type_check_only
class ValidationCheckStatus(typing_extensions.TypedDict, total=False):
    result: _list[ValidationCheckResult]

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    count: str
    version: str

@typing.type_check_only
class Versions(typing_extensions.TypedDict, total=False):
    versions: _list[Version]

@typing.type_check_only
class VmwareAAGConfig(typing_extensions.TypedDict, total=False):
    aagConfigDisabled: bool

@typing.type_check_only
class VmwareAddressPool(typing_extensions.TypedDict, total=False):
    addresses: _list[str]
    avoidBuggyIps: bool
    manualAssign: bool
    pool: str

@typing.type_check_only
class VmwareAdminAddonNodeConfig(typing_extensions.TypedDict, total=False):
    autoResizeConfig: VmwareAutoResizeConfig

@typing.type_check_only
class VmwareAdminAuthorizationConfig(typing_extensions.TypedDict, total=False):
    viewerUsers: _list[ClusterUser]

@typing.type_check_only
class VmwareAdminCluster(typing_extensions.TypedDict, total=False):
    addonNode: VmwareAdminAddonNodeConfig
    annotations: dict[str, typing.Any]
    antiAffinityGroups: VmwareAAGConfig
    authorization: VmwareAdminAuthorizationConfig
    autoRepairConfig: VmwareAutoRepairConfig
    bootstrapClusterMembership: str
    controlPlaneNode: VmwareAdminControlPlaneNodeConfig
    createTime: str
    description: str
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
    reconciling: bool
    state: typing_extensions.Literal[
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
class VmwareAdminControlPlaneNodeConfig(typing_extensions.TypedDict, total=False):
    cpus: str
    memory: str
    replicas: str

@typing.type_check_only
class VmwareAdminF5BigIpConfig(typing_extensions.TypedDict, total=False):
    address: str
    partition: str
    snatPool: str

@typing.type_check_only
class VmwareAdminHAControlPlaneConfig(typing_extensions.TypedDict, total=False):
    controlPlaneIpBlock: VmwareIpBlock

@typing.type_check_only
class VmwareAdminLoadBalancerConfig(typing_extensions.TypedDict, total=False):
    f5Config: VmwareAdminF5BigIpConfig
    manualLbConfig: VmwareAdminManualLbConfig
    metalLbConfig: VmwareAdminMetalLbConfig
    seesawConfig: VmwareAdminSeesawConfig
    vipConfig: VmwareAdminVipConfig

@typing.type_check_only
class VmwareAdminManualLbConfig(typing_extensions.TypedDict, total=False):
    addonsNodePort: int
    controlPlaneNodePort: int
    ingressHttpNodePort: int
    ingressHttpsNodePort: int
    konnectivityServerNodePort: int

@typing.type_check_only
class VmwareAdminMetalLbConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareAdminNetworkConfig(typing_extensions.TypedDict, total=False):
    dhcpIpConfig: VmwareDhcpIpConfig
    haControlPlaneConfig: VmwareAdminHAControlPlaneConfig
    hostConfig: VmwareHostConfig
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]
    staticIpConfig: VmwareStaticIpConfig
    vcenterNetwork: str

@typing.type_check_only
class VmwareAdminPreparedSecretsConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareAdminSeesawConfig(typing_extensions.TypedDict, total=False):
    enableHa: bool
    group: str
    ipBlocks: _list[VmwareIpBlock]
    masterIp: str
    stackdriverName: str
    vms: _list[str]

@typing.type_check_only
class VmwareAdminVCenterConfig(typing_extensions.TypedDict, total=False):
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
class VmwareAdminVipConfig(typing_extensions.TypedDict, total=False):
    addonsVip: str
    controlPlaneVip: str

@typing.type_check_only
class VmwareAutoRepairConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareAutoResizeConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareBundleConfig(typing_extensions.TypedDict, total=False):
    status: ResourceStatus
    version: str

@typing.type_check_only
class VmwareCluster(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
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
class VmwareClusterUpgradePolicy(typing_extensions.TypedDict, total=False):
    controlPlaneOnly: bool

@typing.type_check_only
class VmwareControlPlaneNodeConfig(typing_extensions.TypedDict, total=False):
    autoResizeConfig: VmwareAutoResizeConfig
    cpus: str
    memory: str
    replicas: str
    vsphereConfig: VmwareControlPlaneVsphereConfig

@typing.type_check_only
class VmwareControlPlaneV2Config(typing_extensions.TypedDict, total=False):
    controlPlaneIpBlock: VmwareIpBlock

@typing.type_check_only
class VmwareControlPlaneVsphereConfig(typing_extensions.TypedDict, total=False):
    datastore: str
    storagePolicyName: str

@typing.type_check_only
class VmwareDataplaneV2Config(typing_extensions.TypedDict, total=False):
    advancedNetworking: bool
    dataplaneV2Enabled: bool
    forwardMode: str
    windowsDataplaneV2Enabled: bool

@typing.type_check_only
class VmwareDhcpIpConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class VmwareF5BigIpConfig(typing_extensions.TypedDict, total=False):
    address: str
    partition: str
    snatPool: str

@typing.type_check_only
class VmwareHostConfig(typing_extensions.TypedDict, total=False):
    dnsSearchDomains: _list[str]
    dnsServers: _list[str]
    ntpServers: _list[str]

@typing.type_check_only
class VmwareHostIp(typing_extensions.TypedDict, total=False):
    hostname: str
    ip: str

@typing.type_check_only
class VmwareIpBlock(typing_extensions.TypedDict, total=False):
    gateway: str
    ips: _list[VmwareHostIp]
    netmask: str

@typing.type_check_only
class VmwareLoadBalancerConfig(typing_extensions.TypedDict, total=False):
    f5Config: VmwareF5BigIpConfig
    manualLbConfig: VmwareManualLbConfig
    metalLbConfig: VmwareMetalLbConfig
    seesawConfig: VmwareSeesawConfig
    vipConfig: VmwareVipConfig

@typing.type_check_only
class VmwareManualLbConfig(typing_extensions.TypedDict, total=False):
    controlPlaneNodePort: int
    ingressHttpNodePort: int
    ingressHttpsNodePort: int
    konnectivityServerNodePort: int

@typing.type_check_only
class VmwareMetalLbConfig(typing_extensions.TypedDict, total=False):
    addressPools: _list[VmwareAddressPool]

@typing.type_check_only
class VmwareNetworkConfig(typing_extensions.TypedDict, total=False):
    controlPlaneV2Config: VmwareControlPlaneV2Config
    dhcpIpConfig: VmwareDhcpIpConfig
    hostConfig: VmwareHostConfig
    podAddressCidrBlocks: _list[str]
    serviceAddressCidrBlocks: _list[str]
    staticIpConfig: VmwareStaticIpConfig
    vcenterNetwork: str

@typing.type_check_only
class VmwareNodeConfig(typing_extensions.TypedDict, total=False):
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
class VmwareNodePool(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
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
class VmwareNodePoolAutoscalingConfig(typing_extensions.TypedDict, total=False):
    maxReplicas: int
    minReplicas: int

@typing.type_check_only
class VmwarePlatformConfig(typing_extensions.TypedDict, total=False):
    bundles: _list[VmwareBundleConfig]
    platformVersion: str
    requiredPlatformVersion: str
    status: ResourceStatus

@typing.type_check_only
class VmwareSeesawConfig(typing_extensions.TypedDict, total=False):
    enableHa: bool
    group: str
    ipBlocks: _list[VmwareIpBlock]
    masterIp: str
    stackdriverName: str
    vms: _list[str]

@typing.type_check_only
class VmwareStaticIpConfig(typing_extensions.TypedDict, total=False):
    ipBlocks: _list[VmwareIpBlock]

@typing.type_check_only
class VmwareStorageConfig(typing_extensions.TypedDict, total=False):
    vsphereCsiDisabled: bool

@typing.type_check_only
class VmwareVCenterConfig(typing_extensions.TypedDict, total=False):
    address: str
    caCertData: str
    cluster: str
    datacenter: str
    datastore: str
    folder: str
    resourcePool: str
    storagePolicyName: str

@typing.type_check_only
class VmwareVersionInfo(typing_extensions.TypedDict, total=False):
    dependencies: _list[UpgradeDependency]
    hasDependencies: bool
    isInstalled: bool
    version: str

@typing.type_check_only
class VmwareVipConfig(typing_extensions.TypedDict, total=False):
    controlPlaneVip: str
    ingressVip: str

@typing.type_check_only
class VmwareVsphereConfig(typing_extensions.TypedDict, total=False):
    datastore: str
    hostGroups: _list[str]
    tags: _list[VmwareVsphereTag]

@typing.type_check_only
class VmwareVsphereTag(typing_extensions.TypedDict, total=False):
    category: str
    tag: str
