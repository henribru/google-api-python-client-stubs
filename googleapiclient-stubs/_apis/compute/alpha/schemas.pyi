import typing

_list = list

@typing.type_check_only
class AWSV4Signature(typing.TypedDict, total=False):
    accessKey: str
    accessKeyId: str
    accessKeyVersion: str
    originRegion: str

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: str

@typing.type_check_only
class AcceleratorPodController(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    managementInterfaces: dict[str, typing.Any]
    name: str
    selfLink: str
    selfLinkWithId: str
    target: str
    zone: str

@typing.type_check_only
class AcceleratorPodControllersListResponse(typing.TypedDict, total=False):
    items: _list[AcceleratorPodController]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTopologiesInfo(typing.TypedDict, total=False):
    acceleratorTopologyInfos: _list[AcceleratorTopologiesInfoAcceleratorTopologyInfo]

@typing.type_check_only
class AcceleratorTopologiesInfoAcceleratorTopologyInfo(typing.TypedDict, total=False):
    acceleratorTopology: str
    infoPerTopologyStates: _list[
        AcceleratorTopologiesInfoAcceleratorTopologyInfoInfoPerTopologyState
    ]

@typing.type_check_only
class AcceleratorTopologiesInfoAcceleratorTopologyInfoInfoPerTopologyState(
    typing.TypedDict, total=False
):
    count: int
    state: typing.Literal[
        "AVAILABLE", "DEGRADED", "RUNNING", "TOPOLOGY_STATE_UNSPECIFIED", "UNHEALTHY"
    ]

@typing.type_check_only
class AcceleratorType(typing.TypedDict, total=False):
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    maximumCardsPerInstance: int
    name: str
    selfLink: str
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class AcceleratorTypeAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTypeList(typing.TypedDict, total=False):
    id: str
    items: _list[AcceleratorType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTypesScopedList(typing.TypedDict, total=False):
    acceleratorTypes: _list[AcceleratorType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AccessConfig(typing.TypedDict, total=False):
    externalIpv6: str
    externalIpv6PrefixLength: int
    kind: str
    name: str
    natIP: str
    networkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    publicDnsName: str
    publicPtrDomainName: str
    securityPolicy: str
    setPublicDns: bool
    setPublicPtr: bool
    type: typing.Literal["DIRECT_IPV6", "ONE_TO_ONE_NAT"]

@typing.type_check_only
class Address(typing.TypedDict, total=False):
    address: str
    addressType: typing.Literal[
        "DNS_FORWARDING", "EXTERNAL", "INTERNAL", "UNSPECIFIED_TYPE"
    ]
    creationTimestamp: str
    description: str
    id: str
    ipCollection: str
    ipVersion: typing.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    ipv6EndpointType: typing.Literal["NETLB", "VM"]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    networkAttachment: str
    networkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    prefixLength: int
    ptrDomainName: str
    ptrDomainNameTtl: int
    purpose: typing.Literal[
        "APPLICATION_AND_PROXY_LOAD_BALANCERS",
        "DNS_RESOLVER",
        "GCE_ENDPOINT",
        "IPSEC_INTERCONNECT",
        "NAT_AUTO",
        "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0",
        "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1",
        "PRIVATE_SERVICE_CONNECT",
        "SERVERLESS",
        "SHARED_LOADBALANCER_VIP",
        "SYSTEM_MANAGED",
        "VPC_PEERING",
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    serviceClassId: str
    status: typing.Literal["IN_USE", "RESERVED", "RESERVING"]
    subnetwork: str
    users: _list[str]

@typing.type_check_only
class AddressAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AddressList(typing.TypedDict, total=False):
    id: str
    items: _list[Address]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AddressesScopedList(typing.TypedDict, total=False):
    addresses: _list[Address]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AdvancedMachineFeatures(typing.TypedDict, total=False):
    enableNestedVirtualization: bool
    enableUefiNetworking: bool
    enableWatchdogTimer: bool
    numaNodeCount: int
    performanceMonitoringUnit: typing.Literal[
        "ARCHITECTURAL",
        "ENHANCED",
        "PERFORMANCE_MONITORING_UNIT_UNSPECIFIED",
        "STANDARD",
    ]
    threadsPerCore: int
    turboMode: str
    visibleCoreCount: int

@typing.type_check_only
class AliasIpRange(typing.TypedDict, total=False):
    candidateSubnetworkRangeNames: _list[str]
    effectiveSubnetworkRangeName: str
    ipCidrRange: str
    subnetworkRangeName: str

@typing.type_check_only
class AllocationAggregateReservation(typing.TypedDict, total=False):
    hostCount: int
    inUseHostCount: int
    inUseInstanceCount: int
    inUseResources: _list[AllocationAggregateReservationReservedResourceInfo]
    reservedResources: _list[AllocationAggregateReservationReservedResourceInfo]
    vmFamily: typing.Literal[
        "VM_FAMILY_CLOUD_TPU_DEVICE_CT3",
        "VM_FAMILY_CLOUD_TPU_LITE_DEVICE_CT5L",
        "VM_FAMILY_CLOUD_TPU_LITE_POD_SLICE_CT5LP",
        "VM_FAMILY_CLOUD_TPU_LITE_POD_SLICE_CT6E",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT3P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT4P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT5P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU7",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU7X",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU8I_METAL",
    ]
    workloadType: typing.Literal["BATCH", "SERVING", "UNSPECIFIED"]

@typing.type_check_only
class AllocationAggregateReservationReservedResourceInfo(typing.TypedDict, total=False):
    accelerator: AllocationAggregateReservationReservedResourceInfoAccelerator

@typing.type_check_only
class AllocationAggregateReservationReservedResourceInfoAccelerator(
    typing.TypedDict, total=False
):
    acceleratorCount: int
    acceleratorType: str

@typing.type_check_only
class AllocationReservationSharingPolicy(typing.TypedDict, total=False):
    serviceShareType: typing.Literal[
        "ALLOW_ALL", "DISALLOW_ALL", "SERVICE_SHARE_TYPE_UNSPECIFIED"
    ]

@typing.type_check_only
class AllocationResourceStatus(typing.TypedDict, total=False):
    aggregateAllocation: AllocationResourceStatusAggregateAllocation
    healthInfo: AllocationResourceStatusHealthInfo
    reservationBlockCount: int
    reservationMaintenance: GroupMaintenanceInfo
    specificSkuAllocation: AllocationResourceStatusSpecificSKUAllocation

@typing.type_check_only
class AllocationResourceStatusAggregateAllocation(typing.TypedDict, total=False):
    utilizations: dict[str, typing.Any]

@typing.type_check_only
class AllocationResourceStatusHealthInfo(typing.TypedDict, total=False):
    degradedBlockCount: int
    healthStatus: typing.Literal["DEGRADED", "HEALTHY", "HEALTH_STATUS_UNSPECIFIED"]
    healthyBlockCount: int

@typing.type_check_only
class AllocationResourceStatusSpecificSKUAllocation(typing.TypedDict, total=False):
    sourceInstanceTemplateId: str
    utilizations: dict[str, typing.Any]

@typing.type_check_only
class AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk(
    typing.TypedDict, total=False
):
    diskSizeGb: str
    interface: typing.Literal["NVDIMM", "NVME", "SCSI"]

@typing.type_check_only
class AllocationSpecificSKUAllocationReservedInstanceProperties(
    typing.TypedDict, total=False
):
    guestAccelerators: _list[AcceleratorConfig]
    localSsds: _list[
        AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk
    ]
    locationHint: str
    machineType: str
    maintenanceFreezeDurationHours: int
    maintenanceInterval: typing.Literal["AS_NEEDED", "PERIODIC", "RECURRENT"]
    minCpuPlatform: str

@typing.type_check_only
class AllocationSpecificSKUReservation(typing.TypedDict, total=False):
    assuredCount: str
    count: str
    inUseCount: str
    instanceProperties: AllocationSpecificSKUAllocationReservedInstanceProperties
    sourceInstanceTemplate: str

@typing.type_check_only
class AsyncReplicationStatus(typing.TypedDict, total=False):
    diskPairReplicationState: DiskPairReplicationState
    lastReplicationDetails: ReplicationDetails

@typing.type_check_only
class AttachedDisk(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    forceAttach: bool
    guestOsFeatures: _list[GuestOsFeature]
    index: int
    initializeParams: AttachedDiskInitializeParams
    interface: typing.Literal["NVDIMM", "NVME", "SCSI"]
    kind: str
    licenses: _list[str]
    locked: bool
    mode: typing.Literal["READ_ONLY", "READ_WRITE"]
    savedState: typing.Literal["DISK_SAVED_STATE_UNSPECIFIED", "PRESERVED"]
    shieldedInstanceInitialState: InitialStateConfig
    source: str
    type: typing.Literal["PERSISTENT", "SCRATCH"]

@typing.type_check_only
class AttachedDiskInitializeParams(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    description: str
    diskName: str
    diskSizeGb: str
    diskType: str
    enableConfidentialCompute: bool
    guestOsFeatures: _list[GuestOsFeature]
    interface: typing.Literal["NVME", "SCSI", "UNSPECIFIED"]
    labels: dict[str, typing.Any]
    licenseCodes: _list[str]
    licenses: _list[str]
    multiWriter: bool
    onUpdateAction: typing.Literal[
        "RECREATE_DISK", "RECREATE_DISK_IF_SOURCE_CHANGED", "USE_EXISTING_DISK"
    ]
    provisionedIops: str
    provisionedThroughput: str
    replicaZones: _list[str]
    resourceManagerTags: dict[str, typing.Any]
    resourcePolicies: _list[str]
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceInstantSnapshot: str
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey
    storagePool: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "ADMIN_READ", "DATA_READ", "DATA_WRITE", "LOG_TYPE_UNSPECIFIED"
    ]

@typing.type_check_only
class AuthenticationConfig(typing.TypedDict, total=False):
    trustConfig: str

@typing.type_check_only
class AuthenticationPolicy(typing.TypedDict, total=False):
    origins: _list[OriginAuthenticationMethod]
    peers: _list[PeerAuthenticationMethod]
    principalBinding: typing.Literal["INVALID", "USE_ORIGIN", "USE_PEER"]
    serverTlsContext: TlsContext

@typing.type_check_only
class AuthorizationConfig(typing.TypedDict, total=False):
    policies: _list[RbacPolicy]

@typing.type_check_only
class Autoscaler(typing.TypedDict, total=False):
    autoscalingPolicy: AutoscalingPolicy
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    recommendedSize: int
    region: str
    scalingScheduleStatus: dict[str, typing.Any]
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal["ACTIVE", "DELETING", "ERROR", "PENDING"]
    statusDetails: _list[AutoscalerStatusDetails]
    target: str
    zone: str

@typing.type_check_only
class AutoscalerAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AutoscalerList(typing.TypedDict, total=False):
    id: str
    items: _list[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AutoscalerStatusDetails(typing.TypedDict, total=False):
    message: str
    type: typing.Literal[
        "ALL_INSTANCES_UNHEALTHY",
        "BACKEND_SERVICE_DOES_NOT_EXIST",
        "CAPPED_AT_MAX_NUM_REPLICAS",
        "CUSTOM_METRIC_DATA_POINTS_TOO_SPARSE",
        "CUSTOM_METRIC_INVALID",
        "MIN_EQUALS_MAX",
        "MISSING_CUSTOM_METRIC_DATA_POINTS",
        "MISSING_LOAD_BALANCING_DATA_POINTS",
        "MODE_OFF",
        "MODE_ONLY_SCALE_OUT",
        "MODE_ONLY_UP",
        "MORE_THAN_ONE_BACKEND_SERVICE",
        "NOT_ENOUGH_QUOTA_AVAILABLE",
        "REGION_RESOURCE_STOCKOUT",
        "SCALING_TARGET_DOES_NOT_EXIST",
        "SCHEDULED_INSTANCES_GREATER_THAN_AUTOSCALER_MAX",
        "SCHEDULED_INSTANCES_LESS_THAN_AUTOSCALER_MIN",
        "UNKNOWN",
        "UNSUPPORTED_MAX_RATE_LOAD_BALANCING_CONFIGURATION",
        "ZONE_RESOURCE_STOCKOUT",
    ]

@typing.type_check_only
class AutoscalersScopedList(typing.TypedDict, total=False):
    autoscalers: _list[Autoscaler]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AutoscalingPolicy(typing.TypedDict, total=False):
    coolDownPeriodSec: int
    cpuUtilization: AutoscalingPolicyCpuUtilization
    customMetricUtilizations: _list[AutoscalingPolicyCustomMetricUtilization]
    loadBalancingUtilization: AutoscalingPolicyLoadBalancingUtilization
    maxNumReplicas: int
    minNumReplicas: int
    mode: typing.Literal["OFF", "ON", "ONLY_SCALE_OUT", "ONLY_UP"]
    scaleDownControl: AutoscalingPolicyScaleDownControl
    scaleInControl: AutoscalingPolicyScaleInControl
    scalingSchedules: dict[str, typing.Any]
    stabilizationPeriodSec: int

@typing.type_check_only
class AutoscalingPolicyCpuUtilization(typing.TypedDict, total=False):
    predictiveMethod: typing.Literal[
        "NONE", "OPTIMIZE_AVAILABILITY", "PREDICTIVE_METHOD_UNSPECIFIED", "STANDARD"
    ]
    utilizationTarget: float

@typing.type_check_only
class AutoscalingPolicyCustomMetricUtilization(typing.TypedDict, total=False):
    filter: str
    metric: str
    singleInstanceAssignment: float
    utilizationTarget: float
    utilizationTargetType: typing.Literal[
        "DELTA_PER_MINUTE", "DELTA_PER_SECOND", "GAUGE"
    ]

@typing.type_check_only
class AutoscalingPolicyLoadBalancingUtilization(typing.TypedDict, total=False):
    utilizationTarget: float

@typing.type_check_only
class AutoscalingPolicyScaleDownControl(typing.TypedDict, total=False):
    maxScaledDownReplicas: FixedOrPercent
    timeWindowSec: int

@typing.type_check_only
class AutoscalingPolicyScaleInControl(typing.TypedDict, total=False):
    maxScaledInReplicas: FixedOrPercent
    timeWindowSec: int

@typing.type_check_only
class AutoscalingPolicyScalingSchedule(typing.TypedDict, total=False):
    description: str
    disabled: bool
    durationSec: int
    minRequiredReplicas: int
    schedule: str
    timeZone: str

@typing.type_check_only
class Backend(typing.TypedDict, total=False):
    balancingMode: typing.Literal[
        "CONNECTION", "CUSTOM_METRICS", "IN_FLIGHT", "RATE", "UTILIZATION"
    ]
    capacityScaler: float
    customMetrics: _list[BackendCustomMetric]
    description: str
    failover: bool
    group: str
    maxConnections: int
    maxConnectionsPerEndpoint: int
    maxConnectionsPerInstance: int
    maxInFlightRequests: int
    maxInFlightRequestsPerEndpoint: int
    maxInFlightRequestsPerInstance: int
    maxRate: int
    maxRatePerEndpoint: float
    maxRatePerInstance: float
    maxUtilization: float
    orchestrationInfo: BackendBackendOrchestrationInfo
    preference: typing.Literal["DEFAULT", "PREFERENCE_UNSPECIFIED", "PREFERRED"]
    service: str
    trafficDuration: typing.Literal["LONG", "SHORT", "TRAFFIC_DURATION_UNSPECIFIED"]

@typing.type_check_only
class BackendBackendOrchestrationInfo(typing.TypedDict, total=False):
    resourceUri: str

@typing.type_check_only
class BackendBucket(typing.TypedDict, total=False):
    bucketName: str
    cdnPolicy: BackendBucketCdnPolicy
    compressionMode: typing.Literal["AUTOMATIC", "DISABLED"]
    creationTimestamp: str
    customResponseHeaders: _list[str]
    description: str
    edgeSecurityPolicy: str
    enableCdn: bool
    id: str
    kind: str
    loadBalancingScheme: typing.Literal["EXTERNAL_MANAGED", "INTERNAL_MANAGED"]
    name: str
    params: BackendBucketParams
    region: str
    selfLink: str
    selfLinkWithId: str
    usedBy: _list[BackendBucketUsedBy]

@typing.type_check_only
class BackendBucketAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendBucketCdnPolicy(typing.TypedDict, total=False):
    bypassCacheOnRequestHeaders: _list[BackendBucketCdnPolicyBypassCacheOnRequestHeader]
    cacheKeyPolicy: BackendBucketCdnPolicyCacheKeyPolicy
    cacheMode: typing.Literal[
        "CACHE_ALL_STATIC",
        "FORCE_CACHE_ALL",
        "INVALID_CACHE_MODE",
        "USE_ORIGIN_HEADERS",
    ]
    clientTtl: int
    defaultTtl: int
    maxTtl: int
    negativeCaching: bool
    negativeCachingPolicy: _list[BackendBucketCdnPolicyNegativeCachingPolicy]
    requestCoalescing: bool
    serveWhileStale: int
    signedUrlCacheMaxAgeSec: str
    signedUrlKeyNames: _list[str]

@typing.type_check_only
class BackendBucketCdnPolicyBypassCacheOnRequestHeader(typing.TypedDict, total=False):
    headerName: str

@typing.type_check_only
class BackendBucketCdnPolicyCacheKeyPolicy(typing.TypedDict, total=False):
    includeHttpHeaders: _list[str]
    queryStringWhitelist: _list[str]

@typing.type_check_only
class BackendBucketCdnPolicyNegativeCachingPolicy(typing.TypedDict, total=False):
    code: int
    ttl: int

@typing.type_check_only
class BackendBucketList(typing.TypedDict, total=False):
    id: str
    items: _list[BackendBucket]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendBucketListUsable(typing.TypedDict, total=False):
    id: str
    items: _list[BackendBucket]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendBucketParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class BackendBucketUsedBy(typing.TypedDict, total=False):
    reference: str

@typing.type_check_only
class BackendBucketsScopedList(typing.TypedDict, total=False):
    backendBuckets: _list[BackendBucket]
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendCustomMetric(typing.TypedDict, total=False):
    dryRun: bool
    maxUtilization: float
    name: str

@typing.type_check_only
class BackendService(typing.TypedDict, total=False):
    affinityCookieTtlSec: int
    allowMultinetwork: bool
    backends: _list[Backend]
    cdnPolicy: BackendServiceCdnPolicy
    circuitBreakers: CircuitBreakers
    compressionMode: typing.Literal["AUTOMATIC", "DISABLED"]
    connectionDraining: ConnectionDraining
    connectionTrackingPolicy: BackendServiceConnectionTrackingPolicy
    consistentHash: ConsistentHashLoadBalancerSettings
    creationTimestamp: str
    customMetrics: _list[BackendServiceCustomMetric]
    customRequestHeaders: _list[str]
    customResponseHeaders: _list[str]
    description: str
    dynamicForwarding: BackendServiceDynamicForwarding
    edgeSecurityPolicy: str
    enableCDN: bool
    externalManagedMigrationState: typing.Literal[
        "PREPARE", "TEST_ALL_TRAFFIC", "TEST_BY_PERCENTAGE"
    ]
    externalManagedMigrationTestingPercentage: float
    failoverPolicy: BackendServiceFailoverPolicy
    fingerprint: str
    haPolicy: BackendServiceHAPolicy
    healthChecks: _list[str]
    iap: BackendServiceIAP
    id: str
    ipAddressSelectionPolicy: typing.Literal[
        "IPV4_ONLY",
        "IPV6_ONLY",
        "IP_ADDRESS_SELECTION_POLICY_UNSPECIFIED",
        "PREFER_IPV6",
    ]
    kind: str
    loadBalancingScheme: typing.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "EXTERNAL_PASSTHROUGH",
        "INTERNAL",
        "INTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
        "INVALID_LOAD_BALANCING_SCHEME",
    ]
    localityLbPolicies: _list[BackendServiceLocalityLoadBalancingPolicyConfig]
    localityLbPolicy: typing.Literal[
        "INVALID_LB_POLICY",
        "LEAST_REQUEST",
        "MAGLEV",
        "ORIGINAL_DESTINATION",
        "RANDOM",
        "RING_HASH",
        "ROUND_ROBIN",
        "WEIGHTED_GCP_RENDEZVOUS",
        "WEIGHTED_MAGLEV",
        "WEIGHTED_ROUND_ROBIN",
    ]
    logConfig: BackendServiceLogConfig
    maxStreamDuration: Duration
    metadatas: dict[str, typing.Any]
    name: str
    network: str
    networkPassThroughLbTrafficPolicy: BackendServiceNetworkPassThroughLbTrafficPolicy
    orchestrationInfo: BackendServiceOrchestrationInfo
    outlierDetection: OutlierDetection
    params: BackendServiceParams
    port: int
    portName: str
    protocol: typing.Literal[
        "ALL",
        "GRPC",
        "H2C",
        "HTTP",
        "HTTP2",
        "HTTPS",
        "SSL",
        "TCP",
        "UDP",
        "UNSPECIFIED",
    ]
    region: str
    securityPolicy: str
    securitySettings: SecuritySettings
    selfLink: str
    selfLinkWithId: str
    serviceBindings: _list[str]
    serviceLbPolicy: str
    sessionAffinity: typing.Literal[
        "CLIENT_IP",
        "CLIENT_IP_NO_DESTINATION",
        "CLIENT_IP_PORT_PROTO",
        "CLIENT_IP_PROTO",
        "GENERATED_COOKIE",
        "HEADER_FIELD",
        "HTTP_COOKIE",
        "NONE",
        "STRONG_COOKIE_AFFINITY",
    ]
    strongSessionAffinityCookie: BackendServiceHttpCookie
    subsetting: Subsetting
    timeoutSec: int
    tlsSettings: BackendServiceTlsSettings
    usedBy: _list[BackendServiceUsedBy]

@typing.type_check_only
class BackendServiceAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceCdnPolicy(typing.TypedDict, total=False):
    bypassCacheOnRequestHeaders: _list[
        BackendServiceCdnPolicyBypassCacheOnRequestHeader
    ]
    cacheKeyPolicy: CacheKeyPolicy
    cacheMode: typing.Literal[
        "CACHE_ALL_STATIC",
        "FORCE_CACHE_ALL",
        "INVALID_CACHE_MODE",
        "USE_ORIGIN_HEADERS",
    ]
    clientTtl: int
    defaultTtl: int
    maxTtl: int
    negativeCaching: bool
    negativeCachingPolicy: _list[BackendServiceCdnPolicyNegativeCachingPolicy]
    requestCoalescing: bool
    serveWhileStale: int
    signedUrlCacheMaxAgeSec: str
    signedUrlKeyNames: _list[str]

@typing.type_check_only
class BackendServiceCdnPolicyBypassCacheOnRequestHeader(typing.TypedDict, total=False):
    headerName: str

@typing.type_check_only
class BackendServiceCdnPolicyNegativeCachingPolicy(typing.TypedDict, total=False):
    code: int
    ttl: int

@typing.type_check_only
class BackendServiceConnectionTrackingPolicy(typing.TypedDict, total=False):
    connectionPersistenceOnUnhealthyBackends: typing.Literal[
        "ALWAYS_PERSIST", "DEFAULT_FOR_PROTOCOL", "NEVER_PERSIST"
    ]
    enableStrongAffinity: bool
    idleTimeoutSec: int
    trackingMode: typing.Literal[
        "INVALID_TRACKING_MODE", "PER_CONNECTION", "PER_SESSION"
    ]

@typing.type_check_only
class BackendServiceCustomMetric(typing.TypedDict, total=False):
    dryRun: bool
    name: str

@typing.type_check_only
class BackendServiceDynamicForwarding(typing.TypedDict, total=False):
    forwardProxy: BackendServiceDynamicForwardingForwardProxy
    ipPortSelection: BackendServiceDynamicForwardingIpPortSelection

@typing.type_check_only
class BackendServiceDynamicForwardingForwardProxy(typing.TypedDict, total=False):
    enabled: bool
    proxyMode: typing.Literal["CLOUD_RUN", "DIRECT_FORWARDING"]

@typing.type_check_only
class BackendServiceDynamicForwardingIpPortSelection(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class BackendServiceFailoverPolicy(typing.TypedDict, total=False):
    disableConnectionDrainOnFailover: bool
    dropTrafficIfUnhealthy: bool
    failoverRatio: float

@typing.type_check_only
class BackendServiceGroupHealth(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    healthStatus: _list[HealthStatus]
    kind: str

@typing.type_check_only
class BackendServiceHAPolicy(typing.TypedDict, total=False):
    fastIPMove: typing.Literal["DISABLED", "GARP_RA"]
    leader: BackendServiceHAPolicyLeader

@typing.type_check_only
class BackendServiceHAPolicyLeader(typing.TypedDict, total=False):
    backendGroup: str
    networkEndpoint: BackendServiceHAPolicyLeaderNetworkEndpoint

@typing.type_check_only
class BackendServiceHAPolicyLeaderNetworkEndpoint(typing.TypedDict, total=False):
    instance: str

@typing.type_check_only
class BackendServiceHttpCookie(typing.TypedDict, total=False):
    name: str
    path: str
    ttl: Duration

@typing.type_check_only
class BackendServiceIAP(typing.TypedDict, total=False):
    enabled: bool
    oauth2ClientId: str
    oauth2ClientInfo: BackendServiceIAPOAuth2ClientInfo
    oauth2ClientSecret: str
    oauth2ClientSecretSha256: str

@typing.type_check_only
class BackendServiceIAPOAuth2ClientInfo(typing.TypedDict, total=False):
    applicationName: str
    clientName: str
    developerEmailAddress: str

@typing.type_check_only
class BackendServiceList(typing.TypedDict, total=False):
    id: str
    items: _list[BackendService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceListUsable(typing.TypedDict, total=False):
    id: str
    items: _list[BackendService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceLocalityLoadBalancingPolicyConfig(typing.TypedDict, total=False):
    customPolicy: BackendServiceLocalityLoadBalancingPolicyConfigCustomPolicy
    policy: BackendServiceLocalityLoadBalancingPolicyConfigPolicy

@typing.type_check_only
class BackendServiceLocalityLoadBalancingPolicyConfigCustomPolicy(
    typing.TypedDict, total=False
):
    data: str
    name: str

@typing.type_check_only
class BackendServiceLocalityLoadBalancingPolicyConfigPolicy(
    typing.TypedDict, total=False
):
    name: typing.Literal[
        "INVALID_LB_POLICY",
        "LEAST_REQUEST",
        "MAGLEV",
        "ORIGINAL_DESTINATION",
        "RANDOM",
        "RING_HASH",
        "ROUND_ROBIN",
        "WEIGHTED_GCP_RENDEZVOUS",
        "WEIGHTED_MAGLEV",
        "WEIGHTED_ROUND_ROBIN",
    ]

@typing.type_check_only
class BackendServiceLogConfig(typing.TypedDict, total=False):
    enable: bool
    loggingHttpRequestHeaders: _list[BackendServiceLogConfigLoggingHttpHeader]
    loggingHttpResponseHeaders: _list[BackendServiceLogConfigLoggingHttpHeader]
    optional: typing.Literal[
        "CUSTOM",
        "EXCLUDE_ALL_OPTIONAL",
        "INCLUDE_ALL_OPTIONAL",
        "UNSPECIFIED_OPTIONAL_MODE",
    ]
    optionalFields: _list[str]
    optionalMode: typing.Literal[
        "CUSTOM",
        "EXCLUDE_ALL_OPTIONAL",
        "INCLUDE_ALL_OPTIONAL",
        "UNSPECIFIED_OPTIONAL_MODE",
    ]
    sampleRate: float

@typing.type_check_only
class BackendServiceLogConfigLoggingHttpHeader(typing.TypedDict, total=False):
    headerName: str

@typing.type_check_only
class BackendServiceNetworkPassThroughLbTrafficPolicy(typing.TypedDict, total=False):
    zonalAffinity: BackendServiceNetworkPassThroughLbTrafficPolicyZonalAffinity

@typing.type_check_only
class BackendServiceNetworkPassThroughLbTrafficPolicyZonalAffinity(
    typing.TypedDict, total=False
):
    spillover: typing.Literal[
        "ZONAL_AFFINITY_DISABLED",
        "ZONAL_AFFINITY_SPILL_CROSS_ZONE",
        "ZONAL_AFFINITY_STAY_WITHIN_ZONE",
    ]
    spilloverRatio: float

@typing.type_check_only
class BackendServiceOrchestrationInfo(typing.TypedDict, total=False):
    resourceUri: str

@typing.type_check_only
class BackendServiceParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceReference(typing.TypedDict, total=False):
    backendService: str

@typing.type_check_only
class BackendServiceTlsSettings(typing.TypedDict, total=False):
    authenticationConfig: str
    identity: str
    sni: str
    subjectAltNames: _list[BackendServiceTlsSettingsSubjectAltName]

@typing.type_check_only
class BackendServiceTlsSettingsSubjectAltName(typing.TypedDict, total=False):
    dnsName: str
    uniformResourceIdentifier: str

@typing.type_check_only
class BackendServiceUsedBy(typing.TypedDict, total=False):
    reference: str

@typing.type_check_only
class BackendServicesGetEffectiveSecurityPoliciesResponse(
    typing.TypedDict, total=False
):
    securityPolicies: _list[SecurityPolicy]

@typing.type_check_only
class BackendServicesScopedList(typing.TypedDict, total=False):
    backendServices: _list[BackendService]
    warning: dict[str, typing.Any]

@typing.type_check_only
class BfdPacket(typing.TypedDict, total=False):
    authenticationPresent: bool
    controlPlaneIndependent: bool
    demand: bool
    diagnostic: typing.Literal[
        "ADMINISTRATIVELY_DOWN",
        "CONCATENATED_PATH_DOWN",
        "CONTROL_DETECTION_TIME_EXPIRED",
        "DIAGNOSTIC_UNSPECIFIED",
        "ECHO_FUNCTION_FAILED",
        "FORWARDING_PLANE_RESET",
        "NEIGHBOR_SIGNALED_SESSION_DOWN",
        "NO_DIAGNOSTIC",
        "PATH_DOWN",
        "REVERSE_CONCATENATED_PATH_DOWN",
    ]
    final: bool
    length: int
    minEchoRxIntervalMs: int
    minRxIntervalMs: int
    minTxIntervalMs: int
    multiplier: int
    multipoint: bool
    myDiscriminator: int
    poll: bool
    state: typing.Literal["ADMIN_DOWN", "DOWN", "INIT", "STATE_UNSPECIFIED", "UP"]
    version: int
    yourDiscriminator: int

@typing.type_check_only
class BfdStatus(typing.TypedDict, total=False):
    bfdSessionInitializationMode: typing.Literal["ACTIVE", "DISABLED", "PASSIVE"]
    configUpdateTimestampMicros: str
    controlPacketCounts: BfdStatusPacketCounts
    controlPacketIntervals: _list[PacketIntervals]
    echoPacketCounts: BfdStatusPacketCounts
    echoPacketIntervals: _list[PacketIntervals]
    localDiagnostic: typing.Literal[
        "ADMINISTRATIVELY_DOWN",
        "CONCATENATED_PATH_DOWN",
        "CONTROL_DETECTION_TIME_EXPIRED",
        "DIAGNOSTIC_UNSPECIFIED",
        "ECHO_FUNCTION_FAILED",
        "FORWARDING_PLANE_RESET",
        "NEIGHBOR_SIGNALED_SESSION_DOWN",
        "NO_DIAGNOSTIC",
        "PATH_DOWN",
        "REVERSE_CONCATENATED_PATH_DOWN",
    ]
    localState: typing.Literal["ADMIN_DOWN", "DOWN", "INIT", "STATE_UNSPECIFIED", "UP"]
    negotiatedLocalControlTxIntervalMs: int
    negotiatedLocalEchoTxIntervalMs: int
    rxPacket: BfdPacket
    txPacket: BfdPacket
    uptimeMs: str
    usingEchoMode: bool

@typing.type_check_only
class BfdStatusPacketCounts(typing.TypedDict, total=False):
    numRx: int
    numRxRejected: int
    numRxSuccessful: int
    numTx: int

@typing.type_check_only
class BgpRoute(typing.TypedDict, total=False):
    asPaths: _list[BgpRouteAsPath]
    communities: _list[str]
    destination: BgpRouteNetworkLayerReachabilityInformation
    med: int
    origin: typing.Literal["BGP_ORIGIN_EGP", "BGP_ORIGIN_IGP", "BGP_ORIGIN_INCOMPLETE"]

@typing.type_check_only
class BgpRouteAsPath(typing.TypedDict, total=False):
    asns: _list[int]
    asns32: _list[int]
    type: typing.Literal["AS_PATH_TYPE_SEQUENCE", "AS_PATH_TYPE_SET"]

@typing.type_check_only
class BgpRouteNetworkLayerReachabilityInformation(typing.TypedDict, total=False):
    pathId: int
    prefix: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BulkInsertDiskResource(typing.TypedDict, total=False):
    instantSnapshotGroupParameters: InstantSnapshotGroupParameters
    snapshotGroupParameters: SnapshotGroupParameters
    sourceConsistencyGroupPolicy: str

@typing.type_check_only
class BulkInsertInstanceResource(typing.TypedDict, total=False):
    count: str
    instanceFlexibilityPolicy: InstanceFlexibilityPolicy
    instanceProperties: InstanceProperties
    locationPolicy: LocationPolicy
    minCount: str
    namePattern: str
    perInstanceProperties: dict[str, typing.Any]
    sourceInstanceTemplate: str

@typing.type_check_only
class BulkInsertInstanceResourcePerInstanceProperties(typing.TypedDict, total=False):
    hostname: str
    name: str

@typing.type_check_only
class BulkInsertOperationStatus(typing.TypedDict, total=False):
    createdVmCount: int
    deletedVmCount: int
    failedToCreateVmCount: int
    status: typing.Literal["CREATING", "DONE", "ROLLING_BACK", "STATUS_UNSPECIFIED"]
    targetVmCount: int

@typing.type_check_only
class BulkSetLabelsRequest(typing.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class BulkZoneSetLabelsRequest(typing.TypedDict, total=False):
    requests: _list[BulkSetLabelsRequest]

@typing.type_check_only
class BundledLocalSsds(typing.TypedDict, total=False):
    defaultInterface: str
    partitionCount: int

@typing.type_check_only
class CacheInvalidationRule(typing.TypedDict, total=False):
    backendService: str
    cacheTags: _list[str]
    contentType: str
    host: str
    httpStatus: int
    path: str

@typing.type_check_only
class CacheKeyPolicy(typing.TypedDict, total=False):
    includeHost: bool
    includeHttpHeaders: _list[str]
    includeNamedCookies: _list[str]
    includeProtocol: bool
    includeQueryString: bool
    queryStringBlacklist: _list[str]
    queryStringWhitelist: _list[str]

@typing.type_check_only
class CachePolicy(typing.TypedDict, total=False):
    cacheBypassRequestHeaderNames: _list[str]
    cacheKeyPolicy: CachePolicyCacheKeyPolicy
    cacheMode: typing.Literal[
        "CACHE_ALL_STATIC", "FORCE_CACHE_ALL", "USE_ORIGIN_HEADERS"
    ]
    clientTtl: Duration
    defaultTtl: Duration
    maxTtl: Duration
    negativeCaching: bool
    negativeCachingPolicy: _list[CachePolicyNegativeCachingPolicy]
    requestCoalescing: bool
    serveWhileStale: Duration

@typing.type_check_only
class CachePolicyCacheKeyPolicy(typing.TypedDict, total=False):
    excludedQueryParameters: _list[str]
    includeHost: bool
    includeProtocol: bool
    includeQueryString: bool
    includedCookieNames: _list[str]
    includedHeaderNames: _list[str]
    includedQueryParameters: _list[str]

@typing.type_check_only
class CachePolicyNegativeCachingPolicy(typing.TypedDict, total=False):
    code: int
    ttl: Duration

@typing.type_check_only
class CalendarModeAdviceRequest(typing.TypedDict, total=False):
    futureResourcesSpecs: dict[str, typing.Any]

@typing.type_check_only
class CalendarModeAdviceResponse(typing.TypedDict, total=False):
    recommendations: _list[CalendarModeRecommendation]

@typing.type_check_only
class CalendarModeExtensionAdviceRequest(typing.TypedDict, total=False):
    endTimeNotLaterThan: str
    futureReservation: str

@typing.type_check_only
class CalendarModeExtensionAdviceResponse(typing.TypedDict, total=False):
    endTime: str
    notRecommendedReason: CalendarModeExtensionAdviceResponseNotRecommendedReason
    recommendationId: str

@typing.type_check_only
class CalendarModeExtensionAdviceResponseNotRecommendedReason(
    typing.TypedDict, total=False
):
    details: str
    status: typing.Literal[
        "CONDITIONS_NOT_MET", "NOT_RECOMMENDED_REASON_STATUS_UNSPECIFIED", "NO_CAPACITY"
    ]

@typing.type_check_only
class CalendarModeRecommendation(typing.TypedDict, total=False):
    recommendationsPerSpec: dict[str, typing.Any]

@typing.type_check_only
class CallCredentials(typing.TypedDict, total=False):
    callCredentialType: typing.Literal["FROM_PLUGIN", "GCE_VM", "INVALID"]
    fromPlugin: MetadataCredentialsFromPlugin

@typing.type_check_only
class CapacityAdviceRequest(typing.TypedDict, total=False):
    distributionPolicy: CapacityAdviceRequestDistributionPolicy
    instanceFlexibilityPolicy: CapacityAdviceRequestInstanceFlexibilityPolicy
    instanceProperties: CapacityAdviceRequestInstanceProperties
    size: int

@typing.type_check_only
class CapacityAdviceRequestDistributionPolicy(typing.TypedDict, total=False):
    targetShape: typing.Literal[
        "ANY", "ANY_SINGLE_ZONE", "BALANCED", "TARGET_SHAPE_UNSPECIFIED"
    ]
    zones: _list[CapacityAdviceRequestDistributionPolicyZoneConfiguration]

@typing.type_check_only
class CapacityAdviceRequestDistributionPolicyZoneConfiguration(
    typing.TypedDict, total=False
):
    zone: str

@typing.type_check_only
class CapacityAdviceRequestInstanceFlexibilityPolicy(typing.TypedDict, total=False):
    instanceSelections: dict[str, typing.Any]

@typing.type_check_only
class CapacityAdviceRequestInstanceFlexibilityPolicyInstanceSelection(
    typing.TypedDict, total=False
):
    disks: _list[
        CapacityAdviceRequestInstanceFlexibilityPolicyInstanceSelectionAttachedDisk
    ]
    guestAccelerators: _list[AcceleratorConfig]
    machineTypes: _list[str]

@typing.type_check_only
class CapacityAdviceRequestInstanceFlexibilityPolicyInstanceSelectionAttachedDisk(
    typing.TypedDict, total=False
):
    type: typing.Literal["DISK_TYPE_UNSPECIFIED", "SCRATCH"]

@typing.type_check_only
class CapacityAdviceRequestInstanceProperties(typing.TypedDict, total=False):
    acceleratorTopology: str
    scheduling: CapacityAdviceRequestInstancePropertiesScheduling

@typing.type_check_only
class CapacityAdviceRequestInstancePropertiesScheduling(typing.TypedDict, total=False):
    maxRunDuration: str
    provisioningModel: typing.Literal[
        "FLEX_START", "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]

@typing.type_check_only
class CapacityAdviceResponse(typing.TypedDict, total=False):
    recommendations: _list[CapacityAdviceResponseRecommendation]

@typing.type_check_only
class CapacityAdviceResponseRecommendation(typing.TypedDict, total=False):
    scores: CapacityAdviceResponseRecommendationScores
    shards: _list[CapacityAdviceResponseRecommendationShard]

@typing.type_check_only
class CapacityAdviceResponseRecommendationScores(typing.TypedDict, total=False):
    estimatedUptime: str
    estimatedWaitDuration: str
    obtainability: float
    uptimeScore: float

@typing.type_check_only
class CapacityAdviceResponseRecommendationShard(typing.TypedDict, total=False):
    instanceCount: int
    machineType: str
    provisioningModel: typing.Literal[
        "FLEX_START", "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]
    zone: str

@typing.type_check_only
class CapacityHistoryRequest(typing.TypedDict, total=False):
    instanceProperties: CapacityHistoryRequestInstanceProperties
    locationPolicy: CapacityHistoryRequestLocationPolicy
    types: _list[typing.Literal["HISTORY_TYPE_UNSPECIFIED", "PREEMPTION", "PRICE"]]

@typing.type_check_only
class CapacityHistoryRequestInstanceProperties(typing.TypedDict, total=False):
    machineType: str
    scheduling: CapacityHistoryRequestInstancePropertiesScheduling

@typing.type_check_only
class CapacityHistoryRequestInstancePropertiesScheduling(typing.TypedDict, total=False):
    provisioningModel: typing.Literal[
        "FLEX_START", "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]

@typing.type_check_only
class CapacityHistoryRequestLocationPolicy(typing.TypedDict, total=False):
    location: str

@typing.type_check_only
class CapacityHistoryResponse(typing.TypedDict, total=False):
    location: str
    machineType: str
    preemptionHistory: _list[CapacityHistoryResponsePreemptionRecord]
    priceHistory: _list[CapacityHistoryResponsePriceRecord]

@typing.type_check_only
class CapacityHistoryResponsePreemptionRecord(typing.TypedDict, total=False):
    interval: Interval
    preemptionRate: float

@typing.type_check_only
class CapacityHistoryResponsePriceRecord(typing.TypedDict, total=False):
    interval: Interval
    listPrice: Money

@typing.type_check_only
class ChannelCredentials(typing.TypedDict, total=False):
    certificates: TlsCertificatePaths
    channelCredentialType: typing.Literal["CERTIFICATES", "GCE_VM", "INVALID"]

@typing.type_check_only
class CircuitBreakers(typing.TypedDict, total=False):
    connectTimeout: Duration
    maxConnections: int
    maxPendingRequests: int
    maxRequests: int
    maxRequestsPerConnection: int
    maxRetries: int

@typing.type_check_only
class ClientTlsSettings(typing.TypedDict, total=False):
    clientTlsContext: TlsContext
    mode: typing.Literal["DISABLE", "INVALID", "MUTUAL", "SIMPLE"]
    sni: str
    subjectAltNames: _list[str]

@typing.type_check_only
class Commitment(typing.TypedDict, total=False):
    autoRenew: bool
    category: typing.Literal[
        "CATEGORY_UNSPECIFIED", "LICENSE", "MACHINE", "PERSISTENT_DISK"
    ]
    creationTimestamp: str
    customEndTimestamp: str
    description: str
    endTimestamp: str
    existingReservations: _list[str]
    id: str
    kind: str
    licenseResource: LicenseResourceCommitment
    mergeSourceCommitments: _list[str]
    name: str
    params: CommitmentParams
    persistentDiskResources: _list[PersistentDiskResourceCommitment]
    plan: typing.Literal[
        "INVALID",
        "SIXTY_MONTH",
        "THIRTY_SIX_MONTH",
        "TWELVE_MONTH",
        "TWENTY_FOUR_MONTH",
    ]
    region: str
    reservations: _list[Reservation]
    resourceStatus: CommitmentResourceStatus
    resources: _list[ResourceCommitment]
    selfLink: str
    selfLinkWithId: str
    splitSourceCommitment: str
    startTimestamp: str
    status: typing.Literal[
        "ACTIVE",
        "CANCELED_EARLY_TERMINATION",
        "CANCELING",
        "CANCELLED",
        "CREATING",
        "EXPIRED",
        "NOT_YET_ACTIVE",
    ]
    statusMessage: str
    type: typing.Literal[
        "ACCELERATOR_OPTIMIZED",
        "ACCELERATOR_OPTIMIZED_A3",
        "ACCELERATOR_OPTIMIZED_A3_MEGA",
        "ACCELERATOR_OPTIMIZED_A3_ULTRA",
        "ACCELERATOR_OPTIMIZED_A4",
        "ACCELERATOR_OPTIMIZED_A4X",
        "ACCELERATOR_OPTIMIZED_A4X_MAX",
        "ACCELERATOR_OPTIMIZED_A5X",
        "COMPUTE_OPTIMIZED",
        "COMPUTE_OPTIMIZED_C2D",
        "COMPUTE_OPTIMIZED_C3",
        "COMPUTE_OPTIMIZED_C3D",
        "COMPUTE_OPTIMIZED_H3",
        "COMPUTE_OPTIMIZED_H4D",
        "GENERAL_PURPOSE",
        "GENERAL_PURPOSE_C4",
        "GENERAL_PURPOSE_C4A",
        "GENERAL_PURPOSE_C4D",
        "GENERAL_PURPOSE_E2",
        "GENERAL_PURPOSE_N2",
        "GENERAL_PURPOSE_N2D",
        "GENERAL_PURPOSE_N4",
        "GENERAL_PURPOSE_N4A",
        "GENERAL_PURPOSE_N4D",
        "GENERAL_PURPOSE_T2D",
        "GRAPHICS_OPTIMIZED",
        "GRAPHICS_OPTIMIZED_G4",
        "GRAPHICS_OPTIMIZED_G4_VGPU",
        "MEMORY_OPTIMIZED",
        "MEMORY_OPTIMIZED_M3",
        "MEMORY_OPTIMIZED_M4",
        "MEMORY_OPTIMIZED_M4N",
        "MEMORY_OPTIMIZED_M4N_6TB",
        "MEMORY_OPTIMIZED_M4_6TB",
        "MEMORY_OPTIMIZED_X4",
        "MEMORY_OPTIMIZED_X4_1440_24T",
        "MEMORY_OPTIMIZED_X4_16TB",
        "MEMORY_OPTIMIZED_X4_1920_32T",
        "MEMORY_OPTIMIZED_X4_24TB",
        "MEMORY_OPTIMIZED_X4_32TB",
        "MEMORY_OPTIMIZED_X4_480_6T",
        "MEMORY_OPTIMIZED_X4_480_8T",
        "MEMORY_OPTIMIZED_X4_960_12T",
        "MEMORY_OPTIMIZED_X4_960_16T",
        "NETWORK_OPTIMIZED_C4N",
        "NETWORK_OPTIMIZED_U4C",
        "NETWORK_OPTIMIZED_U4P",
        "NETWORK_OPTIMIZED_U4S",
        "STORAGE_OPTIMIZED_Z3",
        "STORAGE_OPTIMIZED_Z4D",
        "STORAGE_OPTIMIZED_Z4M",
        "TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class CommitmentAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class CommitmentList(typing.TypedDict, total=False):
    id: str
    items: _list[Commitment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class CommitmentParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class CommitmentResourceStatus(typing.TypedDict, total=False):
    cancellationInformation: CommitmentResourceStatusCancellationInformation
    customTermEligibilityEndTimestamp: str

@typing.type_check_only
class CommitmentResourceStatusCancellationInformation(typing.TypedDict, total=False):
    canceledCommitment: Money
    canceledCommitmentLastUpdatedTimestamp: str
    cancellationCap: Money
    cancellationFee: Money
    cancellationFeeExpirationTimestamp: str

@typing.type_check_only
class CommitmentsScopedList(typing.TypedDict, total=False):
    commitments: _list[Commitment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class CompositeHealthCheck(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    healthDestination: str
    healthSources: _list[str]
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class CompositeHealthCheckAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class CompositeHealthCheckHealth(typing.TypedDict, total=False):
    healthSources: _list[CompositeHealthChecksGetHealthResponseHealthSourceHealth]
    healthState: typing.Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
    kind: str

@typing.type_check_only
class CompositeHealthCheckList(typing.TypedDict, total=False):
    id: str
    items: _list[CompositeHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class CompositeHealthChecksGetHealthResponseHealthSourceHealth(
    typing.TypedDict, total=False
):
    healthState: typing.Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
    source: str

@typing.type_check_only
class CompositeHealthChecksScopedList(typing.TypedDict, total=False):
    compositeHealthChecks: _list[CompositeHealthCheck]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ConfidentialInstanceConfig(typing.TypedDict, total=False):
    confidentialInstanceType: typing.Literal[
        "CCA", "CONFIDENTIAL_INSTANCE_TYPE_UNSPECIFIED", "SEV", "SEV_SNP", "TDX"
    ]
    confidentialParavisorConfig: ConfidentialParavisorConfig
    enableConfidentialCompute: bool

@typing.type_check_only
class ConfidentialParavisorConfig(typing.TypedDict, total=False):
    confidentialTpmType: typing.Literal[
        "CONFIDENTIAL_TPM_TYPE_UNSPECIFIED", "EPHEMERAL", "NO_CC_TPM"
    ]
    sevSnpIrqMode: typing.Literal[
        "RESTRICTED", "SEV_SNP_IRQ_MODE_UNSPECIFIED", "UNRESTRICTED"
    ]

@typing.type_check_only
class ConnectionDraining(typing.TypedDict, total=False):
    drainingTimeoutSec: int

@typing.type_check_only
class ConsistentHashLoadBalancerSettings(typing.TypedDict, total=False):
    httpCookie: ConsistentHashLoadBalancerSettingsHttpCookie
    httpHeaderName: str
    minimumRingSize: str

@typing.type_check_only
class ConsistentHashLoadBalancerSettingsHttpCookie(typing.TypedDict, total=False):
    name: str
    path: str
    ttl: Duration

@typing.type_check_only
class CorsPolicy(typing.TypedDict, total=False):
    allowCredentials: bool
    allowHeaders: _list[str]
    allowMethods: _list[str]
    allowOriginRegexes: _list[str]
    allowOrigins: _list[str]
    disabled: bool
    exposeHeaders: _list[str]
    maxAge: int

@typing.type_check_only
class CrossSiteNetwork(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class CrossSiteNetworkList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[CrossSiteNetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class CustomErrorResponsePolicy(typing.TypedDict, total=False):
    errorResponseRules: _list[CustomErrorResponsePolicyCustomErrorResponseRule]
    errorService: str

@typing.type_check_only
class CustomErrorResponsePolicyCustomErrorResponseRule(typing.TypedDict, total=False):
    matchResponseCodes: _list[str]
    overrideResponseCode: int
    path: str

@typing.type_check_only
class CustomerEncryptionKey(typing.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyServiceAccount: str
    rawKey: str
    rsaEncryptedKey: str
    sha256: str

@typing.type_check_only
class CustomerEncryptionKeyProtectedDisk(typing.TypedDict, total=False):
    diskEncryptionKey: CustomerEncryptionKey
    source: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateTime(typing.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: TimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class DeprecationStatus(typing.TypedDict, total=False):
    deleted: str
    deprecated: str
    obsolete: str
    replacement: str
    state: typing.Literal["ACTIVE", "DELETED", "DEPRECATED", "OBSOLETE"]
    stateOverride: RolloutPolicy

@typing.type_check_only
class DhcpOptionsConfig(typing.TypedDict, total=False):
    associations: dict[str, typing.Any]
    bootFileIpv4Name: str
    bootFileIpv6Parameters: _list[str]
    bootFileIpv6Url: str
    creationTimestamp: str
    description: str
    dnsSearchPaths: _list[str]
    dnsServerIpv4Addresses: _list[str]
    dnsServerIpv6Addresses: _list[str]
    domainName: str
    id: str
    kind: str
    leaseTimeSec: str
    name: str
    ntpServerIpv4Addresses: _list[str]
    ntpServerIpv6Addresses: _list[str]
    region: str
    selfLink: str
    tftpServerIpv4Addresses: _list[str]
    tftpServerIpv4Name: str

@typing.type_check_only
class DhcpOptionsConfigAssociation(typing.TypedDict, total=False):
    network: str
    networkId: str
    state: typing.Literal["ACTIVE", "ORPHANED", "STATE_UNSPECIFIED"]

@typing.type_check_only
class DhcpOptionsConfigList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[DhcpOptionsConfig]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Disk(typing.TypedDict, total=False):
    accessMode: typing.Literal["READ_ONLY_MANY", "READ_WRITE_MANY", "READ_WRITE_SINGLE"]
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    asyncPrimaryDisk: DiskAsyncReplication
    asyncSecondaryDisks: dict[str, typing.Any]
    creationTimestamp: str
    description: str
    diskEncryptionKey: CustomerEncryptionKey
    enableConfidentialCompute: bool
    eraseWindowsVssSignature: bool
    guestOsFeatures: _list[GuestOsFeature]
    id: str
    interface: typing.Literal["NVME", "SCSI", "UNSPECIFIED"]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    lastAttachTimestamp: str
    lastDetachTimestamp: str
    licenseCodes: _list[str]
    licenses: _list[str]
    locationHint: str
    locked: bool
    multiWriter: bool
    name: str
    options: str
    params: DiskParams
    physicalBlockSizeBytes: str
    provisionedIops: str
    provisionedThroughput: str
    region: str
    replicaZones: _list[str]
    resourcePolicies: _list[str]
    resourceStatus: DiskResourceStatus
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    sizeGb: str
    sourceConsistencyGroupPolicy: str
    sourceConsistencyGroupPolicyId: str
    sourceDisk: str
    sourceDiskId: str
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceImageId: str
    sourceInstantSnapshot: str
    sourceInstantSnapshotId: str
    sourceMachineImage: str
    sourceMachineImageDiskDeviceName: str
    sourceMachineImageEncryptionKey: CustomerEncryptionKey
    sourceMachineImageId: str
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey
    sourceSnapshotId: str
    sourceStorageObject: str
    status: typing.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RESTORING", "UNAVAILABLE"
    ]
    storagePool: str
    storageType: typing.Literal["HDD", "SSD"]
    type: str
    users: _list[str]
    zone: str

@typing.type_check_only
class DiskAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskAsyncReplication(typing.TypedDict, total=False):
    consistencyGroupPolicy: str
    consistencyGroupPolicyId: str
    disk: str
    diskId: str

@typing.type_check_only
class DiskAsyncReplicationList(typing.TypedDict, total=False):
    asyncReplicationDisk: DiskAsyncReplication

@typing.type_check_only
class DiskConvertParams(typing.TypedDict, total=False):
    forceStopInProgressSnapshot: bool
    provisionedIops: str
    provisionedThroughput: str
    quickConversionOnly: bool
    resetSupportedVmFamilies: bool
    targetDiskType: str

@typing.type_check_only
class DiskInstantiationConfig(typing.TypedDict, total=False):
    autoDelete: bool
    customImage: str
    deviceName: str
    instantiateFrom: typing.Literal[
        "ATTACH_READ_ONLY",
        "BLANK",
        "CUSTOM_IMAGE",
        "DEFAULT",
        "DO_NOT_INCLUDE",
        "SOURCE_IMAGE",
        "SOURCE_IMAGE_FAMILY",
    ]

@typing.type_check_only
class DiskList(typing.TypedDict, total=False):
    id: str
    items: _list[Disk]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskMoveRequest(typing.TypedDict, total=False):
    destinationZone: str
    targetDisk: str

@typing.type_check_only
class DiskPairReplicationState(typing.TypedDict, total=False):
    dataReplicationState: typing.Literal[
        "ASYNC_REPLICATION_STATE_INITIALIZING",
        "ASYNC_REPLICATION_STATE_REPLICATING_BEHIND_CG_HIGH_CHURN",
        "ASYNC_REPLICATION_STATE_REPLICATING_BEHIND_HIGH_CHURN",
        "ASYNC_REPLICATION_STATE_REPLICATING_BEHIND_SYSTEM_LAGGING",
        "ASYNC_REPLICATION_STATE_REPLICATING_HEALTHY",
        "ASYNC_REPLICATION_STATE_REPLICATION_STUCK",
        "ASYNC_REPLICATION_STATE_STOPPED",
        "ASYNC_REPLICATION_STATE_STOPPING",
        "ASYNC_REPLICATION_STATE_UNSPECIFIED",
    ]
    replicationDiskPair: ReplicationDiskPair

@typing.type_check_only
class DiskParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class DiskResourceStatus(typing.TypedDict, total=False):
    asyncPrimaryDisk: DiskResourceStatusAsyncReplicationStatus
    asyncSecondaryDisks: dict[str, typing.Any]
    usedBytes: str

@typing.type_check_only
class DiskResourceStatusAsyncReplicationStatus(typing.TypedDict, total=False):
    state: typing.Literal[
        "ACTIVE", "CREATED", "STARTING", "STATE_UNSPECIFIED", "STOPPED", "STOPPING"
    ]

@typing.type_check_only
class DiskSettings(typing.TypedDict, total=False):
    accessLocation: DiskSettingsAccessLocation
    defaultResourcePolicies: dict[str, typing.Any]

@typing.type_check_only
class DiskSettingsAccessLocation(typing.TypedDict, total=False):
    locations: dict[str, typing.Any]
    policy: typing.Literal["ALL_REGIONS", "POLICY_UNSPECIFIED", "SPECIFIC_REGIONS"]

@typing.type_check_only
class DiskSettingsAccessLocationAccessLocationPreference(typing.TypedDict, total=False):
    region: str

@typing.type_check_only
class DiskSettingsResourcePolicyDetails(typing.TypedDict, total=False):
    excludedDiskTypes: _list[str]
    resourcePolicy: str

@typing.type_check_only
class DiskType(typing.TypedDict, total=False):
    creationTimestamp: str
    defaultDiskSizeGb: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    selfLinkWithId: str
    validDiskSize: str
    zone: str

@typing.type_check_only
class DiskTypeAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskTypeList(typing.TypedDict, total=False):
    id: str
    items: _list[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskTypesScopedList(typing.TypedDict, total=False):
    diskTypes: _list[DiskType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskUpdateKmsKeyRequest(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class DisksAddResourcePoliciesRequest(typing.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class DisksConvertRequest(typing.TypedDict, total=False):
    params: DiskConvertParams

@typing.type_check_only
class DisksRemoveResourcePoliciesRequest(typing.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class DisksResizeRequest(typing.TypedDict, total=False):
    sizeGb: str

@typing.type_check_only
class DisksScopedList(typing.TypedDict, total=False):
    disks: _list[Disk]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DisksStartAsyncReplicationRequest(typing.TypedDict, total=False):
    asyncSecondaryDisk: str

@typing.type_check_only
class DisksStopGroupAsyncReplicationResource(typing.TypedDict, total=False):
    resourcePolicy: str

@typing.type_check_only
class DisplayDevice(typing.TypedDict, total=False):
    enableDisplay: bool

@typing.type_check_only
class DistributionPolicy(typing.TypedDict, total=False):
    targetShape: typing.Literal["ANY", "ANY_SINGLE_ZONE", "BALANCED", "EVEN"]
    zones: _list[DistributionPolicyZoneConfiguration]

@typing.type_check_only
class DistributionPolicyZoneConfiguration(typing.TypedDict, total=False):
    zone: str

@typing.type_check_only
class Duration(typing.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    domain: str
    metadatas: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class ExchangedPeeringRoute(typing.TypedDict, total=False):
    destRange: str
    imported: bool
    nextHopRegion: str
    priority: int
    type: typing.Literal[
        "DYNAMIC_PEERING_ROUTE", "STATIC_PEERING_ROUTE", "SUBNET_PEERING_ROUTE"
    ]

@typing.type_check_only
class ExchangedPeeringRoutesList(typing.TypedDict, total=False):
    id: str
    items: _list[ExchangedPeeringRoute]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalVpnGateway(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    interfaces: _list[ExternalVpnGatewayInterface]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    params: ExternalVpnGatewayParams
    redundancyType: typing.Literal[
        "FOUR_IPS_REDUNDANCY", "SINGLE_IP_INTERNALLY_REDUNDANT", "TWO_IPS_REDUNDANCY"
    ]
    selfLink: str

@typing.type_check_only
class ExternalVpnGatewayInterface(typing.TypedDict, total=False):
    id: int
    ipAddress: str
    ipv6Address: str

@typing.type_check_only
class ExternalVpnGatewayList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[ExternalVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ExternalVpnGatewayParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class FileContentBuffer(typing.TypedDict, total=False):
    content: str
    fileType: typing.Literal["BIN", "UNDEFINED", "X509"]

@typing.type_check_only
class Firewall(typing.TypedDict, total=False):
    allowed: _list[dict[str, typing.Any]]
    creationTimestamp: str
    denied: _list[dict[str, typing.Any]]
    description: str
    destinationRanges: _list[str]
    direction: typing.Literal["EGRESS", "INGRESS"]
    disabled: bool
    enableLogging: bool
    id: str
    kind: str
    logConfig: FirewallLogConfig
    name: str
    network: str
    params: FirewallParams
    priority: int
    selfLink: str
    selfLinkWithId: str
    sourceRanges: _list[str]
    sourceServiceAccounts: _list[str]
    sourceTags: _list[str]
    targetServiceAccounts: _list[str]
    targetTags: _list[str]

@typing.type_check_only
class FirewallList(typing.TypedDict, total=False):
    id: str
    items: _list[Firewall]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class FirewallLogConfig(typing.TypedDict, total=False):
    enable: bool
    metadata: typing.Literal["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]

@typing.type_check_only
class FirewallParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class FirewallPoliciesListAssociationsResponse(typing.TypedDict, total=False):
    associations: _list[FirewallPolicyAssociation]
    kind: str

@typing.type_check_only
class FirewallPoliciesScopedList(typing.TypedDict, total=False):
    firewallPolicies: _list[FirewallPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FirewallPolicy(typing.TypedDict, total=False):
    associations: _list[FirewallPolicyAssociation]
    creationTimestamp: str
    description: str
    displayName: str
    fingerprint: str
    id: str
    kind: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    parent: str
    policySource: typing.Literal["SYSTEM", "USER_DEFINED"]
    policyType: typing.Literal[
        "RDMA_FALCON_POLICY", "RDMA_ROCE_POLICY", "ULL_POLICY", "VPC_POLICY"
    ]
    region: str
    rolloutOperation: FirewallPolicyRolloutOperation
    ruleTupleCount: int
    rules: _list[FirewallPolicyRule]
    selfLink: str
    selfLinkWithId: str
    shortName: str
    vpcNetworkScope: typing.Literal["GLOBAL_VPC_NETWORK", "REGIONAL_VPC_NETWORK"]

@typing.type_check_only
class FirewallPolicyAssociation(typing.TypedDict, total=False):
    attachmentTarget: str
    displayName: str
    firewallPolicyId: str
    name: str
    priority: int
    shortName: str

@typing.type_check_only
class FirewallPolicyList(typing.TypedDict, total=False):
    id: str
    items: _list[FirewallPolicy]
    kind: str
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class FirewallPolicyRolloutOperation(typing.TypedDict, total=False):
    rolloutInput: FirewallPolicyRolloutOperationRolloutInput
    rolloutStatus: FirewallPolicyRolloutOperationRolloutStatus

@typing.type_check_only
class FirewallPolicyRolloutOperationRolloutInput(typing.TypedDict, total=False):
    name: str
    predefinedRolloutPlan: typing.Literal["DEFAULT_ROLLOUT_PLAN"]
    retryUuid: str

@typing.type_check_only
class FirewallPolicyRolloutOperationRolloutStatus(typing.TypedDict, total=False):
    nextRollout: FirewallPolicyRolloutOperationRolloutStatusNextRollout
    ongoingRollouts: _list[FirewallPolicyRolloutOperationRolloutStatusRolloutMetadata]
    previousRollout: FirewallPolicyRolloutOperationRolloutStatusRolloutMetadata

@typing.type_check_only
class FirewallPolicyRolloutOperationRolloutStatusNextRollout(
    typing.TypedDict, total=False
):
    rolloutId: str
    rolloutPlan: str

@typing.type_check_only
class FirewallPolicyRolloutOperationRolloutStatusRolloutMetadata(
    typing.TypedDict, total=False
):
    rollout: str
    rolloutPlan: str
    state: typing.Literal[
        "CANCELLED", "COMPLETED", "FAILED", "PAUSED", "PROCESSING", "UNKNOWN"
    ]

@typing.type_check_only
class FirewallPolicyRule(typing.TypedDict, total=False):
    action: str
    description: str
    direction: typing.Literal["EGRESS", "INGRESS"]
    disabled: bool
    enableLogging: bool
    kind: str
    match: FirewallPolicyRuleMatcher
    priority: int
    ruleName: str
    ruleTupleCount: int
    securityProfileGroup: str
    targetForwardingRules: _list[str]
    targetResources: _list[str]
    targetSecureTags: _list[FirewallPolicyRuleSecureTag]
    targetServiceAccounts: _list[str]
    targetType: typing.Literal["INSTANCES", "INTERNAL_MANAGED_LB"]
    tlsInspect: bool

@typing.type_check_only
class FirewallPolicyRuleMatcher(typing.TypedDict, total=False):
    destAddressGroups: _list[str]
    destFqdns: _list[str]
    destIpRanges: _list[str]
    destNetworkContext: typing.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    destNetworkScope: typing.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    destNetworkType: typing.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    destRegionCodes: _list[str]
    destThreatIntelligences: _list[str]
    layer4Configs: _list[FirewallPolicyRuleMatcherLayer4Config]
    srcAddressGroups: _list[str]
    srcFqdns: _list[str]
    srcIpRanges: _list[str]
    srcNetworkContext: typing.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    srcNetworkScope: typing.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    srcNetworkType: typing.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    srcNetworks: _list[str]
    srcRegionCodes: _list[str]
    srcSecureTags: _list[FirewallPolicyRuleSecureTag]
    srcThreatIntelligences: _list[str]

@typing.type_check_only
class FirewallPolicyRuleMatcherLayer4Config(typing.TypedDict, total=False):
    ipProtocol: str
    ports: _list[str]

@typing.type_check_only
class FirewallPolicyRuleOperationMetadata(typing.TypedDict, total=False):
    allocatedPriority: int

@typing.type_check_only
class FirewallPolicyRuleSecureTag(typing.TypedDict, total=False):
    name: str
    state: typing.Literal["EFFECTIVE", "INEFFECTIVE"]

@typing.type_check_only
class FixedOrPercent(typing.TypedDict, total=False):
    calculated: int
    fixed: int
    percent: int

@typing.type_check_only
class FlexibleTimeRange(typing.TypedDict, total=False):
    endTimeNotEarlierThan: str
    endTimeNotLaterThan: str
    maxDuration: str
    minDuration: str
    startTimeNotEarlierThan: str
    startTimeNotLaterThan: str

@typing.type_check_only
class FolderVmExtensionPolicyAggregatedListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ForwardingRule(typing.TypedDict, total=False):
    IPAddress: str
    IPAddresses: _list[str]
    IPProtocol: typing.Literal[
        "AH", "ALL", "ESP", "ICMP", "L3_DEFAULT", "SCTP", "TCP", "UDP"
    ]
    allPorts: bool
    allowGlobalAccess: bool
    allowPscGlobalAccess: bool
    attachedExtensions: _list[ForwardingRuleAttachedExtension]
    availabilityGroup: typing.Literal[
        "AVAILABILITY_GROUP0", "AVAILABILITY_GROUP1", "AVAILABILITY_GROUP_UNSPECIFIED"
    ]
    backendService: str
    baseForwardingRule: str
    childForwardingRules: _list[str]
    creationTimestamp: str
    description: str
    externalManagedBackendBucketMigrationState: typing.Literal[
        "PREPARE", "TEST_ALL_TRAFFIC", "TEST_BY_PERCENTAGE"
    ]
    externalManagedBackendBucketMigrationTestingPercentage: float
    fingerprint: str
    id: str
    ipCollection: str
    ipVersion: typing.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    isMirroringCollector: bool
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "EXTERNAL_PASSTHROUGH",
        "INTERNAL",
        "INTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
        "INVALID",
    ]
    metadataFilters: _list[MetadataFilter]
    name: str
    network: str
    networkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    noAutomateDnsZone: bool
    parentForwardingRule: str
    portRange: str
    ports: _list[str]
    pscConnectionId: str
    pscConnectionStatus: typing.Literal[
        "ACCEPTED",
        "ACCEPTED_LIMITED_CAPACITY",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    serviceDirectoryRegistrations: _list[ForwardingRuleServiceDirectoryRegistration]
    serviceLabel: str
    serviceName: str
    sourceIpRanges: _list[str]
    subnetwork: str
    target: str

@typing.type_check_only
class ForwardingRuleAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ForwardingRuleAttachedExtension(typing.TypedDict, total=False):
    reference: str

@typing.type_check_only
class ForwardingRuleList(typing.TypedDict, total=False):
    id: str
    items: _list[ForwardingRule]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ForwardingRuleReference(typing.TypedDict, total=False):
    forwardingRule: str

@typing.type_check_only
class ForwardingRuleServiceDirectoryRegistration(typing.TypedDict, total=False):
    namespace: str
    service: str
    serviceDirectoryRegion: str

@typing.type_check_only
class ForwardingRulesScopedList(typing.TypedDict, total=False):
    forwardingRules: _list[ForwardingRule]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FutureReservation(typing.TypedDict, total=False):
    advancedDeploymentControl: ReservationAdvancedDeploymentControl
    aggregateReservation: AllocationAggregateReservation
    autoCreatedReservationsDeleteTime: str
    autoCreatedReservationsDuration: Duration
    autoDeleteAutoCreatedReservations: bool
    colocationResource: str
    commitmentInfo: FutureReservationCommitmentInfo
    confidentialComputeType: typing.Literal[
        "CONFIDENTIAL_COMPUTE_TYPE_TDX", "CONFIDENTIAL_COMPUTE_TYPE_UNSPECIFIED"
    ]
    creationTimestamp: str
    deploymentType: typing.Literal["DENSE", "DEPLOYMENT_TYPE_UNSPECIFIED", "FLEXIBLE"]
    description: str
    enableEmergentMaintenance: bool
    id: str
    kind: str
    name: str
    namePrefix: str
    params: FutureReservationParams
    planningStatus: typing.Literal["DRAFT", "PLANNING_STATUS_UNSPECIFIED", "SUBMITTED"]
    protectionTier: typing.Literal[
        "CAPACITY_OPTIMIZED", "PROTECTION_TIER_UNSPECIFIED", "STANDARD"
    ]
    reservationMode: typing.Literal[
        "CALENDAR", "DEFAULT", "RESERVATION_MODE_UNSPECIFIED"
    ]
    reservationName: str
    resourceName: str
    schedulingType: typing.Literal[
        "GROUPED", "GROUP_MAINTENANCE_TYPE_UNSPECIFIED", "INDEPENDENT"
    ]
    selfLink: str
    selfLinkWithId: str
    shareSettings: ShareSettings
    specificReservationRequired: bool
    specificSkuProperties: FutureReservationSpecificSKUProperties
    status: FutureReservationStatus
    storagePoolProperties: FutureReservationStoragePoolProperties
    timeWindow: FutureReservationTimeWindow
    zone: str

@typing.type_check_only
class FutureReservationCommitmentInfo(typing.TypedDict, total=False):
    commitmentName: str
    commitmentPlan: typing.Literal[
        "INVALID",
        "SIXTY_MONTH",
        "THIRTY_SIX_MONTH",
        "TWELVE_MONTH",
        "TWENTY_FOUR_MONTH",
    ]
    previousCommitmentTerms: typing.Literal[
        "EXTEND", "PREVIOUSCOMMITMENTTERM_UNSPECIFIED"
    ]

@typing.type_check_only
class FutureReservationParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class FutureReservationSpecificSKUProperties(typing.TypedDict, total=False):
    instanceProperties: AllocationSpecificSKUAllocationReservedInstanceProperties
    sourceInstanceTemplate: str
    totalCount: str

@typing.type_check_only
class FutureReservationStatus(typing.TypedDict, total=False):
    amendmentStatus: typing.Literal[
        "AMENDMENT_APPROVED",
        "AMENDMENT_DECLINED",
        "AMENDMENT_IN_REVIEW",
        "AMENDMENT_STATUS_UNSPECIFIED",
    ]
    autoCreatedReservations: _list[str]
    exapoolProvisionedCapacityGb: StoragePoolExapoolProvisionedCapacityGb
    existingMatchingUsageInfo: FutureReservationStatusExistingMatchingUsageInfo
    fulfilledCount: str
    lastKnownGoodState: FutureReservationStatusLastKnownGoodState
    lockTime: str
    procurementStatus: typing.Literal[
        "APPROVED",
        "CANCELLED",
        "COMMITTED",
        "DECLINED",
        "DRAFTING",
        "FAILED",
        "FAILED_PARTIALLY_FULFILLED",
        "FULFILLED",
        "PENDING_AMENDMENT_APPROVAL",
        "PENDING_APPROVAL",
        "PROCUREMENT_STATUS_UNSPECIFIED",
        "PROCURING",
        "PROVISIONING",
    ]
    specificSkuProperties: FutureReservationStatusSpecificSKUProperties
    storagePoolProvisionedCapacity: FutureReservationStoragePoolProvisionedCapacity

@typing.type_check_only
class FutureReservationStatusExistingMatchingUsageInfo(typing.TypedDict, total=False):
    count: str
    timestamp: str

@typing.type_check_only
class FutureReservationStatusLastKnownGoodState(typing.TypedDict, total=False):
    description: str
    existingMatchingUsageInfo: FutureReservationStatusExistingMatchingUsageInfo
    futureReservationSpecs: (
        FutureReservationStatusLastKnownGoodStateFutureReservationSpecs
    )
    lockTime: str
    namePrefix: str
    procurementStatus: typing.Literal[
        "APPROVED",
        "CANCELLED",
        "COMMITTED",
        "DECLINED",
        "DRAFTING",
        "FAILED",
        "FAILED_PARTIALLY_FULFILLED",
        "FULFILLED",
        "PENDING_AMENDMENT_APPROVAL",
        "PENDING_APPROVAL",
        "PROCUREMENT_STATUS_UNSPECIFIED",
        "PROCURING",
        "PROVISIONING",
    ]

@typing.type_check_only
class FutureReservationStatusLastKnownGoodStateFutureReservationSpecs(
    typing.TypedDict, total=False
):
    shareSettings: ShareSettings
    specificSkuProperties: FutureReservationSpecificSKUProperties
    timeWindow: FutureReservationTimeWindow

@typing.type_check_only
class FutureReservationStatusSpecificSKUProperties(typing.TypedDict, total=False):
    sourceInstanceTemplateId: str

@typing.type_check_only
class FutureReservationStoragePoolProperties(typing.TypedDict, total=False):
    requestedExapoolProvisionedCapacityGb: StoragePoolExapoolProvisionedCapacityGb
    requestedStoragePoolProvisionedCapacity: (
        FutureReservationStoragePoolProvisionedCapacity
    )
    storagePoolType: str

@typing.type_check_only
class FutureReservationStoragePoolProvisionedCapacity(typing.TypedDict, total=False):
    poolProvisionedCapacityGb: str
    poolProvisionedIops: str
    poolProvisionedThroughput: str

@typing.type_check_only
class FutureReservationTimeWindow(typing.TypedDict, total=False):
    duration: Duration
    endTime: str
    startTime: str

@typing.type_check_only
class FutureReservationsAggregatedListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FutureReservationsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[FutureReservation]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FutureReservationsScopedList(typing.TypedDict, total=False):
    futureReservations: _list[FutureReservation]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FutureResourcesRecommendation(typing.TypedDict, total=False):
    endTime: str
    location: str
    otherLocations: dict[str, typing.Any]
    recommendationId: str
    recommendationType: typing.Literal[
        "FUTURE_RESERVATION", "RECOMMENDATION_TYPE_UNSPECIFIED"
    ]
    startTime: str

@typing.type_check_only
class FutureResourcesRecommendationOtherLocation(typing.TypedDict, total=False):
    details: str
    status: typing.Literal[
        "CONDITIONS_NOT_MET",
        "NOT_SUPPORTED",
        "NO_CAPACITY",
        "OTHER_LOCATION_STATUS_UNDEFINED",
        "RECOMMENDED",
    ]

@typing.type_check_only
class FutureResourcesSpec(typing.TypedDict, total=False):
    deploymentType: typing.Literal["DENSE", "DEPLOYMENT_TYPE_UNSPECIFIED", "FLEXIBLE"]
    locationPolicy: FutureResourcesSpecLocationPolicy
    targetResources: FutureResourcesSpecTargetResources
    timeRangeSpec: FlexibleTimeRange

@typing.type_check_only
class FutureResourcesSpecAggregateResources(typing.TypedDict, total=False):
    acceleratorCount: str
    vmFamily: typing.Literal[
        "VM_FAMILY_CLOUD_TPU_DEVICE_CT3",
        "VM_FAMILY_CLOUD_TPU_LITE_DEVICE_CT5L",
        "VM_FAMILY_CLOUD_TPU_LITE_POD_SLICE_CT5LP",
        "VM_FAMILY_CLOUD_TPU_LITE_POD_SLICE_CT6E",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT3P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT4P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT5P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU7",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU7X",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU8I_METAL",
    ]
    workloadType: typing.Literal["BATCH", "SERVING", "UNSPECIFIED"]

@typing.type_check_only
class FutureResourcesSpecLocalSsdPartition(typing.TypedDict, total=False):
    diskInterface: typing.Literal["NVDIMM", "NVME", "SCSI"]
    diskSizeGb: str

@typing.type_check_only
class FutureResourcesSpecLocationPolicy(typing.TypedDict, total=False):
    locations: dict[str, typing.Any]

@typing.type_check_only
class FutureResourcesSpecLocationPolicyLocation(typing.TypedDict, total=False):
    preference: typing.Literal["ALLOW", "DENY", "PREFERENCE_UNSPECIFIED"]

@typing.type_check_only
class FutureResourcesSpecSpecificSKUResources(typing.TypedDict, total=False):
    instanceCount: str
    localSsdPartitions: _list[FutureResourcesSpecLocalSsdPartition]
    machineType: str

@typing.type_check_only
class FutureResourcesSpecTargetResources(typing.TypedDict, total=False):
    aggregateResources: FutureResourcesSpecAggregateResources
    specificSkuResources: FutureResourcesSpecSpecificSKUResources

@typing.type_check_only
class GRPCHealthCheck(typing.TypedDict, total=False):
    grpcServiceName: str
    port: int
    portName: str
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]

@typing.type_check_only
class GRPCTLSHealthCheck(typing.TypedDict, total=False):
    grpcServiceName: str
    port: int
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]

@typing.type_check_only
class GetAsyncReplicationStatusResponse(typing.TypedDict, total=False):
    asyncReplicationStatus: AsyncReplicationStatus
    etag: str

@typing.type_check_only
class GetHealthOperationMetadata(typing.TypedDict, total=False):
    healthInfo: GetHealthOperationMetadataHealthInfo

@typing.type_check_only
class GetHealthOperationMetadataHealthInfo(typing.TypedDict, total=False):
    availabilitySloStatus: typing.Literal[
        "AVAILABILITY_SLO_STATUS_IN_SLO",
        "AVAILABILITY_SLO_STATUS_OUT_OF_SLO",
        "AVAILABILITY_SLO_STATUS_SLO_UNKNOWN",
        "AVAILABILITY_SLO_STATUS_UNSPECIFIED",
    ]
    healthStatus: typing.Literal[
        "HEALTH_STATUS_HEALTHY", "HEALTH_STATUS_UNHEALTHY", "HEALTH_STATUS_UNSPECIFIED"
    ]
    repairCategory: typing.Literal[
        "REPAIR_CATEGORY_CRITICAL_FAILURE",
        "REPAIR_CATEGORY_EMERGENT_MAINTENANCE",
        "REPAIR_CATEGORY_PLANNED_MAINTENANCE",
        "REPAIR_CATEGORY_UNSPECIFIED",
        "REPAIR_CATEGORY_USER_REPORTED_FAULT",
    ]
    unhealthyReason: typing.Literal[
        "UNHEALTHY_REASON_PENDING_USER_APPROVAL",
        "UNHEALTHY_REASON_REPAIRING",
        "UNHEALTHY_REASON_UNSCHEDULABLE",
        "UNHEALTHY_REASON_UNSPECIFIED",
    ]
    updateTime: str

@typing.type_check_only
class GetOwnerInstanceResponse(typing.TypedDict, total=False):
    instance: str

@typing.type_check_only
class GetVersionOperationMetadata(typing.TypedDict, total=False):
    inlineSbomInfo: GetVersionOperationMetadataSbomInfo

@typing.type_check_only
class GetVersionOperationMetadataSbomInfo(typing.TypedDict, total=False):
    currentComponentVersions: dict[str, typing.Any]
    targetComponentVersions: dict[str, typing.Any]

@typing.type_check_only
class GlobalAddressesMoveRequest(typing.TypedDict, total=False):
    description: str
    destinationAddress: str

@typing.type_check_only
class GlobalListVmExtensionsResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[GlobalVmExtension]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class GlobalNetworkEndpointGroupsAttachEndpointsRequest(typing.TypedDict, total=False):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class GlobalNetworkEndpointGroupsDetachEndpointsRequest(typing.TypedDict, total=False):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class GlobalOrganizationSetPolicyRequest(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class GlobalSetLabelsRequest(typing.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class GlobalSetPolicyRequest(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class GlobalVmExtension(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    selfLink: str
    versions: _list[str]

@typing.type_check_only
class GlobalVmExtensionPolicy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    extensionPolicies: dict[str, typing.Any]
    id: str
    instanceSelectors: _list[GlobalVmExtensionPolicyInstanceSelector]
    kind: str
    name: str
    priority: int
    rolloutOperation: GlobalVmExtensionPolicyRolloutOperation
    scopedResourceStatus: typing.Literal[
        "SCOPED_RESOURCE_STATUS_DELETING", "SCOPED_RESOURCE_STATUS_UNSPECIFIED"
    ]
    selfLink: str
    selfLinkWithId: str
    updateTimestamp: str

@typing.type_check_only
class GlobalVmExtensionPolicyExtensionPolicy(typing.TypedDict, total=False):
    installedSoftwareSelector: GlobalVmExtensionPolicyInstalledSoftwareSelector
    pinnedVersion: str
    stringConfig: str

@typing.type_check_only
class GlobalVmExtensionPolicyInstalledSoftwareSelector(typing.TypedDict, total=False):
    anyOfSelectors: dict[str, typing.Any]

@typing.type_check_only
class GlobalVmExtensionPolicyInstalledSoftwareSelectorSelectorSet(
    typing.TypedDict, total=False
):
    allOfSelectors: _list[str]

@typing.type_check_only
class GlobalVmExtensionPolicyInstanceSelector(typing.TypedDict, total=False):
    labelSelector: GlobalVmExtensionPolicyLabelSelector

@typing.type_check_only
class GlobalVmExtensionPolicyLabelSelector(typing.TypedDict, total=False):
    inclusionLabels: dict[str, typing.Any]

@typing.type_check_only
class GlobalVmExtensionPolicyList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[GlobalVmExtensionPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class GlobalVmExtensionPolicyRolloutOperation(typing.TypedDict, total=False):
    rolloutInput: GlobalVmExtensionPolicyRolloutOperationRolloutInput
    rolloutStatus: GlobalVmExtensionPolicyRolloutOperationRolloutStatus

@typing.type_check_only
class GlobalVmExtensionPolicyRolloutOperationRolloutInput(
    typing.TypedDict, total=False
):
    conflictBehavior: str
    name: str
    predefinedRolloutPlan: typing.Literal[
        "FAST_ROLLOUT", "ROLLOUT_PLAN_UNSPECIFIED", "SLOW_ROLLOUT"
    ]
    retryUuid: str

@typing.type_check_only
class GlobalVmExtensionPolicyRolloutOperationRolloutStatus(
    typing.TypedDict, total=False
):
    currentRollouts: _list[
        GlobalVmExtensionPolicyRolloutOperationRolloutStatusRolloutMetadata
    ]
    previousRollout: GlobalVmExtensionPolicyRolloutOperationRolloutStatusRolloutMetadata

@typing.type_check_only
class GlobalVmExtensionPolicyRolloutOperationRolloutStatusRolloutMetadata(
    typing.TypedDict, total=False
):
    locationRolloutStatus: dict[str, typing.Any]
    rollout: str
    rolloutPlan: str
    state: typing.Literal[
        "STATE_CANCELLED",
        "STATE_COMPLETED",
        "STATE_FAILED",
        "STATE_PAUSED",
        "STATE_PROCESSING",
        "STATE_UNKNOWN",
        "STATE_UNSPECIFIED",
    ]

@typing.type_check_only
class GlobalVmExtensionPolicyRolloutOperationRolloutStatusRolloutMetadataLocationRolloutStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal[
        "LOCATION_ROLLOUT_STATE_COMPLETED",
        "LOCATION_ROLLOUT_STATE_FAILED",
        "LOCATION_ROLLOUT_STATE_NOT_STARTED",
        "LOCATION_ROLLOUT_STATE_SKIPPED",
        "LOCATION_ROLLOUT_STATE_UNSPECIFIED",
    ]

@typing.type_check_only
class GroupMaintenanceInfo(typing.TypedDict, total=False):
    instanceMaintenanceOngoingCount: int
    instanceMaintenancePendingCount: int
    maintenanceOngoingCount: int
    maintenancePendingCount: int
    schedulingType: typing.Literal[
        "GROUPED", "GROUP_MAINTENANCE_TYPE_UNSPECIFIED", "INDEPENDENT"
    ]
    subblockInfraMaintenanceOngoingCount: int
    subblockInfraMaintenancePendingCount: int
    upcomingGroupMaintenance: UpcomingMaintenance

@typing.type_check_only
class GrpcServiceConfig(typing.TypedDict, total=False):
    callCredentials: CallCredentials
    channelCredentials: ChannelCredentials
    targetUri: str

@typing.type_check_only
class GuestAttributes(typing.TypedDict, total=False):
    kind: str
    queryPath: str
    queryValue: GuestAttributesValue
    selfLink: str
    variableKey: str
    variableValue: str

@typing.type_check_only
class GuestAttributesEntry(typing.TypedDict, total=False):
    key: str
    namespace: str
    value: str

@typing.type_check_only
class GuestAttributesValue(typing.TypedDict, total=False):
    items: _list[GuestAttributesEntry]

@typing.type_check_only
class GuestOsFeature(typing.TypedDict, total=False):
    type: typing.Literal[
        "BARE_METAL_LINUX_COMPATIBLE",
        "CCA_CAPABLE",
        "FEATURE_TYPE_UNSPECIFIED",
        "GVNIC",
        "IDPF",
        "MULTI_IP_SUBNET",
        "SECURE_BOOT",
        "SEV_CAPABLE",
        "SEV_LIVE_MIGRATABLE",
        "SEV_LIVE_MIGRATABLE_V2",
        "SEV_SNP_CAPABLE",
        "SNP_SVSM_CAPABLE",
        "TDX_CAPABLE",
        "UEFI_COMPATIBLE",
        "VIRTIO_SCSI_MULTIQUEUE",
        "WINDOWS",
    ]

@typing.type_check_only
class HTTP2HealthCheck(typing.TypedDict, total=False):
    host: str
    port: int
    portName: str
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    requestPath: str
    response: str
    weightReportMode: typing.Literal["DISABLE", "DRY_RUN", "ENABLE"]

@typing.type_check_only
class HTTPHealthCheck(typing.TypedDict, total=False):
    host: str
    port: int
    portName: str
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    requestPath: str
    response: str
    weightReportMode: typing.Literal["DISABLE", "DRY_RUN", "ENABLE"]

@typing.type_check_only
class HTTPSHealthCheck(typing.TypedDict, total=False):
    host: str
    port: int
    portName: str
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    requestPath: str
    response: str
    weightReportMode: typing.Literal["DISABLE", "DRY_RUN", "ENABLE"]

@typing.type_check_only
class HaController(typing.TypedDict, total=False):
    backendServices: _list[str]
    creationTimestamp: str
    description: str
    failoverInitiation: typing.Literal[
        "AUTOMATIC", "FAILOVER_INITIATION_UNSPECIFIED", "MANUAL_ONLY"
    ]
    id: str
    instanceName: str
    kind: str
    name: str
    networkingAutoConfiguration: HaControllerNetworkingAutoConfiguration
    region: str
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal[
        "ACTIVE",
        "CREATING",
        "DELETING",
        "FAILOVER_IN_PROGRESS",
        "FAILOVER_UNAVAILABLE",
        "MULTI_ZONE_FAILURE",
        "PENDING_FAILOVER",
        "STARTING",
        "STATE_UNSPECIFIED",
        "STOPPED",
        "STOPPING",
        "UPDATING",
    ]
    status: HaControllerStatus
    zoneConfigurations: dict[str, typing.Any]

@typing.type_check_only
class HaControllerNetworkingAutoConfiguration(typing.TypedDict, total=False):
    internal: HaControllerNetworkingAutoConfigurationInternal

@typing.type_check_only
class HaControllerNetworkingAutoConfigurationInternal(typing.TypedDict, total=False):
    ipAddress: str
    ipv6Address: str
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]

@typing.type_check_only
class HaControllerStatus(typing.TypedDict, total=False):
    failoverProgress: HaControllerStatusFailoverProgress
    lastFailoverInfo: HaControllerStatusFailoverProgress
    ongoingFailover: bool
    primaryInstance: str
    primaryZone: str
    readyForFailover: bool
    zoneStatus: dict[str, typing.Any]

@typing.type_check_only
class HaControllerStatusFailoverProgress(typing.TypedDict, total=False):
    failoverCompleteTimestamp: str
    failoverDuration: str
    failoverTrigger: typing.Literal[
        "AUTOMATIC", "FAILOVER_TRIGGER_UNSPECIFIED", "MANUAL"
    ]
    failoverTriggerTimestamp: str
    lastFailoverAttempt: HaControllerStatusFailoverProgressLastFailoverAttempt

@typing.type_check_only
class HaControllerStatusFailoverProgressLastFailoverAttempt(
    typing.TypedDict, total=False
):
    errors: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class HaControllerStatusZoneStatus(typing.TypedDict, total=False):
    isPrimary: bool
    isZoneReady: bool
    lastError: HaControllerStatusZoneStatusLastError

@typing.type_check_only
class HaControllerStatusZoneStatusLastError(typing.TypedDict, total=False):
    errors: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class HaControllerZoneConfiguration(typing.TypedDict, total=False):
    nodeAffinities: _list[HaControllerZoneConfigurationNodeAffinity]
    reservationAffinity: HaControllerZoneConfigurationReservationAffinity

@typing.type_check_only
class HaControllerZoneConfigurationNodeAffinity(typing.TypedDict, total=False):
    key: str
    operator: typing.Literal["IN", "NOT_IN", "OPERATOR_UNSPECIFIED"]
    values: _list[str]

@typing.type_check_only
class HaControllerZoneConfigurationReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "ANY_RESERVATION",
        "ANY_RESERVATION_THEN_FAIL",
        "NO_RESERVATION",
        "SPECIFIC_RESERVATION",
        "SPECIFIC_THEN_ANY_RESERVATION",
        "SPECIFIC_THEN_NO_RESERVATION",
        "UNSPECIFIED",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class HaControllersAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HaControllersFailoverRequest(typing.TypedDict, total=False):
    failoverToZone: str

@typing.type_check_only
class HaControllersList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[HaController]
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HaControllersScopedList(typing.TypedDict, total=False):
    haControllers: _list[HaController]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthAggregationPoliciesScopedList(typing.TypedDict, total=False):
    healthAggregationPolicies: _list[HealthAggregationPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthAggregationPolicy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    healthyPercentThreshold: int
    id: str
    kind: str
    minHealthyThreshold: int
    name: str
    policyType: typing.Literal["BACKEND_SERVICE_POLICY", "DNS_PUBLIC_IP_POLICY"]
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class HealthAggregationPolicyAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthAggregationPolicyList(typing.TypedDict, total=False):
    id: str
    items: _list[HealthAggregationPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthCheck(typing.TypedDict, total=False):
    checkIntervalSec: int
    creationTimestamp: str
    description: str
    grpcHealthCheck: GRPCHealthCheck
    grpcTlsHealthCheck: GRPCTLSHealthCheck
    healthyThreshold: int
    http2HealthCheck: HTTP2HealthCheck
    httpHealthCheck: HTTPHealthCheck
    httpsHealthCheck: HTTPSHealthCheck
    id: str
    kind: str
    logConfig: HealthCheckLogConfig
    name: str
    region: str
    selfLink: str
    selfLinkWithId: str
    sourceRegions: _list[str]
    sslHealthCheck: SSLHealthCheck
    tcpHealthCheck: TCPHealthCheck
    timeoutSec: int
    type: typing.Literal[
        "GRPC",
        "GRPC_WITH_TLS",
        "HTTP",
        "HTTP2",
        "HTTPS",
        "INVALID",
        "SSL",
        "TCP",
        "UDP",
    ]
    udpHealthCheck: UDPHealthCheck
    unhealthyThreshold: int

@typing.type_check_only
class HealthCheckList(typing.TypedDict, total=False):
    id: str
    items: _list[HealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthCheckLogConfig(typing.TypedDict, total=False):
    enable: bool

@typing.type_check_only
class HealthCheckReference(typing.TypedDict, total=False):
    healthCheck: str

@typing.type_check_only
class HealthCheckService(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    healthChecks: _list[str]
    healthStatusAggregationPolicy: typing.Literal["AND", "NO_AGGREGATION"]
    healthStatusAggregationStrategy: typing.Literal["AND", "NO_AGGREGATION"]
    id: str
    kind: str
    name: str
    networkEndpointGroups: _list[str]
    notificationEndpoints: _list[str]
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class HealthCheckServiceAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthCheckServiceReference(typing.TypedDict, total=False):
    healthCheckService: str

@typing.type_check_only
class HealthCheckServicesList(typing.TypedDict, total=False):
    id: str
    items: _list[HealthCheckService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthCheckServicesScopedList(typing.TypedDict, total=False):
    resources: _list[HealthCheckService]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthChecksAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthChecksScopedList(typing.TypedDict, total=False):
    healthChecks: _list[HealthCheck]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthSource(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    healthAggregationPolicy: str
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    selfLinkWithId: str
    sourceType: typing.Literal["BACKEND_SERVICE"]
    sources: _list[str]

@typing.type_check_only
class HealthSourceAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthSourceHealth(typing.TypedDict, total=False):
    healthState: typing.Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
    kind: str
    sources: _list[HealthSourcesGetHealthResponseSourceInfo]

@typing.type_check_only
class HealthSourceList(typing.TypedDict, total=False):
    id: str
    items: _list[HealthSource]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthSourcesGetHealthResponseSourceInfo(typing.TypedDict, total=False):
    backends: _list[HealthSourcesGetHealthResponseSourceInfoBackendInfo]
    forwardingRule: str
    source: str

@typing.type_check_only
class HealthSourcesGetHealthResponseSourceInfoBackendInfo(
    typing.TypedDict, total=False
):
    endpointCount: int
    group: str
    healthyEndpointCount: int

@typing.type_check_only
class HealthSourcesScopedList(typing.TypedDict, total=False):
    healthSources: _list[HealthSource]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthStatus(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    forwardingRule: str
    forwardingRuleIp: str
    healthState: typing.Literal["HEALTHY", "UNHEALTHY"]
    instance: str
    ipAddress: str
    ipv6Address: str
    ipv6HealthState: typing.Literal["HEALTHY", "UNHEALTHY"]
    port: int
    weight: str
    weightError: typing.Literal[
        "INVALID_WEIGHT", "MISSING_WEIGHT", "UNAVAILABLE_WEIGHT", "WEIGHT_NONE"
    ]

@typing.type_check_only
class HealthStatusForNetworkEndpoint(typing.TypedDict, total=False):
    backendService: BackendServiceReference
    forwardingRule: ForwardingRuleReference
    healthCheck: HealthCheckReference
    healthCheckService: HealthCheckServiceReference
    healthState: typing.Literal["DRAINING", "HEALTHY", "UNHEALTHY", "UNKNOWN"]
    ipv6HealthState: typing.Literal["DRAINING", "HEALTHY", "UNHEALTHY", "UNKNOWN"]

@typing.type_check_only
class Help(typing.TypedDict, total=False):
    links: _list[HelpLink]

@typing.type_check_only
class HelpLink(typing.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class Host(typing.TypedDict, total=False):
    aliasLinks: _list[str]
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal[
        "ACTIVE", "CREATING", "DELETING", "STATE_UNSPECIFIED", "UNAVAILABLE"
    ]
    status: HostStatus
    zone: str

@typing.type_check_only
class HostPhysicalTopology(typing.TypedDict, total=False):
    block: str
    cluster: str
    host: str
    subBlock: str

@typing.type_check_only
class HostRule(typing.TypedDict, total=False):
    description: str
    hosts: _list[str]
    pathMatcher: str

@typing.type_check_only
class HostStatus(typing.TypedDict, total=False):
    physicalTopology: HostPhysicalTopology
    runningInstances: _list[str]

@typing.type_check_only
class HostsGetVersionRequest(typing.TypedDict, total=False):
    sbomSelections: _list[
        typing.Literal[
            "SBOM_SELECTION_CURRENT",
            "SBOM_SELECTION_TARGET",
            "SBOM_SELECTION_UNSPECIFIED",
        ]
    ]

@typing.type_check_only
class HostsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[Host]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HttpFaultAbort(typing.TypedDict, total=False):
    httpStatus: int
    percentage: float

@typing.type_check_only
class HttpFaultDelay(typing.TypedDict, total=False):
    fixedDelay: Duration
    percentage: float

@typing.type_check_only
class HttpFaultInjection(typing.TypedDict, total=False):
    abort: HttpFaultAbort
    delay: HttpFaultDelay

@typing.type_check_only
class HttpFilterConfig(typing.TypedDict, total=False):
    config: str
    configTypeUrl: str
    filterName: str

@typing.type_check_only
class HttpHeaderAction(typing.TypedDict, total=False):
    requestHeadersToAdd: _list[HttpHeaderOption]
    requestHeadersToRemove: _list[str]
    responseHeadersToAdd: _list[HttpHeaderOption]
    responseHeadersToRemove: _list[str]

@typing.type_check_only
class HttpHeaderMatch(typing.TypedDict, total=False):
    exactMatch: str
    headerName: str
    invertMatch: bool
    prefixMatch: str
    presentMatch: bool
    rangeMatch: Int64RangeMatch
    regexMatch: str
    suffixMatch: str

@typing.type_check_only
class HttpHeaderOption(typing.TypedDict, total=False):
    headerName: str
    headerValue: str
    replace: bool

@typing.type_check_only
class HttpHealthCheck(typing.TypedDict, total=False):
    checkIntervalSec: int
    creationTimestamp: str
    description: str
    healthyThreshold: int
    host: str
    id: str
    kind: str
    name: str
    port: int
    requestPath: str
    selfLink: str
    selfLinkWithId: str
    timeoutSec: int
    unhealthyThreshold: int

@typing.type_check_only
class HttpHealthCheckList(typing.TypedDict, total=False):
    id: str
    items: _list[HttpHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HttpQueryParameterMatch(typing.TypedDict, total=False):
    exactMatch: str
    name: str
    presentMatch: bool
    regexMatch: str

@typing.type_check_only
class HttpRedirectAction(typing.TypedDict, total=False):
    hostRedirect: str
    httpsRedirect: bool
    pathRedirect: str
    prefixRedirect: str
    redirectResponseCode: typing.Literal[
        "FOUND",
        "MOVED_PERMANENTLY_DEFAULT",
        "PERMANENT_REDIRECT",
        "SEE_OTHER",
        "TEMPORARY_REDIRECT",
    ]
    stripQuery: bool

@typing.type_check_only
class HttpRetryPolicy(typing.TypedDict, total=False):
    numRetries: int
    perTryTimeout: Duration
    retryConditions: _list[str]

@typing.type_check_only
class HttpRouteAction(typing.TypedDict, total=False):
    cachePolicy: CachePolicy
    corsPolicy: CorsPolicy
    faultInjectionPolicy: HttpFaultInjection
    imageOptimizationPolicy: ImageOptimizationPolicy
    maxStreamDuration: Duration
    requestMirrorPolicy: RequestMirrorPolicy
    retryPolicy: HttpRetryPolicy
    timeout: Duration
    urlRewrite: UrlRewrite
    weightedBackendServices: _list[WeightedBackendService]

@typing.type_check_only
class HttpRouteRule(typing.TypedDict, total=False):
    customErrorResponsePolicy: CustomErrorResponsePolicy
    description: str
    headerAction: HttpHeaderAction
    httpFilterConfigs: _list[HttpFilterConfig]
    httpFilterMetadata: _list[HttpFilterConfig]
    matchRules: _list[HttpRouteRuleMatch]
    priority: int
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

@typing.type_check_only
class HttpRouteRuleMatch(typing.TypedDict, total=False):
    fullPathMatch: str
    headerMatches: _list[HttpHeaderMatch]
    ignoreCase: bool
    metadataFilters: _list[MetadataFilter]
    pathTemplateMatch: str
    prefixMatch: str
    queryParameterMatches: _list[HttpQueryParameterMatch]
    regexMatch: str

@typing.type_check_only
class HttpsHealthCheck(typing.TypedDict, total=False):
    checkIntervalSec: int
    creationTimestamp: str
    description: str
    healthyThreshold: int
    host: str
    id: str
    kind: str
    name: str
    port: int
    requestPath: str
    selfLink: str
    selfLinkWithId: str
    timeoutSec: int
    unhealthyThreshold: int

@typing.type_check_only
class HttpsHealthCheckList(typing.TypedDict, total=False):
    id: str
    items: _list[HttpsHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    archiveSizeBytes: str
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    diskSizeGb: str
    enableConfidentialCompute: bool
    family: str
    guestOsFeatures: _list[GuestOsFeature]
    id: str
    imageEncryptionKey: CustomerEncryptionKey
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    licenseCodes: _list[str]
    licenses: _list[str]
    locked: bool
    name: str
    params: ImageParams
    rawDisk: dict[str, typing.Any]
    rolloutOverride: RolloutPolicy
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    shieldedInstanceInitialState: InitialStateConfig
    sourceDisk: str
    sourceDiskEncryptionKey: CustomerEncryptionKey
    sourceDiskId: str
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceImageId: str
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey
    sourceSnapshotId: str
    sourceType: typing.Literal["RAW"]
    status: typing.Literal["DELETING", "FAILED", "PENDING", "READY"]
    storageLocations: _list[str]

@typing.type_check_only
class ImageFamilyView(typing.TypedDict, total=False):
    image: Image

@typing.type_check_only
class ImageList(typing.TypedDict, total=False):
    id: str
    items: _list[Image]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ImageOptimizationPolicy(typing.TypedDict, total=False):
    queryParameterInterpretation: typing.Literal[
        "DISABLED", "ENABLED", "QUERY_PARAMETER_INTERPRETATION_UNSPECIFIED"
    ]

@typing.type_check_only
class ImageParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class ImageView(typing.TypedDict, total=False):
    image: Image

@typing.type_check_only
class ImageViewsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[ImageView]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InitialStateConfig(typing.TypedDict, total=False):
    dbs: _list[FileContentBuffer]
    dbxs: _list[FileContentBuffer]
    keks: _list[FileContentBuffer]
    pk: FileContentBuffer

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    advancedMachineFeatures: AdvancedMachineFeatures
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    cpuPlatform: str
    creationTimestamp: str
    deletionProtection: bool
    description: str
    disks: _list[AttachedDisk]
    displayDevice: DisplayDevice
    eraseWindowsVssSignature: bool
    fingerprint: str
    guestAccelerators: _list[AcceleratorConfig]
    hostname: str
    id: str
    identity: str
    identityCertificate: bool
    instanceEncryptionKey: CustomerEncryptionKey
    keyRevocationActionType: typing.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    lastStartTimestamp: str
    lastStopTimestamp: str
    lastSuspendedTimestamp: str
    localSsdEncryptionMode: typing.Literal[
        "EPHEMERAL_KEY_ENCRYPTION",
        "LOCAL_SSD_ENCRYPTION_MODE_UNSPECIFIED",
        "STANDARD_ENCRYPTION",
    ]
    machineType: str
    managementInterfaces: dict[str, typing.Any]
    metadata: Metadata
    minCpuPlatform: str
    name: str
    networkInterfaces: _list[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    params: InstanceParams
    partnerMetadata: dict[str, typing.Any]
    postKeyRevocationActionType: typing.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    preservedStateSizeGb: str
    privateIpv6GoogleAccess: typing.Literal[
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "INHERIT_FROM_SUBNETWORK",
    ]
    reservationAffinity: ReservationAffinity
    resourcePolicies: _list[str]
    resourceStatus: ResourceStatus
    satisfiesPzi: bool
    satisfiesPzs: bool
    scheduling: Scheduling
    secureTags: _list[str]
    selfLink: str
    selfLinkWithId: str
    serviceAccounts: _list[ServiceAccount]
    serviceIntegrationSpecs: dict[str, typing.Any]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedInstanceIntegrityPolicy: ShieldedInstanceIntegrityPolicy
    shieldedVmConfig: ShieldedVmConfig
    shieldedVmIntegrityPolicy: ShieldedVmIntegrityPolicy
    sourceMachineImage: str
    sourceMachineImageEncryptionKey: CustomerEncryptionKey
    startRestricted: bool
    status: typing.Literal[
        "DEPROVISIONING",
        "PENDING",
        "PENDING_STOP",
        "PROVISIONING",
        "REPAIRING",
        "RUNNING",
        "STAGING",
        "STOPPED",
        "STOPPING",
        "SUSPENDED",
        "SUSPENDING",
        "TERMINATED",
    ]
    statusMessage: str
    tags: Tags
    upcomingMaintenance: UpcomingMaintenance
    workloadIdentityConfig: WorkloadIdentityConfig
    zone: str

@typing.type_check_only
class InstanceAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceConsumptionData(typing.TypedDict, total=False):
    consumptionInfo: InstanceConsumptionInfo
    instance: str

@typing.type_check_only
class InstanceConsumptionInfo(typing.TypedDict, total=False):
    guestCpus: int
    localSsdGb: int
    memoryMb: int
    minNodeCpus: int

@typing.type_check_only
class InstanceFlexibilityPolicy(typing.TypedDict, total=False):
    instanceSelections: dict[str, typing.Any]

@typing.type_check_only
class InstanceFlexibilityPolicyInstanceSelection(typing.TypedDict, total=False):
    disks: _list[AttachedDisk]
    machineTypes: _list[str]
    minCpuPlatform: str
    rank: str

@typing.type_check_only
class InstanceGroup(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    namedPorts: _list[NamedPort]
    network: str
    region: str
    selfLink: str
    selfLinkWithId: str
    size: int
    subnetwork: str
    zone: str

@typing.type_check_only
class InstanceGroupAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupList(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManager(typing.TypedDict, total=False):
    allInstancesConfig: InstanceGroupManagerAllInstancesConfig
    autoHealingPolicies: _list[InstanceGroupManagerAutoHealingPolicy]
    baseInstanceName: str
    creationTimestamp: str
    currentActions: InstanceGroupManagerActionsSummary
    description: str
    distributionPolicy: DistributionPolicy
    failoverAction: typing.Literal["NO_FAILOVER", "UNKNOWN"]
    fingerprint: str
    id: str
    instanceFlexibilityPolicy: InstanceGroupManagerInstanceFlexibilityPolicy
    instanceGroup: str
    instanceLifecyclePolicy: InstanceGroupManagerInstanceLifecyclePolicy
    instanceTemplate: str
    kind: str
    listManagedInstancesResults: typing.Literal["PAGELESS", "PAGINATED"]
    multiMig: str
    name: str
    namedPorts: _list[NamedPort]
    params: InstanceGroupManagerParams
    region: str
    resourcePolicies: InstanceGroupManagerResourcePolicies
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    serviceAccount: str
    standbyPolicy: InstanceGroupManagerStandbyPolicy
    statefulPolicy: StatefulPolicy
    status: InstanceGroupManagerStatus
    targetPools: _list[str]
    targetSize: int
    targetSizePolicy: InstanceGroupManagerTargetSizePolicy
    targetSizeUnit: typing.Literal["INSTANCE", "VCPU"]
    targetStoppedSize: int
    targetSuspendedSize: int
    updatePolicy: InstanceGroupManagerUpdatePolicy
    versions: _list[InstanceGroupManagerVersion]
    zone: str

@typing.type_check_only
class InstanceGroupManagerActionsSummary(typing.TypedDict, total=False):
    abandoning: int
    adopting: int
    creating: int
    creatingAtomically: int
    creatingWithoutRetries: int
    deleting: int
    none: int
    queuing: int
    recreating: int
    refreshing: int
    restarting: int
    restartingInPlace: int
    resuming: int
    starting: int
    stopping: int
    suspending: int
    verifying: int

@typing.type_check_only
class InstanceGroupManagerAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerAllInstancesConfig(typing.TypedDict, total=False):
    properties: InstancePropertiesPatch

@typing.type_check_only
class InstanceGroupManagerAutoHealingPolicy(typing.TypedDict, total=False):
    autoHealingTriggers: InstanceGroupManagerAutoHealingPolicyAutoHealingTriggers
    healthCheck: str
    initialDelaySec: int
    maxUnavailable: FixedOrPercent

@typing.type_check_only
class InstanceGroupManagerAutoHealingPolicyAutoHealingTriggers(
    typing.TypedDict, total=False
):
    onHealthCheck: typing.Literal["OFF", "ON"]

@typing.type_check_only
class InstanceGroupManagerInstanceFlexibilityPolicy(typing.TypedDict, total=False):
    instanceSelectionLists: dict[str, typing.Any]
    instanceSelections: dict[str, typing.Any]
    provisioningModelMix: (
        InstanceGroupManagerInstanceFlexibilityPolicyProvisioningModelMix
    )

@typing.type_check_only
class InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelection(
    typing.TypedDict, total=False
):
    disks: _list[AttachedDisk]
    machineTypes: _list[str]
    minCpuPlatform: str
    rank: int

@typing.type_check_only
class InstanceGroupManagerInstanceFlexibilityPolicyProvisioningModelMix(
    typing.TypedDict, total=False
):
    standardCapacityBase: int
    standardCapacityPercentAboveBase: int

@typing.type_check_only
class InstanceGroupManagerInstanceLifecyclePolicy(typing.TypedDict, total=False):
    defaultActionOnFailure: typing.Literal["DELETE", "DO_NOTHING", "REPAIR"]
    forceUpdateOnRepair: typing.Literal["NO", "YES"]
    metadataBasedReadinessSignal: (
        InstanceGroupManagerInstanceLifecyclePolicyMetadataBasedReadinessSignal
    )
    onFailedHealthCheck: typing.Literal["DEFAULT_ACTION", "DO_NOTHING", "REPAIR"]
    onRepair: InstanceGroupManagerInstanceLifecyclePolicyOnRepair

@typing.type_check_only
class InstanceGroupManagerInstanceLifecyclePolicyMetadataBasedReadinessSignal(
    typing.TypedDict, total=False
):
    timeoutSec: int

@typing.type_check_only
class InstanceGroupManagerInstanceLifecyclePolicyOnRepair(
    typing.TypedDict, total=False
):
    allowChangingZone: typing.Literal["NO", "YES"]

@typing.type_check_only
class InstanceGroupManagerList(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerResizeRequest(typing.TypedDict, total=False):
    count: int
    creationTimestamp: str
    description: str
    id: str
    instances: _list[PerInstanceConfig]
    kind: str
    name: str
    queuingPolicy: QueuingPolicy
    region: str
    requestedRunDuration: Duration
    resizeBy: int
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal[
        "ACCEPTED",
        "CANCELLED",
        "CREATING",
        "DELETING",
        "FAILED",
        "PROVISIONING",
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
    ]
    status: InstanceGroupManagerResizeRequestStatus
    zone: str

@typing.type_check_only
class InstanceGroupManagerResizeRequestStatus(typing.TypedDict, total=False):
    error: dict[str, typing.Any]
    lastAttempt: InstanceGroupManagerResizeRequestStatusLastAttempt
    queuingPolicy: QueuingPolicy

@typing.type_check_only
class InstanceGroupManagerResizeRequestStatusLastAttempt(typing.TypedDict, total=False):
    error: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerResizeRequestsListResponse(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceGroupManagerResizeRequest]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerResourcePolicies(typing.TypedDict, total=False):
    workloadPolicy: str

@typing.type_check_only
class InstanceGroupManagerStandbyPolicy(typing.TypedDict, total=False):
    initialDelaySec: int
    mode: typing.Literal["MANUAL", "SCALE_OUT_POOL"]

@typing.type_check_only
class InstanceGroupManagerStatus(typing.TypedDict, total=False):
    allInstancesConfig: InstanceGroupManagerStatusAllInstancesConfig
    appliedAcceleratorTopologies: _list[InstanceGroupManagerStatusAcceleratorTopology]
    autoscaler: str
    bulkInstanceOperation: InstanceGroupManagerStatusBulkInstanceOperation
    currentInstanceStatuses: InstanceGroupManagerStatusInstanceStatusSummary
    isStable: bool
    stateful: InstanceGroupManagerStatusStateful
    versionTarget: InstanceGroupManagerStatusVersionTarget

@typing.type_check_only
class InstanceGroupManagerStatusAcceleratorTopology(typing.TypedDict, total=False):
    acceleratorTopology: str
    state: typing.Literal[
        "ACTIVATING",
        "ACTIVE",
        "ACTIVE_DEGRADED",
        "DEACTIVATING",
        "FAILED",
        "INCOMPLETE",
        "REACTIVATING",
    ]
    stateDetails: (
        InstanceGroupManagerStatusAcceleratorTopologyAcceleratorTopologyStateDetails
    )

@typing.type_check_only
class InstanceGroupManagerStatusAcceleratorTopologyAcceleratorTopologyStateDetails(
    typing.TypedDict, total=False
):
    error: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class InstanceGroupManagerStatusAllInstancesConfig(typing.TypedDict, total=False):
    currentRevision: str
    effective: bool

@typing.type_check_only
class InstanceGroupManagerStatusBulkInstanceOperation(typing.TypedDict, total=False):
    inProgress: bool
    lastProgressCheck: InstanceGroupManagerStatusBulkInstanceOperationLastProgressCheck

@typing.type_check_only
class InstanceGroupManagerStatusBulkInstanceOperationLastProgressCheck(
    typing.TypedDict, total=False
):
    error: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class InstanceGroupManagerStatusInstanceStatusSummary(typing.TypedDict, total=False):
    deprovisioning: int
    nonExistent: int
    pending: int
    pendingStop: int
    provisioning: int
    repairing: int
    running: int
    staging: int
    stopped: int
    stopping: int
    suspended: int
    suspending: int
    terminated: int

@typing.type_check_only
class InstanceGroupManagerStatusStateful(typing.TypedDict, total=False):
    hasStatefulConfig: bool
    isStateful: bool
    perInstanceConfigs: InstanceGroupManagerStatusStatefulPerInstanceConfigs

@typing.type_check_only
class InstanceGroupManagerStatusStatefulPerInstanceConfigs(
    typing.TypedDict, total=False
):
    allEffective: bool

@typing.type_check_only
class InstanceGroupManagerStatusVersionTarget(typing.TypedDict, total=False):
    isReached: bool

@typing.type_check_only
class InstanceGroupManagerTargetSizePolicy(typing.TypedDict, total=False):
    mode: typing.Literal["BULK", "INDIVIDUAL", "UNSPECIFIED_MODE"]

@typing.type_check_only
class InstanceGroupManagerUpdatePolicy(typing.TypedDict, total=False):
    allowedActions: _list[
        typing.Literal["NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"]
    ]
    disruptionMode: typing.Literal["LEGACY", "OPTIMIZED"]
    instanceRedistributionType: typing.Literal["NONE", "PROACTIVE"]
    maxSurge: FixedOrPercent
    maxUnavailable: FixedOrPercent
    minReadySec: int
    minimalAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]
    mostDisruptiveAllowedAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]
    replacementMethod: typing.Literal["RECREATE", "SUBSTITUTE"]
    type: typing.Literal["OPPORTUNISTIC", "PROACTIVE"]

@typing.type_check_only
class InstanceGroupManagerVersion(typing.TypedDict, total=False):
    instanceTemplate: str
    name: str
    tag: str
    targetSize: FixedOrPercent

@typing.type_check_only
class InstanceGroupManagersAbandonInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersApplyUpdatesRequest(typing.TypedDict, total=False):
    allInstances: bool
    allowedActions: _list[
        typing.Literal["NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"]
    ]
    disruptionMode: typing.Literal["LEGACY", "OPTIMIZED"]
    instances: _list[str]
    maximalAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]
    minimalAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]
    mostDisruptiveAllowedAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]

@typing.type_check_only
class InstanceGroupManagersConfigureAcceleratorTopologiesRequest(
    typing.TypedDict, total=False
):
    acceleratorTopologyActions: dict[str, typing.Any]
    acceleratorTopologyConfigurations: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersConfigureAcceleratorTopologiesRequestAcceleratorTopologyConfiguration(
    typing.TypedDict, total=False
):
    action: typing.Literal[
        "ACCELERATOR_TOPOLOGY_ACTION_UNSPECIFIED", "ACTIVATE", "DEACTIVATE"
    ]
    externalId: str

@typing.type_check_only
class InstanceGroupManagersCreateInstancesRequest(typing.TypedDict, total=False):
    instances: _list[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupManagersDeleteInstancesRequest(typing.TypedDict, total=False):
    instanceNames: _list[str]
    instances: _list[str]
    skipInstancesOnValidationError: bool

@typing.type_check_only
class InstanceGroupManagersDeletePerInstanceConfigsReq(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class InstanceGroupManagersGetAvailableAcceleratorTopologiesResponse(
    typing.TypedDict, total=False
):
    acceleratorTopologiesInfo: dict[str, typing.Any]
    multiMig: str

@typing.type_check_only
class InstanceGroupManagersGetAvailableAcceleratorTopologiesResponseAcceleratorTopologyInfo(
    typing.TypedDict, total=False
):
    acceleratorTopology: str
    acceleratorTopologyHealth: typing.Literal["DEGRADED", "HEALTHY", "UNHEALTHY"]
    acceleratorTopologyState: InstanceGroupManagersGetAvailableAcceleratorTopologiesResponseAcceleratorTopologyState
    instancesHealth: typing.Literal["ALL_HEALTHY", "UNHEALTHY_OR_MISSING"]
    parent: str

@typing.type_check_only
class InstanceGroupManagersGetAvailableAcceleratorTopologiesResponseAcceleratorTopologyState(
    typing.TypedDict, total=False
):
    currentState: typing.Literal[
        "ACTIVATING",
        "ACTIVE",
        "ACTIVE_DEGRADED",
        "DEACTIVATING",
        "FAILED",
        "INACTIVE",
        "INCOMPLETE",
    ]
    error: dict[str, typing.Any]
    errorTimestamp: str
    externalId: str

@typing.type_check_only
class InstanceGroupManagersListErrorsResponse(typing.TypedDict, total=False):
    items: _list[InstanceManagedByIgmError]
    nextPageToken: str

@typing.type_check_only
class InstanceGroupManagersListManagedInstancesResponse(typing.TypedDict, total=False):
    managedInstances: _list[ManagedInstance]
    nextPageToken: str

@typing.type_check_only
class InstanceGroupManagersListPerInstanceConfigsResp(typing.TypedDict, total=False):
    items: _list[PerInstanceConfig]
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersPatchPerInstanceConfigsReq(typing.TypedDict, total=False):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupManagersRecreateInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersResizeAdvancedRequest(typing.TypedDict, total=False):
    noCreationRetries: bool
    scaleInProtection: bool
    targetSize: int

@typing.type_check_only
class InstanceGroupManagersResumeInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersScopedList(typing.TypedDict, total=False):
    instanceGroupManagers: _list[InstanceGroupManager]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersSetAutoHealingRequest(typing.TypedDict, total=False):
    autoHealingPolicies: _list[InstanceGroupManagerAutoHealingPolicy]

@typing.type_check_only
class InstanceGroupManagersSetInstanceTemplateRequest(typing.TypedDict, total=False):
    instanceTemplate: str

@typing.type_check_only
class InstanceGroupManagersSetTargetPoolsRequest(typing.TypedDict, total=False):
    fingerprint: str
    targetPools: _list[str]

@typing.type_check_only
class InstanceGroupManagersStartInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersStopInstancesRequest(typing.TypedDict, total=False):
    forceStop: bool
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersSuspendInstancesRequest(typing.TypedDict, total=False):
    forceSuspend: bool
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersUpdatePerInstanceConfigsReq(typing.TypedDict, total=False):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupsAddInstancesRequest(typing.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class InstanceGroupsListInstances(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupsListInstancesRequest(typing.TypedDict, total=False):
    instanceState: typing.Literal["ALL", "RUNNING"]

@typing.type_check_only
class InstanceGroupsRemoveInstancesRequest(typing.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class InstanceGroupsScopedList(typing.TypedDict, total=False):
    instanceGroups: _list[InstanceGroup]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupsSetNamedPortsRequest(typing.TypedDict, total=False):
    fingerprint: str
    namedPorts: _list[NamedPort]

@typing.type_check_only
class InstanceList(typing.TypedDict, total=False):
    id: str
    items: _list[Instance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceListReferrers(typing.TypedDict, total=False):
    id: str
    items: _list[Reference]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceManagedByIgmError(typing.TypedDict, total=False):
    error: InstanceManagedByIgmErrorManagedInstanceError
    instanceActionDetails: InstanceManagedByIgmErrorInstanceActionDetails
    timestamp: str

@typing.type_check_only
class InstanceManagedByIgmErrorInstanceActionDetails(typing.TypedDict, total=False):
    action: typing.Literal[
        "ABANDONING",
        "ADOPTING",
        "CREATING",
        "CREATING_ATOMICALLY",
        "CREATING_WITHOUT_RETRIES",
        "DELETING",
        "NONE",
        "QUEUING",
        "RECREATING",
        "REFRESHING",
        "RESTARTING",
        "RESTARTING_IN_PLACE",
        "RESUMING",
        "STARTING",
        "STOPPING",
        "SUSPENDING",
        "VERIFYING",
    ]
    instance: str
    version: ManagedInstanceVersion

@typing.type_check_only
class InstanceManagedByIgmErrorManagedInstanceError(typing.TypedDict, total=False):
    code: str
    message: str

@typing.type_check_only
class InstanceManagementInterface(typing.TypedDict, total=False):
    authenticationConfig: InstanceManagementInterfaceAuthenticationConfig
    ipv4Address: str
    ipv6Address: str
    network: str
    state: typing.Literal["ACTIVE", "INACTIVE", "PENDING", "STATE_UNSPECIFIED"]
    subnetwork: str
    type: typing.Literal["HOST_MANAGEMENT", "TYPE_UNSPECIFIED"]

@typing.type_check_only
class InstanceManagementInterfaceAuthenticationConfig(typing.TypedDict, total=False):
    trustConfig: str

@typing.type_check_only
class InstanceMoveRequest(typing.TypedDict, total=False):
    destinationZone: str
    targetInstance: str

@typing.type_check_only
class InstanceParams(typing.TypedDict, total=False):
    requestValidForDuration: Duration
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InstanceProperties(typing.TypedDict, total=False):
    advancedMachineFeatures: AdvancedMachineFeatures
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    description: str
    disks: _list[AttachedDisk]
    displayDevice: DisplayDevice
    guestAccelerators: _list[AcceleratorConfig]
    identity: str
    identityCertificate: bool
    keyRevocationActionType: typing.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    labels: dict[str, typing.Any]
    localSsdEncryptionMode: typing.Literal[
        "EPHEMERAL_KEY_ENCRYPTION",
        "LOCAL_SSD_ENCRYPTION_MODE_UNSPECIFIED",
        "STANDARD_ENCRYPTION",
    ]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: _list[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    partnerMetadata: dict[str, typing.Any]
    postKeyRevocationActionType: typing.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    privateIpv6GoogleAccess: typing.Literal[
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "INHERIT_FROM_SUBNETWORK",
    ]
    reservationAffinity: ReservationAffinity
    resourceManagerTags: dict[str, typing.Any]
    resourcePolicies: _list[str]
    scheduling: Scheduling
    secureTags: _list[str]
    serviceAccounts: _list[ServiceAccount]
    serviceIntegrationSpecs: dict[str, typing.Any]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedVmConfig: ShieldedVmConfig
    tags: Tags
    workloadIdentityConfig: WorkloadIdentityConfig

@typing.type_check_only
class InstancePropertiesPatch(typing.TypedDict, total=False):
    exposeHostTopology: bool
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]

@typing.type_check_only
class InstanceReference(typing.TypedDict, total=False):
    instance: str

@typing.type_check_only
class InstanceSettings(typing.TypedDict, total=False):
    email: str
    fingerprint: str
    kind: str
    metadata: InstanceSettingsMetadata
    zone: str

@typing.type_check_only
class InstanceSettingsMetadata(typing.TypedDict, total=False):
    items: dict[str, typing.Any]
    kind: str

@typing.type_check_only
class InstanceTemplate(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    properties: InstanceProperties
    region: str
    selfLink: str
    selfLinkWithId: str
    sourceInstance: str
    sourceInstanceParams: SourceInstanceParams

@typing.type_check_only
class InstanceTemplateAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceTemplateList(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceTemplatesScopedList(typing.TypedDict, total=False):
    instanceTemplates: _list[InstanceTemplate]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceWithNamedPorts(typing.TypedDict, total=False):
    instance: str
    namedPorts: _list[NamedPort]
    status: typing.Literal[
        "DEPROVISIONING",
        "PENDING",
        "PENDING_STOP",
        "PROVISIONING",
        "REPAIRING",
        "RUNNING",
        "STAGING",
        "STOPPED",
        "STOPPING",
        "SUSPENDED",
        "SUSPENDING",
        "TERMINATED",
    ]

@typing.type_check_only
class InstancesAddResourcePoliciesRequest(typing.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class InstancesBulkInsertOperationMetadata(typing.TypedDict, total=False):
    perLocationStatus: dict[str, typing.Any]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponse(typing.TypedDict, total=False):
    firewallPolicys: _list[
        InstancesGetEffectiveFirewallsResponseEffectiveFirewallPolicy
    ]
    firewalls: _list[Firewall]
    organizationFirewalls: _list[
        InstancesGetEffectiveFirewallsResponseOrganizationFirewallPolicy
    ]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    priority: int
    rules: _list[FirewallPolicyRule]
    shortName: str
    type: typing.Literal[
        "HIERARCHY",
        "NETWORK",
        "NETWORK_REGIONAL",
        "SYSTEM_GLOBAL",
        "SYSTEM_REGIONAL",
        "UNSPECIFIED",
    ]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseOrganizationFirewallPolicy(
    typing.TypedDict, total=False
):
    id: str
    rules: _list[SecurityPolicyRule]

@typing.type_check_only
class InstancesRemoveResourcePoliciesRequest(typing.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class InstancesReportHostAsFaultyRequest(typing.TypedDict, total=False):
    actionHint: typing.Literal[
        "ACTION_HINT_UNSPECIFIED",
        "DIAGNOSE_AND_REPAIR",
        "EXECUTE_ALL_RECOMMENDED_SCANS",
    ]
    disruptionSchedule: typing.Literal[
        "DISRUPTION_SCHEDULE_UNSPECIFIED", "FUTURE", "IMMEDIATE"
    ]
    faultReasons: _list[InstancesReportHostAsFaultyRequestFaultReason]

@typing.type_check_only
class InstancesReportHostAsFaultyRequestFaultReason(typing.TypedDict, total=False):
    behavior: typing.Literal[
        "BEHAVIOR_UNSPECIFIED",
        "CHIP_ERROR",
        "PERFORMANCE",
        "SILENT_DATA_CORRUPTION",
        "UNRECOVERABLE_GPU_ERROR",
    ]
    description: str

@typing.type_check_only
class InstancesResumeRequest(typing.TypedDict, total=False):
    disks: _list[CustomerEncryptionKeyProtectedDisk]
    instanceEncryptionKey: CustomerEncryptionKey

@typing.type_check_only
class InstancesScopedList(typing.TypedDict, total=False):
    instances: _list[Instance]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstancesSetLabelsRequest(typing.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class InstancesSetMachineResourcesRequest(typing.TypedDict, total=False):
    guestAccelerators: _list[AcceleratorConfig]

@typing.type_check_only
class InstancesSetMachineTypeRequest(typing.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class InstancesSetMinCpuPlatformRequest(typing.TypedDict, total=False):
    minCpuPlatform: str

@typing.type_check_only
class InstancesSetNameRequest(typing.TypedDict, total=False):
    currentName: str
    name: str

@typing.type_check_only
class InstancesSetSecurityPolicyRequest(typing.TypedDict, total=False):
    networkInterfaces: _list[str]
    securityPolicy: str

@typing.type_check_only
class InstancesSetServiceAccountRequest(typing.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class InstancesStartWithEncryptionKeyRequest(typing.TypedDict, total=False):
    disks: _list[CustomerEncryptionKeyProtectedDisk]
    instanceEncryptionKey: CustomerEncryptionKey

@typing.type_check_only
class InstantSnapshot(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    creationTimestamp: str
    description: str
    diskSizeGb: str
    guestFlush: bool
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    params: InstantSnapshotParams
    region: str
    resourceStatus: InstantSnapshotResourceStatus
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    sourceDisk: str
    sourceDiskId: str
    sourceInstantSnapshotGroup: str
    sourceInstantSnapshotGroupId: str
    status: typing.Literal["CREATING", "DELETING", "FAILED", "READY", "UNAVAILABLE"]
    zone: str

@typing.type_check_only
class InstantSnapshotAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstantSnapshotGroup(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    region: str
    resourceStatus: InstantSnapshotGroupResourceStatus
    selfLink: str
    selfLinkWithId: str
    sourceConsistencyGroup: str
    status: typing.Literal[
        "CREATING", "DELETING", "FAILED", "INVALID", "READY", "UNKNOWN"
    ]
    zone: str

@typing.type_check_only
class InstantSnapshotGroupParameters(typing.TypedDict, total=False):
    sourceInstantSnapshotGroup: str

@typing.type_check_only
class InstantSnapshotGroupResourceStatus(typing.TypedDict, total=False):
    consistencyMembershipResolutionTime: str
    sourceInfo: InstantSnapshotGroupSourceInfo

@typing.type_check_only
class InstantSnapshotGroupSourceInfo(typing.TypedDict, total=False):
    consistencyGroup: str
    consistencyGroupId: str

@typing.type_check_only
class InstantSnapshotList(typing.TypedDict, total=False):
    id: str
    items: _list[InstantSnapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstantSnapshotParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InstantSnapshotResourceStatus(typing.TypedDict, total=False):
    storageSizeBytes: str

@typing.type_check_only
class InstantSnapshotsScopedList(typing.TypedDict, total=False):
    instantSnapshots: _list[InstantSnapshot]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Int64RangeMatch(typing.TypedDict, total=False):
    rangeEnd: str
    rangeStart: str

@typing.type_check_only
class Interconnect(typing.TypedDict, total=False):
    aaiEnabled: bool
    adminEnabled: bool
    applicationAwareInterconnect: InterconnectApplicationAwareInterconnect
    availableFeatures: _list[
        typing.Literal["IF_CROSS_SITE_NETWORK", "IF_L2_FORWARDING", "IF_MACSEC"]
    ]
    circuitInfos: _list[InterconnectCircuitInfo]
    creationTimestamp: str
    customerName: str
    description: str
    effectiveLocation: str
    expectedOutages: _list[InterconnectOutageNotification]
    googleIpAddress: str
    googleReferenceId: str
    id: str
    interconnectAttachments: _list[str]
    interconnectGroups: _list[str]
    interconnectType: typing.Literal["DEDICATED", "IT_PRIVATE", "PARTNER"]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    linkType: typing.Literal[
        "LINK_TYPE_ETHERNET_100G_LR",
        "LINK_TYPE_ETHERNET_10G_LR",
        "LINK_TYPE_ETHERNET_400G_LR4",
    ]
    location: str
    macsec: InterconnectMacsec
    macsecEnabled: bool
    name: str
    nocContactEmail: str
    operationalStatus: typing.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    params: InterconnectParams
    peerIpAddress: str
    provisionedLinkCount: int
    remoteLocation: str
    requestedFeatures: _list[
        typing.Literal["IF_CROSS_SITE_NETWORK", "IF_L2_FORWARDING", "IF_MACSEC"]
    ]
    requestedLinkCount: int
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal["ACTIVE", "UNPROVISIONED"]
    subzone: typing.Literal["SUBZONE_A", "SUBZONE_B"]
    wireGroups: _list[str]

@typing.type_check_only
class InterconnectApplicationAwareInterconnect(typing.TypedDict, total=False):
    bandwidthPercentagePolicy: (
        InterconnectApplicationAwareInterconnectBandwidthPercentagePolicy
    )
    profileDescription: str
    shapeAveragePercentages: _list[
        InterconnectApplicationAwareInterconnectBandwidthPercentage
    ]
    strictPriorityPolicy: InterconnectApplicationAwareInterconnectStrictPriorityPolicy

@typing.type_check_only
class InterconnectApplicationAwareInterconnectBandwidthPercentage(
    typing.TypedDict, total=False
):
    percentage: int
    trafficClass: typing.Literal["TC1", "TC2", "TC3", "TC4", "TC5", "TC6"]

@typing.type_check_only
class InterconnectApplicationAwareInterconnectBandwidthPercentagePolicy(
    typing.TypedDict, total=False
):
    bandwidthPercentages: _list[
        InterconnectApplicationAwareInterconnectBandwidthPercentage
    ]

@typing.type_check_only
class InterconnectApplicationAwareInterconnectStrictPriorityPolicy(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class InterconnectAttachment(typing.TypedDict, total=False):
    adminEnabled: bool
    attachmentGroup: str
    bandwidth: typing.Literal[
        "BPS_100G",
        "BPS_100M",
        "BPS_10G",
        "BPS_1G",
        "BPS_200M",
        "BPS_20G",
        "BPS_2G",
        "BPS_300M",
        "BPS_400G",
        "BPS_400M",
        "BPS_500M",
        "BPS_50G",
        "BPS_50M",
        "BPS_5G",
    ]
    candidateCloudRouterIpAddress: str
    candidateCloudRouterIpv6Address: str
    candidateCustomerRouterIpAddress: str
    candidateCustomerRouterIpv6Address: str
    candidateIpv6Subnets: _list[str]
    candidateSubnets: _list[str]
    cloudRouterIpAddress: str
    cloudRouterIpv6Address: str
    cloudRouterIpv6InterfaceId: str
    configurationConstraints: InterconnectAttachmentConfigurationConstraints
    creationTimestamp: str
    customerRouterIpAddress: str
    customerRouterIpv6Address: str
    customerRouterIpv6InterfaceId: str
    dataplaneVersion: int
    description: str
    edgeAvailabilityDomain: typing.Literal[
        "AVAILABILITY_DOMAIN_1", "AVAILABILITY_DOMAIN_2", "AVAILABILITY_DOMAIN_ANY"
    ]
    encryption: typing.Literal["IPSEC", "NONE"]
    googleReferenceId: str
    id: str
    interconnect: str
    ipsecInternalAddresses: _list[str]
    kind: str
    l2Forwarding: InterconnectAttachmentL2Forwarding
    labelFingerprint: str
    labels: dict[str, typing.Any]
    mtu: int
    multicastEnabled: bool
    name: str
    operationalStatus: typing.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    pairingKey: str
    params: InterconnectAttachmentParams
    partnerAsn: str
    partnerMetadata: InterconnectAttachmentPartnerMetadata
    privateInterconnectInfo: InterconnectAttachmentPrivateInfo
    region: str
    remoteService: str
    router: str
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY"]
    state: typing.Literal[
        "ACTIVE",
        "DEFUNCT",
        "PARTNER_REQUEST_RECEIVED",
        "PENDING_CUSTOMER",
        "PENDING_PARTNER",
        "STATE_UNSPECIFIED",
        "UNPROVISIONED",
    ]
    subnetLength: int
    type: typing.Literal["DEDICATED", "L2_DEDICATED", "PARTNER", "PARTNER_PROVIDER"]
    vlanTag8021q: int

@typing.type_check_only
class InterconnectAttachmentAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentConfigurationConstraints(typing.TypedDict, total=False):
    bgpMd5: typing.Literal["MD5_OPTIONAL", "MD5_REQUIRED", "MD5_UNSUPPORTED"]
    bgpPeerAsnRanges: _list[
        InterconnectAttachmentConfigurationConstraintsBgpPeerASNRange
    ]

@typing.type_check_only
class InterconnectAttachmentConfigurationConstraintsBgpPeerASNRange(
    typing.TypedDict, total=False
):
    max: int
    min: int

@typing.type_check_only
class InterconnectAttachmentGroup(typing.TypedDict, total=False):
    attachments: dict[str, typing.Any]
    configured: InterconnectAttachmentGroupConfigured
    creationTimestamp: str
    description: str
    etag: str
    id: str
    intent: InterconnectAttachmentGroupIntent
    interconnectGroup: str
    kind: str
    logicalStructure: InterconnectAttachmentGroupLogicalStructure
    name: str
    selfLink: str

@typing.type_check_only
class InterconnectAttachmentGroupAttachment(typing.TypedDict, total=False):
    attachment: str

@typing.type_check_only
class InterconnectAttachmentGroupConfigured(typing.TypedDict, total=False):
    availabilitySla: InterconnectAttachmentGroupConfiguredAvailabilitySLA

@typing.type_check_only
class InterconnectAttachmentGroupConfiguredAvailabilitySLA(
    typing.TypedDict, total=False
):
    effectiveSla: typing.Literal[
        "EFFECTIVE_SLA_UNSPECIFIED",
        "NO_SLA",
        "PRODUCTION_CRITICAL",
        "PRODUCTION_NON_CRITICAL",
    ]
    intendedSlaBlockers: _list[
        InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockers
    ]

@typing.type_check_only
class InterconnectAttachmentGroupConfiguredAvailabilitySLAIntendedSlaBlockers(
    typing.TypedDict, total=False
):
    attachments: _list[str]
    blockerType: typing.Literal[
        "BLOCKER_TYPE_UNSPECIFIED",
        "INCOMPATIBLE_METROS",
        "INCOMPATIBLE_REGIONS",
        "MISSING_GLOBAL_ROUTING",
        "NO_ATTACHMENTS",
        "NO_ATTACHMENTS_IN_METRO_AND_ZONE",
        "OTHER",
    ]
    documentationLink: str
    explanation: str
    metros: _list[str]
    regions: _list[str]
    zones: _list[str]

@typing.type_check_only
class InterconnectAttachmentGroupIntent(typing.TypedDict, total=False):
    availabilitySla: typing.Literal[
        "AVAILABILITY_SLA_UNSPECIFIED",
        "NO_SLA",
        "PRODUCTION_CRITICAL",
        "PRODUCTION_NON_CRITICAL",
    ]

@typing.type_check_only
class InterconnectAttachmentGroupLogicalStructure(typing.TypedDict, total=False):
    regions: _list[InterconnectAttachmentGroupLogicalStructureRegion]

@typing.type_check_only
class InterconnectAttachmentGroupLogicalStructureRegion(typing.TypedDict, total=False):
    metros: _list[InterconnectAttachmentGroupLogicalStructureRegionMetro]
    region: str

@typing.type_check_only
class InterconnectAttachmentGroupLogicalStructureRegionMetro(
    typing.TypedDict, total=False
):
    facilities: _list[InterconnectAttachmentGroupLogicalStructureRegionMetroFacility]
    metro: str

@typing.type_check_only
class InterconnectAttachmentGroupLogicalStructureRegionMetroFacility(
    typing.TypedDict, total=False
):
    facility: str
    zones: _list[InterconnectAttachmentGroupLogicalStructureRegionMetroFacilityZone]

@typing.type_check_only
class InterconnectAttachmentGroupLogicalStructureRegionMetroFacilityZone(
    typing.TypedDict, total=False
):
    attachments: _list[str]
    zone: str

@typing.type_check_only
class InterconnectAttachmentGroupsCreateMembers(typing.TypedDict, total=False):
    attachments: _list[
        InterconnectAttachmentGroupsCreateMembersInterconnectAttachmentInput
    ]
    intentMismatchBehavior: typing.Literal["CREATE", "REJECT", "UNSPECIFIED"]
    templateAttachment: (
        InterconnectAttachmentGroupsCreateMembersInterconnectAttachmentInput
    )

@typing.type_check_only
class InterconnectAttachmentGroupsCreateMembersInterconnectAttachmentInput(
    typing.TypedDict, total=False
):
    adminEnabled: bool
    bandwidth: typing.Literal[
        "BPS_100G",
        "BPS_100M",
        "BPS_10G",
        "BPS_1G",
        "BPS_200M",
        "BPS_20G",
        "BPS_2G",
        "BPS_300M",
        "BPS_400G",
        "BPS_400M",
        "BPS_500M",
        "BPS_50G",
        "BPS_50M",
        "BPS_5G",
    ]
    candidateCloudRouterIpAddress: str
    candidateCloudRouterIpv6Address: str
    candidateCustomerRouterIpAddress: str
    candidateCustomerRouterIpv6Address: str
    candidateIpv6Subnets: _list[str]
    candidateSubnets: _list[str]
    cloudRouterIpv6InterfaceId: str
    customerRouterIpv6InterfaceId: str
    description: str
    edgeAvailabilityDomain: typing.Literal[
        "AVAILABILITY_DOMAIN_1", "AVAILABILITY_DOMAIN_2", "AVAILABILITY_DOMAIN_ANY"
    ]
    encryption: typing.Literal["IPSEC", "NONE"]
    interconnect: str
    ipsecInternalAddresses: _list[str]
    l2Forwarding: InterconnectAttachmentL2Forwarding
    mtu: int
    multicastEnabled: bool
    name: str
    pairingKey: str
    partnerAsn: str
    partnerMetadata: InterconnectAttachmentPartnerMetadata
    region: str
    router: str
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY"]
    subnetLength: int
    type: typing.Literal["DEDICATED", "L2_DEDICATED", "PARTNER", "PARTNER_PROVIDER"]
    vlanTag8021q: int

@typing.type_check_only
class InterconnectAttachmentGroupsCreateMembersRequest(typing.TypedDict, total=False):
    request: InterconnectAttachmentGroupsCreateMembers

@typing.type_check_only
class InterconnectAttachmentGroupsGetOperationalStatusResponse(
    typing.TypedDict, total=False
):
    etag: str
    result: InterconnectAttachmentGroupsOperationalStatus

@typing.type_check_only
class InterconnectAttachmentGroupsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[InterconnectAttachmentGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentGroupsOperationalStatus(typing.TypedDict, total=False):
    attachmentStatuses: _list[
        InterconnectAttachmentGroupsOperationalStatusAttachmentStatus
    ]
    configured: InterconnectAttachmentGroupConfigured
    groupStatus: typing.Literal["DEGRADED", "FULLY_DOWN", "FULLY_UP", "UNSPECIFIED"]
    intent: InterconnectAttachmentGroupIntent
    operational: InterconnectAttachmentGroupConfigured

@typing.type_check_only
class InterconnectAttachmentGroupsOperationalStatusAttachmentStatus(
    typing.TypedDict, total=False
):
    adminEnabled: bool
    attachment: str
    isActive: typing.Literal["ACTIVE", "INACTIVE", "UNSPECIFIED"]
    status: typing.Literal[
        "ATTACHMENT_STATUS_UNKNOWN",
        "CONNECTION_DISABLED",
        "CONNECTION_DOWN",
        "CONNECTION_UP",
        "DEFUNCT",
        "IPSEC_CONFIGURATION_NEEDED_STATUS",
        "IPSEC_READY_TO_RESUME_FLOW_STATUS",
        "IPV4_DOWN_IPV6_UP",
        "IPV4_UP_IPV6_DOWN",
        "PARTNER_REQUEST_RECEIVED",
        "PENDING_CUSTOMER",
        "PENDING_PARTNER",
        "PROVISIONED",
        "ROUTER_CONFIGURATION_BROKEN",
        "UNPROVISIONED",
    ]

@typing.type_check_only
class InterconnectAttachmentL2Forwarding(typing.TypedDict, total=False):
    applianceMappings: dict[str, typing.Any]
    defaultApplianceIpAddress: str
    geneveHeader: InterconnectAttachmentL2ForwardingGeneveHeader
    network: str
    tunnelEndpointIpAddress: str

@typing.type_check_only
class InterconnectAttachmentL2ForwardingApplianceMapping(typing.TypedDict, total=False):
    applianceIpAddress: str
    innerVlanToApplianceMappings: _list[
        InterconnectAttachmentL2ForwardingApplianceMappingInnerVlanToApplianceMapping
    ]
    name: str

@typing.type_check_only
class InterconnectAttachmentL2ForwardingApplianceMappingInnerVlanToApplianceMapping(
    typing.TypedDict, total=False
):
    innerApplianceIpAddress: str
    innerVlanTags: _list[str]

@typing.type_check_only
class InterconnectAttachmentL2ForwardingGeneveHeader(typing.TypedDict, total=False):
    vni: int

@typing.type_check_only
class InterconnectAttachmentList(typing.TypedDict, total=False):
    id: str
    items: _list[InterconnectAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentPartnerMetadata(typing.TypedDict, total=False):
    interconnectName: str
    partnerName: str
    portalUrl: str

@typing.type_check_only
class InterconnectAttachmentPrivateInfo(typing.TypedDict, total=False):
    tag8021q: int

@typing.type_check_only
class InterconnectAttachmentsScopedList(typing.TypedDict, total=False):
    interconnectAttachments: _list[InterconnectAttachment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectCircuitInfo(typing.TypedDict, total=False):
    customerDemarcId: str
    googleCircuitId: str
    googleDemarcId: str

@typing.type_check_only
class InterconnectDiagnostics(typing.TypedDict, total=False):
    arpCaches: _list[InterconnectDiagnosticsARPEntry]
    bundleAggregationType: typing.Literal[
        "BUNDLE_AGGREGATION_TYPE_LACP", "BUNDLE_AGGREGATION_TYPE_STATIC"
    ]
    bundleOperationalStatus: typing.Literal[
        "BUNDLE_OPERATIONAL_STATUS_DOWN", "BUNDLE_OPERATIONAL_STATUS_UP"
    ]
    links: _list[InterconnectDiagnosticsLinkStatus]
    macAddress: str

@typing.type_check_only
class InterconnectDiagnosticsARPEntry(typing.TypedDict, total=False):
    ipAddress: str
    macAddress: str

@typing.type_check_only
class InterconnectDiagnosticsLinkLACPStatus(typing.TypedDict, total=False):
    googleSystemId: str
    neighborSystemId: str
    state: typing.Literal["ACTIVE", "DETACHED"]

@typing.type_check_only
class InterconnectDiagnosticsLinkOpticalPower(typing.TypedDict, total=False):
    state: typing.Literal[
        "HIGH_ALARM", "HIGH_WARNING", "LOW_ALARM", "LOW_WARNING", "OK"
    ]
    value: float

@typing.type_check_only
class InterconnectDiagnosticsLinkStatus(typing.TypedDict, total=False):
    arpCaches: _list[InterconnectDiagnosticsARPEntry]
    circuitId: str
    googleDemarc: str
    lacpStatus: InterconnectDiagnosticsLinkLACPStatus
    macsec: InterconnectDiagnosticsMacsecStatus
    operationalStatus: typing.Literal[
        "LINK_OPERATIONAL_STATUS_DOWN", "LINK_OPERATIONAL_STATUS_UP"
    ]
    receivingOpticalPower: InterconnectDiagnosticsLinkOpticalPower
    transmittingOpticalPower: InterconnectDiagnosticsLinkOpticalPower

@typing.type_check_only
class InterconnectDiagnosticsMacsecStatus(typing.TypedDict, total=False):
    ckn: str
    operational: bool

@typing.type_check_only
class InterconnectGroup(typing.TypedDict, total=False):
    configured: InterconnectGroupConfigured
    creationTimestamp: str
    description: str
    etag: str
    id: str
    intent: InterconnectGroupIntent
    interconnects: dict[str, typing.Any]
    kind: str
    name: str
    physicalStructure: InterconnectGroupPhysicalStructure
    selfLink: str

@typing.type_check_only
class InterconnectGroupConfigured(typing.TypedDict, total=False):
    topologyCapability: InterconnectGroupConfiguredTopologyCapability

@typing.type_check_only
class InterconnectGroupConfiguredTopologyCapability(typing.TypedDict, total=False):
    intendedCapabilityBlockers: _list[
        InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers
    ]
    supportedSla: typing.Literal[
        "NO_SLA", "PRODUCTION_CRITICAL", "PRODUCTION_NON_CRITICAL", "UNSPECIFIED"
    ]

@typing.type_check_only
class InterconnectGroupConfiguredTopologyCapabilityIntendedCapabilityBlockers(
    typing.TypedDict, total=False
):
    blockerType: typing.Literal[
        "INCOMPATIBLE_METROS",
        "NOT_AVAILABLE",
        "NO_INTERCONNECTS",
        "NO_INTERCONNECTS_IN_METRO_AND_ZONE",
        "OTHER",
        "UNSPECIFIED",
    ]
    documentationLink: str
    explanation: str
    facilities: _list[str]
    interconnects: _list[str]
    metros: _list[str]
    zones: _list[str]

@typing.type_check_only
class InterconnectGroupIntent(typing.TypedDict, total=False):
    topologyCapability: typing.Literal[
        "NO_SLA", "PRODUCTION_CRITICAL", "PRODUCTION_NON_CRITICAL", "UNSPECIFIED"
    ]

@typing.type_check_only
class InterconnectGroupInterconnect(typing.TypedDict, total=False):
    interconnect: str

@typing.type_check_only
class InterconnectGroupPhysicalStructure(typing.TypedDict, total=False):
    metros: _list[InterconnectGroupPhysicalStructureMetros]

@typing.type_check_only
class InterconnectGroupPhysicalStructureMetros(typing.TypedDict, total=False):
    facilities: _list[InterconnectGroupPhysicalStructureMetrosFacilities]
    metro: str

@typing.type_check_only
class InterconnectGroupPhysicalStructureMetrosFacilities(typing.TypedDict, total=False):
    facility: str
    zones: _list[InterconnectGroupPhysicalStructureMetrosFacilitiesZones]

@typing.type_check_only
class InterconnectGroupPhysicalStructureMetrosFacilitiesZones(
    typing.TypedDict, total=False
):
    interconnects: _list[str]
    zone: str

@typing.type_check_only
class InterconnectGroupsCreateMembers(typing.TypedDict, total=False):
    intentMismatchBehavior: typing.Literal["CREATE", "REJECT", "UNSPECIFIED"]
    interconnects: _list[InterconnectGroupsCreateMembersInterconnectInput]
    templateInterconnect: InterconnectGroupsCreateMembersInterconnectInput

@typing.type_check_only
class InterconnectGroupsCreateMembersInterconnectInput(typing.TypedDict, total=False):
    adminEnabled: bool
    customerName: str
    description: str
    facility: str
    interconnectType: typing.Literal["DEDICATED", "IT_PRIVATE", "PARTNER"]
    linkType: typing.Literal[
        "LINK_TYPE_ETHERNET_100G_LR",
        "LINK_TYPE_ETHERNET_10G_LR",
        "LINK_TYPE_ETHERNET_400G_LR4",
    ]
    name: str
    nocContactEmail: str
    remoteLocation: str
    requestedFeatures: _list[
        typing.Literal["IF_CROSS_SITE_NETWORK", "IF_L2_FORWARDING", "IF_MACSEC"]
    ]
    requestedLinkCount: int

@typing.type_check_only
class InterconnectGroupsCreateMembersRequest(typing.TypedDict, total=False):
    request: InterconnectGroupsCreateMembers

@typing.type_check_only
class InterconnectGroupsGetOperationalStatusResponse(typing.TypedDict, total=False):
    etag: str
    result: InterconnectGroupsOperationalStatus

@typing.type_check_only
class InterconnectGroupsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[InterconnectGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectGroupsOperationalStatus(typing.TypedDict, total=False):
    configured: InterconnectGroupConfigured
    groupStatus: typing.Literal[
        "DEGRADED", "FULLY_DOWN", "FULLY_UP", "GROUPS_STATUS_UNSPECIFIED"
    ]
    intent: InterconnectGroupIntent
    interconnectStatuses: _list[InterconnectGroupsOperationalStatusInterconnectStatus]
    operational: InterconnectGroupConfigured

@typing.type_check_only
class InterconnectGroupsOperationalStatusInterconnectStatus(
    typing.TypedDict, total=False
):
    adminEnabled: bool
    diagnostics: InterconnectDiagnostics
    interconnect: str
    isActive: typing.Literal["ACTIVE", "INACTIVE", "IS_ACTIVE_UNSPECIFIED"]

@typing.type_check_only
class InterconnectList(typing.TypedDict, total=False):
    id: str
    items: _list[Interconnect]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectLocation(typing.TypedDict, total=False):
    address: str
    availabilityZone: str
    availableFeatures: _list[
        typing.Literal["IF_CROSS_SITE_NETWORK", "IF_L2_FORWARDING", "IF_MACSEC"]
    ]
    availableLinkTypes: _list[
        typing.Literal[
            "LINK_TYPE_ETHERNET_100G_LR",
            "LINK_TYPE_ETHERNET_10G_LR",
            "LINK_TYPE_ETHERNET_400G_LR4",
        ]
    ]
    city: str
    continent: typing.Literal[
        "AFRICA",
        "ASIA_PAC",
        "C_AFRICA",
        "C_ASIA_PAC",
        "C_EUROPE",
        "C_NORTH_AMERICA",
        "C_SOUTH_AMERICA",
        "EUROPE",
        "NORTH_AMERICA",
        "SOUTH_AMERICA",
    ]
    creationTimestamp: str
    crossSiteInterconnectInfos: _list[InterconnectLocationCrossSiteInterconnectInfo]
    description: str
    facilityProvider: str
    facilityProviderFacilityId: str
    id: str
    kind: str
    name: str
    peeringdbFacilityId: str
    regionInfos: _list[InterconnectLocationRegionInfo]
    selfLink: str
    selfLinkWithId: str
    singleRegionProductionCriticalPeerLocations: _list[str]
    status: typing.Literal["AVAILABLE", "CLOSED"]
    supportsPzs: bool

@typing.type_check_only
class InterconnectLocationCrossSiteInterconnectInfo(typing.TypedDict, total=False):
    city: str
    maxSingleFlowGbps: int

@typing.type_check_only
class InterconnectLocationList(typing.TypedDict, total=False):
    id: str
    items: _list[InterconnectLocation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectLocationRegionInfo(typing.TypedDict, total=False):
    expectedRttMs: str
    l2ForwardingEnabled: bool
    locationPresence: typing.Literal[
        "GLOBAL", "LOCAL_REGION", "LP_GLOBAL", "LP_LOCAL_REGION"
    ]
    region: str

@typing.type_check_only
class InterconnectMacsec(typing.TypedDict, total=False):
    failOpen: bool
    interconnectKeyGroup: str
    preSharedKeys: _list[InterconnectMacsecPreSharedKey]

@typing.type_check_only
class InterconnectMacsecConfig(typing.TypedDict, total=False):
    preSharedKeys: _list[InterconnectMacsecConfigPreSharedKey]

@typing.type_check_only
class InterconnectMacsecConfigPreSharedKey(typing.TypedDict, total=False):
    cak: str
    ckn: str
    name: str
    startTime: str

@typing.type_check_only
class InterconnectMacsecPreSharedKey(typing.TypedDict, total=False):
    name: str
    startTime: str

@typing.type_check_only
class InterconnectOutageNotification(typing.TypedDict, total=False):
    affectedCircuits: _list[str]
    description: str
    endTime: str
    issueType: typing.Literal[
        "IT_OUTAGE", "IT_PARTIAL_OUTAGE", "OUTAGE", "PARTIAL_OUTAGE"
    ]
    name: str
    source: typing.Literal["GOOGLE", "NSRC_GOOGLE"]
    startTime: str
    state: typing.Literal[
        "ACTIVE", "CANCELLED", "COMPLETED", "NS_ACTIVE", "NS_CANCELED"
    ]

@typing.type_check_only
class InterconnectParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InterconnectRemoteLocation(typing.TypedDict, total=False):
    address: str
    attachmentConfigurationConstraints: InterconnectAttachmentConfigurationConstraints
    city: str
    constraints: InterconnectRemoteLocationConstraints
    continent: typing.Literal[
        "AFRICA", "ASIA_PAC", "EUROPE", "NORTH_AMERICA", "SOUTH_AMERICA"
    ]
    creationTimestamp: str
    description: str
    facilityProvider: str
    facilityProviderFacilityId: str
    id: str
    kind: str
    lacp: typing.Literal["LACP_SUPPORTED", "LACP_UNSUPPORTED"]
    maxLagSize100Gbps: int
    maxLagSize10Gbps: int
    maxLagSize400Gbps: int
    name: str
    peeringdbFacilityId: str
    permittedConnections: _list[InterconnectRemoteLocationPermittedConnections]
    remoteService: str
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal["AVAILABLE", "CLOSED"]

@typing.type_check_only
class InterconnectRemoteLocationConstraints(typing.TypedDict, total=False):
    portPairRemoteLocation: typing.Literal[
        "PORT_PAIR_MATCHING_REMOTE_LOCATION", "PORT_PAIR_UNCONSTRAINED_REMOTE_LOCATION"
    ]
    portPairVlan: typing.Literal[
        "PORT_PAIR_MATCHING_VLAN", "PORT_PAIR_UNCONSTRAINED_VLAN"
    ]
    subnetLengthRange: InterconnectRemoteLocationConstraintsSubnetLengthRange

@typing.type_check_only
class InterconnectRemoteLocationConstraintsSubnetLengthRange(
    typing.TypedDict, total=False
):
    max: int
    min: int

@typing.type_check_only
class InterconnectRemoteLocationList(typing.TypedDict, total=False):
    id: str
    items: _list[InterconnectRemoteLocation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectRemoteLocationPermittedConnections(typing.TypedDict, total=False):
    interconnectLocation: str

@typing.type_check_only
class InterconnectsGetDiagnosticsResponse(typing.TypedDict, total=False):
    result: InterconnectDiagnostics

@typing.type_check_only
class InterconnectsGetMacsecConfigResponse(typing.TypedDict, total=False):
    etag: str
    result: InterconnectMacsecConfig

@typing.type_check_only
class InterconnectsSetNameRequest(typing.TypedDict, total=False):
    currentName: str
    name: str

@typing.type_check_only
class InternalIpAddress(typing.TypedDict, total=False):
    cidr: str
    owner: str
    purpose: str
    region: str
    type: typing.Literal[
        "PEER_RESERVED",
        "PEER_USED",
        "REMOTE_RESERVED",
        "REMOTE_USED",
        "RESERVED",
        "SUBNETWORK",
        "TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class InternalIpOwner(typing.TypedDict, total=False):
    ipCidrRange: str
    owners: _list[str]
    systemOwned: bool

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class IpAddressesList(typing.TypedDict, total=False):
    id: str
    items: _list[InternalIpAddress]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class IpOwnerList(typing.TypedDict, total=False):
    id: str
    items: _list[InternalIpOwner]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Jwt(typing.TypedDict, total=False):
    audiences: _list[str]
    issuer: str
    jwksPublicKeys: str
    jwtHeaders: _list[JwtHeader]
    jwtParams: _list[str]

@typing.type_check_only
class JwtHeader(typing.TypedDict, total=False):
    name: str
    valuePrefix: str

@typing.type_check_only
class License(typing.TypedDict, total=False):
    allowedReplacementLicenses: _list[str]
    appendableToDisk: bool
    chargesUseFee: bool
    creationTimestamp: str
    description: str
    id: str
    incompatibleLicenses: _list[str]
    kind: str
    licenseCode: str
    minimumRetention: Duration
    multiTenantOnly: bool
    name: str
    osLicense: bool
    params: LicenseParams
    removableFromDisk: bool
    requiredCoattachedLicenses: _list[str]
    resourceRequirements: LicenseResourceRequirements
    selfLink: str
    selfLinkWithId: str
    soleTenantOnly: bool
    transferable: bool
    updateTimestamp: str

@typing.type_check_only
class LicenseCode(typing.TypedDict, total=False):
    allowedReplacementLicenses: _list[str]
    appendableToDisk: bool
    creationTimestamp: str
    description: str
    id: str
    incompatibleLicenses: _list[str]
    kind: str
    licenseAlias: _list[LicenseCodeLicenseAlias]
    minimumRetention: Duration
    multiTenantOnly: bool
    name: str
    osLicense: bool
    removableFromDisk: bool
    requiredCoattachedLicenses: _list[str]
    selfLink: str
    soleTenantOnly: bool
    state: typing.Literal[
        "DISABLED", "ENABLED", "RESTRICTED", "STATE_UNSPECIFIED", "TERMINATED"
    ]
    transferable: bool
    updateTimestamp: str

@typing.type_check_only
class LicenseCodeLicenseAlias(typing.TypedDict, total=False):
    description: str
    selfLink: str

@typing.type_check_only
class LicenseParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class LicenseResourceCommitment(typing.TypedDict, total=False):
    amount: str
    coresPerLicense: str
    license: str

@typing.type_check_only
class LicenseResourceRequirements(typing.TypedDict, total=False):
    minGuestCpuCount: int
    minMemoryMb: int

@typing.type_check_only
class LicensesListResponse(typing.TypedDict, total=False):
    id: str
    items: _list[License]
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ListInstantSnapshotGroups(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[InstantSnapshotGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ListSnapshotGroups(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[SnapshotGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ListVmExtensionStatesResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[VmExtensionState]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ListVmExtensionsResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[VmExtension]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class LocalDisk(typing.TypedDict, total=False):
    diskCount: int
    diskSizeGb: int
    diskType: str

@typing.type_check_only
class LocalizedMessage(typing.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class LocationPolicy(typing.TypedDict, total=False):
    locations: dict[str, typing.Any]
    targetShape: typing.Literal["ANY", "ANY_SINGLE_ZONE", "BALANCED"]
    zones: _list[LocationPolicyZoneConfiguration]

@typing.type_check_only
class LocationPolicyLocation(typing.TypedDict, total=False):
    constraints: LocationPolicyLocationConstraints
    names: _list[str]
    preference: typing.Literal["ALLOW", "DENY", "PREFERENCE_UNSPECIFIED"]

@typing.type_check_only
class LocationPolicyLocationConstraints(typing.TypedDict, total=False):
    maxCount: int

@typing.type_check_only
class LocationPolicyZoneConfiguration(typing.TypedDict, total=False):
    zone: str

@typing.type_check_only
class MachineImage(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    guestFlush: bool
    id: str
    instanceProperties: InstanceProperties
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    machineImageEncryptionKey: CustomerEncryptionKey
    name: str
    params: MachineImageParams
    satisfiesPzi: bool
    satisfiesPzs: bool
    savedDisks: _list[SavedDisk]
    selfLink: str
    selfLinkWithId: str
    sourceDiskEncryptionKeys: _list[SourceDiskEncryptionKey]
    sourceInstance: str
    sourceInstanceProperties: SourceInstanceProperties
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY", "UPLOADING"]
    storageLocations: _list[str]
    totalStorageBytes: str

@typing.type_check_only
class MachineImageList(typing.TypedDict, total=False):
    id: str
    items: _list[MachineImage]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class MachineImageParams(typing.TypedDict, total=False):
    excludedDisks: _list[str]
    includedDisks: _list[str]
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class MachineType(typing.TypedDict, total=False):
    accelerators: _list[dict[str, typing.Any]]
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    bundledLocalSsds: BundledLocalSsds
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    guestCpus: int
    id: str
    isSharedCpu: bool
    kind: str
    maximumPersistentDisks: int
    maximumPersistentDisksSizeGb: str
    memoryMb: int
    name: str
    selfLink: str
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class MachineTypeAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class MachineTypeList(typing.TypedDict, total=False):
    id: str
    items: _list[MachineType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class MachineTypesScopedList(typing.TypedDict, total=False):
    machineTypes: _list[MachineType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ManagedInstance(typing.TypedDict, total=False):
    allInstancesConfig: ManagedInstanceAllInstancesConfig
    currentAction: typing.Literal[
        "ABANDONING",
        "ADOPTING",
        "CREATING",
        "CREATING_ATOMICALLY",
        "CREATING_WITHOUT_RETRIES",
        "DELETING",
        "NONE",
        "QUEUING",
        "RECREATING",
        "REFRESHING",
        "RESTARTING",
        "RESTARTING_IN_PLACE",
        "RESUMING",
        "STARTING",
        "STOPPING",
        "SUSPENDING",
        "VERIFYING",
    ]
    currentActionDetails: ManagedInstanceCurrentActionDetails
    id: str
    instance: str
    instanceFlexibilityOverride: ManagedInstanceInstanceFlexibilityOverride
    instanceHealth: _list[ManagedInstanceInstanceHealth]
    instanceStatus: typing.Literal[
        "DEPROVISIONING",
        "PENDING",
        "PENDING_STOP",
        "PROVISIONING",
        "REPAIRING",
        "RUNNING",
        "STAGING",
        "STOPPED",
        "STOPPING",
        "SUSPENDED",
        "SUSPENDING",
        "TERMINATED",
    ]
    instanceTemplate: str
    lastAttempt: ManagedInstanceLastAttempt
    name: str
    preservedStateFromConfig: PreservedState
    preservedStateFromPolicy: PreservedState
    propertiesFromFlexibilityPolicy: ManagedInstancePropertiesFromFlexibilityPolicy
    scheduling: ManagedInstanceScheduling
    shutdownDetails: ManagedInstanceShutdownDetails
    sizeInUnit: float
    tag: str
    targetStatus: typing.Literal[
        "ABANDONED", "DELETED", "RUNNING", "STOPPED", "SUSPENDED"
    ]
    version: ManagedInstanceVersion

@typing.type_check_only
class ManagedInstanceAllInstancesConfig(typing.TypedDict, total=False):
    revision: str

@typing.type_check_only
class ManagedInstanceCurrentActionDetails(typing.TypedDict, total=False):
    methodName: str
    trigger: typing.Literal[
        "API",
        "AUTOSCALING",
        "FAILED_CREATION",
        "FAILED_HEALTH_CHECK",
        "INSTANCE_FAILURE",
        "MAINTENANCE",
        "NONE",
        "PROACTIVE_UPDATE",
        "REDISTRIBUTION",
        "STANDBY_REFILL",
        "TERMINATION_TIMESTAMP",
    ]

@typing.type_check_only
class ManagedInstanceInstanceFlexibilityOverride(typing.TypedDict, total=False):
    disks: _list[AttachedDisk]
    machineType: str
    minCpuPlatform: str
    provisioningModel: typing.Literal[
        "FLEX_START", "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]

@typing.type_check_only
class ManagedInstanceInstanceHealth(typing.TypedDict, total=False):
    detailedHealthState: typing.Literal[
        "DRAINING", "HEALTHY", "TIMEOUT", "UNHEALTHY", "UNKNOWN"
    ]
    healthCheck: str
    healthState: typing.Literal["HEALTHY", "UNHEALTHY"]

@typing.type_check_only
class ManagedInstanceLastAttempt(typing.TypedDict, total=False):
    errors: dict[str, typing.Any]

@typing.type_check_only
class ManagedInstancePropertiesFromFlexibilityPolicy(typing.TypedDict, total=False):
    disks: _list[AttachedDisk]
    machineType: str
    minCpuPlatform: str
    provisioningModel: typing.Literal[
        "FLEX_START", "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]

@typing.type_check_only
class ManagedInstanceScheduling(typing.TypedDict, total=False):
    gracefulShutdownTimestamp: str
    terminationTimestamp: str

@typing.type_check_only
class ManagedInstanceShutdownDetails(typing.TypedDict, total=False):
    maxDuration: Duration
    requestTimestamp: str

@typing.type_check_only
class ManagedInstanceVersion(typing.TypedDict, total=False):
    instanceTemplate: str
    name: str

@typing.type_check_only
class ManagedRuleset(typing.TypedDict, total=False):
    changeLog: str
    creationTimestamp: str
    description: str
    id: str
    name: str
    ruleIds: _list[str]
    rulesetId: str
    selfLink: str

@typing.type_check_only
class ManagedRulesetList(typing.TypedDict, total=False):
    id: str
    items: _list[ManagedRuleset]
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ManagementInterface(typing.TypedDict, total=False):
    authenticationConfig: AuthenticationConfig
    ipv4Address: str
    ipv6Address: str
    network: str
    state: typing.Literal["ACTIVE", "INACTIVE", "PENDING", "STATE_UNSPECIFIED"]
    subnetwork: str
    type: typing.Literal[
        "TYPE_NVLINK_PARTITION_MANAGEMENT",
        "TYPE_NVLINK_SWITCH_MONITORING",
        "TYPE_TPU_SLICE_MANAGEMENT",
        "TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    fingerprint: str
    items: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class MetadataCredentialsFromPlugin(typing.TypedDict, total=False):
    name: str
    structConfig: str

@typing.type_check_only
class MetadataFilter(typing.TypedDict, total=False):
    filterLabels: _list[MetadataFilterLabelMatch]
    filterMatchCriteria: typing.Literal["MATCH_ALL", "MATCH_ANY", "NOT_SET"]

@typing.type_check_only
class MetadataFilterLabelMatch(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MultiMig(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    region: str
    resourcePolicies: MultiMigResourcePolicies
    selfLink: str
    status: MultiMigStatus

@typing.type_check_only
class MultiMigMember(typing.TypedDict, total=False):
    creationTimestamp: str
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    status: MultiMigMemberStatus

@typing.type_check_only
class MultiMigMemberList(typing.TypedDict, total=False):
    id: str
    items: _list[MultiMigMember]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class MultiMigMemberStatus(typing.TypedDict, total=False):
    instanceGroupManager: str

@typing.type_check_only
class MultiMigResourcePolicies(typing.TypedDict, total=False):
    workloadPolicy: str

@typing.type_check_only
class MultiMigStatus(typing.TypedDict, total=False):
    appliedAcceleratorTopologies: _list[MultiMigStatusAcceleratorTopology]
    memberInstanceGroupManagers: _list[str]
    membersCount: int

@typing.type_check_only
class MultiMigStatusAcceleratorTopology(typing.TypedDict, total=False):
    acceleratorTopology: str
    acceleratorTopologyState: typing.Literal[
        "ACTIVATING",
        "ACTIVE",
        "ACTIVE_DEGRADED",
        "DEACTIVATING",
        "FAILED",
        "INCOMPLETE",
    ]
    acceleratorTopologyStateLastCheck: (
        MultiMigStatusAcceleratorTopologyAcceleratorTopologyStateLastCheck
    )

@typing.type_check_only
class MultiMigStatusAcceleratorTopologyAcceleratorTopologyStateLastCheck(
    typing.TypedDict, total=False
):
    error: dict[str, typing.Any]
    timestamp: str

@typing.type_check_only
class MultiMigsList(typing.TypedDict, total=False):
    id: str
    items: _list[MultiMig]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class MutualTls(typing.TypedDict, total=False):
    mode: typing.Literal["INVALID", "PERMISSIVE", "STRICT"]

@typing.type_check_only
class NamedPort(typing.TypedDict, total=False):
    name: str
    port: int

@typing.type_check_only
class NamedSet(typing.TypedDict, total=False):
    description: str
    elements: _list[Expr]
    fingerprint: str
    name: str
    type: typing.Literal["NAMED_SET_TYPE_COMMUNITY", "NAMED_SET_TYPE_PREFIX"]

@typing.type_check_only
class NatIpInfo(typing.TypedDict, total=False):
    natIpInfoMappings: _list[NatIpInfoNatIpInfoMapping]
    natName: str

@typing.type_check_only
class NatIpInfoNatIpInfoMapping(typing.TypedDict, total=False):
    mode: typing.Literal["AUTO", "MANUAL"]
    natIp: str
    usage: typing.Literal["IN_USE", "UNUSED"]

@typing.type_check_only
class NatIpInfoResponse(typing.TypedDict, total=False):
    result: _list[NatIpInfo]

@typing.type_check_only
class Network(typing.TypedDict, total=False):
    IPv4Range: str
    autoCreateSubnetworks: bool
    creationTimestamp: str
    description: str
    enableUlaInternalIpv6: bool
    firewallPolicy: str
    gatewayIPv4: str
    id: str
    internalIpv6Range: str
    kind: str
    mtu: int
    name: str
    networkFirewallPolicyEnforcementOrder: typing.Literal[
        "AFTER_CLASSIC_FIREWALL", "BEFORE_CLASSIC_FIREWALL"
    ]
    networkProfile: str
    params: NetworkParams
    peerings: _list[NetworkPeering]
    region: str
    routingConfig: NetworkRoutingConfig
    selfLink: str
    selfLinkWithId: str
    subnetworks: _list[str]

@typing.type_check_only
class NetworkAttachment(typing.TypedDict, total=False):
    connectionEndpoints: _list[NetworkAttachmentConnectedEndpoint]
    connectionPreference: typing.Literal["ACCEPT_AUTOMATIC", "ACCEPT_MANUAL", "INVALID"]
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    network: str
    producerAcceptLists: _list[str]
    producerRejectLists: _list[str]
    region: str
    selfLink: str
    selfLinkWithId: str
    subnetworks: _list[str]

@typing.type_check_only
class NetworkAttachmentAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkAttachmentConnectedEndpoint(typing.TypedDict, total=False):
    ipAddress: str
    ipv6Address: str
    projectIdOrNum: str
    secondaryIpCidrRanges: _list[str]
    serviceClassId: str
    status: typing.Literal[
        "ACCEPTED",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "RESERVED",
        "STATUS_UNSPECIFIED",
    ]
    subnetwork: str
    subnetworkCidrRange: str

@typing.type_check_only
class NetworkAttachmentList(typing.TypedDict, total=False):
    id: str
    items: _list[NetworkAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkAttachmentsScopedList(typing.TypedDict, total=False):
    networkAttachments: _list[NetworkAttachment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEdgeSecurityService(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    region: str
    securityPolicy: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class NetworkEdgeSecurityServiceAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEdgeSecurityServicesScopedList(typing.TypedDict, total=False):
    networkEdgeSecurityServices: _list[NetworkEdgeSecurityService]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpoint(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clientDestinationPort: int
    fqdn: str
    instance: str
    ipAddress: str
    ipv6Address: str
    port: int

@typing.type_check_only
class NetworkEndpointGroup(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    appEngine: NetworkEndpointGroupAppEngine
    cloudFunction: NetworkEndpointGroupCloudFunction
    cloudRun: NetworkEndpointGroupCloudRun
    creationTimestamp: str
    defaultPort: int
    description: str
    id: str
    kind: str
    loadBalancer: NetworkEndpointGroupLbNetworkEndpointGroup
    name: str
    network: str
    networkEndpointType: typing.Literal[
        "GCE_VM_IP",
        "GCE_VM_IP_DEDICATED_BACKEND",
        "GCE_VM_IP_PORT",
        "GCE_VM_IP_PORTMAP",
        "INTERNET_FQDN_PORT",
        "INTERNET_IP_PORT",
        "NON_GCP_PRIVATE_IP_PORT",
        "PRIVATE_SERVICE_CONNECT",
        "SERVERLESS",
    ]
    pscData: NetworkEndpointGroupPscData
    pscTargetService: str
    region: str
    selfLink: str
    selfLinkWithId: str
    serverlessDeployment: NetworkEndpointGroupServerlessDeployment
    size: int
    subnetwork: str
    type: typing.Literal["LOAD_BALANCING"]
    zone: str

@typing.type_check_only
class NetworkEndpointGroupAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupAppEngine(typing.TypedDict, total=False):
    service: str
    urlMask: str
    version: str

@typing.type_check_only
class NetworkEndpointGroupCloudFunction(typing.TypedDict, total=False):
    function: str
    urlMask: str

@typing.type_check_only
class NetworkEndpointGroupCloudRun(typing.TypedDict, total=False):
    service: str
    tag: str
    urlMask: str

@typing.type_check_only
class NetworkEndpointGroupLbNetworkEndpointGroup(typing.TypedDict, total=False):
    defaultPort: int
    network: str
    subnetwork: str
    zone: str

@typing.type_check_only
class NetworkEndpointGroupList(typing.TypedDict, total=False):
    id: str
    items: _list[NetworkEndpointGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupPscData(typing.TypedDict, total=False):
    consumerPscAddress: str
    producerPort: int
    pscConnectionId: str
    pscConnectionStatus: typing.Literal[
        "ACCEPTED",
        "ACCEPTED_LIMITED_CAPACITY",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]

@typing.type_check_only
class NetworkEndpointGroupServerlessDeployment(typing.TypedDict, total=False):
    platform: str
    resource: str
    urlMask: str
    version: str

@typing.type_check_only
class NetworkEndpointGroupsAttachEndpointsRequest(typing.TypedDict, total=False):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class NetworkEndpointGroupsDetachEndpointsRequest(typing.TypedDict, total=False):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class NetworkEndpointGroupsListEndpointsRequest(typing.TypedDict, total=False):
    endpointFilters: _list[
        NetworkEndpointGroupsListEndpointsRequestNetworkEndpointFilter
    ]
    healthStatus: typing.Literal["SHOW", "SKIP"]

@typing.type_check_only
class NetworkEndpointGroupsListEndpointsRequestNetworkEndpointFilter(
    typing.TypedDict, total=False
):
    networkEndpoint: NetworkEndpoint

@typing.type_check_only
class NetworkEndpointGroupsListNetworkEndpoints(typing.TypedDict, total=False):
    id: str
    items: _list[NetworkEndpointWithHealthStatus]
    kind: str
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupsScopedList(typing.TypedDict, total=False):
    networkEndpointGroups: _list[NetworkEndpointGroup]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointWithHealthStatus(typing.TypedDict, total=False):
    healths: _list[HealthStatusForNetworkEndpoint]
    networkEndpoint: NetworkEndpoint

@typing.type_check_only
class NetworkFirewallPolicyAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkInterface(typing.TypedDict, total=False):
    accessConfigs: _list[AccessConfig]
    aliasIpRanges: _list[AliasIpRange]
    aliasIpv6Ranges: _list[AliasIpRange]
    dns64Eligible: bool
    enableVpcScopedDns: bool
    fingerprint: str
    igmpQuery: typing.Literal["IGMP_QUERY_DISABLED", "IGMP_QUERY_V2"]
    internalIpv6PrefixLength: int
    internalNicLoadBalancingIpv6Address: str
    internalNicLoadBalancingIpv6PrefixLength: int
    ipv6AccessConfigs: _list[AccessConfig]
    ipv6AccessType: typing.Literal["EXTERNAL", "INTERNAL"]
    ipv6Address: str
    kind: str
    macAddress: str
    name: str
    nat64Eligible: bool
    network: str
    networkAttachment: str
    networkIP: str
    nicType: typing.Literal[
        "GVNIC", "IDPF", "IRDMA", "MRDMA", "UNSPECIFIED_NIC_TYPE", "VIRTIO_NET"
    ]
    parentNicName: str
    queueCount: int
    serviceClassId: str
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    subinterfaces: _list[NetworkInterfaceSubInterface]
    subnetwork: str
    vlan: int

@typing.type_check_only
class NetworkInterfaceSubInterface(typing.TypedDict, total=False):
    ipAddress: str
    ipAllocationMode: typing.Literal["ALLOCATE_IP", "DO_NOT_ALLOCATE_IP", "UNSPECIFIED"]
    subnetwork: str
    vlan: int

@typing.type_check_only
class NetworkList(typing.TypedDict, total=False):
    id: str
    items: _list[Network]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class NetworkPeering(typing.TypedDict, total=False):
    advertisePeerSubnetsViaRouters: bool
    autoCreateRoutes: bool
    connectionStatus: NetworkPeeringConnectionStatus
    exchangeSubnetRoutes: bool
    exportCustomRoutes: bool
    exportSubnetRoutesWithPublicIp: bool
    importCustomRoutes: bool
    importSubnetRoutesWithPublicIp: bool
    name: str
    network: str
    peerMtu: int
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY"]
    state: typing.Literal[
        "ACTIVE", "INACTIVE", "NCC_MIGRATION_COMPLETE", "NCC_MIGRATION_IN_PROGRESS"
    ]
    stateDetails: str
    updateStrategy: typing.Literal["CONSENSUS", "INDEPENDENT", "UNSPECIFIED"]

@typing.type_check_only
class NetworkPeeringConnectionStatus(typing.TypedDict, total=False):
    consensusState: NetworkPeeringConnectionStatusConsensusState
    trafficConfiguration: NetworkPeeringConnectionStatusTrafficConfiguration
    updateStrategy: typing.Literal["CONSENSUS", "INDEPENDENT", "UNSPECIFIED"]

@typing.type_check_only
class NetworkPeeringConnectionStatusConsensusState(typing.TypedDict, total=False):
    deleteStatus: typing.Literal[
        "DELETE_ACKNOWLEDGED",
        "DELETE_STATUS_UNSPECIFIED",
        "LOCAL_CANCEL_REQUESTED",
        "LOCAL_DELETE_REQUESTED",
        "PEER_CANCEL_REQUESTED",
        "PEER_DELETE_REQUESTED",
    ]
    updateStatus: typing.Literal[
        "IN_SYNC",
        "PENDING_LOCAL_ACKNOWLEDMENT",
        "PENDING_PEER_ACKNOWLEDGEMENT",
        "UPDATE_STATUS_UNSPECIFIED",
    ]

@typing.type_check_only
class NetworkPeeringConnectionStatusTrafficConfiguration(typing.TypedDict, total=False):
    exportCustomRoutesToPeer: bool
    exportSubnetRoutesWithPublicIpToPeer: bool
    importCustomRoutesFromPeer: bool
    importSubnetRoutesWithPublicIpFromPeer: bool
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY"]

@typing.type_check_only
class NetworkPerformanceConfig(typing.TypedDict, total=False):
    externalIpEgressBandwidthTier: typing.Literal["DEFAULT", "TIER_1"]
    totalEgressBandwidthTier: typing.Literal["DEFAULT", "TIER_1"]

@typing.type_check_only
class NetworkPoliciesScopedList(typing.TypedDict, total=False):
    networkPolicies: _list[NetworkPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkPolicy(typing.TypedDict, total=False):
    associations: _list[NetworkPolicyAssociation]
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    region: str
    ruleTupleCount: int
    selfLink: str
    selfLinkWithId: str
    trafficClassificationRules: _list[NetworkPolicyTrafficClassificationRule]

@typing.type_check_only
class NetworkPolicyAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkPolicyAssociation(typing.TypedDict, total=False):
    attachmentTarget: str
    name: str

@typing.type_check_only
class NetworkPolicyList(typing.TypedDict, total=False):
    id: str
    items: _list[NetworkPolicy]
    kind: str
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkPolicyTrafficClassificationRule(typing.TypedDict, total=False):
    action: NetworkPolicyTrafficClassificationRuleAction
    description: str
    disabled: bool
    kind: str
    match: NetworkPolicyTrafficClassificationRuleMatcher
    priority: int
    ruleName: str
    ruleTupleCount: int
    targetSecureTags: _list[NetworkPolicyTrafficClassificationRuleSecureTag]
    targetServiceAccounts: _list[str]

@typing.type_check_only
class NetworkPolicyTrafficClassificationRuleAction(typing.TypedDict, total=False):
    dscpMode: typing.Literal["AUTO", "CUSTOM"]
    dscpValue: int
    trafficClass: typing.Literal["TC1", "TC2", "TC3", "TC4", "TC5", "TC6"]
    type: str

@typing.type_check_only
class NetworkPolicyTrafficClassificationRuleMatcher(typing.TypedDict, total=False):
    destAddressGroups: _list[str]
    destIpRanges: _list[str]
    layer4Configs: _list[NetworkPolicyTrafficClassificationRuleMatcherLayer4Config]
    srcIpRanges: _list[str]

@typing.type_check_only
class NetworkPolicyTrafficClassificationRuleMatcherLayer4Config(
    typing.TypedDict, total=False
):
    ipProtocol: str
    ports: _list[str]

@typing.type_check_only
class NetworkPolicyTrafficClassificationRuleSecureTag(typing.TypedDict, total=False):
    name: str
    state: typing.Literal["EFFECTIVE", "INEFFECTIVE", "STATE_UNSPECIFIED"]

@typing.type_check_only
class NetworkProfile(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    features: NetworkProfileNetworkFeatures
    id: str
    kind: str
    location: NetworkProfileLocation
    name: str
    profileType: NetworkProfileProfileType
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class NetworkProfileLocation(typing.TypedDict, total=False):
    name: str
    scope: typing.Literal["REGION", "ZONE"]

@typing.type_check_only
class NetworkProfileNetworkFeatures(typing.TypedDict, total=False):
    addressPurposes: _list[
        typing.Literal[
            "APPLICATION_AND_PROXY_LOAD_BALANCERS",
            "DNS_RESOLVER",
            "GCE_ENDPOINT",
            "IPSEC_INTERCONNECT",
            "NAT_AUTO",
            "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0",
            "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1",
            "PRIVATE_SERVICE_CONNECT",
            "SERVERLESS",
            "SHARED_LOADBALANCER_VIP",
            "SYSTEM_MANAGED",
            "VPC_PEERING",
        ]
    ]
    allowAddressCreation: typing.Literal[
        "ADDRESS_CREATION_ALLOWED", "ADDRESS_CREATION_BLOCKED"
    ]
    allowAliasIpRanges: typing.Literal[
        "ALIAS_IP_RANGES_ALLOWED", "ALIAS_IP_RANGES_BLOCKED"
    ]
    allowAutoModeSubnet: typing.Literal[
        "AUTO_MODE_SUBNET_ALLOWED", "AUTO_MODE_SUBNET_BLOCKED"
    ]
    allowClassDFirewalls: typing.Literal[
        "CLASS_D_FIREWALLS_ALLOWED", "CLASS_D_FIREWALLS_BLOCKED"
    ]
    allowCloudNat: typing.Literal["CLOUD_NAT_ALLOWED", "CLOUD_NAT_BLOCKED"]
    allowCloudRouter: typing.Literal["CLOUD_ROUTER_ALLOWED", "CLOUD_ROUTER_BLOCKED"]
    allowDefaultNicAttachment: typing.Literal[
        "DEFAULT_NIC_ATTACHMENT_ALLOWED", "DEFAULT_NIC_ATTACHMENT_BLOCKED"
    ]
    allowExternalIpAccess: typing.Literal[
        "EXTERNAL_IP_ACCESS_ALLOWED", "EXTERNAL_IP_ACCESS_BLOCKED"
    ]
    allowFirewallPolicy: typing.Literal[
        "FIREWALL_POLICY_ALLOWED", "FIREWALL_POLICY_BLOCKED"
    ]
    allowInterconnect: typing.Literal["INTERCONNECT_ALLOWED", "INTERCONNECT_BLOCKED"]
    allowIpForwarding: typing.Literal["IP_FORWARDING_ALLOWED", "IP_FORWARDING_BLOCKED"]
    allowLoadBalancing: typing.Literal[
        "LOAD_BALANCING_ALLOWED", "LOAD_BALANCING_BLOCKED"
    ]
    allowMultiNicInSameNetwork: typing.Literal[
        "MULTI_NIC_IN_SAME_NETWORK_ALLOWED", "MULTI_NIC_IN_SAME_NETWORK_BLOCKED"
    ]
    allowMultiNicInSameSubnetwork: typing.Literal[
        "MULTI_NIC_IN_SAME_SUBNETWORK_ALLOWED", "MULTI_NIC_IN_SAME_SUBNETWORK_BLOCKED"
    ]
    allowMulticast: typing.Literal["MULTICAST_ALLOWED", "MULTICAST_BLOCKED"]
    allowNcc: typing.Literal["NCC_ALLOWED", "NCC_BLOCKED"]
    allowNetworkMigration: typing.Literal[
        "NETWORK_MIGRATION_ALLOWED", "NETWORK_MIGRATION_BLOCKED"
    ]
    allowPacketMirroring: typing.Literal[
        "PACKET_MIRRORING_ALLOWED", "PACKET_MIRRORING_BLOCKED"
    ]
    allowPrivateGoogleAccess: typing.Literal[
        "PRIVATE_GOOGLE_ACCESS_ALLOWED", "PRIVATE_GOOGLE_ACCESS_BLOCKED"
    ]
    allowPsc: typing.Literal["PSC_ALLOWED", "PSC_BLOCKED"]
    allowSameNetworkUnicast: typing.Literal[
        "SAME_NETWORK_UNICAST_ALLOWED", "SAME_NETWORK_UNICAST_BLOCKED"
    ]
    allowStaticRoutes: typing.Literal["STATIC_ROUTES_ALLOWED", "STATIC_ROUTES_BLOCKED"]
    allowSubInterfaces: typing.Literal["SUBINTERFACES_ALLOWED", "SUBINTERFACES_BLOCKED"]
    allowSubnetworkCreation: typing.Literal[
        "SUBNETWORK_CREATION_ALLOWED", "SUBNETWORK_CREATION_BLOCKED"
    ]
    allowVpcFirewallRules: typing.Literal[
        "VPC_FIREWALL_RULES_ALLOWED", "VPC_FIREWALL_RULES_BLOCKED"
    ]
    allowVpcPeering: typing.Literal["VPC_PEERING_ALLOWED", "VPC_PEERING_BLOCKED"]
    allowVpn: typing.Literal["VPN_ALLOWED", "VPN_BLOCKED"]
    firewallPolicyTypes: _list[
        typing.Literal[
            "RDMA_FALCON_POLICY", "RDMA_ROCE_POLICY", "ULL_POLICY", "VPC_POLICY"
        ]
    ]
    interfaceTypes: _list[
        typing.Literal[
            "GVNIC", "IDPF", "IRDMA", "MRDMA", "UNSPECIFIED_NIC_TYPE", "VIRTIO_NET"
        ]
    ]
    multicast: typing.Literal["MULTICAST_SDN", "MULTICAST_ULL"]
    predefinedNetworkInternalIpv6Range: str
    predefinedSubnetworkRanges: _list[
        NetworkProfileNetworkFeaturesPredefinedSubnetworkRange
    ]
    subnetPurposes: _list[
        typing.Literal["SUBNET_PURPOSE_CUSTOM_HARDWARE", "SUBNET_PURPOSE_PRIVATE"]
    ]
    subnetStackTypes: _list[
        typing.Literal[
            "SUBNET_STACK_TYPE_IPV4_IPV6",
            "SUBNET_STACK_TYPE_IPV4_ONLY",
            "SUBNET_STACK_TYPE_IPV6_ONLY",
        ]
    ]
    subnetworkPurposes: _list[
        typing.Literal[
            "AGGREGATE",
            "CLOUD_EXTENSION",
            "CUSTOM_HARDWARE_LINK",
            "GLOBAL_MANAGED_PROXY",
            "INTERNAL_HTTPS_LOAD_BALANCER",
            "PEER_MIGRATION",
            "PRIVATE",
            "PRIVATE_NAT",
            "PRIVATE_RFC_1918",
            "PRIVATE_SERVICE_CONNECT",
            "REGIONAL_MANAGED_PROXY",
        ]
    ]
    subnetworkStackTypes: _list[typing.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]]
    unicast: typing.Literal["UNICAST_SDN", "UNICAST_ULL"]

@typing.type_check_only
class NetworkProfileNetworkFeaturesPredefinedSubnetworkRange(
    typing.TypedDict, total=False
):
    ipv6Range: str
    namePrefix: str

@typing.type_check_only
class NetworkProfileProfileType(typing.TypedDict, total=False):
    networkType: typing.Literal["RDMA", "ULL", "VPC"]
    rdmaSubtype: typing.Literal["FALCON", "ROCE", "ROCE_METAL"]
    ullSubtype: typing.Literal["OPERATOR", "PARTICIPANT"]
    vpcSubtype: typing.Literal["REGIONAL"]

@typing.type_check_only
class NetworkProfilesListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[NetworkProfile]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkRoutingConfig(typing.TypedDict, total=False):
    bgpAlwaysCompareMed: bool
    bgpBestPathSelectionMode: typing.Literal["LEGACY", "STANDARD"]
    bgpInterRegionCost: typing.Literal["ADD_COST_TO_MED", "DEFAULT"]
    effectiveBgpAlwaysCompareMed: bool
    effectiveBgpInterRegionCost: typing.Literal["ADD_COST_TO_MED", "DEFAULT"]
    routingMode: typing.Literal["GLOBAL", "REGIONAL"]

@typing.type_check_only
class NetworksAddPeeringRequest(typing.TypedDict, total=False):
    autoCreateRoutes: bool
    exportCustomRoutes: bool
    importCustomRoutes: bool
    name: str
    networkPeering: NetworkPeering
    peerNetwork: str

@typing.type_check_only
class NetworksCancelRequestRemovePeeringRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponse(typing.TypedDict, total=False):
    firewallPolicys: _list[NetworksGetEffectiveFirewallsResponseEffectiveFirewallPolicy]
    firewalls: _list[Firewall]
    organizationFirewalls: _list[
        NetworksGetEffectiveFirewallsResponseOrganizationFirewallPolicy
    ]

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    priority: int
    rules: _list[FirewallPolicyRule]
    shortName: str
    type: typing.Literal["HIERARCHY", "NETWORK", "SYSTEM", "UNSPECIFIED"]

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseOrganizationFirewallPolicy(
    typing.TypedDict, total=False
):
    id: str
    rules: _list[SecurityPolicyRule]

@typing.type_check_only
class NetworksRemovePeeringRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class NetworksRequestRemovePeeringRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class NetworksUpdatePeeringRequest(typing.TypedDict, total=False):
    networkPeering: NetworkPeering

@typing.type_check_only
class NodeGroup(typing.TypedDict, total=False):
    autoscalingPolicy: NodeGroupAutoscalingPolicy
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    locationHint: str
    maintenanceInterval: typing.Literal["AS_NEEDED", "PERIODIC", "RECURRENT"]
    maintenancePolicy: typing.Literal[
        "DEFAULT",
        "MAINTENANCE_POLICY_UNSPECIFIED",
        "MIGRATE_WITHIN_NODE_GROUP",
        "RESTART_IN_PLACE",
    ]
    maintenanceWindow: NodeGroupMaintenanceWindow
    name: str
    nodeTemplate: str
    selfLink: str
    selfLinkWithId: str
    shareSettings: ShareSettings
    size: int
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY"]
    zone: str

@typing.type_check_only
class NodeGroupAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupAutoscalingPolicy(typing.TypedDict, total=False):
    maxNodes: int
    minNodes: int
    mode: typing.Literal["MODE_UNSPECIFIED", "OFF", "ON", "ONLY_SCALE_OUT"]

@typing.type_check_only
class NodeGroupList(typing.TypedDict, total=False):
    id: str
    items: _list[NodeGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupMaintenanceWindow(typing.TypedDict, total=False):
    duration: str
    maintenanceDuration: Duration
    startTime: str

@typing.type_check_only
class NodeGroupNode(typing.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    consumedResources: InstanceConsumptionInfo
    cpuOvercommitType: typing.Literal[
        "CPU_OVERCOMMIT_TYPE_UNSPECIFIED", "ENABLED", "NONE"
    ]
    disks: _list[LocalDisk]
    instanceConsumptionData: _list[InstanceConsumptionData]
    instances: _list[str]
    name: str
    nodeType: str
    satisfiesPzs: bool
    serverBinding: ServerBinding
    serverId: str
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY", "REPAIRING"]
    totalResources: InstanceConsumptionInfo
    upcomingMaintenance: UpcomingMaintenance

@typing.type_check_only
class NodeGroupsAddNodesRequest(typing.TypedDict, total=False):
    additionalNodeCount: int

@typing.type_check_only
class NodeGroupsDeleteNodesRequest(typing.TypedDict, total=False):
    nodes: _list[str]

@typing.type_check_only
class NodeGroupsListNodes(typing.TypedDict, total=False):
    id: str
    items: _list[NodeGroupNode]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupsPerformMaintenanceRequest(typing.TypedDict, total=False):
    nodes: _list[str]
    startTime: str

@typing.type_check_only
class NodeGroupsScopedList(typing.TypedDict, total=False):
    nodeGroups: _list[NodeGroup]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupsSetNodeTemplateRequest(typing.TypedDict, total=False):
    nodeTemplate: str

@typing.type_check_only
class NodeGroupsSimulateMaintenanceEventRequest(typing.TypedDict, total=False):
    nodes: _list[str]

@typing.type_check_only
class NodeTemplate(typing.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    cpuOvercommitType: typing.Literal[
        "CPU_OVERCOMMIT_TYPE_UNSPECIFIED", "ENABLED", "NONE"
    ]
    creationTimestamp: str
    description: str
    disks: _list[LocalDisk]
    id: str
    kind: str
    name: str
    nodeAffinityLabels: dict[str, typing.Any]
    nodeType: str
    nodeTypeFlexibility: NodeTemplateNodeTypeFlexibility
    region: str
    selfLink: str
    selfLinkWithId: str
    serverBinding: ServerBinding
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY"]
    statusMessage: str

@typing.type_check_only
class NodeTemplateAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTemplateList(typing.TypedDict, total=False):
    id: str
    items: _list[NodeTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTemplateNodeTypeFlexibility(typing.TypedDict, total=False):
    cpus: str
    localSsd: str
    memory: str

@typing.type_check_only
class NodeTemplatesScopedList(typing.TypedDict, total=False):
    nodeTemplates: _list[NodeTemplate]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeType(typing.TypedDict, total=False):
    cpuPlatform: str
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    guestCpus: int
    id: str
    kind: str
    localSsdGb: int
    maxVms: int
    memoryMb: int
    name: str
    selfLink: str
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class NodeTypeAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTypeList(typing.TypedDict, total=False):
    id: str
    items: _list[NodeType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTypesScopedList(typing.TypedDict, total=False):
    nodeTypes: _list[NodeType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NotificationEndpoint(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    grpcSettings: NotificationEndpointGrpcSettings
    id: str
    kind: str
    name: str
    region: str
    selfLink: str

@typing.type_check_only
class NotificationEndpointAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NotificationEndpointGrpcSettings(typing.TypedDict, total=False):
    authority: str
    endpoint: str
    payloadName: str
    resendInterval: Duration
    retryDurationSec: int

@typing.type_check_only
class NotificationEndpointList(typing.TypedDict, total=False):
    id: str
    items: _list[NotificationEndpoint]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NotificationEndpointsScopedList(typing.TypedDict, total=False):
    resources: _list[NotificationEndpoint]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: dict[str, typing.Any]
    firewallPolicyRuleOperationMetadata: FirewallPolicyRuleOperationMetadata
    getHealthOperationMetadata: GetHealthOperationMetadata
    getVersionOperationMetadata: GetVersionOperationMetadata
    httpErrorMessage: str
    httpErrorStatusCode: int
    id: str
    insertTime: str
    instancesBulkInsertOperationMetadata: InstancesBulkInsertOperationMetadata
    kind: str
    name: str
    operationGroupId: str
    operationType: str
    progress: int
    region: str
    selfLink: str
    selfLinkWithId: str
    setCommonInstanceMetadataOperationMetadata: (
        SetCommonInstanceMetadataOperationMetadata
    )
    startTime: str
    status: typing.Literal["DONE", "PENDING", "RUNNING"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: _list[dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class OperationList(typing.TypedDict, total=False):
    id: str
    items: _list[Operation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class OperationsScopedList(typing.TypedDict, total=False):
    operations: _list[Operation]
    warning: dict[str, typing.Any]

@typing.type_check_only
class OrganizationRolloutsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[Rollout]
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class OrganizationSecurityPoliciesListAssociationsResponse(
    typing.TypedDict, total=False
):
    associations: _list[SecurityPolicyAssociation]
    kind: str

@typing.type_check_only
class OrganizationVmExtensionPolicyAggregatedListResponse(
    typing.TypedDict, total=False
):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class OriginAuthenticationMethod(typing.TypedDict, total=False):
    jwt: Jwt

@typing.type_check_only
class OutlierDetection(typing.TypedDict, total=False):
    baseEjectionTime: Duration
    consecutiveErrors: int
    consecutiveGatewayFailure: int
    enforcingConsecutiveErrors: int
    enforcingConsecutiveGatewayFailure: int
    enforcingSuccessRate: int
    interval: Duration
    maxEjectionPercent: int
    successRateMinimumHosts: int
    successRateRequestVolume: int
    successRateStdevFactor: int

@typing.type_check_only
class PacketIntervals(typing.TypedDict, total=False):
    avgMs: str
    duration: typing.Literal["DURATION_UNSPECIFIED", "HOUR", "MAX", "MINUTE"]
    maxMs: str
    minMs: str
    numIntervals: str
    type: typing.Literal["LOOPBACK", "RECEIVE", "TRANSMIT", "TYPE_UNSPECIFIED"]

@typing.type_check_only
class PacketMirroring(typing.TypedDict, total=False):
    collectorIlb: PacketMirroringForwardingRuleInfo
    creationTimestamp: str
    description: str
    enable: typing.Literal["FALSE", "TRUE"]
    filter: PacketMirroringFilter
    id: str
    kind: str
    mirroredResources: PacketMirroringMirroredResourceInfo
    name: str
    network: PacketMirroringNetworkInfo
    priority: int
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class PacketMirroringAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PacketMirroringFilter(typing.TypedDict, total=False):
    IPProtocols: _list[str]
    cidrRanges: _list[str]
    direction: typing.Literal["BOTH", "EGRESS", "INGRESS"]

@typing.type_check_only
class PacketMirroringForwardingRuleInfo(typing.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringList(typing.TypedDict, total=False):
    id: str
    items: _list[PacketMirroring]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class PacketMirroringMirroredResourceInfo(typing.TypedDict, total=False):
    instances: _list[PacketMirroringMirroredResourceInfoInstanceInfo]
    subnetworks: _list[PacketMirroringMirroredResourceInfoSubnetInfo]
    tags: _list[str]

@typing.type_check_only
class PacketMirroringMirroredResourceInfoInstanceInfo(typing.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringMirroredResourceInfoSubnetInfo(typing.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringNetworkInfo(typing.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringsScopedList(typing.TypedDict, total=False):
    packetMirrorings: _list[PacketMirroring]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PartnerMetadata(typing.TypedDict, total=False):
    fingerprint: str
    partnerMetadata: dict[str, typing.Any]

@typing.type_check_only
class PathMatcher(typing.TypedDict, total=False):
    defaultCustomErrorResponsePolicy: CustomErrorResponsePolicy
    defaultRouteAction: HttpRouteAction
    defaultService: str
    defaultUrlRedirect: HttpRedirectAction
    description: str
    headerAction: HttpHeaderAction
    name: str
    pathRules: _list[PathRule]
    routeRules: _list[HttpRouteRule]

@typing.type_check_only
class PathRule(typing.TypedDict, total=False):
    customErrorResponsePolicy: CustomErrorResponsePolicy
    paths: _list[str]
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

@typing.type_check_only
class PeerAuthenticationMethod(typing.TypedDict, total=False):
    mtls: MutualTls

@typing.type_check_only
class PerInstanceConfig(typing.TypedDict, total=False):
    fingerprint: str
    name: str
    preservedState: PreservedState
    status: typing.Literal[
        "APPLYING", "DELETING", "EFFECTIVE", "NONE", "UNAPPLIED", "UNAPPLIED_DELETION"
    ]

@typing.type_check_only
class PeriodicPartialMaintenanceSchedule(typing.TypedDict, total=False):
    subType: typing.Literal[
        "MAINTENANCE_SUBTYPE_UNSPECIFIED",
        "MAINTENANCE_TYPE_CUSTOMER_MAINTENANCE",
        "MAINTENANCE_TYPE_DISRUPTIVE_UPGRADE",
        "MAINTENANCE_TYPE_STABLE",
        "MAINTENANCE_TYPE_TRANSITION",
    ]
    targetResource: str
    type: typing.Literal["MAINTENANCE_TYPE_UNSPECIFIED", "PRIVATE_ZONE_MAINTENANCE"]
    windowEndTime: DateTime
    windowStartTime: DateTime

@typing.type_check_only
class Permission(typing.TypedDict, total=False):
    constraints: _list[PermissionConstraint]
    hosts: _list[str]
    methods: _list[str]
    notHosts: _list[str]
    notMethods: _list[str]
    notPaths: _list[str]
    notPorts: _list[str]
    paths: _list[str]
    ports: _list[str]

@typing.type_check_only
class PermissionConstraint(typing.TypedDict, total=False):
    key: str
    values: _list[str]

@typing.type_check_only
class PersistentDiskResourceCommitment(typing.TypedDict, total=False):
    amount: str
    dimensionType: typing.Literal[
        "CAPACITY_OPTIMIZED",
        "DIMENSION_TYPE_UNSPECIFIED",
        "READ_OPTIMIZED",
        "WRITE_OPTIMIZED",
    ]
    productType: typing.Literal[
        "HYPERDISK_EXAPOOL_BALANCED",
        "HYPERDISK_EXAPOOL_THROUGHPUT",
        "PRODUCT_TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PreconfiguredWafSet(typing.TypedDict, total=False):
    expressionSets: _list[WafExpressionSet]

@typing.type_check_only
class PreservedState(typing.TypedDict, total=False):
    disks: dict[str, typing.Any]
    externalIPs: dict[str, typing.Any]
    internalIPs: dict[str, typing.Any]
    metadata: dict[str, typing.Any]

@typing.type_check_only
class PreservedStatePreservedDisk(typing.TypedDict, total=False):
    autoDelete: typing.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]
    mode: typing.Literal["READ_ONLY", "READ_WRITE"]
    source: str

@typing.type_check_only
class PreservedStatePreservedNetworkIp(typing.TypedDict, total=False):
    autoDelete: typing.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]
    ipAddress: PreservedStatePreservedNetworkIpIpAddress

@typing.type_check_only
class PreservedStatePreservedNetworkIpIpAddress(typing.TypedDict, total=False):
    address: str
    literal: str

@typing.type_check_only
class PreviewFeature(typing.TypedDict, total=False):
    activationStatus: typing.Literal[
        "ACTIVATION_STATE_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    rolloutOperation: PreviewFeatureRolloutOperation
    selfLink: str
    status: PreviewFeatureStatus

@typing.type_check_only
class PreviewFeatureList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[PreviewFeature]
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PreviewFeatureRolloutOperation(typing.TypedDict, total=False):
    rolloutInput: PreviewFeatureRolloutOperationRolloutInput

@typing.type_check_only
class PreviewFeatureRolloutOperationRolloutInput(typing.TypedDict, total=False):
    name: str
    predefinedRolloutPlan: typing.Literal[
        "ROLLOUT_PLAN_FAST_ROLLOUT",
        "ROLLOUT_PLAN_TWO_DAY_ROLLOUT",
        "ROLLOUT_PLAN_UNSPECIFIED",
    ]

@typing.type_check_only
class PreviewFeatureStatus(typing.TypedDict, total=False):
    description: str
    helpLink: str
    releaseStatus: PreviewFeatureStatusReleaseStatus

@typing.type_check_only
class PreviewFeatureStatusReleaseStatus(typing.TypedDict, total=False):
    stage: typing.Literal["DEPRECATED", "GA", "PREVIEW", "STAGE_UNSPECIFIED"]
    updateDate: Date

@typing.type_check_only
class Principal(typing.TypedDict, total=False):
    condition: str
    groups: _list[str]
    ips: _list[str]
    namespaces: _list[str]
    notGroups: _list[str]
    notIps: _list[str]
    notNamespaces: _list[str]
    notUsers: _list[str]
    properties: dict[str, typing.Any]
    users: _list[str]

@typing.type_check_only
class Project(typing.TypedDict, total=False):
    cloudArmorTier: typing.Literal[
        "CA_ENTERPRISE_ANNUAL", "CA_ENTERPRISE_PAYGO", "CA_STANDARD"
    ]
    commonInstanceMetadata: Metadata
    creationTimestamp: str
    defaultNetworkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    defaultServiceAccount: str
    description: str
    enabledFeatures: _list[str]
    id: str
    kind: str
    managedProtectionTier: typing.Literal[
        "CAMP_PLUS_ANNUAL", "CAMP_PLUS_PAYGO", "CA_STANDARD"
    ]
    name: str
    quotas: _list[Quota]
    selfLink: str
    usageExportLocation: UsageExportLocation
    vmDnsSetting: typing.Literal[
        "GLOBAL_DEFAULT", "UNSPECIFIED_VM_DNS_SETTING", "ZONAL_DEFAULT", "ZONAL_ONLY"
    ]
    xpnProjectStatus: typing.Literal["HOST", "UNSPECIFIED_XPN_PROJECT_STATUS"]

@typing.type_check_only
class ProjectView(typing.TypedDict, total=False):
    project: Project

@typing.type_check_only
class ProjectsDisableXpnResourceRequest(typing.TypedDict, total=False):
    xpnResource: XpnResourceId

@typing.type_check_only
class ProjectsEnableXpnResourceRequest(typing.TypedDict, total=False):
    xpnResource: XpnResourceId

@typing.type_check_only
class ProjectsGetXpnResources(typing.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[XpnResourceId]

@typing.type_check_only
class ProjectsListXpnHostsRequest(typing.TypedDict, total=False):
    organization: str
    returnPartialPage: bool

@typing.type_check_only
class ProjectsSetCloudArmorTierRequest(typing.TypedDict, total=False):
    cloudArmorTier: typing.Literal[
        "CA_ENTERPRISE_ANNUAL", "CA_ENTERPRISE_PAYGO", "CA_STANDARD"
    ]

@typing.type_check_only
class ProjectsSetDefaultNetworkTierRequest(typing.TypedDict, total=False):
    networkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]

@typing.type_check_only
class ProjectsSetDefaultServiceAccountRequest(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class ProjectsSetManagedProtectionTierRequest(typing.TypedDict, total=False):
    managedProtectionTier: typing.Literal[
        "CAMP_PLUS_ANNUAL", "CAMP_PLUS_PAYGO", "CA_STANDARD"
    ]

@typing.type_check_only
class PublicAdvertisedPrefix(typing.TypedDict, total=False):
    byoipApiVersion: typing.Literal["V1", "V2"]
    creationTimestamp: str
    description: str
    dnsVerificationIp: str
    fingerprint: str
    id: str
    ipCidrRange: str
    ipv6AccessType: typing.Literal["EXTERNAL", "INTERNAL"]
    kind: str
    name: str
    networkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    pdpScope: typing.Literal["GLOBAL", "GLOBAL_AND_REGIONAL", "REGIONAL"]
    publicDelegatedPrefixs: _list[PublicAdvertisedPrefixPublicDelegatedPrefix]
    selfLink: str
    selfLinkWithId: str
    sharedSecret: str
    status: typing.Literal[
        "ANNOUNCED_TO_INTERNET",
        "INITIAL",
        "PREFIX_CONFIGURATION_COMPLETE",
        "PREFIX_CONFIGURATION_IN_PROGRESS",
        "PREFIX_REMOVAL_IN_PROGRESS",
        "PTR_CONFIGURED",
        "READY_TO_ANNOUNCE",
        "REVERSE_DNS_LOOKUP_FAILED",
        "VALIDATED",
    ]

@typing.type_check_only
class PublicAdvertisedPrefixList(typing.TypedDict, total=False):
    id: str
    items: _list[PublicAdvertisedPrefix]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class PublicAdvertisedPrefixPublicDelegatedPrefix(typing.TypedDict, total=False):
    ipRange: str
    name: str
    project: str
    region: str
    status: str

@typing.type_check_only
class PublicDelegatedPrefix(typing.TypedDict, total=False):
    allocatablePrefixLength: int
    byoipApiVersion: typing.Literal["V1", "V2"]
    creationTimestamp: str
    description: str
    enableEnhancedIpv4Allocation: bool
    fingerprint: str
    id: str
    ipCidrRange: str
    ipv6AccessType: typing.Literal["EXTERNAL", "INTERNAL"]
    isLiveMigration: bool
    kind: str
    mode: typing.Literal[
        "DELEGATION",
        "EXTERNAL_IPV6_FORWARDING_RULE_CREATION",
        "EXTERNAL_IPV6_SUBNETWORK_CREATION",
        "INTERNAL_IPV6_SUBNETWORK_CREATION",
    ]
    name: str
    networkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    parentPrefix: str
    publicDelegatedSubPrefixs: _list[PublicDelegatedPrefixPublicDelegatedSubPrefix]
    purpose: typing.Literal[
        "APPLICATION_AND_PROXY_LOAD_BALANCERS",
        "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0",
        "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1",
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal[
        "ACTIVE",
        "ANNOUNCED",
        "ANNOUNCED_TO_GOOGLE",
        "ANNOUNCED_TO_INTERNET",
        "DELETING",
        "INITIALIZING",
        "READY_TO_ANNOUNCE",
    ]

@typing.type_check_only
class PublicDelegatedPrefixAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PublicDelegatedPrefixList(typing.TypedDict, total=False):
    id: str
    items: _list[PublicDelegatedPrefix]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class PublicDelegatedPrefixPublicDelegatedSubPrefix(typing.TypedDict, total=False):
    allocatablePrefixLength: int
    delegateeProject: str
    description: str
    enableEnhancedIpv4Allocation: bool
    ipCidrRange: str
    ipv6AccessType: typing.Literal["EXTERNAL", "INTERNAL"]
    isAddress: bool
    mode: typing.Literal[
        "DELEGATION",
        "EXTERNAL_IPV6_FORWARDING_RULE_CREATION",
        "EXTERNAL_IPV6_SUBNETWORK_CREATION",
        "INTERNAL_IPV6_SUBNETWORK_CREATION",
    ]
    name: str
    purpose: typing.Literal[
        "APPLICATION_AND_PROXY_LOAD_BALANCERS",
        "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0",
        "PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1",
    ]
    region: str
    status: typing.Literal["ACTIVE", "INACTIVE"]

@typing.type_check_only
class PublicDelegatedPrefixesScopedList(typing.TypedDict, total=False):
    publicDelegatedPrefixes: _list[PublicDelegatedPrefix]
    warning: dict[str, typing.Any]

@typing.type_check_only
class QueuedResource(typing.TypedDict, total=False):
    bulkInsertInstanceResource: BulkInsertInstanceResource
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    queuingPolicy: QueuingPolicy
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal[
        "ACCEPTED",
        "CANCELLED",
        "CREATING",
        "DELETING",
        "FAILED",
        "PROVISIONING",
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
    ]
    status: QueuedResourceStatus
    zone: str

@typing.type_check_only
class QueuedResourceList(typing.TypedDict, total=False):
    id: str
    items: _list[QueuedResource]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class QueuedResourceStatus(typing.TypedDict, total=False):
    failedData: QueuedResourceStatusFailedData
    provisioningOperations: _list[str]
    queuingPolicy: QueuingPolicy

@typing.type_check_only
class QueuedResourceStatusFailedData(typing.TypedDict, total=False):
    error: dict[str, typing.Any]

@typing.type_check_only
class QueuedResourcesAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class QueuedResourcesScopedList(typing.TypedDict, total=False):
    queuedResources: _list[QueuedResource]
    warning: dict[str, typing.Any]

@typing.type_check_only
class QueuingPolicy(typing.TypedDict, total=False):
    validUntilDuration: Duration
    validUntilTime: str

@typing.type_check_only
class Quota(typing.TypedDict, total=False):
    limit: float
    metric: typing.Literal[
        "A2_CPUS",
        "AFFINITY_GROUPS",
        "AMD_S9300_GPUS",
        "AUTOSCALERS",
        "BACKEND_BUCKETS",
        "BACKEND_SERVICES",
        "C2D_CPUS",
        "C2_CPUS",
        "C3_CPUS",
        "COMMITMENTS",
        "COMMITTED_A2_CPUS",
        "COMMITTED_C2D_CPUS",
        "COMMITTED_C2_CPUS",
        "COMMITTED_C3_CPUS",
        "COMMITTED_CPUS",
        "COMMITTED_E2_CPUS",
        "COMMITTED_LICENSES",
        "COMMITTED_LOCAL_SSD_TOTAL_GB",
        "COMMITTED_M3_CPUS",
        "COMMITTED_MEMORY_OPTIMIZED_CPUS",
        "COMMITTED_N2A_CPUS",
        "COMMITTED_N2D_CPUS",
        "COMMITTED_N2_CPUS",
        "COMMITTED_NVIDIA_A100_80GB_GPUS",
        "COMMITTED_NVIDIA_A100_GPUS",
        "COMMITTED_NVIDIA_H100_GPUS",
        "COMMITTED_NVIDIA_K80_GPUS",
        "COMMITTED_NVIDIA_L4_GPUS",
        "COMMITTED_NVIDIA_P100_GPUS",
        "COMMITTED_NVIDIA_P4_GPUS",
        "COMMITTED_NVIDIA_T4_GPUS",
        "COMMITTED_NVIDIA_V100_GPUS",
        "COMMITTED_T2A_CPUS",
        "COMMITTED_T2D_CPUS",
        "COMMITTED_Z3_CPUS",
        "CPUS",
        "CPUS_ALL_REGIONS",
        "DISKS_TOTAL_GB",
        "E2_CPUS",
        "EXTERNAL_MANAGED_FORWARDING_RULES",
        "EXTERNAL_NETWORK_LB_FORWARDING_RULES",
        "EXTERNAL_PROTOCOL_FORWARDING_RULES",
        "EXTERNAL_VPN_GATEWAYS",
        "FIREWALLS",
        "FORWARDING_RULES",
        "GLOBAL_EXTERNAL_MANAGED_BACKEND_SERVICES",
        "GLOBAL_EXTERNAL_MANAGED_FORWARDING_RULES",
        "GLOBAL_EXTERNAL_PROXY_LB_BACKEND_SERVICES",
        "GLOBAL_INTERNAL_ADDRESSES",
        "GLOBAL_INTERNAL_MANAGED_BACKEND_SERVICES",
        "GLOBAL_INTERNAL_TRAFFIC_DIRECTOR_BACKEND_SERVICES",
        "GPUS_ALL_REGIONS",
        "HDB_TOTAL_GB",
        "HDB_TOTAL_IOPS",
        "HDB_TOTAL_THROUGHPUT",
        "HEALTH_CHECKS",
        "IMAGES",
        "INSTANCES",
        "INSTANCE_GROUPS",
        "INSTANCE_GROUP_MANAGERS",
        "INSTANCE_TEMPLATES",
        "INTERCONNECTS",
        "INTERCONNECT_ATTACHMENTS_PER_REGION",
        "INTERCONNECT_ATTACHMENTS_TOTAL_MBPS",
        "INTERCONNECT_TOTAL_GBPS",
        "INTERNAL_ADDRESSES",
        "INTERNAL_TRAFFIC_DIRECTOR_FORWARDING_RULES",
        "IN_PLACE_SNAPSHOTS",
        "IN_USE_ADDRESSES",
        "IN_USE_BACKUP_SCHEDULES",
        "IN_USE_MAINTENANCE_WINDOWS",
        "IN_USE_SNAPSHOT_SCHEDULES",
        "LOCAL_SSD_TOTAL_GB",
        "M1_CPUS",
        "M2_CPUS",
        "M3_CPUS",
        "MACHINE_IMAGES",
        "N2A_CPUS",
        "N2D_CPUS",
        "N2_CPUS",
        "NETWORKS",
        "NETWORK_ATTACHMENTS",
        "NETWORK_ENDPOINT_GROUPS",
        "NETWORK_FIREWALL_POLICIES",
        "NET_LB_SECURITY_POLICIES_PER_REGION",
        "NET_LB_SECURITY_POLICY_RULES_PER_REGION",
        "NET_LB_SECURITY_POLICY_RULE_ATTRIBUTES_PER_REGION",
        "NODE_GROUPS",
        "NODE_TEMPLATES",
        "NVIDIA_A100_80GB_GPUS",
        "NVIDIA_A100_GPUS",
        "NVIDIA_K80_GPUS",
        "NVIDIA_L4_GPUS",
        "NVIDIA_P100_GPUS",
        "NVIDIA_P100_VWS_GPUS",
        "NVIDIA_P4_GPUS",
        "NVIDIA_P4_VWS_GPUS",
        "NVIDIA_T4_GPUS",
        "NVIDIA_T4_VWS_GPUS",
        "NVIDIA_V100_GPUS",
        "PACKET_MIRRORINGS",
        "PD_EXTREME_TOTAL_PROVISIONED_IOPS",
        "PREEMPTIBLE_CPUS",
        "PREEMPTIBLE_LOCAL_SSD_GB",
        "PREEMPTIBLE_NVIDIA_A100_80GB_GPUS",
        "PREEMPTIBLE_NVIDIA_A100_GPUS",
        "PREEMPTIBLE_NVIDIA_H100_GPUS",
        "PREEMPTIBLE_NVIDIA_K80_GPUS",
        "PREEMPTIBLE_NVIDIA_L4_GPUS",
        "PREEMPTIBLE_NVIDIA_P100_GPUS",
        "PREEMPTIBLE_NVIDIA_P100_VWS_GPUS",
        "PREEMPTIBLE_NVIDIA_P4_GPUS",
        "PREEMPTIBLE_NVIDIA_P4_VWS_GPUS",
        "PREEMPTIBLE_NVIDIA_T4_GPUS",
        "PREEMPTIBLE_NVIDIA_T4_VWS_GPUS",
        "PREEMPTIBLE_NVIDIA_V100_GPUS",
        "PREEMPTIBLE_TPU_LITE_DEVICE_V4",
        "PREEMPTIBLE_TPU_LITE_DEVICE_V5",
        "PREEMPTIBLE_TPU_LITE_PODSLICE_V5",
        "PREEMPTIBLE_TPU_PODSLICE_V4",
        "PRIVATE_V6_ACCESS_SUBNETWORKS",
        "PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK",
        "PSC_INTERNAL_LB_FORWARDING_RULES",
        "PUBLIC_ADVERTISED_PREFIXES",
        "PUBLIC_DELEGATED_PREFIXES",
        "QUEUED_RESOURCES",
        "REGIONAL_AUTOSCALERS",
        "REGIONAL_EXTERNAL_MANAGED_BACKEND_SERVICES",
        "REGIONAL_EXTERNAL_NETWORK_LB_BACKEND_SERVICES",
        "REGIONAL_INSTANCE_GROUP_MANAGERS",
        "REGIONAL_INTERNAL_LB_BACKEND_SERVICES",
        "REGIONAL_INTERNAL_MANAGED_BACKEND_SERVICES",
        "REGIONAL_INTERNAL_TRAFFIC_DIRECTOR_BACKEND_SERVICES",
        "REGION_EXTERNAL_MANAGED_BACKEND_BUCKETS",
        "REGION_INTERNAL_MANAGED_BACKEND_BUCKETS",
        "RESERVATIONS",
        "RESOURCE_POLICIES",
        "ROUTERS",
        "ROUTES",
        "SECURITY_POLICIES",
        "SECURITY_POLICIES_PER_REGION",
        "SECURITY_POLICY_ADVANCED_RULES_PER_REGION",
        "SECURITY_POLICY_CEVAL_RULES",
        "SECURITY_POLICY_RULES",
        "SECURITY_POLICY_RULES_PER_REGION",
        "SERVICE_ATTACHMENTS",
        "SNAPSHOTS",
        "SSD_TOTAL_GB",
        "SSL_CERTIFICATES",
        "SSL_POLICIES",
        "STATIC_ADDRESSES",
        "STATIC_BYOIP_ADDRESSES",
        "STATIC_EXTERNAL_IPV6_ADDRESS_RANGES",
        "SUBNETWORKS",
        "T2A_CPUS",
        "T2D_CPUS",
        "TARGET_HTTPS_PROXIES",
        "TARGET_HTTP_PROXIES",
        "TARGET_INSTANCES",
        "TARGET_POOLS",
        "TARGET_SSL_PROXIES",
        "TARGET_TCP_PROXIES",
        "TARGET_VPN_GATEWAYS",
        "TPU_LITE_DEVICE_V4",
        "TPU_LITE_DEVICE_V5",
        "TPU_LITE_PODSLICE_V5",
        "TPU_PODSLICE_V4",
        "URL_MAPS",
        "VARIABLE_IPV6_PUBLIC_DELEGATED_PREFIXES",
        "VPN_GATEWAYS",
        "VPN_TUNNELS",
        "XPN_SERVICE_PROJECTS",
    ]
    owner: str
    usage: float

@typing.type_check_only
class QuotaExceededInfo(typing.TypedDict, total=False):
    dimensions: dict[str, typing.Any]
    futureLimit: float
    limit: float
    limitName: str
    metricName: str
    rolloutStatus: typing.Literal["IN_PROGRESS", "ROLLOUT_STATUS_UNSPECIFIED"]

@typing.type_check_only
class RbacPolicy(typing.TypedDict, total=False):
    name: str
    permissions: _list[Permission]
    principals: _list[Principal]

@typing.type_check_only
class RecoverableSnapshot(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    originalResource: RecoverableSnapshotOriginalSnapshot
    purgeTimestamp: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RECOVERING", "UNKNOWN"
    ]

@typing.type_check_only
class RecoverableSnapshotAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RecoverableSnapshotList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[RecoverableSnapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RecoverableSnapshotOriginalSnapshot(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    autoCreated: bool
    chainName: str
    creationSizeBytes: str
    creationTimestamp: str
    deletionTimestamp: str
    description: str
    diskSizeGb: str
    downloadBytes: str
    enableConfidentialCompute: bool
    guestOsFeatures: _list[GuestOsFeature]
    id: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    licenseCodes: _list[str]
    licenses: _list[str]
    maxRetentionDays: int
    name: str
    region: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    snapshotEncryptionKey: CustomerEncryptionKey
    snapshotGroupId: str
    snapshotGroupName: str
    snapshotType: typing.Literal["ARCHIVE", "STANDARD"]
    sourceDisk: str
    sourceDiskEncryptionKey: CustomerEncryptionKey
    sourceDiskForRecoveryCheckpoint: str
    sourceDiskId: str
    sourceInstantSnapshot: str
    sourceInstantSnapshotEncryptionKey: CustomerEncryptionKey
    sourceInstantSnapshotId: str
    sourceSnapshotSchedulePolicy: str
    sourceSnapshotSchedulePolicyId: str
    storageBytes: str
    storageBytesStatus: typing.Literal["UPDATING", "UP_TO_DATE"]
    storageLocations: _list[str]

@typing.type_check_only
class RecoverableSnapshotsScopedList(typing.TypedDict, total=False):
    recoverablesnapshots: _list[RecoverableSnapshot]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Reference(typing.TypedDict, total=False):
    kind: str
    referenceType: str
    referrer: str
    target: str

@typing.type_check_only
class RegexRewrite(typing.TypedDict, total=False):
    pathPattern: str
    pathSubstitution: str

@typing.type_check_only
class Region(typing.TypedDict, total=False):
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    quotaStatusWarning: dict[str, typing.Any]
    quotas: _list[Quota]
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal["DOWN", "UP"]
    supportsPzs: bool
    zones: _list[str]

@typing.type_check_only
class RegionAddressesMoveRequest(typing.TypedDict, total=False):
    description: str
    destinationAddress: str

@typing.type_check_only
class RegionAddressesUpdatePublicPtrRequest(typing.TypedDict, total=False):
    ptrDomainName: str
    ptrDomainNameTtl: int

@typing.type_check_only
class RegionAutoscalerList(typing.TypedDict, total=False):
    id: str
    items: _list[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionCommitmentsUpdateReservationsRequest(typing.TypedDict, total=False):
    reservations: _list[Reservation]

@typing.type_check_only
class RegionDiskTypeList(typing.TypedDict, total=False):
    id: str
    items: _list[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionDiskUpdateKmsKeyRequest(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class RegionDisksAddResourcePoliciesRequest(typing.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class RegionDisksRemoveResourcePoliciesRequest(typing.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class RegionDisksResizeRequest(typing.TypedDict, total=False):
    sizeGb: str

@typing.type_check_only
class RegionDisksStartAsyncReplicationRequest(typing.TypedDict, total=False):
    asyncSecondaryDisk: str

@typing.type_check_only
class RegionInstanceGroupList(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerDeleteInstanceConfigReq(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagerList(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerPatchInstanceConfigReq(typing.TypedDict, total=False):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagerResizeRequestsListResponse(
    typing.TypedDict, total=False
):
    etag: str
    id: str
    items: _list[InstanceGroupManagerResizeRequest]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerUpdateInstanceConfigReq(typing.TypedDict, total=False):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersAbandonInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersAdoptInstancesRequest(typing.TypedDict, total=False):
    instances: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersApplyUpdatesRequest(typing.TypedDict, total=False):
    allInstances: bool
    allowedActions: _list[
        typing.Literal["NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"]
    ]
    disruptionMode: typing.Literal["LEGACY", "OPTIMIZED"]
    instances: _list[str]
    maximalAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]
    minimalAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]
    mostDisruptiveAllowedAction: typing.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART", "RESTART_IN_PLACE"
    ]

@typing.type_check_only
class RegionInstanceGroupManagersCreateInstancesRequest(typing.TypedDict, total=False):
    instances: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersDeleteInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]
    skipInstancesOnValidationError: bool

@typing.type_check_only
class RegionInstanceGroupManagersListErrorsResponse(typing.TypedDict, total=False):
    items: _list[InstanceManagedByIgmError]
    nextPageToken: str

@typing.type_check_only
class RegionInstanceGroupManagersListInstanceConfigsResp(typing.TypedDict, total=False):
    items: _list[PerInstanceConfig]
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagersListInstancesResponse(typing.TypedDict, total=False):
    managedInstances: _list[ManagedInstance]
    nextPageToken: str

@typing.type_check_only
class RegionInstanceGroupManagersRecreateRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersResizeAdvancedRequest(typing.TypedDict, total=False):
    noCreationRetries: bool
    scaleInProtection: bool
    targetSize: int

@typing.type_check_only
class RegionInstanceGroupManagersResumeInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersSetAutoHealingRequest(typing.TypedDict, total=False):
    autoHealingPolicies: _list[InstanceGroupManagerAutoHealingPolicy]

@typing.type_check_only
class RegionInstanceGroupManagersSetTargetPoolsRequest(typing.TypedDict, total=False):
    fingerprint: str
    targetPools: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersSetTemplateRequest(typing.TypedDict, total=False):
    instanceTemplate: str

@typing.type_check_only
class RegionInstanceGroupManagersStartInstancesRequest(typing.TypedDict, total=False):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersStopInstancesRequest(typing.TypedDict, total=False):
    forceStop: bool
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersSuspendInstancesRequest(typing.TypedDict, total=False):
    forceSuspend: bool
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupsListInstances(typing.TypedDict, total=False):
    id: str
    items: _list[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupsListInstancesRequest(typing.TypedDict, total=False):
    instanceState: typing.Literal["ALL", "RUNNING"]
    portName: str

@typing.type_check_only
class RegionInstanceGroupsSetNamedPortsRequest(typing.TypedDict, total=False):
    fingerprint: str
    namedPorts: _list[NamedPort]

@typing.type_check_only
class RegionList(typing.TypedDict, total=False):
    id: str
    items: _list[Region]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionNetworkEndpointGroupsAttachEndpointsRequest(typing.TypedDict, total=False):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class RegionNetworkEndpointGroupsDetachEndpointsRequest(typing.TypedDict, total=False):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse(
    typing.TypedDict, total=False
):
    firewallPolicys: _list[
        RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponseEffectiveFirewallPolicy
    ]
    firewalls: _list[Firewall]

@typing.type_check_only
class RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing.TypedDict, total=False
):
    displayName: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    priority: int
    rules: _list[FirewallPolicyRule]
    type: typing.Literal[
        "HIERARCHY",
        "NETWORK",
        "NETWORK_REGIONAL",
        "SYSTEM_GLOBAL",
        "SYSTEM_REGIONAL",
        "UNSPECIFIED",
    ]

@typing.type_check_only
class RegionSetLabelsRequest(typing.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class RegionSetPolicyRequest(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class RegionSnapshotUpdateKmsKeyRequest(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class RegionTargetHttpsProxiesSetSslCertificatesRequest(typing.TypedDict, total=False):
    sslCertificates: _list[str]

@typing.type_check_only
class RegionUrlMapsValidateRequest(typing.TypedDict, total=False):
    resource: UrlMap

@typing.type_check_only
class RegionWaitForReplicationCatchUpRequest(typing.TypedDict, total=False):
    maxWaitDuration: str

@typing.type_check_only
class ReliabilityRisk(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    details: RiskDetails
    id: str
    kind: str
    name: str
    recommendation: RiskRecommendation
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class ReliabilityRisksListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[ReliabilityRisk]
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReplicationDetails(typing.TypedDict, total=False):
    lastReplicationTime: str
    secondsSinceLastReplication: str

@typing.type_check_only
class ReplicationDiskPair(typing.TypedDict, total=False):
    primaryDisk: str
    secondaryDisk: str

@typing.type_check_only
class RequestMirrorPolicy(typing.TypedDict, total=False):
    backendService: str
    mirrorPercent: float

@typing.type_check_only
class Reservation(typing.TypedDict, total=False):
    advancedDeploymentControl: ReservationAdvancedDeploymentControl
    aggregateReservation: AllocationAggregateReservation
    commitment: str
    confidentialComputeType: typing.Literal[
        "CONFIDENTIAL_COMPUTE_TYPE_TDX", "CONFIDENTIAL_COMPUTE_TYPE_UNSPECIFIED"
    ]
    creationTimestamp: str
    deleteAfterDuration: Duration
    deleteAtTime: str
    deploymentType: typing.Literal["DENSE", "DEPLOYMENT_TYPE_UNSPECIFIED", "FLEXIBLE"]
    description: str
    earlyAccessMaintenance: typing.Literal["NO_EARLY_ACCESS", "WAVE1", "WAVE2"]
    enableEmergentMaintenance: bool
    id: str
    kind: str
    linkedCommitments: _list[str]
    name: str
    params: ReservationParams
    protectionTier: typing.Literal[
        "CAPACITY_OPTIMIZED", "PROTECTION_TIER_UNSPECIFIED", "STANDARD"
    ]
    reservationMode: typing.Literal[
        "CALENDAR", "DEFAULT", "RESERVATION_MODE_UNSPECIFIED"
    ]
    reservationSharingPolicy: AllocationReservationSharingPolicy
    resourcePolicies: dict[str, typing.Any]
    resourceStatus: AllocationResourceStatus
    satisfiesPzs: bool
    schedulingType: typing.Literal[
        "GROUPED", "GROUP_MAINTENANCE_TYPE_UNSPECIFIED", "INDEPENDENT"
    ]
    selfLink: str
    selfLinkWithId: str
    shareSettings: ShareSettings
    specificReservation: AllocationSpecificSKUReservation
    specificReservationRequired: bool
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY", "UPDATING"]
    zone: str

@typing.type_check_only
class ReservationAdvancedDeploymentControl(typing.TypedDict, total=False):
    reservationOperationalMode: typing.Literal[
        "ALL_CAPACITY",
        "HIGHLY_AVAILABLE_CAPACITY",
        "RESERVATION_OPERATIONAL_MODE_UNSPECIFIED",
    ]

@typing.type_check_only
class ReservationAffinity(typing.TypedDict, total=False):
    consumeReservationType: typing.Literal[
        "ANY_RESERVATION",
        "ANY_RESERVATION_THEN_FAIL",
        "NO_RESERVATION",
        "SPECIFIC_RESERVATION",
        "SPECIFIC_THEN_ANY_RESERVATION",
        "SPECIFIC_THEN_NO_RESERVATION",
        "UNSPECIFIED",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ReservationAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationBlock(typing.TypedDict, total=False):
    count: int
    creationTimestamp: str
    healthInfo: ReservationBlockHealthInfo
    id: str
    inUseCount: int
    inUseHostCount: int
    kind: str
    locationPrefix: str
    name: str
    physicalTopology: ReservationBlockPhysicalTopology
    reservationMaintenance: GroupMaintenanceInfo
    reservationSubBlockCount: int
    reservationSubBlockInUseCount: int
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY"]
    zone: str

@typing.type_check_only
class ReservationBlockHealthInfo(typing.TypedDict, total=False):
    degradedSubBlockCount: int
    healthStatus: typing.Literal["DEGRADED", "HEALTHY", "HEALTH_STATUS_UNSPECIFIED"]
    healthySubBlockCount: int

@typing.type_check_only
class ReservationBlockPhysicalTopology(typing.TypedDict, total=False):
    block: str
    cluster: str
    instances: _list[ReservationBlockPhysicalTopologyInstance]

@typing.type_check_only
class ReservationBlockPhysicalTopologyInstance(typing.TypedDict, total=False):
    instanceId: str
    physicalHostTopology: ReservationBlockPhysicalTopologyInstancePhysicalHostTopology
    projectId: str

@typing.type_check_only
class ReservationBlockPhysicalTopologyInstancePhysicalHostTopology(
    typing.TypedDict, total=False
):
    host: str
    subBlock: str

@typing.type_check_only
class ReservationBlocksGetResponse(typing.TypedDict, total=False):
    resource: ReservationBlock

@typing.type_check_only
class ReservationBlocksListResponse(typing.TypedDict, total=False):
    id: str
    items: _list[ReservationBlock]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationConsumedInstance(typing.TypedDict, total=False):
    instance: str
    service: str
    status: ReservationConsumedInstanceStatus

@typing.type_check_only
class ReservationConsumedInstanceStatus(typing.TypedDict, total=False):
    linkageErrors: dict[str, typing.Any]

@typing.type_check_only
class ReservationConsumedInstancesListResponse(typing.TypedDict, total=False):
    id: str
    items: _list[ReservationConsumedInstance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationList(typing.TypedDict, total=False):
    id: str
    items: _list[Reservation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class ReservationSlot(typing.TypedDict, total=False):
    creationTimestamp: str
    id: str
    kind: str
    name: str
    physicalTopology: ReservationSlotPhysicalTopology
    selfLink: str
    selfLinkWithId: str
    shareSettings: ShareSettings
    state: typing.Literal[
        "ACTIVE", "CREATING", "DELETING", "STATE_UNSPECIFIED", "UNAVAILABLE"
    ]
    status: ReservationSlotStatus
    zone: str

@typing.type_check_only
class ReservationSlotPhysicalTopology(typing.TypedDict, total=False):
    block: str
    cluster: str
    host: str
    subBlock: str

@typing.type_check_only
class ReservationSlotStatus(typing.TypedDict, total=False):
    physicalTopology: ReservationSlotPhysicalTopology
    rdmaIpAddresses: _list[str]
    runningInstances: _list[str]

@typing.type_check_only
class ReservationSlotsGetResponse(typing.TypedDict, total=False):
    resource: ReservationSlot

@typing.type_check_only
class ReservationSlotsGetVersionRequest(typing.TypedDict, total=False):
    sbomSelections: _list[
        typing.Literal[
            "SBOM_SELECTION_CURRENT",
            "SBOM_SELECTION_TARGET",
            "SBOM_SELECTION_UNSPECIFIED",
        ]
    ]

@typing.type_check_only
class ReservationSlotsListResponse(typing.TypedDict, total=False):
    id: str
    items: _list[ReservationSlot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationSubBlock(typing.TypedDict, total=False):
    acceleratorTopologiesInfo: AcceleratorTopologiesInfo
    count: int
    creationTimestamp: str
    healthInfo: ReservationSubBlockHealthInfo
    id: str
    inUseCount: int
    inUseHostCount: int
    kind: str
    name: str
    physicalTopology: ReservationSubBlockPhysicalTopology
    reservationSubBlockMaintenance: GroupMaintenanceInfo
    retentionPriority: int
    selfLink: str
    selfLinkWithId: str
    status: typing.Literal["CREATING", "DELETING", "INVALID", "READY", "UPDATING"]
    zone: str

@typing.type_check_only
class ReservationSubBlockHealthInfo(typing.TypedDict, total=False):
    degradedHostCount: int
    degradedInfraCount: int
    healthStatus: typing.Literal["DEGRADED", "HEALTHY", "HEALTH_STATUS_UNSPECIFIED"]
    healthyHostCount: int
    healthyInfraCount: int

@typing.type_check_only
class ReservationSubBlockPhysicalTopology(typing.TypedDict, total=False):
    block: str
    cluster: str
    subBlock: str

@typing.type_check_only
class ReservationSubBlocksGetResponse(typing.TypedDict, total=False):
    resource: ReservationSubBlock

@typing.type_check_only
class ReservationSubBlocksGetVersionRequest(typing.TypedDict, total=False):
    sbomSelections: _list[
        typing.Literal[
            "SBOM_SELECTION_CURRENT",
            "SBOM_SELECTION_TARGET",
            "SBOM_SELECTION_UNSPECIFIED",
        ]
    ]

@typing.type_check_only
class ReservationSubBlocksListResponse(typing.TypedDict, total=False):
    id: str
    items: _list[ReservationSubBlock]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationSubBlocksReportFaultyRequest(typing.TypedDict, total=False):
    disruptionSchedule: typing.Literal["DISRUPTION_SCHEDULE_UNSPECIFIED", "IMMEDIATE"]
    failureComponent: typing.Literal[
        "FAILURE_COMPONENT_UNSPECIFIED", "MULTIPLE_FAULTY_HOSTS", "NVLINK_SWITCH"
    ]
    faultReasons: _list[ReservationSubBlocksReportFaultyRequestFaultReason]

@typing.type_check_only
class ReservationSubBlocksReportFaultyRequestFaultReason(typing.TypedDict, total=False):
    behavior: typing.Literal[
        "FAULT_BEHAVIOR_UNSPECIFIED",
        "GPU_ERROR",
        "NVSWITCH_FAULT_CONTROLLER_ERROR",
        "NVSWITCH_FAULT_DEGRADED_BANDWIDTH",
        "NVSWITCH_FAULT_SWITCH_ERROR",
        "PERFORMANCE",
        "SILENT_DATA_CORRUPTION",
        "SWITCH_FAILURE",
    ]
    description: str

@typing.type_check_only
class ReservationsBlocksPerformMaintenanceRequest(typing.TypedDict, total=False):
    maintenanceScope: typing.Literal[
        "ALL", "MAINTENANCE_SCOPE_UNSPECIFIED", "RUNNING_VMS", "UNUSED_CAPACITY"
    ]

@typing.type_check_only
class ReservationsPerformMaintenanceRequest(typing.TypedDict, total=False):
    maintenanceScope: typing.Literal[
        "ALL", "MAINTENANCE_SCOPE_UNSPECIFIED", "RUNNING_VMS", "UNUSED_CAPACITY"
    ]

@typing.type_check_only
class ReservationsResizeRequest(typing.TypedDict, total=False):
    specificSkuCount: str

@typing.type_check_only
class ReservationsScopedList(typing.TypedDict, total=False):
    reservations: _list[Reservation]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourceCommitment(typing.TypedDict, total=False):
    acceleratorType: str
    amount: str
    type: typing.Literal["ACCELERATOR", "LOCAL_SSD", "MEMORY", "UNSPECIFIED", "VCPU"]

@typing.type_check_only
class ResourceGroupReference(typing.TypedDict, total=False):
    group: str

@typing.type_check_only
class ResourcePoliciesScopedList(typing.TypedDict, total=False):
    resourcePolicies: _list[ResourcePolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    diskConsistencyGroupPolicy: ResourcePolicyDiskConsistencyGroupPolicy
    groupPlacementPolicy: ResourcePolicyGroupPlacementPolicy
    id: str
    instanceSchedulePolicy: ResourcePolicyInstanceSchedulePolicy
    kind: str
    name: str
    region: str
    resourceStatus: ResourcePolicyResourceStatus
    selfLink: str
    selfLinkWithId: str
    snapshotSchedulePolicy: ResourcePolicySnapshotSchedulePolicy
    status: typing.Literal["CREATING", "DELETING", "EXPIRED", "INVALID", "READY"]
    vmMaintenancePolicy: ResourcePolicyVmMaintenancePolicy
    workloadPolicy: ResourcePolicyWorkloadPolicy

@typing.type_check_only
class ResourcePolicyAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicyDailyCycle(typing.TypedDict, total=False):
    daysInCycle: int
    duration: str
    startTime: str

@typing.type_check_only
class ResourcePolicyDiskConsistencyGroupPolicy(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResourcePolicyGroupPlacementPolicy(typing.TypedDict, total=False):
    acceleratorTopologyMode: typing.Literal["AUTO_CONNECT", "PROVISION_ONLY"]
    availabilityDomainCount: int
    collocation: typing.Literal[
        "CLUSTERED", "COLLOCATED", "MAX_SPREAD", "UNSPECIFIED_COLLOCATION"
    ]
    gpuTopology: str
    maxDistance: int
    scope: typing.Literal["HOST", "UNSPECIFIED_SCOPE"]
    sliceCount: int
    tpuTopology: str
    vmCount: int

@typing.type_check_only
class ResourcePolicyHourlyCycle(typing.TypedDict, total=False):
    duration: str
    hoursInCycle: int
    startTime: str

@typing.type_check_only
class ResourcePolicyInstanceSchedulePolicy(typing.TypedDict, total=False):
    expirationTime: str
    startTime: str
    timeZone: str
    vmStartSchedule: ResourcePolicyInstanceSchedulePolicySchedule
    vmStopSchedule: ResourcePolicyInstanceSchedulePolicySchedule

@typing.type_check_only
class ResourcePolicyInstanceSchedulePolicySchedule(typing.TypedDict, total=False):
    schedule: str

@typing.type_check_only
class ResourcePolicyList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[ResourcePolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicyResourceStatus(typing.TypedDict, total=False):
    instanceSchedulePolicy: ResourcePolicyResourceStatusInstanceSchedulePolicyStatus

@typing.type_check_only
class ResourcePolicyResourceStatusInstanceSchedulePolicyStatus(
    typing.TypedDict, total=False
):
    lastRunStartTime: str
    nextRunStartTime: str

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicy(typing.TypedDict, total=False):
    retentionPolicy: ResourcePolicySnapshotSchedulePolicyRetentionPolicy
    schedule: ResourcePolicySnapshotSchedulePolicySchedule
    snapshotProperties: ResourcePolicySnapshotSchedulePolicySnapshotProperties

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicyRetentionPolicy(
    typing.TypedDict, total=False
):
    maxRetentionDays: int
    onPolicySwitch: typing.Literal[
        "DO_NOT_RETROACTIVELY_APPLY",
        "RETROACTIVELY_APPLY",
        "UNSPECIFIED_ON_POLICY_SWITCH",
    ]
    onSourceDiskDelete: typing.Literal[
        "APPLY_RETENTION_POLICY",
        "KEEP_AUTO_SNAPSHOTS",
        "UNSPECIFIED_ON_SOURCE_DISK_DELETE",
    ]

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicySchedule(typing.TypedDict, total=False):
    dailySchedule: ResourcePolicyDailyCycle
    hourlySchedule: ResourcePolicyHourlyCycle
    weeklySchedule: ResourcePolicyWeeklyCycle

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicySnapshotProperties(
    typing.TypedDict, total=False
):
    chainName: str
    guestFlush: bool
    labels: dict[str, typing.Any]
    region: str
    storageLocations: _list[str]

@typing.type_check_only
class ResourcePolicyVmMaintenancePolicy(typing.TypedDict, total=False):
    concurrencyControlGroup: ResourcePolicyVmMaintenancePolicyConcurrencyControl
    maintenanceWindow: ResourcePolicyVmMaintenancePolicyMaintenanceWindow

@typing.type_check_only
class ResourcePolicyVmMaintenancePolicyConcurrencyControl(
    typing.TypedDict, total=False
):
    concurrencyLimit: int

@typing.type_check_only
class ResourcePolicyVmMaintenancePolicyMaintenanceWindow(typing.TypedDict, total=False):
    dailyMaintenanceWindow: ResourcePolicyDailyCycle

@typing.type_check_only
class ResourcePolicyWeeklyCycle(typing.TypedDict, total=False):
    dayOfWeeks: _list[ResourcePolicyWeeklyCycleDayOfWeek]

@typing.type_check_only
class ResourcePolicyWeeklyCycleDayOfWeek(typing.TypedDict, total=False):
    day: typing.Literal[
        "FRIDAY",
        "INVALID",
        "MONDAY",
        "SATURDAY",
        "SUNDAY",
        "THURSDAY",
        "TUESDAY",
        "WEDNESDAY",
    ]
    duration: str
    startTime: str

@typing.type_check_only
class ResourcePolicyWorkloadPolicy(typing.TypedDict, total=False):
    acceleratorTopology: str
    acceleratorTopologyMode: typing.Literal["AUTO_CONNECT", "PROVISION_ONLY"]
    maxTopologyDistance: typing.Literal["BLOCK", "CLUSTER", "SUBBLOCK"]
    type: typing.Literal["HIGH_AVAILABILITY", "HIGH_THROUGHPUT"]

@typing.type_check_only
class ResourceStatus(typing.TypedDict, total=False):
    acceleratorStatus: _list[ResourceStatusAcceleratorStatus]
    consumedReservation: str
    consumedReservationBlock: str
    effectiveInstanceMetadata: ResourceStatusEffectiveInstanceMetadata
    lastInstanceTerminationDetails: ResourceStatusLastInstanceTerminationDetails
    physicalHost: str
    physicalHostTopology: ResourceStatusPhysicalHostTopology
    reservationConsumptionInfo: ResourceStatusReservationConsumptionInfo
    scheduling: ResourceStatusScheduling
    serviceIntegrationStatuses: dict[str, typing.Any]
    shutdownDetails: ResourceStatusShutdownDetails
    upcomingMaintenance: UpcomingMaintenance

@typing.type_check_only
class ResourceStatusAcceleratorStatus(typing.TypedDict, total=False):
    passedScans: _list[ResourceStatusAcceleratorStatusPassedScan]
    recommendedScans: _list[ResourceStatusAcceleratorStatusRecommendedScan]
    serialNumber: str
    uuid: str

@typing.type_check_only
class ResourceStatusAcceleratorStatusPassedScan(typing.TypedDict, total=False):
    endTime: str
    name: str
    startTime: str
    version: str

@typing.type_check_only
class ResourceStatusAcceleratorStatusRecommendedScan(typing.TypedDict, total=False):
    estimatedDuration: Duration
    name: str
    version: str

@typing.type_check_only
class ResourceStatusEffectiveInstanceMetadata(typing.TypedDict, total=False):
    blockProjectSshKeysMetadataValue: bool
    enableGuestAttributesMetadataValue: bool
    enableOsInventoryMetadataValue: bool
    enableOsconfigMetadataValue: bool
    enableOsloginMetadataValue: bool
    gceContainerDeclarationMetadataValue: bool
    serialPortEnableMetadataValue: bool
    serialPortLoggingEnableMetadataValue: bool
    vmDnsSettingMetadataValue: str

@typing.type_check_only
class ResourceStatusLastInstanceTerminationDetails(typing.TypedDict, total=False):
    terminationReason: typing.Literal[
        "BAD_BILLING_ACCOUNT",
        "CLOUD_ABUSE_DETECTED",
        "DISK_ERROR",
        "FREE_TRIAL_EXPIRED",
        "INSTANCE_UPDATE_REQUIRED_RESTART",
        "INTERNAL_ERROR",
        "KMS_REJECTION",
        "MANAGED_INSTANCE_GROUP",
        "OS_TERMINATED",
        "PREEMPTED",
        "SCHEDULED_STOP",
        "SHUTDOWN_DUE_TO_HOST_ERROR",
        "SHUTDOWN_DUE_TO_MAINTENANCE",
        "SHUTDOWN_DUE_TO_SHEDDING_EVENT",
        "USER_TERMINATED",
    ]

@typing.type_check_only
class ResourceStatusPhysicalHostTopology(typing.TypedDict, total=False):
    additionalAttributes: ResourceStatusPhysicalHostTopologyAdditionalAttributes
    block: str
    cluster: str
    host: str
    subblock: str

@typing.type_check_only
class ResourceStatusPhysicalHostTopologyAdditionalAttributes(
    typing.TypedDict, total=False
):
    acceleratorTopologyIds: dict[str, typing.Any]
    networkTopologyIds: dict[str, typing.Any]

@typing.type_check_only
class ResourceStatusReservationConsumptionInfo(typing.TypedDict, total=False):
    consumedReservation: str
    consumedReservationBlock: str
    consumedReservationSubBlock: str

@typing.type_check_only
class ResourceStatusScheduling(typing.TypedDict, total=False):
    availabilityDomain: int
    gracefulShutdownTimestamp: str
    terminationTimestamp: str

@typing.type_check_only
class ResourceStatusServiceIntegrationStatus(typing.TypedDict, total=False):
    backupDr: ResourceStatusServiceIntegrationStatusBackupDRStatus

@typing.type_check_only
class ResourceStatusServiceIntegrationStatusBackupDRStatus(
    typing.TypedDict, total=False
):
    integrationDetails: str
    state: typing.Literal[
        "ACTIVE", "CREATING", "DELETING", "FAILED", "STATE_UNSPECIFIED"
    ]

@typing.type_check_only
class ResourceStatusShutdownDetails(typing.TypedDict, total=False):
    maxDuration: Duration
    requestTimestamp: str
    stopState: typing.Literal["PENDING_STOP", "STOPPING"]
    targetState: typing.Literal["DELETED", "STOPPED"]

@typing.type_check_only
class RiskDetails(typing.TypedDict, total=False):
    duration: str
    globalDnsInsight: RiskDetailsGlobalDnsInsight
    lastUpdateTimestamp: str
    severity: typing.Literal[
        "CRITICAL", "HIGH", "LOW", "MEDIUM", "SEVERITY_UNSPECIFIED"
    ]
    type: typing.Literal["GLOBAL_DNS", "RISK_TYPE_UNSPECIFIED"]

@typing.type_check_only
class RiskDetailsGlobalDnsInsight(typing.TypedDict, total=False):
    projectDefaultIsGlobalDns: bool
    queryObservationWindow: str
    riskyQueryCount: str
    totalQueryCount: str

@typing.type_check_only
class RiskRecommendation(typing.TypedDict, total=False):
    content: str
    referenceUrl: str

@typing.type_check_only
class Rollout(typing.TypedDict, total=False):
    cancellationTime: str
    completionTime: str
    creationTimestamp: str
    currentWaveNumber: str
    description: str
    etag: str
    id: str
    kind: str
    name: str
    pauseTime: str
    resumeTime: str
    rolloutEntity: RolloutRolloutEntity
    rolloutPlan: str
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal[
        "CANCELLED",
        "CANCELLING",
        "CANCEL_FAILED",
        "COMPLETED",
        "COMPLETE_FAILED",
        "COMPLETING",
        "FAILED",
        "PAUSED",
        "PAUSE_FAILED",
        "PAUSING",
        "PROCESSING",
        "READY",
        "RESUMING",
        "ROLLBACK_WAVE_FAILED",
        "ROLLING_BACK",
        "STATE_UNSPECIFIED",
        "UNINITIALIZED",
        "WAVE_FAILED",
    ]
    waveDetails: _list[RolloutWaveDetails]

@typing.type_check_only
class RolloutPlan(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    locationScope: typing.Literal["LOCATION_SCOPE_UNSPECIFIED", "REGIONAL", "ZONAL"]
    name: str
    selfLink: str
    selfLinkWithId: str
    waves: _list[RolloutPlanWave]

@typing.type_check_only
class RolloutPlanWave(typing.TypedDict, total=False):
    displayName: str
    number: str
    orchestrationOptions: RolloutPlanWaveOrchestrationOptions
    selectors: _list[RolloutPlanWaveSelector]
    validation: RolloutPlanWaveValidation

@typing.type_check_only
class RolloutPlanWaveOrchestrationOptions(typing.TypedDict, total=False):
    delays: _list[RolloutPlanWaveOrchestrationOptionsDelay]
    maxConcurrentLocations: str
    maxConcurrentResourcesPerLocation: str

@typing.type_check_only
class RolloutPlanWaveOrchestrationOptionsDelay(typing.TypedDict, total=False):
    delimiter: typing.Literal[
        "DELIMITER_BATCH", "DELIMITER_LOCATION", "DELIMITER_UNSPECIFIED"
    ]
    duration: str
    type: typing.Literal["TYPE_MINIMUM", "TYPE_OFFSET", "TYPE_UNSPECIFIED"]

@typing.type_check_only
class RolloutPlanWaveSelector(typing.TypedDict, total=False):
    locationSelector: RolloutPlanWaveSelectorLocationSelector
    resourceHierarchySelector: RolloutPlanWaveSelectorResourceHierarchySelector

@typing.type_check_only
class RolloutPlanWaveSelectorLocationSelector(typing.TypedDict, total=False):
    includedLocations: _list[str]

@typing.type_check_only
class RolloutPlanWaveSelectorResourceHierarchySelector(typing.TypedDict, total=False):
    includedFolders: _list[str]
    includedOrganizations: _list[str]
    includedProjects: _list[str]

@typing.type_check_only
class RolloutPlanWaveValidation(typing.TypedDict, total=False):
    timeBasedValidationMetadata: RolloutPlanWaveValidationTimeBasedValidationMetadata
    type: str

@typing.type_check_only
class RolloutPlanWaveValidationTimeBasedValidationMetadata(
    typing.TypedDict, total=False
):
    waitDuration: str

@typing.type_check_only
class RolloutPlansListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[RolloutPlan]
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RolloutPolicy(typing.TypedDict, total=False):
    defaultRolloutTime: str
    locationRolloutPolicies: dict[str, typing.Any]

@typing.type_check_only
class RolloutRolloutEntity(typing.TypedDict, total=False):
    orchestratedEntity: RolloutRolloutEntityOrchestratedEntity

@typing.type_check_only
class RolloutRolloutEntityOrchestratedEntity(typing.TypedDict, total=False):
    conflictBehavior: str
    orchestrationAction: str
    orchestrationSource: str

@typing.type_check_only
class RolloutWaveDetails(typing.TypedDict, total=False):
    orchestratedWaveDetails: RolloutWaveDetailsOrchestratedWaveDetails
    waveDisplayName: str
    waveNumber: str

@typing.type_check_only
class RolloutWaveDetailsOrchestratedWaveDetails(typing.TypedDict, total=False):
    completedResourcesCount: str
    estimatedCompletionTime: str
    estimatedTotalResourcesCount: str
    failedLocations: _list[str]
    failedResourcesCount: str
    locationStatus: dict[str, typing.Any]

@typing.type_check_only
class RolloutWaveDetailsOrchestratedWaveDetailsLocationStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal[
        "STATE_FAILED",
        "STATE_IN_PROGRESS",
        "STATE_PENDING",
        "STATE_SKIPPED",
        "STATE_SUCCEEDED",
        "STATE_UNSPECIFIED",
    ]

@typing.type_check_only
class RolloutsListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[Rollout]
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Route(typing.TypedDict, total=False):
    allowConflictingSubnetworks: bool
    asPaths: _list[RouteAsPath]
    creationTimestamp: str
    description: str
    destRange: str
    id: str
    ilbRouteBehaviorOnUnhealthy: typing.Literal[
        "DO_NOT_WITHDRAW_ROUTE_IF_ILB_UNHEALTHY", "WITHDRAW_ROUTE_IF_ILB_UNHEALTHY"
    ]
    kind: str
    name: str
    network: str
    nextHopGateway: str
    nextHopHub: str
    nextHopIlb: str
    nextHopInstance: str
    nextHopInterRegionCost: int
    nextHopInterconnectAttachment: str
    nextHopIp: str
    nextHopMed: int
    nextHopNetwork: str
    nextHopOrigin: typing.Literal["EGP", "IGP", "INCOMPLETE"]
    nextHopPeering: str
    nextHopVpnTunnel: str
    params: RouteParams
    priority: int
    routeStatus: typing.Literal[
        "ACTIVE",
        "DROPPED",
        "INACTIVE",
        "OVERRIDDEN_BY_HUB",
        "OVERRIDDEN_BY_PEERING",
        "PENDING",
    ]
    routeType: typing.Literal["BGP", "STATIC", "SUBNET", "TRANSIT"]
    selfLink: str
    selfLinkWithId: str
    tags: _list[str]
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class RouteAsPath(typing.TypedDict, total=False):
    asLists: _list[int]
    pathSegmentType: typing.Literal[
        "AS_CONFED_SEQUENCE", "AS_CONFED_SET", "AS_SEQUENCE", "AS_SET"
    ]

@typing.type_check_only
class RouteList(typing.TypedDict, total=False):
    id: str
    items: _list[Route]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RouteParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class RoutePolicy(typing.TypedDict, total=False):
    description: str
    fingerprint: str
    name: str
    terms: _list[RoutePolicyPolicyTerm]
    type: typing.Literal["ROUTE_POLICY_TYPE_EXPORT", "ROUTE_POLICY_TYPE_IMPORT"]

@typing.type_check_only
class RoutePolicyPolicyTerm(typing.TypedDict, total=False):
    actions: _list[Expr]
    match: Expr
    priority: int

@typing.type_check_only
class Router(typing.TypedDict, total=False):
    bgp: RouterBgp
    bgpPeers: _list[RouterBgpPeer]
    creationTimestamp: str
    description: str
    encryptedInterconnectRouter: bool
    etag: str
    id: str
    interfaces: _list[RouterInterface]
    kind: str
    md5AuthenticationKeys: _list[RouterMd5AuthenticationKey]
    name: str
    nats: _list[RouterNat]
    nccGateway: str
    network: str
    params: RouterParams
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class RouterAdvertisedIpRange(typing.TypedDict, total=False):
    description: str
    range: str

@typing.type_check_only
class RouterAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RouterBgp(typing.TypedDict, total=False):
    advertiseMode: typing.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: _list[
        typing.Literal["ALL_PEER_VPC_SUBNETS", "ALL_SUBNETS", "ALL_VPC_SUBNETS"]
    ]
    advertisedIpRanges: _list[RouterAdvertisedIpRange]
    asn: int
    identifierRange: str
    keepaliveInterval: int

@typing.type_check_only
class RouterBgpPeer(typing.TypedDict, total=False):
    advertiseMode: typing.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: _list[
        typing.Literal["ALL_PEER_VPC_SUBNETS", "ALL_SUBNETS", "ALL_VPC_SUBNETS"]
    ]
    advertisedIpRanges: _list[RouterAdvertisedIpRange]
    advertisedRoutePriority: int
    bfd: RouterBgpPeerBfd
    customLearnedIpRanges: _list[RouterBgpPeerCustomLearnedIpRange]
    customLearnedRoutePriority: int
    enable: typing.Literal["FALSE", "TRUE"]
    enableIpv4: bool
    enableIpv6: bool
    exportPolicies: _list[str]
    importPolicies: _list[str]
    interfaceName: str
    ipAddress: str
    ipv4NexthopAddress: str
    ipv6NexthopAddress: str
    linkedCustomHardware: str
    managementType: typing.Literal["MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"]
    md5AuthenticationKeyName: str
    name: str
    peerAsn: int
    peerIpAddress: str
    peerIpv4NexthopAddress: str
    peerIpv6NexthopAddress: str
    routerApplianceInstance: str

@typing.type_check_only
class RouterBgpPeerBfd(typing.TypedDict, total=False):
    minReceiveInterval: int
    minTransmitInterval: int
    mode: typing.Literal["ACTIVE", "DISABLED", "PASSIVE"]
    multiplier: int
    packetMode: typing.Literal["CONTROL_AND_ECHO", "CONTROL_ONLY"]
    sessionInitializationMode: typing.Literal["ACTIVE", "DISABLED", "PASSIVE"]
    slowTimerInterval: int

@typing.type_check_only
class RouterBgpPeerCustomLearnedIpRange(typing.TypedDict, total=False):
    range: str

@typing.type_check_only
class RouterInterface(typing.TypedDict, total=False):
    ipRange: str
    ipVersion: typing.Literal["IPV4", "IPV6"]
    linkedInterconnectAttachment: str
    linkedVpnTunnel: str
    managementType: typing.Literal["MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"]
    name: str
    privateIpAddress: str
    redundantInterface: str
    subnetwork: str

@typing.type_check_only
class RouterList(typing.TypedDict, total=False):
    id: str
    items: _list[Router]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RouterMd5AuthenticationKey(typing.TypedDict, total=False):
    key: str
    name: str

@typing.type_check_only
class RouterNat(typing.TypedDict, total=False):
    autoNetworkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    drainNatIps: _list[str]
    effectiveTcpTimeWaitTimeoutSec: int
    enableDynamicPortAllocation: bool
    enableEndpointIndependentMapping: bool
    endpointTypes: _list[
        typing.Literal[
            "ENDPOINT_TYPE_MANAGED_PROXY_LB", "ENDPOINT_TYPE_SWG", "ENDPOINT_TYPE_VM"
        ]
    ]
    icmpIdleTimeoutSec: int
    logConfig: RouterNatLogConfig
    maxPortsPerVm: int
    minPortsPerVm: int
    name: str
    nat64Subnetworks: _list[RouterNatSubnetworkToNat64]
    natIpAllocateOption: typing.Literal["AUTO_ONLY", "MANUAL_ONLY"]
    natIps: _list[str]
    rules: _list[RouterNatRule]
    sourceSubnetworkIpRangesToNat: typing.Literal[
        "ALL_SUBNETWORKS_ALL_IP_RANGES",
        "ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES",
        "LIST_OF_SUBNETWORKS",
    ]
    sourceSubnetworkIpRangesToNat64: typing.Literal[
        "ALL_IPV6_SUBNETWORKS", "LIST_OF_IPV6_SUBNETWORKS"
    ]
    subnetworks: _list[RouterNatSubnetworkToNat]
    tcpEstablishedIdleTimeoutSec: int
    tcpTimeWaitTimeoutSec: int
    tcpTransitoryIdleTimeoutSec: int
    type: typing.Literal["PRIVATE", "PUBLIC"]
    udpIdleTimeoutSec: int

@typing.type_check_only
class RouterNatLogConfig(typing.TypedDict, total=False):
    enable: bool
    filter: typing.Literal["ALL", "ERRORS_ONLY", "TRANSLATIONS_ONLY"]

@typing.type_check_only
class RouterNatRule(typing.TypedDict, total=False):
    action: RouterNatRuleAction
    description: str
    match: str
    ruleNumber: int
    sourceWorkloadIdentities: _list[str]

@typing.type_check_only
class RouterNatRuleAction(typing.TypedDict, total=False):
    sourceNatActiveIps: _list[str]
    sourceNatActiveRanges: _list[str]
    sourceNatDrainIps: _list[str]
    sourceNatDrainRanges: _list[str]

@typing.type_check_only
class RouterNatSubnetworkToNat(typing.TypedDict, total=False):
    name: str
    secondaryIpRangeNames: _list[str]
    sourceIpRangesToNat: _list[
        typing.Literal[
            "ALL_IP_RANGES", "LIST_OF_SECONDARY_IP_RANGES", "PRIMARY_IP_RANGE"
        ]
    ]

@typing.type_check_only
class RouterNatSubnetworkToNat64(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class RouterParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class RouterStatus(typing.TypedDict, total=False):
    bestRoutes: _list[Route]
    bestRoutesForRouter: _list[Route]
    bgpPeerStatus: _list[RouterStatusBgpPeerStatus]
    natStatus: _list[RouterStatusNatStatus]
    nccGateway: str
    network: str

@typing.type_check_only
class RouterStatusBgpPeerStatus(typing.TypedDict, total=False):
    advertisedRoutes: _list[Route]
    bfdStatus: BfdStatus
    depreferenced: bool
    enableIpv4: bool
    enableIpv6: bool
    ipAddress: str
    ipv4NexthopAddress: str
    ipv6NexthopAddress: str
    linkedCustomHardware: str
    linkedVpnTunnel: str
    md5AuthEnabled: bool
    name: str
    numLearnedRoutes: int
    peerIpAddress: str
    peerIpv4NexthopAddress: str
    peerIpv6NexthopAddress: str
    routerApplianceInstance: str
    state: str
    status: typing.Literal["DOWN", "UNKNOWN", "UP"]
    statusReason: typing.Literal[
        "IPV4_PEER_ON_IPV6_ONLY_CONNECTION",
        "IPV6_PEER_ON_IPV4_ONLY_CONNECTION",
        "MD5_AUTH_INTERNAL_PROBLEM",
        "STATUS_REASON_UNSPECIFIED",
    ]
    uptime: str
    uptimeSeconds: str

@typing.type_check_only
class RouterStatusNatStatus(typing.TypedDict, total=False):
    autoAllocatedNatIps: _list[str]
    drainAutoAllocatedNatIps: _list[str]
    drainUserAllocatedNatIps: _list[str]
    minExtraNatIpsNeeded: int
    name: str
    numVmEndpointsWithNatMappings: int
    ruleStatus: _list[RouterStatusNatStatusNatRuleStatus]
    userAllocatedNatIpResources: _list[str]
    userAllocatedNatIps: _list[str]

@typing.type_check_only
class RouterStatusNatStatusNatRuleStatus(typing.TypedDict, total=False):
    activeNatIps: _list[str]
    drainNatIps: _list[str]
    minExtraIpsNeeded: int
    numVmEndpointsWithNatMappings: int
    ruleNumber: int

@typing.type_check_only
class RouterStatusResponse(typing.TypedDict, total=False):
    kind: str
    result: RouterStatus

@typing.type_check_only
class RoutersGetNamedSetResponse(typing.TypedDict, total=False):
    etag: str
    resource: NamedSet

@typing.type_check_only
class RoutersGetRoutePolicyResponse(typing.TypedDict, total=False):
    etag: str
    resource: RoutePolicy

@typing.type_check_only
class RoutersListBgpRoutes(typing.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    nextPageToken: str
    result: _list[BgpRoute]
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RoutersListNamedSets(typing.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    nextPageToken: str
    result: _list[NamedSet]
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RoutersListRoutePolicies(typing.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    nextPageToken: str
    result: _list[RoutePolicy]
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RoutersPreviewResponse(typing.TypedDict, total=False):
    resource: Router

@typing.type_check_only
class RoutersScopedList(typing.TypedDict, total=False):
    routers: _list[Router]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SSLHealthCheck(typing.TypedDict, total=False):
    port: int
    portName: str
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    request: str
    response: str

@typing.type_check_only
class SavedAttachedDisk(typing.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    diskType: str
    guestOsFeatures: _list[GuestOsFeature]
    index: int
    interface: typing.Literal["NVDIMM", "NVME", "SCSI"]
    kind: str
    licenses: _list[str]
    mode: typing.Literal["READ_ONLY", "READ_WRITE"]
    source: str
    storageBytes: str
    storageBytesStatus: typing.Literal["UPDATING", "UP_TO_DATE"]
    type: typing.Literal["PERSISTENT", "SCRATCH"]

@typing.type_check_only
class SavedDisk(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    kind: str
    sourceDisk: str
    storageBytes: str
    storageBytesStatus: typing.Literal["UPDATING", "UP_TO_DATE"]

@typing.type_check_only
class ScalingScheduleStatus(typing.TypedDict, total=False):
    lastStartTime: str
    nextStartTime: str
    state: typing.Literal["ACTIVE", "DISABLED", "OBSOLETE", "READY"]

@typing.type_check_only
class Scheduling(typing.TypedDict, total=False):
    automaticRestart: bool
    availabilityDomain: int
    currentCpus: int
    currentMemoryMb: str
    exposeHostTopology: bool
    gracefulShutdown: SchedulingGracefulShutdown
    hostErrorTimeoutSeconds: int
    instanceTerminationAction: typing.Literal[
        "DELETE", "INSTANCE_TERMINATION_ACTION_UNSPECIFIED", "STOP"
    ]
    latencyTolerant: bool
    localSsdRecoveryTimeout: Duration
    locationHint: str
    maintenanceFreezeDurationHours: int
    maintenanceInterval: typing.Literal["AS_NEEDED", "PERIODIC", "RECURRENT"]
    maxRunDuration: Duration
    minNodeCpus: int
    nodeAffinities: _list[SchedulingNodeAffinity]
    onHostMaintenance: typing.Literal["MIGRATE", "TERMINATE"]
    onInstanceStopAction: SchedulingOnInstanceStopAction
    preemptible: bool
    preemptionNoticeDuration: Duration
    provisioningModel: typing.Literal[
        "FLEX_START", "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]
    shutdownTimeout: Duration
    skipGuestOsShutdown: bool
    terminationTime: str
    vsockMode: SchedulingVsockMode
    windowsLicenseOptimizationMode: typing.Literal[
        "AUTO",
        "BALANCED",
        "COST_OPTIMIZED",
        "MANAGED",
        "OFF",
        "PERFORMANCE",
        "UNSPECIFIED",
    ]

@typing.type_check_only
class SchedulingGracefulShutdown(typing.TypedDict, total=False):
    enabled: bool
    maxDuration: Duration

@typing.type_check_only
class SchedulingNodeAffinity(typing.TypedDict, total=False):
    key: str
    operator: typing.Literal["IN", "NOT_IN", "OPERATOR_UNSPECIFIED"]
    values: _list[str]

@typing.type_check_only
class SchedulingOnInstanceStopAction(typing.TypedDict, total=False):
    discardLocalSsd: bool

@typing.type_check_only
class SchedulingVsockMode(typing.TypedDict, total=False):
    mode: typing.Literal["DISABLED", "ENABLED", "VSOCK_MODE_UNSPECIFIED"]

@typing.type_check_only
class Screenshot(typing.TypedDict, total=False):
    contents: str
    kind: str

@typing.type_check_only
class SdsConfig(typing.TypedDict, total=False):
    grpcServiceConfig: GrpcServiceConfig

@typing.type_check_only
class SecurityPoliciesAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SecurityPoliciesListPreconfiguredExpressionSetsResponse(
    typing.TypedDict, total=False
):
    preconfiguredExpressionSets: SecurityPoliciesWafConfig

@typing.type_check_only
class SecurityPoliciesScopedList(typing.TypedDict, total=False):
    securityPolicies: _list[SecurityPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SecurityPoliciesWafConfig(typing.TypedDict, total=False):
    wafRules: PreconfiguredWafSet

@typing.type_check_only
class SecurityPolicy(typing.TypedDict, total=False):
    adaptiveProtectionConfig: SecurityPolicyAdaptiveProtectionConfig
    advancedOptionsConfig: SecurityPolicyAdvancedOptionsConfig
    associations: _list[SecurityPolicyAssociation]
    cloudArmorConfig: SecurityPolicyCloudArmorConfig
    creationTimestamp: str
    ddosProtectionConfig: SecurityPolicyDdosProtectionConfig
    description: str
    displayName: str
    fingerprint: str
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    parent: str
    recaptchaOptionsConfig: SecurityPolicyRecaptchaOptionsConfig
    region: str
    ruleTupleCount: int
    rules: _list[SecurityPolicyRule]
    selfLink: str
    selfLinkWithId: str
    shortName: str
    type: typing.Literal[
        "CLOUD_ARMOR",
        "CLOUD_ARMOR_EDGE",
        "CLOUD_ARMOR_INTERNAL_SERVICE",
        "CLOUD_ARMOR_NETWORK",
        "FIREWALL",
    ]
    userDefinedFields: _list[SecurityPolicyUserDefinedField]

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfig(typing.TypedDict, total=False):
    autoDeployConfig: SecurityPolicyAdaptiveProtectionConfigAutoDeployConfig
    layer7DdosDefenseConfig: (
        SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig
    )

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigAutoDeployConfig(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    expirationSec: int
    impactedBaselineThreshold: float
    loadThreshold: float

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig(
    typing.TypedDict, total=False
):
    enable: bool
    ruleVisibility: typing.Literal["PREMIUM", "STANDARD"]
    thresholdConfigs: _list[
        SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigThresholdConfig
    ]

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigThresholdConfig(
    typing.TypedDict, total=False
):
    autoDeployConfidenceThreshold: float
    autoDeployExpirationSec: int
    autoDeployImpactedBaselineThreshold: float
    autoDeployLoadThreshold: float
    detectionAbsoluteQps: float
    detectionLoadThreshold: float
    detectionRelativeToBaselineQps: float
    name: str
    trafficGranularityConfigs: _list[
        SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigThresholdConfigTrafficGranularityConfig
    ]

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigThresholdConfigTrafficGranularityConfig(
    typing.TypedDict, total=False
):
    enableEachUniqueValue: bool
    type: typing.Literal["HTTP_HEADER_HOST", "HTTP_PATH", "UNSPECIFIED_TYPE"]
    value: str

@typing.type_check_only
class SecurityPolicyAdvancedOptionsConfig(typing.TypedDict, total=False):
    jsonCustomConfig: SecurityPolicyAdvancedOptionsConfigJsonCustomConfig
    jsonParsing: typing.Literal["DISABLED", "STANDARD", "STANDARD_WITH_GRAPHQL"]
    logLevel: typing.Literal["NORMAL", "VERBOSE"]
    requestBodyInspectionSize: str
    userIpRequestHeaders: _list[str]

@typing.type_check_only
class SecurityPolicyAdvancedOptionsConfigJsonCustomConfig(
    typing.TypedDict, total=False
):
    contentTypes: _list[str]

@typing.type_check_only
class SecurityPolicyAssociation(typing.TypedDict, total=False):
    attachmentId: str
    displayName: str
    excludedFolders: _list[str]
    excludedProjects: _list[str]
    name: str
    securityPolicyId: str
    shortName: str

@typing.type_check_only
class SecurityPolicyCloudArmorConfig(typing.TypedDict, total=False):
    enableMl: bool

@typing.type_check_only
class SecurityPolicyDdosProtectionConfig(typing.TypedDict, total=False):
    ddosAdaptiveProtection: typing.Literal[
        "DDOS_ADAPTIVE_PROTECTION_UNSPECIFIED",
        "DISABLED",
        "ENABLED",
        "PREVIEW",
        "UNSPECIFIED_ADAPTIVE_PROTECTION",
    ]
    ddosImpactedBaselineThreshold: float
    ddosProtection: typing.Literal["ADVANCED", "ADVANCED_PREVIEW", "STANDARD"]

@typing.type_check_only
class SecurityPolicyList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[SecurityPolicy]
    kind: str
    nextPageToken: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SecurityPolicyRecaptchaOptionsConfig(typing.TypedDict, total=False):
    redirectSiteKey: str

@typing.type_check_only
class SecurityPolicyReference(typing.TypedDict, total=False):
    securityPolicy: str

@typing.type_check_only
class SecurityPolicyRule(typing.TypedDict, total=False):
    action: str
    description: str
    direction: typing.Literal["EGRESS", "INGRESS"]
    enableLogging: bool
    headerAction: SecurityPolicyRuleHttpHeaderAction
    kind: str
    match: SecurityPolicyRuleMatcher
    networkMatch: SecurityPolicyRuleNetworkMatcher
    preconfiguredWafConfig: SecurityPolicyRulePreconfiguredWafConfig
    preview: bool
    priority: int
    rateLimitOptions: SecurityPolicyRuleRateLimitOptions
    redirectOptions: SecurityPolicyRuleRedirectOptions
    redirectTarget: str
    ruleManagedProtectionTier: typing.Literal[
        "CAMP_PLUS_ANNUAL", "CAMP_PLUS_PAYGO", "CA_STANDARD"
    ]
    ruleNumber: str
    ruleTupleCount: int
    targetResources: _list[str]
    targetServiceAccounts: _list[str]

@typing.type_check_only
class SecurityPolicyRuleHttpHeaderAction(typing.TypedDict, total=False):
    requestHeadersToAdds: _list[SecurityPolicyRuleHttpHeaderActionHttpHeaderOption]

@typing.type_check_only
class SecurityPolicyRuleHttpHeaderActionHttpHeaderOption(typing.TypedDict, total=False):
    headerName: str
    headerValue: str

@typing.type_check_only
class SecurityPolicyRuleMatcher(typing.TypedDict, total=False):
    config: SecurityPolicyRuleMatcherConfig
    expr: Expr
    exprOptions: SecurityPolicyRuleMatcherExprOptions
    versionedExpr: typing.Literal["FIREWALL", "SRC_IPS_V1"]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfig(typing.TypedDict, total=False):
    destIpRanges: _list[str]
    destPorts: _list[SecurityPolicyRuleMatcherConfigDestinationPort]
    layer4Configs: _list[SecurityPolicyRuleMatcherConfigLayer4Config]
    srcIpRanges: _list[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfigDestinationPort(typing.TypedDict, total=False):
    ipProtocol: str
    ports: _list[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfigLayer4Config(typing.TypedDict, total=False):
    ipProtocol: str
    ports: _list[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherExprOptions(typing.TypedDict, total=False):
    recaptchaOptions: SecurityPolicyRuleMatcherExprOptionsRecaptchaOptions

@typing.type_check_only
class SecurityPolicyRuleMatcherExprOptionsRecaptchaOptions(
    typing.TypedDict, total=False
):
    actionTokenSiteKeys: _list[str]
    sessionTokenSiteKeys: _list[str]

@typing.type_check_only
class SecurityPolicyRuleNetworkMatcher(typing.TypedDict, total=False):
    destIpRanges: _list[str]
    destPorts: _list[str]
    ipProtocols: _list[str]
    srcAsns: _list[int]
    srcIpRanges: _list[str]
    srcPorts: _list[str]
    srcRegionCodes: _list[str]
    userDefinedFields: _list[SecurityPolicyRuleNetworkMatcherUserDefinedFieldMatch]

@typing.type_check_only
class SecurityPolicyRuleNetworkMatcherUserDefinedFieldMatch(
    typing.TypedDict, total=False
):
    name: str
    values: _list[str]

@typing.type_check_only
class SecurityPolicyRulePreconfiguredWafConfig(typing.TypedDict, total=False):
    exclusions: _list[SecurityPolicyRulePreconfiguredWafConfigExclusion]

@typing.type_check_only
class SecurityPolicyRulePreconfiguredWafConfigExclusion(typing.TypedDict, total=False):
    requestBodiesToExclude: _list[
        SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams
    ]
    requestCookiesToExclude: _list[
        SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams
    ]
    requestHeadersToExclude: _list[
        SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams
    ]
    requestQueryParamsToExclude: _list[
        SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams
    ]
    requestUrisToExclude: _list[
        SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams
    ]
    targetRuleIds: _list[str]
    targetRuleSet: str

@typing.type_check_only
class SecurityPolicyRulePreconfiguredWafConfigExclusionFieldParams(
    typing.TypedDict, total=False
):
    op: typing.Literal["CONTAINS", "ENDS_WITH", "EQUALS", "EQUALS_ANY", "STARTS_WITH"]
    val: str

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptions(typing.TypedDict, total=False):
    banDurationSec: int
    banThreshold: SecurityPolicyRuleRateLimitOptionsThreshold
    conformAction: str
    enforceOnKey: typing.Literal[
        "ALL",
        "ALL_IPS",
        "ASN",
        "HTTP_COOKIE",
        "HTTP_HEADER",
        "HTTP_PATH",
        "IP",
        "REGION_CODE",
        "SNI",
        "TLS_JA3_FINGERPRINT",
        "TLS_JA4_FINGERPRINT",
        "USER_IP",
        "XFF_IP",
    ]
    enforceOnKeyConfigs: _list[SecurityPolicyRuleRateLimitOptionsEnforceOnKeyConfig]
    enforceOnKeyName: str
    exceedAction: str
    exceedActionRpcStatus: SecurityPolicyRuleRateLimitOptionsRpcStatus
    exceedRedirectOptions: SecurityPolicyRuleRedirectOptions
    rateLimitThreshold: SecurityPolicyRuleRateLimitOptionsThreshold

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptionsEnforceOnKeyConfig(
    typing.TypedDict, total=False
):
    enforceOnKeyName: str
    enforceOnKeyType: typing.Literal[
        "ALL",
        "ALL_IPS",
        "ASN",
        "HTTP_COOKIE",
        "HTTP_HEADER",
        "HTTP_PATH",
        "IP",
        "REGION_CODE",
        "SNI",
        "TLS_JA3_FINGERPRINT",
        "TLS_JA4_FINGERPRINT",
        "USER_IP",
        "XFF_IP",
    ]

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptionsRpcStatus(typing.TypedDict, total=False):
    code: int
    message: str

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptionsThreshold(typing.TypedDict, total=False):
    count: int
    intervalSec: int

@typing.type_check_only
class SecurityPolicyRuleRedirectOptions(typing.TypedDict, total=False):
    target: str
    type: typing.Literal["EXTERNAL_302", "GOOGLE_RECAPTCHA"]

@typing.type_check_only
class SecurityPolicyUserDefinedField(typing.TypedDict, total=False):
    base: typing.Literal["IPV4", "IPV6", "TCP", "UDP"]
    mask: str
    name: str
    offset: int
    size: int

@typing.type_check_only
class SecuritySettings(typing.TypedDict, total=False):
    authentication: str
    authenticationPolicy: AuthenticationPolicy
    authorizationConfig: AuthorizationConfig
    awsV4Authentication: AWSV4Signature
    clientTlsPolicy: str
    clientTlsSettings: ClientTlsSettings
    subjectAltNames: _list[str]

@typing.type_check_only
class SerialPortOutput(typing.TypedDict, total=False):
    contents: str
    kind: str
    next: str
    selfLink: str
    start: str

@typing.type_check_only
class ServerBinding(typing.TypedDict, total=False):
    type: typing.Literal[
        "RESTART_NODE_ON_ANY_SERVER",
        "RESTART_NODE_ON_MINIMAL_SERVERS",
        "SERVER_BINDING_TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class ServerTlsSettings(typing.TypedDict, total=False):
    proxyTlsContext: TlsContext
    subjectAltNames: _list[str]
    tlsMode: typing.Literal["INVALID", "MUTUAL", "SIMPLE"]

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class ServiceAttachment(typing.TypedDict, total=False):
    connectedEndpoints: _list[ServiceAttachmentConnectedEndpoint]
    connectionPreference: typing.Literal[
        "ACCEPT_AUTOMATIC", "ACCEPT_MANUAL", "CONNECTION_PREFERENCE_UNSPECIFIED"
    ]
    consumerAcceptLists: _list[ServiceAttachmentConsumerProjectLimit]
    consumerRejectLists: _list[str]
    creationTimestamp: str
    description: str
    domainNames: _list[str]
    enableProxyProtocol: bool
    fingerprint: str
    id: str
    kind: str
    metadata: dict[str, typing.Any]
    name: str
    natIpsPerEndpoint: int
    natSubnets: _list[str]
    producerForwardingRule: str
    propagatedConnectionLimit: int
    pscServiceAttachmentId: Uint128
    reconcileConnections: bool
    region: str
    selfLink: str
    targetService: str
    tunnelingConfig: ServiceAttachmentTunnelingConfig

@typing.type_check_only
class ServiceAttachmentAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ServiceAttachmentConnectedEndpoint(typing.TypedDict, total=False):
    consumerNetwork: str
    endpoint: str
    endpointWithId: str
    natIps: _list[str]
    propagatedConnectionCount: int
    pscConnectionId: str
    status: typing.Literal[
        "ACCEPTED",
        "ACCEPTED_LIMITED_CAPACITY",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]

@typing.type_check_only
class ServiceAttachmentConsumerProjectLimit(typing.TypedDict, total=False):
    connectionLimit: int
    endpointUrl: str
    networkUrl: str
    projectIdOrNum: str

@typing.type_check_only
class ServiceAttachmentList(typing.TypedDict, total=False):
    id: str
    items: _list[ServiceAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ServiceAttachmentTunnelingConfig(typing.TypedDict, total=False):
    encapsulationProfile: typing.Literal[
        "GENEVE_SECURITY_V1", "UNSPECIFIED_ENCAPSULATION_PROFILE"
    ]
    routingMode: typing.Literal[
        "PACKET_INJECTION", "STANDARD_ROUTING", "UNSPECIFIED_ROUTING_MODE"
    ]

@typing.type_check_only
class ServiceAttachmentsScopedList(typing.TypedDict, total=False):
    serviceAttachments: _list[ServiceAttachment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ServiceIntegrationSpec(typing.TypedDict, total=False):
    backupDr: ServiceIntegrationSpecBackupDRSpec

@typing.type_check_only
class ServiceIntegrationSpecBackupDRSpec(typing.TypedDict, total=False):
    plan: str

@typing.type_check_only
class SetCommonInstanceMetadataOperationMetadata(typing.TypedDict, total=False):
    clientOperationId: str
    perLocationOperations: dict[str, typing.Any]

@typing.type_check_only
class SetCommonInstanceMetadataOperationMetadataPerLocationOperationInfo(
    typing.TypedDict, total=False
):
    error: Status
    state: typing.Literal[
        "ABANDONED", "DONE", "FAILED", "PROPAGATED", "PROPAGATING", "UNSPECIFIED"
    ]

@typing.type_check_only
class ShareSettings(typing.TypedDict, total=False):
    folderMap: dict[str, typing.Any]
    projectMap: dict[str, typing.Any]
    projects: _list[str]
    shareType: typing.Literal[
        "DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS",
        "LOCAL",
        "ORGANIZATION",
        "SHARE_TYPE_UNSPECIFIED",
        "SPECIFIC_PROJECTS",
    ]

@typing.type_check_only
class ShareSettingsFolderConfig(typing.TypedDict, total=False):
    folderId: str

@typing.type_check_only
class ShareSettingsProjectConfig(typing.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class ShieldedInstanceIdentity(typing.TypedDict, total=False):
    eccP256EncryptionKey: ShieldedInstanceIdentityEntry
    eccP256SigningKey: ShieldedInstanceIdentityEntry
    encryptionKey: ShieldedInstanceIdentityEntry
    kind: str
    signingKey: ShieldedInstanceIdentityEntry

@typing.type_check_only
class ShieldedInstanceIdentityEntry(typing.TypedDict, total=False):
    ekCert: str
    ekPub: str

@typing.type_check_only
class ShieldedInstanceIntegrityPolicy(typing.TypedDict, total=False):
    updateAutoLearnPolicy: bool

@typing.type_check_only
class ShieldedVmConfig(typing.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class ShieldedVmIdentity(typing.TypedDict, total=False):
    encryptionKey: ShieldedVmIdentityEntry
    kind: str
    signingKey: ShieldedVmIdentityEntry

@typing.type_check_only
class ShieldedVmIdentityEntry(typing.TypedDict, total=False):
    ekCert: str
    ekPub: str

@typing.type_check_only
class ShieldedVmIntegrityPolicy(typing.TypedDict, total=False):
    updateAutoLearnPolicy: bool

@typing.type_check_only
class SignedUrlKey(typing.TypedDict, total=False):
    keyName: str
    keyValue: str

@typing.type_check_only
class Snapshot(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"]
    autoCreated: bool
    chainName: str
    creationSizeBytes: str
    creationTimestamp: str
    description: str
    diskSizeGb: str
    downloadBytes: str
    enableConfidentialCompute: bool
    guestFlush: bool
    guestOsFeatures: _list[GuestOsFeature]
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    licenseCodes: _list[str]
    licenses: _list[str]
    locationHint: str
    maxRetentionDays: int
    name: str
    params: SnapshotParams
    region: str
    resourceStatus: SnapshotResourceStatus
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    snapshotEncryptionKey: CustomerEncryptionKey
    snapshotGroupId: str
    snapshotGroupName: str
    snapshotType: typing.Literal["ARCHIVE", "STANDARD"]
    sourceDisk: str
    sourceDiskEncryptionKey: CustomerEncryptionKey
    sourceDiskForRecoveryCheckpoint: str
    sourceDiskId: str
    sourceInstantSnapshot: str
    sourceInstantSnapshotEncryptionKey: CustomerEncryptionKey
    sourceInstantSnapshotId: str
    sourceSnapshotSchedulePolicy: str
    sourceSnapshotSchedulePolicyId: str
    status: typing.Literal["CREATING", "DELETING", "FAILED", "READY", "UPLOADING"]
    storageBytes: str
    storageBytesStatus: typing.Literal["UPDATING", "UP_TO_DATE"]
    storageLocations: _list[str]

@typing.type_check_only
class SnapshotAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SnapshotGroup(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    selfLink: str
    selfLinkWithId: str
    sourceInfo: SnapshotGroupSourceInfo
    sourceInstantSnapshotGroup: str
    sourceInstantSnapshotGroupInfo: SnapshotGroupSourceInstantSnapshotGroupInfo
    status: typing.Literal[
        "CREATING", "DELETING", "FAILED", "INVALID", "READY", "UNKNOWN", "UPLOADING"
    ]

@typing.type_check_only
class SnapshotGroupParameters(typing.TypedDict, total=False):
    replicaZones: _list[str]
    sourceSnapshotGroup: str
    type: str

@typing.type_check_only
class SnapshotGroupSourceInfo(typing.TypedDict, total=False):
    consistencyGroup: str
    consistencyGroupId: str

@typing.type_check_only
class SnapshotGroupSourceInstantSnapshotGroupInfo(typing.TypedDict, total=False):
    instantSnapshotGroup: str
    instantSnapshotGroupId: str

@typing.type_check_only
class SnapshotList(typing.TypedDict, total=False):
    id: str
    items: _list[Snapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SnapshotParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class SnapshotRecycleBinPolicy(typing.TypedDict, total=False):
    rules: dict[str, typing.Any]
    systemRules: dict[str, typing.Any]

@typing.type_check_only
class SnapshotRecycleBinPolicyRule(typing.TypedDict, total=False):
    standardSnapshots: SnapshotRecycleBinPolicyRuleRuleConfig

@typing.type_check_only
class SnapshotRecycleBinPolicyRuleRuleConfig(typing.TypedDict, total=False):
    retentionDurationDays: str

@typing.type_check_only
class SnapshotResourceStatus(typing.TypedDict, total=False):
    scheduledDeletionTime: str

@typing.type_check_only
class SnapshotSettings(typing.TypedDict, total=False):
    accessLocation: SnapshotSettingsAccessLocation
    storageLocation: SnapshotSettingsStorageLocationSettings

@typing.type_check_only
class SnapshotSettingsAccessLocation(typing.TypedDict, total=False):
    locations: dict[str, typing.Any]
    policy: typing.Literal["ALL_REGIONS", "POLICY_UNSPECIFIED", "SPECIFIC_REGIONS"]

@typing.type_check_only
class SnapshotSettingsAccessLocationAccessLocationPreference(
    typing.TypedDict, total=False
):
    region: str

@typing.type_check_only
class SnapshotSettingsStorageLocationSettings(typing.TypedDict, total=False):
    locations: dict[str, typing.Any]
    policy: typing.Literal[
        "LOCAL_REGION",
        "NEAREST_MULTI_REGION",
        "SPECIFIC_LOCATIONS",
        "STORAGE_LOCATION_POLICY_UNSPECIFIED",
    ]

@typing.type_check_only
class SnapshotSettingsStorageLocationSettingsStorageLocationPreference(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class SnapshotUpdateKmsKeyRequest(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class SnapshotsGetEffectiveRecycleBinRuleResponse(typing.TypedDict, total=False):
    retentionDurationDays: str

@typing.type_check_only
class SnapshotsScopedList(typing.TypedDict, total=False):
    snapshots: _list[Snapshot]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SourceDiskEncryptionKey(typing.TypedDict, total=False):
    diskEncryptionKey: CustomerEncryptionKey
    sourceDisk: str

@typing.type_check_only
class SourceInstanceParams(typing.TypedDict, total=False):
    diskConfigs: _list[DiskInstantiationConfig]

@typing.type_check_only
class SourceInstanceProperties(typing.TypedDict, total=False):
    canIpForward: bool
    deletionProtection: bool
    description: str
    disks: _list[SavedAttachedDisk]
    guestAccelerators: _list[AcceleratorConfig]
    keyRevocationActionType: typing.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    labels: dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: _list[NetworkInterface]
    postKeyRevocationActionType: typing.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    scheduling: Scheduling
    serviceAccounts: _list[ServiceAccount]
    tags: Tags

@typing.type_check_only
class SslCertificate(typing.TypedDict, total=False):
    certificate: str
    creationTimestamp: str
    description: str
    expireTime: str
    id: str
    kind: str
    managed: SslCertificateManagedSslCertificate
    name: str
    privateKey: str
    region: str
    selfLink: str
    selfLinkWithId: str
    selfManaged: SslCertificateSelfManagedSslCertificate
    subjectAlternativeNames: _list[str]
    type: typing.Literal["MANAGED", "SELF_MANAGED", "TYPE_UNSPECIFIED"]

@typing.type_check_only
class SslCertificateAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslCertificateList(typing.TypedDict, total=False):
    id: str
    items: _list[SslCertificate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslCertificateManagedSslCertificate(typing.TypedDict, total=False):
    domainStatus: dict[str, typing.Any]
    domains: _list[str]
    status: typing.Literal[
        "ACTIVE",
        "MANAGED_CERTIFICATE_STATUS_UNSPECIFIED",
        "PROVISIONING",
        "PROVISIONING_FAILED",
        "PROVISIONING_FAILED_PERMANENTLY",
        "RENEWAL_FAILED",
    ]

@typing.type_check_only
class SslCertificateSelfManagedSslCertificate(typing.TypedDict, total=False):
    certificate: str
    privateKey: str

@typing.type_check_only
class SslCertificatesScopedList(typing.TypedDict, total=False):
    sslCertificates: _list[SslCertificate]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesList(typing.TypedDict, total=False):
    id: str
    items: _list[SslPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesListAvailableFeaturesResponse(typing.TypedDict, total=False):
    features: _list[str]

@typing.type_check_only
class SslPoliciesScopedList(typing.TypedDict, total=False):
    sslPolicies: _list[SslPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPolicy(typing.TypedDict, total=False):
    creationTimestamp: str
    customFeatures: _list[str]
    description: str
    enabledFeatures: _list[str]
    fingerprint: str
    id: str
    kind: str
    minTlsVersion: typing.Literal["TLS_1_0", "TLS_1_1", "TLS_1_2", "TLS_1_3"]
    name: str
    postQuantumKeyExchange: typing.Literal["DEFAULT", "DEFERRED", "ENABLED"]
    profile: typing.Literal[
        "COMPATIBLE", "CUSTOM", "FIPS_202205", "MODERN", "RESTRICTED"
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    tlsSettings: ServerTlsSettings
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class SslPolicyReference(typing.TypedDict, total=False):
    sslPolicy: str

@typing.type_check_only
class StatefulPolicy(typing.TypedDict, total=False):
    preservedState: StatefulPolicyPreservedState

@typing.type_check_only
class StatefulPolicyPreservedState(typing.TypedDict, total=False):
    disks: dict[str, typing.Any]
    externalIPs: dict[str, typing.Any]
    internalIPs: dict[str, typing.Any]

@typing.type_check_only
class StatefulPolicyPreservedStateDiskDevice(typing.TypedDict, total=False):
    autoDelete: typing.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

@typing.type_check_only
class StatefulPolicyPreservedStateNetworkIp(typing.TypedDict, total=False):
    autoDelete: typing.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StoragePool(typing.TypedDict, total=False):
    capacityProvisioningType: typing.Literal["ADVANCED", "STANDARD", "UNSPECIFIED"]
    creationTimestamp: str
    description: str
    exapoolProvisionedCapacityGb: StoragePoolExapoolProvisionedCapacityGb
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    params: StoragePoolParams
    performanceProvisioningType: typing.Literal["ADVANCED", "STANDARD", "UNSPECIFIED"]
    poolProvisionedCapacityGb: str
    poolProvisionedIops: str
    poolProvisionedThroughput: str
    provisionedIops: str
    provisionedThroughput: str
    resourceStatus: StoragePoolResourceStatus
    selfLink: str
    selfLinkWithId: str
    shareSettings: StoragePoolShareSettings
    sizeGb: str
    state: typing.Literal["CREATING", "DELETING", "FAILED", "READY"]
    status: StoragePoolResourceStatus
    storagePoolType: str
    zone: str

@typing.type_check_only
class StoragePoolAggregatedList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolDisk(typing.TypedDict, total=False):
    attachedInstances: _list[str]
    creationTimestamp: str
    disk: str
    name: str
    provisionedIops: str
    provisionedThroughput: str
    resourcePolicies: _list[str]
    sizeGb: str
    status: typing.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RESTORING", "UNAVAILABLE"
    ]
    type: str
    usedBytes: str

@typing.type_check_only
class StoragePoolExapoolProvisionedCapacityGb(typing.TypedDict, total=False):
    capacityOptimized: str
    readOptimized: str
    writeOptimized: str

@typing.type_check_only
class StoragePoolList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[StoragePool]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolListDisks(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[StoragePoolDisk]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolResourceStatus(typing.TypedDict, total=False):
    aggregateDiskProvisionedIops: str
    aggregateDiskSizeGb: str
    diskCount: str
    exapoolMaxReadIops: str
    exapoolMaxReadThroughput: str
    exapoolMaxWriteIops: str
    exapoolMaxWriteThroughput: str
    lastResizeTimestamp: str
    maxAggregateDiskSizeGb: str
    maxTotalProvisionedDiskCapacityGb: str
    numberOfDisks: str
    poolUsedCapacityBytes: str
    poolUsedIops: str
    poolUsedThroughput: str
    poolUserWrittenBytes: str
    totalProvisionedDiskCapacityGb: str
    totalProvisionedDiskIops: str
    totalProvisionedDiskThroughput: str
    usedBytes: str
    usedReducedBytes: str
    usedThroughput: str

@typing.type_check_only
class StoragePoolShareSettings(typing.TypedDict, total=False):
    projectMap: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolShareSettingsProjectConfig(typing.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class StoragePoolType(typing.TypedDict, total=False):
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    maxPoolProvisionedCapacityGb: str
    maxPoolProvisionedIops: str
    maxPoolProvisionedThroughput: str
    minPoolProvisionedCapacityGb: str
    minPoolProvisionedIops: str
    minPoolProvisionedThroughput: str
    minSizeGb: str
    name: str
    selfLink: str
    selfLinkWithId: str
    supportedDiskTypes: _list[str]
    zone: str

@typing.type_check_only
class StoragePoolTypeAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolTypeList(typing.TypedDict, total=False):
    id: str
    items: _list[StoragePoolType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolTypesScopedList(typing.TypedDict, total=False):
    storagePoolTypes: _list[StoragePoolType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolsScopedList(typing.TypedDict, total=False):
    storagePools: _list[StoragePool]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StructuredEntries(typing.TypedDict, total=False):
    entries: dict[str, typing.Any]

@typing.type_check_only
class Subnetwork(typing.TypedDict, total=False):
    aggregationInterval: typing.Literal[
        "INTERVAL_10_MIN",
        "INTERVAL_15_MIN",
        "INTERVAL_1_MIN",
        "INTERVAL_30_SEC",
        "INTERVAL_5_MIN",
        "INTERVAL_5_SEC",
    ]
    allowSubnetCidrRoutesOverlap: bool
    creationTimestamp: str
    description: str
    enableFlowLogs: bool
    enableL2: bool
    enablePrivateV6Access: bool
    externalIpv6Prefix: str
    fingerprint: str
    flowSampling: float
    gatewayAddress: str
    id: str
    internalIpv6Prefix: str
    ipCidrRange: str
    ipCollection: str
    ipv6AccessType: typing.Literal["EXTERNAL", "INTERNAL"]
    ipv6CidrRange: str
    ipv6GceEndpoint: typing.Literal["VM_AND_FR", "VM_ONLY"]
    ipv6NetworkTier: typing.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    kind: str
    logConfig: SubnetworkLogConfig
    metadata: typing.Literal["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]
    name: str
    network: str
    params: SubnetworkParams
    privateIpGoogleAccess: bool
    privateIpv6GoogleAccess: typing.Literal[
        "DISABLE_GOOGLE_ACCESS",
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
    ]
    purpose: typing.Literal[
        "AGGREGATE",
        "CLOUD_EXTENSION",
        "CUSTOM_HARDWARE_LINK",
        "GLOBAL_MANAGED_PROXY",
        "INTERNAL_HTTPS_LOAD_BALANCER",
        "PEER_MIGRATION",
        "PRIVATE",
        "PRIVATE_NAT",
        "PRIVATE_RFC_1918",
        "PRIVATE_SERVICE_CONNECT",
        "REGIONAL_MANAGED_PROXY",
    ]
    region: str
    reservedInternalRange: str
    resolveSubnetMask: typing.Literal[
        "ARP_ALL_RANGES",
        "ARP_BROADCAST_PRIMARY_RANGE",
        "ARP_BROADCAST_PRIMARY_RANGE_WITH_LEARNING",
        "ARP_PRIMARY_RANGE",
    ]
    role: typing.Literal["ACTIVE", "BACKUP"]
    secondaryIpRanges: _list[SubnetworkSecondaryRange]
    selfLink: str
    selfLinkWithId: str
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    state: typing.Literal["DRAINING", "READY"]
    systemReservedExternalIpv6Ranges: _list[str]
    systemReservedInternalIpv6Ranges: _list[str]
    utilizationDetails: SubnetworkUtilizationDetails
    vlans: _list[int]

@typing.type_check_only
class SubnetworkAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworkList(typing.TypedDict, total=False):
    id: str
    items: _list[Subnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworkLogConfig(typing.TypedDict, total=False):
    aggregationInterval: typing.Literal[
        "INTERVAL_10_MIN",
        "INTERVAL_15_MIN",
        "INTERVAL_1_MIN",
        "INTERVAL_30_SEC",
        "INTERVAL_5_MIN",
        "INTERVAL_5_SEC",
    ]
    enable: bool
    filterExpr: str
    flowSampling: float
    metadata: typing.Literal[
        "CUSTOM_METADATA", "EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"
    ]
    metadataFields: _list[str]

@typing.type_check_only
class SubnetworkParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class SubnetworkSecondaryRange(typing.TypedDict, total=False):
    ipCidrRange: str
    ipCollection: str
    ipVersion: typing.Literal["IPV4", "IPV6", "IP_VERSION_UNSPECIFIED"]
    rangeName: str
    reservedInternalRange: str

@typing.type_check_only
class SubnetworkUtilizationDetails(typing.TypedDict, total=False):
    externalIpv6InstanceUtilization: SubnetworkUtilizationDetailsIPV6Utilization
    externalIpv6LbUtilization: SubnetworkUtilizationDetailsIPV6Utilization
    internalIpv6Utilization: SubnetworkUtilizationDetailsIPV6Utilization
    ipv4Utilizations: _list[SubnetworkUtilizationDetailsIPV4Utilization]

@typing.type_check_only
class SubnetworkUtilizationDetailsIPV4Utilization(typing.TypedDict, total=False):
    rangeName: str
    totalAllocatedIp: str
    totalFreeIp: str

@typing.type_check_only
class SubnetworkUtilizationDetailsIPV6Utilization(typing.TypedDict, total=False):
    totalAllocatedIp: Uint128
    totalFreeIp: Uint128

@typing.type_check_only
class SubnetworksExpandIpCidrRangeRequest(typing.TypedDict, total=False):
    ipCidrRange: str

@typing.type_check_only
class SubnetworksScopedList(typing.TypedDict, total=False):
    subnetworks: _list[Subnetwork]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworksScopedWarning(typing.TypedDict, total=False):
    scopeName: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworksSetPrivateIpGoogleAccessRequest(typing.TypedDict, total=False):
    privateIpGoogleAccess: bool

@typing.type_check_only
class Subsetting(typing.TypedDict, total=False):
    policy: typing.Literal["CONSISTENT_HASH_SUBSETTING", "NONE"]
    subsetSize: int

@typing.type_check_only
class TCPHealthCheck(typing.TypedDict, total=False):
    port: int
    portName: str
    portSpecification: typing.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    request: str
    response: str

@typing.type_check_only
class Tags(typing.TypedDict, total=False):
    fingerprint: str
    items: _list[str]

@typing.type_check_only
class TargetGrpcProxy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    selfLink: str
    selfLinkWithId: str
    urlMap: str
    validateForProxyless: bool

@typing.type_check_only
class TargetGrpcProxyList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetGrpcProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxiesScopedList(typing.TypedDict, total=False):
    targetHttpProxies: _list[TargetHttpProxy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    httpFilters: _list[str]
    httpKeepAliveTimeoutSec: int
    id: str
    kind: str
    name: str
    proxyBind: bool
    region: str
    selfLink: str
    selfLinkWithId: str
    urlMap: str

@typing.type_check_only
class TargetHttpProxyAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxyList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetHttpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxiesScopedList(typing.TypedDict, total=False):
    targetHttpsProxies: _list[TargetHttpsProxy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxiesSetCertificateMapRequest(typing.TypedDict, total=False):
    certificateMap: str

@typing.type_check_only
class TargetHttpsProxiesSetQuicOverrideRequest(typing.TypedDict, total=False):
    quicOverride: typing.Literal["DISABLE", "ENABLE", "NONE"]

@typing.type_check_only
class TargetHttpsProxiesSetSslCertificatesRequest(typing.TypedDict, total=False):
    sslCertificates: _list[str]

@typing.type_check_only
class TargetHttpsProxy(typing.TypedDict, total=False):
    authentication: str
    authorization: str
    authorizationPolicy: str
    certificateMap: str
    creationTimestamp: str
    description: str
    fingerprint: str
    httpFilters: _list[str]
    httpKeepAliveTimeoutSec: int
    id: str
    kind: str
    name: str
    proxyBind: bool
    quicOverride: typing.Literal["DISABLE", "ENABLE", "NONE"]
    region: str
    selfLink: str
    selfLinkWithId: str
    serverTlsPolicy: str
    sslCertificates: _list[str]
    sslPolicy: str
    tlsEarlyData: typing.Literal["DISABLED", "PERMISSIVE", "STRICT", "UNRESTRICTED"]
    urlMap: str

@typing.type_check_only
class TargetHttpsProxyAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxyList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetHttpsProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetInstance(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    instance: str
    kind: str
    name: str
    natPolicy: typing.Literal["NO_NAT"]
    network: str
    securityPolicy: str
    selfLink: str
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class TargetInstanceAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetInstanceList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetInstance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetInstancesScopedList(typing.TypedDict, total=False):
    targetInstances: _list[TargetInstance]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetPool(typing.TypedDict, total=False):
    backupPool: str
    creationTimestamp: str
    description: str
    failoverRatio: float
    healthChecks: _list[str]
    id: str
    instances: _list[str]
    kind: str
    name: str
    region: str
    securityPolicy: str
    selfLink: str
    selfLinkWithId: str
    sessionAffinity: typing.Literal[
        "CLIENT_IP",
        "CLIENT_IP_NO_DESTINATION",
        "CLIENT_IP_PORT_PROTO",
        "CLIENT_IP_PROTO",
        "GENERATED_COOKIE",
        "HEADER_FIELD",
        "HTTP_COOKIE",
        "NONE",
        "STRONG_COOKIE_AFFINITY",
    ]

@typing.type_check_only
class TargetPoolAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetPoolInstanceHealth(typing.TypedDict, total=False):
    healthStatus: _list[HealthStatus]
    kind: str

@typing.type_check_only
class TargetPoolList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetPool]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetPoolsAddHealthCheckRequest(typing.TypedDict, total=False):
    healthChecks: _list[HealthCheckReference]

@typing.type_check_only
class TargetPoolsAddInstanceRequest(typing.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class TargetPoolsRemoveHealthCheckRequest(typing.TypedDict, total=False):
    healthChecks: _list[HealthCheckReference]

@typing.type_check_only
class TargetPoolsRemoveInstanceRequest(typing.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class TargetPoolsScopedList(typing.TypedDict, total=False):
    targetPools: _list[TargetPool]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetReference(typing.TypedDict, total=False):
    target: str

@typing.type_check_only
class TargetSslProxiesSetBackendServiceRequest(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class TargetSslProxiesSetCertificateMapRequest(typing.TypedDict, total=False):
    certificateMap: str

@typing.type_check_only
class TargetSslProxiesSetProxyHeaderRequest(typing.TypedDict, total=False):
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]

@typing.type_check_only
class TargetSslProxiesSetSslCertificatesRequest(typing.TypedDict, total=False):
    sslCertificates: _list[str]

@typing.type_check_only
class TargetSslProxy(typing.TypedDict, total=False):
    certificateMap: str
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    selfLink: str
    service: str
    sslCertificates: _list[str]
    sslPolicy: str

@typing.type_check_only
class TargetSslProxyList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetSslProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetTcpProxiesScopedList(typing.TypedDict, total=False):
    targetTcpProxies: _list[TargetTcpProxy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetTcpProxiesSetBackendServiceRequest(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class TargetTcpProxiesSetProxyHeaderRequest(typing.TypedDict, total=False):
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]

@typing.type_check_only
class TargetTcpProxy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    loadBalancingScheme: typing.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "INTERNAL_MANAGED",
        "LOAD_BALANCING_SCHEME_UNSPECIFIED",
    ]
    name: str
    proxyBind: bool
    proxyHeader: typing.Literal["NONE", "PROXY_V1"]
    region: str
    selfLink: str
    service: str

@typing.type_check_only
class TargetTcpProxyAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetTcpProxyList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetTcpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGateway(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    forwardingRules: _list[str]
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    params: TargetVpnGatewayParams
    region: str
    selfLink: str
    status: typing.Literal["CREATING", "DELETING", "FAILED", "READY"]
    tunnels: _list[str]

@typing.type_check_only
class TargetVpnGatewayAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewayList(typing.TypedDict, total=False):
    id: str
    items: _list[TargetVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewayParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewaysScopedList(typing.TypedDict, total=False):
    targetVpnGateways: _list[TargetVpnGateway]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TestFailure(typing.TypedDict, total=False):
    actualOutputUrl: str
    actualRedirectResponseCode: int
    actualService: str
    expectedOutputUrl: str
    expectedRedirectResponseCode: int
    expectedService: str
    headers: _list[UrlMapTestHeader]
    host: str
    path: str

@typing.type_check_only
class TestPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class TlsCertificateContext(typing.TypedDict, total=False):
    certificatePaths: TlsCertificatePaths
    certificateSource: typing.Literal["INVALID", "USE_PATH", "USE_SDS"]
    sdsConfig: SdsConfig

@typing.type_check_only
class TlsCertificatePaths(typing.TypedDict, total=False):
    certificatePath: str
    privateKeyPath: str

@typing.type_check_only
class TlsContext(typing.TypedDict, total=False):
    certificateContext: TlsCertificateContext
    validationContext: TlsValidationContext

@typing.type_check_only
class TlsValidationContext(typing.TypedDict, total=False):
    certificatePath: str
    sdsConfig: SdsConfig
    validationSource: typing.Literal["INVALID", "USE_PATH", "USE_SDS"]

@typing.type_check_only
class UDPHealthCheck(typing.TypedDict, total=False):
    port: int
    portName: str
    request: str
    response: str

@typing.type_check_only
class Uint128(typing.TypedDict, total=False):
    high: str
    low: str

@typing.type_check_only
class UpcomingMaintenance(typing.TypedDict, total=False):
    canReschedule: bool
    date: str
    latestWindowStartTime: str
    maintenanceMethod: typing.Literal[
        "LIVE_UPDATE", "MAINTENANCE_METHOD_UNSPECIFIED", "TERMINATION"
    ]
    maintenanceOnShutdown: bool
    maintenanceReasons: _list[
        typing.Literal[
            "FAILURE_DISK",
            "FAILURE_GPU",
            "FAILURE_GPU_MULTIPLE_FAULTY_HOSTS_CUSTOMER_REPORTED",
            "FAILURE_GPU_NVLINK_SWITCH_CUSTOMER_REPORTED",
            "FAILURE_GPU_TEMPERATURE",
            "FAILURE_GPU_XID",
            "FAILURE_INFRA",
            "FAILURE_INTERFACE",
            "FAILURE_MEMORY",
            "FAILURE_NETWORK",
            "FAILURE_NVLINK",
            "FAILURE_REDUNDANT_HARDWARE_FAULT",
            "FAILURE_TPU",
            "INFRASTRUCTURE_RELOCATION",
            "MAINTENANCE_REASON_UNKNOWN",
            "PLANNED_NETWORK_UPDATE",
            "PLANNED_UPDATE",
        ]
    ]
    maintenanceStatus: typing.Literal["ONGOING", "PENDING", "UNKNOWN"]
    startTimeWindow: UpcomingMaintenanceTimeWindow
    time: str
    type: typing.Literal["MULTIPLE", "SCHEDULED", "UNKNOWN_TYPE", "UNSCHEDULED"]
    windowEndTime: str
    windowStartTime: str

@typing.type_check_only
class UpcomingMaintenanceTimeWindow(typing.TypedDict, total=False):
    earliest: str
    latest: str

@typing.type_check_only
class UrlMap(typing.TypedDict, total=False):
    creationTimestamp: str
    defaultCustomErrorResponsePolicy: CustomErrorResponsePolicy
    defaultRouteAction: HttpRouteAction
    defaultService: str
    defaultUrlRedirect: HttpRedirectAction
    description: str
    fingerprint: str
    headerAction: HttpHeaderAction
    hostRules: _list[HostRule]
    id: str
    kind: str
    name: str
    pathMatchers: _list[PathMatcher]
    region: str
    selfLink: str
    status: UrlMapStatus
    tests: _list[UrlMapTest]

@typing.type_check_only
class UrlMapList(typing.TypedDict, total=False):
    id: str
    items: _list[UrlMap]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class UrlMapQuotaUsage(typing.TypedDict, total=False):
    forwardingRules: int
    units: str

@typing.type_check_only
class UrlMapReference(typing.TypedDict, total=False):
    urlMap: str

@typing.type_check_only
class UrlMapStatus(typing.TypedDict, total=False):
    quotaUsage: UrlMapQuotaUsage

@typing.type_check_only
class UrlMapTest(typing.TypedDict, total=False):
    backendServiceWeight: int
    description: str
    expectedOutputUrl: str
    expectedRedirectResponseCode: int
    expectedUrlRedirect: str
    headers: _list[UrlMapTestHeader]
    host: str
    path: str
    service: str

@typing.type_check_only
class UrlMapTestHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class UrlMapValidationResult(typing.TypedDict, total=False):
    loadErrors: _list[str]
    loadSucceeded: bool
    quotaUsage: UrlMapQuotaUsage
    testFailures: _list[TestFailure]
    testPassed: bool

@typing.type_check_only
class UrlMapsAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class UrlMapsScopedList(typing.TypedDict, total=False):
    urlMaps: _list[UrlMap]
    warning: dict[str, typing.Any]

@typing.type_check_only
class UrlMapsValidateRequest(typing.TypedDict, total=False):
    loadBalancingSchemes: _list[
        typing.Literal[
            "EXTERNAL", "EXTERNAL_MANAGED", "LOAD_BALANCING_SCHEME_UNSPECIFIED"
        ]
    ]
    resource: UrlMap

@typing.type_check_only
class UrlMapsValidateResponse(typing.TypedDict, total=False):
    result: UrlMapValidationResult

@typing.type_check_only
class UrlRewrite(typing.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str
    pathTemplateRewrite: str
    regexRewrite: RegexRewrite

@typing.type_check_only
class UsableSubnetwork(typing.TypedDict, total=False):
    externalIpv6Prefix: str
    internalIpv6Prefix: str
    ipCidrRange: str
    ipv6AccessType: typing.Literal["EXTERNAL", "INTERNAL"]
    network: str
    purpose: typing.Literal[
        "AGGREGATE",
        "CLOUD_EXTENSION",
        "CUSTOM_HARDWARE_LINK",
        "GLOBAL_MANAGED_PROXY",
        "INTERNAL_HTTPS_LOAD_BALANCER",
        "PEER_MIGRATION",
        "PRIVATE",
        "PRIVATE_NAT",
        "PRIVATE_RFC_1918",
        "PRIVATE_SERVICE_CONNECT",
        "REGIONAL_MANAGED_PROXY",
    ]
    role: typing.Literal["ACTIVE", "BACKUP"]
    secondaryIpRanges: _list[UsableSubnetworkSecondaryRange]
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    subnetwork: str

@typing.type_check_only
class UsableSubnetworkSecondaryRange(typing.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class UsableSubnetworksAggregatedList(typing.TypedDict, total=False):
    id: str
    items: _list[UsableSubnetwork]
    kind: str
    nextPageToken: str
    scopedWarnings: _list[SubnetworksScopedWarning]
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class UsageExportLocation(typing.TypedDict, total=False):
    bucketName: str
    reportNamePrefix: str

@typing.type_check_only
class VmEndpointNatMappings(typing.TypedDict, total=False):
    instanceName: str
    interfaceNatMappings: _list[VmEndpointNatMappingsInterfaceNatMappings]

@typing.type_check_only
class VmEndpointNatMappingsInterfaceNatMappings(typing.TypedDict, total=False):
    drainNatIpPortRanges: _list[str]
    natIpPortRanges: _list[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    ruleMappings: _list[VmEndpointNatMappingsInterfaceNatMappingsNatRuleMappings]
    sourceAliasIpRange: str
    sourceVirtualIp: str

@typing.type_check_only
class VmEndpointNatMappingsInterfaceNatMappingsNatRuleMappings(
    typing.TypedDict, total=False
):
    drainNatIpPortRanges: _list[str]
    natIpPortRanges: _list[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    ruleNumber: int

@typing.type_check_only
class VmEndpointNatMappingsList(typing.TypedDict, total=False):
    id: str
    kind: str
    nextPageToken: str
    result: _list[VmEndpointNatMappings]
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class VmExtension(typing.TypedDict, total=False):
    name: str
    versions: _list[str]

@typing.type_check_only
class VmExtensionPoliciesScopedList(typing.TypedDict, total=False):
    vmExtensionPolicies: _list[VmExtensionPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VmExtensionPolicy(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    extensionPolicies: dict[str, typing.Any]
    globalResourceLink: str
    id: str
    instanceSelectors: _list[VmExtensionPolicyInstanceSelector]
    kind: str
    managedByGlobal: bool
    name: str
    priority: int
    selfLink: str
    selfLinkWithId: str
    state: typing.Literal["ACTIVE", "DELETING", "STATE_UNSPECIFIED"]
    updateTimestamp: str

@typing.type_check_only
class VmExtensionPolicyAggregatedListResponse(typing.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VmExtensionPolicyExtensionPolicy(typing.TypedDict, total=False):
    installedSoftwareSelector: VmExtensionPolicyInstalledSoftwareSelector
    pinnedVersion: str
    stringConfig: str

@typing.type_check_only
class VmExtensionPolicyInstalledSoftwareSelector(typing.TypedDict, total=False):
    anyOfSelectors: dict[str, typing.Any]

@typing.type_check_only
class VmExtensionPolicyInstalledSoftwareSelectorSelectorSet(
    typing.TypedDict, total=False
):
    allOfSelectors: _list[str]

@typing.type_check_only
class VmExtensionPolicyInstanceSelector(typing.TypedDict, total=False):
    labelSelector: VmExtensionPolicyLabelSelector

@typing.type_check_only
class VmExtensionPolicyLabelSelector(typing.TypedDict, total=False):
    inclusionLabels: dict[str, typing.Any]

@typing.type_check_only
class VmExtensionPolicyList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[VmExtensionPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VmExtensionState(typing.TypedDict, total=False):
    enforcementMsg: str
    enforcementState: typing.Literal[
        "APPLYING_CONFIG",
        "ENFORCEMENT_STATE_UNSPECIFIED",
        "INCOMPATIBLE",
        "INSTALLED",
        "INSTALLING",
        "INSTALL_FAILED",
        "REMOVING",
        "ROLLBACK_FAILED",
        "ROLLED_BACK",
        "ROLLING_BACK",
        "SERVICE_DISABLED",
    ]
    healthMsg: str
    healthStatus: typing.Literal[
        "CRASHED",
        "HEALTH_STATUS_UNSPECIFIED",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
    ]
    name: str
    policyId: str
    version: str

@typing.type_check_only
class VpnGateway(typing.TypedDict, total=False):
    creationTimestamp: str
    description: str
    gatewayIpVersion: typing.Literal["IPV4", "IPV6"]
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    params: VpnGatewayParams
    region: str
    selfLink: str
    stackType: typing.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    vpnInterfaces: _list[VpnGatewayVpnGatewayInterface]

@typing.type_check_only
class VpnGatewayAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayList(typing.TypedDict, total=False):
    id: str
    items: _list[VpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayStatus(typing.TypedDict, total=False):
    vpnConnections: _list[VpnGatewayStatusVpnConnection]

@typing.type_check_only
class VpnGatewayStatusHighAvailabilityRequirementState(typing.TypedDict, total=False):
    state: typing.Literal["CONNECTION_REDUNDANCY_MET", "CONNECTION_REDUNDANCY_NOT_MET"]
    unsatisfiedReason: typing.Literal["INCOMPLETE_TUNNELS_COVERAGE"]

@typing.type_check_only
class VpnGatewayStatusTunnel(typing.TypedDict, total=False):
    localGatewayInterface: int
    peerGatewayInterface: int
    tunnelUrl: str

@typing.type_check_only
class VpnGatewayStatusVpnConnection(typing.TypedDict, total=False):
    peerExternalGateway: str
    peerGcpGateway: str
    state: VpnGatewayStatusHighAvailabilityRequirementState
    tunnels: _list[VpnGatewayStatusTunnel]

@typing.type_check_only
class VpnGatewayVpnGatewayInterface(typing.TypedDict, total=False):
    id: int
    interconnectAttachment: str
    ipAddress: str
    ipv6Address: str

@typing.type_check_only
class VpnGatewaysGetStatusResponse(typing.TypedDict, total=False):
    result: VpnGatewayStatus

@typing.type_check_only
class VpnGatewaysScopedList(typing.TypedDict, total=False):
    vpnGateways: _list[VpnGateway]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnel(typing.TypedDict, total=False):
    capacityTier: typing.Literal["DEFAULT", "HIGH"]
    cipherSuite: VpnTunnelCipherSuite
    creationTimestamp: str
    description: str
    detailedStatus: str
    id: str
    ikeVersion: int
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    localTrafficSelector: _list[str]
    name: str
    params: VpnTunnelParams
    peerExternalGateway: str
    peerExternalGatewayInterface: int
    peerGcpGateway: str
    peerIp: str
    pqcPhase1: VpnTunnelPqc
    pqcPhase2: VpnTunnelPqc
    region: str
    remoteTrafficSelector: _list[str]
    router: str
    selfLink: str
    sharedSecret: str
    sharedSecretHash: str
    status: typing.Literal[
        "ALLOCATING_RESOURCES",
        "AUTHORIZATION_ERROR",
        "DEPROVISIONING",
        "ESTABLISHED",
        "FAILED",
        "FIRST_HANDSHAKE",
        "NEGOTIATION_FAILURE",
        "NETWORK_ERROR",
        "NO_INCOMING_PACKETS",
        "PROVISIONING",
        "REJECTED",
        "STOPPED",
        "WAITING_FOR_FULL_CONFIG",
    ]
    targetVpnGateway: str
    vpnGateway: str
    vpnGatewayInterface: int

@typing.type_check_only
class VpnTunnelAdditionalKeyExchanges(typing.TypedDict, total=False):
    ke1s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]
    ke2s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]
    ke3s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]
    ke4s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]
    ke5s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]
    ke6s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]
    ke7s: _list[
        typing.Literal[
            "KEY_ENCAPSULATION_MECHANISM_UNSPECIFIED",
            "KE_NONE",
            "ML_KEM_1024",
            "ML_KEM_768",
        ]
    ]

@typing.type_check_only
class VpnTunnelAggregatedList(typing.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelCipherSuite(typing.TypedDict, total=False):
    phase1: VpnTunnelPhase1Algorithms
    phase2: VpnTunnelPhase2Algorithms

@typing.type_check_only
class VpnTunnelList(typing.TypedDict, total=False):
    id: str
    items: _list[VpnTunnel]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelParams(typing.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelPhase1Algorithms(typing.TypedDict, total=False):
    dh: _list[str]
    encryption: _list[str]
    integrity: _list[str]
    prf: _list[str]

@typing.type_check_only
class VpnTunnelPhase2Algorithms(typing.TypedDict, total=False):
    encryption: _list[str]
    integrity: _list[str]
    pfs: _list[str]

@typing.type_check_only
class VpnTunnelPqc(typing.TypedDict, total=False):
    keys: VpnTunnelAdditionalKeyExchanges
    mode: typing.Literal["DISABLED", "ENABLED", "PQC_MODE_UNSPECIFIED"]

@typing.type_check_only
class VpnTunnelsScopedList(typing.TypedDict, total=False):
    vpnTunnels: _list[VpnTunnel]
    warning: dict[str, typing.Any]

@typing.type_check_only
class WafExpressionSet(typing.TypedDict, total=False):
    aliases: _list[str]
    expressions: _list[WafExpressionSetExpression]
    id: str

@typing.type_check_only
class WafExpressionSetExpression(typing.TypedDict, total=False):
    id: str
    sensitivity: int

@typing.type_check_only
class WaitForReplicationCatchUpRequest(typing.TypedDict, total=False):
    maxWaitDuration: str

@typing.type_check_only
class WeightedBackendService(typing.TypedDict, total=False):
    backendService: str
    headerAction: HttpHeaderAction
    weight: int

@typing.type_check_only
class Wire(typing.TypedDict, total=False):
    adminEnabled: bool
    endpoints: _list[WireEndpoint]
    label: str
    wireProperties: WireProperties

@typing.type_check_only
class WireEndpoint(typing.TypedDict, total=False):
    interconnect: str
    vlanTag: int

@typing.type_check_only
class WireGroup(typing.TypedDict, total=False):
    adminEnabled: bool
    creationTimestamp: str
    description: str
    endpoints: dict[str, typing.Any]
    id: str
    kind: str
    name: str
    reconciling: bool
    selfLink: str
    selfLinkWithId: str
    serviceLevel: WireGroupServiceLevel
    topology: WireGroupTopology
    wireGroupProperties: WireGroupProperties
    wireInputs: dict[str, typing.Any]
    wireProperties: WireProperties
    wires: _list[Wire]

@typing.type_check_only
class WireGroupEndpoint(typing.TypedDict, total=False):
    interconnects: dict[str, typing.Any]

@typing.type_check_only
class WireGroupEndpointInterconnect(typing.TypedDict, total=False):
    interconnect: str
    vlanTags: _list[int]

@typing.type_check_only
class WireGroupList(typing.TypedDict, total=False):
    etag: str
    id: str
    items: _list[WireGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class WireGroupProperties(typing.TypedDict, total=False):
    type: typing.Literal["BOX_AND_CROSS", "REDUNDANT", "WIRE"]

@typing.type_check_only
class WireGroupServiceLevel(typing.TypedDict, total=False):
    availabilityClass: typing.Literal[
        "AVAILABILITY_99",
        "AVAILABILITY_999",
        "AVAILABILITY_9995",
        "NO_AVAILABILITY_SLA",
    ]

@typing.type_check_only
class WireGroupTopology(typing.TypedDict, total=False):
    endpoints: _list[WireGroupTopologyEndpoint]

@typing.type_check_only
class WireGroupTopologyEndpoint(typing.TypedDict, total=False):
    city: str
    label: str

@typing.type_check_only
class WireGroupWireInputs(typing.TypedDict, total=False):
    adminEnabled: bool
    wirePropertyOverrides: WireProperties

@typing.type_check_only
class WireProperties(typing.TypedDict, total=False):
    bandwidthAllocation: typing.Literal["ALLOCATE_PER_WIRE", "SHARED_WITH_WIRE_GROUP"]
    bandwidthMetered: str
    bandwidthUnmetered: str
    faultResponse: typing.Literal["DISABLE_PORT", "NONE"]
    flowManagement: typing.Literal["DYNAMIC_PATH", "FIXED_PATH"]
    networkServiceClass: typing.Literal["BRONZE", "GOLD"]

@typing.type_check_only
class WorkloadIdentityConfig(typing.TypedDict, total=False):
    identity: str
    identityCertificateEnabled: bool
    identityType: typing.Literal[
        "AGENT_IDENTITY", "IDENTITY_TYPE_UNSPECIFIED", "SERVICE_ACCOUNT"
    ]

@typing.type_check_only
class XpnHostList(typing.TypedDict, total=False):
    id: str
    items: _list[Project]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class XpnResourceId(typing.TypedDict, total=False):
    id: str
    type: typing.Literal["PROJECT", "XPN_RESOURCE_TYPE_UNSPECIFIED"]

@typing.type_check_only
class Zone(typing.TypedDict, total=False):
    availableCpuPlatforms: _list[str]
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    region: str
    resourceStatus: ZoneResourceStatus
    selfLink: str
    status: typing.Literal["DOWN", "UP"]
    supportsPzs: bool

@typing.type_check_only
class ZoneList(typing.TypedDict, total=False):
    id: str
    items: _list[Zone]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ZoneResourceStatus(typing.TypedDict, total=False):
    upcomingMaintenances: _list[PeriodicPartialMaintenanceSchedule]

@typing.type_check_only
class ZoneSetLabelsRequest(typing.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class ZoneSetPolicyRequest(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy
