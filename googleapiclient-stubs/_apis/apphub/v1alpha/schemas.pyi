import typing

import typing_extensions

_list = list

@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    createTime: str
    description: str
    displayName: str
    name: str
    scope: Scope
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class AssetLocation(typing_extensions.TypedDict, total=False):
    ccfeRmsPath: str
    expected: IsolationExpectations
    extraParameters: _list[ExtraParameter]
    locationData: _list[LocationData]
    parentAsset: _list[CloudAsset]

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    businessOwners: _list[ContactInfo]
    criticality: Criticality
    developerOwners: _list[ContactInfo]
    environment: Environment
    operatorOwners: _list[ContactInfo]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BlobstoreLocation(typing_extensions.TypedDict, total=False):
    policyId: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class CloudAsset(typing_extensions.TypedDict, total=False):
    assetName: str
    assetType: str

@typing.type_check_only
class CloudAssetComposition(typing_extensions.TypedDict, total=False):
    childAsset: _list[CloudAsset]

@typing.type_check_only
class ContactInfo(typing_extensions.TypedDict, total=False):
    channel: Channel
    displayName: str
    email: str

@typing.type_check_only
class Criticality(typing_extensions.TypedDict, total=False):
    level: str
    missionCritical: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "MISSION_CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]

@typing.type_check_only
class DetachServiceProjectAttachmentRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class DetachServiceProjectAttachmentResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class DirectLocationAssignment(typing_extensions.TypedDict, total=False):
    location: _list[LocationAssignment]

@typing.type_check_only
class DiscoveredService(typing_extensions.TypedDict, total=False):
    name: str
    serviceProperties: ServiceProperties
    serviceReference: ServiceReference

@typing.type_check_only
class DiscoveredWorkload(typing_extensions.TypedDict, total=False):
    name: str
    workloadProperties: WorkloadProperties
    workloadReference: WorkloadReference

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    environment: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PRODUCTION", "STAGING", "TEST", "DEVELOPMENT"
    ]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtraParameter(typing_extensions.TypedDict, total=False):
    regionalMigDistributionPolicy: RegionalMigDistributionPolicy

@typing.type_check_only
class FindUnregisteredServicesResponse(typing_extensions.TypedDict, total=False):
    discoveredServices: _list[DiscoveredService]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class FindUnregisteredWorkloadsResponse(typing_extensions.TypedDict, total=False):
    discoveredWorkloads: _list[DiscoveredWorkload]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class IsolationExpectations(typing_extensions.TypedDict, total=False):
    requirementOverride: RequirementOverride
    ziOrgPolicy: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    ziRegionPolicy: typing_extensions.Literal[
        "ZI_REGION_POLICY_UNSPECIFIED",
        "ZI_REGION_POLICY_UNKNOWN",
        "ZI_REGION_POLICY_NOT_SET",
        "ZI_REGION_POLICY_FAIL_OPEN",
        "ZI_REGION_POLICY_FAIL_CLOSED",
    ]
    ziRegionState: typing_extensions.Literal[
        "ZI_REGION_UNSPECIFIED",
        "ZI_REGION_UNKNOWN",
        "ZI_REGION_NOT_ENABLED",
        "ZI_REGION_ENABLED",
    ]
    zoneIsolation: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    zoneSeparation: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]
    zsOrgPolicy: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]
    zsRegionState: typing_extensions.Literal[
        "ZS_REGION_UNSPECIFIED",
        "ZS_REGION_UNKNOWN",
        "ZS_REGION_NOT_ENABLED",
        "ZS_REGION_ENABLED",
    ]

@typing.type_check_only
class ListApplicationsResponse(typing_extensions.TypedDict, total=False):
    applications: _list[Application]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredServicesResponse(typing_extensions.TypedDict, total=False):
    discoveredServices: _list[DiscoveredService]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredWorkloadsResponse(typing_extensions.TypedDict, total=False):
    discoveredWorkloads: _list[DiscoveredWorkload]
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
class ListServiceProjectAttachmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    serviceProjectAttachments: _list[ServiceProjectAttachment]
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]
    unreachable: _list[str]

@typing.type_check_only
class ListWorkloadsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workloads: _list[Workload]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationAssignment(typing_extensions.TypedDict, total=False):
    location: str
    locationType: typing_extensions.Literal[
        "UNSPECIFIED",
        "CLUSTER",
        "POP",
        "CLOUD_ZONE",
        "CLOUD_REGION",
        "MULTI_REGION_GEO",
        "MULTI_REGION_JURISDICTION",
        "GLOBAL",
        "OTHER",
    ]

@typing.type_check_only
class LocationData(typing_extensions.TypedDict, total=False):
    blobstoreLocation: BlobstoreLocation
    childAssetLocation: CloudAssetComposition
    directLocation: DirectLocationAssignment
    gcpProjectProxy: TenantProjectProxy
    placerLocation: PlacerLocation
    spannerLocation: SpannerLocation

@typing.type_check_only
class LookupDiscoveredServiceResponse(typing_extensions.TypedDict, total=False):
    discoveredService: DiscoveredService

@typing.type_check_only
class LookupDiscoveredWorkloadResponse(typing_extensions.TypedDict, total=False):
    discoveredWorkload: DiscoveredWorkload

@typing.type_check_only
class LookupServiceProjectAttachmentResponse(typing_extensions.TypedDict, total=False):
    serviceProjectAttachment: ServiceProjectAttachment

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
class PlacerLocation(typing_extensions.TypedDict, total=False):
    placerConfig: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RegionalMigDistributionPolicy(typing_extensions.TypedDict, total=False):
    targetShape: int
    zones: _list[ZoneConfiguration]

@typing.type_check_only
class RequirementOverride(typing_extensions.TypedDict, total=False):
    ziOverride: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    zsOverride: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]

@typing.type_check_only
class Scope(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "REGIONAL", "GLOBAL"]

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    createTime: str
    description: str
    discoveredService: str
    displayName: str
    name: str
    serviceProperties: ServiceProperties
    serviceReference: ServiceReference
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "DETACHED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class ServiceProjectAttachment(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    serviceProject: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]
    uid: str

@typing.type_check_only
class ServiceProperties(typing_extensions.TypedDict, total=False):
    gcpProject: str
    location: str
    zone: str

@typing.type_check_only
class ServiceReference(typing_extensions.TypedDict, total=False):
    path: str
    uri: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SpannerLocation(typing_extensions.TypedDict, total=False):
    backupName: _list[str]
    dbName: _list[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TenantProjectProxy(typing_extensions.TypedDict, total=False):
    projectNumbers: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Workload(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    createTime: str
    description: str
    discoveredWorkload: str
    displayName: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "DETACHED"
    ]
    uid: str
    updateTime: str
    workloadProperties: WorkloadProperties
    workloadReference: WorkloadReference

@typing.type_check_only
class WorkloadProperties(typing_extensions.TypedDict, total=False):
    gcpProject: str
    location: str
    zone: str

@typing.type_check_only
class WorkloadReference(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class ZoneConfiguration(typing_extensions.TypedDict, total=False):
    zone: str
