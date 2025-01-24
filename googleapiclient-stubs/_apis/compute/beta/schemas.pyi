import typing

import typing_extensions

_list = list

@typing.type_check_only
class AWSV4Signature(typing_extensions.TypedDict, total=False):
    accessKey: str
    accessKeyId: str
    accessKeyVersion: str
    originRegion: str

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: str

@typing.type_check_only
class AcceleratorType(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    maximumCardsPerInstance: int
    name: str
    selfLink: str
    zone: str

@typing.type_check_only
class AcceleratorTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[AcceleratorType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTypesScopedList(typing_extensions.TypedDict, total=False):
    acceleratorTypes: _list[AcceleratorType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AccessConfig(typing_extensions.TypedDict, total=False):
    externalIpv6: str
    externalIpv6PrefixLength: int
    kind: str
    name: str
    natIP: str
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD", "PREMIUM", "STANDARD", "STANDARD_OVERRIDES_FIXED_STANDARD"
    ]
    publicPtrDomainName: str
    securityPolicy: str
    setPublicPtr: bool
    type: typing_extensions.Literal["DIRECT_IPV6", "ONE_TO_ONE_NAT"]

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    address: str
    addressType: typing_extensions.Literal["EXTERNAL", "INTERNAL", "UNSPECIFIED_TYPE"]
    creationTimestamp: str
    description: str
    id: str
    ipVersion: typing_extensions.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    ipv6EndpointType: typing_extensions.Literal["NETLB", "VM"]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD", "PREMIUM", "STANDARD", "STANDARD_OVERRIDES_FIXED_STANDARD"
    ]
    prefixLength: int
    purpose: typing_extensions.Literal[
        "DNS_RESOLVER",
        "GCE_ENDPOINT",
        "IPSEC_INTERCONNECT",
        "NAT_AUTO",
        "PRIVATE_SERVICE_CONNECT",
        "SERVERLESS",
        "SHARED_LOADBALANCER_VIP",
        "VPC_PEERING",
    ]
    region: str
    selfLink: str
    status: typing_extensions.Literal["IN_USE", "RESERVED", "RESERVING"]
    subnetwork: str
    users: _list[str]

@typing.type_check_only
class AddressAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AddressList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Address]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AddressesScopedList(typing_extensions.TypedDict, total=False):
    addresses: _list[Address]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AdvancedMachineFeatures(typing_extensions.TypedDict, total=False):
    enableNestedVirtualization: bool
    enableUefiNetworking: bool
    performanceMonitoringUnit: typing_extensions.Literal[
        "ARCHITECTURAL",
        "ENHANCED",
        "PERFORMANCE_MONITORING_UNIT_UNSPECIFIED",
        "STANDARD",
    ]
    threadsPerCore: int
    turboMode: str
    visibleCoreCount: int

@typing.type_check_only
class AliasIpRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    subnetworkRangeName: str

@typing.type_check_only
class AllocationAggregateReservation(typing_extensions.TypedDict, total=False):
    inUseResources: _list[AllocationAggregateReservationReservedResourceInfo]
    reservedResources: _list[AllocationAggregateReservationReservedResourceInfo]
    vmFamily: typing_extensions.Literal[
        "VM_FAMILY_CLOUD_TPU_DEVICE_CT3",
        "VM_FAMILY_CLOUD_TPU_LITE_DEVICE_CT5L",
        "VM_FAMILY_CLOUD_TPU_LITE_POD_SLICE_CT5LP",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT3P",
        "VM_FAMILY_CLOUD_TPU_POD_SLICE_CT4P",
    ]
    workloadType: typing_extensions.Literal["BATCH", "SERVING", "UNSPECIFIED"]

@typing.type_check_only
class AllocationAggregateReservationReservedResourceInfo(
    typing_extensions.TypedDict, total=False
):
    accelerator: AllocationAggregateReservationReservedResourceInfoAccelerator

@typing.type_check_only
class AllocationAggregateReservationReservedResourceInfoAccelerator(
    typing_extensions.TypedDict, total=False
):
    acceleratorCount: int
    acceleratorType: str

@typing.type_check_only
class AllocationReservationSharingPolicy(typing_extensions.TypedDict, total=False):
    serviceShareType: typing_extensions.Literal[
        "ALLOW_ALL", "DISALLOW_ALL", "SERVICE_SHARE_TYPE_UNSPECIFIED"
    ]

@typing.type_check_only
class AllocationResourceStatus(typing_extensions.TypedDict, total=False):
    reservationBlockCount: int
    reservationMaintenance: GroupMaintenanceInfo
    specificSkuAllocation: AllocationResourceStatusSpecificSKUAllocation

@typing.type_check_only
class AllocationResourceStatusSpecificSKUAllocation(
    typing_extensions.TypedDict, total=False
):
    sourceInstanceTemplateId: str
    utilizations: dict[str, typing.Any]

@typing.type_check_only
class AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    interface: typing_extensions.Literal["NVME", "SCSI"]

@typing.type_check_only
class AllocationSpecificSKUAllocationReservedInstanceProperties(
    typing_extensions.TypedDict, total=False
):
    guestAccelerators: _list[AcceleratorConfig]
    localSsds: _list[
        AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk
    ]
    locationHint: str
    machineType: str
    maintenanceFreezeDurationHours: int
    maintenanceInterval: typing_extensions.Literal["AS_NEEDED", "PERIODIC", "RECURRENT"]
    minCpuPlatform: str

@typing.type_check_only
class AllocationSpecificSKUReservation(typing_extensions.TypedDict, total=False):
    assuredCount: str
    count: str
    inUseCount: str
    instanceProperties: AllocationSpecificSKUAllocationReservedInstanceProperties
    sourceInstanceTemplate: str

@typing.type_check_only
class AttachedDisk(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    forceAttach: bool
    guestOsFeatures: _list[GuestOsFeature]
    index: int
    initializeParams: AttachedDiskInitializeParams
    interface: typing_extensions.Literal["NVME", "SCSI"]
    kind: str
    licenses: _list[str]
    locked: bool
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    savedState: typing_extensions.Literal["DISK_SAVED_STATE_UNSPECIFIED", "PRESERVED"]
    shieldedInstanceInitialState: InitialStateConfig
    source: str
    type: typing_extensions.Literal["PERSISTENT", "SCRATCH"]
    userLicenses: _list[str]

@typing.type_check_only
class AttachedDiskInitializeParams(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
    description: str
    diskName: str
    diskSizeGb: str
    diskType: str
    enableConfidentialCompute: bool
    guestOsFeatures: _list[GuestOsFeature]
    labels: dict[str, typing.Any]
    licenses: _list[str]
    multiWriter: bool
    onUpdateAction: typing_extensions.Literal[
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
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "ADMIN_READ", "DATA_READ", "DATA_WRITE", "LOG_TYPE_UNSPECIFIED"
    ]

@typing.type_check_only
class Autoscaler(typing_extensions.TypedDict, total=False):
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
    status: typing_extensions.Literal["ACTIVE", "DELETING", "ERROR", "PENDING"]
    statusDetails: _list[AutoscalerStatusDetails]
    target: str
    zone: str

@typing.type_check_only
class AutoscalerAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AutoscalerList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class AutoscalerStatusDetails(typing_extensions.TypedDict, total=False):
    message: str
    type: typing_extensions.Literal[
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
class AutoscalersScopedList(typing_extensions.TypedDict, total=False):
    autoscalers: _list[Autoscaler]
    warning: dict[str, typing.Any]

@typing.type_check_only
class AutoscalingPolicy(typing_extensions.TypedDict, total=False):
    coolDownPeriodSec: int
    cpuUtilization: AutoscalingPolicyCpuUtilization
    customMetricUtilizations: _list[AutoscalingPolicyCustomMetricUtilization]
    loadBalancingUtilization: AutoscalingPolicyLoadBalancingUtilization
    maxNumReplicas: int
    minNumReplicas: int
    mode: typing_extensions.Literal["OFF", "ON", "ONLY_SCALE_OUT", "ONLY_UP"]
    scaleDownControl: AutoscalingPolicyScaleDownControl
    scaleInControl: AutoscalingPolicyScaleInControl
    scalingSchedules: dict[str, typing.Any]

@typing.type_check_only
class AutoscalingPolicyCpuUtilization(typing_extensions.TypedDict, total=False):
    predictiveMethod: typing_extensions.Literal[
        "NONE", "OPTIMIZE_AVAILABILITY", "PREDICTIVE_METHOD_UNSPECIFIED"
    ]
    utilizationTarget: float

@typing.type_check_only
class AutoscalingPolicyCustomMetricUtilization(
    typing_extensions.TypedDict, total=False
):
    filter: str
    metric: str
    singleInstanceAssignment: float
    utilizationTarget: float
    utilizationTargetType: typing_extensions.Literal[
        "DELTA_PER_MINUTE", "DELTA_PER_SECOND", "GAUGE"
    ]

@typing.type_check_only
class AutoscalingPolicyLoadBalancingUtilization(
    typing_extensions.TypedDict, total=False
):
    utilizationTarget: float

@typing.type_check_only
class AutoscalingPolicyScaleDownControl(typing_extensions.TypedDict, total=False):
    maxScaledDownReplicas: FixedOrPercent
    timeWindowSec: int

@typing.type_check_only
class AutoscalingPolicyScaleInControl(typing_extensions.TypedDict, total=False):
    maxScaledInReplicas: FixedOrPercent
    timeWindowSec: int

@typing.type_check_only
class AutoscalingPolicyScalingSchedule(typing_extensions.TypedDict, total=False):
    description: str
    disabled: bool
    durationSec: int
    minRequiredReplicas: int
    schedule: str
    timeZone: str

@typing.type_check_only
class Backend(typing_extensions.TypedDict, total=False):
    balancingMode: typing_extensions.Literal[
        "CONNECTION", "CUSTOM_METRICS", "RATE", "UTILIZATION"
    ]
    capacityScaler: float
    customMetrics: _list[BackendCustomMetric]
    description: str
    failover: bool
    group: str
    maxConnections: int
    maxConnectionsPerEndpoint: int
    maxConnectionsPerInstance: int
    maxRate: int
    maxRatePerEndpoint: float
    maxRatePerInstance: float
    maxUtilization: float
    preference: typing_extensions.Literal[
        "DEFAULT", "PREFERENCE_UNSPECIFIED", "PREFERRED"
    ]

@typing.type_check_only
class BackendBucket(typing_extensions.TypedDict, total=False):
    bucketName: str
    cdnPolicy: BackendBucketCdnPolicy
    compressionMode: typing_extensions.Literal["AUTOMATIC", "DISABLED"]
    creationTimestamp: str
    customResponseHeaders: _list[str]
    description: str
    edgeSecurityPolicy: str
    enableCdn: bool
    id: str
    kind: str
    loadBalancingScheme: typing_extensions.Literal["INTERNAL_MANAGED"]
    name: str
    selfLink: str
    usedBy: _list[BackendBucketUsedBy]

@typing.type_check_only
class BackendBucketCdnPolicy(typing_extensions.TypedDict, total=False):
    bypassCacheOnRequestHeaders: _list[BackendBucketCdnPolicyBypassCacheOnRequestHeader]
    cacheKeyPolicy: BackendBucketCdnPolicyCacheKeyPolicy
    cacheMode: typing_extensions.Literal[
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
class BackendBucketCdnPolicyBypassCacheOnRequestHeader(
    typing_extensions.TypedDict, total=False
):
    headerName: str

@typing.type_check_only
class BackendBucketCdnPolicyCacheKeyPolicy(typing_extensions.TypedDict, total=False):
    includeHttpHeaders: _list[str]
    queryStringWhitelist: _list[str]

@typing.type_check_only
class BackendBucketCdnPolicyNegativeCachingPolicy(
    typing_extensions.TypedDict, total=False
):
    code: int
    ttl: int

@typing.type_check_only
class BackendBucketList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[BackendBucket]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendBucketUsedBy(typing_extensions.TypedDict, total=False):
    reference: str

@typing.type_check_only
class BackendCustomMetric(typing_extensions.TypedDict, total=False):
    dryRun: bool
    maxUtilization: float
    name: str

@typing.type_check_only
class BackendService(typing_extensions.TypedDict, total=False):
    affinityCookieTtlSec: int
    backends: _list[Backend]
    cdnPolicy: BackendServiceCdnPolicy
    circuitBreakers: CircuitBreakers
    compressionMode: typing_extensions.Literal["AUTOMATIC", "DISABLED"]
    connectionDraining: ConnectionDraining
    connectionTrackingPolicy: BackendServiceConnectionTrackingPolicy
    consistentHash: ConsistentHashLoadBalancerSettings
    creationTimestamp: str
    customMetrics: _list[BackendServiceCustomMetric]
    customRequestHeaders: _list[str]
    customResponseHeaders: _list[str]
    description: str
    edgeSecurityPolicy: str
    enableCDN: bool
    externalManagedMigrationState: typing_extensions.Literal[
        "PREPARE", "TEST_ALL_TRAFFIC", "TEST_BY_PERCENTAGE"
    ]
    externalManagedMigrationTestingPercentage: float
    failoverPolicy: BackendServiceFailoverPolicy
    fingerprint: str
    healthChecks: _list[str]
    iap: BackendServiceIAP
    id: str
    ipAddressSelectionPolicy: typing_extensions.Literal[
        "IPV4_ONLY",
        "IPV6_ONLY",
        "IP_ADDRESS_SELECTION_POLICY_UNSPECIFIED",
        "PREFER_IPV6",
    ]
    kind: str
    loadBalancingScheme: typing_extensions.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "INTERNAL",
        "INTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
        "INVALID_LOAD_BALANCING_SCHEME",
    ]
    localityLbPolicies: _list[BackendServiceLocalityLoadBalancingPolicyConfig]
    localityLbPolicy: typing_extensions.Literal[
        "INVALID_LB_POLICY",
        "LEAST_REQUEST",
        "MAGLEV",
        "ORIGINAL_DESTINATION",
        "RANDOM",
        "RING_HASH",
        "ROUND_ROBIN",
        "WEIGHTED_MAGLEV",
        "WEIGHTED_ROUND_ROBIN",
    ]
    logConfig: BackendServiceLogConfig
    maxStreamDuration: Duration
    metadatas: dict[str, typing.Any]
    name: str
    network: str
    outlierDetection: OutlierDetection
    port: int
    portName: str
    protocol: typing_extensions.Literal[
        "GRPC", "H2C", "HTTP", "HTTP2", "HTTPS", "SSL", "TCP", "UDP", "UNSPECIFIED"
    ]
    region: str
    securityPolicy: str
    securitySettings: SecuritySettings
    selfLink: str
    serviceBindings: _list[str]
    serviceLbPolicy: str
    sessionAffinity: typing_extensions.Literal[
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
class BackendServiceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceCdnPolicy(typing_extensions.TypedDict, total=False):
    bypassCacheOnRequestHeaders: _list[
        BackendServiceCdnPolicyBypassCacheOnRequestHeader
    ]
    cacheKeyPolicy: CacheKeyPolicy
    cacheMode: typing_extensions.Literal[
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
class BackendServiceCdnPolicyBypassCacheOnRequestHeader(
    typing_extensions.TypedDict, total=False
):
    headerName: str

@typing.type_check_only
class BackendServiceCdnPolicyNegativeCachingPolicy(
    typing_extensions.TypedDict, total=False
):
    code: int
    ttl: int

@typing.type_check_only
class BackendServiceConnectionTrackingPolicy(typing_extensions.TypedDict, total=False):
    connectionPersistenceOnUnhealthyBackends: typing_extensions.Literal[
        "ALWAYS_PERSIST", "DEFAULT_FOR_PROTOCOL", "NEVER_PERSIST"
    ]
    enableStrongAffinity: bool
    idleTimeoutSec: int
    trackingMode: typing_extensions.Literal[
        "INVALID_TRACKING_MODE", "PER_CONNECTION", "PER_SESSION"
    ]

@typing.type_check_only
class BackendServiceCustomMetric(typing_extensions.TypedDict, total=False):
    dryRun: bool
    name: str

@typing.type_check_only
class BackendServiceFailoverPolicy(typing_extensions.TypedDict, total=False):
    disableConnectionDrainOnFailover: bool
    dropTrafficIfUnhealthy: bool
    failoverRatio: float

@typing.type_check_only
class BackendServiceGroupHealth(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    healthStatus: _list[HealthStatus]
    kind: str

@typing.type_check_only
class BackendServiceHttpCookie(typing_extensions.TypedDict, total=False):
    name: str
    path: str
    ttl: Duration

@typing.type_check_only
class BackendServiceIAP(typing_extensions.TypedDict, total=False):
    enabled: bool
    oauth2ClientId: str
    oauth2ClientSecret: str
    oauth2ClientSecretSha256: str

@typing.type_check_only
class BackendServiceList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[BackendService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceListUsable(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[BackendService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class BackendServiceLocalityLoadBalancingPolicyConfig(
    typing_extensions.TypedDict, total=False
):
    customPolicy: BackendServiceLocalityLoadBalancingPolicyConfigCustomPolicy
    policy: BackendServiceLocalityLoadBalancingPolicyConfigPolicy

@typing.type_check_only
class BackendServiceLocalityLoadBalancingPolicyConfigCustomPolicy(
    typing_extensions.TypedDict, total=False
):
    data: str
    name: str

@typing.type_check_only
class BackendServiceLocalityLoadBalancingPolicyConfigPolicy(
    typing_extensions.TypedDict, total=False
):
    name: typing_extensions.Literal[
        "INVALID_LB_POLICY",
        "LEAST_REQUEST",
        "MAGLEV",
        "ORIGINAL_DESTINATION",
        "RANDOM",
        "RING_HASH",
        "ROUND_ROBIN",
        "WEIGHTED_MAGLEV",
        "WEIGHTED_ROUND_ROBIN",
    ]

@typing.type_check_only
class BackendServiceLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    optionalFields: _list[str]
    optionalMode: typing_extensions.Literal[
        "CUSTOM", "EXCLUDE_ALL_OPTIONAL", "INCLUDE_ALL_OPTIONAL"
    ]
    sampleRate: float

@typing.type_check_only
class BackendServiceReference(typing_extensions.TypedDict, total=False):
    backendService: str

@typing.type_check_only
class BackendServiceTlsSettings(typing_extensions.TypedDict, total=False):
    authenticationConfig: str
    sni: str
    subjectAltNames: _list[BackendServiceTlsSettingsSubjectAltName]

@typing.type_check_only
class BackendServiceTlsSettingsSubjectAltName(typing_extensions.TypedDict, total=False):
    dnsName: str
    uniformResourceIdentifier: str

@typing.type_check_only
class BackendServiceUsedBy(typing_extensions.TypedDict, total=False):
    reference: str

@typing.type_check_only
class BackendServicesGetEffectiveSecurityPoliciesResponse(
    typing_extensions.TypedDict, total=False
):
    securityPolicies: _list[SecurityPolicy]

@typing.type_check_only
class BackendServicesScopedList(typing_extensions.TypedDict, total=False):
    backendServices: _list[BackendService]
    warning: dict[str, typing.Any]

@typing.type_check_only
class BfdPacket(typing_extensions.TypedDict, total=False):
    authenticationPresent: bool
    controlPlaneIndependent: bool
    demand: bool
    diagnostic: typing_extensions.Literal[
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
    state: typing_extensions.Literal[
        "ADMIN_DOWN", "DOWN", "INIT", "STATE_UNSPECIFIED", "UP"
    ]
    version: int
    yourDiscriminator: int

@typing.type_check_only
class BfdStatus(typing_extensions.TypedDict, total=False):
    bfdSessionInitializationMode: typing_extensions.Literal[
        "ACTIVE", "DISABLED", "PASSIVE"
    ]
    configUpdateTimestampMicros: str
    controlPacketCounts: BfdStatusPacketCounts
    controlPacketIntervals: _list[PacketIntervals]
    localDiagnostic: typing_extensions.Literal[
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
    localState: typing_extensions.Literal[
        "ADMIN_DOWN", "DOWN", "INIT", "STATE_UNSPECIFIED", "UP"
    ]
    negotiatedLocalControlTxIntervalMs: int
    rxPacket: BfdPacket
    txPacket: BfdPacket
    uptimeMs: str

@typing.type_check_only
class BfdStatusPacketCounts(typing_extensions.TypedDict, total=False):
    numRx: int
    numRxRejected: int
    numRxSuccessful: int
    numTx: int

@typing.type_check_only
class BgpRoute(typing_extensions.TypedDict, total=False):
    asPaths: _list[BgpRouteAsPath]
    communities: _list[str]
    destination: BgpRouteNetworkLayerReachabilityInformation
    med: int
    origin: typing_extensions.Literal[
        "BGP_ORIGIN_EGP", "BGP_ORIGIN_IGP", "BGP_ORIGIN_INCOMPLETE"
    ]

@typing.type_check_only
class BgpRouteAsPath(typing_extensions.TypedDict, total=False):
    asns: _list[int]
    type: typing_extensions.Literal["AS_PATH_TYPE_SEQUENCE", "AS_PATH_TYPE_SET"]

@typing.type_check_only
class BgpRouteNetworkLayerReachabilityInformation(
    typing_extensions.TypedDict, total=False
):
    pathId: int
    prefix: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BulkInsertDiskResource(typing_extensions.TypedDict, total=False):
    sourceConsistencyGroupPolicy: str

@typing.type_check_only
class BulkInsertInstanceResource(typing_extensions.TypedDict, total=False):
    count: str
    instanceProperties: InstanceProperties
    locationPolicy: LocationPolicy
    minCount: str
    namePattern: str
    perInstanceProperties: dict[str, typing.Any]
    sourceInstanceTemplate: str

@typing.type_check_only
class BulkInsertInstanceResourcePerInstanceProperties(
    typing_extensions.TypedDict, total=False
):
    hostname: str
    name: str

@typing.type_check_only
class BulkInsertOperationStatus(typing_extensions.TypedDict, total=False):
    createdVmCount: int
    deletedVmCount: int
    failedToCreateVmCount: int
    status: typing_extensions.Literal[
        "CREATING", "DONE", "ROLLING_BACK", "STATUS_UNSPECIFIED"
    ]
    targetVmCount: int

@typing.type_check_only
class BundledLocalSsds(typing_extensions.TypedDict, total=False):
    defaultInterface: str
    partitionCount: int

@typing.type_check_only
class CacheInvalidationRule(typing_extensions.TypedDict, total=False):
    host: str
    path: str

@typing.type_check_only
class CacheKeyPolicy(typing_extensions.TypedDict, total=False):
    includeHost: bool
    includeHttpHeaders: _list[str]
    includeNamedCookies: _list[str]
    includeProtocol: bool
    includeQueryString: bool
    queryStringBlacklist: _list[str]
    queryStringWhitelist: _list[str]

@typing.type_check_only
class CircuitBreakers(typing_extensions.TypedDict, total=False):
    connectTimeout: Duration
    maxConnections: int
    maxPendingRequests: int
    maxRequests: int
    maxRequestsPerConnection: int
    maxRetries: int

@typing.type_check_only
class Commitment(typing_extensions.TypedDict, total=False):
    autoRenew: bool
    category: typing_extensions.Literal["CATEGORY_UNSPECIFIED", "LICENSE", "MACHINE"]
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
    plan: typing_extensions.Literal["INVALID", "THIRTY_SIX_MONTH", "TWELVE_MONTH"]
    region: str
    reservations: _list[Reservation]
    resourceStatus: CommitmentResourceStatus
    resources: _list[ResourceCommitment]
    selfLink: str
    splitSourceCommitment: str
    startTimestamp: str
    status: typing_extensions.Literal[
        "ACTIVE", "CANCELLED", "CREATING", "EXPIRED", "NOT_YET_ACTIVE"
    ]
    statusMessage: str
    type: typing_extensions.Literal[
        "ACCELERATOR_OPTIMIZED",
        "ACCELERATOR_OPTIMIZED_A3",
        "ACCELERATOR_OPTIMIZED_A3_MEGA",
        "COMPUTE_OPTIMIZED",
        "COMPUTE_OPTIMIZED_C2D",
        "COMPUTE_OPTIMIZED_C3",
        "COMPUTE_OPTIMIZED_C3D",
        "COMPUTE_OPTIMIZED_H3",
        "GENERAL_PURPOSE",
        "GENERAL_PURPOSE_C4",
        "GENERAL_PURPOSE_C4A",
        "GENERAL_PURPOSE_E2",
        "GENERAL_PURPOSE_N2",
        "GENERAL_PURPOSE_N2D",
        "GENERAL_PURPOSE_N4",
        "GENERAL_PURPOSE_T2D",
        "GRAPHICS_OPTIMIZED",
        "MEMORY_OPTIMIZED",
        "MEMORY_OPTIMIZED_M3",
        "MEMORY_OPTIMIZED_X4_16TB",
        "MEMORY_OPTIMIZED_X4_24TB",
        "MEMORY_OPTIMIZED_X4_32TB",
        "STORAGE_OPTIMIZED_Z3",
        "TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class CommitmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class CommitmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Commitment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class CommitmentResourceStatus(typing_extensions.TypedDict, total=False):
    customTermEligibilityEndTimestamp: str

@typing.type_check_only
class CommitmentsScopedList(typing_extensions.TypedDict, total=False):
    commitments: _list[Commitment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
    confidentialInstanceType: typing_extensions.Literal[
        "CONFIDENTIAL_INSTANCE_TYPE_UNSPECIFIED", "SEV", "SEV_SNP", "TDX"
    ]
    enableConfidentialCompute: bool

@typing.type_check_only
class ConnectionDraining(typing_extensions.TypedDict, total=False):
    drainingTimeoutSec: int

@typing.type_check_only
class ConsistentHashLoadBalancerSettings(typing_extensions.TypedDict, total=False):
    httpCookie: ConsistentHashLoadBalancerSettingsHttpCookie
    httpHeaderName: str
    minimumRingSize: str

@typing.type_check_only
class ConsistentHashLoadBalancerSettingsHttpCookie(
    typing_extensions.TypedDict, total=False
):
    name: str
    path: str
    ttl: Duration

@typing.type_check_only
class CorsPolicy(typing_extensions.TypedDict, total=False):
    allowCredentials: bool
    allowHeaders: _list[str]
    allowMethods: _list[str]
    allowOriginRegexes: _list[str]
    allowOrigins: _list[str]
    disabled: bool
    exposeHeaders: _list[str]
    maxAge: int

@typing.type_check_only
class CustomErrorResponsePolicy(typing_extensions.TypedDict, total=False):
    errorResponseRules: _list[CustomErrorResponsePolicyCustomErrorResponseRule]
    errorService: str

@typing.type_check_only
class CustomErrorResponsePolicyCustomErrorResponseRule(
    typing_extensions.TypedDict, total=False
):
    matchResponseCodes: _list[str]
    overrideResponseCode: int
    path: str

@typing.type_check_only
class CustomerEncryptionKey(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyServiceAccount: str
    rawKey: str
    rsaEncryptedKey: str
    sha256: str

@typing.type_check_only
class CustomerEncryptionKeyProtectedDisk(typing_extensions.TypedDict, total=False):
    diskEncryptionKey: CustomerEncryptionKey
    source: str

@typing.type_check_only
class DeprecationStatus(typing_extensions.TypedDict, total=False):
    deleted: str
    deprecated: str
    obsolete: str
    replacement: str
    state: typing_extensions.Literal["ACTIVE", "DELETED", "DEPRECATED", "OBSOLETE"]
    stateOverride: RolloutPolicy

@typing.type_check_only
class Disk(typing_extensions.TypedDict, total=False):
    accessMode: typing_extensions.Literal[
        "READ_ONLY_MANY", "READ_WRITE_MANY", "READ_WRITE_SINGLE"
    ]
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
    asyncPrimaryDisk: DiskAsyncReplication
    asyncSecondaryDisks: dict[str, typing.Any]
    creationTimestamp: str
    description: str
    diskEncryptionKey: CustomerEncryptionKey
    enableConfidentialCompute: bool
    eraseWindowsVssSignature: bool
    guestOsFeatures: _list[GuestOsFeature]
    id: str
    interface: typing_extensions.Literal["NVME", "SCSI", "UNSPECIFIED"]
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
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey
    sourceSnapshotId: str
    sourceStorageObject: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RESTORING", "UNAVAILABLE"
    ]
    storagePool: str
    storageType: typing_extensions.Literal["HDD", "SSD"]
    type: str
    userLicenses: _list[str]
    users: _list[str]
    zone: str

@typing.type_check_only
class DiskAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskAsyncReplication(typing_extensions.TypedDict, total=False):
    consistencyGroupPolicy: str
    consistencyGroupPolicyId: str
    disk: str
    diskId: str

@typing.type_check_only
class DiskAsyncReplicationList(typing_extensions.TypedDict, total=False):
    asyncReplicationDisk: DiskAsyncReplication

@typing.type_check_only
class DiskInstantiationConfig(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    customImage: str
    deviceName: str
    instantiateFrom: typing_extensions.Literal[
        "ATTACH_READ_ONLY",
        "BLANK",
        "CUSTOM_IMAGE",
        "DEFAULT",
        "DO_NOT_INCLUDE",
        "SOURCE_IMAGE",
        "SOURCE_IMAGE_FAMILY",
    ]

@typing.type_check_only
class DiskList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Disk]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskMoveRequest(typing_extensions.TypedDict, total=False):
    destinationZone: str
    targetDisk: str

@typing.type_check_only
class DiskParams(typing_extensions.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class DiskResourceStatus(typing_extensions.TypedDict, total=False):
    asyncPrimaryDisk: DiskResourceStatusAsyncReplicationStatus
    asyncSecondaryDisks: dict[str, typing.Any]

@typing.type_check_only
class DiskResourceStatusAsyncReplicationStatus(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "ACTIVE", "CREATED", "STARTING", "STATE_UNSPECIFIED", "STOPPED", "STOPPING"
    ]

@typing.type_check_only
class DiskType(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    defaultDiskSizeGb: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    validDiskSize: str
    zone: str

@typing.type_check_only
class DiskTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class DiskTypesScopedList(typing_extensions.TypedDict, total=False):
    diskTypes: _list[DiskType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DisksAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class DisksRemoveResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class DisksResizeRequest(typing_extensions.TypedDict, total=False):
    sizeGb: str

@typing.type_check_only
class DisksScopedList(typing_extensions.TypedDict, total=False):
    disks: _list[Disk]
    warning: dict[str, typing.Any]

@typing.type_check_only
class DisksStartAsyncReplicationRequest(typing_extensions.TypedDict, total=False):
    asyncSecondaryDisk: str

@typing.type_check_only
class DisksStopGroupAsyncReplicationResource(typing_extensions.TypedDict, total=False):
    resourcePolicy: str

@typing.type_check_only
class DisplayDevice(typing_extensions.TypedDict, total=False):
    enableDisplay: bool

@typing.type_check_only
class DistributionPolicy(typing_extensions.TypedDict, total=False):
    targetShape: typing_extensions.Literal["ANY", "ANY_SINGLE_ZONE", "BALANCED", "EVEN"]
    zones: _list[DistributionPolicyZoneConfiguration]

@typing.type_check_only
class DistributionPolicyZoneConfiguration(typing_extensions.TypedDict, total=False):
    zone: str

@typing.type_check_only
class Duration(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

@typing.type_check_only
class ErrorInfo(typing_extensions.TypedDict, total=False):
    domain: str
    metadatas: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class ExchangedPeeringRoute(typing_extensions.TypedDict, total=False):
    destRange: str
    imported: bool
    nextHopRegion: str
    priority: int
    type: typing_extensions.Literal[
        "DYNAMIC_PEERING_ROUTE", "STATIC_PEERING_ROUTE", "SUBNET_PEERING_ROUTE"
    ]

@typing.type_check_only
class ExchangedPeeringRoutesList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[ExchangedPeeringRoute]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalVpnGateway(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    interfaces: _list[ExternalVpnGatewayInterface]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    redundancyType: typing_extensions.Literal[
        "FOUR_IPS_REDUNDANCY", "SINGLE_IP_INTERNALLY_REDUNDANT", "TWO_IPS_REDUNDANCY"
    ]
    selfLink: str

@typing.type_check_only
class ExternalVpnGatewayInterface(typing_extensions.TypedDict, total=False):
    id: int
    ipAddress: str
    ipv6Address: str

@typing.type_check_only
class ExternalVpnGatewayList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[ExternalVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class FileContentBuffer(typing_extensions.TypedDict, total=False):
    content: str
    fileType: typing_extensions.Literal["BIN", "UNDEFINED", "X509"]

@typing.type_check_only
class Firewall(typing_extensions.TypedDict, total=False):
    allowed: _list[dict[str, typing.Any]]
    creationTimestamp: str
    denied: _list[dict[str, typing.Any]]
    description: str
    destinationRanges: _list[str]
    direction: typing_extensions.Literal["EGRESS", "INGRESS"]
    disabled: bool
    enableLogging: bool
    id: str
    kind: str
    logConfig: FirewallLogConfig
    name: str
    network: str
    priority: int
    selfLink: str
    sourceRanges: _list[str]
    sourceServiceAccounts: _list[str]
    sourceTags: _list[str]
    targetServiceAccounts: _list[str]
    targetTags: _list[str]

@typing.type_check_only
class FirewallList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Firewall]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class FirewallLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    metadata: typing_extensions.Literal["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]

@typing.type_check_only
class FirewallPoliciesListAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    associations: _list[FirewallPolicyAssociation]
    kind: str

@typing.type_check_only
class FirewallPoliciesScopedList(typing_extensions.TypedDict, total=False):
    firewallPolicies: _list[FirewallPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FirewallPolicy(typing_extensions.TypedDict, total=False):
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
    region: str
    ruleTupleCount: int
    rules: _list[FirewallPolicyRule]
    selfLink: str
    selfLinkWithId: str
    shortName: str

@typing.type_check_only
class FirewallPolicyAssociation(typing_extensions.TypedDict, total=False):
    attachmentTarget: str
    displayName: str
    firewallPolicyId: str
    name: str
    shortName: str

@typing.type_check_only
class FirewallPolicyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[FirewallPolicy]
    kind: str
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class FirewallPolicyRule(typing_extensions.TypedDict, total=False):
    action: str
    description: str
    direction: typing_extensions.Literal["EGRESS", "INGRESS"]
    disabled: bool
    enableLogging: bool
    kind: str
    match: FirewallPolicyRuleMatcher
    priority: int
    ruleName: str
    ruleTupleCount: int
    securityProfileGroup: str
    targetResources: _list[str]
    targetSecureTags: _list[FirewallPolicyRuleSecureTag]
    targetServiceAccounts: _list[str]
    tlsInspect: bool

@typing.type_check_only
class FirewallPolicyRuleMatcher(typing_extensions.TypedDict, total=False):
    destAddressGroups: _list[str]
    destFqdns: _list[str]
    destIpRanges: _list[str]
    destNetworkScope: typing_extensions.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    destRegionCodes: _list[str]
    destThreatIntelligences: _list[str]
    layer4Configs: _list[FirewallPolicyRuleMatcherLayer4Config]
    srcAddressGroups: _list[str]
    srcFqdns: _list[str]
    srcIpRanges: _list[str]
    srcNetworkScope: typing_extensions.Literal[
        "INTERNET", "INTRA_VPC", "NON_INTERNET", "UNSPECIFIED", "VPC_NETWORKS"
    ]
    srcNetworks: _list[str]
    srcRegionCodes: _list[str]
    srcSecureTags: _list[FirewallPolicyRuleSecureTag]
    srcThreatIntelligences: _list[str]

@typing.type_check_only
class FirewallPolicyRuleMatcherLayer4Config(typing_extensions.TypedDict, total=False):
    ipProtocol: str
    ports: _list[str]

@typing.type_check_only
class FirewallPolicyRuleSecureTag(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal["EFFECTIVE", "INEFFECTIVE"]

@typing.type_check_only
class FixedOrPercent(typing_extensions.TypedDict, total=False):
    calculated: int
    fixed: int
    percent: int

@typing.type_check_only
class ForwardingRule(typing_extensions.TypedDict, total=False):
    IPAddress: str
    IPProtocol: typing_extensions.Literal[
        "AH", "ESP", "ICMP", "L3_DEFAULT", "SCTP", "TCP", "UDP"
    ]
    allPorts: bool
    allowGlobalAccess: bool
    allowPscGlobalAccess: bool
    allowPscPacketInjection: bool
    backendService: str
    baseForwardingRule: str
    creationTimestamp: str
    description: str
    externalManagedBackendBucketMigrationState: typing_extensions.Literal[
        "PREPARE", "TEST_ALL_TRAFFIC", "TEST_BY_PERCENTAGE"
    ]
    externalManagedBackendBucketMigrationTestingPercentage: float
    fingerprint: str
    id: str
    ipCollection: str
    ipVersion: typing_extensions.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    isMirroringCollector: bool
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    loadBalancingScheme: typing_extensions.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "INTERNAL",
        "INTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
        "INVALID",
    ]
    metadataFilters: _list[MetadataFilter]
    name: str
    network: str
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD", "PREMIUM", "STANDARD", "STANDARD_OVERRIDES_FIXED_STANDARD"
    ]
    noAutomateDnsZone: bool
    portRange: str
    ports: _list[str]
    pscConnectionId: str
    pscConnectionStatus: typing_extensions.Literal[
        "ACCEPTED",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]
    region: str
    selfLink: str
    serviceDirectoryRegistrations: _list[ForwardingRuleServiceDirectoryRegistration]
    serviceLabel: str
    serviceName: str
    sourceIpRanges: _list[str]
    subnetwork: str
    target: str

@typing.type_check_only
class ForwardingRuleAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ForwardingRuleList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[ForwardingRule]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ForwardingRuleReference(typing_extensions.TypedDict, total=False):
    forwardingRule: str

@typing.type_check_only
class ForwardingRuleServiceDirectoryRegistration(
    typing_extensions.TypedDict, total=False
):
    namespace: str
    service: str
    serviceDirectoryRegion: str

@typing.type_check_only
class ForwardingRulesScopedList(typing_extensions.TypedDict, total=False):
    forwardingRules: _list[ForwardingRule]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FutureReservation(typing_extensions.TypedDict, total=False):
    autoCreatedReservationsDeleteTime: str
    autoCreatedReservationsDuration: Duration
    autoDeleteAutoCreatedReservations: bool
    commitmentInfo: FutureReservationCommitmentInfo
    creationTimestamp: str
    deploymentType: typing_extensions.Literal[
        "DENSE", "DEPLOYMENT_TYPE_UNSPECIFIED", "FLEXIBLE"
    ]
    description: str
    id: str
    kind: str
    name: str
    namePrefix: str
    planningStatus: typing_extensions.Literal[
        "DRAFT", "PLANNING_STATUS_UNSPECIFIED", "SUBMITTED"
    ]
    reservationName: str
    schedulingType: typing_extensions.Literal[
        "GROUPED", "GROUP_MAINTENANCE_TYPE_UNSPECIFIED", "INDEPENDENT"
    ]
    selfLink: str
    selfLinkWithId: str
    shareSettings: ShareSettings
    specificReservationRequired: bool
    specificSkuProperties: FutureReservationSpecificSKUProperties
    status: FutureReservationStatus
    timeWindow: FutureReservationTimeWindow
    zone: str

@typing.type_check_only
class FutureReservationCommitmentInfo(typing_extensions.TypedDict, total=False):
    commitmentName: str
    commitmentPlan: typing_extensions.Literal[
        "INVALID", "THIRTY_SIX_MONTH", "TWELVE_MONTH"
    ]
    previousCommitmentTerms: typing_extensions.Literal[
        "EXTEND", "PREVIOUSCOMMITMENTTERM_UNSPECIFIED"
    ]

@typing.type_check_only
class FutureReservationSpecificSKUProperties(typing_extensions.TypedDict, total=False):
    instanceProperties: AllocationSpecificSKUAllocationReservedInstanceProperties
    sourceInstanceTemplate: str
    totalCount: str

@typing.type_check_only
class FutureReservationStatus(typing_extensions.TypedDict, total=False):
    amendmentStatus: typing_extensions.Literal[
        "AMENDMENT_APPROVED",
        "AMENDMENT_DECLINED",
        "AMENDMENT_IN_REVIEW",
        "AMENDMENT_STATUS_UNSPECIFIED",
    ]
    autoCreatedReservations: _list[str]
    existingMatchingUsageInfo: FutureReservationStatusExistingMatchingUsageInfo
    fulfilledCount: str
    lastKnownGoodState: FutureReservationStatusLastKnownGoodState
    lockTime: str
    procurementStatus: typing_extensions.Literal[
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

@typing.type_check_only
class FutureReservationStatusExistingMatchingUsageInfo(
    typing_extensions.TypedDict, total=False
):
    count: str
    timestamp: str

@typing.type_check_only
class FutureReservationStatusLastKnownGoodState(
    typing_extensions.TypedDict, total=False
):
    description: str
    existingMatchingUsageInfo: FutureReservationStatusExistingMatchingUsageInfo
    futureReservationSpecs: (
        FutureReservationStatusLastKnownGoodStateFutureReservationSpecs
    )
    lockTime: str
    namePrefix: str
    procurementStatus: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    shareSettings: ShareSettings
    specificSkuProperties: FutureReservationSpecificSKUProperties
    timeWindow: FutureReservationTimeWindow

@typing.type_check_only
class FutureReservationStatusSpecificSKUProperties(
    typing_extensions.TypedDict, total=False
):
    sourceInstanceTemplateId: str

@typing.type_check_only
class FutureReservationTimeWindow(typing_extensions.TypedDict, total=False):
    duration: Duration
    endTime: str
    startTime: str

@typing.type_check_only
class FutureReservationsAggregatedListResponse(
    typing_extensions.TypedDict, total=False
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
class FutureReservationsListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[FutureReservation]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class FutureReservationsScopedList(typing_extensions.TypedDict, total=False):
    futureReservations: _list[FutureReservation]
    warning: dict[str, typing.Any]

@typing.type_check_only
class GRPCHealthCheck(typing_extensions.TypedDict, total=False):
    grpcServiceName: str
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]

@typing.type_check_only
class GlobalAddressesMoveRequest(typing_extensions.TypedDict, total=False):
    description: str
    destinationAddress: str

@typing.type_check_only
class GlobalNetworkEndpointGroupsAttachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class GlobalNetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class GlobalOrganizationSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class GlobalSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class GroupMaintenanceInfo(typing_extensions.TypedDict, total=False):
    maintenanceOngoingCount: int
    maintenancePendingCount: int
    schedulingType: typing_extensions.Literal[
        "GROUPED", "GROUP_MAINTENANCE_TYPE_UNSPECIFIED", "INDEPENDENT"
    ]
    upcomingGroupMaintenance: UpcomingMaintenance

@typing.type_check_only
class GuestAttributes(typing_extensions.TypedDict, total=False):
    kind: str
    queryPath: str
    queryValue: GuestAttributesValue
    selfLink: str
    variableKey: str
    variableValue: str

@typing.type_check_only
class GuestAttributesEntry(typing_extensions.TypedDict, total=False):
    key: str
    namespace: str
    value: str

@typing.type_check_only
class GuestAttributesValue(typing_extensions.TypedDict, total=False):
    items: _list[GuestAttributesEntry]

@typing.type_check_only
class GuestOsFeature(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "FEATURE_TYPE_UNSPECIFIED",
        "GVNIC",
        "IDPF",
        "MULTI_IP_SUBNET",
        "SECURE_BOOT",
        "SEV_CAPABLE",
        "SEV_LIVE_MIGRATABLE",
        "SEV_LIVE_MIGRATABLE_V2",
        "SEV_SNP_CAPABLE",
        "TDX_CAPABLE",
        "UEFI_COMPATIBLE",
        "VIRTIO_SCSI_MULTIQUEUE",
        "WINDOWS",
    ]

@typing.type_check_only
class HTTP2HealthCheck(typing_extensions.TypedDict, total=False):
    host: str
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    requestPath: str
    response: str

@typing.type_check_only
class HTTPHealthCheck(typing_extensions.TypedDict, total=False):
    host: str
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    requestPath: str
    response: str

@typing.type_check_only
class HTTPSHealthCheck(typing_extensions.TypedDict, total=False):
    host: str
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    requestPath: str
    response: str

@typing.type_check_only
class HealthCheck(typing_extensions.TypedDict, total=False):
    checkIntervalSec: int
    creationTimestamp: str
    description: str
    grpcHealthCheck: GRPCHealthCheck
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
    sourceRegions: _list[str]
    sslHealthCheck: SSLHealthCheck
    tcpHealthCheck: TCPHealthCheck
    timeoutSec: int
    type: typing_extensions.Literal[
        "GRPC", "HTTP", "HTTP2", "HTTPS", "INVALID", "SSL", "TCP"
    ]
    unhealthyThreshold: int

@typing.type_check_only
class HealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[HealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthCheckLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool

@typing.type_check_only
class HealthCheckReference(typing_extensions.TypedDict, total=False):
    healthCheck: str

@typing.type_check_only
class HealthCheckService(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    healthChecks: _list[str]
    healthStatusAggregationPolicy: typing_extensions.Literal["AND", "NO_AGGREGATION"]
    healthStatusAggregationStrategy: typing_extensions.Literal["AND", "NO_AGGREGATION"]
    id: str
    kind: str
    name: str
    networkEndpointGroups: _list[str]
    notificationEndpoints: _list[str]
    region: str
    selfLink: str

@typing.type_check_only
class HealthCheckServiceReference(typing_extensions.TypedDict, total=False):
    healthCheckService: str

@typing.type_check_only
class HealthCheckServicesList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[HealthCheckService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthChecksAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthChecksScopedList(typing_extensions.TypedDict, total=False):
    healthChecks: _list[HealthCheck]
    warning: dict[str, typing.Any]

@typing.type_check_only
class HealthStatus(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    forwardingRule: str
    forwardingRuleIp: str
    healthState: typing_extensions.Literal["HEALTHY", "UNHEALTHY"]
    instance: str
    ipAddress: str
    ipv6Address: str
    ipv6HealthState: typing_extensions.Literal["HEALTHY", "UNHEALTHY"]
    port: int
    weight: str
    weightError: typing_extensions.Literal[
        "INVALID_WEIGHT", "MISSING_WEIGHT", "UNAVAILABLE_WEIGHT", "WEIGHT_NONE"
    ]

@typing.type_check_only
class HealthStatusForNetworkEndpoint(typing_extensions.TypedDict, total=False):
    backendService: BackendServiceReference
    forwardingRule: ForwardingRuleReference
    healthCheck: HealthCheckReference
    healthCheckService: HealthCheckServiceReference
    healthState: typing_extensions.Literal[
        "DRAINING", "HEALTHY", "UNHEALTHY", "UNKNOWN"
    ]
    ipv6HealthState: typing_extensions.Literal[
        "DRAINING", "HEALTHY", "UNHEALTHY", "UNKNOWN"
    ]

@typing.type_check_only
class Help(typing_extensions.TypedDict, total=False):
    links: _list[HelpLink]

@typing.type_check_only
class HelpLink(typing_extensions.TypedDict, total=False):
    description: str
    url: str

@typing.type_check_only
class HostRule(typing_extensions.TypedDict, total=False):
    description: str
    hosts: _list[str]
    pathMatcher: str

@typing.type_check_only
class HttpFaultAbort(typing_extensions.TypedDict, total=False):
    httpStatus: int
    percentage: float

@typing.type_check_only
class HttpFaultDelay(typing_extensions.TypedDict, total=False):
    fixedDelay: Duration
    percentage: float

@typing.type_check_only
class HttpFaultInjection(typing_extensions.TypedDict, total=False):
    abort: HttpFaultAbort
    delay: HttpFaultDelay

@typing.type_check_only
class HttpFilterConfig(typing_extensions.TypedDict, total=False):
    config: str
    configTypeUrl: str
    filterName: str

@typing.type_check_only
class HttpHeaderAction(typing_extensions.TypedDict, total=False):
    requestHeadersToAdd: _list[HttpHeaderOption]
    requestHeadersToRemove: _list[str]
    responseHeadersToAdd: _list[HttpHeaderOption]
    responseHeadersToRemove: _list[str]

@typing.type_check_only
class HttpHeaderMatch(typing_extensions.TypedDict, total=False):
    exactMatch: str
    headerName: str
    invertMatch: bool
    prefixMatch: str
    presentMatch: bool
    rangeMatch: Int64RangeMatch
    regexMatch: str
    suffixMatch: str

@typing.type_check_only
class HttpHeaderOption(typing_extensions.TypedDict, total=False):
    headerName: str
    headerValue: str
    replace: bool

@typing.type_check_only
class HttpHealthCheck(typing_extensions.TypedDict, total=False):
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
    timeoutSec: int
    unhealthyThreshold: int

@typing.type_check_only
class HttpHealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[HttpHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class HttpQueryParameterMatch(typing_extensions.TypedDict, total=False):
    exactMatch: str
    name: str
    presentMatch: bool
    regexMatch: str

@typing.type_check_only
class HttpRedirectAction(typing_extensions.TypedDict, total=False):
    hostRedirect: str
    httpsRedirect: bool
    pathRedirect: str
    prefixRedirect: str
    redirectResponseCode: typing_extensions.Literal[
        "FOUND",
        "MOVED_PERMANENTLY_DEFAULT",
        "PERMANENT_REDIRECT",
        "SEE_OTHER",
        "TEMPORARY_REDIRECT",
    ]
    stripQuery: bool

@typing.type_check_only
class HttpRetryPolicy(typing_extensions.TypedDict, total=False):
    numRetries: int
    perTryTimeout: Duration
    retryConditions: _list[str]

@typing.type_check_only
class HttpRouteAction(typing_extensions.TypedDict, total=False):
    corsPolicy: CorsPolicy
    faultInjectionPolicy: HttpFaultInjection
    maxStreamDuration: Duration
    requestMirrorPolicy: RequestMirrorPolicy
    retryPolicy: HttpRetryPolicy
    timeout: Duration
    urlRewrite: UrlRewrite
    weightedBackendServices: _list[WeightedBackendService]

@typing.type_check_only
class HttpRouteRule(typing_extensions.TypedDict, total=False):
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
class HttpRouteRuleMatch(typing_extensions.TypedDict, total=False):
    fullPathMatch: str
    headerMatches: _list[HttpHeaderMatch]
    ignoreCase: bool
    metadataFilters: _list[MetadataFilter]
    pathTemplateMatch: str
    prefixMatch: str
    queryParameterMatches: _list[HttpQueryParameterMatch]
    regexMatch: str

@typing.type_check_only
class HttpsHealthCheck(typing_extensions.TypedDict, total=False):
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
    timeoutSec: int
    unhealthyThreshold: int

@typing.type_check_only
class HttpsHealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[HttpsHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
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
    rawDisk: dict[str, typing.Any]
    rolloutOverride: RolloutPolicy
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
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
    sourceType: typing_extensions.Literal["RAW"]
    status: typing_extensions.Literal["DELETING", "FAILED", "PENDING", "READY"]
    storageLocations: _list[str]
    userLicenses: _list[str]

@typing.type_check_only
class ImageFamilyView(typing_extensions.TypedDict, total=False):
    image: Image

@typing.type_check_only
class ImageList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Image]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InitialStateConfig(typing_extensions.TypedDict, total=False):
    dbs: _list[FileContentBuffer]
    dbxs: _list[FileContentBuffer]
    keks: _list[FileContentBuffer]
    pk: FileContentBuffer

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
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
    instanceEncryptionKey: CustomerEncryptionKey
    keyRevocationActionType: typing_extensions.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    lastStartTimestamp: str
    lastStopTimestamp: str
    lastSuspendedTimestamp: str
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    name: str
    networkInterfaces: _list[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    params: InstanceParams
    partnerMetadata: dict[str, typing.Any]
    postKeyRevocationActionType: typing_extensions.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    privateIpv6GoogleAccess: typing_extensions.Literal[
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
    selfLink: str
    serviceAccounts: _list[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedInstanceIntegrityPolicy: ShieldedInstanceIntegrityPolicy
    shieldedVmConfig: ShieldedVmConfig
    shieldedVmIntegrityPolicy: ShieldedVmIntegrityPolicy
    sourceMachineImage: str
    sourceMachineImageEncryptionKey: CustomerEncryptionKey
    startRestricted: bool
    status: typing_extensions.Literal[
        "DEPROVISIONING",
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
    zone: str

@typing.type_check_only
class InstanceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceConsumptionData(typing_extensions.TypedDict, total=False):
    consumptionInfo: InstanceConsumptionInfo
    instance: str

@typing.type_check_only
class InstanceConsumptionInfo(typing_extensions.TypedDict, total=False):
    guestCpus: int
    localSsdGb: int
    memoryMb: int
    minNodeCpus: int

@typing.type_check_only
class InstanceGroup(typing_extensions.TypedDict, total=False):
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
    size: int
    subnetwork: str
    zone: str

@typing.type_check_only
class InstanceGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManager(typing_extensions.TypedDict, total=False):
    allInstancesConfig: InstanceGroupManagerAllInstancesConfig
    autoHealingPolicies: _list[InstanceGroupManagerAutoHealingPolicy]
    baseInstanceName: str
    creationTimestamp: str
    currentActions: InstanceGroupManagerActionsSummary
    description: str
    distributionPolicy: DistributionPolicy
    failoverAction: typing_extensions.Literal["NO_FAILOVER", "UNKNOWN"]
    fingerprint: str
    id: str
    instanceFlexibilityPolicy: InstanceGroupManagerInstanceFlexibilityPolicy
    instanceGroup: str
    instanceLifecyclePolicy: InstanceGroupManagerInstanceLifecyclePolicy
    instanceTemplate: str
    kind: str
    listManagedInstancesResults: typing_extensions.Literal["PAGELESS", "PAGINATED"]
    multiMig: str
    name: str
    namedPorts: _list[NamedPort]
    params: InstanceGroupManagerParams
    region: str
    resourcePolicies: InstanceGroupManagerResourcePolicies
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    serviceAccount: str
    standbyPolicy: InstanceGroupManagerStandbyPolicy
    statefulPolicy: StatefulPolicy
    status: InstanceGroupManagerStatus
    targetPools: _list[str]
    targetSize: int
    targetStoppedSize: int
    targetSuspendedSize: int
    updatePolicy: InstanceGroupManagerUpdatePolicy
    versions: _list[InstanceGroupManagerVersion]
    zone: str

@typing.type_check_only
class InstanceGroupManagerActionsSummary(typing_extensions.TypedDict, total=False):
    abandoning: int
    creating: int
    creatingWithoutRetries: int
    deleting: int
    none: int
    recreating: int
    refreshing: int
    restarting: int
    resuming: int
    starting: int
    stopping: int
    suspending: int
    verifying: int

@typing.type_check_only
class InstanceGroupManagerAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerAllInstancesConfig(typing_extensions.TypedDict, total=False):
    properties: InstancePropertiesPatch

@typing.type_check_only
class InstanceGroupManagerAutoHealingPolicy(typing_extensions.TypedDict, total=False):
    healthCheck: str
    initialDelaySec: int

@typing.type_check_only
class InstanceGroupManagerInstanceFlexibilityPolicy(
    typing_extensions.TypedDict, total=False
):
    instanceSelections: dict[str, typing.Any]
    provisioningModelMix: (
        InstanceGroupManagerInstanceFlexibilityPolicyProvisioningModelMix
    )

@typing.type_check_only
class InstanceGroupManagerInstanceFlexibilityPolicyInstanceSelection(
    typing_extensions.TypedDict, total=False
):
    machineTypes: _list[str]
    rank: int

@typing.type_check_only
class InstanceGroupManagerInstanceFlexibilityPolicyProvisioningModelMix(
    typing_extensions.TypedDict, total=False
):
    standardCapacityBase: int
    standardCapacityPercentAboveBase: int

@typing.type_check_only
class InstanceGroupManagerInstanceLifecyclePolicy(
    typing_extensions.TypedDict, total=False
):
    defaultActionOnFailure: typing_extensions.Literal["DELETE", "DO_NOTHING", "REPAIR"]
    forceUpdateOnRepair: typing_extensions.Literal["NO", "YES"]

@typing.type_check_only
class InstanceGroupManagerList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerParams(typing_extensions.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerResizeRequest(typing_extensions.TypedDict, total=False):
    count: int
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    region: str
    requestedRunDuration: Duration
    resizeBy: int
    selfLink: str
    selfLinkWithId: str
    state: typing_extensions.Literal[
        "ACCEPTED",
        "CANCELLED",
        "CREATING",
        "FAILED",
        "PROVISIONING",
        "STATE_UNSPECIFIED",
        "SUCCEEDED",
    ]
    status: InstanceGroupManagerResizeRequestStatus
    zone: str

@typing.type_check_only
class InstanceGroupManagerResizeRequestStatus(typing_extensions.TypedDict, total=False):
    error: dict[str, typing.Any]
    lastAttempt: InstanceGroupManagerResizeRequestStatusLastAttempt

@typing.type_check_only
class InstanceGroupManagerResizeRequestStatusLastAttempt(
    typing_extensions.TypedDict, total=False
):
    error: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerResizeRequestsListResponse(
    typing_extensions.TypedDict, total=False
):
    id: str
    items: _list[InstanceGroupManagerResizeRequest]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerResourcePolicies(typing_extensions.TypedDict, total=False):
    workloadPolicy: str

@typing.type_check_only
class InstanceGroupManagerStandbyPolicy(typing_extensions.TypedDict, total=False):
    initialDelaySec: int
    mode: typing_extensions.Literal["MANUAL", "SCALE_OUT_POOL"]

@typing.type_check_only
class InstanceGroupManagerStatus(typing_extensions.TypedDict, total=False):
    allInstancesConfig: InstanceGroupManagerStatusAllInstancesConfig
    autoscaler: str
    isStable: bool
    stateful: InstanceGroupManagerStatusStateful
    versionTarget: InstanceGroupManagerStatusVersionTarget

@typing.type_check_only
class InstanceGroupManagerStatusAllInstancesConfig(
    typing_extensions.TypedDict, total=False
):
    currentRevision: str
    effective: bool

@typing.type_check_only
class InstanceGroupManagerStatusStateful(typing_extensions.TypedDict, total=False):
    hasStatefulConfig: bool
    isStateful: bool
    perInstanceConfigs: InstanceGroupManagerStatusStatefulPerInstanceConfigs

@typing.type_check_only
class InstanceGroupManagerStatusStatefulPerInstanceConfigs(
    typing_extensions.TypedDict, total=False
):
    allEffective: bool

@typing.type_check_only
class InstanceGroupManagerStatusVersionTarget(typing_extensions.TypedDict, total=False):
    isReached: bool

@typing.type_check_only
class InstanceGroupManagerUpdatePolicy(typing_extensions.TypedDict, total=False):
    instanceRedistributionType: typing_extensions.Literal["NONE", "PROACTIVE"]
    maxSurge: FixedOrPercent
    maxUnavailable: FixedOrPercent
    minReadySec: int
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]
    replacementMethod: typing_extensions.Literal["RECREATE", "SUBSTITUTE"]
    type: typing_extensions.Literal["OPPORTUNISTIC", "PROACTIVE"]

@typing.type_check_only
class InstanceGroupManagerVersion(typing_extensions.TypedDict, total=False):
    instanceTemplate: str
    name: str
    targetSize: FixedOrPercent

@typing.type_check_only
class InstanceGroupManagersAbandonInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersApplyUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    allInstances: bool
    instances: _list[str]
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]

@typing.type_check_only
class InstanceGroupManagersCreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupManagersDeleteInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]
    skipInstancesOnValidationError: bool

@typing.type_check_only
class InstanceGroupManagersDeletePerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class InstanceGroupManagersListErrorsResponse(typing_extensions.TypedDict, total=False):
    items: _list[InstanceManagedByIgmError]
    nextPageToken: str

@typing.type_check_only
class InstanceGroupManagersListManagedInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    managedInstances: _list[ManagedInstance]
    nextPageToken: str

@typing.type_check_only
class InstanceGroupManagersListPerInstanceConfigsResp(
    typing_extensions.TypedDict, total=False
):
    items: _list[PerInstanceConfig]
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersPatchPerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupManagersRecreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersResizeAdvancedRequest(
    typing_extensions.TypedDict, total=False
):
    noCreationRetries: bool
    targetSize: int

@typing.type_check_only
class InstanceGroupManagersResumeInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersScopedList(typing_extensions.TypedDict, total=False):
    instanceGroupManagers: _list[InstanceGroupManager]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersSetAutoHealingRequest(
    typing_extensions.TypedDict, total=False
):
    autoHealingPolicies: _list[InstanceGroupManagerAutoHealingPolicy]

@typing.type_check_only
class InstanceGroupManagersSetInstanceTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    instanceTemplate: str

@typing.type_check_only
class InstanceGroupManagersSetTargetPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    targetPools: _list[str]

@typing.type_check_only
class InstanceGroupManagersStartInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersStopInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    forceStop: bool
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersSuspendInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    forceSuspend: bool
    instances: _list[str]

@typing.type_check_only
class InstanceGroupManagersUpdatePerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupsAddInstancesRequest(typing_extensions.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class InstanceGroupsListInstances(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupsListInstancesRequest(typing_extensions.TypedDict, total=False):
    instanceState: typing_extensions.Literal["ALL", "RUNNING"]

@typing.type_check_only
class InstanceGroupsRemoveInstancesRequest(typing_extensions.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class InstanceGroupsScopedList(typing_extensions.TypedDict, total=False):
    instanceGroups: _list[InstanceGroup]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupsSetNamedPortsRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str
    namedPorts: _list[NamedPort]

@typing.type_check_only
class InstanceList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Instance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceListReferrers(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Reference]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceManagedByIgmError(typing_extensions.TypedDict, total=False):
    error: InstanceManagedByIgmErrorManagedInstanceError
    instanceActionDetails: InstanceManagedByIgmErrorInstanceActionDetails
    timestamp: str

@typing.type_check_only
class InstanceManagedByIgmErrorInstanceActionDetails(
    typing_extensions.TypedDict, total=False
):
    action: typing_extensions.Literal[
        "ABANDONING",
        "CREATING",
        "CREATING_WITHOUT_RETRIES",
        "DELETING",
        "NONE",
        "RECREATING",
        "REFRESHING",
        "RESTARTING",
        "RESUMING",
        "STARTING",
        "STOPPING",
        "SUSPENDING",
        "VERIFYING",
    ]
    instance: str
    version: ManagedInstanceVersion

@typing.type_check_only
class InstanceManagedByIgmErrorManagedInstanceError(
    typing_extensions.TypedDict, total=False
):
    code: str
    message: str

@typing.type_check_only
class InstanceMoveRequest(typing_extensions.TypedDict, total=False):
    destinationZone: str
    targetInstance: str

@typing.type_check_only
class InstanceParams(typing_extensions.TypedDict, total=False):
    resourceManagerTags: dict[str, typing.Any]

@typing.type_check_only
class InstanceProperties(typing_extensions.TypedDict, total=False):
    advancedMachineFeatures: AdvancedMachineFeatures
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    description: str
    disks: _list[AttachedDisk]
    displayDevice: DisplayDevice
    guestAccelerators: _list[AcceleratorConfig]
    keyRevocationActionType: typing_extensions.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    labels: dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: _list[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    partnerMetadata: dict[str, typing.Any]
    postKeyRevocationActionType: typing_extensions.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "INHERIT_FROM_SUBNETWORK",
    ]
    reservationAffinity: ReservationAffinity
    resourceManagerTags: dict[str, typing.Any]
    resourcePolicies: _list[str]
    scheduling: Scheduling
    serviceAccounts: _list[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedVmConfig: ShieldedVmConfig
    tags: Tags

@typing.type_check_only
class InstancePropertiesPatch(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]

@typing.type_check_only
class InstanceReference(typing_extensions.TypedDict, total=False):
    instance: str

@typing.type_check_only
class InstanceSettings(typing_extensions.TypedDict, total=False):
    fingerprint: str
    kind: str
    metadata: InstanceSettingsMetadata
    zone: str

@typing.type_check_only
class InstanceSettingsMetadata(typing_extensions.TypedDict, total=False):
    items: dict[str, typing.Any]
    kind: str

@typing.type_check_only
class InstanceTemplate(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    properties: InstanceProperties
    region: str
    selfLink: str
    sourceInstance: str
    sourceInstanceParams: SourceInstanceParams

@typing.type_check_only
class InstanceTemplateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceTemplateList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceTemplatesScopedList(typing_extensions.TypedDict, total=False):
    instanceTemplates: _list[InstanceTemplate]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstanceWithNamedPorts(typing_extensions.TypedDict, total=False):
    instance: str
    namedPorts: _list[NamedPort]
    status: typing_extensions.Literal[
        "DEPROVISIONING",
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
class InstancesAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class InstancesBulkInsertOperationMetadata(typing_extensions.TypedDict, total=False):
    perLocationStatus: dict[str, typing.Any]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponse(typing_extensions.TypedDict, total=False):
    firewallPolicys: _list[
        InstancesGetEffectiveFirewallsResponseEffectiveFirewallPolicy
    ]
    firewalls: _list[Firewall]
    organizationFirewalls: _list[
        InstancesGetEffectiveFirewallsResponseOrganizationFirewallPolicy
    ]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    priority: int
    rules: _list[FirewallPolicyRule]
    shortName: str
    type: typing_extensions.Literal[
        "HIERARCHY",
        "NETWORK",
        "NETWORK_REGIONAL",
        "SYSTEM_GLOBAL",
        "SYSTEM_REGIONAL",
        "UNSPECIFIED",
    ]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseOrganizationFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    id: str
    rules: _list[SecurityPolicyRule]

@typing.type_check_only
class InstancesRemoveResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class InstancesResumeRequest(typing_extensions.TypedDict, total=False):
    disks: _list[CustomerEncryptionKeyProtectedDisk]
    instanceEncryptionKey: CustomerEncryptionKey

@typing.type_check_only
class InstancesScopedList(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstancesSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class InstancesSetMachineResourcesRequest(typing_extensions.TypedDict, total=False):
    guestAccelerators: _list[AcceleratorConfig]

@typing.type_check_only
class InstancesSetMachineTypeRequest(typing_extensions.TypedDict, total=False):
    machineType: str

@typing.type_check_only
class InstancesSetMinCpuPlatformRequest(typing_extensions.TypedDict, total=False):
    minCpuPlatform: str

@typing.type_check_only
class InstancesSetNameRequest(typing_extensions.TypedDict, total=False):
    currentName: str
    name: str

@typing.type_check_only
class InstancesSetSecurityPolicyRequest(typing_extensions.TypedDict, total=False):
    networkInterfaces: _list[str]
    securityPolicy: str

@typing.type_check_only
class InstancesSetServiceAccountRequest(typing_extensions.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class InstancesStartWithEncryptionKeyRequest(typing_extensions.TypedDict, total=False):
    disks: _list[CustomerEncryptionKeyProtectedDisk]

@typing.type_check_only
class InstantSnapshot(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
    creationTimestamp: str
    description: str
    diskSizeGb: str
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    region: str
    resourceStatus: InstantSnapshotResourceStatus
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    sourceDisk: str
    sourceDiskId: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "UNAVAILABLE"
    ]
    zone: str

@typing.type_check_only
class InstantSnapshotAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstantSnapshotList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstantSnapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InstantSnapshotResourceStatus(typing_extensions.TypedDict, total=False):
    storageSizeBytes: str

@typing.type_check_only
class InstantSnapshotsScopedList(typing_extensions.TypedDict, total=False):
    instantSnapshots: _list[InstantSnapshot]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Int64RangeMatch(typing_extensions.TypedDict, total=False):
    rangeEnd: str
    rangeStart: str

@typing.type_check_only
class Interconnect(typing_extensions.TypedDict, total=False):
    aaiEnabled: bool
    adminEnabled: bool
    applicationAwareInterconnect: InterconnectApplicationAwareInterconnect
    availableFeatures: _list[typing_extensions.Literal["IF_MACSEC"]]
    circuitInfos: _list[InterconnectCircuitInfo]
    creationTimestamp: str
    customerName: str
    description: str
    expectedOutages: _list[InterconnectOutageNotification]
    googleIpAddress: str
    googleReferenceId: str
    id: str
    interconnectAttachments: _list[str]
    interconnectType: typing_extensions.Literal["DEDICATED", "IT_PRIVATE", "PARTNER"]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    linkType: typing_extensions.Literal[
        "LINK_TYPE_ETHERNET_100G_LR", "LINK_TYPE_ETHERNET_10G_LR"
    ]
    location: str
    macsec: InterconnectMacsec
    macsecEnabled: bool
    name: str
    nocContactEmail: str
    operationalStatus: typing_extensions.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    peerIpAddress: str
    provisionedLinkCount: int
    remoteLocation: str
    requestedFeatures: _list[typing_extensions.Literal["IF_MACSEC"]]
    requestedLinkCount: int
    satisfiesPzs: bool
    selfLink: str
    state: typing_extensions.Literal["ACTIVE", "UNPROVISIONED"]

@typing.type_check_only
class InterconnectApplicationAwareInterconnect(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    percentage: int
    trafficClass: typing_extensions.Literal["TC1", "TC2", "TC3", "TC4", "TC5", "TC6"]

@typing.type_check_only
class InterconnectApplicationAwareInterconnectBandwidthPercentagePolicy(
    typing_extensions.TypedDict, total=False
):
    bandwidthPercentages: _list[
        InterconnectApplicationAwareInterconnectBandwidthPercentage
    ]

@typing.type_check_only
class InterconnectApplicationAwareInterconnectStrictPriorityPolicy(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class InterconnectAttachment(typing_extensions.TypedDict, total=False):
    adminEnabled: bool
    bandwidth: typing_extensions.Literal[
        "BPS_100G",
        "BPS_100M",
        "BPS_10G",
        "BPS_1G",
        "BPS_200M",
        "BPS_20G",
        "BPS_2G",
        "BPS_300M",
        "BPS_400M",
        "BPS_500M",
        "BPS_50G",
        "BPS_50M",
        "BPS_5G",
    ]
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
    edgeAvailabilityDomain: typing_extensions.Literal[
        "AVAILABILITY_DOMAIN_1", "AVAILABILITY_DOMAIN_2", "AVAILABILITY_DOMAIN_ANY"
    ]
    encryption: typing_extensions.Literal["IPSEC", "NONE"]
    googleReferenceId: str
    id: str
    interconnect: str
    ipsecInternalAddresses: _list[str]
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    mtu: int
    name: str
    operationalStatus: typing_extensions.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    pairingKey: str
    partnerAsn: str
    partnerMetadata: InterconnectAttachmentPartnerMetadata
    privateInterconnectInfo: InterconnectAttachmentPrivateInfo
    region: str
    remoteService: str
    router: str
    satisfiesPzs: bool
    selfLink: str
    stackType: typing_extensions.Literal["IPV4_IPV6", "IPV4_ONLY"]
    state: typing_extensions.Literal[
        "ACTIVE",
        "DEFUNCT",
        "PARTNER_REQUEST_RECEIVED",
        "PENDING_CUSTOMER",
        "PENDING_PARTNER",
        "STATE_UNSPECIFIED",
        "UNPROVISIONED",
    ]
    subnetLength: int
    type: typing_extensions.Literal["DEDICATED", "PARTNER", "PARTNER_PROVIDER"]
    vlanTag8021q: int

@typing.type_check_only
class InterconnectAttachmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentConfigurationConstraints(
    typing_extensions.TypedDict, total=False
):
    bgpMd5: typing_extensions.Literal["MD5_OPTIONAL", "MD5_REQUIRED", "MD5_UNSUPPORTED"]
    bgpPeerAsnRanges: _list[
        InterconnectAttachmentConfigurationConstraintsBgpPeerASNRange
    ]

@typing.type_check_only
class InterconnectAttachmentConfigurationConstraintsBgpPeerASNRange(
    typing_extensions.TypedDict, total=False
):
    max: int
    min: int

@typing.type_check_only
class InterconnectAttachmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InterconnectAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentPartnerMetadata(typing_extensions.TypedDict, total=False):
    interconnectName: str
    partnerName: str
    portalUrl: str

@typing.type_check_only
class InterconnectAttachmentPrivateInfo(typing_extensions.TypedDict, total=False):
    tag8021q: int

@typing.type_check_only
class InterconnectAttachmentsScopedList(typing_extensions.TypedDict, total=False):
    interconnectAttachments: _list[InterconnectAttachment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectCircuitInfo(typing_extensions.TypedDict, total=False):
    customerDemarcId: str
    googleCircuitId: str
    googleDemarcId: str

@typing.type_check_only
class InterconnectDiagnostics(typing_extensions.TypedDict, total=False):
    arpCaches: _list[InterconnectDiagnosticsARPEntry]
    bundleAggregationType: typing_extensions.Literal[
        "BUNDLE_AGGREGATION_TYPE_LACP", "BUNDLE_AGGREGATION_TYPE_STATIC"
    ]
    bundleOperationalStatus: typing_extensions.Literal[
        "BUNDLE_OPERATIONAL_STATUS_DOWN", "BUNDLE_OPERATIONAL_STATUS_UP"
    ]
    links: _list[InterconnectDiagnosticsLinkStatus]
    macAddress: str

@typing.type_check_only
class InterconnectDiagnosticsARPEntry(typing_extensions.TypedDict, total=False):
    ipAddress: str
    macAddress: str

@typing.type_check_only
class InterconnectDiagnosticsLinkLACPStatus(typing_extensions.TypedDict, total=False):
    googleSystemId: str
    neighborSystemId: str
    state: typing_extensions.Literal["ACTIVE", "DETACHED"]

@typing.type_check_only
class InterconnectDiagnosticsLinkOpticalPower(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "HIGH_ALARM", "HIGH_WARNING", "LOW_ALARM", "LOW_WARNING", "OK"
    ]
    value: float

@typing.type_check_only
class InterconnectDiagnosticsLinkStatus(typing_extensions.TypedDict, total=False):
    arpCaches: _list[InterconnectDiagnosticsARPEntry]
    circuitId: str
    googleDemarc: str
    lacpStatus: InterconnectDiagnosticsLinkLACPStatus
    macsec: InterconnectDiagnosticsMacsecStatus
    operationalStatus: typing_extensions.Literal[
        "LINK_OPERATIONAL_STATUS_DOWN", "LINK_OPERATIONAL_STATUS_UP"
    ]
    receivingOpticalPower: InterconnectDiagnosticsLinkOpticalPower
    transmittingOpticalPower: InterconnectDiagnosticsLinkOpticalPower

@typing.type_check_only
class InterconnectDiagnosticsMacsecStatus(typing_extensions.TypedDict, total=False):
    ckn: str
    operational: bool

@typing.type_check_only
class InterconnectList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Interconnect]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectLocation(typing_extensions.TypedDict, total=False):
    address: str
    availabilityZone: str
    availableFeatures: _list[typing_extensions.Literal["IF_MACSEC"]]
    availableLinkTypes: _list[
        typing_extensions.Literal[
            "LINK_TYPE_ETHERNET_100G_LR", "LINK_TYPE_ETHERNET_10G_LR"
        ]
    ]
    city: str
    continent: typing_extensions.Literal[
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
    description: str
    facilityProvider: str
    facilityProviderFacilityId: str
    id: str
    kind: str
    name: str
    peeringdbFacilityId: str
    regionInfos: _list[InterconnectLocationRegionInfo]
    selfLink: str
    status: typing_extensions.Literal["AVAILABLE", "CLOSED"]
    supportsPzs: bool

@typing.type_check_only
class InterconnectLocationList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InterconnectLocation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectLocationRegionInfo(typing_extensions.TypedDict, total=False):
    expectedRttMs: str
    locationPresence: typing_extensions.Literal[
        "GLOBAL", "LOCAL_REGION", "LP_GLOBAL", "LP_LOCAL_REGION"
    ]
    region: str

@typing.type_check_only
class InterconnectMacsec(typing_extensions.TypedDict, total=False):
    failOpen: bool
    preSharedKeys: _list[InterconnectMacsecPreSharedKey]

@typing.type_check_only
class InterconnectMacsecConfig(typing_extensions.TypedDict, total=False):
    preSharedKeys: _list[InterconnectMacsecConfigPreSharedKey]

@typing.type_check_only
class InterconnectMacsecConfigPreSharedKey(typing_extensions.TypedDict, total=False):
    cak: str
    ckn: str
    name: str
    startTime: str

@typing.type_check_only
class InterconnectMacsecPreSharedKey(typing_extensions.TypedDict, total=False):
    name: str
    startTime: str

@typing.type_check_only
class InterconnectOutageNotification(typing_extensions.TypedDict, total=False):
    affectedCircuits: _list[str]
    description: str
    endTime: str
    issueType: typing_extensions.Literal[
        "IT_OUTAGE", "IT_PARTIAL_OUTAGE", "OUTAGE", "PARTIAL_OUTAGE"
    ]
    name: str
    source: typing_extensions.Literal["GOOGLE", "NSRC_GOOGLE"]
    startTime: str
    state: typing_extensions.Literal[
        "ACTIVE", "CANCELLED", "COMPLETED", "NS_ACTIVE", "NS_CANCELED"
    ]

@typing.type_check_only
class InterconnectRemoteLocation(typing_extensions.TypedDict, total=False):
    address: str
    attachmentConfigurationConstraints: InterconnectAttachmentConfigurationConstraints
    city: str
    constraints: InterconnectRemoteLocationConstraints
    continent: typing_extensions.Literal[
        "AFRICA", "ASIA_PAC", "EUROPE", "NORTH_AMERICA", "SOUTH_AMERICA"
    ]
    creationTimestamp: str
    description: str
    facilityProvider: str
    facilityProviderFacilityId: str
    id: str
    kind: str
    lacp: typing_extensions.Literal["LACP_SUPPORTED", "LACP_UNSUPPORTED"]
    maxLagSize100Gbps: int
    maxLagSize10Gbps: int
    name: str
    peeringdbFacilityId: str
    permittedConnections: _list[InterconnectRemoteLocationPermittedConnections]
    remoteService: str
    selfLink: str
    status: typing_extensions.Literal["AVAILABLE", "CLOSED"]

@typing.type_check_only
class InterconnectRemoteLocationConstraints(typing_extensions.TypedDict, total=False):
    portPairRemoteLocation: typing_extensions.Literal[
        "PORT_PAIR_MATCHING_REMOTE_LOCATION", "PORT_PAIR_UNCONSTRAINED_REMOTE_LOCATION"
    ]
    portPairVlan: typing_extensions.Literal[
        "PORT_PAIR_MATCHING_VLAN", "PORT_PAIR_UNCONSTRAINED_VLAN"
    ]
    subnetLengthRange: InterconnectRemoteLocationConstraintsSubnetLengthRange

@typing.type_check_only
class InterconnectRemoteLocationConstraintsSubnetLengthRange(
    typing_extensions.TypedDict, total=False
):
    max: int
    min: int

@typing.type_check_only
class InterconnectRemoteLocationList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InterconnectRemoteLocation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class InterconnectRemoteLocationPermittedConnections(
    typing_extensions.TypedDict, total=False
):
    interconnectLocation: str

@typing.type_check_only
class InterconnectsGetDiagnosticsResponse(typing_extensions.TypedDict, total=False):
    result: InterconnectDiagnostics

@typing.type_check_only
class InterconnectsGetMacsecConfigResponse(typing_extensions.TypedDict, total=False):
    etag: str
    result: InterconnectMacsecConfig

@typing.type_check_only
class License(typing_extensions.TypedDict, total=False):
    chargesUseFee: bool
    creationTimestamp: str
    description: str
    id: str
    kind: str
    licenseCode: str
    name: str
    resourceRequirements: LicenseResourceRequirements
    selfLink: str
    transferable: bool

@typing.type_check_only
class LicenseCode(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    licenseAlias: _list[LicenseCodeLicenseAlias]
    name: str
    selfLink: str
    state: typing_extensions.Literal[
        "DISABLED", "ENABLED", "RESTRICTED", "STATE_UNSPECIFIED", "TERMINATED"
    ]
    transferable: bool

@typing.type_check_only
class LicenseCodeLicenseAlias(typing_extensions.TypedDict, total=False):
    description: str
    selfLink: str

@typing.type_check_only
class LicenseResourceCommitment(typing_extensions.TypedDict, total=False):
    amount: str
    coresPerLicense: str
    license: str

@typing.type_check_only
class LicenseResourceRequirements(typing_extensions.TypedDict, total=False):
    minGuestCpuCount: int
    minMemoryMb: int

@typing.type_check_only
class LicensesListResponse(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[License]
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class LocalDisk(typing_extensions.TypedDict, total=False):
    diskCount: int
    diskSizeGb: int
    diskType: str

@typing.type_check_only
class LocalizedMessage(typing_extensions.TypedDict, total=False):
    locale: str
    message: str

@typing.type_check_only
class LocationPolicy(typing_extensions.TypedDict, total=False):
    locations: dict[str, typing.Any]
    targetShape: typing_extensions.Literal["ANY", "ANY_SINGLE_ZONE", "BALANCED"]

@typing.type_check_only
class LocationPolicyLocation(typing_extensions.TypedDict, total=False):
    constraints: LocationPolicyLocationConstraints
    preference: typing_extensions.Literal["ALLOW", "DENY", "PREFERENCE_UNSPECIFIED"]

@typing.type_check_only
class LocationPolicyLocationConstraints(typing_extensions.TypedDict, total=False):
    maxCount: int

@typing.type_check_only
class MachineImage(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    guestFlush: bool
    id: str
    instanceProperties: InstanceProperties
    kind: str
    machineImageEncryptionKey: CustomerEncryptionKey
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    savedDisks: _list[SavedDisk]
    selfLink: str
    sourceDiskEncryptionKeys: _list[SourceDiskEncryptionKey]
    sourceInstance: str
    sourceInstanceProperties: SourceInstanceProperties
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "UPLOADING"
    ]
    storageLocations: _list[str]
    totalStorageBytes: str

@typing.type_check_only
class MachineImageList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[MachineImage]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class MachineType(typing_extensions.TypedDict, total=False):
    accelerators: _list[dict[str, typing.Any]]
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
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
    zone: str

@typing.type_check_only
class MachineTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class MachineTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[MachineType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class MachineTypesScopedList(typing_extensions.TypedDict, total=False):
    machineTypes: _list[MachineType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ManagedInstance(typing_extensions.TypedDict, total=False):
    allInstancesConfig: ManagedInstanceAllInstancesConfig
    currentAction: typing_extensions.Literal[
        "ABANDONING",
        "CREATING",
        "CREATING_WITHOUT_RETRIES",
        "DELETING",
        "NONE",
        "RECREATING",
        "REFRESHING",
        "RESTARTING",
        "RESUMING",
        "STARTING",
        "STOPPING",
        "SUSPENDING",
        "VERIFYING",
    ]
    id: str
    instance: str
    instanceHealth: _list[ManagedInstanceInstanceHealth]
    instanceStatus: typing_extensions.Literal[
        "DEPROVISIONING",
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
    lastAttempt: ManagedInstanceLastAttempt
    name: str
    preservedStateFromConfig: PreservedState
    preservedStateFromPolicy: PreservedState
    propertiesFromFlexibilityPolicy: ManagedInstancePropertiesFromFlexibilityPolicy
    targetStatus: typing_extensions.Literal[
        "ABANDONED", "DELETED", "RUNNING", "STOPPED", "SUSPENDED"
    ]
    version: ManagedInstanceVersion

@typing.type_check_only
class ManagedInstanceAllInstancesConfig(typing_extensions.TypedDict, total=False):
    revision: str

@typing.type_check_only
class ManagedInstanceInstanceHealth(typing_extensions.TypedDict, total=False):
    detailedHealthState: typing_extensions.Literal[
        "DRAINING", "HEALTHY", "TIMEOUT", "UNHEALTHY", "UNKNOWN"
    ]
    healthCheck: str

@typing.type_check_only
class ManagedInstanceLastAttempt(typing_extensions.TypedDict, total=False):
    errors: dict[str, typing.Any]

@typing.type_check_only
class ManagedInstancePropertiesFromFlexibilityPolicy(
    typing_extensions.TypedDict, total=False
):
    machineType: str
    provisioningModel: typing_extensions.Literal[
        "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]

@typing.type_check_only
class ManagedInstanceVersion(typing_extensions.TypedDict, total=False):
    instanceTemplate: str
    name: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    fingerprint: str
    items: _list[dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class MetadataFilter(typing_extensions.TypedDict, total=False):
    filterLabels: _list[MetadataFilterLabelMatch]
    filterMatchCriteria: typing_extensions.Literal["MATCH_ALL", "MATCH_ANY", "NOT_SET"]

@typing.type_check_only
class MetadataFilterLabelMatch(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class MultiMig(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    region: str
    resourcePolicies: MultiMigResourcePolicies
    selfLink: str

@typing.type_check_only
class MultiMigResourcePolicies(typing_extensions.TypedDict, total=False):
    workloadPolicy: str

@typing.type_check_only
class MultiMigsList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[MultiMig]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NamedPort(typing_extensions.TypedDict, total=False):
    name: str
    port: int

@typing.type_check_only
class NatIpInfo(typing_extensions.TypedDict, total=False):
    natIpInfoMappings: _list[NatIpInfoNatIpInfoMapping]
    natName: str

@typing.type_check_only
class NatIpInfoNatIpInfoMapping(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["AUTO", "MANUAL"]
    natIp: str
    usage: typing_extensions.Literal["IN_USE", "UNUSED"]

@typing.type_check_only
class NatIpInfoResponse(typing_extensions.TypedDict, total=False):
    result: _list[NatIpInfo]

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
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
    networkFirewallPolicyEnforcementOrder: typing_extensions.Literal[
        "AFTER_CLASSIC_FIREWALL", "BEFORE_CLASSIC_FIREWALL"
    ]
    networkProfile: str
    peerings: _list[NetworkPeering]
    routingConfig: NetworkRoutingConfig
    selfLink: str
    selfLinkWithId: str
    subnetworks: _list[str]

@typing.type_check_only
class NetworkAttachment(typing_extensions.TypedDict, total=False):
    connectionEndpoints: _list[NetworkAttachmentConnectedEndpoint]
    connectionPreference: typing_extensions.Literal[
        "ACCEPT_AUTOMATIC", "ACCEPT_MANUAL", "INVALID"
    ]
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
class NetworkAttachmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkAttachmentConnectedEndpoint(typing_extensions.TypedDict, total=False):
    ipAddress: str
    ipv6Address: str
    projectIdOrNum: str
    secondaryIpCidrRanges: _list[str]
    status: typing_extensions.Literal[
        "ACCEPTED",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]
    subnetwork: str
    subnetworkCidrRange: str

@typing.type_check_only
class NetworkAttachmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NetworkAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkAttachmentsScopedList(typing_extensions.TypedDict, total=False):
    networkAttachments: _list[NetworkAttachment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEdgeSecurityService(typing_extensions.TypedDict, total=False):
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
class NetworkEdgeSecurityServiceAggregatedList(
    typing_extensions.TypedDict, total=False
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
class NetworkEdgeSecurityServicesScopedList(typing_extensions.TypedDict, total=False):
    networkEdgeSecurityServices: _list[NetworkEdgeSecurityService]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clientDestinationPort: int
    fqdn: str
    instance: str
    ipAddress: str
    ipv6Address: str
    port: int

@typing.type_check_only
class NetworkEndpointGroup(typing_extensions.TypedDict, total=False):
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
    networkEndpointType: typing_extensions.Literal[
        "GCE_VM_IP",
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
    serverlessDeployment: NetworkEndpointGroupServerlessDeployment
    size: int
    subnetwork: str
    zone: str

@typing.type_check_only
class NetworkEndpointGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupAppEngine(typing_extensions.TypedDict, total=False):
    service: str
    urlMask: str
    version: str

@typing.type_check_only
class NetworkEndpointGroupCloudFunction(typing_extensions.TypedDict, total=False):
    function: str
    urlMask: str

@typing.type_check_only
class NetworkEndpointGroupCloudRun(typing_extensions.TypedDict, total=False):
    service: str
    tag: str
    urlMask: str

@typing.type_check_only
class NetworkEndpointGroupLbNetworkEndpointGroup(
    typing_extensions.TypedDict, total=False
):
    defaultPort: int
    network: str
    subnetwork: str
    zone: str

@typing.type_check_only
class NetworkEndpointGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NetworkEndpointGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupPscData(typing_extensions.TypedDict, total=False):
    consumerPscAddress: str
    producerPort: int
    pscConnectionId: str
    pscConnectionStatus: typing_extensions.Literal[
        "ACCEPTED",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]

@typing.type_check_only
class NetworkEndpointGroupServerlessDeployment(
    typing_extensions.TypedDict, total=False
):
    platform: str
    resource: str
    urlMask: str
    version: str

@typing.type_check_only
class NetworkEndpointGroupsAttachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class NetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class NetworkEndpointGroupsListEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    endpointFilters: _list[
        NetworkEndpointGroupsListEndpointsRequestNetworkEndpointFilter
    ]
    healthStatus: typing_extensions.Literal["SHOW", "SKIP"]

@typing.type_check_only
class NetworkEndpointGroupsListEndpointsRequestNetworkEndpointFilter(
    typing_extensions.TypedDict, total=False
):
    networkEndpoint: NetworkEndpoint

@typing.type_check_only
class NetworkEndpointGroupsListNetworkEndpoints(
    typing_extensions.TypedDict, total=False
):
    id: str
    items: _list[NetworkEndpointWithHealthStatus]
    kind: str
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupsScopedList(typing_extensions.TypedDict, total=False):
    networkEndpointGroups: _list[NetworkEndpointGroup]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointWithHealthStatus(typing_extensions.TypedDict, total=False):
    healths: _list[HealthStatusForNetworkEndpoint]
    networkEndpoint: NetworkEndpoint

@typing.type_check_only
class NetworkFirewallPolicyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    accessConfigs: _list[AccessConfig]
    aliasIpRanges: _list[AliasIpRange]
    fingerprint: str
    internalIpv6PrefixLength: int
    ipv6AccessConfigs: _list[AccessConfig]
    ipv6AccessType: typing_extensions.Literal["EXTERNAL", "INTERNAL"]
    ipv6Address: str
    kind: str
    name: str
    network: str
    networkAttachment: str
    networkIP: str
    nicType: typing_extensions.Literal[
        "GVNIC", "IDPF", "IRDMA", "MRDMA", "UNSPECIFIED_NIC_TYPE", "VIRTIO_NET"
    ]
    queueCount: int
    stackType: typing_extensions.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    subnetwork: str

@typing.type_check_only
class NetworkList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Network]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkPeering(typing_extensions.TypedDict, total=False):
    autoCreateRoutes: bool
    exchangeSubnetRoutes: bool
    exportCustomRoutes: bool
    exportSubnetRoutesWithPublicIp: bool
    importCustomRoutes: bool
    importSubnetRoutesWithPublicIp: bool
    name: str
    network: str
    peerMtu: int
    stackType: typing_extensions.Literal["IPV4_IPV6", "IPV4_ONLY"]
    state: typing_extensions.Literal["ACTIVE", "INACTIVE"]
    stateDetails: str

@typing.type_check_only
class NetworkPerformanceConfig(typing_extensions.TypedDict, total=False):
    totalEgressBandwidthTier: typing_extensions.Literal["DEFAULT", "TIER_1"]

@typing.type_check_only
class NetworkProfile(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    features: NetworkProfileNetworkFeatures
    id: str
    kind: str
    location: NetworkProfileLocation
    name: str
    selfLink: str
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class NetworkProfileLocation(typing_extensions.TypedDict, total=False):
    name: str
    scope: typing_extensions.Literal["REGION", "ZONE"]

@typing.type_check_only
class NetworkProfileNetworkFeatures(typing_extensions.TypedDict, total=False):
    addressPurposes: _list[
        typing_extensions.Literal[
            "DNS_RESOLVER",
            "GCE_ENDPOINT",
            "IPSEC_INTERCONNECT",
            "NAT_AUTO",
            "PRIVATE_SERVICE_CONNECT",
            "SERVERLESS",
            "SHARED_LOADBALANCER_VIP",
            "VPC_PEERING",
        ]
    ]
    allowAliasIpRanges: typing_extensions.Literal[
        "ALIAS_IP_RANGES_ALLOWED", "ALIAS_IP_RANGES_BLOCKED"
    ]
    allowAutoModeSubnet: typing_extensions.Literal[
        "AUTO_MODE_SUBNET_ALLOWED", "AUTO_MODE_SUBNET_BLOCKED"
    ]
    allowClassDFirewalls: typing_extensions.Literal[
        "CLASS_D_FIREWALLS_ALLOWED", "CLASS_D_FIREWALLS_BLOCKED"
    ]
    allowCloudNat: typing_extensions.Literal["CLOUD_NAT_ALLOWED", "CLOUD_NAT_BLOCKED"]
    allowCloudRouter: typing_extensions.Literal[
        "CLOUD_ROUTER_ALLOWED", "CLOUD_ROUTER_BLOCKED"
    ]
    allowExternalIpAccess: typing_extensions.Literal[
        "EXTERNAL_IP_ACCESS_ALLOWED", "EXTERNAL_IP_ACCESS_BLOCKED"
    ]
    allowInterconnect: typing_extensions.Literal[
        "INTERCONNECT_ALLOWED", "INTERCONNECT_BLOCKED"
    ]
    allowLoadBalancing: typing_extensions.Literal[
        "LOAD_BALANCING_ALLOWED", "LOAD_BALANCING_BLOCKED"
    ]
    allowMultiNicInSameNetwork: typing_extensions.Literal[
        "MULTI_NIC_IN_SAME_NETWORK_ALLOWED", "MULTI_NIC_IN_SAME_NETWORK_BLOCKED"
    ]
    allowPacketMirroring: typing_extensions.Literal[
        "PACKET_MIRRORING_ALLOWED", "PACKET_MIRRORING_BLOCKED"
    ]
    allowPrivateGoogleAccess: typing_extensions.Literal[
        "PRIVATE_GOOGLE_ACCESS_ALLOWED", "PRIVATE_GOOGLE_ACCESS_BLOCKED"
    ]
    allowPsc: typing_extensions.Literal["PSC_ALLOWED", "PSC_BLOCKED"]
    allowSameNetworkUnicast: typing_extensions.Literal[
        "SAME_NETWORK_UNICAST_ALLOWED", "SAME_NETWORK_UNICAST_BLOCKED"
    ]
    allowStaticRoutes: typing_extensions.Literal[
        "STATIC_ROUTES_ALLOWED", "STATIC_ROUTES_BLOCKED"
    ]
    allowSubInterfaces: typing_extensions.Literal[
        "SUBINTERFACES_ALLOWED", "SUBINTERFACES_BLOCKED"
    ]
    allowVpcPeering: typing_extensions.Literal[
        "VPC_PEERING_ALLOWED", "VPC_PEERING_BLOCKED"
    ]
    allowVpn: typing_extensions.Literal["VPN_ALLOWED", "VPN_BLOCKED"]
    interfaceTypes: _list[
        typing_extensions.Literal[
            "GVNIC", "IDPF", "IRDMA", "MRDMA", "UNSPECIFIED_NIC_TYPE", "VIRTIO_NET"
        ]
    ]
    subnetPurposes: _list[
        typing_extensions.Literal[
            "SUBNET_PURPOSE_CUSTOM_HARDWARE", "SUBNET_PURPOSE_PRIVATE"
        ]
    ]
    subnetStackTypes: _list[
        typing_extensions.Literal[
            "SUBNET_STACK_TYPE_IPV4_IPV6",
            "SUBNET_STACK_TYPE_IPV4_ONLY",
            "SUBNET_STACK_TYPE_IPV6_ONLY",
        ]
    ]
    unicast: typing_extensions.Literal["UNICAST_SDN", "UNICAST_ULL"]

@typing.type_check_only
class NetworkProfilesListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[NetworkProfile]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NetworkRoutingConfig(typing_extensions.TypedDict, total=False):
    bgpAlwaysCompareMed: bool
    bgpBestPathSelectionMode: typing_extensions.Literal["LEGACY", "STANDARD"]
    bgpInterRegionCost: typing_extensions.Literal["ADD_COST_TO_MED", "DEFAULT"]
    effectiveBgpAlwaysCompareMed: bool
    effectiveBgpInterRegionCost: typing_extensions.Literal["ADD_COST_TO_MED", "DEFAULT"]
    routingMode: typing_extensions.Literal["GLOBAL", "REGIONAL"]

@typing.type_check_only
class NetworksAddPeeringRequest(typing_extensions.TypedDict, total=False):
    autoCreateRoutes: bool
    name: str
    networkPeering: NetworkPeering
    peerNetwork: str

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponse(typing_extensions.TypedDict, total=False):
    firewallPolicys: _list[NetworksGetEffectiveFirewallsResponseEffectiveFirewallPolicy]
    firewalls: _list[Firewall]
    organizationFirewalls: _list[
        NetworksGetEffectiveFirewallsResponseOrganizationFirewallPolicy
    ]

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    priority: int
    rules: _list[FirewallPolicyRule]
    shortName: str
    type: typing_extensions.Literal["HIERARCHY", "NETWORK", "SYSTEM", "UNSPECIFIED"]

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseOrganizationFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    id: str
    rules: _list[SecurityPolicyRule]

@typing.type_check_only
class NetworksRemovePeeringRequest(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class NetworksUpdatePeeringRequest(typing_extensions.TypedDict, total=False):
    networkPeering: NetworkPeering

@typing.type_check_only
class NodeGroup(typing_extensions.TypedDict, total=False):
    autoscalingPolicy: NodeGroupAutoscalingPolicy
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    locationHint: str
    maintenanceInterval: typing_extensions.Literal["AS_NEEDED", "PERIODIC", "RECURRENT"]
    maintenancePolicy: typing_extensions.Literal[
        "DEFAULT",
        "MAINTENANCE_POLICY_UNSPECIFIED",
        "MIGRATE_WITHIN_NODE_GROUP",
        "RESTART_IN_PLACE",
    ]
    maintenanceWindow: NodeGroupMaintenanceWindow
    name: str
    nodeTemplate: str
    selfLink: str
    shareSettings: ShareSettings
    size: int
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    zone: str

@typing.type_check_only
class NodeGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupAutoscalingPolicy(typing_extensions.TypedDict, total=False):
    maxNodes: int
    minNodes: int
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "OFF", "ON", "ONLY_SCALE_OUT"]

@typing.type_check_only
class NodeGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NodeGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupMaintenanceWindow(typing_extensions.TypedDict, total=False):
    maintenanceDuration: Duration
    startTime: str

@typing.type_check_only
class NodeGroupNode(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    consumedResources: InstanceConsumptionInfo
    cpuOvercommitType: typing_extensions.Literal[
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
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "REPAIRING"
    ]
    totalResources: InstanceConsumptionInfo
    upcomingMaintenance: UpcomingMaintenance

@typing.type_check_only
class NodeGroupsAddNodesRequest(typing_extensions.TypedDict, total=False):
    additionalNodeCount: int

@typing.type_check_only
class NodeGroupsDeleteNodesRequest(typing_extensions.TypedDict, total=False):
    nodes: _list[str]

@typing.type_check_only
class NodeGroupsListNodes(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NodeGroupNode]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupsPerformMaintenanceRequest(typing_extensions.TypedDict, total=False):
    nodes: _list[str]
    startTime: str

@typing.type_check_only
class NodeGroupsScopedList(typing_extensions.TypedDict, total=False):
    nodeGroups: _list[NodeGroup]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeGroupsSetNodeTemplateRequest(typing_extensions.TypedDict, total=False):
    nodeTemplate: str

@typing.type_check_only
class NodeGroupsSimulateMaintenanceEventRequest(
    typing_extensions.TypedDict, total=False
):
    nodes: _list[str]

@typing.type_check_only
class NodeTemplate(typing_extensions.TypedDict, total=False):
    accelerators: _list[AcceleratorConfig]
    cpuOvercommitType: typing_extensions.Literal[
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
    serverBinding: ServerBinding
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    statusMessage: str

@typing.type_check_only
class NodeTemplateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTemplateList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NodeTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTemplateNodeTypeFlexibility(typing_extensions.TypedDict, total=False):
    cpus: str
    localSsd: str
    memory: str

@typing.type_check_only
class NodeTemplatesScopedList(typing_extensions.TypedDict, total=False):
    nodeTemplates: _list[NodeTemplate]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeType(typing_extensions.TypedDict, total=False):
    cpuPlatform: str
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    guestCpus: int
    id: str
    kind: str
    localSsdGb: int
    memoryMb: int
    name: str
    selfLink: str
    zone: str

@typing.type_check_only
class NodeTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NodeType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class NodeTypesScopedList(typing_extensions.TypedDict, total=False):
    nodeTypes: _list[NodeType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class NotificationEndpoint(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    grpcSettings: NotificationEndpointGrpcSettings
    id: str
    kind: str
    name: str
    region: str
    selfLink: str

@typing.type_check_only
class NotificationEndpointGrpcSettings(typing_extensions.TypedDict, total=False):
    authority: str
    endpoint: str
    payloadName: str
    resendInterval: Duration
    retryDurationSec: int

@typing.type_check_only
class NotificationEndpointList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[NotificationEndpoint]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: dict[str, typing.Any]
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
    setCommonInstanceMetadataOperationMetadata: (
        SetCommonInstanceMetadataOperationMetadata
    )
    startTime: str
    status: typing_extensions.Literal["DONE", "PENDING", "RUNNING"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: _list[dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class OperationList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Operation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class OperationsScopedList(typing_extensions.TypedDict, total=False):
    operations: _list[Operation]
    warning: dict[str, typing.Any]

@typing.type_check_only
class OrganizationSecurityPoliciesListAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    associations: _list[SecurityPolicyAssociation]
    kind: str

@typing.type_check_only
class OutlierDetection(typing_extensions.TypedDict, total=False):
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
class PacketIntervals(typing_extensions.TypedDict, total=False):
    avgMs: str
    duration: typing_extensions.Literal["DURATION_UNSPECIFIED", "HOUR", "MAX", "MINUTE"]
    maxMs: str
    minMs: str
    numIntervals: str
    type: typing_extensions.Literal[
        "LOOPBACK", "RECEIVE", "TRANSMIT", "TYPE_UNSPECIFIED"
    ]

@typing.type_check_only
class PacketMirroring(typing_extensions.TypedDict, total=False):
    collectorIlb: PacketMirroringForwardingRuleInfo
    creationTimestamp: str
    description: str
    enable: typing_extensions.Literal["FALSE", "TRUE"]
    filter: PacketMirroringFilter
    id: str
    kind: str
    mirroredResources: PacketMirroringMirroredResourceInfo
    name: str
    network: PacketMirroringNetworkInfo
    priority: int
    region: str
    selfLink: str

@typing.type_check_only
class PacketMirroringAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PacketMirroringFilter(typing_extensions.TypedDict, total=False):
    IPProtocols: _list[str]
    cidrRanges: _list[str]
    direction: typing_extensions.Literal["BOTH", "EGRESS", "INGRESS"]

@typing.type_check_only
class PacketMirroringForwardingRuleInfo(typing_extensions.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[PacketMirroring]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class PacketMirroringMirroredResourceInfo(typing_extensions.TypedDict, total=False):
    instances: _list[PacketMirroringMirroredResourceInfoInstanceInfo]
    subnetworks: _list[PacketMirroringMirroredResourceInfoSubnetInfo]
    tags: _list[str]

@typing.type_check_only
class PacketMirroringMirroredResourceInfoInstanceInfo(
    typing_extensions.TypedDict, total=False
):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringMirroredResourceInfoSubnetInfo(
    typing_extensions.TypedDict, total=False
):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringNetworkInfo(typing_extensions.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringsScopedList(typing_extensions.TypedDict, total=False):
    packetMirrorings: _list[PacketMirroring]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PartnerMetadata(typing_extensions.TypedDict, total=False):
    fingerprint: str
    partnerMetadata: dict[str, typing.Any]

@typing.type_check_only
class PathMatcher(typing_extensions.TypedDict, total=False):
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
class PathRule(typing_extensions.TypedDict, total=False):
    customErrorResponsePolicy: CustomErrorResponsePolicy
    paths: _list[str]
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

@typing.type_check_only
class PerInstanceConfig(typing_extensions.TypedDict, total=False):
    fingerprint: str
    name: str
    preservedState: PreservedState
    status: typing_extensions.Literal[
        "APPLYING", "DELETING", "EFFECTIVE", "NONE", "UNAPPLIED", "UNAPPLIED_DELETION"
    ]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PreconfiguredWafSet(typing_extensions.TypedDict, total=False):
    expressionSets: _list[WafExpressionSet]

@typing.type_check_only
class PreservedState(typing_extensions.TypedDict, total=False):
    disks: dict[str, typing.Any]
    externalIPs: dict[str, typing.Any]
    internalIPs: dict[str, typing.Any]
    metadata: dict[str, typing.Any]

@typing.type_check_only
class PreservedStatePreservedDisk(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    source: str

@typing.type_check_only
class PreservedStatePreservedNetworkIp(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]
    ipAddress: PreservedStatePreservedNetworkIpIpAddress

@typing.type_check_only
class PreservedStatePreservedNetworkIpIpAddress(
    typing_extensions.TypedDict, total=False
):
    address: str
    literal: str

@typing.type_check_only
class Project(typing_extensions.TypedDict, total=False):
    cloudArmorTier: typing_extensions.Literal[
        "CA_ENTERPRISE_ANNUAL", "CA_ENTERPRISE_PAYGO", "CA_STANDARD"
    ]
    commonInstanceMetadata: Metadata
    creationTimestamp: str
    defaultNetworkTier: typing_extensions.Literal[
        "FIXED_STANDARD", "PREMIUM", "STANDARD", "STANDARD_OVERRIDES_FIXED_STANDARD"
    ]
    defaultServiceAccount: str
    description: str
    enabledFeatures: _list[str]
    id: str
    kind: str
    managedProtectionTier: typing_extensions.Literal[
        "CAMP_PLUS_ANNUAL", "CAMP_PLUS_PAYGO", "CA_STANDARD"
    ]
    name: str
    quotas: _list[Quota]
    selfLink: str
    usageExportLocation: UsageExportLocation
    vmDnsSetting: typing_extensions.Literal[
        "GLOBAL_DEFAULT", "UNSPECIFIED_VM_DNS_SETTING", "ZONAL_DEFAULT", "ZONAL_ONLY"
    ]
    xpnProjectStatus: typing_extensions.Literal[
        "HOST", "UNSPECIFIED_XPN_PROJECT_STATUS"
    ]

@typing.type_check_only
class ProjectsDisableXpnResourceRequest(typing_extensions.TypedDict, total=False):
    xpnResource: XpnResourceId

@typing.type_check_only
class ProjectsEnableXpnResourceRequest(typing_extensions.TypedDict, total=False):
    xpnResource: XpnResourceId

@typing.type_check_only
class ProjectsGetXpnResources(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: _list[XpnResourceId]

@typing.type_check_only
class ProjectsListXpnHostsRequest(typing_extensions.TypedDict, total=False):
    organization: str

@typing.type_check_only
class ProjectsSetCloudArmorTierRequest(typing_extensions.TypedDict, total=False):
    cloudArmorTier: typing_extensions.Literal[
        "CA_ENTERPRISE_ANNUAL", "CA_ENTERPRISE_PAYGO", "CA_STANDARD"
    ]

@typing.type_check_only
class ProjectsSetDefaultNetworkTierRequest(typing_extensions.TypedDict, total=False):
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD", "PREMIUM", "STANDARD", "STANDARD_OVERRIDES_FIXED_STANDARD"
    ]

@typing.type_check_only
class ProjectsSetManagedProtectionTierRequest(typing_extensions.TypedDict, total=False):
    managedProtectionTier: typing_extensions.Literal[
        "CAMP_PLUS_ANNUAL", "CAMP_PLUS_PAYGO", "CA_STANDARD"
    ]

@typing.type_check_only
class PublicAdvertisedPrefix(typing_extensions.TypedDict, total=False):
    byoipApiVersion: typing_extensions.Literal["V1", "V2"]
    creationTimestamp: str
    description: str
    dnsVerificationIp: str
    fingerprint: str
    id: str
    ipCidrRange: str
    kind: str
    name: str
    pdpScope: typing_extensions.Literal["GLOBAL", "GLOBAL_AND_REGIONAL", "REGIONAL"]
    publicDelegatedPrefixs: _list[PublicAdvertisedPrefixPublicDelegatedPrefix]
    selfLink: str
    sharedSecret: str
    status: typing_extensions.Literal[
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
class PublicAdvertisedPrefixList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[PublicAdvertisedPrefix]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class PublicAdvertisedPrefixPublicDelegatedPrefix(
    typing_extensions.TypedDict, total=False
):
    ipRange: str
    name: str
    project: str
    region: str
    status: str

@typing.type_check_only
class PublicDelegatedPrefix(typing_extensions.TypedDict, total=False):
    allocatablePrefixLength: int
    byoipApiVersion: typing_extensions.Literal["V1", "V2"]
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    ipCidrRange: str
    isLiveMigration: bool
    kind: str
    mode: typing_extensions.Literal[
        "DELEGATION",
        "EXTERNAL_IPV6_FORWARDING_RULE_CREATION",
        "EXTERNAL_IPV6_SUBNETWORK_CREATION",
    ]
    name: str
    parentPrefix: str
    publicDelegatedSubPrefixs: _list[PublicDelegatedPrefixPublicDelegatedSubPrefix]
    region: str
    selfLink: str
    status: typing_extensions.Literal[
        "ANNOUNCED",
        "ANNOUNCED_TO_GOOGLE",
        "ANNOUNCED_TO_INTERNET",
        "DELETING",
        "INITIALIZING",
        "READY_TO_ANNOUNCE",
    ]

@typing.type_check_only
class PublicDelegatedPrefixAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class PublicDelegatedPrefixList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[PublicDelegatedPrefix]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class PublicDelegatedPrefixPublicDelegatedSubPrefix(
    typing_extensions.TypedDict, total=False
):
    allocatablePrefixLength: int
    delegateeProject: str
    description: str
    ipCidrRange: str
    isAddress: bool
    mode: typing_extensions.Literal[
        "DELEGATION",
        "EXTERNAL_IPV6_FORWARDING_RULE_CREATION",
        "EXTERNAL_IPV6_SUBNETWORK_CREATION",
    ]
    name: str
    region: str
    status: typing_extensions.Literal["ACTIVE", "INACTIVE"]

@typing.type_check_only
class PublicDelegatedPrefixesScopedList(typing_extensions.TypedDict, total=False):
    publicDelegatedPrefixes: _list[PublicDelegatedPrefix]
    warning: dict[str, typing.Any]

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    limit: float
    metric: typing_extensions.Literal[
        "A2_CPUS",
        "AFFINITY_GROUPS",
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
        "PREEMPTIBLE_TPU_LITE_DEVICE_V5",
        "PREEMPTIBLE_TPU_LITE_PODSLICE_V5",
        "PREEMPTIBLE_TPU_PODSLICE_V4",
        "PRIVATE_V6_ACCESS_SUBNETWORKS",
        "PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK",
        "PSC_INTERNAL_LB_FORWARDING_RULES",
        "PUBLIC_ADVERTISED_PREFIXES",
        "PUBLIC_DELEGATED_PREFIXES",
        "REGIONAL_AUTOSCALERS",
        "REGIONAL_EXTERNAL_MANAGED_BACKEND_SERVICES",
        "REGIONAL_EXTERNAL_NETWORK_LB_BACKEND_SERVICES",
        "REGIONAL_INSTANCE_GROUP_MANAGERS",
        "REGIONAL_INTERNAL_LB_BACKEND_SERVICES",
        "REGIONAL_INTERNAL_MANAGED_BACKEND_SERVICES",
        "REGIONAL_INTERNAL_TRAFFIC_DIRECTOR_BACKEND_SERVICES",
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
class QuotaExceededInfo(typing_extensions.TypedDict, total=False):
    dimensions: dict[str, typing.Any]
    futureLimit: float
    limit: float
    limitName: str
    metricName: str
    rolloutStatus: typing_extensions.Literal[
        "IN_PROGRESS", "ROLLOUT_STATUS_UNSPECIFIED"
    ]

@typing.type_check_only
class Reference(typing_extensions.TypedDict, total=False):
    kind: str
    referenceType: str
    referrer: str
    target: str

@typing.type_check_only
class Region(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    quotaStatusWarning: dict[str, typing.Any]
    quotas: _list[Quota]
    selfLink: str
    status: typing_extensions.Literal["DOWN", "UP"]
    supportsPzs: bool
    zones: _list[str]

@typing.type_check_only
class RegionAddressesMoveRequest(typing_extensions.TypedDict, total=False):
    description: str
    destinationAddress: str

@typing.type_check_only
class RegionAutoscalerList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionCommitmentsUpdateReservationsRequest(
    typing_extensions.TypedDict, total=False
):
    reservations: _list[Reservation]

@typing.type_check_only
class RegionDiskTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionDisksAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: _list[str]

@typing.type_check_only
class RegionDisksRemoveResourcePoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    resourcePolicies: _list[str]

@typing.type_check_only
class RegionDisksResizeRequest(typing_extensions.TypedDict, total=False):
    sizeGb: str

@typing.type_check_only
class RegionDisksStartAsyncReplicationRequest(typing_extensions.TypedDict, total=False):
    asyncSecondaryDisk: str

@typing.type_check_only
class RegionInstanceGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerDeleteInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagerList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerPatchInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagerResizeRequestsListResponse(
    typing_extensions.TypedDict, total=False
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
class RegionInstanceGroupManagerUpdateInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersAbandonInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersApplyUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    allInstances: bool
    instances: _list[str]
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]

@typing.type_check_only
class RegionInstanceGroupManagersCreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersDeleteInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]
    skipInstancesOnValidationError: bool

@typing.type_check_only
class RegionInstanceGroupManagersListErrorsResponse(
    typing_extensions.TypedDict, total=False
):
    items: _list[InstanceManagedByIgmError]
    nextPageToken: str

@typing.type_check_only
class RegionInstanceGroupManagersListInstanceConfigsResp(
    typing_extensions.TypedDict, total=False
):
    items: _list[PerInstanceConfig]
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagersListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    managedInstances: _list[ManagedInstance]
    nextPageToken: str

@typing.type_check_only
class RegionInstanceGroupManagersRecreateRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersResizeAdvancedRequest(
    typing_extensions.TypedDict, total=False
):
    noCreationRetries: bool
    targetSize: int

@typing.type_check_only
class RegionInstanceGroupManagersResumeInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersSetAutoHealingRequest(
    typing_extensions.TypedDict, total=False
):
    autoHealingPolicies: _list[InstanceGroupManagerAutoHealingPolicy]

@typing.type_check_only
class RegionInstanceGroupManagersSetTargetPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    targetPools: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersSetTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    instanceTemplate: str

@typing.type_check_only
class RegionInstanceGroupManagersStartInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersStopInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    forceStop: bool
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupManagersSuspendInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    forceSuspend: bool
    instances: _list[str]

@typing.type_check_only
class RegionInstanceGroupsListInstances(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupsListInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instanceState: typing_extensions.Literal["ALL", "RUNNING"]
    portName: str

@typing.type_check_only
class RegionInstanceGroupsSetNamedPortsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    namedPorts: _list[NamedPort]

@typing.type_check_only
class RegionList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Region]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RegionNetworkEndpointGroupsAttachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class RegionNetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: _list[NetworkEndpoint]

@typing.type_check_only
class RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse(
    typing_extensions.TypedDict, total=False
):
    firewallPolicys: _list[
        RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponseEffectiveFirewallPolicy
    ]
    firewalls: _list[Firewall]

@typing.type_check_only
class RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    packetMirroringRules: _list[FirewallPolicyRule]
    priority: int
    rules: _list[FirewallPolicyRule]
    type: typing_extensions.Literal[
        "HIERARCHY",
        "NETWORK",
        "NETWORK_REGIONAL",
        "SYSTEM_GLOBAL",
        "SYSTEM_REGIONAL",
        "UNSPECIFIED",
    ]

@typing.type_check_only
class RegionSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class RegionSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class RegionTargetHttpsProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: _list[str]

@typing.type_check_only
class RegionUrlMapsValidateRequest(typing_extensions.TypedDict, total=False):
    resource: UrlMap

@typing.type_check_only
class RequestMirrorPolicy(typing_extensions.TypedDict, total=False):
    backendService: str
    mirrorPercent: float

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    aggregateReservation: AllocationAggregateReservation
    commitment: str
    creationTimestamp: str
    deleteAfterDuration: Duration
    deleteAtTime: str
    deploymentType: typing_extensions.Literal[
        "DENSE", "DEPLOYMENT_TYPE_UNSPECIFIED", "FLEXIBLE"
    ]
    description: str
    id: str
    kind: str
    name: str
    reservationSharingPolicy: AllocationReservationSharingPolicy
    resourcePolicies: dict[str, typing.Any]
    resourceStatus: AllocationResourceStatus
    satisfiesPzs: bool
    selfLink: str
    shareSettings: ShareSettings
    specificReservation: AllocationSpecificSKUReservation
    specificReservationRequired: bool
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "UPDATING"
    ]
    zone: str

@typing.type_check_only
class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "ANY_RESERVATION",
        "NO_RESERVATION",
        "SPECIFIC_RESERVATION",
        "SPECIFIC_THEN_ANY_RESERVATION",
        "SPECIFIC_THEN_NO_RESERVATION",
        "UNSPECIFIED",
    ]
    key: str
    values: _list[str]

@typing.type_check_only
class ReservationAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationBlock(typing_extensions.TypedDict, total=False):
    count: int
    creationTimestamp: str
    id: str
    inUseCount: int
    kind: str
    name: str
    physicalTopology: ReservationBlockPhysicalTopology
    reservationMaintenance: GroupMaintenanceInfo
    selfLink: str
    selfLinkWithId: str
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    zone: str

@typing.type_check_only
class ReservationBlockPhysicalTopology(typing_extensions.TypedDict, total=False):
    block: str
    cluster: str

@typing.type_check_only
class ReservationBlocksGetResponse(typing_extensions.TypedDict, total=False):
    resource: ReservationBlock

@typing.type_check_only
class ReservationBlocksListResponse(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[ReservationBlock]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Reservation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ReservationsResizeRequest(typing_extensions.TypedDict, total=False):
    specificSkuCount: str

@typing.type_check_only
class ReservationsScopedList(typing_extensions.TypedDict, total=False):
    reservations: _list[Reservation]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourceCommitment(typing_extensions.TypedDict, total=False):
    acceleratorType: str
    amount: str
    type: typing_extensions.Literal[
        "ACCELERATOR", "LOCAL_SSD", "MEMORY", "UNSPECIFIED", "VCPU"
    ]

@typing.type_check_only
class ResourceGroupReference(typing_extensions.TypedDict, total=False):
    group: str

@typing.type_check_only
class ResourcePoliciesScopedList(typing_extensions.TypedDict, total=False):
    resourcePolicies: _list[ResourcePolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicy(typing_extensions.TypedDict, total=False):
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
    snapshotSchedulePolicy: ResourcePolicySnapshotSchedulePolicy
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "EXPIRED", "INVALID", "READY"
    ]
    workloadPolicy: ResourcePolicyWorkloadPolicy

@typing.type_check_only
class ResourcePolicyAggregatedList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicyDailyCycle(typing_extensions.TypedDict, total=False):
    daysInCycle: int
    duration: str
    startTime: str

@typing.type_check_only
class ResourcePolicyDiskConsistencyGroupPolicy(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ResourcePolicyGroupPlacementPolicy(typing_extensions.TypedDict, total=False):
    availabilityDomainCount: int
    collocation: typing_extensions.Literal["COLLOCATED", "UNSPECIFIED_COLLOCATION"]
    maxDistance: int
    sliceCount: int
    tpuTopology: str
    vmCount: int

@typing.type_check_only
class ResourcePolicyHourlyCycle(typing_extensions.TypedDict, total=False):
    duration: str
    hoursInCycle: int
    startTime: str

@typing.type_check_only
class ResourcePolicyInstanceSchedulePolicy(typing_extensions.TypedDict, total=False):
    expirationTime: str
    startTime: str
    timeZone: str
    vmStartSchedule: ResourcePolicyInstanceSchedulePolicySchedule
    vmStopSchedule: ResourcePolicyInstanceSchedulePolicySchedule

@typing.type_check_only
class ResourcePolicyInstanceSchedulePolicySchedule(
    typing_extensions.TypedDict, total=False
):
    schedule: str

@typing.type_check_only
class ResourcePolicyList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[ResourcePolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicyResourceStatus(typing_extensions.TypedDict, total=False):
    instanceSchedulePolicy: ResourcePolicyResourceStatusInstanceSchedulePolicyStatus

@typing.type_check_only
class ResourcePolicyResourceStatusInstanceSchedulePolicyStatus(
    typing_extensions.TypedDict, total=False
):
    lastRunStartTime: str
    nextRunStartTime: str

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicy(typing_extensions.TypedDict, total=False):
    retentionPolicy: ResourcePolicySnapshotSchedulePolicyRetentionPolicy
    schedule: ResourcePolicySnapshotSchedulePolicySchedule
    snapshotProperties: ResourcePolicySnapshotSchedulePolicySnapshotProperties

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicyRetentionPolicy(
    typing_extensions.TypedDict, total=False
):
    maxRetentionDays: int
    onSourceDiskDelete: typing_extensions.Literal[
        "APPLY_RETENTION_POLICY",
        "KEEP_AUTO_SNAPSHOTS",
        "UNSPECIFIED_ON_SOURCE_DISK_DELETE",
    ]

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicySchedule(
    typing_extensions.TypedDict, total=False
):
    dailySchedule: ResourcePolicyDailyCycle
    hourlySchedule: ResourcePolicyHourlyCycle
    weeklySchedule: ResourcePolicyWeeklyCycle

@typing.type_check_only
class ResourcePolicySnapshotSchedulePolicySnapshotProperties(
    typing_extensions.TypedDict, total=False
):
    chainName: str
    guestFlush: bool
    labels: dict[str, typing.Any]
    storageLocations: _list[str]

@typing.type_check_only
class ResourcePolicyWeeklyCycle(typing_extensions.TypedDict, total=False):
    dayOfWeeks: _list[ResourcePolicyWeeklyCycleDayOfWeek]

@typing.type_check_only
class ResourcePolicyWeeklyCycleDayOfWeek(typing_extensions.TypedDict, total=False):
    day: typing_extensions.Literal[
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
class ResourcePolicyWorkloadPolicy(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["HIGH_AVAILABILITY", "HIGH_THROUGHPUT"]

@typing.type_check_only
class ResourceStatus(typing_extensions.TypedDict, total=False):
    physicalHost: str
    physicalHostTopology: ResourceStatusPhysicalHostTopology
    scheduling: ResourceStatusScheduling
    shutdownDetails: ResourceStatusShutdownDetails
    upcomingMaintenance: UpcomingMaintenance

@typing.type_check_only
class ResourceStatusPhysicalHostTopology(typing_extensions.TypedDict, total=False):
    block: str
    cluster: str
    host: str
    subblock: str

@typing.type_check_only
class ResourceStatusScheduling(typing_extensions.TypedDict, total=False):
    availabilityDomain: int
    terminationTimestamp: str

@typing.type_check_only
class ResourceStatusShutdownDetails(typing_extensions.TypedDict, total=False):
    maxDuration: Duration
    requestTimestamp: str
    stopState: typing_extensions.Literal["PENDING_STOP", "STOPPING"]
    targetState: typing_extensions.Literal["DELETED", "STOPPED"]

@typing.type_check_only
class RolloutPolicy(typing_extensions.TypedDict, total=False):
    defaultRolloutTime: str
    locationRolloutPolicies: dict[str, typing.Any]

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    asPaths: _list[RouteAsPath]
    creationTimestamp: str
    description: str
    destRange: str
    id: str
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
    nextHopOrigin: typing_extensions.Literal["EGP", "IGP", "INCOMPLETE"]
    nextHopPeering: str
    nextHopVpnTunnel: str
    priority: int
    routeStatus: typing_extensions.Literal["ACTIVE", "DROPPED", "INACTIVE", "PENDING"]
    routeType: typing_extensions.Literal["BGP", "STATIC", "SUBNET", "TRANSIT"]
    selfLink: str
    tags: _list[str]
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class RouteAsPath(typing_extensions.TypedDict, total=False):
    asLists: _list[int]
    pathSegmentType: typing_extensions.Literal[
        "AS_CONFED_SEQUENCE", "AS_CONFED_SET", "AS_SEQUENCE", "AS_SET"
    ]

@typing.type_check_only
class RouteList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Route]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RoutePolicy(typing_extensions.TypedDict, total=False):
    description: str
    fingerprint: str
    name: str
    terms: _list[RoutePolicyPolicyTerm]
    type: typing_extensions.Literal[
        "ROUTE_POLICY_TYPE_EXPORT", "ROUTE_POLICY_TYPE_IMPORT"
    ]

@typing.type_check_only
class RoutePolicyPolicyTerm(typing_extensions.TypedDict, total=False):
    actions: _list[Expr]
    match: Expr
    priority: int

@typing.type_check_only
class Router(typing_extensions.TypedDict, total=False):
    bgp: RouterBgp
    bgpPeers: _list[RouterBgpPeer]
    creationTimestamp: str
    description: str
    encryptedInterconnectRouter: bool
    id: str
    interfaces: _list[RouterInterface]
    kind: str
    md5AuthenticationKeys: _list[RouterMd5AuthenticationKey]
    name: str
    nats: _list[RouterNat]
    network: str
    region: str
    selfLink: str

@typing.type_check_only
class RouterAdvertisedIpRange(typing_extensions.TypedDict, total=False):
    description: str
    range: str

@typing.type_check_only
class RouterAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RouterBgp(typing_extensions.TypedDict, total=False):
    advertiseMode: typing_extensions.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: _list[typing_extensions.Literal["ALL_SUBNETS"]]
    advertisedIpRanges: _list[RouterAdvertisedIpRange]
    asn: int
    identifierRange: str
    keepaliveInterval: int

@typing.type_check_only
class RouterBgpPeer(typing_extensions.TypedDict, total=False):
    advertiseMode: typing_extensions.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: _list[typing_extensions.Literal["ALL_SUBNETS"]]
    advertisedIpRanges: _list[RouterAdvertisedIpRange]
    advertisedRoutePriority: int
    bfd: RouterBgpPeerBfd
    customLearnedIpRanges: _list[RouterBgpPeerCustomLearnedIpRange]
    customLearnedRoutePriority: int
    enable: typing_extensions.Literal["FALSE", "TRUE"]
    enableIpv4: bool
    enableIpv6: bool
    exportPolicies: _list[str]
    importPolicies: _list[str]
    interfaceName: str
    ipAddress: str
    ipv4NexthopAddress: str
    ipv6NexthopAddress: str
    managementType: typing_extensions.Literal[
        "MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"
    ]
    md5AuthenticationKeyName: str
    name: str
    peerAsn: int
    peerIpAddress: str
    peerIpv4NexthopAddress: str
    peerIpv6NexthopAddress: str
    routerApplianceInstance: str

@typing.type_check_only
class RouterBgpPeerBfd(typing_extensions.TypedDict, total=False):
    minReceiveInterval: int
    minTransmitInterval: int
    multiplier: int
    sessionInitializationMode: typing_extensions.Literal[
        "ACTIVE", "DISABLED", "PASSIVE"
    ]

@typing.type_check_only
class RouterBgpPeerCustomLearnedIpRange(typing_extensions.TypedDict, total=False):
    range: str

@typing.type_check_only
class RouterInterface(typing_extensions.TypedDict, total=False):
    ipRange: str
    ipVersion: typing_extensions.Literal["IPV4", "IPV6"]
    linkedInterconnectAttachment: str
    linkedVpnTunnel: str
    managementType: typing_extensions.Literal[
        "MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"
    ]
    name: str
    privateIpAddress: str
    redundantInterface: str
    subnetwork: str

@typing.type_check_only
class RouterList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Router]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class RouterMd5AuthenticationKey(typing_extensions.TypedDict, total=False):
    key: str
    name: str

@typing.type_check_only
class RouterNat(typing_extensions.TypedDict, total=False):
    autoNetworkTier: typing_extensions.Literal[
        "FIXED_STANDARD", "PREMIUM", "STANDARD", "STANDARD_OVERRIDES_FIXED_STANDARD"
    ]
    drainNatIps: _list[str]
    enableDynamicPortAllocation: bool
    enableEndpointIndependentMapping: bool
    endpointTypes: _list[
        typing_extensions.Literal[
            "ENDPOINT_TYPE_MANAGED_PROXY_LB", "ENDPOINT_TYPE_SWG", "ENDPOINT_TYPE_VM"
        ]
    ]
    icmpIdleTimeoutSec: int
    logConfig: RouterNatLogConfig
    maxPortsPerVm: int
    minPortsPerVm: int
    name: str
    nat64Subnetworks: _list[RouterNatSubnetworkToNat64]
    natIpAllocateOption: typing_extensions.Literal["AUTO_ONLY", "MANUAL_ONLY"]
    natIps: _list[str]
    rules: _list[RouterNatRule]
    sourceSubnetworkIpRangesToNat: typing_extensions.Literal[
        "ALL_SUBNETWORKS_ALL_IP_RANGES",
        "ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES",
        "LIST_OF_SUBNETWORKS",
    ]
    sourceSubnetworkIpRangesToNat64: typing_extensions.Literal[
        "ALL_IPV6_SUBNETWORKS", "LIST_OF_IPV6_SUBNETWORKS"
    ]
    subnetworks: _list[RouterNatSubnetworkToNat]
    tcpEstablishedIdleTimeoutSec: int
    tcpTimeWaitTimeoutSec: int
    tcpTransitoryIdleTimeoutSec: int
    type: typing_extensions.Literal["PRIVATE", "PUBLIC"]
    udpIdleTimeoutSec: int

@typing.type_check_only
class RouterNatLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    filter: typing_extensions.Literal["ALL", "ERRORS_ONLY", "TRANSLATIONS_ONLY"]

@typing.type_check_only
class RouterNatRule(typing_extensions.TypedDict, total=False):
    action: RouterNatRuleAction
    description: str
    match: str
    ruleNumber: int

@typing.type_check_only
class RouterNatRuleAction(typing_extensions.TypedDict, total=False):
    sourceNatActiveIps: _list[str]
    sourceNatActiveRanges: _list[str]
    sourceNatDrainIps: _list[str]
    sourceNatDrainRanges: _list[str]

@typing.type_check_only
class RouterNatSubnetworkToNat(typing_extensions.TypedDict, total=False):
    name: str
    secondaryIpRangeNames: _list[str]
    sourceIpRangesToNat: _list[
        typing_extensions.Literal[
            "ALL_IP_RANGES", "LIST_OF_SECONDARY_IP_RANGES", "PRIMARY_IP_RANGE"
        ]
    ]

@typing.type_check_only
class RouterNatSubnetworkToNat64(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class RouterStatus(typing_extensions.TypedDict, total=False):
    bestRoutes: _list[Route]
    bestRoutesForRouter: _list[Route]
    bgpPeerStatus: _list[RouterStatusBgpPeerStatus]
    natStatus: _list[RouterStatusNatStatus]
    network: str

@typing.type_check_only
class RouterStatusBgpPeerStatus(typing_extensions.TypedDict, total=False):
    advertisedRoutes: _list[Route]
    bfdStatus: BfdStatus
    enableIpv4: bool
    enableIpv6: bool
    ipAddress: str
    ipv4NexthopAddress: str
    ipv6NexthopAddress: str
    linkedVpnTunnel: str
    md5AuthEnabled: bool
    name: str
    numLearnedRoutes: int
    peerIpAddress: str
    peerIpv4NexthopAddress: str
    peerIpv6NexthopAddress: str
    routerApplianceInstance: str
    state: str
    status: typing_extensions.Literal["DOWN", "UNKNOWN", "UP"]
    statusReason: typing_extensions.Literal[
        "IPV4_PEER_ON_IPV6_ONLY_CONNECTION",
        "IPV6_PEER_ON_IPV4_ONLY_CONNECTION",
        "MD5_AUTH_INTERNAL_PROBLEM",
        "STATUS_REASON_UNSPECIFIED",
    ]
    uptime: str
    uptimeSeconds: str

@typing.type_check_only
class RouterStatusNatStatus(typing_extensions.TypedDict, total=False):
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
class RouterStatusNatStatusNatRuleStatus(typing_extensions.TypedDict, total=False):
    activeNatIps: _list[str]
    drainNatIps: _list[str]
    minExtraIpsNeeded: int
    numVmEndpointsWithNatMappings: int
    ruleNumber: int

@typing.type_check_only
class RouterStatusResponse(typing_extensions.TypedDict, total=False):
    kind: str
    result: RouterStatus

@typing.type_check_only
class RoutersGetRoutePolicyResponse(typing_extensions.TypedDict, total=False):
    resource: RoutePolicy

@typing.type_check_only
class RoutersListBgpRoutes(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    nextPageToken: str
    result: _list[BgpRoute]
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RoutersListRoutePolicies(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    nextPageToken: str
    result: _list[RoutePolicy]
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class RoutersPreviewResponse(typing_extensions.TypedDict, total=False):
    resource: Router

@typing.type_check_only
class RoutersScopedList(typing_extensions.TypedDict, total=False):
    routers: _list[Router]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SSLHealthCheck(typing_extensions.TypedDict, total=False):
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    request: str
    response: str

@typing.type_check_only
class SavedAttachedDisk(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    diskType: str
    guestOsFeatures: _list[GuestOsFeature]
    index: int
    interface: typing_extensions.Literal["NVME", "SCSI"]
    kind: str
    licenses: _list[str]
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    source: str
    storageBytes: str
    storageBytesStatus: typing_extensions.Literal["UPDATING", "UP_TO_DATE"]
    type: typing_extensions.Literal["PERSISTENT", "SCRATCH"]

@typing.type_check_only
class SavedDisk(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
    kind: str
    sourceDisk: str
    storageBytes: str
    storageBytesStatus: typing_extensions.Literal["UPDATING", "UP_TO_DATE"]

@typing.type_check_only
class ScalingScheduleStatus(typing_extensions.TypedDict, total=False):
    lastStartTime: str
    nextStartTime: str
    state: typing_extensions.Literal["ACTIVE", "DISABLED", "OBSOLETE", "READY"]

@typing.type_check_only
class Scheduling(typing_extensions.TypedDict, total=False):
    automaticRestart: bool
    availabilityDomain: int
    gracefulShutdown: SchedulingGracefulShutdown
    hostErrorTimeoutSeconds: int
    instanceTerminationAction: typing_extensions.Literal[
        "DELETE", "INSTANCE_TERMINATION_ACTION_UNSPECIFIED", "STOP"
    ]
    localSsdRecoveryTimeout: Duration
    locationHint: str
    maintenanceFreezeDurationHours: int
    maintenanceInterval: typing_extensions.Literal["AS_NEEDED", "PERIODIC", "RECURRENT"]
    maxRunDuration: Duration
    minNodeCpus: int
    nodeAffinities: _list[SchedulingNodeAffinity]
    onHostMaintenance: typing_extensions.Literal["MIGRATE", "TERMINATE"]
    onInstanceStopAction: SchedulingOnInstanceStopAction
    preemptible: bool
    provisioningModel: typing_extensions.Literal[
        "RESERVATION_BOUND", "SPOT", "STANDARD"
    ]
    terminationTime: str

@typing.type_check_only
class SchedulingGracefulShutdown(typing_extensions.TypedDict, total=False):
    enabled: bool
    maxDuration: Duration

@typing.type_check_only
class SchedulingNodeAffinity(typing_extensions.TypedDict, total=False):
    key: str
    operator: typing_extensions.Literal["IN", "NOT_IN", "OPERATOR_UNSPECIFIED"]
    values: _list[str]

@typing.type_check_only
class SchedulingOnInstanceStopAction(typing_extensions.TypedDict, total=False):
    discardLocalSsd: bool

@typing.type_check_only
class Screenshot(typing_extensions.TypedDict, total=False):
    contents: str
    kind: str

@typing.type_check_only
class SecurityPoliciesAggregatedList(typing_extensions.TypedDict, total=False):
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
    typing_extensions.TypedDict, total=False
):
    preconfiguredExpressionSets: SecurityPoliciesWafConfig

@typing.type_check_only
class SecurityPoliciesScopedList(typing_extensions.TypedDict, total=False):
    securityPolicies: _list[SecurityPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SecurityPoliciesWafConfig(typing_extensions.TypedDict, total=False):
    wafRules: PreconfiguredWafSet

@typing.type_check_only
class SecurityPolicy(typing_extensions.TypedDict, total=False):
    adaptiveProtectionConfig: SecurityPolicyAdaptiveProtectionConfig
    advancedOptionsConfig: SecurityPolicyAdvancedOptionsConfig
    associations: _list[SecurityPolicyAssociation]
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
    type: typing_extensions.Literal[
        "CLOUD_ARMOR", "CLOUD_ARMOR_EDGE", "CLOUD_ARMOR_NETWORK", "FIREWALL"
    ]
    userDefinedFields: _list[SecurityPolicyUserDefinedField]

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfig(typing_extensions.TypedDict, total=False):
    autoDeployConfig: SecurityPolicyAdaptiveProtectionConfigAutoDeployConfig
    layer7DdosDefenseConfig: (
        SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig
    )

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigAutoDeployConfig(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    expirationSec: int
    impactedBaselineThreshold: float
    loadThreshold: float

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig(
    typing_extensions.TypedDict, total=False
):
    enable: bool
    ruleVisibility: typing_extensions.Literal["PREMIUM", "STANDARD"]
    thresholdConfigs: _list[
        SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigThresholdConfig
    ]

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfigThresholdConfig(
    typing_extensions.TypedDict, total=False
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
    typing_extensions.TypedDict, total=False
):
    enableEachUniqueValue: bool
    type: typing_extensions.Literal["HTTP_HEADER_HOST", "HTTP_PATH", "UNSPECIFIED_TYPE"]
    value: str

@typing.type_check_only
class SecurityPolicyAdvancedOptionsConfig(typing_extensions.TypedDict, total=False):
    jsonCustomConfig: SecurityPolicyAdvancedOptionsConfigJsonCustomConfig
    jsonParsing: typing_extensions.Literal[
        "DISABLED", "STANDARD", "STANDARD_WITH_GRAPHQL"
    ]
    logLevel: typing_extensions.Literal["NORMAL", "VERBOSE"]
    requestBodyInspectionSize: str
    userIpRequestHeaders: _list[str]

@typing.type_check_only
class SecurityPolicyAdvancedOptionsConfigJsonCustomConfig(
    typing_extensions.TypedDict, total=False
):
    contentTypes: _list[str]

@typing.type_check_only
class SecurityPolicyAssociation(typing_extensions.TypedDict, total=False):
    attachmentId: str
    displayName: str
    excludedFolders: _list[str]
    excludedProjects: _list[str]
    name: str
    securityPolicyId: str
    shortName: str

@typing.type_check_only
class SecurityPolicyDdosProtectionConfig(typing_extensions.TypedDict, total=False):
    ddosProtection: typing_extensions.Literal[
        "ADVANCED", "ADVANCED_PREVIEW", "STANDARD"
    ]

@typing.type_check_only
class SecurityPolicyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[SecurityPolicy]
    kind: str
    nextPageToken: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SecurityPolicyRecaptchaOptionsConfig(typing_extensions.TypedDict, total=False):
    redirectSiteKey: str

@typing.type_check_only
class SecurityPolicyReference(typing_extensions.TypedDict, total=False):
    securityPolicy: str

@typing.type_check_only
class SecurityPolicyRule(typing_extensions.TypedDict, total=False):
    action: str
    description: str
    direction: typing_extensions.Literal["EGRESS", "INGRESS"]
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
    ruleNumber: str
    ruleTupleCount: int
    targetResources: _list[str]
    targetServiceAccounts: _list[str]

@typing.type_check_only
class SecurityPolicyRuleHttpHeaderAction(typing_extensions.TypedDict, total=False):
    requestHeadersToAdds: _list[SecurityPolicyRuleHttpHeaderActionHttpHeaderOption]

@typing.type_check_only
class SecurityPolicyRuleHttpHeaderActionHttpHeaderOption(
    typing_extensions.TypedDict, total=False
):
    headerName: str
    headerValue: str

@typing.type_check_only
class SecurityPolicyRuleMatcher(typing_extensions.TypedDict, total=False):
    config: SecurityPolicyRuleMatcherConfig
    expr: Expr
    exprOptions: SecurityPolicyRuleMatcherExprOptions
    versionedExpr: typing_extensions.Literal["FIREWALL", "SRC_IPS_V1"]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfig(typing_extensions.TypedDict, total=False):
    destIpRanges: _list[str]
    layer4Configs: _list[SecurityPolicyRuleMatcherConfigLayer4Config]
    srcIpRanges: _list[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfigLayer4Config(
    typing_extensions.TypedDict, total=False
):
    ipProtocol: str
    ports: _list[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherExprOptions(typing_extensions.TypedDict, total=False):
    recaptchaOptions: SecurityPolicyRuleMatcherExprOptionsRecaptchaOptions

@typing.type_check_only
class SecurityPolicyRuleMatcherExprOptionsRecaptchaOptions(
    typing_extensions.TypedDict, total=False
):
    actionTokenSiteKeys: _list[str]
    sessionTokenSiteKeys: _list[str]

@typing.type_check_only
class SecurityPolicyRuleNetworkMatcher(typing_extensions.TypedDict, total=False):
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
    typing_extensions.TypedDict, total=False
):
    name: str
    values: _list[str]

@typing.type_check_only
class SecurityPolicyRulePreconfiguredWafConfig(
    typing_extensions.TypedDict, total=False
):
    exclusions: _list[SecurityPolicyRulePreconfiguredWafConfigExclusion]

@typing.type_check_only
class SecurityPolicyRulePreconfiguredWafConfigExclusion(
    typing_extensions.TypedDict, total=False
):
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
    typing_extensions.TypedDict, total=False
):
    op: typing_extensions.Literal[
        "CONTAINS", "ENDS_WITH", "EQUALS", "EQUALS_ANY", "STARTS_WITH"
    ]
    val: str

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptions(typing_extensions.TypedDict, total=False):
    banDurationSec: int
    banThreshold: SecurityPolicyRuleRateLimitOptionsThreshold
    conformAction: str
    enforceOnKey: typing_extensions.Literal[
        "ALL",
        "ALL_IPS",
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
    exceedRedirectOptions: SecurityPolicyRuleRedirectOptions
    rateLimitThreshold: SecurityPolicyRuleRateLimitOptionsThreshold

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptionsEnforceOnKeyConfig(
    typing_extensions.TypedDict, total=False
):
    enforceOnKeyName: str
    enforceOnKeyType: typing_extensions.Literal[
        "ALL",
        "ALL_IPS",
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
class SecurityPolicyRuleRateLimitOptionsThreshold(
    typing_extensions.TypedDict, total=False
):
    count: int
    intervalSec: int

@typing.type_check_only
class SecurityPolicyRuleRedirectOptions(typing_extensions.TypedDict, total=False):
    target: str
    type: typing_extensions.Literal["EXTERNAL_302", "GOOGLE_RECAPTCHA"]

@typing.type_check_only
class SecurityPolicyUserDefinedField(typing_extensions.TypedDict, total=False):
    base: typing_extensions.Literal["IPV4", "IPV6", "TCP", "UDP"]
    mask: str
    name: str
    offset: int
    size: int

@typing.type_check_only
class SecuritySettings(typing_extensions.TypedDict, total=False):
    authentication: str
    awsV4Authentication: AWSV4Signature
    clientTlsPolicy: str
    subjectAltNames: _list[str]

@typing.type_check_only
class SerialPortOutput(typing_extensions.TypedDict, total=False):
    contents: str
    kind: str
    next: str
    selfLink: str
    start: str

@typing.type_check_only
class ServerBinding(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "RESTART_NODE_ON_ANY_SERVER",
        "RESTART_NODE_ON_MINIMAL_SERVERS",
        "SERVER_BINDING_TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: _list[str]

@typing.type_check_only
class ServiceAttachment(typing_extensions.TypedDict, total=False):
    connectedEndpoints: _list[ServiceAttachmentConnectedEndpoint]
    connectionPreference: typing_extensions.Literal[
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
    name: str
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
class ServiceAttachmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class ServiceAttachmentConnectedEndpoint(typing_extensions.TypedDict, total=False):
    consumerNetwork: str
    endpoint: str
    propagatedConnectionCount: int
    pscConnectionId: str
    status: typing_extensions.Literal[
        "ACCEPTED",
        "CLOSED",
        "NEEDS_ATTENTION",
        "PENDING",
        "REJECTED",
        "STATUS_UNSPECIFIED",
    ]

@typing.type_check_only
class ServiceAttachmentConsumerProjectLimit(typing_extensions.TypedDict, total=False):
    connectionLimit: int
    networkUrl: str
    projectIdOrNum: str

@typing.type_check_only
class ServiceAttachmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[ServiceAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ServiceAttachmentTunnelingConfig(typing_extensions.TypedDict, total=False):
    encapsulationProfile: typing_extensions.Literal[
        "GENEVE_SECURITY_V1", "UNSPECIFIED_ENCAPSULATION_PROFILE"
    ]
    routingMode: typing_extensions.Literal[
        "PACKET_INJECTION", "STANDARD_ROUTING", "UNSPECIFIED_ROUTING_MODE"
    ]

@typing.type_check_only
class ServiceAttachmentsScopedList(typing_extensions.TypedDict, total=False):
    serviceAttachments: _list[ServiceAttachment]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SetCommonInstanceMetadataOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    clientOperationId: str
    perLocationOperations: dict[str, typing.Any]

@typing.type_check_only
class SetCommonInstanceMetadataOperationMetadataPerLocationOperationInfo(
    typing_extensions.TypedDict, total=False
):
    error: Status
    state: typing_extensions.Literal[
        "ABANDONED", "DONE", "FAILED", "PROPAGATED", "PROPAGATING", "UNSPECIFIED"
    ]

@typing.type_check_only
class ShareSettings(typing_extensions.TypedDict, total=False):
    projectMap: dict[str, typing.Any]
    projects: _list[str]
    shareType: typing_extensions.Literal[
        "LOCAL", "ORGANIZATION", "SHARE_TYPE_UNSPECIFIED", "SPECIFIC_PROJECTS"
    ]

@typing.type_check_only
class ShareSettingsProjectConfig(typing_extensions.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class ShieldedInstanceIdentity(typing_extensions.TypedDict, total=False):
    encryptionKey: ShieldedInstanceIdentityEntry
    kind: str
    signingKey: ShieldedInstanceIdentityEntry

@typing.type_check_only
class ShieldedInstanceIdentityEntry(typing_extensions.TypedDict, total=False):
    ekCert: str
    ekPub: str

@typing.type_check_only
class ShieldedInstanceIntegrityPolicy(typing_extensions.TypedDict, total=False):
    updateAutoLearnPolicy: bool

@typing.type_check_only
class ShieldedVmConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

@typing.type_check_only
class ShieldedVmIdentity(typing_extensions.TypedDict, total=False):
    encryptionKey: ShieldedVmIdentityEntry
    kind: str
    signingKey: ShieldedVmIdentityEntry

@typing.type_check_only
class ShieldedVmIdentityEntry(typing_extensions.TypedDict, total=False):
    ekCert: str
    ekPub: str

@typing.type_check_only
class ShieldedVmIntegrityPolicy(typing_extensions.TypedDict, total=False):
    updateAutoLearnPolicy: bool

@typing.type_check_only
class SignedUrlKey(typing_extensions.TypedDict, total=False):
    keyName: str
    keyValue: str

@typing.type_check_only
class Snapshot(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED", "ARM64", "X86_64"
    ]
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
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    selfLink: str
    snapshotEncryptionKey: CustomerEncryptionKey
    snapshotType: typing_extensions.Literal["ARCHIVE", "STANDARD"]
    sourceDisk: str
    sourceDiskEncryptionKey: CustomerEncryptionKey
    sourceDiskForRecoveryCheckpoint: str
    sourceDiskId: str
    sourceInstantSnapshot: str
    sourceInstantSnapshotEncryptionKey: CustomerEncryptionKey
    sourceInstantSnapshotId: str
    sourceSnapshotSchedulePolicy: str
    sourceSnapshotSchedulePolicyId: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "UPLOADING"
    ]
    storageBytes: str
    storageBytesStatus: typing_extensions.Literal["UPDATING", "UP_TO_DATE"]
    storageLocations: _list[str]
    userLicenses: _list[str]

@typing.type_check_only
class SnapshotList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Snapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SnapshotSettings(typing_extensions.TypedDict, total=False):
    storageLocation: SnapshotSettingsStorageLocationSettings

@typing.type_check_only
class SnapshotSettingsStorageLocationSettings(typing_extensions.TypedDict, total=False):
    locations: dict[str, typing.Any]
    policy: typing_extensions.Literal[
        "LOCAL_REGION",
        "NEAREST_MULTI_REGION",
        "SPECIFIC_LOCATIONS",
        "STORAGE_LOCATION_POLICY_UNSPECIFIED",
    ]

@typing.type_check_only
class SnapshotSettingsStorageLocationSettingsStorageLocationPreference(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class SourceDiskEncryptionKey(typing_extensions.TypedDict, total=False):
    diskEncryptionKey: CustomerEncryptionKey
    sourceDisk: str

@typing.type_check_only
class SourceInstanceParams(typing_extensions.TypedDict, total=False):
    diskConfigs: _list[DiskInstantiationConfig]

@typing.type_check_only
class SourceInstanceProperties(typing_extensions.TypedDict, total=False):
    canIpForward: bool
    deletionProtection: bool
    description: str
    disks: _list[SavedAttachedDisk]
    guestAccelerators: _list[AcceleratorConfig]
    keyRevocationActionType: typing_extensions.Literal[
        "KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "NONE", "STOP"
    ]
    labels: dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: _list[NetworkInterface]
    postKeyRevocationActionType: typing_extensions.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    scheduling: Scheduling
    serviceAccounts: _list[ServiceAccount]
    tags: Tags

@typing.type_check_only
class SslCertificate(typing_extensions.TypedDict, total=False):
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
    selfManaged: SslCertificateSelfManagedSslCertificate
    subjectAlternativeNames: _list[str]
    type: typing_extensions.Literal["MANAGED", "SELF_MANAGED", "TYPE_UNSPECIFIED"]

@typing.type_check_only
class SslCertificateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslCertificateList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[SslCertificate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslCertificateManagedSslCertificate(typing_extensions.TypedDict, total=False):
    domainStatus: dict[str, typing.Any]
    domains: _list[str]
    status: typing_extensions.Literal[
        "ACTIVE",
        "MANAGED_CERTIFICATE_STATUS_UNSPECIFIED",
        "PROVISIONING",
        "PROVISIONING_FAILED",
        "PROVISIONING_FAILED_PERMANENTLY",
        "RENEWAL_FAILED",
    ]

@typing.type_check_only
class SslCertificateSelfManagedSslCertificate(typing_extensions.TypedDict, total=False):
    certificate: str
    privateKey: str

@typing.type_check_only
class SslCertificatesScopedList(typing_extensions.TypedDict, total=False):
    sslCertificates: _list[SslCertificate]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesAggregatedList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[SslPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesListAvailableFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: _list[str]

@typing.type_check_only
class SslPoliciesScopedList(typing_extensions.TypedDict, total=False):
    sslPolicies: _list[SslPolicy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SslPolicy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    customFeatures: _list[str]
    description: str
    enabledFeatures: _list[str]
    fingerprint: str
    id: str
    kind: str
    minTlsVersion: typing_extensions.Literal["TLS_1_0", "TLS_1_1", "TLS_1_2"]
    name: str
    profile: typing_extensions.Literal["COMPATIBLE", "CUSTOM", "MODERN", "RESTRICTED"]
    region: str
    selfLink: str
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class SslPolicyReference(typing_extensions.TypedDict, total=False):
    sslPolicy: str

@typing.type_check_only
class StatefulPolicy(typing_extensions.TypedDict, total=False):
    preservedState: StatefulPolicyPreservedState

@typing.type_check_only
class StatefulPolicyPreservedState(typing_extensions.TypedDict, total=False):
    disks: dict[str, typing.Any]
    externalIPs: dict[str, typing.Any]
    internalIPs: dict[str, typing.Any]

@typing.type_check_only
class StatefulPolicyPreservedStateDiskDevice(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

@typing.type_check_only
class StatefulPolicyPreservedStateNetworkIp(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StoragePool(typing_extensions.TypedDict, total=False):
    capacityProvisioningType: typing_extensions.Literal[
        "ADVANCED", "STANDARD", "UNSPECIFIED"
    ]
    creationTimestamp: str
    description: str
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    performanceProvisioningType: typing_extensions.Literal[
        "ADVANCED", "STANDARD", "UNSPECIFIED"
    ]
    poolProvisionedCapacityGb: str
    poolProvisionedIops: str
    poolProvisionedThroughput: str
    resourceStatus: StoragePoolResourceStatus
    selfLink: str
    selfLinkWithId: str
    state: typing_extensions.Literal["CREATING", "DELETING", "FAILED", "READY"]
    status: StoragePoolResourceStatus
    storagePoolType: str
    zone: str

@typing.type_check_only
class StoragePoolAggregatedList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolDisk(typing_extensions.TypedDict, total=False):
    attachedInstances: _list[str]
    creationTimestamp: str
    disk: str
    name: str
    provisionedIops: str
    provisionedThroughput: str
    resourcePolicies: _list[str]
    sizeGb: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RESTORING", "UNAVAILABLE"
    ]
    type: str
    usedBytes: str

@typing.type_check_only
class StoragePoolList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[StoragePool]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolListDisks(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: _list[StoragePoolDisk]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolResourceStatus(typing_extensions.TypedDict, total=False):
    diskCount: str
    lastResizeTimestamp: str
    maxTotalProvisionedDiskCapacityGb: str
    poolUsedCapacityBytes: str
    poolUsedIops: str
    poolUsedThroughput: str
    poolUserWrittenBytes: str
    totalProvisionedDiskCapacityGb: str
    totalProvisionedDiskIops: str
    totalProvisionedDiskThroughput: str

@typing.type_check_only
class StoragePoolType(typing_extensions.TypedDict, total=False):
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
class StoragePoolTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[StoragePoolType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolTypesScopedList(typing_extensions.TypedDict, total=False):
    storagePoolTypes: _list[StoragePoolType]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StoragePoolsScopedList(typing_extensions.TypedDict, total=False):
    storagePools: _list[StoragePool]
    warning: dict[str, typing.Any]

@typing.type_check_only
class StructuredEntries(typing_extensions.TypedDict, total=False):
    entries: dict[str, typing.Any]

@typing.type_check_only
class Subnetwork(typing_extensions.TypedDict, total=False):
    allowSubnetCidrRoutesOverlap: bool
    creationTimestamp: str
    description: str
    enableFlowLogs: bool
    externalIpv6Prefix: str
    fingerprint: str
    gatewayAddress: str
    id: str
    internalIpv6Prefix: str
    ipCidrRange: str
    ipCollection: str
    ipv6AccessType: typing_extensions.Literal["EXTERNAL", "INTERNAL"]
    ipv6CidrRange: str
    ipv6GceEndpoint: typing_extensions.Literal["VM_AND_FR", "VM_ONLY"]
    kind: str
    logConfig: SubnetworkLogConfig
    name: str
    network: str
    privateIpGoogleAccess: bool
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "DISABLE_GOOGLE_ACCESS",
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
    ]
    purpose: typing_extensions.Literal[
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
    role: typing_extensions.Literal["ACTIVE", "BACKUP"]
    secondaryIpRanges: _list[SubnetworkSecondaryRange]
    selfLink: str
    stackType: typing_extensions.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    state: typing_extensions.Literal["DRAINING", "READY"]

@typing.type_check_only
class SubnetworkAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworkList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Subnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworkLogConfig(typing_extensions.TypedDict, total=False):
    aggregationInterval: typing_extensions.Literal[
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
    metadata: typing_extensions.Literal[
        "CUSTOM_METADATA", "EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"
    ]
    metadataFields: _list[str]

@typing.type_check_only
class SubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str
    reservedInternalRange: str

@typing.type_check_only
class SubnetworksExpandIpCidrRangeRequest(typing_extensions.TypedDict, total=False):
    ipCidrRange: str

@typing.type_check_only
class SubnetworksScopedList(typing_extensions.TypedDict, total=False):
    subnetworks: _list[Subnetwork]
    warning: dict[str, typing.Any]

@typing.type_check_only
class SubnetworksSetPrivateIpGoogleAccessRequest(
    typing_extensions.TypedDict, total=False
):
    privateIpGoogleAccess: bool

@typing.type_check_only
class Subsetting(typing_extensions.TypedDict, total=False):
    policy: typing_extensions.Literal["CONSISTENT_HASH_SUBSETTING", "NONE"]
    subsetSize: int

@typing.type_check_only
class TCPHealthCheck(typing_extensions.TypedDict, total=False):
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    request: str
    response: str

@typing.type_check_only
class Tags(typing_extensions.TypedDict, total=False):
    fingerprint: str
    items: _list[str]

@typing.type_check_only
class TargetGrpcProxy(typing_extensions.TypedDict, total=False):
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
class TargetGrpcProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetGrpcProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetHttpProxies: _list[TargetHttpProxy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxy(typing_extensions.TypedDict, total=False):
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
    urlMap: str

@typing.type_check_only
class TargetHttpProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetHttpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetHttpsProxies: _list[TargetHttpsProxy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxiesSetCertificateMapRequest(
    typing_extensions.TypedDict, total=False
):
    certificateMap: str

@typing.type_check_only
class TargetHttpsProxiesSetQuicOverrideRequest(
    typing_extensions.TypedDict, total=False
):
    quicOverride: typing_extensions.Literal["DISABLE", "ENABLE", "NONE"]

@typing.type_check_only
class TargetHttpsProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: _list[str]

@typing.type_check_only
class TargetHttpsProxy(typing_extensions.TypedDict, total=False):
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
    quicOverride: typing_extensions.Literal["DISABLE", "ENABLE", "NONE"]
    region: str
    selfLink: str
    serverTlsPolicy: str
    sslCertificates: _list[str]
    sslPolicy: str
    tlsEarlyData: typing_extensions.Literal[
        "DISABLED", "PERMISSIVE", "STRICT", "UNRESTRICTED"
    ]
    urlMap: str

@typing.type_check_only
class TargetHttpsProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetHttpsProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetInstance(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    instance: str
    kind: str
    name: str
    natPolicy: typing_extensions.Literal["NO_NAT"]
    network: str
    securityPolicy: str
    selfLink: str
    zone: str

@typing.type_check_only
class TargetInstanceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetInstanceList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetInstance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetInstancesScopedList(typing_extensions.TypedDict, total=False):
    targetInstances: _list[TargetInstance]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetPool(typing_extensions.TypedDict, total=False):
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
    sessionAffinity: typing_extensions.Literal[
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
class TargetPoolAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetPoolInstanceHealth(typing_extensions.TypedDict, total=False):
    healthStatus: _list[HealthStatus]
    kind: str

@typing.type_check_only
class TargetPoolList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetPool]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetPoolsAddHealthCheckRequest(typing_extensions.TypedDict, total=False):
    healthChecks: _list[HealthCheckReference]

@typing.type_check_only
class TargetPoolsAddInstanceRequest(typing_extensions.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class TargetPoolsRemoveHealthCheckRequest(typing_extensions.TypedDict, total=False):
    healthChecks: _list[HealthCheckReference]

@typing.type_check_only
class TargetPoolsRemoveInstanceRequest(typing_extensions.TypedDict, total=False):
    instances: _list[InstanceReference]

@typing.type_check_only
class TargetPoolsScopedList(typing_extensions.TypedDict, total=False):
    targetPools: _list[TargetPool]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetReference(typing_extensions.TypedDict, total=False):
    target: str

@typing.type_check_only
class TargetSslProxiesSetBackendServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: str

@typing.type_check_only
class TargetSslProxiesSetCertificateMapRequest(
    typing_extensions.TypedDict, total=False
):
    certificateMap: str

@typing.type_check_only
class TargetSslProxiesSetProxyHeaderRequest(typing_extensions.TypedDict, total=False):
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]

@typing.type_check_only
class TargetSslProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: _list[str]

@typing.type_check_only
class TargetSslProxy(typing_extensions.TypedDict, total=False):
    certificateMap: str
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    selfLink: str
    service: str
    sslCertificates: _list[str]
    sslPolicy: str

@typing.type_check_only
class TargetSslProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetSslProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetTcpProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetTcpProxies: _list[TargetTcpProxy]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetTcpProxiesSetBackendServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: str

@typing.type_check_only
class TargetTcpProxiesSetProxyHeaderRequest(typing_extensions.TypedDict, total=False):
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]

@typing.type_check_only
class TargetTcpProxy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    proxyBind: bool
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    region: str
    selfLink: str
    service: str

@typing.type_check_only
class TargetTcpProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetTcpProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetTcpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGateway(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    forwardingRules: _list[str]
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    region: str
    selfLink: str
    status: typing_extensions.Literal["CREATING", "DELETING", "FAILED", "READY"]
    tunnels: _list[str]

@typing.type_check_only
class TargetVpnGatewayAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewayList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[TargetVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewaysScopedList(typing_extensions.TypedDict, total=False):
    targetVpnGateways: _list[TargetVpnGateway]
    warning: dict[str, typing.Any]

@typing.type_check_only
class TestFailure(typing_extensions.TypedDict, total=False):
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
class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Uint128(typing_extensions.TypedDict, total=False):
    high: str
    low: str

@typing.type_check_only
class UpcomingMaintenance(typing_extensions.TypedDict, total=False):
    canReschedule: bool
    latestWindowStartTime: str
    maintenanceStatus: typing_extensions.Literal["ONGOING", "PENDING", "UNKNOWN"]
    type: typing_extensions.Literal["SCHEDULED", "UNKNOWN_TYPE", "UNSCHEDULED"]
    windowEndTime: str
    windowStartTime: str

@typing.type_check_only
class UrlMap(typing_extensions.TypedDict, total=False):
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
    tests: _list[UrlMapTest]

@typing.type_check_only
class UrlMapList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[UrlMap]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class UrlMapReference(typing_extensions.TypedDict, total=False):
    urlMap: str

@typing.type_check_only
class UrlMapTest(typing_extensions.TypedDict, total=False):
    description: str
    expectedOutputUrl: str
    expectedRedirectResponseCode: int
    headers: _list[UrlMapTestHeader]
    host: str
    path: str
    service: str

@typing.type_check_only
class UrlMapTestHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class UrlMapValidationResult(typing_extensions.TypedDict, total=False):
    loadErrors: _list[str]
    loadSucceeded: bool
    testFailures: _list[TestFailure]
    testPassed: bool

@typing.type_check_only
class UrlMapsAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class UrlMapsScopedList(typing_extensions.TypedDict, total=False):
    urlMaps: _list[UrlMap]
    warning: dict[str, typing.Any]

@typing.type_check_only
class UrlMapsValidateRequest(typing_extensions.TypedDict, total=False):
    loadBalancingSchemes: _list[
        typing_extensions.Literal[
            "EXTERNAL", "EXTERNAL_MANAGED", "LOAD_BALANCING_SCHEME_UNSPECIFIED"
        ]
    ]
    resource: UrlMap

@typing.type_check_only
class UrlMapsValidateResponse(typing_extensions.TypedDict, total=False):
    result: UrlMapValidationResult

@typing.type_check_only
class UrlRewrite(typing_extensions.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str
    pathTemplateRewrite: str

@typing.type_check_only
class UsableSubnetwork(typing_extensions.TypedDict, total=False):
    externalIpv6Prefix: str
    internalIpv6Prefix: str
    ipCidrRange: str
    ipv6AccessType: typing_extensions.Literal["EXTERNAL", "INTERNAL"]
    network: str
    purpose: typing_extensions.Literal[
        "GLOBAL_MANAGED_PROXY",
        "INTERNAL_HTTPS_LOAD_BALANCER",
        "PEER_MIGRATION",
        "PRIVATE",
        "PRIVATE_NAT",
        "PRIVATE_RFC_1918",
        "PRIVATE_SERVICE_CONNECT",
        "REGIONAL_MANAGED_PROXY",
    ]
    role: typing_extensions.Literal["ACTIVE", "BACKUP"]
    secondaryIpRanges: _list[UsableSubnetworkSecondaryRange]
    stackType: typing_extensions.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    subnetwork: str

@typing.type_check_only
class UsableSubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class UsableSubnetworksAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[UsableSubnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class UsageExportLocation(typing_extensions.TypedDict, total=False):
    bucketName: str
    reportNamePrefix: str

@typing.type_check_only
class VmEndpointNatMappings(typing_extensions.TypedDict, total=False):
    instanceName: str
    interfaceNatMappings: _list[VmEndpointNatMappingsInterfaceNatMappings]

@typing.type_check_only
class VmEndpointNatMappingsInterfaceNatMappings(
    typing_extensions.TypedDict, total=False
):
    drainNatIpPortRanges: _list[str]
    natIpPortRanges: _list[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    ruleMappings: _list[VmEndpointNatMappingsInterfaceNatMappingsNatRuleMappings]
    sourceAliasIpRange: str
    sourceVirtualIp: str

@typing.type_check_only
class VmEndpointNatMappingsInterfaceNatMappingsNatRuleMappings(
    typing_extensions.TypedDict, total=False
):
    drainNatIpPortRanges: _list[str]
    natIpPortRanges: _list[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    ruleNumber: int

@typing.type_check_only
class VmEndpointNatMappingsList(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    nextPageToken: str
    result: _list[VmEndpointNatMappings]
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnGateway(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    gatewayIpVersion: typing_extensions.Literal["IPV4", "IPV6"]
    id: str
    kind: str
    labelFingerprint: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    region: str
    selfLink: str
    stackType: typing_extensions.Literal["IPV4_IPV6", "IPV4_ONLY", "IPV6_ONLY"]
    vpnInterfaces: _list[VpnGatewayVpnGatewayInterface]

@typing.type_check_only
class VpnGatewayAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[VpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayStatus(typing_extensions.TypedDict, total=False):
    vpnConnections: _list[VpnGatewayStatusVpnConnection]

@typing.type_check_only
class VpnGatewayStatusHighAvailabilityRequirementState(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "CONNECTION_REDUNDANCY_MET", "CONNECTION_REDUNDANCY_NOT_MET"
    ]
    unsatisfiedReason: typing_extensions.Literal["INCOMPLETE_TUNNELS_COVERAGE"]

@typing.type_check_only
class VpnGatewayStatusTunnel(typing_extensions.TypedDict, total=False):
    localGatewayInterface: int
    peerGatewayInterface: int
    tunnelUrl: str

@typing.type_check_only
class VpnGatewayStatusVpnConnection(typing_extensions.TypedDict, total=False):
    peerExternalGateway: str
    peerGcpGateway: str
    state: VpnGatewayStatusHighAvailabilityRequirementState
    tunnels: _list[VpnGatewayStatusTunnel]

@typing.type_check_only
class VpnGatewayVpnGatewayInterface(typing_extensions.TypedDict, total=False):
    id: int
    interconnectAttachment: str
    ipAddress: str
    ipv6Address: str

@typing.type_check_only
class VpnGatewaysGetStatusResponse(typing_extensions.TypedDict, total=False):
    result: VpnGatewayStatus

@typing.type_check_only
class VpnGatewaysScopedList(typing_extensions.TypedDict, total=False):
    vpnGateways: _list[VpnGateway]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnel(typing_extensions.TypedDict, total=False):
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
    peerExternalGateway: str
    peerExternalGatewayInterface: int
    peerGcpGateway: str
    peerIp: str
    region: str
    remoteTrafficSelector: _list[str]
    router: str
    selfLink: str
    sharedSecret: str
    sharedSecretHash: str
    status: typing_extensions.Literal[
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
class VpnTunnelAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: _list[str]
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[VpnTunnel]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelsScopedList(typing_extensions.TypedDict, total=False):
    vpnTunnels: _list[VpnTunnel]
    warning: dict[str, typing.Any]

@typing.type_check_only
class WafExpressionSet(typing_extensions.TypedDict, total=False):
    aliases: _list[str]
    expressions: _list[WafExpressionSetExpression]
    id: str

@typing.type_check_only
class WafExpressionSetExpression(typing_extensions.TypedDict, total=False):
    id: str
    sensitivity: int

@typing.type_check_only
class WeightedBackendService(typing_extensions.TypedDict, total=False):
    backendService: str
    headerAction: HttpHeaderAction
    weight: int

@typing.type_check_only
class XpnHostList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Project]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class XpnResourceId(typing_extensions.TypedDict, total=False):
    id: str
    type: typing_extensions.Literal["PROJECT", "XPN_RESOURCE_TYPE_UNSPECIFIED"]

@typing.type_check_only
class Zone(typing_extensions.TypedDict, total=False):
    availableCpuPlatforms: _list[str]
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    status: typing_extensions.Literal["DOWN", "UP"]
    supportsPzs: bool

@typing.type_check_only
class ZoneList(typing_extensions.TypedDict, total=False):
    id: str
    items: _list[Zone]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: dict[str, typing.Any]

@typing.type_check_only
class ZoneSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class ZoneSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy
