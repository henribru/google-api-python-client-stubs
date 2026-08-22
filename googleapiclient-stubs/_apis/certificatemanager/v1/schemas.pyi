import typing

_list = list

@typing.type_check_only
class AllowlistedCertificate(typing.TypedDict, total=False):
    pemCertificate: str

@typing.type_check_only
class AuthorizationAttemptInfo(typing.TypedDict, total=False):
    attemptTime: str
    details: str
    domain: str
    failureReason: typing.Literal[
        "FAILURE_REASON_UNSPECIFIED", "CONFIG", "CAA", "RATE_LIMITED"
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "AUTHORIZING", "AUTHORIZED", "FAILED"]
    troubleshooting: Troubleshooting

@typing.type_check_only
class CNAME(typing.TypedDict, total=False):
    expectedData: str
    name: str
    resolvedData: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Certificate(typing.TypedDict, total=False):
    createTime: str
    description: str
    expireTime: str
    labels: dict[str, typing.Any]
    managed: ManagedCertificate
    managedIdentity: ManagedIdentityCertificate
    name: str
    pemCertificate: str
    sanDnsnames: _list[str]
    scope: typing.Literal["DEFAULT", "EDGE_CACHE", "ALL_REGIONS", "CLIENT_AUTH"]
    selfManaged: SelfManagedCertificate
    tags: dict[str, typing.Any]
    updateTime: str
    usedBy: _list[UsedBy]

@typing.type_check_only
class CertificateAuthorityConfig(typing.TypedDict, total=False):
    certificateAuthorityServiceConfig: CertificateAuthorityServiceConfig

@typing.type_check_only
class CertificateAuthorityServiceConfig(typing.TypedDict, total=False):
    caPool: str

@typing.type_check_only
class CertificateIssuanceConfig(typing.TypedDict, total=False):
    certificateAuthorityConfig: CertificateAuthorityConfig
    createTime: str
    description: str
    keyAlgorithm: typing.Literal["KEY_ALGORITHM_UNSPECIFIED", "RSA_2048", "ECDSA_P256"]
    labels: dict[str, typing.Any]
    lifetime: str
    name: str
    rotationWindowPercentage: int
    tags: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class CertificateMap(typing.TypedDict, total=False):
    createTime: str
    description: str
    gclbTargets: _list[GclbTarget]
    labels: dict[str, typing.Any]
    name: str
    tags: dict[str, typing.Any]
    updateTime: str

@typing.type_check_only
class CertificateMapEntry(typing.TypedDict, total=False):
    certificates: _list[str]
    createTime: str
    description: str
    hostname: str
    labels: dict[str, typing.Any]
    matcher: typing.Literal["MATCHER_UNSPECIFIED", "PRIMARY"]
    name: str
    state: typing.Literal["SERVING_STATE_UNSPECIFIED", "ACTIVE", "PENDING"]
    updateTime: str

@typing.type_check_only
class DnsAuthorization(typing.TypedDict, total=False):
    createTime: str
    description: str
    dnsResourceRecord: DnsResourceRecord
    domain: str
    labels: dict[str, typing.Any]
    name: str
    tags: dict[str, typing.Any]
    type: typing.Literal["TYPE_UNSPECIFIED", "FIXED_RECORD", "PER_PROJECT_RECORD"]
    updateTime: str

@typing.type_check_only
class DnsResourceRecord(typing.TypedDict, total=False):
    data: str
    name: str
    type: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GclbTarget(typing.TypedDict, total=False):
    ipConfigs: _list[IpConfig]
    targetHttpsProxy: str
    targetSslProxy: str

@typing.type_check_only
class IPs(typing.TypedDict, total=False):
    resolved: _list[str]
    serving: _list[str]
    servingOnAltPorts: _list[str]

@typing.type_check_only
class IntermediateCA(typing.TypedDict, total=False):
    pemCertificate: str

@typing.type_check_only
class IpConfig(typing.TypedDict, total=False):
    ipAddress: str
    ports: _list[int]

@typing.type_check_only
class ListCertificateIssuanceConfigsResponse(typing.TypedDict, total=False):
    certificateIssuanceConfigs: _list[CertificateIssuanceConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateMapEntriesResponse(typing.TypedDict, total=False):
    certificateMapEntries: _list[CertificateMapEntry]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateMapsResponse(typing.TypedDict, total=False):
    certificateMaps: _list[CertificateMap]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificatesResponse(typing.TypedDict, total=False):
    certificates: _list[Certificate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDnsAuthorizationsResponse(typing.TypedDict, total=False):
    dnsAuthorizations: _list[DnsAuthorization]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListTrustConfigsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    trustConfigs: _list[TrustConfig]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagedCertificate(typing.TypedDict, total=False):
    authorizationAttemptInfo: _list[AuthorizationAttemptInfo]
    dnsAuthorizations: _list[str]
    domains: _list[str]
    issuanceConfig: str
    provisioningIssue: ProvisioningIssue
    state: typing.Literal["STATE_UNSPECIFIED", "PROVISIONING", "FAILED", "ACTIVE"]

@typing.type_check_only
class ManagedIdentityCertificate(typing.TypedDict, total=False):
    identity: str
    provisioningIssue: ProvisioningIssue
    state: typing.Literal["STATE_UNSPECIFIED", "PROVISIONING", "FAILED", "ACTIVE"]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ProvisioningIssue(typing.TypedDict, total=False):
    details: str
    reason: typing.Literal["REASON_UNSPECIFIED", "AUTHORIZATION_ISSUE", "RATE_LIMITED"]

@typing.type_check_only
class SelfManagedCertificate(typing.TypedDict, total=False):
    pemCertificate: str
    pemPrivateKey: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Troubleshooting(typing.TypedDict, total=False):
    cname: CNAME
    ips: IPs
    issues: _list[
        typing.Literal[
            "ISSUE_UNSPECIFIED",
            "CNAME_MISMATCH",
            "RESOLVED_TO_NOT_SERVING",
            "RESOLVED_TO_SERVING_ON_ALT_PORTS",
            "NO_RESOLVED_IPS",
            "CERTIFICATE_NOT_ATTACHED",
        ]
    ]

@typing.type_check_only
class TrustAnchor(typing.TypedDict, total=False):
    pemCertificate: str

@typing.type_check_only
class TrustConfig(typing.TypedDict, total=False):
    allowlistedCertificates: _list[AllowlistedCertificate]
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    spiffeTrustStores: dict[str, typing.Any]
    tags: dict[str, typing.Any]
    trustStores: _list[TrustStore]
    updateTime: str

@typing.type_check_only
class TrustStore(typing.TypedDict, total=False):
    intermediateCas: _list[IntermediateCA]
    trustAnchors: _list[TrustAnchor]

@typing.type_check_only
class UsedBy(typing.TypedDict, total=False):
    name: str
