import typing

_list = list

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing.TypedDict, total=False):
    createTime: str
    description: str
    endpointForwardingRule: str
    endpointIp: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]
    threatExceptions: _list[str]
    trafficLogs: bool
    updateTime: str

@typing.type_check_only
class ListEndpointsResponse(typing.TypedDict, total=False):
    endpoints: _list[Endpoint]
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
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
