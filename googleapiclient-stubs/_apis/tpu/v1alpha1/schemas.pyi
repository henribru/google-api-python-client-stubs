import typing

_list = list

@typing.type_check_only
class AcceleratorType(typing.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

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
class ListTensorFlowVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tensorflowVersions: _list[TensorFlowVersion]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class NetworkEndpoint(typing.TypedDict, total=False):
    ipAddress: str
    port: int

@typing.type_check_only
class Node(typing.TypedDict, total=False):
    acceleratorType: str
    apiVersion: typing.Literal[
        "API_VERSION_UNSPECIFIED", "V1_ALPHA1", "V1", "V2_ALPHA1"
    ]
    cidrBlock: str
    createTime: str
    description: str
    health: typing.Literal[
        "HEALTH_UNSPECIFIED",
        "HEALTHY",
        "DEPRECATED_UNHEALTHY",
        "TIMEOUT",
        "UNHEALTHY_TENSORFLOW",
        "UNHEALTHY_MAINTENANCE",
    ]
    healthDescription: str
    ipAddress: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    networkEndpoints: _list[NetworkEndpoint]
    port: str
    schedulingConfig: SchedulingConfig
    serviceAccount: str
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
    tensorflowVersion: str
    useServiceNetworking: bool

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
class ReimageNodeRequest(typing.TypedDict, total=False):
    tensorflowVersion: str

@typing.type_check_only
class SchedulingConfig(typing.TypedDict, total=False):
    preemptible: bool
    reserved: bool

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
class TensorFlowVersion(typing.TypedDict, total=False):
    name: str
    version: str
