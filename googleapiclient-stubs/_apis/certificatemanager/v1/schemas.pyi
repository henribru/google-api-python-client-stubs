import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuthorizationAttemptInfo(typing_extensions.TypedDict, total=False):
    details: str
    domain: str
    failureReason: typing_extensions.Literal[
        "FAILURE_REASON_UNSPECIFIED", "CONFIG", "CAA", "RATE_LIMITED"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "AUTHORIZING", "AUTHORIZED", "FAILED"
    ]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Certificate(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    expireTime: str
    labels: dict[str, typing.Any]
    managed: ManagedCertificate
    name: str
    pemCertificate: str
    sanDnsnames: _list[str]
    scope: typing_extensions.Literal["DEFAULT", "EDGE_CACHE"]
    selfManaged: SelfManagedCertificate
    updateTime: str

@typing.type_check_only
class CertificateAuthorityConfig(typing_extensions.TypedDict, total=False):
    certificateAuthorityServiceConfig: CertificateAuthorityServiceConfig

@typing.type_check_only
class CertificateAuthorityServiceConfig(typing_extensions.TypedDict, total=False):
    caPool: str

@typing.type_check_only
class CertificateIssuanceConfig(typing_extensions.TypedDict, total=False):
    certificateAuthorityConfig: CertificateAuthorityConfig
    createTime: str
    description: str
    keyAlgorithm: typing_extensions.Literal[
        "KEY_ALGORITHM_UNSPECIFIED", "RSA_2048", "ECDSA_P256"
    ]
    labels: dict[str, typing.Any]
    lifetime: str
    name: str
    rotationWindowPercentage: int
    updateTime: str

@typing.type_check_only
class CertificateMap(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    gclbTargets: _list[GclbTarget]
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class CertificateMapEntry(typing_extensions.TypedDict, total=False):
    certificates: _list[str]
    createTime: str
    description: str
    hostname: str
    labels: dict[str, typing.Any]
    matcher: typing_extensions.Literal["MATCHER_UNSPECIFIED", "PRIMARY"]
    name: str
    state: typing_extensions.Literal["SERVING_STATE_UNSPECIFIED", "ACTIVE", "PENDING"]
    updateTime: str

@typing.type_check_only
class DnsAuthorization(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    dnsResourceRecord: DnsResourceRecord
    domain: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class DnsResourceRecord(typing_extensions.TypedDict, total=False):
    data: str
    name: str
    type: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GclbTarget(typing_extensions.TypedDict, total=False):
    ipConfigs: _list[IpConfig]
    targetHttpsProxy: str
    targetSslProxy: str

@typing.type_check_only
class IpConfig(typing_extensions.TypedDict, total=False):
    ipAddress: str
    ports: _list[int]

@typing.type_check_only
class ListCertificateIssuanceConfigsResponse(typing_extensions.TypedDict, total=False):
    certificateIssuanceConfigs: _list[CertificateIssuanceConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateMapEntriesResponse(typing_extensions.TypedDict, total=False):
    certificateMapEntries: _list[CertificateMapEntry]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificateMapsResponse(typing_extensions.TypedDict, total=False):
    certificateMaps: _list[CertificateMap]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: _list[Certificate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDnsAuthorizationsResponse(typing_extensions.TypedDict, total=False):
    dnsAuthorizations: _list[DnsAuthorization]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagedCertificate(typing_extensions.TypedDict, total=False):
    authorizationAttemptInfo: _list[AuthorizationAttemptInfo]
    dnsAuthorizations: _list[str]
    domains: _list[str]
    issuanceConfig: str
    provisioningIssue: ProvisioningIssue
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PROVISIONING", "FAILED", "ACTIVE"
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ProvisioningIssue(typing_extensions.TypedDict, total=False):
    details: str
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED", "AUTHORIZATION_ISSUE", "RATE_LIMITED"
    ]

@typing.type_check_only
class SelfManagedCertificate(typing_extensions.TypedDict, total=False):
    pemCertificate: str
    pemPrivateKey: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
