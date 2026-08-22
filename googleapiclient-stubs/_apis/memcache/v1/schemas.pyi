import typing

_list = list

@typing.type_check_only
class ApplyParametersRequest(typing.TypedDict, total=False):
    applyAll: bool
    nodeIds: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

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
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GetTagsRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GetTagsResponse(typing.TypedDict, total=False):
    etag: str
    name: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMemcacheV1LocationMetadata(typing.TypedDict, total=False):
    availableZones: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudMemcacheV1MaintenancePolicy(typing.TypedDict, total=False):
    createTime: str
    description: str
    updateTime: str
    weeklyMaintenanceWindow: _list[WeeklyMaintenanceWindow]

@typing.type_check_only
class GoogleCloudMemcacheV1OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudMemcacheV1UpgradeInstanceRequest(typing.TypedDict, total=False):
    memcacheVersion: typing.Literal[
        "MEMCACHE_VERSION_UNSPECIFIED", "MEMCACHE_1_5", "MEMCACHE_1_6_15"
    ]

@typing.type_check_only
class GoogleCloudMemcacheV1ZoneMetadata(typing.TypedDict, total=False): ...

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
class Instance(typing.TypedDict, total=False):
    authorizedNetwork: str
    availableMaintenanceVersions: _list[str]
    createTime: str
    discoveryEndpoint: str
    displayName: str
    effectiveMaintenanceVersion: str
    instanceMessages: _list[InstanceMessage]
    labels: dict[str, typing.Any]
    maintenancePolicy: GoogleCloudMemcacheV1MaintenancePolicy
    maintenanceSchedule: MaintenanceSchedule
    maintenanceVersion: str
    memcacheFullVersion: str
    memcacheNodes: _list[Node]
    memcacheVersion: typing.Literal[
        "MEMCACHE_VERSION_UNSPECIFIED", "MEMCACHE_1_5", "MEMCACHE_1_6_15"
    ]
    name: str
    nodeConfig: NodeConfig
    nodeCount: int
    parameters: MemcacheParameters
    reservedIpRangeId: _list[str]
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "PERFORMING_MAINTENANCE",
        "MEMCACHE_VERSION_UPGRADING",
    ]
    updateTime: str
    zones: _list[str]

@typing.type_check_only
class InstanceMessage(typing.TypedDict, total=False):
    code: typing.Literal["CODE_UNSPECIFIED", "ZONE_DISTRIBUTION_UNBALANCED"]
    message: str

@typing.type_check_only
class ListInstancesResponse(typing.TypedDict, total=False):
    instances: _list[Instance]
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
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    availableZones: dict[str, typing.Any]

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
class MaintenanceSchedule(typing.TypedDict, total=False):
    endTime: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class MaintenanceWindow(typing.TypedDict, total=False):
    dailyCycle: DailyCycle
    weeklyCycle: WeeklyCycle

@typing.type_check_only
class MemcacheParameters(typing.TypedDict, total=False):
    id: str
    params: dict[str, typing.Any]

@typing.type_check_only
class Node(typing.TypedDict, total=False):
    host: str
    memcacheFullVersion: str
    memcacheVersion: typing.Literal[
        "MEMCACHE_VERSION_UNSPECIFIED", "MEMCACHE_1_5", "MEMCACHE_1_6_15"
    ]
    nodeId: str
    parameters: MemcacheParameters
    port: int
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]
    zone: str

@typing.type_check_only
class NodeConfig(typing.TypedDict, total=False):
    cpuCount: int
    memorySizeMb: int

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
class RescheduleMaintenanceRequest(typing.TypedDict, total=False):
    rescheduleType: typing.Literal[
        "RESCHEDULE_TYPE_UNSPECIFIED",
        "IMMEDIATE",
        "NEXT_AVAILABLE_WINDOW",
        "SPECIFIC_TIME",
    ]
    scheduleTime: str

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
class SetTagsRequest(typing.TypedDict, total=False):
    etag: str
    name: str
    requestId: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class SetTagsResponse(typing.TypedDict, total=False):
    etag: str
    name: str
    tags: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class UpdateParametersRequest(typing.TypedDict, total=False):
    parameters: MemcacheParameters
    updateMask: str

@typing.type_check_only
class UpdatePolicy(typing.TypedDict, total=False):
    channel: typing.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class WeeklyCycle(typing.TypedDict, total=False):
    schedule: _list[Schedule]

@typing.type_check_only
class WeeklyMaintenanceWindow(typing.TypedDict, total=False):
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
class ZoneMetadata(typing.TypedDict, total=False): ...
