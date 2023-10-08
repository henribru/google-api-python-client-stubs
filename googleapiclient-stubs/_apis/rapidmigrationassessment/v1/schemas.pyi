import typing

import typing_extensions

_list = list

@typing.type_check_only
class Annotation(typing_extensions.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_LEGACY_EXPORT_CONSENT", "TYPE_QWIKLAB"
    ]
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Collector(typing_extensions.TypedDict, total=False):
    bucket: str
    clientVersion: str
    collectionDays: int
    createTime: str
    description: str
    displayName: str
    eulaUri: str
    expectedAssetCount: str
    guestOsScan: GuestOsScan
    labels: dict[str, typing.Any]
    name: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_INITIALIZING",
        "STATE_READY_TO_USE",
        "STATE_REGISTERED",
        "STATE_ACTIVE",
        "STATE_PAUSED",
        "STATE_DELETING",
        "STATE_DECOMMISSIONED",
        "STATE_ERROR",
    ]
    updateTime: str
    vsphereScan: VSphereScan

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GuestOsScan(typing_extensions.TypedDict, total=False):
    coreSource: str

@typing.type_check_only
class ListCollectorsResponse(typing_extensions.TypedDict, total=False):
    collectors: _list[Collector]
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
class PauseCollectorRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class RegisterCollectorRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class ResumeCollectorRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class VSphereScan(typing_extensions.TypedDict, total=False):
    coreSource: str
