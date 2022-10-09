import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApplyParametersRequest(typing_extensions.TypedDict, total=False):
    applyAll: bool
    nodeIds: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

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
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudMemcacheV1LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMemcacheV1MaintenancePolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    updateTime: str
    weeklyMaintenanceWindow: _list[WeeklyMaintenanceWindow]

@typing.type_check_only
class GoogleCloudMemcacheV1OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMemcacheV1ZoneMetadata(typing_extensions.TypedDict, total=False): ...

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
class Instance(typing_extensions.TypedDict, total=False):
    authorizedNetwork: str
    createTime: str
    discoveryEndpoint: str
    displayName: str
    instanceMessages: _list[InstanceMessage]
    labels: dict[str, typing.Any]
    maintenancePolicy: GoogleCloudMemcacheV1MaintenancePolicy
    maintenanceSchedule: MaintenanceSchedule
    memcacheFullVersion: str
    memcacheNodes: _list[Node]
    memcacheVersion: typing_extensions.Literal[
        "MEMCACHE_VERSION_UNSPECIFIED", "MEMCACHE_1_5"
    ]
    name: str
    nodeConfig: NodeConfig
    nodeCount: int
    parameters: MemcacheParameters
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "PERFORMING_MAINTENANCE",
    ]
    updateTime: str
    zones: _list[str]

@typing.type_check_only
class InstanceMessage(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "ZONE_DISTRIBUTION_UNBALANCED"]
    message: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
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
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: dict[str, typing.Any]

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
class MaintenanceSchedule(typing_extensions.TypedDict, total=False):
    endTime: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

@typing.type_check_only
class MemcacheParameters(typing_extensions.TypedDict, total=False):
    id: str
    params: dict[str, typing.Any]

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    host: str
    nodeId: str
    parameters: MemcacheParameters
    port: int
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]
    zone: str

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    cpuCount: int
    memorySizeMb: int

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
class RescheduleMaintenanceRequest(typing_extensions.TypedDict, total=False):
    rescheduleType: typing_extensions.Literal[
        "RESCHEDULE_TYPE_UNSPECIFIED",
        "IMMEDIATE",
        "NEXT_AVAILABLE_WINDOW",
        "SPECIFIC_TIME",
    ]
    scheduleTime: str

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UpdateParametersRequest(typing_extensions.TypedDict, total=False):
    parameters: MemcacheParameters
    updateMask: str

@typing.type_check_only
class UpdatePolicy(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class WeeklyCycle(typing_extensions.TypedDict, total=False):
    schedule: _list[Schedule]

@typing.type_check_only
class WeeklyMaintenanceWindow(typing_extensions.TypedDict, total=False):
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
class ZoneMetadata(typing_extensions.TypedDict, total=False): ...
