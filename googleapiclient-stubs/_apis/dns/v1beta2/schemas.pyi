import typing

_list = list

@typing.type_check_only
class Change(typing.TypedDict, total=False):
    additions: _list[ResourceRecordSet]
    deletions: _list[ResourceRecordSet]
    id: str
    isServing: bool
    kind: str
    startTime: str
    status: typing.Literal["pending", "done"]

@typing.type_check_only
class ChangesListResponse(typing.TypedDict, total=False):
    changes: _list[Change]
    kind: str
    nextPageToken: str

@typing.type_check_only
class DnsKey(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]
    creationTime: str
    description: str
    digests: _list[DnsKeyDigest]
    id: str
    isActive: bool
    keyLength: int
    keyTag: int
    kind: str
    publicKey: str
    type: typing.Literal["keySigning", "zoneSigning"]

@typing.type_check_only
class DnsKeyDigest(typing.TypedDict, total=False):
    digest: str
    type: typing.Literal["sha1", "sha256", "sha384"]

@typing.type_check_only
class DnsKeySpec(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]
    keyLength: int
    keyType: typing.Literal["keySigning", "zoneSigning"]
    kind: str

@typing.type_check_only
class DnsKeysListResponse(typing.TypedDict, total=False):
    dnsKeys: _list[DnsKey]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GoogleIamV1GetPolicyOptions

@typing.type_check_only
class GoogleIamV1GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class ManagedZone(typing.TypedDict, total=False):
    cloudLoggingConfig: ManagedZoneCloudLoggingConfig
    creationTime: str
    description: str
    dnsName: str
    dnssecConfig: ManagedZoneDnsSecConfig
    forwardingConfig: ManagedZoneForwardingConfig
    id: str
    kind: str
    labels: dict[str, typing.Any]
    name: str
    nameServerSet: str
    nameServers: _list[str]
    peeringConfig: ManagedZonePeeringConfig
    privateVisibilityConfig: ManagedZonePrivateVisibilityConfig
    reverseLookupConfig: ManagedZoneReverseLookupConfig
    serviceDirectoryConfig: ManagedZoneServiceDirectoryConfig
    visibility: typing.Literal["public", "private"]

@typing.type_check_only
class ManagedZoneCloudLoggingConfig(typing.TypedDict, total=False):
    enableLogging: bool
    kind: str

@typing.type_check_only
class ManagedZoneDnsSecConfig(typing.TypedDict, total=False):
    defaultKeySpecs: _list[DnsKeySpec]
    kind: str
    nonExistence: typing.Literal["nsec", "nsec3"]
    state: typing.Literal["off", "on", "transfer"]

@typing.type_check_only
class ManagedZoneForwardingConfig(typing.TypedDict, total=False):
    kind: str
    targetNameServers: _list[ManagedZoneForwardingConfigNameServerTarget]

@typing.type_check_only
class ManagedZoneForwardingConfigNameServerTarget(typing.TypedDict, total=False):
    domainName: str
    forwardingPath: typing.Literal["default", "private"]
    ipv4Address: str
    ipv6Address: str
    kind: str

@typing.type_check_only
class ManagedZoneOperationsListResponse(typing.TypedDict, total=False):
    kind: str
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ManagedZonePeeringConfig(typing.TypedDict, total=False):
    kind: str
    targetNetwork: ManagedZonePeeringConfigTargetNetwork

@typing.type_check_only
class ManagedZonePeeringConfigTargetNetwork(typing.TypedDict, total=False):
    deactivateTime: str
    kind: str
    networkUrl: str

@typing.type_check_only
class ManagedZonePrivateVisibilityConfig(typing.TypedDict, total=False):
    gkeClusters: _list[ManagedZonePrivateVisibilityConfigGKECluster]
    kind: str
    networks: _list[ManagedZonePrivateVisibilityConfigNetwork]

@typing.type_check_only
class ManagedZonePrivateVisibilityConfigGKECluster(typing.TypedDict, total=False):
    gkeClusterName: str
    kind: str

@typing.type_check_only
class ManagedZonePrivateVisibilityConfigNetwork(typing.TypedDict, total=False):
    kind: str
    networkUrl: str

@typing.type_check_only
class ManagedZoneReverseLookupConfig(typing.TypedDict, total=False):
    kind: str

@typing.type_check_only
class ManagedZoneServiceDirectoryConfig(typing.TypedDict, total=False):
    kind: str
    namespace: ManagedZoneServiceDirectoryConfigNamespace

@typing.type_check_only
class ManagedZoneServiceDirectoryConfigNamespace(typing.TypedDict, total=False):
    deletionTime: str
    kind: str
    namespaceUrl: str

@typing.type_check_only
class ManagedZonesListResponse(typing.TypedDict, total=False):
    kind: str
    managedZones: _list[ManagedZone]
    nextPageToken: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    dnsKeyContext: OperationDnsKeyContext
    id: str
    kind: str
    startTime: str
    status: typing.Literal["pending", "done"]
    type: str
    user: str
    zoneContext: OperationManagedZoneContext

@typing.type_check_only
class OperationDnsKeyContext(typing.TypedDict, total=False):
    newValue: DnsKey
    oldValue: DnsKey

@typing.type_check_only
class OperationManagedZoneContext(typing.TypedDict, total=False):
    newValue: ManagedZone
    oldValue: ManagedZone

@typing.type_check_only
class PoliciesListResponse(typing.TypedDict, total=False):
    kind: str
    nextPageToken: str
    policies: _list[Policy]

@typing.type_check_only
class PoliciesPatchResponse(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class PoliciesUpdateResponse(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    alternativeNameServerConfig: PolicyAlternativeNameServerConfig
    description: str
    dns64Config: PolicyDns64Config
    enableInboundForwarding: bool
    enableLogging: bool
    id: str
    kind: str
    name: str
    networks: _list[PolicyNetwork]

@typing.type_check_only
class PolicyAlternativeNameServerConfig(typing.TypedDict, total=False):
    kind: str
    targetNameServers: _list[PolicyAlternativeNameServerConfigTargetNameServer]

@typing.type_check_only
class PolicyAlternativeNameServerConfigTargetNameServer(typing.TypedDict, total=False):
    forwardingPath: typing.Literal["default", "private"]
    ipv4Address: str
    ipv6Address: str
    kind: str

@typing.type_check_only
class PolicyDns64Config(typing.TypedDict, total=False):
    kind: str
    scope: PolicyDns64ConfigScope

@typing.type_check_only
class PolicyDns64ConfigScope(typing.TypedDict, total=False):
    allQueries: bool
    kind: str

@typing.type_check_only
class PolicyNetwork(typing.TypedDict, total=False):
    kind: str
    networkUrl: str

@typing.type_check_only
class Project(typing.TypedDict, total=False):
    id: str
    kind: str
    number: str
    quota: Quota

@typing.type_check_only
class Quota(typing.TypedDict, total=False):
    dnsKeysPerManagedZone: int
    gkeClustersPerManagedZone: int
    gkeClustersPerPolicy: int
    gkeClustersPerResponsePolicy: int
    internetHealthChecksPerManagedZone: int
    itemsPerRoutingPolicy: int
    kind: str
    managedZones: int
    managedZonesPerGkeCluster: int
    managedZonesPerNetwork: int
    nameserversPerDelegation: int
    networksPerManagedZone: int
    networksPerPolicy: int
    networksPerResponsePolicy: int
    peeringZonesPerTargetNetwork: int
    policies: int
    resourceRecordsPerRrset: int
    responsePolicies: int
    responsePolicyRulesPerResponsePolicy: int
    rrsetAdditionsPerChange: int
    rrsetDeletionsPerChange: int
    rrsetsPerManagedZone: int
    targetNameServersPerManagedZone: int
    targetNameServersPerPolicy: int
    totalRrdataSizePerChange: int
    whitelistedKeySpecs: _list[DnsKeySpec]

@typing.type_check_only
class RRSetRoutingPolicy(typing.TypedDict, total=False):
    geo: RRSetRoutingPolicyGeoPolicy
    geoPolicy: RRSetRoutingPolicyGeoPolicy
    healthCheck: str
    kind: str
    primaryBackup: RRSetRoutingPolicyPrimaryBackupPolicy
    wrr: RRSetRoutingPolicyWrrPolicy
    wrrPolicy: RRSetRoutingPolicyWrrPolicy

@typing.type_check_only
class RRSetRoutingPolicyGeoPolicy(typing.TypedDict, total=False):
    enableFencing: bool
    items: _list[RRSetRoutingPolicyGeoPolicyGeoPolicyItem]
    kind: str

@typing.type_check_only
class RRSetRoutingPolicyGeoPolicyGeoPolicyItem(typing.TypedDict, total=False):
    healthCheckedTargets: RRSetRoutingPolicyHealthCheckTargets
    kind: str
    location: str
    rrdatas: _list[str]
    signatureRrdatas: _list[str]

@typing.type_check_only
class RRSetRoutingPolicyHealthCheckTargets(typing.TypedDict, total=False):
    externalEndpoints: _list[str]
    internalLoadBalancers: _list[RRSetRoutingPolicyLoadBalancerTarget]

@typing.type_check_only
class RRSetRoutingPolicyLoadBalancerTarget(typing.TypedDict, total=False):
    ipAddress: str
    ipProtocol: typing.Literal["undefined", "tcp", "udp"]
    kind: str
    loadBalancerType: typing.Literal[
        "none", "globalL7ilb", "regionalL4ilb", "regionalL7ilb"
    ]
    networkUrl: str
    port: str
    project: str
    region: str

@typing.type_check_only
class RRSetRoutingPolicyPrimaryBackupPolicy(typing.TypedDict, total=False):
    backupGeoTargets: RRSetRoutingPolicyGeoPolicy
    kind: str
    primaryTargets: RRSetRoutingPolicyHealthCheckTargets
    trickleTraffic: float

@typing.type_check_only
class RRSetRoutingPolicyWrrPolicy(typing.TypedDict, total=False):
    items: _list[RRSetRoutingPolicyWrrPolicyWrrPolicyItem]
    kind: str

@typing.type_check_only
class RRSetRoutingPolicyWrrPolicyWrrPolicyItem(typing.TypedDict, total=False):
    healthCheckedTargets: RRSetRoutingPolicyHealthCheckTargets
    kind: str
    rrdatas: _list[str]
    signatureRrdatas: _list[str]
    weight: float

@typing.type_check_only
class ResourceRecordSet(typing.TypedDict, total=False):
    kind: str
    name: str
    routingPolicy: RRSetRoutingPolicy
    rrdatas: _list[str]
    signatureRrdatas: _list[str]
    ttl: int
    type: str

@typing.type_check_only
class ResourceRecordSetsListResponse(typing.TypedDict, total=False):
    kind: str
    nextPageToken: str
    rrsets: _list[ResourceRecordSet]

@typing.type_check_only
class ResponsePoliciesListResponse(typing.TypedDict, total=False):
    nextPageToken: str
    responsePolicies: _list[ResponsePolicy]

@typing.type_check_only
class ResponsePoliciesPatchResponse(typing.TypedDict, total=False):
    responsePolicy: ResponsePolicy

@typing.type_check_only
class ResponsePoliciesUpdateResponse(typing.TypedDict, total=False):
    responsePolicy: ResponsePolicy

@typing.type_check_only
class ResponsePolicy(typing.TypedDict, total=False):
    description: str
    gkeClusters: _list[ResponsePolicyGKECluster]
    id: str
    kind: str
    labels: dict[str, typing.Any]
    networks: _list[ResponsePolicyNetwork]
    responsePolicyName: str

@typing.type_check_only
class ResponsePolicyGKECluster(typing.TypedDict, total=False):
    gkeClusterName: str
    kind: str

@typing.type_check_only
class ResponsePolicyNetwork(typing.TypedDict, total=False):
    kind: str
    networkUrl: str

@typing.type_check_only
class ResponsePolicyRule(typing.TypedDict, total=False):
    behavior: typing.Literal["behaviorUnspecified", "bypassResponsePolicy"]
    dnsName: str
    kind: str
    localData: ResponsePolicyRuleLocalData
    ruleName: str

@typing.type_check_only
class ResponsePolicyRuleLocalData(typing.TypedDict, total=False):
    localDatas: _list[ResourceRecordSet]

@typing.type_check_only
class ResponsePolicyRulesListResponse(typing.TypedDict, total=False):
    nextPageToken: str
    responsePolicyRules: _list[ResponsePolicyRule]

@typing.type_check_only
class ResponsePolicyRulesPatchResponse(typing.TypedDict, total=False):
    responsePolicyRule: ResponsePolicyRule

@typing.type_check_only
class ResponsePolicyRulesUpdateResponse(typing.TypedDict, total=False):
    responsePolicyRule: ResponsePolicyRule

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
