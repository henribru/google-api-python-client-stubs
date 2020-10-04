import typing

import typing_extensions
@typing.type_check_only
class AcceleratorType(typing_extensions.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListAcceleratorTypesResponse(typing_extensions.TypedDict, total=False):
    acceleratorTypes: typing.List[AcceleratorType]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListNodesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodes: typing.List[Node]
    unreachable: typing.List[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListTensorFlowVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tensorflowVersions: typing.List[TensorFlowVersion]
    unreachable: typing.List[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class NetworkEndpoint(typing_extensions.TypedDict, total=False):
    ipAddress: str
    port: int

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    acceleratorType: str
    cidrBlock: str
    createTime: str
    description: str
    health: typing_extensions.Literal[
        "HEALTH_UNSPECIFIED",
        "HEALTHY",
        "DEPRECATED_UNHEALTHY",
        "TIMEOUT",
        "UNHEALTHY_TENSORFLOW",
        "UNHEALTHY_MAINTENANCE",
    ]
    healthDescription: str
    ipAddress: str
    labels: typing.Dict[str, typing.Any]
    name: str
    network: str
    networkEndpoints: typing.List[NetworkEndpoint]
    port: str
    schedulingConfig: SchedulingConfig
    serviceAccount: str
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
    symptoms: typing.List[Symptom]
    tensorflowVersion: str
    useServiceNetworking: bool

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
class ReimageNodeRequest(typing_extensions.TypedDict, total=False):
    tensorflowVersion: str

@typing.type_check_only
class SchedulingConfig(typing_extensions.TypedDict, total=False):
    preemptible: bool
    reserved: bool

@typing.type_check_only
class StartNodeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopNodeRequest(typing_extensions.TypedDict, total=False): ...

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
    ]
    workerId: str

@typing.type_check_only
class TensorFlowVersion(typing_extensions.TypedDict, total=False):
    name: str
    version: str
