import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CertVerification(typing_extensions.TypedDict, total=False):
    dns: DnsUpdates
    http: HttpUpdate

@typing.type_check_only
class CustomDomainMetadata(typing_extensions.TypedDict, total=False):
    certState: typing_extensions.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing_extensions.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_MISMATCH",
        "HOST_CONFLICT",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    liveMigrationSteps: _list[LiveMigrationStep]
    ownershipState: typing_extensions.Literal[
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
class DnsRecord(typing_extensions.TypedDict, total=False):
    domainName: str
    rdata: str
    requiredAction: typing_extensions.Literal["NONE", "ADD", "REMOVE"]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "A", "CNAME", "TXT", "AAAA", "CAA"
    ]

@typing.type_check_only
class DnsRecordSet(typing_extensions.TypedDict, total=False):
    checkError: Status
    domainName: str
    records: _list[DnsRecord]

@typing.type_check_only
class DnsUpdates(typing_extensions.TypedDict, total=False):
    checkTime: str
    desired: _list[DnsRecordSet]
    discovered: _list[DnsRecordSet]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class HttpUpdate(typing_extensions.TypedDict, total=False):
    checkError: Status
    desired: str
    discovered: str
    lastCheckTime: str
    path: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class LiveMigrationStep(typing_extensions.TypedDict, total=False):
    certVerification: CertVerification
    dnsUpdates: DnsUpdates
    issues: _list[Status]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PREPARING",
        "PENDING",
        "INCOMPLETE",
        "PROCESSING",
        "COMPLETE",
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
