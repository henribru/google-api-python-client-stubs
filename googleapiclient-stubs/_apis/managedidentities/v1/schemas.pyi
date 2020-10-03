import typing

import typing_extensions

class DetachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class Location(typing_extensions.TypedDict, total=False):
    name: str
    labels: typing.Dict[str, typing.Any]
    displayName: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]

class AttachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class ValidateTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    duration: str
    sliName: str
    startTime: str
    reason: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    nodeId: str
    location: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]

class GoogleCloudManagedidentitiesV1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    requestedCancellation: bool
    verb: str
    createTime: str
    apiVersion: str
    target: str
    endTime: str

class ResetAdminPasswordRequest(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Trust(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "DELETING",
        "CONNECTED",
        "DISCONNECTED",
    ]
    trustDirection: typing_extensions.Literal[
        "TRUST_DIRECTION_UNSPECIFIED", "INBOUND", "OUTBOUND", "BIDIRECTIONAL"
    ]
    lastTrustHeartbeatTime: str
    targetDnsIpAddresses: typing.List[str]
    targetDomainName: str
    stateDescription: str
    trustHandshakeSecret: str
    selectiveAuthentication: bool
    trustType: typing_extensions.Literal["TRUST_TYPE_UNSPECIFIED", "FOREST", "EXTERNAL"]
    createTime: str
    updateTime: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    reason: str
    eligible: bool

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    location: str
    title: str

class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    nextPageToken: str
    domains: typing.List[Domain]

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int

class OperationMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    statusDetail: str
    cancelRequested: bool
    verb: str
    createTime: str
    apiVersion: str
    target: str

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    tier: str

class Domain(typing_extensions.TypedDict, total=False):
    statusMessage: str
    authorizedNetworks: typing.List[str]
    name: str
    labels: typing.Dict[str, typing.Any]
    createTime: str
    reservedIpRange: str
    admin: str
    locations: typing.List[str]
    trusts: typing.List[Trust]
    fqdn: str
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
    updateTime: str

class ResetAdminPasswordResponse(typing_extensions.TypedDict, total=False):
    password: str

class GoogleCloudManagedidentitiesV1alpha1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    target: str
    verb: str
    apiVersion: str
    createTime: str
    requestedCancellation: bool
    endTime: str

class ReconfigureTrustRequest(typing_extensions.TypedDict, total=False):
    targetDnsIpAddresses: typing.List[str]
    targetDomainName: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    metadata: typing.Dict[str, typing.Any]
    error: Status

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    canReschedule: bool
    rolloutManagementPolicy: str
    endTime: str
    startTime: str

class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    labels: typing.Dict[str, typing.Any]
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    producerMetadata: typing.Dict[str, typing.Any]
    name: str
    maintenanceSchedules: typing.Dict[str, typing.Any]
    maintenancePolicyNames: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    updateTime: str
    consumerDefinedName: str
    slmInstanceTemplate: str
    softwareVersions: typing.Dict[str, typing.Any]
    createTime: str
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    tenantProjectId: str

class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceUrl: str
    resourceType: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    condition: Expr

class GoogleCloudManagedidentitiesV1beta1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    verb: str
    createTime: str
    endTime: str
    target: str
    apiVersion: str
    requestedCancellation: bool

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
