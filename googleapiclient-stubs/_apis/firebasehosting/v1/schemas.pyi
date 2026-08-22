import typing

_list = list

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CertVerification(typing.TypedDict, total=False):
    dns: DnsUpdates
    http: HttpUpdate

@typing.type_check_only
class CustomDomainMetadata(typing.TypedDict, total=False):
    certState: typing.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_MISMATCH",
        "HOST_CONFLICT",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    liveMigrationSteps: _list[LiveMigrationStep]
    ownershipState: typing.Literal[
        "OWNERSHIP_STATE_UNSPECIFIED",
        "OWNERSHIP_MISSING",
        "OWNERSHIP_UNREACHABLE",
        "OWNERSHIP_MISMATCH",
        "OWNERSHIP_CONFLICT",
        "OWNERSHIP_PENDING",
        "OWNERSHIP_ACTIVE",
    ]
    quickSetupUpdates: DnsUpdates

@typing.type_check_only
class DnsRecord(typing.TypedDict, total=False):
    domainName: str
    rdata: str
    requiredAction: typing.Literal["NONE", "ADD", "REMOVE"]
    type: typing.Literal["TYPE_UNSPECIFIED", "A", "CNAME", "TXT", "AAAA", "CAA"]

@typing.type_check_only
class DnsRecordSet(typing.TypedDict, total=False):
    checkError: Status
    domainName: str
    records: _list[DnsRecord]

@typing.type_check_only
class DnsUpdates(typing.TypedDict, total=False):
    checkTime: str
    desired: _list[DnsRecordSet]
    discovered: _list[DnsRecordSet]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class HttpUpdate(typing.TypedDict, total=False):
    checkError: Status
    desired: str
    discovered: str
    lastCheckTime: str
    path: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class LiveMigrationStep(typing.TypedDict, total=False):
    certVerification: CertVerification
    dnsUpdates: DnsUpdates
    issues: _list[Status]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PREPARING",
        "PENDING",
        "INCOMPLETE",
        "PROCESSING",
        "COMPLETE",
    ]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
