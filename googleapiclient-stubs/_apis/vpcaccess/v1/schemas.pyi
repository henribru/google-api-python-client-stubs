import typing

_list = list

@typing.type_check_only
class Connector(typing.TypedDict, total=False):
    connectedProjects: _list[str]
    ipCidrRange: str
    machineType: str
    maxInstances: int
    maxThroughput: int
    minInstances: int
    minThroughput: int
    name: str
    network: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "READY", "CREATING", "DELETING", "ERROR", "UPDATING"
    ]
    subnet: Subnet

@typing.type_check_only
class ListConnectorsResponse(typing.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str

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
    createTime: str
    endTime: str
    method: str
    target: str

@typing.type_check_only
class OperationMetadataV1Alpha1(typing.TypedDict, total=False):
    endTime: str
    insertTime: str
    method: str
    target: str

@typing.type_check_only
class OperationMetadataV1Beta1(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    method: str
    target: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subnet(typing.TypedDict, total=False):
    name: str
    projectId: str
