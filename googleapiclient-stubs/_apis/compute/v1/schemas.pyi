import typing

import typing_extensions

class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    acceleratorCount: int
    acceleratorType: str

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

class AcceleratorTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class AcceleratorTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[AcceleratorType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class AcceleratorTypesScopedList(typing_extensions.TypedDict, total=False):
    acceleratorTypes: typing.List[AcceleratorType]
    warning: typing.Dict[str, typing.Any]

class AccessConfig(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    natIP: str
    networkTier: typing_extensions.Literal["PREMIUM", "STANDARD"]
    publicPtrDomainName: str
    setPublicPtr: bool
    type: typing_extensions.Literal["ONE_TO_ONE_NAT"]

class Address(typing_extensions.TypedDict, total=False):
    address: str
    addressType: typing_extensions.Literal["EXTERNAL", "INTERNAL", "UNSPECIFIED_TYPE"]
    creationTimestamp: str
    description: str
    id: str
    ipVersion: typing_extensions.Literal["IPV4", "IPV6", "UNSPECIFIED_VERSION"]
    kind: str
    name: str
    network: str
    networkTier: typing_extensions.Literal["PREMIUM", "STANDARD"]
    prefixLength: int
    purpose: typing_extensions.Literal[
        "DNS_RESOLVER",
        "GCE_ENDPOINT",
        "NAT_AUTO",
        "SHARED_LOADBALANCER_VIP",
        "VPC_PEERING",
    ]
    region: str
    selfLink: str
    status: typing_extensions.Literal["IN_USE", "RESERVED", "RESERVING"]
    subnetwork: str
    users: typing.List[str]

class AddressAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class AddressList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Address]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class AddressesScopedList(typing_extensions.TypedDict, total=False):
    addresses: typing.List[Address]
    warning: typing.Dict[str, typing.Any]

class AliasIpRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    subnetworkRangeName: str

class AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    interface: typing_extensions.Literal["NVME", "SCSI"]

class AllocationSpecificSKUAllocationReservedInstanceProperties(
    typing_extensions.TypedDict, total=False
):
    guestAccelerators: typing.List[AcceleratorConfig]
    localSsds: typing.List[
        AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk
    ]
    machineType: str
    minCpuPlatform: str

class AllocationSpecificSKUReservation(typing_extensions.TypedDict, total=False):
    count: str
    inUseCount: str
    instanceProperties: AllocationSpecificSKUAllocationReservedInstanceProperties

class AttachedDisk(typing_extensions.TypedDict, total=False):
    autoDelete: bool
    boot: bool
    deviceName: str
    diskEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    guestOsFeatures: typing.List[GuestOsFeature]
    index: int
    initializeParams: AttachedDiskInitializeParams
    interface: typing_extensions.Literal["NVME", "SCSI"]
    kind: str
    licenses: typing.List[str]
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    shieldedInstanceInitialState: InitialStateConfig
    source: str
    type: typing_extensions.Literal["PERSISTENT", "SCRATCH"]

class AttachedDiskInitializeParams(typing_extensions.TypedDict, total=False):
    description: str
    diskName: str
    diskSizeGb: str
    diskType: str
    labels: typing.Dict[str, typing.Any]
    onUpdateAction: typing_extensions.Literal[
        "RECREATE_DISK", "RECREATE_DISK_IF_SOURCE_CHANGED", "USE_EXISTING_DISK"
    ]
    resourcePolicies: typing.List[str]
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    exemptedMembers: typing.List[str]
    service: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool
    logType: typing_extensions.Literal[
        "ADMIN_READ", "DATA_READ", "DATA_WRITE", "LOG_TYPE_UNSPECIFIED"
    ]

class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: typing_extensions.Literal[
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
        "PERMISSION_TYPE_UNSPECIFIED",
    ]

class Autoscaler(typing_extensions.TypedDict, total=False):
    autoscalingPolicy: AutoscalingPolicy
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    recommendedSize: int
    region: str
    selfLink: str
    status: typing_extensions.Literal["ACTIVE", "DELETING", "ERROR", "PENDING"]
    statusDetails: typing.List[AutoscalerStatusDetails]
    target: str
    zone: str

class AutoscalerAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class AutoscalerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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

class AutoscalersScopedList(typing_extensions.TypedDict, total=False):
    autoscalers: typing.List[Autoscaler]
    warning: typing.Dict[str, typing.Any]

class AutoscalingPolicy(typing_extensions.TypedDict, total=False):
    coolDownPeriodSec: int
    cpuUtilization: AutoscalingPolicyCpuUtilization
    customMetricUtilizations: typing.List[AutoscalingPolicyCustomMetricUtilization]
    loadBalancingUtilization: AutoscalingPolicyLoadBalancingUtilization
    maxNumReplicas: int
    minNumReplicas: int
    mode: typing_extensions.Literal["OFF", "ON", "ONLY_SCALE_OUT", "ONLY_UP"]
    scaleInControl: AutoscalingPolicyScaleInControl

class AutoscalingPolicyCpuUtilization(typing_extensions.TypedDict, total=False):
    utilizationTarget: float

class AutoscalingPolicyCustomMetricUtilization(
    typing_extensions.TypedDict, total=False
):
    metric: str
    utilizationTarget: float
    utilizationTargetType: typing_extensions.Literal[
        "DELTA_PER_MINUTE", "DELTA_PER_SECOND", "GAUGE"
    ]

class AutoscalingPolicyLoadBalancingUtilization(
    typing_extensions.TypedDict, total=False
):
    utilizationTarget: float

class AutoscalingPolicyScaleInControl(typing_extensions.TypedDict, total=False):
    maxScaledInReplicas: FixedOrPercent
    timeWindowSec: int

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

class BackendBucket(typing_extensions.TypedDict, total=False):
    bucketName: str
    cdnPolicy: BackendBucketCdnPolicy
    creationTimestamp: str
    description: str
    enableCdn: bool
    id: str
    kind: str
    name: str
    selfLink: str

class BackendBucketCdnPolicy(typing_extensions.TypedDict, total=False):
    signedUrlCacheMaxAgeSec: str
    signedUrlKeyNames: typing.List[str]

class BackendBucketList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[BackendBucket]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class BackendService(typing_extensions.TypedDict, total=False):
    affinityCookieTtlSec: int
    backends: typing.List[Backend]
    cdnPolicy: BackendServiceCdnPolicy
    circuitBreakers: CircuitBreakers
    connectionDraining: ConnectionDraining
    consistentHash: ConsistentHashLoadBalancerSettings
    creationTimestamp: str
    customRequestHeaders: typing.List[str]
    description: str
    enableCDN: bool
    failoverPolicy: BackendServiceFailoverPolicy
    fingerprint: str
    healthChecks: typing.List[str]
    iap: BackendServiceIAP
    id: str
    kind: str
    loadBalancingScheme: typing_extensions.Literal[
        "EXTERNAL",
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
    name: str
    network: str
    outlierDetection: OutlierDetection
    port: int
    portName: str
    protocol: typing_extensions.Literal[
        "GRPC", "HTTP", "HTTP2", "HTTPS", "SSL", "TCP", "UDP"
    ]
    region: str
    securityPolicy: str
    selfLink: str
    sessionAffinity: typing_extensions.Literal[
        "CLIENT_IP",
        "CLIENT_IP_PORT_PROTO",
        "CLIENT_IP_PROTO",
        "GENERATED_COOKIE",
        "HEADER_FIELD",
        "HTTP_COOKIE",
        "NONE",
    ]
    timeoutSec: int

class BackendServiceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class BackendServiceCdnPolicy(typing_extensions.TypedDict, total=False):
    cacheKeyPolicy: CacheKeyPolicy
    signedUrlCacheMaxAgeSec: str
    signedUrlKeyNames: typing.List[str]

class BackendServiceFailoverPolicy(typing_extensions.TypedDict, total=False):
    disableConnectionDrainOnFailover: bool
    dropTrafficIfUnhealthy: bool
    failoverRatio: float

class BackendServiceGroupHealth(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    healthStatus: typing.List[HealthStatus]
    kind: str

class BackendServiceIAP(typing_extensions.TypedDict, total=False):
    enabled: bool
    oauth2ClientId: str
    oauth2ClientSecret: str
    oauth2ClientSecretSha256: str

class BackendServiceList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[BackendService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class BackendServiceLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    sampleRate: float

class BackendServiceReference(typing_extensions.TypedDict, total=False):
    backendService: str

class BackendServicesScopedList(typing_extensions.TypedDict, total=False):
    backendServices: typing.List[BackendService]
    warning: typing.Dict[str, typing.Any]

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    members: typing.List[str]
    role: str

class CacheInvalidationRule(typing_extensions.TypedDict, total=False):
    host: str
    path: str

class CacheKeyPolicy(typing_extensions.TypedDict, total=False):
    includeHost: bool
    includeProtocol: bool
    includeQueryString: bool
    queryStringBlacklist: typing.List[str]
    queryStringWhitelist: typing.List[str]

class CircuitBreakers(typing_extensions.TypedDict, total=False):
    maxConnections: int
    maxPendingRequests: int
    maxRequests: int
    maxRequestsPerConnection: int
    maxRetries: int

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
    startTimestamp: str
    status: typing_extensions.Literal["ACTIVE", "CREATING", "EXPIRED", "NOT_YET_ACTIVE"]
    statusMessage: str

class CommitmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class CommitmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Commitment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class CommitmentsScopedList(typing_extensions.TypedDict, total=False):
    commitments: typing.List[Commitment]
    warning: typing.Dict[str, typing.Any]

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

class ConfidentialInstanceConfig(typing_extensions.TypedDict, total=False):
    enableConfidentialCompute: bool

class ConnectionDraining(typing_extensions.TypedDict, total=False):
    drainingTimeoutSec: int

class ConsistentHashLoadBalancerSettings(typing_extensions.TypedDict, total=False):
    httpCookie: ConsistentHashLoadBalancerSettingsHttpCookie
    httpHeaderName: str
    minimumRingSize: str

class ConsistentHashLoadBalancerSettingsHttpCookie(
    typing_extensions.TypedDict, total=False
):
    name: str
    path: str
    ttl: Duration

class CorsPolicy(typing_extensions.TypedDict, total=False):
    allowCredentials: bool
    allowHeaders: typing.List[str]
    allowMethods: typing.List[str]
    allowOriginRegexes: typing.List[str]
    allowOrigins: typing.List[str]
    disabled: bool
    exposeHeaders: typing.List[str]
    maxAge: int

class CustomerEncryptionKey(typing_extensions.TypedDict, total=False):
    kmsKeyName: str
    kmsKeyServiceAccount: str
    rawKey: str
    sha256: str

class CustomerEncryptionKeyProtectedDisk(typing_extensions.TypedDict, total=False):
    diskEncryptionKey: CustomerEncryptionKey
    source: str

class DeprecationStatus(typing_extensions.TypedDict, total=False):
    deleted: str
    deprecated: str
    obsolete: str
    replacement: str
    state: typing_extensions.Literal["ACTIVE", "DELETED", "DEPRECATED", "OBSOLETE"]

class Disk(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    diskEncryptionKey: CustomerEncryptionKey
    guestOsFeatures: typing.List[GuestOsFeature]
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    lastAttachTimestamp: str
    lastDetachTimestamp: str
    licenseCodes: typing.List[str]
    licenses: typing.List[str]
    name: str
    options: str
    physicalBlockSizeBytes: str
    region: str
    replicaZones: typing.List[str]
    resourcePolicies: typing.List[str]
    selfLink: str
    sizeGb: str
    sourceDisk: str
    sourceDiskId: str
    sourceImage: str
    sourceImageEncryptionKey: CustomerEncryptionKey
    sourceImageId: str
    sourceSnapshot: str
    sourceSnapshotEncryptionKey: CustomerEncryptionKey
    sourceSnapshotId: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "FAILED", "READY", "RESTORING"
    ]
    type: str
    users: typing.List[str]
    zone: str

class DiskAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

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

class DiskList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Disk]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class DiskMoveRequest(typing_extensions.TypedDict, total=False):
    destinationZone: str
    targetDisk: str

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

class DiskTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class DiskTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class DiskTypesScopedList(typing_extensions.TypedDict, total=False):
    diskTypes: typing.List[DiskType]
    warning: typing.Dict[str, typing.Any]

class DisksAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

class DisksRemoveResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

class DisksResizeRequest(typing_extensions.TypedDict, total=False):
    sizeGb: str

class DisksScopedList(typing_extensions.TypedDict, total=False):
    disks: typing.List[Disk]
    warning: typing.Dict[str, typing.Any]

class DisplayDevice(typing_extensions.TypedDict, total=False):
    enableDisplay: bool

class DistributionPolicy(typing_extensions.TypedDict, total=False):
    zones: typing.List[DistributionPolicyZoneConfiguration]

class DistributionPolicyZoneConfiguration(typing_extensions.TypedDict, total=False):
    zone: str

class Duration(typing_extensions.TypedDict, total=False):
    nanos: int
    seconds: str

class ExchangedPeeringRoute(typing_extensions.TypedDict, total=False):
    destRange: str
    imported: bool
    nextHopRegion: str
    priority: int
    type: typing_extensions.Literal[
        "DYNAMIC_PEERING_ROUTE", "STATIC_PEERING_ROUTE", "SUBNET_PEERING_ROUTE"
    ]

class ExchangedPeeringRoutesList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[ExchangedPeeringRoute]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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

class ExternalVpnGatewayInterface(typing_extensions.TypedDict, total=False):
    id: int
    ipAddress: str

class ExternalVpnGatewayList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: typing.List[ExternalVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class FileContentBuffer(typing_extensions.TypedDict, total=False):
    content: str
    fileType: typing_extensions.Literal["BIN", "UNDEFINED", "X509"]

class Firewall(typing_extensions.TypedDict, total=False):
    allowed: typing.List[typing.Dict[str, typing.Any]]
    creationTimestamp: str
    denied: typing.List[typing.Dict[str, typing.Any]]
    description: str
    destinationRanges: typing.List[str]
    direction: typing_extensions.Literal["EGRESS", "INGRESS"]
    disabled: bool
    id: str
    kind: str
    logConfig: FirewallLogConfig
    name: str
    network: str
    priority: int
    selfLink: str
    sourceRanges: typing.List[str]
    sourceServiceAccounts: typing.List[str]
    sourceTags: typing.List[str]
    targetServiceAccounts: typing.List[str]
    targetTags: typing.List[str]

class FirewallList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Firewall]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class FirewallLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    metadata: typing_extensions.Literal["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]

class FixedOrPercent(typing_extensions.TypedDict, total=False):
    calculated: int
    fixed: int
    percent: int

class ForwardingRule(typing_extensions.TypedDict, total=False):
    IPAddress: str
    IPProtocol: typing_extensions.Literal["AH", "ESP", "ICMP", "SCTP", "TCP", "UDP"]
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
    loadBalancingScheme: typing_extensions.Literal[
        "EXTERNAL", "INTERNAL", "INTERNAL_MANAGED", "INTERNAL_SELF_MANAGED", "INVALID"
    ]
    metadataFilters: typing.List[MetadataFilter]
    name: str
    network: str
    networkTier: typing_extensions.Literal["PREMIUM", "STANDARD"]
    portRange: str
    ports: typing.List[str]
    region: str
    selfLink: str
    serviceLabel: str
    serviceName: str
    subnetwork: str
    target: str

class ForwardingRuleAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class ForwardingRuleList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[ForwardingRule]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class ForwardingRuleReference(typing_extensions.TypedDict, total=False):
    forwardingRule: str

class ForwardingRulesScopedList(typing_extensions.TypedDict, total=False):
    forwardingRules: typing.List[ForwardingRule]
    warning: typing.Dict[str, typing.Any]

class GRPCHealthCheck(typing_extensions.TypedDict, total=False):
    grpcServiceName: str
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]

class GlobalNetworkEndpointGroupsAttachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

class GlobalNetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

class GlobalSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy

class GuestAttributes(typing_extensions.TypedDict, total=False):
    kind: str
    queryPath: str
    queryValue: GuestAttributesValue
    selfLink: str
    variableKey: str
    variableValue: str

class GuestAttributesEntry(typing_extensions.TypedDict, total=False):
    key: str
    namespace: str
    value: str

class GuestAttributesValue(typing_extensions.TypedDict, total=False):
    items: typing.List[GuestAttributesEntry]

class GuestOsFeature(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "FEATURE_TYPE_UNSPECIFIED",
        "MULTI_IP_SUBNET",
        "SECURE_BOOT",
        "SEV_CAPABLE",
        "UEFI_COMPATIBLE",
        "VIRTIO_SCSI_MULTIQUEUE",
        "WINDOWS",
    ]

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
    name: str
    region: str
    selfLink: str
    sslHealthCheck: SSLHealthCheck
    tcpHealthCheck: TCPHealthCheck
    timeoutSec: int
    type: typing_extensions.Literal[
        "GRPC", "HTTP", "HTTP2", "HTTPS", "INVALID", "SSL", "TCP"
    ]
    unhealthyThreshold: int

class HealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class HealthCheckReference(typing_extensions.TypedDict, total=False):
    healthCheck: str

class HealthCheckService(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    healthChecks: typing.List[str]
    healthStatusAggregationPolicy: typing_extensions.Literal["AND", "NO_AGGREGATION"]
    id: str
    kind: str
    name: str
    networkEndpointGroups: typing.List[str]
    notificationEndpoints: typing.List[str]
    region: str
    selfLink: str

class HealthCheckServiceReference(typing_extensions.TypedDict, total=False):
    healthCheckService: str

class HealthCheckServicesList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HealthCheckService]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class HealthChecksAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class HealthChecksScopedList(typing_extensions.TypedDict, total=False):
    healthChecks: typing.List[HealthCheck]
    warning: typing.Dict[str, typing.Any]

class HealthStatus(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    healthState: typing_extensions.Literal["HEALTHY", "UNHEALTHY"]
    instance: str
    ipAddress: str
    port: int

class HealthStatusForNetworkEndpoint(typing_extensions.TypedDict, total=False):
    backendService: BackendServiceReference
    forwardingRule: ForwardingRuleReference
    healthCheck: HealthCheckReference
    healthCheckService: HealthCheckServiceReference
    healthState: typing_extensions.Literal[
        "DRAINING", "HEALTHY", "UNHEALTHY", "UNKNOWN"
    ]

class HostRule(typing_extensions.TypedDict, total=False):
    description: str
    hosts: typing.List[str]
    pathMatcher: str

class HttpFaultAbort(typing_extensions.TypedDict, total=False):
    httpStatus: int
    percentage: float

class HttpFaultDelay(typing_extensions.TypedDict, total=False):
    fixedDelay: Duration
    percentage: float

class HttpFaultInjection(typing_extensions.TypedDict, total=False):
    abort: HttpFaultAbort
    delay: HttpFaultDelay

class HttpHeaderAction(typing_extensions.TypedDict, total=False):
    requestHeadersToAdd: typing.List[HttpHeaderOption]
    requestHeadersToRemove: typing.List[str]
    responseHeadersToAdd: typing.List[HttpHeaderOption]
    responseHeadersToRemove: typing.List[str]

class HttpHeaderMatch(typing_extensions.TypedDict, total=False):
    exactMatch: str
    headerName: str
    invertMatch: bool
    prefixMatch: str
    presentMatch: bool
    rangeMatch: Int64RangeMatch
    regexMatch: str
    suffixMatch: str

class HttpHeaderOption(typing_extensions.TypedDict, total=False):
    headerName: str
    headerValue: str
    replace: bool

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

class HttpHealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HttpHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class HttpQueryParameterMatch(typing_extensions.TypedDict, total=False):
    exactMatch: str
    name: str
    presentMatch: bool
    regexMatch: str

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

class HttpRetryPolicy(typing_extensions.TypedDict, total=False):
    numRetries: int
    perTryTimeout: Duration
    retryConditions: typing.List[str]

class HttpRouteAction(typing_extensions.TypedDict, total=False):
    corsPolicy: CorsPolicy
    faultInjectionPolicy: HttpFaultInjection
    requestMirrorPolicy: RequestMirrorPolicy
    retryPolicy: HttpRetryPolicy
    timeout: Duration
    urlRewrite: UrlRewrite
    weightedBackendServices: typing.List[WeightedBackendService]

class HttpRouteRule(typing_extensions.TypedDict, total=False):
    description: str
    headerAction: HttpHeaderAction
    matchRules: typing.List[HttpRouteRuleMatch]
    priority: int
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

class HttpRouteRuleMatch(typing_extensions.TypedDict, total=False):
    fullPathMatch: str
    headerMatches: typing.List[HttpHeaderMatch]
    ignoreCase: bool
    metadataFilters: typing.List[MetadataFilter]
    prefixMatch: str
    queryParameterMatches: typing.List[HttpQueryParameterMatch]
    regexMatch: str

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

class HttpsHealthCheckList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[HttpsHealthCheck]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    storageLocations: typing.List[str]

class ImageList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Image]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InitialStateConfig(typing_extensions.TypedDict, total=False):
    dbs: typing.List[FileContentBuffer]
    dbxs: typing.List[FileContentBuffer]
    keks: typing.List[FileContentBuffer]
    pk: FileContentBuffer

class Instance(typing_extensions.TypedDict, total=False):
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    cpuPlatform: str
    creationTimestamp: str
    deletionProtection: bool
    description: str
    disks: typing.List[AttachedDisk]
    displayDevice: DisplayDevice
    fingerprint: str
    guestAccelerators: typing.List[AcceleratorConfig]
    hostname: str
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    name: str
    networkInterfaces: typing.List[NetworkInterface]
    privateIpv6GoogleAccess: typing_extensions.Literal[
        "ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE",
        "ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE",
        "INHERIT_FROM_SUBNETWORK",
    ]
    reservationAffinity: ReservationAffinity
    resourcePolicies: typing.List[str]
    scheduling: Scheduling
    selfLink: str
    serviceAccounts: typing.List[ServiceAccount]
    shieldedInstanceConfig: ShieldedInstanceConfig
    shieldedInstanceIntegrityPolicy: ShieldedInstanceIntegrityPolicy
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
    zone: str

class InstanceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

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
    size: int
    subnetwork: str
    zone: str

class InstanceGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class InstanceGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InstanceGroupManager(typing_extensions.TypedDict, total=False):
    autoHealingPolicies: typing.List[InstanceGroupManagerAutoHealingPolicy]
    baseInstanceName: str
    creationTimestamp: str
    currentActions: InstanceGroupManagerActionsSummary
    description: str
    distributionPolicy: DistributionPolicy
    fingerprint: str
    id: str
    instanceGroup: str
    instanceTemplate: str
    kind: str
    name: str
    namedPorts: typing.List[NamedPort]
    region: str
    selfLink: str
    statefulPolicy: StatefulPolicy
    status: InstanceGroupManagerStatus
    targetPools: typing.List[str]
    targetSize: int
    updatePolicy: InstanceGroupManagerUpdatePolicy
    versions: typing.List[InstanceGroupManagerVersion]
    zone: str

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

class InstanceGroupManagerAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class InstanceGroupManagerAutoHealingPolicy(typing_extensions.TypedDict, total=False):
    healthCheck: str
    initialDelaySec: int

class InstanceGroupManagerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InstanceGroupManagerStatus(typing_extensions.TypedDict, total=False):
    autoscaler: str
    isStable: bool
    stateful: InstanceGroupManagerStatusStateful
    versionTarget: InstanceGroupManagerStatusVersionTarget

class InstanceGroupManagerStatusStateful(typing_extensions.TypedDict, total=False):
    hasStatefulConfig: bool
    perInstanceConfigs: InstanceGroupManagerStatusStatefulPerInstanceConfigs

class InstanceGroupManagerStatusStatefulPerInstanceConfigs(
    typing_extensions.TypedDict, total=False
):
    allEffective: bool

class InstanceGroupManagerStatusVersionTarget(typing_extensions.TypedDict, total=False):
    isReached: bool

class InstanceGroupManagerUpdatePolicy(typing_extensions.TypedDict, total=False):
    instanceRedistributionType: typing_extensions.Literal["NONE", "PROACTIVE"]
    maxSurge: FixedOrPercent
    maxUnavailable: FixedOrPercent
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    replacementMethod: typing_extensions.Literal["RECREATE", "SUBSTITUTE"]
    type: typing_extensions.Literal["OPPORTUNISTIC", "PROACTIVE"]

class InstanceGroupManagerVersion(typing_extensions.TypedDict, total=False):
    instanceTemplate: str
    name: str
    targetSize: FixedOrPercent

class InstanceGroupManagersAbandonInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

class InstanceGroupManagersApplyUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]

class InstanceGroupManagersCreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[PerInstanceConfig]

class InstanceGroupManagersDeleteInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

class InstanceGroupManagersDeletePerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

class InstanceGroupManagersListErrorsResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[InstanceManagedByIgmError]
    nextPageToken: str

class InstanceGroupManagersListManagedInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    managedInstances: typing.List[ManagedInstance]
    nextPageToken: str

class InstanceGroupManagersListPerInstanceConfigsResp(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[PerInstanceConfig]
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

class InstanceGroupManagersPatchPerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

class InstanceGroupManagersRecreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

class InstanceGroupManagersScopedList(typing_extensions.TypedDict, total=False):
    instanceGroupManagers: typing.List[InstanceGroupManager]
    warning: typing.Dict[str, typing.Any]

class InstanceGroupManagersSetInstanceTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    instanceTemplate: str

class InstanceGroupManagersSetTargetPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    targetPools: typing.List[str]

class InstanceGroupManagersUpdatePerInstanceConfigsReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

class InstanceGroupsAddInstancesRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

class InstanceGroupsListInstances(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InstanceGroupsListInstancesRequest(typing_extensions.TypedDict, total=False):
    instanceState: typing_extensions.Literal["ALL", "RUNNING"]

class InstanceGroupsRemoveInstancesRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

class InstanceGroupsScopedList(typing_extensions.TypedDict, total=False):
    instanceGroups: typing.List[InstanceGroup]
    warning: typing.Dict[str, typing.Any]

class InstanceGroupsSetNamedPortsRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str
    namedPorts: typing.List[NamedPort]

class InstanceList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Instance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InstanceListReferrers(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Reference]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InstanceManagedByIgmError(typing_extensions.TypedDict, total=False):
    error: InstanceManagedByIgmErrorManagedInstanceError
    instanceActionDetails: InstanceManagedByIgmErrorInstanceActionDetails
    timestamp: str

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

class InstanceManagedByIgmErrorManagedInstanceError(
    typing_extensions.TypedDict, total=False
):
    code: str
    message: str

class InstanceMoveRequest(typing_extensions.TypedDict, total=False):
    destinationZone: str
    targetInstance: str

class InstanceProperties(typing_extensions.TypedDict, total=False):
    canIpForward: bool
    confidentialInstanceConfig: ConfidentialInstanceConfig
    description: str
    disks: typing.List[AttachedDisk]
    guestAccelerators: typing.List[AcceleratorConfig]
    labels: typing.Dict[str, typing.Any]
    machineType: str
    metadata: Metadata
    minCpuPlatform: str
    networkInterfaces: typing.List[NetworkInterface]
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
    tags: Tags

class InstanceReference(typing_extensions.TypedDict, total=False):
    instance: str

class InstanceTemplate(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    properties: InstanceProperties
    selfLink: str
    sourceInstance: str
    sourceInstanceParams: SourceInstanceParams

class InstanceTemplateList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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

class InstancesAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

class InstancesRemoveResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

class InstancesScopedList(typing_extensions.TypedDict, total=False):
    instances: typing.List[Instance]
    warning: typing.Dict[str, typing.Any]

class InstancesSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

class InstancesSetMachineResourcesRequest(typing_extensions.TypedDict, total=False):
    guestAccelerators: typing.List[AcceleratorConfig]

class InstancesSetMachineTypeRequest(typing_extensions.TypedDict, total=False):
    machineType: str

class InstancesSetMinCpuPlatformRequest(typing_extensions.TypedDict, total=False):
    minCpuPlatform: str

class InstancesSetServiceAccountRequest(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

class InstancesStartWithEncryptionKeyRequest(typing_extensions.TypedDict, total=False):
    disks: typing.List[CustomerEncryptionKeyProtectedDisk]

class Int64RangeMatch(typing_extensions.TypedDict, total=False):
    rangeEnd: str
    rangeStart: str

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
    state: typing_extensions.Literal["ACTIVE", "UNPROVISIONED"]

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
    description: str
    edgeAvailabilityDomain: typing_extensions.Literal[
        "AVAILABILITY_DOMAIN_1", "AVAILABILITY_DOMAIN_2", "AVAILABILITY_DOMAIN_ANY"
    ]
    googleReferenceId: str
    id: str
    interconnect: str
    kind: str
    name: str
    operationalStatus: typing_extensions.Literal["OS_ACTIVE", "OS_UNPROVISIONED"]
    pairingKey: str
    partnerAsn: str
    partnerMetadata: InterconnectAttachmentPartnerMetadata
    privateInterconnectInfo: InterconnectAttachmentPrivateInfo
    region: str
    router: str
    selfLink: str
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

class InterconnectAttachmentAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class InterconnectAttachmentList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InterconnectAttachment]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InterconnectAttachmentPartnerMetadata(typing_extensions.TypedDict, total=False):
    interconnectName: str
    partnerName: str
    portalUrl: str

class InterconnectAttachmentPrivateInfo(typing_extensions.TypedDict, total=False):
    tag8021q: int

class InterconnectAttachmentsScopedList(typing_extensions.TypedDict, total=False):
    interconnectAttachments: typing.List[InterconnectAttachment]
    warning: typing.Dict[str, typing.Any]

class InterconnectCircuitInfo(typing_extensions.TypedDict, total=False):
    customerDemarcId: str
    googleCircuitId: str
    googleDemarcId: str

class InterconnectDiagnostics(typing_extensions.TypedDict, total=False):
    arpCaches: typing.List[InterconnectDiagnosticsARPEntry]
    links: typing.List[InterconnectDiagnosticsLinkStatus]
    macAddress: str

class InterconnectDiagnosticsARPEntry(typing_extensions.TypedDict, total=False):
    ipAddress: str
    macAddress: str

class InterconnectDiagnosticsLinkLACPStatus(typing_extensions.TypedDict, total=False):
    googleSystemId: str
    neighborSystemId: str
    state: typing_extensions.Literal["ACTIVE", "DETACHED"]

class InterconnectDiagnosticsLinkOpticalPower(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "HIGH_ALARM", "HIGH_WARNING", "LOW_ALARM", "LOW_WARNING", "OK"
    ]
    value: float

class InterconnectDiagnosticsLinkStatus(typing_extensions.TypedDict, total=False):
    arpCaches: typing.List[InterconnectDiagnosticsARPEntry]
    circuitId: str
    googleDemarc: str
    lacpStatus: InterconnectDiagnosticsLinkLACPStatus
    receivingOpticalPower: InterconnectDiagnosticsLinkOpticalPower
    transmittingOpticalPower: InterconnectDiagnosticsLinkOpticalPower

class InterconnectList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Interconnect]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    status: typing_extensions.Literal["AVAILABLE", "CLOSED"]

class InterconnectLocationList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InterconnectLocation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class InterconnectLocationRegionInfo(typing_extensions.TypedDict, total=False):
    expectedRttMs: str
    locationPresence: typing_extensions.Literal[
        "GLOBAL", "LOCAL_REGION", "LP_GLOBAL", "LP_LOCAL_REGION"
    ]
    region: str

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

class InterconnectsGetDiagnosticsResponse(typing_extensions.TypedDict, total=False):
    result: InterconnectDiagnostics

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

class LicenseCodeLicenseAlias(typing_extensions.TypedDict, total=False):
    description: str
    selfLink: str

class LicenseResourceCommitment(typing_extensions.TypedDict, total=False):
    amount: str
    coresPerLicense: str
    license: str

class LicenseResourceRequirements(typing_extensions.TypedDict, total=False):
    minGuestCpuCount: int
    minMemoryMb: int

class LicensesListResponse(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[License]
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class LogConfig(typing_extensions.TypedDict, total=False):
    cloudAudit: LogConfigCloudAuditOptions
    counter: LogConfigCounterOptions
    dataAccess: LogConfigDataAccessOptions

class LogConfigCloudAuditOptions(typing_extensions.TypedDict, total=False):
    authorizationLoggingOptions: AuthorizationLoggingOptions
    logName: typing_extensions.Literal[
        "ADMIN_ACTIVITY", "DATA_ACCESS", "UNSPECIFIED_LOG_NAME"
    ]

class LogConfigCounterOptions(typing_extensions.TypedDict, total=False):
    customFields: typing.List[LogConfigCounterOptionsCustomField]
    field: str
    metric: str

class LogConfigCounterOptionsCustomField(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class LogConfigDataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: typing_extensions.Literal["LOG_FAIL_CLOSED", "LOG_MODE_UNSPECIFIED"]

class MachineType(typing_extensions.TypedDict, total=False):
    accelerators: typing.List[typing.Dict[str, typing.Any]]
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    guestCpus: int
    id: str
    imageSpaceGb: int
    isSharedCpu: bool
    kind: str
    maximumPersistentDisks: int
    maximumPersistentDisksSizeGb: str
    memoryMb: int
    name: str
    scratchDisks: typing.List[typing.Dict[str, typing.Any]]
    selfLink: str
    zone: str

class MachineTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class MachineTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[MachineType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class MachineTypesScopedList(typing_extensions.TypedDict, total=False):
    machineTypes: typing.List[MachineType]
    warning: typing.Dict[str, typing.Any]

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
    lastAttempt: ManagedInstanceLastAttempt
    preservedStateFromConfig: PreservedState
    preservedStateFromPolicy: PreservedState
    version: ManagedInstanceVersion

class ManagedInstanceInstanceHealth(typing_extensions.TypedDict, total=False):
    detailedHealthState: typing_extensions.Literal[
        "DRAINING", "HEALTHY", "TIMEOUT", "UNHEALTHY", "UNKNOWN"
    ]
    healthCheck: str

class ManagedInstanceLastAttempt(typing_extensions.TypedDict, total=False):
    errors: typing.Dict[str, typing.Any]

class ManagedInstanceVersion(typing_extensions.TypedDict, total=False):
    instanceTemplate: str
    name: str

class Metadata(typing_extensions.TypedDict, total=False):
    fingerprint: str
    items: typing.List[typing.Dict[str, typing.Any]]
    kind: str

class MetadataFilter(typing_extensions.TypedDict, total=False):
    filterLabels: typing.List[MetadataFilterLabelMatch]
    filterMatchCriteria: typing_extensions.Literal["MATCH_ALL", "MATCH_ANY", "NOT_SET"]

class MetadataFilterLabelMatch(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class NamedPort(typing_extensions.TypedDict, total=False):
    name: str
    port: int

class Network(typing_extensions.TypedDict, total=False):
    IPv4Range: str
    autoCreateSubnetworks: bool
    creationTimestamp: str
    description: str
    gatewayIPv4: str
    id: str
    kind: str
    mtu: int
    name: str
    peerings: typing.List[NetworkPeering]
    routingConfig: NetworkRoutingConfig
    selfLink: str
    subnetworks: typing.List[str]

class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    fqdn: str
    instance: str
    ipAddress: str
    port: int

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
    name: str
    network: str
    networkEndpointType: typing_extensions.Literal[
        "GCE_VM_IP_PORT",
        "INTERNET_FQDN_PORT",
        "INTERNET_IP_PORT",
        "NON_GCP_PRIVATE_IP_PORT",
        "SERVERLESS",
    ]
    region: str
    selfLink: str
    size: int
    subnetwork: str
    zone: str

class NetworkEndpointGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class NetworkEndpointGroupAppEngine(typing_extensions.TypedDict, total=False):
    service: str
    urlMask: str
    version: str

class NetworkEndpointGroupCloudFunction(typing_extensions.TypedDict, total=False):
    function: str
    urlMask: str

class NetworkEndpointGroupCloudRun(typing_extensions.TypedDict, total=False):
    service: str
    tag: str
    urlMask: str

class NetworkEndpointGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NetworkEndpointGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class NetworkEndpointGroupsAttachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

class NetworkEndpointGroupsDetachEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    networkEndpoints: typing.List[NetworkEndpoint]

class NetworkEndpointGroupsListEndpointsRequest(
    typing_extensions.TypedDict, total=False
):
    healthStatus: typing_extensions.Literal["SHOW", "SKIP"]

class NetworkEndpointGroupsListNetworkEndpoints(
    typing_extensions.TypedDict, total=False
):
    id: str
    items: typing.List[NetworkEndpointWithHealthStatus]
    kind: str
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

class NetworkEndpointGroupsScopedList(typing_extensions.TypedDict, total=False):
    networkEndpointGroups: typing.List[NetworkEndpointGroup]
    warning: typing.Dict[str, typing.Any]

class NetworkEndpointWithHealthStatus(typing_extensions.TypedDict, total=False):
    healths: typing.List[HealthStatusForNetworkEndpoint]
    networkEndpoint: NetworkEndpoint

class NetworkInterface(typing_extensions.TypedDict, total=False):
    accessConfigs: typing.List[AccessConfig]
    aliasIpRanges: typing.List[AliasIpRange]
    fingerprint: str
    ipv6Address: str
    kind: str
    name: str
    network: str
    networkIP: str
    subnetwork: str

class NetworkList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Network]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    state: typing_extensions.Literal["ACTIVE", "INACTIVE"]
    stateDetails: str

class NetworkRoutingConfig(typing_extensions.TypedDict, total=False):
    routingMode: typing_extensions.Literal["GLOBAL", "REGIONAL"]

class NetworksAddPeeringRequest(typing_extensions.TypedDict, total=False):
    autoCreateRoutes: bool
    name: str
    networkPeering: NetworkPeering
    peerNetwork: str

class NetworksRemovePeeringRequest(typing_extensions.TypedDict, total=False):
    name: str

class NetworksUpdatePeeringRequest(typing_extensions.TypedDict, total=False):
    networkPeering: NetworkPeering

class NodeGroup(typing_extensions.TypedDict, total=False):
    autoscalingPolicy: NodeGroupAutoscalingPolicy
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    maintenancePolicy: typing_extensions.Literal[
        "DEFAULT",
        "MAINTENANCE_POLICY_UNSPECIFIED",
        "MIGRATE_WITHIN_NODE_GROUP",
        "RESTART_IN_PLACE",
    ]
    name: str
    nodeTemplate: str
    selfLink: str
    size: int
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    zone: str

class NodeGroupAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class NodeGroupAutoscalingPolicy(typing_extensions.TypedDict, total=False):
    maxNodes: int
    minNodes: int
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "OFF", "ON", "ONLY_SCALE_OUT"]

class NodeGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class NodeGroupNode(typing_extensions.TypedDict, total=False):
    cpuOvercommitType: typing_extensions.Literal[
        "CPU_OVERCOMMIT_TYPE_UNSPECIFIED", "ENABLED", "NONE"
    ]
    instances: typing.List[str]
    name: str
    nodeType: str
    serverBinding: ServerBinding
    serverId: str
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "REPAIRING"
    ]

class NodeGroupsAddNodesRequest(typing_extensions.TypedDict, total=False):
    additionalNodeCount: int

class NodeGroupsDeleteNodesRequest(typing_extensions.TypedDict, total=False):
    nodes: typing.List[str]

class NodeGroupsListNodes(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeGroupNode]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class NodeGroupsScopedList(typing_extensions.TypedDict, total=False):
    nodeGroups: typing.List[NodeGroup]
    warning: typing.Dict[str, typing.Any]

class NodeGroupsSetNodeTemplateRequest(typing_extensions.TypedDict, total=False):
    nodeTemplate: str

class NodeTemplate(typing_extensions.TypedDict, total=False):
    cpuOvercommitType: typing_extensions.Literal[
        "CPU_OVERCOMMIT_TYPE_UNSPECIFIED", "ENABLED", "NONE"
    ]
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    nodeAffinityLabels: typing.Dict[str, typing.Any]
    nodeType: str
    nodeTypeFlexibility: NodeTemplateNodeTypeFlexibility
    region: str
    selfLink: str
    serverBinding: ServerBinding
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]
    statusMessage: str

class NodeTemplateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class NodeTemplateList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeTemplate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class NodeTemplateNodeTypeFlexibility(typing_extensions.TypedDict, total=False):
    cpus: str
    localSsd: str
    memory: str

class NodeTemplatesScopedList(typing_extensions.TypedDict, total=False):
    nodeTemplates: typing.List[NodeTemplate]
    warning: typing.Dict[str, typing.Any]

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

class NodeTypeAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class NodeTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NodeType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class NodeTypesScopedList(typing_extensions.TypedDict, total=False):
    nodeTypes: typing.List[NodeType]
    warning: typing.Dict[str, typing.Any]

class NotificationEndpoint(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    grpcSettings: NotificationEndpointGrpcSettings
    id: str
    kind: str
    name: str
    region: str
    selfLink: str

class NotificationEndpointGrpcSettings(typing_extensions.TypedDict, total=False):
    authority: str
    endpoint: str
    payloadName: str
    resendInterval: Duration
    retryDurationSec: int

class NotificationEndpointList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[NotificationEndpoint]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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
    name: str
    operationType: str
    progress: int
    region: str
    selfLink: str
    startTime: str
    status: typing_extensions.Literal["DONE", "PENDING", "RUNNING"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    zone: str

class OperationAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class OperationList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Operation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class OperationsScopedList(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    warning: typing.Dict[str, typing.Any]

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

class PacketMirroringAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class PacketMirroringFilter(typing_extensions.TypedDict, total=False):
    IPProtocols: typing.List[str]
    cidrRanges: typing.List[str]

class PacketMirroringForwardingRuleInfo(typing_extensions.TypedDict, total=False):
    canonicalUrl: str
    url: str

class PacketMirroringList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[PacketMirroring]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class PacketMirroringMirroredResourceInfo(typing_extensions.TypedDict, total=False):
    instances: typing.List[PacketMirroringMirroredResourceInfoInstanceInfo]
    subnetworks: typing.List[PacketMirroringMirroredResourceInfoSubnetInfo]
    tags: typing.List[str]

class PacketMirroringMirroredResourceInfoInstanceInfo(
    typing_extensions.TypedDict, total=False
):
    canonicalUrl: str
    url: str

class PacketMirroringMirroredResourceInfoSubnetInfo(
    typing_extensions.TypedDict, total=False
):
    canonicalUrl: str
    url: str

class PacketMirroringNetworkInfo(typing_extensions.TypedDict, total=False):
    canonicalUrl: str
    url: str

class PacketMirroringsScopedList(typing_extensions.TypedDict, total=False):
    packetMirrorings: typing.List[PacketMirroring]
    warning: typing.Dict[str, typing.Any]

class PathMatcher(typing_extensions.TypedDict, total=False):
    defaultRouteAction: HttpRouteAction
    defaultService: str
    defaultUrlRedirect: HttpRedirectAction
    description: str
    headerAction: HttpHeaderAction
    name: str
    pathRules: typing.List[PathRule]
    routeRules: typing.List[HttpRouteRule]

class PathRule(typing_extensions.TypedDict, total=False):
    paths: typing.List[str]
    routeAction: HttpRouteAction
    service: str
    urlRedirect: HttpRedirectAction

class PerInstanceConfig(typing_extensions.TypedDict, total=False):
    fingerprint: str
    name: str
    preservedState: PreservedState
    status: typing_extensions.Literal[
        "APPLYING", "DELETING", "EFFECTIVE", "NONE", "UNAPPLIED", "UNAPPLIED_DELETION"
    ]

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    iamOwned: bool
    rules: typing.List[Rule]
    version: int

class PreconfiguredWafSet(typing_extensions.TypedDict, total=False):
    expressionSets: typing.List[WafExpressionSet]

class PreservedState(typing_extensions.TypedDict, total=False):
    disks: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class PreservedStatePreservedDisk(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]
    mode: typing_extensions.Literal["READ_ONLY", "READ_WRITE"]
    source: str

class Project(typing_extensions.TypedDict, total=False):
    commonInstanceMetadata: Metadata
    creationTimestamp: str
    defaultNetworkTier: typing_extensions.Literal["PREMIUM", "STANDARD"]
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

class ProjectsDisableXpnResourceRequest(typing_extensions.TypedDict, total=False):
    xpnResource: XpnResourceId

class ProjectsEnableXpnResourceRequest(typing_extensions.TypedDict, total=False):
    xpnResource: XpnResourceId

class ProjectsGetXpnResources(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    resources: typing.List[XpnResourceId]

class ProjectsListXpnHostsRequest(typing_extensions.TypedDict, total=False):
    organization: str

class ProjectsSetDefaultNetworkTierRequest(typing_extensions.TypedDict, total=False):
    networkTier: typing_extensions.Literal["PREMIUM", "STANDARD"]

class Quota(typing_extensions.TypedDict, total=False):
    limit: float
    metric: typing_extensions.Literal[
        "A2_CPUS",
        "AFFINITY_GROUPS",
        "AUTOSCALERS",
        "BACKEND_BUCKETS",
        "BACKEND_SERVICES",
        "C2_CPUS",
        "COMMITMENTS",
        "COMMITTED_A2_CPUS",
        "COMMITTED_C2_CPUS",
        "COMMITTED_CPUS",
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
    ]
    owner: str
    usage: float

class Reference(typing_extensions.TypedDict, total=False):
    kind: str
    referenceType: str
    referrer: str
    target: str

class Region(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    deprecated: DeprecationStatus
    description: str
    id: str
    kind: str
    name: str
    quotas: typing.List[Quota]
    selfLink: str
    status: typing_extensions.Literal["DOWN", "UP"]
    zones: typing.List[str]

class RegionAutoscalerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Autoscaler]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RegionDiskTypeList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[DiskType]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RegionDisksAddResourcePoliciesRequest(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[str]

class RegionDisksRemoveResourcePoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    resourcePolicies: typing.List[str]

class RegionDisksResizeRequest(typing_extensions.TypedDict, total=False):
    sizeGb: str

class RegionInstanceGroupList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroup]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RegionInstanceGroupManagerDeleteInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    names: typing.List[str]

class RegionInstanceGroupManagerList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceGroupManager]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RegionInstanceGroupManagerPatchInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

class RegionInstanceGroupManagerUpdateInstanceConfigReq(
    typing_extensions.TypedDict, total=False
):
    perInstanceConfigs: typing.List[PerInstanceConfig]

class RegionInstanceGroupManagersAbandonInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

class RegionInstanceGroupManagersApplyUpdatesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]
    minimalAction: typing_extensions.Literal["NONE", "REFRESH", "REPLACE", "RESTART"]
    mostDisruptiveAllowedAction: typing_extensions.Literal[
        "NONE", "REFRESH", "REPLACE", "RESTART"
    ]

class RegionInstanceGroupManagersCreateInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[PerInstanceConfig]

class RegionInstanceGroupManagersDeleteInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

class RegionInstanceGroupManagersListErrorsResponse(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[InstanceManagedByIgmError]
    nextPageToken: str

class RegionInstanceGroupManagersListInstanceConfigsResp(
    typing_extensions.TypedDict, total=False
):
    items: typing.List[PerInstanceConfig]
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

class RegionInstanceGroupManagersListInstancesResponse(
    typing_extensions.TypedDict, total=False
):
    managedInstances: typing.List[ManagedInstance]
    nextPageToken: str

class RegionInstanceGroupManagersRecreateRequest(
    typing_extensions.TypedDict, total=False
):
    instances: typing.List[str]

class RegionInstanceGroupManagersSetTargetPoolsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    targetPools: typing.List[str]

class RegionInstanceGroupManagersSetTemplateRequest(
    typing_extensions.TypedDict, total=False
):
    instanceTemplate: str

class RegionInstanceGroupsListInstances(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[InstanceWithNamedPorts]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RegionInstanceGroupsListInstancesRequest(
    typing_extensions.TypedDict, total=False
):
    instanceState: typing_extensions.Literal["ALL", "RUNNING"]
    portName: str

class RegionInstanceGroupsSetNamedPortsRequest(
    typing_extensions.TypedDict, total=False
):
    fingerprint: str
    namedPorts: typing.List[NamedPort]

class RegionList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Region]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RegionSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

class RegionSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy

class RegionTargetHttpsProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: typing.List[str]

class RegionUrlMapsValidateRequest(typing_extensions.TypedDict, total=False):
    resource: UrlMap

class RequestMirrorPolicy(typing_extensions.TypedDict, total=False):
    backendService: str

class Reservation(typing_extensions.TypedDict, total=False):
    commitment: str
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    selfLink: str
    specificReservation: AllocationSpecificSKUReservation
    specificReservationRequired: bool
    status: typing_extensions.Literal[
        "CREATING", "DELETING", "INVALID", "READY", "UPDATING"
    ]
    zone: str

class ReservationAffinity(typing_extensions.TypedDict, total=False):
    consumeReservationType: typing_extensions.Literal[
        "ANY_RESERVATION", "NO_RESERVATION", "SPECIFIC_RESERVATION", "UNSPECIFIED"
    ]
    key: str
    values: typing.List[str]

class ReservationAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class ReservationList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Reservation]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class ReservationsResizeRequest(typing_extensions.TypedDict, total=False):
    specificSkuCount: str

class ReservationsScopedList(typing_extensions.TypedDict, total=False):
    reservations: typing.List[Reservation]
    warning: typing.Dict[str, typing.Any]

class ResourceCommitment(typing_extensions.TypedDict, total=False):
    acceleratorType: str
    amount: str
    type: typing_extensions.Literal[
        "ACCELERATOR", "LOCAL_SSD", "MEMORY", "UNSPECIFIED", "VCPU"
    ]

class ResourceGroupReference(typing_extensions.TypedDict, total=False):
    group: str

class ResourcePoliciesScopedList(typing_extensions.TypedDict, total=False):
    resourcePolicies: typing.List[ResourcePolicy]
    warning: typing.Dict[str, typing.Any]

class ResourcePolicy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    groupPlacementPolicy: ResourcePolicyGroupPlacementPolicy
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    snapshotSchedulePolicy: ResourcePolicySnapshotSchedulePolicy
    status: typing_extensions.Literal["CREATING", "DELETING", "INVALID", "READY"]

class ResourcePolicyAggregatedList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class ResourcePolicyDailyCycle(typing_extensions.TypedDict, total=False):
    daysInCycle: int
    duration: str
    startTime: str

class ResourcePolicyGroupPlacementPolicy(typing_extensions.TypedDict, total=False):
    availabilityDomainCount: int
    collocation: typing_extensions.Literal["COLLOCATED", "UNSPECIFIED_COLLOCATION"]
    vmCount: int

class ResourcePolicyHourlyCycle(typing_extensions.TypedDict, total=False):
    duration: str
    hoursInCycle: int
    startTime: str

class ResourcePolicyList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    items: typing.List[ResourcePolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class ResourcePolicySnapshotSchedulePolicy(typing_extensions.TypedDict, total=False):
    retentionPolicy: ResourcePolicySnapshotSchedulePolicyRetentionPolicy
    schedule: ResourcePolicySnapshotSchedulePolicySchedule
    snapshotProperties: ResourcePolicySnapshotSchedulePolicySnapshotProperties

class ResourcePolicySnapshotSchedulePolicyRetentionPolicy(
    typing_extensions.TypedDict, total=False
):
    maxRetentionDays: int
    onSourceDiskDelete: typing_extensions.Literal[
        "APPLY_RETENTION_POLICY",
        "KEEP_AUTO_SNAPSHOTS",
        "UNSPECIFIED_ON_SOURCE_DISK_DELETE",
    ]

class ResourcePolicySnapshotSchedulePolicySchedule(
    typing_extensions.TypedDict, total=False
):
    dailySchedule: ResourcePolicyDailyCycle
    hourlySchedule: ResourcePolicyHourlyCycle
    weeklySchedule: ResourcePolicyWeeklyCycle

class ResourcePolicySnapshotSchedulePolicySnapshotProperties(
    typing_extensions.TypedDict, total=False
):
    guestFlush: bool
    labels: typing.Dict[str, typing.Any]
    storageLocations: typing.List[str]

class ResourcePolicyWeeklyCycle(typing_extensions.TypedDict, total=False):
    dayOfWeeks: typing.List[ResourcePolicyWeeklyCycleDayOfWeek]

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
    nextHopIp: str
    nextHopNetwork: str
    nextHopPeering: str
    nextHopVpnTunnel: str
    priority: int
    selfLink: str
    tags: typing.List[str]
    warnings: typing.List[typing.Dict[str, typing.Any]]

class RouteList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Route]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class Router(typing_extensions.TypedDict, total=False):
    bgp: RouterBgp
    bgpPeers: typing.List[RouterBgpPeer]
    creationTimestamp: str
    description: str
    id: str
    interfaces: typing.List[RouterInterface]
    kind: str
    name: str
    nats: typing.List[RouterNat]
    network: str
    region: str
    selfLink: str

class RouterAdvertisedIpRange(typing_extensions.TypedDict, total=False):
    description: str
    range: str

class RouterAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class RouterBgp(typing_extensions.TypedDict, total=False):
    advertiseMode: typing_extensions.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: typing.List[str]
    advertisedIpRanges: typing.List[RouterAdvertisedIpRange]
    asn: int

class RouterBgpPeer(typing_extensions.TypedDict, total=False):
    advertiseMode: typing_extensions.Literal["CUSTOM", "DEFAULT"]
    advertisedGroups: typing.List[str]
    advertisedIpRanges: typing.List[RouterAdvertisedIpRange]
    advertisedRoutePriority: int
    interfaceName: str
    ipAddress: str
    managementType: typing_extensions.Literal[
        "MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"
    ]
    name: str
    peerAsn: int
    peerIpAddress: str

class RouterInterface(typing_extensions.TypedDict, total=False):
    ipRange: str
    linkedInterconnectAttachment: str
    linkedVpnTunnel: str
    managementType: typing_extensions.Literal[
        "MANAGED_BY_ATTACHMENT", "MANAGED_BY_USER"
    ]
    name: str

class RouterList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Router]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class RouterNat(typing_extensions.TypedDict, total=False):
    drainNatIps: typing.List[str]
    icmpIdleTimeoutSec: int
    logConfig: RouterNatLogConfig
    minPortsPerVm: int
    name: str
    natIpAllocateOption: typing_extensions.Literal["AUTO_ONLY", "MANUAL_ONLY"]
    natIps: typing.List[str]
    sourceSubnetworkIpRangesToNat: typing_extensions.Literal[
        "ALL_SUBNETWORKS_ALL_IP_RANGES",
        "ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES",
        "LIST_OF_SUBNETWORKS",
    ]
    subnetworks: typing.List[RouterNatSubnetworkToNat]
    tcpEstablishedIdleTimeoutSec: int
    tcpTransitoryIdleTimeoutSec: int
    udpIdleTimeoutSec: int

class RouterNatLogConfig(typing_extensions.TypedDict, total=False):
    enable: bool
    filter: typing_extensions.Literal["ALL", "ERRORS_ONLY", "TRANSLATIONS_ONLY"]

class RouterNatSubnetworkToNat(typing_extensions.TypedDict, total=False):
    name: str
    secondaryIpRangeNames: typing.List[str]
    sourceIpRangesToNat: typing.List[str]

class RouterStatus(typing_extensions.TypedDict, total=False):
    bestRoutes: typing.List[Route]
    bestRoutesForRouter: typing.List[Route]
    bgpPeerStatus: typing.List[RouterStatusBgpPeerStatus]
    natStatus: typing.List[RouterStatusNatStatus]
    network: str

class RouterStatusBgpPeerStatus(typing_extensions.TypedDict, total=False):
    advertisedRoutes: typing.List[Route]
    ipAddress: str
    linkedVpnTunnel: str
    name: str
    numLearnedRoutes: int
    peerIpAddress: str
    state: str
    status: typing_extensions.Literal["DOWN", "UNKNOWN", "UP"]
    uptime: str
    uptimeSeconds: str

class RouterStatusNatStatus(typing_extensions.TypedDict, total=False):
    autoAllocatedNatIps: typing.List[str]
    drainAutoAllocatedNatIps: typing.List[str]
    drainUserAllocatedNatIps: typing.List[str]
    minExtraNatIpsNeeded: int
    name: str
    numVmEndpointsWithNatMappings: int
    userAllocatedNatIpResources: typing.List[str]
    userAllocatedNatIps: typing.List[str]

class RouterStatusResponse(typing_extensions.TypedDict, total=False):
    kind: str
    result: RouterStatus

class RoutersPreviewResponse(typing_extensions.TypedDict, total=False):
    resource: Router

class RoutersScopedList(typing_extensions.TypedDict, total=False):
    routers: typing.List[Router]
    warning: typing.Dict[str, typing.Any]

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

class SSLHealthCheck(typing_extensions.TypedDict, total=False):
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    request: str
    response: str

class Scheduling(typing_extensions.TypedDict, total=False):
    automaticRestart: bool
    minNodeCpus: int
    nodeAffinities: typing.List[SchedulingNodeAffinity]
    onHostMaintenance: typing_extensions.Literal["MIGRATE", "TERMINATE"]
    preemptible: bool

class SchedulingNodeAffinity(typing_extensions.TypedDict, total=False):
    key: str
    operator: typing_extensions.Literal["IN", "NOT_IN", "OPERATOR_UNSPECIFIED"]
    values: typing.List[str]

class Screenshot(typing_extensions.TypedDict, total=False):
    contents: str
    kind: str

class SecurityPoliciesListPreconfiguredExpressionSetsResponse(
    typing_extensions.TypedDict, total=False
):
    preconfiguredExpressionSets: SecurityPoliciesWafConfig

class SecurityPoliciesWafConfig(typing_extensions.TypedDict, total=False):
    wafRules: PreconfiguredWafSet

class SecurityPolicy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    rules: typing.List[SecurityPolicyRule]
    selfLink: str

class SecurityPolicyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[SecurityPolicy]
    kind: str
    nextPageToken: str
    warning: typing.Dict[str, typing.Any]

class SecurityPolicyReference(typing_extensions.TypedDict, total=False):
    securityPolicy: str

class SecurityPolicyRule(typing_extensions.TypedDict, total=False):
    action: str
    description: str
    kind: str
    match: SecurityPolicyRuleMatcher
    preview: bool
    priority: int

class SecurityPolicyRuleMatcher(typing_extensions.TypedDict, total=False):
    config: SecurityPolicyRuleMatcherConfig
    expr: Expr
    versionedExpr: typing_extensions.Literal["SRC_IPS_V1"]

class SecurityPolicyRuleMatcherConfig(typing_extensions.TypedDict, total=False):
    srcIpRanges: typing.List[str]

class SerialPortOutput(typing_extensions.TypedDict, total=False):
    contents: str
    kind: str
    next: str
    selfLink: str
    start: str

class ServerBinding(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "RESTART_NODE_ON_ANY_SERVER",
        "RESTART_NODE_ON_MINIMAL_SERVERS",
        "SERVER_BINDING_TYPE_UNSPECIFIED",
    ]

class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scopes: typing.List[str]

class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableIntegrityMonitoring: bool
    enableSecureBoot: bool
    enableVtpm: bool

class ShieldedInstanceIdentity(typing_extensions.TypedDict, total=False):
    encryptionKey: ShieldedInstanceIdentityEntry
    kind: str
    signingKey: ShieldedInstanceIdentityEntry

class ShieldedInstanceIdentityEntry(typing_extensions.TypedDict, total=False):
    ekCert: str
    ekPub: str

class ShieldedInstanceIntegrityPolicy(typing_extensions.TypedDict, total=False):
    updateAutoLearnPolicy: bool

class SignedUrlKey(typing_extensions.TypedDict, total=False):
    keyName: str
    keyValue: str

class Snapshot(typing_extensions.TypedDict, total=False):
    autoCreated: bool
    creationTimestamp: str
    description: str
    diskSizeGb: str
    downloadBytes: str
    id: str
    kind: str
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]
    licenseCodes: typing.List[str]
    licenses: typing.List[str]
    name: str
    selfLink: str
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

class SnapshotList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Snapshot]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class SourceInstanceParams(typing_extensions.TypedDict, total=False):
    diskConfigs: typing.List[DiskInstantiationConfig]

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
    subjectAlternativeNames: typing.List[str]
    type: typing_extensions.Literal["MANAGED", "SELF_MANAGED", "TYPE_UNSPECIFIED"]

class SslCertificateAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class SslCertificateList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[SslCertificate]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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

class SslCertificateSelfManagedSslCertificate(typing_extensions.TypedDict, total=False):
    certificate: str
    privateKey: str

class SslCertificatesScopedList(typing_extensions.TypedDict, total=False):
    sslCertificates: typing.List[SslCertificate]
    warning: typing.Dict[str, typing.Any]

class SslPoliciesList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[SslPolicy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class SslPoliciesListAvailableFeaturesResponse(
    typing_extensions.TypedDict, total=False
):
    features: typing.List[str]

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
    warnings: typing.List[typing.Dict[str, typing.Any]]

class SslPolicyReference(typing_extensions.TypedDict, total=False):
    sslPolicy: str

class StatefulPolicy(typing_extensions.TypedDict, total=False):
    preservedState: StatefulPolicyPreservedState

class StatefulPolicyPreservedState(typing_extensions.TypedDict, total=False):
    disks: typing.Dict[str, typing.Any]

class StatefulPolicyPreservedStateDiskDevice(typing_extensions.TypedDict, total=False):
    autoDelete: typing_extensions.Literal["NEVER", "ON_PERMANENT_INSTANCE_DELETION"]

class Subnetwork(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    enableFlowLogs: bool
    fingerprint: str
    gatewayAddress: str
    id: str
    ipCidrRange: str
    ipv6CidrRange: str
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
        "INTERNAL_HTTPS_LOAD_BALANCER", "PRIVATE", "PRIVATE_RFC_1918"
    ]
    region: str
    role: typing_extensions.Literal["ACTIVE", "BACKUP"]
    secondaryIpRanges: typing.List[SubnetworkSecondaryRange]
    selfLink: str
    state: typing_extensions.Literal["DRAINING", "READY"]

class SubnetworkAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class SubnetworkList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Subnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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

class SubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

class SubnetworksExpandIpCidrRangeRequest(typing_extensions.TypedDict, total=False):
    ipCidrRange: str

class SubnetworksScopedList(typing_extensions.TypedDict, total=False):
    subnetworks: typing.List[Subnetwork]
    warning: typing.Dict[str, typing.Any]

class SubnetworksSetPrivateIpGoogleAccessRequest(
    typing_extensions.TypedDict, total=False
):
    privateIpGoogleAccess: bool

class TCPHealthCheck(typing_extensions.TypedDict, total=False):
    port: int
    portName: str
    portSpecification: typing_extensions.Literal[
        "USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"
    ]
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    request: str
    response: str

class Tags(typing_extensions.TypedDict, total=False):
    fingerprint: str
    items: typing.List[str]

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

class TargetGrpcProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetGrpcProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetHttpProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetHttpProxies: typing.List[TargetHttpProxy]
    warning: typing.Dict[str, typing.Any]

class TargetHttpProxy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    fingerprint: str
    id: str
    kind: str
    name: str
    region: str
    selfLink: str
    urlMap: str

class TargetHttpProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]

class TargetHttpProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetHttpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetHttpsProxiesScopedList(typing_extensions.TypedDict, total=False):
    targetHttpsProxies: typing.List[TargetHttpsProxy]
    warning: typing.Dict[str, typing.Any]

class TargetHttpsProxiesSetQuicOverrideRequest(
    typing_extensions.TypedDict, total=False
):
    quicOverride: typing_extensions.Literal["DISABLE", "ENABLE", "NONE"]

class TargetHttpsProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: typing.List[str]

class TargetHttpsProxy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    quicOverride: typing_extensions.Literal["DISABLE", "ENABLE", "NONE"]
    region: str
    selfLink: str
    sslCertificates: typing.List[str]
    sslPolicy: str
    urlMap: str

class TargetHttpsProxyAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class TargetHttpsProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetHttpsProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetInstance(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    instance: str
    kind: str
    name: str
    natPolicy: typing_extensions.Literal["NO_NAT"]
    selfLink: str
    zone: str

class TargetInstanceAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class TargetInstanceList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetInstance]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetInstancesScopedList(typing_extensions.TypedDict, total=False):
    targetInstances: typing.List[TargetInstance]
    warning: typing.Dict[str, typing.Any]

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
    sessionAffinity: typing_extensions.Literal[
        "CLIENT_IP",
        "CLIENT_IP_PORT_PROTO",
        "CLIENT_IP_PROTO",
        "GENERATED_COOKIE",
        "HEADER_FIELD",
        "HTTP_COOKIE",
        "NONE",
    ]

class TargetPoolAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class TargetPoolInstanceHealth(typing_extensions.TypedDict, total=False):
    healthStatus: typing.List[HealthStatus]
    kind: str

class TargetPoolList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetPool]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetPoolsAddHealthCheckRequest(typing_extensions.TypedDict, total=False):
    healthChecks: typing.List[HealthCheckReference]

class TargetPoolsAddInstanceRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

class TargetPoolsRemoveHealthCheckRequest(typing_extensions.TypedDict, total=False):
    healthChecks: typing.List[HealthCheckReference]

class TargetPoolsRemoveInstanceRequest(typing_extensions.TypedDict, total=False):
    instances: typing.List[InstanceReference]

class TargetPoolsScopedList(typing_extensions.TypedDict, total=False):
    targetPools: typing.List[TargetPool]
    warning: typing.Dict[str, typing.Any]

class TargetReference(typing_extensions.TypedDict, total=False):
    target: str

class TargetSslProxiesSetBackendServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: str

class TargetSslProxiesSetProxyHeaderRequest(typing_extensions.TypedDict, total=False):
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]

class TargetSslProxiesSetSslCertificatesRequest(
    typing_extensions.TypedDict, total=False
):
    sslCertificates: typing.List[str]

class TargetSslProxy(typing_extensions.TypedDict, total=False):
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

class TargetSslProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetSslProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetTcpProxiesSetBackendServiceRequest(
    typing_extensions.TypedDict, total=False
):
    service: str

class TargetTcpProxiesSetProxyHeaderRequest(typing_extensions.TypedDict, total=False):
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]

class TargetTcpProxy(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    id: str
    kind: str
    name: str
    proxyHeader: typing_extensions.Literal["NONE", "PROXY_V1"]
    selfLink: str
    service: str

class TargetTcpProxyList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetTcpProxy]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetVpnGateway(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    forwardingRules: typing.List[str]
    id: str
    kind: str
    name: str
    network: str
    region: str
    selfLink: str
    status: typing_extensions.Literal["CREATING", "DELETING", "FAILED", "READY"]
    tunnels: typing.List[str]

class TargetVpnGatewayAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class TargetVpnGatewayList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[TargetVpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class TargetVpnGatewaysScopedList(typing_extensions.TypedDict, total=False):
    targetVpnGateways: typing.List[TargetVpnGateway]
    warning: typing.Dict[str, typing.Any]

class TestFailure(typing_extensions.TypedDict, total=False):
    actualService: str
    expectedService: str
    host: str
    path: str

class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

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

class UrlMapList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[UrlMap]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class UrlMapReference(typing_extensions.TypedDict, total=False):
    urlMap: str

class UrlMapTest(typing_extensions.TypedDict, total=False):
    description: str
    host: str
    path: str
    service: str

class UrlMapValidationResult(typing_extensions.TypedDict, total=False):
    loadErrors: typing.List[str]
    loadSucceeded: bool
    testFailures: typing.List[TestFailure]
    testPassed: bool

class UrlMapsAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class UrlMapsScopedList(typing_extensions.TypedDict, total=False):
    urlMaps: typing.List[UrlMap]
    warning: typing.Dict[str, typing.Any]

class UrlMapsValidateRequest(typing_extensions.TypedDict, total=False):
    resource: UrlMap

class UrlMapsValidateResponse(typing_extensions.TypedDict, total=False):
    result: UrlMapValidationResult

class UrlRewrite(typing_extensions.TypedDict, total=False):
    hostRewrite: str
    pathPrefixRewrite: str

class UsableSubnetwork(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    network: str
    secondaryIpRanges: typing.List[UsableSubnetworkSecondaryRange]
    subnetwork: str

class UsableSubnetworkSecondaryRange(typing_extensions.TypedDict, total=False):
    ipCidrRange: str
    rangeName: str

class UsableSubnetworksAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[UsableSubnetwork]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class UsageExportLocation(typing_extensions.TypedDict, total=False):
    bucketName: str
    reportNamePrefix: str

class VmEndpointNatMappings(typing_extensions.TypedDict, total=False):
    instanceName: str
    interfaceNatMappings: typing.List[VmEndpointNatMappingsInterfaceNatMappings]

class VmEndpointNatMappingsInterfaceNatMappings(
    typing_extensions.TypedDict, total=False
):
    drainNatIpPortRanges: typing.List[str]
    natIpPortRanges: typing.List[str]
    numTotalDrainNatPorts: int
    numTotalNatPorts: int
    sourceAliasIpRange: str
    sourceVirtualIp: str

class VmEndpointNatMappingsList(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    nextPageToken: str
    result: typing.List[VmEndpointNatMappings]
    selfLink: str
    warning: typing.Dict[str, typing.Any]

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

class VpnGatewayAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class VpnGatewayList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[VpnGateway]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class VpnGatewayStatus(typing_extensions.TypedDict, total=False):
    vpnConnections: typing.List[VpnGatewayStatusVpnConnection]

class VpnGatewayStatusHighAvailabilityRequirementState(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "CONNECTION_REDUNDANCY_MET", "CONNECTION_REDUNDANCY_NOT_MET"
    ]
    unsatisfiedReason: typing_extensions.Literal["INCOMPLETE_TUNNELS_COVERAGE"]

class VpnGatewayStatusTunnel(typing_extensions.TypedDict, total=False):
    localGatewayInterface: int
    peerGatewayInterface: int
    tunnelUrl: str

class VpnGatewayStatusVpnConnection(typing_extensions.TypedDict, total=False):
    peerExternalGateway: str
    peerGcpGateway: str
    state: VpnGatewayStatusHighAvailabilityRequirementState
    tunnels: typing.List[VpnGatewayStatusTunnel]

class VpnGatewayVpnGatewayInterface(typing_extensions.TypedDict, total=False):
    id: int
    ipAddress: str

class VpnGatewaysGetStatusResponse(typing_extensions.TypedDict, total=False):
    result: VpnGatewayStatus

class VpnGatewaysScopedList(typing_extensions.TypedDict, total=False):
    vpnGateways: typing.List[VpnGateway]
    warning: typing.Dict[str, typing.Any]

class VpnTunnel(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    description: str
    detailedStatus: str
    id: str
    ikeVersion: int
    kind: str
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

class VpnTunnelAggregatedList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.Dict[str, typing.Any]
    kind: str
    nextPageToken: str
    selfLink: str
    unreachables: typing.List[str]
    warning: typing.Dict[str, typing.Any]

class VpnTunnelList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[VpnTunnel]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class VpnTunnelsScopedList(typing_extensions.TypedDict, total=False):
    vpnTunnels: typing.List[VpnTunnel]
    warning: typing.Dict[str, typing.Any]

class WafExpressionSet(typing_extensions.TypedDict, total=False):
    aliases: typing.List[str]
    expressions: typing.List[WafExpressionSetExpression]
    id: str

class WafExpressionSetExpression(typing_extensions.TypedDict, total=False):
    id: str

class WeightedBackendService(typing_extensions.TypedDict, total=False):
    backendService: str
    headerAction: HttpHeaderAction
    weight: int

class XpnHostList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Project]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class XpnResourceId(typing_extensions.TypedDict, total=False):
    id: str
    type: typing_extensions.Literal["PROJECT", "XPN_RESOURCE_TYPE_UNSPECIFIED"]

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

class ZoneList(typing_extensions.TypedDict, total=False):
    id: str
    items: typing.List[Zone]
    kind: str
    nextPageToken: str
    selfLink: str
    warning: typing.Dict[str, typing.Any]

class ZoneSetLabelsRequest(typing_extensions.TypedDict, total=False):
    labelFingerprint: str
    labels: typing.Dict[str, typing.Any]

class ZoneSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    policy: Policy
