import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuthorizedCertificate(typing_extensions.TypedDict, total=False):
    certificateRawData: CertificateRawData
    displayName: str
    domainMappingsCount: int
    domainNames: _list[str]
    expireTime: str
    id: str
    managedCertificate: ManagedCertificate
    name: str
    visibleDomainMappings: _list[str]

@typing.type_check_only
class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class CertificateRawData(typing_extensions.TypedDict, total=False):
    privateKey: str
    publicCertificate: str

@typing.type_check_only
class CreateVersionMetadataV1(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Beta(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class DomainMapping(typing_extensions.TypedDict, total=False):
    id: str
    name: str
    resourceRecords: _list[ResourceRecord]
    sslSettings: SslSettings

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAppengineV1betaLocationMetadata(typing_extensions.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ListAuthorizedCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: _list[AuthorizedCertificate]
    nextPageToken: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    domainMappings: _list[DomainMapping]
    nextPageToken: str

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
class LocationMetadata(typing_extensions.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ManagedCertificate(typing_extensions.TypedDict, total=False):
    lastRenewalTime: str
    status: typing_extensions.Literal[
        "UNSPECIFIED_STATUS",
        "OK",
        "PENDING",
        "FAILED_RETRYING_INTERNAL",
        "FAILED_RETRYING_NOT_VISIBLE",
        "FAILED_PERMANENTLY_NOT_VISIBLE",
        "FAILED_RETRYING_CAA_FORBIDDEN",
        "FAILED_RETRYING_CAA_CHECKING",
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Alpha
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Beta(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Beta
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["A", "AAAA", "CNAME"]

@typing.type_check_only
class SslSettings(typing_extensions.TypedDict, total=False):
    certificateId: str
    isManagedCertificate: bool

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
