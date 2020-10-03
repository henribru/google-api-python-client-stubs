import typing

import typing_extensions

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: Status
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]

class Symptom(typing_extensions.TypedDict, total=False):
    details: str
    symptomType: typing_extensions.Literal[
        "SYMPTOM_TYPE_UNSPECIFIED",
        "LOW_MEMORY",
        "OUT_OF_MEMORY",
        "EXECUTE_TIMED_OUT",
        "MESH_BUILD_FAIL",
        "HBM_OUT_OF_MEMORY",
    ]
    createTime: str
    workerId: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class SchedulingConfig(typing_extensions.TypedDict, total=False):
    preemptible: bool
    reserved: bool

class StartNodeRequest(typing_extensions.TypedDict, total=False): ...

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    displayName: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]

class ReimageNodeRequest(typing_extensions.TypedDict, total=False):
    tensorflowVersion: str

class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    ipAddress: str
    port: int

class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    endTime: str
    apiVersion: str
    target: str
    verb: str
    statusDetail: str
    cancelRequested: bool

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Empty(typing_extensions.TypedDict, total=False): ...

class TensorFlowVersion(typing_extensions.TypedDict, total=False):
    name: str
    version: str

class Node(typing_extensions.TypedDict, total=False):
    network: str
    schedulingConfig: SchedulingConfig
    useServiceNetworking: bool
    labels: typing.Dict[str, typing.Any]
    acceleratorType: str
    cidrBlock: str
    tensorflowVersion: str
    name: str
    description: str
    health: typing_extensions.Literal[
        "HEALTH_UNSPECIFIED",
        "HEALTHY",
        "DEPRECATED_UNHEALTHY",
        "TIMEOUT",
        "UNHEALTHY_TENSORFLOW",
        "UNHEALTHY_MAINTENANCE",
    ]
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
    ]
    networkEndpoints: typing.List[NetworkEndpoint]
    serviceAccount: str
    port: str
    createTime: str
    ipAddress: str
    symptoms: typing.List[Symptom]
    healthDescription: str

class StopNodeRequest(typing_extensions.TypedDict, total=False): ...

class ListTensorFlowVersionsResponse(typing_extensions.TypedDict, total=False):
    tensorflowVersions: typing.List[TensorFlowVersion]
    unreachable: typing.List[str]
    nextPageToken: str

class AcceleratorType(typing_extensions.TypedDict, total=False):
    name: str
    type: str

class ListAcceleratorTypesResponse(typing_extensions.TypedDict, total=False):
    acceleratorTypes: typing.List[AcceleratorType]
    unreachable: typing.List[str]
    nextPageToken: str

class ListNodesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodes: typing.List[Node]
    unreachable: typing.List[str]
