import typing

_list = list

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    attributes: Attributes
    createTime: str
    description: str
    displayName: str
    name: str
    scope: Scope
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"]
    uid: str
    updateTime: str

@typing.type_check_only
class Attributes(typing.TypedDict, total=False):
    businessOwners: _list[ContactInfo]
    criticality: Criticality
    developerOwners: _list[ContactInfo]
    environment: Environment
    operatorOwners: _list[ContactInfo]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Boundary(typing.TypedDict, total=False):
    createTime: str
    crmNode: str
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "AUTOMATIC", "MANUAL", "MANAGED_AUTOMATIC"]
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Channel(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class ContactInfo(typing.TypedDict, total=False):
    channel: Channel
    displayName: str
    email: str

@typing.type_check_only
class Criticality(typing.TypedDict, total=False):
    level: str
    missionCritical: bool
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class DetachServiceProjectAttachmentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DetachServiceProjectAttachmentResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class DiscoveredService(typing.TypedDict, total=False):
    name: str
    serviceProperties: ServiceProperties
    serviceReference: ServiceReference

@typing.type_check_only
class DiscoveredWorkload(typing.TypedDict, total=False):
    name: str
    workloadProperties: WorkloadProperties
    workloadReference: WorkloadReference

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    environment: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendedMetadata(typing.TypedDict, total=False):
    metadataStruct: dict[str, typing.Any]

@typing.type_check_only
class ExtendedMetadataSchema(typing.TypedDict, total=False):
    jsonSchema: str
    name: str
    schemaVersion: str

@typing.type_check_only
class FindUnregisteredServicesResponse(typing.TypedDict, total=False):
    discoveredServices: _list[DiscoveredService]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class FindUnregisteredWorkloadsResponse(typing.TypedDict, total=False):
    discoveredWorkloads: _list[DiscoveredWorkload]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class FunctionalType(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "AGENT", "MCP_SERVER", "ENDPOINT"]

@typing.type_check_only
class Identity(typing.TypedDict, total=False):
    principal: str

@typing.type_check_only
class ListApplicationsResponse(typing.TypedDict, total=False):
    applications: _list[Application]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredServicesResponse(typing.TypedDict, total=False):
    discoveredServices: _list[DiscoveredService]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredWorkloadsResponse(typing.TypedDict, total=False):
    discoveredWorkloads: _list[DiscoveredWorkload]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExtendedMetadataSchemasResponse(typing.TypedDict, total=False):
    extendedMetadataSchemas: _list[ExtendedMetadataSchema]
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
class ListServiceProjectAttachmentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    serviceProjectAttachments: _list[ServiceProjectAttachment]
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]
    unreachable: _list[str]

@typing.type_check_only
class ListWorkloadsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workloads: _list[Workload]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LookupDiscoveredServiceResponse(typing.TypedDict, total=False):
    discoveredService: DiscoveredService

@typing.type_check_only
class LookupDiscoveredWorkloadResponse(typing.TypedDict, total=False):
    discoveredWorkload: DiscoveredWorkload

@typing.type_check_only
class LookupServiceProjectAttachmentResponse(typing.TypedDict, total=False):
    serviceProjectAttachment: ServiceProjectAttachment

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
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RegistrationType(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "EXCLUSIVE", "SHARED"]

@typing.type_check_only
class Scope(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "REGIONAL", "GLOBAL"]

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    attributes: Attributes
    createTime: str
    description: str
    discoveredService: str
    displayName: str
    name: str
    serviceProperties: ServiceProperties
    serviceReference: ServiceReference
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "DETACHED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class ServiceProjectAttachment(typing.TypedDict, total=False):
    createTime: str
    name: str
    serviceProject: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"]
    uid: str

@typing.type_check_only
class ServiceProperties(typing.TypedDict, total=False):
    extendedMetadata: dict[str, typing.Any]
    functionalType: FunctionalType
    gcpProject: str
    identity: Identity
    location: str
    registrationType: RegistrationType
    zone: str

@typing.type_check_only
class ServiceReference(typing.TypedDict, total=False):
    path: str
    uri: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Workload(typing.TypedDict, total=False):
    attributes: Attributes
    createTime: str
    description: str
    discoveredWorkload: str
    displayName: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "DETACHED"
    ]
    uid: str
    updateTime: str
    workloadProperties: WorkloadProperties
    workloadReference: WorkloadReference

@typing.type_check_only
class WorkloadProperties(typing.TypedDict, total=False):
    extendedMetadata: dict[str, typing.Any]
    functionalType: FunctionalType
    gcpProject: str
    identity: Identity
    location: str
    zone: str

@typing.type_check_only
class WorkloadReference(typing.TypedDict, total=False):
    uri: str
