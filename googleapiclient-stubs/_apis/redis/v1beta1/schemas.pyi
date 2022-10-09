import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportInstanceRequest(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig

@typing.type_check_only
class FailoverInstanceRequest(typing_extensions.TypedDict, total=False):
    dataProtectionMode: typing_extensions.Literal[
        "DATA_PROTECTION_MODE_UNSPECIFIED", "LIMITED_DATA_LOSS", "FORCE_DATA_LOSS"
    ]

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudRedisV1beta1LocationMetadata(typing_extensions.TypedDict, total=False):
    availableZones: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudRedisV1beta1ZoneMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportInstanceRequest(typing_extensions.TypedDict, total=False):
    inputConfig: InputConfig

@typing.type_check_only
class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    alternativeLocationId: str
    authEnabled: bool
    authorizedNetwork: str
    availableMaintenanceVersions: _list[str]
    connectMode: typing_extensions.Literal[
        "CONNECT_MODE_UNSPECIFIED", "DIRECT_PEERING", "PRIVATE_SERVICE_ACCESS"
    ]
    createTime: str
    currentLocationId: str
    customerManagedKey: str
    displayName: str
    host: str
    labels: dict[str, typing.Any]
    locationId: str
    maintenancePolicy: MaintenancePolicy
    maintenanceSchedule: MaintenanceSchedule
    maintenanceVersion: str
    memorySizeGb: int
    name: str
    nodes: _list[NodeInfo]
    persistenceConfig: PersistenceConfig
    persistenceIamIdentity: str
    port: int
    readEndpoint: str
    readEndpointPort: int
    readReplicasMode: typing_extensions.Literal[
        "READ_REPLICAS_MODE_UNSPECIFIED",
        "READ_REPLICAS_DISABLED",
        "READ_REPLICAS_ENABLED",
    ]
    redisConfigs: dict[str, typing.Any]
    redisVersion: str
    replicaCount: int
    reservedIpRange: str
    secondaryIpRange: str
    serverCaCerts: _list[TlsCertificate]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "UPDATING",
        "DELETING",
        "REPAIRING",
        "MAINTENANCE",
        "IMPORTING",
        "FAILING_OVER",
    ]
    statusMessage: str
    suspensionReasons: _list[str]
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "BASIC", "STANDARD_HA"]
    transitEncryptionMode: typing_extensions.Literal[
        "TRANSIT_ENCRYPTION_MODE_UNSPECIFIED", "SERVER_AUTHENTICATION", "DISABLED"
    ]

@typing.type_check_only
class InstanceAuthString(typing_extensions.TypedDict, total=False):
    authString: str

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
class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    updateTime: str
    weeklyMaintenanceWindow: _list[WeeklyMaintenanceWindow]

@typing.type_check_only
class MaintenanceSchedule(typing_extensions.TypedDict, total=False):
    canReschedule: bool
    endTime: str
    scheduleDeadlineTime: str
    startTime: str

@typing.type_check_only
class NodeInfo(typing_extensions.TypedDict, total=False):
    id: str
    zone: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class PersistenceConfig(typing_extensions.TypedDict, total=False):
    persistenceMode: typing_extensions.Literal[
        "PERSISTENCE_MODE_UNSPECIFIED", "DISABLED", "RDB"
    ]
    rdbNextSnapshotTime: str
    rdbSnapshotPeriod: typing_extensions.Literal[
        "SNAPSHOT_PERIOD_UNSPECIFIED",
        "ONE_HOUR",
        "SIX_HOURS",
        "TWELVE_HOURS",
        "TWENTY_FOUR_HOURS",
    ]
    rdbSnapshotStartTime: str

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
class TlsCertificate(typing_extensions.TypedDict, total=False):
    cert: str
    createTime: str
    expireTime: str
    serialNumber: str
    sha1Fingerprint: str

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False):
    redisVersion: str

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
