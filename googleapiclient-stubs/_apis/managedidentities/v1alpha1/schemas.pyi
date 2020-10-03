import typing

import typing_extensions

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    locationId: str
    name: str
    displayName: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ResetAdminPasswordResponse(typing_extensions.TypedDict, total=False):
    password: str

class AttachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class ResetAdminPasswordRequest(typing_extensions.TypedDict, total=False): ...

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

class ValidateTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class GoogleCloudManagedidentitiesV1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    target: str
    endTime: str
    verb: str
    apiVersion: str
    requestedCancellation: bool
    createTime: str

class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domains: typing.List[Domain]
    unreachable: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    tier: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]
    eligibility: GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility
    nodes: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]

class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    rolloutManagementPolicy: str
    endTime: str
    canReschedule: bool
    startTime: str

class ReconfigureTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class GoogleCloudManagedidentitiesV1beta1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    requestedCancellation: bool
    createTime: str
    verb: str
    endTime: str
    target: str
    apiVersion: str

class GoogleCloudManagedidentitiesV1alpha1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    verb: str
    target: str
    endTime: str
    apiVersion: str
    requestedCancellation: bool

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]
    condition: Expr

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Trust(typing_extensions.TypedDict, total=False):
    targetDnsIpAddresses: typing.List[str]
    trustHandshakeSecret: str
    updateTime: str
    trustType: typing_extensions.Literal["TRUST_TYPE_UNSPECIFIED", "FOREST", "EXTERNAL"]
    targetDomainName: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "DELETING",
        "CONNECTED",
        "DISCONNECTED",
    ]
    selectiveAuthentication: bool
    createTime: str
    lastKnownTrustConnectedHeartbeatTime: str
    trustDirection: typing_extensions.Literal[
        "TRUST_DIRECTION_UNSPECIFIED", "INBOUND", "OUTBOUND", "BIDIRECTIONAL"
    ]
    stateDescription: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    nodeId: str
    location: str
    exclusions: typing.List[GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion]

class GoogleCloudSaasacceleratorManagementProvidersV1SloExclusion(
    typing_extensions.TypedDict, total=False
):
    reason: str
    duration: str
    sliName: str
    startTime: str

class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    eligible: bool
    reason: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class DetachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    name: str
    maintenanceSchedules: typing.Dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    slmInstanceTemplate: str
    labels: typing.Dict[str, typing.Any]
    createTime: str
    tenantProjectId: str
    provisionedResources: typing.List[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    producerMetadata: typing.Dict[str, typing.Any]
    consumerDefinedName: str
    updateTime: str
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    softwareVersions: typing.Dict[str, typing.Any]
    maintenancePolicyNames: typing.Dict[str, typing.Any]

class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class OperationMetadata(typing_extensions.TypedDict, total=False):
    cancelRequested: bool
    target: str
    apiVersion: str
    createTime: str
    endTime: str
    verb: str
    statusDetail: str

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    description: str
    location: str
    expression: str

class Domain(typing_extensions.TypedDict, total=False):
    authorizedNetworks: typing.List[str]
    labels: typing.Dict[str, typing.Any]
    name: str
    statusMessage: str
    createTime: str
    fqdn: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "PERFORMING_MAINTENANCE",
        "DOWN",
    ]
    locations: typing.List[str]
    reservedIpRange: str
    auditLogsEnabled: bool
    updateTime: str
    managedIdentitiesAdminName: str
    trusts: typing.List[Trust]
