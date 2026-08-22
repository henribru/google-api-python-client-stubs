import typing

_list = list

@typing.type_check_only
class AuthorizedCertificate(typing.TypedDict, total=False):
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
class AuthorizedDomain(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class CertificateRawData(typing.TypedDict, total=False):
    privateKey: str
    publicCertificate: str

@typing.type_check_only
class ContainerState(typing.TypedDict, total=False):
    currentReasons: Reasons
    previousReasons: Reasons
    state: typing.Literal["UNKNOWN_STATE", "ON", "OFF", "DELETED"]

@typing.type_check_only
class CreateVersionMetadataV1(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Alpha(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class CreateVersionMetadataV1Beta(typing.TypedDict, total=False):
    cloudBuildId: str

@typing.type_check_only
class DomainMapping(typing.TypedDict, total=False):
    id: str
    name: str
    resourceRecords: _list[ResourceRecord]
    sslSettings: SslSettings

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GceTag(typing.TypedDict, total=False):
    parent: _list[str]
    tag: str

@typing.type_check_only
class GoogleAppengineV1betaLocationMetadata(typing.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ListAuthorizedCertificatesResponse(typing.TypedDict, total=False):
    certificates: _list[AuthorizedCertificate]
    nextPageToken: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListDomainMappingsResponse(typing.TypedDict, total=False):
    domainMappings: _list[DomainMapping]
    nextPageToken: str

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
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    flexibleEnvironmentAvailable: bool
    searchApiAvailable: bool
    standardEnvironmentAvailable: bool

@typing.type_check_only
class ManagedCertificate(typing.TypedDict, total=False):
    lastRenewalTime: str
    status: typing.Literal[
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
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadataV1(typing.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Alpha(typing.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Alpha
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class OperationMetadataV1Beta(typing.TypedDict, total=False):
    createVersionMetadata: CreateVersionMetadataV1Beta
    endTime: str
    ephemeralMessage: str
    insertTime: str
    method: str
    target: str
    user: str
    warning: _list[str]

@typing.type_check_only
class ProjectEvent(typing.TypedDict, total=False):
    eventId: str
    phase: typing.Literal[
        "CONTAINER_EVENT_PHASE_UNSPECIFIED",
        "BEFORE_RESOURCE_HANDLING",
        "AFTER_RESOURCE_HANDLING",
    ]
    projectMetadata: ProjectsMetadata
    state: ContainerState

@typing.type_check_only
class ProjectsMetadata(typing.TypedDict, total=False):
    consumerProjectId: str
    consumerProjectNumber: str
    consumerProjectState: typing.Literal["UNKNOWN_STATE", "ON", "OFF", "DELETED"]
    gceTag: _list[GceTag]
    isGceProjectDeprovisioning: bool
    p4ServiceAccount: str
    producerProjectId: str
    producerProjectNumber: str
    tenantProjectId: str
    tenantProjectNumber: str

@typing.type_check_only
class Reasons(typing.TypedDict, total=False):
    abuse: typing.Literal[
        "ABUSE_UNKNOWN_REASON", "ABUSE_CONTROL_PLANE_SYNC", "SUSPEND", "REINSTATE"
    ]
    billing: typing.Literal[
        "BILLING_UNKNOWN_REASON",
        "BILLING_CONTROL_PLANE_SYNC",
        "PROBATION",
        "CLOSE",
        "OPEN",
    ]
    dataGovernance: typing.Literal[
        "DATA_GOVERNANCE_UNKNOWN_REASON",
        "DATA_GOVERNANCE_CONTROL_PLANE_SYNC",
        "HIDE",
        "UNHIDE",
        "PURGE",
    ]
    serviceActivation: typing.Literal[
        "SERVICE_ACTIVATION_STATUS_UNSPECIFIED",
        "SERVICE_ACTIVATION_ENABLED",
        "SERVICE_ACTIVATION_DISABLED",
        "SERVICE_ACTIVATION_DISABLED_FULL",
        "SERVICE_ACTIVATION_UNKNOWN_REASON",
    ]
    serviceManagement: typing.Literal[
        "SERVICE_MANAGEMENT_UNKNOWN_REASON",
        "SERVICE_MANAGEMENT_CONTROL_PLANE_SYNC",
        "ACTIVATION",
        "PREPARE_DEACTIVATION",
        "ABORT_DEACTIVATION",
        "COMMIT_DEACTIVATION",
    ]

@typing.type_check_only
class ResourceEvent(typing.TypedDict, total=False):
    eventId: str
    name: str
    state: ContainerState

@typing.type_check_only
class ResourceRecord(typing.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing.Literal["A", "AAAA", "CNAME"]

@typing.type_check_only
class SslSettings(typing.TypedDict, total=False):
    certificateId: str
    isManagedCertificate: bool

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
