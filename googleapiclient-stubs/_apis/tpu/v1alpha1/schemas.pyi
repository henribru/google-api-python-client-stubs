import typing

import typing_extensions

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class StopNodeRequest(typing_extensions.TypedDict, total=False): ...

class Symptom(typing_extensions.TypedDict, total=False):
    symptomType: typing_extensions.Literal[
        "SYMPTOM_TYPE_UNSPECIFIED",
        "LOW_MEMORY",
        "OUT_OF_MEMORY",
        "EXECUTE_TIMED_OUT",
        "MESH_BUILD_FAIL",
        "HBM_OUT_OF_MEMORY",
    ]
    details: str
    workerId: str
    createTime: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class ListNodesResponse(typing_extensions.TypedDict, total=False):
    nodes: typing.List[Node]
    unreachable: typing.List[str]
    nextPageToken: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class AcceleratorType(typing_extensions.TypedDict, total=False):
    type: str
    name: str

class TensorFlowVersion(typing_extensions.TypedDict, total=False):
    version: str
    name: str

class StartNodeRequest(typing_extensions.TypedDict, total=False): ...

class ReimageNodeRequest(typing_extensions.TypedDict, total=False):
    tensorflowVersion: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    target: str
    verb: str
    endTime: str
    apiVersion: str
    cancelRequested: bool
    createTime: str
    statusDetail: str

class ListAcceleratorTypesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    acceleratorTypes: typing.List[AcceleratorType]
    nextPageToken: str

class Location(typing_extensions.TypedDict, total=False):
    name: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    displayName: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Node(typing_extensions.TypedDict, total=False):
    description: str
    ipAddress: str
    name: str
    cidrBlock: str
    acceleratorType: str
    serviceAccount: str
    healthDescription: str
    tensorflowVersion: str
    network: str
    symptoms: typing.List[Symptom]
    useServiceNetworking: bool
    port: str
    schedulingConfig: SchedulingConfig
    networkEndpoints: typing.List[NetworkEndpoint]
    createTime: str
    labels: typing.Dict[str, typing.Any]
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
    health: typing_extensions.Literal[
        "HEALTH_UNSPECIFIED",
        "HEALTHY",
        "DEPRECATED_UNHEALTHY",
        "TIMEOUT",
        "UNHEALTHY_TENSORFLOW",
        "UNHEALTHY_MAINTENANCE",
    ]

class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    ipAddress: str
    port: int

class ListTensorFlowVersionsResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    tensorflowVersions: typing.List[TensorFlowVersion]
    nextPageToken: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    name: str
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    done: bool

class SchedulingConfig(typing_extensions.TypedDict, total=False):
    preemptible: bool
    reserved: bool
