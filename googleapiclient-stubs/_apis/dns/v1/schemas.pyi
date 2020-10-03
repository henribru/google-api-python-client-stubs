import typing

import typing_extensions

class ManagedZoneForwardingConfigNameServerTarget(
    typing_extensions.TypedDict, total=False
):
    ipv4Address: str
    kind: str
    forwardingPath: typing_extensions.Literal["default", "private"]

class PoliciesUpdateResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

class OperationDnsKeyContext(typing_extensions.TypedDict, total=False):
    newValue: DnsKey
    oldValue: DnsKey

class Project(typing_extensions.TypedDict, total=False):
    quota: Quota
    kind: str
    id: str
    number: str

class ManagedZonePeeringConfig(typing_extensions.TypedDict, total=False):
    kind: str
    targetNetwork: ManagedZonePeeringConfigTargetNetwork

class Change(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal["pending", "done"]
    kind: str
    startTime: str
    isServing: bool
    additions: typing.List[ResourceRecordSet]
    id: str
    deletions: typing.List[ResourceRecordSet]

class ManagedZonesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    managedZones: typing.List[ManagedZone]
    kind: str
    header: ResponseHeader

class ManagedZonePrivateVisibilityConfigNetwork(
    typing_extensions.TypedDict, total=False
):
    kind: str
    networkUrl: str

class ManagedZonePrivateVisibilityConfig(typing_extensions.TypedDict, total=False):
    networks: typing.List[ManagedZonePrivateVisibilityConfigNetwork]
    kind: str

class PoliciesPatchResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    policy: Policy

class PoliciesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    kind: str
    nextPageToken: str
    policies: typing.List[Policy]

class PolicyAlternativeNameServerConfig(typing_extensions.TypedDict, total=False):
    targetNameServers: typing.List[PolicyAlternativeNameServerConfigTargetNameServer]
    kind: str

class ManagedZoneDnsSecConfig(typing_extensions.TypedDict, total=False):
    defaultKeySpecs: typing.List[DnsKeySpec]
    state: typing_extensions.Literal["off", "on", "transfer"]
    nonExistence: typing_extensions.Literal["nsec", "nsec3"]
    kind: str

class ManagedZoneReverseLookupConfig(typing_extensions.TypedDict, total=False):
    kind: str

class ChangesListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    changes: typing.List[Change]
    nextPageToken: str
    kind: str

class ResponseHeader(typing_extensions.TypedDict, total=False):
    operationId: str

class ManagedZoneForwardingConfig(typing_extensions.TypedDict, total=False):
    targetNameServers: typing.List[ManagedZoneForwardingConfigNameServerTarget]
    kind: str

class ManagedZonePeeringConfigTargetNetwork(typing_extensions.TypedDict, total=False):
    networkUrl: str
    kind: str
    deactivateTime: str

class DnsKeysListResponse(typing_extensions.TypedDict, total=False):
    kind: str
    header: ResponseHeader
    dnsKeys: typing.List[DnsKey]
    nextPageToken: str

class Quota(typing_extensions.TypedDict, total=False):
    policies: int
    networksPerPolicy: int
    managedZonesPerNetwork: int
    resourceRecordsPerRrset: int
    rrsetDeletionsPerChange: int
    networksPerManagedZone: int
    rrsetsPerManagedZone: int
    totalRrdataSizePerChange: int
    rrsetAdditionsPerChange: int
    targetNameServersPerManagedZone: int
    targetNameServersPerPolicy: int
    whitelistedKeySpecs: typing.List[DnsKeySpec]
    dnsKeysPerManagedZone: int
    kind: str
    managedZones: int

class Operation(typing_extensions.TypedDict, total=False):
    dnsKeyContext: OperationDnsKeyContext
    type: str
    kind: str
    zoneContext: OperationManagedZoneContext
    user: str
    status: typing_extensions.Literal["pending", "done"]
    startTime: str
    id: str

class ResourceRecordSetsListResponse(typing_extensions.TypedDict, total=False):
    header: ResponseHeader
    nextPageToken: str
    kind: str
    rrsets: typing.List[ResourceRecordSet]

class PolicyNetwork(typing_extensions.TypedDict, total=False):
    kind: str
    networkUrl: str

class ManagedZoneOperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    header: ResponseHeader
    kind: str
    operations: typing.List[Operation]

class DnsKeySpec(typing_extensions.TypedDict, total=False):
    kind: str
    keyLength: int
    algorithm: typing_extensions.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]
    keyType: typing_extensions.Literal["keySigning", "zoneSigning"]

class OperationManagedZoneContext(typing_extensions.TypedDict, total=False):
    oldValue: ManagedZone
    newValue: ManagedZone

class Policy(typing_extensions.TypedDict, total=False):
    enableInboundForwarding: bool
    kind: str
    description: str
    enableLogging: bool
    networks: typing.List[PolicyNetwork]
    name: str
    alternativeNameServerConfig: PolicyAlternativeNameServerConfig
    id: str

class DnsKeyDigest(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["sha1", "sha256", "sha384"]
    digest: str

class DnsKey(typing_extensions.TypedDict, total=False):
    kind: str
    isActive: bool
    algorithm: typing_extensions.Literal[
        "rsasha1", "rsasha256", "rsasha512", "ecdsap256sha256", "ecdsap384sha384"
    ]
    publicKey: str
    keyTag: int
    creationTime: str
    id: str
    digests: typing.List[DnsKeyDigest]
    keyLength: int
    description: str
    type: typing_extensions.Literal["keySigning", "zoneSigning"]

class ManagedZone(typing_extensions.TypedDict, total=False):
    visibility: typing_extensions.Literal["public", "private"]
    forwardingConfig: ManagedZoneForwardingConfig
    nameServers: typing.List[str]
    name: str
    peeringConfig: ManagedZonePeeringConfig
    privateVisibilityConfig: ManagedZonePrivateVisibilityConfig
    dnssecConfig: ManagedZoneDnsSecConfig
    id: str
    kind: str
    reverseLookupConfig: ManagedZoneReverseLookupConfig
    nameServerSet: str
    dnsName: str
    labels: typing.Dict[str, typing.Any]
    creationTime: str
    description: str

class ResourceRecordSet(typing_extensions.TypedDict, total=False):
    rrdatas: typing.List[str]
    signatureRrdatas: typing.List[str]
    ttl: int
    kind: str
    name: str
    type: str

class PolicyAlternativeNameServerConfigTargetNameServer(
    typing_extensions.TypedDict, total=False
):
    ipv4Address: str
    forwardingPath: typing_extensions.Literal["default", "private"]
    kind: str
