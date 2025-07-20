import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    endpointForwardingRule: str
    endpointIp: str
    labels: dict[str, typing.Any]
    name: str
    network: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "INFORMATIONAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]
    threatExceptions: _list[str]
    trafficLogs: bool
    updateTime: str

@typing.type_check_only
class ListEndpointsResponse(typing_extensions.TypedDict, total=False):
    endpoints: _list[Endpoint]
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
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
