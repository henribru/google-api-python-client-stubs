import typing

import typing_extensions

_list = list

@typing.type_check_only
class AttachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING"
    ]
    statusMessage: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "ON_DEMAND", "SCHEDULED", "SCHEMA_EXTENSION"
    ]
    updateTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Certificate(dict[str, typing.Any]): ...

@typing.type_check_only
class DailyCycle(typing_extensions.TypedDict, total=False):
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DenyMaintenancePeriod(typing_extensions.TypedDict, total=False):
    endDate: Date
    startDate: Date
    time: TimeOfDay

@typing.type_check_only
class DetachTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class Domain(typing_extensions.TypedDict, total=False):
    auditLogsEnabled: bool
    authorizedNetworks: _list[str]
    createTime: str
    fqdn: str
    labels: dict[str, typing.Any]
    locations: _list[str]
    managedIdentitiesAdminName: str
    name: str
    reservedIpRange: str
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
    statusMessage: str
    trusts: _list[Trust]
    updateTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendSchemaRequest(typing_extensions.TypedDict, total=False):
    description: str
    fileContents: str
    gcsPath: str

@typing.type_check_only
class GoogleCloudManagedidentitiesV1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudManagedidentitiesV1alpha1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudManagedidentitiesV1beta1OpMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing_extensions.TypedDict, total=False
):
    consumerDefinedName: str
    createTime: str
    instanceType: str
    labels: dict[str, typing.Any]
    maintenancePolicyNames: dict[str, typing.Any]
    maintenanceSchedules: dict[str, typing.Any]
    maintenanceSettings: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    name: str
    notificationParameters: dict[str, typing.Any]
    producerMetadata: dict[str, typing.Any]
    provisionedResources: _list[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    slmInstanceTemplate: str
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    softwareVersions: dict[str, typing.Any]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "REPAIRING",
        "DELETING",
        "ERROR",
    ]
    tenantProjectId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule(
    typing_extensions.TypedDict, total=False
):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing_extensions.TypedDict, total=False
):
    exclude: bool
    isRollback: bool
    maintenancePolicies: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing_extensions.TypedDict, total=False
):
    location: str
    nodeId: str
    perSliEligibility: GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibility

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameter(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibility(
    typing_extensions.TypedDict, total=False
):
    eligibilities: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing_extensions.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing_extensions.TypedDict, total=False
):
    eligible: bool
    reason: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing_extensions.TypedDict, total=False
):
    nodes: _list[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    perSliEligibility: GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibility
    tier: str

@typing.type_check_only
class LDAPSSettings(typing_extensions.TypedDict, total=False):
    certificate: Certificate
    certificatePassword: str
    certificatePfx: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UPDATING", "ACTIVE", "FAILED"
    ]
    updateTime: str

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[Domain]
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
class ListPeeringsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    peerings: _list[Peering]
    unreachable: _list[str]

@typing.type_check_only
class ListSQLIntegrationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sqlIntegrations: _list[SQLIntegration]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "READY", "DELETING"]
    updatePolicy: UpdatePolicy
    updateTime: str

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

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
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Peering(typing_extensions.TypedDict, total=False):
    authorizedNetwork: str
    createTime: str
    domainResource: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CONNECTED", "DISCONNECTED", "DELETING"
    ]
    statusMessage: str
    updateTime: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ReconfigureTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class ResetAdminPasswordRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResetAdminPasswordResponse(typing_extensions.TypedDict, total=False):
    password: str

@typing.type_check_only
class RestoreDomainRequest(typing_extensions.TypedDict, total=False):
    backupId: str

@typing.type_check_only
class SQLIntegration(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    sqlInstance: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "DELETING", "READY"
    ]
    updateTime: str

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    day: typing_extensions.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Trust(typing_extensions.TypedDict, total=False):
    createTime: str
    lastKnownTrustConnectedHeartbeatTime: str
    selectiveAuthentication: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "DELETING",
        "CONNECTED",
        "DISCONNECTED",
    ]
    stateDescription: str
    targetDnsIpAddresses: _list[str]
    targetDomainName: str
    trustDirection: typing_extensions.Literal[
        "TRUST_DIRECTION_UNSPECIFIED", "INBOUND", "OUTBOUND", "BIDIRECTIONAL"
    ]
    trustHandshakeSecret: str
    trustType: typing_extensions.Literal["TRUST_TYPE_UNSPECIFIED", "FOREST", "EXTERNAL"]
    updateTime: str

@typing.type_check_only
class UpdatePolicy(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class ValidateTrustRequest(typing_extensions.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class WeeklyCycle(typing_extensions.TypedDict, total=False):
    schedule: _list[Schedule]
