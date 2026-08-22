import typing

_list = list

@typing.type_check_only
class AttachTrustRequest(typing.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class Backup(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING"
    ]
    statusMessage: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "ON_DEMAND", "SCHEDULED", "SCHEMA_EXTENSION"
    ]
    updateTime: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Certificate(typing.TypedDict, total=False):
    expireTime: str
    issuingCertificate: Certificate
    subject: str
    subjectAlternativeName: _list[str]
    thumbprint: str

@typing.type_check_only
class CheckMigrationPermissionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckMigrationPermissionResponse(typing.TypedDict, total=False):
    onpremDomains: _list[OnPremDomainSIDDetails]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "DISABLED", "ENABLED", "NEEDS_MAINTENANCE"
    ]

@typing.type_check_only
class DailyCycle(typing.TypedDict, total=False):
    duration: str
    startTime: TimeOfDay

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DenyMaintenancePeriod(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date
    time: TimeOfDay

@typing.type_check_only
class DetachTrustRequest(typing.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class DisableMigrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Domain(typing.TypedDict, total=False):
    admin: str
    auditLogsEnabled: bool
    authorizedNetworks: _list[str]
    createTime: str
    fqdn: str
    labels: dict[str, typing.Any]
    locations: _list[str]
    name: str
    reservedIpRange: str
    state: typing.Literal[
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
    trusts: _list[Trust]
    updateTime: str

@typing.type_check_only
class DomainJoinMachineRequest(typing.TypedDict, total=False):
    force: bool
    ouName: str
    vmIdToken: str

@typing.type_check_only
class DomainJoinMachineResponse(typing.TypedDict, total=False):
    domainJoinBlob: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableMigrationRequest(typing.TypedDict, total=False):
    enableDuration: str
    migratingDomains: _list[OnPremDomainDetails]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtendSchemaRequest(typing.TypedDict, total=False):
    description: str
    fileContents: str
    gcsPath: str

@typing.type_check_only
class GoogleCloudManagedidentitiesV1OpMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudManagedidentitiesV1alpha1OpMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudManagedidentitiesV1beta1OpMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1Instance(
    typing.TypedDict, total=False
):
    consumerDefinedName: str
    consumerProjectNumber: str
    createTime: str
    instanceType: str
    labels: dict[str, typing.Any]
    maintenancePolicyNames: dict[str, typing.Any]
    maintenanceSchedules: dict[str, typing.Any]
    maintenanceSettings: (
        GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings
    )
    name: str
    notificationParameters: dict[str, typing.Any]
    producerMetadata: dict[str, typing.Any]
    provisionedResources: _list[
        GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource
    ]
    slmInstanceTemplate: str
    sloMetadata: GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata
    softwareVersions: dict[str, typing.Any]
    state: typing.Literal[
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
    typing.TypedDict, total=False
):
    canReschedule: bool
    endTime: str
    rolloutManagementPolicy: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings(
    typing.TypedDict, total=False
):
    exclude: bool
    isRollback: bool
    maintenancePolicies: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata(
    typing.TypedDict, total=False
):
    location: str
    nodeId: str
    perSliEligibility: (
        GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibility
    )

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameter(
    typing.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibility(
    typing.TypedDict, total=False
):
    eligibilities: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource(
    typing.TypedDict, total=False
):
    resourceType: str
    resourceUrl: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloEligibility(
    typing.TypedDict, total=False
):
    eligible: bool
    reason: str

@typing.type_check_only
class GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata(
    typing.TypedDict, total=False
):
    nodes: _list[GoogleCloudSaasacceleratorManagementProvidersV1NodeSloMetadata]
    perSliEligibility: (
        GoogleCloudSaasacceleratorManagementProvidersV1PerSliSloEligibility
    )
    tier: str

@typing.type_check_only
class LDAPSSettings(typing.TypedDict, total=False):
    certificate: Certificate
    certificatePassword: str
    certificatePfx: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "UPDATING", "ACTIVE", "FAILED"]
    updateTime: str

@typing.type_check_only
class ListBackupsResponse(typing.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDomainsResponse(typing.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str
    unreachable: _list[str]

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
class ListPeeringsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    peerings: _list[Peering]
    unreachable: _list[str]

@typing.type_check_only
class ListSqlIntegrationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sqlIntegrations: _list[SqlIntegration]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MaintenancePolicy(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "READY", "DELETING"]
    updatePolicy: UpdatePolicy
    updateTime: str

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

@typing.type_check_only
class OnPremDomainDetails(typing.TypedDict, total=False):
    disableSidFiltering: bool
    domainName: str

@typing.type_check_only
class OnPremDomainSIDDetails(typing.TypedDict, total=False):
    name: str
    sidFilteringState: typing.Literal[
        "SID_FILTERING_STATE_UNSPECIFIED", "ENABLED", "DISABLED"
    ]

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
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Peering(typing.TypedDict, total=False):
    authorizedNetwork: str
    createTime: str
    domainResource: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CONNECTED", "DISCONNECTED", "DELETING"
    ]
    statusMessage: str
    updateTime: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ReconfigureTrustRequest(typing.TypedDict, total=False):
    targetDnsIpAddresses: _list[str]
    targetDomainName: str

@typing.type_check_only
class ResetAdminPasswordRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResetAdminPasswordResponse(typing.TypedDict, total=False):
    password: str

@typing.type_check_only
class RestoreDomainRequest(typing.TypedDict, total=False):
    backupId: str

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    day: typing.Literal[
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
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class SqlIntegration(typing.TypedDict, total=False):
    createTime: str
    name: str
    sqlInstance: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "DELETING", "READY"]
    updateTime: str

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
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class Trust(typing.TypedDict, total=False):
    createTime: str
    lastTrustHeartbeatTime: str
    selectiveAuthentication: bool
    state: typing.Literal[
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
    trustDirection: typing.Literal[
        "TRUST_DIRECTION_UNSPECIFIED", "INBOUND", "OUTBOUND", "BIDIRECTIONAL"
    ]
    trustHandshakeSecret: str
    trustType: typing.Literal["TRUST_TYPE_UNSPECIFIED", "FOREST", "EXTERNAL"]
    updateTime: str

@typing.type_check_only
class UpdatePolicy(typing.TypedDict, total=False):
    channel: typing.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class ValidateTrustRequest(typing.TypedDict, total=False):
    trust: Trust

@typing.type_check_only
class WeeklyCycle(typing.TypedDict, total=False):
    schedule: _list[Schedule]
