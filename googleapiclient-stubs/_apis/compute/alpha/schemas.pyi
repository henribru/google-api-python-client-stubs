import typing

import typing_extensions
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
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class AcceleratorTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[AcceleratorType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AcceleratorTypesScopedList(typing_extensions.TypedDict, total=False):
    acceleratorTypes: typing.List[AcceleratorType]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AccessConfig(typing_extensions.TypedDict, total=False):
    externalIpv6: str
    externalIpv6PrefixLength: int
    kind: str
    name: str
    natIP: str
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    publicDnsName: str
    publicPtrDomainName: str
    setPublicDns: bool
    setPublicPtr: bool
    type: typing_extensions.Literal["DIRECT_IPV6", "ONE_TO_ONE_NAT"]

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    address: str
    addressType: typing_extensions.Literal[
        "DNS_FORWARDING", "EXTERNAL", "INTERNAL", "UNSPECIFIED_TYPE"
    ]
    creationTimestamp: str
    description: str
    id: str
    ipVersion: typing_extensions.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    network: str
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    prefixLength: int
    purpose: typing_extensions.Literal[
        "DNS_RESOLVER",
        "GCE_ENDPOINT",
        "IPSEC_INTERCONNECT",
        "NAT_AUTO",
        "PRIVATE_SERVICE_CONNECT",
        "PSC_PRODUCER_NAT_RANGE",
        "SHARED_LOADBALANCER_VIP",
        "VPC_PEERING",
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    status: typing_extensions.Literal["IN_USE", "RESERVED", "RESERVING"]
    subnetwork: str
    users: typing.List[str]

@typing.type_check_only
class AddressAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AddressList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Address]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AddressesScopedList(typing_extensions.TypedDict, total=False):
    addresses: typing.List[Address]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AdvancedMachineFeatures(typing_extensions.TypedDict, total=False):
    enableNestedVirtualization: bool
    threadsPerCore: int

@typing.type_check_only
class AliasIpRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    subnetworkRangeName: str

@typing.type_check_only
class AllocationShareSettings(typing_extensions.TypedDict, total=False):
    projects: typing.List[str]
    shareType: typing_extensions.Literal[
        "ORGANIZATION", "SHARE_TYPE_UNSPECIFIED", "SPECIFIC_PROJECTS"
    ]

@typing.type_check_only
class AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    interface: typing_extensions.Literal["NVDIMM", "NVME", "SCSI"]

@typing.type_check_only
class AllocationSpecificSKUAllocationReservedInstanceProperties(
    typing_extensions.TypedDict, total=False
):
    guestAccelerators: typing.List[AcceleratorConfig]
    localSsds: typing.List[
        AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk
    ]
    locationHint: str
    machineType: str
    maintenanceFreezeDurationHours: int
    maintenanceInterval: typing_extensions.Literal["PERIODIC"]
    minCpuPlatform: str

@typing.type_check_only
class AllocationSpecificSKUReservation(typing_extensions.TypedDict, total=False):
    count: str
    inUseCount: str
    instanceProperties: AllocationSpecificSKUAllocationReservedInstanceProperties

@typing.type_check_only
class Any(typing_extensions.TypedDict, total=False):
    typeUrl: str
    value: str

@typing.type_check_only
class AttachedDisk(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    forceAttach: bool
    guestOsFeatures: typing.List[GuestOsFeature]
    index: int
    initializeParams: AttachedDiskInitializeParams
    interface: typing_extensions.Literal["NVDIMM", "NVME", "SCSI"]
    kind: str
    licenses: typing.List[str]
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    savedState: typing_extensions.Literal["DISK_SAVED_STATE_UNSPECIFIED", "PRESERVED"]
    shieldedInstanceInitialState: InitialStateConfig
    source: str
    type: typing_extensions.Literal["PERSISTENT", "SCRATCH"]
    userLicenses: typing.List[str]

@typing.type_check_only
class AttachedDiskInitializeParams(typing_extensions.TypedDict, total=False):
    description: str
    diskName: str
    diskSizeGb: str
    diskType: str
    guestOsFeatures: typing.List[GuestOsFeature]
    labels: typing.Dict[str, typing.Any]
    multiWriter: bool
    onUpdateAction: typing_extensions.Literal[
        "RECREATE_DISK", "RECREATE_DISK_IF_SOURCE_CHANGED", "USE_EXISTING_DISK"
    ]
    provisionedIops: str
    replicaZones: typing.List[str]
    resourcePolicies: typing.List[str]
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    exemptedMembers: typing.List[str]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool
    logType: typing_extensions.Literal[
        "ADMIN_READ", "DATA_READ", "DATA_WRITE", "LOG_TYPE_UNSPECIFIED"
    ]

@typing.type_check_only
class AuthenticationPolicy(typing_extensions.TypedDict, total=False):
    origins: typing.List[OriginAuthenticationMethod]
    peers: typing.List[PeerAuthenticationMethod]
    principalBinding: typing_extensions.Literal["INVALID", "USE_ORIGIN", "USE_PEER"]
    serverTlsContext: TlsContext

@typing.type_check_only
class AuthorizationConfig(typing_extensions.TypedDict, total=False):
    policies: typing.List[RbacPolicy]

@typing.type_check_only
class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: typing_extensions.Literal[
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
        "PERMISSION_TYPE_UNSPECIFIED",
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
    scalingScheduleStatus: typing.Dict[str, typing.Any]
    selfLink: str
    selfLinkWithId: str
    status: typing_extensions.Literal["ACTIVE", "DELETING", "ERROR", "PENDING"]
    statusDetails: typing.List[AutoscalerStatusDetails]
    target: str
    zone: str

@typing.type_check_only
class AutoscalerAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AutoscalerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
        "UNKNOWN",
        "UNSUPPORTED_MAX_RATE_LOAD_BALANCING_CONFIGURATION",
        "ZONE_RESOURCE_STOCKOUT",
    ]

@typing.type_check_only
class AutoscalersScopedList(typing_extensions.TypedDict, total=False):
    autoscalers: typing.List[Autoscaler]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class AutoscalingPolicy(typing_extensions.TypedDict, total=False):
    coolDownPeriodSec: int
    cpuUtilization: AutoscalingPolicyCpuUtilization
    customMetricUtilizations: typing.List[AutoscalingPolicyCustomMetricUtilization]
    loadBalancingUtilization: AutoscalingPolicyLoadBalancingUtilization
    maxNumReplicas: int
    minNumReplicas: int
    mode: typing_extensions.Literal["OFF", "ON", "ONLY_SCALE_OUT", "ONLY_UP"]
    scaleDownControl: AutoscalingPolicyScaleDownControl
    scaleInControl: AutoscalingPolicyScaleInControl
    scalingSchedules: typing.Dict[str, typing.Any]

@typing.type_check_only
class AutoscalingPolicyCpuUtilization(typing_extensions.TypedDict, total=False):
    predictiveMethod: typing_extensions.Literal[
        "NONE", "OPTIMIZE_AVAILABILITY", "PREDICTIVE_METHOD_UNSPECIFIED", "STANDARD"
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
    balancingMode: typing_extensions.Literal["CONNECTION", "RATE", "UTILIZATION"]
    capacityScaler: float
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

@typing.type_check_only
class BackendBucket(typing_extensions.TypedDict, total=False):
    bucketName: str
    cdnPolicy: BackendBucketCdnPolicy
    creationTimestamp: str
    customResponseHeaders: typing.List[str]
    description: str
    edgeSecurityPolicy: str
    enableCdn: bool
    id: str
    kind: str
    name: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class BackendBucketCdnPolicy(typing_extensions.TypedDict, total=False):
    bypassCacheOnRequestHeaders: typing.List[
        BackendBucketCdnPolicyBypassCacheOnRequestHeader
    ]
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
    negativeCachingPolicy: typing.List[BackendBucketCdnPolicyNegativeCachingPolicy]
    requestCoalescing: bool
    serveWhileStale: int
    signedUrlCacheMaxAgeSec: str
    signedUrlKeyNames: typing.List[str]

@typing.type_check_only
class BackendBucketCdnPolicyBypassCacheOnRequestHeader(
    typing_extensions.TypedDict, total=False
):
    headerName: str

@typing.type_check_only
class BackendBucketCdnPolicyNegativeCachingPolicy(
    typing_extensions.TypedDict, total=False
):
    code: int
    ttl: int

@typing.type_check_only
class BackendBucketList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[BackendBucket]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class BackendService(typing_extensions.TypedDict, total=False):
    affinityCookieTtlSec: int
    backends: typing.List[Backend]
    cdnPolicy: BackendServiceCdnPolicy
    circuitBreakers: CircuitBreakers
    connectionDraining: ConnectionDraining
    connectionTrackingPolicy: BackendServiceConnectionTrackingPolicy
    consistentHash: ConsistentHashLoadBalancerSettings
    creationTimestamp: str
    customRequestHeaders: typing.List[str]
    customResponseHeaders: typing.List[str]
    description: str
    edgeSecurityPolicy: str
    enableCDN: bool
    failoverPolicy: BackendServiceFailoverPolicy
    fingerprint: str
    healthChecks: typing.List[str]
    iap: BackendServiceIAP
    id: str
    kind: str
    loadBalancingScheme: typing_extensions.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "INTERNAL",
        "INTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
        "INVALID_LOAD_BALANCING_SCHEME",
    ]
    localityLbPolicy: typing_extensions.Literal[
        "INVALID_LB_POLICY",
        "LEAST_REQUEST",
        "MAGLEV",
        "ORIGINAL_DESTINATION",
        "RANDOM",
        "RING_HASH",
        "ROUND_ROBIN",
    ]
    logConfig: BackendServiceLogConfig
    maxStreamDuration: Duration
    name: str
    network: str
    outlierDetection: OutlierDetection
    port: int
    portName: str
    protocol: typing_extensions.Literal[
        "ALL", "GRPC", "HTTP", "HTTP2", "HTTPS", "SSL", "TCP", "UDP"
    ]
    region: str
    securityPolicy: str
    securitySettings: SecuritySettings
    selfLink: str
    selfLinkWithId: str
    sessionAffinity: typing_extensions.Literal[
        "CLIENT_IP",
        "CLIENT_IP_NO_DESTINATION",
        "CLIENT_IP_PORT_PROTO",
        "CLIENT_IP_PROTO",
        "GENERATED_COOKIE",
        "HEADER_FIELD",
        "HTTP_COOKIE",
        "NONE",
    ]
    subsetting: Subsetting
    timeoutSec: int

@typing.type_check_only
class BackendServiceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class BackendServiceCdnPolicy(typing_extensions.TypedDict, total=False):
    bypassCacheOnRequestHeaders: typing.List[
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
    negativeCachingPolicy: typing.List[BackendServiceCdnPolicyNegativeCachingPolicy]
    requestCoalescing: bool
    serveWhileStale: int
    signedUrlCacheMaxAgeSec: str
    signedUrlKeyNames: typing.List[str]

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
    idleTimeoutSec: int
    trackingMode: typing_extensions.Literal[
        "INVALID_TRACKING_MODE", "PER_CONNECTION", "PER_SESSION"
    ]

@typing.type_check_only
class BackendServiceFailoverPolicy(typing_extensions.TypedDict, total=False):
    disableConnectionDrainOnFailover: bool
    dropTrafficIfUnhealthy: bool
    failoverRatio: float

@typing.type_check_only
class BackendServiceGroupHealth(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    healthStatus: typing.List[HealthStatus]
    kind: str

@typing.type_check_only
class BackendServiceIAP(typing_extensions.TypedDict, total=False):
    enabled: bool
    oauth2ClientId: str
    oauth2ClientInfo: BackendServiceIAPOAuth2ClientInfo
    oauth2ClientSecret: str
    oauth2ClientSecretSha256: str

@typing.type_check_only
class BackendServiceIAPOAuth2ClientInfo(typing_extensions.TypedDict, total=False):
    applicationName: str
    clientName: str
    developerEmailAddress: str

@typing.type_check_only
class BackendServiceList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[BackendService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class BackendServiceLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    sampleRate: float

@typing.type_check_only
class BackendServiceReference(typing_extensions.TypedDict, total=False):
    backendService: str

@typing.type_check_only
class BackendServicesScopedList(typing_extensions.TypedDict, total=False):
    backendServices: typing.List[BackendService]
    warning: typing.Dict[str, typing.Any]

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
    controlPacketIntervals: typing.List[PacketIntervals]
    echoPacketCounts: BfdStatusPacketCounts
    echoPacketIntervals: typing.List[PacketIntervals]
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
    negotiatedLocalEchoTxIntervalMs: int
    rxPacket: BfdPacket
    txPacket: BfdPacket
    uptimeMs: str
    usingEchoMode: bool

@typing.type_check_only
class BfdStatusPacketCounts(typing_extensions.TypedDict, total=False):
    numRx: int
    numRxRejected: int
    numRxSuccessful: int
    numTx: int

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class BulkInsertInstanceResource(typing_extensions.TypedDict, total=False):
    count: str
    instance: Instance
    instanceProperties: InstanceProperties
    locationPolicy: LocationPolicy
    minCount: str
    namePattern: str
    perInstanceProperties: typing.Dict[str, typing.Any]
    predefinedNames: typing.List[str]
    sourceInstanceTemplate: str

@typing.type_check_only
class BulkInsertInstanceResourcePerInstanceProperties(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class CacheInvalidationRule(typing_extensions.TypedDict, total=False):
    host: str
    path: str

@typing.type_check_only
class CacheKeyPolicy(typing_extensions.TypedDict, total=False):
    includeHost: bool
    includeProtocol: bool
    includeQueryString: bool
    queryStringBlacklist: typing.List[str]
    queryStringWhitelist: typing.List[str]

@typing.type_check_only
class CallCredentials(typing_extensions.TypedDict, total=False):
    callCredentialType: typing_extensions.Literal["FROM_PLUGIN", "GCE_VM", "INVALID"]
    fromPlugin: MetadataCredentialsFromPlugin

@typing.type_check_only
class ChannelCredentials(typing_extensions.TypedDict, total=False):
    certificates: TlsCertificatePaths
    channelCredentialType: typing_extensions.Literal[
        "CERTIFICATES", "GCE_VM", "INVALID"
    ]

@typing.type_check_only
class CircuitBreakers(typing_extensions.TypedDict, total=False):
    connectTimeout: Duration
    maxConnections: int
    maxPendingRequests: int
    maxRequests: int
    maxRequestsPerConnection: int
    maxRetries: int

@typing.type_check_only
class ClientTlsSettings(typing_extensions.TypedDict, total=False):
    clientTlsContext: TlsContext
    mode: typing_extensions.Literal["DISABLE", "INVALID", "MUTUAL", "SIMPLE"]
    sni: str
    subjectAltNames: typing.List[str]

@typing.type_check_only
class Commitment(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal["CATEGORY_UNSPECIFIED", "LICENSE", "MACHINE"]
    creationTimestamp: str
    description: str
    endTimestamp: str
    id: str
    kind: str
    licenseResource: LicenseResourceCommitment
    name: str
    plan: typing_extensions.Literal["INVALID", "THIRTY_SIX_MONTH", "TWELVE_MONTH"]
    region: str
    reservations: typing.List[Reservation]
    resources: typing.List[ResourceCommitment]
    selfLink: str
    selfLinkWithId: str
    startTimestamp: str
    status: typing_extensions.Literal["ACTIVE", "CREATING", "EXPIRED", "NOT_YET_ACTIVE"]
    statusMessage: str
    type: typing_extensions.Literal[
        "ACCELERATOR_OPTIMIZED",
        "COMPUTE_OPTIMIZED",
        "COMPUTE_OPTIMIZED_C2D",
        "GENERAL_PURPOSE",
        "GENERAL_PURPOSE_E2",
        "GENERAL_PURPOSE_N2",
        "GENERAL_PURPOSE_N2D",
        "MEMORY_OPTIMIZED",
        "TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class CommitmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class CommitmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Commitment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class CommitmentsScopedList(typing_extensions.TypedDict, total=False):
    commitments: typing.List[Commitment]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    iam: typing_extensions.Literal[
        "APPROVER",
        "ATTRIBUTION",
        "AUTHORITY",
        "CREDENTIALS_TYPE",
        "CREDS_ASSERTION",
        "JUSTIFICATION_TYPE",
        "NO_ATTR",
        "SECURITY_REALM",
    ]
    op: typing_extensions.Literal[
        "DISCHARGED", "EQUALS", "IN", "NOT_EQUALS", "NOT_IN", "NO_OP"
    ]
    svc: str
    sys: typing_extensions.Literal["IP", "NAME", "NO_ATTR", "REGION", "SERVICE"]
    values: typing.List[str]

@typing.type_check_only
class ConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
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
    allowHeaders: typing.List[str]
    allowMethods: typing.List[str]
    allowOriginRegexes: typing.List[str]
    allowOrigins: typing.List[str]
    disabled: bool
    exposeHeaders: typing.List[str]
    maxAge: int

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
    creationTimestamp: str
    description: str
    diskEncryptionKey: CustomerEncryptionKey
    eraseWindowsVssSignature: bool
    guestOsFeatures: typing.List[GuestOsFeature]
    id: str
    interface: typing_extensions.Literal["NVME", "SCSI", "UNSPECIFIED"]
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    lastAttachTimestamp: str
    lastDetachTimestamp: str
    licenseCodes: typing.List[str]
    licenses: typing.List[str]
    locationHint: str
    multiWriter: bool
    name: str
    options: str
    physicalBlockSizeBytes: str
    provisionedIops: str
    region: str
    replicaZones: typing.List[str]
    resourcePolicies: typing.List[str]
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    sizeGb: str
    sourceDisk: str
    sourceDiskId: str
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceImageId: str
    sourceInPlaceSnapshot: str
    sourceInPlaceSnapshotId: str
    sourceInstantSnapshot: str
    sourceInstantSnapshotId: str
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey
    sourceSnapshotId: str
    sourceStorageObject: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RESTORING"
    ]
    storageType: typing_extensions.Literal["HDD", "SSD"]
    type: str
    userLicenses: typing.List[str]
    users: typing.List[str]
    zone: str

@typing.type_check_only
class DiskAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

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
    items: typing.List[Disk]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class DiskMoveRequest(typing_extensions.TypedDict, total=False):
    destinationZone: str
    targetDisk: str

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
    selfLinkWithId: str
    validDiskSize: str
    zone: str

@typing.type_check_only
class DiskTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class DiskTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class DiskTypesScopedList(typing_extensions.TypedDict, total=False):
    diskTypes: typing.List[DiskType]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class DisksAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

@typing.type_check_only
class DisksRemoveResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

@typing.type_check_only
class DisksResizeRequest(typing_extensions.TypedDict, total=False):
    sizeGb: str

@typing.type_check_only
class DisksScopedList(typing_extensions.TypedDict, total=False):
    disks: typing.List[Disk]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class DisplayDevice(typing_extensions.TypedDict, total=False):
    enableDisplay: bool

@typing.type_check_only
class DistributionPolicy(typing_extensions.TypedDict, total=False):
    targetShape: typing_extensions.Literal["ANY", "BALANCED", "EVEN"]
    zones: typing.List[DistributionPolicyZoneConfiguration]

@typing.type_check_only
class DistributionPolicyZoneConfiguration(typing_extensions.TypedDict, total=False):
    zone: str

@typing.type_check_only
class Duration(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

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
    items: typing.List[ExchangedPeeringRoute]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    interfaces: typing.List[ExternalVpnGatewayInterface]
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    redundancyType: typing_extensions.Literal[
        "FOUR_IPS_REDUNDANCY", "SINGLE_IP_INTERNALLY_REDUNDANT", "TWO_IPS_REDUNDANCY"
    ]
    selfLink: str

@typing.type_check_only
class ExternalVpnGatewayInterface(typing_extensions.TypedDict, total=False):
    id: int
    ipAddress: str

@typing.type_check_only
class ExternalVpnGatewayList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: typing.List[ExternalVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class FileContentBuffer(typing_extensions.TypedDict, total=False):
    content: str
    fileType: typing_extensions.Literal["BIN", "UNDEFINED", "X509"]

@typing.type_check_only
class Firewall(typing_extensions.TypedDict, total=False):
    allowed: typing.List[typing.Dict[str, typing.Any]]
    creationTimestamp: str
    denied: typing.List[typing.Dict[str, typing.Any]]
    description: str
    destinationRanges: typing.List[str]
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
    selfLinkWithId: str
    sourceRanges: typing.List[str]
    sourceServiceAccounts: typing.List[str]
    sourceTags: typing.List[str]
    targetServiceAccounts: typing.List[str]
    targetTags: typing.List[str]

@typing.type_check_only
class FirewallList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Firewall]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class FirewallLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    metadata: typing_extensions.Literal["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]

@typing.type_check_only
class FirewallPoliciesListAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    associations: typing.List[FirewallPolicyAssociation]
    kind: str

@typing.type_check_only
class FirewallPolicy(typing_extensions.TypedDict, total=False):
    associations: typing.List[FirewallPolicyAssociation]
    creationTimestamp: str
    description: str
    displayName: str
    fingerprint: str
    id: str
    kind: str
    name: str
    parent: str
    ruleTupleCount: int
    rules: typing.List[FirewallPolicyRule]
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class FirewallPolicyAssociation(typing_extensions.TypedDict, total=False):
    attachmentTarget: str
    displayName: str
    firewallPolicyId: str
    name: str

@typing.type_check_only
class FirewallPolicyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[FirewallPolicy]
    kind: str
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

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
    ruleTupleCount: int
    targetResources: typing.List[str]
    targetSecureLabels: typing.List[str]
    targetSecureTags: typing.List[FirewallPolicyRuleSecureTag]
    targetServiceAccounts: typing.List[str]

@typing.type_check_only
class FirewallPolicyRuleMatcher(typing_extensions.TypedDict, total=False):
    destIpRanges: typing.List[str]
    layer4Configs: typing.List[FirewallPolicyRuleMatcherLayer4Config]
    srcIpRanges: typing.List[str]
    srcSecureLabels: typing.List[str]
    srcSecureTags: typing.List[FirewallPolicyRuleSecureTag]

@typing.type_check_only
class FirewallPolicyRuleMatcherLayer4Config(typing_extensions.TypedDict, total=False):
    ipProtocol: str
    ports: typing.List[str]

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
        "AH", "ALL", "ESP", "ICMP", "SCTP", "TCP", "UDP"
    ]
    allPorts: bool
    allowGlobalAccess: bool
    backendService: str
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    ipVersion: typing_extensions.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    isMirroringCollector: bool
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    loadBalancingScheme: typing_extensions.Literal[
        "EXTERNAL",
        "EXTERNAL_MANAGED",
        "INTERNAL",
        "INTERNAL_MANAGED",
        "INTERNAL_SELF_MANAGED",
        "INVALID",
    ]
    metadataFilters: typing.List[MetadataFilter]
    name: str
    network: str
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    portRange: str
    ports: typing.List[str]
    pscConnectionId: str
    region: str
    selfLink: str
    selfLinkWithId: str
    serviceDirectoryRegistrations: typing.List[
        ForwardingRuleServiceDirectoryRegistration
    ]
    serviceLabel: str
    serviceName: str
    subnetwork: str
    target: str

@typing.type_check_only
class ForwardingRuleAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ForwardingRuleList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[ForwardingRule]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    forwardingRules: typing.List[ForwardingRule]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class GRPCHealthCheck(typing_extensions.TypedDict, total=False):
    grpcServiceName: str
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]

@typing.type_check_only
class GetOwnerInstanceResponse(typing_extensions.TypedDict, total=False):
    instance: str

@typing.type_check_only
class GlobalNetworkEndpointGroupsAttachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

@typing.type_check_only
class GlobalNetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

@typing.type_check_only
class GlobalOrganizationSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class GlobalSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class GrpcServiceConfig(typing_extensions.TypedDict, total=False):
    callCredentials: CallCredentials
    channelCredentials: ChannelCredentials
    targetUri: str

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
    items: typing.List[GuestAttributesEntry]

@typing.type_check_only
class GuestOsFeature(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "BARE_METAL_LINUX_COMPATIBLE",
        "FEATURE_TYPE_UNSPECIFIED",
        "GVNIC",
        "MULTI_IP_SUBNET",
        "SECURE_BOOT",
        "SEV_CAPABLE",
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
    selfLinkWithId: str
    sslHealthCheck: SSLHealthCheck
    tcpHealthCheck: TCPHealthCheck
    timeoutSec: int
    type: typing_extensions.Literal[
        "GRPC", "HTTP", "HTTP2", "HTTPS", "INVALID", "SSL", "TCP", "UDP"
    ]
    udpHealthCheck: UDPHealthCheck
    unhealthyThreshold: int

@typing.type_check_only
class HealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    healthChecks: typing.List[str]
    healthStatusAggregationPolicy: typing_extensions.Literal["AND", "NO_AGGREGATION"]
    healthStatusAggregationStrategy: typing_extensions.Literal["AND", "NO_AGGREGATION"]
    id: str
    kind: str
    name: str
    networkEndpointGroups: typing.List[str]
    notificationEndpoints: typing.List[str]
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class HealthCheckServiceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class HealthCheckServiceReference(typing_extensions.TypedDict, total=False):
    healthCheckService: str

@typing.type_check_only
class HealthCheckServicesList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HealthCheckService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class HealthCheckServicesScopedList(typing_extensions.TypedDict, total=False):
    resources: typing.List[HealthCheckService]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class HealthChecksAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class HealthChecksScopedList(typing_extensions.TypedDict, total=False):
    healthChecks: typing.List[HealthCheck]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class HealthStatus(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    healthState: typing_extensions.Literal["HEALTHY", "UNHEALTHY"]
    instance: str
    ipAddress: str
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

@typing.type_check_only
class HostRule(typing_extensions.TypedDict, total=False):
    description: str
    hosts: typing.List[str]
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
    requestHeadersToAdd: typing.List[HttpHeaderOption]
    requestHeadersToRemove: typing.List[str]
    responseHeadersToAdd: typing.List[HttpHeaderOption]
    responseHeadersToRemove: typing.List[str]

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
    selfLinkWithId: str
    timeoutSec: int
    unhealthyThreshold: int

@typing.type_check_only
class HttpHealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HttpHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    retryConditions: typing.List[str]

@typing.type_check_only
class HttpRouteAction(typing_extensions.TypedDict, total=False):
    corsPolicy: CorsPolicy
    faultInjectionPolicy: HttpFaultInjection
    maxStreamDuration: Duration
    requestMirrorPolicy: RequestMirrorPolicy
    retryPolicy: HttpRetryPolicy
    timeout: Duration
    urlRewrite: UrlRewrite
    weightedBackendServices: typing.List[WeightedBackendService]

@typing.type_check_only
class HttpRouteRule(typing_extensions.TypedDict, total=False):
    description: str
    headerAction: HttpHeaderAction
    httpFilterConfigs: typing.List[HttpFilterConfig]
    httpFilterMetadata: typing.List[HttpFilterConfig]
    matchRules: typing.List[HttpRouteRuleMatch]
    priority: int
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

@typing.type_check_only
class HttpRouteRuleMatch(typing_extensions.TypedDict, total=False):
    fullPathMatch: str
    headerMatches: typing.List[HttpHeaderMatch]
    ignoreCase: bool
    metadataFilters: typing.List[MetadataFilter]
    prefixMatch: str
    queryParameterMatches: typing.List[HttpQueryParameterMatch]
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
    selfLinkWithId: str
    timeoutSec: int
    unhealthyThreshold: int

@typing.type_check_only
class HttpsHealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HttpsHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    archiveSizeBytes: str
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    diskSizeGb: str
    family: str
    guestOsFeatures: typing.List[GuestOsFeature]
    id: str
    imageEncryptionKey: CustomerEncryptionKey
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    licenseCodes: typing.List[str]
    licenses: typing.List[str]
    name: str
    rawDisk: typing.Dict[str, typing.Any]
    rolloutOverride: RolloutPolicy
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
    sourceType: typing_extensions.Literal["RAW"]
    status: typing_extensions.Literal["DELETING", "FAILED", "PENDING", "READY"]
    storageLocations: typing.List[str]

@typing.type_check_only
class ImageFamilyView(typing_extensions.TypedDict, total=False):
    image: Image

@typing.type_check_only
class ImageList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Image]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InPlaceSnapshot(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    diskSizeGb: str
    guestFlush: bool
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    region: str
    selfLink: str
    selfLinkWithId: str
    sourceDisk: str
    sourceDiskId: str
    status: typing_extensions.Literal["CREATING", "DELETING", "FAILED", "READY"]
    zone: str

@typing.type_check_only
class InPlaceSnapshotList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InPlaceSnapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InitialStateConfig(typing_extensions.TypedDict, total=False):
    dbs: typing.List[FileContentBuffer]
    dbxs: typing.List[FileContentBuffer]
    keks: typing.List[FileContentBuffer]
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
    disks: typing.List[AttachedDisk]
    displayDevice: DisplayDevice
    eraseWindowsVssSignature: bool
    fingerprint: str
    guestAccelerators: typing.List[AcceleratorConfig]
    hostname: str
    id: str
    instanceEncryptionKey: CustomerEncryptionKey
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    lastStartTimestamp: str
    lastStopTimestamp: str
    lastSuspendedTimestamp: str
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    name: str
    networkInterfaces: typing.List[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    postKeyRevocationActionType: typing_extensions.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    preservedStateSizeGb: str
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "INHERIT_FROM_SUBNETWORK",
    ]
    reservationAffinity: ReservationAffinity
    resourcePolicies: typing.List[str]
    resourceStatus: ResourceStatus
    satisfiesPzs: bool
    scheduling: Scheduling
    secureLabels: typing.List[str]
    secureTags: typing.List[str]
    selfLink: str
    selfLinkWithId: str
    serviceAccounts: typing.List[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedInstanceIntegrityPolicy: ShieldedInstanceIntegrityPolicy
    shieldedVmConfig: ShieldedVmConfig
    shieldedVmIntegrityPolicy: ShieldedVmIntegrityPolicy
    sourceMachineImage: str
    sourceMachineImageEncryptionKey: CustomerEncryptionKey
    startRestricted: bool
    status: typing_extensions.Literal[
        "DEPROVISIONING",
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
    zone: str

@typing.type_check_only
class InstanceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroup(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    namedPorts: typing.List[NamedPort]
    network: str
    region: str
    selfLink: str
    selfLinkWithId: str
    size: int
    subnetwork: str
    zone: str

@typing.type_check_only
class InstanceGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManager(typing_extensions.TypedDict, total=False):
    autoHealingPolicies: typing.List[InstanceGroupManagerAutoHealingPolicy]
    baseInstanceName: str
    creationTimestamp: str
    currentActions: InstanceGroupManagerActionsSummary
    description: str
    distributionPolicy: DistributionPolicy
    failoverAction: typing_extensions.Literal["NO_FAILOVER", "UNKNOWN"]
    fingerprint: str
    id: str
    instanceGroup: str
    instanceTemplate: str
    kind: str
    name: str
    namedPorts: typing.List[NamedPort]
    region: str
    selfLink: str
    selfLinkWithId: str
    serviceAccount: str
    statefulPolicy: StatefulPolicy
    status: InstanceGroupManagerStatus
    targetPools: typing.List[str]
    targetSize: int
    updatePolicy: InstanceGroupManagerUpdatePolicy
    versions: typing.List[InstanceGroupManagerVersion]
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
    verifying: int

@typing.type_check_only
class InstanceGroupManagerAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerAutoHealingPolicy(typing_extensions.TypedDict, total=False):
    healthCheck: str
    initialDelaySec: int
    maxUnavailable: FixedOrPercent

@typing.type_check_only
class InstanceGroupManagerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagerStatus(typing_extensions.TypedDict, total=False):
    autoscaler: str
    isStable: bool
    stateful: InstanceGroupManagerStatusStateful
    versionTarget: InstanceGroupManagerStatusVersionTarget

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
    tag: str
    targetSize: FixedOrPercent

@typing.type_check_only
class InstanceGroupManagersAbandonInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

@typing.type_check_only
class InstanceGroupManagersApplyUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    allInstances: bool
    instances: typing.List[str]
    maximalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]

@typing.type_check_only
class InstanceGroupManagersCreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupManagersDeleteInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

@typing.type_check_only
class InstanceGroupManagersDeletePerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

@typing.type_check_only
class InstanceGroupManagersListErrorsResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[InstanceManagedByIgmError]
    nextPageToken: str

@typing.type_check_only
class InstanceGroupManagersListManagedInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    managedInstances: typing.List[ManagedInstance]
    nextPageToken: str

@typing.type_check_only
class InstanceGroupManagersListPerInstanceConfigsResp(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[PerInstanceConfig]
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersPatchPerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupManagersRecreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

@typing.type_check_only
class InstanceGroupManagersResizeAdvancedRequest(
    typing_extensions.TypedDict, total=False
):
    noCreationRetries: bool
    targetSize: int

@typing.type_check_only
class InstanceGroupManagersScopedList(typing_extensions.TypedDict, total=False):
    instanceGroupManagers: typing.List[InstanceGroupManager]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupManagersSetAutoHealingRequest(
    typing_extensions.TypedDict, total=False
):
    autoHealingPolicies: typing.List[InstanceGroupManagerAutoHealingPolicy]

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
    targetPools: typing.List[str]

@typing.type_check_only
class InstanceGroupManagersUpdatePerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

@typing.type_check_only
class InstanceGroupsAddInstancesRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

@typing.type_check_only
class InstanceGroupsListInstances(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupsListInstancesRequest(typing_extensions.TypedDict, total=False):
    instanceState: typing_extensions.Literal["ALL", "RUNNING"]

@typing.type_check_only
class InstanceGroupsRemoveInstancesRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

@typing.type_check_only
class InstanceGroupsScopedList(typing_extensions.TypedDict, total=False):
    instanceGroups: typing.List[InstanceGroup]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceGroupsSetNamedPortsRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str
    namedPorts: typing.List[NamedPort]

@typing.type_check_only
class InstanceList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Instance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceListReferrers(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Reference]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
class InstanceProperties(typing_extensions.TypedDict, total=False):
    advancedMachineFeatures: AdvancedMachineFeatures
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    description: str
    disks: typing.List[AttachedDisk]
    displayDevice: DisplayDevice
    guestAccelerators: typing.List[AcceleratorConfig]
    labels: typing.Dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: typing.List[NetworkInterface]
    networkPerformanceConfig: NetworkPerformanceConfig
    postKeyRevocationActionType: typing_extensions.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "INHERIT_FROM_SUBNETWORK",
    ]
    reservationAffinity: ReservationAffinity
    resourcePolicies: typing.List[str]
    scheduling: Scheduling
    serviceAccounts: typing.List[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedVmConfig: ShieldedVmConfig
    tags: Tags

@typing.type_check_only
class InstanceReference(typing_extensions.TypedDict, total=False):
    instance: str

@typing.type_check_only
class InstanceTemplate(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    properties: InstanceProperties
    selfLink: str
    selfLinkWithId: str
    sourceInstance: str
    sourceInstanceParams: SourceInstanceParams

@typing.type_check_only
class InstanceTemplateList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstanceWithNamedPorts(typing_extensions.TypedDict, total=False):
    instance: str
    namedPorts: typing.List[NamedPort]
    status: typing_extensions.Literal[
        "DEPROVISIONING",
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
    resourcePolicies: typing.List[str]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponse(typing_extensions.TypedDict, total=False):
    firewallPolicys: typing.List[
        InstancesGetEffectiveFirewallsResponseEffectiveFirewallPolicy
    ]
    firewalls: typing.List[Firewall]
    organizationFirewalls: typing.List[
        InstancesGetEffectiveFirewallsResponseOrganizationFirewallPolicy
    ]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    rules: typing.List[FirewallPolicyRule]
    type: typing_extensions.Literal["HIERARCHY", "NETWORK", "UNSPECIFIED"]

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseOrganizationFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    id: str
    rules: typing.List[SecurityPolicyRule]

@typing.type_check_only
class InstancesRemoveResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

@typing.type_check_only
class InstancesResumeRequest(typing_extensions.TypedDict, total=False):
    disks: typing.List[CustomerEncryptionKeyProtectedDisk]
    instanceEncryptionKey: CustomerEncryptionKey

@typing.type_check_only
class InstancesScopedList(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstancesSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class InstancesSetMachineResourcesRequest(typing_extensions.TypedDict, total=False):
    guestAccelerators: typing.List[AcceleratorConfig]

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
class InstancesSetServiceAccountRequest(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

@typing.type_check_only
class InstancesStartWithEncryptionKeyRequest(typing_extensions.TypedDict, total=False):
    disks: typing.List[CustomerEncryptionKeyProtectedDisk]
    instanceEncryptionKey: CustomerEncryptionKey

@typing.type_check_only
class InstantSnapshot(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    diskSizeGb: str
    guestFlush: bool
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    region: str
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    sourceDisk: str
    sourceDiskId: str
    status: typing_extensions.Literal["CREATING", "DELETING", "FAILED", "READY"]
    zone: str

@typing.type_check_only
class InstantSnapshotExportParams(typing_extensions.TypedDict, total=False):
    baseInstantSnapshot: str
    bucketName: str
    encryptionKey: CustomerEncryptionKey
    objectName: str
    outputType: typing_extensions.Literal[
        "INVALID", "METADATA_AND_DATA", "METADATA_ONLY"
    ]

@typing.type_check_only
class InstantSnapshotList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstantSnapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Int64RangeMatch(typing_extensions.TypedDict, total=False):
    rangeEnd: str
    rangeStart: str

@typing.type_check_only
class Interconnect(typing_extensions.TypedDict, total=False):
    adminEnabled: bool
    circuitInfos: typing.List[InterconnectCircuitInfo]
    creationTimestamp: str
    customerName: str
    description: str
    expectedOutages: typing.List[InterconnectOutageNotification]
    googleIpAddress: str
    googleReferenceId: str
    id: str
    interconnectAttachments: typing.List[str]
    interconnectType: typing_extensions.Literal["DEDICATED", "IT_PRIVATE", "PARTNER"]
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    linkType: typing_extensions.Literal[
        "LINK_TYPE_ETHERNET_100G_LR", "LINK_TYPE_ETHERNET_10G_LR"
    ]
    location: str
    name: str
    nocContactEmail: str
    operationalStatus: typing_extensions.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    peerIpAddress: str
    provisionedLinkCount: int
    requestedLinkCount: int
    selfLink: str
    selfLinkWithId: str
    state: typing_extensions.Literal["ACTIVE", "UNPROVISIONED"]

@typing.type_check_only
class InterconnectAttachment(typing_extensions.TypedDict, total=False):
    adminEnabled: bool
    bandwidth: typing_extensions.Literal[
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
    candidateSubnets: typing.List[str]
    cloudRouterIpAddress: str
    creationTimestamp: str
    customerRouterIpAddress: str
    dataplaneVersion: int
    description: str
    edgeAvailabilityDomain: typing_extensions.Literal[
        "AVAILABILITY_DOMAIN_1", "AVAILABILITY_DOMAIN_2", "AVAILABILITY_DOMAIN_ANY"
    ]
    encryption: typing_extensions.Literal["IPSEC", "NONE"]
    googleReferenceId: str
    id: str
    interconnect: str
    ipsecInternalAddresses: typing.List[str]
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    mtu: int
    name: str
    operationalStatus: typing_extensions.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    pairingKey: str
    partnerAsn: str
    partnerMetadata: InterconnectAttachmentPartnerMetadata
    privateInterconnectInfo: InterconnectAttachmentPrivateInfo
    region: str
    router: str
    selfLink: str
    selfLinkWithId: str
    state: typing_extensions.Literal[
        "ACTIVE",
        "DEFUNCT",
        "PARTNER_REQUEST_RECEIVED",
        "PENDING_CUSTOMER",
        "PENDING_PARTNER",
        "STATE_UNSPECIFIED",
        "UNPROVISIONED",
    ]
    type: typing_extensions.Literal["DEDICATED", "PARTNER", "PARTNER_PROVIDER"]
    vlanTag8021q: int

@typing.type_check_only
class InterconnectAttachmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InterconnectAttachmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InterconnectAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    interconnectAttachments: typing.List[InterconnectAttachment]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InterconnectCircuitInfo(typing_extensions.TypedDict, total=False):
    customerDemarcId: str
    googleCircuitId: str
    googleDemarcId: str

@typing.type_check_only
class InterconnectDiagnostics(typing_extensions.TypedDict, total=False):
    arpCaches: typing.List[InterconnectDiagnosticsARPEntry]
    links: typing.List[InterconnectDiagnosticsLinkStatus]
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
    arpCaches: typing.List[InterconnectDiagnosticsARPEntry]
    circuitId: str
    googleDemarc: str
    lacpStatus: InterconnectDiagnosticsLinkLACPStatus
    receivingOpticalPower: InterconnectDiagnosticsLinkOpticalPower
    transmittingOpticalPower: InterconnectDiagnosticsLinkOpticalPower

@typing.type_check_only
class InterconnectList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Interconnect]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InterconnectLocation(typing_extensions.TypedDict, total=False):
    address: str
    availabilityZone: str
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
    regionInfos: typing.List[InterconnectLocationRegionInfo]
    selfLink: str
    selfLinkWithId: str
    status: typing_extensions.Literal["AVAILABLE", "CLOSED"]

@typing.type_check_only
class InterconnectLocationList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InterconnectLocation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class InterconnectLocationRegionInfo(typing_extensions.TypedDict, total=False):
    expectedRttMs: str
    locationPresence: typing_extensions.Literal[
        "GLOBAL", "LOCAL_REGION", "LP_GLOBAL", "LP_LOCAL_REGION"
    ]
    region: str

@typing.type_check_only
class InterconnectOutageNotification(typing_extensions.TypedDict, total=False):
    affectedCircuits: typing.List[str]
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
class InterconnectsGetDiagnosticsResponse(typing_extensions.TypedDict, total=False):
    result: InterconnectDiagnostics

@typing.type_check_only
class InternalIpAddress(typing_extensions.TypedDict, total=False):
    cidr: str
    owner: str
    purpose: str
    region: str
    type: typing_extensions.Literal[
        "PEER_RESERVED",
        "PEER_USED",
        "REMOTE_RESERVED",
        "REMOTE_USED",
        "RESERVED",
        "SUBNETWORK",
        "TYPE_UNSPECIFIED",
    ]

@typing.type_check_only
class InternalIpOwner(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    owners: typing.List[str]
    systemOwned: bool

@typing.type_check_only
class IpAddressesList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InternalIpAddress]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class IpOwnerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InternalIpOwner]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Jwt(typing_extensions.TypedDict, total=False):
    audiences: typing.List[str]
    issuer: str
    jwksPublicKeys: str
    jwtHeaders: typing.List[JwtHeader]
    jwtParams: typing.List[str]

@typing.type_check_only
class JwtHeader(typing_extensions.TypedDict, total=False):
    name: str
    valuePrefix: str

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
    selfLinkWithId: str
    transferable: bool

@typing.type_check_only
class LicenseCode(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    licenseAlias: typing.List[LicenseCodeLicenseAlias]
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
    items: typing.List[License]
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class LocalDisk(typing_extensions.TypedDict, total=False):
    diskCount: int
    diskSizeGb: int
    diskType: str

@typing.type_check_only
class LocationPolicy(typing_extensions.TypedDict, total=False):
    locations: typing.Dict[str, typing.Any]

@typing.type_check_only
class LocationPolicyLocation(typing_extensions.TypedDict, total=False):
    preference: typing_extensions.Literal["ALLOW", "DENY", "PREFERENCE_UNSPECIFIED"]

@typing.type_check_only
class LogConfig(typing_extensions.TypedDict, total=False):
    cloudAudit: LogConfigCloudAuditOptions
    counter: LogConfigCounterOptions
    dataAccess: LogConfigDataAccessOptions

@typing.type_check_only
class LogConfigCloudAuditOptions(typing_extensions.TypedDict, total=False):
    authorizationLoggingOptions: AuthorizationLoggingOptions
    logName: typing_extensions.Literal[
        "ADMIN_ACTIVITY", "DATA_ACCESS", "UNSPECIFIED_LOG_NAME"
    ]

@typing.type_check_only
class LogConfigCounterOptions(typing_extensions.TypedDict, total=False):
    customFields: typing.List[LogConfigCounterOptionsCustomField]
    field: str
    metric: str

@typing.type_check_only
class LogConfigCounterOptionsCustomField(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class LogConfigDataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: typing_extensions.Literal["LOG_FAIL_CLOSED", "LOG_MODE_UNSPECIFIED"]

@typing.type_check_only
class MachineImage(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    guestFlush: bool
    id: str
    kind: str
    machineImageEncryptionKey: CustomerEncryptionKey
    name: str
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    sourceDiskEncryptionKeys: typing.List[SourceDiskEncryptionKey]
    sourceInstance: str
    sourceInstanceProperties: SourceInstanceProperties
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "UPLOADING"
    ]
    storageLocations: typing.List[str]
    totalStorageBytes: str

@typing.type_check_only
class MachineImageList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[MachineImage]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class MachineType(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[typing.Dict[str, typing.Any]]
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
class MachineTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class MachineTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[MachineType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class MachineTypesScopedList(typing_extensions.TypedDict, total=False):
    machineTypes: typing.List[MachineType]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ManagedInstance(typing_extensions.TypedDict, total=False):
    currentAction: typing_extensions.Literal[
        "ABANDONING",
        "CREATING",
        "CREATING_WITHOUT_RETRIES",
        "DELETING",
        "NONE",
        "RECREATING",
        "REFRESHING",
        "RESTARTING",
        "VERIFYING",
    ]
    id: str
    instance: str
    instanceHealth: typing.List[ManagedInstanceInstanceHealth]
    instanceStatus: typing_extensions.Literal[
        "DEPROVISIONING",
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
    preservedStateFromConfig: PreservedState
    preservedStateFromPolicy: PreservedState
    tag: str
    version: ManagedInstanceVersion

@typing.type_check_only
class ManagedInstanceInstanceHealth(typing_extensions.TypedDict, total=False):
    detailedHealthState: typing_extensions.Literal[
        "DRAINING", "HEALTHY", "TIMEOUT", "UNHEALTHY", "UNKNOWN"
    ]
    healthCheck: str
    healthState: typing_extensions.Literal["HEALTHY", "UNHEALTHY"]

@typing.type_check_only
class ManagedInstanceLastAttempt(typing_extensions.TypedDict, total=False):
    errors: typing.Dict[str, typing.Any]

@typing.type_check_only
class ManagedInstanceVersion(typing_extensions.TypedDict, total=False):
    instanceTemplate: str
    name: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    fingerprint: str
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

@typing.type_check_only
class MetadataCredentialsFromPlugin(typing_extensions.TypedDict, total=False):
    name: str
    structConfig: str

@typing.type_check_only
class MetadataFilter(typing_extensions.TypedDict, total=False):
    filterLabels: typing.List[MetadataFilterLabelMatch]
    filterMatchCriteria: typing_extensions.Literal["MATCH_ALL", "MATCH_ANY", "NOT_SET"]

@typing.type_check_only
class MetadataFilterLabelMatch(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class MutualTls(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["INVALID", "PERMISSIVE", "STRICT"]

@typing.type_check_only
class NamedPort(typing_extensions.TypedDict, total=False):
    name: str
    port: int

@typing.type_check_only
class Network(typing_extensions.TypedDict, total=False):
    IPv4Range: str
    autoCreateSubnetworks: bool
    creationTimestamp: str
    description: str
    firewallPolicy: str
    gatewayIPv4: str
    id: str
    kind: str
    mtu: int
    name: str
    peerings: typing.List[NetworkPeering]
    routingConfig: NetworkRoutingConfig
    selfLink: str
    selfLinkWithId: str
    subnetworks: typing.List[str]

@typing.type_check_only
class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    fqdn: str
    instance: str
    ipAddress: str
    port: int

@typing.type_check_only
class NetworkEndpointGroup(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
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
        "GCE_VM_PRIMARY_IP",
        "INTERNET_FQDN_PORT",
        "INTERNET_IP_PORT",
        "NON_GCP_PRIVATE_IP_PORT",
        "SERVERLESS",
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    serverlessDeployment: NetworkEndpointGroupServerlessDeployment
    size: int
    subnetwork: str
    type: typing_extensions.Literal["LOAD_BALANCING"]
    zone: str

@typing.type_check_only
class NetworkEndpointGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

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
    items: typing.List[NetworkEndpointGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    networkEndpoints: typing.List[NetworkEndpoint]

@typing.type_check_only
class NetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

@typing.type_check_only
class NetworkEndpointGroupsListEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    endpointFilters: typing.List[
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
    items: typing.List[NetworkEndpointWithHealthStatus]
    kind: str
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointGroupsScopedList(typing_extensions.TypedDict, total=False):
    networkEndpointGroups: typing.List[NetworkEndpointGroup]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NetworkEndpointWithHealthStatus(typing_extensions.TypedDict, total=False):
    healths: typing.List[HealthStatusForNetworkEndpoint]
    networkEndpoint: NetworkEndpoint

@typing.type_check_only
class NetworkInterface(typing_extensions.TypedDict, total=False):
    accessConfigs: typing.List[AccessConfig]
    aliasIpRanges: typing.List[AliasIpRange]
    fingerprint: str
    internalIpv6PrefixLength: int
    ipv6AccessConfigs: typing.List[AccessConfig]
    ipv6AccessType: typing_extensions.Literal[
        "EXTERNAL", "INTERNAL", "UNSPECIFIED_IPV6_ACCESS_TYPE"
    ]
    ipv6Address: str
    kind: str
    name: str
    network: str
    networkIP: str
    nicType: typing_extensions.Literal["GVNIC", "UNSPECIFIED_NIC_TYPE", "VIRTIO_NET"]
    queueCount: int
    stackType: typing_extensions.Literal[
        "IPV4_IPV6", "IPV4_ONLY", "UNSPECIFIED_STACK_TYPE"
    ]
    subinterfaces: typing.List[NetworkInterfaceSubInterface]
    subnetwork: str

@typing.type_check_only
class NetworkInterfaceSubInterface(typing_extensions.TypedDict, total=False):
    ipAddress: str
    subnetwork: str
    vlan: int

@typing.type_check_only
class NetworkList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Network]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NetworkPeering(typing_extensions.TypedDict, total=False):
    advertisePeerSubnetsViaRouters: bool
    autoCreateRoutes: bool
    exchangeSubnetRoutes: bool
    exportCustomRoutes: bool
    exportSubnetRoutesWithPublicIp: bool
    importCustomRoutes: bool
    importSubnetRoutesWithPublicIp: bool
    name: str
    network: str
    peerMtu: int
    state: typing_extensions.Literal["ACTIVE", "INACTIVE"]
    stateDetails: str

@typing.type_check_only
class NetworkPerformanceConfig(typing_extensions.TypedDict, total=False):
    externalIpEgressBandwidthTier: typing_extensions.Literal["DEFAULT", "TIER_1"]
    totalEgressBandwidthTier: typing_extensions.Literal["DEFAULT", "TIER_1"]

@typing.type_check_only
class NetworkRoutingConfig(typing_extensions.TypedDict, total=False):
    routingMode: typing_extensions.Literal["GLOBAL", "REGIONAL"]

@typing.type_check_only
class NetworksAddPeeringRequest(typing_extensions.TypedDict, total=False):
    autoCreateRoutes: bool
    exportCustomRoutes: bool
    importCustomRoutes: bool
    name: str
    networkPeering: NetworkPeering
    peerNetwork: str

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponse(typing_extensions.TypedDict, total=False):
    firewallPolicys: typing.List[
        NetworksGetEffectiveFirewallsResponseEffectiveFirewallPolicy
    ]
    firewalls: typing.List[Firewall]
    organizationFirewalls: typing.List[
        NetworksGetEffectiveFirewallsResponseOrganizationFirewallPolicy
    ]

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseEffectiveFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    name: str
    rules: typing.List[FirewallPolicyRule]
    type: typing_extensions.Literal["HIERARCHY", "NETWORK", "UNSPECIFIED"]

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseOrganizationFirewallPolicy(
    typing_extensions.TypedDict, total=False
):
    id: str
    rules: typing.List[SecurityPolicyRule]

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
    selfLinkWithId: str
    size: int
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    zone: str

@typing.type_check_only
class NodeGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeGroupAutoscalingPolicy(typing_extensions.TypedDict, total=False):
    maxNodes: int
    minNodes: int
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "OFF", "ON", "ONLY_SCALE_OUT"]

@typing.type_check_only
class NodeGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeGroupMaintenanceWindow(typing_extensions.TypedDict, total=False):
    duration: str
    maintenanceDuration: Duration
    startTime: str

@typing.type_check_only
class NodeGroupNode(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[AcceleratorConfig]
    cpuOvercommitType: typing_extensions.Literal[
        "CPU_OVERCOMMIT_TYPE_UNSPECIFIED", "ENABLED", "NONE"
    ]
    disks: typing.List[LocalDisk]
    instances: typing.List[str]
    name: str
    nodeType: str
    satisfiesPzs: bool
    serverBinding: ServerBinding
    serverId: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "REPAIRING"
    ]

@typing.type_check_only
class NodeGroupsAddNodesRequest(typing_extensions.TypedDict, total=False):
    additionalNodeCount: int

@typing.type_check_only
class NodeGroupsDeleteNodesRequest(typing_extensions.TypedDict, total=False):
    nodes: typing.List[str]

@typing.type_check_only
class NodeGroupsListNodes(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeGroupNode]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeGroupsScopedList(typing_extensions.TypedDict, total=False):
    nodeGroups: typing.List[NodeGroup]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeGroupsSetNodeTemplateRequest(typing_extensions.TypedDict, total=False):
    nodeTemplate: str

@typing.type_check_only
class NodeTemplate(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[AcceleratorConfig]
    cpuOvercommitType: typing_extensions.Literal[
        "CPU_OVERCOMMIT_TYPE_UNSPECIFIED", "ENABLED", "NONE"
    ]
    creationTimestamp: str
    description: str
    disks: typing.List[LocalDisk]
    id: str
    kind: str
    name: str
    nodeAffinityLabels: typing.Dict[str, typing.Any]
    nodeType: str
    nodeTypeFlexibility: NodeTemplateNodeTypeFlexibility
    region: str
    selfLink: str
    selfLinkWithId: str
    serverBinding: ServerBinding
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    statusMessage: str

@typing.type_check_only
class NodeTemplateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeTemplateList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeTemplateNodeTypeFlexibility(typing_extensions.TypedDict, total=False):
    cpus: str
    localSsd: str
    memory: str

@typing.type_check_only
class NodeTemplatesScopedList(typing_extensions.TypedDict, total=False):
    nodeTemplates: typing.List[NodeTemplate]
    warning: typing.Dict[str, typing.Any]

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
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class NodeTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NodeTypesScopedList(typing_extensions.TypedDict, total=False):
    nodeTypes: typing.List[NodeType]
    warning: typing.Dict[str, typing.Any]

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
class NotificationEndpointAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

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
    items: typing.List[NotificationEndpoint]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class NotificationEndpointsScopedList(typing_extensions.TypedDict, total=False):
    resources: typing.List[NotificationEndpoint]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: typing.Dict[str, typing.Any]
    httpErrorMessage: str
    httpErrorStatusCode: int
    id: str
    insertTime: str
    kind: str
    metadata: Any
    name: str
    operationGroupId: str
    operationType: str
    progress: int
    region: str
    selfLink: str
    selfLinkWithId: str
    startTime: str
    status: typing_extensions.Literal["DONE", "PENDING", "RUNNING"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Operation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationsScopedList(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class OrganizationSecurityPoliciesListAssociationsResponse(
    typing_extensions.TypedDict, total=False
):
    associations: typing.List[SecurityPolicyAssociation]
    kind: str

@typing.type_check_only
class OriginAuthenticationMethod(typing_extensions.TypedDict, total=False):
    jwt: Jwt

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
    selfLinkWithId: str

@typing.type_check_only
class PacketMirroringAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class PacketMirroringFilter(typing_extensions.TypedDict, total=False):
    IPProtocols: typing.List[str]
    cidrRanges: typing.List[str]
    direction: typing_extensions.Literal["BOTH", "EGRESS", "INGRESS"]

@typing.type_check_only
class PacketMirroringForwardingRuleInfo(typing_extensions.TypedDict, total=False):
    canonicalUrl: str
    url: str

@typing.type_check_only
class PacketMirroringList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[PacketMirroring]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class PacketMirroringMirroredResourceInfo(typing_extensions.TypedDict, total=False):
    instances: typing.List[PacketMirroringMirroredResourceInfoInstanceInfo]
    subnetworks: typing.List[PacketMirroringMirroredResourceInfoSubnetInfo]
    tags: typing.List[str]

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
    packetMirrorings: typing.List[PacketMirroring]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class PathMatcher(typing_extensions.TypedDict, total=False):
    defaultRouteAction: HttpRouteAction
    defaultService: str
    defaultUrlRedirect: HttpRedirectAction
    description: str
    headerAction: HttpHeaderAction
    name: str
    pathRules: typing.List[PathRule]
    routeRules: typing.List[HttpRouteRule]

@typing.type_check_only
class PathRule(typing_extensions.TypedDict, total=False):
    paths: typing.List[str]
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

@typing.type_check_only
class PeerAuthenticationMethod(typing_extensions.TypedDict, total=False):
    mtls: MutualTls

@typing.type_check_only
class PerInstanceConfig(typing_extensions.TypedDict, total=False):
    fingerprint: str
    name: str
    preservedState: PreservedState
    status: typing_extensions.Literal[
        "APPLYING", "DELETING", "EFFECTIVE", "NONE", "UNAPPLIED", "UNAPPLIED_DELETION"
    ]

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    constraints: typing.List[PermissionConstraint]
    hosts: typing.List[str]
    methods: typing.List[str]
    notHosts: typing.List[str]
    notMethods: typing.List[str]
    notPaths: typing.List[str]
    notPorts: typing.List[str]
    paths: typing.List[str]
    ports: typing.List[str]

@typing.type_check_only
class PermissionConstraint(typing_extensions.TypedDict, total=False):
    key: str
    values: typing.List[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    iamOwned: bool
    rules: typing.List[Rule]
    version: int

@typing.type_check_only
class PreconfiguredWafSet(typing_extensions.TypedDict, total=False):
    expressionSets: typing.List[WafExpressionSet]

@typing.type_check_only
class PreservedState(typing_extensions.TypedDict, total=False):
    disks: typing.Dict[str, typing.Any]
    externalIPs: typing.Dict[str, typing.Any]
    internalIPs: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

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
class Principal(typing_extensions.TypedDict, total=False):
    condition: str
    groups: typing.List[str]
    ips: typing.List[str]
    namespaces: typing.List[str]
    notGroups: typing.List[str]
    notIps: typing.List[str]
    notNamespaces: typing.List[str]
    notUsers: typing.List[str]
    properties: typing.Dict[str, typing.Any]
    users: typing.List[str]

@typing.type_check_only
class Project(typing_extensions.TypedDict, total=False):
    commonInstanceMetadata: Metadata
    creationTimestamp: str
    defaultNetworkTier: typing_extensions.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]
    defaultServiceAccount: str
    description: str
    enabledFeatures: typing.List[str]
    id: str
    kind: str
    name: str
    quotas: typing.List[Quota]
    selfLink: str
    usageExportLocation: UsageExportLocation
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
    resources: typing.List[XpnResourceId]

@typing.type_check_only
class ProjectsListXpnHostsRequest(typing_extensions.TypedDict, total=False):
    organization: str

@typing.type_check_only
class ProjectsSetDefaultNetworkTierRequest(typing_extensions.TypedDict, total=False):
    networkTier: typing_extensions.Literal[
        "FIXED_STANDARD",
        "PREMIUM",
        "SELECT",
        "STANDARD",
        "STANDARD_OVERRIDES_FIXED_STANDARD",
    ]

@typing.type_check_only
class ProjectsSetDefaultServiceAccountRequest(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class PublicAdvertisedPrefix(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    dnsVerificationIp: str
    fingerprint: str
    id: str
    ipCidrRange: str
    kind: str
    name: str
    publicDelegatedPrefixs: typing.List[PublicAdvertisedPrefixPublicDelegatedPrefix]
    selfLink: str
    selfLinkWithId: str
    sharedSecret: str
    status: typing_extensions.Literal[
        "INITIAL",
        "PREFIX_CONFIGURATION_COMPLETE",
        "PREFIX_CONFIGURATION_IN_PROGRESS",
        "PREFIX_REMOVAL_IN_PROGRESS",
        "PTR_CONFIGURED",
        "REVERSE_DNS_LOOKUP_FAILED",
        "VALIDATED",
    ]

@typing.type_check_only
class PublicAdvertisedPrefixList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[PublicAdvertisedPrefix]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    ipCidrRange: str
    isLiveMigration: bool
    kind: str
    name: str
    parentPrefix: str
    publicDelegatedSubPrefixs: typing.List[
        PublicDelegatedPrefixPublicDelegatedSubPrefix
    ]
    region: str
    selfLink: str
    selfLinkWithId: str
    status: typing_extensions.Literal["ANNOUNCED", "DELETING", "INITIALIZING"]

@typing.type_check_only
class PublicDelegatedPrefixAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class PublicDelegatedPrefixList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[PublicDelegatedPrefix]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class PublicDelegatedPrefixPublicDelegatedSubPrefix(
    typing_extensions.TypedDict, total=False
):
    delegateeProject: str
    description: str
    ipCidrRange: str
    isAddress: bool
    name: str
    region: str
    status: typing_extensions.Literal["ACTIVE", "INACTIVE"]

@typing.type_check_only
class PublicDelegatedPrefixesScopedList(typing_extensions.TypedDict, total=False):
    publicDelegatedPrefixes: typing.List[PublicDelegatedPrefix]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    limit: float
    metric: typing_extensions.Literal[
        "A2_CPUS",
        "AFFINITY_GROUPS",
        "ALIASES_PER_NETWORK_GLOBAL",
        "AMD_S9300_GPUS",
        "AUTOSCALERS",
        "BACKEND_BUCKETS",
        "BACKEND_SERVICES",
        "C2_CPUS",
        "COMMITMENTS",
        "COMMITTED_A2_CPUS",
        "COMMITTED_C2_CPUS",
        "COMMITTED_CPUS",
        "COMMITTED_E2_CPUS",
        "COMMITTED_LICENSES",
        "COMMITTED_LOCAL_SSD_TOTAL_GB",
        "COMMITTED_MEMORY_OPTIMIZED_CPUS",
        "COMMITTED_N2D_CPUS",
        "COMMITTED_N2_CPUS",
        "COMMITTED_NVIDIA_A100_GPUS",
        "COMMITTED_NVIDIA_K80_GPUS",
        "COMMITTED_NVIDIA_P100_GPUS",
        "COMMITTED_NVIDIA_P4_GPUS",
        "COMMITTED_NVIDIA_T4_GPUS",
        "COMMITTED_NVIDIA_V100_GPUS",
        "CPUS",
        "CPUS_ALL_REGIONS",
        "DISKS_TOTAL_GB",
        "E2_CPUS",
        "EXTERNAL_NETWORK_LB_FORWARDING_RULES",
        "EXTERNAL_PROTOCOL_FORWARDING_RULES",
        "EXTERNAL_VPN_GATEWAYS",
        "FIREWALLS",
        "FORWARDING_RULES",
        "GLOBAL_INTERNAL_ADDRESSES",
        "GPUS_ALL_REGIONS",
        "HEALTH_CHECKS",
        "IMAGES",
        "INSTANCES",
        "INSTANCES_PER_NETWORK_GLOBAL",
        "INSTANCE_GROUPS",
        "INSTANCE_GROUP_MANAGERS",
        "INSTANCE_TEMPLATES",
        "INTERCONNECTS",
        "INTERCONNECT_ATTACHMENTS_PER_REGION",
        "INTERCONNECT_ATTACHMENTS_TOTAL_MBPS",
        "INTERCONNECT_TOTAL_GBPS",
        "INTERNAL_ADDRESSES",
        "INTERNAL_FORWARDING_RULES_PER_NETWORK",
        "INTERNAL_FORWARDING_RULES_WITH_GLOBAL_ACCESS_PER_NETWORK",
        "INTERNAL_FORWARDING_RULES_WITH_TARGET_INSTANCE_PER_NETWORK",
        "INTERNAL_TARGET_INSTANCE_WITH_GLOBAL_ACCESS_PER_NETWORK",
        "INTERNAL_TRAFFIC_DIRECTOR_FORWARDING_RULES",
        "IN_PLACE_SNAPSHOTS",
        "IN_USE_ADDRESSES",
        "IN_USE_BACKUP_SCHEDULES",
        "IN_USE_MAINTENANCE_WINDOWS",
        "IN_USE_SNAPSHOT_SCHEDULES",
        "LOCAL_SSD_TOTAL_GB",
        "M1_CPUS",
        "M2_CPUS",
        "MACHINE_IMAGES",
        "N2D_CPUS",
        "N2_CPUS",
        "NETWORKS",
        "NETWORK_ENDPOINT_GROUPS",
        "NETWORK_FIREWALL_POLICIES",
        "NODE_GROUPS",
        "NODE_TEMPLATES",
        "NVIDIA_A100_GPUS",
        "NVIDIA_K80_GPUS",
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
        "PREEMPTIBLE_NVIDIA_A100_GPUS",
        "PREEMPTIBLE_NVIDIA_K80_GPUS",
        "PREEMPTIBLE_NVIDIA_P100_GPUS",
        "PREEMPTIBLE_NVIDIA_P100_VWS_GPUS",
        "PREEMPTIBLE_NVIDIA_P4_GPUS",
        "PREEMPTIBLE_NVIDIA_P4_VWS_GPUS",
        "PREEMPTIBLE_NVIDIA_T4_GPUS",
        "PREEMPTIBLE_NVIDIA_T4_VWS_GPUS",
        "PREEMPTIBLE_NVIDIA_V100_GPUS",
        "PRIVATE_V6_ACCESS_SUBNETWORKS",
        "PSC_GOOGLE_APIS_FORWARDING_RULES_PER_NETWORK",
        "PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK",
        "PUBLIC_ADVERTISED_PREFIXES",
        "PUBLIC_DELEGATED_PREFIXES",
        "REGIONAL_AUTOSCALERS",
        "REGIONAL_INSTANCE_GROUP_MANAGERS",
        "RESERVATIONS",
        "RESOURCE_POLICIES",
        "ROUTERS",
        "ROUTES",
        "SECURITY_POLICIES",
        "SECURITY_POLICY_CEVAL_RULES",
        "SECURITY_POLICY_RULES",
        "SNAPSHOTS",
        "SSD_TOTAL_GB",
        "SSL_CERTIFICATES",
        "STATIC_ADDRESSES",
        "STATIC_BYOIP_ADDRESSES",
        "SUBNETWORKS",
        "SUBNET_RANGES_PER_NETWORK",
        "TARGET_HTTPS_PROXIES",
        "TARGET_HTTP_PROXIES",
        "TARGET_INSTANCES",
        "TARGET_POOLS",
        "TARGET_SSL_PROXIES",
        "TARGET_TCP_PROXIES",
        "TARGET_VPN_GATEWAYS",
        "URL_MAPS",
        "VPN_GATEWAYS",
        "VPN_TUNNELS",
        "XPN_SERVICE_PROJECTS",
    ]
    owner: str
    usage: float

@typing.type_check_only
class RbacPolicy(typing_extensions.TypedDict, total=False):
    name: str
    permissions: typing.List[Permission]
    principals: typing.List[Principal]

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
    quotas: typing.List[Quota]
    selfLink: str
    selfLinkWithId: str
    status: typing_extensions.Literal["DOWN", "UP"]
    supportsPzs: bool
    zones: typing.List[str]

@typing.type_check_only
class RegionAutoscalerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionCommitmentsUpdateReservationsRequest(
    typing_extensions.TypedDict, total=False
):
    reservations: typing.List[Reservation]

@typing.type_check_only
class RegionDiskTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionDisksAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

@typing.type_check_only
class RegionDisksRemoveResourcePoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    resourcePolicies: typing.List[str]

@typing.type_check_only
class RegionDisksResizeRequest(typing_extensions.TypedDict, total=False):
    sizeGb: str

@typing.type_check_only
class RegionInstanceGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerDeleteInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

@typing.type_check_only
class RegionInstanceGroupManagerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagerPatchInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagerUpdateInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersAbandonInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

@typing.type_check_only
class RegionInstanceGroupManagersApplyUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    allInstances: bool
    instances: typing.List[str]
    maximalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]

@typing.type_check_only
class RegionInstanceGroupManagersCreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[PerInstanceConfig]

@typing.type_check_only
class RegionInstanceGroupManagersDeleteInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]
    skipInapplicableInstances: bool

@typing.type_check_only
class RegionInstanceGroupManagersListErrorsResponse(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[InstanceManagedByIgmError]
    nextPageToken: str

@typing.type_check_only
class RegionInstanceGroupManagersListInstanceConfigsResp(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[PerInstanceConfig]
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionInstanceGroupManagersListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    managedInstances: typing.List[ManagedInstance]
    nextPageToken: str

@typing.type_check_only
class RegionInstanceGroupManagersRecreateRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

@typing.type_check_only
class RegionInstanceGroupManagersResizeAdvancedRequest(
    typing_extensions.TypedDict, total=False
):
    noCreationRetries: bool
    targetSize: int

@typing.type_check_only
class RegionInstanceGroupManagersSetAutoHealingRequest(
    typing_extensions.TypedDict, total=False
):
    autoHealingPolicies: typing.List[InstanceGroupManagerAutoHealingPolicy]

@typing.type_check_only
class RegionInstanceGroupManagersSetTargetPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    targetPools: typing.List[str]

@typing.type_check_only
class RegionInstanceGroupManagersSetTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    instanceTemplate: str

@typing.type_check_only
class RegionInstanceGroupsListInstances(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    namedPorts: typing.List[NamedPort]

@typing.type_check_only
class RegionInstantSnapshotsExportRequest(typing_extensions.TypedDict, total=False):
    exportParams: InstantSnapshotExportParams

@typing.type_check_only
class RegionList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Region]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class RegionSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class RegionTargetHttpsProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: typing.List[str]

@typing.type_check_only
class RegionUrlMapsValidateRequest(typing_extensions.TypedDict, total=False):
    resource: UrlMap

@typing.type_check_only
class RequestMirrorPolicy(typing_extensions.TypedDict, total=False):
    backendService: str

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    commitment: str
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    shareSettings: AllocationShareSettings
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
        "UNSPECIFIED",
    ]
    key: str
    values: typing.List[str]

@typing.type_check_only
class ReservationAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ReservationList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Reservation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ReservationsResizeRequest(typing_extensions.TypedDict, total=False):
    specificSkuCount: str

@typing.type_check_only
class ReservationsScopedList(typing_extensions.TypedDict, total=False):
    reservations: typing.List[Reservation]
    warning: typing.Dict[str, typing.Any]

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
    resourcePolicies: typing.List[ResourcePolicy]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
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
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "EXPIRED", "INVALID", "READY"
    ]
    vmMaintenancePolicy: ResourcePolicyVmMaintenancePolicy

@typing.type_check_only
class ResourcePolicyAggregatedList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ResourcePolicyDailyCycle(typing_extensions.TypedDict, total=False):
    daysInCycle: int
    duration: str
    startTime: str

@typing.type_check_only
class ResourcePolicyGroupPlacementPolicy(typing_extensions.TypedDict, total=False):
    availabilityDomainCount: int
    collocation: typing_extensions.Literal[
        "CLUSTERED", "COLLOCATED", "UNSPECIFIED_COLLOCATION"
    ]
    locality: typing_extensions.Literal["BEST_EFFORT", "STRICT", "UNSPECIFIED_LOCALITY"]
    scope: typing_extensions.Literal["HOST", "UNSPECIFIED_SCOPE"]
    style: typing_extensions.Literal[
        "COMPACT", "FULLY_SPREAD", "UNSPECIFIED_PLACEMENT_TYPE"
    ]
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
    items: typing.List[ResourcePolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    onPolicySwitch: typing_extensions.Literal[
        "DO_NOT_RETROACTIVELY_APPLY",
        "RETROACTIVELY_APPLY",
        "UNSPECIFIED_ON_POLICY_SWITCH",
    ]
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
    labels: typing.Dict[str, typing.Any]
    storageLocations: typing.List[str]

@typing.type_check_only
class ResourcePolicyVmMaintenancePolicy(typing_extensions.TypedDict, total=False):
    concurrencyControlGroup: ResourcePolicyVmMaintenancePolicyConcurrencyControl
    maintenanceWindow: ResourcePolicyVmMaintenancePolicyMaintenanceWindow

@typing.type_check_only
class ResourcePolicyVmMaintenancePolicyConcurrencyControl(
    typing_extensions.TypedDict, total=False
):
    concurrencyLimit: int

@typing.type_check_only
class ResourcePolicyVmMaintenancePolicyMaintenanceWindow(
    typing_extensions.TypedDict, total=False
):
    dailyMaintenanceWindow: ResourcePolicyDailyCycle

@typing.type_check_only
class ResourcePolicyWeeklyCycle(typing_extensions.TypedDict, total=False):
    dayOfWeeks: typing.List[ResourcePolicyWeeklyCycleDayOfWeek]

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
class ResourceStatus(typing_extensions.TypedDict, total=False):
    scheduling: ResourceStatusScheduling

@typing.type_check_only
class ResourceStatusScheduling(typing_extensions.TypedDict, total=False):
    availabilityDomain: int

@typing.type_check_only
class RolloutPolicy(typing_extensions.TypedDict, total=False):
    defaultRolloutTime: str
    locationRolloutPolicies: typing.Dict[str, typing.Any]

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    destRange: str
    id: str
    kind: str
    name: str
    network: str
    nextHopGateway: str
    nextHopIlb: str
    nextHopInstance: str
    nextHopInterconnectAttachment: str
    nextHopIp: str
    nextHopNetwork: str
    nextHopPeering: str
    nextHopVpnTunnel: str
    priority: int
    selfLink: str
    selfLinkWithId: str
    tags: typing.List[str]
    warnings: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class RouteList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Route]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Router(typing_extensions.TypedDict, total=False):
    bgp: RouterBgp
    bgpPeers: typing.List[RouterBgpPeer]
    creationTimestamp: str
    description: str
    encryptedInterconnectRouter: bool
    id: str
    interfaces: typing.List[RouterInterface]
    kind: str
    name: str
    nats: typing.List[RouterNat]
    network: str
    region: str
    selfLink: str
    selfLinkWithId: str

@typing.type_check_only
class RouterAdvertisedIpRange(typing_extensions.TypedDict, total=False):
    description: str
    range: str

@typing.type_check_only
class RouterAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RouterBgp(typing_extensions.TypedDict, total=False):
    advertiseMode: typing_extensions.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: typing.List[str]
    advertisedIpRanges: typing.List[RouterAdvertisedIpRange]
    asn: int
    keepaliveInterval: int

@typing.type_check_only
class RouterBgpPeer(typing_extensions.TypedDict, total=False):
    advertiseMode: typing_extensions.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: typing.List[str]
    advertisedIpRanges: typing.List[RouterAdvertisedIpRange]
    advertisedRoutePriority: int
    bfd: RouterBgpPeerBfd
    enable: typing_extensions.Literal["FALSE", "TRUE"]
    interfaceName: str
    ipAddress: str
    managementType: typing_extensions.Literal[
        "MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"
    ]
    name: str
    peerAsn: int
    peerIpAddress: str
    routerApplianceInstance: str

@typing.type_check_only
class RouterBgpPeerBfd(typing_extensions.TypedDict, total=False):
    minReceiveInterval: int
    minTransmitInterval: int
    mode: typing_extensions.Literal["ACTIVE", "DISABLED", "PASSIVE"]
    multiplier: int
    packetMode: typing_extensions.Literal["CONTROL_AND_ECHO", "CONTROL_ONLY"]
    sessionInitializationMode: typing_extensions.Literal[
        "ACTIVE", "DISABLED", "PASSIVE"
    ]
    slowTimerInterval: int

@typing.type_check_only
class RouterInterface(typing_extensions.TypedDict, total=False):
    ipRange: str
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
    items: typing.List[Router]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class RouterNat(typing_extensions.TypedDict, total=False):
    drainNatIps: typing.List[str]
    enableEndpointIndependentMapping: bool
    icmpIdleTimeoutSec: int
    logConfig: RouterNatLogConfig
    minPortsPerVm: int
    name: str
    natIpAllocateOption: typing_extensions.Literal["AUTO_ONLY", "MANUAL_ONLY"]
    natIps: typing.List[str]
    rules: typing.List[RouterNatRule]
    sourceSubnetworkIpRangesToNat: typing_extensions.Literal[
        "ALL_SUBNETWORKS_ALL_IP_RANGES",
        "ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES",
        "LIST_OF_SUBNETWORKS",
    ]
    subnetworks: typing.List[RouterNatSubnetworkToNat]
    tcpEstablishedIdleTimeoutSec: int
    tcpTimeWaitTimeoutSec: int
    tcpTransitoryIdleTimeoutSec: int
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
    sourceNatActiveIps: typing.List[str]
    sourceNatDrainIps: typing.List[str]

@typing.type_check_only
class RouterNatSubnetworkToNat(typing_extensions.TypedDict, total=False):
    name: str
    secondaryIpRangeNames: typing.List[str]
    sourceIpRangesToNat: typing.List[str]

@typing.type_check_only
class RouterStatus(typing_extensions.TypedDict, total=False):
    bestRoutes: typing.List[Route]
    bestRoutesForRouter: typing.List[Route]
    bgpPeerStatus: typing.List[RouterStatusBgpPeerStatus]
    natStatus: typing.List[RouterStatusNatStatus]
    network: str

@typing.type_check_only
class RouterStatusBgpPeerStatus(typing_extensions.TypedDict, total=False):
    advertisedRoutes: typing.List[Route]
    bfdStatus: BfdStatus
    ipAddress: str
    linkedVpnTunnel: str
    name: str
    numLearnedRoutes: int
    peerIpAddress: str
    state: str
    status: typing_extensions.Literal["DOWN", "UNKNOWN", "UP"]
    uptime: str
    uptimeSeconds: str

@typing.type_check_only
class RouterStatusNatStatus(typing_extensions.TypedDict, total=False):
    autoAllocatedNatIps: typing.List[str]
    drainAutoAllocatedNatIps: typing.List[str]
    drainUserAllocatedNatIps: typing.List[str]
    minExtraNatIpsNeeded: int
    name: str
    numVmEndpointsWithNatMappings: int
    ruleStatus: typing.List[RouterStatusNatStatusNatRuleStatus]
    userAllocatedNatIpResources: typing.List[str]
    userAllocatedNatIps: typing.List[str]

@typing.type_check_only
class RouterStatusNatStatusNatRuleStatus(typing_extensions.TypedDict, total=False):
    activeNatIps: typing.List[str]
    drainNatIps: typing.List[str]
    minExtraIpsNeeded: int
    numVmEndpointsWithNatMappings: int
    ruleNumber: int

@typing.type_check_only
class RouterStatusResponse(typing_extensions.TypedDict, total=False):
    kind: str
    result: RouterStatus

@typing.type_check_only
class RoutersPreviewResponse(typing_extensions.TypedDict, total=False):
    resource: Router

@typing.type_check_only
class RoutersScopedList(typing_extensions.TypedDict, total=False):
    routers: typing.List[Router]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class Rule(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "ALLOW", "ALLOW_WITH_LOG", "DENY", "DENY_WITH_LOG", "LOG", "NO_ACTION"
    ]
    conditions: typing.List[Condition]
    description: str
    ins: typing.List[str]
    logConfigs: typing.List[LogConfig]
    notIns: typing.List[str]
    permissions: typing.List[str]

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
    guestOsFeatures: typing.List[GuestOsFeature]
    index: int
    interface: typing_extensions.Literal["NVDIMM", "NVME", "SCSI"]
    kind: str
    licenses: typing.List[str]
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    source: str
    storageBytes: str
    storageBytesStatus: typing_extensions.Literal["UPDATING", "UP_TO_DATE"]
    type: typing_extensions.Literal["PERSISTENT", "SCRATCH"]

@typing.type_check_only
class ScalingScheduleStatus(typing_extensions.TypedDict, total=False):
    lastStartTime: str
    nextStartTime: str
    state: typing_extensions.Literal["ACTIVE", "DISABLED", "OBSOLETE", "READY"]

@typing.type_check_only
class Scheduling(typing_extensions.TypedDict, total=False):
    automaticRestart: bool
    availabilityDomain: int
    latencyTolerant: bool
    locationHint: str
    maintenanceFreezeDurationHours: int
    maintenanceInterval: typing_extensions.Literal["PERIODIC"]
    minNodeCpus: int
    nodeAffinities: typing.List[SchedulingNodeAffinity]
    onHostMaintenance: typing_extensions.Literal["MIGRATE", "TERMINATE"]
    preemptible: bool

@typing.type_check_only
class SchedulingNodeAffinity(typing_extensions.TypedDict, total=False):
    key: str
    operator: typing_extensions.Literal["IN", "NOT_IN", "OPERATOR_UNSPECIFIED"]
    values: typing.List[str]

@typing.type_check_only
class Screenshot(typing_extensions.TypedDict, total=False):
    contents: str
    kind: str

@typing.type_check_only
class SdsConfig(typing_extensions.TypedDict, total=False):
    grpcServiceConfig: GrpcServiceConfig

@typing.type_check_only
class SecurityPoliciesListPreconfiguredExpressionSetsResponse(
    typing_extensions.TypedDict, total=False
):
    preconfiguredExpressionSets: SecurityPoliciesWafConfig

@typing.type_check_only
class SecurityPoliciesWafConfig(typing_extensions.TypedDict, total=False):
    wafRules: PreconfiguredWafSet

@typing.type_check_only
class SecurityPolicy(typing_extensions.TypedDict, total=False):
    adaptiveProtectionConfig: SecurityPolicyAdaptiveProtectionConfig
    associations: typing.List[SecurityPolicyAssociation]
    cloudArmorConfig: SecurityPolicyCloudArmorConfig
    creationTimestamp: str
    description: str
    displayName: str
    fingerprint: str
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    parent: str
    ruleTupleCount: int
    rules: typing.List[SecurityPolicyRule]
    selfLink: str
    selfLinkWithId: str
    type: typing_extensions.Literal["CLOUD_ARMOR", "CLOUD_ARMOR_EDGE", "FIREWALL"]

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfig(typing_extensions.TypedDict, total=False):
    layer7DdosDefenseConfig: SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig

@typing.type_check_only
class SecurityPolicyAdaptiveProtectionConfigLayer7DdosDefenseConfig(
    typing_extensions.TypedDict, total=False
):
    enable: bool
    ruleVisibility: typing_extensions.Literal["PREMIUM", "STANDARD"]

@typing.type_check_only
class SecurityPolicyAssociation(typing_extensions.TypedDict, total=False):
    attachmentId: str
    displayName: str
    name: str
    securityPolicyId: str

@typing.type_check_only
class SecurityPolicyCloudArmorConfig(typing_extensions.TypedDict, total=False):
    enableMl: bool

@typing.type_check_only
class SecurityPolicyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[SecurityPolicy]
    kind: str
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SecurityPolicyReference(typing_extensions.TypedDict, total=False):
    securityPolicy: str

@typing.type_check_only
class SecurityPolicyRule(typing_extensions.TypedDict, total=False):
    action: str
    description: str
    direction: typing_extensions.Literal["EGRESS", "INGRESS"]
    enableLogging: bool
    kind: str
    match: SecurityPolicyRuleMatcher
    preview: bool
    priority: int
    rateLimitOptions: SecurityPolicyRuleRateLimitOptions
    redirectTarget: str
    ruleNumber: str
    ruleTupleCount: int
    targetResources: typing.List[str]
    targetServiceAccounts: typing.List[str]

@typing.type_check_only
class SecurityPolicyRuleMatcher(typing_extensions.TypedDict, total=False):
    config: SecurityPolicyRuleMatcherConfig
    expr: Expr
    versionedExpr: typing_extensions.Literal["FIREWALL", "SRC_IPS_V1"]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfig(typing_extensions.TypedDict, total=False):
    destIpRanges: typing.List[str]
    destPorts: typing.List[SecurityPolicyRuleMatcherConfigDestinationPort]
    layer4Configs: typing.List[SecurityPolicyRuleMatcherConfigLayer4Config]
    srcIpRanges: typing.List[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfigDestinationPort(
    typing_extensions.TypedDict, total=False
):
    ipProtocol: str
    ports: typing.List[str]

@typing.type_check_only
class SecurityPolicyRuleMatcherConfigLayer4Config(
    typing_extensions.TypedDict, total=False
):
    ipProtocol: str
    ports: typing.List[str]

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptions(typing_extensions.TypedDict, total=False):
    banDurationSec: int
    banThreshold: SecurityPolicyRuleRateLimitOptionsThreshold
    blockDuration: int
    conformAction: str
    enforceOnKey: typing_extensions.Literal["ALL_IPS", "IP"]
    exceedAction: str
    rateLimitThreshold: SecurityPolicyRuleRateLimitOptionsThreshold
    thresholdRps: int

@typing.type_check_only
class SecurityPolicyRuleRateLimitOptionsThreshold(
    typing_extensions.TypedDict, total=False
):
    count: int
    intervalSec: int

@typing.type_check_only
class SecuritySettings(typing_extensions.TypedDict, total=False):
    authentication: str
    authenticationPolicy: AuthenticationPolicy
    authorizationConfig: AuthorizationConfig
    clientTlsPolicy: str
    clientTlsSettings: ClientTlsSettings
    subjectAltNames: typing.List[str]

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
class ServerTlsSettings(typing_extensions.TypedDict, total=False):
    proxyTlsContext: TlsContext
    subjectAltNames: typing.List[str]
    tlsMode: typing_extensions.Literal["INVALID", "MUTUAL", "SIMPLE"]

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

@typing.type_check_only
class ServiceAttachment(typing_extensions.TypedDict, total=False):
    connectionPreference: typing_extensions.Literal[
        "ACCEPT_AUTOMATIC", "CONNECTION_PREFERENCE_UNSPECIFIED"
    ]
    consumerForwardingRules: typing.List[ServiceAttachmentConsumerForwardingRule]
    creationTimestamp: str
    description: str
    enableProxyProtocol: bool
    id: str
    kind: str
    name: str
    natSubnets: typing.List[str]
    producerForwardingRule: str
    region: str
    selfLink: str

@typing.type_check_only
class ServiceAttachmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ServiceAttachmentConsumerForwardingRule(typing_extensions.TypedDict, total=False):
    forwardingRule: str
    status: typing_extensions.Literal[
        "ACCEPTED", "PENDING", "REJECTED", "STATUS_UNSPECIFIED"
    ]

@typing.type_check_only
class ServiceAttachmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[ServiceAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ServiceAttachmentsScopedList(typing_extensions.TypedDict, total=False):
    resources: typing.List[ServiceAttachment]
    warning: typing.Dict[str, typing.Any]

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
    autoCreated: bool
    chainName: str
    creationTimestamp: str
    description: str
    diskSizeGb: str
    downloadBytes: str
    guestFlush: bool
    guestOsFeatures: typing.List[GuestOsFeature]
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    licenseCodes: typing.List[str]
    licenses: typing.List[str]
    locationHint: str
    name: str
    satisfiesPzs: bool
    selfLink: str
    selfLinkWithId: str
    snapshotEncryptionKey: CustomerEncryptionKey
    sourceDisk: str
    sourceDiskEncryptionKey: CustomerEncryptionKey
    sourceDiskId: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "UPLOADING"
    ]
    storageBytes: str
    storageBytesStatus: typing_extensions.Literal["UPDATING", "UP_TO_DATE"]
    storageLocations: typing.List[str]

@typing.type_check_only
class SnapshotList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Snapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SourceDiskEncryptionKey(typing_extensions.TypedDict, total=False):
    diskEncryptionKey: CustomerEncryptionKey
    sourceDisk: str

@typing.type_check_only
class SourceInstanceParams(typing_extensions.TypedDict, total=False):
    diskConfigs: typing.List[DiskInstantiationConfig]

@typing.type_check_only
class SourceInstanceProperties(typing_extensions.TypedDict, total=False):
    canIpForward: bool
    deletionProtection: bool
    description: str
    disks: typing.List[SavedAttachedDisk]
    guestAccelerators: typing.List[AcceleratorConfig]
    labels: typing.Dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: typing.List[NetworkInterface]
    postKeyRevocationActionType: typing_extensions.Literal[
        "NOOP", "POST_KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED", "SHUTDOWN"
    ]
    scheduling: Scheduling
    serviceAccounts: typing.List[ServiceAccount]
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
    selfLinkWithId: str
    selfManaged: SslCertificateSelfManagedSslCertificate
    subjectAlternativeNames: typing.List[str]
    type: typing_extensions.Literal["MANAGED", "SELF_MANAGED", "TYPE_UNSPECIFIED"]

@typing.type_check_only
class SslCertificateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SslCertificateList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[SslCertificate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SslCertificateManagedSslCertificate(typing_extensions.TypedDict, total=False):
    domainStatus: typing.Dict[str, typing.Any]
    domains: typing.List[str]
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
    sslCertificates: typing.List[SslCertificate]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[SslPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SslPoliciesListAvailableFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: typing.List[str]

@typing.type_check_only
class SslPolicy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    customFeatures: typing.List[str]
    description: str
    enabledFeatures: typing.List[str]
    fingerprint: str
    id: str
    kind: str
    minTlsVersion: typing_extensions.Literal["TLS_1_0", "TLS_1_1", "TLS_1_2"]
    name: str
    profile: typing_extensions.Literal["COMPATIBLE", "CUSTOM", "MODERN", "RESTRICTED"]
    selfLink: str
    selfLinkWithId: str
    tlsSettings: ServerTlsSettings
    warnings: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class SslPolicyReference(typing_extensions.TypedDict, total=False):
    sslPolicy: str

@typing.type_check_only
class StatefulPolicy(typing_extensions.TypedDict, total=False):
    preservedState: StatefulPolicyPreservedState

@typing.type_check_only
class StatefulPolicyPreservedState(typing_extensions.TypedDict, total=False):
    disks: typing.Dict[str, typing.Any]
    externalIPs: typing.Dict[str, typing.Any]
    internalIPs: typing.Dict[str, typing.Any]

@typing.type_check_only
class StatefulPolicyPreservedStateDiskDevice(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

@typing.type_check_only
class StatefulPolicyPreservedStateNetworkIp(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

@typing.type_check_only
class Subnetwork(typing_extensions.TypedDict, total=False):
    aggregationInterval: typing_extensions.Literal[
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
    ipCidrRange: str
    ipv6AccessType: typing_extensions.Literal[
        "EXTERNAL", "INTERNAL", "UNSPECIFIED_IPV6_ACCESS_TYPE"
    ]
    ipv6CidrRange: str
    kind: str
    logConfig: SubnetworkLogConfig
    metadata: typing_extensions.Literal["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]
    name: str
    network: str
    privateIpGoogleAccess: bool
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "DISABLE_GOOGLE_ACCESS",
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE_FOR_SERVICE_ACCOUNTS",
    ]
    privateIpv6GoogleAccessServiceAccounts: typing.List[str]
    purpose: typing_extensions.Literal[
        "AGGREGATE",
        "CLOUD_EXTENSION",
        "INTERNAL_HTTPS_LOAD_BALANCER",
        "PRIVATE",
        "PRIVATE_RFC_1918",
        "PRIVATE_SERVICE_CONNECT",
    ]
    region: str
    role: typing_extensions.Literal["ACTIVE", "BACKUP"]
    secondaryIpRanges: typing.List[SubnetworkSecondaryRange]
    selfLink: str
    selfLinkWithId: str
    stackType: typing_extensions.Literal[
        "IPV4_IPV6", "IPV4_ONLY", "UNSPECIFIED_STACK_TYPE"
    ]
    state: typing_extensions.Literal["DRAINING", "READY"]
    vlans: typing.List[int]

@typing.type_check_only
class SubnetworkAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SubnetworkList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Subnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    metadataFields: typing.List[str]

@typing.type_check_only
class SubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class SubnetworksExpandIpCidrRangeRequest(typing_extensions.TypedDict, total=False):
    ipCidrRange: str

@typing.type_check_only
class SubnetworksScopedList(typing_extensions.TypedDict, total=False):
    subnetworks: typing.List[Subnetwork]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class SubnetworksSetPrivateIpGoogleAccessRequest(
    typing_extensions.TypedDict, total=False
):
    privateIpGoogleAccess: bool

@typing.type_check_only
class Subsetting(typing_extensions.TypedDict, total=False):
    policy: typing_extensions.Literal["CONSISTENT_HASH_SUBSETTING", "NONE"]

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
    items: typing.List[str]

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
    items: typing.List[TargetGrpcProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetHttpProxies: typing.List[TargetHttpProxy]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    httpFilters: typing.List[str]
    id: str
    kind: str
    name: str
    proxyBind: bool
    region: str
    selfLink: str
    selfLinkWithId: str
    urlMap: str

@typing.type_check_only
class TargetHttpProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetHttpProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetHttpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetHttpsProxies: typing.List[TargetHttpsProxy]
    warning: typing.Dict[str, typing.Any]

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
    sslCertificates: typing.List[str]

@typing.type_check_only
class TargetHttpsProxy(typing_extensions.TypedDict, total=False):
    authentication: str
    authorization: str
    authorizationPolicy: str
    certificateMap: str
    creationTimestamp: str
    description: str
    fingerprint: str
    httpFilters: typing.List[str]
    id: str
    kind: str
    name: str
    proxyBind: bool
    quicOverride: typing_extensions.Literal["DISABLE", "ENABLE", "NONE"]
    region: str
    selfLink: str
    selfLinkWithId: str
    serverTlsPolicy: str
    sslCertificates: typing.List[str]
    sslPolicy: str
    urlMap: str

@typing.type_check_only
class TargetHttpsProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetHttpsProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetHttpsProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    selfLink: str
    selfLinkWithId: str
    zone: str

@typing.type_check_only
class TargetInstanceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetInstanceList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetInstance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetInstancesScopedList(typing_extensions.TypedDict, total=False):
    targetInstances: typing.List[TargetInstance]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetPool(typing_extensions.TypedDict, total=False):
    backupPool: str
    creationTimestamp: str
    description: str
    failoverRatio: float
    healthChecks: typing.List[str]
    id: str
    instances: typing.List[str]
    kind: str
    name: str
    region: str
    selfLink: str
    selfLinkWithId: str
    sessionAffinity: typing_extensions.Literal[
        "CLIENT_IP",
        "CLIENT_IP_NO_DESTINATION",
        "CLIENT_IP_PORT_PROTO",
        "CLIENT_IP_PROTO",
        "GENERATED_COOKIE",
        "HEADER_FIELD",
        "HTTP_COOKIE",
        "NONE",
    ]

@typing.type_check_only
class TargetPoolAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetPoolInstanceHealth(typing_extensions.TypedDict, total=False):
    healthStatus: typing.List[HealthStatus]
    kind: str

@typing.type_check_only
class TargetPoolList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetPool]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetPoolsAddHealthCheckRequest(typing_extensions.TypedDict, total=False):
    healthChecks: typing.List[HealthCheckReference]

@typing.type_check_only
class TargetPoolsAddInstanceRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

@typing.type_check_only
class TargetPoolsRemoveHealthCheckRequest(typing_extensions.TypedDict, total=False):
    healthChecks: typing.List[HealthCheckReference]

@typing.type_check_only
class TargetPoolsRemoveInstanceRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

@typing.type_check_only
class TargetPoolsScopedList(typing_extensions.TypedDict, total=False):
    targetPools: typing.List[TargetPool]
    warning: typing.Dict[str, typing.Any]

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
    sslCertificates: typing.List[str]

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
    sslCertificates: typing.List[str]
    sslPolicy: str

@typing.type_check_only
class TargetSslProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetSslProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    selfLink: str
    service: str

@typing.type_check_only
class TargetTcpProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetTcpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGateway(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    forwardingRules: typing.List[str]
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    network: str
    region: str
    selfLink: str
    status: typing_extensions.Literal["CREATING", "DELETING", "FAILED", "READY"]
    tunnels: typing.List[str]

@typing.type_check_only
class TargetVpnGatewayAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewayList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TargetVpnGatewaysScopedList(typing_extensions.TypedDict, total=False):
    targetVpnGateways: typing.List[TargetVpnGateway]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class TestFailure(typing_extensions.TypedDict, total=False):
    actualOutputUrl: str
    actualRedirectResponseCode: int
    actualService: str
    expectedOutputUrl: str
    expectedRedirectResponseCode: int
    expectedService: str
    headers: typing.List[UrlMapTestHeader]
    host: str
    path: str

@typing.type_check_only
class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TlsCertificateContext(typing_extensions.TypedDict, total=False):
    certificatePaths: TlsCertificatePaths
    certificateSource: typing_extensions.Literal["INVALID", "USE_PATH", "USE_SDS"]
    sdsConfig: SdsConfig

@typing.type_check_only
class TlsCertificatePaths(typing_extensions.TypedDict, total=False):
    certificatePath: str
    privateKeyPath: str

@typing.type_check_only
class TlsContext(typing_extensions.TypedDict, total=False):
    certificateContext: TlsCertificateContext
    validationContext: TlsValidationContext

@typing.type_check_only
class TlsValidationContext(typing_extensions.TypedDict, total=False):
    certificatePath: str
    sdsConfig: SdsConfig
    validationSource: typing_extensions.Literal["INVALID", "USE_PATH", "USE_SDS"]

@typing.type_check_only
class UDPHealthCheck(typing_extensions.TypedDict, total=False):
    port: int
    portName: str
    request: str
    response: str

@typing.type_check_only
class UpcomingMaintenance(typing_extensions.TypedDict, total=False):
    date: str
    startTimeWindow: UpcomingMaintenanceTimeWindow
    time: str
    type: typing_extensions.Literal["SCHEDULED", "UNKNOWN_TYPE", "UNSCHEDULED"]

@typing.type_check_only
class UpcomingMaintenanceTimeWindow(typing_extensions.TypedDict, total=False):
    earliest: str
    latest: str

@typing.type_check_only
class UrlMap(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    defaultRouteAction: HttpRouteAction
    defaultService: str
    defaultUrlRedirect: HttpRedirectAction
    description: str
    fingerprint: str
    headerAction: HttpHeaderAction
    hostRules: typing.List[HostRule]
    id: str
    kind: str
    name: str
    pathMatchers: typing.List[PathMatcher]
    region: str
    selfLink: str
    tests: typing.List[UrlMapTest]

@typing.type_check_only
class UrlMapList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[UrlMap]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class UrlMapReference(typing_extensions.TypedDict, total=False):
    urlMap: str

@typing.type_check_only
class UrlMapTest(typing_extensions.TypedDict, total=False):
    backendServiceWeight: int
    description: str
    expectedOutputUrl: str
    expectedRedirectResponseCode: int
    expectedUrlRedirect: str
    headers: typing.List[UrlMapTestHeader]
    host: str
    path: str
    service: str

@typing.type_check_only
class UrlMapTestHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class UrlMapValidationResult(typing_extensions.TypedDict, total=False):
    loadErrors: typing.List[str]
    loadSucceeded: bool
    testFailures: typing.List[TestFailure]
    testPassed: bool

@typing.type_check_only
class UrlMapsAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class UrlMapsScopedList(typing_extensions.TypedDict, total=False):
    urlMaps: typing.List[UrlMap]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class UrlMapsValidateRequest(typing_extensions.TypedDict, total=False):
    resource: UrlMap

@typing.type_check_only
class UrlMapsValidateResponse(typing_extensions.TypedDict, total=False):
    result: UrlMapValidationResult

@typing.type_check_only
class UrlRewrite(typing_extensions.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str

@typing.type_check_only
class UsableSubnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str
    secondaryIpRanges: typing.List[UsableSubnetworkSecondaryRange]
    subnetwork: str

@typing.type_check_only
class UsableSubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

@typing.type_check_only
class UsableSubnetworksAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[UsableSubnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class UsageExportLocation(typing_extensions.TypedDict, total=False):
    bucketName: str
    reportNamePrefix: str

@typing.type_check_only
class VmEndpointNatMappings(typing_extensions.TypedDict, total=False):
    instanceName: str
    interfaceNatMappings: typing.List[VmEndpointNatMappingsInterfaceNatMappings]

@typing.type_check_only
class VmEndpointNatMappingsInterfaceNatMappings(
    typing_extensions.TypedDict, total=False
):
    drainNatIpPortRanges: typing.List[str]
    natIpPortRanges: typing.List[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    ruleMappings: typing.List[VmEndpointNatMappingsInterfaceNatMappingsNatRuleMappings]
    sourceAliasIpRange: str
    sourceVirtualIp: str

@typing.type_check_only
class VmEndpointNatMappingsInterfaceNatMappingsNatRuleMappings(
    typing_extensions.TypedDict, total=False
):
    drainNatIpPortRanges: typing.List[str]
    natIpPortRanges: typing.List[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    ruleNumber: int

@typing.type_check_only
class VmEndpointNatMappingsList(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    nextPageToken: str
    result: typing.List[VmEndpointNatMappings]
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class VpnGateway(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    name: str
    network: str
    region: str
    selfLink: str
    vpnInterfaces: typing.List[VpnGatewayVpnGatewayInterface]

@typing.type_check_only
class VpnGatewayAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[VpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class VpnGatewayStatus(typing_extensions.TypedDict, total=False):
    vpnConnections: typing.List[VpnGatewayStatusVpnConnection]

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
    tunnels: typing.List[VpnGatewayStatusTunnel]

@typing.type_check_only
class VpnGatewayVpnGatewayInterface(typing_extensions.TypedDict, total=False):
    id: int
    interconnectAttachment: str
    ipAddress: str

@typing.type_check_only
class VpnGatewaysGetStatusResponse(typing_extensions.TypedDict, total=False):
    result: VpnGatewayStatus

@typing.type_check_only
class VpnGatewaysScopedList(typing_extensions.TypedDict, total=False):
    vpnGateways: typing.List[VpnGateway]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class VpnTunnel(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    detailedStatus: str
    id: str
    ikeVersion: int
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    localTrafficSelector: typing.List[str]
    name: str
    peerExternalGateway: str
    peerExternalGatewayInterface: int
    peerGcpGateway: str
    peerIp: str
    region: str
    remoteTrafficSelector: typing.List[str]
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
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[VpnTunnel]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class VpnTunnelsScopedList(typing_extensions.TypedDict, total=False):
    vpnTunnels: typing.List[VpnTunnel]
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class WafExpressionSet(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    expressions: typing.List[WafExpressionSetExpression]
    id: str

@typing.type_check_only
class WafExpressionSetExpression(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class WeightedBackendService(typing_extensions.TypedDict, total=False):
    backendService: str
    headerAction: HttpHeaderAction
    weight: int

@typing.type_check_only
class XpnHostList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Project]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class XpnResourceId(typing_extensions.TypedDict, total=False):
    id: str
    type: typing_extensions.Literal["PROJECT", "XPN_RESOURCE_TYPE_UNSPECIFIED"]

@typing.type_check_only
class Zone(typing_extensions.TypedDict, total=False):
    availableCpuPlatforms: typing.List[str]
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
class ZoneInstantSnapshotsExportRequest(typing_extensions.TypedDict, total=False):
    exportParams: InstantSnapshotExportParams

@typing.type_check_only
class ZoneList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Zone]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

@typing.type_check_only
class ZoneSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class ZoneSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy
