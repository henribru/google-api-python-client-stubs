import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcceleratorConfig(typing_extensions.TypedDict, total=False):
    topology: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "V2", "V3", "V4", "V5LITE_POD", "V5P", "V6E"
    ]

@typing.type_check_only
class AcceleratorType(typing_extensions.TypedDict, total=False):
    acceleratorConfigs: _list[AcceleratorConfig]
    name: str
    type: str

@typing.type_check_only
class AcceptedData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AccessConfig(typing_extensions.TypedDict, total=False):
    externalIp: str

@typing.type_check_only
class ActiveData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AttachedDisk(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["DISK_MODE_UNSPECIFIED", "READ_WRITE", "READ_ONLY"]
    sourceDisk: str

@typing.type_check_only
class BestEffort(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BootDiskConfig(typing_extensions.TypedDict, total=False):
    customerEncryptionKey: CustomerEncryptionKey
    enableConfidentialCompute: bool

@typing.type_check_only
class CreatingData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CustomerEncryptionKey(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class DeletingData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FailedData(typing_extensions.TypedDict, total=False):
    error: Status

@typing.type_check_only
class GenerateServiceIdentityRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GenerateServiceIdentityResponse(typing_extensions.TypedDict, total=False):
    identity: ServiceIdentity

@typing.type_check_only
class GetGuestAttributesRequest(typing_extensions.TypedDict, total=False):
    queryPath: str
    workerIds: _list[str]

@typing.type_check_only
class GetGuestAttributesResponse(typing_extensions.TypedDict, total=False):
    guestAttributes: _list[GuestAttributes]

@typing.type_check_only
class Guaranteed(typing_extensions.TypedDict, total=False):
    minDuration: str
    reserved: bool

@typing.type_check_only
class GuestAttributes(typing_extensions.TypedDict, total=False):
    queryPath: str
    queryValue: GuestAttributesValue

@typing.type_check_only
class GuestAttributesEntry(typing_extensions.TypedDict, total=False):
    key: str
    namespace: str
    value: str

@typing.type_check_only
class GuestAttributesValue(typing_extensions.TypedDict, total=False):
    items: _list[GuestAttributesEntry]

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ListAcceleratorTypesResponse(typing_extensions.TypedDict, total=False):
    acceleratorTypes: _list[AcceleratorType]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNodesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodes: _list[Node]
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListQueuedResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    queuedResources: _list[QueuedResource]
    unreachable: _list[str]

@typing.type_check_only
class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class ListRuntimeVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    runtimeVersions: _list[RuntimeVersion]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MultiNodeParams(typing_extensions.TypedDict, total=False):
    nodeCount: int
    nodeIdPrefix: str
    workloadType: typing_extensions.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "THROUGHPUT_OPTIMIZED", "AVAILABILITY_OPTIMIZED"
    ]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    canIpForward: bool
    enableExternalIps: bool
    network: str
    queueCount: int
    subnetwork: str

@typing.type_check_only
class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    accessConfig: AccessConfig
    ipAddress: str
    port: int

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    acceleratorConfig: AcceleratorConfig
    acceleratorType: str
    apiVersion: typing_extensions.Literal[
        "API_VERSION_UNSPECIFIED", "V1_ALPHA1", "V1", "V2_ALPHA1"
    ]
    autocheckpointEnabled: bool
    bootDiskConfig: BootDiskConfig
    cidrBlock: str
    createTime: str
    dataDisks: _list[AttachedDisk]
    description: str
    health: typing_extensions.Literal[
        "HEALTH_UNSPECIFIED",
        "HEALTHY",
        "TIMEOUT",
        "UNHEALTHY_TENSORFLOW",
        "UNHEALTHY_MAINTENANCE",
    ]
    healthDescription: str
    id: str
    labels: dict[str, typing.Any]
    metadata: dict[str, typing.Any]
    multisliceNode: bool
    name: str
    networkConfig: NetworkConfig
    networkConfigs: _list[NetworkConfig]
    networkEndpoints: _list[NetworkEndpoint]
    queuedResource: str
    runtimeVersion: str
    schedulingConfig: SchedulingConfig
    serviceAccount: ServiceAccount
    shieldedInstanceConfig: ShieldedInstanceConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "READY",
        "RESTARTING",
        "REIMAGING",
        "DELETING",
        "REPAIRING",
        "STOPPED",
        "STOPPING",
        "STARTING",
        "PREEMPTED",
        "TERMINATED",
        "HIDING",
        "HIDDEN",
        "UNHIDING",
        "UNKNOWN",
    ]
    symptoms: _list[Symptom]
    tags: _list[str]
    upcomingMaintenance: UpcomingMaintenance

@typing.type_check_only
class NodeSpec(typing_extensions.TypedDict, total=False):
    multiNodeParams: MultiNodeParams
    node: Node
    nodeId: str
    parent: str

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
class PerformMaintenanceQueuedResourceRequest(typing_extensions.TypedDict, total=False):
    nodeNames: _list[str]

@typing.type_check_only
class PerformMaintenanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ProvisioningData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class QueuedResource(typing_extensions.TypedDict, total=False):
    bestEffort: BestEffort
    createTime: str
    guaranteed: Guaranteed
    name: str
    queueingPolicy: QueueingPolicy
    reservationName: str
    spot: Spot
    state: QueuedResourceState
    tpu: Tpu

@typing.type_check_only
class QueuedResourceState(typing_extensions.TypedDict, total=False):
    acceptedData: AcceptedData
    activeData: ActiveData
    creatingData: CreatingData
    deletingData: DeletingData
    failedData: FailedData
    provisioningData: ProvisioningData
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACCEPTED",
        "PROVISIONING",
        "FAILED",
        "DELETING",
        "ACTIVE",
        "SUSPENDING",
        "SUSPENDED",
        "WAITING_FOR_RESOURCES",
    ]
    stateInitiator: typing_extensions.Literal[
        "STATE_INITIATOR_UNSPECIFIED", "USER", "SERVICE"
    ]
    suspendedData: SuspendedData
    suspendingData: SuspendingData

@typing.type_check_only
class QueueingPolicy(typing_extensions.TypedDict, total=False):
    validAfterDuration: str
    validAfterTime: str
    validInterval: Interval
    validUntilDuration: str
    validUntilTime: str

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    name: str
    standard: Standard
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "APPROVED",
        "PROVISIONING",
        "ACTIVE",
        "DEPROVISIONING",
        "EXPIRED",
        "FAILED",
    ]

@typing.type_check_only
class ResetQueuedResourceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RuntimeVersion(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class SchedulingConfig(typing_extensions.TypedDict, total=False):
    preemptible: bool
    reserved: bool
    spot: bool

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str
    scope: _list[str]

@typing.type_check_only
class ServiceIdentity(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class ShieldedInstanceConfig(typing_extensions.TypedDict, total=False):
    enableSecureBoot: bool

@typing.type_check_only
class SimulateMaintenanceEventRequest(typing_extensions.TypedDict, total=False):
    workerIds: _list[str]

@typing.type_check_only
class Spot(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Standard(typing_extensions.TypedDict, total=False):
    capacityUnits: typing_extensions.Literal[
        "CAPACITY_UNITS_UNSPECIFIED", "CORES", "CHIPS"
    ]
    interval: Interval
    resourceType: str
    size: int
    usage: Usage

@typing.type_check_only
class StartNodeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopNodeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SuspendedData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SuspendingData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Symptom(typing_extensions.TypedDict, total=False):
    createTime: str
    details: str
    symptomType: typing_extensions.Literal[
        "SYMPTOM_TYPE_UNSPECIFIED",
        "LOW_MEMORY",
        "OUT_OF_MEMORY",
        "EXECUTE_TIMED_OUT",
        "MESH_BUILD_FAIL",
        "HBM_OUT_OF_MEMORY",
        "PROJECT_ABUSE",
    ]
    workerId: str

@typing.type_check_only
class Tpu(typing_extensions.TypedDict, total=False):
    nodeSpec: _list[NodeSpec]

@typing.type_check_only
class UpcomingMaintenance(typing_extensions.TypedDict, total=False):
    canReschedule: bool
    latestWindowStartTime: str
    maintenanceStatus: typing_extensions.Literal["UNKNOWN", "PENDING", "ONGOING"]
    type: typing_extensions.Literal["UNKNOWN_TYPE", "SCHEDULED", "UNSCHEDULED"]
    windowEndTime: str
    windowStartTime: str

@typing.type_check_only
class Usage(typing_extensions.TypedDict, total=False):
    total: str
