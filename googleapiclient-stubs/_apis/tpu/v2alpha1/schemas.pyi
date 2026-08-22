import typing

_list = list

@typing.type_check_only
class AcceleratorConfig(typing.TypedDict, total=False):
    topology: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "V2", "V3", "V4", "V5LITE_POD", "V5P", "V6E"
    ]

@typing.type_check_only
class AcceleratorType(typing.TypedDict, total=False):
    acceleratorConfigs: _list[AcceleratorConfig]
    name: str
    type: str

@typing.type_check_only
class AcceptedData(typing.TypedDict, total=False): ...

@typing.type_check_only
class AccessConfig(typing.TypedDict, total=False):
    externalIp: str

@typing.type_check_only
class ActiveData(typing.TypedDict, total=False): ...

@typing.type_check_only
class AttachedDisk(typing.TypedDict, total=False):
    mode: typing.Literal["DISK_MODE_UNSPECIFIED", "READ_WRITE", "READ_ONLY"]
    sourceDisk: str
    workerIds: _list[str]

@typing.type_check_only
class BestEffort(typing.TypedDict, total=False): ...

@typing.type_check_only
class BootDiskConfig(typing.TypedDict, total=False):
    customerEncryptionKey: CustomerEncryptionKey
    diskSizeGb: str
    enableConfidentialCompute: bool
    provisionedIops: str
    provisionedThroughput: str
    sourceImage: str
    storagePool: str

@typing.type_check_only
class CreatingData(typing.TypedDict, total=False): ...

@typing.type_check_only
class CustomerEncryptionKey(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class DeletingData(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FailedData(typing.TypedDict, total=False):
    error: Status

@typing.type_check_only
class GenerateServiceIdentityRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenerateServiceIdentityResponse(typing.TypedDict, total=False):
    identity: ServiceIdentity

@typing.type_check_only
class GetGuestAttributesRequest(typing.TypedDict, total=False):
    queryPath: str
    workerIds: _list[str]

@typing.type_check_only
class GetGuestAttributesResponse(typing.TypedDict, total=False):
    guestAttributes: _list[GuestAttributes]

@typing.type_check_only
class GetMaintenanceInfoResponse(typing.TypedDict, total=False):
    nodeUpcomingMaintenances: _list[NodeUpcomingMaintenanceInfo]

@typing.type_check_only
class Guaranteed(typing.TypedDict, total=False):
    minDuration: str
    reserved: bool

@typing.type_check_only
class GuestAttributes(typing.TypedDict, total=False):
    queryPath: str
    queryValue: GuestAttributesValue

@typing.type_check_only
class GuestAttributesEntry(typing.TypedDict, total=False):
    key: str
    namespace: str
    value: str

@typing.type_check_only
class GuestAttributesValue(typing.TypedDict, total=False):
    items: _list[GuestAttributesEntry]

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ListAcceleratorTypesResponse(typing.TypedDict, total=False):
    acceleratorTypes: _list[AcceleratorType]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNodesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nodes: _list[Node]
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListQueuedResourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    queuedResources: _list[QueuedResource]
    unreachable: _list[str]

@typing.type_check_only
class ListReservationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class ListRuntimeVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    runtimeVersions: _list[RuntimeVersion]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MultiNodeParams(typing.TypedDict, total=False):
    nodeCount: int
    nodeIdPrefix: str
    workloadType: typing.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "THROUGHPUT_OPTIMIZED", "AVAILABILITY_OPTIMIZED"
    ]

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    canIpForward: bool
    enableExternalIps: bool
    network: str
    queueCount: int
    subnetwork: str

@typing.type_check_only
class NetworkEndpoint(typing.TypedDict, total=False):
    accessConfig: AccessConfig
    ipAddress: str
    port: int

@typing.type_check_only
class Node(typing.TypedDict, total=False):
    acceleratorConfig: AcceleratorConfig
    acceleratorType: str
    apiVersion: typing.Literal[
        "API_VERSION_UNSPECIFIED", "V1_ALPHA1", "V1", "V2_ALPHA1"
    ]
    autocheckpointEnabled: bool
    bootDiskConfig: BootDiskConfig
    cidrBlock: str
    createTime: str
    dataDisks: _list[AttachedDisk]
    description: str
    health: typing.Literal[
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
    state: typing.Literal[
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
class NodeSpec(typing.TypedDict, total=False):
    multiNodeParams: MultiNodeParams
    node: Node
    nodeId: str
    parent: str

@typing.type_check_only
class NodeUpcomingMaintenanceInfo(typing.TypedDict, total=False):
    nodeName: str
    nodeUid: str
    upcomingMaintenance: UpcomingMaintenance

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
class PerformMaintenanceQueuedResourceRequest(typing.TypedDict, total=False):
    nodeNames: _list[str]

@typing.type_check_only
class PerformMaintenanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ProvisioningData(typing.TypedDict, total=False): ...

@typing.type_check_only
class QueuedResource(typing.TypedDict, total=False):
    bestEffort: BestEffort
    createTime: str
    guaranteed: Guaranteed
    name: str
    provisioningModel: typing.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED",
        "STANDARD",
        "SPOT",
        "RESERVATION_BOUND",
        "FLEX_START",
    ]
    queueingPolicy: QueueingPolicy
    reservationName: str
    runDuration: RunDuration
    spot: Spot
    state: QueuedResourceState
    tpu: Tpu

@typing.type_check_only
class QueuedResourceState(typing.TypedDict, total=False):
    acceptedData: AcceptedData
    activeData: ActiveData
    creatingData: CreatingData
    deletingData: DeletingData
    failedData: FailedData
    provisioningData: ProvisioningData
    state: typing.Literal[
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
    stateInitiator: typing.Literal["STATE_INITIATOR_UNSPECIFIED", "USER", "SERVICE"]
    suspendedData: SuspendedData
    suspendingData: SuspendingData

@typing.type_check_only
class QueueingPolicy(typing.TypedDict, total=False):
    validAfterDuration: str
    validAfterTime: str
    validInterval: Interval
    validUntilDuration: str
    validUntilTime: str

@typing.type_check_only
class Reservation(typing.TypedDict, total=False):
    name: str
    standard: Standard
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "APPROVED",
        "PROVISIONING",
        "ACTIVE",
        "DEPROVISIONING",
        "EXPIRED",
        "FAILED",
    ]

@typing.type_check_only
class ResetQueuedResourceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RunDuration(typing.TypedDict, total=False):
    maxRunDuration: str
    terminationTime: str

@typing.type_check_only
class RuntimeVersion(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class SchedulingConfig(typing.TypedDict, total=False):
    preemptible: bool
    provisioningModel: typing.Literal[
        "PROVISIONING_MODEL_UNSPECIFIED", "STANDARD", "SPOT", "RESERVATION_BOUND"
    ]
    reservationName: str
    reserved: bool
    spot: bool
    terminationTimestamp: str

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str
    scope: _list[str]

@typing.type_check_only
class ServiceIdentity(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class ShieldedInstanceConfig(typing.TypedDict, total=False):
    enableSecureBoot: bool

@typing.type_check_only
class SimulateMaintenanceEventRequest(typing.TypedDict, total=False):
    workerIds: _list[str]

@typing.type_check_only
class Spot(typing.TypedDict, total=False): ...

@typing.type_check_only
class Standard(typing.TypedDict, total=False):
    capacityUnits: typing.Literal["CAPACITY_UNITS_UNSPECIFIED", "CORES", "CHIPS"]
    interval: Interval
    resourceType: str
    size: int
    usage: Usage

@typing.type_check_only
class StartNodeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopNodeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SuspendedData(typing.TypedDict, total=False): ...

@typing.type_check_only
class SuspendingData(typing.TypedDict, total=False): ...

@typing.type_check_only
class Symptom(typing.TypedDict, total=False):
    createTime: str
    details: str
    symptomType: typing.Literal[
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
class Tpu(typing.TypedDict, total=False):
    nodeSpec: _list[NodeSpec]

@typing.type_check_only
class UpcomingMaintenance(typing.TypedDict, total=False):
    canReschedule: bool
    latestWindowStartTime: str
    maintenanceStatus: typing.Literal["UNKNOWN", "PENDING", "ONGOING"]
    type: typing.Literal["UNKNOWN_TYPE", "SCHEDULED", "UNSCHEDULED"]
    windowEndTime: str
    windowStartTime: str

@typing.type_check_only
class Usage(typing.TypedDict, total=False):
    total: str
