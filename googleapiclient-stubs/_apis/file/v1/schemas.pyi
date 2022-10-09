import typing

import typing_extensions

_list = list

@typing.type_check_only
class Backup(typing_extensions.TypedDict, total=False):
    capacityGb: str
    createTime: str
    description: str
    downloadBytes: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzs: bool
    sourceFileShare: str
    sourceInstance: str
    sourceInstanceTier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
        "ENTERPRISE",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "FINALIZING", "READY", "DELETING"
    ]
    storageBytes: str

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
class FileShareConfig(typing_extensions.TypedDict, total=False):
    capacityGb: str
    name: str
    nfsExportOptions: _list[NfsExportOptions]
    sourceBackup: str

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
    createTime: str
    description: str
    etag: str
    fileShares: _list[FileShareConfig]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    name: str
    networks: _list[NetworkConfig]
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "REPAIRING",
        "DELETING",
        "ERROR",
        "RESTORING",
        "SUSPENDED",
    ]
    statusMessage: str
    suspensionReasons: _list[str]
    tier: typing_extensions.Literal[
        "TIER_UNSPECIFIED",
        "STANDARD",
        "PREMIUM",
        "BASIC_HDD",
        "BASIC_SSD",
        "HIGH_SCALE_SSD",
        "ENTERPRISE",
    ]

@typing.type_check_only
class ListBackupsResponse(typing_extensions.TypedDict, total=False):
    backups: _list[Backup]
    nextPageToken: str
    unreachable: _list[str]

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
class ListSnapshotsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    snapshots: _list[Snapshot]

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
class NetworkConfig(typing_extensions.TypedDict, total=False):
    connectMode: typing_extensions.Literal[
        "CONNECT_MODE_UNSPECIFIED", "DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"
    ]
    ipAddresses: _list[str]
    modes: _list[str]
    network: str
    reservedIpRange: str

@typing.type_check_only
class NfsExportOptions(typing_extensions.TypedDict, total=False):
    accessMode: typing_extensions.Literal[
        "ACCESS_MODE_UNSPECIFIED", "READ_ONLY", "READ_WRITE"
    ]
    anonGid: str
    anonUid: str
    ipRanges: _list[str]
    squashMode: typing_extensions.Literal[
        "SQUASH_MODE_UNSPECIFIED", "NO_ROOT_SQUASH", "ROOT_SQUASH"
    ]

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
class RestoreInstanceRequest(typing_extensions.TypedDict, total=False):
    fileShare: str
    sourceBackup: str

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
class Snapshot(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    filesystemUsedBytes: str
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING"
    ]

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
class UpdatePolicy(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "UPDATE_CHANNEL_UNSPECIFIED", "EARLIER", "LATER", "WEEK1", "WEEK2", "WEEK5"
    ]
    denyMaintenancePeriods: _list[DenyMaintenancePeriod]
    window: MaintenanceWindow

@typing.type_check_only
class WeeklyCycle(typing_extensions.TypedDict, total=False):
    schedule: _list[Schedule]
