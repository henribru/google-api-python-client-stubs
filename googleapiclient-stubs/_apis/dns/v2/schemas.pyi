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
    status: typing.Literal["PENDING", "DONE"]

@typing.type_check_only
class ChangesListResponse(typing.TypedDict, total=False):
    changes: _list[Change]
    header: ResponseHeader
    kind: str
    nextPageToken: str

@typing.type_check_only
class DnsKey(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "RSASHA1", "RSASHA256", "RSASHA512", "ECDSAP256SHA256", "ECDSAP384SHA384"
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
    type: typing.Literal["KEY_SIGNING", "ZONE_SIGNING"]

@typing.type_check_only
class DnsKeyDigest(typing.TypedDict, total=False):
    digest: str
    type: typing.Literal["SHA1", "SHA256", "SHA384"]

@typing.type_check_only
class DnsKeySpec(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "RSASHA1", "RSASHA256", "RSASHA512", "ECDSAP256SHA256", "ECDSAP384SHA384"
    ]
    keyLength: int
    keyType: typing.Literal["KEY_SIGNING", "ZONE_SIGNING"]
    kind: str

@typing.type_check_only
class DnsKeysListResponse(typing.TypedDict, total=False):
    dnsKeys: _list[DnsKey]
    header: ResponseHeader
    kind: str
    nextPageToken: str

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
    visibility: typing.Literal["PUBLIC", "PRIVATE"]

@typing.type_check_only
class ManagedZoneCloudLoggingConfig(typing.TypedDict, total=False):
    enableLogging: bool
    kind: str

@typing.type_check_only
class ManagedZoneDnsSecConfig(typing.TypedDict, total=False):
    defaultKeySpecs: _list[DnsKeySpec]
    kind: str
    nonExistence: typing.Literal["NSEC", "NSEC3"]
    state: typing.Literal["OFF", "ON", "TRANSFER"]

@typing.type_check_only
class ManagedZoneForwardingConfig(typing.TypedDict, total=False):
    kind: str
    targetNameServers: _list[ManagedZoneForwardingConfigNameServerTarget]

@typing.type_check_only
class ManagedZoneForwardingConfigNameServerTarget(typing.TypedDict, total=False):
    forwardingPath: typing.Literal["DEFAULT", "PRIVATE"]
    ipv4Address: str
    kind: str

@typing.type_check_only
class ManagedZoneOperationsListResponse(typing.TypedDict, total=False):
    header: ResponseHeader
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
    header: ResponseHeader
    kind: str
    managedZones: _list[ManagedZone]
    nextPageToken: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    dnsKeyContext: OperationDnsKeyContext
    id: str
    kind: str
    startTime: str
    status: typing.Literal["PENDING", "DONE"]
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
    header: ResponseHeader
    kind: str
    nextPageToken: str
    policies: _list[Policy]

@typing.type_check_only
class PoliciesPatchResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

@typing.type_check_only
class PoliciesUpdateResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    alternativeNameServerConfig: PolicyAlternativeNameServerConfig
    description: str
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
    forwardingPath: typing.Literal["DEFAULT", "PRIVATE"]
    ipv4Address: str
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
    itemsPerRoutingPolicy: int
    kind: str
    managedZones: int
    managedZonesPerNetwork: int
    networksPerManagedZone: int
    networksPerPolicy: int
    peeringZonesPerTargetNetwork: int
    policies: int
    resourceRecordsPerRrset: int
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
    kind: str
    wrr: RRSetRoutingPolicyWrrPolicy

@typing.type_check_only
class RRSetRoutingPolicyGeoPolicy(typing.TypedDict, total=False):
    items: _list[RRSetRoutingPolicyGeoPolicyGeoPolicyItem]
    kind: str

@typing.type_check_only
class RRSetRoutingPolicyGeoPolicyGeoPolicyItem(typing.TypedDict, total=False):
    kind: str
    location: str
    rrdatas: _list[str]
    signatureRrdatas: _list[str]

@typing.type_check_only
class RRSetRoutingPolicyWrrPolicy(typing.TypedDict, total=False):
    items: _list[RRSetRoutingPolicyWrrPolicyWrrPolicyItem]
    kind: str

@typing.type_check_only
class RRSetRoutingPolicyWrrPolicyWrrPolicyItem(typing.TypedDict, total=False):
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
    header: ResponseHeader
    kind: str
    nextPageToken: str
    rrsets: _list[ResourceRecordSet]

@typing.type_check_only
class ResponseHeader(typing.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class ResponsePoliciesListResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    nextPageToken: str
    responsePolicies: _list[ResponsePolicy]

@typing.type_check_only
class ResponsePoliciesPatchResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    responsePolicy: ResponsePolicy

@typing.type_check_only
class ResponsePoliciesUpdateResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    responsePolicy: ResponsePolicy

@typing.type_check_only
class ResponsePolicy(typing.TypedDict, total=False):
    description: str
    gkeClusters: _list[ResponsePolicyGKECluster]
    id: str
    kind: str
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
    behavior: typing.Literal["BEHAVIOR_UNSPECIFIED", "BYPASS_RESPONSE_POLICY"]
    dnsName: str
    kind: str
    localData: ResponsePolicyRuleLocalData
    ruleName: str

@typing.type_check_only
class ResponsePolicyRuleLocalData(typing.TypedDict, total=False):
    localDatas: _list[ResourceRecordSet]

@typing.type_check_only
class ResponsePolicyRulesListResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    nextPageToken: str
    responsePolicyRules: _list[ResponsePolicyRule]

@typing.type_check_only
class ResponsePolicyRulesPatchResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    responsePolicyRule: ResponsePolicyRule

@typing.type_check_only
class ResponsePolicyRulesUpdateResponse(typing.TypedDict, total=False):
    header: ResponseHeader
    responsePolicyRule: ResponsePolicyRule
