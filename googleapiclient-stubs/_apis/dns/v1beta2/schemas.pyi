import typing

import typing_extensions

class ManagedZoneServiceDirectoryConfigNamespace(
    typing_extensions.TypedDict, total=False
):
    namespaceUrl: str
    kind: str
    deletionTime: str

class ManagedZoneForwardingConfigNameServerTarget(
    typing_extensions.TypedDict, total=False
):
    kind: str
    ipv4Address: str
    forwardingPath: typing_extensions.Literal["default", "private"]

class DnsKeySpec(typing_extensions.TypedDict, total=False):
    keyType: typing_extensions.Literal["keySigning", "zoneSigning"]
    keyLength: int
    kind: str
    algorithm: typing_extensions.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]

class ManagedZonePrivateVisibilityConfigNetwork(
    typing_extensions.TypedDict, total=False
):
    kind: str
    networkUrl: str

class PoliciesUpdateResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

class ResourceRecordSet(typing_extensions.TypedDict, total=False):
    signatureRrdatas: typing.List[str]
    type: str
    ttl: int
    kind: str
    rrdatas: typing.List[str]
    name: str

class ManagedZoneServiceDirectoryConfig(typing_extensions.TypedDict, total=False):
    namespace: ManagedZoneServiceDirectoryConfigNamespace
    kind: str

class PolicyAlternativeNameServerConfig(typing_extensions.TypedDict, total=False):
    kind: str
    targetNameServers: typing.List[PolicyAlternativeNameServerConfigTargetNameServer]

class Operation(typing_extensions.TypedDict, total=False):
    startTime: str
    user: str
    kind: str
    type: str
    id: str
    status: typing_extensions.Literal["pending", "done"]
    zoneContext: OperationManagedZoneContext
    dnsKeyContext: OperationDnsKeyContext

class Change(typing_extensions.TypedDict, total=False):
    startTime: str
    kind: str
    additions: typing.List[ResourceRecordSet]
    status: typing_extensions.Literal["pending", "done"]
    id: str
    isServing: bool
    deletions: typing.List[ResourceRecordSet]

class PoliciesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    policies: typing.List[Policy]
    header: ResponseHeader

class ResourceRecordSetsListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    nextPageToken: str
    kind: str
    rrsets: typing.List[ResourceRecordSet]

class DnsKeyDigest(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["sha1", "sha256", "sha384"]
    digest: str

class ManagedZonePrivateVisibilityConfig(typing_extensions.TypedDict, total=False):
    kind: str
    networks: typing.List[ManagedZonePrivateVisibilityConfigNetwork]

class ManagedZonesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    kind: str
    nextPageToken: str
    managedZones: typing.List[ManagedZone]

class DnsKeysListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    header: ResponseHeader
    dnsKeys: typing.List[DnsKey]

class ManagedZoneForwardingConfig(typing_extensions.TypedDict, total=False):
    targetNameServers: typing.List[ManagedZoneForwardingConfigNameServerTarget]
    kind: str

class Policy(typing_extensions.TypedDict, total=False):
    kind: str
    networks: typing.List[PolicyNetwork]
    enableInboundForwarding: bool
    id: str
    alternativeNameServerConfig: PolicyAlternativeNameServerConfig
    enableLogging: bool
    name: str
    description: str

class OperationDnsKeyContext(typing_extensions.TypedDict, total=False):
    oldValue: DnsKey
    newValue: DnsKey

class PolicyNetwork(typing_extensions.TypedDict, total=False):
    networkUrl: str
    kind: str

class ChangesListResponse(typing_extensions.TypedDict, total=False):
    changes: typing.List[Change]
    header: ResponseHeader
    kind: str
    nextPageToken: str

class ManagedZonePeeringConfigTargetNetwork(typing_extensions.TypedDict, total=False):
    kind: str
    deactivateTime: str
    networkUrl: str

class OperationManagedZoneContext(typing_extensions.TypedDict, total=False):
    oldValue: ManagedZone
    newValue: ManagedZone

class ManagedZoneOperationsListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    header: ResponseHeader
    operations: typing.List[Operation]
    nextPageToken: str

class Project(typing_extensions.TypedDict, total=False):
    quota: Quota
    id: str
    number: str
    kind: str

class ManagedZone(typing_extensions.TypedDict, total=False):
    description: str
    visibility: typing_extensions.Literal["public", "private"]
    name: str
    privateVisibilityConfig: ManagedZonePrivateVisibilityConfig
    forwardingConfig: ManagedZoneForwardingConfig
    creationTime: str
    peeringConfig: ManagedZonePeeringConfig
    reverseLookupConfig: ManagedZoneReverseLookupConfig
    dnssecConfig: ManagedZoneDnsSecConfig
    dnsName: str
    id: str
    labels: typing.Dict[str, typing.Any]
    serviceDirectoryConfig: ManagedZoneServiceDirectoryConfig
    nameServers: typing.List[str]
    kind: str
    nameServerSet: str

class ManagedZoneDnsSecConfig(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["off", "on", "transfer"]
    kind: str
    nonExistence: typing_extensions.Literal["nsec", "nsec3"]
    defaultKeySpecs: typing.List[DnsKeySpec]

class ResponseHeader(typing_extensions.TypedDict, total=False):
    operationId: str

class ManagedZoneReverseLookupConfig(typing_extensions.TypedDict, total=False):
    kind: str

class PolicyAlternativeNameServerConfigTargetNameServer(
    typing_extensions.TypedDict, total=False
):
    ipv4Address: str
    forwardingPath: typing_extensions.Literal["default", "private"]
    kind: str

class ManagedZonePeeringConfig(typing_extensions.TypedDict, total=False):
    targetNetwork: ManagedZonePeeringConfigTargetNetwork
    kind: str

class PoliciesPatchResponse(typing_extensions.TypedDict, total=False):
    policy: Policy
    header: ResponseHeader

class Quota(typing_extensions.TypedDict, total=False):
    networksPerPolicy: int
    kind: str
    totalRrdataSizePerChange: int
    whitelistedKeySpecs: typing.List[DnsKeySpec]
    targetNameServersPerManagedZone: int
    managedZonesPerNetwork: int
    networksPerManagedZone: int
    rrsetsPerManagedZone: int
    resourceRecordsPerRrset: int
    policies: int
    dnsKeysPerManagedZone: int
    rrsetAdditionsPerChange: int
    rrsetDeletionsPerChange: int
    targetNameServersPerPolicy: int
    managedZones: int

class DnsKey(typing_extensions.TypedDict, total=False):
    keyLength: int
    description: str
    keyTag: int
    algorithm: typing_extensions.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]
    id: str
    kind: str
    publicKey: str
    digests: typing.List[DnsKeyDigest]
    creationTime: str
    isActive: bool
    type: typing_extensions.Literal["keySigning", "zoneSigning"]
