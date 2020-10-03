import typing

import typing_extensions

class CreateVersionMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class SslSettings(typing_extensions.TypedDict, total=False):
    isManagedCertificate: bool
    certificateId: str

class ListAuthorizedCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: typing.List[AuthorizedCertificate]
    nextPageToken: str

class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domains: typing.List[AuthorizedDomain]

class OperationMetadataV1Alpha(typing_extensions.TypedDict, total=False):
    ephemeralMessage: str
    insertTime: str
    createVersionMetadata: CreateVersionMetadataV1Alpha
    warning: typing.List[str]
    target: str
    user: str
    endTime: str
    method: str

class CertificateRawData(typing_extensions.TypedDict, total=False):
    privateKey: str
    publicCertificate: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class OperationMetadataV1Beta(typing_extensions.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Beta
    method: str
    warning: typing.List[str]
    ephemeralMessage: str
    insertTime: str
    target: str
    endTime: str
    user: str

class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["A", "AAAA", "CNAME"]

class OperationMetadataV1(typing_extensions.TypedDict, total=False):
    insertTime: str
    warning: typing.List[str]
    createVersionMetadata: CreateVersionMetadataV1
    user: str
    method: str
    target: str
    ephemeralMessage: str
    endTime: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status
    done: bool

class Empty(typing_extensions.TypedDict, total=False): ...

class CreateVersionMetadataV1(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domainMappings: typing.List[DomainMapping]

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    locationId: str
    name: str
    labels: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class CreateVersionMetadataV1Beta(typing_extensions.TypedDict, total=False):
    cloudBuildId: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

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

class AuthorizedCertificate(typing_extensions.TypedDict, total=False):
    domainNames: typing.List[str]
    name: str
    id: str
    certificateRawData: CertificateRawData
    domainMappingsCount: int
    expireTime: str
    visibleDomainMappings: typing.List[str]
    managedCertificate: ManagedCertificate
    displayName: str

class LocationMetadata(typing_extensions.TypedDict, total=False):
    standardEnvironmentAvailable: bool
    flexibleEnvironmentAvailable: bool

class DomainMapping(typing_extensions.TypedDict, total=False):
    resourceRecords: typing.List[ResourceRecord]
    name: str
    id: str
    sslSettings: SslSettings

class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str
