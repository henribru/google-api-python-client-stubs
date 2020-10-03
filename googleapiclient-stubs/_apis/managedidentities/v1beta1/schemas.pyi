import typing

import typing_extensions

class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    tier: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]

class AttachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class OperationMetadata(typing_extensions.TypedDict, total=False):
    target: str
    statusDetail: str
    cancelRequested: bool
    createTime: str
    endTime: str
    apiVersion: str
    verb: str

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    updateTime: str
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    slmInstanceTemplate: str
    name: str
    producerMetadata: typing.Dict[str, typing.Any]
    tenantProjectId: str
    maintenanceSchedules: typing.Dict[str, typing.Any]
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    createTime: str
    consumerDefinedName: str
    labels: typing.Dict[str, typing.Any]
    softwareVersions: typing.Dict[str, typing.Any]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Domain(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "PERFORMING_MAINTENANCE",
        "UNAVAILABLE",
    ]
    statusMessage: str
    admin: str
    reservedIpRange: str
    createTime: str
    name: str
    labels: typing.Dict[str, typing.Any]
    updateTime: str
    auditLogsEnabled: bool
    fqdn: str
    trusts: typing.List[Trust]
    authorizedNetworks: typing.List[str]
    locations: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class GoogleCloudManagedidentitiesV1beta1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    target: str
    requestedCancellation: bool
    endTime: str
    apiVersion: str
    createTime: str
    verb: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    reason: str
    eligible: bool

class ReconfigureTrustRequest(typing_extensions.TypedDict, total=False):
    targetDomainName: str
    targetDnsIpAddresses: typing.List[str]

class ValidateTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    reason: str
    startTime: str
    sliName: str
    duration: str

class GoogleCloudManagedidentitiesV1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    target: str
    requestedCancellation: bool
    verb: str
    endTime: str
    apiVersion: str
    createTime: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DetachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    canReschedule: bool
    startTime: str
    rolloutManagementPolicy: str

class Trust(typing_extensions.TypedDict, total=False):
    selectiveAuthentication: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "DELETING",
        "CONNECTED",
        "DISCONNECTED",
    ]
    lastTrustHeartbeatTime: str
    targetDomainName: str
    createTime: str
    updateTime: str
    trustHandshakeSecret: str
    stateDescription: str
    trustType: typing_extensions.Literal["TRUST_TYPE_UNSPECIFIED", "FOREST", "EXTERNAL"]
    trustDirection: typing_extensions.Literal[
        "TRUST_DIRECTION_UNSPECIFIED", "INBOUND", "OUTBOUND", "BIDIRECTIONAL"
    ]
    targetDnsIpAddresses: typing.List[str]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...
class ResetAdminPasswordRequest(typing_extensions.TypedDict, total=False): ...

class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: typing.List[Domain]
    unreachable: typing.List[str]
    nextPageToken: str

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    description: str
    expression: str
    title: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

class GoogleCloudManagedidentitiesV1alpha1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    target: str
    apiVersion: str
    verb: str
    requestedCancellation: bool
    endTime: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int

class ResetAdminPasswordResponse(typing_extensions.TypedDict, total=False):
    password: str

class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    nodeId: str
    location: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    name: str
    error: Status

class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class Location(typing_extensions.TypedDict, total=False):
    locationId: str
    displayName: str
    metadata: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    name: str
