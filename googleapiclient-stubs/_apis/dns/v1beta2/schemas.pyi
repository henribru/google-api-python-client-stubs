import typing

import typing_extensions

_list = list

@typing.type_check_only
class Change(typing_extensions.TypedDict, total=False):
    additions: _list[ResourceRecordSet]
    deletions: _list[ResourceRecordSet]
    id: str
    isServing: bool
    kind: str
    startTime: str
    status: typing_extensions.Literal["pending", "done"]

@typing.type_check_only
class ChangesListResponse(typing_extensions.TypedDict, total=False):
    changes: _list[Change]
    header: ResponseHeader
    kind: str
    nextPageToken: str

@typing.type_check_only
class DnsKey(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
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
    type: typing_extensions.Literal["keySigning", "zoneSigning"]

@typing.type_check_only
class DnsKeyDigest(typing_extensions.TypedDict, total=False):
    digest: str
    type: typing_extensions.Literal["sha1", "sha256", "sha384"]

@typing.type_check_only
class DnsKeySpec(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]
    keyLength: int
    keyType: typing_extensions.Literal["keySigning", "zoneSigning"]
    kind: str

@typing.type_check_only
class DnsKeysListResponse(typing_extensions.TypedDict, total=False):
    dnsKeys: _list[DnsKey]
    header: ResponseHeader
    kind: str
    nextPageToken: str

@typing.type_check_only
class ManagedZone(typing_extensions.TypedDict, total=False):
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
    visibility: typing_extensions.Literal["public", "private"]

@typing.type_check_only
class ManagedZoneDnsSecConfig(typing_extensions.TypedDict, total=False):
    defaultKeySpecs: _list[DnsKeySpec]
    kind: str
    nonExistence: typing_extensions.Literal["nsec", "nsec3"]
    state: typing_extensions.Literal["off", "on", "transfer"]

@typing.type_check_only
class ManagedZoneForwardingConfig(typing_extensions.TypedDict, total=False):
    kind: str
    targetNameServers: _list[ManagedZoneForwardingConfigNameServerTarget]

@typing.type_check_only
class ManagedZoneForwardingConfigNameServerTarget(
    typing_extensions.TypedDict, total=False
):
    forwardingPath: typing_extensions.Literal["default", "private"]
    ipv4Address: str
    ipv6Address: str
    kind: str

@typing.type_check_only
class ManagedZoneOperationsListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    kind: str
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ManagedZonePeeringConfig(typing_extensions.TypedDict, total=False):
    kind: str
    targetNetwork: ManagedZonePeeringConfigTargetNetwork

@typing.type_check_only
class ManagedZonePeeringConfigTargetNetwork(typing_extensions.TypedDict, total=False):
    deactivateTime: str
    kind: str
    networkUrl: str

@typing.type_check_only
class ManagedZonePrivateVisibilityConfig(typing_extensions.TypedDict, total=False):
    gkeClusters: _list[ManagedZonePrivateVisibilityConfigGKECluster]
    kind: str
    networks: _list[ManagedZonePrivateVisibilityConfigNetwork]

@typing.type_check_only
class ManagedZonePrivateVisibilityConfigGKECluster(
    typing_extensions.TypedDict, total=False
):
    gkeClusterName: str
    kind: str

@typing.type_check_only
class ManagedZonePrivateVisibilityConfigNetwork(
    typing_extensions.TypedDict, total=False
):
    kind: str
    networkUrl: str

@typing.type_check_only
class ManagedZoneReverseLookupConfig(typing_extensions.TypedDict, total=False):
    kind: str

@typing.type_check_only
class ManagedZoneServiceDirectoryConfig(typing_extensions.TypedDict, total=False):
    kind: str
    namespace: ManagedZoneServiceDirectoryConfigNamespace

@typing.type_check_only
class ManagedZoneServiceDirectoryConfigNamespace(
    typing_extensions.TypedDict, total=False
):
    deletionTime: str
    kind: str
    namespaceUrl: str

@typing.type_check_only
class ManagedZonesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    kind: str
    managedZones: _list[ManagedZone]
    nextPageToken: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    dnsKeyContext: OperationDnsKeyContext
    id: str
    kind: str
    startTime: str
    status: typing_extensions.Literal["pending", "done"]
    type: str
    user: str
    zoneContext: OperationManagedZoneContext

@typing.type_check_only
class OperationDnsKeyContext(typing_extensions.TypedDict, total=False):
    newValue: DnsKey
    oldValue: DnsKey

@typing.type_check_only
class OperationManagedZoneContext(typing_extensions.TypedDict, total=False):
    newValue: ManagedZone
    oldValue: ManagedZone

@typing.type_check_only
class PoliciesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    kind: str
    nextPageToken: str
    policies: _list[Policy]

@typing.type_check_only
class PoliciesPatchResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

@typing.type_check_only
class PoliciesUpdateResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    alternativeNameServerConfig: PolicyAlternativeNameServerConfig
    description: str
    enableInboundForwarding: bool
    enableLogging: bool
    id: str
    kind: str
    name: str
    networks: _list[PolicyNetwork]

@typing.type_check_only
class PolicyAlternativeNameServerConfig(typing_extensions.TypedDict, total=False):
    kind: str
    targetNameServers: _list[PolicyAlternativeNameServerConfigTargetNameServer]

@typing.type_check_only
class PolicyAlternativeNameServerConfigTargetNameServer(
    typing_extensions.TypedDict, total=False
):
    forwardingPath: typing_extensions.Literal["default", "private"]
    ipv4Address: str
    ipv6Address: str
    kind: str

@typing.type_check_only
class PolicyNetwork(typing_extensions.TypedDict, total=False):
    kind: str
    networkUrl: str

@typing.type_check_only
class Project(typing_extensions.TypedDict, total=False):
    id: str
    kind: str
    number: str
    quota: Quota

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    dnsKeysPerManagedZone: int
    gkeClustersPerManagedZone: int
    gkeClustersPerResponsePolicy: int
    itemsPerRoutingPolicy: int
    kind: str
    managedZones: int
    managedZonesPerGkeCluster: int
    managedZonesPerNetwork: int
    networksPerManagedZone: int
    networksPerPolicy: int
    policies: int
    resourceRecordsPerRrset: int
    responsePolicyRulesPerResponsePolicy: int
    rrsetAdditionsPerChange: int
    rrsetDeletionsPerChange: int
    rrsetsPerManagedZone: int
    targetNameServersPerManagedZone: int
    targetNameServersPerPolicy: int
    totalRrdataSizePerChange: int
    whitelistedKeySpecs: _list[DnsKeySpec]

@typing.type_check_only
class RRSetRoutingPolicy(typing_extensions.TypedDict, total=False):
    geo: RRSetRoutingPolicyGeoPolicy
    geoPolicy: RRSetRoutingPolicyGeoPolicy
    kind: str
    wrr: RRSetRoutingPolicyWrrPolicy
    wrrPolicy: RRSetRoutingPolicyWrrPolicy

@typing.type_check_only
class RRSetRoutingPolicyGeoPolicy(typing_extensions.TypedDict, total=False):
    failovers: _list[RRSetRoutingPolicyGeoPolicyGeoPolicyItem]
    items: _list[RRSetRoutingPolicyGeoPolicyGeoPolicyItem]
    kind: str

@typing.type_check_only
class RRSetRoutingPolicyGeoPolicyGeoPolicyItem(
    typing_extensions.TypedDict, total=False
):
    kind: str
    location: str
    rrdatas: _list[str]
    signatureRrdatas: _list[str]

@typing.type_check_only
class RRSetRoutingPolicyWrrPolicy(typing_extensions.TypedDict, total=False):
    items: _list[RRSetRoutingPolicyWrrPolicyWrrPolicyItem]
    kind: str

@typing.type_check_only
class RRSetRoutingPolicyWrrPolicyWrrPolicyItem(
    typing_extensions.TypedDict, total=False
):
    kind: str
    rrdatas: _list[str]
    signatureRrdatas: _list[str]
    weight: float

@typing.type_check_only
class ResourceRecordSet(typing_extensions.TypedDict, total=False):
    kind: str
    name: str
    routingPolicy: RRSetRoutingPolicy
    rrdatas: _list[str]
    signatureRrdatas: _list[str]
    ttl: int
    type: str

@typing.type_check_only
class ResourceRecordSetsListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    kind: str
    nextPageToken: str
    rrsets: _list[ResourceRecordSet]

@typing.type_check_only
class ResponseHeader(typing_extensions.TypedDict, total=False):
    operationId: str

@typing.type_check_only
class ResponsePoliciesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    nextPageToken: str
    responsePolicies: _list[ResponsePolicy]

@typing.type_check_only
class ResponsePoliciesPatchResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    responsePolicy: ResponsePolicy

@typing.type_check_only
class ResponsePoliciesUpdateResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    responsePolicy: ResponsePolicy

@typing.type_check_only
class ResponsePolicy(typing_extensions.TypedDict, total=False):
    description: str
    gkeClusters: _list[ResponsePolicyGKECluster]
    id: str
    kind: str
    networks: _list[ResponsePolicyNetwork]
    responsePolicyName: str

@typing.type_check_only
class ResponsePolicyGKECluster(typing_extensions.TypedDict, total=False):
    gkeClusterName: str
    kind: str

@typing.type_check_only
class ResponsePolicyNetwork(typing_extensions.TypedDict, total=False):
    kind: str
    networkUrl: str

@typing.type_check_only
class ResponsePolicyRule(typing_extensions.TypedDict, total=False):
    behavior: typing_extensions.Literal["behaviorUnspecified", "bypassResponsePolicy"]
    dnsName: str
    kind: str
    localData: ResponsePolicyRuleLocalData
    ruleName: str

@typing.type_check_only
class ResponsePolicyRuleLocalData(typing_extensions.TypedDict, total=False):
    localDatas: _list[ResourceRecordSet]

@typing.type_check_only
class ResponsePolicyRulesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    nextPageToken: str
    responsePolicyRules: _list[ResponsePolicyRule]

@typing.type_check_only
class ResponsePolicyRulesPatchResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    responsePolicyRule: ResponsePolicyRule

@typing.type_check_only
class ResponsePolicyRulesUpdateResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    responsePolicyRule: ResponsePolicyRule
